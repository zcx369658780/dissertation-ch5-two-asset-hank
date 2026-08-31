"""Source-faithful local policy/upwind block extracted from the designated MATLAB HJB."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .contracts import EconomicParams, HouseholdInputs
from .economics import (
    asset_drifts_matlab_faithful,
    consumption_from_vb,
    flow_utility,
    labor_from_vb,
    matlab_faithful_illiquid_return,
    transfer_candidate_matlab_faithful_raw_vb,
)


MATLAB_DRIFT_TOLERANCE = 1.0e-12
MATLAB_DERIVATIVE_FLOOR = 1.0e-6


@dataclass(frozen=True)
class MatlabFaithfulLocalPolicy:
    """One cell of the designated MATLAB policy/upwind construction."""

    liquid_label: str
    transfer_label: str
    consumption: float
    labor: float
    transfer: float
    adjustment_cost: float
    effective_illiquid_return: float
    mu_a: float
    mu_b: float
    utility: float
    liquid_direction: str
    illiquid_direction: str
    b_backward_rate: float
    b_forward_rate: float
    a_backward_rate: float
    a_forward_rate: float
    iteration_b_backward_rate: float
    iteration_b_forward_rate: float


def _direction(value: float, tolerance: float) -> str:
    if value > tolerance:
        return "F"
    if value < -tolerance:
        return "B"
    return "0"


def select_matlab_faithful_local_policy(
    *,
    a: float,
    b: float,
    z: float,
    v_a_forward: float,
    v_a_backward: float,
    v_b_forward: float,
    v_b_backward: float,
    baseline_labor: float,
    transfer_income: float,
    borrowing_rate_gap: float,
    a_max: float,
    da: float,
    db: float,
    at_lower_a: bool,
    at_upper_a: bool,
    at_lower_b: bool,
    at_upper_b: bool,
    inputs: HouseholdInputs,
    params: EconomicParams,
    tolerance: float = MATLAB_DRIFT_TOLERANCE,
) -> MatlabFaithfulLocalPolicy:
    """Evaluate MATLAB lines 124--198 and 262--267 for one local cell.

    This is deliberately separate from the corrected/reference candidate and KKT
    selector.  Boundary booleans are explicit because this bounded entry point
    consumes a frozen local case rather than running an HJB grid iteration.
    """
    scalars = np.array(
        [
            a,
            b,
            z,
            v_a_forward,
            v_a_backward,
            v_b_forward,
            v_b_backward,
            baseline_labor,
            transfer_income,
            borrowing_rate_gap,
            a_max,
            da,
            db,
            tolerance,
        ],
        dtype=float,
    )
    if not np.all(np.isfinite(scalars)):
        raise ValueError("faithful local-policy inputs must be finite")
    if inputs.wages.size != 1:
        raise ValueError("designated MATLAB local policy requires one wage/labor type")
    if a < 0.0 or a > a_max or a_max <= 0.0 or da <= 0.0 or db <= 0.0:
        raise ValueError("faithful local-policy state/grid domain is invalid")
    if z <= 0.0 or baseline_labor < 0.0 or tolerance <= 0.0:
        raise ValueError("faithful local-policy productivity/labor/tolerance is invalid")
    if at_lower_a != np.isclose(a, 0.0) or at_upper_a != np.isclose(a, a_max):
        raise ValueError("illiquid boundary flags must match a and a_max")
    if at_lower_a and at_upper_a:
        raise ValueError("faithful local policy requires a nondegenerate illiquid grid")
    if at_lower_b and at_upper_b:
        raise ValueError("faithful local policy requires a nondegenerate liquid grid")
    effective_r_b = inputs.r_b + (borrowing_rate_gap if b < 0.0 else 0.0)
    local_inputs = HouseholdInputs(
        inputs.r_a,
        effective_r_b,
        inputs.tau,
        inputs.wages,
        inputs.migration_costs,
        inputs.labor_weights,
    )
    vb_b = max(v_b_backward, MATLAB_DERIVATIVE_FLOOR)
    vb_f = max(v_b_forward, MATLAB_DERIVATIVE_FLOOR)
    consumption_b = consumption_from_vb(vb_b, params)
    consumption_f = consumption_from_vb(vb_f, params)
    labor_b = float(labor_from_vb(vb_b, z, local_inputs, params)[0])
    labor_f = float(labor_from_vb(vb_f, z, local_inputs, params)[0])
    net_wage = float(
        local_inputs.wages[0]
        * (1.0 - local_inputs.tau - local_inputs.migration_costs[0])
        * z
    )
    liquid_resources_b = net_wage * labor_b + transfer_income + effective_r_b * b
    liquid_resources_f = net_wage * labor_f + transfer_income + effective_r_b * b
    sc_b = liquid_resources_b - consumption_b
    sc_f = liquid_resources_f - consumption_f
    use_liquid_b = sc_b < -tolerance
    use_liquid_f = sc_f > tolerance and not use_liquid_b
    if use_liquid_b:
        liquid_label = "B"
        consumption = consumption_b
        labor = labor_b
    elif use_liquid_f:
        liquid_label = "F"
        consumption = consumption_f
        labor = labor_f
    else:
        liquid_label = "0"
        labor = baseline_labor
        consumption = net_wage * baseline_labor + transfer_income + effective_r_b * b
    if consumption <= 0.0:
        raise ValueError("MATLAB zero/liquid branch produced non-positive consumption")

    d_bb = transfer_candidate_matlab_faithful_raw_vb(v_a_backward, v_b_backward, a, params)
    d_bf = transfer_candidate_matlab_faithful_raw_vb(v_a_forward, v_b_backward, a, params)
    d_fb = transfer_candidate_matlab_faithful_raw_vb(v_a_backward, v_b_forward, a, params)
    d_ff = transfer_candidate_matlab_faithful_raw_vb(v_a_forward, v_b_forward, a, params)
    d_b = (d_bf if d_bf > 0.0 else 0.0) + (d_bb if d_bb < 0.0 else 0.0)
    d_f = (d_ff if d_ff > 0.0 else 0.0) + (d_fb if d_fb < 0.0 else 0.0)
    if at_lower_a:
        d_b = d_bf if d_bf > tolerance else 0.0
        d_f = d_ff if d_ff > tolerance else 0.0
        if at_lower_b:
            d_b = max(d_b, 0.0)
    if at_upper_a:
        d_b = d_bb if d_bb < -tolerance else 0.0
        d_f = d_fb if d_fb < -tolerance else 0.0

    sdh_b = -d_b - float(
        # The accepted cost helper retains MATLAB's max(a, a_bar) denominator floor.
        asset_drifts_matlab_faithful(
            a,
            b,
            z,
            0.0,
            np.array([0.0]),
            d_b,
            local_inputs,
            params,
            a_max,
        )[2]
    )
    sdh_f = -d_f - float(
        asset_drifts_matlab_faithful(
            a,
            b,
            z,
            0.0,
            np.array([0.0]),
            d_f,
            local_inputs,
            params,
            a_max,
        )[2]
    )
    use_transfer_f = sdh_f > tolerance
    use_transfer_b = sdh_b < -tolerance and not use_transfer_f
    if at_lower_b:
        use_transfer_b = False
    if at_upper_b:
        use_transfer_f = False
        use_transfer_b = True
    if use_transfer_b:
        transfer_label = "B"
        transfer = d_b
        shadow_transfer_b = d_bb
        shadow_transfer_f = d_bf
    elif use_transfer_f:
        transfer_label = "F"
        transfer = d_f
        shadow_transfer_b = d_fb
        shadow_transfer_f = d_ff
    else:
        transfer_label = "0"
        transfer = 0.0
        shadow_transfer_b = 0.0
        shadow_transfer_f = 0.0

    effective_return = float(matlab_faithful_illiquid_return(a, a_max, inputs.r_a))
    mh_b = min(shadow_transfer_b, 0.0)
    mh_f = max(shadow_transfer_f, 0.0) + effective_return * a
    if at_upper_a:
        mh_b = shadow_transfer_b + effective_return * a_max
        mh_f = 0.0

    mu_a, mu_b, cost = asset_drifts_matlab_faithful(
        a,
        b,
        z,
        consumption - transfer_income,
        np.array([labor]),
        transfer,
        local_inputs,
        params,
        a_max,
    )
    utility = flow_utility(consumption, np.array([labor]), local_inputs, params)
    return MatlabFaithfulLocalPolicy(
        liquid_label=liquid_label,
        transfer_label=transfer_label,
        consumption=float(consumption),
        labor=float(labor),
        transfer=float(transfer),
        adjustment_cost=float(cost),
        effective_illiquid_return=effective_return,
        mu_a=float(mu_a),
        mu_b=float(mu_b),
        utility=float(utility),
        liquid_direction=_direction(float(mu_b), tolerance),
        illiquid_direction=_direction(float(mu_a), tolerance),
        b_backward_rate=max(-float(mu_b), 0.0) / db,
        b_forward_rate=max(float(mu_b), 0.0) / db,
        a_backward_rate=-float(mh_b) / da,
        a_forward_rate=float(mh_f) / da,
        iteration_b_backward_rate=-float(
            (sc_b if use_liquid_b else 0.0) + (sdh_b if use_transfer_b else 0.0)
        )
        / db,
        iteration_b_forward_rate=float(
            (sc_f if use_liquid_f else 0.0) + (sdh_f if use_transfer_f else 0.0)
        )
        / db,
    )
