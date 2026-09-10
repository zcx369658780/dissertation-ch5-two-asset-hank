import csv
import json
import math
from pathlib import Path

import pytest

from validators.multi_province.steady_state_redesign.contracts import (
    LAMBDA_CANDIDATES,
    alpha_contract,
    damp,
    hysteresis_candidates,
)


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "docs" / "CH5_MP4C_MULTI_PROVINCE_STEADY_STATE_CALIBRATION_AND_INITIALIZATION_REDESIGN_SPEC.md"
OUT = ROOT / "reports" / "mp4c_multi_province_steady_state_redesign_20260910"


def csv_rows(name: str):
    with (OUT / name).open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def test_required_deliverables_exist():
    names = ["source_to_successor_contract.csv", "unit_contract.csv", "initialization_contract.md",
             "update_order_contract.md", "calibration_stage_contract.md", "future_validation_matrix.csv",
             "source_hash_receipt.json", "zero_scientific_call_ledger.json"]
    assert REPORT.is_file()
    assert all((OUT / name).is_file() for name in names)


def test_unit_contract_covers_required_objects_and_exact_bridge():
    rows = csv_rows("unit_contract.csv")
    assert len(rows) == 20
    assert all(None not in row for row in rows)
    objects = {row["object"] for row in rows}
    required = {"Y0", "N/L0", "K0/PIM", "GovInv", "At", "Bt", "Lt", "Ct", "At*N",
                "Kt_supply", "Kt", "Zt", "alpha", "ra", "rah", "rb", "wjt", "w"}
    assert required <= objects
    bridge = next(row for row in rows if row["object"] == "At*N")
    assert "explicit_asset_bridge" in bridge["successor_conversion_or_bridge"]
    assert bridge["classification"] == "FUTURE_VALIDATION_REQUIRED"


def test_current_alpha_is_not_changed():
    raw = 0.7380939146868483
    result = alpha_contract(raw)
    assert result["alpha_raw"] == raw
    assert result["alpha_used"] == raw
    assert result["alpha_clip_flag"] is False
    assert result["alpha_clip_reason"] == "NONE_INSIDE_RANGE"


def test_alpha_synthetic_boundaries():
    assert alpha_contract(0.1)["alpha_used"] == 0.2
    assert alpha_contract(0.9)["alpha_used"] == 0.8
    assert alpha_contract(0.2)["alpha_clip_flag"] is False
    assert alpha_contract(0.8)["alpha_clip_flag"] is False


def test_damping_candidates_are_convex_and_fixed_point_preserving():
    for lam in LAMBDA_CANDIDATES:
        value = damp(2.0, 6.0, lam)
        assert 2.0 <= value <= 6.0
        assert damp(4.0, 4.0, lam) == 4.0
    with pytest.raises(ValueError):
        damp(1.0, 2.0, 0.0)


def test_hysteresis_grid_has_strict_exit_and_is_preregistered():
    grid = hysteresis_candidates()
    assert len(grid) == 9
    assert all(exit_ > enter > 0 and consecutive in {2, 3, 5} for enter, exit_, consecutive in grid)


def test_update_order_clips_aggregates_then_damps():
    text = (OUT / "update_order_contract.md").read_text(encoding="utf-8")
    expected = "firm raw prices → firm clipping/tax compensation → raw cross-province composite prices → composite damping"
    assert expected in text
    assert "damp raw firm price → clip` is rejected" in text


def test_source_receipt_exact_hashes_and_read_only_authority():
    receipt = json.loads((OUT / "source_hash_receipt.json").read_text(encoding="utf-8"))
    assert receipt["read_only"] is True
    assert len(receipt["sources"]) == 10
    by_name = {row["file"]: row["sha256"] for row in receipt["sources"]}
    assert by_name["HANK_mp_1eq.m"] == "ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF"
    assert by_name["load_GDPdata.m"] == "DECA8AF3F22097550B8957FE848989E6342619CB9929A1C00076E020549366C5"


def test_zero_call_ledger_is_complete():
    ledger = json.loads((OUT / "zero_scientific_call_ledger.json").read_text(encoding="utf-8"))
    assert sum(ledger["calls"].values()) == 0
    assert ledger["results_eligible"] is False


def test_report_answers_first_and_retains_partial_boundary():
    text = REPORT.read_text(encoding="utf-8")
    assert text.index("## Required answers") < text.index("## Verdict")
    assert all(f"{i}. **" in text for i in range(1, 12))
    assert "STEADY_STATE_REDESIGN_SPEC_PARTIAL__OWNER_OR_UNIT_DECISION_REMAINS" in text
    assert "Results eligibility=FALSE" in text
