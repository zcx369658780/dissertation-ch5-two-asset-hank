import math
from pathlib import Path

import numpy as np
import pytest
from scipy import sparse

from ch5_two_asset_hank.corrected_diagnostic import checkpoint11_kfe_validation as subject


def test_preflight_binds_exact_checkpoint11_without_sparse_q_load(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def forbidden_load(*args: object, **kwargs: object) -> object:
        raise AssertionError("preflight must not sparse-load Q11")

    monkeypatch.setattr(sparse, "load_npz", forbidden_load)
    receipt = subject.preflight_binding(Path("."))

    assert receipt["accepted_manifest"]["sha256"] == subject.ACCEPTED_MANIFEST_SHA256
    assert receipt["accepted_manifest"]["entry_count"] == 819
    assert receipt["accepted_manifest"]["full_readback_failures"] == 0
    assert receipt["checkpoint11"]["value_sha256"] == subject.V11_SHA256
    assert receipt["checkpoint11"]["policy_identity_sha256"] == subject.P11_SHA256
    assert receipt["checkpoint11"]["utility_sha256"] == subject.U11_SHA256
    assert receipt["checkpoint11"]["q_artifact_sha256"] == subject.Q11_SHA256
    assert receipt["checkpoint11"]["q_identity"] == subject.Q11_IDENTITY
    assert receipt["checkpoint11"]["checkpoint_identity_sha256"] == subject.CHECKPOINT11_IDENTITY
    assert receipt["checkpoint11"]["policy_map_rerun"] is False
    assert receipt["checkpoint11"]["q11_reassembly"] is False
    assert receipt["q11_sparse_loads"] == 0
    assert receipt["scientific_calls"] == 0


def test_secondary_reaggregation_preserves_raw_discrepancy_and_frozen_bound() -> None:
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


def test_rank_contract_is_fixed_gamma_864_threshold() -> None:
    values = np.linspace(2.0, 1.0, subject.N)
    values[-1] = 0.0

    receipt = subject.rank_receipt(values)

    assert receipt["numerical_rank"] == 799
    assert receipt["numerical_nullity"] == 1
    assert receipt["second_smallest_strictly_above_tau_rank"] is True


def test_ledger_enforces_one_shot_terminal_budget() -> None:
    ledger = subject.Ledger(
        q11_loads=1,
        structural_conservation_audits=1,
        q11_times_one=1,
        exact_positive_graph_constructions=1,
        scc_decompositions=1,
        dense_gesvd=1,
        normalized_stationary_candidates=1,
        global_sign_orientations=1,
        total_mass_normalizations=1,
        q11_transpose_times_p=1,
    )
    subject._check_ledger(ledger)

    ledger.dense_gesvd = 2
    with pytest.raises(subject.FailClosed, match="LEDGER_BUDGET_BREACH"):
        subject._check_ledger(ledger)
