import numpy as np
import pytest
from scipy import sparse

from ch5_two_asset_hank.contracts import EconomicParams, GridSpec, PolicySnapshot
from ch5_two_asset_hank.diagnostics import validate_operator
from ch5_two_asset_hank.generator import build_operator
from ch5_two_asset_hank.indexing import flatten
from ch5_two_asset_hank.kfe_contract import make_kfe_input
from ch5_two_asset_hank.productivity import build_z_generator


def fixture():
    grid = GridSpec(np.array([0.0, 1.0]), np.array([-1.0, 0.0]), np.array([0.5, 1.0, 1.5]), -1.0)
    params = EconomicParams(0.05, 2.0, 1.0, 0.01, 0.2, 0.5, 0.2, 0.1)
    return grid, params


def policy(grid, mu_a, mu_b):
    zeros = np.zeros(grid.shape)
    return PolicySnapshot(np.ones(grid.shape), np.zeros(grid.shape + (1,)), zeros, zeros,
                          mu_a, mu_b, zeros, np.full(grid.shape, "fixture"), zeros, zeros,
                          zeros, {}, 0.0, 0.0)


def test_productivity_generator_is_monotone_conservative_and_closed():
    grid, params = fixture()
    generator = build_z_generator(grid, params)
    np.testing.assert_allclose(np.asarray(generator.sum(axis=1)).ravel(), 0.0, atol=1e-14)
    off = generator - sparse.diags(generator.diagonal())
    assert np.all(off.data >= 0.0)
    assert generator[0, -1] == 0.0 and generator[-1, 0] == 0.0
    diffusion = 0.5 * params.sigma_z**2
    lower_test_function = (grid.z - grid.z[0]) ** 2
    assert np.isclose((generator @ lower_test_function)[0], 2.0 * diffusion, atol=1e-11)
    assert np.isclose(generator[0, 1], 2.0 * diffusion / (grid.z[1] - grid.z[0]) ** 2)


def test_productivity_support_rejects_nonpositive_economic_lower_bound():
    with pytest.raises(ValueError, match="z_L > 0"):
        GridSpec(np.array([0.0, 1.0]), np.array([-1.0, 0.0]), np.array([0.0, 0.5, 1.0]), -1.0)


def test_shared_operator_dimensions_ordering_and_linear_action():
    grid, params = fixture()
    mu_a = np.zeros(grid.shape); mu_b = np.zeros(grid.shape)
    mu_a[0] = 0.2; mu_a[1] = -0.3
    mu_b[:, 0] = 0.4; mu_b[:, 1] = -0.1
    operator = build_operator(grid, params, policy(grid, mu_a, mu_b), 1e-12)
    assert operator.g.shape == (grid.size, grid.size)
    validate_operator(operator, 1e-12)
    a_values = np.broadcast_to(grid.a[:, None, None], grid.shape)
    b_values = np.broadcast_to(grid.b[None, :, None], grid.shape)
    np.testing.assert_allclose(operator.g_a @ flatten(a_values, grid.shape), flatten(mu_a, grid.shape))
    np.testing.assert_allclose(operator.g_b @ flatten(b_values, grid.shape), flatten(mu_b, grid.shape))


def test_outward_boundary_drift_fails_closed_and_kfe_is_interface_only():
    grid, params = fixture()
    zeros = np.zeros(grid.shape); outward = zeros.copy(); outward[-1] = 0.1
    with pytest.raises(ValueError, match="upper boundary"):
        build_operator(grid, params, policy(grid, outward, zeros), 1e-12)
    kfe = make_kfe_input(sparse.eye(grid.size, format="csr"), grid.shape, np.ones(grid.shape))
    assert kfe.generator.shape == (grid.size, grid.size)
    assert not hasattr(kfe, "solve")
