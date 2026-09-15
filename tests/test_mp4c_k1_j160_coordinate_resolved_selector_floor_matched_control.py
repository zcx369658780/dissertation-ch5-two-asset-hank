from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from validators.multi_province.k1_j160_coordinate_resolved_selector_floor_matched_control import (
    finalize,
    run,
)


def test_frozen_panel_order_and_numerics_use_exact_accepted_inputs() -> None:
    rows = run.load_panel_authority()["provinces"]
    assert [(row["province_index"], row["province"]) for row in rows] == [
        (1, "天津"), (13, "江西"), (23, "贵州"), (27, "甘肃"),
        (17, "湖南"), (8, "上海"), (12, "福建"),
    ]
    fixtures = [run.build_fixture(row) for row in rows]
    assert all(fixture.grid.b.size == 20 for fixture in fixtures)
    assert all(fixture.grid.a.size == 160 for fixture in fixtures)
    assert all(fixture.grid.z.size == 2 for fixture in fixtures)
    assert all(fixture.grid.b[[0, -1]] == pytest.approx([-2.0, 20.0]) for fixture in fixtures)
    assert all(fixture.grid.a[[0, -1]] == pytest.approx([0.0, 100.0]) for fixture in fixtures)
    assert all(fixture.numerics.delta == pytest.approx(1000.0) for fixture in fixtures)
    assert all(fixture.numerics.convergence_tolerance == pytest.approx(1e-7) for fixture in fixtures)
    assert all(fixture.numerics.max_iterations == 100 for fixture in fixtures)


def test_panel_input_receipt_uses_sealed_replay_initialization_authority() -> None:
    receipt = run.input_authority_receipt(run.load_panel_authority())
    assert receipt["pass"] is True
    assert receipt["fresh_initial_value_object_count"] == 7
    assert receipt["fresh_baseline_labor_object_count"] == 7
    assert all(item["checks"]["initial_value"] for item in receipt["entries"])
    assert all(item["checks"]["baseline_labor"] for item in receipt["entries"])


def test_engineering_retry_is_only_eligible_for_known_pre_science_receipt_failure() -> None:
    prior = {
        "status": {"status": "FAIL", "science_calls": 0},
        "source_pass": True,
        "instrumentation_pass": True,
        "hjb_calls_started": 0,
        "engineering_retries_used": 0,
        "failed_check_names": {"initial_value", "baseline_labor"},
    }
    assert run.engineering_retry_eligible(prior) is True
    prior["hjb_calls_started"] = 1
    assert run.engineering_retry_eligible(prior) is False


def test_five_spatial_bins_are_fixed_before_science() -> None:
    assert finalize.axis_bin(0, 20) == "exact_lower"
    assert finalize.axis_bin(1, 20) == "near_lower"
    assert finalize.axis_bin(2, 20) == "interior"
    assert finalize.axis_bin(17, 20) == "interior"
    assert finalize.axis_bin(18, 20) == "near_upper"
    assert finalize.axis_bin(19, 20) == "exact_upper"


def test_changed_cell_records_include_coordinates_and_old_new_labels() -> None:
    grid = run.SimpleGrid(
        b=np.array([-2.0, 0.0, 20.0]),
        a=np.array([0.0, 50.0, 100.0]),
        z=np.array([0.8, 1.3]),
    )
    old = np.full((3, 3, 2), "0")
    new = old.copy()
    new[2, 1, 0] = "B"
    records = run.changed_cell_records(new, old, grid)
    assert records == [{
        "index_zero_based": {"b": 2, "a": 1, "z": 0},
        "state": {"b": 20.0, "a": 50.0, "z": 0.8},
        "old_label": "0", "new_label": "B",
    }]
    assert np.array_equal(old, np.full((3, 3, 2), "0"))


def test_floor_records_are_separated_by_raw_derivative_type() -> None:
    grid = run.SimpleGrid(
        b=np.array([-2.0, 0.0, 20.0]),
        a=np.array([0.0, 50.0, 100.0]),
        z=np.array([0.8, 1.3]),
    )
    values = np.full((3, 3, 2), 2.0e-6)
    values[0, 2, 1] = 0.5e-6
    records = run.floor_hit_records(values, grid, floor_type="vb_forward", floor=1.0e-6)
    assert records == [{
        "index_zero_based": {"b": 0, "a": 2, "z": 1},
        "state": {"b": -2.0, "a": 100.0, "z": 1.3},
        "floor_type": "vb_forward", "raw_derivative": 0.5e-6,
    }]


def test_observer_returns_exact_solver_result_and_restores_primitives(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    sentinel = object()
    original_policy = run.oracle.select_matlab_faithful_local_policy
    original_assembler = run.oracle.assemble_source_operator
    original_spsolve = run.oracle.linalg.spsolve
    monkeypatch.setattr(run.oracle, "solve_matlab_faithful_hjb", lambda *args: sentinel)
    result, trace = run.observe_coordinate_hjb(*([None] * 8))
    assert result is sentinel
    assert trace["iterations"] == []
    assert run.oracle.select_matlab_faithful_local_policy is original_policy
    assert run.oracle.assemble_source_operator is original_assembler
    assert run.oracle.linalg.spsolve is original_spsolve


def test_coordinate_summary_reports_axis_and_joint_bins_without_thresholds() -> None:
    records = [
        {"index_zero_based": {"b": 19, "a": 159, "z": 0}},
        {"index_zero_based": {"b": 19, "a": 80, "z": 1}},
        {"index_zero_based": {"b": 10, "a": 80, "z": 1}},
    ]
    summary = finalize.coordinate_summary(records, b_size=20, a_size=160)
    assert summary["b"]["exact_upper"] == 2
    assert summary["a"]["exact_upper"] == 1
    assert summary["joint"]["dual_boundary"] == 1
    assert summary["joint"]["liquid_boundary"] == 1
    assert summary["joint"]["double_interior"] == 1


def test_panel_decision_prioritizes_reproducibility_blocker() -> None:
    comparison = {"evidence_sufficient": True, "upper_specific_all_pairs": True, "matched_overlap_all_pairs": True,
                  "common_other_specific": True, "failure_heterogeneous": True}
    assert finalize.panel_classification([True] * 6 + [False], comparison) == "MATCHED_PANEL_REPRODUCIBILITY_BLOCKER"


@pytest.mark.parametrize(
    ("comparison", "expected"),
    [
        ({"evidence_sufficient": True, "upper_specific_all_pairs": True, "matched_overlap_all_pairs": False,
          "common_other_specific": False, "failure_heterogeneous": False},
         "FAILURE_SPECIFIC_LIQUID_UPPER_BOUNDARY_SELECTOR_FLOOR_CONCENTRATION"),
        ({"evidence_sufficient": True, "upper_specific_all_pairs": False, "matched_overlap_all_pairs": False,
          "common_other_specific": True, "failure_heterogeneous": False},
         "FAILURE_SPECIFIC_OTHER_BOUNDARY_OR_INTERIOR_CONCENTRATION"),
        ({"evidence_sufficient": True, "upper_specific_all_pairs": False, "matched_overlap_all_pairs": True,
          "common_other_specific": False, "failure_heterogeneous": False},
         "FAILURE_CONTROL_FOOTPRINTS_OVERLAP_SUBSTANTIALLY"),
        ({"evidence_sufficient": True, "upper_specific_all_pairs": False, "matched_overlap_all_pairs": False,
          "common_other_specific": False, "failure_heterogeneous": True},
         "HETEROGENEOUS_COORDINATE_RESOLVED_FAILURE_FOOTPRINTS"),
        ({"evidence_sufficient": False, "upper_specific_all_pairs": False, "matched_overlap_all_pairs": False,
          "common_other_specific": False, "failure_heterogeneous": False},
         "COORDINATE_RESOLVED_MECHANISM_UNRESOLVED"),
    ],
)
def test_panel_decision_rules_are_frozen_before_science(comparison: dict[str, bool], expected: str) -> None:
    assert finalize.panel_classification([True] * 7, comparison) == expected


def test_empty_call_ledger_has_exact_budget_and_zero_forbidden_routes() -> None:
    ledger = run.empty_call_ledger()
    assert ledger["hjb_budget"] == 7
    assert ledger["failed_province_hjb_budget"] == 4
    assert ledger["successful_control_hjb_budget"] == 3
    assert ledger["hjb_calls_started"] == 0
    assert ledger["kfe_calls"] == 0
    assert ledger["scientific_retries"] == 0
    assert ledger["engineering_retry_budget"] == 1


def test_runner_contains_no_forbidden_scientific_routes() -> None:
    text = Path(run.__file__).read_text(encoding="utf-8")
    for forbidden in (
        "solve_matlab_faithful_stationary_kfe(", "solve_household_steady_state(",
        "matlab.engine", "max_iterations=200", "max_iterations=500", "warm_start=",
    ):
        assert forbidden not in text


def test_generated_report_contains_type_resolved_and_named_case_interpretations() -> None:
    report = (
        run.REPO / "docs/CH5_MP4C_K1_J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC_REPORT.md"
    ).read_text(encoding="utf-8")
    assert "## Type-resolved selector and floor footprints" in report
    assert "江西 floor hits are primarily double-interior" in report
    assert "天津's mixed value argmax does not imply a mixed selector/floor footprint" in report
    assert "甘肃's upper-b argmax concentration is not mirrored by its selector footprint" in report
    assert "engineering retry=`1/1` before science" in report
