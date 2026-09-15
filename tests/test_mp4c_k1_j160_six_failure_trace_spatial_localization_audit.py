from __future__ import annotations

import pytest

from validators.multi_province.k1_j160_six_failure_trace_spatial_localization_audit import (
    finalize,
)


def test_boundary_band_is_fixed_to_one_index_and_excludes_exact_boundary() -> None:
    assert finalize.axis_zone(0, 20) == "lower_exact"
    assert finalize.axis_zone(1, 20) == "lower_near"
    assert finalize.axis_zone(2, 20) == "interior"
    assert finalize.axis_zone(17, 20) == "interior"
    assert finalize.axis_zone(18, 20) == "upper_near"
    assert finalize.axis_zone(19, 20) == "upper_exact"


def test_boundary_band_rejects_invalid_indices_and_degenerate_grids() -> None:
    with pytest.raises(ValueError, match="size must be at least 5"):
        finalize.axis_zone(0, 4)
    with pytest.raises(ValueError, match="index outside grid"):
        finalize.axis_zone(20, 20)


@pytest.mark.parametrize(
    ("shares", "expected"),
    [
        ({"b_lower_band": 0.80}, "LIQUID_LOWER_BOUNDARY_CONCENTRATED"),
        ({"b_upper_band": 0.81}, "LIQUID_UPPER_BOUNDARY_CONCENTRATED"),
        ({"a_lower_band": 0.95}, "ILLIQUID_LOWER_BOUNDARY_CONCENTRATED"),
        ({"a_upper_band": 1.00}, "ILLIQUID_UPPER_BOUNDARY_CONCENTRATED"),
        (
            {"b_lower_band": 0.80, "a_upper_band": 0.80},
            "MULTI_BOUNDARY_CONCENTRATED",
        ),
        ({"joint_asset_interior": 0.80}, "INTERIOR_CONCENTRATED"),
        ({"b_lower_band": 0.79, "joint_asset_interior": 0.79}, "MIXED_SPATIAL_FOOTPRINT"),
    ],
)
def test_preregistered_value_argmax_label_rules(shares: dict[str, float], expected: str) -> None:
    complete = {
        "b_lower_band": 0.0,
        "b_upper_band": 0.0,
        "a_lower_band": 0.0,
        "a_upper_band": 0.0,
        "joint_asset_interior": 0.0,
    }
    complete.update(shares)
    assert finalize.spatial_label(complete, coordinate_evidence_available=True) == expected


def test_coordinate_evidence_unavailable_fails_closed() -> None:
    assert (
        finalize.spatial_label({}, coordinate_evidence_available=False)
        == "SPATIAL_LOCALIZATION_UNRESOLVED"
    )


def test_selector_and_floor_coordinates_are_not_inferred_from_counts_or_hashes() -> None:
    row = {
        "selector_changes": {"liquid": 4, "transfer": 7},
        "derivative_floor_hits": {"vb_backward": 3, "vb_forward": 2},
        "hashes": {"liquid_labels": "ABC", "transfer_labels": "DEF"},
    }
    availability = finalize.coordinate_availability([row])
    assert availability["selector"] == "COORDINATE_LEVEL_SELECTOR_FOOTPRINT_UNAVAILABLE"
    assert availability["derivative_floor"] == "FLOOR_COORDINATE_LOCALIZATION_UNAVAILABLE"


def test_panel_decision_is_preregistered_and_fail_closed() -> None:
    boundary = ["LIQUID_LOWER_BOUNDARY_CONCENTRATED"] * 6
    interior = ["INTERIOR_CONCENTRATED"] * 6
    mixed = boundary[:5] + ["INTERIOR_CONCENTRATED"]
    unresolved = boundary[:5] + ["SPATIAL_LOCALIZATION_UNRESOLVED"]
    assert finalize.panel_decision(boundary) == "COMMON_BOUNDARY_LOCALIZATION_ACROSS_FAILURES"
    assert finalize.panel_decision(interior) == "COMMON_INTERIOR_LOCALIZATION_ACROSS_FAILURES"
    assert finalize.panel_decision(mixed) == "HETEROGENEOUS_SPATIAL_LOCALIZATION_ACROSS_FAILURES"
    assert finalize.panel_decision(unresolved) == "SPATIAL_LOCALIZATION_EVIDENCE_INSUFFICIENT"


def test_common_signature_threshold_is_total_variation_at_twenty_percent() -> None:
    left = [0.8, 0.0, 0.0, 0.0, 0.2]
    at_limit = [0.6, 0.0, 0.0, 0.0, 0.4]
    above_limit = [0.59, 0.0, 0.0, 0.0, 0.41]
    assert finalize.total_variation(left, at_limit) == pytest.approx(0.20)
    assert finalize.materially_common([left, at_limit]) is True
    assert finalize.materially_common([left, above_limit]) is False


def test_accepted_j640_bom_csv_is_read_as_one_hundred_offline_rows() -> None:
    summary = finalize._j640_summary()
    assert summary["new_j640_runtime"] == 0
    assert summary["value_argmax_spatial_footprint"]["iteration_count"] == 100


def test_source_authority_records_fresh_repository_checks_without_git_runtime() -> None:
    authority = finalize.source_trace_authority()
    checks = authority["repository_state_checks_recorded_from_fresh_preflight"]
    assert authority["pass"] is True
    assert checks == {
        "accepted_candidate_object_is_commit": True,
        "accepted_candidate_parent_match": True,
        "accepted_candidate_is_ancestor_of_actual_baseline": True,
        "accepted_evidence_diff_candidate_to_baseline_is_empty": True,
        "validator_git_calls": 0,
    }


def test_report_states_the_supported_j640_value_argmax_comparison() -> None:
    authority = finalize.source_trace_authority()
    summary = finalize.province_summaries()
    cross = finalize.cross_province_summary(summary)
    panel = {"panel_spatial_classification": finalize.panel_decision([item["spatial_label"] for item in summary["provinces"]])}
    report = finalize._report(authority, summary, cross, panel)
    assert "J640 sealed value-argmax label: `LIQUID_UPPER_BOUNDARY_CONCENTRATED`" in report
