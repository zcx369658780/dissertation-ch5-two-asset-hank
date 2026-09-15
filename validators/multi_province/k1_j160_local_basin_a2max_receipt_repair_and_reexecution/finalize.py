"""Finalize the controlled A2max receipt reexecution without new science calls."""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
from typing import Any

from validators.multi_province.k1_j160_first_turn_local_basin_interpolation_diagnostic import run as blocked
from validators.multi_province.k1_j160_local_basin_a2max_receipt_repair_and_reexecution import run


NEXT_GATE = "REVIEWER_J160_LOCAL_BASIN_REEXECUTION_ROUTE_DECISION"


def reproducibility_comparison(authority: dict[str, Any], probes: list[dict[str, Any]]) -> dict[str, Any]:
    expected = {item["point_id"]: item for item in authority["points"]}
    entries = []
    for actual in probes:
        prior = expected[actual["point_id"]]
        d_v_diff = (
            abs(actual["final_max_abs_delta_v"] - prior["final_max_abs_delta_v"])
            if actual["final_max_abs_delta_v"] is not None else None
        )
        d_v_bit_exact = bool(
            actual["final_max_abs_delta_v"] is not None
            and float(actual["final_max_abs_delta_v"]).hex() == float(prior["final_max_abs_delta_v"]).hex()
        )
        entries.append({
            "point_id": actual["point_id"],
            "sealed_inputs_exact": (
                actual["consumed_r_a"] == prior["consumed_r_a"]
                and actual["household_composite_wage"] == prior["household_composite_wage"]
            ),
            "previous_terminal_class": prior["hjb_classification"],
            "reexecuted_terminal_class": actual["hjb_classification"],
            "terminal_class_exact": actual["hjb_classification"] == prior["hjb_classification"],
            "previous_iterations": prior["iterations"], "reexecuted_iterations": actual["iterations"],
            "iteration_count_exact": actual["iterations"] == prior["iterations"],
            "previous_final_max_abs_delta_v": prior["final_max_abs_delta_v"],
            "reexecuted_final_max_abs_delta_v": actual["final_max_abs_delta_v"],
            "final_max_abs_delta_v_absolute_difference": d_v_diff,
            "final_max_abs_delta_v_exact": d_v_bit_exact,
        })
    receipt = {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_REEXECUTION_REPRODUCIBILITY_V1",
        "point_count": len(entries), "entries": entries,
        "scientific_retries": 0,
    }
    receipt["pass"] = bool(
        len(entries) == 12 and all(
            item["sealed_inputs_exact"] and item["terminal_class_exact"]
            and item["iteration_count_exact"] and item["final_max_abs_delta_v_exact"]
            for item in entries
        )
    )
    return receipt


def pair_topology(authority: dict[str, Any], probes: list[dict[str, Any]]) -> dict[str, Any]:
    pair_authority = {item["pair_id"]: item for item in authority["accepted_pair_authority"]["pairs"]}
    pairs = []
    for pair_id, pair in pair_authority.items():
        interior = sorted((item for item in probes if item["pair_id"] == pair_id), key=lambda item: item["t"])
        pair_class = blocked.pair_classification(interior)
        ordered = [{
            "t": 0.0, "source": "accepted failure endpoint", "province": pair["failure"]["province"],
            "classification": pair["failure"]["accepted_hjb_classification"], "converged": False,
        }]
        ordered.extend({
            "t": item["t"], "source": "controlled reexecution synthetic probe", "province": None,
            "classification": item["hjb_classification"], "converged": item["converged"],
            "numerically_valid": item["numerically_valid"],
        } for item in interior)
        ordered.append({
            "t": 1.0, "source": "accepted success endpoint", "province": pair["success"]["province"],
            "classification": pair["success"]["accepted_hjb_classification"], "converged": True,
        })
        pairs.append({
            "pair_index": pair["pair_index"], "pair_id": pair_id,
            "failure_province": pair["failure"]["province"], "success_province": pair["success"]["province"],
            "ordered_outcomes": ordered, "pair_classification": pair_class,
            "all_three_interior_legality_receipts_valid": all(item["numerically_valid"] for item in interior),
            "unique_threshold_inferred": False,
        })
    pairs.sort(key=lambda item: item["pair_index"])
    return {"schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_REEXECUTION_PAIR_TOPOLOGY_V1", "pair_count": len(pairs), "pairs": pairs}


def _seal(root: Path) -> dict[str, Any]:
    entries = []
    for path in sorted(item for item in root.rglob("*") if item.is_file() and item.name != "sealed_manifest_sha256.json"):
        entries.append({"path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size, "sha256": run.file_sha256(path)})
    return {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_REEXECUTION_SEALED_MANIFEST_V1",
        "entry_count": len(entries), "bytes_excluding_manifest": sum(item["bytes"] for item in entries), "entries": entries,
    }


def _report(panel: dict[str, Any], topology: dict[str, Any], reproducibility: dict[str, Any], probes: list[dict[str, Any]], ledger: dict[str, Any]) -> str:
    lines = [
        "# CH5 MP4C K1 — J160 local-basin A2max receipt repair and controlled reexecution", "",
        "## Panel terminal class", "", f"`{panel['panel_classification']}`", "", "Results eligibility=`FALSE`.", "",
        "## Receipt repair and invariance", "",
        "Scientific A2max now contains only source-generator observations from actual HJB iterations. Sequence length is checked "
        "against the returned scientific iteration count. The post-convergence implicit system matrix is separately retained as "
        "`NOT_SCIENTIFIC_A2MAX / EXCLUDED_FROM_LEGALITY`. Accepted observer invariance and focused deterministic tests passed; "
        "no parity HJB call was added.", "", "## Exact probe receipts", "",
        "| pair | t | HJB | iterations | final max abs dV | max scientific A2max | argmax iter | first illegal | legal | reproducible |",
        "|---|---:|---|---:|---:|---:|---:|---:|---|---|",
    ]
    comparison = {item["point_id"]: item for item in reproducibility["entries"]}
    for item in probes:
        a2 = item["scientific_a2max_receipt"] or {}
        rep = comparison[item["point_id"]]
        lines.append(
            f"| {item['failure_province']}→{item['success_province']} | {item['t']:.2f} | {item['hjb_classification']} | "
            f"{item['iterations']} | {item['final_max_abs_delta_v']} | {a2.get('max_scientific_A2max')} | "
            f"{a2.get('max_scientific_A2max_iteration')} | {a2.get('first_scientific_illegal_iteration')} | "
            f"{a2.get('scientific_operator_legal')} | {rep['terminal_class_exact'] and rep['iteration_count_exact'] and rep['final_max_abs_delta_v_exact']} |"
        )
    lines.extend(["", "## Formal pair topology", ""])
    for pair in topology["pairs"]:
        sequence = " → ".join(f"t={item['t']:g}:{'C' if item['converged'] else 'F'}" for item in pair["ordered_outcomes"])
        lines.append(f"- {pair['failure_province']}→{pair['success_province']}: `{sequence}`; `{pair['pair_classification']}`.")
    nonconverged = [item for item in probes if not item["converged"] and item["hard_error"] is None]
    lines.extend(["", "## Nonconverged mechanism summaries", ""])
    for item in nonconverged:
        lines.append(f"- {item['point_id']}: `{item['trace_events']['mechanism_classification']}`.")
    lines.extend([
        "", "## Interpretation boundary", "",
        "The confirmed nonmonotone local numerical basin is not an economic multiple equilibrium, provincial-equilibrium multiplicity, "
        "calibration error, or mapping error. These synthetic points remain numerical HJB diagnostics only and do not authorize "
        "recalibration, clipping, guard/mapping/HJB/selector/floor/grid changes, or Results use.", "",
        f"HJB started/completed/hard-error=`{ledger['hjb_calls_started']}/{ledger['hjb_calls_completed']}/{ledger['hjb_hard_errors']}`; "
        f"KFE=`0`; endpoint HJB=`0`; scientific retries=`0`; engineering retries=`{ledger['engineering_retries_used']}`.", "",
        "No outer/firm/wage/return/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results route ran.", "",
        "## Exactly one next gate", "", f"`{NEXT_GATE}`", "",
    ])
    return "\n".join(lines)


def finalize(evidence_root: Path, report_path: Path) -> dict[str, Any]:
    root = Path(evidence_root)
    authority = json.loads((root / "pair_input_authority.json").read_text(encoding="utf-8"))
    probes = json.loads((root / "probe_receipts.json").read_text(encoding="utf-8"))["probes"]
    ledger = json.loads((root / "call_ledger.json").read_text(encoding="utf-8"))
    reproducibility = reproducibility_comparison(authority, probes)
    topology = pair_topology(authority, probes)
    classes = [item["pair_classification"] for item in topology["pairs"]]
    panel_class = blocked.panel_classification(classes)
    panel = {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_REEXECUTION_PANEL_DECISION_V1",
        "panel_classification": panel_class, "pair_class_counts": dict(Counter(classes)),
        "all_twelve_scientific_legality_receipts_valid": all(item["numerically_valid"] for item in probes),
        "blocked_run_reproducibility_pass": reproducibility["pass"],
        "hjb_calls_started": ledger["hjb_calls_started"], "hjb_calls_completed": ledger["hjb_calls_completed"],
        "hjb_hard_errors": ledger["hjb_hard_errors"], "kfe_calls": 0, "scientific_retries": 0,
        "results_eligibility": False, "next_gate": NEXT_GATE,
    }
    run.write_json(root / "reproducibility_comparison.json", reproducibility)
    run.write_json(root / "pair_topology.json", topology)
    run.write_json(root / "panel_decision.json", panel)
    with Path(report_path).open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(_report(panel, topology, reproducibility, probes, ledger))
    run.write_json(root / "sealed_manifest_sha256.json", _seal(root))
    return panel


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence_root", type=Path)
    parser.add_argument("report_path", type=Path)
    args = parser.parse_args()
    panel = finalize(args.evidence_root, args.report_path)
    print(json.dumps(panel, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
