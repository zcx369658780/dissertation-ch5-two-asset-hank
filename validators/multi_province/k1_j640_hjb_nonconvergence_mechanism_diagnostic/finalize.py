"""Offline finalization for the J640 HJB mechanism diagnostic."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

from validators.multi_province.k1_j640_hjb_nonconvergence_mechanism_diagnostic import run
from validators.multi_province.k1_standalone_hjb_ra_wage_frontier_narrow_3x3.finalize import (
    seal,
)


def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _first_positive(rows: list[dict[str, Any]], axis: str) -> int | None:
    return next(
        (
            int(row["iteration"])
            for row in rows
            if row["selector_changes"][axis] is not None
            and row["selector_changes"][axis] > 0
        ),
        None,
    )


def _minimum_period(rows: list[dict[str, Any]], key: str) -> dict[str, Any] | None:
    values = [
        (int(row["iteration"]), float(row[key]))
        for row in rows
        if row.get(key) is not None
    ]
    if not values:
        return None
    iteration, value = min(values, key=lambda item: item[1])
    return {"iteration": iteration, "distance_inf": value}


def derive_summary(trace: dict[str, Any], base: dict[str, Any]) -> dict[str, Any]:
    rows = trace["iterations"]
    statistics = [float(row["convergence_statistic"]) for row in rows]
    rebounds = [
        {
            "iteration": int(rows[index]["iteration"]),
            "previous": statistics[index - 1],
            "current": statistics[index],
            "increase": statistics[index] - statistics[index - 1],
        }
        for index in range(1, len(rows))
        if statistics[index] >= statistics[index - 1]
    ]
    events = [
        ["policy_or_selector_switch", base.get("first_policy_or_selector_switch_iteration")],
        ["value_stat_non_decrease", base.get("first_value_stat_non_decrease_iteration")],
        ["derivative_floor_hit", base.get("first_derivative_floor_hit_iteration")],
    ]
    events = sorted((item for item in events if item[1] is not None), key=lambda item: item[1])
    cycle = base["cycle_evidence"]
    result = dict(base)
    result.update(
        {
            "event_ordering": events,
            "first_liquid_selector_change_iteration": _first_positive(rows, "liquid"),
            "first_transfer_selector_change_iteration": _first_positive(rows, "transfer"),
            "selector_switch_iterations": sum(
                ((row["selector_changes"]["liquid"] or 0) + (row["selector_changes"]["transfer"] or 0)) > 0
                for row in rows
            ),
            "liquid_selector_change_total": sum(row["selector_changes"]["liquid"] or 0 for row in rows),
            "transfer_selector_change_total": sum(row["selector_changes"]["transfer"] or 0 for row in rows),
            "largest_value_stat_rebounds": sorted(rebounds, key=lambda item: item["increase"], reverse=True)[:10],
            "minimum_statistic_iteration": (
                int(rows[min(range(len(rows)), key=lambda index: statistics[index])]["iteration"])
                if rows else None
            ),
            "derivative_floor_active_iterations": sum(
                sum(row["derivative_floor_hits"].values()) > 0 for row in rows
            ),
            "maximum_combined_derivative_floor_hits": max(
                (sum(row["derivative_floor_hits"].values()) for row in rows), default=0
            ),
            "minimum_period_2_value_distance": _minimum_period(rows, "value_period_2_inf"),
            "minimum_period_3_value_distance": _minimum_period(rows, "value_period_3_inf"),
            "unique_value_hashes": len({row["hashes"]["value"] for row in rows}),
            "unique_joint_selector_hashes": len(
                {(row["hashes"]["liquid_labels"], row["hashes"]["transfer_labels"]) for row in rows}
            ),
            "exact_low_period_value_cycle": cycle["exact_value_low_period_2_or_3"],
            "exact_low_period_joint_selector_cycle": cycle["exact_joint_label_low_period_2_or_3"],
            "all_iteration_operators_legal": all(row["operator"]["legal"] for row in rows),
            "maximum_A2max": max((row["operator"]["a2max"] for row in rows), default=None),
            "all_finite_checks_pass": all(all(row["finite_checks"].values()) for row in rows),
            "all_shape_checks_pass": all(all(row["shape_checks"].values()) for row in rows),
            "linear_solve_residual_range": (
                [
                    min(row["linear_solve_residual_inf"] for row in rows),
                    max(row["linear_solve_residual_inf"] for row in rows),
                ]
                if rows else None
            ),
            "temporal_interpretation": "selector switching and value-stat non-decrease precede derivative-floor activation",
            "prior_accepted_mechanism_comparison": "same broad ordering as prior accepted failed-call evidence; descriptive only, not a causal identity claim",
            "pure_monotone_slow_supported": False,
            "pure_low_period_cycle_supported": False,
            "derivative_floor_as_initiating_event_supported": False,
        }
    )
    return result


def _csv_row(row: dict[str, Any]) -> dict[str, Any]:
    coordinate = row["argmax"]
    policies = row["policy_changes"]
    return {
        "iteration": row["iteration"],
        "convergence_statistic": row["convergence_statistic"],
        "signed_dV_at_argmax": row["signed_dV_at_argmax"],
        "argmax_b_index": coordinate["index_zero_based"]["b"],
        "argmax_a_index": coordinate["index_zero_based"]["a"],
        "argmax_z_index": coordinate["index_zero_based"]["z"],
        "argmax_b": coordinate["state"]["b"],
        "argmax_a": coordinate["state"]["a"],
        "argmax_z": coordinate["state"]["z"],
        "A2max": row["operator"]["a2max"],
        "operator_legal": row["operator"]["legal"],
        "finite_checks_pass": all(row["finite_checks"].values()),
        "shape_checks_pass": all(row["shape_checks"].values()),
        "liquid_selector_changes": row["selector_changes"]["liquid"],
        "transfer_selector_changes": row["selector_changes"]["transfer"],
        "consumption_change_count": policies["consumption"]["count"],
        "consumption_change_max_abs": policies["consumption"]["max_abs"],
        "labor_change_count": policies["labor"]["count"],
        "labor_change_max_abs": policies["labor"]["max_abs"],
        "transfer_change_count": policies["transfer"]["count"],
        "transfer_change_max_abs": policies["transfer"]["max_abs"],
        "vb_forward_floor_hits": row["derivative_floor_hits"]["vb_forward"],
        "vb_backward_floor_hits": row["derivative_floor_hits"]["vb_backward"],
        "value_sha256": row["hashes"]["value"],
        "liquid_label_sha256": row["hashes"]["liquid_labels"],
        "transfer_label_sha256": row["hashes"]["transfer_labels"],
        "value_period_2_inf": row["value_period_2_inf"],
        "value_period_3_inf": row["value_period_3_inf"],
        "linear_solve_residual_inf": row["linear_solve_residual_inf"],
    }


def build(raw_root: Path, compact_root: Path, first_preflight_root: Path) -> int:
    raw_root = Path(raw_root)
    compact_root = Path(compact_root)
    first_preflight_root = Path(first_preflight_root)
    compact_root.mkdir(parents=True, exist_ok=False)
    trace = read_json(raw_root / "iteration_trace.json")
    base = read_json(raw_root / "mechanism_summary.json")
    summary = derive_summary(trace, base)
    for name in (
        "source_identity.json",
        "input_invariance_receipt.json",
        "instrumentation_invariance_receipt.json",
        "call_ledger.json",
    ):
        run.write_json(compact_root / name, read_json(raw_root / name))
    run.write_json(compact_root / "mechanism_summary.json", summary)
    first_source = read_json(first_preflight_root / "source_identity.json")
    run.write_json(
        compact_root / "engineering_retry_receipt.json",
        {
            "engineering_retries": 1,
            "first_preflight_status": "FAIL",
            "first_preflight_science_calls": 0,
            "failure_scope": "line-ending representation used for accepted parity manifest entry verification",
            "expected_manifest_sha256": first_source["accepted_small_grid_instrumentation_parity_entry"]["expected_sha256"],
            "first_actual_canonical_lf_sha256": first_source["accepted_small_grid_instrumentation_parity_entry"]["actual_sha256"],
            "retry_repair": "record byte and canonical-LF hashes; accept only an exact match of either representation",
            "second_preflight_status": "PASS",
            "science_changed": False,
        },
    )
    external_manifest = seal(raw_root, "CH5_MP4C_K1_J640_HJB_MECHANISM_EXTERNAL_V1")
    run.write_json(compact_root / "external_manifest.json", external_manifest)
    rows = [_csv_row(row) for row in trace["iterations"]]
    with (compact_root / "iteration_trace.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    seal(compact_root, "CH5_MP4C_K1_J640_HJB_MECHANISM_COMPACT_V1")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("raw_root", type=Path)
    parser.add_argument("compact_root", type=Path)
    parser.add_argument("first_preflight_root", type=Path)
    args = parser.parse_args()
    return build(args.raw_root, args.compact_root, args.first_preflight_root)


if __name__ == "__main__":
    raise SystemExit(main())
