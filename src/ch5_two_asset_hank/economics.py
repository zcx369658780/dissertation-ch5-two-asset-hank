"""Pure source-bound household equations."""

from __future__ import annotations

import numpy as np

from .contracts import EconomicParams, HouseholdInputs


def adjustment_cost(d: np.ndarray | float, a: np.ndarray | float, params: EconomicParams) -> np.ndarray:
    d_array = np.asarray(d, dtype=float)
    scale = np.maximum(np.asarray(a, dtype=float), params.a_bar)
    return params.chi_0 * np.abs(d_array) + 0.5 * params.chi_1 * d_array**2 / scale


def transfer_candidate(v_a: float, v_b: float, a: float, params: EconomicParams) -> float:
    if not np.isfinite([v_a, v_b, a]).all() or v_b <= 0:
        raise ValueError("transfer FOC requires finite derivatives and V_b > 0")
    q = v_a / v_b - 1.0
    threshold = min(q + params.chi_0, 0.0) + max(q - params.chi_0, 0.0)
    return max(a, params.a_bar) * threshold / params.chi_1


def consumption_from_vb(v_b: float, params: EconomicParams) -> float:
    if not np.isfinite(v_b) or v_b <= 0:
        raise ValueError("consumption FOC requires V_b > 0")
    return float(v_b ** (-1.0 / params.gamma_c))


def labor_from_vb(v_b: float, z: float, inputs: HouseholdInputs, params: EconomicParams) -> np.ndarray:
    if v_b <= 0 or z < 0:
        raise ValueError("labor FOC requires V_b > 0 and z >= 0")
    net_wage = inputs.wages * (1.0 - inputs.tau - inputs.migration_costs) * z
    labor = np.power(v_b * net_wage / inputs.labor_weights, 1.0 / params.phi)
    return np.asarray(labor, dtype=float)


def flow_utility(consumption: float, labor: np.ndarray, inputs: HouseholdInputs, params: EconomicParams) -> float:
    if consumption <= 0 or np.any(labor < 0):
        return -np.inf
    if np.isclose(params.gamma_c, 1.0):
        consumption_utility = np.log(consumption)
    else:
        consumption_utility = consumption ** (1.0 - params.gamma_c) / (1.0 - params.gamma_c)
    disutility = np.sum(inputs.labor_weights * labor ** (1.0 + params.phi) / (1.0 + params.phi))
    return float(consumption_utility - disutility)


def asset_drifts(
    a: float,
    b: float,
    z: float,
    consumption: float,
    labor: np.ndarray,
    transfer: float,
    inputs: HouseholdInputs,
    params: EconomicParams,
) -> tuple[float, float, float]:
    cost = float(adjustment_cost(transfer, a, params))
    labor_income = float(
        np.sum(inputs.wages * (1.0 - inputs.tau - inputs.migration_costs) * z * labor)
    )
    mu_b = inputs.r_b * b + labor_income - transfer - cost - consumption
    mu_a = inputs.r_a * a + transfer
    return mu_a, mu_b, cost

