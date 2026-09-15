from __future__ import annotations

import pytest

from validators.multi_province.k1_j160_first_turn_local_basin_interpolation_diagnostic import run


def test_pair_authority_and_probe_fixture_invariance() -> None:
    authority = run.load_pair_authority()
    assert authority["pass"] is True
    assert [(item["failure"]["province"], item["success"]["province"]) for item in authority["pairs"]] == [
        ("山西", "河北"), ("重庆", "河北"), ("江西", "安徽"), ("贵州", "四川"),
    ]
    assert all(item["non_interpolated_inputs_exact"] for item in authority["pairs"])

    points, fixtures = run.build_probe_fixtures(authority)
    receipt = run.input_invariance_receipt(points, fixtures)
    assert len(points) == len(fixtures) == 12
    assert [item["t"] for item in points] == [0.25, 0.5, 0.75] * 4
    assert receipt["pass"] is True
    assert receipt["varying_fields"] == ["inputs.r_a", "inputs.wages[0]"]
    assert receipt["fresh_initial_value_object_count"] == 12
    assert receipt["fresh_baseline_labor_object_count"] == 12


@pytest.mark.parametrize(
    ("interior", "expected"),
    [
        ([True, True, True], "ALL_INTERIOR_PROBES_CONVERGE"),
        ([False, False, False], "ALL_INTERIOR_PROBES_FAIL"),
        ([False, False, True], "SINGLE_TRANSITION_FAILURE_TO_SUCCESS"),
        ([False, True, True], "SINGLE_TRANSITION_FAILURE_TO_SUCCESS"),
        ([True, False, True], "NONMONOTONE_OR_INTERLEAVED_LOCAL_BASIN"),
    ],
)
def test_pair_classification(interior: list[bool], expected: str) -> None:
    outcomes = [{"converged": value, "numerically_valid": True} for value in interior]
    assert run.pair_classification(outcomes) == expected


def test_numerical_invalidity_has_pair_precedence() -> None:
    outcomes = [
        {"converged": False, "numerically_valid": True},
        {"converged": False, "numerically_valid": False},
        {"converged": True, "numerically_valid": True},
    ]
    assert run.pair_classification(outcomes) == "PAIR_NUMERICAL_INVALIDITY_BLOCKER"


def test_panel_classification_precedence() -> None:
    simple = [
        "ALL_INTERIOR_PROBES_CONVERGE",
        "SINGLE_TRANSITION_FAILURE_TO_SUCCESS",
        "ALL_INTERIOR_PROBES_FAIL",
        "SINGLE_TRANSITION_FAILURE_TO_SUCCESS",
    ]
    assert run.panel_classification(simple) == "LOCAL_BASIN_BOUNDARIES_SIMPLE_AND_PAIR_SPECIFIC"
    assert run.panel_classification(simple[:3] + ["NONMONOTONE_OR_INTERLEAVED_LOCAL_BASIN"]) == (
        "LOCAL_BASIN_TOPOLOGY_HETEROGENEOUS_OR_INTERLEAVED"
    )
    assert run.panel_classification(simple[:3] + ["PAIR_NUMERICAL_INVALIDITY_BLOCKER"]) == (
        "LOCAL_BASIN_EVIDENCE_NUMERICALLY_BLOCKED"
    )


def test_empty_ledger_is_exactly_bounded() -> None:
    ledger = run.empty_call_ledger()
    assert ledger["hjb_budget"] == 12
    assert ledger["hjb_calls_started"] == ledger["hjb_calls_completed"] == 0
    assert ledger["kfe_calls"] == 0
    assert ledger["endpoint_hjb_calls"] == 0
    assert ledger["scientific_retries"] == 0


def test_scientific_operator_gate_excludes_post_convergence_system_matrix() -> None:
    trace = {
        "iterations": [{"operator": {"iteration": 1, "a2max": 0.002, "legal": True}}],
        "post_convergence_operator": {"iteration": 2, "a2max": 1.5, "legal": False},
    }
    receipt = run.scientific_operator_gate(trace)
    assert receipt["maximum_a2max"] == 0.002
    assert receipt["all_iteration_operators_legal"] is True
    assert receipt["first_illegal_iteration"] is None
    assert receipt["post_convergence_system_matrix_excluded_from_generator_gate"] is True
