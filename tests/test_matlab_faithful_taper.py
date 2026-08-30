import inspect

import numpy as np
import pytest

import ch5_two_asset_hank.generator as generator_module
from ch5_two_asset_hank.contracts import (
    EconomicParams,
    GridSpec,
    HouseholdInputs,
    PolicySnapshot,
)
from ch5_two_asset_hank.economics import (
    asset_drifts,
    asset_drifts_matlab_faithful,
    matlab_faithful_illiquid_return,
)
from ch5_two_asset_hank.generator import build_operator
from ch5_two_asset_hank.indexing import canonical_index, flatten


PARAMS = EconomicParams(0.05, 2.0, 1.0, 0.1, 2.0, 0.5, 0.2, 0.1)
INPUTS = HouseholdInputs(0.04, 0.02, 0.1, np.array([2.0]), np.array([0.05]), np.array([1.5]))


def _policy(grid, mu_a):
    zeros = np.zeros(grid.shape)
    return PolicySnapshot(
        np.ones(grid.shape), np.zeros(grid.shape + (1,)), zeros, zeros,
        mu_a, zeros, zeros, np.full(grid.shape, "faithful-taper"), zeros, zeros,
        zeros, {}, 0.0, 0.0,
    )


def test_matlab_faithful_illiquid_return_endpoints_and_interior():
    r_a, a_max = 0.04, 2.0
    assert matlab_faithful_illiquid_return(0.0, a_max, r_a) == r_a
    assert np.isclose(matlab_faithful_illiquid_return(1.0, a_max, r_a), r_a * (1.0 - 0.1 * 0.5**9))
    assert np.isclose(matlab_faithful_illiquid_return(a_max, a_max, r_a), 0.9 * r_a)


def test_matlab_faithful_illiquid_return_vector_matches_designated_formula():
    a = np.array([0.25, 0.5, 1.0, 2.0])
    expected = 0.04 * (1.0 - 0.1 * (2.0 / a) ** (-9))
    np.testing.assert_allclose(
        matlab_faithful_illiquid_return(a, 2.0, 0.04),
        expected,
        rtol=0.0,
        atol=np.finfo(float).eps,
    )


@pytest.mark.parametrize(
    ("a", "a_max", "r_a", "message"),
    (
        (np.nan, 2.0, 0.04, "finite"),
        (0.0, 0.0, 0.04, "a_max > 0"),
        (-0.1, 2.0, 0.04, "0 <= a <= a_max"),
        (2.1, 2.0, 0.04, "0 <= a <= a_max"),
    ),
)
def test_matlab_faithful_illiquid_return_rejects_out_of_domain_inputs(a, a_max, r_a, message):
    with pytest.raises(ValueError, match=message):
        matlab_faithful_illiquid_return(a, a_max, r_a)


def test_matlab_faithful_asset_drift_changes_only_illiquid_return_term():
    args = (1.0, -0.5, 1.0, 0.8, np.array([0.4]), 0.2, INPUTS, PARAMS)
    constant_mu_a, constant_mu_b, constant_cost = asset_drifts(*args)
    faithful_mu_a, faithful_mu_b, faithful_cost = asset_drifts_matlab_faithful(*args, a_max=2.0)
    expected_return = float(matlab_faithful_illiquid_return(1.0, 2.0, INPUTS.r_a))
    assert np.isclose(faithful_mu_a, expected_return + 0.2)
    assert not np.isclose(faithful_mu_a, constant_mu_a, rtol=0.0, atol=1e-12)
    assert faithful_mu_b == constant_mu_b
    assert faithful_cost == constant_cost


def test_generator_consumes_faithful_tapered_drift_without_duplicating_taper_logic():
    grid = GridSpec(
        np.array([0.0, 1.0, 2.0]),
        np.array([-1.0, 0.0]),
        np.array([0.5, 1.0, 1.5]),
        -1.0,
    )
    mu_a = np.zeros(grid.shape)
    for i_a, a in enumerate(grid.a):
        transfer = 0.0
        if i_a == grid.a.size - 1:
            transfer = -float(matlab_faithful_illiquid_return(a, grid.a[-1], INPUTS.r_a)) * a
        mu_a[i_a] = asset_drifts_matlab_faithful(
            a, 0.0, 1.0, 1.0, np.array([0.0]), transfer,
            INPUTS, PARAMS, grid.a[-1],
        )[0]

    operator = build_operator(grid, PARAMS, _policy(grid, mu_a), 1e-12)
    selected = (1, 0, 0)
    row = canonical_index(*selected, grid.shape)
    col = canonical_index(2, 0, 0, grid.shape)
    da = grid.a[2] - grid.a[1]
    assert mu_a[selected] > 0.0
    assert np.isclose(operator.g_a[row, col], abs(mu_a[selected]) / da)
    a_values = np.broadcast_to(grid.a[:, None, None], grid.shape)
    np.testing.assert_allclose(
        operator.g_a @ flatten(a_values, grid.shape),
        flatten(mu_a, grid.shape),
        rtol=0.0,
        atol=1e-14,
    )
    np.testing.assert_allclose(np.asarray(operator.g_a.sum(axis=1)).ravel(), 0.0, atol=1e-14)
    generator_source = inspect.getsource(generator_module)
    assert "matlab_faithful_illiquid_return" not in generator_source
    assert "0.1" not in generator_source
