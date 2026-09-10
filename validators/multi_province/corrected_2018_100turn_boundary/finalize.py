"""Finalize the saved 100-turn trajectory without scientific calls."""
from __future__ import annotations

import csv
import json
import shutil
from collections import Counter
from hashlib import sha256
from pathlib import Path
from typing import Any, Iterable

import numpy as np

from validators.multi_province.corrected_2018_100turn_boundary import run

REPO = Path(__file__).resolve().parents[3]
EVIDENCE = Path(r"D:\ProjectTemp\ch5-corrected-2018-100turn-boundary-trajectory-20260910-002")
REPORT_DIR = REPO / "reports/mp4c_corrected_2018_100turn_boundary_trajectory_20260910"
REPORT = REPO / "docs/CH5_MP4C_CORRECTED_2018_100_TURN_BOUNDARY_TRAJECTORY_DIAGNOSTIC_REPORT.md"
EXECUTED = {run.VERDICT_PASS, run.VERDICT_PARTIAL, run.VERDICT_FAIL, run.VERDICT_BLOCKED,
            *run.VERDICT_TURN_MISMATCH.values()}


def read(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
        stream.write("\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fields: Iterable[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    names = list(fields or (rows[0].keys() if rows else ()))
    with path.open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=names)
        writer.writeheader()
        writer.writerows(rows)


def file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def manifest_for(root: Path, excluded: set[str]) -> list[dict[str, Any]]:
    return [{"path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size,
             "sha256": file_sha256(path)}
            for path in sorted(p for p in root.rglob("*") if p.is_file())
            if path.relative_to(root).as_posix() not in excluded]


def flat_stats(prefix: str, value: dict[str, Any]) -> dict[str, Any]:
    return {f"{prefix}_{name}": value[name] for name in ("min", "median", "max")}


def turn_ledger(summaries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for item in summaries:
        row = {
            "turn": item["turn"],
            "ra_lower_hit_count": item["firm_rate_regions"]["lower"],
            "ra_upper_hit_count": item["firm_rate_regions"]["upper"],
            "wjt_lower_hit_count": item["wage_regions"]["lower"],
            "wjt_upper_hit_count": item["wage_regions"]["upper"],
            "ra_lower_hit_provinces": "|".join(item["ra_lower_hit_provinces"]),
            "ra_upper_hit_provinces": "|".join(item["ra_upper_hit_provinces"]),
            "wjt_lower_hit_provinces": "|".join(item["wage_lower_hit_provinces"]),
            "wjt_upper_hit_provinces": "|".join(item["wage_upper_hit_provinces"]),
            "household_convergence_count": 31 - item["hjb_failures"],
            "max_abs_kn_gap": item["nk_gap"]["max"],
            "max_abs_y_y_prev_gap": item["yt_gap"]["max"],
            "max_abs_y_y0_gap": item["gdp_level_gap"]["max"],
            "source_converged": item["source_converged"],
            "zt_adjusted_count": item["controller"]["zt_adjusted_count"],
            "kfe_diagnostic_only_count": item["kfe_diagnostic_status_counts"].get("DIAGNOSTIC_ONLY", 0),
            "kfe_upper_b_leak_cells": item["kfe_upper_b_leak_cells"],
            "hjb_negative_offdiagonals": item["hjb_negative_offdiagonals"],
        }
        actions = item["controller"]["govinv_action_counts"]
        row.update({
            "govinv_decrease_count": actions.get("LOW_RA_DECREASE_0P9", 0),
            "govinv_increase_count": actions.get("HIGH_RA_INCREASE_1P1", 0),
            "govinv_hold_count": actions.get("NONE", 0),
        })
        for prefix, key in (
            ("raw_ra", "raw_ra0"), ("used_ra", "used_ra"),
            ("raw_wjt", "raw_wage"), ("used_wjt", "used_wage"),
            ("household_rah", "household_rah"), ("household_w", "household_composite_wage"),
            ("At", "At"), ("Bt", "Bt"), ("Lt", "Lt"), ("Ct", "Ct"),
            ("GovInv", "GovInv"),
        ):
            row.update(flat_stats(prefix, item[key]))
        rows.append(row)
    return rows


def boundary_rows(all_rows: list[list[dict[str, Any]]]) -> list[dict[str, Any]]:
    result = []
    for turn_rows in all_rows:
        for row in turn_rows:
            for family, lower, upper in (
                ("ra", "ra_clipped_lower", "ra_clipped_upper"),
                ("wjt", "wage_clipped_lower", "wage_clipped_upper"),
            ):
                if row[lower]:
                    result.append({"turn": row["turn"], "family": family, "bound": "lower",
                                   "province_index": row["province_index"], "province": row["province"]})
                if row[upper]:
                    result.append({"turn": row["turn"], "family": family, "bound": "upper",
                                   "province_index": row["province_index"], "province": row["province"]})
    return result


def longest_runs(boundaries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str], list[int]] = {}
    for row in boundaries:
        grouped.setdefault((row["family"], row["bound"], row["province"]), []).append(int(row["turn"]))
    result = []
    for (family, bound, province), turns in grouped.items():
        best_start = best_end = current_start = previous = turns[0]
        for turn in turns[1:]:
            if turn != previous + 1:
                if previous - current_start > best_end - best_start:
                    best_start, best_end = current_start, previous
                current_start = turn
            previous = turn
        if previous - current_start > best_end - best_start:
            best_start, best_end = current_start, previous
        result.append({"family": family, "bound": bound, "province": province,
                       "longest_consecutive_turns": best_end - best_start + 1,
                       "run_start": best_start, "run_end": best_end,
                       "total_hit_turns": len(turns)})
    return sorted(result, key=lambda x: (x["family"], -x["longest_consecutive_turns"], x["province"]))


def window_rows(summaries: list[dict[str, Any]], boundaries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result = []
    for family in ("ra", "wage"):
        key = "firm_rate_regions" if family == "ra" else "wage_regions"
        classification = run.classify_boundary_path(summaries, family)
        for start, end in run.WINDOWS:
            subset = [item for item in summaries if start <= item["turn"] <= end]
            if not subset:
                continue
            counts = [item[key]["lower"] + item[key]["upper"] for item in subset]
            ledger_family = "wjt" if family == "wage" else "ra"
            provinces = sorted({row["province"] for row in boundaries
                                if row["family"] == ledger_family and start <= row["turn"] <= end})
            result.append({"family": family, "window": f"{start}-{end}",
                           "turns_observed": len(subset), "first_count": counts[0],
                           "last_count": counts[-1], "min_count": min(counts),
                           "mean_count": float(np.mean(counts)), "max_count": max(counts),
                           "distinct_hit_province_count": len(provinces),
                           "hit_provinces": "|".join(provinces),
                           "overall_classification": classification})
    return result


def validity_rows(all_rows: list[list[dict[str, Any]]]) -> list[dict[str, Any]]:
    result = []
    for rows in all_rows:
        result.append({
            "turn": rows[0]["turn"],
            "hjb_converged_count": sum(row["hjb_converged"] for row in rows),
            "kfe_returned_count": sum(row["kfe_returned"] for row in rows),
            "kfe_valid_count": sum(row["kfe_diagnostic_status"] == "VALID" for row in rows),
            "kfe_diagnostic_only_count": sum(row["kfe_diagnostic_status"] == "DIAGNOSTIC_ONLY" for row in rows),
            "max_kfe_source_free_residual_inf": max(row["kfe_source_free_residual_inf"] for row in rows),
            "max_kfe_source_free_normwise_ratio": max(row["kfe_source_free_normwise_ratio"] for row in rows),
            "upper_b_leak_cells": sum(row["kfe_upper_b_leak_count"] for row in rows),
            "max_upper_b_leak_rate": max(row["kfe_upper_b_max_leak_rate"] for row in rows),
            "hjb_operator_valid_count": sum(row["hjb_operator_status"] == "VALID" for row in rows),
            "hjb_operator_diagnostic_only_count":
                sum(row["hjb_operator_status"] == "DIAGNOSTIC_ONLY" for row in rows),
            "hjb_negative_offdiagonal_count": sum(row["hjb_negative_offdiagonal_count"] for row in rows),
            "minimum_hjb_offdiagonal": min(row["hjb_minimum_offdiagonal"] for row in rows),
        })
    return result


def path_shape(ledger: list[dict[str, Any]]) -> str:
    if ledger[-1]["source_converged"]:
        return "SOURCE_PREDICATE_CONVERGED"
    sequence = np.array([max(row["max_abs_kn_gap"], row["max_abs_y_y_prev_gap"],
                             row["max_abs_y_y0_gap"]) for row in ledger], dtype=float)
    if sequence[-1] > 2.0 * sequence[min(9, len(sequence) - 1)]:
        return "DIVERGENT"
    diffs = np.diff(sequence)
    nonzero = diffs[diffs != 0]
    changes = int(np.count_nonzero(nonzero[1:] * nonzero[:-1] < 0))
    if changes >= 3 and sequence[-1] > 0.5 * sequence[min(9, len(sequence) - 1)]:
        return "OSCILLATORY"
    return "SLOWLY_CONVERGENT" if sequence[-1] < sequence[min(9, len(sequence) - 1)] else "NOT_CONVERGENT"


def finalize() -> None:
    if REPORT.exists() or REPORT_DIR.exists():
        raise FileExistsError("report output already exists")
    terminal = read(EVIDENCE / "terminal_result.json")
    calls = read(EVIDENCE / "call_ledger.json")
    receipt = read(EVIDENCE / "runtime_input_receipt.json")
    if terminal["verdict"] not in EXECUTED:
        raise ValueError("unexpected terminal verdict")
    completed = int(calls["counts"]["turns_completed"])
    if completed < 1:
        raise ValueError("no completed turn to finalize")
    all_rows = [read(EVIDENCE / f"turn_{turn:02d}/per_province_observables.json")
                for turn in range(1, completed + 1)]
    summaries = [read(EVIDENCE / f"turn_{turn:02d}/national_summary.json")
                 for turn in range(1, completed + 1)]
    controllers = [read(EVIDENCE / f"turn_{turn:02d}/controller_observables.json")
                   for turn in range(1, completed + 1)]
    ledger = turn_ledger(summaries)
    boundaries = boundary_rows(all_rows)
    windows = window_rows(summaries, boundaries)
    persistent = longest_runs(boundaries)
    validity = validity_rows(all_rows)
    anhui = [row[11] for row in all_rows]
    anhui_fields = [
        "turn", "province", "firm_ra0", "firm_ra_used", "firm_wage_raw", "firm_wage_used",
        "household_rah", "household_composite_wage", "At", "Bt", "Lt", "Ct", "Kt_supply",
        "GovInv", "govinv_after", "firm_K", "firm_Y", "same_year_Zt", "zt_after",
        "nk_gap", "yt_gap", "gdp_level_gap", "kfe_diagnostic_status", "hjb_operator_status",
    ]
    controller_rows = [{
        "turn": i + 1,
        "source_converged": item["source_converged"],
        "adaptation_gate_open": item["adaptation_allowed"],
        "zt_adjusted_count": sum(action["zt_adjusted"] for action in item["actions"]),
        "govinv_decrease_count": sum(action["govinv_action"] == "LOW_RA_DECREASE_0P9"
                                     for action in item["actions"]),
        "govinv_increase_count": sum(action["govinv_action"] == "HIGH_RA_INCREASE_1P1"
                                     for action in item["actions"]),
        "govinv_hold_count": sum(action["govinv_action"] == "NONE" for action in item["actions"]),
        "max_nk_gap": item["max_nk_gap"], "max_yt_gap": item["max_yt_gap"],
    } for i, item in enumerate(controllers)]

    REPORT_DIR.mkdir(parents=True, exist_ok=False)
    outputs = {
        "turn_ledger.csv": ledger,
        "boundary_hit_province_ledger.csv": boundaries,
        "window_decay_summary.csv": windows,
        "anhui_trace.csv": [{name: row[name] for name in anhui_fields} for row in anhui],
        "controller_action_summary.csv": controller_rows,
        "scientific_validity_ledger.csv": validity,
        "persistent_boundary_offenders.csv": persistent,
    }
    for name, rows in outputs.items():
        write_csv(REPORT_DIR / name, rows)
    for name in ("call_ledger.json", "terminal_result.json", "runtime_input_receipt.json",
                 "predecessor_reproduction.json", "engineering_preflight.json",
                 "pre_science_tests.xml", "post_science_tests.xml", "static_checks.log"):
        source = EVIDENCE / name
        if source.exists():
            shutil.copyfile(source, REPORT_DIR / (name.removesuffix(".log") + ".txt"
                                                   if name.endswith(".log") else name))

    selected = [turn for turn in (1, 2, 3, 5, 10, 25, 50, 75, 100) if turn <= completed]
    selected_table = "\n".join(
        f"| {turn} | {anhui[turn-1]['firm_ra0']:.17g} | {anhui[turn-1]['firm_ra_used']:.17g} | "
        f"{anhui[turn-1]['firm_wage_raw']:.17g} | {anhui[turn-1]['firm_wage_used']:.17g} | "
        f"{anhui[turn-1]['household_rah']:.17g} | {anhui[turn-1]['A_plus_B']:.17g} | "
        f"{anhui[turn-1]['GovInv']:.17g} | {anhui[turn-1]['same_year_Zt']:.17g} | "
        f"{anhui[turn-1]['nk_gap']:.17g} | {anhui[turn-1]['gdp_level_gap']:.17g} | "
        f"{anhui[turn-1]['kfe_diagnostic_status']} | {anhui[turn-1]['hjb_operator_status']} |"
        for turn in selected)
    ra_class = terminal["boundary_classification"]["ra"]
    wage_class = terminal["boundary_classification"]["wage"]
    rate_persistent = [x for x in persistent if x["family"] == "ra"][:10]
    wage_persistent = [x for x in persistent if x["family"] == "wjt"][:10]
    t2 = anhui[1] if completed >= 2 else None
    t3 = anhui[2] if completed >= 3 else None
    collapse_ratio = (t3["A_plus_B"] / t2["A_plus_B"]) if t2 and t3 and t2["A_plus_B"] else None
    collapse = collapse_ratio is not None and collapse_ratio < 0.2
    active = [i for i, row in enumerate(controller_rows[:-1])
              if row["zt_adjusted_count"] or row["govinv_decrease_count"] or row["govinv_increase_count"]]
    deltas = [(ledger[i + 1]["ra_lower_hit_count"] + ledger[i + 1]["ra_upper_hit_count"]
               + ledger[i + 1]["wjt_lower_hit_count"] + ledger[i + 1]["wjt_upper_hit_count"])
              - (ledger[i]["ra_lower_hit_count"] + ledger[i]["ra_upper_hit_count"]
                 + ledger[i]["wjt_lower_hit_count"] + ledger[i]["wjt_upper_hit_count"])
              for i in active]
    controller_direction = (
        "TOWARD_ADMISSIBLE_REGION" if deltas and sum(delta < 0 for delta in deltas) > len(deltas) / 2 else
        "AWAY_FROM_ADMISSIBLE_REGION" if deltas and sum(delta > 0 for delta in deltas) > len(deltas) / 2 else
        "NO_MATERIAL_DIRECTIONAL_BOUNDARY_IMPROVEMENT_ESTABLISHED"
    )
    report = f"""# Chapter 5 corrected-2018 source-faithful 100-turn boundary trajectory diagnostic

## Verdict

`{terminal['verdict']}`

Exactly one trajectory was launched. It completed {completed} outer turns and
{calls['counts']['province_updates_completed']} province updates, stopping because
`{terminal['stop_reason']}`. No second trajectory or scientific retry was used.

## Direct answers

1. Firm-rate boundary path: `{ra_class}`; turn 50/100 evidence is recorded in the ledger when reached.
2. Wage-boundary path: `{wage_class}`. This is path behavior only; absolute wage normalization remains unresolved.
3. Longest firm-rate offenders: `{rate_persistent}`. Longest wage offenders: `{wage_persistent}`.
4. Existing GovInv/Zt actions are classified `{controller_direction}` by the mean next-turn change in total boundary hits after active-controller turns; this is temporal association, not causal redesign evidence.
5. Recorded KN/Y/GDP gap path: `{path_shape(ledger)}`.
6. Anhui turn2-to-turn3 A+B ratio: `{collapse_ratio}`; collapse under the frozen <0.2 descriptive rule: `{collapse}`.
7. The Anhui table below preserves the timing of entering rah/w/GovInv/Zt and same-turn firm ra/wage; no parameter was changed to improve the path.
8. KFE diagnostic-only counts, source-free residuals, upper-b leakage, and HJB-loop negative offdiagonals remain separately recorded in `scientific_validity_ledger.csv`. Any surviving blocker prevents economic acceptance even if outer boundary counts improve.

## Selected Anhui trace

| turn | raw ra | used ra | raw wage | used wage | entering rah | A+B | GovInv | Zt | KN gap | GDP gap | KFE | HJB operator |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
{selected_table}

## Calls and protected boundary

Scientific processes/trajectories: {calls['counts']['scientific_processes']}/{calls['counts']['trajectory_attempts']}.
HJB/KFE direct solves: {calls['counts']['hjb_direct_solves']}/{calls['counts']['kfe_direct_solves']}.
Labor roots/Brent calls: {calls['counts']['labor_roots_attempted']}/{calls['counts']['brentq_calls_attempted']}.
Scientific retries: {calls['counts']['scientific_retries']}. MATLAB/GE/annual/IRF/Results calls:
{calls['matlab_calls']}/{calls['ge_calls']}/{calls['annual_model_calls']}/{calls['irf_calls']}/{calls['results_calls']}.

This diagnostic does not establish production steady state, KFE/HJB admissibility,
GE/annual validity, or Results readiness. Turn 101+ authorized: **NO**. Results eligibility: **FALSE**.
"""
    REPORT.write_text(report, encoding="utf-8", newline="\n")

    repo_records = manifest_for(REPORT_DIR, {"manifest.json", "manifest_readback.json"})
    write_json(REPORT_DIR / "manifest.json", {"files": repo_records})
    write_json(REPORT_DIR / "manifest_readback.json", {
        "checked_files": len(repo_records),
        "passed": all((REPORT_DIR / row["path"]).stat().st_size == row["bytes"]
                      and file_sha256(REPORT_DIR / row["path"]) == row["sha256"]
                      for row in repo_records),
    })
    external_records = manifest_for(EVIDENCE, {"manifest.json", "manifest_readback.json"})
    write_json(EVIDENCE / "manifest.json", {"files": external_records})
    write_json(EVIDENCE / "manifest_readback.json", {
        "checked_files": len(external_records),
        "passed": all((EVIDENCE / row["path"]).stat().st_size == row["bytes"]
                      and file_sha256(EVIDENCE / row["path"]) == row["sha256"]
                      for row in external_records),
    })


if __name__ == "__main__":
    finalize()
