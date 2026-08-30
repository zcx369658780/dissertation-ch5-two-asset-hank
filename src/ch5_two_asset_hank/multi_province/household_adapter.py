"""Static MP1 bridge to the accepted two-asset household oracle.

This module deliberately cannot run the household solver.  It freezes names and
roles at the boundary between ``HANK_mp_1turn.m`` and the accepted standalone
API, leaving execution to a later, separately authorised layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Iterable, Mapping

import numpy as np


NO_LEGACY_R5_RUNTIME_DEPENDENCY = True


@dataclass(frozen=True)
class AcceptedHAPublicAPI:
    solver_symbol: str
    household_inputs_symbol: str
    aggregate_fields: tuple[str, ...]


ACCEPTED_HA_PUBLIC_API = AcceptedHAPublicAPI(
    solver_symbol="exports.matlab_faithful_two_asset_ha.solve_household_steady_state",
    household_inputs_symbol="exports.matlab_faithful_two_asset_ha.HouseholdInputs",
    aggregate_fields=(
        "c_ss",
        "l_ss",
        "a_ss",
        "b_ss",
        "total_assets",
        "density_normalization",
    ),
)

# Source/API crosswalk frozen from HANK_2ASSETS_HJB.m and the accepted export.
# Expressions are intentionally explicit where the two APIs do not use the
# same parameterisation (notably phi = 1 / frisch_l).
MATLAB_TO_ACCEPTED_HA_FIELD_MAP: Mapping[str, str] = MappingProxyType(
    {
        "results.rah": "HouseholdInputs.r_a",
        "results.rb": "HouseholdInputs.r_b",
        "results.tau": "HouseholdInputs.tau",
        "results.w": "HouseholdInputs.wages[0]",
        "composite_zero_migration_wedge": "HouseholdInputs.migration_costs[0]",
        "param.alphal": "HouseholdInputs.labor_weights[0]",
        "results.Tt": "solve_household_steady_state.transfer_income",
        "results.rb_gap": "solve_household_steady_state.borrowing_rate_gap",
        "param.rho": "EconomicParams.rho",
        "param.ga": "EconomicParams.gamma_c",
        "1 / param.frisch_l": "EconomicParams.phi",
        "CHIh.chi0": "EconomicParams.chi_0",
        "CHIh.chi1": "EconomicParams.chi_1",
        "CHIh.a_bar": "EconomicParams.a_bar",
        "grid.la_mat": "MatlabFaithfulHJBGrid.switch_matrix",
        "linspace(grid.amin, grid.amax, grid.J)": "MatlabFaithfulHJBGrid.a",
        "linspace(grid.bmin, grid.bmax, grid.I)": "MatlabFaithfulHJBGrid.b",
        "grid.z": "MatlabFaithfulHJBGrid.z",
        "results.V": "solve_household_steady_state.initial_value",
        "results.l": "solve_household_steady_state.baseline_labor",
        "num": "solve_household_steady_state.numerics",
    }
)

MATLAB_TO_ACCEPTED_HA_OUTPUT_MAP: Mapping[str, str] = MappingProxyType(
    {
        "results.Ct": "HouseholdSteadyStateResult.aggregates.c_ss",
        "results.Lt": "HouseholdSteadyStateResult.aggregates.l_ss",
        "results.At": "HouseholdSteadyStateResult.aggregates.a_ss",
        "results.Bt": "HouseholdSteadyStateResult.aggregates.b_ss",
        "results.AtTax": "post_solve_reconstruction.AtTax_from_density_and_tapered_illiquid_return",
        "results.convergent": "HouseholdSteadyStateResult.hjb.converged",
        "HJB convergence statistic": "HouseholdSteadyStateResult.hjb.convergence_statistic",
    }
)


def _finite_scalar(name: str, value: float) -> float:
    result = float(value)
    if not np.isfinite(result):
        raise ValueError(f"{name} must be finite")
    return result


def _require_public_fields(name: str, value: object, fields: tuple[str, ...]) -> None:
    missing = tuple(field for field in fields if not hasattr(value, field))
    if missing:
        raise ValueError(f"{name} is missing accepted public fields: {missing!r}")


@dataclass(frozen=True)
class MultiProvinceHouseholdInputs:
    """All outer-state values required to describe one accepted HA call.

    ``composite_wage`` is already reduced before the HJB.  The singleton vector
    representation is required only because the accepted Python API generalises
    the labor FOC over labor choices; it does not expose 31 illiquid states.
    Every economic and numerical object is mandatory to prevent implicit
    calibration defaults.
    """

    rah: float
    rb: float
    tau: float
    composite_wage: float
    composite_migration_cost: float
    composite_labor_weight: float
    transfer_income: float
    borrowing_rate_gap: float
    grid: object
    economic_params: object
    initial_value: np.ndarray
    baseline_labor: np.ndarray
    numerics: object

    def __post_init__(self) -> None:
        for name in (
            "rah",
            "rb",
            "tau",
            "composite_wage",
            "composite_migration_cost",
            "composite_labor_weight",
            "transfer_income",
            "borrowing_rate_gap",
        ):
            object.__setattr__(self, name, _finite_scalar(name, getattr(self, name)))
        if self.composite_wage < 0.0:
            raise ValueError("composite_wage must be non-negative")
        if self.composite_labor_weight <= 0.0:
            raise ValueError("composite_labor_weight must be positive")
        if 1.0 - self.tau - self.composite_migration_cost < 0.0:
            raise ValueError("the composite after-tax wage wedge must be non-negative")
        for name in ("grid", "economic_params", "initial_value", "baseline_labor", "numerics"):
            if getattr(self, name) is None:
                raise ValueError(f"{name} is required; MP1 defines no hidden default")
        _require_public_fields("grid", self.grid, ("b", "a", "z", "switch_matrix"))
        _require_public_fields(
            "economic_params",
            self.economic_params,
            ("rho", "gamma_c", "phi", "chi_0", "chi_1", "a_bar", "mu_z", "sigma_z"),
        )
        _require_public_fields(
            "numerics",
            self.numerics,
            ("delta", "convergence_tolerance", "max_iterations", "drift_tolerance"),
        )
        b = np.asarray(getattr(self.grid, "b"), dtype=float)
        a = np.asarray(getattr(self.grid, "a"), dtype=float)
        z = np.asarray(getattr(self.grid, "z"), dtype=float)
        switch = np.asarray(getattr(self.grid, "switch_matrix"), dtype=float)
        if any(
            axis.ndim != 1
            or axis.size < 2
            or not np.isfinite(axis).all()
            or not np.all(np.diff(axis) > 0.0)
            for axis in (b, a, z)
        ):
            raise ValueError(
                "accepted grid axes must be finite, one-dimensional, and strictly increasing"
            )
        if switch.shape != (z.size, z.size) or not np.isfinite(switch).all():
            raise ValueError("accepted grid switch_matrix must have shape (z,z) and be finite")
        initial = np.array(self.initial_value, dtype=float, copy=True)
        labor = np.array(self.baseline_labor, dtype=float, copy=True)
        accepted_shape = (b.size, a.size, z.size)
        if initial.shape != accepted_shape or labor.shape != accepted_shape:
            raise ValueError(
                "initial_value and baseline_labor must match accepted grid shape (b,a,z)"
            )
        if not np.all(np.isfinite(initial)) or not np.all(np.isfinite(labor)):
            raise ValueError("initial_value and baseline_labor must be finite")
        if np.any(labor < 0.0):
            raise ValueError("baseline_labor must be non-negative")
        initial.flags.writeable = False
        labor.flags.writeable = False
        object.__setattr__(self, "initial_value", initial)
        object.__setattr__(self, "baseline_labor", labor)


@dataclass(frozen=True)
class StaticHouseholdCall:
    household_input_kwargs: Mapping[str, float | tuple[float, ...]]
    grid: object
    economic_params: object
    initial_value: np.ndarray
    baseline_labor: np.ndarray
    transfer_income: float
    borrowing_rate_gap: float
    numerics: object
    pre_solve_composite_fields: tuple[str, ...]
    post_solve_reconstruction: tuple[str, ...]
    scientific_solver_called: bool = False


def build_static_household_call(inputs: MultiProvinceHouseholdInputs) -> StaticHouseholdCall:
    """Map source roles to accepted API arguments without invoking any callable."""

    return StaticHouseholdCall(
        household_input_kwargs=MappingProxyType({
            "r_a": inputs.rah,
            "r_b": inputs.rb,
            "tau": inputs.tau,
            "wages": (inputs.composite_wage,),
            "migration_costs": (inputs.composite_migration_cost,),
            "labor_weights": (inputs.composite_labor_weight,),
        }),
        grid=inputs.grid,
        economic_params=inputs.economic_params,
        initial_value=inputs.initial_value,
        baseline_labor=inputs.baseline_labor,
        transfer_income=inputs.transfer_income,
        borrowing_rate_gap=inputs.borrowing_rate_gap,
        numerics=inputs.numerics,
        pre_solve_composite_fields=("w", "rah", "rb", "tau", "Tt", "rb_gap"),
        post_solve_reconstruction=(
            "AtTax_from_density_and_tapered_illiquid_return",
            "Lt_mat_from_Ct_and_destination_firm_wages",
            "Lt_supply_as_destination_row_sum",
        ),
    )


@dataclass(frozen=True)
class FrozenHouseholdOutputs:
    """Outer-loop household outputs; ``Lt`` is not destination firm labor."""

    Ct: float
    Lt: float
    At: float
    Bt: float
    AtTax: float
    converged: bool
    convergence_statistic: float

    def __post_init__(self) -> None:
        values = np.array(
            [self.Ct, self.Lt, self.At, self.Bt, self.AtTax, self.convergence_statistic],
            dtype=float,
        )
        if not np.all(np.isfinite(values)):
            raise ValueError("frozen household outputs must be finite")
        if self.Ct <= 0.0 or self.Lt < 0.0 or self.At < 0.0:
            raise ValueError("frozen household levels violate their source domains")
        if self.convergence_statistic < 0.0 or not isinstance(self.converged, (bool, np.bool_)):
            raise ValueError("household convergence diagnostics are invalid")


def reject_legacy_runtime_references(module_names_or_paths: Iterable[str]) -> None:
    """Fail closed if a proposed active dependency names the superseded R5 runtime."""

    forbidden = ("chapter5_model", "dissertation-ch5-r5-python-model")
    for reference in module_names_or_paths:
        normalized = str(reference).replace("\\", "/").casefold()
        if any(marker in normalized for marker in forbidden):
            raise ValueError(f"legacy R5 runtime dependency is forbidden: {reference}")
