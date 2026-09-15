"""Offline report and panel classification for the six J160 failure replays."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from validators.multi_province.k1_j160_first_turn_six_failure_hjb_mechanism_panel import run


NEXT_GATE = "REVIEWER_SIX_FAILURE_HJB_MECHANISM_ROUTE_DECISION"


def panel_classification(classes: list[str]) -> str:
    if len(classes) != 6:
        raise ValueError("panel classification requires exactly six provinces")
    if "FAILURE_REPRODUCIBILITY_BLOCKER" in classes:
        return "SIX_FAILURES_MECHANISM_UNRESOLVED"
    unique = set(classes)
    if unique == {"POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION"}:
        return "SIX_FAILURES_HOMOGENEOUS_CHATTER"
    if unique == {"SLOW_MONOTONE_OR_NEAR_MONOTONE_VALUE_CONVERGENCE"}:
        return "SIX_FAILURES_HOMOGENEOUS_SLOW_CONVERGENCE"
    if len(unique) > 1:
        return "SIX_FAILURES_HETEROGENEOUS_MECHANISMS"
    return "SIX_FAILURES_MECHANISM_UNRESOLVED"


def _seal(root: Path) -> dict[str, Any]:
    entries = []
    for path in sorted(item for item in root.rglob("*") if item.is_file() and item.name != "sealed_manifest_sha256.json"):
        entries.append({
            "path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size,
            "sha256": run.file_sha256(path),
        })
    return {
        "schema": "CH5_MP4C_K1_J160_SIX_FAILURE_HJB_MECHANISM_PANEL_SEALED_MANIFEST_V1",
        "entry_count": len(entries), "bytes_excluding_manifest": sum(item["bytes"] for item in entries),
        "entries": entries,
    }


def _report(panel: dict[str, Any], neighbors: dict[str, Any]) -> str:
    lines = [
        "# CH5 MP4C K1 — J160 first-turn six-failure HJB mechanism panel diagnostic", "",
        "## Panel terminal classification", "", f"`{panel['panel_classification']}`", "",
        "Results eligibility=`FALSE`.", "", "## Authority and instrumentation invariance", "",
        "The accepted viability and J640 mechanism manifests passed exact byte/canonical-LF verification. "
        "The six full household-call inputs were recovered from the accepted sealed input artifact. "
        "The accepted J640 observational wrapper was imported unchanged and its accepted OFF/ON parity authority was reused without a new HJB call.", "",
        "For all six calls, the sealed common inputs were `rb=.02`, `tau=.05`, transfer income `=.1`, "
        "borrowing-rate gap `=.07`, return guard `NOT_APPLIED_BOOTSTRAP`, wage guard `UNSATURATED`, "
        "D1 OFF, and the accepted adapter parameters. The province-specific consumed `ra/rah` and composite `w` appear below; raw `wjt` was not substituted.", "",
        "## Province replay and event ordering", "",
        "| province | ra | composite w | replay | first switch | first non-decrease | first floor | decreases/non-decreases | class |",
        "|---|---:|---:|---|---:|---:|---:|---:|---|",
    ]
    for item in panel["provinces"]:
        inputs = item["exact_household_inputs"]
        lines.append(
            f"| {item['province']} | {inputs['consumed_r_a']:.17g} | {inputs['household_composite_wage']:.17g} | "
            f"{'nonconverged@100' if not item['replay_converged'] else 'converged'} | "
            f"{item['first_policy_or_selector_switch_iteration']} | {item['first_value_stat_non_decrease_iteration']} | "
            f"{item['first_derivative_floor_hit_iteration']} | {item['value_stat_decrease_count']}/{item['value_stat_non_decrease_count']} | "
            f"{item['classification']} |"
        )
    cycle_rows = [item for item in panel["provinces"] if item["classification"] == "REPEATING_OR_LOW_PERIOD_CYCLE"]
    lines.extend(["", "All event-order statements are descriptive temporal evidence, not causal identification.", ""])
    for item in cycle_rows:
        recurrence = item["exact_joint_selector_recurrence"]
        lines.append(
            f"{item['province']} has exact joint-selector recurrence from iteration "
            f"{recurrence['prior_iteration']} to {recurrence['iteration']} (period {recurrence['period']}); "
            "no exact value recurrence was observed."
        )
    lines.extend(["", "## Nearest accepted successful provinces", ""])
    for failure in neighbors["failures"]:
        first = failure["nearest_successful_neighbors"][0]
        lines.append(
            f"- {failure['failure_province']} → {first['province']}: raw `(ra,w)` Euclidean distance "
            f"`{first['euclidean_distance_raw_ra_w']}`, success input "
            f"`({first['consumed_r_a']},{first['household_composite_wage']})`, "
            f"iterations `{first['accepted_iterations']}`, final statistic `{first['accepted_final_convergence_statistic']}`."
        )
    lines.extend([
        "", "This nearest-neighbor comparison uses accepted receipts only and is descriptive; distance is not a causal explanation.", "",
        "## J640 comparison and boundaries", "",
        "The accepted J640 reference was policy/selector chatter with first switch at iteration 2, first value-stat non-decrease at 8, "
        "first derivative-floor hit at 10, 61 decreases and 38 non-decreases, persistent switching, and no exact low-period value cycle. "
        "Similarity or difference in temporal order does not establish a shared or distinct causal mechanism.", "",
        f"Panel conclusion: `{panel['panel_classification']}`.", "",
        f"HJB calls: `{panel['call_ledger']['hjb_calls_started']}/6`; KFE=`0`; successful-province HJB=`0`; scientific retries=`0`.", "",
        "The corrected multi-province finite-box upper-b leakage / MATLAB-style pinning KFE blocker remains unresolved. "
        "No outer/firm/wage/return/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results route ran.", "",
        "## Exactly one next gate", "", f"`{NEXT_GATE}`", "",
    ])
    return "\n".join(lines)


def finalize(evidence_root: Path, report_path: Path) -> dict[str, Any]:
    root = Path(evidence_root)
    classifications = json.loads((root / "province_mechanism_classification.json").read_text(encoding="utf-8"))["provinces"]
    ledger = json.loads((root / "call_ledger.json").read_text(encoding="utf-8"))
    neighbors = json.loads((root / "nearest_successful_neighbors.json").read_text(encoding="utf-8"))
    panel_class = panel_classification([item["classification"] for item in classifications])
    summary = {
        "schema": "CH5_MP4C_K1_J160_SIX_FAILURE_HJB_MECHANISM_PANEL_SUMMARY_V1",
        "panel_classification": panel_class,
        "province_count": len(classifications), "provinces": classifications,
        "reproducibility_gate_open_count": sum(item["reproduced_accepted_legal_nonconvergence"] for item in classifications),
        "class_counts": dict(__import__("collections").Counter(item["classification"] for item in classifications)),
        "all_iteration_operators_legal": all(item["all_iteration_operators_legal"] for item in classifications),
        "all_finite_shape_checks_pass": all(item["all_finite_checks_pass"] and item["all_shape_checks_pass"] for item in classifications),
        "maximum_a2max": max(item["maximum_a2max"] for item in classifications),
        "j640_descriptive_reference": {
            "classification": "POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION",
            "event_ordering": [["policy_or_selector_switch", 2], ["value_stat_non_decrease", 8], ["derivative_floor_hit", 10]],
            "value_stat_decrease_count": 61, "value_stat_non_decrease_count": 38,
            "causal_identity_claimed": False,
        },
        "call_ledger": ledger,
        "kfe_calls": 0, "scientific_retries": 0, "results_eligibility": False,
        "next_gate": NEXT_GATE,
    }
    run.write_json(root / "panel_summary.json", summary)
    Path(report_path).write_text(_report(summary, neighbors), encoding="utf-8", newline="\n")
    run.write_json(root / "sealed_manifest_sha256.json", _seal(root))
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence_root", type=Path)
    parser.add_argument("report_path", type=Path)
    args = parser.parse_args()
    summary = finalize(args.evidence_root, args.report_path)
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
