from __future__ import annotations

import numpy as np
import pytest

from validators.multi_province.k1_standalone_hjb_ra_wage_3x3 import finalize, run


def test_exact_grid_and_frozen_configuration() -> None:
    assert run.POINTS == tuple(
        (ra, wage)
        for ra in (0.02, 0.055, 0.09)
        for wage in (0.8, 1.05, 1.3)
    )
    fixture = run.build_fixture(0.055, 1.05)
    assert np.array_equal(fixture.grid.b, np.linspace(-2.0, 5.0, 20))
    assert np.array_equal(fixture.grid.a, np.linspace(0.0, 10.0, 20))
    assert np.array_equal(fixture.grid.z, np.array([0.8, 1.3]))
    assert np.array_equal(
        fixture.grid.switch_matrix,
        np.array([[-1.0 / 3.0, 1.0 / 3.0], [1.0 / 3.0, -1.0 / 3.0]]),
    )
    assert fixture.inputs.r_b == 0.02
    assert fixture.inputs.tau == 0.05
    assert fixture.transfer_income == 0.1
    assert fixture.borrowing_rate_gap == 0.07
    assert fixture.numerics.delta == 1000.0
    assert fixture.numerics.convergence_tolerance == 1e-7
    assert fixture.numerics.max_iterations == 100
    assert fixture.numerics.drift_tolerance == 1e-12


def test_fresh_initial_arrays_and_only_ra_wage_vary() -> None:
    left = run.build_fixture(0.02, 0.8)
    same = run.build_fixture(0.02, 0.8)
    right = run.build_fixture(0.09, 1.3)
    assert left.initial_value is not same.initial_value
    assert left.baseline_labor is not same.baseline_labor
    assert np.array_equal(left.initial_value, same.initial_value)
    assert np.array_equal(left.baseline_labor, same.baseline_labor)
    receipt = run.input_invariance_receipt([left, right])
    assert receipt["varying_fields"] == ["inputs.r_a", "inputs.wages[0]"]
    assert receipt["unexpected_varying_fields"] == []


def test_classification_precedence_and_kfe_condition() -> None:
    assert run.classify_hjb(converged=True, hard_error=None, first_illegal_iteration=3) == (
        "HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX"
    )
    assert run.classify_hjb(converged=False, hard_error=None, first_illegal_iteration=None) == "HJB_NOT_CONVERGED"
    assert run.classify_hjb(converged=True, hard_error=None, first_illegal_iteration=None) == "HJB_CONVERGED"
    assert run.kfe_authorized("HJB_CONVERGED") is True
    assert run.kfe_authorized("HJB_NOT_CONVERGED") is False
    assert run.kfe_authorized("HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX") is False


def test_operator_receipt_uses_matlab_homecrit() -> None:
    legal = run.operator_legality_receipt(np.array([[-1.0, 1.0], [2.0, -2.0]]), iteration=1)
    illegal = run.operator_legality_receipt(np.array([[-1.0, 1.02], [2.0, -2.0]]), iteration=2)
    assert legal["a2max"] == 0.0 and legal["legal"] is True
    assert illegal["a2max"] == 0.020000000000000018 and illegal["legal"] is False
    assert legal["homecrit"] == illegal["homecrit"] == 0.01


def test_marginal_receipt_preserves_mass_and_endpoints() -> None:
    fixture = run.build_fixture(0.055, 1.05)
    density = np.ones((20, 20, 2), dtype=float)
    density /= density.sum() * fixture.db * fixture.da
    receipt = run.distribution_receipt(fixture.grid, density)
    assert receipt["total_mass"] == pytest.approx(1.0)
    assert len(receipt["b_marginal_mass"]) == 20
    assert len(receipt["a_marginal_mass"]) == 20
    assert receipt["boundary_mass_shares"] == pytest.approx({
        "bmin": 0.05, "bmax": 0.05, "amin": 0.05, "amax": 0.05,
    })


def test_forbidden_global_runtime_is_absent_from_runner_source() -> None:
    text = run.Path(run.__file__).read_text(encoding="utf-8")
    for forbidden in (
        "evaluate_firm(", "solve_multi_province", "solve_steady_state(",
        "matlab.engine", "subprocess", "os.system", "warm_start",
    ):
        assert forbidden not in text


def test_quality_labels_are_receipt_driven_and_preserve_ambiguity() -> None:
    high = {
        "distribution": {
            "boundary_mass_shares": {"amin": 0.0, "amax": 0.19},
            "modal_a": [10.0],
        }
    }
    low = {
        "distribution": {
            "boundary_mass_shares": {"amin": 1.0, "amax": 0.0},
            "modal_a": [0.0],
        }
    }
    assert finalize.descriptive_quality_label(high) == "BOUNDARY_CONVERGED_CANDIDATE"
    assert finalize.descriptive_quality_label(low) == "QUALITY_AMBIGUOUS__OWNER_REVIEW_REQUIRED"
