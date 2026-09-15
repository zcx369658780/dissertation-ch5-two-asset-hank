from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from validators.multi_province.k1_j640_hjb_nonconvergence_mechanism_diagnostic import (
    finalize,
    run,
)


def test_frozen_j640_fixture_and_numerics() -> None:
    fixture = run.build_fixture()
    assert fixture.grid.b.size == 20
    assert fixture.grid.a.size == 640
    assert fixture.grid.z.size == 2
    assert fixture.grid.b[[0, -1]] == pytest.approx([-2.0, 20.0])
    assert fixture.grid.a[[0, -1]] == pytest.approx([0.0, 100.0])
    assert fixture.inputs.r_b == pytest.approx(0.02)
    assert fixture.inputs.r_a == pytest.approx(0.0675)
    assert fixture.inputs.wages == pytest.approx([15.5])
    assert fixture.numerics.delta == pytest.approx(1000.0)
    assert fixture.numerics.convergence_tolerance == pytest.approx(1e-7)
    assert fixture.numerics.max_iterations == 100
    assert fixture.numerics.drift_tolerance == pytest.approx(1e-12)


def test_observer_returns_the_exact_accepted_solver_result_object(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    sentinel = object()
    original_policy = run.oracle.select_matlab_faithful_local_policy
    original_assembler = run.oracle.assemble_source_operator
    original_spsolve = run.oracle.linalg.spsolve
    monkeypatch.setattr(run.oracle, "solve_matlab_faithful_hjb", lambda *args: sentinel)

    result, trace = run.observe_accepted_hjb(*([None] * 8))

    assert result is sentinel
    assert trace["iterations"] == []
    assert run.oracle.select_matlab_faithful_local_policy is original_policy
    assert run.oracle.assemble_source_operator is original_assembler
    assert run.oracle.linalg.spsolve is original_spsolve


def test_accepted_small_grid_instrumentation_parity_is_reused_without_calls() -> None:
    receipt = json.loads(run.ACCEPTED_PARITY.read_text(encoding="utf-8"))
    assert receipt["status"] == "PASS"
    assert receipt["off_on_exact"] is True
    assert receipt["off_accepted_exact"] is True
    assert receipt["off_iterations"] == receipt["on_iterations"] == 17


def test_cycle_detection_uses_exact_hashes() -> None:
    rows = [
        {"iteration": 1, "hashes": {"value": "A", "liquid_labels": "L1", "transfer_labels": "T1"}},
        {"iteration": 2, "hashes": {"value": "B", "liquid_labels": "L2", "transfer_labels": "T2"}},
        {"iteration": 3, "hashes": {"value": "A", "liquid_labels": "L1", "transfer_labels": "T1"}},
    ]
    result = run.exact_cycle_evidence(rows)
    assert result["first_exact_value_recurrence"] == {"iteration": 3, "prior_iteration": 1, "period": 2}
    assert result["first_exact_joint_label_recurrence"] == {"iteration": 3, "prior_iteration": 1, "period": 2}


def test_runner_has_no_forbidden_runtime_routes() -> None:
    text = Path(run.__file__).read_text(encoding="utf-8")
    for forbidden in (
        "solve_matlab_faithful_stationary_kfe(",
        "solve_household_steady_state(",
        "matlab.engine",
        "max_iterations=200",
        "max_iterations=500",
        "max_iterations=1000",
        "warm_start=",
    ):
        assert forbidden not in text


def _classification_trace(
    statistics: list[float], switch_iteration: int | None, floor_iteration: int | None
) -> dict[str, object]:
    rows = []
    for iteration, statistic in enumerate(statistics, start=1):
        switched = 1 if iteration == switch_iteration else 0
        rows.append(
            {
                "iteration": iteration,
                "convergence_statistic": statistic,
                "selector_changes": {
                    "liquid": None if iteration == 1 else switched,
                    "transfer": None if iteration == 1 else 0,
                },
            }
        )
    return {
        "iterations": rows,
        "first_derivative_floor_hit_iteration": floor_iteration,
        "cycle_evidence": {
            "first_exact_value_recurrence": None,
            "first_exact_joint_label_recurrence": None,
            "exact_value_low_period_2_or_3": False,
            "exact_joint_label_low_period_2_or_3": False,
        },
    }


def test_preregistered_mechanism_classes_distinguish_timing() -> None:
    slow = run.classify_mechanism(_classification_trace([10.0, 8.0, 6.0], None, None), False)
    chatter = run.classify_mechanism(_classification_trace([10.0, 11.0, 9.0], 2, 3), False)
    floor = run.classify_mechanism(_classification_trace([10.0, 9.0, 8.0, 9.0], 2, 4), False)
    assert slow["classification"] == "SLOW_MONOTONE_OR_NEAR_MONOTONE_VALUE_CONVERGENCE"
    assert chatter["classification"] == "POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION"
    assert floor["classification"] == "DERIVATIVE_FLOOR_AMPLIFICATION_AFTER_EARLIER_SWITCHING"


def test_offline_summary_preserves_temporal_and_cycle_boundaries() -> None:
    trace = _classification_trace([10.0, 8.0, 9.0], 2, 3)
    for row in trace["iterations"]:
        row.update(
            {
                "derivative_floor_hits": {"vb_forward": 1, "vb_backward": 1},
                "operator": {"legal": True, "a2max": 0.0},
                "finite_checks": {"value": True},
                "shape_checks": {"value": True},
                "linear_solve_residual_inf": 0.0,
                "value_period_2_inf": None,
                "value_period_3_inf": None,
                "hashes": {"value": str(row["iteration"]), "liquid_labels": "L", "transfer_labels": "T"},
            }
        )
    base = run.classify_mechanism(trace, False)
    summary = finalize.derive_summary(trace, base)
    assert summary["event_ordering"] == [
        ["policy_or_selector_switch", 2],
        ["value_stat_non_decrease", 3],
        ["derivative_floor_hit", 3],
    ]
    assert summary["all_iteration_operators_legal"] is True
    assert summary["exact_low_period_value_cycle"] is False
