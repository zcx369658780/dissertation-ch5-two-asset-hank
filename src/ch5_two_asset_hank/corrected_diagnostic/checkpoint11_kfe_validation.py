"""One-shot pin-free/source-free invariant-mass validation for accepted Q11."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import time
from typing import Any
import warnings

import numpy as np
from scipy import linalg, sparse
from scipy.sparse import csgraph

from . import q0_kfe_validation as base


N = 800
SHAPE = (20, 20, 2)
OMEGA = 70.0 / 361.0
TASK_ID = "CH5_MP4C_2018_KFE_D123_CHECKPOINT11_TERMINAL_SOURCE_FREE_KFE_VALIDATION_20260920"
BASELINE_SHA = "BC10E8778DAB6D8BA00FEAA0B18FC5957D7B6435"
ACCEPTED_CANDIDATE = "47AB268E788C856B2515EBADCA0356DBECBCDA81"
V11_SHA256 = "A097A3DDA767B979224638A51CEDC53EA635687CCDEFBE190FED0B899606921F"
P11_SHA256 = "89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3"
U11_SHA256 = "2E9A077FFA809F2DECEE385FD9E7F50C03E16750C2A074F990C0F3CBCC212648"
Q11_SHA256 = "33367258F3EADB1482D4A5CB30A64A8574830C993B0E5280C451499CBD6913AD"
Q11_BYTES = 24450
Q11_IDENTITY = {
    "data": "9D489C6A5C8E4A1F705CEC228EDE380FF0A5F51D569CA31DE9BCF9B4BC56537A",
    "indices": "9A1E128BD9B13A6711B20FB992699DB405DEF5450543921ACAB69B57FA5474E6",
    "indptr": "63190CF1D9F4C98D89C81A9990736462F19170B45F97E03AD7B507D492D9C327",
}
CHECKPOINT11_IDENTITY = "8093BE714CA83531816B20DFEB2BAB3DCB7AF9B971AD255C3596C1CA2A9E2A3B"
CHECKPOINT_ARRAYS_SHA256 = "F620823F15CEB71A168437880AC8655FCBC075D0B7894CBA013780759A8157B2"
D2_RECEIPT_SHA256 = "8DFE252180421E1339EC7761E658D194F425F4B7DEEE9E3F8474560FCAA71F96"
D2_RECEIPT_BYTES = 2854
CHECKPOINT_MANIFEST_SHA256 = "0892EB5C79164FE3475FF4B070AE8373435D35F8DA6560672774934F119E1B11"
CHECKPOINT_MANIFEST_BYTES = 16045
ACCEPTED_MANIFEST_SHA256 = "5E67E595B32024213EC5E6517389A7DCA6462A24FB735B06EB2F85D6E1621E41"
ACCEPTED_MANIFEST_BYTES = 139426
ACCEPTED_MANIFEST_ENTRIES = 819
ACCEPTED_MANIFEST_TOTAL_BYTES = 13089592
Q_ONE_BOUND = 1.8450485966201867e-14
WALL_SECONDS_LIMIT = 300.0
RSS_BYTES_LIMIT = 2 * 1024**3
ACCEPTED_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_checkpoint10_to_checkpoint12_"
    "bounded_nonlinear_continuation_20260920_run001"
)
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_checkpoint11_terminal_source_free_"
    "kfe_validation_20260920_run001"
)
SCIENTIFIC_PATHS = (
    "src/ch5_two_asset_hank/corrected_diagnostic/q0_kfe_validation.py",
    "src/ch5_two_asset_hank/corrected_diagnostic/q1_kfe_validation.py",
    "src/ch5_two_asset_hank/corrected_diagnostic/checkpoint11_kfe_validation.py",
    "tests/test_mp4c_2018_kfe_d123_checkpoint11_kfe_validation.py",
)

FailClosed = base.FailClosed
gamma = base.gamma
normalize_null_vector = base._normalize_null_vector
rank_receipt = base._rank_receipt


@dataclass
class Ledger:
    q11_loads: int = 0
    structural_conservation_audits: int = 0
    q11_times_one: int = 0
    exact_positive_graph_constructions: int = 0
    scc_decompositions: int = 0
    dense_gesvd: int = 0
    normalized_stationary_candidates: int = 0
    global_sign_orientations: int = 0
    total_mass_normalizations: int = 0
    q11_transpose_times_p: int = 0

    def as_dict(self, terminal: str) -> dict[str, Any]:
        return {
            "q11_artifact_loads": self.q11_loads,
            "structural_conservation_audits": self.structural_conservation_audits,
            "q11_times_one": self.q11_times_one,
            "exact_positive_graph_constructions": self.exact_positive_graph_constructions,
            "scc_decompositions": self.scc_decompositions,
            "dense_scipy_linalg_svd_gesvd": self.dense_gesvd,
            "normalized_stationary_candidates": self.normalized_stationary_candidates,
            "global_sign_orientations": self.global_sign_orientations,
            "total_mass_normalizations": self.total_mass_normalizations,
            "q11_transpose_times_p": self.q11_transpose_times_p,
            "retries": 0,
            "solver_substitutions": 0,
            "iterative_eigensolver_or_nullspace_solves": 0,
            "row_replaced_or_direct_kfe_solves": 0,
            "selector_evaluations": 0,
            "scalar_roots": 0,
            "policy_maps": 0,
            "d2_reassemblies": 0,
            "hjb_solves_or_updates": 0,
            "checkpoint12_work": 0,
            "damping_relaxation_adaptive_delta_or_continuation": 0,
            "clipping_artificial_diffusion_or_parameter_continuation": 0,
            "forbidden_calls": {
                "MATLAB": 0,
                "outer": 0,
                "firm": 0,
                "wage_return": 0,
                "GE": 0,
                "annual": 0,
                "shock": 0,
                "IRF": 0,
                "Results": 0,
            },
            "terminal_classification": terminal,
        }


def _check_ledger(ledger: Ledger) -> None:
    counts = ledger.as_dict("LEDGER_CHECK")
    one_call_keys = (
        "q11_artifact_loads",
        "structural_conservation_audits",
        "q11_times_one",
        "exact_positive_graph_constructions",
        "scc_decompositions",
        "dense_scipy_linalg_svd_gesvd",
        "normalized_stationary_candidates",
        "global_sign_orientations",
        "total_mass_normalizations",
        "q11_transpose_times_p",
    )
    breaches = {
        key: int(counts[key]) for key in one_call_keys if int(counts[key]) > 1
    }
    zero_keys = (
        "retries",
        "solver_substitutions",
        "iterative_eigensolver_or_nullspace_solves",
        "row_replaced_or_direct_kfe_solves",
        "selector_evaluations",
        "scalar_roots",
        "policy_maps",
        "d2_reassemblies",
        "hjb_solves_or_updates",
        "checkpoint12_work",
        "damping_relaxation_adaptive_delta_or_continuation",
        "clipping_artificial_diffusion_or_parameter_continuation",
    )
    breaches.update(
        {key: int(counts[key]) for key in zero_keys if int(counts[key]) != 0}
    )
    if any(int(value) != 0 for value in counts["forbidden_calls"].values()):
        breaches["forbidden_calls"] = counts["forbidden_calls"]
    if breaches:
        raise FailClosed("FAIL__SCIENTIFIC_LEDGER_BUDGET_BREACH__NO_RETRY", breaches)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _array_sha256(values: np.ndarray, dtype: str = "<f8") -> str:
    return hashlib.sha256(np.asarray(values, dtype=dtype).tobytes()).hexdigest().upper()


def _sparse_identity(matrix: sparse.csr_matrix) -> dict[str, str]:
    q = sparse.csr_matrix(matrix)
    return {
        "data": _array_sha256(q.data),
        "indices": _array_sha256(q.indices, "<i8"),
        "indptr": _array_sha256(q.indptr, "<i8"),
    }


def _write_json(path: Path, value: Any) -> None:
    encoded = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(encoded + "\n", encoding="utf-8")
    temporary.replace(path)


def _git_head(repository: Path) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=repository, text=True
    ).strip()


def _scientific_hashes(repository: Path) -> dict[str, str]:
    return {name: _sha256(repository / name) for name in SCIENTIFIC_PATHS}


def _manifest_entries(document: dict[str, Any]) -> dict[str, dict[str, Any]]:
    entries = document.get("entries")
    if not isinstance(entries, list):
        raise FailClosed("FAIL__ACCEPTED_MANIFEST_SCHEMA_MISMATCH__NO_SCIENCE")
    result: dict[str, dict[str, Any]] = {}
    for entry in entries:
        name = str(entry.get("path", ""))
        if not name or name in result:
            raise FailClosed("FAIL__ACCEPTED_MANIFEST_PATH_SET_INVALID__NO_SCIENCE")
        result[name] = entry
    return result


def preflight_binding(repository: Path) -> dict[str, Any]:
    """Bind accepted checkpoint 11 and D2 without loading Q11 as sparse data."""

    repository = repository.resolve(strict=True)
    accepted = repository / ACCEPTED_RELATIVE
    manifest_path = accepted / "sealed_manifest.json"
    checkpoint = accepted / "checkpoint_011"
    q11_path = checkpoint / "q_generator.npz"
    d2_path = checkpoint / "d2_receipt.json"
    checkpoint_manifest_path = checkpoint / "checkpoint_manifest.json"
    checkpoint_arrays_path = checkpoint / "checkpoint_arrays.npz"
    required = (
        manifest_path,
        q11_path,
        d2_path,
        checkpoint_manifest_path,
        checkpoint_arrays_path,
    )
    if not accepted.is_dir() or not all(path.is_file() for path in required):
        raise FailClosed("FAIL__ACCEPTED_Q11_EVIDENCE_MISSING__NO_SCIENCE")

    manifest_hash = _sha256(manifest_path)
    if (
        manifest_path.stat().st_size != ACCEPTED_MANIFEST_BYTES
        or manifest_hash != ACCEPTED_MANIFEST_SHA256
    ):
        raise FailClosed("FAIL__ACCEPTED_MANIFEST_IDENTITY_MISMATCH__NO_SCIENCE")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = _manifest_entries(manifest)
    if (
        len(entries) != ACCEPTED_MANIFEST_ENTRIES
        or int(manifest.get("entry_count", -1)) != ACCEPTED_MANIFEST_ENTRIES
        or int(manifest.get("total_bytes", -1)) != ACCEPTED_MANIFEST_TOTAL_BYTES
    ):
        raise FailClosed("FAIL__ACCEPTED_MANIFEST_CARDINALITY_MISMATCH__NO_SCIENCE")
    expected_entries = {
        "checkpoint_011/q_generator.npz": {
            "bytes": Q11_BYTES,
            "path": "checkpoint_011/q_generator.npz",
            "sha256": Q11_SHA256,
        },
        "checkpoint_011/d2_receipt.json": {
            "bytes": D2_RECEIPT_BYTES,
            "path": "checkpoint_011/d2_receipt.json",
            "sha256": D2_RECEIPT_SHA256,
        },
        "checkpoint_011/checkpoint_manifest.json": {
            "bytes": CHECKPOINT_MANIFEST_BYTES,
            "path": "checkpoint_011/checkpoint_manifest.json",
            "sha256": CHECKPOINT_MANIFEST_SHA256,
        },
        "checkpoint_011/checkpoint_arrays.npz": {
            "bytes": 29158,
            "path": "checkpoint_011/checkpoint_arrays.npz",
            "sha256": CHECKPOINT_ARRAYS_SHA256,
        },
    }
    for name, expected in expected_entries.items():
        path = accepted / name
        if entries.get(name) != expected:
            raise FailClosed("FAIL__Q11_MANIFEST_ENTRY_MISMATCH__NO_SCIENCE", {"path": name})
        if path.stat().st_size != expected["bytes"] or _sha256(path) != expected["sha256"]:
            raise FailClosed("FAIL__Q11_AUTHORITY_IDENTITY_MISMATCH__NO_SCIENCE", {"path": name})

    bad_entries: list[str] = []
    for name, entry in entries.items():
        path = accepted / name
        if (
            not path.is_file()
            or path.stat().st_size != int(entry.get("bytes", -1))
            or _sha256(path) != str(entry.get("sha256", ""))
        ):
            bad_entries.append(name)
    if bad_entries:
        raise FailClosed(
            "FAIL__ACCEPTED_MANIFEST_READBACK_MISMATCH__NO_SCIENCE",
            {"first_bad_path": bad_entries[0], "bad_count": len(bad_entries)},
        )

    d2 = json.loads(d2_path.read_text(encoding="utf-8"))
    checks = d2.get("checks", {})
    if (
        d2.get("status") != "PASS"
        or d2.get("diagonal_construction_error") != 0.0
        or checks.get("diagonal_construction_error_exact_zero") is not True
        or d2.get("max_abs_q_one") != 1.7763568394002505e-15
        or d2.get("arithmetic_tolerance") != Q_ONE_BOUND
        or d2.get("minimum_offdiagonal") != 2.7404782515125115e-06
        or checks.get("zero_outward_face_count") is not True
        or checks.get("zero_outward_face_amount") is not True
        or d2.get("q_artifact", {}).get("sha256") != Q11_SHA256
        or d2.get("q_identity") != Q11_IDENTITY
    ):
        raise FailClosed("FAIL__Q11_D2_AUTHORITY_MISMATCH__NO_SCIENCE")

    checkpoint_manifest = json.loads(
        checkpoint_manifest_path.read_text(encoding="utf-8")
    )
    if (
        checkpoint_manifest.get("value_sha256") != V11_SHA256
        or checkpoint_manifest.get("policy_identity_sha256") != P11_SHA256
        or checkpoint_manifest.get("utility_sha256") != U11_SHA256
        or checkpoint_manifest.get("q_artifact_sha256") != Q11_SHA256
        or checkpoint_manifest.get("q_identity") != Q11_IDENTITY
        or checkpoint_manifest.get("checkpoint_identity_sha256")
        != CHECKPOINT11_IDENTITY
        or checkpoint_manifest.get("checkpoint_arrays", {}).get("sha256")
        != CHECKPOINT_ARRAYS_SHA256
        or checkpoint_manifest.get("d2_receipt_status") != "PASS"
        or checkpoint_manifest.get("primary_convergence_pass") is not True
        or checkpoint_manifest.get("bellman_residual_inf")
        != 5.456747553811425e-11
        or checkpoint_manifest.get("value_change_inf")
        != 5.4012647243695255e-08
    ):
        raise FailClosed("FAIL__CHECKPOINT11_IDENTITY_MISMATCH__NO_SCIENCE")

    return {
        "status": "PASS",
        "task_id": TASK_ID,
        "baseline_live_main": BASELINE_SHA,
        "accepted_candidate": ACCEPTED_CANDIDATE,
        "checkpoint11": {
            "value_sha256": V11_SHA256,
            "policy_identity_sha256": P11_SHA256,
            "utility_sha256": U11_SHA256,
            "q_artifact_sha256": Q11_SHA256,
            "q_identity": Q11_IDENTITY,
            "checkpoint_identity_sha256": CHECKPOINT11_IDENTITY,
            "checkpoint_arrays_sha256": CHECKPOINT_ARRAYS_SHA256,
            "bellman_residual_inf": 5.456747553811425e-11,
            "value_change_inf": 5.4012647243695255e-08,
            "d2_status": "PASS",
            "primary_convergence_pass": True,
            "policy_map_rerun": False,
            "q11_reassembly": False,
        },
        "q11": {
            "path": str(q11_path.relative_to(repository)),
            "bytes": Q11_BYTES,
            "sha256": Q11_SHA256,
            "csr_identity": Q11_IDENTITY,
        },
        "accepted_d2_construction": {
            "path": str(d2_path.relative_to(repository)),
            "bytes": D2_RECEIPT_BYTES,
            "sha256": D2_RECEIPT_SHA256,
            "diagonal_construction_error": 0.0,
            "diagonal_construction_error_exact_zero": True,
            "q11_times_one_accepted": d2["max_abs_q_one"],
            "prospective_bound": Q_ONE_BOUND,
        },
        "accepted_manifest": {
            "path": str(manifest_path.relative_to(repository)),
            "bytes": ACCEPTED_MANIFEST_BYTES,
            "sha256": manifest_hash,
            "entry_count": len(entries),
            "total_bytes": ACCEPTED_MANIFEST_TOTAL_BYTES,
            "full_readback_failures": 0,
        },
        "state_contract": {
            "shape_b_a_z": list(SHAPE),
            "flatten_order": "F",
            "fastest_dimension": "b",
            "omega": OMEGA,
            "forward_stationarity": "Q11.T @ p = 0",
        },
        "known_identity_change_count_800_representation_false_positive_ignored": True,
        "q11_sparse_loads": 0,
        "scientific_calls": 0,
    }


def secondary_sparse_reaggregation_audit(q: sparse.csr_matrix) -> dict[str, Any]:
    offdiagonal = q.copy()
    offdiagonal.setdiag(0.0)
    offdiagonal.eliminate_zeros()
    stored_outgoing = np.asarray(offdiagonal.sum(axis=1)).ravel()
    discrepancy = np.asarray(q.diagonal() + stored_outgoing).ravel()
    finite = bool(np.all(np.isfinite(discrepancy)))
    maximum = float(np.max(np.abs(discrepancy), initial=0.0))
    return {
        "formula": "diag(Q11) + row_sum(stored CSR offdiagonals)",
        "maximum_absolute_discrepancy": maximum,
        "discrepancy_sha256": _array_sha256(discrepancy),
        "finite": finite,
        "bound": Q_ONE_BOUND,
        "within_frozen_bound": finite and maximum <= Q_ONE_BOUND,
        "discrepancy_was_not_modified_or_zeroed": True,
    }


def _closed_component_receipt(
    adjacency: sparse.csr_matrix, component_count: int, labels: np.ndarray
) -> dict[str, Any]:
    closed = np.ones(component_count, dtype=bool)
    for origin in range(N):
        source = int(labels[origin])
        for destination in adjacency.indices[adjacency.indptr[origin] : adjacency.indptr[origin + 1]]:
            if int(labels[int(destination)]) != source:
                closed[source] = False
    sizes = np.bincount(labels, minlength=component_count)
    closed_labels = [int(value) for value in np.flatnonzero(closed)]
    closed_members = [
        [int(value) for value in np.flatnonzero(labels == label)] for label in closed_labels
    ]
    closed_size = sum(len(row) for row in closed_members)
    return {
        "component_count": int(component_count),
        "component_sizes_by_label": [int(value) for value in sizes],
        "closed_component_labels": closed_labels,
        "closed_component_count": len(closed_labels),
        "closed_component_sizes": [len(row) for row in closed_members],
        "closed_component_members": closed_members,
        "transient_state_count": int(N - closed_size),
        "exact_positive_edge_count": int(adjacency.nnz),
        "edge_rule": "Q11[i,j] > 0 exactly, offdiagonal only",
        "membership_was_discovered_not_imposed": True,
    }


def _seal_manifest(evidence: Path) -> None:
    entries = []
    for path in sorted(item for item in evidence.iterdir() if item.name != "sealed_manifest.json"):
        if path.is_file():
            entries.append({"path": path.name, "bytes": path.stat().st_size, "sha256": _sha256(path)})
    _write_json(
        evidence / "sealed_manifest.json",
        {
            "schema": "CH5_D123_CHECKPOINT11_TERMINAL_SOURCE_FREE_KFE_VALIDATION_V1",
            "entry_count": len(entries),
            "total_bytes": sum(int(entry["bytes"]) for entry in entries),
            "entries": entries,
        },
    )


def _resource_receipt(started: float) -> dict[str, Any]:
    return {
        "wall_seconds": float(time.perf_counter() - started),
        "wall_seconds_limit": WALL_SECONDS_LIMIT,
        "peak_resident_bytes": base._peak_rss_bytes(),
        "resident_bytes_limit": RSS_BYTES_LIMIT,
    }


def _require_resource_budget(started: float) -> dict[str, Any]:
    receipt = _resource_receipt(started)
    if receipt["wall_seconds"] > WALL_SECONDS_LIMIT:
        raise FailClosed("FAIL__WALL_TIME_BUDGET_EXCEEDED__NO_RETRY", receipt)
    if receipt["peak_resident_bytes"] > RSS_BYTES_LIMIT:
        raise FailClosed("FAIL__RESIDENT_MEMORY_BUDGET_EXCEEDED__NO_RETRY", receipt)
    return receipt


def _finalize(
    repository: Path,
    evidence: Path,
    ledger: Ledger,
    pre_hashes: dict[str, str],
    terminal: str,
    started: float,
    detail: dict[str, Any] | None = None,
) -> str:
    try:
        _check_ledger(ledger)
    except FailClosed as failure:
        terminal = failure.terminal
        detail = failure.detail
    resources = _resource_receipt(started)
    after = _scientific_hashes(repository)
    freeze_matches = after == pre_hashes
    if not freeze_matches and terminal.startswith("PASS__"):
        terminal = "FAIL__SCIENTIFIC_CODE_MUTATED_AFTER_FREEZE__NO_RETRY"
    _write_json(
        evidence / "post_execution_freeze_check.json",
        {
            "matches_pre_execution_freeze": freeze_matches,
            "scientific_code_sha256_after_execution": after,
            "resources": resources,
        },
    )
    _write_json(evidence / "execution_ledger.json", ledger.as_dict(terminal))
    _write_json(evidence / "terminal_receipt.json", {"terminal": terminal, "detail": detail or {}})
    _seal_manifest(evidence)
    return terminal


def execute(repository: Path) -> str:
    repository = repository.resolve(strict=True)
    evidence = repository / OUTPUT_RELATIVE
    clean_before_evidence = not subprocess.check_output(
        ["git", "status", "--porcelain"], cwd=repository, text=True
    ).strip()
    origin_main = subprocess.check_output(
        ["git", "rev-parse", "origin/main"], cwd=repository, text=True
    ).strip().upper()
    evidence.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    ledger = Ledger()
    try:
        if not clean_before_evidence or origin_main != BASELINE_SHA:
            raise FailClosed(
                "FAIL__GIT_PREFLIGHT_MISMATCH__NO_SCIENCE",
                {
                    "worktree_clean_before_evidence": clean_before_evidence,
                    "origin_main": origin_main,
                    "expected_origin_main": BASELINE_SHA,
                },
            )
        preflight = preflight_binding(repository)
        _write_json(evidence / "preflight_binding_receipt.json", preflight)
        pre_hashes = _scientific_hashes(repository)
        _write_json(
            evidence / "pre_execution_code_freeze.json",
            {
                "git_head_before_q11_load": _git_head(repository),
                "worktree_clean_before_evidence": clean_before_evidence,
                "origin_main": origin_main,
                "scientific_code_sha256_before_q11_load": pre_hashes,
                "q11_sha256": Q11_SHA256,
                "frozen_budget": {
                    "q11_loads": 1,
                    "structural_conservation_audits": 1,
                    "q11_times_one": 1,
                    "scc_decompositions": 1,
                    "dense_gesvd": 1,
                    "normalized_stationary_candidates": 1,
                    "q11_transpose_times_p": 1,
                    "retries": 0,
                    "wall_seconds": WALL_SECONDS_LIMIT,
                    "resident_bytes": RSS_BYTES_LIMIT,
                },
            },
        )
    except FailClosed as failure:
        pre_hashes = _scientific_hashes(repository)
        return _finalize(repository, evidence, ledger, pre_hashes, failure.terminal, started, failure.detail)

    try:
        _require_resource_budget(started)
        ledger.q11_loads += 1
        q_loaded = sparse.load_npz(
            repository / ACCEPTED_RELATIVE / "checkpoint_011" / "q_generator.npz"
        )
        if getattr(q_loaded, "format", None) != "csr":
            raise FailClosed("FAIL__Q11_NOT_CSR__NO_SVD")
        q = sparse.csr_matrix(q_loaded, copy=False)

        ledger.structural_conservation_audits += 1
        if q.shape != (N, N) or not np.all(np.isfinite(q.data)):
            raise FailClosed("FAIL__Q11_SHAPE_OR_FINITE_AUDIT__NO_SVD")
        q_identity = _sparse_identity(q)
        if q_identity != Q11_IDENTITY:
            raise FailClosed(
                "FAIL__Q11_CSR_IDENTITY_MISMATCH__NO_SVD",
                {"actual": q_identity, "expected": Q11_IDENTITY},
            )
        off = q.copy()
        off.setdiag(0.0)
        off.eliminate_zeros()
        negative_offdiagonal_count = int(np.count_nonzero(off.data < 0.0))
        if negative_offdiagonal_count:
            raise FailClosed(
                "FAIL__NEGATIVE_OFFDIAGONAL__NO_SVD",
                {"negative_offdiagonal_count": negative_offdiagonal_count},
            )
        reaggregation = secondary_sparse_reaggregation_audit(q)
        ledger.q11_times_one += 1
        q_one = np.asarray(q @ np.ones(N, dtype=float)).ravel()
        q_one_max = float(np.max(np.abs(q_one), initial=0.0))
        ledger.exact_positive_graph_constructions += 1
        adjacency = base._exact_positive_adjacency(q)
        structural = {
            "status": "PASS",
            "shape": list(q.shape),
            "format": q.format,
            "nnz": int(q.nnz),
            "finite": True,
            "q11_csr_identity": q_identity,
            "minimum_exact_positive_offdiagonal": float(np.min(off.data)) if off.nnz else 0.0,
            "negative_offdiagonal_count": negative_offdiagonal_count,
            "accepted_d2_construction_identity": preflight["accepted_d2_construction"],
            "secondary_sparse_reaggregation_audit": reaggregation,
            "max_abs_q11_times_one": q_one_max,
            "q11_times_one_bound": Q_ONE_BOUND,
            "q11_times_one_passes": q_one_max <= Q_ONE_BOUND,
            "q11_times_one_sha256": _array_sha256(q_one),
            "exact_positive_graph_constructed_once": True,
            "exact_positive_edge_count": int(adjacency.nnz),
        }
        if (
            negative_offdiagonal_count
            or not reaggregation["within_frozen_bound"]
            or q_one_max > Q_ONE_BOUND
        ):
            structural["status"] = "FAIL"
            _write_json(evidence / "structural_conservation_receipt.json", structural)
            raise FailClosed("FAIL__Q11_STRUCTURAL_OR_CONSERVATION_AUDIT__NO_SVD", structural)
        _write_json(evidence / "structural_conservation_receipt.json", structural)
        _require_resource_budget(started)

        ledger.scc_decompositions += 1
        component_count, labels = csgraph.connected_components(
            adjacency, directed=True, connection="strong", return_labels=True
        )
        scc = _closed_component_receipt(adjacency, int(component_count), labels)
        scc_pass = scc["closed_component_count"] == 1
        scc["status"] = "PASS" if scc_pass else "FAIL"
        scc["labels_sha256"] = _array_sha256(labels, "<i8")
        _write_json(evidence / "scc_receipt.json", scc)
        if not scc_pass:
            raise FailClosed("FAIL__Q11_CLOSED_CLASS_COUNT__NO_SVD", scc)
        _require_resource_budget(started)

        a = q.transpose().tocsr()
        ledger.dense_gesvd += 1
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            _u, singular_values, vh = linalg.svd(
                a.toarray(),
                full_matrices=True,
                lapack_driver="gesvd",
                check_finite=True,
            )
        warning_receipt = [
            {"category": item.category.__name__, "message": str(item.message)} for item in caught
        ]
        rank = rank_receipt(singular_values)
        singular_values_at_or_below_tau = int(
            np.count_nonzero(singular_values <= float(rank["tau_rank"]))
        )
        rank.update(
            {
                "status": "PASS",
                "solver": "scipy.linalg.svd",
                "lapack_driver": "gesvd",
                "full_matrices": True,
                "check_finite": True,
                "warnings": warning_receipt,
                "singular_values_at_or_below_tau_rank": singular_values_at_or_below_tau,
            }
        )
        if (
            warning_receipt
            or rank["numerical_rank"] != 799
            or rank["numerical_nullity"] != 1
            or singular_values_at_or_below_tau != 1
            or not rank["second_smallest_strictly_above_tau_rank"]
        ):
            rank["status"] = "FAIL"
            _write_json(evidence / "svd_rank_nullity_receipt.json", rank)
            raise FailClosed("FAIL__SVD_RANK_NULLITY_CONTRACT__NO_RETRY", rank)
        if scc["closed_component_count"] != rank["numerical_nullity"]:
            rank["status"] = "FAIL_GRAPH_NUMERICAL_DISAGREEMENT"
            _write_json(evidence / "svd_rank_nullity_receipt.json", rank)
            raise FailClosed("FAIL__GRAPH_NUMERICAL_NULLITY_DISAGREEMENT__NO_RETRY", rank)
        _write_json(evidence / "svd_rank_nullity_receipt.json", rank)
        _require_resource_budget(started)

        ledger.normalized_stationary_candidates += 1
        p, orientation = normalize_null_vector(vh[-1, :])
        ledger.global_sign_orientations += 1
        ledger.total_mass_normalizations += 1
        g = p / OMEGA
        if not np.all(np.isfinite(p)) or not np.all(np.isfinite(g)):
            raise FailClosed("FAIL__NORMALIZED_MASS_NONFINITE__NO_RETRY")
        ledger.q11_transpose_times_p += 1
        residual = np.asarray(a @ p).ravel()
        a_inf = float(np.max(np.asarray(abs(a).sum(axis=1)).ravel(), initial=0.0))
        p_inf = float(np.linalg.norm(p, ord=np.inf))
        p_l1 = math.fsum(abs(float(value)) for value in p)
        residual_inf = float(np.linalg.norm(residual, ord=np.inf))
        stationarity_scale = max(1.0, a_inf * p_inf)
        tau_stationarity = gamma(N + 64) * stationarity_scale
        backward_ratio = residual_inf / stationarity_scale
        residual_sum = math.fsum(float(value) for value in residual)
        q_one_dot_p = float(np.dot(q_one, p))
        source_discrepancy = abs(residual_sum - q_one_dot_p)
        source_bound = gamma(N + 64) * max(1.0, N * a_inf * p_inf)
        p_sum = math.fsum(float(value) for value in p)
        p_normalization_bound = gamma(N) * max(1.0, p_l1)
        g_abs_sum = math.fsum(abs(float(value)) for value in g)
        weighted_density_sum = OMEGA * math.fsum(float(value) for value in g)
        grouped_density_bound = gamma(N + 2) * max(1.0, OMEGA * g_abs_sum)
        tau_nonnegative = gamma(N + 64) * max(1.0, p_inf)
        negative = [max(-float(value), 0.0) for value in p]
        negative_count = sum(value > 0.0 for value in negative)
        total_negative = math.fsum(negative)
        minimum_mass = float(np.min(p))
        checks = {
            "residual_finite": bool(np.all(np.isfinite(residual))),
            "stationarity_inf_within_bound": residual_inf <= tau_stationarity,
            "normwise_backward_ratio_within_gamma_864": backward_ratio <= gamma(N + 64),
            "residual_sum_within_global_source_bound": abs(residual_sum) <= source_bound,
            "q11_one_dot_p_within_global_source_bound": abs(q_one_dot_p) <= source_bound,
            "source_identity_discrepancy_within_bound": source_discrepancy <= source_bound,
            "probability_mass_normalized": abs(p_sum - 1.0) <= p_normalization_bound,
            "density_volume_normalized": abs(weighted_density_sum - 1.0) <= grouped_density_bound,
            "minimum_mass_within_allowance": minimum_mass >= -tau_nonnegative,
            "total_negative_mass_within_allowance": total_negative <= N * tau_nonnegative,
            "no_clipping": True,
            "no_tolerance_tuning": True,
            "no_retry": True,
        }
        mass_receipt = {
            "status": "PASS" if all(checks.values()) else "FAIL",
            "checks": checks,
            "orientation_and_normalization": orientation,
            "stationarity": {
                "residual_inf": residual_inf,
                "a_inf": a_inf,
                "p_inf": p_inf,
                "tau_stationarity": tau_stationarity,
                "normwise_backward_ratio": backward_ratio,
                "gamma_864": gamma(N + 64),
                "math_fsum_residual": residual_sum,
                "dot_q11_times_one_p": q_one_dot_p,
                "source_identity_discrepancy": source_discrepancy,
                "prospective_global_source_bound": source_bound,
                "global_source_bound_formula": "gamma_864 * max(1, N * ||A||_inf * ||p||_inf)",
            },
            "normalization": {
                "math_fsum_p": p_sum,
                "sum_abs_p": p_l1,
                "probability_mass_bound": p_normalization_bound,
                "omega": OMEGA,
                "omega_times_math_fsum_g": weighted_density_sum,
                "grouped_density_bound": grouped_density_bound,
                "grouped_density_bound_formula": "gamma_802 * max(1, omega * sum(abs(g)))",
            },
            "nonnegativity": {
                "minimum_p": minimum_mass,
                "negative_entry_count": int(negative_count),
                "total_negative_mass": total_negative,
                "tau_nonnegative": tau_nonnegative,
                "total_negative_mass_bound": N * tau_nonnegative,
            },
        }
        np.savez_compressed(
            evidence / "stationary_mass_arrays.npz",
            p=p,
            g=g,
            residual=residual,
            q11_times_one=q_one,
            singular_values=singular_values,
            scc_labels=labels,
        )
        mass_receipt["arrays_artifact"] = {
            "path": "stationary_mass_arrays.npz",
            "bytes": (evidence / "stationary_mass_arrays.npz").stat().st_size,
            "sha256": _sha256(evidence / "stationary_mass_arrays.npz"),
            "p_sha256": _array_sha256(p),
            "g_sha256": _array_sha256(g),
            "residual_sha256": _array_sha256(residual),
        }
        _write_json(evidence / "stationarity_normalization_nonnegativity_receipt.json", mass_receipt)
        if not all(checks.values()):
            raise FailClosed("FAIL__STATIONARY_MASS_ACCEPTANCE_CONTRACT__NO_RETRY", mass_receipt)
        _write_json(evidence / "resource_receipt.json", _require_resource_budget(started))
        terminal = (
            "PASS__CHECKPOINT11_UNIQUE_SOURCE_FREE_INVARIANT_MASS__"
            "HOUSEHOLD_HJB_KFE_FIXED_POINT_CANDIDATE"
        )
        return _finalize(repository, evidence, ledger, pre_hashes, terminal, started)
    except FailClosed as failure:
        return _finalize(repository, evidence, ledger, pre_hashes, failure.terminal, started, failure.detail)
    except Exception as exc:
        return _finalize(
            repository,
            evidence,
            ledger,
            pre_hashes,
            "FAIL__UNEXPECTED_VALIDATION_EXCEPTION__NO_RETRY",
            started,
            {"type": type(exc).__name__, "message": str(exc)},
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args(argv)
    repository = args.repository.resolve(strict=True)
    if args.preflight_only:
        try:
            receipt = preflight_binding(repository)
        except FailClosed as failure:
            print(json.dumps({"status": "FAIL", "terminal": failure.terminal, "detail": failure.detail}, indent=2))
            return 2
        print(json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False))
        return 0
    terminal = execute(repository)
    print(terminal)
    return 0 if terminal.startswith("PASS__") else 2


if __name__ == "__main__":
    sys.exit(main())
