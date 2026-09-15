from __future__ import annotations

from pathlib import Path

import pytest

from validators.multi_province.k1_j160_first_turn_six_failure_hjb_mechanism_panel import (
    finalize,
    run,
)
from validators.multi_province.k1_j640_hjb_nonconvergence_mechanism_diagnostic import (
    run as j640,
)


def test_exact_six_failure_authority_is_sealed_and_ordered() -> None:
    receipt = run.load_six_failure_authority()
    rows = receipt["failures"]
    assert receipt["pass"] is True
    assert [(row["province_index"], row["province"]) for row in rows] == [
        (1, "天津"), (3, "山西"), (13, "江西"),
        (21, "重庆"), (23, "贵州"), (27, "甘肃"),
    ]
    assert [row["consumed_r_a"] for row in rows] == pytest.approx(
        [0.06490365475420734, 0.08643576394514026, 0.08911960456738838,
         0.08592885327235546, 0.08979022758512188, 0.09]
    )
    assert all(row["accepted_hjb_classification"] == "HJB_NOT_CONVERGED" for row in rows)
    assert all(row["accepted_iterations"] == 100 for row in rows)
    assert receipt["input_artifact_manifest_match"] is True
    assert receipt["province_receipts_manifest_match"] is True


def test_each_failure_fixture_preserves_frozen_science_and_fresh_initialization() -> None:
    rows = run.load_six_failure_authority()["failures"][:2]
    fixtures = [run.build_fixture(row) for row in rows]
    for row, fixture in zip(rows, fixtures):
        assert (fixture.grid.b.size, fixture.grid.a.size, fixture.grid.z.size) == (20, 160, 2)
        assert fixture.grid.b[[0, -1]] == pytest.approx([-2.0, 20.0])
        assert fixture.grid.a[[0, -1]] == pytest.approx([0.0, 100.0])
        assert fixture.inputs.r_a == pytest.approx(row["consumed_r_a"])
        assert fixture.inputs.r_b == pytest.approx(row["r_b"])
        assert fixture.inputs.wages == pytest.approx([row["household_composite_wage"]])
        assert fixture.numerics.delta == pytest.approx(1000.0)
        assert fixture.numerics.convergence_tolerance == pytest.approx(1e-7)
        assert fixture.numerics.max_iterations == 100
    assert fixtures[0].initial_value is not fixtures[1].initial_value
    assert fixtures[0].baseline_labor is not fixtures[1].baseline_labor


def test_observer_is_the_accepted_j640_observational_methodology() -> None:
    assert run.observe_accepted_hjb is j640.observe_accepted_hjb
    receipt = run.instrumentation_invariance_receipt()
    assert receipt["pass"] is True
    assert receipt["new_hjb_calls"] == 0
    assert receipt["accepted_off_on_exact"] is True
    assert receipt["scientific_control_flow_reads_observations"] is False


def _trace(
    statistics: list[float], *, switch_iterations: set[int] = frozenset(),
    floor_iteration: int | None = None, exact_cycle: bool = False,
) -> dict[str, object]:
    rows = []
    for iteration, statistic in enumerate(statistics, start=1):
        rows.append({
            "iteration": iteration,
            "convergence_statistic": statistic,
            "selector_changes": {
                "liquid": None if iteration == 1 else int(iteration in switch_iterations),
                "transfer": None if iteration == 1 else 0,
            },
            "derivative_floor_hits": {
                "vb_forward": int(floor_iteration is not None and iteration >= floor_iteration),
                "vb_backward": 0,
            },
            "hashes": {
                "value": f"V{iteration}",
                "liquid_labels": f"L{iteration}",
                "transfer_labels": "T",
            },
            "value_period_2_inf": None,
            "value_period_3_inf": None,
            "operator": {"legal": True, "a2max": 0.001},
            "finite_checks": {"value": True},
            "shape_checks": {"value": True},
            "linear_solve_residual_inf": 1e-12,
        })
    return {
        "iterations": rows,
        "first_derivative_floor_hit_iteration": floor_iteration,
        "cycle_evidence": {
            "first_exact_value_recurrence": {"period": 2} if exact_cycle else None,
            "first_exact_joint_label_recurrence": None,
            "exact_value_low_period_2_or_3": exact_cycle,
            "exact_joint_label_low_period_2_or_3": False,
        },
    }


def test_preregistered_classes_distinguish_slow_chatter_floor_cycle_and_reproducibility() -> None:
    slow = run.classify_trace(_trace([10.0, 8.0, 6.0, 4.0]), replay_converged=False)
    chatter = run.classify_trace(
        _trace([10.0, 8.0, 9.0, 7.0, 8.0], switch_iterations={2, 3, 4, 5}, floor_iteration=5),
        replay_converged=False,
    )
    floor = run.classify_trace(
        _trace([10.0, 9.0, 8.0, 9.0, 10.0], switch_iterations={2, 3}, floor_iteration=4),
        replay_converged=False,
    )
    cycle = run.classify_trace(_trace([10.0, 8.0, 9.0], exact_cycle=True), replay_converged=False)
    blocker = run.classify_trace(_trace([10.0, 1e-8]), replay_converged=True)
    assert slow["classification"] == "SLOW_MONOTONE_OR_NEAR_MONOTONE_VALUE_CONVERGENCE"
    assert chatter["classification"] == "POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION"
    assert floor["classification"] == "DERIVATIVE_FLOOR_AMPLIFICATION_AFTER_EARLIER_SWITCHING"
    assert cycle["classification"] == "REPEATING_OR_LOW_PERIOD_CYCLE"
    assert blocker["classification"] == "FAILURE_REPRODUCIBILITY_BLOCKER"


def test_nearest_successful_neighbors_are_offline_and_sorted() -> None:
    receipt = run.nearest_successful_neighbors()
    assert receipt["successful_province_hjb_calls"] == 0
    assert len(receipt["failures"]) == 6
    for failure in receipt["failures"]:
        assert len(failure["nearest_successful_neighbors"]) == 3
        distances = [row["euclidean_distance_raw_ra_w"] for row in failure["nearest_successful_neighbors"]]
        assert distances == sorted(distances)
        assert all(row["accepted_hjb_classification"] == "HJB_CONVERGED" for row in failure["nearest_successful_neighbors"])


def test_panel_classification_and_exact_call_budget() -> None:
    assert finalize.panel_classification(["POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION"] * 6) == "SIX_FAILURES_HOMOGENEOUS_CHATTER"
    assert finalize.panel_classification(["SLOW_MONOTONE_OR_NEAR_MONOTONE_VALUE_CONVERGENCE"] * 6) == "SIX_FAILURES_HOMOGENEOUS_SLOW_CONVERGENCE"
    assert finalize.panel_classification([
        "POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION",
        "SLOW_MONOTONE_OR_NEAR_MONOTONE_VALUE_CONVERGENCE",
    ] * 3) == "SIX_FAILURES_HETEROGENEOUS_MECHANISMS"
    assert finalize.panel_classification(["FAILURE_REPRODUCIBILITY_BLOCKER"] * 6) == "SIX_FAILURES_MECHANISM_UNRESOLVED"
    ledger = run.empty_call_ledger()
    assert ledger["hjb_budget"] == 6
    assert ledger["kfe_budget"] == 0
    assert ledger["successful_province_hjb_budget"] == 0
    assert ledger["scientific_retries"] == 0
    assert all(ledger[key] == 0 for key in run.FORBIDDEN_LEDGER_KEYS)


def test_runner_contains_no_forbidden_scientific_routes() -> None:
    text = Path(run.__file__).read_text(encoding="utf-8")
    for forbidden in (
        "solve_matlab_faithful_stationary_kfe(", "solve_household_steady_state(",
        "matlab.engine", "max_iterations=200", "max_iterations=500",
        "max_iterations=1000", "warm_start=", "damping=", "relaxation=",
    ):
        assert forbidden not in text
