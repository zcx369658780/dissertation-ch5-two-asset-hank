"""One-shot Beijing unique-closed-class KFE method-candidate diagnostic.

The implementation is opt-in and task-local.  It never changes the accepted
KFE implementation or any predecessor evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
from typing import Any
import warnings

import numpy as np
from scipy import linalg, sparse


TASK_ID = "CH5_MP4C_CORRECTED_OPTIONB_BEIJING_UNIQUE_CLOSED_CLASS_KFE_METHOD_CANDIDATE_DIAGNOSTIC_20260920"
BASELINE_SHA = "39ea65985cab75f99c820bf9b9c7004bc8cc76b7"
PASS_TERMINAL = "PASS__UNIQUE_CLOSED_CLASS_RESTRICTED_KFE_CANDIDATE_DIAGNOSTIC__OWNER_METHOD_ADOPTION_DECISION_REQUIRED"
FAIL_TERMINAL = "FAIL__UNIQUE_CLOSED_CLASS_RESTRICTED_KFE_CANDIDATE_DIAGNOSTIC__METHOD_NOT_SUPPORTED"

RUN003_ROOT_RELATIVE = Path(
    "reports/ch5_mp4c_corrected_optionb_initial_turn_31_province_household_kfe_"
    "k1a_c1_one_turn_integration_20260920_run003"
)
FORENSIC_ROOT_RELATIVE = Path(
    "reports/ch5_mp4c_corrected_optionb_run003_stationary_mass_negativity_"
    "support_forensic_20260920_run001"
)
OUTPUT_ROOT_RELATIVE = Path(
    "reports/ch5_mp4c_corrected_optionb_beijing_unique_closed_class_kfe_"
    "candidate_20260920_run001"
)
REPORT_RELATIVE = Path(
    "docs/CH5_MP4C_CORRECTED_OPTIONB_BEIJING_UNIQUE_CLOSED_CLASS_KFE_METHOD_"
    "CANDIDATE_DIAGNOSTIC_REPORT.md"
)

RUN003_MANIFEST_SHA256 = "18D62A1E388E17D3D0A7001D22998B86389C946B7136D481FB7DE11777A3388B"
FORENSIC_MANIFEST_SHA256 = "E8E346EAFD41A41362B55D479CA1014A124C28724CB7625BABE262F01B691242"
Q_SHA256 = "E1F55D0B755CB83D4F6A3CB4FEFD6DBC8CD4F05C6D23FC5DE00302E16B74BF20"
RUN003_MASS_SHA256 = "15C6D7B24375A20CADB8C871527C75B7447EE9397FCAA44C72FCFC26D064E436"
RUN003_P_SHA256 = "F29C4A816652520ABB678301976BA8D3B62773652546B6434BB05674A88DF1CC"
ACCEPTED_FULL_TAU_RANK = 3.735954297981181e-12
Q_CONSERVATION_BOUND = 1.9355021455918682e-14
N_FULL = 800
N_CLOSED = 400
EXPECTED_CLOSED = tuple(range(200, 400)) + tuple(range(600, 800))


def file_sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()


def field_sha256(values: np.ndarray, dtype: str = "<f8") -> str:
    return hashlib.sha256(np.asarray(values, dtype=dtype).tobytes(order="F")).hexdigest().upper()


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def gamma(count: int) -> float:
    eps = np.finfo(float).eps
    return float(count * eps / (1.0 - count * eps))


def stable_csr_row_sums(matrix: sparse.csr_matrix) -> np.ndarray:
    matrix = sparse.csr_matrix(matrix)
    return np.asarray(
        [
            math.fsum(float(value) for value in matrix.data[matrix.indptr[i] : matrix.indptr[i + 1]])
            for i in range(matrix.shape[0])
        ],
        dtype=np.float64,
    )


def threshold_view(singular_values: np.ndarray, dimension: int) -> dict[str, Any]:
    values = np.asarray(singular_values, dtype=np.float64)
    if values.shape != (N_CLOSED,) or not np.all(np.isfinite(values)):
        raise ValueError("restricted singular values must be finite length 400")
    sigma_max = float(values[0])
    tau = gamma(dimension + 64) * max(1.0, sigma_max)
    nullity = int(np.count_nonzero(values <= tau))
    return {
        "dimension_in_gamma": dimension,
        "gamma_count": dimension + 64,
        "sigma_max": sigma_max,
        "tau_rank": tau,
        "numerical_rank": N_CLOSED - nullity,
        "numerical_nullity": nullity,
        "second_smallest": float(values[-2]),
        "smallest": float(values[-1]),
        "second_smallest_over_tau_rank": float(values[-2] / tau),
        "smallest_over_tau_rank": float(values[-1] / tau),
    }


def orient_and_normalize(vector: np.ndarray) -> tuple[np.ndarray, dict[str, Any]]:
    candidate = np.asarray(vector, dtype=np.float64).copy()
    if candidate.shape != (N_CLOSED,) or not np.all(np.isfinite(candidate)):
        raise ValueError("smallest right singular vector is invalid")
    absolute_sum = math.fsum(abs(float(value)) for value in candidate)
    raw_sum = math.fsum(float(value) for value in candidate)
    tau_sum = gamma(N_CLOSED) * max(1.0, absolute_sum)
    if not math.isfinite(raw_sum) or abs(raw_sum) <= tau_sum:
        raise ValueError("restricted null-vector sum is not separated from zero")
    sign_reversed = raw_sum < 0.0
    if sign_reversed:
        candidate = -candidate
    oriented_sum = math.fsum(float(value) for value in candidate)
    normalized = candidate / oriented_sum
    return normalized, {
        "orientation_calls": 1,
        "global_sign_reversed": sign_reversed,
        "raw_math_fsum": raw_sum,
        "sum_abs_v": absolute_sum,
        "tau_sum_local_dimension": tau_sum,
        "strict_sum_separation": True,
        "oriented_math_fsum": oriented_sum,
        "normalization_calls": 1,
    }


def structural_receipt(
    q: sparse.csr_matrix,
    closed: np.ndarray,
    transient: np.ndarray,
) -> tuple[sparse.csr_matrix, dict[str, Any]]:
    q = sparse.csr_matrix(q)
    q_cc = q[closed, :][:, closed].tocsr()
    q_ct = q[closed, :][:, transient].tocsr()
    positive_outgoing = q_ct.data[q_ct.data > 0.0]
    row_sums = stable_csr_row_sums(q_cc)
    off = q_cc.copy()
    off.setdiag(0.0)
    off.eliminate_zeros()
    receipt = {
        "q_full_shape": list(q.shape),
        "q_full_data_finite": bool(np.all(np.isfinite(q.data))),
        "q_cc_shape": list(q_cc.shape),
        "q_cc_data_finite": bool(np.all(np.isfinite(q_cc.data))),
        "q_cc_nnz": int(q_cc.nnz),
        "q_cc_minimum_offdiagonal": float(np.min(off.data)) if off.nnz else 0.0,
        "closed_to_transient_stored_nnz": int(q_ct.nnz),
        "closed_to_transient_positive_count": int(positive_outgoing.size),
        "closed_to_transient_positive_rate_sum": float(
            math.fsum(float(value) for value in positive_outgoing)
        ),
        "closed_to_transient_maximum_positive_rate": (
            float(np.max(positive_outgoing)) if positive_outgoing.size else 0.0
        ),
        "q_cc_maximum_absolute_stable_row_sum": float(np.max(np.abs(row_sums))),
        "accepted_q_arithmetic_conservation_bound": Q_CONSERVATION_BOUND,
        "q_cc_stable_row_sums_sha256": field_sha256(row_sums),
    }
    receipt["checks"] = {
        "q_full_shape_800x800": q.shape == (N_FULL, N_FULL),
        "q_full_finite": receipt["q_full_data_finite"],
        "q_cc_shape_400x400": q_cc.shape == (N_CLOSED, N_CLOSED),
        "q_cc_finite": receipt["q_cc_data_finite"],
        "no_positive_closed_to_transient_outgoing_rate": positive_outgoing.size == 0,
        "q_cc_row_conservation_within_accepted_scale": (
            receipt["q_cc_maximum_absolute_stable_row_sum"] <= Q_CONSERVATION_BOUND
        ),
        "q_cc_offdiagonals_nonnegative": bool(not off.nnz or np.all(off.data >= 0.0)),
    }
    receipt["status"] = "PASS" if all(receipt["checks"].values()) else "FAIL"
    return q_cc, receipt


def candidate_statistics(candidate: np.ndarray) -> dict[str, Any]:
    values = np.asarray(candidate, dtype=np.float64)
    negative = values[values < 0.0]
    l1 = math.fsum(abs(float(value)) for value in values)
    total = math.fsum(float(value) for value in values)
    normalization_bound = gamma(values.size) * max(1.0, l1)
    receipt = {
        "finite": bool(np.all(np.isfinite(values))),
        "math_fsum": total,
        "normalization_bound": normalization_bound,
        "minimum": float(np.min(values)),
        "maximum": float(np.max(values)),
        "negative_entry_count": int(negative.size),
        "total_negative_mass": float(math.fsum(-float(value) for value in negative)),
        "l1_mass": float(l1),
        "p_sha256": field_sha256(values),
    }
    receipt["checks"] = {
        "finite": receipt["finite"],
        "normalized_within_arithmetic_bound": abs(total - 1.0) <= normalization_bound,
        "minimum_strictly_positive": receipt["minimum"] > 0.0,
        "negative_entry_count_zero": receipt["negative_entry_count"] == 0,
        "total_negative_mass_zero": receipt["total_negative_mass"] == 0.0,
    }
    receipt["status"] = "PASS" if all(receipt["checks"].values()) else "FAIL"
    return receipt


def embedded_statistics(
    p_full: np.ndarray,
    p_closed: np.ndarray,
    closed: np.ndarray,
    transient: np.ndarray,
) -> dict[str, Any]:
    transient_values = p_full[transient]
    closed_values = p_full[closed]
    total = math.fsum(float(value) for value in p_full)
    l1 = math.fsum(abs(float(value)) for value in p_full)
    bound = gamma(N_FULL) * max(1.0, l1)
    negative = p_full[p_full < 0.0]
    transient_bits = np.asarray(transient_values, dtype="<f8").view("<u8")
    receipt = {
        "finite": bool(np.all(np.isfinite(p_full))),
        "state_count": int(p_full.size),
        "closed_entry_count": int(closed_values.size),
        "transient_entry_count": int(transient_values.size),
        "transient_exact_numeric_zero_count": int(np.count_nonzero(transient_values == 0.0)),
        "transient_positive_zero_bit_pattern_count": int(np.count_nonzero(transient_bits == 0)),
        "closed_exact_candidate_match": bool(np.array_equal(closed_values, p_closed)),
        "math_fsum": total,
        "normalization_bound": bound,
        "minimum": float(np.min(p_full)),
        "maximum": float(np.max(p_full)),
        "negative_entry_count": int(negative.size),
        "total_negative_mass": float(math.fsum(-float(value) for value in negative)),
        "l1_mass": float(l1),
        "p_full_sha256": field_sha256(p_full),
    }
    receipt["checks"] = {
        "finite": receipt["finite"],
        "exactly_400_transient_entries": transient_values.size == N_CLOSED,
        "all_transient_entries_bitwise_positive_zero": (
            receipt["transient_positive_zero_bit_pattern_count"] == N_CLOSED
        ),
        "exactly_400_closed_entries": closed_values.size == N_CLOSED,
        "closed_entries_equal_restricted_candidate": receipt["closed_exact_candidate_match"],
        "normalized_within_arithmetic_bound": abs(total - 1.0) <= bound,
        "negative_entry_count_zero": receipt["negative_entry_count"] == 0,
    }
    receipt["status"] = "PASS" if all(receipt["checks"].values()) else "FAIL"
    return receipt


def stationarity_receipt(
    q: sparse.csr_matrix,
    p_full: np.ndarray,
    residual: np.ndarray,
) -> dict[str, Any]:
    a_inf = float(np.max(np.asarray(abs(q.transpose()).sum(axis=1)).ravel(), initial=0.0))
    p_inf = float(np.linalg.norm(p_full, ord=np.inf))
    residual_inf = float(np.linalg.norm(residual, ord=np.inf))
    residual_l1 = float(math.fsum(abs(float(value)) for value in residual))
    scale = max(1.0, a_inf * p_inf)
    backward_ratio = residual_inf / scale
    tau_stationarity = gamma(N_FULL + 64) * scale
    residual_sum = float(math.fsum(float(value) for value in residual))
    q_one = stable_csr_row_sums(q)
    q_one_dot_p = float(
        math.fsum(float(q_one[i]) * float(p_full[i]) for i in range(N_FULL))
    )
    discrepancy = abs(residual_sum - q_one_dot_p)
    source_bound = gamma(N_FULL + 64) * max(1.0, N_FULL * a_inf * p_inf)
    receipt = {
        "q_transpose_p_calls": 1,
        "residual_infinity_norm": residual_inf,
        "residual_l1_norm": residual_l1,
        "signed_math_fsum_residual": residual_sum,
        "a_infinity_norm": a_inf,
        "p_infinity_norm": p_inf,
        "normwise_scale": scale,
        "normwise_backward_ratio": backward_ratio,
        "gamma_864": gamma(N_FULL + 64),
        "tau_stationarity": tau_stationarity,
        "q_one_stable_row_sums_sha256": field_sha256(q_one),
        "maximum_absolute_q_one": float(np.max(np.abs(q_one))),
        "dot_q_one_p": q_one_dot_p,
        "source_identity_discrepancy": discrepancy,
        "source_bound": source_bound,
        "residual_sha256": field_sha256(residual),
    }
    receipt["checks"] = {
        "residual_finite": bool(np.all(np.isfinite(residual))),
        "stationarity_inf_within_bound": residual_inf <= tau_stationarity,
        "normwise_backward_ratio_within_gamma_864": backward_ratio <= gamma(N_FULL + 64),
        "residual_sum_within_global_source_bound": abs(residual_sum) <= source_bound,
        "q_one_dot_p_within_global_source_bound": abs(q_one_dot_p) <= source_bound,
        "source_identity_discrepancy_within_bound": discrepancy <= source_bound,
        "q_one_within_accepted_conservation_bound": (
            receipt["maximum_absolute_q_one"] <= Q_CONSERVATION_BOUND
        ),
    }
    receipt["status"] = "PASS" if all(receipt["checks"].values()) else "FAIL"
    return receipt


def scientific_ledger() -> dict[str, Any]:
    return {
        "schema": "CH5_MP4C_BEIJING_UNIQUE_CLOSED_CLASS_KFE_CANDIDATE_LEDGER_V1",
        "q12_artifact_loads": 0,
        "topology_scc_recomputations": 0,
        "hjb_policy_d2_calls": 0,
        "restricted_dense_gesvd_calls": 0,
        "normalized_stationary_candidates": 0,
        "full_q_transpose_p_calls": 0,
        "full_space_800x800_gesvd_calls": 0,
        "alternate_svd_eigen_nullspace_calls": 0,
        "scientific_retries": 0,
        "clipping_projection_of_run003_p_calls": 0,
        "aggregate_k1a_c1_firm_outer_calls": 0,
        "matlab_ge_annual_shock_irf_welfare_results_calls": 0,
        "remaining_province_household_runs": 0,
        "turn2_calls": 0,
    }


def git_blob_bytes(repository: Path, relative: Path) -> bytes:
    return subprocess.check_output(
        ["git", "show", f"HEAD:{relative.as_posix()}"], cwd=repository
    )


def verify_git_manifest(
    repository: Path, root_relative: Path, expected_sha256: str
) -> dict[str, Any]:
    manifest_relative = root_relative / "sealed_manifest.json"
    canonical = git_blob_bytes(repository, manifest_relative)
    manifest = json.loads(canonical)
    bad_paths = []
    for entry in manifest["entries"]:
        content = git_blob_bytes(repository, root_relative / entry["path"])
        actual_hash = hashlib.sha256(content).hexdigest().upper()
        if actual_hash != entry["sha256"] or len(content) != entry["bytes"]:
            bad_paths.append(entry["path"])
    actual = hashlib.sha256(canonical).hexdigest().upper()
    return {
        "canonical_git_blob_sha256": actual,
        "expected_sha256": expected_sha256,
        "working_tree_sha256": file_sha256(repository / manifest_relative),
        "core_autocrlf": subprocess.run(
            ["git", "config", "--get", "core.autocrlf"],
            cwd=repository, text=True, capture_output=True, check=False,
        ).stdout.strip(),
        "entry_count": len(manifest["entries"]),
        "total_bytes": sum(int(row["bytes"]) for row in manifest["entries"]),
        "bad_paths": bad_paths,
        "status": "PASS" if actual == expected_sha256 and not bad_paths else "FAIL",
    }


def verify_file_manifest(root: Path, expected_sha256: str) -> dict[str, Any]:
    path = root / "sealed_manifest.json"
    manifest = read_json(path)
    bad_paths = []
    for entry in manifest["entries"]:
        target = root / entry["path"]
        if (
            not target.is_file()
            or target.stat().st_size != entry["bytes"]
            or file_sha256(target) != entry["sha256"]
        ):
            bad_paths.append(entry["path"])
    actual = file_sha256(path)
    return {
        "actual_sha256": actual,
        "expected_sha256": expected_sha256,
        "entry_count": len(manifest["entries"]),
        "total_bytes": sum(int(row["bytes"]) for row in manifest["entries"]),
        "bad_paths": bad_paths,
        "status": "PASS" if actual == expected_sha256 and not bad_paths else "FAIL",
    }


def seal(root: Path) -> dict[str, Any]:
    excluded = {"sealed_manifest.json", "independent_readback_receipt.json"}
    entries = []
    for path in sorted(item for item in root.iterdir() if item.is_file() and item.name not in excluded):
        entries.append(
            {"path": path.name, "bytes": path.stat().st_size, "sha256": file_sha256(path)}
        )
    return {
        "schema": "CH5_MP4C_BEIJING_UNIQUE_CLOSED_CLASS_KFE_CANDIDATE_SEALED_MANIFEST_V1",
        "entry_count": len(entries),
        "total_bytes": sum(int(row["bytes"]) for row in entries),
        "entries": entries,
    }


def readback(root: Path) -> dict[str, Any]:
    manifest_path = root / "sealed_manifest.json"
    manifest = read_json(manifest_path)
    bad_paths = []
    for entry in manifest["entries"]:
        target = root / entry["path"]
        if (
            not target.is_file()
            or target.stat().st_size != entry["bytes"]
            or file_sha256(target) != entry["sha256"]
        ):
            bad_paths.append(entry["path"])
    passed = (
        not bad_paths
        and manifest["entry_count"] == len(manifest["entries"])
        and manifest["total_bytes"] == sum(int(row["bytes"]) for row in manifest["entries"])
    )
    return {
        "status": "PASS" if passed else "FAIL",
        "manifest_sha256": file_sha256(manifest_path),
        "entry_count": len(manifest["entries"]),
        "total_bytes": sum(int(row["bytes"]) for row in manifest["entries"]),
        "bad_paths": bad_paths,
    }


def write_report(
    report_path: Path,
    terminal: str,
    structure: dict[str, Any],
    rank: dict[str, Any],
    candidate: dict[str, Any],
    embedded: dict[str, Any],
    stationarity: dict[str, Any],
    comparison: dict[str, Any],
) -> None:
    local = rank["local_dimension_threshold_view"]
    inherited = rank["inherited_full_space_dimension_threshold_view"]
    lines = [
        "# Chapter 5 Beijing unique-closed-class KFE method-candidate diagnostic", "",
        "## Terminal classification", "", f"`{terminal}`", "",
        "This is a numerical-method candidate diagnostic only. The accepted KFE method remains unchanged and the 31-province run was not reopened.", "",
        "## Q_CC structural checks", "",
        f"- Shape: `{structure['q_cc_shape']}`; nnz: `{structure['q_cc_nnz']}`; finite: `{structure['q_cc_data_finite']}`.",
        f"- Closed-to-transient positive outgoing count/rate: `{structure['closed_to_transient_positive_count']}` / `{structure['closed_to_transient_positive_rate_sum']:.17g}`.",
        f"- Maximum absolute stable Q_CC row sum: `{structure['q_cc_maximum_absolute_stable_row_sum']:.17g}` against `{structure['accepted_q_arithmetic_conservation_bound']:.17g}`.", "",
        "## Restricted GESVD", "",
        f"- sigma_max: `{rank['sigma_max']:.17g}`; second-smallest: `{rank['second_smallest']:.17g}`; smallest: `{rank['smallest']:.17g}`.",
        f"- Local 400 threshold: `{local['tau_rank']:.17g}` -> rank/nullity `{local['numerical_rank']}/{local['numerical_nullity']}`.",
        f"- Inherited 800-dimension convention: `{inherited['tau_rank']:.17g}` -> rank/nullity `{inherited['numerical_rank']}/{inherited['numerical_nullity']}`.", "",
        "## Restricted and embedded candidates", "",
        f"- Closed candidate min/max: `{candidate['minimum']:.17g}` / `{candidate['maximum']:.17g}`; negative count `{candidate['negative_entry_count']}`; math.fsum `{candidate['math_fsum']:.17g}`.",
        f"- Embedded transient positive-zero bit patterns: `{embedded['transient_positive_zero_bit_pattern_count']}/400`; negative count `{embedded['negative_entry_count']}`; math.fsum `{embedded['math_fsum']:.17g}`.", "",
        "## One full-Q stationarity validation", "",
        f"- Residual infinity/L1: `{stationarity['residual_infinity_norm']:.17g}` / `{stationarity['residual_l1_norm']:.17g}`.",
        f"- Signed residual sum: `{stationarity['signed_math_fsum_residual']:.17g}`; normwise backward ratio: `{stationarity['normwise_backward_ratio']:.17g}`.",
        f"- Frozen stationarity bound: `{stationarity['tau_stationarity']:.17g}`; source identity discrepancy: `{stationarity['source_identity_discrepancy']:.17g}`.", "",
        "## Comparison with persisted run003 full-space p", "",
        f"- Run003 transient signed/L1 mass: `{comparison['run003_transient_signed_mass']:.17g}` / `{comparison['run003_transient_l1_mass']:.17g}`.",
        f"- Closed max-abs/L1 difference: `{comparison['closed_maximum_absolute_difference']:.17g}` / `{comparison['closed_l1_difference']:.17g}`.",
        f"- Closed cosine similarity: `{comparison['closed_cosine_similarity']:.17g}`.",
        f"- Mass-accounting discrepancy after transient leakage identity: `{comparison['mass_accounting_discrepancy']:.17g}`.", "",
        "All task-forbidden calls are zero. Exactly one restricted GESVD, one orientation, one normalization, and one original full-Q `Q.T@p_full` were executed. No method adoption occurred.", "",
    ]
    report_path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def execute(repository: Path, output: Path, report_path: Path) -> dict[str, Any]:
    if output.exists():
        raise FileExistsError(f"fresh evidence root required: {output}")
    output.mkdir(parents=True)
    ledger = scientific_ledger()

    run_root = repository / RUN003_ROOT_RELATIVE
    forensic_root = repository / FORENSIC_ROOT_RELATIVE
    checkpoint = run_root / "household/p00_北京/checkpoint_012"
    terminal_kfe = run_root / "household/p00_北京/terminal_kfe"
    q_path = checkpoint / "q_generator.npz"
    mass_path = terminal_kfe / "stationary_mass_arrays.npz"
    topology = read_json(terminal_kfe / "topology_receipt.json")
    full_rank = read_json(terminal_kfe / "svd_rank_nullity_receipt.json")
    checkpoint_manifest = read_json(checkpoint / "checkpoint_manifest.json")
    forensic_terminal = read_json(forensic_root / "terminal_classification.json")
    forensic_stats = read_json(forensic_root / "group_statistics.json")["groups"]
    forensic_mask = read_json(forensic_root / "closed_transient_mask_receipt.json")

    run_manifest = verify_file_manifest(run_root, RUN003_MANIFEST_SHA256)
    forensic_manifest = verify_git_manifest(
        repository, FORENSIC_ROOT_RELATIVE, FORENSIC_MANIFEST_SHA256
    )
    closed_members = tuple(int(value) for group in topology["closed_members"] for value in group)
    authority_checks = {
        "run003_manifest_pass": run_manifest["status"] == "PASS",
        "support_forensic_canonical_git_manifest_pass": forensic_manifest["status"] == "PASS",
        "q12_artifact_sha256_match": file_sha256(q_path) == Q_SHA256,
        "run003_mass_artifact_sha256_match": file_sha256(mass_path) == RUN003_MASS_SHA256,
        "checkpoint_12": checkpoint_manifest.get("checkpoint") == 12,
        "checkpoint_q_identity_match": (
            checkpoint_manifest.get("d2_receipt", {}).get("q_artifact", {}).get("sha256") == Q_SHA256
        ),
        "topology_unique_closed_class": topology.get("closed_class_count") == 1,
        "closed_members_exact": closed_members == EXPECTED_CLOSED,
        "closed_size_400": len(closed_members) == N_CLOSED,
        "transient_size_400": topology.get("transient_state_count") == N_CLOSED,
        "full_space_rank_nullity_799_1": (
            full_rank.get("numerical_rank") == 799 and full_rank.get("numerical_nullity") == 1
        ),
        "forensic_classification_a": forensic_terminal.get("classification_a_condition") is True,
        "forensic_closed_breaches_zero": forensic_stats["closed"]["below_negative_tau_breach_count"] == 0,
        "forensic_closed_all_positive": forensic_stats["closed"]["positive_count"] == N_CLOSED,
        "forensic_mask_matches_topology": tuple(forensic_mask["closed_members"]) == closed_members,
    }
    authority = {
        "schema": "CH5_MP4C_BEIJING_UNIQUE_CLOSED_CLASS_KFE_CANDIDATE_AUTHORITY_V1",
        "task_id": TASK_ID,
        "actual_live_main_baseline": BASELINE_SHA,
        "run003_manifest": run_manifest,
        "support_forensic_manifest": forensic_manifest,
        "q12_artifact_sha256": file_sha256(q_path),
        "run003_mass_artifact_sha256": file_sha256(mass_path),
        "checks": authority_checks,
        "status": "PASS" if all(authority_checks.values()) else "FAIL",
    }
    write_json(output / "authority_binding.json", authority)
    if authority["status"] != "PASS":
        raise RuntimeError("input authority binding failed before scientific execution")

    closed = np.asarray(closed_members, dtype=np.int64)
    closed_mask = np.zeros(N_FULL, dtype=bool)
    closed_mask[closed] = True
    transient = np.flatnonzero(~closed_mask)
    index_receipt = {
        "source": "persisted topology_receipt.closed_members exact stored order",
        "closed_count": int(closed.size),
        "transient_count": int(transient.size),
        "closed_members": closed.astype(int).tolist(),
        "closed_members_sha256_little_endian_int64": hashlib.sha256(
            np.asarray(closed, dtype="<i8").tobytes()
        ).hexdigest().upper(),
        "transient_members_sha256_little_endian_int64": hashlib.sha256(
            np.asarray(transient, dtype="<i8").tobytes()
        ).hexdigest().upper(),
        "topology_scc_recomputations": 0,
    }
    write_json(output / "closed_transient_index_receipt.json", index_receipt)

    ledger["q12_artifact_loads"] += 1
    q = sparse.load_npz(q_path).tocsr()
    q_cc, structure = structural_receipt(q, closed, transient)
    write_json(output / "q_cc_structural_receipt.json", structure)
    if structure["status"] != "PASS":
        raise RuntimeError(FAIL_TERMINAL)

    ledger["restricted_dense_gesvd_calls"] += 1
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        _u, singular_values, vh = linalg.svd(
            q_cc.transpose().toarray(),
            full_matrices=True,
            lapack_driver="gesvd",
            check_finite=True,
        )
    warning_rows = [
        {"category": row.category.__name__, "message": str(row.message)} for row in caught
    ]
    local_view = threshold_view(singular_values, N_CLOSED)
    inherited_view = threshold_view(singular_values, N_FULL)
    rank = {
        "solver": "scipy.linalg.svd",
        "lapack_driver": "gesvd",
        "full_matrices": True,
        "check_finite": True,
        "restricted_dense_gesvd_calls": 1,
        "singular_value_count": int(singular_values.size),
        "singular_values_sha256": field_sha256(singular_values),
        "sigma_max": float(singular_values[0]),
        "second_smallest": float(singular_values[-2]),
        "smallest": float(singular_values[-1]),
        "local_dimension_threshold_view": local_view,
        "inherited_full_space_dimension_threshold_view": inherited_view,
        "accepted_full_space_tau_rank_reference": ACCEPTED_FULL_TAU_RANK,
        "warnings": warning_rows,
    }
    rank["checks"] = {
        "no_warnings": not warning_rows,
        "local_rank_nullity_399_1": (
            local_view["numerical_rank"] == 399 and local_view["numerical_nullity"] == 1
        ),
        "inherited_rank_nullity_399_1": (
            inherited_view["numerical_rank"] == 399
            and inherited_view["numerical_nullity"] == 1
        ),
    }
    rank["status"] = "PASS" if all(rank["checks"].values()) else "FAIL"
    np.savez_compressed(output / "restricted_singular_spectrum.npz", singular_values=singular_values)
    write_json(output / "restricted_gesvd_rank_nullity_receipt.json", rank)
    if rank["status"] != "PASS":
        raise RuntimeError(FAIL_TERMINAL)

    ledger["normalized_stationary_candidates"] += 1
    p_closed, orientation = orient_and_normalize(vh[-1, :])
    closed_candidate = candidate_statistics(p_closed)
    closed_candidate["orientation_and_normalization"] = orientation
    closed_candidate["smallest_right_singular_vector_only"] = True
    np.savez_compressed(output / "closed_class_stationary_candidate.npz", p_closed=p_closed)
    closed_candidate["artifact"] = {
        "path": "closed_class_stationary_candidate.npz",
        "sha256": file_sha256(output / "closed_class_stationary_candidate.npz"),
        "bytes": (output / "closed_class_stationary_candidate.npz").stat().st_size,
    }
    write_json(output / "closed_class_stationary_candidate_receipt.json", closed_candidate)
    if closed_candidate["status"] != "PASS":
        raise RuntimeError(FAIL_TERMINAL)

    p_full = np.zeros(N_FULL, dtype=np.float64)
    p_full[closed] = p_closed
    embedded = embedded_statistics(p_full, p_closed, closed, transient)
    np.savez_compressed(output / "embedded_full_space_candidate.npz", p_full=p_full)
    embedded["artifact"] = {
        "path": "embedded_full_space_candidate.npz",
        "sha256": file_sha256(output / "embedded_full_space_candidate.npz"),
        "bytes": (output / "embedded_full_space_candidate.npz").stat().st_size,
    }
    write_json(output / "embedded_full_space_candidate_receipt.json", embedded)
    if embedded["status"] != "PASS":
        raise RuntimeError(FAIL_TERMINAL)

    ledger["full_q_transpose_p_calls"] += 1
    residual = np.asarray(q.transpose().tocsr() @ p_full).ravel()
    stationarity = stationarity_receipt(q, p_full, residual)
    np.savez_compressed(output / "full_q_stationarity_residual.npz", residual=residual)
    stationarity["artifact"] = {
        "path": "full_q_stationarity_residual.npz",
        "sha256": file_sha256(output / "full_q_stationarity_residual.npz"),
        "bytes": (output / "full_q_stationarity_residual.npz").stat().st_size,
    }
    write_json(output / "full_q_stationarity_receipt.json", stationarity)
    if stationarity["status"] != "PASS":
        raise RuntimeError(FAIL_TERMINAL)

    with np.load(mass_path, allow_pickle=False) as archive:
        p_run003 = np.asarray(archive["p"], dtype=np.float64)
    if field_sha256(p_run003) != RUN003_P_SHA256:
        raise RuntimeError("run003 p field identity mismatch")
    p_run_closed = p_run003[closed]
    p_run_transient = p_run003[transient]
    difference = p_closed - p_run_closed
    closed_mass = math.fsum(float(value) for value in p_run_closed)
    transient_mass = math.fsum(float(value) for value in p_run_transient)
    closed_candidate_mass = math.fsum(float(value) for value in p_closed)
    denominator = float(np.linalg.norm(p_closed) * np.linalg.norm(p_run_closed))
    comparison = {
        "run003_p_sha256": field_sha256(p_run003),
        "run003_vector_modified": False,
        "run003_vector_renormalized": False,
        "run003_transient_signed_mass": transient_mass,
        "run003_transient_l1_mass": float(
            math.fsum(abs(float(value)) for value in p_run_transient)
        ),
        "run003_closed_signed_mass": closed_mass,
        "restricted_candidate_closed_signed_mass": closed_candidate_mass,
        "closed_maximum_absolute_difference": float(np.max(np.abs(difference))),
        "closed_l1_difference": float(
            math.fsum(abs(float(value)) for value in difference)
        ),
        "closed_cosine_similarity": float(np.dot(p_closed, p_run_closed) / denominator),
        "candidate_minus_run003_closed_mass": closed_candidate_mass - closed_mass,
        "run003_transient_leakage_signed_mass": transient_mass,
        "mass_accounting_discrepancy": (
            (closed_candidate_mass - closed_mass) - transient_mass
        ),
        "mass_discrepancy_explained_by_transient_leakage": (
            abs((closed_candidate_mass - closed_mass) - transient_mass) <= gamma(N_FULL)
        ),
    }
    write_json(output / "comparison_to_run003_receipt.json", comparison)

    ledger["orientation_calls"] = orientation["orientation_calls"]
    ledger["normalization_calls"] = orientation["normalization_calls"]
    write_json(output / "scientific_ledger.json", ledger)
    forbidden_zero = all(
        ledger[name] == 0
        for name in (
            "topology_scc_recomputations", "hjb_policy_d2_calls",
            "full_space_800x800_gesvd_calls", "alternate_svd_eigen_nullspace_calls",
            "scientific_retries", "clipping_projection_of_run003_p_calls",
            "aggregate_k1a_c1_firm_outer_calls",
            "matlab_ge_annual_shock_irf_welfare_results_calls",
            "remaining_province_household_runs", "turn2_calls",
        )
    )
    supported = bool(
        structure["status"] == "PASS"
        and rank["status"] == "PASS"
        and closed_candidate["status"] == "PASS"
        and embedded["status"] == "PASS"
        and stationarity["status"] == "PASS"
        and comparison["mass_discrepancy_explained_by_transient_leakage"]
        and ledger["q12_artifact_loads"] == 1
        and ledger["restricted_dense_gesvd_calls"] == 1
        and ledger["normalized_stationary_candidates"] == 1
        and ledger["full_q_transpose_p_calls"] == 1
        and ledger["orientation_calls"] == 1
        and ledger["normalization_calls"] == 1
        and forbidden_zero
    )
    terminal = PASS_TERMINAL if supported else FAIL_TERMINAL
    terminal_receipt = {
        "terminal_classification": terminal,
        "candidate_supported": supported,
        "accepted_kfe_method_changed": False,
        "method_adopted": False,
        "owner_method_adoption_decision_required": supported,
        "remaining_30_provinces_run": False,
        "turn2_run": False,
        "results_eligibility": False,
    }
    write_json(output / "terminal_receipt.json", terminal_receipt)
    write_report(
        report_path, terminal, structure, rank, closed_candidate,
        embedded, stationarity, comparison,
    )
    write_json(output / "sealed_manifest.json", seal(output))
    independent = readback(output)
    write_json(output / "independent_readback_receipt.json", independent)
    if independent["status"] != "PASS":
        raise RuntimeError("independent readback failed")
    return {
        **terminal_receipt,
        "evidence_root": output.relative_to(repository).as_posix(),
        "sealed_manifest_sha256": independent["manifest_sha256"],
        "manifest_entry_count": independent["entry_count"],
        "manifest_total_bytes": independent["total_bytes"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    repository = args.repository.resolve()
    output = (args.output or repository / OUTPUT_ROOT_RELATIVE).resolve()
    report = (args.report or repository / REPORT_RELATIVE).resolve()
    result = execute(repository, output, report)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
