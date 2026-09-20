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
    select_constrained_policy,
)


REPOSITORY = Path(__file__).resolve().parents[1]
CELL = REPOSITORY / (
    "reports/ch5_mp4c_interior_b_negative_ratio_repair_turn1_parity_turn2_"
    "run003_20260921/household/p02_河北/checkpoint_001/cell_0005.json"
)
PARAMETERS = CorrectedSelectorParameters(
    gamma_c=2.0,
    phi=5.0,
    labor_weight=1.0,
    chi_0=0.1,
    chi_1=2.0,
    a_bar=1.0e-6,
)


def _cell() -> CorrectedSelectorCell:
    row = json.loads(CELL.read_text(encoding="utf-8"))["selector_cell"]
    derivatives = CellDerivatives(**row.pop("derivatives"))
    return CorrectedSelectorCell(**row, derivatives=derivatives)


def _budget() -> SelectorBudget:
    return SelectorBudget(
        max_selector_evaluations=1,
        max_root_invocations=64,
        max_interior_z_root_invocations=32,
        max_interior_a_switching_root_invocations=32,
        max_joint_switching_root_invocations=32,
    )


def _ordinary_lower_a_zero(result, branch: str):
    rows = [
        candidate
        for candidate in result.candidates
        if candidate.active_constraints == ("lower_a",)
        and candidate.transfer_branch == "zero_kink"
        and candidate.derivative_branches == {"b": branch, "a": "forward"}
        and candidate.interior_z_receipt is None
    ]
    assert len(rows) == 1
    return rows[0]


def test_hebei_f0005_normal_selector_selects_combined_candidate() -> None:
    budget = _budget()
    result = select_constrained_policy(_cell(), PARAMETERS, budget=budget)
    selected = result.selected

    assert result.outcome == "SELECTED_ADMISSIBLE"
    assert selected is not None
    assert selected.active_constraints == ("lower_a",)
    assert selected.transfer_branch == "zero_kink"
    assert selected.derivative_branches == {"b": "zero", "a": "forward"}
    # The accepted forensic decimal root rounds to the first value.  SciPy's
    # frozen 513-point screened Brent path can finish within two binary64 ulps.
    assert selected.q_b == pytest.approx(0.012085132579009488, rel=0.0, abs=2e-17)
    receipt = selected.lower_a_zero_kink_multiplier_receipt
    assert receipt is not None
    assert receipt.raw_kink_interval == pytest.approx(
        (0.01087661932110854, 0.013293645836910438), rel=0.0, abs=4e-18
    )
    assert selected.q_a == pytest.approx(0.01087661932110854, rel=0.0, abs=4e-18)
    assert selected.multipliers["lower_a"] == pytest.approx(
        0.00028489863234105843, rel=0.0, abs=4e-18
    )
    assert selected.d == 0.0
    assert selected.g_a == 0.0
    assert selected.g_b == 0.0
    assert selected.transfer_kkt_residual == 0.0
    assert selected.complementarity_residuals["lower_a"] == 0.0
    assert selected.hamiltonian == pytest.approx(
        -0.1280816705218543, rel=0.0, abs=3e-17
    )
    assert selected.admissible is True
    assert result.interior_z_root_invocations == 4


def test_f0005_ordinary_endpoint_rejections_are_unchanged() -> None:
    result = select_constrained_policy(_cell(), PARAMETERS, budget=_budget())
    backward = _ordinary_lower_a_zero(result, "backward")
    forward = _ordinary_lower_a_zero(result, "forward")

    assert backward.admissible is False
    assert backward.rejection_reasons == ("B_DERIVATIVE_DIRECTION_INCONSISTENT",)
    assert backward.q_b == 0.016103423470140932
    assert backward.q_a == 0.014493081123126838
    assert backward.g_b == 1.7486866578989382
    assert forward.admissible is False
    assert forward.rejection_reasons == (
        "ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERSECTION_EMPTY",
    )
    assert forward.q_b is None
    assert forward.q_a is None
    assert forward.g_b is None


def test_lower_a_composition_invokes_no_z_root_without_strict_crossing() -> None:
    cell = _cell()
    same_shadow = cell.derivatives.p_b_backward
    cell = replace(
        cell,
        derivatives=replace(
            cell.derivatives,
            p_b_forward=same_shadow,
        ),
    )
    budget = _budget()

    result = select_constrained_policy(cell, PARAMETERS, budget=budget)

    assert result.interior_z_root_invocations == 0
    assert budget.interior_z_root_invocations == 0
    assert not any(row.interior_z_receipt for row in result.candidates)


@pytest.mark.parametrize("b", [-2.0, 5.0])
def test_active_liquid_faces_do_not_enter_composition_repair(b: float) -> None:
    cell = replace(_cell(), b=b)
    budget = _budget()

    result = select_constrained_policy(cell, PARAMETERS, budget=budget)

    assert result.interior_z_root_invocations == 0
    assert budget.interior_z_root_invocations == 0
    assert not any(row.interior_z_receipt for row in result.candidates)
