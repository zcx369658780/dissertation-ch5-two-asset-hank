from __future__ import annotations

import ast
import json
import math
from pathlib import Path

import numpy as np
from scipy import sparse

from validators.multi_province.beijing_unique_closed_class_kfe_candidate import run


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "validators/multi_province/beijing_unique_closed_class_kfe_candidate/run.py"


def test_gamma_and_two_threshold_views_are_preregistered() -> None:
    singular = np.linspace(4.0, 1.0, 400)
    singular[-1] = 0.0
    local = run.threshold_view(singular, 400)
    inherited = run.threshold_view(singular, 800)
    assert local["tau_rank"] == run.gamma(464) * 4.0
    assert inherited["tau_rank"] == run.gamma(864) * 4.0
    assert local["numerical_rank"] == inherited["numerical_rank"] == 399
    assert local["numerical_nullity"] == inherited["numerical_nullity"] == 1
    assert inherited["tau_rank"] > local["tau_rank"]


def test_orientation_and_normalization_is_exactly_once() -> None:
    raw = -np.arange(1.0, 401.0)
    candidate, receipt = run.orient_and_normalize(raw)
    assert receipt["orientation_calls"] == 1
    assert receipt["normalization_calls"] == 1
    assert receipt["global_sign_reversed"] is True
    assert math.fsum(float(value) for value in candidate) == 1.0
    assert np.min(candidate) > 0.0


def test_structural_receipt_detects_closed_outgoing_rate() -> None:
    q = sparse.lil_matrix((800, 800), dtype=float)
    for i in range(800):
        q[i, i] = 0.0
    closed = np.arange(400)
    transient = np.arange(400, 800)
    _q_cc, receipt = run.structural_receipt(q.tocsr(), closed, transient)
    assert receipt["status"] == "PASS"
    q[0, 400] = 0.25
    q[0, 0] = -0.25
    _q_cc, failed = run.structural_receipt(q.tocsr(), closed, transient)
    assert failed["checks"]["no_positive_closed_to_transient_outgoing_rate"] is False
    assert failed["status"] == "FAIL"


def test_candidate_and_embedding_require_positive_closed_and_bitwise_zero_transient() -> None:
    closed = np.asarray(run.EXPECTED_CLOSED, dtype=np.int64)
    mask = np.zeros(800, dtype=bool)
    mask[closed] = True
    transient = np.flatnonzero(~mask)
    p_closed = np.full(400, 1.0 / 400.0)
    p_full = np.zeros(800, dtype=np.float64)
    p_full[closed] = p_closed
    assert run.candidate_statistics(p_closed)["status"] == "PASS"
    receipt = run.embedded_statistics(p_full, p_closed, closed, transient)
    assert receipt["status"] == "PASS"
    assert receipt["transient_positive_zero_bit_pattern_count"] == 400
    assert receipt["closed_exact_candidate_match"] is True


def test_stationarity_receipt_uses_existing_full_space_convention() -> None:
    q = sparse.csr_matrix((800, 800), dtype=float)
    p = np.zeros(800)
    p[200:400] = 1.0 / 400.0
    p[600:800] = 1.0 / 400.0
    residual = np.zeros(800)
    receipt = run.stationarity_receipt(q, p, residual)
    assert receipt["status"] == "PASS"
    assert receipt["q_transpose_p_calls"] == 1
    assert receipt["tau_stationarity"] == run.gamma(864)


def test_scientific_ledger_starts_at_literal_zero() -> None:
    ledger = run.scientific_ledger()
    assert all(value == 0 for key, value in ledger.items() if key != "schema")


def test_runner_does_not_import_model_runtime() -> None:
    tree = ast.parse(RUNNER.read_text(encoding="utf-8"))
    imports = "\n".join(
        ast.unparse(node)
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
    ).lower()
    for forbidden in (
        "ch5_two_asset_hank", "nonlinear_continuation", "selector", "household", "firm"
    ):
        assert forbidden not in imports


def test_canonical_support_forensic_manifest_binds_despite_autocrlf_checkout() -> None:
    receipt = run.verify_git_manifest(
        ROOT, run.FORENSIC_ROOT_RELATIVE, run.FORENSIC_MANIFEST_SHA256
    )
    assert receipt["status"] == "PASS"
    assert receipt["canonical_git_blob_sha256"] == run.FORENSIC_MANIFEST_SHA256
    assert receipt["bad_paths"] == []


def test_run003_manifest_and_binary_inputs_bind_without_loading_q() -> None:
    run_root = ROOT / run.RUN003_ROOT_RELATIVE
    assert run.verify_file_manifest(run_root, run.RUN003_MANIFEST_SHA256)["status"] == "PASS"
    q_path = run_root / "household/p00_北京/checkpoint_012/q_generator.npz"
    mass_path = run_root / "household/p00_北京/terminal_kfe/stationary_mass_arrays.npz"
    assert run.file_sha256(q_path) == run.Q_SHA256
    assert run.file_sha256(mass_path) == run.RUN003_MASS_SHA256


def test_persisted_candidate_evidence_satisfies_terminal_contract() -> None:
    evidence = ROOT / run.OUTPUT_ROOT_RELATIVE
    terminal = json.loads((evidence / "terminal_receipt.json").read_text(encoding="utf-8"))
    rank = json.loads(
        (evidence / "restricted_gesvd_rank_nullity_receipt.json").read_text(encoding="utf-8")
    )
    candidate = json.loads(
        (evidence / "closed_class_stationary_candidate_receipt.json").read_text(encoding="utf-8")
    )
    embedded = json.loads(
        (evidence / "embedded_full_space_candidate_receipt.json").read_text(encoding="utf-8")
    )
    assert terminal["terminal_classification"] == run.PASS_TERMINAL
    assert terminal["method_adopted"] is False
    assert rank["local_dimension_threshold_view"]["numerical_rank"] == 399
    assert rank["local_dimension_threshold_view"]["numerical_nullity"] == 1
    assert rank["inherited_full_space_dimension_threshold_view"]["numerical_rank"] == 399
    assert rank["inherited_full_space_dimension_threshold_view"]["numerical_nullity"] == 1
    assert candidate["minimum"] > 0.0
    assert candidate["negative_entry_count"] == 0
    assert embedded["transient_positive_zero_bit_pattern_count"] == 400
    with np.load(evidence / "restricted_singular_spectrum.npz", allow_pickle=False) as archive:
        assert archive["singular_values"].shape == (400,)


def test_persisted_ledger_and_manifest_readback_are_exact() -> None:
    evidence = ROOT / run.OUTPUT_ROOT_RELATIVE
    ledger = json.loads((evidence / "scientific_ledger.json").read_text(encoding="utf-8"))
    assert ledger["q12_artifact_loads"] == 1
    assert ledger["restricted_dense_gesvd_calls"] == 1
    assert ledger["normalized_stationary_candidates"] == 1
    assert ledger["orientation_calls"] == 1
    assert ledger["normalization_calls"] == 1
    assert ledger["full_q_transpose_p_calls"] == 1
    assert ledger["scientific_retries"] == 0
    persisted = json.loads(
        (evidence / "independent_readback_receipt.json").read_text(encoding="utf-8")
    )
    assert persisted == run.readback(evidence)
    assert persisted["status"] == "PASS"
