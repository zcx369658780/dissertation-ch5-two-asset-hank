"""Deterministic MATLAB-faithful multi-province one-turn composition.

The input boundary is a complete batch of *already computed* household
outputs.  This module has no solver callback and imports no household, HJB,
KFE, fixed-point, validator, or legacy runtime.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from types import MappingProxyType
from typing import Mapping, Sequence

import numpy as np

from .capital_allocation import (
    CapitalAllocationInputs,
    CapitalAllocationResult,
    allocate_productive_capital,
)
from .firm import FirmResult, evaluate_firm
from .fiscal_diagnostics import FiscalDiagnostics, national_fiscal_diagnostics
from .migration_labor import (
    MigrationLaborInputs,
    MigrationLaborResult,
    reconstruct_migration_labor,
)
from .monetary import MonetaryResult, taylor_assignment
from .wage import composite_household_wages


SOURCE_UPDATE_ORDER: tuple[str, ...] = (
    "pre_frozen_household_outputs",
    "migration_labor",
    "at_only_productive_capital_and_pre_firm_rah",
    "firm",
    "household_composite_wage",
    "taylor_rb",
    "fiscal_diagnostics",
)


def _readonly_vector(name: str, values: object, n: int | None = None) -> np.ndarray:
    array = np.array(values, dtype=float, copy=True)
    if array.ndim != 1 or array.size < 2 or (n is not None and array.shape != (n,)):
        expected = "a vector with at least two provinces" if n is None else f"shape ({n},)"
        raise ValueError(f"{name} must have {expected}")
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must contain only finite values")
    array.flags.writeable = False
    return array


@dataclass(frozen=True)
class PreFrozenHouseholdOutputBatch:
    """Complete simultaneous household outputs supplied before outer updates."""

    ct: np.ndarray
    household_lt: np.ndarray
    at: np.ndarray
    bt: np.ndarray
    at_tax: np.ndarray
    converged: tuple[bool, ...]
    diagnostics: tuple[Mapping[str, object], ...]

    def __post_init__(self) -> None:
        ct = _readonly_vector("household_outputs.ct", self.ct)
        n = ct.size
        vectors = {
            "household_lt": _readonly_vector("household_outputs.household_lt", self.household_lt, n),
            "at": _readonly_vector("household_outputs.at", self.at, n),
            "bt": _readonly_vector("household_outputs.bt", self.bt, n),
            "at_tax": _readonly_vector("household_outputs.at_tax", self.at_tax, n),
        }
        if np.any(ct <= 0.0) or np.any(vectors["household_lt"] < 0.0):
            raise ValueError("household Ct must be positive and household Lt non-negative")
        if np.any(vectors["at"] < 0.0):
            raise ValueError("household At must be non-negative")
        converged = tuple(self.converged)
        diagnostics = tuple(MappingProxyType(dict(item)) for item in self.diagnostics)
        if len(converged) != n or len(diagnostics) != n:
            raise ValueError("household convergence evidence must match the province count")
        if any(not isinstance(value, (bool, np.bool_)) for value in converged):
            raise ValueError("household converged flags must be boolean")
        object.__setattr__(self, "ct", ct)
        for name, value in vectors.items():
            object.__setattr__(self, name, value)
        object.__setattr__(self, "converged", tuple(bool(value) for value in converged))
        object.__setattr__(self, "diagnostics", diagnostics)


@dataclass(frozen=True)
class OneTurnInputs:
    """All old-turn objects and pre-frozen household outputs for one turn."""

    province_order: tuple[str, ...]
    old_provinces: tuple[Mapping[str, float], ...]
    params: Mapping[str, float]
    phi_destination_origin: np.ndarray
    migration_wedge_destination_origin: np.ndarray
    household_outputs: PreFrozenHouseholdOutputBatch

    def __post_init__(self) -> None:
        order = tuple(self.province_order)
        n = self.household_outputs.ct.size
        if len(order) != n or len(set(order)) != n or any(not name for name in order):
            raise ValueError("province_order must contain one unique nonempty label per province")
        if len(self.old_provinces) != n:
            raise ValueError("old_provinces must exactly match province_order")
        provinces = tuple(MappingProxyType(dict(province)) for province in self.old_provinces)
        for index, province in enumerate(provinces):
            if str(province.get("name", "")) != order[index]:
                raise ValueError("old province records must exactly match province_order")
        params = MappingProxyType(dict(self.params))
        phi = np.array(self.phi_destination_origin, dtype=float, copy=True)
        wedges = np.array(self.migration_wedge_destination_origin, dtype=float, copy=True)
        if phi.shape != (n, n) or wedges.shape != (n, n):
            raise ValueError("cross-province matrices must have destination-by-origin shape")
        if not np.all(np.isfinite(phi)) or not np.all(np.isfinite(wedges)):
            raise ValueError("cross-province matrices must contain only finite values")
        phi.flags.writeable = False
        wedges.flags.writeable = False
        object.__setattr__(self, "province_order", order)
        object.__setattr__(self, "old_provinces", provinces)
        object.__setattr__(self, "params", params)
        object.__setattr__(self, "phi_destination_origin", phi)
        object.__setattr__(self, "migration_wedge_destination_origin", wedges)


@dataclass(frozen=True)
class OneTurnResult:
    """Immutable, auditable component result; contains no convergence update."""

    province_order: tuple[str, ...]
    household_outputs: PreFrozenHouseholdOutputBatch
    migration: MigrationLaborResult
    capital: CapitalAllocationResult
    firms: tuple[FirmResult, ...]
    household_composite_wage: tuple[float, ...]
    monetary: MonetaryResult
    fiscal: FiscalDiagnostics
    source_update_order: tuple[str, ...] = SOURCE_UPDATE_ORDER

    def __post_init__(self) -> None:
        n = len(self.province_order)
        if (
            len(self.firms) != n
            or len(self.household_composite_wage) != n
            or self.migration.lt_supply.shape != (n,)
            or self.capital.kt_supply.shape != (n,)
            or len(self.fiscal.Govinc) != n
        ):
            raise ValueError("one-turn result components do not share one province axis")
        if self.source_update_order != SOURCE_UPDATE_ORDER:
            raise ValueError("one-turn source update order is immutable")
        if not all(isfinite(float(value)) for value in self.household_composite_wage):
            raise ValueError("household composite wages must be finite")


def run_source_faithful_one_turn(inputs: OneTurnInputs) -> OneTurnResult:
    """Compose the MP2 arithmetic once, in literal MATLAB source order."""

    n = len(inputs.province_order)
    household = inputs.household_outputs
    provinces = inputs.old_provinces

    migration = reconstruct_migration_labor(MigrationLaborInputs(
        consumption_by_origin=household.ct,
        population_by_origin=[province["N"] for province in provinces],
        old_firm_wage_by_destination=[province["wjt"] for province in provinces],
        tax_by_origin=[province["tau"] for province in provinces],
        phi_destination_origin=inputs.phi_destination_origin,
        migration_wedge_destination_origin=inputs.migration_wedge_destination_origin,
        gamma_c=inputs.params["ga"],
        phi_l=inputs.params["phi_l"],
    ))

    capital = allocate_productive_capital(CapitalAllocationInputs(
        illiquid_assets_at=household.at,
        population=[province["N"] for province in provinces],
        inter_province_ratio=[province["inter_prv_ratio"] for province in provinces],
        old_firm_return_ra=[province["ra"] for province in provinces],
    ))

    firms: list[FirmResult] = []
    for index in range(n):
        firm_source = dict(provinces[index])
        firm_source["AtTax"] = float(household.at_tax[index])
        firms.append(evaluate_firm(
            firm_source,
            float(capital.kt_supply[index]),
            float(migration.lt_supply[index]),
            inputs.params,
        ))

    composite_wage = composite_household_wages(
        provinces,
        [firm.wjt for firm in firms],
        inputs.phi_destination_origin,
        inputs.migration_wedge_destination_origin,
        phi_l=inputs.params["phi_l"],
        alphal=inputs.params["alphal"],
    )
    monetary = taylor_assignment(
        istar=inputs.params["istar"],
        rho_pi=inputs.params["rho_pi"],
        totalpit=inputs.params["totalpit"],
        epsilon_pi=inputs.params["epsilon_pi"],
    )
    fiscal = national_fiscal_diagnostics(
        [firm.Govinc for firm in firms],
        household.bt,
        monetary.rb,
        [province["N"] for province in provinces],
    )
    return OneTurnResult(
        province_order=inputs.province_order,
        household_outputs=household,
        migration=migration,
        capital=capital,
        firms=tuple(firms),
        household_composite_wage=tuple(composite_wage),
        monetary=monetary,
        fiscal=fiscal,
    )


# Descriptive alias for callers that prefer composition terminology.
compose_one_turn = run_source_faithful_one_turn
