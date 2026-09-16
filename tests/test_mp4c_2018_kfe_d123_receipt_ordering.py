import json

import pytest

from ch5_two_asset_hank.corrected_diagnostic import run_panel
from ch5_two_asset_hank.corrected_diagnostic.panel import BoundPanelCell
from ch5_two_asset_hank.corrected_diagnostic.selector import (
    CellDerivatives,
    CorrectedSelectorCell,
    CorrectedSelectorParameters,
    SelectorBudget,
    SelectorCandidate,
    SelectorResult,
)


def _cell() -> BoundPanelCell:
    selector_cell = CorrectedSelectorCell(
        cell_id="forced-d2-failure",
        b=1.0,
        a=1.0,
        z=1.0,
        b_lower=0.0,
        b_upper=1.0,
        a_lower=0.0,
        a_upper=1.0,
        net_wage=1.0,
        effective_r_b=0.0,
        transfer_income=0.0,
        effective_r_a=0.0,
        derivatives=CellDerivatives(1.0, 1.0, 1.0, 1.0),
    )
    return BoundPanelCell(
        panel_id="forced_d2_failure",
        source_snapshot_id="synthetic",
        source_path="synthetic.npz",
        source_sha256="A" * 64,
        source_bytes=1,
        source_row_label=1,
        index=(1, 1, 0),
        flat_index_f=3,
        scalar_binding_path="binding.json",
        scalar_binding_sha256="B" * 64,
        scalar_binding_bytes=2,
        grid_b=(0.0, 1.0),
        grid_a=(0.0, 1.0),
        grid_z=(1.0,),
        selector_cell=selector_cell,
        selector_parameters=CorrectedSelectorParameters(2.0, 1.0, 1.0, 0.0, 1.0, 1.0),
        bound_inputs={"raw": 7.0},
    )


def _result() -> SelectorResult:
    selected = SelectorCandidate(
        active_constraints=("upper_b",),
        transfer_branch="zero_kink",
        derivative_branches={"b": "backward", "a": "backward"},
        admissible=True,
        rejection_reasons=(),
        root_invoked=False,
        root_status="NOT_REQUIRED",
        g_b=0.0,
        g_a=0.0,
    )
    rejected = SelectorCandidate(
        active_constraints=(),
        transfer_branch="positive",
        derivative_branches={"b": "forward", "a": "forward"},
        admissible=False,
        rejection_reasons=("synthetic rejection",),
        root_invoked=False,
        root_status="NOT_REQUIRED",
    )
    return SelectorResult(
        cell_id="forced-d2-failure",
        outcome="SELECTED_ADMISSIBLE",
        selected=selected,
        candidates=(selected, rejected),
        admissible_comparison_count=1,
        face_active_set_count=1,
        regime_attempt_count=2,
        root_invocations=0,
        selector_evaluation_ordinal=1,
    )


def test_forced_d2_failure_preserves_complete_selector_receipt_before_check(
    tmp_path, monkeypatch
) -> None:
    cell = _cell()
    result = _result()
    budget = SelectorBudget(10, 120, selector_evaluations=1, root_invocations=0)
    freeze_identity = {
        "authority_id": "synthetic-authority",
        "git_head_before_first_real_selector_call": "C" * 40,
        "scientific_code_sha256_before_first_real_selector_call": {
            "src/example.py": "D" * 64
        },
    }
    receipt_path = tmp_path / "cell_01_forced_d2_failure.json"

    def forced_d2_failure(actual_cell, actual_result):
        assert actual_cell is cell
        assert actual_result is result
        durable = json.loads(receipt_path.read_text(encoding="utf-8"))
        assert durable["selector_result"]["candidates"] == [
            json.loads(json.dumps(run_panel.asdict(candidate)))
            for candidate in result.candidates
        ]
        assert durable["cumulative_selector_evaluations"] == 1
        assert durable["cumulative_scalar_root_invocations"] == 0
        assert durable["panel_identity"]["panel_id"] == cell.panel_id
        assert durable["code_freeze_identity"] == freeze_identity
        assert (
            durable["receipt_persistence_order"]
            == "SELECTOR_RECEIPT_DURABLE_BEFORE_D2"
        )
        assert durable["d2_assembler_check"]["status"] == "PENDING"
        assert all(durable["budget_postconditions"].values())
        raise ValueError("forced strict D2 rejection")

    monkeypatch.setattr(run_panel, "_d2_check", forced_d2_failure)

    with pytest.raises(ValueError, match="forced strict D2 rejection"):
        run_panel.persist_selector_receipt_then_check_d2(
            tmp_path,
            ordinal=1,
            cell=cell,
            result=result,
            budget=budget,
            code_freeze_identity=freeze_identity,
        )

    durable = json.loads(receipt_path.read_text(encoding="utf-8"))
    assert len(durable["selector_result"]["candidates"]) == 2
    assert durable["selector_result"]["selected"] is not None
    assert durable["d2_assembler_check"] == {
        "status": "D2_ASSEMBLER_RAISED",
        "exception_type": "ValueError",
        "exception_message": "forced strict D2 rejection",
    }
