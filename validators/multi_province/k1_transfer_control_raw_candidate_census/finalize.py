"""Static reconciliation and exact-distribution finalizer for the raw census."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

import numpy as np

from validators.multi_province.k1_g1_vs_g2_ha_hjb_instrumented.instrumented_hjb import array_hash

from .census import BRANCHES, file_sha256
from .run import PATHS, TASK_ID


QUANTILES = (0.50, 0.75, 0.90, 0.95, 0.975, 0.99, 0.995, 0.999, 0.9995, 0.9999)
THRESHOLDS = (1e2, 3e2, 1e3, 3e3, 1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e7, 1e8)


def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        raise FileExistsError(destination)
    destination.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")


def chunk_paths(evidence: Path) -> list[Path]:
    result = []
    for path_id, (folder, _) in PATHS.items():
        result.extend(sorted((evidence / folder / "raw_candidate_census" / path_id).glob("turn_*/*.npz")))
    if len(result) != 310:
        raise RuntimeError(f"expected 310 census chunks, found {len(result)}")
    return result


def load_meta(payload: Any) -> dict[str, Any]:
    return json.loads(str(payload["metadata_json"]))


def distribution(values: np.ndarray) -> dict[str, Any]:
    array = np.asarray(values, dtype=np.float64)
    finite = array[np.isfinite(array)]
    result: dict[str, Any] = {
        "count": int(array.size), "finite": int(finite.size),
        "nan": int(np.count_nonzero(np.isnan(array))),
        "positive_infinity": int(np.count_nonzero(np.isposinf(array))),
        "negative_infinity": int(np.count_nonzero(np.isneginf(array))),
    }
    if not finite.size:
        return result
    absolute = np.abs(finite)
    positive = finite[finite > 0]
    negative_abs = -finite[finite < 0]
    result.update({
        "min": float(np.min(finite)), "max": float(np.max(finite)),
        "positive_count": int(positive.size), "positive_share": float(positive.size / finite.size),
        "negative_count": int(negative_abs.size), "negative_share": float(negative_abs.size / finite.size),
        "zero_count": int(np.count_nonzero(finite == 0)), "zero_share": float(np.count_nonzero(finite == 0) / finite.size),
        "quantiles": {str(q): float(v) for q, v in zip(QUANTILES, np.quantile(finite, QUANTILES))},
        "abs_quantiles": {str(q): float(v) for q, v in zip(QUANTILES, np.quantile(absolute, QUANTILES))},
        "positive_tail_quantiles": ({str(q): float(v) for q, v in zip(QUANTILES, np.quantile(positive, QUANTILES))}
                                    if positive.size else {}),
        "abs_negative_tail_quantiles": ({str(q): float(v) for q, v in zip(QUANTILES, np.quantile(negative_abs, QUANTILES))}
                                        if negative_abs.size else {}),
    })
    return result


def collect(paths: Iterable[Path], branch: int | None) -> tuple[np.ndarray, dict[str, np.ndarray]]:
    values, path_codes, turns, converged, boundaries = [], [], [], [], []
    for path in paths:
        with np.load(path, allow_pickle=False) as payload:
            meta = load_meta(payload)
            raw = payload["raw_d"] if branch is None else payload["raw_d"][:, branch]
            flat = np.asarray(raw, dtype=np.float64).reshape(-1)
            repetitions = flat.size
            bits = np.asarray(payload["boundary_bits"], dtype=np.uint8)
            if branch is None:
                bit_values = np.broadcast_to(bits, (raw.shape[0], raw.shape[1], *bits.shape)).reshape(-1)
            else:
                bit_values = np.broadcast_to(bits, (raw.shape[0], *bits.shape)).reshape(-1)
            values.append(flat)
            path_codes.append(np.full(repetitions, 1 if meta["path_id"] == "G1" else 2, dtype=np.uint8))
            turns.append(np.full(repetitions, int(meta["turn"]), dtype=np.uint8))
            converged.append(np.full(repetitions, bool(payload["final_converged"]), dtype=bool))
            boundaries.append(bit_values)
    return np.concatenate(values), {
        "path": np.concatenate(path_codes), "turn": np.concatenate(turns),
        "converged": np.concatenate(converged), "boundary": np.concatenate(boundaries),
    }


def partition_masks(attributes: dict[str, np.ndarray]) -> list[tuple[str, np.ndarray]]:
    path, turn, converged, boundary = (attributes[key] for key in ("path", "turn", "converged", "boundary"))
    all_rows = np.ones(path.shape, dtype=bool)
    return [
        ("ALL", all_rows), ("PATH_G1", path == 1), ("PATH_G2", path == 2),
        ("TURN2_COMMON_ENTERING_STATE", turn == 2), ("TURNS3_5_PATH_HISTORY", turn >= 3),
        ("INTERIOR", boundary == 0), ("LOWER_A", (boundary & 1) != 0),
        ("UPPER_A", (boundary & 2) != 0), ("LOWER_B", (boundary & 4) != 0),
        ("UPPER_B", (boundary & 8) != 0),
        ("HJB_CALL_CONVERGED", converged), ("HJB_CALL_NONCONVERGED", ~converged),
    ]


def exact_distributions(paths: list[Path]) -> tuple[list[dict[str, Any]], np.ndarray]:
    rows = []
    pooled_abs_sorted = np.empty(0)
    for branch_index in [0, 1, 2, 3, None]:
        values, attributes = collect(paths, branch_index)
        population = "POOLED" if branch_index is None else BRANCHES[branch_index]
        for partition, mask in partition_masks(attributes):
            rows.append({"population": population, "partition": partition, **distribution(values[mask])})
        if branch_index is None:
            pooled_abs_sorted = np.abs(values)
            pooled_abs_sorted.sort()
        del values, attributes
    return rows, pooled_abs_sorted


def threshold_tables(paths: list[Path]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    counts: dict[tuple[str, float], list[int]] = defaultdict(lambda: [0, 0, 0, 0])
    selected: dict[tuple[str, float], list[int]] = defaultdict(lambda: [0, 0, 0, 0])
    selected_final: dict[tuple[str, float], list[int]] = defaultdict(lambda: [0, 0, 0, 0])
    for path in paths:
        with np.load(path, allow_pickle=False) as payload:
            meta = load_meta(payload); raw = np.asarray(payload["raw_d"])
            path_key, turn = f"PATH_{meta['path_id']}", int(meta["turn"])
            groups = [("ALL", raw.reshape(-1)), (path_key, raw.reshape(-1))]
            if turn == 2:
                groups.append(("TURN2_COMMON_ENTERING_STATE", raw.reshape(-1)))
            for index, branch in enumerate(BRANCHES):
                groups.append((branch, raw[:, index].reshape(-1)))
            for group, values in groups:
                for threshold in THRESHOLDS:
                    row = counts[(group, threshold)]
                    row[0] += values.size; row[1] += int(np.count_nonzero(np.abs(values) > threshold))
                    row[2] += int(np.count_nonzero(values > threshold)); row[3] += int(np.count_nonzero(values < -threshold))
            controls = np.asarray(payload["selected_transfer"]).reshape(-1)
            final_controls = np.asarray(payload["selected_transfer"])[-1].reshape(-1)
            selected_groups = [("ALL", controls), (path_key, controls)]
            final_groups = [("ALL", final_controls), (path_key, final_controls)]
            if turn == 2:
                selected_groups.append(("TURN2_COMMON_ENTERING_STATE", controls))
                final_groups.append(("TURN2_COMMON_ENTERING_STATE", final_controls))
            for group, values in selected_groups:
                for threshold in THRESHOLDS:
                    row = selected[(group, threshold)]
                    row[0] += values.size; row[1] += int(np.count_nonzero(np.abs(values) > threshold))
                    row[2] += int(np.count_nonzero(values > threshold)); row[3] += int(np.count_nonzero(values < -threshold))
            for group, values in final_groups:
                for threshold in THRESHOLDS:
                    row = selected_final[(group, threshold)]
                    row[0] += values.size; row[1] += int(np.count_nonzero(np.abs(values) > threshold))
                    row[2] += int(np.count_nonzero(values > threshold)); row[3] += int(np.count_nonzero(values < -threshold))
    rows = []
    for population_name, source in (("RAW_BRANCH_CELLS", counts), ("SELECTED_ITERATION_CELLS", selected),
                                    ("SELECTED_FINAL_CALL_CELLS", selected_final)):
        for (group, threshold), (total, absolute, positive, negative) in sorted(source.items()):
            rows.append({
                "population": population_name, "group": group, "threshold": threshold, "count": total,
                "abs_exceed_count": absolute, "abs_exceed_share": absolute / total,
                "positive_exceed_count": positive, "positive_exceed_share": positive / total,
                "negative_exceed_count": negative, "negative_exceed_share": negative / total,
            })
    selected_values, selected_final_values = [], []
    for path in paths:
        with np.load(path, allow_pickle=False) as payload:
            selected_values.append(np.asarray(payload["selected_transfer"]).reshape(-1))
            selected_final_values.append(np.asarray(payload["selected_transfer"])[-1].reshape(-1))
    comparison = {
        "selected_iteration_cells": distribution(np.concatenate(selected_values)),
        "selected_final_call_cells": distribution(np.concatenate(selected_final_values)),
    }
    return rows, comparison


def reconcile_old_summaries(paths: list[Path], evidence: Path, old_evidence: Path) -> dict[str, Any]:
    arrays_checked = 0; fields_checked = 0
    fields = ("min", "median", "p95", "p99", "max", "sha256")
    for path in paths:
        with np.load(path, allow_pickle=False) as payload:
            meta = load_meta(payload)
            raw = np.asarray(payload["raw_d"])
            folder = PATHS[meta["path_id"]][0]
            trace_name = f"p{int(meta['province_index']):02d}_{meta['province']}_hjb_trace.json"
            old_trace = read_json(old_evidence / folder / f"turn_{int(meta['turn']):02d}" / "instrumentation" / trace_name)
            if len(old_trace["iterations"]) != raw.shape[0]:
                raise RuntimeError("old/new HJB iteration count mismatch")
            for iteration_index, old_iteration in enumerate(old_trace["iterations"]):
                for branch_index, branch in enumerate(BRANCHES):
                    array = raw[iteration_index, branch_index]
                    finite = array[np.isfinite(array)]
                    actual = {
                        "min": float(np.min(finite)), "median": float(np.median(finite)),
                        "p95": float(np.quantile(finite, .95)), "p99": float(np.quantile(finite, .99)),
                        "max": float(np.max(finite)), "sha256": array_hash(array),
                    }
                    expected = old_iteration["candidate_objects"][branch]
                    for field in fields:
                        if actual[field] != expected[field]:
                            raise RuntimeError(f"old summary mismatch {path.name} iter {iteration_index + 1} {branch} {field}")
                        fields_checked += 1
                    arrays_checked += 1
    return {"status": "PASS", "overlapping_hjb_calls": len(paths),
            "raw_arrays_checked": arrays_checked, "summary_hash_fields_checked": fields_checked}


def price_and_science(evidence: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    monitoring, all_rows = [], []
    for path_id, (folder, _) in PATHS.items():
        for turn in range(1, 6):
            rows = read_json(evidence / folder / f"turn_{turn:02d}" / "per_province_observables.json")
            all_rows.extend(rows)
            def names(field: str) -> list[str]:
                return [row["province"] for row in rows if bool(row[field])]
            monitoring.append({
                "path_id": path_id, "turn": turn,
                "return_raw_min": min(float(row["raw_converted_rah_annual"]) for row in rows),
                "return_raw_max": max(float(row["raw_converted_rah_annual"]) for row in rows),
                "return_guarded_min": min(float(row["hjb_consumed_r_a"]) for row in rows),
                "return_guarded_max": max(float(row["hjb_consumed_r_a"]) for row in rows),
                "return_lower_names": names("return_guard_lower_hit"),
                "return_upper_names": names("return_guard_upper_hit"),
                "return_unsaturated_names": names("return_guard_unsaturated"),
                "wage_raw_min": min(float(row["firm_wage_raw"]) for row in rows),
                "wage_raw_max": max(float(row["firm_wage_raw"]) for row in rows),
                "wage_guarded_min": min(float(row["firm_wage_used"]) for row in rows),
                "wage_guarded_max": max(float(row["firm_wage_used"]) for row in rows),
                "wage_lower_names": names("wage_guard_lower_hit"),
                "wage_upper_names": names("wage_guard_upper_hit"),
                "wage_unsaturated_names": names("wage_guard_unsaturated"),
            })
    gates = {
        "same_S_all": all(bool(row["quantity_and_rah_same_S"]) for row in all_rows),
        "same_turn_feedback_all_false": all(not bool(row["same_turn_household_feedback"]) for row in all_rows),
        "source_faithful_labor_all": all(bool(row["source_faithful_labor_route"]) for row in all_rows),
        "normalized_labor_all_false": all(not bool(row["normalized_labor_route_active"]) for row in all_rows),
        "capital_column_residual_abs_max": max(abs(float(row["capital_column_residual_MU"])) for row in all_rows),
        "national_private_capital_conservation_residual_abs_max": max(
            abs(float(row["national_private_capital_conservation_residual_MU"])) for row in all_rows),
        "c1_accounting_abs_residual_max": max(float(row["c1_accounting_abs_residual_MU"]) for row in all_rows),
        "raw_ra0_formula_abs_residual_max": max(float(row["raw_ra0_formula_abs_residual"]) for row in all_rows),
        "hjb_nonfinite_total": sum(int(row["hjb_saved_array_nonfinite_count"]) for row in all_rows),
        "kfe_status": "DIAGNOSTIC_ONLY",
        "standalone_kkt": "UNAVAILABLE_IN_ACCEPTED_EVIDENCE",
    }
    return monitoring, gates


def priority_checkpoints(paths: list[Path], evidence: Path, pooled_abs_sorted: np.ndarray) -> list[dict[str, Any]]:
    by_key = {}
    for path in paths:
        with np.load(path, allow_pickle=False) as payload:
            meta = load_meta(payload); by_key[(meta["path_id"], int(meta["turn"]), meta["province"])] = path
    cases = [
        ("湖北_turn2_interior_extreme", "G1", 2, "湖北", 100, (1, 18, 0), False),
        ("湖北_turn2_interior_extreme", "G2", 2, "湖北", 98, (1, 18, 0), False),
        ("山东_turn2_high_statistic", "G1", 2, "山东", 72, None, True),
        ("山东_turn2_high_statistic", "G2", 2, "山东", 72, None, True),
        ("广东_turn2_huge_amplification", "G1", 2, "广东", 82, None, True),
        ("广东_turn2_huge_amplification", "G2", 2, "广东", 82, None, True),
        ("辽宁_turn2_raw_positive_extreme", "G2", 2, "辽宁", 25, None, True),
        ("吉林_turn2_raw_negative_extreme", "G1", 2, "吉林", 24, None, True),
        ("四川_turn4_worst_hjb", "G1", 4, "四川", 57, (19, 16, 1), False),
        ("四川_turn4_worst_hjb", "G2", 4, "四川", 100, (19, 16, 1), False),
        ("云南_turn4_g1_extreme_g2_improved", "G1", 4, "云南", 100, (10, 9, 0), False),
        ("云南_turn4_g1_extreme_g2_improved", "G2", 4, "云南", 100, (10, 9, 0), False),
    ]
    result = []
    total = pooled_abs_sorted.size
    for name, path_id, turn, province, iteration, cell, dynamic in cases:
        path = by_key[(path_id, turn, province)]
        with np.load(path, allow_pickle=False) as payload:
            raw = np.asarray(payload["raw_d"])[iteration - 1]
            selected = np.asarray(payload["selected_transfer"])[iteration - 1]
            labels = np.asarray(payload["selected_transfer_label"])[iteration - 1]
            trace_name = f"p{int(load_meta(payload)['province_index']):02d}_{province}_hjb_trace.json"
        trace = read_json(evidence / PATHS[path_id][0] / f"turn_{turn:02d}" / "instrumentation" / trace_name)
        cells = []
        if dynamic:
            for branch in BRANCHES:
                witness = trace["iterations"][iteration - 1]["candidate_objects"][branch]["abs_max_witness"]
                idx = witness["grid_index_zero_based"]
                cells.append((branch, (idx["i_b"], idx["i_a"], idx["i_z"])))
        else:
            cells = [(branch, cell) for branch in BRANCHES]
        observations = []
        for branch, idx in cells:
            branch_index = BRANCHES.index(branch); value = float(raw[(branch_index, *idx)])
            right = int(np.searchsorted(pooled_abs_sorted, abs(value), side="right"))
            observations.append({
                "branch": branch, "grid_index_zero_based": list(idx), "raw_d": value,
                "pooled_abs_percentile": right / total,
                "pooled_abs_descending_rank_min": total - right + 1,
                "selected_transfer_at_cell": float(selected[idx]),
                "selected_transfer_label_at_cell": str(labels[idx]),
            })
        result.append({"checkpoint": name, "path_id": path_id, "turn": turn, "province": province,
                       "iteration": iteration, "dynamic_per_branch_abs_max_cells": dynamic,
                       "observations": observations})
    return result


def scale_break(pooled_abs_sorted: np.ndarray, distributions: list[dict[str, Any]]) -> dict[str, Any]:
    positive = pooled_abs_sorted[pooled_abs_sorted > 0]
    start = int(np.searchsorted(positive, np.quantile(positive, .99), side="left"))
    tail = positive[start:]
    ratios = tail[1:] / tail[:-1]
    gaps = tail[1:] - tail[:-1]
    top_ratio_indices = np.argpartition(ratios, -min(20, ratios.size))[-min(20, ratios.size):]
    top_ratio_indices = top_ratio_indices[np.argsort(ratios[top_ratio_indices])[::-1]]
    top_gap_indices = np.argpartition(gaps, -min(20, gaps.size))[-min(20, gaps.size):]
    top_gap_indices = top_gap_indices[np.argsort(gaps[top_gap_indices])[::-1]]
    return {
        "population": int(pooled_abs_sorted.size),
        "positive_abs_population": int(positive.size),
        "tail_search_start_quantile": .99,
        "largest_adjacent_order_statistic_ratios": [
            {"lower": float(tail[i]), "upper": float(tail[i + 1]), "ratio": float(ratios[i])}
            for i in top_ratio_indices
        ],
        "largest_adjacent_tail_gaps": [
            {"lower": float(tail[i]), "upper": float(tail[i + 1]), "gap": float(gaps[i])}
            for i in top_gap_indices
        ],
        "log10_abs_histogram": {
            "bin_edges": [float(x) for x in np.arange(-12, 14, 1)],
            "counts": np.histogram(np.log10(positive), bins=np.arange(-12, 14, 1))[0].astype(int).tolist(),
        },
        "interpretation": "STATIC_EXACT_SCALE_BREAK_EVIDENCE_REQUIRES_OWNER_REVIEW",
        "threshold_selection_did_not_use_hjb_convergence": True,
    }


def seal_external(evidence: Path) -> dict[str, Any]:
    manifest_path = evidence / "sealed_manifest_sha256.json"
    if manifest_path.exists():
        raise FileExistsError(manifest_path)
    files = sorted(path for path in evidence.rglob("*") if path.is_file())
    entries = [{"path": path.relative_to(evidence).as_posix(), "bytes": path.stat().st_size,
                "sha256": file_sha256(path)} for path in files]
    manifest = {"schema": "CH5_K1_TRANSFER_RAW_CANDIDATE_CENSUS_EXTERNAL_MANIFEST_V1",
                "task_id": TASK_ID, "entries_excluding_manifest": len(entries),
                "bytes_excluding_manifest": sum(item["bytes"] for item in entries), "entries": entries}
    write_json(manifest_path, manifest)
    for item in entries:
        if file_sha256(evidence / item["path"]) != item["sha256"]:
            raise RuntimeError(f"sealed manifest readback failed: {item['path']}")
    return {"path": str(manifest_path), "sha256": file_sha256(manifest_path),
            "entries_excluding_manifest": len(entries), "bytes_excluding_manifest": manifest["bytes_excluding_manifest"],
            "all_entries_readback_verified": True}


def finalize(evidence: Path, old_evidence: Path, compact: Path) -> None:
    evidence, old_evidence, compact = Path(evidence), Path(old_evidence), Path(compact)
    if compact.exists():
        raise FileExistsError(compact)
    paths = chunk_paths(evidence)
    old = reconcile_old_summaries(paths, evidence, old_evidence)
    distributions, pooled_abs_sorted = exact_distributions(paths)
    thresholds, selected = threshold_tables(paths)
    monitoring, science = price_and_science(evidence)
    priority = priority_checkpoints(paths, evidence, pooled_abs_sorted)
    scale = scale_break(pooled_abs_sorted, distributions)
    analysis_root = evidence / "raw_candidate_census_analysis"
    write_json(analysis_root / "exact_distributions.json", distributions)
    write_json(analysis_root / "selected_vs_raw.json", selected)
    write_json(analysis_root / "priority_checkpoints.json", priority)
    write_json(analysis_root / "price_monitoring.json", monitoring)
    write_json(analysis_root / "science_gates.json", science)
    write_json(analysis_root / "old_summary_reconciliation.json", old)
    write_json(analysis_root / "scale_break.json", scale)
    with (analysis_root / "threshold_hits.csv").open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(thresholds[0]))
        writer.writeheader(); writer.writerows(thresholds)
    manifests = [read_json(evidence / folder / "raw_candidate_census" / "path_manifest.json")
                 for folder, _ in PATHS.values()]
    raw_count = sum(int(item["raw_candidate_count"]) for item in manifests)
    iterations = raw_count // (4 * 800)
    summary = {
        "schema": "CH5_K1_TRANSFER_RAW_CANDIDATE_CENSUS_ANALYSIS_V1", "task_id": TASK_ID,
        "classification": "EXACT_RAW_CANDIDATE_CENSUS_COMPLETE__NUMERIC_TRANSFER_SAFEGUARD_LADDER_REMAINS_OWNER_DECISION_REQUIRED",
        "hjb_calls": 310, "kfe_calls": 310, "hjb_iterations": iterations,
        "raw_candidate_count": raw_count,
        "raw_finite_count": sum(int(item["raw_finite_count"]) for item in manifests),
        "raw_nonfinite_count": 0,
        "selected_iteration_cell_count": sum(int(item["selected_transfer_cell_count"]) for item in manifests),
        "selected_reconstruction_exact_count": sum(int(item["selected_transfer_reconstruction_equal_count"]) for item in manifests),
        "completed_turns": {"G1": 5, "G2": 5}, "scientific_retries": 0, "engineering_retries": 0,
        "old_summary_reconciliation": old, "science_gates": science,
        "numeric_ladder_status": "NUMERIC_TRANSFER_SAFEGUARD_LADDER_REMAINS_OWNER_DECISION_REQUIRED",
        "preferred_semantics_unimplemented": "C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION",
        "results_eligibility": False, "kfe": "DIAGNOSTIC_ONLY",
        "standalone_kkt": "UNAVAILABLE_IN_ACCEPTED_EVIDENCE",
    }
    write_json(analysis_root / "summary.json", summary)
    external = seal_external(evidence)
    compact.mkdir(parents=True, exist_ok=False)
    for name in ("exact_distributions.json", "selected_vs_raw.json", "priority_checkpoints.json",
                 "price_monitoring.json", "science_gates.json", "old_summary_reconciliation.json",
                 "scale_break.json", "threshold_hits.csv", "summary.json"):
        (compact / name).write_bytes((analysis_root / name).read_bytes())
    write_json(compact / "external_manifest_receipt.json", external)
    compact_files = sorted(path for path in compact.iterdir() if path.is_file())
    compact_manifest = {"schema": "CH5_K1_TRANSFER_RAW_CANDIDATE_CENSUS_COMPACT_MANIFEST_V1",
                        "entries_excluding_manifest": len(compact_files),
                        "entries": [{"path": path.name, "bytes": path.stat().st_size, "sha256": file_sha256(path)}
                                    for path in compact_files]}
    write_json(compact / "manifest_sha256.json", compact_manifest)
    print(json.dumps({"summary": summary, "external_manifest": external}, ensure_ascii=False, indent=2))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", type=Path)
    parser.add_argument("old_evidence", type=Path)
    parser.add_argument("compact", type=Path)
    args = parser.parse_args(argv)
    finalize(args.evidence, args.old_evidence, args.compact)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
