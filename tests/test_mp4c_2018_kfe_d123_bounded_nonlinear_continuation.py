from pathlib import Path

import numpy as np
from scipy import sparse

from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import (
    _verify_accepted_q1_kfe_reuse,
    checkpoint_identity,
    detect_approximate_cycle,
    detect_exact_cycle,
    normwise_backward_error,
    primary_converged,
)


def test_primary_convergence_is_inclusive_and_conjunctive() -> None:
    assert primary_converged(1.0e-8, 1.0e-7)
    assert not primary_converged(np.nextafter(1.0e-8, np.inf), 1.0e-7)
    assert not primary_converged(1.0e-8, np.nextafter(1.0e-7, np.inf))


def test_exact_cycle_ignores_period_one_and_detects_period_two_or_more() -> None:
    identities = ["a", "b", "b"]
    assert detect_exact_cycle(identities) is None

    identities = ["a", "b", "a"]
    assert detect_exact_cycle(identities) == 2

    identities = ["a", "b", "c", "a"]
    assert detect_exact_cycle(identities) == 3


def test_approximate_period_two_requires_complete_two_comparison_window() -> None:
    values = [
        np.array([0.0]),
        np.array([1.0]),
        np.array([5.0e-9]),
        np.array([1.0 + 5.0e-9]),
    ]
    result = detect_approximate_cycle(values, tolerance=1.0e-8)
    assert result is not None
    assert result["period"] == 2
    assert result["comparisons"] == [5.0e-9, 4.999999969612645e-09]

    assert detect_approximate_cycle(values[:3], tolerance=1.0e-8) is None


def test_approximate_period_three_requires_complete_three_comparison_window() -> None:
    values = [
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([4.0e-9]),
        np.array([1.0 + 4.0e-9]),
        np.array([2.0 + 4.0e-9]),
    ]
    result = detect_approximate_cycle(values, tolerance=1.0e-8)
    assert result is not None
    assert result["period"] == 3
    assert all(value <= 1.0e-8 for value in result["comparisons"])


def test_normwise_backward_error_uses_original_equation_scale() -> None:
    matrix = sparse.csr_matrix(np.array([[2.0, 0.0], [0.0, 4.0]]))
    solution = np.array([1.0, 2.0])
    rhs = np.array([2.0, 8.0 + 1.0e-12])

    receipt = normwise_backward_error(matrix, solution, rhs)

    expected_residual = float(np.linalg.norm(matrix @ solution - rhs, ord=np.inf))
    expected_scale = 4.0 * 2.0 + float(np.linalg.norm(rhs, ord=np.inf))
    assert receipt["residual_inf"] == expected_residual
    assert receipt["denominator"] == expected_scale
    assert receipt["normwise_backward_error"] == expected_residual / expected_scale


def test_checkpoint_identity_binds_value_policy_and_q() -> None:
    left = checkpoint_identity("V", "P", {"data": "D", "indices": "I", "indptr": "R"})
    right = checkpoint_identity("V", "P", {"data": "D", "indices": "I", "indptr": "R"})
    changed = checkpoint_identity("V", "P2", {"data": "D", "indices": "I", "indptr": "R"})

    assert left == right
    assert left != changed


def test_accepted_q1_terminal_kfe_evidence_is_complete_for_exact_reuse() -> None:
    repository = Path(__file__).resolve().parents[1]

    receipt = _verify_accepted_q1_kfe_reuse(repository)

    assert receipt["status"] == "PASS"
    assert all(receipt["checks"].values())
    assert receipt["new_kfe_calls"] == 0
