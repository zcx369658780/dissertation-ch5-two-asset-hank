import math

import numpy as np
import pytest
from scipy import sparse

from ch5_two_asset_hank.corrected_diagnostic import q0_kfe_validation as subject


def test_gamma_is_prospective_binary64_bound():
    eps = np.finfo(float).eps
    assert subject.gamma(864) == 864 * eps / (1.0 - 864 * eps)


def test_peak_resident_memory_probe_returns_positive_bytes():
    assert subject._peak_rss_bytes() > 0


def test_exact_positive_adjacency_uses_no_edge_tolerance():
    q = sparse.csr_matrix(
        np.array([[-1.0, 1.0, 0.0], [0.0, -np.nextafter(0.0, 1.0), np.nextafter(0.0, 1.0)], [2.0, 0.0, -2.0]])
    )
    adjacency = subject._exact_positive_adjacency(q)
    assert adjacency.nnz == 3
    assert adjacency[0, 1] == 1
    assert adjacency[1, 2] == 1
    assert adjacency[2, 0] == 1


def test_exact_positive_adjacency_rejects_negative_offdiagonal():
    q = sparse.csr_matrix(np.array([[1.0, -1.0], [0.0, 0.0]]))
    with pytest.raises(subject.FailClosed, match="NEGATIVE_OFFDIAGONAL"):
        subject._exact_positive_adjacency(q)


def test_null_vector_orientation_and_single_normalization():
    vector = -np.ones(subject.N)
    p, receipt = subject._normalize_null_vector(vector)
    assert receipt["global_sign_reversed"] is True
    assert receipt["normalizations"] == 1
    assert math.fsum(float(value) for value in p) == 1.0
    assert np.all(p > 0.0)


def test_null_vector_sum_must_be_separated_from_zero():
    vector = np.ones(subject.N)
    vector[1::2] = -1.0
    with pytest.raises(subject.FailClosed, match="SUM_NOT_SEPARATED"):
        subject._normalize_null_vector(vector)


def test_rank_receipt_applies_frozen_gamma_864_threshold():
    values = np.linspace(2.0, 1.0, subject.N)
    values[-1] = 0.0
    receipt = subject._rank_receipt(values)
    assert receipt["numerical_rank"] == 799
    assert receipt["numerical_nullity"] == 1
    assert receipt["second_smallest_strictly_above_tau_rank"] is True


def test_rank_receipt_exposes_multiple_nullity_without_retuning():
    values = np.linspace(2.0, 1.0, subject.N)
    values[-2:] = 0.0
    receipt = subject._rank_receipt(values)
    assert receipt["numerical_rank"] == 798
    assert receipt["numerical_nullity"] == 2
    assert receipt["second_smallest_strictly_above_tau_rank"] is False
