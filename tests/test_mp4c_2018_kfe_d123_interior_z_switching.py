import math

import pytest

from ch5_two_asset_hank.corrected_diagnostic import selector
from ch5_two_asset_hank.corrected_diagnostic.selector import (
    CellDerivatives,
    CorrectedSelectorCell,
    CorrectedSelectorParameters,
    SelectorBudget,
    select_constrained_policy,
)


def _parameters() -> CorrectedSelectorParameters:
    return CorrectedSelectorParameters(
        gamma_c=2.0,
        phi=5.0,
        labor_weight=1.0,
        chi_0=0.1,
        chi_1=2.0,
        a_bar=1.0e-6,
    )


def _cell5(*, b: float = -0.1578947368421053) -> CorrectedSelectorCell:
    return CorrectedSelectorCell(
        cell_id="option-a-cell-5-style",
        b=b,
        a=0.0,
        z=0.8,
        b_lower=-2.0,
        b_upper=5.0,
        a_lower=0.0,
        a_upper=10.0,
        net_wage=12.783312529860462,
        effective_r_b=0.09000000000000001,
        transfer_income=0.1,
        effective_r_a=0.09,
        derivatives=CellDerivatives(
            p_b_backward=0.02256028269097067,
            p_b_forward=0.012481806039037598,
            p_a_backward=-1.687538997430238e-15,
            p_a_forward=-1.687538997430238e-15,
        ),
    )


def _budget() -> SelectorBudget:
    return SelectorBudget(
        max_selector_evaluations=1,
        max_root_invocations=16,
        max_interior_z_root_invocations=8,
    )


def test_cell5_strict_crossing_creates_one_selected_z_candidate() -> None:
    budget = _budget()

    result = select_constrained_policy(_cell5(), _parameters(), budget=budget)

    assert result.outcome == "SELECTED_ADMISSIBLE"
    assert result.selected is not None
    assert result.selected.derivative_branches["b"] == "zero"
    assert result.selected.q_b == pytest.approx(
        0.01250021388291760706054915182349077777, rel=2.0e-15
    )
    assert result.selected.g_b == 0.0
    assert result.selected.c == pytest.approx(result.selected.q_b ** -0.5)
    assert result.selected.l == pytest.approx(
        (result.selected.q_b * _cell5().net_wage) ** 0.2
    )
    assert result.selected.lower_a_zero_kink_multiplier_receipt is not None
    assert (
        result.selected.lower_a_zero_kink_multiplier_receipt.marker
        == "ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_CANONICAL_MIN"
    )
    receipt = result.selected.interior_z_receipt
    assert receipt is not None
    assert receipt.marker == "INTERIOR_LIQUID_Z_ZERO_DRIFT_SWITCH"
    assert receipt.endpoint_shadows == pytest.approx(
        {
            "backward": 0.02256028269097067,
            "forward": 0.012481806039037598,
        }
    )
    assert receipt.endpoint_drifts["backward"] > receipt.endpoint_bounds["backward"]
    assert receipt.endpoint_drifts["forward"] < -receipt.endpoint_bounds["forward"]
    assert receipt.root_bracket == pytest.approx(
        (0.012481806039037598, 0.02256028269097067)
    )
    assert receipt.root_method == "BRENTQ_UNIQUE_LOG_SCREENED_BRACKET"
    assert receipt.root_status == "ROOT_CONVERGED"
    assert abs(receipt.raw_root_residual) <= receipt.arithmetic_bound
    z_candidates = [
        candidate
        for candidate in result.candidates
        if candidate.derivative_branches.get("b") == "zero"
    ]
    assert len(z_candidates) == 4
    assert all(candidate.root_invoked for candidate in z_candidates)
    assert result.interior_z_root_invocations == 4
    assert budget.interior_z_root_invocations == 4


@pytest.mark.parametrize(
    "backward,forward",
    [
        (0.012481806039037598, 0.012481806039037598),
        (0.02256028269097067, 0.02256028269097067),
        (-0.5, 0.012481806039037598),
    ],
)
def test_no_strict_positive_endpoint_crossing_invokes_no_z_root(
    backward: float, forward: float
) -> None:
    cell = _cell5()
    cell = selector.CorrectedSelectorCell(
        **{
            **cell.__dict__,
            "derivatives": CellDerivatives(
                backward,
                forward,
                cell.derivatives.p_a_backward,
                cell.derivatives.p_a_forward,
            ),
        }
    )
    budget = _budget()

    result = select_constrained_policy(cell, _parameters(), budget=budget)

    assert result.interior_z_root_invocations == 0
    assert budget.interior_z_root_invocations == 0
    assert not any(candidate.interior_z_receipt for candidate in result.candidates)


@pytest.mark.parametrize("b", [-2.0, 5.0])
def test_liquid_faces_never_use_interior_z(b: float) -> None:
    budget = _budget()

    result = select_constrained_policy(_cell5(b=b), _parameters(), budget=budget)

    assert result.interior_z_root_invocations == 0
    assert budget.interior_z_root_invocations == 0
    assert not any(candidate.interior_z_receipt for candidate in result.candidates)


def test_endpoint_already_zero_within_prospective_bound_invokes_no_z_root() -> None:
    cell = _cell5()
    cell = selector.CorrectedSelectorCell(
        **{
            **cell.__dict__,
            "derivatives": CellDerivatives(
                cell.derivatives.p_b_backward,
                0.012500213882917607,
                cell.derivatives.p_a_backward,
                cell.derivatives.p_a_forward,
            ),
        }
    )
    budget = _budget()

    result = select_constrained_policy(cell, _parameters(), budget=budget)

    assert result.interior_z_root_invocations == 0
    assert budget.interior_z_root_invocations == 0
    assert not any(candidate.interior_z_receipt for candidate in result.candidates)


def test_interior_z_root_detects_nonunique_root_without_retry() -> None:
    budget = _budget()

    root, status = selector._one_interior_z_root(
        lambda q: (q - 1.25) * (q - 1.5) * (q - 1.75),
        lower=1.0,
        upper=2.0,
        budget=budget,
    )

    assert root is None
    assert status == "ROOT_FAILURE_NO_UNIQUE_BRACKET"
    assert budget.root_invocations == 1
    assert budget.interior_z_root_invocations == 1


def test_interior_z_root_rejects_out_of_interval_result_without_retry(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    budget = _budget()
    monkeypatch.setattr(selector, "brentq", lambda *args, **kwargs: 3.0)

    root, status = selector._one_interior_z_root(
        lambda q: q - 1.5,
        lower=1.0,
        upper=2.0,
        budget=budget,
    )

    assert root is None
    assert status == "ROOT_FAILURE_OUTSIDE_DERIVATIVE_INTERVAL"
    assert budget.root_invocations == 1
    assert budget.interior_z_root_invocations == 1


def test_interior_z_root_function_failure_is_fail_closed_without_retry() -> None:
    budget = _budget()

    def broken(_: float) -> float:
        raise ValueError("synthetic failure")

    root, status = selector._one_interior_z_root(
        broken,
        lower=1.0,
        upper=2.0,
        budget=budget,
    )

    assert root is None
    assert status == "ROOT_FUNCTION_FAILURE:ValueError"
    assert budget.root_invocations == 1
    assert budget.interior_z_root_invocations == 1


def test_z_root_is_not_an_average_or_interpolation() -> None:
    result = select_constrained_policy(_cell5(), _parameters(), budget=_budget())
    assert result.selected is not None
    midpoint = 0.5 * (
        _cell5().derivatives.p_b_backward + _cell5().derivatives.p_b_forward
    )
    assert not math.isclose(result.selected.q_b, midpoint, rel_tol=1.0e-3)
