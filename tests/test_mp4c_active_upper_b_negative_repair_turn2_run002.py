from __future__ import annotations

from pathlib import Path

from validators.multi_province.active_upper_b_negative_repair_turn2_run002.run import (
    predecessor_impact_audit,
)


REPOSITORY = Path(__file__).resolve().parents[1]


def test_predecessor_impact_set_is_empty_in_persisted_compact_receipts() -> None:
    receipt = predecessor_impact_audit(REPOSITORY)
    assert receipt["status"] == "PASS"
    assert receipt["match_count"] == 0
    assert receipt["checkpoint2_f0579_partial_receipt_excluded"] is True
    assert all(row["exact_target_token_file_count"] == 0 for row in receipt["targets"])
    assert all(row["persisted_cell_receipts_scanned"] == 0 for row in receipt["targets"])
