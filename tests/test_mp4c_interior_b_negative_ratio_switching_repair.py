from __future__ import annotations

from dataclasses import replace
from pathlib import Path

from ch5_two_asset_hank.corrected_diagnostic.selector import (
    SelectorBudget,
    _interior_a_switching_candidate,
    select_constrained_policy,
)
from validators.multi_province.turn2_f0364_negative_ratio_switching_forensic import (
    run as forensic,
)


REPOSITORY = Path(__file__).resolve().parents[1]


def _f0364():
    _, cell, _ = forensic.load_cell(REPOSITORY)
    budget = SelectorBudget(
        max_selector_evaluations=1,
        max_root_invocations=0,
        max_interior_z_root_invocations=0,
        max_interior_a_switching_root_invocations=0,
        max_joint_switching_root_invocations=0,
    )
    return cell, budget, select_constrained_policy(
        cell, forensic.PARAMETERS, budget=budget
    )


def _negative_backward_pair(result):
    ordinary = [
        candidate
        for candidate in result.candidates
        if candidate.transfer_branch == "negative"
        and candidate.derivative_branches.get("b") == "backward"
        and candidate.derivative_branches.get("a") in {"backward", "forward"}
        and candidate.interior_a_switching_receipt is None
    ]
    return ordinary[0], ordinary[1]


def test_f0364_normal_selector_selects_exact_accepted_switching_policy() -> None:
    _, budget, result = _f0364()
    selected = result.selected

    assert result.outcome == "SELECTED_ADMISSIBLE"
    assert selected is not None
    assert selected.transfer_branch == "negative"
    assert selected.derivative_branches == {"b": "backward", "a": "zero"}
    assert selected.interior_a_switching_receipt is not None
    assert selected.q_b == 0.006091715618507631
    assert selected.q_a == -0.0045978913784868415
    assert selected.d == -7.8384208979658965
    assert selected.g_a == 0.0
    assert selected.g_b == -4.227123020026542
    assert selected.transfer_kkt_residual == 0.0
    assert selected.hamiltonian == -0.11188508398929994
    assert selected.rejection_reasons == ()
    assert selected.admissible is True
    assert budget.root_invocations == 0
    assert budget.interior_a_switching_root_invocations == 0


def test_f0364_forward_switching_candidate_remains_inadmissible() -> None:
    _, _, result = _f0364()
    forward_switching = [
        candidate
        for candidate in result.candidates
        if candidate.transfer_branch == "negative"
        and candidate.derivative_branches == {"b": "forward", "a": "zero"}
    ]
    forward_ordinary = [
        candidate
        for candidate in result.candidates
        if candidate.transfer_branch == "negative"
        and candidate.derivative_branches.get("b") == "forward"
    ]

    assert forward_switching == []
    assert forward_ordinary
    assert all(not candidate.admissible for candidate in forward_ordinary)


def test_negative_ratio_remains_fail_closed_for_active_liquid_face() -> None:
    cell, budget, result = _f0364()
    backward, forward = _negative_backward_pair(result)

    candidate = _interior_a_switching_candidate(
        cell,
        forensic.PARAMETERS,
        {"b": "upper_b"},
        ("upper_b",),
        "negative",
        "backward",
        cell.derivatives.p_b_backward,
        backward,
        forward,
        budget,
    )

    assert candidate is None
    assert budget.root_invocations == 0


def test_zero_ratio_remains_fail_closed() -> None:
    cell, budget, result = _f0364()
    backward, forward = _negative_backward_pair(result)
    zero_ratio_cell = replace(cell, a=1.0, effective_r_a=0.45)

    candidate = _interior_a_switching_candidate(
        zero_ratio_cell,
        forensic.PARAMETERS,
        {},
        (),
        "negative",
        "backward",
        zero_ratio_cell.derivatives.p_b_backward,
        backward,
        forward,
        budget,
    )

    assert candidate is None
    assert budget.root_invocations == 0
