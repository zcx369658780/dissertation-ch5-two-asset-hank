from dataclasses import replace

import pytest

from ch5_two_asset_hank.corrected_diagnostic.selector import (
    CellDerivatives,
    CorrectedSelectorCell,
    CorrectedSelectorParameters,
    SelectorBudget,
    _joint_switching_candidate,
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


def _cell185() -> CorrectedSelectorCell:
    return CorrectedSelectorCell(
        cell_id="v002_f0185_b005_a009_z000_joint_switching",
        b=-0.1578947368421053,
        a=4.7368421052631575,
        z=0.8,
        b_lower=-2.0,
        b_upper=5.0,
        a_lower=0.0,
        a_upper=10.0,
        net_wage=12.783312529860462,
        effective_r_b=0.09000000000000001,
        transfer_income=0.1,
        effective_r_a=0.08998919455428576,
        derivatives=CellDerivatives(
            p_b_backward=0.013362109688537174,
            p_b_forward=0.009574726769001294,
            p_a_backward=0.00857557540065246,
            p_a_forward=0.008489317330830281,
        ),
    )


def _budget() -> SelectorBudget:
    return SelectorBudget(
        max_selector_evaluations=1,
        max_root_invocations=64,
        max_interior_z_root_invocations=16,
        max_interior_a_switching_root_invocations=16,
        max_joint_switching_root_invocations=8,
    )


def _cell100() -> CorrectedSelectorCell:
    return CorrectedSelectorCell(
        cell_id="v002_f0100_b000_a005_z000_one_axis_sufficient",
        b=-2.0,
        a=2.6315789473684212,
        z=0.8,
        b_lower=-2.0,
        b_upper=5.0,
        a_lower=0.0,
        a_upper=10.0,
        net_wage=12.783312529860462,
        effective_r_b=0.09000000000000001,
        transfer_income=0.1,
        effective_r_a=0.08999994552589044,
        derivatives=CellDerivatives(
            p_b_backward=0.012333311206716577,
            p_b_forward=0.012333311206716577,
            p_a_backward=0.00903315440190679,
            p_a_forward=0.008957007194295222,
        ),
    )


def test_cell185_adds_exactly_one_legal_joint_zero_drift_policy() -> None:
    result = select_constrained_policy(_cell185(), _parameters(), budget=_budget())

    joint = [
        candidate
        for candidate in result.candidates
        if candidate.joint_switching_receipt is not None
    ]
    assert len(joint) == 1
    candidate = joint[0]
    receipt = candidate.joint_switching_receipt
    assert receipt is not None
    assert receipt.strict_crossing
    assert receipt.post_liquid_a_drifts == pytest.approx(
        {"backward": 0.009287240997760404, "forward": -0.005170298666228812}
    )
    assert receipt.d_zz == pytest.approx(-0.42626460578345887)
    assert receipt.transfer_regime == "negative"
    assert receipt.d3_ratio == pytest.approx(0.7200216108914285)
    assert receipt.liquid_derivative_interval == pytest.approx(
        (0.009574726769001294, 0.013362109688537174)
    )
    assert receipt.illiquid_derivative_interval == pytest.approx(
        (0.008489317330830281, 0.00857557540065246)
    )
    assert receipt.mapped_q_b_interval == pytest.approx(
        (0.011790364625750628, 0.011910163904713082)
    )
    assert receipt.root_interval == pytest.approx(receipt.mapped_q_b_interval)
    assert receipt.root_endpoint_drifts == pytest.approx(
        (-0.023007467717380714, 0.041147374843733764)
    )
    assert candidate.root_status == "ROOT_CONVERGED"
    assert candidate.q_b is not None
    assert receipt.root_interval[0] < candidate.q_b < receipt.root_interval[1]
    assert candidate.q_a is not None
    assert (
        receipt.illiquid_derivative_interval[0]
        < candidate.q_a
        < receipt.illiquid_derivative_interval[1]
    )
    assert candidate.g_b == 0.0
    assert candidate.g_a == 0.0
    assert candidate.admissible
    assert candidate.d2_assembler_admissible
    assert candidate.transfer_kkt_residual == pytest.approx(0.0, abs=1.0e-15)
    assert result.selected == candidate
    assert result.outcome == "SELECTED_ADMISSIBLE"
    assert result.joint_switching_root_invocations == 1


def test_cell185_joint_candidate_is_not_a_sequential_duplicate() -> None:
    result = select_constrained_policy(_cell185(), _parameters(), budget=_budget())
    joint = [
        candidate
        for candidate in result.candidates
        if candidate.joint_switching_receipt is not None
    ]
    assert len(joint) == 1
    candidate = joint[0]
    assert candidate.interior_z_receipt is None
    assert candidate.interior_a_switching_receipt is None
    assert candidate.derivative_branches == {"b": "zero", "a": "zero"}


def test_joint_fallback_does_not_run_when_one_axis_closure_is_sufficient() -> None:
    result = select_constrained_policy(_cell100(), _parameters(), budget=_budget())
    assert result.outcome == "SELECTED_ADMISSIBLE"
    assert result.selected is not None
    assert result.selected.interior_a_switching_receipt is not None
    assert not any(
        candidate.joint_switching_receipt is not None
        for candidate in result.candidates
    )
    assert result.joint_switching_root_invocations == 0


@pytest.mark.parametrize(
    ("axis", "value"),
    [("b", -2.0), ("b", 5.0), ("a", 0.0), ("a", 10.0)],
)
def test_joint_switching_does_not_trigger_at_asset_boundaries(
    axis: str, value: float
) -> None:
    cell = _cell185()
    boundary = CorrectedSelectorCell(
        **{
            **cell.__dict__,
            "cell_id": f"{axis}-boundary-no-joint-switch",
            axis: value,
        }
    )
    result = select_constrained_policy(boundary, _parameters(), budget=_budget())
    assert not any(
        candidate.joint_switching_receipt is not None
        for candidate in result.candidates
    )
    assert result.joint_switching_root_invocations == 0


def test_joint_switching_never_pairs_liquid_z_receipts_across_regimes() -> None:
    cell = _cell185()
    result = select_constrained_policy(cell, _parameters(), budget=_budget())
    liquid_z = {
        candidate.derivative_branches["a"]: candidate
        for candidate in result.candidates
        if candidate.interior_z_receipt is not None
        and candidate.transfer_branch == "negative"
    }
    cross_regime_forward = replace(liquid_z["forward"], transfer_branch="positive")
    budget = _budget()
    candidate = _joint_switching_candidate(
        cell,
        _parameters(),
        {},
        (),
        "negative",
        liquid_z["backward"],
        cross_regime_forward,
        budget,
    )
    assert candidate is None
    assert budget.joint_switching_root_invocations == 0
