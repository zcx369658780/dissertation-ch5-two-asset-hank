import numpy as np

from ch5_two_asset_hank.boundaries import (
    check_boundary,
    drift_matches_direction,
    kkt_residuals,
)
from ch5_two_asset_hank.contracts import EconomicParams, HouseholdInputs
from ch5_two_asset_hank.economics import asset_drifts
from ch5_two_asset_hank.policies import (
    _dual_upper_corner_controls,
    _interior_zero_illiquid_controls,
    _lower_boundary_controls,
    _upper_a_interior_b_controls,
    _upper_a_lower_b_controls,
    _zero_liquid_shadow,
)


def test_frozen_r4_zero_drift_candidate_is_residual_certified_without_relaxation():
    tolerance = 1e-12
    params = EconomicParams(0.05, 1.0, 1.0, 0.05, 1.0, 0.5, 0.2, 0.1)
    inputs = HouseholdInputs(
        0.04, 0.03, 0.0, np.array([1.0]), np.array([0.0]), np.array([1.0]),
    )
    a, b, z = 0.0, 5.0, 1.5625
    v_a = 0.7619162076101915

    shadow_b = _zero_liquid_shadow(
        v_a, a, b, z, True, inputs, params, tolerance,
    )
    assert shadow_b is not None
    consumption, labor, transfer = _lower_boundary_controls(
        v_a, shadow_b, a, b, z, True, False, inputs, params, tolerance,
    )
    mu_a, mu_b, _ = asset_drifts(
        a, b, z, consumption, labor, transfer, inputs, params,
    )

    assert np.isclose(shadow_b, 0.6282469107363821, rtol=0.0, atol=1e-12)
    assert np.isclose(transfer, 0.081382772911, rtol=0.0, atol=1e-12)
    assert abs(mu_b) <= tolerance
    assert drift_matches_direction(mu_b, "Z", tolerance)
    assert mu_a > 0.0
    assert drift_matches_direction(mu_a, "F", tolerance)

    boundary = check_boundary(0, 2, 3, 3, mu_a, mu_b, tolerance)
    assert boundary.feasible
    assert boundary.violation <= tolerance
    _, _, components = kkt_residuals(
        active_a=True,
        active_b=False,
        a=a,
        b=b,
        z=z,
        consumption=consumption,
        labor=labor,
        transfer=transfer,
        mu_a=mu_a,
        mu_b=mu_b,
        v_a=v_a,
        v_b=shadow_b,
        inputs=inputs,
        params=params,
        zero_tolerance=tolerance,
    )
    assert max(components.values()) <= 1e-7


def test_frozen_r4_crossing_upwind_state_has_endogenous_zero_a_drift_candidate():
    tolerance = 1e-12
    params = EconomicParams(0.05, 1.0, 1.0, 0.05, 1.0, 0.5, 0.2, 0.1)
    inputs = HouseholdInputs(
        0.04, 0.03, 0.0, np.array([1.0]), np.array([0.0]), np.array([1.0]),
    )
    a, b, z = 0.5, 0.0, 0.75
    a_forward = 1.1703333447650266
    a_backward = 1.2263220986701668
    v_b = 1.269836394939054

    candidate = _interior_zero_illiquid_controls(
        a_forward, a_backward, v_b, a, b, z, True,
        inputs, params, tolerance,
    )
    assert candidate is not None
    v_a, consumption, labor, transfer = candidate
    mu_a, mu_b, _ = asset_drifts(
        a, b, z, consumption, labor, transfer, inputs, params,
    )

    assert np.isclose(transfer, -inputs.r_a * a, rtol=0.0, atol=1e-15)
    assert abs(mu_a) <= tolerance
    assert abs(mu_b) <= tolerance
    assert a_forward <= v_a <= a_backward
    assert np.isclose(v_a, 1.198381277481218, rtol=0.0, atol=1e-12)

    boundary = check_boundary(1, 0, 3, 3, mu_a, mu_b, tolerance)
    assert boundary.feasible
    assert boundary.violation <= tolerance
    _, _, components = kkt_residuals(
        active_a=False,
        active_b=True,
        a=a,
        b=b,
        z=z,
        consumption=consumption,
        labor=labor,
        transfer=transfer,
        mu_a=mu_a,
        mu_b=mu_b,
        v_a=v_a,
        v_b=v_b,
        inputs=inputs,
        params=params,
        zero_tolerance=tolerance,
    )
    assert max(components.values()) <= 1e-7


def test_frozen_r4_upper_a_state_has_endogenous_boundary_multiplier():
    tolerance = 1e-12
    params = EconomicParams(0.05, 1.0, 1.0, 0.05, 1.0, 0.5, 0.2, 0.1)
    inputs = HouseholdInputs(
        0.04, 0.03, 0.0, np.array([1.0]), np.array([0.0]), np.array([1.0]),
    )
    a, b, z = 1.0, 0.0, 0.8125
    v_a = 1.14861142347835
    v_b = 1.2230360302145613

    consumption, labor, _ = _lower_boundary_controls(
        v_a, v_b, a, b, z, False, True, inputs, params, tolerance,
    )
    transfer = -inputs.r_a * a
    mu_a, mu_b, _ = asset_drifts(
        a, b, z, consumption, labor, transfer, inputs, params,
    )

    assert abs(mu_a) <= tolerance
    assert mu_b >= -tolerance
    boundary = check_boundary(2, 0, 3, 3, mu_a, mu_b, tolerance)
    assert boundary.feasible
    assert boundary.violation <= tolerance

    eta_a, _, components = kkt_residuals(
        active_a=False,
        active_a_upper=True,
        active_b=True,
        a=a,
        b=b,
        z=z,
        consumption=consumption,
        labor=labor,
        transfer=transfer,
        mu_a=mu_a,
        mu_b=mu_b,
        v_a=v_a,
        v_b=v_b,
        inputs=inputs,
        params=params,
        zero_tolerance=tolerance,
    )
    assert eta_a > 0.0
    assert "primal_a_upper" in components
    assert "dual_a_upper" in components
    assert "complementarity_a_upper" in components
    assert max(components.values()) <= 1e-7


def test_frozen_r4_dual_upper_corner_has_joint_zero_drift_kkt_closure():
    tolerance = 1e-12
    params = EconomicParams(0.05, 1.0, 1.0, 0.05, 1.0, 0.5, 0.2, 0.1)
    inputs = HouseholdInputs(
        0.04, 0.03, 0.0, np.array([1.0]), np.array([0.0]), np.array([1.0]),
    )
    a, b, z = 1.0, 5.0, 1.5
    v_a = 0.5713121926071842
    v_b = 0.903756799527612

    candidate = _dual_upper_corner_controls(
        v_a, v_b, a, b, z, inputs, params, tolerance,
    )
    assert candidate is not None
    shadow_b, consumption, labor, transfer = candidate
    mu_a, mu_b, _ = asset_drifts(
        a, b, z, consumption, labor, transfer, inputs, params,
    )

    assert np.isclose(transfer, -inputs.r_a * a, rtol=0.0, atol=1e-15)
    assert abs(mu_a) <= tolerance
    assert abs(mu_b) <= tolerance
    assert 0.0 < shadow_b < v_b
    assert drift_matches_direction(mu_a, "Z", tolerance)
    assert drift_matches_direction(mu_b, "Z", tolerance)

    boundary = check_boundary(2, 2, 3, 3, mu_a, mu_b, tolerance)
    assert boundary.feasible
    assert boundary.violation <= tolerance

    eta_a, eta_b, components = kkt_residuals(
        active_a=False,
        active_a_upper=True,
        active_b=False,
        active_b_upper=True,
        a=a,
        b=b,
        z=z,
        consumption=consumption,
        labor=labor,
        transfer=transfer,
        mu_a=mu_a,
        mu_b=mu_b,
        v_a=v_a,
        v_b=v_b,
        inputs=inputs,
        params=params,
        zero_tolerance=tolerance,
    )
    assert eta_a >= 0.0
    assert eta_b > 0.0
    assert "primal_b_upper" in components
    assert "dual_b_upper" in components
    assert "complementarity_b_upper" in components
    assert max(components.values()) <= 1e-7


def test_frozen_r4_interior_a_upper_b_has_joint_zero_drift_kkt_closure():
    tolerance = 1e-12
    params = EconomicParams(0.05, 1.0, 1.0, 0.05, 1.0, 0.5, 0.2, 0.1)
    inputs = HouseholdInputs(
        0.04, 0.03, 0.0, np.array([1.0]), np.array([0.0]), np.array([1.0]),
    )
    a, b, z = 0.5, 5.0, 1.0
    a_forward = 0.8275208181618545
    a_backward = 0.8443295393722572
    v_b = 1.0695715067232137

    candidate = _interior_zero_illiquid_controls(
        a_forward, a_backward, v_b, a, b, z, False,
        inputs, params, tolerance, active_b_upper=True,
    )
    assert candidate is not None
    v_a, consumption, labor, transfer = candidate
    mu_a, mu_b, _ = asset_drifts(
        a, b, z, consumption, labor, transfer, inputs, params,
    )

    assert np.isclose(transfer, -inputs.r_a * a, rtol=0.0, atol=1e-15)
    assert abs(mu_a) <= tolerance
    assert abs(mu_b) <= tolerance
    assert a_forward <= v_a <= a_backward
    assert np.isclose(v_a, 0.8365147286465846, rtol=0.0, atol=1e-12)
    assert drift_matches_direction(mu_a, "Z", tolerance)
    assert drift_matches_direction(mu_b, "Z", tolerance)

    boundary = check_boundary(1, 2, 3, 3, mu_a, mu_b, tolerance)
    assert boundary.feasible
    assert boundary.violation <= tolerance

    _, eta_b, components = kkt_residuals(
        active_a=False,
        active_b=False,
        active_b_upper=True,
        a=a,
        b=b,
        z=z,
        consumption=consumption,
        labor=labor,
        transfer=transfer,
        mu_a=mu_a,
        mu_b=mu_b,
        v_a=v_a,
        v_b=v_b,
        inputs=inputs,
        params=params,
        zero_tolerance=tolerance,
    )
    assert eta_b > 0.0
    assert "primal_b_upper" in components
    assert "dual_b_upper" in components
    assert "complementarity_b_upper" in components
    assert max(components.values()) <= 1e-7


def test_frozen_r4_upper_a_lower_b_has_joint_zero_drift_kkt_closure():
    tolerance = 1e-12
    params = EconomicParams(0.05, 1.0, 1.0, 0.05, 1.0, 0.5, 0.2, 0.1)
    inputs = HouseholdInputs(
        0.04, 0.03, 0.0, np.array([1.0]), np.array([0.0]), np.array([1.0]),
    )
    a, b, z = 1.0, 0.0, 0.6875
    v_a = 1.3096756237319624
    v_b = 1.2588632353149407

    candidate = _upper_a_lower_b_controls(
        v_a, v_b, a, b, z, inputs, params, tolerance,
    )
    assert candidate is not None
    shadow_b, consumption, labor, transfer = candidate
    mu_a, mu_b, _ = asset_drifts(
        a, b, z, consumption, labor, transfer, inputs, params,
    )

    assert np.isclose(transfer, -inputs.r_a * a, rtol=0.0, atol=1e-15)
    assert np.isclose(shadow_b, 1.4157256171872949, rtol=0.0, atol=1e-12)
    assert shadow_b > v_b
    assert abs(mu_a) <= tolerance
    assert abs(mu_b) <= tolerance
    assert drift_matches_direction(mu_a, "Z", tolerance)
    assert drift_matches_direction(mu_b, "Z", tolerance)

    boundary = check_boundary(2, 0, 3, 3, mu_a, mu_b, tolerance)
    assert boundary.feasible
    assert boundary.violation <= tolerance

    eta_a, lambda_b, components = kkt_residuals(
        active_a=False,
        active_a_upper=True,
        active_b=True,
        a=a,
        b=b,
        z=z,
        consumption=consumption,
        labor=labor,
        transfer=transfer,
        mu_a=mu_a,
        mu_b=mu_b,
        v_a=v_a,
        v_b=v_b,
        inputs=inputs,
        params=params,
        zero_tolerance=tolerance,
    )
    assert eta_a > 0.0
    assert lambda_b > 0.0
    assert "primal_a_upper" in components
    assert "complementarity_a_upper" in components
    assert "primal_b" in components
    assert "complementarity_b" in components
    assert max(components.values()) <= 1e-7


def test_frozen_r4_upper_a_interior_b_has_joint_zero_drift_kkt_closure():
    tolerance = 1e-12
    params = EconomicParams(0.05, 1.0, 1.0, 0.05, 1.0, 0.5, 0.2, 0.1)
    inputs = HouseholdInputs(
        0.04, 0.03, 0.0, np.array([1.0]), np.array([0.0]), np.array([1.0]),
    )
    a, b, z = 1.0, 2.5, 0.8125
    v_a = 1.0900614604620955
    b_forward = 1.0850659085568666
    b_backward = 1.235872027778018

    candidate = _upper_a_interior_b_controls(
        v_a, b_forward, b_backward, a, b, z, inputs, params, tolerance,
    )
    assert candidate is not None
    v_b, consumption, labor, transfer = candidate
    mu_a, mu_b, _ = asset_drifts(
        a, b, z, consumption, labor, transfer, inputs, params,
    )

    assert np.isclose(transfer, -inputs.r_a * a, rtol=0.0, atol=1e-15)
    assert np.isclose(v_b, 1.1487196278246121, rtol=0.0, atol=1e-12)
    assert min(b_forward, b_backward) < v_b < max(b_forward, b_backward)
    assert abs(mu_a) <= tolerance
    assert abs(mu_b) <= tolerance
    assert drift_matches_direction(mu_a, "Z", tolerance)
    assert drift_matches_direction(mu_b, "Z", tolerance)

    boundary = check_boundary(2, 1, 3, 3, mu_a, mu_b, tolerance)
    assert boundary.feasible
    assert boundary.violation <= tolerance

    eta_a, lambda_b, components = kkt_residuals(
        active_a=False,
        active_a_upper=True,
        active_b=False,
        active_b_upper=False,
        a=a,
        b=b,
        z=z,
        consumption=consumption,
        labor=labor,
        transfer=transfer,
        mu_a=mu_a,
        mu_b=mu_b,
        v_a=v_a,
        v_b=v_b,
        inputs=inputs,
        params=params,
        zero_tolerance=tolerance,
    )
    assert eta_a > 0.0
    assert lambda_b == 0.0
    assert "primal_a_upper" in components
    assert "dual_a_upper" in components
    assert "complementarity_a_upper" in components
    assert max(components.values()) <= 1e-7


def test_frozen_r4_upper_a_lower_b_slack_branch_recomputes_forward_controls():
    tolerance = 1e-12
    params = EconomicParams(0.05, 1.0, 1.0, 0.05, 1.0, 0.5, 0.2, 0.1)
    inputs = HouseholdInputs(
        0.04, 0.03, 0.0, np.array([1.0]), np.array([0.0]), np.array([1.0]),
    )
    a, b, z = 1.0, 0.0, 0.8125
    v_a = 1.3407408769313847
    v_b = 1.249395172408839

    candidate = _upper_a_lower_b_controls(
        v_a, v_b, a, b, z, inputs, params, tolerance,
    )
    assert candidate is not None
    shadow_b, consumption, labor, transfer = candidate
    mu_a, mu_b, _ = asset_drifts(
        a, b, z, consumption, labor, transfer, inputs, params,
    )

    assert shadow_b == v_b
    assert np.isclose(consumption, 0.8003872770470178, rtol=0.0, atol=1e-12)
    assert np.isclose(labor[0], 1.0151335775821817, rtol=0.0, atol=1e-12)
    assert np.isclose(transfer, -inputs.r_a * a, rtol=0.0, atol=1e-15)
    assert abs(mu_a) <= tolerance
    assert np.isclose(mu_b, 0.0616087547385048, rtol=0.0, atol=1e-12)
    assert drift_matches_direction(mu_a, "Z", tolerance)
    assert drift_matches_direction(mu_b, "F", tolerance)

    boundary = check_boundary(2, 0, 3, 3, mu_a, mu_b, tolerance)
    assert boundary.feasible
    assert boundary.violation <= tolerance

    eta_a, lambda_b, components = kkt_residuals(
        active_a=False,
        active_a_upper=True,
        active_b=True,
        a=a,
        b=b,
        z=z,
        consumption=consumption,
        labor=labor,
        transfer=transfer,
        mu_a=mu_a,
        mu_b=mu_b,
        v_a=v_a,
        v_b=v_b,
        inputs=inputs,
        params=params,
        zero_tolerance=tolerance,
    )
    assert eta_a > 0.0
    assert lambda_b == 0.0
    assert components["complementarity_a_upper"] == 0.0
    assert components["complementarity_b"] == 0.0
    assert max(components.values()) <= 1e-7
