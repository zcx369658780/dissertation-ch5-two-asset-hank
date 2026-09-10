"""Zero-science static gates for the GovInv/labor redesign package."""

from __future__ import annotations

import csv
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
REPORT = REPO / "docs/CH5_MP4C_GOVINV_INITIALIZATION_AND_LABOR_NORMALIZATION_REDESIGN_SPEC.md"
ROOT = REPO / "reports/mp4c_govinv_labor_redesign_20260910"


def rows(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(encoding="utf-8-sig", newline="") as stream:
        data = list(csv.DictReader(stream))
    assert all(None not in row for row in data), f"malformed CSV row in {name}"
    return data


def test_govinv_candidates_are_complete_without_a_selected_production_rule() -> None:
    data = rows("govinv_candidate_matrix.csv")
    assert [row["candidate"].split("_", 1)[0] for row in data] == ["G0", "G1", "G2", "G3"]
    assert data[0]["status"] == "BENCHMARK_ONLY__NOT_DEFENSIBLE_AS_MORE_THAN_HISTORICAL_START"
    assert data[1]["status"] == "STRUCTURALLY_COHERENT__IMPLEMENTATION_NOT_AUTHORIZED"
    assert "DATA" in data[3]["status"]


def test_residual_govinv_algebra_preserves_positivity_and_target_accounting() -> None:
    for target, private in ((100.0, 3.0), (100.0, 140.0), (0.0, 0.0)):
        govinv = max(target - private, 0.0)
        assert govinv >= 0.0
        if private <= target:
            assert private + govinv == target
        else:
            assert govinv == 0.0


def test_labor_chain_separates_household_allocation_and_firm_objects() -> None:
    data = rows("labor_object_dimensional_chain.csv")
    objects = {row["object"] for row in data}
    assert {"N", "household_Lt_per_NU", "Lt_mat_NU", "Lt_supply_NU", "firm_Lt_NU"} <= objects
    overwrite = next(row for row in data if row["object"] == "results_Lt_field_overwrite")
    assert overwrite["confirmed_likely_unresolved"] == "CONFIRMED"
    matrix = next(row for row in data if row["object"] == "Lt_mat_NU")
    assert "persisted only in results{31}.Lt_mat" in matrix["consumer"]


def test_column_normalized_static_reference_conserves_national_total() -> None:
    population = [10.0, 30.0]
    kernel = [[1.0, 3.0], [1.0, 1.0]]  # destination rows, origin columns
    shares = [[kernel[j][i] / sum(kernel[k][i] for k in range(2)) for i in range(2)] for j in range(2)]
    destination = [sum(shares[j][i] * population[i] for i in range(2)) for j in range(2)]
    assert abs(sum(destination) - sum(population)) < 1e-12


def test_labor_candidates_keep_l2_unavailable_and_l1_l3_owner_gated() -> None:
    data = {row["candidate"].split("_", 1)[0]: row for row in rows("labor_reference_candidate_matrix.csv")}
    assert data["L1"]["status"] == "OWNER_OR_DATA_DECISION_REQUIRED"
    assert data["L2"]["status"] == "DATA_NOT_AVAILABLE"
    assert data["L3"]["status"] == "OWNER_OR_DATA_DECISION_REQUIRED"


def test_owner_matrix_contains_all_three_evidence_states() -> None:
    statuses = {row["status"] for row in rows("owner_decision_matrix.csv")}
    assert statuses == {"SOURCE_RESOLVED", "OWNER_OR_DATA_DECISION_REQUIRED", "DATA_NOT_AVAILABLE"}


def test_zero_call_ledger_is_strictly_zero_for_every_scientific_counter() -> None:
    ledger = json.loads((ROOT / "zero_scientific_call_ledger.json").read_text(encoding="utf-8"))
    counters = {key: value for key, value in ledger.items() if key.endswith("_calls") or key == "scientific_model_state_advances"}
    assert counters
    assert all(value == 0 for value in counters.values())
    assert ledger["results_eligibility"] is False


def test_controller_note_recovers_clipped_trigger_and_order_without_freezing_damping() -> None:
    text = (ROOT / "govinv_controller_compatibility.md").read_text(encoding="utf-8")
    for token in ("clipped", "ramin + 0.02", "ramax - 0.02", "0.9", "1.1", "tKNratio"):
        assert token in text
    assert "no parameters frozen" in text


def test_joint_sequence_separates_zero_science_from_future_authority() -> None:
    text = (ROOT / "joint_initialization_sequence.md").read_text(encoding="utf-8")
    assert "Zero-science" in text
    assert "Future scientific authorization" in text
    assert "Lref -> Z0 -> initial prices -> optional one-pass private-K observation -> GovInv0" in text


def test_report_answers_all_required_questions_and_stops_before_implementation() -> None:
    text = REPORT.read_text(encoding="utf-8")
    normalized = " ".join(text.split())
    assert "GOVINV_LABOR_REDESIGN_SPEC_PASS__SEPARATE_CAPITAL_AND_LABOR_CORRECTION_PATHS_DEFINED" in text
    assert "## Required answers" in text
    for number in range(1, 9):
        assert f"{number}. **" in text
    assert "does not select or implement a production winner" in normalized
    assert "Results eligibility=FALSE" in text
