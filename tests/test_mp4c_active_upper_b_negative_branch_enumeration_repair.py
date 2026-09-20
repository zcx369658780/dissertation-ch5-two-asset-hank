from __future__ import annotations

from dataclasses import replace
from pathlib import Path

import ch5_two_asset_hank.corrected_diagnostic.selector as selector_module
from ch5_two_asset_hank.corrected_diagnostic.selector import (
    SelectorBudget,
    select_constrained_policy,
)
from validators.multi_province.turn2_f0579_upper_b_negative_branch_forensic import (
    run as forensic,
)


REPOSITORY = Path(__file__).resolve().parents[1]


def _f0579_result():
    _, cell = forensic.load_cell(REPOSITORY)
    budget = SelectorBudget(
        max_selector_evaluations=1,
        max_root_invocations=4,
        max_interior_z_root_invocations=0,
        max_interior_a_switching_root_invocations=0,
        max_joint_switching_root_invocations=0,
    )
    return select_constrained_policy(cell, forensic.PARAMETERS, budget=budget)


def test_f0579_evaluates_both_negative_branches_and_selects_forward() -> None:
    result = _f0579_result()
    negative = [
        candidate
        for candidate in result.candidates
        if candidate.active_constraints == ("upper_b",)
        and candidate.transfer_branch == "negative"
    ]

    assert len(negative) == 2
    backward, forward = negative
    assert backward.derivative_branches == {"b": "backward", "a": "backward"}
    assert backward.root_status == "ROOT_CONVERGED"
    assert backward.rejection_reasons == ("A_DERIVATIVE_DIRECTION_INCONSISTENT",)
    assert not backward.admissible

    assert forward.derivative_branches == {"b": "backward", "a": "forward"}
    assert forward.root_status == "ROOT_CONVERGED"
    assert forward.rejection_reasons == ()
    assert forward.admissible
    assert result.outcome == "SELECTED_ADMISSIBLE"
    assert result.admissible_comparison_count == 1
    assert result.selected is forward


def test_f0579_selected_forward_matches_accepted_forensic_invariants() -> None:
    selected = _f0579_result().selected
    assert selected is not None
    assert selected.q_b == 0.00470259773014529
    assert selected.q_a == -0.0004814219651986697
    assert selected.d == -2.1102602580753396
    assert selected.g_a == 1.6015031989929152
    assert selected.transfer_kkt_residual == 6.505213034913027e-19
    assert selected.hamiltonian == -0.07995936564187259


def test_f0579_other_upper_b_regimes_and_root_budget_are_unchanged() -> None:
    result = _f0579_result()
    zero_kink = next(
        candidate
        for candidate in result.candidates
        if candidate.active_constraints == ("upper_b",)
        and candidate.transfer_branch == "zero_kink"
    )
    positive = next(
        candidate
        for candidate in result.candidates
        if candidate.active_constraints == ("upper_b",)
        and candidate.transfer_branch == "positive"
    )

    assert zero_kink.root_status == "ROOT_FAILURE_NO_UNIQUE_BRACKET"
    assert zero_kink.rejection_reasons == ("ROOT_FAILURE_NO_UNIQUE_BRACKET",)
    assert not zero_kink.admissible
    assert positive.root_status == "ROOT_CONVERGED"
    assert positive.rejection_reasons == (
        "TRANSFER_SIGN_INCONSISTENT_POSITIVE",
        "TRANSFER_KKT_RESIDUAL",
    )
    assert not positive.admissible
    assert result.root_invocations == 4


def test_synthetic_two_admissible_negative_branches_use_post_root_uniqueness(
    monkeypatch,
) -> None:
    _, cell = forensic.load_cell(REPOSITORY)
    original = selector_module._candidate
    shared_hamiltonian = -0.07995936564187259

    def both_admissible(*args, **kwargs):
        candidate = original(*args, **kwargs)
        if (
            candidate.active_constraints == ("upper_b",)
            and candidate.transfer_branch == "negative"
        ):
            return replace(
                candidate,
                admissible=True,
                rejection_reasons=(),
                hamiltonian=shared_hamiltonian,
            )
        return candidate

    monkeypatch.setattr(selector_module, "_candidate", both_admissible)
    budget = SelectorBudget(
        max_selector_evaluations=1,
        max_root_invocations=4,
        max_interior_z_root_invocations=0,
        max_interior_a_switching_root_invocations=0,
        max_joint_switching_root_invocations=0,
    )
    result = select_constrained_policy(cell, forensic.PARAMETERS, budget=budget)

    assert result.outcome == "NO_UNIQUE_ADMISSIBLE_POLICY"
    assert result.selected is None
    assert result.admissible_comparison_count == 2
    assert result.root_invocations == 4
