"""Static reexecution gates only; no workbook or scientific solver calls."""
from __future__ import annotations

from validators.multi_province.corrected_2018_three_turn import reexecute


def test_historical_reexecution_is_fail_closed_after_runtime_repair() -> None:
    identity = reexecute.verify_repaired_runner()
    assert identity["passed"] is False
    assert identity["superseded_by_corrected_runtime_contract"] is True
    assert identity["combined_predecessor_write_sites"] == 1
    assert identity["noncolliding_sequencing_guard"] is True
    assert identity["exact_three_turn_guard"] is True


def test_reexecution_verdicts_are_task_exact() -> None:
    assert reexecute.VERDICT_PASS == (
        "CORRECTED_2018_THREE_TURN_REEXEC_PASS__DIRECT_CORRECTED_RATE_TRANSMISSION_OBSERVED")
    assert reexecute.VERDICT_TURN1.endswith("TURN1_REPRODUCTION_MISMATCH")
    assert reexecute.VERDICT_TURN2.endswith("TURN2_REPRODUCTION_MISMATCH")
    assert reexecute.VERDICT_HOUSEHOLD.endswith("HOUSEHOLD_OR_NUMERICAL_BLOCKER")
    assert reexecute.VERDICT_UPSTREAM.endswith("UPSTREAM_STATE_OR_FIRM_BLOCKER")


def test_mismatch_terminal_translation_uses_completed_turn(tmp_path) -> None:
    value = {"verdict": reexecute.MISMATCH_SENTINEL, "error": None}
    turn1 = reexecute._translate_terminal(tmp_path, value)
    assert turn1["verdict"] == reexecute.VERDICT_TURN1
    (tmp_path / "turn2_reproduction.json").write_text("{}", encoding="utf-8")
    turn2 = reexecute._translate_terminal(tmp_path, value)
    assert turn2["verdict"] == reexecute.VERDICT_TURN2
