"""Bounded, source-free stationary-mass validation for the accepted Q0.

This module is deliberately isolated from policy selection, generator assembly,
and HJB code.  It loads the already accepted Q0 exactly once and implements the
single SCC / single dense-GESVD contract frozen by the 2026-09-16 task.
"""

from __future__ import annotations

import argparse
import ctypes
from ctypes import wintypes
from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import time
from typing import Any, Iterable
import warnings

import numpy as np
from scipy import linalg, sparse
from scipy.sparse import csgraph


N = 800
SHAPE = (20, 20, 2)
OMEGA = 70.0 / 361.0
Q0_SHA256 = "093E1AF1ADFEEE5C50D3DD91EDDD678EBAC5BBA6C42E64DE73A63B82102AF1D5"
Q0_BYTES = 22474
ACCEPTED_MANIFEST_SHA256 = (
    "D628E24AD421EA5A38EF80230862FE7B3BBD9BFA368CA7BEB08820528ADB643E"
)
ACCEPTED_MANIFEST_BYTES = 125779
ACCEPTED_MANIFEST_ENTRIES = 810
ACCEPTED_MANIFEST_TOTAL_BYTES = 13963843
Q_ONE_BOUND = 5.222144858126786e-14
WALL_SECONDS_LIMIT = 300.0
RSS_BYTES_LIMIT = 2 * 1024**3
ACCEPTED_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_interior_z_switching_option_a_reexecution_20260916"
)
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_corrected_q0_kfe_operator_validation_20260916"
)
SCIENTIFIC_PATHS = (
    "src/ch5_two_asset_hank/corrected_diagnostic/q0_kfe_validation.py",
    "tests/test_mp4c_2018_kfe_d123_q0_kfe_operator_validation.py",
)


class FailClosed(RuntimeError):
    """A terminal contract failure for which retry is forbidden."""

    def __init__(self, terminal: str, detail: dict[str, Any] | None = None):
        super().__init__(terminal)
        self.terminal = terminal
        self.detail = detail or {}


@dataclass
class Ledger:
    q0_loads: int = 0
    structural_conservation_audits: int = 0
    scc_decompositions: int = 0
    dense_gesvd: int = 0
    normalized_stationary_candidates: int = 0
    q0_times_one: int = 0
    q0_transpose_times_p: int = 0

    def as_dict(self, terminal: str) -> dict[str, Any]:
        return {
            "q0_artifact_loads": self.q0_loads,
            "structural_conservation_audits": self.structural_conservation_audits,
            "scc_decompositions": self.scc_decompositions,
            "dense_scipy_linalg_svd_gesvd": self.dense_gesvd,
            "normalized_stationary_candidates": self.normalized_stationary_candidates,
            "q0_times_one": self.q0_times_one,
            "q0_transpose_times_p": self.q0_transpose_times_p,
            "row_replaced_or_direct_kfe_solves": 0,
            "iterative_eigensolver_or_nullspace_solves": 0,
            "solver_substitutions": 0,
            "retries": 0,
            "selector_evaluations": 0,
            "scalar_roots": 0,
            "policy_maps": 0,
            "d2_assemblies": 0,
            "hjb_solves": 0,
            "v1_remaps": 0,
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


def gamma(count: int) -> float:
    eps = np.finfo(float).eps
    return float(count * eps / (1.0 - count * eps))


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


def _peak_rss_bytes() -> int:
    if sys.platform == "win32":
        class ProcessMemoryCountersEx(ctypes.Structure):
            _fields_ = [
                ("cb", ctypes.c_ulong),
                ("PageFaultCount", ctypes.c_ulong),
                ("PeakWorkingSetSize", ctypes.c_size_t),
                ("WorkingSetSize", ctypes.c_size_t),
                ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
                ("QuotaPagedPoolUsage", ctypes.c_size_t),
                ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
                ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                ("PagefileUsage", ctypes.c_size_t),
                ("PeakPagefileUsage", ctypes.c_size_t),
                ("PrivateUsage", ctypes.c_size_t),
            ]

        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        psapi = ctypes.WinDLL("psapi", use_last_error=True)
        kernel32.GetCurrentProcess.argtypes = []
        kernel32.GetCurrentProcess.restype = wintypes.HANDLE
        psapi.GetProcessMemoryInfo.argtypes = [
            wintypes.HANDLE,
            ctypes.POINTER(ProcessMemoryCountersEx),
            wintypes.DWORD,
        ]
        psapi.GetProcessMemoryInfo.restype = wintypes.BOOL
        counters = ProcessMemoryCountersEx()
        counters.cb = ctypes.sizeof(counters)
        handle = kernel32.GetCurrentProcess()
        ok = psapi.GetProcessMemoryInfo(
            handle, ctypes.byref(counters), counters.cb
        )
        if not ok:
            raise ctypes.WinError(ctypes.get_last_error())
        return int(counters.PeakWorkingSetSize)

    import resource

    peak = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return peak if sys.platform == "darwin" else peak * 1024


def _resource_receipt(started: float) -> dict[str, Any]:
    return {
        "wall_seconds": float(time.perf_counter() - started),
        "wall_seconds_limit": WALL_SECONDS_LIMIT,
        "peak_resident_bytes": _peak_rss_bytes(),
        "resident_bytes_limit": RSS_BYTES_LIMIT,
    }


def _require_resource_budget(started: float) -> dict[str, Any]:
    receipt = _resource_receipt(started)
    if receipt["wall_seconds"] > WALL_SECONDS_LIMIT:
        raise FailClosed("FAIL__WALL_TIME_BUDGET_EXCEEDED__NO_RETRY", receipt)
    if receipt["peak_resident_bytes"] > RSS_BYTES_LIMIT:
        raise FailClosed("FAIL__RESIDENT_MEMORY_BUDGET_EXCEEDED__NO_RETRY", receipt)
    return receipt


def _manifest_entries(document: dict[str, Any]) -> dict[str, dict[str, Any]]:
    entries = document.get("entries")
    if not isinstance(entries, list):
        raise FailClosed("FAIL__ACCEPTED_MANIFEST_SCHEMA_MISMATCH__NO_SCIENCE")
    by_path: dict[str, dict[str, Any]] = {}
    for entry in entries:
        name = str(entry.get("path", ""))
        if not name or name in by_path:
            raise FailClosed("FAIL__ACCEPTED_MANIFEST_PATH_SET_INVALID__NO_SCIENCE")
        by_path[name] = entry
    return by_path


def preflight_binding(repository: Path) -> dict[str, Any]:
    """Hash-bind Q0 and all 800 accepted receipts without loading Q0."""

    accepted = repository / ACCEPTED_RELATIVE
    manifest_path = accepted / "manifest.json"
    q0_path = accepted / "d2_generator.npz"
    if not accepted.is_dir() or not manifest_path.is_file() or not q0_path.is_file():
        raise FailClosed("FAIL__ACCEPTED_Q0_EVIDENCE_MISSING__NO_SCIENCE")
    manifest_hash = _sha256(manifest_path)
    if manifest_hash != ACCEPTED_MANIFEST_SHA256 or manifest_path.stat().st_size != ACCEPTED_MANIFEST_BYTES:
        raise FailClosed("FAIL__ACCEPTED_MANIFEST_IDENTITY_MISMATCH__NO_SCIENCE")
    document = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = _manifest_entries(document)
    if (
        int(document.get("entry_count", -1)) != ACCEPTED_MANIFEST_ENTRIES
        or int(document.get("total_bytes", -1)) != ACCEPTED_MANIFEST_TOTAL_BYTES
        or len(entries) != ACCEPTED_MANIFEST_ENTRIES
    ):
        raise FailClosed("FAIL__ACCEPTED_MANIFEST_CARDINALITY_MISMATCH__NO_SCIENCE")
    q0_entry = entries.get("d2_generator.npz")
    if q0_entry != {"bytes": Q0_BYTES, "path": "d2_generator.npz", "sha256": Q0_SHA256}:
        raise FailClosed("FAIL__Q0_MANIFEST_ENTRY_MISMATCH__NO_SCIENCE")
    if q0_path.stat().st_size != Q0_BYTES or _sha256(q0_path) != Q0_SHA256:
        raise FailClosed("FAIL__Q0_ARTIFACT_IDENTITY_MISMATCH__NO_SCIENCE")

    face = {
        "lower_b": {"cells": 0, "outward_rate_sum": 0.0, "outward_drift_sum": 0.0},
        "upper_b": {"cells": 0, "outward_rate_sum": 0.0, "outward_drift_sum": 0.0},
        "lower_a": {"cells": 0, "outward_rate_sum": 0.0, "outward_drift_sum": 0.0},
        "upper_a": {"cells": 0, "outward_rate_sum": 0.0, "outward_drift_sum": 0.0},
    }
    receipt_hashes = hashlib.sha256()
    for flat in range(N):
        name = f"cell_{flat:04d}.json"
        entry = entries.get(name)
        path = accepted / name
        if entry is None or not path.is_file():
            raise FailClosed("FAIL__POLICY_RECEIPT_MISSING__NO_SCIENCE", {"receipt": name})
        actual_hash = _sha256(path)
        actual_bytes = path.stat().st_size
        if actual_hash != str(entry.get("sha256")) or actual_bytes != int(entry.get("bytes", -1)):
            raise FailClosed("FAIL__POLICY_RECEIPT_IDENTITY_MISMATCH__NO_SCIENCE", {"receipt": name})
        receipt_hashes.update(name.encode("ascii"))
        receipt_hashes.update(actual_hash.encode("ascii"))
        receipt = json.loads(path.read_text(encoding="utf-8"))
        expected_index = list(np.unravel_index(flat, SHAPE, order="F"))
        result = receipt.get("selector_result", {})
        selected = result.get("selected")
        if (
            receipt.get("flat_index_f_zero_based") != flat
            or receipt.get("index_b_a_z_zero_based") != expected_index
            or result.get("outcome") != "SELECTED_ADMISSIBLE"
            or not isinstance(selected, dict)
        ):
            raise FailClosed("FAIL__POLICY_RECEIPT_CONTENT_MISMATCH__NO_SCIENCE", {"receipt": name})
        i_b, i_a, _ = expected_index
        g_b = float(selected["g_b"])
        g_a = float(selected["g_a"])
        for key, active, outward in (
            ("lower_b", i_b == 0, max(-g_b, 0.0)),
            ("upper_b", i_b == SHAPE[0] - 1, max(g_b, 0.0)),
            ("lower_a", i_a == 0, max(-g_a, 0.0)),
            ("upper_a", i_a == SHAPE[1] - 1, max(g_a, 0.0)),
        ):
            if active:
                face[key]["cells"] += 1
                face[key]["outward_drift_sum"] += outward
                face[key]["outward_rate_sum"] += outward

    if any(item["cells"] != 40 for item in face.values()):
        raise FailClosed("FAIL__FACE_RECEIPT_CARDINALITY_MISMATCH__NO_SCIENCE", face)
    if any(item["outward_rate_sum"] != 0.0 or item["outward_drift_sum"] != 0.0 for item in face.values()):
        raise FailClosed("FAIL__OUTWARD_FACE_FLUX_PRESENT__NO_SCIENCE", face)
    for item in face.values():
        item["outward_mass_flux_coefficient"] = 0.0

    return {
        "status": "PASS",
        "accepted_candidate": "9a4eb0e5ec3627743596daa9b991436d2124efa9",
        "q0": {"path": str(q0_path.relative_to(repository)), "bytes": Q0_BYTES, "sha256": Q0_SHA256},
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
            "ordered_name_and_sha256_digest": receipt_hashes.hexdigest().upper(),
        },
        "state_contract": {
            "shape_b_a_z": list(SHAPE),
            "flatten_order": "F",
            "fastest_dimension": "b",
            "omega": OMEGA,
            "forward_stationarity": "Q0.T @ p = 0",
        },
        "outside_domain_flux_ledger_before_svd": face,
        "q0_sparse_loads": 0,
        "scientific_calls": 0,
    }


def _exact_positive_adjacency(q: sparse.csr_matrix) -> sparse.csr_matrix:
    off = q.copy()
    off.setdiag(0.0)
    off.eliminate_zeros()
    if off.nnz and np.any(off.data < 0.0):
        raise FailClosed("FAIL__NEGATIVE_OFFDIAGONAL__NO_SVD")
    data = np.ones(off.nnz, dtype=np.int8)
    return sparse.csr_matrix((data, off.indices.copy(), off.indptr.copy()), shape=off.shape)


def _closed_component_receipt(
    adjacency: sparse.csr_matrix, component_count: int, labels: np.ndarray
) -> dict[str, Any]:
    closed = np.ones(component_count, dtype=bool)
    for origin in range(N):
        origin_component = int(labels[origin])
        for destination in adjacency.indices[adjacency.indptr[origin] : adjacency.indptr[origin + 1]]:
            if int(labels[int(destination)]) != origin_component:
                closed[origin_component] = False
    sizes = np.bincount(labels, minlength=component_count)
    closed_labels = np.flatnonzero(closed)
    closed_size = int(np.sum(sizes[closed_labels]))
    return {
        "component_count": int(component_count),
        "component_sizes_by_label": [int(value) for value in sizes],
        "closed_component_labels": [int(value) for value in closed_labels],
        "closed_component_count": int(closed_labels.size),
        "closed_component_sizes": [int(sizes[value]) for value in closed_labels],
        "transient_state_count": int(N - closed_size),
        "exact_positive_edge_count": int(adjacency.nnz),
        "edge_rule": "Q0[i,j] > 0 exactly, offdiagonal only",
    }


def _normalize_null_vector(vector: np.ndarray) -> tuple[np.ndarray, dict[str, Any]]:
    v = np.asarray(vector, dtype=float).copy()
    absolute_sum = math.fsum(abs(float(value)) for value in v)
    raw_sum = math.fsum(float(value) for value in v)
    tau_sum = gamma(N) * max(1.0, absolute_sum)
    if not math.isfinite(raw_sum) or abs(raw_sum) <= tau_sum:
        raise FailClosed(
            "FAIL__NULL_VECTOR_SUM_NOT_SEPARATED_FROM_ZERO__NO_RETRY",
            {"raw_sum": raw_sum, "tau_sum": tau_sum},
        )
    sign_reversed = raw_sum < 0.0
    if sign_reversed:
        v = -v
    oriented_sum = math.fsum(float(value) for value in v)
    p = v / oriented_sum
    return p, {
        "raw_math_fsum": raw_sum,
        "sum_abs_v": absolute_sum,
        "tau_sum": tau_sum,
        "strict_sum_separation": True,
        "global_sign_reversed": sign_reversed,
        "oriented_math_fsum": oriented_sum,
        "normalizations": 1,
    }


def _rank_receipt(singular_values: np.ndarray) -> dict[str, Any]:
    s = np.asarray(singular_values, dtype=float)
    if s.shape != (N,) or not np.all(np.isfinite(s)):
        raise FailClosed("FAIL__SVD_SINGULAR_VALUES_INVALID__NO_RETRY")
    sigma_max = float(s[0])
    tau_rank = gamma(N + 64) * max(1.0, sigma_max)
    nullity = int(np.count_nonzero(s <= tau_rank))
    rank = N - nullity
    second_smallest = float(s[-2])
    smallest = float(s[-1])
    return {
        "sigma_max": sigma_max,
        "second_smallest": second_smallest,
        "smallest": smallest,
        "tau_rank": tau_rank,
        "second_smallest_over_tau_rank": second_smallest / tau_rank,
        "smallest_over_tau_rank": smallest / tau_rank,
        "numerical_rank": rank,
        "numerical_nullity": nullity,
        "second_smallest_strictly_above_tau_rank": second_smallest > tau_rank,
        "singular_values_sha256": _array_sha256(s),
    }


def _seal_manifest(evidence: Path) -> None:
    entries = []
    for path in sorted(item for item in evidence.iterdir() if item.name != "sealed_manifest.json"):
        if path.is_file():
            entries.append(
                {"path": path.name, "bytes": path.stat().st_size, "sha256": _sha256(path)}
            )
    _write_json(
        evidence / "sealed_manifest.json",
        {
            "schema": "CH5_MP4C_2018_KFE_D123_CORRECTED_Q0_KFE_OPERATOR_VALIDATION_V1",
            "entry_count": len(entries),
            "total_bytes": sum(int(entry["bytes"]) for entry in entries),
            "entries": entries,
        },
    )


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
                "git_head_before_q0_load": _git_head(repository),
                "scientific_code_sha256_before_q0_load": pre_hashes,
                "q0_sha256": Q0_SHA256,
                "frozen_budget": {
                    "q0_loads": 1,
                    "structural_conservation_audits": 1,
                    "scc_decompositions": 1,
                    "dense_gesvd": 1,
                    "normalized_stationary_candidates": 1,
                    "q0_times_one": 1,
                    "q0_transpose_times_p": 1,
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
        q_path = repository / ACCEPTED_RELATIVE / "d2_generator.npz"
        ledger.q0_loads += 1
        q_loaded = sparse.load_npz(q_path)
        if getattr(q_loaded, "format", None) != "csr":
            raise FailClosed("FAIL__Q0_NOT_CSR__NO_SVD")
        q = sparse.csr_matrix(q_loaded, copy=False)

        ledger.structural_conservation_audits += 1
        if q.shape != (N, N) or not np.all(np.isfinite(q.data)):
            raise FailClosed("FAIL__Q0_SHAPE_OR_FINITE_AUDIT__NO_SVD")
        adjacency = _exact_positive_adjacency(q)
        off = q.copy()
        off.setdiag(0.0)
        off.eliminate_zeros()
        outgoing = np.asarray(off.sum(axis=1)).ravel()
        diagonal_error = q.diagonal() + outgoing
        diagonal_error_max = float(np.max(np.abs(diagonal_error), initial=0.0))
        ledger.q0_times_one += 1
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
            "diagonal_construction_error_max": diagonal_error_max,
            "diagonal_construction_error_exact_zero": diagonal_error_max == 0.0,
            "max_abs_q0_times_one": q_one_max,
            "q0_times_one_bound": Q_ONE_BOUND,
            "q0_times_one_passes": q_one_max <= Q_ONE_BOUND,
            "q0_times_one_sha256": _array_sha256(q_one),
            "outside_domain_flux_ledger": preflight["outside_domain_flux_ledger_before_svd"],
        }
        if diagonal_error_max != 0.0 or q_one_max > Q_ONE_BOUND:
            structural["status"] = "FAIL"
            _write_json(evidence / "structural_conservation_receipt.json", structural)
            raise FailClosed("FAIL__Q0_STRUCTURAL_OR_CONSERVATION_AUDIT__NO_SVD", structural)
        _write_json(evidence / "structural_conservation_receipt.json", structural)
        _require_resource_budget(started)

        ledger.scc_decompositions += 1
        component_count, labels = csgraph.connected_components(
            adjacency, directed=True, connection="strong", return_labels=True
        )
        scc = _closed_component_receipt(adjacency, int(component_count), labels)
        scc["status"] = "PASS" if scc["closed_component_count"] == 1 else "FAIL"
        scc["labels_sha256"] = _array_sha256(labels, "<i8")
        _write_json(evidence / "scc_receipt.json", scc)
        if scc["closed_component_count"] != 1:
            raise FailClosed("FAIL__CLOSED_COMMUNICATING_CLASS_COUNT__NO_SVD", scc)
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
            {"category": item.category.__name__, "message": str(item.message)}
            for item in caught
        ]
        rank = _rank_receipt(singular_values)
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
        if warning_receipt or rank["numerical_rank"] != 799 or rank["numerical_nullity"] != 1 or not rank["second_smallest_strictly_above_tau_rank"]:
            rank["status"] = "FAIL"
            _write_json(evidence / "svd_rank_receipt.json", rank)
            raise FailClosed("FAIL__SVD_RANK_NULLITY_CONTRACT__NO_RETRY", rank)
        if scc["closed_component_count"] != rank["numerical_nullity"]:
            rank["status"] = "FAIL_GRAPH_NUMERICAL_DISAGREEMENT"
            _write_json(evidence / "svd_rank_receipt.json", rank)
            raise FailClosed("FAIL__GRAPH_NUMERICAL_NULLITY_DISAGREEMENT__NO_RETRY", rank)
        _write_json(evidence / "svd_rank_receipt.json", rank)
        _require_resource_budget(started)

        p, orientation = _normalize_null_vector(vh[-1, :])
        ledger.normalized_stationary_candidates += 1
        g = p / OMEGA
        if not np.all(np.isfinite(p)) or not np.all(np.isfinite(g)):
            raise FailClosed("FAIL__NORMALIZED_MASS_NONFINITE__NO_RETRY")
        ledger.q0_transpose_times_p += 1
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
            "q0_one_dot_p_within_global_source_bound": abs(q_one_dot_p) <= source_bound,
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
                "dot_q0_times_one_p": q_one_dot_p,
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
            q0_times_one=q_one,
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
        resources = _require_resource_budget(started)
        _write_json(evidence / "resource_receipt.json", resources)
        terminal = "PASS__ACCEPTED_Q0_UNIQUE_SOURCE_FREE_NORMALIZED_NONNEGATIVE_INVARIANT_MASS"
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
