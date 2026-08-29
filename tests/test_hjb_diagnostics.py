import numpy as np
import pytest
from scipy import sparse

from ch5_two_asset_hank.contracts import EconomicParams, GridSpec, OperatorBundle, PolicySnapshot
from ch5_two_asset_hank.diagnostics import hjb_residual
from ch5_two_asset_hank.hjb import HJBNumerics
from ch5_two_asset_hank.indexing import unflatten


def test_deterministic_synthetic_fixture_reports_exact_residual():
    grid = GridSpec(np.array([0.0, 1.0]), np.array([-1.0, 0.0]), np.array([0.5, 1.0]), -1.0)
    params = EconomicParams(0.05, 2.0, 1.0, 0.01, 0.2, 0.5, 0.2, 0.1)
    matrix = sparse.csr_matrix((grid.size, grid.size))
    operator = OperatorBundle(matrix, matrix, matrix, matrix, 0.0, 0.0)
    value = unflatten(np.arange(grid.size, dtype=float), grid.shape)
    utility = np.full(grid.shape, 2.0)
    zeros = np.zeros(grid.shape)
    policy = PolicySnapshot(np.ones(grid.shape), np.zeros(grid.shape + (1,)), zeros, zeros,
                            zeros, zeros, utility, np.full(grid.shape, "fixture"), zeros, zeros,
                            zeros, {}, 0.0, 0.0)
    residual = hjb_residual(value, policy, operator, grid, params)
    np.testing.assert_allclose(residual, params.rho * np.arange(grid.size) - 2.0)


def test_numerical_contract_rejects_nonpositive_tolerances():
    with pytest.raises(ValueError, match="tolerances"):
        HJBNumerics(residual_tolerance=0.0)
