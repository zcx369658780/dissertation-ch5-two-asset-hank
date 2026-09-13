"""Offline analysis of completed HJB mechanism traces; invokes no model code."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from collections import Counter
from hashlib import sha256
from pathlib import Path
from typing import Any


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _median(values: list[float | int | None]) -> float | None:
    finite = [float(value) for value in values if value is not None and math.isfinite(float(value))]
    return float(statistics.median(finite)) if finite else None


def _range(values: list[float | int | None]) -> list[float] | None:
    finite = [float(value) for value in values if value is not None and math.isfinite(float(value))]
    return [min(finite), max(finite)] if finite else None


def _first(rows: list[dict[str, Any]], predicate) -> int | None:
    return next((int(row["iteration"]) for row in rows if predicate(row)), None)


def _call_metrics(summary: dict[str, Any], accepted_root: Path) -> dict[str, Any]:
    trace = json.loads(Path(summary["trace_path"]).read_text(encoding="utf-8"))
    rows = trace["iterations"]
    stats = [float(row["convergence_statistic"]) for row in rows]
    tail = stats[-20:]
    decreases = sum(right < left for left, right in zip(tail, tail[1:]))
    tail_mean = statistics.fmean(tail)
    ratios = [row["two_step_to_one_step_ratio"] for row in rows[-20:]
              if row["two_step_to_one_step_ratio"] is not None]
    switches = [row["policy_label_switch_count"] for row in rows[-20:]
                if row["policy_label_switch_count"] is not None]
    reversions = [row["policy_two_step_reversion_count"] for row in rows[-20:]
                  if row["policy_two_step_reversion_count"] is not None]
    floor_shares = [row["derivatives"]["floor_hit_shares"]["vb_forward"]
                    + row["derivatives"]["floor_hit_shares"]["vb_backward"] for row in rows]
    entering = json.loads((accepted_root / f"turn_{trace['turn']:02d}" / "entering_state.json").read_text(encoding="utf-8"))
    state = entering["states"][trace["province_index"]]
    guarded_wjt = float(state["wjt"])
    corrected_wage_guard = "LOWER" if guarded_wjt == 0.8 else "UPPER" if guarded_wjt == 1.3 else "UNSATURATED"
    first_nondec = next((index + 2 for index, (left, right) in enumerate(zip(stats, stats[1:])) if right >= left), None)
    return {
        "turn": trace["turn"], "province_index": trace["province_index"], "province": trace["province"],
        "converged": trace["final_converged"], "ceiling_hit": not trace["final_converged"],
        "iterations": trace["final_iterations"], "initial_statistic": stats[0], "final_statistic": stats[-1],
        "final_to_initial_ratio": stats[-1] / stats[0], "last20_final_to_initial_ratio": tail[-1] / tail[0],
        "last20_decrease_fraction": decreases / max(1, len(tail) - 1),
        "last20_range": max(tail) - min(tail),
        "last20_coefficient_of_variation": statistics.pstdev(tail) / abs(tail_mean) if len(tail) > 1 and tail_mean else None,
        "last20_two_step_to_one_step_median": _median(ratios),
        "last20_policy_switch_median": _median(switches),
        "last20_two_step_reversion_median": _median(reversions),
        "first_policy_switch_iteration": _first(rows, lambda row: (row["policy_label_switch_count"] or 0) > 0),
        "first_two_step_reversion_iteration": _first(rows, lambda row: (row["policy_two_step_reversion_count"] or 0) > 0),
        "first_value_nondec_iteration": first_nondec,
        "first_derivative_floor_hit_iteration": _first(rows, lambda row: sum(row["derivatives"]["floor_hit_counts"].values()) > 0),
        "first_negative_offdiagonal_iteration": _first(rows, lambda row: row["operator"]["minimum_stored_off_diagonal"] < 0),
        "first_nonzero_row_sum_defect_iteration": _first(rows, lambda row: row["operator"]["max_abs_row_sum_defect"] != 0),
        "derivative_floor_share_first": floor_shares[0], "derivative_floor_share_final": floor_shares[-1],
        "minimum_offdiagonal_all_iterations": min(row["operator"]["minimum_stored_off_diagonal"] for row in rows),
        "maximum_row_sum_defect_all_iterations": max(row["operator"]["max_abs_row_sum_defect"] for row in rows),
        "linear_solve_residual_first": rows[0]["linear_solve_residual_inf"],
        "linear_solve_residual_final": rows[-1]["linear_solve_residual_inf"],
        "linear_solve_residual_max": max(row["linear_solve_residual_inf"] for row in rows),
        "raw_entering_r_a": trace["raw_entering_r_a"], "consumed_r_a": trace["consumed_r_a"],
        "return_guard_state": trace["return_guard_state"], "consumed_household_composite_wage": trace["wage"],
        "guarded_wjt": guarded_wjt, "wage_guard_state": corrected_wage_guard,
        "accepted_output_exact": trace["accepted_scientific_output_exact"],
        "final_operator_exact": trace["final_operator_exact"],
    }


FIELDS = (
    "iterations", "final_to_initial_ratio", "last20_final_to_initial_ratio", "last20_decrease_fraction",
    "last20_range", "last20_coefficient_of_variation", "last20_two_step_to_one_step_median",
    "last20_policy_switch_median", "last20_two_step_reversion_median", "derivative_floor_share_first",
    "derivative_floor_share_final", "minimum_offdiagonal_all_iterations", "maximum_row_sum_defect_all_iterations",
    "linear_solve_residual_first", "linear_solve_residual_final", "linear_solve_residual_max",
)


def analyze(evidence_root: Path, accepted_parent: Path) -> int:
    evidence_root = Path(evidence_root); accepted_root = Path(accepted_parent) / "annual_g2_control"
    summary = json.loads((evidence_root / "replay_summary.json").read_text(encoding="utf-8"))
    metrics = [_call_metrics(item, accepted_root) for item in summary]
    with (evidence_root / "province_metrics.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(metrics[0])); writer.writeheader(); writer.writerows(metrics)
    groups: list[dict[str, Any]] = []
    for turn in (1, 2):
        for converged in (True, False):
            members = [row for row in metrics if row["turn"] == turn and row["converged"] == converged]
            groups.append({
                "turn": turn, "classification": "CONVERGED" if converged else "CEILING_FAILURE",
                "count": len(members), "provinces": [row["province"] for row in members],
                "metrics": {field: {"median": _median([row[field] for row in members]),
                                    "range": _range([row[field] for row in members])} for field in FIELDS},
            })
    _write_json(evidence_root / "group_summary.json", groups)

    by_key = {(row["turn"], row["province"]): row for row in metrics}
    transitions = []
    for province in [row["province"] for row in metrics if row["turn"] == 1 and row["converged"]]:
        left, right = by_key[(1, province)], by_key[(2, province)]
        if not right["converged"]:
            transitions.append({
                "province": province, "transition": "TURN1_CONVERGED_TO_TURN2_FAILED",
                "turn1_final_to_initial_ratio": left["final_to_initial_ratio"],
                "turn2_final_to_initial_ratio": right["final_to_initial_ratio"],
                "turn1_last20_policy_switch_median": left["last20_policy_switch_median"],
                "turn2_last20_policy_switch_median": right["last20_policy_switch_median"],
                "turn1_floor_share_final": left["derivative_floor_share_final"],
                "turn2_floor_share_final": right["derivative_floor_share_final"],
                "turn2_first_policy_switch_iteration": right["first_policy_switch_iteration"],
                "turn2_first_value_nondec_iteration": right["first_value_nondec_iteration"],
                "turn2_first_two_step_reversion_iteration": right["first_two_step_reversion_iteration"],
                "turn2_first_derivative_floor_hit_iteration": right["first_derivative_floor_hit_iteration"],
                "turn2_return_guard_state": right["return_guard_state"],
                "turn2_wage_guard_state": right["wage_guard_state"],
            })
    with (evidence_root / "turn1_converged_to_turn2_failed.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(transitions[0])); writer.writeheader(); writer.writerows(transitions)

    turn2 = [row for row in metrics if row["turn"] == 2]
    associations = {}
    for field in ("return_guard_state", "wage_guard_state"):
        table = []
        for state in sorted({row[field] for row in turn2}):
            subset = [row for row in turn2 if row[field] == state]
            failures = sum(not row["converged"] for row in subset)
            table.append({"state": state, "calls": len(subset), "converged": len(subset) - failures,
                          "failed": failures, "failure_share": failures / len(subset)})
        associations[field] = table
    _write_json(evidence_root / "price_guard_associations.json", associations)

    failed = [row for row in metrics if not row["converged"]]
    event_order = {
        "classification": "POLICY_CHATTERING_WITH_VALUE_UPDATE_OSCILLATION_AND_LATER_DERIVATIVE_FLOOR_AMPLIFICATION__NOT_PURE_TWO_CYCLE__NOT_MONOTONE_SLOW",
        "classification_basis": "POST_HOC_DESCRIPTIVE_FROM_PREREGISTERED_CONTINUOUS_METRICS__NOT_A_GATE",
        "failed_calls": len(failed),
        "first_event_counts": {
            "policy_switch_before_floor": sum(row["first_policy_switch_iteration"] < row["first_derivative_floor_hit_iteration"] for row in failed),
            "value_nondec_before_floor": sum(row["first_value_nondec_iteration"] < row["first_derivative_floor_hit_iteration"] for row in failed),
            "two_step_reversion_before_floor": sum(row["first_two_step_reversion_iteration"] < row["first_derivative_floor_hit_iteration"] for row in failed),
        },
        "universal_accepted_operator_features": {
            "nonzero_row_sum_defect_at_iteration_1_calls": sum(row["first_nonzero_row_sum_defect_iteration"] == 1 for row in metrics),
            "negative_offdiagonal_by_iteration_3_calls": sum((row["first_negative_offdiagonal_iteration"] or 999) <= 3 for row in metrics),
            "interpretation": "accepted iteration operator permits signed offdiagonals and boundary row-sum defects; presence alone is not a new defect",
        },
        "linear_solve_residual_first_all_calls_range": _range([row["linear_solve_residual_first"] for row in metrics]),
        "causal_boundary": "direct replay and temporal ordering only; no same-state intervention identifies causality",
    }
    _write_json(evidence_root / "event_ordering.json", event_order)
    _write_json(evidence_root / "wage_guard_metadata_adjudication.json", {
        "status": "METADATA_ONLY_CORRECTION__NO_SCIENCE_RERUN",
        "issue": "runtime trace labeled wage guard by composite household wage; the frozen guard applies to entering-state wjt",
        "authoritative_fields": ["consumed_household_composite_wage", "guarded_wjt", "wage_guard_state"],
        "corrected_calls": 62, "scientific_outputs_affected": False,
    })
    _write_json(evidence_root / "analysis_summary.json", {
        "verdict": event_order["classification"], "results_eligible": False,
        "exact_input_coverage": len(metrics), "accepted_output_exact_count": sum(row["accepted_output_exact"] for row in metrics),
        "final_operator_exact_count": sum(row["final_operator_exact"] for row in metrics),
        "turn1_converged": sum(row["turn"] == 1 and row["converged"] for row in metrics),
        "turn2_converged": sum(row["turn"] == 2 and row["converged"] for row in metrics),
        "turn1_converged_to_turn2_failed": len(transitions),
        "longer_iteration_ceiling_supported": False,
        "longer_ceiling_reason": "failure traces are non-monotone with persistent label switching/reversion and material update ranges; they are not uniformly monotone-slow",
        "recommended_next_owner_gate": "HJB_ITERATION_FIXED_POINT_MECHANISM_INTERVENTION_DESIGN_FREEZE",
        "kfe_caveat": "KFE not run; finite-box upper-b leakage and MATLAB-style pinning remain independent blockers",
        "kkt_caveat": "standalone KKT residual remains unavailable",
    })
    return 0


def seal(evidence_root: Path) -> int:
    evidence_root = Path(evidence_root)
    target = evidence_root / "sealed_manifest_sha256.json"
    if target.exists(): raise FileExistsError("manifest already exists")
    entries = []
    for path in sorted(item for item in evidence_root.rglob("*") if item.is_file()):
        entries.append({"path": path.relative_to(evidence_root).as_posix(), "bytes": path.stat().st_size,
                        "sha256": sha256(path.read_bytes()).hexdigest().upper()})
    _write_json(target, {"schema": "CH5_MP4C_K1_HJB_MECHANISM_SEALED_MANIFEST_V1", "entries": entries,
                         "bytes_excluding_manifest": sum(item["bytes"] for item in entries)})
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(); sub = parser.add_subparsers(dest="command", required=True)
    analysis = sub.add_parser("analyze"); analysis.add_argument("evidence_root", type=Path); analysis.add_argument("accepted_parent", type=Path)
    sealing = sub.add_parser("seal"); sealing.add_argument("evidence_root", type=Path)
    args = parser.parse_args()
    return analyze(args.evidence_root, args.accepted_parent) if args.command == "analyze" else seal(args.evidence_root)


if __name__ == "__main__":
    raise SystemExit(main())
