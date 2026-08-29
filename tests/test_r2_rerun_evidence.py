import numpy as np

from ch5_two_asset_hank import EconomicParams, GridSpec, HouseholdInputs, solve_hjb
from ch5_two_asset_hank.diagnostics import normalized_change
from ch5_two_asset_hank.hjb import HJBNumerics
from ch5_two_asset_hank.productivity import refinement_diagnostics


def synthetic_inputs():
    params = EconomicParams(0.05, 1.0, 1.0, 1.0, 1.0, 0.5, 0.2, 0.1)
    inputs = HouseholdInputs(0.0, 0.03, 0.0, np.array([1.0]), np.array([0.0]), np.array([1.0]))
    return params, inputs


def initial_value(grid, params):
    wage_productivity = grid.z[None, None, :]
    liquid_return = 0.03 * grid.b[None, :, None]
    consumption = 0.5 * (liquid_return + np.sqrt(liquid_return**2 + 4.0 * wage_productivity**2))
    labor = wage_productivity / consumption
    value = (np.log(consumption) - 0.5 * labor**2) / params.rho
    return np.broadcast_to(value, grid.shape).copy()


def solve_fixture(z):
    params, inputs = synthetic_inputs()
    grid = GridSpec(np.array([0.0, 1.0]), np.array([0.0, 5.0]), np.asarray(z), 0.0)
    result = solve_hjb(
        grid, params, inputs, initial_value(grid, params),
        HJBNumerics(pseudo_time_step=10.0, max_iterations=500,
                    change_tolerance=1e-8, residual_tolerance=1e-7),
    )
    return grid, result


def test_productivity_refinement_contract_and_separate_endpoint_errors():
    params = EconomicParams(0.05, 2.0, 1.0, 0.01, 0.2, 0.5, 0.2, 0.1)
    records = refinement_diagnostics(params)
    assert [record.n_z for record in records] == [5, 9, 17]
    for record in records:
        assert record.max_row_sum <= 1e-11
        assert record.min_off_diagonal >= -1e-11
        assert record.constant_error <= 1e-11
        assert record.affine_interior_error <= 1e-11
        assert record.reflected_lower_quadratic_error <= 1e-11
        assert record.left_nullity == 1
        assert record.quadratic_endpoint_error > 0.0
    errors = [record.quadratic_interior_error for record in records]
    assert errors[0] / errors[1] >= 1.8
    assert errors[1] / errors[2] >= 1.8


def test_deterministic_hjb_converges_with_full_lower_boundary_kkt_evidence():
    _, result = solve_fixture(np.array([0.5, 1.0, 1.5]))
    assert result.converged
    assert result.iterations == 41
    assert result.residual_sup <= 1e-7
    assert result.policy.kkt_residual <= 1e-7
    assert result.policy.boundary_violation <= 1e-12
    assert np.max(result.policy.lambda_b) > 0.0
    required = {"primal_a", "dual_a", "complementarity_a",
                "primal_b", "dual_b", "complementarity_b",
                "consumption", "labor_0", "transfer"}
    assert required <= result.policy.kkt_component_maxima.keys()


def test_fixed_lower_reflected_buffer2_buffer3_core_protocol():
    buffer2_grid, buffer2 = solve_fixture(np.arange(0.5, 2.0 + 1e-14, 0.0625))
    buffer3_grid, buffer3 = solve_fixture(np.arange(0.5, 2.25 + 1e-14, 0.0625))
    core2 = np.flatnonzero((buffer2_grid.z >= 0.5) & (buffer2_grid.z <= 1.5))
    core3 = [int(np.flatnonzero(np.isclose(buffer3_grid.z, z))[0]) for z in buffer2_grid.z[core2]]
    value_change = normalized_change(buffer2.value[:, :, core2], buffer3.value[:, :, core3])
    consumption_change = normalized_change(buffer2.policy.consumption[:, :, core2], buffer3.policy.consumption[:, :, core3])
    transfer_change = normalized_change(buffer2.policy.transfer[:, :, core2], buffer3.policy.transfer[:, :, core3])
    labor_change = normalized_change(buffer2.policy.labor[:, :, core2, :], buffer3.policy.labor[:, :, core3, :])
    assert buffer2.residual_sup <= 1e-7 and buffer3.residual_sup <= 1e-7
    assert buffer2.policy.kkt_residual <= 1e-7 and buffer3.policy.kkt_residual <= 1e-7
    np.testing.assert_array_equal(
        buffer2.policy.candidate_id[:, :, core2], buffer3.policy.candidate_id[:, :, core3]
    )
    assert core2[0] == 0 and core2[-1] == 16
    assert core3[0] == 0 and core3[-1] == 16
    assert buffer2_grid.z.size - 1 - core2[-1] == 8
    assert buffer3_grid.z.size - 1 - core3[-1] == 12
    assert transfer_change <= 1e-3
    assert value_change <= 1e-3
    assert consumption_change <= 1e-3
    assert labor_change <= 1e-3


def test_lower_productivity_lower_assets_has_feasible_full_kkt_control():
    grid, result = solve_fixture(np.arange(0.5, 1.5 + 1e-14, 0.0625))
    corner = (0, 0, 0)
    assert grid.z[corner[2]] == 0.5
    assert result.policy.consumption[corner] > 0.0
    assert np.all(result.policy.labor[corner] >= 0.0)
    assert result.policy.mu_a[corner] >= -1e-12
    assert result.policy.mu_b[corner] >= -1e-12
    assert result.policy.kkt_state_residual[corner] <= 1e-7
