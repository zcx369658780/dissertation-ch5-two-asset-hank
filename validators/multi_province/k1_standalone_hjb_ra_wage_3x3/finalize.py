"""Offline-only classification and compact-evidence builder for the 3x3 scan."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

import numpy as np

from . import run


QUALITY_LABELS = {
    "BOUNDARY_CONVERGED_CANDIDATE",
    "GOOD_STEADY_STATE_CANDIDATE",
    "QUALITY_AMBIGUOUS__OWNER_REVIEW_REQUIRED",
}


def descriptive_quality_label(kfe_receipt: dict[str, Any]) -> str:
    """Apply exact endpoint/mode semantics, without a fitted numeric cutoff."""
    distribution = kfe_receipt["distribution"]
    modal_a = set(float(value) for value in distribution["modal_a"])
    modal_b = set(float(value) for value in distribution.get("modal_b", []))
    boundary = distribution["boundary_mass_shares"]
    if (10.0 in modal_a and float(boundary["amax"]) > 0.0) or (
        5.0 in modal_b and float(boundary["bmax"]) > 0.0
    ):
        return "BOUNDARY_CONVERGED_CANDIDATE"
    if 0.0 in modal_a or -2.0 in modal_b:
        return "QUALITY_AMBIGUOUS__OWNER_REVIEW_REQUIRED"
    return "GOOD_STEADY_STATE_CANDIDATE"


def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def seal(directory: Path, schema: str) -> dict[str, Any]:
    directory = Path(directory)
    target = directory / "sealed_manifest_sha256.json"
    entries = []
    for path in sorted(item for item in directory.rglob("*") if item.is_file() and item != target):
        entries.append({
            "path": path.relative_to(directory).as_posix(), "bytes": path.stat().st_size,
            "sha256": run.file_sha256(path),
        })
    manifest = {
        "schema": schema, "entries": entries,
        "entry_count": len(entries), "bytes_excluding_manifest": sum(item["bytes"] for item in entries),
    }
    run.write_json(target, manifest)
    return {"path": str(target.resolve()), "sha256": run.file_sha256(target), **manifest}


def build(external_root: Path, compact_root: Path) -> int:
    external_root = Path(external_root)
    compact_root = Path(compact_root)
    if not (external_root / "execution_complete.json").is_file():
        raise ValueError("external execution is incomplete")
    if (external_root / "sealed_manifest_sha256.json").exists():
        raise FileExistsError("external evidence is already sealed")
    compact_root.mkdir(parents=True, exist_ok=False)

    external_manifest = seal(external_root, "CH5_MP4C_K1_STANDALONE_HJB_RA_WAGE_3X3_EXTERNAL_V1")
    point_paths = sorted(external_root.glob("p*_result.json"))
    if len(point_paths) != 9:
        raise ValueError("expected exactly nine completed point receipts")
    points = [read_json(path) for path in point_paths]
    rows = []
    marginals = []
    for point in points:
        hjb = point["hjb"]
        label = None
        aggregates: dict[str, Any] = {}
        distribution: dict[str, Any] = {}
        if hjb["classification"] == "HJB_CONVERGED" and point["kfe"].get("completed", True):
            label = descriptive_quality_label(point["kfe"])
            aggregates = point["kfe"]["aggregates"]
            distribution = point["kfe"]["distribution"]
            marginals.append({
                "point_id": point["point_id"], "r_a": point["r_a"], "wage": point["wage"],
                "b_grid": np.linspace(-2.0, 5.0, 20).tolist(),
                "a_grid": np.linspace(0.0, 10.0, 20).tolist(),
                "b_marginal_mass": distribution["b_marginal_mass"],
                "a_marginal_mass": distribution["a_marginal_mass"],
            })
        point["preliminary_quality_label"] = label
        rows.append({
            "point_index": point["point_index"], "point_id": point["point_id"],
            "rb": point["r_b"], "ra": point["r_a"], "wage": point["wage"],
            "hjb_classification": hjb["classification"], "iterations": hjb["iterations_used"],
            "final_statistic": hjb["final_convergence_statistic"],
            "first_illegal_iteration": hjb["first_illegal_iteration"],
            "maximum_A2max": hjb["maximum_a2max"],
            "minimum_stored_off_diagonal": hjb["minimum_stored_off_diagonal"],
            "kfe_ran": point["kfe"]["ran"], "quality_label": label,
            "Ct": aggregates.get("Ct"), "Lt": aggregates.get("Lt"),
            "At": aggregates.get("At"), "Bt": aggregates.get("Bt"),
            "Bt_pos": distribution.get("Bt_pos"), "Bt_neg": distribution.get("Bt_neg"),
            "bmin_mass": distribution.get("boundary_mass_shares", {}).get("bmin"),
            "bmax_mass": distribution.get("boundary_mass_shares", {}).get("bmax"),
            "amin_mass": distribution.get("boundary_mass_shares", {}).get("amin"),
            "amax_mass": distribution.get("boundary_mass_shares", {}).get("amax"),
            "modal_b": json.dumps(distribution.get("modal_b"), separators=(",", ":")),
            "modal_a": json.dumps(distribution.get("modal_a"), separators=(",", ":")),
            "total_mass": distribution.get("total_mass"),
            "density_min": distribution.get("density_min"),
            "density_negative_count": distribution.get("density_negative_count"),
            "kfe_raw_residual_inf": point["kfe"].get("kfe", {}).get("raw_residual_inf"),
        })

    good = [row for row in rows if row["quality_label"] == "GOOD_STEADY_STATE_CANDIDATE"]
    summary = {
        "terminal_classification": "ALL_HJB_CONVERGED__LOW_AND_MID_RA_LOWER_BOUND_AMBIGUOUS__HIGH_RA_UPPER_A_BOUNDARY_PILEUP",
        "results_eligibility": False,
        "grid": {"rb": [0.02], "ra": [0.02, 0.055, 0.09], "wage": [0.8, 1.05, 1.3]},
        "counts": {
            "HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX": sum(row["hjb_classification"] == "HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX" for row in rows),
            "HJB_NOT_CONVERGED": sum(row["hjb_classification"] == "HJB_NOT_CONVERGED" for row in rows),
            "HJB_CONVERGED": sum(row["hjb_classification"] == "HJB_CONVERGED" for row in rows),
            "BOUNDARY_CONVERGED_CANDIDATE": sum(row["quality_label"] == "BOUNDARY_CONVERGED_CANDIDATE" for row in rows),
            "GOOD_STEADY_STATE_CANDIDATE": len(good),
            "QUALITY_AMBIGUOUS__OWNER_REVIEW_REQUIRED": sum(row["quality_label"] == "QUALITY_AMBIGUOUS__OWNER_REVIEW_REQUIRED" for row in rows),
        },
        "connected_good_coarse_region": [],
        "connected_good_coarse_region_exists": False,
        "good_candidate_aggregate_ranges": None,
        "observed_transition": {
            "direction": "ra",
            "between": [0.055, 0.09],
            "description": "All wages move from essentially all mass at structural amin to an artificial amax mode/pile-up; wage produces no HJB failure in the coarse grid.",
        },
        "recommended_next_gate": {
            "name": "OWNER_REVIEW_STANDALONE_RA_TRANSITION_REFINEMENT_3X3",
            "run_now": False,
            "grid": {"rb": [0.02], "ra": [0.065, 0.0725, 0.08], "wage": [0.8, 1.05, 1.3]},
            "reason": "Bracket the observed lower-to-upper illiquid-boundary transition while preserving the same wage coverage.",
        },
        "quality_semantics": {
            "cutoff_fitted_after_results": False,
            "upper_endpoint_mode": "BOUNDARY_CONVERGED_CANDIDATE",
            "structural_lower_endpoint_mode": "QUALITY_AMBIGUOUS__OWNER_REVIEW_REQUIRED",
            "interior_mode_without_upper_pileup": "GOOD_STEADY_STATE_CANDIDATE",
        },
        "kfe_caveat": "Accepted standalone MATLAB-faithful contaminated-row KFE only; it does not resolve the corrected-2018 multi-province finite-box upper-b leakage or MATLAB-style pinning blocker.",
        "external_manifest": {"path": external_manifest["path"], "sha256": external_manifest["sha256"], "entry_count": external_manifest["entry_count"]},
    }
    run.write_json(compact_root / "summary.json", summary)
    run.write_json(compact_root / "marginals.json", marginals)
    for source, target in (
        (external_root / "source_identity.json", compact_root / "source_identity.json"),
        (external_root / "input_invariance.json", compact_root / "input_invariance_receipt.json"),
        (external_root / "final_call_ledger.json", compact_root / "call_ledger.json"),
        (external_root / "sealed_manifest_sha256.json", compact_root / "external_manifest.json"),
    ):
        run.write_json(target, read_json(source))
    run.write_json(compact_root / "point_receipts.json", points)
    with (compact_root / "points.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    seal(compact_root, "CH5_MP4C_K1_STANDALONE_HJB_RA_WAGE_3X3_COMPACT_V1")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("external_root", type=Path)
    parser.add_argument("compact_root", type=Path)
    args = parser.parse_args()
    return build(args.external_root, args.compact_root)


if __name__ == "__main__":
    raise SystemExit(main())
