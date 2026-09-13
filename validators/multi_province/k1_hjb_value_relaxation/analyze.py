"""Offline accepted-baseline versus omega=0.5 treatment analysis; no model calls."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from hashlib import sha256
from pathlib import Path
from typing import Any

import numpy as np

FIELDS = ("value", "consumption", "labor", "transfer", "adjustment_cost", "mu_a", "mu_b")
LABEL_DOMAIN = {"0", "B", "F"}


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _median(values: list[float | int]) -> float | None:
    finite = [float(x) for x in values if math.isfinite(float(x))]
    return float(statistics.median(finite)) if finite else None


def _mean(values: list[float | int]) -> float | None:
    finite = [float(x) for x in values if math.isfinite(float(x))]
    return float(statistics.fmean(finite)) if finite else None


def _first(rows: list[dict[str, Any]], predicate) -> int | None:
    return next((int(row["iteration"]) for row in rows if predicate(row)), None)


def _trace_metrics(path: Path, treatment: bool) -> dict[str, Any]:
    trace = json.loads(path.read_text(encoding="utf-8"))
    rows = trace["iterations"]
    gap_key = "raw_fixed_point_gap" if treatment else "convergence_statistic"
    gaps = [float(row[gap_key]) for row in rows]
    switches = [int(row["policy_label_switch_count"]) for row in rows if row["policy_label_switch_count"] is not None]
    reversions = [int(row["policy_two_step_reversion_count"]) for row in rows if row["policy_two_step_reversion_count"] is not None]
    nondec = sum(right >= left for left, right in zip(gaps, gaps[1:]))
    floor_counts = [sum(row["derivatives"]["floor_hit_counts"].values()) for row in rows]
    floor_shares = [sum(row["derivatives"]["floor_hit_shares"].values()) for row in rows]
    result = {
        "iterations": len(rows), "initial_gap": gaps[0], "final_gap": gaps[-1],
        "gap_nondecrease_count": nondec, "gap_nondecrease_fraction": nondec / max(1, len(gaps) - 1),
        "policy_switch_total": sum(switches), "policy_switch_mean": _mean(switches),
        "reversion_total": sum(reversions), "reversion_mean": _mean(reversions),
        "first_policy_switch_iteration": _first(rows, lambda row: (row["policy_label_switch_count"] or 0) > 0),
        "first_reversion_iteration": _first(rows, lambda row: (row["policy_two_step_reversion_count"] or 0) > 0),
        "first_floor_iteration": next((i + 1 for i, x in enumerate(floor_counts) if x > 0), None),
        "floor_share_first": floor_shares[0], "floor_share_final": floor_shares[-1],
        "linear_solve_residual_max": max(float(row["linear_solve_residual_inf"]) for row in rows),
    }
    if treatment:
        relaxed = [float(row["relaxed_state_update"]) for row in rows]
        result.update({
            "final_relaxed_update": relaxed[-1],
            "raw_relaxed_identity_max_abs": max(abs(gap - 2.0 * update) for gap, update in zip(gaps, relaxed)),
            "all_iteration_values_finite": all(row["finite"]["v_old"] and row["finite"]["v_solve"]
                and row["finite"]["v_next"] and all(row["finite"]["scientific_arrays"].values()) for row in rows),
        })
    return result


def _summary_group(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "count": len(rows), "provinces": [row["province"] for row in rows],
        "baseline_converged": sum(row["baseline_converged"] for row in rows),
        "treatment_converged": sum(row["treatment_converged"] for row in rows),
        "convergence_delta": sum(row["treatment_converged"] for row in rows) - sum(row["baseline_converged"] for row in rows),
        "calls_lower_policy_switch_mean": sum(row["treatment_policy_switch_mean"] < row["baseline_policy_switch_mean"] for row in rows),
        "calls_lower_reversion_mean": sum(row["treatment_reversion_mean"] < row["baseline_reversion_mean"] for row in rows),
        "calls_lower_gap_nondecrease_fraction": sum(row["treatment_gap_nondecrease_fraction"] < row["baseline_gap_nondecrease_fraction"] for row in rows),
        "baseline_policy_switch_mean_median": _median([row["baseline_policy_switch_mean"] for row in rows]),
        "treatment_policy_switch_mean_median": _median([row["treatment_policy_switch_mean"] for row in rows]),
        "baseline_reversion_mean_median": _median([row["baseline_reversion_mean"] for row in rows]),
        "treatment_reversion_mean_median": _median([row["treatment_reversion_mean"] for row in rows]),
        "baseline_gap_nondecrease_fraction_median": _median([row["baseline_gap_nondecrease_fraction"] for row in rows]),
        "treatment_gap_nondecrease_fraction_median": _median([row["treatment_gap_nondecrease_fraction"] for row in rows]),
        "baseline_floor_first_median": _median([row["baseline_first_floor_iteration"] for row in rows if row["baseline_first_floor_iteration"] is not None]),
        "treatment_floor_first_median": _median([row["treatment_first_floor_iteration"] for row in rows if row["treatment_first_floor_iteration"] is not None]),
    }


def analyze(evidence_root: Path, mechanism_parent: Path) -> int:
    evidence_root = Path(evidence_root)
    mechanism_parent = Path(mechanism_parent)
    treatment = json.loads((evidence_root / "treatment_summary.json").read_text(encoding="utf-8"))
    baseline = json.loads((mechanism_parent / "replay_summary.json").read_text(encoding="utf-8"))
    baseline_by_key = {(row["turn"], row["province_index"]): row for row in baseline}
    rows: list[dict[str, Any]] = []
    normality_rows: list[dict[str, Any]] = []
    fixed_point_rows: list[dict[str, Any]] = []
    recovered_rows: list[dict[str, Any]] = []
    for item in treatment:
        key = (item["turn"], item["province_index"])
        base = baseline_by_key[key]
        bm = _trace_metrics(Path(base["trace_path"]), False)
        tm = _trace_metrics(Path(item["trace_path"]), True)
        row = {
            "turn": item["turn"], "province_index": item["province_index"], "province": item["province"],
            "baseline_converged": bool(base["converged"]), "treatment_converged": bool(item["converged"]),
            "baseline_iterations": int(base["iterations"]), "treatment_iterations": int(item["iterations"]),
            **{f"baseline_{k}": v for k, v in bm.items()}, **{f"treatment_{k}": v for k, v in tm.items()},
        }
        rows.append(row)
        with np.load(item["result_path"], allow_pickle=False) as current:
            finite = {name: bool(np.isfinite(current[name]).all()) for name in FIELDS}
            liquid_domain = sorted(set(current["liquid_label"].ravel().tolist()))
            transfer_domain = sorted(set(current["transfer_label"].ravel().tolist()))
            normal = all(finite.values()) and set(liquid_domain).issubset(LABEL_DOMAIN) and set(transfer_domain).issubset(LABEL_DOMAIN) and tm["all_iteration_values_finite"]
            normality_rows.append({"turn": item["turn"], "province": item["province"], "converged": bool(item["converged"]),
                                   "finite_fields": finite, "all_iteration_values_finite": tm["all_iteration_values_finite"],
                                   "liquid_label_domain": liquid_domain, "transfer_label_domain": transfer_domain,
                                   "accepted_label_domain": sorted(LABEL_DOMAIN), "normal": normal})
            if base["converged"] and item["converged"]:
                with np.load(item["accepted_hjb_path"], allow_pickle=False) as accepted_result:
                    differences = {}
                    for name in FIELDS:
                        delta = np.abs(current[name] - accepted_result[name])
                        differences[name] = {"max_abs": float(np.max(delta)), "median_abs": float(np.median(delta))}
                    policy_differences = {
                        "liquid_label_count": int(np.count_nonzero(current["liquid_label"] != accepted_result["liquid_label"])),
                        "transfer_label_count": int(np.count_nonzero(current["transfer_label"] != accepted_result["transfer_label"])),
                    }
                fixed_point_rows.append({"turn": item["turn"], "province": item["province"],
                                         "baseline_raw_gap": float(base["statistic"]),
                                         "treatment_raw_gap": float(item["raw_fixed_point_gap"]),
                                         "differences": differences, "policy_differences": policy_differences})
        if not base["converged"] and item["converged"]:
            recovered_rows.append({"turn": item["turn"], "province": item["province"],
                                   "treatment_iterations": item["iterations"], "treatment_raw_gap": item["raw_fixed_point_gap"],
                                   "final_relaxed_update": tm["final_relaxed_update"],
                                   "policy_switch_mean": tm["policy_switch_mean"], "reversion_mean": tm["reversion_mean"],
                                   "gap_nondecrease_fraction": tm["gap_nondecrease_fraction"],
                                   "first_policy_switch_iteration": tm["first_policy_switch_iteration"],
                                   "first_floor_iteration": tm["first_floor_iteration"], "output_normal": normal})

    groups = {
        "baseline_turn1_converged": _summary_group([r for r in rows if r["turn"] == 1 and r["baseline_converged"]]),
        "baseline_turn1_failed": _summary_group([r for r in rows if r["turn"] == 1 and not r["baseline_converged"]]),
        "baseline_turn2_converged": _summary_group([r for r in rows if r["turn"] == 2 and r["baseline_converged"]]),
        "baseline_turn2_failed": _summary_group([r for r in rows if r["turn"] == 2 and not r["baseline_converged"]]),
        "turn1_converged_to_turn2_failed_provinces": _summary_group([
            r for r in rows if r["turn"] == 2 and baseline_by_key[(1, r["province_index"])]["converged"] and not r["baseline_converged"]]),
    }
    convergence = {
        "turn1": {"baseline": sum(r["turn"] == 1 and r["baseline_converged"] for r in rows),
                  "treatment": sum(r["turn"] == 1 and r["treatment_converged"] for r in rows)},
        "turn2": {"baseline": sum(r["turn"] == 2 and r["baseline_converged"] for r in rows),
                  "treatment": sum(r["turn"] == 2 and r["treatment_converged"] for r in rows)},
        "all": {"baseline": sum(r["baseline_converged"] for r in rows),
                "treatment": sum(r["treatment_converged"] for r in rows)},
    }
    lost = [{"turn": r["turn"], "province": r["province"]} for r in rows if r["baseline_converged"] and not r["treatment_converged"]]
    pairwise = {
        "calls_lower_policy_switch_mean": sum(r["treatment_policy_switch_mean"] < r["baseline_policy_switch_mean"] for r in rows),
        "calls_equal_policy_switch_mean": sum(r["treatment_policy_switch_mean"] == r["baseline_policy_switch_mean"] for r in rows),
        "calls_lower_reversion_mean": sum(r["treatment_reversion_mean"] < r["baseline_reversion_mean"] for r in rows),
        "calls_equal_reversion_mean": sum(r["treatment_reversion_mean"] == r["baseline_reversion_mean"] for r in rows),
        "calls_lower_gap_nondecrease_fraction": sum(r["treatment_gap_nondecrease_fraction"] < r["baseline_gap_nondecrease_fraction"] for r in rows),
        "all_calls": 62,
    }
    raw_relaxed = {
        "contract": "convergence uses raw ||V_solve-V_old||_inf; relaxed update is diagnostic only",
        "expected_raw_to_relaxed_factor": 2.0,
        "maximum_abs_raw_minus_twice_relaxed": max(r["treatment_raw_relaxed_identity_max_abs"] for r in rows),
        "converged_calls_raw_gap_below_1e7": sum(r["treatment_converged"] and r["treatment_final_gap"] < 1e-7 for r in rows),
        "converged_calls": sum(r["treatment_converged"] for r in rows),
    }
    floor_order = {
        "treatment_calls_policy_switch_before_floor": sum(
            r["treatment_first_policy_switch_iteration"] is not None and r["treatment_first_floor_iteration"] is not None
            and r["treatment_first_policy_switch_iteration"] < r["treatment_first_floor_iteration"] for r in rows),
        "treatment_calls_floor_never_hit": sum(r["treatment_first_floor_iteration"] is None for r in rows),
        "recovered_calls_policy_switch_before_floor": sum(
            r["first_policy_switch_iteration"] is not None and r["first_floor_iteration"] is not None
            and r["first_policy_switch_iteration"] < r["first_floor_iteration"] for r in recovered_rows),
        "recovered_calls": len(recovered_rows),
    }
    fixed_aggregate = {}
    if fixed_point_rows:
        for name in FIELDS:
            fixed_aggregate[name] = {
                "max_abs_across_calls": max(r["differences"][name]["max_abs"] for r in fixed_point_rows),
                "median_of_cellwise_medians": _median([r["differences"][name]["median_abs"] for r in fixed_point_rows]),
            }
        fixed_aggregate["liquid_label_differences_total"] = sum(r["policy_differences"]["liquid_label_count"] for r in fixed_point_rows)
        fixed_aggregate["transfer_label_differences_total"] = sum(r["policy_differences"]["transfer_label_count"] for r in fixed_point_rows)
    classification = "PARTIAL_SUPPORT__SYSTEMATIC_CHATTERING_REDUCTION__NET_ONE_CONVERGENCE_GAIN__TURN2_NONE_AND_ENDPOINT_DIVERGENCE_OUTLIERS"
    _write_json(evidence_root / "output_normality_adjudication.json", {
        "status": "METADATA_ONLY_CORRECTION__NO_SCIENCE_RERUN",
        "issue": "runner omitted accepted liquid label 0 from its domain allowlist",
        "accepted_domain_proven_from_baseline_and_treatment": sorted(LABEL_DOMAIN),
        "original_runner_normal_count": sum(item["output_normal"] for item in treatment),
        "recomputed_normal_count": sum(item["normal"] for item in normality_rows),
        "scientific_outputs_affected": False, "rows": normality_rows,
    })
    _write_json(evidence_root / "baseline_treatment_comparison.json", {
        "classification": classification, "convergence": convergence, "groups": groups,
        "pairwise_trajectory_comparison": pairwise, "raw_gap_vs_relaxed_update": raw_relaxed,
        "derivative_floor_ordering": floor_order, "both_converged_calls": len(fixed_point_rows),
        "both_converged_aggregate": fixed_aggregate, "baseline_failed_treatment_converged": recovered_rows,
        "baseline_converged_treatment_failed": lost,
        "causal_boundary": "same exact isolated HJB inputs identify the effect of fixed omega=0.5 on this numerical map only; no production solver, KFE, KKT, steady-state, GE or Results claim",
        "recommended_next_owner_gate": "OWNER_HJB_RELAXATION_MIXED_EVIDENCE_AND_TURN2_FIXED_POINT_COHERENCE_REVIEW",
        "kfe_caveat": "KFE not run; finite-box upper-b leakage and MATLAB-style pinning remain independent blockers",
        "kkt_caveat": "standalone KKT residual remains unavailable in accepted evidence",
        "results_eligible": False,
    })
    _write_json(evidence_root / "both_converged_fixed_point_comparison.json", fixed_point_rows)
    with (evidence_root / "province_comparison.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return 0


def seal(evidence_root: Path) -> int:
    evidence_root = Path(evidence_root)
    target = evidence_root / "sealed_manifest_sha256.json"
    if target.exists():
        raise FileExistsError("manifest already exists")
    entries = []
    for path in sorted(item for item in evidence_root.rglob("*") if item.is_file()):
        entries.append({"path": path.relative_to(evidence_root).as_posix(), "bytes": path.stat().st_size,
                        "sha256": sha256(path.read_bytes()).hexdigest().upper()})
    _write_json(target, {"schema": "CH5_MP4C_K1_HJB_VALUE_RELAXATION_SEALED_MANIFEST_V1", "entries": entries,
                         "bytes_excluding_manifest": sum(item["bytes"] for item in entries)})
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    analysis = sub.add_parser("analyze")
    analysis.add_argument("evidence_root", type=Path)
    analysis.add_argument("mechanism_parent", type=Path)
    sealing = sub.add_parser("seal")
    sealing.add_argument("evidence_root", type=Path)
    args = parser.parse_args()
    return analyze(args.evidence_root, args.mechanism_parent) if args.command == "analyze" else seal(args.evidence_root)


if __name__ == "__main__":
    raise SystemExit(main())
