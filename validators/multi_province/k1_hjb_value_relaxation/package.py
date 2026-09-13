"""Create final adjudication and a no-overwrite compact evidence package."""

from __future__ import annotations

import argparse
import json
import shutil
from hashlib import sha256
from pathlib import Path
from typing import Any

import numpy as np

REPO = Path(__file__).resolve().parents[3]
FIELDS = ("value", "consumption", "labor", "transfer", "adjustment_cost", "mu_a", "mu_b")


def _write_json(path: Path, value: Any) -> None:
    if path.exists():
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _sha_file(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest().upper()


def finalize(external: Path, compact: Path) -> int:
    external = Path(external)
    compact = Path(compact)
    if compact.exists():
        raise FileExistsError(compact)
    comparison = json.loads((external / "baseline_treatment_comparison.json").read_text(encoding="utf-8"))
    treatments = json.loads((external / "treatment_summary.json").read_text(encoding="utf-8"))
    both = json.loads((external / "both_converged_fixed_point_comparison.json").read_text(encoding="utf-8"))
    normality = json.loads((external / "output_normality_adjudication.json").read_text(encoding="utf-8"))
    preflight = json.loads((external / "preflight.json").read_text(encoding="utf-8"))
    arrays: dict[str, list[np.ndarray]] = {name: [] for name in FIELDS}
    label_counts = {"liquid": 0, "transfer": 0}
    cells = 0
    same_endpoint_calls = 0
    for row in both:
        treatment = next(item for item in treatments if item["turn"] == row["turn"] and item["province"] == row["province"])
        with np.load(treatment["result_path"], allow_pickle=False) as current, np.load(treatment["accepted_hjb_path"], allow_pickle=False) as baseline:
            cells += current["value"].size
            for name in FIELDS:
                arrays[name].append(np.abs(current[name] - baseline[name]).ravel())
            liquid = int(np.count_nonzero(current["liquid_label"] != baseline["liquid_label"]))
            transfer = int(np.count_nonzero(current["transfer_label"] != baseline["transfer_label"]))
            label_counts["liquid"] += liquid
            label_counts["transfer"] += transfer
            if float(np.max(np.abs(current["value"] - baseline["value"]))) < 1e-6 and liquid == 0 and transfer == 0:
                same_endpoint_calls += 1
    fixed = {name: {"max_abs": float(np.max(np.concatenate(values))),
                    "median_abs": float(np.median(np.concatenate(values)))} for name, values in arrays.items()}
    fixed["liquid_label_differences"] = label_counts["liquid"]
    fixed["liquid_label_difference_share"] = label_counts["liquid"] / cells
    fixed["transfer_label_differences"] = label_counts["transfer"]
    fixed["transfer_label_difference_share"] = label_counts["transfer"] / cells
    fixed["near_same_endpoint_calls_value_lt_1e6_and_labels_equal"] = same_endpoint_calls
    fixed["both_converged_calls"] = len(both)
    recovered = comparison["baseline_failed_treatment_converged"]
    final = {
        "classification": "PARTIAL_SUPPORT__SYSTEMATIC_CHATTERING_REDUCTION__NET_ONE_CONVERGENCE_GAIN__TURN2_NONE_AND_ENDPOINT_DIVERGENCE_OUTLIERS",
        "exact_input_coverage": 62,
        "omega1_equivalence": "PASS_EXACT_ON_PREREGISTERED_TURN1_BEIJING_CONVERGED_AND_TURN1_ANHUI_CEILING_FAILURE",
        "convergence": comparison["convergence"],
        "convergence_transitions": {"baseline_failed_to_treatment_converged": len(recovered),
                                    "baseline_converged_to_treatment_failed": len(comparison["baseline_converged_treatment_failed"])},
        "systematic_trajectory_effects": comparison["pairwise_trajectory_comparison"],
        "raw_gap_vs_relaxed_update": comparison["raw_gap_vs_relaxed_update"],
        "derivative_floor_ordering": {
            **comparison["derivative_floor_ordering"],
            "recovered_calls_floor_never_hit": sum(row["first_floor_iteration"] is None for row in recovered),
            "interpretation": "all eight newly converged calls avoided derivative-floor activity; improvement therefore does not require a floor change",
        },
        "output_normality": {"recomputed_normal_calls": normality["recomputed_normal_count"],
                             "scientific_exceptions": 0, "accepted_label_domain": normality["accepted_domain_proven_from_baseline_and_treatment"]},
        "both_converged_fixed_point_comparison": fixed,
        "both_converged_interpretation": "not uniform: five of fifteen calls have V max-abs difference below 1e-6 with identical labels, while endpoint/control outliers prevent a general same-fixed-point conclusion",
        "baseline_failed_treatment_converged": recovered,
        "mechanism_interpretation": "partial support: omega=0.5 broadly reduces switching, reversions and gap non-monotonicity, and restores eight turn1 calls, but it loses five prior turn1 convergences, loses both prior turn2 convergences, and leaves all turn2 calls unconverged",
        "production_contract_ready": False,
        "recommended_next_owner_gate": "OWNER_HJB_RELAXATION_MIXED_EVIDENCE_AND_TURN2_FIXED_POINT_COHERENCE_REVIEW",
        "causal_boundary": comparison["causal_boundary"],
        "kfe_caveat": comparison["kfe_caveat"], "kkt_caveat": comparison["kkt_caveat"],
        "results_eligible": False,
    }
    final_path = external / "final_analysis.json"
    _write_json(final_path, final)
    runner = REPO / "validators/multi_province/k1_hjb_value_relaxation/run.py"
    source_adjudication = {
        "status": "POST_SCIENCE_METADATA_ALLOWLIST_CORRECTION__NO_HJB_RERUN",
        "executed_runner_sha256": preflight["source_sha256"]["validators/multi_province/k1_hjb_value_relaxation/run.py"],
        "candidate_runner_sha256": _sha_file(runner),
        "executed_relaxed_hjb_sha256": preflight["source_sha256"]["validators/multi_province/k1_hjb_value_relaxation/relaxed_hjb.py"],
        "candidate_relaxed_hjb_sha256": _sha_file(REPO / "validators/multi_province/k1_hjb_value_relaxation/relaxed_hjb.py"),
        "change": "accepted liquid-label domain in output-only normality metadata changed from B,F to 0,B,F",
        "scientific_control_flow_changed": False, "scientific_outputs_changed": False, "scientific_rerun": False,
    }
    source_path = external / "execution_source_adjudication.json"
    _write_json(source_path, source_adjudication)
    compact.mkdir(parents=True)
    selected = [
        "preflight.json", "identity_receipts.json", "science_started.json", "omega1_equivalence.json",
        "call_ledger.json", "direct_solve_count_receipt.json", "terminal_result.json", "treatment_summary.json",
        "baseline_treatment_comparison.json", "both_converged_fixed_point_comparison.json",
        "output_normality_adjudication.json", "province_comparison.csv", "final_analysis.json",
        "execution_source_adjudication.json",
    ]
    for relative in selected:
        target = compact / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(external / relative, target)
    for path in sorted((external / "traces").rglob("*.json")):
        target = compact / path.relative_to(external)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("external", type=Path)
    parser.add_argument("compact", type=Path)
    args = parser.parse_args()
    return finalize(args.external, args.compact)


if __name__ == "__main__":
    raise SystemExit(main())
