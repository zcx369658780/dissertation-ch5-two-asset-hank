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
    OriginPreservingNormalizedMigrationLaborInputs,
    OriginPreservingNormalizedMigrationLaborResult,
    reconstruct_migration_labor,
    reconstruct_origin_preserving_normalized_migration_labor,
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


@dataclass(frozen=True)
class OriginPreservingNormalizedOneTurnResult:
    """Separate successor composition with bilateral normalized labor provenance."""

    province_order: tuple[str, ...]
    household_outputs: PreFrozenHouseholdOutputBatch
    migration: OriginPreservingNormalizedMigrationLaborResult
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
            or self.migration.destination_firm_labor_by_destination.shape != (n,)
            or self.capital.kt_supply.shape != (n,)
            or len(self.fiscal.Govinc) != n
        ):
            raise ValueError("normalized one-turn result components do not share one province axis")
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
        firm_source["Lt_prev"] = float(household.household_lt[index])
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


def run_origin_preserving_normalized_one_turn(
    inputs: OneTurnInputs,
) -> OriginPreservingNormalizedOneTurnResult:
    """Compose one deterministic turn with the separately named normalized labor route.

    This is deliberately not wired into steady-state or annual runtimes.  It
    changes only the migration allocation consumed by the otherwise unchanged
    capital, firm, wage, monetary, and fiscal component functions.
    """

    n = len(inputs.province_order)
    household = inputs.household_outputs
    provinces = inputs.old_provinces

    migration = reconstruct_origin_preserving_normalized_migration_labor(
        OriginPreservingNormalizedMigrationLaborInputs(
            consumption_by_origin=household.ct,
            household_labor_per_capita_by_origin=household.household_lt,
            population_by_origin=[province["N"] for province in provinces],
            old_firm_wage_by_destination=[province["wjt"] for province in provinces],
            tax_by_origin=[province["tau"] for province in provinces],
            phi_destination_origin=inputs.phi_destination_origin,
            migration_wedge_destination_origin=inputs.migration_wedge_destination_origin,
            gamma_c=inputs.params["ga"],
            phi_l=inputs.params["phi_l"],
        )
    )

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
        firm_source["Lt_prev"] = float(household.household_lt[index])
        firms.append(evaluate_firm(
            firm_source,
            float(capital.kt_supply[index]),
            float(migration.destination_firm_labor_by_destination[index]),
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
    return OriginPreservingNormalizedOneTurnResult(
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


def prepare_mainline_household_states(states, fixture):
    """Bind entering payoff to the very S used by this turn's capital quantities.

    S depends only on completed returns/theta/distance, not on current household
    At. Binding-test inputs remain the explicitly frozen initial HA prices.
    """
    from .capital_network import BilateralCapitalNetworkInputs, build_bilateral_capital_network
    p=fixture['parameters']; raw=np.asarray([s['ra0_raw_previous'] for s in states])
    deviation=float(np.std(raw,ddof=0))
    score=np.zeros(len(raw)) if deviation == 0 else (raw-np.mean(raw))/deviation
    network=build_bilateral_capital_network(BilateralCapitalNetworkInputs(
        tuple(fixture['province_order']),np.asarray([s['At'] for s in states]),
        np.asarray([s['N'] for s in states]),np.asarray(fixture['foreign_share_theta']),
        np.asarray(fixture['distance_score_destination_origin']),score,raw,
        p['portfolio_beta_distance'],p['portfolio_beta_return'],
        'LAGGED_COMPLETED_ITERATION_RAW_RETURN__SYNTHETIC_INITIAL_ANCHOR'))
    return tuple(dict(s,rah=float(network.household_portfolio_return_by_origin[i]))
                 for i,s in enumerate(states))


def run_mainline_one_turn(states, batch, fixture):
    """V010 opt-in composition: no legacy capital or C1, immutable entering batch."""
    from .capital_network import BilateralCapitalNetworkInputs, build_bilateral_capital_network
    from .migration_labor import reconstruct_mainline_labor
    from .wage import mainline_phi, mainline_effective_wages
    from .fiscal_diagnostics import mainline_fiscal_accounts
    p = fixture['parameters']; n = len(states)
    if tuple(s['name'] for s in states) != tuple(fixture['province_order']):
        raise ValueError('mainline state axis differs from fixture')
    if not all(batch.converged) or any(not d.get('strict_qualified',False) for d in batch.diagnostics):
        raise ValueError('all household HJB/KFE gates must pass before integration')
    phi = mainline_phi(fixture['pgdp_reference'])
    sigma = np.asarray(fixture['migration_wedge_destination_origin'],dtype=float)
    population = np.array([s['N'] for s in states])
    old_raw = np.array([s['ra0_raw_previous'] for s in states])
    std = float(np.std(old_raw,ddof=0))
    score = np.zeros(n) if std == 0 else (old_raw-np.mean(old_raw))/std
    capital = build_bilateral_capital_network(BilateralCapitalNetworkInputs(
        province_order=tuple(fixture['province_order']), illiquid_assets_per_capita_by_origin=batch.at,
        population_by_origin=population, total_foreign_share_theta_by_origin=np.asarray(fixture['foreign_share_theta']),
        distance_score_destination_origin=np.asarray(fixture['distance_score_destination_origin']),
        lagged_return_score_by_destination=score,portfolio_return_by_destination=old_raw,
        beta_distance=p['portfolio_beta_distance'],beta_return=p['portfolio_beta_return'],
        lagged_return_provenance='LAGGED_COMPLETED_ITERATION_RAW_RETURN__SYNTHETIC_INITIAL_ANCHOR'))
    migration = reconstruct_mainline_labor(consumption=batch.ct,population=population,
        gross_wages=[s['wjt_gross'] for s in states],destination_taxes=[s['tau'] for s in states],
        phi=phi,sigma=sigma,gamma_c=p['gamma_c'],phi_l=p['phi_l'])
    params = {'epsilon':p['epsilon'],'theta':p['theta_rotemberg'],'delta':p['delta_depreciation']}
    firms = []
    for i,state in enumerate(states):
        firm_source = dict(state)
        firm_source['AtTax'] = float(batch.at_tax[i])
        # Keep previous completed firm labor: never replace it by household Lt.
        firms.append(evaluate_firm(firm_source,float(capital.destination_private_productive_capital[i]),
                                  float(migration.lt_supply[i]),params,mainline=True))
    wages = mainline_effective_wages([f.wt0 for f in firms],[s['tau'] for s in states],phi,sigma,
                                    phi_l=p['phi_l'],alphal=p['alphal'])
    monetary = taylor_assignment(istar=p['istar'],rho_pi=p['rho_pi'],
                                 totalpit=fixture['totalpit'],epsilon_pi=fixture['epsilon_pi'])
    fiscal = mainline_fiscal_accounts(states,firms,batch,monetary.rb)
    shares = capital.portfolio_shares_destination_origin
    raw = np.array([f.ra0 for f in firms])
    next_payoff = raw @ shares
    next_states = []
    for i,(state,firm) in enumerate(zip(states,firms)):
        updated = dict(state); updated.update(firm.as_source_dict())
        updated.update(Ct=float(batch.ct[i]),At=float(batch.at[i]),Bt=float(batch.bt[i]),
            AtTax=float(batch.at_tax[i]),Lt_HA=float(batch.household_lt[i]),
            Lt_supply=firm.Lt,Kt_supply=float(capital.destination_private_productive_capital[i]),
            Lt_firm_previous=float(state['Lt_prev']),Lt_firm_current=firm.Lt,
            Lt_prev=firm.Lt,Kt_prev=firm.Kt,Yt_1=float(state['Yt']),
            Zt_1=float(state['Zt']),pit_1=float(state['pit']),wjt_gross=firm.wt0,
            rah=float(next_payoff[i]),w_eff=float(wages[i]),rb=monetary.rb,it=monetary.it,
            ra0_raw_previous=firm.ra0,convergent=True)
        next_states.append(updated)
    return {'states':tuple(next_states),'firms':tuple(firms),'migration':migration,'capital':capital,
            'fiscal':fiscal,'shares':shares,'lagged_score':score,'raw_next_payoff':next_payoff,
            'phi':phi,'update_order':('HA','labor_and_same_S_capital','firm','net_wage','Taylor','fiscal'),
            'GovInv_rule':'SOURCE_BOUNDARY_ADAPTATION_OUTSIDE_SINGLE_TURN__NO_C1'}
