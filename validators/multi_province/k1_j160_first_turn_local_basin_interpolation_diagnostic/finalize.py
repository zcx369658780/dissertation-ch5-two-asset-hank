"""Offline topology classification, report writing, and sealing."""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
from typing import Any

from validators.multi_province.k1_j160_first_turn_local_basin_interpolation_diagnostic import run


NEXT_GATE = "REVIEWER_J160_LOCAL_BASIN_INTERPOLATION_ROUTE_DECISION"


def _seal(root: Path) -> dict[str, Any]:
    entries = []
    for path in sorted(item for item in root.rglob("*") if item.is_file() and item.name != "sealed_manifest_sha256.json"):
        entries.append({
            "path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size,
            "sha256": run.file_sha256(path),
        })
    return {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_SEALED_MANIFEST_V1",
        "entry_count": len(entries), "bytes_excluding_manifest": sum(item["bytes"] for item in entries),
        "entries": entries,
    }


def build_topology(authority: dict[str, Any], probes: list[dict[str, Any]]) -> dict[str, Any]:
    pairs = []
    for pair in authority["pairs"]:
        interior = [item for item in probes if item["pair_id"] == pair["pair_id"]]
        interior.sort(key=lambda item: item["t"])
        pair_class = run.pair_classification(interior)
        ordered = [{
            "t": 0.0, "source": "accepted failure endpoint", "province": pair["failure"]["province"],
            "classification": pair["failure"]["accepted_hjb_classification"], "converged": False,
        }]
        ordered.extend({
            "t": item["t"], "source": "synthetic numerical probe", "province": None,
            "classification": item["hjb_classification"], "converged": item["converged"],
            "numerically_valid": item["numerically_valid"],
        } for item in interior)
        ordered.append({
            "t": 1.0, "source": "accepted success endpoint", "province": pair["success"]["province"],
            "classification": pair["success"]["accepted_hjb_classification"], "converged": True,
        })
        pairs.append({
            "pair_index": pair["pair_index"], "pair_id": pair["pair_id"],
            "failure_province": pair["failure"]["province"], "success_province": pair["success"]["province"],
            "ordered_outcomes": ordered, "pair_classification": pair_class,
            "unique_threshold_inferred": False,
        })
    return {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_PAIR_TOPOLOGY_V1",
        "pair_count": len(pairs), "pairs": pairs,
    }


def _postprocessor_defect(probes: list[dict[str, Any]]) -> dict[str, Any]:
    entries = []
    for item in probes:
        trace = item.get("trace_summary") or {}
        post_only = bool(
            item.get("iterations") is not None
            and trace.get("first_illegal_iteration") == item["iterations"] + 1
            and trace.get("iteration_count_observed") == item["iterations"]
        )
        entries.append({
            "point_id": item["point_id"], "post_system_matrix_is_only_recorded_illegal_operator": post_only,
            "recorded_mixed_maximum": trace.get("maximum_a2max"),
            "scientific_iteration_maximum_exact": None,
            "scientific_iteration_maximum_status": "UNAVAILABLE_AFTER_NONRETRYABLE_AGGREGATION_DEFECT",
            "scientific_iteration_legality_proven_from_ordering": post_only,
        })
    return {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_POSTPROCESSOR_DEFECT_V1",
        "classification": "SCIENTIFIC_A2MAX_EXACT_RECEIPT_UNAVAILABLE",
        "description": (
            "The initial receipt aggregator included the post-convergence implicit system matrix in the generator A2max maximum. "
            "For every call, the first recorded illegal matrix is exactly iteration_count+1, proving the scientific iteration "
            "operators preceded it without an illegal event, but the exact maximum across those scientific operators was not retained."
        ),
        "hjb_rerun_performed": False, "scientific_retry_performed": False,
        "repair_scope": "future postprocessing semantics only; persisted raw probe receipts are not rewritten",
        "all_scientific_iteration_legality_proven": all(item["scientific_iteration_legality_proven_from_ordering"] for item in entries),
        "exact_scientific_maximum_available": False, "entries": entries,
    }


def _report(
    panel: dict[str, Any], topology: dict[str, Any], probes: list[dict[str, Any]],
    ledger: dict[str, Any], defect: dict[str, Any],
) -> str:
    lines = [
        "# CH5 MP4C K1 — J160 first-turn local-basin interpolation diagnostic", "",
        "## Panel terminal class", "", f"`{panel['panel_classification']}`", "",
        "Results eligibility=`FALSE`.", "", "## Frozen authority", "",
        "The four preregistered accepted failure/success pairs passed exact non-`(ra,w)` household-input equality. "
        "No endpoint HJB was rerun. All twelve synthetic probes used fresh source-style initialization on "
        "`I=20,J=160,Nz=2`, `a=[0,100]`, `b=[-2,20]`, `Delta=1000`, tolerance `1e-7`, maxit `100`, and A2max gate `0.01`.", "",
        "## Probe outcomes", "",
        "| pair | t | synthetic ra | synthetic composite w | HJB | iterations | final max abs dV | mixed observer max* | mechanism if nonconverged |", 
        "|---|---:|---:|---:|---|---:|---:|---:|---|",
    ]
    for item in probes:
        trace = item.get("trace_summary") or {}
        lines.append(
            f"| {item['failure_province']}→{item['success_province']} | {item['t']:.2f} | "
            f"{item['consumed_r_a']:.17g} | {item['household_composite_wage']:.17g} | "
            f"{item['hjb_classification']} | {item['iterations']} | {item['final_max_abs_delta_v']} | "
            f"{trace.get('maximum_a2max')} | {trace.get('mechanism_classification')} |"
        )
    lines.extend(["", "## Pair topology", ""])
    for pair in topology["pairs"]:
        sequence = " → ".join(
            f"t={item['t']:g}:{'C' if item['converged'] else 'F'}" for item in pair["ordered_outcomes"]
        )
        lines.append(
            f"- {pair['failure_province']}→{pair['success_province']}: `{sequence}`; `{pair['pair_classification']}`."
        )
    lines.extend([
        "", "## Receipt blocker", "",
        f"`{defect['classification']}`. The first implementation incorrectly pooled the post-convergence implicit system matrix "
        "with source-generator A2max observations. In all 12 receipts the sole recorded illegal event is at `iterations+1`, so all "
        "scientific iteration operators are proven legal; however, their exact maximum A2max was not retained. The mixed values in "
        "the table (about 1–2) belong to the post-convergence system matrix and are not scientific generator A2max values.", "",
        "Because the exact required maximum receipt cannot be reconstructed without another HJB call, all four pair decisions are "
        "fail-closed as `PAIR_NUMERICAL_INVALIDITY_BLOCKER`; no rerun or scientific retry was performed.", "",
        "", "## Interpretation boundary", "",
        "These interpolated points are numerical probes only. They are not feasible provincial equilibria, calibrated states, "
        "upstream mapping outputs, or counterfactuals. The panel does not identify causality or authorize a threshold, clipping rule, "
        "recalibration, mapping/guard/HJB change, or Results use.", "",
        f"HJB started/completed/hard-error=`{ledger['hjb_calls_started']}/{ledger['hjb_calls_completed']}/{ledger['hjb_hard_errors']}`; "
        "KFE=`0`; endpoint HJB reruns=`0`; scientific retries=`0`; engineering retries=`0`.", "",
        "No outer/firm/wage/return/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results route ran.", "",
        "## Exactly one next gate", "", f"`{NEXT_GATE}`", "",
    ])
    return "\n".join(lines)


def finalize(evidence_root: Path, report_path: Path) -> dict[str, Any]:
    root = Path(evidence_root)
    authority = json.loads((root / "pair_input_authority.json").read_text(encoding="utf-8"))
    probes = json.loads((root / "probe_receipts.json").read_text(encoding="utf-8"))["probes"]
    ledger = json.loads((root / "call_ledger.json").read_text(encoding="utf-8"))
    topology = build_topology(authority, probes)
    defect = _postprocessor_defect(probes)
    classes = [item["pair_classification"] for item in topology["pairs"]]
    panel_class = run.panel_classification(classes)
    panel = {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_PANEL_DECISION_V1",
        "panel_classification": panel_class, "pair_class_counts": dict(Counter(classes)),
        "all_twelve_calls_started": ledger["hjb_calls_started"] == 12,
        "all_non_error_calls_numerically_valid": all(item["numerically_valid"] for item in probes),
        "hjb_calls_started": ledger["hjb_calls_started"], "hjb_calls_completed": ledger["hjb_calls_completed"],
        "hjb_hard_errors": ledger["hjb_hard_errors"], "kfe_calls": 0, "scientific_retries": 0,
        "results_eligibility": False, "next_gate": NEXT_GATE,
    }
    run.write_json(root / "pair_topology.json", topology)
    run.write_json(root / "panel_decision.json", panel)
    run.write_json(root / "receipt_postprocessor_defect.json", defect)
    Path(report_path).write_text(_report(panel, topology, probes, ledger, defect), encoding="utf-8", newline="\n")
    run.write_json(root / "sealed_manifest_sha256.json", _seal(root))
    return panel


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
