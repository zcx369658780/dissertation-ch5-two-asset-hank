import math
from pathlib import Path

import numpy as np
import pytest
from scipy import sparse

from ch5_two_asset_hank.corrected_diagnostic import q1_kfe_validation as subject


def test_preflight_binds_exact_q1_artifact_and_d2_construction() -> None:
    receipt = subject.preflight_binding(Path("."))

    assert receipt["q1"]["sha256"] == subject.Q1_SHA256
    assert receipt["accepted_d2_construction"]["diagonal_construction_error"] == 0.0
    assert receipt["accepted_d2_construction"][
        "diagonal_construction_error_exact_zero"
    ] is True
    assert receipt["accepted_topology"]["closed_members"] == [[5, 6, 405, 406]]


def test_secondary_reaggregation_preserves_raw_discrepancy_and_q1_bound() -> None:
    stored_rate = np.nextafter(1.0, 0.0)
    q = sparse.csr_matrix(np.array([[-1.0, stored_rate], [0.0, 0.0]]))

    receipt = subject.secondary_sparse_reaggregation_audit(q)

    assert receipt["maximum_absolute_discrepancy"] == 1.0 - stored_rate
    assert receipt["maximum_absolute_discrepancy"] > 0.0
    assert receipt["bound"] == subject.Q_ONE_BOUND
    assert receipt["discrepancy_was_not_modified_or_zeroed"] is True


def test_null_vector_contract_allows_one_sign_and_one_normalization() -> None:
    vector = -np.ones(subject.N)

    p, receipt = subject.normalize_null_vector(vector)

    assert receipt["global_sign_reversed"] is True
    assert receipt["normalizations"] == 1
    assert math.fsum(float(value) for value in p) == 1.0
    assert np.all(p > 0.0)


def test_null_vector_contract_fails_on_unresolved_zero_sum() -> None:
    vector = np.ones(subject.N)
    vector[1::2] = -1.0

    with pytest.raises(subject.FailClosed, match="SUM_NOT_SEPARATED"):
        subject.normalize_null_vector(vector)


def test_rank_contract_is_fixed_gamma_864_threshold() -> None:
    values = np.linspace(2.0, 1.0, subject.N)
    values[-1] = 0.0

    receipt = subject.rank_receipt(values)

    assert receipt["numerical_rank"] == 799
    assert receipt["numerical_nullity"] == 1
    assert receipt["second_smallest_strictly_above_tau_rank"] is True
