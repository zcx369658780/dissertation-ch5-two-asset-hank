"""Offline consolidation for the frozen 31-province J160 HJB execution."""
from __future__ import annotations

import argparse
import csv
import json
from hashlib import sha256
from pathlib import Path
from statistics import median
from typing import Any

from validators.multi_province.k1_standalone_hjb_ra_wage_3x3 import run as accepted_hjb


PASS = "J160_FIRST_TURN_PROVINCIAL_HJB_VIABILITY_PASS"
BLOCKED = "J160_FIRST_TURN_PROVINCIAL_HJB_VIABILITY_BLOCKED"
NEXT_GATE = "REVIEWER_J160_FIRST_TURN_PROVINCIAL_ROUTE_DECISION"


def support_location(ra: float, wage: float) -> str:
    inside = 0.06 <= ra <= 0.07 and 13.0 <= wage <= 18.0
    boundary = inside and (ra in {0.06, 0.07} or wage in {13.0, 18.0})
    if boundary:
        return "ON_ACCEPTED_J160_BOUNDARY"
    if inside:
        return "INSIDE_ACCEPTED_J160_RECTANGLE"
    return "OUTSIDE_ACCEPTED_J160_RECTANGLE"


def terminal_classification(points: list[dict[str, Any]]) -> str:
    if len(points) != 31:
        raise ValueError(f"expected exactly 31 province receipts, found {len(points)}")
    return PASS if all(item["hjb"]["classification"] == "HJB_CONVERGED" for item in points) else BLOCKED


def _distribution(values: list[float]) -> dict[str, float | int | None]:
    finite = sorted(value for value in values if value is not None)
    if not finite:
        return {"count": 0, "min": None, "median": None, "max": None}
    return {"count": len(finite), "min": finite[0], "median": median(finite), "max": finite[-1]}


def build_summary(points: list[dict[str, Any]], ledger: dict[str, Any]) -> dict[str, Any]:
    decision = terminal_classification(points)
    classes = [item["hjb"]["classification"] for item in points]
    enriched_failures = []
    for item in points:
        if item["hjb"]["classification"] != "HJB_CONVERGED":
            inputs = item["household_inputs"]
            enriched_failures.append({
                "province_index": item["province_index"], "province": item["province"],
                "classification": item["hjb"]["classification"],
                "consumed_r_a": inputs["consumed_r_a"],
                "household_composite_wage": inputs["household_composite_wage"],
                "support_location": support_location(inputs["consumed_r_a"], inputs["household_composite_wage"]),
                "first_illegal_iteration": item["hjb"]["first_illegal_iteration"],
                "hard_error": item["hjb"]["hard_error"],
            })
    support_counts: dict[str, int] = {}
    for item in points:
        inputs = item["household_inputs"]
        label = support_location(inputs["consumed_r_a"], inputs["household_composite_wage"])
        support_counts[label] = support_counts.get(label, 0) + 1
    return {
        "schema": "CH5_MP4C_K1_J160_PROVINCIAL_HJB_SUMMARY_V1",
        "terminal_classification": decision,
        "total_provinces": 31,
        "hjb_converged_count": classes.count("HJB_CONVERGED"),
        "nonconverged_but_legal_count": classes.count("HJB_NOT_CONVERGED"),
        "illegal_operator_count": classes.count("HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX"),
        "hard_error_count": sum(item["hjb"]["hard_error"] is not None for item in points),
        "iteration_distribution": _distribution([item["hjb"]["iterations_used"] for item in points]),
        "final_convergence_statistic_distribution": _distribution([item["hjb"]["final_convergence_statistic"] for item in points]),
        "maximum_a2max_distribution": _distribution([item["hjb"]["maximum_a2max"] for item in points]),
        "failure_provinces": enriched_failures,
        "accepted_standalone_j160_rectangle": {"r_a": [0.06, 0.07], "wage": [13.0, 18.0]},
        "province_support_location_counts": support_counts,
        "support_comparison_scope": "descriptive only; no recalibration authority",
        "call_ledger_checks": {
            "hjb_exactly_31": ledger["hjb_calls_started"] == ledger["hjb_calls_completed"] == 31,
            "kfe_zero": ledger["kfe_calls_started"] == ledger["kfe_calls_completed"] == 0,
            "scientific_retries_zero": ledger["scientific_retries"] == 0,
        },
        "kfe_caveat": "KFE=0; corrected multi-province upper-b leakage/MATLAB-style pinning blocker remains unresolved.",
        "results_eligibility": False,
        "next_gate": NEXT_GATE,
    }


def _write_points_csv(path: Path, points: list[dict[str, Any]]) -> None:
    fields = [
        "province_index", "province", "r_b", "consumed_r_a", "household_composite_wage",
        "tau", "transfer_income", "borrowing_rate_gap", "return_guard_state",
        "wage_guard_state", "classification", "iterations_used",
        "final_convergence_statistic", "maximum_a2max", "first_illegal_iteration",
        "arrays_finite_shape_valid", "support_location",
    ]
    with path.open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for item in points:
            inputs, hjb = item["household_inputs"], item["hjb"]
            writer.writerow({
                "province_index": item["province_index"], "province": item["province"],
                "r_b": inputs["r_b"], "consumed_r_a": inputs["consumed_r_a"],
                "household_composite_wage": inputs["household_composite_wage"],
                "tau": inputs["tau"], "transfer_income": inputs["transfer_income"],
                "borrowing_rate_gap": inputs["borrowing_rate_gap"],
                "return_guard_state": inputs["return_guard_state"],
                "wage_guard_state": inputs["wage_guard_state"],
                "classification": hjb["classification"], "iterations_used": hjb["iterations_used"],
                "final_convergence_statistic": hjb["final_convergence_statistic"],
                "maximum_a2max": hjb["maximum_a2max"],
                "first_illegal_iteration": hjb["first_illegal_iteration"],
                "arrays_finite_shape_valid": item["finite_shape_checks"]["all_arrays_finite_shape_valid"],
                "support_location": support_location(inputs["consumed_r_a"], inputs["household_composite_wage"]),
            })


def _report(summary: dict[str, Any], points: list[dict[str, Any]]) -> str:
    iteration = summary["iteration_distribution"]
    a2 = summary["maximum_a2max_distribution"]
    lines = [
        "# CH5 MP4C K1 — J160 provincial first-turn HJB viability report", "",
        "## Terminal classification", "", f"`{summary['terminal_classification']}`", "",
        "## Authority and scope", "",
        "The accepted compact turn-1 identity artifact supplied exactly 31 unique, provenance-closed province inputs. "
        "Each HJB consumed the sealed composite household wage `w` and consumed `r_a/rah`; no raw `wjt`, firm, wage, or return recomputation was used.", "",
        "Frozen science: `I=20,J=160,Nz=2`, `a=[0,100]`, `b=[-2,20]`, `h=1`, `Delta=1000`, "
        "tolerance `1e-7`, maxit `100`, and `A2max<=0.01`. Every province used a fresh source-style initialization; no warm start or scientific retry occurred.", "",
        "## Aggregate result", "",
        f"- Provinces: `{summary['total_provinces']}`",
        f"- Converged: `{summary['hjb_converged_count']}`",
        f"- Nonconverged but legal: `{summary['nonconverged_but_legal_count']}`",
        f"- Illegal operator: `{summary['illegal_operator_count']}`",
        f"- Hard errors: `{summary['hard_error_count']}`",
        f"- Iterations min/median/max: `{iteration['min']}/{iteration['median']}/{iteration['max']}`",
        f"- max A2max min/median/max: `{a2['min']}/{a2['median']}/{a2['max']}`", "",
        "## Province matrix", "",
        "| idx | province | consumed ra | composite w | class | iter | final statistic | max A2max | support |",
        "|---:|---|---:|---:|---|---:|---:|---:|---|",
    ]
    for item in points:
        inputs, hjb = item["household_inputs"], item["hjb"]
        lines.append(
            f"| {item['province_index']} | {item['province']} | {inputs['consumed_r_a']:.12g} | "
            f"{inputs['household_composite_wage']:.12g} | {hjb['classification']} | {hjb['iterations_used']} | "
            f"{hjb['final_convergence_statistic']} | {hjb['maximum_a2max']} | "
            f"{support_location(inputs['consumed_r_a'], inputs['household_composite_wage'])} |"
        )
    lines.extend([
        "", "## Interpretation boundary", "",
        "The support comparison uses only the accepted J160 rectangle `ra=[.06,.07], w=[13,18]` and is descriptive. "
        "It does not authorize recalibration or imply that points outside that rectangle are scientifically invalid.", "",
        f"Failures: `{json.dumps(summary['failure_provinces'], ensure_ascii=False)}`", "",
        "KFE was not run. The corrected multi-province finite-box upper-`b` leakage / MATLAB-style pinning blocker remains unresolved. "
        "No outer, firm, wage/return recalculation, MATLAB, K1B/K2, GE, downstream, shock, IRF, or Results route ran.", "",
        "Results eligibility=`FALSE`.", "", "## Exactly one next gate", "", f"`{NEXT_GATE}`", "",
    ])
    return "\n".join(lines)


def _seal(root: Path) -> dict[str, Any]:
    entries = []
    for path in sorted(item for item in root.rglob("*") if item.is_file() and item.name != "sealed_manifest_sha256.json"):
        entries.append({
            "path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size,
            "sha256": accepted_hjb.file_sha256(path),
        })
    return {
        "schema": "CH5_MP4C_K1_J160_PROVINCIAL_HJB_SEALED_MANIFEST_V1",
        "entries": entries, "entry_count": len(entries),
        "bytes_excluding_manifest": sum(item["bytes"] for item in entries),
    }


def finalize(evidence_root: Path, report_path: Path) -> dict[str, Any]:
    root = Path(evidence_root)
    points = [json.loads(path.read_text(encoding="utf-8")) for path in sorted(root.glob("p??_*_result.json"))]
    points.sort(key=lambda item: item["province_index"])
    ledger = json.loads((root / "final_call_ledger.json").read_text(encoding="utf-8"))
    summary = build_summary(points, ledger)
    accepted_hjb.write_json(root / "province_receipts.json", points)
    _write_points_csv(root / "points.csv", points)
    accepted_hjb.write_json(root / "summary.json", summary)
    accepted_hjb.write_json(root / "call_ledger.json", ledger)
    report_path = Path(report_path)
    report_path.write_text(_report(summary, points), encoding="utf-8", newline="\n")
    manifest = _seal(root)
    accepted_hjb.write_json(root / "sealed_manifest_sha256.json", manifest)
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
