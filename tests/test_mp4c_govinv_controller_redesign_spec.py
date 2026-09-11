"""Zero-science tests for the GovInv controller forensic/specification."""

from __future__ import annotations

import csv
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / "reports/mp4c_govinv_controller_redesign_20260911"
REPORT = REPO / "docs/CH5_MP4C_GOVINV_CONTROLLER_REDESIGN_FORENSIC_AND_SPEC.md"


def csv_rows(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert rows and all(None not in row for row in rows)
    return rows


def test_c0_formula_replays_all_accepted_actions_exactly() -> None:
    rows = csv_rows("g1_static_directional_forensic.csv")
    assert len(rows) == 775
    assert all(row["c0_replay_exact"] == "True" for row in rows)
    assert all(row["recorded_c0_action"] == row["replayed_c0_action"] for row in rows)


def test_directional_counts_match_required_windows() -> None:
    summary = json.loads((ROOT / "controller_direction_summary.json").read_text(encoding="utf-8"))
    assert summary["c0_formula_replay_mismatches"] == 0
    got = {row["window"]: row["worsening_count"] for row in summary["windows"]}
    assert got == {
        "ALL_TURNS_01_25": 258,
        "TURNS_01_05": 0,
        "TURNS_06_10": 92,
        "TURNS_11_15": 56,
        "TURNS_16_20": 73,
        "TURNS_21_25": 37,
    }


def test_every_worsening_case_is_above_target_high_ra_increase() -> None:
    rows = csv_rows("g1_static_directional_forensic.csv")
    worsening = [row for row in rows if row["c0_capital_gap_direction"] == "CAPITAL_GAP_WORSENING_DIRECTION"]
    assert len(worsening) == 258
    assert all(row["capital_position"] == "ABOVE_TARGET" for row in worsening)
    assert all(row["recorded_c0_action"] == "HIGH_RA_INCREASE_1P1" for row in worsening)


def test_candidate_matrix_has_four_separate_families_and_no_fitted_parameter() -> None:
    rows = csv_rows("controller_candidate_matrix.csv")
    assert [row["candidate"].split("_", 1)[0] for row in rows] == ["C0", "C1", "C2", "C3"]
    assert rows[0]["Ktarget_direct"] == "NO"
    assert rows[1]["Ktarget_direct"] == "YES"
    assert "lambda_K" in rows[1]["tuning_degrees_of_freedom"]
    assert "NOT_REPLAYED" in rows[2]["expected_response_to_accepted_g1"]
    assert "MOST_UNVERIFIED_TUNING" in rows[3]["status"]


def test_c1_static_geometry_preserves_positivity_and_gap_sign() -> None:
    for target, private, govinv in ((100.0, 3.0, 97.0), (100.0, 3.0, 150.0), (100.0, 140.0, 0.0)):
        gap = target - (private + govinv)
        replacement = max(govinv + gap, 0.0)  # lambda_K=1 geometry only
        assert replacement >= 0.0
        if target >= private:
            assert private + replacement == target
        else:
            assert replacement == 0.0


def test_source_map_recovers_exact_order_signal_and_gate() -> None:
    text = (ROOT / "controller_source_timing_map.md").read_text(encoding="utf-8")
    for token in ("max(abs(KNratio/tKNratio-1))<0.1", "clipped", "Zt", "ramin+0.02", "ramax-0.02", "GovInv*=0.9", "GovInv*=1.1", "0.6*KNratio_current+0.4*tKNratio_old"):
        assert token in text
    assert "No C0 expression reads `Ktarget`" in text


def test_owner_matrix_keeps_scientific_choices_open() -> None:
    rows = csv_rows("owner_decision_matrix.csv")
    decisions = {row["decision"] for row in rows}
    assert {"GovInv economic meaning", "primary controller objective", "return signal", "damping and hysteresis", "same-turn Zt and GovInv", "Ktarget reference during iteration", "public-capital data"} <= decisions
    assert any(row["status"] == "DATA_NOT_AVAILABLE" for row in rows)
    assert sum(row["status"] == "OWNER_DECISION_REQUIRED" for row in rows) >= 7


def test_zero_scientific_call_ledger_is_strictly_zero() -> None:
    ledger = json.loads((ROOT / "zero_scientific_call_ledger.json").read_text(encoding="utf-8"))
    counters = {key: value for key, value in ledger.items() if key.endswith("_calls") or key == "scientific_model_state_advances"}
    assert counters and all(value == 0 for value in counters.values())
    assert ledger["results_eligibility"] is False


def test_report_answers_all_questions_and_stops_at_reviewer_gate() -> None:
    text = REPORT.read_text(encoding="utf-8")
    assert "GOVINV_CONTROLLER_REDESIGN_SPEC_PASS__HISTORICAL_CONTROLLER_FAILURE_MECHANISM_QUANTIFIED_AND_CANDIDATES_SEPARATED" in text
    for number in range(1, 9):
        assert f"{number}. **" in text
    assert "does not publish that successor" in text
    assert "Results eligibility=FALSE" in text
