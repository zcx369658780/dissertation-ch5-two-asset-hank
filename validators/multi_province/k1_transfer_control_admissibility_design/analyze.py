"""Static analysis of accepted transfer-candidate receipts.

This module never imports or calls a household, HJB, KFE, firm, or trajectory
entry point.  It reads only already accepted JSON/NPZ evidence.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np


PERCENTILES = (50.0, 75.0, 90.0, 95.0, 97.5, 99.0, 99.5, 99.9, 100.0)
RAW_BRANCHES = ("d_bb", "d_bf", "d_fb", "d_ff")
TRACE_PATTERN = re.compile(
    r"annual_(g1|g2)_guarded/turn_(\d+)/instrumentation/p(\d+)_(.+)_hjb_trace\.json$"
)


def _quantiles(values: np.ndarray) -> dict[str, float]:
    return {
        f"p{percentile:g}": float(np.percentile(values, percentile))
        for percentile in PERCENTILES
    }


def summarize_numeric(values: np.ndarray) -> dict[str, Any]:
    """Summarize an actually persisted numeric population."""
    array = np.asarray(values, dtype=float).ravel()
    finite = array[np.isfinite(array)]
    if finite.size == 0:
        raise ValueError("numeric population contains no finite values")
    positive = finite[finite > 0.0]
    negative_abs = np.abs(finite[finite < 0.0])
    return {
        "count": int(array.size),
        "finite_count": int(finite.size),
        "nan_count": int(np.count_nonzero(np.isnan(array))),
        "positive_infinity_count": int(np.count_nonzero(np.isposinf(array))),
        "negative_infinity_count": int(np.count_nonzero(np.isneginf(array))),
        "min": float(np.min(finite)),
        "max": float(np.max(finite)),
        "median": float(np.median(finite)),
        "quantiles": _quantiles(finite),
        "abs_quantiles": _quantiles(np.abs(finite)),
        "positive_tail_quantiles": _quantiles(positive) if positive.size else {},
        "absolute_negative_tail_quantiles": _quantiles(negative_abs) if negative_abs.size else {},
        "positive_share_of_finite": float(np.count_nonzero(finite > 0.0) / finite.size),
        "negative_share_of_finite": float(np.count_nonzero(finite < 0.0) / finite.size),
        "zero_share_of_finite": float(np.count_nonzero(finite == 0.0) / finite.size),
    }


def assess_raw_candidate_resolution(record: dict[str, Any]) -> dict[str, Any]:
    """Classify the inferential resolution of one accepted trace summary."""
    available = [name for name in ("min", "median", "p95", "p99", "max") if name in record]
    return {
        "raw_candidate_arrays_persisted": False,
        "exact_hit_shares_supported": False,
        "exact_sign_shares_supported": False,
        "requested_full_percentile_set_supported": False,
        "available_order_statistics": available,
        "receipt_role": "ARRAY_SUMMARY_AND_HASH_ONLY",
    }


def exact_interval_hits(values: np.ndarray, lower: float, upper: float) -> dict[str, Any]:
    """Return exact inclusive-interval hit counts for persisted values."""
    if not np.isfinite([lower, upper]).all() or lower >= upper:
        raise ValueError("interval must have finite lower < upper")
    array = np.asarray(values, dtype=float).ravel()
    lower_hits = np.isfinite(array) & (array < lower)
    upper_hits = np.isfinite(array) & (array > upper)
    nonfinite = ~np.isfinite(array)
    hits = lower_hits | upper_hits | nonfinite
    return {
        "count": int(array.size),
        "preserved_unchanged_count": int(np.count_nonzero(~hits)),
        "inadmissible_count": int(np.count_nonzero(hits)),
        "hit_share": float(np.count_nonzero(hits) / array.size) if array.size else 0.0,
        "lower_hit_count": int(np.count_nonzero(lower_hits)),
        "upper_hit_count": int(np.count_nonzero(upper_hits)),
    }


def adjudicate_candidate(value: float, lower: float, upper: float) -> dict[str, Any]:
    """Describe A/B/C semantics for one already persisted raw candidate."""
    if not np.isfinite([value, lower, upper]).all() or lower >= upper:
        raise ValueError("candidate and interval must be finite with lower < upper")
    if value < lower:
        status = "inadmissible_lower"
        clipped = float(lower)
    elif value > upper:
        status = "inadmissible_upper"
        clipped = float(upper)
    else:
        status = "admissible"
        clipped = float(value)
    excluded = status != "admissible"
    return {
        "raw_status": status,
        "A_candidate_rejection": "excluded" if excluded else "admitted_unchanged",
        "B_candidate_clipping": clipped,
        "C_fallback_to_existing_zero": (
            "excluded__existing_zero_remains" if excluded else "admitted_unchanged"
        ),
    }


def raw_summary_interval_bounds(
    records: list[dict[str, Any]], lower: float, upper: float
) -> dict[str, Any]:
    """Bound, but never fabricate, hit counts from min/max-only receipts."""
    if not np.isfinite([lower, upper]).all() or lower >= upper:
        raise ValueError("interval must have finite lower < upper")
    represented = 0
    lower_bound = 0
    upper_bound = 0
    fully_inside = 0
    for record in records:
        count = int(record["count"])
        nonfinite = int(record.get("nonfinite_count", 0))
        finite_count = count - nonfinite
        represented += count
        below = finite_count > 0 and float(record["min"]) < lower
        above = finite_count > 0 and float(record["max"]) > upper
        lower_bound += nonfinite + int(below) + int(above)
        if below or above:
            upper_bound += finite_count
        else:
            fully_inside += finite_count
        upper_bound += nonfinite
    return {
        "represented_candidate_count": represented,
        "definite_inadmissible_lower_bound": lower_bound,
        "possible_inadmissible_upper_bound": upper_bound,
        "definite_preserved_unchanged_count": fully_inside,
        "exact_hit_share_supported": False,
        "hit_share_interval": [
            float(lower_bound / represented) if represented else 0.0,
            float(upper_bound / represented) if represented else 0.0,
        ],
        "bound_basis": "PER_ARRAY_MIN_MAX_AND_NONFINITE_COUNTS_ONLY",
    }


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _status(row: dict[str, Any], family: str) -> str:
    for status in ("lower", "upper", "unsaturated"):
        if bool(row.get(f"{family}_guard_{status}_hit", row.get(f"{family}_guard_{status}", False))):
            return status
    return "unknown"


def _interval_key(threshold: float) -> str:
    value = f"{threshold:g}"
    return f"[-{value},{value}]"


def _group_summary(values: np.ndarray, groups: list[tuple[Any, ...]]) -> dict[str, Any]:
    buckets: dict[str, list[float]] = defaultdict(list)
    for value, group in zip(values, groups, strict=True):
        buckets["|".join(map(str, group))].append(float(value))
    return {name: summarize_numeric(np.asarray(items)) for name, items in sorted(buckets.items())}


def _interval_hits_by_group(
    values: np.ndarray,
    groups: list[tuple[Any, ...]],
    thresholds: tuple[float, ...],
) -> dict[str, Any]:
    indexes: dict[str, list[int]] = defaultdict(list)
    for index, group in enumerate(groups):
        indexes["|".join(map(str, group))].append(index)
    return {
        name: {
            _interval_key(threshold): exact_interval_hits(values[positions], -threshold, threshold)
            for threshold in thresholds
        }
        for name, positions_list in sorted(indexes.items())
        if (positions := np.asarray(positions_list, dtype=int)).size
    }


def _raw_bounds_by_group(
    records: list[dict[str, Any]],
    fields: tuple[str, ...],
    thresholds: tuple[float, ...],
) -> dict[str, Any]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        groups["|".join(str(record[field]) for field in fields)].append(record)
    return {
        name: {
            _interval_key(threshold): raw_summary_interval_bounds(items, -threshold, threshold)
            for threshold in thresholds
        }
        for name, items in sorted(groups.items())
    }


def _array_hash(value: np.ndarray) -> str:
    array = np.asarray(value)
    header = f"{array.dtype.str}|{array.shape}|C|".encode("ascii")
    return hashlib.sha256(header + np.ascontiguousarray(array).tobytes()).hexdigest().upper()


def _known_grid_coordinate(index: tuple[int, int, int], shape: tuple[int, ...]) -> dict[str, float] | None:
    if shape != (20, 20, 2):
        return None
    b = np.linspace(-2.0, 5.0, 20)
    a = np.linspace(0.0, 10.0, 20)
    z = np.asarray([0.8, 1.3])
    return {"b": float(b[index[0]]), "a": float(a[index[1]]), "z": float(z[index[2]])}


def _implied_adjustment_cost(value: float, a: float) -> float:
    return float(0.1 * abs(value) + value * value / max(a, 1.0e-6))


def analyze_evidence(
    evidence_root: Path | str,
    expected_manifest_sha256: str,
    *,
    symmetric_thresholds: tuple[float, ...] = (1.0, 10.0, 100.0, 1_000.0, 10_000.0, 100_000.0, 1_000_000.0, 10_000_000.0),
) -> dict[str, Any]:
    """Analyze accepted evidence without invoking any scientific entry point."""
    root = Path(evidence_root)
    manifest_path = root / "manifest_sha256.json"
    actual_manifest_sha = _sha256(manifest_path)
    if actual_manifest_sha != expected_manifest_sha256.upper():
        raise ValueError("accepted external manifest SHA-256 mismatch")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = {str(item["path"]).replace("\\", "/"): item for item in manifest["files"]}
    if int(manifest["file_count"]) != len(entries):
        raise ValueError("accepted manifest file_count mismatch")

    traces = sorted(path for path in entries if TRACE_PATTERN.match(path))
    observations: dict[tuple[str, int, int], dict[str, Any]] = {}
    consumed_verified: set[str] = set()

    def verify(relative: str) -> Path:
        item = entries.get(relative)
        if item is None:
            raise ValueError(f"consumed evidence is absent from manifest: {relative}")
        path = root / Path(relative)
        if path.stat().st_size != int(item["bytes"]) or _sha256(path) != str(item["sha256"]).upper():
            raise ValueError(f"consumed evidence identity mismatch: {relative}")
        consumed_verified.add(relative)
        return path

    observation_paths = sorted(
        path for path in entries if re.match(r"annual_g[12]_guarded/turn_\d+/per_province_observables\.json$", path)
    )
    for relative in observation_paths:
        path_id = relative.split("/")[0].split("_")[1].upper()
        turn = int(relative.split("/")[1].split("_")[1])
        rows = json.loads(verify(relative).read_text(encoding="utf-8"))
        for row in rows:
            observations[(path_id, turn, int(row["province_index"]))] = row

    raw_records: list[dict[str, Any]] = []
    raw_witnesses: list[dict[str, Any]] = []
    selected_values: list[np.ndarray] = []
    selected_costs: list[np.ndarray] = []
    consumption_values: list[np.ndarray] = []
    labor_income_values: list[np.ndarray] = []
    transfer_income_receipts: list[float] = []
    selected_metadata: list[tuple[Any, ...]] = []
    selected_top: list[dict[str, Any]] = []
    priority: list[dict[str, Any]] = []
    trace_count = 0
    iteration_count = 0
    grid_hash_verified_count = 0

    standard_grid = {
        "b": np.linspace(-2.0, 5.0, 20),
        "a": np.linspace(0.0, 10.0, 20),
        "z": np.asarray([0.8, 1.3]),
        "switch_matrix": np.asarray([[-1 / 3, 1 / 3], [1 / 3, -1 / 3]]),
    }
    priority_cells = {
        ("湖北", 2): (1, 18, 0),
        ("四川", 4): (19, 16, 1),
        ("云南", 4): (10, 9, 0),
    }
    priority_iterations = {
        ("湖北", 2): {1, 2, 3, 4, 98, 100},
        ("四川", 4): {1, 57, 100},
        ("云南", 4): {1, 100},
    }
    dynamic_priority_iterations = {("山东", 2): 72, ("广东", 2): 82}

    for relative in traces:
        match = TRACE_PATTERN.match(relative)
        assert match is not None
        path_id = match.group(1).upper()
        turn = int(match.group(2))
        province_index = int(match.group(3))
        trace = json.loads(verify(relative).read_text(encoding="utf-8"))
        province = str(trace["province"])
        converged = bool(trace["final_converged"])
        obs = observations.get((path_id, turn, province_index), {})
        return_status = _status(obs, "return")
        wage_status = _status(obs, "wage")
        if "grid_sha256" in trace:
            expected_grid_hashes = {name: _array_hash(array) for name, array in standard_grid.items()}
            if trace["grid_sha256"] != expected_grid_hashes:
                raise ValueError(f"accepted trace grid identity mismatch: {relative}")
            grid_hash_verified_count += 1
        trace_count += 1
        for iteration in trace["iterations"]:
            iteration_count += 1
            number = int(iteration["iteration"])
            for branch in RAW_BRANCHES:
                record = dict(iteration["candidate_objects"][branch])
                record.update({
                    "branch": branch,
                    "path_id": path_id,
                    "turn": turn,
                    "province": province,
                    "province_index": province_index,
                    "hjb_iteration": number,
                    "hjb_converged": converged,
                    "return_guard_status": return_status,
                    "wage_guard_status": wage_status,
                })
                raw_records.append(record)
                witness = record.get("abs_max_witness")
                if witness:
                    raw_witnesses.append({
                        key: record[key] for key in (
                            "branch", "path_id", "turn", "province", "province_index",
                            "hjb_iteration", "hjb_converged", "return_guard_status", "wage_guard_status",
                        )
                    } | {
                        "value": float(witness["value"]),
                        "grid_index_zero_based": witness["grid_index_zero_based"],
                    })

            priority_key = (province, turn)
            if priority_key in priority_cells and number in priority_iterations[priority_key]:
                target = priority_cells[priority_key]
                for cell in iteration.get("checkpoint_cells", []):
                    location = cell.get("grid_index_zero_based", {})
                    found = (location.get("i_b"), location.get("i_a"), location.get("i_z"))
                    if found == target and not str(cell.get("witness_reason", "")).startswith("dynamic_abs_max_"):
                        branch_values = {
                            name: float(cell["transfer_candidates"][name]) for name in RAW_BRANCHES
                        }
                        a_value = float(cell["coordinate"]["a"])
                        priority.append({
                            "checkpoint": f"{province}_turn_{turn}_fixed_cell",
                            "path_id": path_id,
                            "turn": turn,
                            "province": province,
                            "province_index": province_index,
                            "hjb_iteration": number,
                            "hjb_converged": converged,
                            "comparison_classification": trace.get("comparison_classification"),
                            "grid_index_zero_based": location,
                            "coordinate": cell["coordinate"],
                            "boundary": cell["boundary"],
                            "raw_branch_candidates": branch_values,
                            "raw_branch_implied_adjustment_costs": {
                                name: _implied_adjustment_cost(value, a_value)
                                for name, value in branch_values.items()
                            },
                            "selected": cell["selected"],
                            "return_guard_status": return_status,
                            "wage_guard_status": wage_status,
                        })
                        break
            dynamic_key = (province, turn)
            if dynamic_priority_iterations.get(dynamic_key) == number:
                branch_witnesses = {}
                for branch in RAW_BRANCHES:
                    witness = iteration["candidate_objects"][branch]["abs_max_witness"]
                    index_dict = witness["grid_index_zero_based"]
                    index = (int(index_dict["i_b"]), int(index_dict["i_a"]), int(index_dict["i_z"]))
                    coordinate = _known_grid_coordinate(index, (20, 20, 2))
                    value = float(witness["value"])
                    branch_witnesses[branch] = {
                        "value": value,
                        "grid_index_zero_based": index_dict,
                        "coordinate": coordinate,
                        "implied_adjustment_cost": _implied_adjustment_cost(value, float(coordinate["a"])),
                    }
                priority.append({
                    "checkpoint": f"{province}_turn_{turn}_iteration_{number}_raw_branch_abs_max_witnesses",
                    "path_id": path_id,
                    "turn": turn,
                    "province": province,
                    "province_index": province_index,
                    "hjb_iteration": number,
                    "hjb_converged": converged,
                    "comparison_classification": trace.get("comparison_classification"),
                    "raw_branch_abs_max_witnesses": branch_witnesses,
                    "return_guard_status": return_status,
                    "wage_guard_status": wage_status,
                    "selected_adjustment_cost_abs_max": iteration.get("selected_objects", {}).get("adjustment_cost", {}).get("abs_max"),
                    "limitation": "Raw branch maxima and selected adjustment-cost maximum may be at different cells.",
                })

        npz_relative = (
            f"annual_{path_id.lower()}_guarded/turn_{turn:02d}/household/"
            f"p{province_index:02d}_{province}/hjb_return.npz"
        )
        npz_path = verify(npz_relative)
        with np.load(npz_path, allow_pickle=False) as payload:
            transfer = np.asarray(payload["transfer"], dtype=float)
            cost = np.asarray(payload["adjustment_cost"], dtype=float)
            labels = np.asarray(payload["transfer_label"])
            consumption = np.asarray(payload["consumption"], dtype=float) if "consumption" in payload.files else None
            labor = np.asarray(payload["labor"], dtype=float) if "labor" in payload.files else None
        selected_values.append(transfer.ravel())
        selected_costs.append(cost.ravel())
        if consumption is not None:
            consumption_values.append(consumption.ravel())
        trace_inputs = trace.get("inputs", {})
        if labor is not None and labor.shape[2] == 2 and trace_inputs:
            wage = float(trace_inputs["wages"][0])
            tax = float(trace_inputs["tau"])
            migration_cost = float(trace_inputs["migration_costs"][0])
            labor_income = np.empty_like(labor)
            for z_index, z_value in enumerate(standard_grid["z"]):
                labor_income[:, :, z_index] = (
                    wage * (1.0 - tax - migration_cost) * float(z_value) * labor[:, :, z_index]
                )
            labor_income_values.append(labor_income.ravel())
        if "transfer_income" in trace_inputs:
            transfer_income_receipts.append(float(trace_inputs["transfer_income"]))
        for index in np.ndindex(transfer.shape):
            boundary = index[0] in (0, transfer.shape[0] - 1) or index[1] in (0, transfer.shape[1] - 1)
            selected_metadata.append((
                path_id, turn, province, province_index, converged, return_status,
                wage_status, str(labels[index]), "asset_boundary" if boundary else "interior",
            ))
        finite_abs = np.where(np.isfinite(transfer), np.abs(transfer), -np.inf).ravel()
        top_count = min(10, finite_abs.size)
        for flat_index in np.argpartition(finite_abs, -top_count)[-top_count:]:
            index = tuple(int(item) for item in np.unravel_index(int(flat_index), transfer.shape))
            coordinate = _known_grid_coordinate(index, transfer.shape)
            row = {
                "path_id": path_id,
                "turn": turn,
                "province": province,
                "province_index": province_index,
                "hjb_converged": converged,
                "return_guard_status": return_status,
                "wage_guard_status": wage_status,
                "transfer_label": str(labels[index]),
                "grid_index_zero_based": {"i_b": index[0], "i_a": index[1], "i_z": index[2]},
                "coordinate": coordinate,
                "value": float(transfer[index]),
                "adjustment_cost": float(cost[index]),
            }
            if consumption is not None:
                row["consumption"] = float(consumption[index])
            if labor is not None:
                row["labor"] = float(labor[index])
            selected_top.append(row)

    selected = np.concatenate(selected_values) if selected_values else np.array([], dtype=float)
    costs = np.concatenate(selected_costs) if selected_costs else np.array([], dtype=float)
    consumption_population = (
        np.concatenate(consumption_values) if consumption_values else np.array([], dtype=float)
    )
    labor_income_population = (
        np.concatenate(labor_income_values) if labor_income_values else np.array([], dtype=float)
    )
    raw_by_branch = {
        branch: {
            "summary_array_count": len(items),
            "represented_candidate_count": int(sum(int(item["count"]) for item in items)),
            "finite_candidate_count": int(sum(int(item["count"]) - int(item.get("nonfinite_count", 0)) for item in items)),
            "nonfinite_candidate_count": int(sum(int(item.get("nonfinite_count", 0)) for item in items)),
            "global_min": float(min(float(item["min"]) for item in items)),
            "global_max": float(max(float(item["max"]) for item in items)),
            "summary_of_per_array_medians": summarize_numeric(np.asarray([item["median"] for item in items])),
            "summary_of_per_array_p99": summarize_numeric(np.asarray([item["p99"] for item in items])),
        }
        for branch in RAW_BRANCHES
        if (items := [item for item in raw_records if item["branch"] == branch])
    }
    raw_interval_bounds = {
        _interval_key(threshold): raw_summary_interval_bounds(raw_records, -threshold, threshold)
        for threshold in symmetric_thresholds
    }
    selected_interval_hits = {
        _interval_key(threshold): exact_interval_hits(selected, -threshold, threshold)
        for threshold in symmetric_thresholds
    }
    raw_top = sorted(raw_witnesses, key=lambda item: abs(item["value"]), reverse=True)[:100]
    selected_top = sorted(selected_top, key=lambda item: abs(item["value"]), reverse=True)[:100]
    positive_raw_max = max(float(item["max"]) for item in raw_records)
    negative_raw_abs_max = max(abs(float(item["min"])) for item in raw_records)
    raw_abs_witness_positive = sum(float(item["value"]) > 0.0 for item in raw_witnesses)
    raw_abs_witness_negative = sum(float(item["value"]) < 0.0 for item in raw_witnesses)
    selected_abs = summarize_numeric(np.abs(selected))
    selected_abs_quantiles = selected_abs["quantiles"]
    selected_groups = {
        "by_path": [(row[0],) for row in selected_metadata],
        "by_turn": [(row[1],) for row in selected_metadata],
        "by_path_turn": [(row[0], row[1]) for row in selected_metadata],
        "by_convergence": [(row[4],) for row in selected_metadata],
        "by_transfer_label": [(row[7],) for row in selected_metadata],
        "by_asset_boundary": [(row[8],) for row in selected_metadata],
        "by_return_guard_status": [(row[5],) for row in selected_metadata],
        "by_wage_guard_status": [(row[6],) for row in selected_metadata],
        "by_return_and_wage_guard_status": [(row[5], row[6]) for row in selected_metadata],
    }
    selected_group_summaries = {
        name: _group_summary(selected, groups) for name, groups in selected_groups.items()
    }
    selected_group_hits = {
        name: _interval_hits_by_group(selected, groups, symmetric_thresholds)
        for name, groups in selected_groups.items()
    }
    treatment_mask = np.asarray([row[1] >= 2 for row in selected_metadata], dtype=bool)
    priority = sorted(priority, key=lambda item: (
        item["province"], item["turn"], item["path_id"], item["hjb_iteration"]
    ))
    for item in priority:
        if "raw_branch_candidates" in item:
            candidates = item["raw_branch_candidates"]
        else:
            candidates = {
                branch: receipt["value"]
                for branch, receipt in item["raw_branch_abs_max_witnesses"].items()
            }
        item["diagnostic_threshold_adjudication"] = {
            _interval_key(threshold): {
                branch: adjudicate_candidate(float(value), -threshold, threshold)
                for branch, value in candidates.items()
            }
            for threshold in symmetric_thresholds
        }

    return {
        "schema": "CH5_MP4C_K1_TRANSFER_CONTROL_ADMISSIBILITY_DESIGN_ANALYSIS_V1",
        "classification": "RAW_CANDIDATE_ARRAYS_NOT_PERSISTED__EXACT_NUMERIC_LADDER_NOT_IDENTIFIED",
        "input_identity": {
            "external_evidence_root": str(root),
            "manifest_sha256": actual_manifest_sha,
            "manifest_file_count_excluding_manifest": len(entries),
            "trace_count": trace_count,
            "hjb_iteration_count": iteration_count,
            "consumed_file_hashes_verified": len(consumed_verified),
            "grid_hashes_verified": grid_hash_verified_count,
        },
        "raw_candidates": {
            "branches": list(RAW_BRANCHES),
            "raw_candidate_arrays_persisted": False,
            "exact_hit_shares_supported": False,
            "exact_sign_shares_supported": False,
            "requested_full_percentile_set_supported": False,
            "available_per_array_order_statistics": ["min", "median", "p95", "p99", "max", "abs_max"],
            "by_branch": raw_by_branch,
            "symmetric_interval_bounds": raw_interval_bounds,
            "symmetric_interval_bounds_by_branch": _raw_bounds_by_group(
                raw_records, ("branch",), symmetric_thresholds
            ),
            "symmetric_interval_bounds_by_path": _raw_bounds_by_group(
                raw_records, ("path_id",), symmetric_thresholds
            ),
            "symmetric_interval_bounds_by_path_turn": _raw_bounds_by_group(
                raw_records, ("path_id", "turn"), symmetric_thresholds
            ),
            "symmetric_interval_bounds_by_return_guard_status": _raw_bounds_by_group(
                raw_records, ("return_guard_status",), symmetric_thresholds
            ),
            "symmetric_interval_bounds_by_wage_guard_status": _raw_bounds_by_group(
                raw_records, ("wage_guard_status",), symmetric_thresholds
            ),
            "top_abs_per_array_witnesses": raw_top,
            "symmetry_receipt": {
                "positive_global_extreme": positive_raw_max,
                "absolute_negative_global_extreme": negative_raw_abs_max,
                "positive_to_negative_extreme_scale_ratio": float(positive_raw_max / negative_raw_abs_max),
                "per_array_abs_max_witness_sign_counts": {
                    "positive": raw_abs_witness_positive,
                    "negative": raw_abs_witness_negative,
                    "zero": len(raw_witnesses) - raw_abs_witness_positive - raw_abs_witness_negative,
                },
                "classification": "EXTREME_SCALE_ASYMMETRY_VISIBLE__CELL_LEVEL_SIGN_FREQUENCIES_UNAVAILABLE",
            },
            "important_limit": "Per-iteration hashes and summaries cannot reconstruct cell-level raw candidates.",
        },
        "selected_control": {
            "population_role": "FINAL_HJB_ITERATION_SELECTED_D_PER_ACCEPTED_PROVINCE_CALL",
            "overall": summarize_numeric(selected),
            "treatment_turns_2_to_5": summarize_numeric(selected[treatment_mask]),
            "adjustment_cost_overall": summarize_numeric(costs),
            "group_summaries": selected_group_summaries,
            "symmetric_interval_hits": selected_interval_hits,
            "symmetric_interval_hits_by_group": selected_group_hits,
            "top_abs_call_witnesses": selected_top,
            "log10_abs_plus_epsilon": summarize_numeric(np.log10(np.abs(selected) + 1.0e-300)),
            "tail_spacing": {
                "p99_5_over_p99": float(selected_abs_quantiles["p99.5"] / selected_abs_quantiles["p99"]),
                "p99_9_over_p99_5": float(selected_abs_quantiles["p99.9"] / selected_abs_quantiles["p99.5"]),
                "max_over_p99_9": float(selected_abs_quantiles["p100"] / selected_abs_quantiles["p99.9"]),
            },
        },
        "ordinary_region_and_explosive_tail": {
            "classification": "DESCRIPTIVE_NUMERICAL_CONTINUATION_DESIGN",
            "selected_abs_median": float(selected_abs_quantiles["p50"]),
            "selected_abs_p99": float(selected_abs_quantiles["p99"]),
            "selected_abs_p99_9": float(selected_abs_quantiles["p99.9"]),
            "selected_abs_max": float(selected_abs_quantiles["p100"]),
            "selected_max_to_median_ratio": float(selected_abs_quantiles["p100"] / selected_abs_quantiles["p50"]),
            "raw_global_abs_max": float(max(positive_raw_max, negative_raw_abs_max)),
            "finding": "Explosive finite tails are visible, but the cell-level raw distribution needed to locate a stable cutoff was not persisted.",
        },
        "asset_grid_scale_context": {
            "a_grid": {"min": 0.0, "max": 10.0, "span": 10.0, "points": 20},
            "b_grid": {"min": -2.0, "max": 5.0, "span": 7.0, "points": 20},
            "z_grid": [0.8, 1.3],
            "annual_control_unit": "d is asset-model units per year under the frozen annual continuous-time contract",
            "selected_abs_quantiles_over_a_span": {
                key: float(value / 10.0) for key, value in selected_abs_quantiles.items()
            },
            "adjustment_cost_formula": "0.1*abs(d) + d^2/max(a,1e-6) under chi0=.1 and chi1=2",
            "persisted_annual_flow_context": {
                "consumption": summarize_numeric(consumption_population) if consumption_population.size else "UNAVAILABLE",
                "labor_income_derived_from_persisted_inputs_and_labor": (
                    summarize_numeric(labor_income_population) if labor_income_population.size else "UNAVAILABLE"
                ),
                "exogenous_transfer_income_by_province_call": (
                    summarize_numeric(np.asarray(transfer_income_receipts))
                    if transfer_income_receipts else "UNAVAILABLE"
                ),
                "selected_transfer_flow": summarize_numeric(selected),
            },
            "interpretation_boundary": "NUMERICAL_SCALE_CONTEXT_ONLY__NOT_AN_ECONOMIC_TURNOVER_RESTRICTION",
        },
        "priority_checkpoints": priority,
        "safeguard_semantics": {
            "A_candidate_rejection": {
                "raw_receipt_preserved": True,
                "candidate_ranking_effect": "Removes inadmissible raw branches before selector competition.",
                "threshold_continuity": "Discrete eligibility change at the threshold.",
                "foc_fidelity": "HIGH_FOR_RETAINED_CANDIDATES",
                "selector_fidelity": "PARTIAL__COMPETITOR_SET_CHANGES",
                "fabricated_foc_candidate_risk": "NONE",
            },
            "B_candidate_clipping": {
                "raw_receipt_preserved": True,
                "candidate_ranking_effect": "Ranks a threshold-valued surrogate rather than the raw FOC candidate.",
                "threshold_continuity": "Control level continuous but derivative/ranking has a kink.",
                "foc_fidelity": "LOW_OUTSIDE_INTERVAL",
                "selector_fidelity": "LOWER__SURROGATE_COMPETITOR_IS_CREATED",
                "fabricated_foc_candidate_risk": "YES",
            },
            "C_fallback_to_existing_zero": {
                "raw_receipt_preserved": True,
                "candidate_ranking_effect": "Excludes inadmissible branches while retaining the already existing zero-transfer option.",
                "threshold_continuity": "Discrete switch may occur when no admissible nonzero branch wins.",
                "foc_fidelity": "HIGH__NO_CLIPPED_FOC_SURROGATE",
                "selector_fidelity": "HIGHEST_IF_ZERO_OPTION_REMAINS_UNCHANGED",
                "fabricated_foc_candidate_risk": "NONE_IF_EXISTING_ZERO_ONLY",
            },
            "preferred_semantics": "C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION",
            "owner_decision_required": True,
        },
        "numeric_ladder": {
            "status": "NUMERIC_TRANSFER_SAFEGUARD_LADDER_REMAINS_OWNER_DECISION_REQUIRED",
            "exact_raw_hit_shares_available": False,
            "bounded_symmetric_option_bands_not_a_preregistered_ladder": [
                {"D_range": [1_000.0, 10_000.0], "role": "tighter diagnostic option"},
                {"D_range": [10_000.0, 100_000.0], "role": "intermediate diagnostic option"},
                {"D_range": [100_000.0, 1_000_000.0], "role": "looser diagnostic option"},
                {"D_range": "OFF", "role": "unbounded comparator"},
            ],
            "symmetry_status": "SYMMETRIC_INTERVAL_IS_ONLY_A_SIMPLIFICATION_CANDIDATE_REQUIRING_OWNER_APPROVAL",
            "reason": "Accepted evidence lacks cell-level raw arrays, so exact raw hit shares, branch hit shares, sign-tail quantiles, and a stable raw scale break cannot be computed.",
        },
        "final_decision": {
            "classification": "TRANSFER_CANDIDATE_EXPLOSIVE_FINITE_TAIL_CONFIRMED__RAW_CELL_DISTRIBUTION_NOT_PERSISTED__NUMERIC_TRANSFER_SAFEGUARD_LADDER_REMAINS_OWNER_DECISION_REQUIRED",
            "preferred_semantics": "C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION",
            "unique_numeric_ladder_supported": False,
            "exactly_one_next_gate": "ADDITIONAL_ZERO_SCIENCE_DESIGN_TO_OBTAIN_CELL_LEVEL_RAW_CANDIDATE_DISTRIBUTIONS_BEFORE_OWNER_NUMERIC_FREEZE",
            "runtime_authorized": False,
            "kfe_caveat": "DIAGNOSTIC_ONLY__FINITE_BOX_UPPER_B_LEAKAGE_AND_MATLAB_STYLE_PINNING_UNRESOLVED",
            "results_eligibility": False,
        },
        "new_scientific_call_ledger": {
            "trajectory": 0,
            "outer_turn": 0,
            "HJB": 0,
            "KFE": 0,
            "household_runtime": 0,
            "firm_runtime": 0,
            "MATLAB_runtime": 0,
            "K1B": 0,
            "K2": 0,
            "GE": 0,
            "annual_downstream": 0,
            "shock_IRF": 0,
            "Results": 0,
        },
    }


def write_outputs(result: dict[str, Any], output_dir: Path | str) -> list[Path]:
    """Write compact task evidence derived from an analysis result."""
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    analysis_path = destination / "analysis.json"
    with analysis_path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False))
        stream.write("\n")
    raw_path = destination / "raw_candidate_interval_bounds.csv"
    with raw_path.open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=(
            "interval", "represented_candidate_count", "definite_inadmissible_lower_bound",
            "possible_inadmissible_upper_bound", "definite_preserved_unchanged_count",
            "hit_share_lower_bound", "hit_share_upper_bound", "exact_hit_share_supported",
        ))
        writer.writeheader()
        for interval, row in result["raw_candidates"]["symmetric_interval_bounds"].items():
            writer.writerow({
                "interval": interval,
                "represented_candidate_count": row["represented_candidate_count"],
                "definite_inadmissible_lower_bound": row["definite_inadmissible_lower_bound"],
                "possible_inadmissible_upper_bound": row["possible_inadmissible_upper_bound"],
                "definite_preserved_unchanged_count": row["definite_preserved_unchanged_count"],
                "hit_share_lower_bound": row["hit_share_interval"][0],
                "hit_share_upper_bound": row["hit_share_interval"][1],
                "exact_hit_share_supported": row["exact_hit_share_supported"],
            })
    selected_path = destination / "selected_control_interval_hits.csv"
    with selected_path.open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=(
            "interval", "count", "preserved_unchanged_count", "inadmissible_count",
            "hit_share", "lower_hit_count", "upper_hit_count",
        ))
        writer.writeheader()
        for interval, row in result["selected_control"]["symmetric_interval_hits"].items():
            writer.writerow({"interval": interval, **row})
    return [analysis_path, raw_path, selected_path]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence-root", type=Path, required=True)
    parser.add_argument("--expected-manifest-sha256", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--symmetric-thresholds",
        default="1,3,5,10,30,100,300,1000,3000,10000,100000,1000000,10000000,100000000",
    )
    args = parser.parse_args()
    thresholds = tuple(float(value) for value in args.symmetric_thresholds.split(","))
    result = analyze_evidence(
        args.evidence_root,
        args.expected_manifest_sha256,
        symmetric_thresholds=thresholds,
    )
    paths = write_outputs(result, args.output_dir)
    print(json.dumps({
        "status": "PASS",
        "classification": result["final_decision"]["classification"],
        "outputs": [str(path) for path in paths],
        "new_scientific_call_ledger": result["new_scientific_call_ledger"],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
