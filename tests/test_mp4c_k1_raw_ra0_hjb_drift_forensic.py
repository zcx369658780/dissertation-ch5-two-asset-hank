from __future__ import annotations

import numpy as np
import pytest

from validators.multi_province.k1_raw_ra0_hjb_drift_forensic import (
    boundary_label,
    boundary_mask,
    correlation,
    finite_stats,
    safe_ratio,
)


def test_finite_stats_reports_required_distribution_fields() -> None:
    result = finite_stats(np.arange(-2.0, 8.0))
    assert tuple(result) == ("min", "median", "p95", "p99", "max", "abs_max")
    assert result["min"] == -2.0
    assert result["median"] == 2.5
    assert result["abs_max"] == 7.0


def test_finite_stats_fails_closed_on_nonfinite() -> None:
    with pytest.raises(ValueError, match="finite"):
        finite_stats([1.0, np.inf])


@pytest.mark.parametrize(
    ("face", "expected"),
    (("lower_a", (1, 0, 0)), ("upper_a", (1, 2, 0)), ("lower_b", (0, 1, 0)), ("upper_b", (2, 1, 0))),
)
def test_boundary_mask_uses_outward_sign_for_each_face(face: str, expected: tuple[int, int, int]) -> None:
    array = np.zeros((3, 3, 1))
    array[1, 0, 0] = -1.0
    array[1, 2, 0] = 1.0
    array[0, 1, 0] = -1.0
    array[2, 1, 0] = 1.0
    mask = boundary_mask(array, face)
    assert np.argwhere(mask).tolist() == [list(expected)]


def test_boundary_mask_rejects_unknown_face() -> None:
    with pytest.raises(ValueError, match="unknown"):
        boundary_mask(np.zeros((3, 3, 1)), "diagonal")


def test_boundary_label_preserves_corner_faces() -> None:
    assert boundary_label(0, 0) == "lower_b+lower_a"
    assert boundary_label(19, 19) == "upper_b+upper_a"
    assert boundary_label(5, 7) == "interior"


def test_safe_ratio_is_exact_and_zero_denominator_is_unavailable() -> None:
    assert safe_ratio(6.0, 2.0) == 3.0
    assert safe_ratio(1.0, 0.0) is None


def test_correlations_support_pearson_and_tie_aware_spearman() -> None:
    assert correlation([1, 2, 3], [2, 4, 6]) == pytest.approx(1.0)
    assert correlation([1, 1, 2, 3], [4, 4, 6, 9], spearman=True) == pytest.approx(1.0)


def test_correlation_constant_vector_is_unavailable() -> None:
    assert correlation([1, 1, 1], [1, 2, 3]) is None
