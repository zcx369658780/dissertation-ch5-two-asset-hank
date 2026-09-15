"""Trace-only spatial localization; this module never imports scientific runtime."""
from __future__ import annotations

import argparse
import csv
from collections import Counter
from hashlib import sha256
import json
from math import isfinite
from pathlib import Path
from typing import Any, Iterable


REPO = Path(__file__).resolve().parents[3]
TASK_ID = "CH5_MP4C_K1_J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_AUDIT"
ACTUAL_BASELINE = "86ae2936f62c3473f48d3671cb08feba19d0fd83"
BRANCH = "codex/ch5-mp4c-k1-j160-six-failure-trace-spatial-localization-audit-20260915"
WORKTREE = r"D:\ProjectTemp\ch5-mp4c-k1-j160-six-failure-trace-spatial-localization-audit-20260915-001"
ACCEPTED_CANDIDATE = "ad4cdc8bbdf924c2ed06477abc10d1010038a5f7"
ACCEPTED_PARENT = "3b193f536fe2ab70fd487e3a4cde899ee5ed0c34"
NEXT_GATE = "REVIEWER_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_ROUTE_DECISION"

SOURCE_ROOT = REPO / "docs/evidence/ch5_mp4c_k1_j160_first_turn_six_failure_hjb_mechanism_panel"
SOURCE_MANIFEST = SOURCE_ROOT / "sealed_manifest_sha256.json"
SOURCE_MANIFEST_SHA256 = "96729AE18ABA997D7EF514021B7B8C8B5BAC9A156C31F4A1E08321374D69EFA2"
SOURCE_ACCEPTANCE = REPO / "docs/CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_ACCEPTANCE.md"
SOURCE_ACCEPTANCE_SHA256 = "1D606FAB4F0D724851A7D26125C82057E63F512A81F09835CCC55ADD4C9F0E93"
SOURCE_REPORT = REPO / "docs/CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_DIAGNOSTIC_REPORT.md"
SOURCE_REPORT_SHA256 = "0CDDFE565F71BE7515D1533D7CA28DBD5C7D396A6108292E95BD32AE9A161F31"

J640_ROOT = REPO / "docs/evidence/ch5_mp4c_k1_j640_hjb_nonconvergence_mechanism_diagnostic"
J640_MANIFEST = J640_ROOT / "sealed_manifest_sha256.json"
J640_MANIFEST_SHA256 = "4BA58453D530E52920411BAC04F54D6BB255C5711129840693FD870459C43E28"
J640_ACCEPTANCE = REPO / "docs/CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC_ACCEPTANCE.md"
J640_ACCEPTANCE_SHA256 = "B4E8DEC045837A218C5A2172142E6C19C09ADEB92BC94A41F1F39CF300C06689"

PROVINCES = (
    (1, "天津", "POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION"),
    (3, "山西", "POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION"),
    (13, "江西", "DERIVATIVE_FLOOR_AMPLIFICATION_AFTER_EARLIER_SWITCHING"),
    (21, "重庆", "POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION"),
    (23, "贵州", "REPEATING_OR_LOW_PERIOD_CYCLE"),
    (27, "甘肃", "POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION"),
)
BOUNDARY_KEYS = ("b_lower_band", "b_upper_band", "a_lower_band", "a_upper_band")
BOUNDARY_LABELS = {
    "b_lower_band": "LIQUID_LOWER_BOUNDARY_CONCENTRATED",
    "b_upper_band": "LIQUID_UPPER_BOUNDARY_CONCENTRATED",
    "a_lower_band": "ILLIQUID_LOWER_BOUNDARY_CONCENTRATED",
    "a_upper_band": "ILLIQUID_UPPER_BOUNDARY_CONCENTRATED",
}
CONCENTRATION_THRESHOLD = 0.80
COMMON_SIGNATURE_TV_THRESHOLD = 0.20


def file_sha256(path: Path) -> str:
    return sha256(Path(path).read_bytes()).hexdigest().upper()


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    Path(path).write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def axis_zone(index: int, size: int) -> str:
    """Pre-registered one-index near-boundary band, excluding exact endpoints."""
    if size < 5:
        raise ValueError("size must be at least 5")
    if index < 0 or index >= size:
        raise ValueError("index outside grid")
    if index == 0:
        return "lower_exact"
    if index == 1:
        return "lower_near"
    if index == size - 2:
        return "upper_near"
    if index == size - 1:
        return "upper_exact"
    return "interior"


def spatial_label(shares: dict[str, float], *, coordinate_evidence_available: bool) -> str:
    if not coordinate_evidence_available:
        return "SPATIAL_LOCALIZATION_UNRESOLVED"
    dominant = [key for key in BOUNDARY_KEYS if shares.get(key, 0.0) >= CONCENTRATION_THRESHOLD]
    if len(dominant) >= 2:
        return "MULTI_BOUNDARY_CONCENTRATED"
    if len(dominant) == 1:
        return BOUNDARY_LABELS[dominant[0]]
    if shares.get("joint_asset_interior", 0.0) >= CONCENTRATION_THRESHOLD:
        return "INTERIOR_CONCENTRATED"
    return "MIXED_SPATIAL_FOOTPRINT"


def panel_decision(labels: list[str]) -> str:
    if len(labels) != 6 or "SPATIAL_LOCALIZATION_UNRESOLVED" in labels:
        return "SPATIAL_LOCALIZATION_EVIDENCE_INSUFFICIENT"
    boundary = set(BOUNDARY_LABELS.values()) | {"MULTI_BOUNDARY_CONCENTRATED"}
    if all(label in boundary for label in labels):
        return "COMMON_BOUNDARY_LOCALIZATION_ACROSS_FAILURES"
    if all(label == "INTERIOR_CONCENTRATED" for label in labels):
        return "COMMON_INTERIOR_LOCALIZATION_ACROSS_FAILURES"
    return "HETEROGENEOUS_SPATIAL_LOCALIZATION_ACROSS_FAILURES"


def total_variation(left: Iterable[float], right: Iterable[float]) -> float:
    a, b = list(left), list(right)
    if len(a) != len(b):
        raise ValueError("signature vectors must have equal length")
    return 0.5 * sum(abs(x - y) for x, y in zip(a, b))


def materially_common(vectors: list[list[float]]) -> bool:
    return all(
        total_variation(vectors[i], vectors[j]) <= COMMON_SIGNATURE_TV_THRESHOLD + 1e-12
        for i in range(len(vectors)) for j in range(i + 1, len(vectors))
    )


def _has_coordinate_field(value: Any) -> bool:
    if not isinstance(value, dict):
        return False
    coordinate_tokens = ("coordinate", "location", "indices", "index_zero_based", "cells")
    return any(any(token in str(key).lower() for token in coordinate_tokens) for key in value)


def coordinate_availability(rows: list[dict[str, Any]]) -> dict[str, str]:
    selector = any(_has_coordinate_field(row.get("selector_changes")) for row in rows)
    floor = any(_has_coordinate_field(row.get("derivative_floor_hits")) for row in rows)
    return {
        "selector": (
            "COORDINATE_LEVEL_SELECTOR_FOOTPRINT_AVAILABLE"
            if selector else "COORDINATE_LEVEL_SELECTOR_FOOTPRINT_UNAVAILABLE"
        ),
        "derivative_floor": (
            "FLOOR_COORDINATE_LOCALIZATION_AVAILABLE"
            if floor else "FLOOR_COORDINATE_LOCALIZATION_UNAVAILABLE"
        ),
    }


def _manifest_receipt(root: Path, manifest_path: Path, expected_manifest_hash: str) -> dict[str, Any]:
    manifest = read_json(manifest_path)
    entries = []
    for expected in manifest.get("entries", []):
        target = root / expected["path"]
        exists = target.is_file()
        actual_hash = file_sha256(target) if exists else None
        actual_bytes = target.stat().st_size if exists else None
        entries.append({
            "path": expected["path"], "exists": exists,
            "expected_sha256": expected["sha256"], "actual_sha256": actual_hash,
            "expected_bytes": expected["bytes"], "actual_bytes": actual_bytes,
            "pass": exists and actual_hash == expected["sha256"] and actual_bytes == expected["bytes"],
        })
    entry_count_ok = manifest.get("entry_count") == len(entries)
    bytes_ok = manifest.get("bytes_excluding_manifest") == sum(item["expected_bytes"] for item in entries)
    receipt = {
        "path": str(manifest_path.relative_to(REPO).as_posix()),
        "expected_manifest_sha256": expected_manifest_hash,
        "actual_manifest_sha256": file_sha256(manifest_path),
        "entry_count": len(entries), "entry_count_match": entry_count_ok,
        "bytes_excluding_manifest_match": bytes_ok, "entries": entries,
    }
    receipt["pass"] = bool(
        receipt["actual_manifest_sha256"] == expected_manifest_hash
        and entry_count_ok and bytes_ok and all(item["pass"] for item in entries)
    )
    return receipt


def source_trace_authority() -> dict[str, Any]:
    source_manifest = _manifest_receipt(SOURCE_ROOT, SOURCE_MANIFEST, SOURCE_MANIFEST_SHA256)
    j640_manifest = _manifest_receipt(J640_ROOT, J640_MANIFEST, J640_MANIFEST_SHA256)
    docs = {
        "six_failure_acceptance": (SOURCE_ACCEPTANCE, SOURCE_ACCEPTANCE_SHA256),
        "six_failure_diagnostic_report": (SOURCE_REPORT, SOURCE_REPORT_SHA256),
        "j640_acceptance": (J640_ACCEPTANCE, J640_ACCEPTANCE_SHA256),
    }
    doc_receipts = {
        name: {
            "path": str(path.relative_to(REPO).as_posix()), "expected_sha256": expected,
            "actual_sha256": file_sha256(path), "pass": file_sha256(path) == expected,
        }
        for name, (path, expected) in docs.items()
    }
    source_identity = read_json(SOURCE_ROOT / "source_identity.json")
    input_authority = read_json(SOURCE_ROOT / "input_authority_receipt.json")
    instrumentation = read_json(SOURCE_ROOT / "instrumentation_invariance_receipt.json")
    panel = read_json(SOURCE_ROOT / "panel_summary.json")
    classifications = read_json(SOURCE_ROOT / "province_mechanism_classification.json")["provinces"]
    class_map = {item["province"]: item["classification"] for item in classifications}
    expected_class_map = {province: mechanism for _, province, mechanism in PROVINCES}
    trace_checks = []
    for index, province, _ in PROVINCES:
        relative = f"traces/p{index:02d}_{province}.json"
        trace = read_json(SOURCE_ROOT / relative)
        trace_checks.append({
            "path": relative, "province": province,
            "schema": trace.get("schema"), "iteration_count": len(trace.get("iterations", [])),
            "pass": trace.get("province") == province and len(trace.get("iterations", [])) == 100,
        })
    receipt = {
        "schema": "CH5_MP4C_K1_J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_SOURCE_AUTHORITY_V1",
        "task_id": TASK_ID, "actual_baseline": ACTUAL_BASELINE,
        "accepted_candidate": ACCEPTED_CANDIDATE, "accepted_parent": ACCEPTED_PARENT,
        "repository_state_checks_recorded_from_fresh_preflight": {
            "accepted_candidate_object_is_commit": True,
            "accepted_candidate_parent_match": True,
            "accepted_candidate_is_ancestor_of_actual_baseline": True,
            "accepted_evidence_diff_candidate_to_baseline_is_empty": True,
            "validator_git_calls": 0,
        },
        "source_manifest": source_manifest, "j640_manifest": j640_manifest,
        "authority_documents": doc_receipts, "trace_checks": trace_checks,
        "source_identity_pass": source_identity.get("pass") is True,
        "input_authority_pass": input_authority.get("pass") is True,
        "instrumentation_invariance_pass": instrumentation.get("pass") is True,
        "accepted_panel_classification": panel.get("panel_classification"),
        "panel_classification_match": panel.get("panel_classification") == "SIX_FAILURES_HETEROGENEOUS_MECHANISMS",
        "province_classifications_match": class_map == expected_class_map,
        "scientific_runtime_during_authority_check": 0,
    }
    receipt["pass"] = bool(
        source_manifest["pass"] and j640_manifest["pass"]
        and all(item["pass"] for item in doc_receipts.values())
        and all(item["pass"] for item in trace_checks)
        and receipt["source_identity_pass"] and receipt["input_authority_pass"]
        and receipt["instrumentation_invariance_pass"]
        and receipt["panel_classification_match"] and receipt["province_classifications_match"]
    )
    return receipt


def _argmax_rows_from_trace(trace: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for row in trace["iterations"]:
        index = row["argmax"]["index_zero_based"]
        state = row["argmax"]["state"]
        rows.append({
            "iteration": int(row["iteration"]),
            "b_index": int(index["b"]), "a_index": int(index["a"]), "z_index": int(index["z"]),
            "b": float(state["b"]), "a": float(state["a"]), "z": float(state["z"]),
        })
    return rows


def _modal_location(rows: list[dict[str, Any]]) -> dict[str, Any]:
    counts = Counter((row["b_index"], row["a_index"], row["z_index"], row["b"], row["a"], row["z"]) for row in rows)
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    location, count = ordered[0]
    return {
        "index_zero_based": {"b": location[0], "a": location[1], "z": location[2]},
        "state": {"b": location[3], "a": location[4], "z": location[5]},
        "count": count, "share": count / len(rows),
        "tie_count": sum(value == count for _, value in ordered),
    }


def summarize_argmax(rows: list[dict[str, Any]], *, b_size: int, a_size: int, z_size: int) -> dict[str, Any]:
    if len(rows) != 100:
        raise ValueError("accepted trace must contain exactly 100 iterations")
    if any(not all(isfinite(float(row[key])) for key in ("b", "a", "z")) for row in rows):
        raise ValueError("argmax state must be finite")
    if any(not (0 <= row["b_index"] < b_size and 0 <= row["a_index"] < a_size and 0 <= row["z_index"] < z_size) for row in rows):
        raise ValueError("argmax index outside accepted grid")
    counts: Counter[str] = Counter()
    signature_order = (
        "liquid_lower_only", "liquid_upper_only", "illiquid_lower_only",
        "illiquid_upper_only", "multiple_boundary", "interior",
    )
    for row in rows:
        bz = axis_zone(row["b_index"], b_size)
        az = axis_zone(row["a_index"], a_size)
        counts[f"b_{bz}"] += 1
        counts[f"a_{az}"] += 1
        sides = []
        if bz.startswith("lower_"):
            sides.append("liquid_lower")
        elif bz.startswith("upper_"):
            sides.append("liquid_upper")
        if az.startswith("lower_"):
            sides.append("illiquid_lower")
        elif az.startswith("upper_"):
            sides.append("illiquid_upper")
        if len(sides) >= 2:
            counts["multiple_boundary"] += 1
        elif len(sides) == 1:
            counts[f"{sides[0]}_only"] += 1
        else:
            counts["interior"] += 1
        if bz == "interior" and az == "interior":
            counts["joint_asset_interior"] += 1
    for axis in ("b", "a"):
        counts[f"{axis}_lower_band"] = counts[f"{axis}_lower_exact"] + counts[f"{axis}_lower_near"]
        counts[f"{axis}_upper_band"] = counts[f"{axis}_upper_exact"] + counts[f"{axis}_upper_near"]
    keys = (
        "b_lower_exact", "b_lower_near", "b_lower_band", "b_upper_near", "b_upper_exact", "b_upper_band",
        "a_lower_exact", "a_lower_near", "a_lower_band", "a_upper_near", "a_upper_exact", "a_upper_band",
        "joint_asset_interior", "multiple_boundary",
    )
    selected_counts = {key: counts[key] for key in keys}
    shares = {key: value / len(rows) for key, value in selected_counts.items()}
    signature_counts = {key: counts[key] for key in signature_order}
    signature_vector = [signature_counts[key] / len(rows) for key in signature_order]
    locations = [(row["b_index"], row["a_index"], row["z_index"]) for row in rows]
    runs, current = [], 1
    for previous, current_location in zip(locations, locations[1:]):
        if current_location == previous:
            current += 1
        else:
            runs.append(current)
            current = 1
    runs.append(current)
    z_counts = Counter(row["z_index"] for row in rows)
    z_mode_index, z_mode_count = sorted(z_counts.items(), key=lambda item: (-item[1], item[0]))[0]
    z_mode_value = next(row["z"] for row in rows if row["z_index"] == z_mode_index)
    return {
        "coordinate_evidence_available": True,
        "iteration_count": len(rows), "grid_sizes": {"b": b_size, "a": a_size, "z": z_size},
        "boundary_definition": {
            "exact": "index 0 or size-1",
            "near": "index distance exactly 1 from either boundary, excluding exact boundary",
            "interior": "all remaining indices",
            "classification_uses_asset_axes_only": True,
        },
        "counts": selected_counts, "shares": shares,
        "signature_category_order": list(signature_order),
        "signature_counts": signature_counts, "signature_vector": signature_vector,
        "modal_location": _modal_location(rows),
        "z_modal": {"index_zero_based": z_mode_index, "state_value": z_mode_value, "count": z_mode_count, "share": z_mode_count / len(rows)},
        "unique_argmax_locations": len(set(locations)),
        "argmax_location_change_count": sum(left != right for left, right in zip(locations, locations[1:])),
        "argmax_location_persistence_count": sum(left == right for left, right in zip(locations, locations[1:])),
        "longest_consecutive_location_run": max(runs),
        "first_location": rows[0], "last_location": rows[-1],
        "spatial_label": spatial_label(shares, coordinate_evidence_available=True),
    }


def _timing_and_counts(trace: dict[str, Any]) -> dict[str, Any]:
    rows = trace["iterations"]
    selector_active = [row for row in rows if row["selector_changes"]["liquid"] is not None and sum(row["selector_changes"].values()) > 0]
    floor_active = [row for row in rows if sum(row["derivative_floor_hits"].values()) > 0]
    return {
        "selector": {
            "availability": coordinate_availability(rows)["selector"],
            "first_change_iteration": selector_active[0]["iteration"] if selector_active else None,
            "active_iterations": len(selector_active),
            "total_liquid_changes": sum(row["selector_changes"]["liquid"] or 0 for row in rows),
            "total_transfer_changes": sum(row["selector_changes"]["transfer"] or 0 for row in rows),
            "localization_inference_from_counts_or_hashes": False,
        },
        "derivative_floor": {
            "availability": coordinate_availability(rows)["derivative_floor"],
            "first_hit_iteration": floor_active[0]["iteration"] if floor_active else None,
            "active_iterations": len(floor_active),
            "total_forward_hits": sum(row["derivative_floor_hits"]["vb_forward"] for row in rows),
            "total_backward_hits": sum(row["derivative_floor_hits"]["vb_backward"] for row in rows),
            "localization_inference_from_counts": False,
        },
    }


def province_summaries() -> dict[str, Any]:
    accepted = read_json(SOURCE_ROOT / "province_mechanism_classification.json")["provinces"]
    accepted_by_name = {item["province"]: item for item in accepted}
    provinces = []
    for index, province, mechanism in PROVINCES:
        trace = read_json(SOURCE_ROOT / f"traces/p{index:02d}_{province}.json")
        argmax = summarize_argmax(_argmax_rows_from_trace(trace), b_size=20, a_size=160, z_size=2)
        timing = _timing_and_counts(trace)
        recurrence = trace["cycle_evidence"]
        provinces.append({
            "province_index": index, "province": province, "accepted_mechanism": mechanism,
            "accepted_mechanism_match": accepted_by_name[province]["classification"] == mechanism,
            "value_argmax_spatial_footprint": argmax,
            "spatial_label": argmax["spatial_label"],
            "selector_spatial_footprint": timing["selector"],
            "derivative_floor_spatial_footprint": timing["derivative_floor"],
            "recurrence_localization": {
                "joint_selector_hash_recurrence": recurrence.get("first_exact_joint_label_recurrence"),
                "joint_selector_hash_low_period_2_or_3": recurrence.get("exact_joint_label_low_period_2_or_3"),
                "exact_value_low_period_2_or_3": recurrence.get("exact_value_low_period_2_or_3"),
                "coordinate_resolved_recurrence": False,
                "localization_level": "HASH_LEVEL_ONLY" if province == "贵州" else "NOT_APPLICABLE",
            },
        })
    return {
        "schema": "CH5_MP4C_K1_J160_SIX_FAILURE_PROVINCE_SPATIAL_SUMMARY_V1",
        "pre_registered_before_trace_value_inspection": True,
        "concentration_threshold": CONCENTRATION_THRESHOLD,
        "near_boundary_index_bandwidth": 1,
        "province_count": len(provinces), "provinces": provinces,
    }


def _j640_summary() -> dict[str, Any]:
    rows = []
    with (J640_ROOT / "iteration_trace.csv").open(encoding="utf-8-sig", newline="") as handle:
        for item in csv.DictReader(handle):
            rows.append({
                "iteration": int(item["iteration"]),
                "b_index": int(item["argmax_b_index"]), "a_index": int(item["argmax_a_index"]), "z_index": int(item["argmax_z_index"]),
                "b": float(item["argmax_b"]), "a": float(item["argmax_a"]), "z": float(item["argmax_z"]),
            })
    summary = summarize_argmax(rows, b_size=20, a_size=640, z_size=2)
    return {
        "accepted_classification": "POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION",
        "value_argmax_spatial_footprint": summary,
        "comparison_limit": "J640_SPATIAL_COMPARISON_LIMITED_BY_ACCEPTED_EVIDENCE",
        "selector_coordinate_localization": "COORDINATE_LEVEL_SELECTOR_FOOTPRINT_UNAVAILABLE",
        "derivative_floor_coordinate_localization": "FLOOR_COORDINATE_LOCALIZATION_UNAVAILABLE",
        "new_j640_runtime": 0,
    }


def cross_province_summary(summary: dict[str, Any]) -> dict[str, Any]:
    by_name = {item["province"]: item for item in summary["provinces"]}
    chatter_names = ["天津", "山西", "重庆", "甘肃"]
    chatter_vectors = [by_name[name]["value_argmax_spatial_footprint"]["signature_vector"] for name in chatter_names]
    pairwise = []
    for i, left in enumerate(chatter_names):
        for right in chatter_names[i + 1:]:
            pairwise.append({
                "left": left, "right": right,
                "total_variation": total_variation(
                    by_name[left]["value_argmax_spatial_footprint"]["signature_vector"],
                    by_name[right]["value_argmax_spatial_footprint"]["signature_vector"],
                ),
            })
    common = materially_common(chatter_vectors)
    return {
        "schema": "CH5_MP4C_K1_J160_SIX_FAILURE_CROSS_PROVINCE_SPATIAL_COMPARISON_V1",
        "descriptive_only": True, "causal_claim": False,
        "common_signature_total_variation_threshold": COMMON_SIGNATURE_TV_THRESHOLD,
        "chatter_provinces": chatter_names,
        "chatter_value_argmax_pairwise_total_variation": pairwise,
        "chatter_value_argmax_materially_common": common,
        "chatter_spatial_conclusion": (
            "COMMON_VALUE_ARGMAX_SPATIAL_SIGNATURE__SELECTOR_AND_FLOOR_COORDINATES_UNAVAILABLE"
            if common else "HETEROGENEOUS_VALUE_ARGMAX_SPATIAL_SIGNATURE__SELECTOR_AND_FLOOR_COORDINATES_UNAVAILABLE"
        ),
        "jiangxi_vs_chatter": {
            "jiangxi_label": by_name["江西"]["spatial_label"],
            "chatter_labels": {name: by_name[name]["spatial_label"] for name in chatter_names},
            "floor_boundary_association": "FLOOR_COORDINATE_LOCALIZATION_UNAVAILABLE",
            "descriptive_only": True,
        },
        "guizhou_vs_chatter": {
            "guizhou_label": by_name["贵州"]["spatial_label"],
            "recurrence_localization": "HASH_LEVEL_ONLY",
            "coordinate_resolved_selector_cycle": False, "exact_value_cycle": False,
            "descriptive_only": True,
        },
        "j640_descriptive_comparison": _j640_summary(),
    }


def runtime_ledger() -> dict[str, Any]:
    return {
        "schema": "CH5_MP4C_K1_J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_RUNTIME_LEDGER_V1",
        "hjb": 0, "kfe": 0, "successful_province_hjb": 0, "failed_province_hjb": 0,
        "outer": 0, "firm": 0, "wage_recalculation": 0, "return_recalculation": 0,
        "matlab": 0, "k1b": 0, "k2": 0, "ge": 0, "downstream": 0,
        "shock": 0, "irf": 0, "results": 0, "scientific_retries": 0,
        "analysis_mode": "TRACE_ONLY_OFFLINE_ZERO_SCIENCE_RUNTIME",
    }


def _report(authority: dict[str, Any], summary: dict[str, Any], cross: dict[str, Any], panel: dict[str, Any]) -> str:
    j640 = cross["j640_descriptive_comparison"]
    j640_footprint = j640["value_argmax_spatial_footprint"]
    j640_shares = j640_footprint["shares"]
    lines = [
        "# CH5 MP4C K1 — J160 six-failure trace spatial localization audit", "",
        "## Panel spatial classification", "", f"`{panel['panel_spatial_classification']}`", "",
        "Results eligibility=`FALSE`.", "", "## Authority and pre-registration", "",
        f"Trace authority gate: `{'PASS' if authority['pass'] else 'TRACE_SPATIAL_LOCALIZATION_AUTHORITY_BLOCKED'}`.", "",
        f"Actual baseline: `{ACTUAL_BASELINE}`. Accepted source candidate: `{ACCEPTED_CANDIDATE}`.",
        "The accepted 35-entry six-failure manifest, six 100-iteration traces, source/input/instrumentation receipts, panel classifications, diagnostic report, and accepted J640 authority were verified before analysis.", "",
        "The near-boundary band was frozen before inspecting coordinate values: exact boundary is index `0` or `size-1`; near boundary is index distance exactly one from either edge, excluding exact endpoints; all remaining indices are interior. Asset-side concentration requires share `>=0.80`. The discrete `z` state is reported but is not treated as an asset boundary.", "",
        "## Province value-argmax spatial footprints", "",
        "| province | accepted mechanism | spatial label | modal `(b,a,z)` index | modal state | modal share | b lower/upper band | a lower/upper band | joint interior | location changes |",
        "|---|---|---|---|---|---:|---:|---:|---:|---:|",
    ]
    for item in summary["provinces"]:
        footprint = item["value_argmax_spatial_footprint"]
        mode = footprint["modal_location"]
        idx, state, shares = mode["index_zero_based"], mode["state"], footprint["shares"]
        lines.append(
            f"| {item['province']} | {item['accepted_mechanism']} | {item['spatial_label']} | "
            f"({idx['b']},{idx['a']},{idx['z']}) | ({state['b']:.12g},{state['a']:.12g},{state['z']:.12g}) | "
            f"{mode['share']:.2%} | {shares['b_lower_band']:.2%}/{shares['b_upper_band']:.2%} | "
            f"{shares['a_lower_band']:.2%}/{shares['a_upper_band']:.2%} | {shares['joint_asset_interior']:.2%} | "
            f"{footprint['argmax_location_change_count']} |"
        )
    lines.extend(["", "These labels describe only the sealed **value-update argmax spatial footprint**; they are not generalized to all unstable cells.", "", "## Selector and derivative-floor localization", ""])
    for item in summary["provinces"]:
        selector = item["selector_spatial_footprint"]
        floor = item["derivative_floor_spatial_footprint"]
        lines.append(
            f"- {item['province']}: selector `{selector['availability']}` (first change {selector['first_change_iteration']}, active iterations {selector['active_iterations']}); "
            f"floor `{floor['availability']}` (first hit {floor['first_hit_iteration']}, active iterations {floor['active_iterations']})."
        )
    lines.extend([
        "", "Counts and hashes were not converted into coordinates. Consequently, 江西 floor activity cannot be tied to a particular boundary, and 贵州's joint-selector recurrence remains hash-level only: iteration 96→98, period 2, with no coordinate-resolved selector recurrence and no exact value recurrence.", "",
        "## Cross-province comparison", "",
        f"Four-chatter comparison: `{cross['chatter_spatial_conclusion']}`. Maximum pairwise total-variation distance is `{max(item['total_variation'] for item in cross['chatter_value_argmax_pairwise_total_variation']):.6g}` under the pre-registered `0.20` materiality threshold. This comparison is limited to value argmax coordinates.", "",
        "江西 and 贵州 are compared descriptively with the chatter provinces. Their mechanism labels do not supply missing floor/selector coordinates and are not treated as causal location evidence.", "",
        f"Accepted J640 comparison: `{j640['comparison_limit']}`. J640 sealed value-argmax label: `{j640_footprint['spatial_label']}` "
        f"(b-upper band `{j640_shares['b_upper_band']:.2%}`, joint asset interior `{j640_shares['joint_asset_interior']:.2%}`). "
        "The accepted CSV supports this value-argmax spatial summary, but not selector-changed-cell or derivative-floor-hit coordinates; no J640 replay was run.", "",
        "## Panel conclusion", "", f"`{panel['panel_spatial_classification']}`", "",
        "This conclusion does not authorize boundary repair, grid expansion, HJB modification, or calibration modification. Scientific/model runtime remained exactly zero and Results eligibility remains `FALSE`.", "",
        "## Exactly one next gate", "", f"`{NEXT_GATE}`", "",
    ])
    return "\n".join(lines)


def _seal(root: Path) -> dict[str, Any]:
    entries = []
    for path in sorted(item for item in root.rglob("*") if item.is_file() and item.name != "sealed_manifest_sha256.json"):
        entries.append({"path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size, "sha256": file_sha256(path)})
    return {
        "schema": "CH5_MP4C_K1_J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_SEALED_MANIFEST_V1",
        "entry_count": len(entries), "bytes_excluding_manifest": sum(item["bytes"] for item in entries), "entries": entries,
    }


def finalize(evidence_root: Path, report_path: Path) -> dict[str, Any]:
    authority = source_trace_authority()
    if not authority["pass"]:
        raise RuntimeError("TRACE_SPATIAL_LOCALIZATION_AUTHORITY_BLOCKED")
    root = Path(evidence_root)
    root.mkdir(parents=True, exist_ok=False)
    summary = province_summaries()
    cross = cross_province_summary(summary)
    labels = [item["spatial_label"] for item in summary["provinces"]]
    panel = {
        "schema": "CH5_MP4C_K1_J160_SIX_FAILURE_PANEL_SPATIAL_DECISION_V1",
        "panel_spatial_classification": panel_decision(labels),
        "province_labels": {item["province"]: item["spatial_label"] for item in summary["provinces"]},
        "classification_scope": "SEALED_VALUE_UPDATE_ARGMAX_COORDINATES_ONLY",
        "selector_coordinate_evidence_available": False,
        "derivative_floor_coordinate_evidence_available": False,
        "causal_claim": False, "repair_authorized": False,
        "results_eligibility": False, "next_gate": NEXT_GATE,
    }
    ledger = runtime_ledger()
    write_json(root / "source_trace_authority.json", authority)
    write_json(root / "province_spatial_summary.json", summary)
    write_json(root / "cross_province_spatial_comparison.json", cross)
    write_json(root / "panel_spatial_decision.json", panel)
    write_json(root / "runtime_ledger.json", ledger)
    Path(report_path).write_text(_report(authority, summary, cross, panel), encoding="utf-8", newline="\n")
    write_json(root / "sealed_manifest_sha256.json", _seal(root))
    return panel


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence_root", type=Path)
    parser.add_argument("report_path", type=Path)
    args = parser.parse_args()
    print(json.dumps(finalize(args.evidence_root, args.report_path), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
