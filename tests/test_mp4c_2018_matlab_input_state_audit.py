from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports/mp4c_2018_matlab_input_data_initial_state_audit_20260910"
CANONICAL = Path(
    r"D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx"
)
EXPECTED_CANONICAL_SHA256 = "AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67"


def load_rows():
    with (REPORT_DIR / "province_comparison_ledger.csv").open(
        "r", encoding="utf-8-sig", newline=""
    ) as fh:
        return list(csv.DictReader(fh))


def test_canonical_identity_and_zero_call_ledger():
    assert hashlib.sha256(CANONICAL.read_bytes()).hexdigest().upper() == EXPECTED_CANONICAL_SHA256
    ledger = json.loads((REPORT_DIR / "call_ledger.json").read_text(encoding="utf-8"))
    assert ledger["scientific_model_calls_total"] == 0
    for key, value in ledger.items():
        if key.endswith("_calls") or key.endswith("_solves"):
            assert value == 0


def test_all_read_source_hashes_match_receipt():
    receipt = json.loads((REPORT_DIR / "source_data_hash_receipt.json").read_text(encoding="utf-8"))
    assert receipt["canonical_match"] is True
    for item in receipt["files"]:
        path = Path(item["path"])
        assert path.stat().st_size == item["size"]
        assert hashlib.sha256(path.read_bytes()).hexdigest().upper() == item["sha256"]


def test_31_province_identity_and_mixed_year_contract():
    rows = load_rows()
    assert len(rows) == 31
    assert len({row["province_name"] for row in rows}) == 31
    assert [int(row["province_index"]) for row in rows] == list(range(1, 32))
    assert {row["MATLAB_level_year"] for row in rows} == {"2009"}
    assert {row["MATLAB_Zt_source_year"] for row in rows} == {"2020"}
    assert {row["MATLAB_PLM_vintage"] for row in rows} == {"19"}
    assert {row["canonical_year"] for row in rows} == {"2018"}


def test_cache_workbook_and_zt_formula_readbacks():
    summary = json.loads((REPORT_DIR / "audit_summary.json").read_text(encoding="utf-8"))
    assert summary["cache_workbook_exact_checks"] == {
        "GDP_2009_after_x1000": 0.0,
        "CAP_2009_after_x1000": 0.0,
        "POP_2009_after_x100": 0.0,
    }
    assert summary["zt_row21_reconstruction_max_abs_diff"] < 1e-15
    assert summary["steady_cache_2018_present"] is False


def test_comparison_classifications_and_missing_markers():
    rows = load_rows()
    assert all(row["GDP_classification"] == "YEAR_OR_VINTAGE_MISMATCH" for row in rows)
    assert all(row["POP_classification"] == "YEAR_OR_VINTAGE_MISMATCH" for row in rows)
    assert all(row["capital_classification"] == "YEAR_OR_VINTAGE_MISMATCH" for row in rows)
    assert all(row["Zt_classification"] == "YEAR_OR_VINTAGE_MISMATCH" for row in rows)
    assert all(row["alpha_classification"] == "EXACT_MATCH" for row in rows)
    assert all(float(row["alpha_diff"]) == 0.0 for row in rows)
    assert all(
        row["corrected_turn1_persisted_Kt_supply"]
        == "NOT_AVAILABLE_WITHOUT_SCIENTIFIC_RERUN"
        for row in rows
    )


def test_anhui_values_and_initial_bound_metadata():
    row = next(row for row in load_rows() if row["province_name"] == "安徽")
    assert row["province_index"] == "12"
    assert row["source_excel_column"] == "N"
    assert float(row["MATLAB_GDP_raw_亿元"]) == 10864.68
    assert float(row["canonical_GDP_raw_亿元"]) == 34010.9
    assert float(row["MATLAB_POP_raw_万人"]) == 6131.0
    assert float(row["canonical_POP_raw_万人"]) == 6076.0
    assert float(row["MATLAB_Zt_fixed_2020_level"]) == 0.000641551386937363
    assert float(row["canonical_same_year_Zt"]) == 0.0006934644495858679
    assert row["initial_ra_at_upper_bound"] == "True"
    assert row["initial_wjt_below_firm_lower_bound"] == "True"


def test_report_answers_required_questions_first():
    report = (ROOT / "docs/CH5_MP4C_2018_MATLAB_INPUT_DATA_AND_INITIAL_STATE_COMPARISON_AUDIT_REPORT.md").read_text(
        encoding="utf-8"
    )
    assert report.startswith("# Chapter 5 MATLAB 2018 input-data")
    assert report.index("## Seven required answers") < report.index("## Authority and identities")
    for number in range(1, 8):
        assert f"{number}. **" in report
    assert "scientific/model calls are exactly 0" in report
