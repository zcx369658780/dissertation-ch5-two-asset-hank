from __future__ import annotations

from dataclasses import replace
import json
from pathlib import Path

import pytest

from ch5_two_asset_hank.corrected_diagnostic.selector import (
    CellDerivatives,
    CorrectedSelectorCell,
    CorrectedSelectorParameters,
    SelectorBudget,
    _interior_a_switching_candidate,
    select_constrained_policy,
)
from validators.multi_province.turn2_f0364_negative_ratio_switching_forensic import run as beijing
from validators.multi_province.k1b_turn4_anhui_f0364_positive_domain_intersection_repair import run as gate


REPOSITORY = Path(__file__).resolve().parents[1]
ANHUI_CELL = Path(
    "reports/ch5_mp4c_k1b_turn4_corrected_household_kfe_and_one_turn_integration_20260921_run001/"
    "household/p11_安徽/checkpoint_004/cell_0364.json"
)
PARAMETERS = CorrectedSelectorParameters(
    gamma_c=2.0,
    phi=5.0,
    labor_weight=1.0,
    chi_0=0.1,
    chi_1=2.0,
    a_bar=1.0e-6,
)


def _budget(roots: int = 0) -> SelectorBudget:
    return SelectorBudget(
        max_selector_evaluations=1,
        max_root_invocations=roots,
        max_interior_z_root_invocations=roots,
        max_interior_a_switching_root_invocations=roots,
        max_joint_switching_root_invocations=roots,
    )


def _anhui_cell() -> CorrectedSelectorCell:
    payload = json.loads((REPOSITORY / ANHUI_CELL).read_text(encoding="utf-8"))
    raw = payload["selector_cell"]
    names = (
        "cell_id", "b", "a", "z", "b_lower", "b_upper", "a_lower",
        "a_upper", "net_wage", "effective_r_b", "transfer_income", "effective_r_a",
    )
    return CorrectedSelectorCell(
        **{name: raw[name] for name in names},
        derivatives=CellDerivatives(**raw["derivatives"]),
    )


def _negative_backward_pair(result):
    rows = [
        row for row in result.candidates
        if row.transfer_branch == "negative"
        and row.derivative_branches.get("b") == "backward"
        and row.derivative_branches.get("a") in {"backward", "forward"}
        and row.interior_a_switching_receipt is None
    ]
    return rows[0], rows[1]


def test_anhui_f0364_selects_unique_exact_backward_switching_candidate() -> None:
    budget = _budget()
    result = select_constrained_policy(_anhui_cell(), PARAMETERS, budget=budget)
    selected = result.selected
    switching = [row for row in result.candidates if row.interior_a_switching_receipt is not None]

    assert result.outcome == "SELECTED_ADMISSIBLE"
    assert selected is not None
    assert switching == [selected]
    assert selected.transfer_branch == "negative"
    assert selected.derivative_branches == {"b": "backward", "a": "zero"}
    assert selected.q_b == 0.0015039676061569449
    assert selected.q_a == -0.0005008835855672058
    assert selected.d == -5.840722762648187
    assert selected.g_a == 0.0
    assert selected.g_b == -17.978717494437753
    assert selected.transfer_kkt_residual == pytest.approx(0.0, abs=2.0e-19)
    assert selected.hamiltonian == -0.06734914681687235
    assert selected.admissible and not selected.rejection_reasons
    assert selected.interior_a_switching_receipt.implied_q_b_interval == (
        -0.000267101992455363,
        0.0016097854371494127,
    )
    assert budget.selector_evaluations == 1
    assert budget.root_invocations == 0


def test_prior_beijing_f0364_remains_bitwise_exact() -> None:
    _, cell, checks = beijing.load_cell(REPOSITORY)
    budget = _budget()
    result = select_constrained_policy(cell, beijing.PARAMETERS, budget=budget)
    selected = result.selected

    assert all(checks.values())
    assert selected is not None
    assert selected.derivative_branches == {"b": "backward", "a": "zero"}
    assert selected.q_b == 0.006091715618507631
    assert selected.q_a == -0.0045978913784868415
    assert selected.d == -7.8384208979658965
    assert selected.g_a == 0.0
    assert selected.g_b == -4.227123020026542
    assert selected.transfer_kkt_residual == 0.0
    assert selected.hamiltonian == -0.11188508398929994
    assert budget.root_invocations == 0


def test_positive_ratio_focused_behavior_is_unchanged() -> None:
    cell = CorrectedSelectorCell(
        cell_id="positive-ratio-existing-authority",
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
    budget = _budget(roots=32)
    result = select_constrained_policy(cell, PARAMETERS, budget=budget)
    selected = result.selected

    assert selected is not None
    assert selected.interior_a_switching_receipt is not None
    assert selected.interior_a_switching_receipt.d3_ratio == pytest.approx(0.72000010894821909)
    assert selected.root_status == "ROOT_CONVERGED"
    assert selected.g_a == selected.g_b == 0.0
    assert selected.admissible
    assert result.interior_a_switching_root_invocations == 1


def test_active_liquid_face_negative_ratio_and_ratio_zero_remain_fail_closed() -> None:
    cell = _anhui_cell()
    result = select_constrained_policy(cell, PARAMETERS, budget=_budget())
    backward, forward = _negative_backward_pair(result)

    active = _interior_a_switching_candidate(
        cell, PARAMETERS, {"b": "upper_b"}, ("upper_b",), "negative",
        "backward", cell.derivatives.p_b_backward, backward, forward, _budget(),
    )
    zero_ratio_cell = replace(cell, a=1.0, effective_r_a=0.45)
    zero = _interior_a_switching_candidate(
        zero_ratio_cell, PARAMETERS, {}, (), "negative", "backward",
        zero_ratio_cell.derivatives.p_b_backward, backward, forward, _budget(),
    )

    assert active is None
    assert zero is None


def test_gate_focused_receipt_and_historical_inventory_are_exact() -> None:
    receipt = gate.focused_parity(REPOSITORY)
    assert receipt["status"] == "PASS"
    assert receipt["selector_evaluations"] == 2
    assert receipt["root_invocations"] == 0
    assert receipt["anhui"]["raw_kkt_residual"] <= 2.0e-19
    assert {
        label: len(gate.inventory(REPOSITORY, root))
        for label, (root, _, _) in gate.MANIFESTS.items()
    } == gate.EXPECTED_MAPS
