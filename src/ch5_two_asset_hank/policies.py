"""Joint derivative candidate and constrained Hamiltonian selection."""

from __future__ import annotations

import math
from collections.abc import Callable

import numpy as np
from scipy.optimize import brentq

from .boundaries import check_boundary, drift_matches_direction, kkt_residuals
from .contracts import EconomicParams, GridSpec, HouseholdInputs, PolicySnapshot
from .derivatives import DerivativeBundle
from .economics import (
    adjustment_cost,
    asset_drifts,
    consumption_from_vb,
    flow_utility,
    labor_from_vb,
    transfer_candidate,
)


class PolicySelectionError(RuntimeError):
    pass


def _certified_zero_drift_root(
    liquid_drift: Callable[[float], float],
    lower: float,
    upper: float,
    tolerance: float,
) -> float:
    """Return a root only when its drift residual meets the shared Z contract."""
    root = brentq(
        liquid_drift,
        lower,
        upper,
        xtol=np.nextafter(0.0, 1.0),
        rtol=4.0 * np.finfo(float).eps,
    )
    residual = abs(float(liquid_drift(root)))
    if not np.isfinite(residual) or residual > tolerance:
        raise PolicySelectionError(
            f"zero-liquid-drift root is not certified: residual={residual:.3e}, "
            f"tolerance={tolerance:.3e}"
        )
    return float(root)


def _controls_from_shadow_values(
    v_a: float, shadow_b: float, a: float, z: float,
    inputs: HouseholdInputs, params: EconomicParams, active_a: bool, tolerance: float,
) -> tuple[float, np.ndarray, float]:
    consumption = consumption_from_vb(shadow_b, params)
    labor = labor_from_vb(shadow_b, z, inputs, params)
    transfer = transfer_candidate(v_a, shadow_b, a, params)
    if active_a and transfer < 0.0:
        transfer = 0.0
    return consumption, labor, transfer


def _lower_boundary_controls(
    v_a: float, v_b: float, a: float, b: float, z: float,
    active_a: bool, active_b: bool, inputs: HouseholdInputs,
    params: EconomicParams, tolerance: float,
) -> tuple[float, np.ndarray, float]:
    consumption, labor, transfer = _controls_from_shadow_values(
        v_a, v_b, a, z, inputs, params, active_a, tolerance,
    )
    if not active_b:
        return consumption, labor, transfer
    _, mu_b, _ = asset_drifts(a, b, z, consumption, labor, transfer, inputs, params)
    if mu_b >= -tolerance:
        return consumption, labor, transfer

    def liquid_drift(shadow_b: float) -> float:
        c_value, l_value, d_value = _controls_from_shadow_values(
            v_a, shadow_b, a, z, inputs, params, active_a, tolerance,
        )
        return asset_drifts(a, b, z, c_value, l_value, d_value, inputs, params)[1]

    upper = max(2.0 * v_b, v_b + 1.0)
    for _ in range(80):
        if liquid_drift(upper) >= 0.0:
            break
        upper *= 2.0
    else:
        raise PolicySelectionError("failed to bracket liquid-boundary shadow value")
    shadow_b = brentq(liquid_drift, v_b, upper, xtol=tolerance, rtol=1e-14)
    return _controls_from_shadow_values(v_a, shadow_b, a, z, inputs, params, active_a, tolerance)


def _zero_liquid_shadow(
    v_a: float, a: float, b: float, z: float, active_a: bool,
    inputs: HouseholdInputs, params: EconomicParams, tolerance: float,
) -> float | None:
    def liquid_drift(shadow_b: float) -> float:
        c_value, l_value, d_value = _controls_from_shadow_values(
            v_a, shadow_b, a, z, inputs, params, active_a, tolerance,
        )
        return asset_drifts(a, b, z, c_value, l_value, d_value, inputs, params)[1]

    lower, upper = 1e-10, 1.0
    f_lower = liquid_drift(lower)
    for _ in range(80):
        f_upper = liquid_drift(upper)
        if f_lower == 0.0:
            return lower
        if f_lower * f_upper <= 0.0:
            return _certified_zero_drift_root(liquid_drift, lower, upper, tolerance)
        upper *= 2.0
    return None


def _interior_zero_illiquid_controls(
    a_forward: float,
    a_backward: float,
    v_b: float,
    a: float,
    b: float,
    z: float,
    active_b: bool,
    inputs: HouseholdInputs,
    params: EconomicParams,
    tolerance: float,
    active_b_upper: bool = False,
) -> tuple[float, float, np.ndarray, float] | None:
    """Construct the endogenous mu_a=0 candidate for a crossing-upwind state."""
    if active_b and active_b_upper:
        raise ValueError("lower and upper liquid constraints cannot both be active")
    transfer = -inputs.r_a * a

    def controls(shadow_b: float) -> tuple[float, np.ndarray]:
        return (
            consumption_from_vb(shadow_b, params),
            labor_from_vb(shadow_b, z, inputs, params),
        )

    def liquid_drift(shadow_b: float) -> float:
        consumption, labor = controls(shadow_b)
        return asset_drifts(
            a, b, z, consumption, labor, transfer, inputs, params,
        )[1]

    shadow_b = v_b
    if active_b and liquid_drift(shadow_b) < -tolerance:
        upper = max(2.0 * shadow_b, shadow_b + 1.0)
        for _ in range(80):
            if liquid_drift(upper) >= 0.0:
                break
            upper *= 2.0
        else:
            raise PolicySelectionError("failed to bracket interior a-zero liquid-boundary shadow")
        shadow_b = _certified_zero_drift_root(
            liquid_drift, shadow_b, upper, tolerance,
        )
    elif active_b_upper and liquid_drift(shadow_b) > tolerance:
        lower = 1e-10
        if liquid_drift(lower) * liquid_drift(shadow_b) > 0.0:
            raise PolicySelectionError(
                "failed to bracket interior a-zero upper-liquid-boundary shadow"
            )
        shadow_b = _certified_zero_drift_root(
            liquid_drift, lower, shadow_b, tolerance,
        )

    scale = max(a, params.a_bar)
    if transfer > tolerance:
        v_a = shadow_b * (1.0 + params.chi_0 + params.chi_1 * transfer / scale)
    elif transfer < -tolerance:
        v_a = shadow_b * (1.0 - params.chi_0 + params.chi_1 * transfer / scale)
    else:
        v_a = shadow_b
    lower_a, upper_a = sorted((a_forward, a_backward))
    if v_a < lower_a - tolerance or v_a > upper_a + tolerance:
        return None
    consumption, labor = controls(shadow_b)
    return float(v_a), consumption, labor, float(transfer)


def _dual_upper_corner_controls(
    v_a: float,
    v_b: float,
    a: float,
    b: float,
    z: float,
    inputs: HouseholdInputs,
    params: EconomicParams,
    tolerance: float,
) -> tuple[float, float, np.ndarray, float] | None:
    """Construct the joint upper-a/upper-b zero-drift state-constraint candidate."""
    if v_a <= 0.0 or v_b <= 0.0 or not np.isfinite([v_a, v_b]).all():
        return None
    transfer = -inputs.r_a * a

    def controls(shadow_b: float) -> tuple[float, np.ndarray]:
        return (
            consumption_from_vb(shadow_b, params),
            labor_from_vb(shadow_b, z, inputs, params),
        )

    def liquid_drift(shadow_b: float) -> float:
        consumption, labor = controls(shadow_b)
        return asset_drifts(
            a, b, z, consumption, labor, transfer, inputs, params,
        )[1]

    lower = 1e-10
    f_lower = liquid_drift(lower)
    f_upper = liquid_drift(v_b)
    if abs(f_upper) <= tolerance:
        shadow_b = v_b
    elif f_lower * f_upper > 0.0:
        return None
    else:
        shadow_b = _certified_zero_drift_root(
            liquid_drift, lower, v_b, tolerance,
        )

    scale = max(a, params.a_bar)
    if transfer > tolerance:
        shadow_a = shadow_b * (
            1.0 + params.chi_0 + params.chi_1 * transfer / scale
        )
    elif transfer < -tolerance:
        shadow_a = shadow_b * (
            1.0 - params.chi_0 + params.chi_1 * transfer / scale
        )
    else:
        shadow_a = shadow_b
    eta_a = v_a - shadow_a
    eta_b = v_b - shadow_b
    if eta_a < -tolerance or eta_b < -tolerance:
        return None
    consumption, labor = controls(shadow_b)
    return float(shadow_b), consumption, labor, float(transfer)


def _upper_a_lower_b_controls(
    v_a: float,
    v_b: float,
    a: float,
    b: float,
    z: float,
    inputs: HouseholdInputs,
    params: EconomicParams,
    tolerance: float,
) -> tuple[float, float, np.ndarray, float] | None:
    """Construct the upper-a candidate for active or slack lower-b closure."""
    if v_a <= 0.0 or v_b <= 0.0 or not np.isfinite([v_a, v_b]).all():
        return None
    transfer = -inputs.r_a * a

    def controls(shadow_b: float) -> tuple[float, np.ndarray]:
        return (
            consumption_from_vb(shadow_b, params),
            labor_from_vb(shadow_b, z, inputs, params),
        )

    def liquid_drift(shadow_b: float) -> float:
        consumption, labor = controls(shadow_b)
        return asset_drifts(
            a, b, z, consumption, labor, transfer, inputs, params,
        )[1]

    drift_at_derivative = liquid_drift(v_b)
    if abs(drift_at_derivative) <= tolerance:
        shadow_b = v_b
    elif drift_at_derivative > 0.0:
        shadow_b = v_b
    else:
        upper = max(2.0 * v_b, v_b + 1.0)
        for _ in range(80):
            if liquid_drift(upper) >= 0.0:
                break
            upper *= 2.0
        else:
            raise PolicySelectionError(
                "failed to bracket upper-a/lower-b liquid-boundary shadow"
            )
        shadow_b = _certified_zero_drift_root(
            liquid_drift, v_b, upper, tolerance,
        )

    scale = max(a, params.a_bar)
    if transfer > tolerance:
        shadow_a = shadow_b * (
            1.0 + params.chi_0 + params.chi_1 * transfer / scale
        )
    elif transfer < -tolerance:
        shadow_a = shadow_b * (
            1.0 - params.chi_0 + params.chi_1 * transfer / scale
        )
    else:
        shadow_a = shadow_b
    if v_a - shadow_a < -tolerance or shadow_b - v_b < -tolerance:
        return None
    consumption, labor = controls(shadow_b)
    return float(shadow_b), consumption, labor, float(transfer)


def _upper_a_interior_b_controls(
    v_a: float,
    b_forward: float,
    b_backward: float,
    a: float,
    b: float,
    z: float,
    inputs: HouseholdInputs,
    params: EconomicParams,
    tolerance: float,
) -> tuple[float, float, np.ndarray, float] | None:
    """Construct the upper-a zero-drift candidate with an interior-b Z shadow."""
    if (
        v_a <= 0.0
        or b_forward <= 0.0
        or b_backward <= 0.0
        or not np.isfinite([v_a, b_forward, b_backward]).all()
    ):
        return None
    transfer = -inputs.r_a * a

    def controls(shadow_b: float) -> tuple[float, np.ndarray]:
        return (
            consumption_from_vb(shadow_b, params),
            labor_from_vb(shadow_b, z, inputs, params),
        )

    def liquid_drift(shadow_b: float) -> float:
        consumption, labor = controls(shadow_b)
        return asset_drifts(
            a, b, z, consumption, labor, transfer, inputs, params,
        )[1]

    lower, upper = sorted((b_forward, b_backward))
    f_lower = liquid_drift(lower)
    f_upper = liquid_drift(upper)
    if abs(f_lower) <= tolerance:
        shadow_b = lower
    elif abs(f_upper) <= tolerance:
        shadow_b = upper
    elif f_lower * f_upper > 0.0:
        return None
    else:
        shadow_b = _certified_zero_drift_root(
            liquid_drift, lower, upper, tolerance,
        )

    scale = max(a, params.a_bar)
    if transfer > tolerance:
        shadow_a = shadow_b * (
            1.0 + params.chi_0 + params.chi_1 * transfer / scale
        )
    elif transfer < -tolerance:
        shadow_a = shadow_b * (
            1.0 - params.chi_0 + params.chi_1 * transfer / scale
        )
    else:
        shadow_a = shadow_b
    if v_a - shadow_a < -tolerance:
        return None
    consumption, labor = controls(shadow_b)
    return float(shadow_b), consumption, labor, float(transfer)


def _budget_roots(base: float, a: float, params: EconomicParams) -> list[float]:
    """Roots of base-d-chi(d,a)=0 on both absolute-value branches."""
    scale = max(a, params.a_bar)
    quadratic = params.chi_1 / (2.0 * scale)
    roots: list[float] = []
    for linear, sign in ((1.0 + params.chi_0, 1), (1.0 - params.chi_0, -1)):
        discriminant = linear * linear + 4.0 * quadratic * base
        if discriminant < 0:
            continue
        root_disc = math.sqrt(discriminant)
        for root in ((-linear + root_disc) / (2.0 * quadratic), (-linear - root_disc) / (2.0 * quadratic)):
            if (sign > 0 and root >= 0) or (sign < 0 and root <= 0):
                roots.append(root)
    return roots


def select_policy(
    derivatives: DerivativeBundle,
    grid: GridSpec,
    params: EconomicParams,
    inputs: HouseholdInputs,
    tolerance: float,
) -> PolicySnapshot:
    shape = grid.shape
    n_labor = inputs.wages.size
    c_out = np.empty(shape)
    l_out = np.empty(shape + (n_labor,))
    d_out = np.empty(shape)
    cost_out = np.empty(shape)
    mu_a_out = np.empty(shape)
    mu_b_out = np.empty(shape)
    utility_out = np.empty(shape)
    candidate_out = np.empty(shape, dtype="U8")
    lambda_a_out = np.zeros(shape)
    lambda_b_out = np.zeros(shape)
    kkt_state_out = np.zeros(shape)
    kkt_component_maxima: dict[str, float] = {}
    max_boundary_violation = 0.0
    max_kkt_residual = 0.0

    a_options = (("F", derivatives.a_forward, derivatives.a_forward_valid), ("B", derivatives.a_backward, derivatives.a_backward_valid))
    b_options = (("F", derivatives.b_forward, derivatives.b_forward_valid), ("B", derivatives.b_backward, derivatives.b_backward_valid))

    for index in np.ndindex(shape):
        i_a, i_b, i_z = index
        a, b, z = grid.a[i_a], grid.b[i_b], grid.z[i_z]
        candidates: list[tuple[float, str, float, np.ndarray, float, float, float, float, float, float, dict[str, float]]] = []
        for a_direction, a_values, a_valid in a_options:
            if not a_valid[index]:
                continue
            v_a = float(a_values[index])
            local_b_options: list[tuple[str, float]] = []
            for b_direction, b_values, b_valid in b_options:
                if b_valid[index]:
                    local_b_options.append((b_direction, float(b_values[index])))
            zero_shadow = _zero_liquid_shadow(
                v_a, a, b, z, i_a == 0, inputs, params, tolerance,
            )
            if zero_shadow is not None:
                local_b_options.append(("Z", zero_shadow))
            for b_direction, v_b in local_b_options:
                if v_b <= 0 or not np.isfinite([v_a, v_b]).all():
                    continue
                active_a = i_a == 0
                active_a_upper = i_a == shape[0] - 1
                active_b = i_b == 0
                active_b_upper = i_b == shape[1] - 1
                consumption, labor, constrained_transfer = _lower_boundary_controls(
                    v_a, v_b, a, b, z, active_a, active_b, inputs, params, tolerance,
                )
                base_income = inputs.r_b * b + float(
                    np.sum(inputs.wages * (1.0 - inputs.tau - inputs.migration_costs) * z * labor)
                ) - consumption
                transfer_values = [constrained_transfer]
                if not (active_a or active_b):
                    transfer_values.extend([transfer_candidate(v_a, v_b, a, params), 0.0])
                    transfer_values.extend(_budget_roots(base_income, a, params))
                if i_a in (0, shape[0] - 1):
                    transfer_values.append(-inputs.r_a * a)
                for transfer in dict.fromkeys(round(value, 14) for value in transfer_values):
                    mu_a, mu_b, cost = asset_drifts(a, b, z, consumption, labor, transfer, inputs, params)
                    if not drift_matches_direction(mu_a, a_direction, tolerance):
                        continue
                    if not drift_matches_direction(mu_b, b_direction, tolerance):
                        continue
                    boundary = check_boundary(i_a, i_b, shape[0], shape[1], mu_a, mu_b, tolerance)
                    if not boundary.feasible:
                        continue
                    utility = flow_utility(consumption, labor, inputs, params)
                    hamiltonian = utility + v_a * mu_a + v_b * mu_b
                    identifier = f"{a_direction}{b_direction}{'0' if abs(transfer) <= tolerance else ''}"
                    lambda_a, lambda_b, components = kkt_residuals(
                        active_a=active_a, active_b=active_b, a=a, b=b, z=z,
                        consumption=consumption, labor=labor, transfer=transfer, mu_a=mu_a, mu_b=mu_b,
                        v_a=v_a, v_b=v_b, inputs=inputs, params=params, zero_tolerance=tolerance,
                        active_a_upper=active_a_upper,
                        active_b_upper=active_b_upper,
                    )
                    kkt_value = max(components.values(), default=0.0)
                    if (active_a or active_a_upper or active_b or active_b_upper) and kkt_value > 1e-7:
                        continue
                    candidates.append((hamiltonian, identifier, consumption, labor, transfer, cost,
                                       mu_a, mu_b, lambda_a, lambda_b, components))
        if (
            i_a == shape[0] - 1
            and i_b == shape[1] - 1
            and derivatives.a_backward_valid[index]
            and derivatives.b_backward_valid[index]
        ):
            v_a = float(derivatives.a_backward[index])
            v_b = float(derivatives.b_backward[index])
            corner = _dual_upper_corner_controls(
                v_a, v_b, a, b, z, inputs, params, tolerance,
            )
            if corner is not None:
                _, consumption, labor, transfer = corner
                mu_a, mu_b, cost = asset_drifts(
                    a, b, z, consumption, labor, transfer, inputs, params,
                )
                boundary = check_boundary(
                    i_a, i_b, shape[0], shape[1], mu_a, mu_b, tolerance,
                )
                lambda_a, lambda_b, components = kkt_residuals(
                    active_a=False, active_a_upper=True,
                    active_b=False, active_b_upper=True,
                    a=a, b=b, z=z, consumption=consumption, labor=labor,
                    transfer=transfer, mu_a=mu_a, mu_b=mu_b,
                    v_a=v_a, v_b=v_b, inputs=inputs, params=params,
                    zero_tolerance=tolerance,
                )
                if (
                    drift_matches_direction(mu_a, "Z", tolerance)
                    and drift_matches_direction(mu_b, "Z", tolerance)
                    and boundary.feasible
                    and max(components.values(), default=0.0) <= 1e-7
                ):
                    utility = flow_utility(consumption, labor, inputs, params)
                    hamiltonian = utility + v_a * mu_a + v_b * mu_b
                    candidates.append((
                        hamiltonian, "ZZU", consumption, labor, transfer, cost,
                        mu_a, mu_b, lambda_a, lambda_b, components,
                    ))
        if (
            i_a == shape[0] - 1
            and i_b == 0
            and derivatives.a_backward_valid[index]
            and derivatives.b_forward_valid[index]
        ):
            v_a = float(derivatives.a_backward[index])
            v_b = float(derivatives.b_forward[index])
            corner = _upper_a_lower_b_controls(
                v_a, v_b, a, b, z, inputs, params, tolerance,
            )
            if corner is not None:
                _, consumption, labor, transfer = corner
                mu_a, mu_b, cost = asset_drifts(
                    a, b, z, consumption, labor, transfer, inputs, params,
                )
                b_direction = "F" if mu_b > tolerance else "Z"
                boundary = check_boundary(
                    i_a, i_b, shape[0], shape[1], mu_a, mu_b, tolerance,
                )
                lambda_a, lambda_b, components = kkt_residuals(
                    active_a=False, active_a_upper=True,
                    active_b=True, active_b_upper=False,
                    a=a, b=b, z=z, consumption=consumption, labor=labor,
                    transfer=transfer, mu_a=mu_a, mu_b=mu_b,
                    v_a=v_a, v_b=v_b, inputs=inputs, params=params,
                    zero_tolerance=tolerance,
                )
                if (
                    drift_matches_direction(mu_a, "Z", tolerance)
                    and drift_matches_direction(mu_b, b_direction, tolerance)
                    and boundary.feasible
                    and max(components.values(), default=0.0) <= 1e-7
                ):
                    utility = flow_utility(consumption, labor, inputs, params)
                    hamiltonian = utility + v_a * mu_a + v_b * mu_b
                    candidates.append((
                        hamiltonian, f"U{b_direction}L", consumption, labor, transfer, cost,
                        mu_a, mu_b, lambda_a, lambda_b, components,
                    ))
        if (
            i_a == shape[0] - 1
            and 0 < i_b < shape[1] - 1
            and derivatives.a_backward_valid[index]
            and derivatives.b_forward_valid[index]
            and derivatives.b_backward_valid[index]
        ):
            v_a = float(derivatives.a_backward[index])
            zero_b = _upper_a_interior_b_controls(
                v_a,
                float(derivatives.b_forward[index]),
                float(derivatives.b_backward[index]),
                a, b, z, inputs, params, tolerance,
            )
            if zero_b is not None:
                v_b, consumption, labor, transfer = zero_b
                mu_a, mu_b, cost = asset_drifts(
                    a, b, z, consumption, labor, transfer, inputs, params,
                )
                boundary = check_boundary(
                    i_a, i_b, shape[0], shape[1], mu_a, mu_b, tolerance,
                )
                lambda_a, lambda_b, components = kkt_residuals(
                    active_a=False, active_a_upper=True,
                    active_b=False, active_b_upper=False,
                    a=a, b=b, z=z, consumption=consumption, labor=labor,
                    transfer=transfer, mu_a=mu_a, mu_b=mu_b,
                    v_a=v_a, v_b=v_b, inputs=inputs, params=params,
                    zero_tolerance=tolerance,
                )
                if (
                    drift_matches_direction(mu_a, "Z", tolerance)
                    and drift_matches_direction(mu_b, "Z", tolerance)
                    and boundary.feasible
                    and max(components.values(), default=0.0) <= 1e-7
                ):
                    utility = flow_utility(consumption, labor, inputs, params)
                    hamiltonian = utility + v_a * mu_a + v_b * mu_b
                    candidates.append((
                        hamiltonian, "UZI", consumption, labor, transfer, cost,
                        mu_a, mu_b, lambda_a, lambda_b, components,
                    ))
        if (
            0 < i_a < shape[0] - 1
            and derivatives.a_forward_valid[index]
            and derivatives.a_backward_valid[index]
        ):
            a_forward = float(derivatives.a_forward[index])
            a_backward = float(derivatives.a_backward[index])
            for b_direction, b_values, b_valid in b_options:
                if not b_valid[index]:
                    continue
                v_b = float(b_values[index])
                if v_b <= 0.0 or not np.isfinite(v_b):
                    continue
                zero_a = _interior_zero_illiquid_controls(
                    a_forward, a_backward, v_b, a, b, z, i_b == 0,
                    inputs, params, tolerance,
                    active_b_upper=i_b == shape[1] - 1,
                )
                if zero_a is None:
                    continue
                v_a, consumption, labor, transfer = zero_a
                mu_a, mu_b, cost = asset_drifts(
                    a, b, z, consumption, labor, transfer, inputs, params,
                )
                if not drift_matches_direction(mu_a, "Z", tolerance):
                    continue
                if not drift_matches_direction(mu_b, b_direction, tolerance):
                    continue
                boundary = check_boundary(
                    i_a, i_b, shape[0], shape[1], mu_a, mu_b, tolerance,
                )
                if not boundary.feasible:
                    continue
                utility = flow_utility(consumption, labor, inputs, params)
                hamiltonian = utility + v_a * mu_a + v_b * mu_b
                identifier = f"Z{b_direction}{'0' if abs(transfer) <= tolerance else ''}"
                lambda_a, lambda_b, components = kkt_residuals(
                    active_a=False, active_b=i_b == 0,
                    active_b_upper=i_b == shape[1] - 1,
                    a=a, b=b, z=z,
                    consumption=consumption, labor=labor, transfer=transfer,
                    mu_a=mu_a, mu_b=mu_b, v_a=v_a, v_b=v_b,
                    inputs=inputs, params=params, zero_tolerance=tolerance,
                )
                if (
                    max(components.values(), default=0.0) > 1e-7
                    and i_b in (0, shape[1] - 1)
                ):
                    continue
                candidates.append((
                    hamiltonian, identifier, consumption, labor, transfer, cost,
                    mu_a, mu_b, lambda_a, lambda_b, components,
                ))
        if not candidates:
            raise PolicySelectionError(f"no admissible self-consistent candidate at state {index}")
        candidates.sort(key=lambda item: (-item[0], 0 if item[1].endswith("0") else 1, item[1]))
        _, identifier, consumption, labor, transfer, cost, mu_a, mu_b, lambda_a, lambda_b, components = candidates[0]
        boundary = check_boundary(i_a, i_b, shape[0], shape[1], mu_a, mu_b, tolerance)
        utility = flow_utility(consumption, labor, inputs, params)
        c_out[index] = consumption
        l_out[index] = labor
        d_out[index] = transfer
        cost_out[index] = cost
        mu_a_out[index] = mu_a
        mu_b_out[index] = mu_b
        utility_out[index] = utility
        candidate_out[index] = identifier
        lambda_a_out[index] = lambda_a
        lambda_b_out[index] = lambda_b
        is_constrained_state = (
            i_a in (0, shape[0] - 1) or i_b in (0, shape[1] - 1)
        )
        kkt_state_out[index] = max(components.values(), default=0.0) if is_constrained_state else 0.0
        if is_constrained_state:
            for name, value in components.items():
                kkt_component_maxima[name] = max(kkt_component_maxima.get(name, 0.0), value)
        max_boundary_violation = max(max_boundary_violation, boundary.violation)
        max_kkt_residual = max(max_kkt_residual, kkt_state_out[index])

    return PolicySnapshot(
        c_out, l_out, d_out, cost_out, mu_a_out, mu_b_out, utility_out,
        candidate_out, lambda_a_out, lambda_b_out, kkt_state_out, kkt_component_maxima,
        max_boundary_violation, max_kkt_residual,
    )
