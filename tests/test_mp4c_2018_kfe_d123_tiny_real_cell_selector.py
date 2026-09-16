from pathlib import Path

import numpy as np
import pytest

import ch5_two_asset_hank.corrected_diagnostic.selector as selector_module

from ch5_two_asset_hank.corrected_diagnostic import (
    CellDerivatives,
    ClosedFaceOutwardDriftError,
    CorrectedDiagnosticGrid,
    CorrectedSelectorCell,
    CorrectedSelectorParameters,
    SelectorBudget,
    assemble_consumed_drift_generator,
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


def test_active_upper_b_roundoff_is_recorded_and_canonicalized_to_exact_zero() -> None:
    cell = CorrectedSelectorCell(
        cell_id="synthetic_active_upper_b_roundoff",
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

    result = select_constrained_policy(
        cell,
        parameters(),
        budget=SelectorBudget(max_selector_evaluations=1, max_root_invocations=12),
    )

    assert result.selected is not None
    receipt = result.selected.active_equality_receipts["upper_b"]
    assert 0.0 < receipt.raw_residual <= receipt.arithmetic_bound
    assert receipt.canonical_drift == 0.0
    assert receipt.marker == "ACTIVE_EQUALITY_CANONICAL_ZERO"
    assert result.selected.g_b == 0.0
    assert result.selected.d2_assembler_admissible
    raw_hamiltonian = result.selected.hamiltonian
    for face, equality in result.selected.active_equality_receipts.items():
        axis = "b" if face.endswith("_b") else "a"
        branch = result.selected.derivative_branches[axis]
        derivative = getattr(cell.derivatives, f"p_{axis}_{branch}")
        raw_hamiltonian += derivative * equality.raw_residual
    assert result.selected.raw_hamiltonian == pytest.approx(raw_hamiltonian)


def test_active_upper_a_roundoff_is_recorded_and_canonicalized_to_exact_zero(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    original_controls = selector_module._controls

    def controls_with_upper_a_roundoff(*args: object, **kwargs: object):
        values = original_controls(*args, **kwargs)
        return (*values[:4], np.nextafter(0.0, 1.0), values[5])

    monkeypatch.setattr(selector_module, "_controls", controls_with_upper_a_roundoff)
    cell = CorrectedSelectorCell(
        cell_id="synthetic_active_upper_a_roundoff",
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

    result = select_constrained_policy(
        cell,
        parameters(),
        budget=SelectorBudget(max_selector_evaluations=1, max_root_invocations=12),
    )

    assert result.selected is not None
    receipt = result.selected.active_equality_receipts["upper_a"]
    assert receipt.raw_residual == np.nextafter(0.0, 1.0)
    assert receipt.raw_residual <= receipt.arithmetic_bound
    assert receipt.canonical_drift == 0.0
    assert receipt.marker == "ACTIVE_EQUALITY_CANONICAL_ZERO"
    assert result.selected.g_a == 0.0


def test_active_equality_residual_outside_bound_is_rejected_not_zeroed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    original_controls = selector_module._controls

    def controls_with_material_upper_a_residual(*args: object, **kwargs: object):
        values = original_controls(*args, **kwargs)
        return (*values[:4], 1.0e-6, values[5])

    monkeypatch.setattr(
        selector_module, "_controls", controls_with_material_upper_a_residual
    )
    cell = CorrectedSelectorCell(
        cell_id="synthetic_active_equality_bound_failure",
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

    result = select_constrained_policy(
        cell,
        parameters(),
        budget=SelectorBudget(max_selector_evaluations=1, max_root_invocations=12),
    )

    checked = [
        candidate
        for candidate in result.candidates
        if "upper_a" in candidate.active_equality_receipts
    ]
    assert checked
    assert all(not candidate.admissible for candidate in checked)
    assert all(candidate.g_a == 1.0e-6 for candidate in checked)
    assert all(
        candidate.active_equality_receipts["upper_a"].canonical_drift is None
        for candidate in checked
    )
    assert all(
        candidate.active_equality_receipts["upper_a"].marker
        == "ACTIVE_EQUALITY_BOUND_EXCEEDED"
        for candidate in checked
    )
    assert all(
        "upper_a_ACTIVE_EQUALITY_RESIDUAL" in candidate.rejection_reasons
        for candidate in checked
    )


def test_inactive_upper_face_nextafter_drift_is_not_canonicalized_and_d2_rejects(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    original_controls = selector_module._controls
    outward = np.nextafter(0.0, 1.0)

    def controls_with_tiny_upper_a_outward_drift(*args: object, **kwargs: object):
        values = original_controls(*args, **kwargs)
        return (*values[:4], outward, values[5])

    monkeypatch.setattr(
        selector_module, "_controls", controls_with_tiny_upper_a_outward_drift
    )
    cell = CorrectedSelectorCell(
        cell_id="synthetic_inactive_upper_a_nextafter",
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

    result = select_constrained_policy(
        cell,
        parameters(),
        budget=SelectorBudget(max_selector_evaluations=1, max_root_invocations=12),
    )
    inactive = next(
        candidate
        for candidate in result.candidates
        if candidate.g_a is not None and "upper_a" not in candidate.active_constraints
    )

    assert inactive.g_a == outward
    assert "upper_a" not in inactive.active_equality_receipts
    assert not inactive.d2_assembler_admissible
    grid = CorrectedDiagnosticGrid(
        b=np.array([-1.0, 1.0]),
        a=np.array([0.0, 1.0]),
        z=np.array([1.0]),
    )
    mu_b = np.zeros(grid.shape)
    mu_a = np.zeros(grid.shape)
    mu_a[-1, -1, 0] = inactive.g_a
    with pytest.raises(ClosedFaceOutwardDriftError):
        assemble_consumed_drift_generator(grid, mu_b=mu_b, mu_a=mu_a)


def test_active_lower_a_keeps_economic_boundary_identity() -> None:
    cell = CorrectedSelectorCell(
        cell_id="synthetic_lower_a_identity",
        b=0.0,
        a=0.0,
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

    result = select_constrained_policy(
        cell,
        parameters(),
        budget=SelectorBudget(max_selector_evaluations=1, max_root_invocations=12),
    )
    active_lower = next(
        candidate
        for candidate in result.candidates
        if candidate.admissible and candidate.active_constraints == ("lower_a",)
    )

    assert tuple(active_lower.active_equality_receipts) == ("lower_a",)
    assert active_lower.active_equality_receipts["lower_a"].face == "lower_a"
    assert active_lower.g_a == 0.0


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
