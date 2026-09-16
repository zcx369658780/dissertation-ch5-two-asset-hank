from pathlib import Path

import pytest

from ch5_two_asset_hank.corrected_diagnostic import (
    CellDerivatives,
    CorrectedSelectorCell,
    CorrectedSelectorParameters,
    SelectorBudget,
    bind_preregistered_panel,
    select_constrained_policy,
)


def parameters() -> CorrectedSelectorParameters:
    return CorrectedSelectorParameters(
        gamma_c=2.0,
        phi=5.0,
        labor_weight=1.0,
        chi_0=0.1,
        chi_1=2.0,
        a_bar=0.5,
    )


def interior_cell() -> CorrectedSelectorCell:
    return CorrectedSelectorCell(
        cell_id="synthetic_interior",
        b=0.0,
        a=1.0,
        z=1.0,
        b_lower=-1.0,
        b_upper=1.0,
        a_lower=0.0,
        a_upper=2.0,
        net_wage=1.0,
        effective_r_b=0.0,
        transfer_income=2.0,
        effective_r_a=0.1,
        derivatives=CellDerivatives(
            p_b_backward=1.0,
            p_b_forward=1.0,
            p_a_backward=1.0,
            p_a_forward=1.0,
        ),
    )


def test_preregistered_panel_identity_is_hash_bound_and_unambiguous() -> None:
    repository = Path(__file__).resolve().parents[1]

    panel = bind_preregistered_panel(repository)

    assert len(panel) == 10
    assert [cell.source_row_label for cell in panel] == [
        0,
        19,
        380,
        399,
        400,
        419,
        780,
        799,
        799,
        379,
    ]
    assert [cell.index for cell in panel] == [
        (0, 0, 0),
        (19, 0, 0),
        (0, 19, 0),
        (19, 19, 0),
        (0, 0, 1),
        (19, 0, 1),
        (0, 19, 1),
        (19, 19, 1),
        (19, 19, 1),
        (19, 18, 0),
    ]
    assert [cell.flat_index_f for cell in panel] == [
        0,
        19,
        380,
        399,
        400,
        419,
        780,
        799,
        799,
        379,
    ]
    assert panel[0].source_sha256 == (
        "4EAA6695A07F8C32B42515631D1AF95AD48190990627934D7895EC7EFC9CCE63"
    )
    assert panel[8].source_sha256 == (
        "AA9DB0664FB0476AFA097C9716AAC88EB56F5779EC1A1346EEA27ED406D12FA3"
    )
    assert panel[9].source_sha256 == (
        "81AC0E3F06E8D268C05E4E78B67F64FD6351FC55924282DB4DD44FF99EA77DDA"
    )


def test_synthetic_interior_zero_kink_selects_one_admissible_policy() -> None:
    budget = SelectorBudget(max_selector_evaluations=1, max_root_invocations=12)

    result = select_constrained_policy(interior_cell(), parameters(), budget=budget)

    assert result.outcome == "SELECTED_ADMISSIBLE"
    assert result.selected is not None
    assert result.selected.transfer_branch == "zero_kink"
    assert result.selected.c == pytest.approx(1.0)
    assert result.selected.l == pytest.approx(1.0)
    assert result.selected.d == 0.0
    assert result.selected.g_b == pytest.approx(2.0)
    assert result.selected.g_a == pytest.approx(0.1)
    assert result.selected.d2_assembler_admissible
    assert result.root_invocations == 0
    assert budget.selector_evaluations == 1


def test_synthetic_dual_upper_active_candidate_uses_one_bounded_root() -> None:
    cell = CorrectedSelectorCell(
        cell_id="synthetic_dual_upper",
        b=1.0,
        a=1.0,
        z=1.0,
        b_lower=-1.0,
        b_upper=1.0,
        a_lower=0.0,
        a_upper=1.0,
        net_wage=1.0,
        effective_r_b=0.0,
        transfer_income=0.0,
        effective_r_a=0.1,
        derivatives=CellDerivatives(
            p_b_backward=1.0,
            p_b_forward=2.0,
            p_a_backward=1.0,
            p_a_forward=2.0,
        ),
    )
    budget = SelectorBudget(max_selector_evaluations=1, max_root_invocations=12)

    result = select_constrained_policy(cell, parameters(), budget=budget)

    assert result.outcome == "SELECTED_ADMISSIBLE"
    assert result.selected is not None
    assert result.selected.active_constraints == ("upper_a", "upper_b")
    assert result.selected.transfer_branch == "negative"
    assert result.selected.g_a == pytest.approx(0.0, abs=1e-13)
    assert result.selected.g_b == pytest.approx(0.0, abs=1e-13)
    assert result.selected.multipliers["upper_a"] >= 0.0
    assert result.selected.multipliers["upper_b"] >= 0.0
    assert 1 <= result.root_invocations <= 12


def test_nonpositive_inward_liquid_derivative_fails_without_floor_or_root_retry() -> None:
    cell = CorrectedSelectorCell(
        cell_id="synthetic_invalid_qb",
        b=1.0,
        a=1.0,
        z=1.0,
        b_lower=-1.0,
        b_upper=1.0,
        a_lower=0.0,
        a_upper=2.0,
        net_wage=1.0,
        effective_r_b=0.0,
        transfer_income=0.0,
        effective_r_a=0.1,
        derivatives=CellDerivatives(
            p_b_backward=-0.01,
            p_b_forward=1.0,
            p_a_backward=1.0,
            p_a_forward=1.0,
        ),
    )
    budget = SelectorBudget(max_selector_evaluations=1, max_root_invocations=12)

    result = select_constrained_policy(cell, parameters(), budget=budget)

    assert result.outcome == "NO_ADMISSIBLE_POLICY"
    assert result.selected is None
    assert result.root_invocations == 0
    assert any(
        "q_b" in reason
        for candidate in result.candidates
        for reason in candidate.rejection_reasons
    )


def test_selector_budget_is_fail_closed() -> None:
    budget = SelectorBudget(max_selector_evaluations=1, max_root_invocations=12)
    select_constrained_policy(interior_cell(), parameters(), budget=budget)

    with pytest.raises(RuntimeError, match="selector evaluation budget"):
        select_constrained_policy(interior_cell(), parameters(), budget=budget)
