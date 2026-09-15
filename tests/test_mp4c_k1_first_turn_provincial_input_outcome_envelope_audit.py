from __future__ import annotations

import math
import hashlib
import json
from pathlib import Path

import pytest

from validators.multi_province.k1_first_turn_provincial_input_outcome_envelope_audit.build import (
    convex_hull,
    hulls_overlap,
    knn_summary,
    nearest_successes,
    point_in_convex_hull,
    quantile_summary,
    standardize_rows,
    threshold_existence,
)


def test_quantile_summary_uses_linear_interpolation() -> None:
    summary = quantile_summary([1.0, 2.0, 3.0, 4.0])
    assert summary == pytest.approx(
        {"min": 1.0, "q25": 1.75, "median": 2.5, "q75": 3.25, "max": 4.0}
    )


def test_threshold_existence_checks_both_directions() -> None:
    below = threshold_existence([1.0, 2.0], [4.0, 5.0])
    above = threshold_existence([4.0, 5.0], [1.0, 2.0])
    overlap = threshold_existence([1.0, 4.0], [2.0, 5.0])

    assert below["exists"] is True
    assert below["direction"] == "FAILURE_BELOW_SUCCESS"
    assert below["open_interval"] == pytest.approx([2.0, 4.0])
    assert above["exists"] is True
    assert above["direction"] == "FAILURE_ABOVE_SUCCESS"
    assert overlap["exists"] is False
    assert overlap["direction"] is None


def test_standardization_is_full_sample_population_scaling() -> None:
    rows = [
        {"province_index": 0, "province": "A", "outcome_group": "success", "consumed_ra": 1.0, "household_composite_w": 10.0},
        {"province_index": 1, "province": "B", "outcome_group": "failure", "consumed_ra": 2.0, "household_composite_w": 20.0},
        {"province_index": 2, "province": "C", "outcome_group": "success", "consumed_ra": 3.0, "household_composite_w": 30.0},
    ]
    standardized, scaling = standardize_rows(rows)

    assert scaling["ra_mean"] == pytest.approx(2.0)
    assert scaling["w_mean"] == pytest.approx(20.0)
    assert scaling["ra_std_ddof0"] == pytest.approx(math.sqrt(2.0 / 3.0))
    assert standardized[1]["z_ra"] == pytest.approx(0.0)
    assert standardized[1]["z_w"] == pytest.approx(0.0)


def test_nearest_success_ties_break_by_province_index() -> None:
    rows = [
        {"province_index": 0, "province": "S0", "outcome_group": "success", "z_ra": -1.0, "z_w": 0.0},
        {"province_index": 1, "province": "F", "outcome_group": "failure", "z_ra": 0.0, "z_w": 0.0},
        {"province_index": 2, "province": "S2", "outcome_group": "success", "z_ra": 1.0, "z_w": 0.0},
    ]
    nearest = nearest_successes(rows)
    assert nearest[0]["failure_province"] == "F"
    assert nearest[0]["nearest_success_province"] == "S0"
    assert nearest[0]["standardized_distance"] == pytest.approx(1.0)


def test_convex_hull_geometry_handles_boundary_and_disjoint_hulls() -> None:
    square = convex_hull([(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)])
    assert point_in_convex_hull((0.5, 0.5), square) is True
    assert point_in_convex_hull((1.0, 0.5), square) is True
    assert point_in_convex_hull((2.0, 0.5), square) is False
    assert hulls_overlap(square, convex_hull([(0.5, 0.5), (0.6, 0.5), (0.5, 0.6)])) is True
    assert hulls_overlap(square, convex_hull([(2.0, 2.0), (3.0, 2.0), (2.0, 3.0)])) is False


def test_knn_summary_reports_failure_success_interleaving() -> None:
    rows = [
        {"province_index": 0, "province": "F0", "outcome_group": "failure", "z_ra": 0.0, "z_w": 0.0},
        {"province_index": 1, "province": "S1", "outcome_group": "success", "z_ra": 0.1, "z_w": 0.0},
        {"province_index": 2, "province": "F2", "outcome_group": "failure", "z_ra": 0.2, "z_w": 0.0},
        {"province_index": 3, "province": "S3", "outcome_group": "success", "z_ra": 0.3, "z_w": 0.0},
        {"province_index": 4, "province": "S4", "outcome_group": "success", "z_ra": 2.0, "z_w": 0.0},
    ]
    summary = knn_summary(rows, k=3)
    assert summary["classification"] == "FAILURE_SUCCESS_NODES_INTERLEAVED"
    assert summary["failure_induced_connected"] is True
    assert summary["failure_to_success_edge_count"] > 0
    assert all(len(item["neighbors"]) == 3 for item in summary["failure_neighbors"])


def _evidence_root() -> Path:
    return (
        Path(__file__).resolve().parents[1]
        / "docs/evidence/ch5_mp4c_k1_first_turn_provincial_input_outcome_envelope_audit"
    )


def _load(name: str) -> dict:
    return json.loads((_evidence_root() / name).read_text(encoding="utf-8"))


def test_generated_table_preserves_required_semantic_boundaries() -> None:
    table = _load("province_input_outcome_table.json")
    assert table["row_count"] == 31
    assert table["success_count"] == 25
    assert table["failure_count"] == 6
    assert [row["province_index"] for row in table["rows"]] == list(range(31))
    assert all(math.isfinite(row["consumed_ra"]) for row in table["rows"])
    assert all(math.isfinite(row["household_composite_w"]) for row in table["rows"])
    assert all(row["raw_provincial_wjt"] is None for row in table["rows"])
    assert all(row["guarded_wjt"] != row["household_composite_w"] for row in table["rows"])
    assert all(row["raw_pre_guard_return"] == row["consumed_ra"] for row in table["rows"])


def test_generated_decision_and_runtime_match_frozen_scope() -> None:
    decision = _load("panel_decision.json")
    runtime = _load("runtime_ledger.json")
    graph = _load("neighbor_graph_summary.json")
    envelope = _load("envelope_overlap.json")

    assert decision["terminal_class"] == "FAILURE_SUCCESS_INPUT_ENVELOPES_OVERLAP_SUBSTANTIALLY"
    assert decision["simple_provincial_input_envelope_supported"] is False
    assert graph["classification"] == "FAILURE_SUCCESS_NODES_INTERLEAVED"
    assert graph["failure_only_region"] is False
    assert envelope["bounding_box"]["overlap"] is True
    assert envelope["convex_hull"]["hulls_overlap"] is True
    assert envelope["single_variable_thresholds"]["consumed_ra"]["exists"] is False
    assert envelope["single_variable_thresholds"]["household_composite_w"]["exists"] is False
    scientific_keys = [
        "hjb_calls",
        "kfe_calls",
        "firm_calls",
        "wage_mapping_calls",
        "return_mapping_calls",
        "outer_calls",
        "matlab_calls",
        "k1b_calls",
        "k2_calls",
        "ge_calls",
        "downstream_calls",
        "shock_calls",
        "irf_calls",
        "results_writes",
        "scientific_retries",
    ]
    assert all(runtime[key] == 0 for key in scientific_keys)


def test_generated_manifest_seals_every_evidence_file() -> None:
    root = _evidence_root()
    manifest = _load("sealed_manifest_sha256.json")
    sealed = {entry["path"] for entry in manifest["entries"]}
    actual = {path.name for path in root.iterdir() if path.name != "sealed_manifest_sha256.json"}
    assert sealed == actual
    assert sum(entry["bytes"] for entry in manifest["entries"]) == manifest[
        "bytes_excluding_manifest"
    ]
    for entry in manifest["entries"]:
        content = (root / entry["path"]).read_bytes()
        assert len(content) == entry["bytes"]
        assert hashlib.sha256(content).hexdigest().upper() == entry["sha256"]
