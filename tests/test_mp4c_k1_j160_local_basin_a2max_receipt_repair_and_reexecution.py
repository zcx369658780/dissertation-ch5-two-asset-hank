from __future__ import annotations

from validators.multi_province.k1_j160_local_basin_a2max_receipt_repair_and_reexecution import run


def test_scientific_a2max_receipt_excludes_post_convergence_matrix() -> None:
    trace = {
        "iterations": [
            {"iteration": 1, "operator": {"iteration": 1, "a2max": 0.002, "legal": True}},
            {"iteration": 2, "operator": {"iteration": 2, "a2max": 0.003, "legal": True}},
        ],
        "post_convergence_operator": {"iteration": 3, "a2max": 1.5, "legal": False},
    }
    receipt = run.scientific_a2max_receipt(trace, scientific_iteration_count=2)
    assert receipt["scientific_A2max_sequence"] == [0.002, 0.003]
    assert receipt["sequence_length"] == receipt["scientific_iteration_count"] == 2
    assert receipt["max_scientific_A2max"] == 0.003
    assert receipt["max_scientific_A2max_iteration"] == 2
    assert receipt["first_scientific_illegal_iteration"] is None
    assert receipt["scientific_operator_legal"] is True
    assert receipt["receipt_complete"] is True
    assert receipt["post_convergence_system_matrix_metric"]["classification"] == "NOT_SCIENTIFIC_A2MAX"
    assert receipt["post_convergence_system_matrix_metric"]["legality_treatment"] == "EXCLUDED_FROM_LEGALITY"


def test_scientific_a2max_receipt_fails_closed_on_sequence_length() -> None:
    trace = {
        "iterations": [{"iteration": 1, "operator": {"iteration": 1, "a2max": 0.002, "legal": True}}],
        "post_convergence_operator": None,
    }
    receipt = run.scientific_a2max_receipt(trace, scientific_iteration_count=2)
    assert receipt["sequence_length_matches_scientific_iteration_count"] is False
    assert receipt["receipt_complete"] is False
    assert receipt["scientific_operator_legal"] is False


def test_blocked_authority_loads_exact_sealed_points_without_interpolation() -> None:
    authority = run.load_blocked_authority()
    assert authority["pass"] is True
    assert len(authority["points"]) == 12
    assert [point["point_id"] for point in authority["points"][:3]] == [
        "pair01_山西_to_河北_t25",
        "pair01_山西_to_河北_t50",
        "pair01_山西_to_河北_t75",
    ]
    assert authority["points"][0]["consumed_r_a"] == 0.08642883060040293
    assert authority["points"][0]["household_composite_wage"] == 18.182765068872058
    assert authority["points"][10]["hjb_classification"] == "HJB_NOT_CONVERGED"
    assert authority["points"][10]["iterations"] == 100
    assert authority["synthetic_inputs_recomputed"] is False


def test_exact_fixture_construction_retains_twelve_fresh_initializations() -> None:
    authority = run.load_blocked_authority()
    fixtures = run.build_exact_fixtures(authority)
    receipt = run.input_invariance_receipt(authority["points"], fixtures)
    assert len(fixtures) == 12
    assert receipt["pass"] is True
    assert receipt["fresh_initial_value_object_count"] == 12
    assert receipt["fresh_baseline_labor_object_count"] == 12
    assert receipt["all_exact_sealed_ra_w_consumed"] is True


def test_empty_ledger_preserves_exact_budget() -> None:
    ledger = run.empty_call_ledger()
    assert ledger["hjb_budget"] == 12
    assert ledger["hjb_calls_started"] == ledger["hjb_calls_completed"] == 0
    assert ledger["kfe_calls"] == ledger["endpoint_hjb_calls"] == 0
    assert ledger["scientific_retries"] == 0
    assert ledger["engineering_retries_used"] == 1
