from __future__ import annotations

import numpy as np
import pytest

from validators.multi_province.k1_standalone_hjb_ra_transition_refinement_3x3 import finalize, run


def test_exact_refinement_grid_and_frozen_configuration() -> None:
    assert run.POINTS == tuple(
        (ra, wage)
        for ra in (0.065, 0.0725, 0.08)
        for wage in (0.8, 1.05, 1.3)
    )
    fixture = run.build_fixture(0.0725, 1.05)
    assert np.array_equal(fixture.grid.b, np.linspace(-2.0, 5.0, 20))
    assert np.array_equal(fixture.grid.a, np.linspace(0.0, 10.0, 20))
    assert np.array_equal(fixture.grid.z, np.array([0.8, 1.3]))
    assert fixture.inputs.r_b == 0.02
    assert fixture.inputs.r_a == 0.0725
    assert fixture.inputs.wages[0] == 1.05
    assert fixture.inputs.tau == 0.05
    assert fixture.transfer_income == 0.1
    assert fixture.borrowing_rate_gap == 0.07
    assert fixture.numerics.delta == 1000.0
    assert fixture.numerics.convergence_tolerance == 1e-7
    assert fixture.numerics.max_iterations == 100
    assert fixture.numerics.drift_tolerance == 1e-12


def test_outside_refinement_grid_is_rejected() -> None:
    with pytest.raises(ValueError, match="outside the preregistered refinement grid"):
        run.build_fixture(0.055, 1.05)


def test_only_ra_and_wage_vary_and_initial_arrays_are_fresh() -> None:
    left = run.build_fixture(0.065, 0.8)
    same = run.build_fixture(0.065, 0.8)
    right = run.build_fixture(0.08, 1.3)
    assert left.initial_value is not same.initial_value
    assert left.baseline_labor is not same.baseline_labor
    assert np.array_equal(left.initial_value, same.initial_value)
    assert np.array_equal(left.baseline_labor, same.baseline_labor)
    receipt = run.coarse.input_invariance_receipt([left, right])
    assert receipt["varying_fields"] == ["inputs.r_a", "inputs.wages[0]"]
    assert receipt["unexpected_varying_fields"] == []


def test_illiquid_receipt_reports_interior_mass_and_top_three_bins() -> None:
    a = np.linspace(0.0, 10.0, 20)
    marginal = np.zeros(20)
    marginal[[0, 8, 9, 10, 18, 19]] = [0.05, 0.15, 0.35, 0.20, 0.15, 0.10]
    receipt = run.illiquid_transition_receipt(a, marginal)
    assert receipt["interior_a_mass"] == pytest.approx(0.85)
    assert receipt["top_3_a_bins"] == [
        {"a": float(a[9]), "mass": 0.35, "index_zero_based": 9},
        {"a": float(a[10]), "mass": 0.2, "index_zero_based": 10},
        {"a": float(a[8]), "mass": 0.15, "index_zero_based": 8},
    ]
    assert receipt["amax_to_adjacent_interior_ratio"] == pytest.approx(2.0 / 3.0)


def test_distribution_labels_are_order_based_without_fitted_cutoff() -> None:
    a = np.linspace(0.0, 10.0, 20)
    lower = np.zeros(20); lower[0] = 0.9; lower[1] = 0.1
    interior = np.zeros(20); interior[9] = 0.6; interior[10] = 0.2; interior[0] = 0.1; interior[-1] = 0.1
    upper = np.zeros(20); upper[-1] = 0.55; upper[-2] = 0.45
    mixed = np.zeros(20); mixed[0] = 0.5; mixed[9] = 0.5
    assert finalize.descriptive_distribution_label(a, lower) == "LOWER_A_BOUNDARY_DOMINATED"
    assert finalize.descriptive_distribution_label(a, interior) == "INTERIOR_A_DISTRIBUTION_CANDIDATE"
    assert finalize.descriptive_distribution_label(a, upper) == "UPPER_A_BOUNDARY_PILEUP"
    assert finalize.descriptive_distribution_label(a, mixed) == "TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED"


def test_runner_has_no_forbidden_global_runtime_or_warm_start() -> None:
    text = run.Path(run.__file__).read_text(encoding="utf-8")
    for forbidden in (
        "evaluate_firm(", "solve_multi_province", "solve_steady_state(",
        "matlab.engine", "subprocess", "os.system", "warm_start",
    ):
        assert forbidden not in text
