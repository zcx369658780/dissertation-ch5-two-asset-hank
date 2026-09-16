"""One-shot pin-free/source-free invariant-mass validation for accepted Q1."""

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
Q1_SHA256 = "5F96C2CFAAFB3EA7EF32943A892A9191FEDCC5DBC7AB28D066F5893D3F560D1E"
Q1_BYTES = 23773
D2_RECEIPT_SHA256 = "EDE6EED10F4558BA4D902CC3AA9FDED7E23D961D997C12DE8E3654DC2990085A"
D2_RECEIPT_BYTES = 3560
TOPOLOGY_SHA256 = "4FDD25E33E2D1025849370391D43CE65F925859DAB4A4E97BDE28784D658E86D"
TOPOLOGY_BYTES = 98454
ACCEPTED_MANIFEST_SHA256 = "573FCF61220E5982EB4A6E78FAFC5D82310BAC7F7638D2D83B576B1420DDCF37"
ACCEPTED_MANIFEST_BYTES = 125417
ACCEPTED_MANIFEST_ENTRIES = 808
ACCEPTED_MANIFEST_TOTAL_BYTES = 14117850
EXPECTED_CLOSED_MEMBERS = [[5, 6, 405, 406]]
Q_ONE_BOUND = 2.976424297233587e-14
WALL_SECONDS_LIMIT = 300.0
RSS_BYTES_LIMIT = 2 * 1024**3
ACCEPTED_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_v1_policy_remap_q1_topology_20260916"
)
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_q1_source_free_kfe_operator_validation_20260916"
)
SCIENTIFIC_PATHS = (
    "src/ch5_two_asset_hank/corrected_diagnostic/q0_kfe_validation.py",
    "src/ch5_two_asset_hank/corrected_diagnostic/q1_kfe_validation.py",
    "tests/test_mp4c_2018_kfe_d123_q1_kfe_operator_validation.py",
)

FailClosed = base.FailClosed
gamma = base.gamma
normalize_null_vector = base._normalize_null_vector
rank_receipt = base._rank_receipt


@dataclass
class Ledger:
    q1_loads: int = 0
    structural_conservation_audits: int = 0
    q1_times_one: int = 0
    scc_decompositions: int = 0
    dense_gesvd: int = 0
    normalized_stationary_candidates: int = 0
    q1_transpose_times_p: int = 0

    def as_dict(self, terminal: str) -> dict[str, Any]:
        return {
            "q1_artifact_loads": self.q1_loads,
            "structural_conservation_audits": self.structural_conservation_audits,
            "q1_times_one": self.q1_times_one,
            "scc_decompositions": self.scc_decompositions,
            "dense_scipy_linalg_svd_gesvd": self.dense_gesvd,
            "normalized_stationary_candidates": self.normalized_stationary_candidates,
            "q1_transpose_times_p": self.q1_transpose_times_p,
            "retries": 0,
            "solver_substitutions": 0,
            "iterative_eigensolver_or_nullspace_solves": 0,
            "row_replaced_or_direct_kfe_solves": 0,
            "selector_evaluations": 0,
            "scalar_roots": 0,
            "policy_maps": 0,
            "d2_reassemblies": 0,
            "hjb_v2_or_nonlinear_continuation": 0,
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


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _array_sha256(values: np.ndarray, dtype: str = "<f8") -> str:
    return hashlib.sha256(np.asarray(values, dtype=dtype).tobytes()).hexdigest().upper()


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
    """Bind accepted Q1/D2/topology and receipts without loading Q1."""

    repository = repository.resolve(strict=True)
    accepted = repository / ACCEPTED_RELATIVE
    manifest_path = accepted / "sealed_manifest.json"
    q1_path = accepted / "q1_generator.npz"
    d2_path = accepted / "q1_d2_receipt.json"
    topology_path = accepted / "q1_topology.json"
    required = (manifest_path, q1_path, d2_path, topology_path)
    if not accepted.is_dir() or not all(path.is_file() for path in required):
        raise FailClosed("FAIL__ACCEPTED_Q1_EVIDENCE_MISSING__NO_SCIENCE")

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
        "q1_generator.npz": {"bytes": Q1_BYTES, "path": "q1_generator.npz", "sha256": Q1_SHA256},
        "q1_d2_receipt.json": {"bytes": D2_RECEIPT_BYTES, "path": "q1_d2_receipt.json", "sha256": D2_RECEIPT_SHA256},
        "q1_topology.json": {"bytes": TOPOLOGY_BYTES, "path": "q1_topology.json", "sha256": TOPOLOGY_SHA256},
    }
    for name, expected in expected_entries.items():
        path = accepted / name
        if entries.get(name) != expected:
            raise FailClosed("FAIL__Q1_MANIFEST_ENTRY_MISMATCH__NO_SCIENCE", {"path": name})
        if path.stat().st_size != expected["bytes"] or _sha256(path) != expected["sha256"]:
            raise FailClosed("FAIL__Q1_AUTHORITY_IDENTITY_MISMATCH__NO_SCIENCE", {"path": name})

    d2 = json.loads(d2_path.read_text(encoding="utf-8"))
    checks = d2.get("checks", {})
    if (
        d2.get("status") != "PASS"
        or d2.get("diagonal_construction_error") != 0.0
        or checks.get("diagonal_construction_error_exact_zero") is not True
        or d2.get("max_abs_q_one") != 2.220446049250313e-15
        or d2.get("arithmetic_tolerance") != Q_ONE_BOUND
        or d2.get("minimum_offdiagonal") != 0.016508228132885275
        or checks.get("exact_zero_outward_drift_rate_flux") is not True
    ):
        raise FailClosed("FAIL__Q1_D2_AUTHORITY_MISMATCH__NO_SCIENCE")
    topology = json.loads(topology_path.read_text(encoding="utf-8"))
    if (
        topology.get("q1", {}).get("closed_class_count") != 1
        or topology.get("q1", {}).get("closed_members") != EXPECTED_CLOSED_MEMBERS
        or topology.get("q1", {}).get("exact_positive_edge_count") != 2307
    ):
        raise FailClosed("FAIL__Q1_TOPOLOGY_AUTHORITY_MISMATCH__NO_SCIENCE")

    faces = {
        name: {"cells": 0, "outward_drift_sum": 0.0, "outward_rate_sum": 0.0}
        for name in ("lower_b", "upper_b", "lower_a", "upper_a")
    }
    receipt_digest = hashlib.sha256()
    for flat in range(N):
        name = f"cell_{flat:04d}.json"
        entry = entries.get(name)
        path = accepted / name
        if entry is None or not path.is_file():
            raise FailClosed("FAIL__POLICY_RECEIPT_MISSING__NO_SCIENCE", {"receipt": name})
        actual_hash = _sha256(path)
        if path.stat().st_size != int(entry.get("bytes", -1)) or actual_hash != str(entry.get("sha256")):
            raise FailClosed("FAIL__POLICY_RECEIPT_IDENTITY_MISMATCH__NO_SCIENCE", {"receipt": name})
        receipt_digest.update(name.encode("ascii"))
        receipt_digest.update(actual_hash.encode("ascii"))
        receipt = json.loads(path.read_text(encoding="utf-8"))
        index = list(np.unravel_index(flat, SHAPE, order="F"))
        selected = receipt.get("selector_result", {}).get("selected")
        if (
            receipt.get("flat_index_f_zero_based") != flat
            or receipt.get("index_b_a_z_zero_based") != index
            or receipt.get("selector_result", {}).get("outcome") != "SELECTED_ADMISSIBLE"
            or not isinstance(selected, dict)
        ):
            raise FailClosed("FAIL__POLICY_RECEIPT_CONTENT_MISMATCH__NO_SCIENCE", {"receipt": name})
        i_b, i_a, _ = index
        g_b = float(selected["g_b"])
        g_a = float(selected["g_a"])
        for key, active, outward in (
            ("lower_b", i_b == 0, max(-g_b, 0.0)),
            ("upper_b", i_b == SHAPE[0] - 1, max(g_b, 0.0)),
            ("lower_a", i_a == 0, max(-g_a, 0.0)),
            ("upper_a", i_a == SHAPE[1] - 1, max(g_a, 0.0)),
        ):
            if active:
                faces[key]["cells"] += 1
                faces[key]["outward_drift_sum"] += outward
                faces[key]["outward_rate_sum"] += outward
    if any(row["cells"] != 40 for row in faces.values()):
        raise FailClosed("FAIL__FACE_RECEIPT_CARDINALITY_MISMATCH__NO_SCIENCE", faces)
    if any(row["outward_drift_sum"] != 0.0 or row["outward_rate_sum"] != 0.0 for row in faces.values()):
        raise FailClosed("FAIL__OUTWARD_FACE_FLUX_PRESENT__NO_SCIENCE", faces)
    for row in faces.values():
        row["outward_mass_flux_coefficient"] = 0.0

    return {
        "status": "PASS",
        "accepted_candidate": "368d58c96a9e6068fd4f7b36cca0f433d7f2ec3a",
        "q1": {"path": str(q1_path.relative_to(repository)), "bytes": Q1_BYTES, "sha256": Q1_SHA256},
        "accepted_d2_construction": {
            "path": str(d2_path.relative_to(repository)),
            "bytes": D2_RECEIPT_BYTES,
            "sha256": D2_RECEIPT_SHA256,
            "diagonal_construction_error": 0.0,
            "diagonal_construction_error_exact_zero": True,
            "q1_times_one_accepted": d2["max_abs_q_one"],
            "prospective_bound": Q_ONE_BOUND,
        },
        "accepted_topology": {
            "path": str(topology_path.relative_to(repository)),
            "bytes": TOPOLOGY_BYTES,
            "sha256": TOPOLOGY_SHA256,
            "closed_members": EXPECTED_CLOSED_MEMBERS,
            "exact_positive_edge_count": 2307,
        },
        "accepted_manifest": {
            "path": str(manifest_path.relative_to(repository)),
            "bytes": ACCEPTED_MANIFEST_BYTES,
            "sha256": manifest_hash,
            "entry_count": len(entries),
            "total_bytes": ACCEPTED_MANIFEST_TOTAL_BYTES,
        },
        "policy_receipts": {
            "count": N,
            "all_selected_admissible": True,
            "ordered_name_and_sha256_digest": receipt_digest.hexdigest().upper(),
        },
        "state_contract": {
            "shape_b_a_z": list(SHAPE),
            "flatten_order": "F",
            "fastest_dimension": "b",
            "omega": OMEGA,
            "forward_stationarity": "Q1.T @ p = 0",
        },
        "outside_domain_flux_ledger_before_svd": faces,
        "q1_sparse_loads": 0,
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
        "formula": "diag(Q1) + row_sum(stored CSR offdiagonals)",
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
        "expected_closed_component_members": EXPECTED_CLOSED_MEMBERS,
        "expected_membership_exact": closed_members == EXPECTED_CLOSED_MEMBERS,
        "transient_state_count": int(N - closed_size),
        "exact_positive_edge_count": int(adjacency.nnz),
        "edge_rule": "Q1[i,j] > 0 exactly, offdiagonal only",
    }


def _seal_manifest(evidence: Path) -> None:
    entries = []
    for path in sorted(item for item in evidence.iterdir() if item.name != "sealed_manifest.json"):
        if path.is_file():
            entries.append({"path": path.name, "bytes": path.stat().st_size, "sha256": _sha256(path)})
    _write_json(
        evidence / "sealed_manifest.json",
        {
            "schema": "CH5_D123_Q1_SOURCE_FREE_KFE_OPERATOR_VALIDATION_V1",
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
    evidence.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    ledger = Ledger()
    try:
        preflight = preflight_binding(repository)
        _write_json(evidence / "preflight_binding_receipt.json", preflight)
        pre_hashes = _scientific_hashes(repository)
        _write_json(
            evidence / "pre_execution_code_freeze.json",
            {
                "git_head_before_q1_load": _git_head(repository),
                "scientific_code_sha256_before_q1_load": pre_hashes,
                "q1_sha256": Q1_SHA256,
                "frozen_budget": {
                    "q1_loads": 1,
                    "structural_conservation_audits": 1,
                    "q1_times_one": 1,
                    "scc_decompositions": 1,
                    "dense_gesvd": 1,
                    "normalized_stationary_candidates": 1,
                    "q1_transpose_times_p": 1,
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
        ledger.q1_loads += 1
        q_loaded = sparse.load_npz(repository / ACCEPTED_RELATIVE / "q1_generator.npz")
        if getattr(q_loaded, "format", None) != "csr":
            raise FailClosed("FAIL__Q1_NOT_CSR__NO_SVD")
        q = sparse.csr_matrix(q_loaded, copy=False)

        ledger.structural_conservation_audits += 1
        if q.shape != (N, N) or not np.all(np.isfinite(q.data)):
            raise FailClosed("FAIL__Q1_SHAPE_OR_FINITE_AUDIT__NO_SVD")
        adjacency = base._exact_positive_adjacency(q)
        off = q.copy()
        off.setdiag(0.0)
        off.eliminate_zeros()
        reaggregation = secondary_sparse_reaggregation_audit(q)
        ledger.q1_times_one += 1
        q_one = np.asarray(q @ np.ones(N, dtype=float)).ravel()
        q_one_max = float(np.max(np.abs(q_one), initial=0.0))
        structural = {
            "status": "PASS",
            "shape": list(q.shape),
            "format": q.format,
            "nnz": int(q.nnz),
            "finite": True,
            "minimum_exact_positive_offdiagonal": float(np.min(off.data)) if off.nnz else 0.0,
            "negative_offdiagonal_count": int(np.count_nonzero(off.data < 0.0)),
            "accepted_d2_construction_identity": preflight["accepted_d2_construction"],
            "secondary_sparse_reaggregation_audit": reaggregation,
            "max_abs_q1_times_one": q_one_max,
            "q1_times_one_bound": Q_ONE_BOUND,
            "q1_times_one_passes": q_one_max <= Q_ONE_BOUND,
            "q1_times_one_sha256": _array_sha256(q_one),
            "outside_domain_flux_ledger": preflight["outside_domain_flux_ledger_before_svd"],
        }
        if not reaggregation["within_frozen_bound"] or q_one_max > Q_ONE_BOUND:
            structural["status"] = "FAIL"
            _write_json(evidence / "structural_conservation_receipt.json", structural)
            raise FailClosed("FAIL__Q1_STRUCTURAL_OR_CONSERVATION_AUDIT__NO_SVD", structural)
        _write_json(evidence / "structural_conservation_receipt.json", structural)
        _require_resource_budget(started)

        ledger.scc_decompositions += 1
        component_count, labels = csgraph.connected_components(
            adjacency, directed=True, connection="strong", return_labels=True
        )
        scc = _closed_component_receipt(adjacency, int(component_count), labels)
        scc_pass = (
            scc["closed_component_count"] == 1
            and scc["expected_membership_exact"]
            and scc["exact_positive_edge_count"] == 2307
        )
        scc["status"] = "PASS" if scc_pass else "FAIL"
        scc["labels_sha256"] = _array_sha256(labels, "<i8")
        _write_json(evidence / "scc_receipt.json", scc)
        if not scc_pass:
            raise FailClosed("FAIL__Q1_CLOSED_CLASS_MEMBERSHIP__NO_SVD", scc)
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
        rank.update(
            {
                "status": "PASS",
                "solver": "scipy.linalg.svd",
                "lapack_driver": "gesvd",
                "full_matrices": True,
                "check_finite": True,
                "warnings": warning_receipt,
            }
        )
        if (
            warning_receipt
            or rank["numerical_rank"] != 799
            or rank["numerical_nullity"] != 1
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

        p, orientation = normalize_null_vector(vh[-1, :])
        ledger.normalized_stationary_candidates += 1
        g = p / OMEGA
        if not np.all(np.isfinite(p)) or not np.all(np.isfinite(g)):
            raise FailClosed("FAIL__NORMALIZED_MASS_NONFINITE__NO_RETRY")
        ledger.q1_transpose_times_p += 1
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
            "q1_one_dot_p_within_global_source_bound": abs(q_one_dot_p) <= source_bound,
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
                "dot_q1_times_one_p": q_one_dot_p,
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
            q1_times_one=q_one,
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
        terminal = "PASS__ACCEPTED_Q1_UNIQUE_SOURCE_FREE_NORMALIZED_NONNEGATIVE_INVARIANT_MASS"
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
