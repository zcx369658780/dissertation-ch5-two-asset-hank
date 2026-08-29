"""State-constraint feasibility and diagnostics."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .contracts import EconomicParams, HouseholdInputs
from .economics import adjustment_cost


@dataclass(frozen=True)
class BoundaryCheck:
    feasible: bool
    violation: float
    active_a: bool
    active_b: bool


def check_boundary(
    i_a: int,
    i_b: int,
    n_a: int,
    n_b: int,
    mu_a: float,
    mu_b: float,
    tolerance: float,
) -> BoundaryCheck:
    violations: list[float] = []
    active_a = i_a == 0
    active_b = i_b == 0
    if i_a == 0:
        violations.append(max(0.0, -mu_a))
    if i_b == 0:
        violations.append(max(0.0, -mu_b))
    if i_a == n_a - 1:
        violations.append(max(0.0, mu_a))
    if i_b == n_b - 1:
        violations.append(max(0.0, mu_b))
    violation = max(violations, default=0.0)
    return BoundaryCheck(violation <= tolerance, violation, active_a, active_b)


def drift_matches_direction(drift: float, direction: str, tolerance: float) -> bool:
    if direction == "Z":
        return abs(drift) <= tolerance
    if drift > tolerance:
        return direction == "F"
    if drift < -tolerance:
        return direction == "B"
    return True


def _distance_to_interval(value: float, lower: float, upper: float) -> float:
    if value < lower:
        return lower - value
    if value > upper:
        return value - upper
    return 0.0


def recover_multipliers(
    *, active_a: bool, active_b: bool, consumption: float, transfer: float,
    v_a: float, v_b: float, a: float, params: EconomicParams, zero_tolerance: float,
    active_a_upper: bool = False,
    active_b_upper: bool = False,
) -> tuple[float, float]:
    if active_a and active_a_upper:
        raise ValueError("lower and upper illiquid constraints cannot both be active")
    if active_b and active_b_upper:
        raise ValueError("lower and upper liquid constraints cannot both be active")
    marginal_c = consumption ** (-params.gamma_c)
    if active_b:
        lambda_b = marginal_c - v_b
        shadow_b = v_b + lambda_b
    elif active_b_upper:
        lambda_b = v_b - marginal_c
        shadow_b = v_b - lambda_b
    else:
        lambda_b = 0.0
        shadow_b = v_b
    if not (active_a or active_a_upper):
        return 0.0, lambda_b
    scale = max(a, params.a_bar)
    if transfer > zero_tolerance:
        lambda_a = shadow_b * (1.0 + params.chi_0 + params.chi_1 * transfer / scale) - v_a
    elif transfer < -zero_tolerance:
        lambda_a = shadow_b * (1.0 - params.chi_0 + params.chi_1 * transfer / scale) - v_a
    else:
        lower = shadow_b * (1.0 - params.chi_0) - v_a
        upper = shadow_b * (1.0 + params.chi_0) - v_a
        lambda_a = max(0.0, -upper) if active_a_upper else min(max(0.0, lower), upper)
    if active_a_upper and abs(transfer) > zero_tolerance:
        lambda_a = -lambda_a
    return lambda_a, lambda_b


def kkt_residuals(
    *, active_a: bool, active_b: bool, a: float, b: float, z: float,
    consumption: float, labor: np.ndarray, transfer: float, mu_a: float, mu_b: float,
    v_a: float, v_b: float, inputs: HouseholdInputs, params: EconomicParams,
    zero_tolerance: float,
    active_a_upper: bool = False,
    active_b_upper: bool = False,
) -> tuple[float, float, dict[str, float]]:
    lambda_a, lambda_b = recover_multipliers(
        active_a=active_a, active_b=active_b, consumption=consumption, transfer=transfer,
        v_a=v_a, v_b=v_b, a=a, params=params, zero_tolerance=zero_tolerance,
        active_a_upper=active_a_upper,
        active_b_upper=active_b_upper,
    )
    cost = float(adjustment_cost(transfer, a, params))
    wage_terms = inputs.wages * (1.0 - inputs.tau - inputs.migration_costs) * z
    labor_income = float(np.sum(wage_terms * labor))
    scale_mu = max(1.0, abs(inputs.r_a * a), abs(inputs.r_b * b), consumption,
                   abs(transfer), cost, abs(labor_income))
    marginal_c = consumption ** (-params.gamma_c)
    scale_v = max(1.0, abs(v_a), abs(v_b), abs(lambda_a), abs(lambda_b), marginal_c)
    shadow_a = v_a - lambda_a if active_a_upper else v_a + lambda_a
    shadow_b = v_b - lambda_b if active_b_upper else v_b + lambda_b
    components: dict[str, float] = {
        "control_domain": max(0.0, -float(np.min(labor))) / scale_mu if labor.size else 0.0,
        "consumption": abs(marginal_c - shadow_b) / scale_v,
    }
    if active_a:
        components["primal_a"] = max(0.0, -mu_a) / scale_mu
        components["dual_a"] = max(0.0, -lambda_a) / scale_v
        components["complementarity_a"] = abs(lambda_a * mu_a) / (scale_v * scale_mu)
    if active_a_upper:
        components["primal_a_upper"] = max(0.0, mu_a) / scale_mu
        components["dual_a_upper"] = max(0.0, -lambda_a) / scale_v
        components["complementarity_a_upper"] = abs(lambda_a * mu_a) / (scale_v * scale_mu)
    if active_b:
        components["primal_b"] = max(0.0, -mu_b) / scale_mu
        components["dual_b"] = max(0.0, -lambda_b) / scale_v
        components["complementarity_b"] = abs(lambda_b * mu_b) / (scale_v * scale_mu)
    if active_b_upper:
        components["primal_b_upper"] = max(0.0, mu_b) / scale_mu
        components["dual_b_upper"] = max(0.0, -lambda_b) / scale_v
        components["complementarity_b_upper"] = abs(lambda_b * mu_b) / (scale_v * scale_mu)
    labor_stationarity = -inputs.labor_weights * labor ** params.phi + shadow_b * wage_terms
    for j, stationarity in enumerate(labor_stationarity):
        raw = abs(stationarity) if labor[j] > zero_tolerance else max(float(stationarity), 0.0)
        components[f"labor_{j}"] = raw / scale_v
    scale = max(a, params.a_bar)
    if transfer > zero_tolerance:
        raw_d = abs(shadow_a - shadow_b * (1.0 + params.chi_0 + params.chi_1 * transfer / scale))
    elif transfer < -zero_tolerance:
        raw_d = abs(shadow_a - shadow_b * (1.0 - params.chi_0 + params.chi_1 * transfer / scale))
    else:
        raw_d = _distance_to_interval(shadow_a - shadow_b, -shadow_b * params.chi_0, shadow_b * params.chi_0)
    components["transfer"] = raw_d / scale_v if shadow_b > 0.0 else np.inf
    if not np.isfinite(list(components.values())).all():
        return lambda_a, lambda_b, {**components, "finiteness": np.inf}
    return lambda_a, lambda_b, components
