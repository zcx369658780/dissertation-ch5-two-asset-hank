"""Deterministic support forensic for the persisted run003 stationary mass.

This module deliberately imports no Chapter 5 scientific runtime.  It only
hashes and loads sealed JSON/NPZ artifacts, constructs a mask from persisted
``closed_members``, and performs descriptive reductions.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable

import numpy as np


TASK_ID = "CH5_MP4C_CORRECTED_OPTIONB_RUN003_STATIONARY_MASS_NEGATIVITY_SUPPORT_FORENSIC_20260920"
BASELINE_SHA = "03a6c3d17b9741cf60fb0d3f4bd2b981ac5e2fef"
TERMINAL_MARKER = "PASS__RUN003_STATIONARY_MASS_NEGATIVITY_SUPPORT_FORENSIC_COMPLETE__NO_KFE_METHOD_CHANGE"
CLASSIFICATION_A = (
    "RUN003_NEGATIVITY_BREACHES_TRANSIENT_ONLY__CLOSED_CLASS_MASS_PASSES_"
    "ENTRYWISE_FLOOR__KFE_METHOD_DECISION_REQUIRED"
)
CLASSIFICATION_B = (
    "RUN003_CLOSED_CLASS_ENTRYWISE_NEGATIVITY_BREACH_CONFIRMED__KFE_METHOD_DECISION_REQUIRED"
)
CLASSIFICATION_C = (
    "RUN003_STATIONARY_MASS_SUPPORT_FORENSIC_INCONSISTENT__NO_METHOD_DECISION"
)

SOURCE_ROOT_RELATIVE = Path(
    "reports/ch5_mp4c_corrected_optionb_initial_turn_31_province_household_kfe_"
    "k1a_c1_one_turn_integration_20260920_run003"
)
OUTPUT_ROOT_RELATIVE = Path(
    "reports/ch5_mp4c_corrected_optionb_run003_stationary_mass_negativity_"
    "support_forensic_20260920_run001"
)
REPORT_RELATIVE = Path(
    "docs/CH5_MP4C_CORRECTED_OPTIONB_RUN003_STATIONARY_MASS_NEGATIVITY_"
    "SUPPORT_FORENSIC_REPORT.md"
)
MANIFEST_SHA256 = "18D62A1E388E17D3D0A7001D22998B86389C946B7136D481FB7DE11777A3388B"
MASS_ARTIFACT_SHA256 = "15C6D7B24375A20CADB8C871527C75B7447EE9397FCAA44C72FCFC26D064E436"
P_SHA256 = "F29C4A816652520ABB678301976BA8D3B62773652546B6434BB05674A88DF1CC"
G_SHA256 = "99BAC1D6842B04EF71D7914D31DCA04BE8E4C8E9BECC995A1307DD096859B46D"
RESIDUAL_SHA256 = "A180AD4C72DE3D7951EEDE186BC93E95683D57B43CBE48CE08F968EF662CCD4D"
Q_SHA256 = "E1F55D0B755CB83D4F6A3CB4FEFD6DBC8CD4F05C6D23FC5DE00302E16B74BF20"
TAU_NONNEGATIVE = 1.9184653865526386e-13
TOTAL_NEGATIVE_MASS_BOUND = 1.5347723092421108e-10
SHAPE = (20, 20, 2)
N = math.prod(SHAPE)
EXPECTED_CLOSED = tuple(range(200, 400)) + tuple(range(600, 800))


def file_sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()


def field_sha256(values: np.ndarray) -> str:
    encoded = np.asarray(values, dtype="<f8").tobytes(order="F")
    return hashlib.sha256(encoded).hexdigest().upper()


def write_json(path: Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def verify_source_manifest(source_root: Path) -> dict[str, Any]:
    manifest_path = source_root / "sealed_manifest.json"
    manifest = read_json(manifest_path)
    bad_paths: list[dict[str, Any]] = []
    entries = manifest.get("entries", [])
    for entry in entries:
        target = source_root / entry["path"]
        actual_hash = file_sha256(target) if target.is_file() else None
        actual_bytes = target.stat().st_size if target.is_file() else None
        if actual_hash != entry["sha256"] or actual_bytes != entry["bytes"]:
            bad_paths.append(
                {
                    "path": entry["path"],
                    "expected_sha256": entry["sha256"],
                    "actual_sha256": actual_hash,
                    "expected_bytes": entry["bytes"],
                    "actual_bytes": actual_bytes,
                }
            )
    entry_count_match = manifest.get("entry_count") == len(entries)
    total_bytes_match = manifest.get("total_bytes") == sum(int(row["bytes"]) for row in entries)
    actual_manifest_hash = file_sha256(manifest_path)
    passed = bool(
        actual_manifest_hash == MANIFEST_SHA256
        and entry_count_match
        and total_bytes_match
        and not bad_paths
    )
    return {
        "path": manifest_path.as_posix(),
        "expected_sha256": MANIFEST_SHA256,
        "actual_sha256": actual_manifest_hash,
        "entry_count": len(entries),
        "entry_count_match": entry_count_match,
        "total_bytes": sum(int(row["bytes"]) for row in entries),
        "total_bytes_match": total_bytes_match,
        "bad_paths": bad_paths,
        "status": "PASS" if passed else "FAIL",
    }


def _group_statistics(p: np.ndarray, indices: np.ndarray, tau: float) -> dict[str, Any]:
    values = np.asarray(p[indices], dtype=np.float64)
    if values.size == 0:
        raise ValueError("support group must not be empty")
    minimum = float(np.min(values))
    maximum = float(np.max(values))
    minimum_indices = indices[np.flatnonzero(values == minimum)].astype(int).tolist()
    maximum_abs = float(np.max(np.abs(values)))
    maximum_abs_indices = indices[np.flatnonzero(np.abs(values) == maximum_abs)].astype(int).tolist()
    negative = values[values < 0.0]
    positive = values[values > 0.0]
    breaches = values[values < -tau]
    return {
        "state_count": int(values.size),
        "exact_zero_count": int(np.count_nonzero(values == 0.0)),
        "positive_count": int(positive.size),
        "negative_count": int(negative.size),
        "below_negative_tau_breach_count": int(breaches.size),
        "minimum_p": minimum,
        "maximum_p": maximum,
        "minimum_flat_index": minimum_indices[0],
        "minimum_flat_indices": minimum_indices,
        "signed_math_fsum_p": float(math.fsum(float(value) for value in values)),
        "positive_mass_sum": float(math.fsum(float(value) for value in positive)),
        "total_negative_mass": float(math.fsum(-float(value) for value in negative)),
        "l1_mass": float(math.fsum(abs(float(value)) for value in values)),
        "maximum_absolute_entry": maximum_abs,
        "maximum_absolute_entry_flat_index": maximum_abs_indices[0],
        "maximum_absolute_entry_flat_indices": maximum_abs_indices,
    }


def flat_coordinate(flat_index: int) -> tuple[int, int, int]:
    if not 0 <= flat_index < N:
        raise ValueError("flat index outside accepted state grid")
    coordinate = np.unravel_index(flat_index, SHAPE, order="F")
    return tuple(int(value) for value in coordinate)


def localized_row(flat_index: int, p_value: float, closed_mask: np.ndarray) -> dict[str, Any]:
    b_index, a_index, z_index = flat_coordinate(flat_index)
    b_grid = np.linspace(-2.0, 5.0, 20)
    a_grid = np.linspace(0.0, 10.0, 20)
    z_grid = np.asarray([0.8, 1.3], dtype=np.float64)
    return {
        "flat_index": int(flat_index),
        "b_index": b_index,
        "a_index": a_index,
        "z_index": z_index,
        "b": float(b_grid[b_index]),
        "a": float(a_grid[a_index]),
        "z": float(z_grid[z_index]),
        "p": float(p_value),
        "support_class": "closed" if bool(closed_mask[flat_index]) else "transient",
    }


def residual_statistics(residual: np.ndarray, indices: np.ndarray) -> dict[str, Any]:
    values = np.asarray(residual[indices], dtype=np.float64)
    absolute = np.abs(values)
    inf_norm = float(np.max(absolute))
    maxima = indices[np.flatnonzero(absolute == inf_norm)].astype(int).tolist()
    return {
        "state_count": int(values.size),
        "infinity_norm": inf_norm,
        "l1_norm": float(math.fsum(abs(float(value)) for value in values)),
        "signed_math_fsum": float(math.fsum(float(value) for value in values)),
        "max_absolute_residual_flat_index": maxima[0],
        "max_absolute_residual_flat_indices": maxima,
    }


def classify(closed_breach_count: int, transient_breach_count: int, consistent: bool = True) -> str:
    if not consistent:
        return CLASSIFICATION_C
    if closed_breach_count > 0:
        return CLASSIFICATION_B
    if transient_breach_count > 0:
        return CLASSIFICATION_A
    return CLASSIFICATION_C


def zero_science_ledger() -> dict[str, Any]:
    return {
        "schema": "CH5_MP4C_RUN003_STATIONARY_MASS_SUPPORT_FORENSIC_ZERO_SCIENCE_LEDGER_V1",
        "source_native_initialization_calls": 0,
        "selector_calls": 0,
        "root_calls": 0,
        "d2_q_assembly_calls": 0,
        "hjb_calls": 0,
        "direct_solve_calls": 0,
        "scc_calls": 0,
        "connected_components_calls": 0,
        "topology_recomputation_calls": 0,
        "svd_calls": 0,
        "eigen_calls": 0,
        "nullspace_calls": 0,
        "sign_orientation_calls": 0,
        "normalization_calls": 0,
        "q_transpose_p_calls": 0,
        "kfe_calls": 0,
        "clipping_projection_truncation_abs_repair_calls": 0,
        "renormalization_calls": 0,
        "aggregate_calls": 0,
        "k1a_calls": 0,
        "c1_calls": 0,
        "firm_calls": 0,
        "outer_calls": 0,
        "matlab_scientific_calls": 0,
        "ge_calls": 0,
        "results_calls": 0,
        "scientific_retries": 0,
        "allowed_operations": [
            "sealed artifact reads and hashes",
            "JSON and NPZ loading",
            "persisted closed-member mask construction",
            "deterministic indexing and descriptive reductions",
            "serialization, sealing, and readback",
        ],
    }


def _seal(root: Path) -> dict[str, Any]:
    entries = []
    excluded = {"sealed_manifest.json", "independent_readback_receipt.json"}
    for path in sorted(item for item in root.rglob("*") if item.is_file() and item.name not in excluded):
        entries.append(
            {
                "path": path.relative_to(root).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": file_sha256(path),
            }
        )
    return {
        "schema": "CH5_MP4C_RUN003_STATIONARY_MASS_SUPPORT_FORENSIC_SEALED_MANIFEST_V1",
        "entry_count": len(entries),
        "total_bytes": sum(int(item["bytes"]) for item in entries),
        "entries": entries,
    }


def _readback(root: Path) -> dict[str, Any]:
    manifest_path = root / "sealed_manifest.json"
    manifest = read_json(manifest_path)
    bad_paths = []
    for entry in manifest["entries"]:
        path = root / entry["path"]
        if (
            not path.is_file()
            or path.stat().st_size != entry["bytes"]
            or file_sha256(path) != entry["sha256"]
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
        "scientific_calls": 0,
    }


def _report(
    classification: str,
    stats: dict[str, Any],
    minimum: dict[str, Any],
    breaches: list[dict[str, Any]],
    residuals: dict[str, Any],
    ratios: dict[str, float],
) -> str:
    lines = [
        "# Chapter 5 run003 stationary-mass negativity support forensic", "",
        "## Terminal result", "", f"`{TERMINAL_MARKER}`", "", f"`{classification}`", "",
        "The forensic is deterministic post-processing of the accepted run003 artifacts. The existing KFE result remains FAIL and no KFE method or tolerance was changed.", "",
        "## Authority binding", "",
        f"- Actual live-main baseline: `{BASELINE_SHA}`.",
        f"- Accepted run003 manifest: `{MANIFEST_SHA256}`.",
        f"- Accepted stationary-mass artifact: `{MASS_ARTIFACT_SHA256}`.",
        f"- Accepted p / g / residual identities: `{P_SHA256}` / `{G_SHA256}` / `{RESIDUAL_SHA256}`.", "",
        "## Closed and transient mass statistics", "",
        "| support | states | zero | positive | negative | breaches | min p | max p | signed mass | positive mass | negative mass | L1 mass | max abs |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for key, label in (("all", "all"), ("closed", "closed"), ("transient", "transient")):
        row = stats[key]
        lines.append(
            f"| {label} | {row['state_count']} | {row['exact_zero_count']} | {row['positive_count']} | "
            f"{row['negative_count']} | {row['below_negative_tau_breach_count']} | {row['minimum_p']:.17g} | "
            f"{row['maximum_p']:.17g} | {row['signed_math_fsum_p']:.17g} | {row['positive_mass_sum']:.17g} | "
            f"{row['total_negative_mass']:.17g} | {row['l1_mass']:.17g} | {row['maximum_absolute_entry']:.17g} |"
        )
    lines.extend([
        "", "## Global minimum and breaches", "",
        f"Global minimum is flat index `{minimum['flat_index']}` at `(b_index,a_index,z_index)=({minimum['b_index']},{minimum['a_index']},{minimum['z_index']})`, physical state `(b,a,z)=({minimum['b']:.17g},{minimum['a']:.17g},{minimum['z']:.17g})`, p=`{minimum['p']:.17g}`, support=`{minimum['support_class']}`.", "",
        f"Closed/transient breach counts: `{stats['closed']['below_negative_tau_breach_count']}` / `{stats['transient']['below_negative_tau_breach_count']}`. `abs(global_min)/tau={ratios['absolute_global_min_over_tau_nonnegative']:.17g}`; total-negative-mass/bound=`{ratios['total_negative_mass_over_bound']:.17g}`.", "",
        "Top 20 floor breaches by magnitude:", "",
        "| flat | (b,a,z) index | physical (b,a,z) | p | support |",
        "|---:|---|---|---:|---|",
    ])
    for row in sorted(breaches, key=lambda item: (item["p"], item["flat_index"]))[:20]:
        lines.append(
            f"| {row['flat_index']} | ({row['b_index']},{row['a_index']},{row['z_index']}) | "
            f"({row['b']:.17g},{row['a']:.17g},{row['z']:.17g}) | {row['p']:.17g} | {row['support_class']} |"
        )
    lines.extend([
        "", "The complete breach table is persisted as JSON and CSV in the evidence root.", "",
        "## Persisted residual decomposition", "",
        "| support | inf norm | L1 norm | signed sum | max-abs flat index |",
        "|---|---:|---:|---:|---:|",
    ])
    for key in ("closed", "transient"):
        row = residuals[key]
        lines.append(
            f"| {key} | {row['infinity_norm']:.17g} | {row['l1_norm']:.17g} | "
            f"{row['signed_math_fsum']:.17g} | {row['max_absolute_residual_flat_index']} |"
        )
    lines.extend([
        "", "The residual was loaded from the persisted artifact. No `Q.T@p` multiplication was performed.", "",
        "## Scientific boundary", "",
        "All prohibited scientific-call counters are zero. No vector entry was clipped, projected, truncated, absolutized, oriented, normalized, or otherwise changed. Results eligibility remains `FALSE`.", "",
    ])
    return "\n".join(lines)


def execute(repository: Path, output_root: Path, report_path: Path) -> dict[str, Any]:
    source_root = repository / SOURCE_ROOT_RELATIVE
    terminal = source_root / "household/p00_北京/terminal_kfe"
    topology_path = terminal / "topology_receipt.json"
    svd_path = terminal / "svd_rank_nullity_receipt.json"
    stationarity_path = terminal / "stationarity_normalization_nonnegativity_receipt.json"
    arrays_path = terminal / "stationary_mass_arrays.npz"
    checkpoint_path = source_root / "household/p00_北京/checkpoint_012/checkpoint_manifest.json"

    if output_root.exists():
        raise FileExistsError(f"evidence root already exists: {output_root}")
    output_root.mkdir(parents=True)

    source_manifest = verify_source_manifest(source_root)
    topology = read_json(topology_path)
    svd = read_json(svd_path)
    stationarity = read_json(stationarity_path)
    checkpoint = read_json(checkpoint_path)
    with np.load(arrays_path, allow_pickle=False) as archive:
        keys = sorted(archive.files)
        p = np.asarray(archive["p"], dtype=np.float64)
        g = np.asarray(archive["g"], dtype=np.float64)
        residual = np.asarray(archive["residual"], dtype=np.float64)

    closed_members_raw = topology.get("closed_members", [])
    closed_members = tuple(int(item) for group in closed_members_raw for item in group)
    consistency_checks = {
        "source_manifest_pass": source_manifest["status"] == "PASS",
        "stationary_mass_artifact_sha256_match": file_sha256(arrays_path) == MASS_ARTIFACT_SHA256,
        "npz_fields_include_required": {"p", "g", "residual"}.issubset(keys),
        "p_shape_match": p.shape == (N,),
        "g_shape_match": g.shape == (N,),
        "residual_shape_match": residual.shape == (N,),
        "p_finite": bool(np.all(np.isfinite(p))),
        "g_finite": bool(np.all(np.isfinite(g))),
        "residual_finite": bool(np.all(np.isfinite(residual))),
        "p_sha256_match": field_sha256(p) == P_SHA256,
        "g_sha256_match": field_sha256(g) == G_SHA256,
        "residual_sha256_match": field_sha256(residual) == RESIDUAL_SHA256,
        "topology_closed_class_count_one": topology.get("closed_class_count") == 1,
        "topology_closed_members_exact": closed_members == EXPECTED_CLOSED,
        "topology_transient_count_400": topology.get("transient_state_count") == 400,
        "svd_rank_nullity_799_1": (
            svd.get("numerical_rank") == 799 and svd.get("numerical_nullity") == 1
        ),
        "stationarity_tau_match": stationarity.get("nonnegativity", {}).get("tau_nonnegative") == TAU_NONNEGATIVE,
        "stationarity_total_negative_bound_match": (
            stationarity.get("nonnegativity", {}).get("total_negative_mass_bound")
            == TOTAL_NEGATIVE_MASS_BOUND
        ),
        "checkpoint_12_match": checkpoint.get("checkpoint") == 12,
        "checkpoint_q_sha256_match": (
            checkpoint.get("d2_receipt", {}).get("q_artifact", {}).get("sha256") == Q_SHA256
        ),
    }
    consistent = all(consistency_checks.values())
    authority = {
        "schema": "CH5_MP4C_RUN003_STATIONARY_MASS_SUPPORT_FORENSIC_AUTHORITY_BINDING_V1",
        "task_id": TASK_ID,
        "actual_live_main_baseline": BASELINE_SHA,
        "source_root": SOURCE_ROOT_RELATIVE.as_posix(),
        "source_manifest": source_manifest,
        "bound_paths": {
            "topology_receipt": topology_path.relative_to(repository).as_posix(),
            "svd_rank_nullity_receipt": svd_path.relative_to(repository).as_posix(),
            "stationarity_receipt": stationarity_path.relative_to(repository).as_posix(),
            "stationary_mass_arrays": arrays_path.relative_to(repository).as_posix(),
            "checkpoint_012_manifest": checkpoint_path.relative_to(repository).as_posix(),
        },
        "npz_fields": keys,
        "field_identities": {
            "p": field_sha256(p), "g": field_sha256(g), "residual": field_sha256(residual)
        },
        "checks": consistency_checks,
        "status": "PASS" if consistent else "FAIL",
    }
    write_json(output_root / "authority_binding.json", authority)

    if not consistent:
        classification = CLASSIFICATION_C
        terminal_receipt = {
            "terminal_marker": TERMINAL_MARKER,
            "classification": classification,
            "kfe_status": "FAIL_UNCHANGED",
            "kfe_method_changed": False,
            "results_eligibility": False,
        }
        write_json(output_root / "zero_science_ledger.json", zero_science_ledger())
        write_json(output_root / "terminal_classification.json", terminal_receipt)
        write_json(output_root / "sealed_manifest.json", _seal(output_root))
        write_json(output_root / "independent_readback_receipt.json", _readback(output_root))
        return terminal_receipt

    closed_mask = np.zeros(N, dtype=bool)
    closed_mask[np.asarray(closed_members, dtype=np.int64)] = True
    transient_mask = ~closed_mask
    all_indices = np.arange(N, dtype=np.int64)
    closed_indices = np.flatnonzero(closed_mask)
    transient_indices = np.flatnonzero(transient_mask)
    mask_receipt = {
        "schema": "CH5_MP4C_RUN003_STATIONARY_MASS_SUPPORT_MASK_V1",
        "construction_authority": "persisted topology_receipt.closed_members only",
        "topology_recomputation_calls": 0,
        "shape_f_order": list(SHAPE),
        "b_fastest": True,
        "closed_class_count": topology["closed_class_count"],
        "closed_state_count": int(np.count_nonzero(closed_mask)),
        "transient_state_count": int(np.count_nonzero(transient_mask)),
        "closed_members": list(closed_members),
        "closed_members_sha256_little_endian_int64": hashlib.sha256(
            np.asarray(closed_members, dtype="<i8").tobytes()
        ).hexdigest().upper(),
        "closed_ranges_inclusive": [[200, 399], [600, 799]],
    }
    write_json(output_root / "closed_transient_mask_receipt.json", mask_receipt)

    stats = {
        "schema": "CH5_MP4C_RUN003_STATIONARY_MASS_GROUP_STATISTICS_V1",
        "tau_nonnegative": TAU_NONNEGATIVE,
        "groups": {
            "all": _group_statistics(p, all_indices, TAU_NONNEGATIVE),
            "closed": _group_statistics(p, closed_indices, TAU_NONNEGATIVE),
            "transient": _group_statistics(p, transient_indices, TAU_NONNEGATIVE),
        },
    }
    all_stats = stats["groups"]
    global_min_index = int(np.argmin(p))
    minimum = localized_row(global_min_index, float(p[global_min_index]), closed_mask)
    breach_indices = np.flatnonzero(p < -TAU_NONNEGATIVE)
    breaches = [localized_row(int(index), float(p[index]), closed_mask) for index in breach_indices]
    closed_breaches = [row for row in breaches if row["support_class"] == "closed"]
    transient_breaches = [row for row in breaches if row["support_class"] == "transient"]

    def maximum_breach(rows: list[dict[str, Any]]) -> dict[str, Any]:
        if not rows:
            return {"magnitude": 0.0, "flat_index": None}
        row = min(rows, key=lambda item: (item["p"], item["flat_index"]))
        return {"magnitude": -float(row["p"]), "flat_index": int(row["flat_index"])}

    ratios = {
        "absolute_global_min_over_tau_nonnegative": abs(float(p[global_min_index])) / TAU_NONNEGATIVE,
        "total_negative_mass_over_bound": (
            all_stats["all"]["total_negative_mass"] / TOTAL_NEGATIVE_MASS_BOUND
        ),
    }
    support_summary = {
        "schema": "CH5_MP4C_RUN003_STATIONARY_MASS_SUPPORT_SUMMARY_V1",
        "global_minimum": minimum,
        "closed_breach_count": len(closed_breaches),
        "transient_breach_count": len(transient_breaches),
        "closed_maximum_breach": maximum_breach(closed_breaches),
        "transient_maximum_breach": maximum_breach(transient_breaches),
        "transient_signed_mass": all_stats["transient"]["signed_math_fsum_p"],
        "transient_l1_mass": all_stats["transient"]["l1_mass"],
        "closed_signed_mass": all_stats["closed"]["signed_math_fsum_p"],
        "tau_nonnegative": TAU_NONNEGATIVE,
        "total_negative_mass_bound": TOTAL_NEGATIVE_MASS_BOUND,
        **ratios,
    }
    write_json(output_root / "group_statistics.json", stats)
    write_json(output_root / "support_summary.json", support_summary)
    write_json(
        output_root / "complete_breach_table.json",
        {
            "schema": "CH5_MP4C_RUN003_STATIONARY_MASS_COMPLETE_BREACH_TABLE_V1",
            "strict_condition": "p < -tau_nonnegative",
            "tau_nonnegative": TAU_NONNEGATIVE,
            "row_count": len(breaches),
            "rows": breaches,
        },
    )
    with (output_root / "complete_breach_table.csv").open("w", encoding="utf-8", newline="") as handle:
        columns = [
            "flat_index", "b_index", "a_index", "z_index", "b", "a", "z", "p", "support_class"
        ]
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(breaches)

    residuals = {
        "schema": "CH5_MP4C_RUN003_PERSISTED_RESIDUAL_SUPPORT_DECOMPOSITION_V1",
        "residual_source": "persisted stationary_mass_arrays.npz residual",
        "residual_sha256": field_sha256(residual),
        "q_transpose_p_calls": 0,
        "closed": residual_statistics(residual, closed_indices),
        "transient": residual_statistics(residual, transient_indices),
    }
    write_json(output_root / "persisted_residual_support_decomposition.json", residuals)
    ledger = zero_science_ledger()
    write_json(output_root / "zero_science_ledger.json", ledger)

    classification = classify(len(closed_breaches), len(transient_breaches), consistent=True)
    terminal_receipt = {
        "terminal_marker": TERMINAL_MARKER,
        "classification": classification,
        "classification_a_condition": len(closed_breaches) == 0 and len(transient_breaches) > 0,
        "classification_b_condition": len(closed_breaches) > 0,
        "classification_c_condition": False,
        "kfe_status": "FAIL_UNCHANGED",
        "kfe_accepted": False,
        "kfe_method_changed": False,
        "results_eligibility": False,
    }
    write_json(output_root / "terminal_classification.json", terminal_receipt)
    report_path.write_text(
        _report(classification, all_stats, minimum, breaches, residuals, ratios),
        encoding="utf-8",
        newline="\n",
    )
    write_json(output_root / "sealed_manifest.json", _seal(output_root))
    readback = _readback(output_root)
    write_json(output_root / "independent_readback_receipt.json", readback)
    if readback["status"] != "PASS":
        raise RuntimeError("independent readback failed")
    return {
        **terminal_receipt,
        "evidence_root": output_root.relative_to(repository).as_posix(),
        "sealed_manifest_sha256": readback["manifest_sha256"],
        "manifest_entry_count": readback["entry_count"],
        "manifest_total_bytes": readback["total_bytes"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output-root", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    repository = args.repository.resolve()
    output_root = (args.output_root or repository / OUTPUT_ROOT_RELATIVE).resolve()
    report = (args.report or repository / REPORT_RELATIVE).resolve()
    result = execute(repository, output_root, report)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
