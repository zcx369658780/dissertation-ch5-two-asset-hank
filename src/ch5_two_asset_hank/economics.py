"""Pure source-bound household equations."""

from __future__ import annotations

import numpy as np

from .contracts import EconomicParams, HouseholdInputs


def adjustment_cost(d: np.ndarray | float, a: np.ndarray | float, params: EconomicParams) -> np.ndarray:
    d_array = np.asarray(d, dtype=float)
    scale = np.maximum(np.asarray(a, dtype=float), params.a_bar)
    return params.chi_0 * np.abs(d_array) + 0.5 * params.chi_1 * d_array**2 / scale


def transfer_candidate(v_a: float, v_b: float, a: float, params: EconomicParams) -> float:
    """Return the production MATLAB-faithful bare-a transfer candidate."""
    if not np.isfinite([v_a, v_b, a]).all() or v_b <= 0:
        raise ValueError("transfer FOC requires finite derivatives and V_b > 0")
    q = v_a / v_b - 1.0
    threshold = min(q + params.chi_0, 0.0) + max(q - params.chi_0, 0.0)
    return a * threshold / params.chi_1


def transfer_candidate_matlab_faithful_raw_vb(
    v_a: float,
    v_b: float,
    a: float,
    params: EconomicParams,
) -> float:
    """Reproduce protected ``HANK3_FOC`` arithmetic using raw ``V_b``."""
    if not np.isfinite([v_a, v_b, a]).all():
        raise ValueError("faithful raw-Vb transfer FOC requires finite inputs")
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = np.divide(np.float64(v_a), np.float64(v_b))
        threshold = np.fmin(ratio - 1.0 + params.chi_0, 0.0) + np.fmax(
            ratio - 1.0 - params.chi_0,
            0.0,
        )
        value = np.divide(np.float64(a) * threshold, params.chi_1)
    return float(value)


def transfer_candidate_corrected_max_scale(
    v_a: float,
    v_b: float,
    a: float,
    params: EconomicParams,
) -> float:
    """Retain the historical corrected-equation max-scale reference candidate."""
    if not np.isfinite([v_a, v_b, a]).all() or v_b <= 0:
        raise ValueError("transfer FOC requires finite derivatives and V_b > 0")
    q = v_a / v_b - 1.0
    threshold = min(q + params.chi_0, 0.0) + max(q - params.chi_0, 0.0)
    return max(a, params.a_bar) * threshold / params.chi_1


def matlab_faithful_illiquid_return(
    a: np.ndarray | float,
    a_max: float,
    r_a: float,
) -> np.ndarray:
    """Apply the designated MATLAB finite-grid illiquid-return taper."""
    a_array = np.asarray(a, dtype=float)
    if not np.all(np.isfinite(a_array)) or not np.isfinite([a_max, r_a]).all():
        raise ValueError("faithful illiquid-return inputs must be finite")
    if a_max <= 0.0:
        raise ValueError("faithful illiquid-return taper requires a_max > 0")
    if np.any(a_array < 0.0) or np.any(a_array > a_max):
        raise ValueError("faithful illiquid-return taper requires 0 <= a <= a_max")
    return r_a * (1.0 - 0.1 * (a_array / a_max) ** 9)


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


def asset_drifts_matlab_faithful(
    a: float,
    b: float,
    z: float,
    consumption: float,
    labor: np.ndarray,
    transfer: float,
    inputs: HouseholdInputs,
    params: EconomicParams,
    a_max: float,
) -> tuple[float, float, float]:
    """Use the MATLAB taper in mu_a while preserving the existing liquid budget."""
    cost = float(adjustment_cost(transfer, a, params))
    labor_income = float(
        np.sum(inputs.wages * (1.0 - inputs.tau - inputs.migration_costs) * z * labor)
    )
    mu_b = inputs.r_b * b + labor_income - transfer - cost - consumption
    r_a_effective = float(matlab_faithful_illiquid_return(a, a_max, inputs.r_a))
    mu_a = r_a_effective * a + transfer
    return mu_a, mu_b, cost
