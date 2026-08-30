import numpy as np
import pytest

from ch5_two_asset_hank.boundaries import check_boundary
from ch5_two_asset_hank.contracts import EconomicParams, HouseholdInputs
from ch5_two_asset_hank.economics import (
    adjustment_cost,
    asset_drifts,
    transfer_candidate,
    transfer_candidate_corrected_max_scale,
)
from ch5_two_asset_hank.policies import _budget_roots


PARAMS = EconomicParams(0.05, 2.0, 1.0, 0.1, 2.0, 0.5, 0.2, 0.1)
INPUTS = HouseholdInputs(0.03, 0.02, 0.1, np.array([2.0]), np.array([0.05]), np.array([1.5]))


def test_adjustment_cost_retains_matlab_denominator_floor():
    assert adjustment_cost(2.0, 0.0, PARAMS) == adjustment_cost(
        2.0, PARAMS.a_bar, PARAMS,
    )


@pytest.mark.parametrize(
    ("a", "expected"),
    ((0.0, 0.0), (0.25, 0.05), (0.5, 0.10)),
)
def test_matlab_faithful_transfer_candidate_uses_bare_a_positive_branch(a, expected):
    assert np.isclose(transfer_candidate(1.5, 1.0, a, PARAMS), expected)


def test_matlab_faithful_transfer_candidate_uses_bare_a_negative_branch():
    assert np.isclose(transfer_candidate(0.5, 1.0, 0.25, PARAMS), -0.05)


@pytest.mark.parametrize("a", (0.0, 0.25))
def test_corrected_max_scale_reference_preserves_historical_foc_evidence(a):
    corrected = transfer_candidate_corrected_max_scale(1.5, 1.0, a, PARAMS)
    faithful = transfer_candidate(1.5, 1.0, a, PARAMS)
    assert np.isclose(corrected, 0.10)
    assert not np.isclose(corrected, faithful)


def test_budget_roots_cover_positive_and_negative_absolute_value_branches():
    for base in (-0.05, 1.0):
        roots = _budget_roots(base, 0.25, PARAMS)
        assert roots
        for root in roots:
            assert np.isclose(base - root - adjustment_cost(root, 0.25, PARAMS), 0.0, atol=1e-12)


def test_budget_has_no_unfrozen_transfer_term_and_boundary_fails_outward():
    mu_a, mu_b, cost = asset_drifts(1.0, -0.5, 1.0, 0.8, np.array([0.4]), 0.2, INPUTS, PARAMS)
    expected_income = 2.0 * (1.0 - 0.1 - 0.05) * 0.4
    assert np.isclose(mu_a, 0.03 + 0.2)
    assert np.isclose(mu_b, 0.02 * -0.5 + expected_income - 0.2 - cost - 0.8)
    assert not check_boundary(0, 0, 3, 3, -1e-3, 0.0, 1e-12).feasible
    assert not check_boundary(2, 2, 3, 3, 0.0, 1e-3, 1e-12).feasible


def test_household_inputs_fail_closed_when_all_effective_wages_are_zero():
    with pytest.raises(ValueError, match="strictly positive effective wage"):
        HouseholdInputs(0.03, 0.02, 0.1, np.array([0.0]), np.array([0.0]), np.array([1.0]))
