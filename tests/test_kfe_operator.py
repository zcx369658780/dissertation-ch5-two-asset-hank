import numpy as np
import pytest
from scipy import sparse

from ch5_two_asset_hank import (
    EconomicParams,
    GridSpec,
    HouseholdInputs,
    make_kfe_input_from_operator,
    solve_hjb,
    solve_stationary_kfe,
)
from ch5_two_asset_hank.hjb import HJBNumerics
from ch5_two_asset_hank.kfe import KFEValidationError, build_forward_operator
from ch5_two_asset_hank.kfe_contract import make_kfe_input


def _grid():
    return GridSpec(
        np.array([0.0, 1.0]),
        np.array([0.0, 5.0]),
        np.array([0.5, 1.0, 1.5]),
        0.0,
    )


def _hjb_result(grid):
    params = EconomicParams(0.05, 1.0, 1.0, 1.0, 1.0, 0.5, 0.2, 0.1)
    inputs = HouseholdInputs(
        0.0, 0.03, 0.0, np.array([1.0]), np.array([0.0]), np.array([1.0]),
    )
    wage_productivity = grid.z[None, None, :]
    liquid_return = 0.03 * grid.b[None, :, None]
    consumption = 0.5 * (
        liquid_return + np.sqrt(liquid_return**2 + 4.0 * wage_productivity**2)
    )
    labor = wage_productivity / consumption
    initial = np.broadcast_to(
        (np.log(consumption) - 0.5 * labor**2) / params.rho, grid.shape,
    ).copy()
    return solve_hjb(
        grid, params, inputs, initial,
        HJBNumerics(
            pseudo_time_step=10.0,
            max_iterations=500,
            change_tolerance=1e-8,
            residual_tolerance=1e-7,
        ),
    )


def test_kfe_uses_exact_shared_transpose_and_fails_closed_on_nonunique_hjb_policy():
    grid = _grid()
    hjb = _hjb_result(grid)
    weights = np.full(grid.shape, 0.25)
    kfe_input = make_kfe_input_from_operator(hjb.operator, grid.shape, weights)
    forward = build_forward_operator(kfe_input)
    assert (forward != hjb.operator.g.transpose()).nnz == 0

    with pytest.raises(KFEValidationError, match="found 2 closed classes"):
        solve_stationary_kfe(kfe_input, grid)


def test_unique_source_independent_ctmc_returns_stationary_mass_and_accounting():
    grid = _grid()
    rows = np.arange(grid.size)
    columns = (rows + 1) % grid.size
    generator = sparse.csr_matrix(
        (
            np.concatenate((np.ones(grid.size), -np.ones(grid.size))),
            (
                np.concatenate((rows, rows)),
                np.concatenate((columns, rows)),
            ),
        ),
        shape=(grid.size, grid.size),
    )
    weights = np.full(grid.shape, 0.25)
    kfe_input = make_kfe_input(generator, grid.shape, weights)
    result = solve_stationary_kfe(kfe_input, grid)
    diagnostics = result.diagnostics
    assert diagnostics.unique_stationary
    assert diagnostics.closed_class_count == 1
    assert diagnostics.stationarity_sup <= 1e-10
    assert diagnostics.normalization_error <= 1e-10
    assert diagnostics.minimum_mass >= -1e-12
    assert diagnostics.negative_mass_count == 0
    assert diagnostics.mass_conservation_error <= 1e-11
    assert np.isclose(np.sum(result.mass), 1.0)
    assert np.isclose(np.sum(result.density * weights), 1.0)
    assert np.isclose(result.a_hh, 0.5)
    assert np.isclose(result.b_hh, 2.5)


def test_kfe_fails_closed_for_multiple_closed_classes():
    grid = _grid()
    zero = sparse.csr_matrix((grid.size, grid.size))
    kfe_input = make_kfe_input(zero, grid.shape, np.ones(grid.shape))
    with pytest.raises(KFEValidationError, match="not unique"):
        solve_stationary_kfe(kfe_input, grid)


def test_kfe_rejects_nonconservative_or_negative_rate_generator():
    grid = _grid()
    bad_conservation = sparse.eye(grid.size, format="csr")
    with pytest.raises(KFEValidationError, match="does not conserve"):
        solve_stationary_kfe(
            make_kfe_input(bad_conservation, grid.shape, np.ones(grid.shape)), grid,
        )

    negative_rate = sparse.lil_matrix((grid.size, grid.size))
    negative_rate[0, 1] = -1.0
    negative_rate[0, 0] = 1.0
    with pytest.raises(KFEValidationError, match="negative off-diagonal"):
        solve_stationary_kfe(
            make_kfe_input(negative_rate.tocsr(), grid.shape, np.ones(grid.shape)), grid,
        )


def test_kfe_contract_rejects_shape_or_weight_mismatch():
    grid = _grid()
    with pytest.raises(ValueError, match="generator shape"):
        make_kfe_input(sparse.eye(2, format="csr"), grid.shape, np.ones(grid.shape))
    with pytest.raises(ValueError, match="cell weights"):
        make_kfe_input(
            sparse.eye(grid.size, format="csr"), grid.shape, np.zeros(grid.shape),
        )
