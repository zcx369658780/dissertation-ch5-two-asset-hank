"""Offline classification and compact-evidence builder for the refinement scan."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

import numpy as np

from validators.multi_province.k1_standalone_hjb_ra_wage_3x3 import run as coarse
from . import run


LABELS = {
    "LOWER_A_BOUNDARY_DOMINATED",
    "INTERIOR_A_DISTRIBUTION_CANDIDATE",
    "UPPER_A_BOUNDARY_PILEUP",
    "TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED",
}


def descriptive_distribution_label(a_grid: np.ndarray, a_marginal_mass: np.ndarray) -> str:
    """Classify by exact modal/dominance relations, not a fitted percentage cutoff."""
    a = np.asarray(a_grid, dtype=float)
    mass = np.asarray(a_marginal_mass, dtype=float)
    if a.shape != mass.shape or a.ndim != 1 or not np.isfinite(mass).all():
        return "TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED"
    maximum = float(np.max(mass))
    modes = set(int(index) for index in np.flatnonzero(mass == maximum))
    interior_mass = float(np.sum(mass[1:-1]))
    top_two = set(int(index) for index in np.argsort(-mass, kind="stable")[:2])
    if a.size - 1 in modes:
        return "UPPER_A_BOUNDARY_PILEUP"
    if modes == {0} and float(mass[0]) > interior_mass:
        return "LOWER_A_BOUNDARY_DOMINATED"
    if modes and all(0 < index < a.size - 1 for index in modes) and all(
        0 < index < a.size - 1 for index in top_two
    ):
        if float(mass[0]) < maximum and float(mass[-1]) < maximum:
            return "INTERIOR_A_DISTRIBUTION_CANDIDATE"
    return "TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED"


def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def seal(directory: Path, schema: str) -> dict[str, Any]:
    directory = Path(directory)
    target = directory / "sealed_manifest_sha256.json"
    entries = []
    for path in sorted(item for item in directory.rglob("*") if item.is_file() and item != target):
        entries.append({
            "path": path.relative_to(directory).as_posix(), "bytes": path.stat().st_size,
            "sha256": coarse.file_sha256(path),
        })
    manifest = {
        "schema": schema, "entries": entries, "entry_count": len(entries),
        "bytes_excluding_manifest": sum(item["bytes"] for item in entries),
    }
    coarse.write_json(target, manifest)
    return {"path": str(target.resolve()), "sha256": coarse.file_sha256(target), **manifest}


def _connected_interior_ra(rows: list[dict[str, Any]]) -> list[float]:
    values = []
    for ra in (0.065, 0.0725, 0.08):
        members = [row for row in rows if row["ra"] == ra]
        if len(members) == 3 and all(
            row["distribution_label"] == "INTERIOR_A_DISTRIBUTION_CANDIDATE"
            for row in members
        ):
            values.append(ra)
    return values


def build(external_root: Path, compact_root: Path) -> int:
    external_root = Path(external_root); compact_root = Path(compact_root)
    if not (external_root / "execution_complete.json").is_file():
        raise ValueError("external execution is incomplete")
    if (external_root / "sealed_manifest_sha256.json").exists():
        raise FileExistsError("external evidence is already sealed")
    compact_root.mkdir(parents=True, exist_ok=False)
    external_manifest = seal(
        external_root, "CH5_MP4C_K1_STANDALONE_HJB_RA_TRANSITION_REFINEMENT_3X3_EXTERNAL_V1"
    )
    point_paths = sorted(external_root.glob("p*_result.json"))
    if len(point_paths) != 9:
        raise ValueError("expected exactly nine completed point receipts")
    points = [read_json(path) for path in point_paths]
    rows: list[dict[str, Any]] = []
    marginals = []
    a_grid = np.linspace(0.0, 10.0, 20)
    b_grid = np.linspace(-2.0, 5.0, 20)
    for point in points:
        hjb = point["hjb"]
        label = None; aggregates: dict[str, Any] = {}; distribution: dict[str, Any] = {}
        if hjb["classification"] == "HJB_CONVERGED" and point["kfe"].get("completed", True):
            aggregates = point["kfe"]["aggregates"]
            distribution = point["kfe"]["distribution"]
            label = descriptive_distribution_label(a_grid, distribution["a_marginal_mass"])
            marginals.append({
                "point_id": point["point_id"], "r_a": point["r_a"], "wage": point["wage"],
                "a_grid": a_grid.tolist(), "a_marginal_mass": distribution["a_marginal_mass"],
                "b_grid": b_grid.tolist(), "b_marginal_mass": distribution["b_marginal_mass"],
            })
        point["distribution_label"] = label
        rows.append({
            "point_index": point["point_index"], "point_id": point["point_id"],
            "rb": point["r_b"], "ra": point["r_a"], "wage": point["wage"],
            "hjb_classification": hjb["classification"], "iterations": hjb["iterations_used"],
            "final_statistic": hjb["final_convergence_statistic"],
            "maximum_A2max": hjb["maximum_a2max"],
            "first_illegal_iteration": hjb["first_illegal_iteration"],
            "kfe_ran": point["kfe"]["ran"], "distribution_label": label,
            "Ct": aggregates.get("Ct"), "Lt": aggregates.get("Lt"),
            "At": aggregates.get("At"), "Bt": aggregates.get("Bt"),
            "Bt_pos": distribution.get("Bt_pos"), "Bt_neg": distribution.get("Bt_neg"),
            "amin_mass": distribution.get("boundary_mass_shares", {}).get("amin"),
            "amax_mass": distribution.get("boundary_mass_shares", {}).get("amax"),
            "bmin_mass": distribution.get("boundary_mass_shares", {}).get("bmin"),
            "bmax_mass": distribution.get("boundary_mass_shares", {}).get("bmax"),
            "interior_a_mass": distribution.get("interior_a_mass"),
            "modal_a": json.dumps(distribution.get("modal_a"), separators=(",", ":")),
            "modal_b": json.dumps(distribution.get("modal_b"), separators=(",", ":")),
            "top_3_a_bins": json.dumps(distribution.get("top_3_a_bins"), separators=(",", ":")),
            "amax_to_adjacent_ratio": distribution.get("amax_to_adjacent_interior_ratio"),
            "total_mass": distribution.get("total_mass"),
            "density_min": distribution.get("density_min"),
            "density_negative_count": distribution.get("density_negative_count"),
            "kfe_raw_residual_inf": point["kfe"].get("kfe", {}).get("raw_residual_inf"),
        })

    interior_ra = _connected_interior_ra(rows)
    interior_rows = [
        row for row in rows
        if row["distribution_label"] == "INTERIOR_A_DISTRIBUTION_CANDIDATE"
    ]
    ranges = None
    if interior_rows:
        ranges = {
            name: [min(float(row[name]) for row in interior_rows), max(float(row[name]) for row in interior_rows)]
            for name in ("Ct", "Lt", "At", "Bt")
        }
    if len(interior_ra) >= 2:
        next_gate = {
            "name": "OWNER_REVIEW_PROVISIONAL_STANDALONE_RA_HEALTH_BAND_FREEZE",
            "run_now": False,
            "candidate_ra_values": interior_ra,
            "reason": "All three wage points are interior candidates at these connected preregistered ra values.",
        }
    elif interior_rows:
        next_gate = {
            "name": "OWNER_REVIEW_NARROWER_RA_REFINEMENT_AROUND_WAGE_DEPENDENT_FRONTIER",
            "run_now": False,
            "recommended_grid": {"rb": [0.02], "ra": [0.06, 0.0675, 0.07], "wage": [0.8, 1.05, 1.3]},
            "reason": "Interior candidates exist but do not form a wage-robust nondegenerate ra band; this one grid brackets both the .055-to-.065 lower/interior transition and the .065-to-.0725 wage-dependent upper frontier.",
        }
    else:
        next_gate = {
            "name": "OWNER_REVIEW_UNRESOLVED_STANDALONE_RA_TRANSITION",
            "run_now": False,
            "reason": "No interior candidate was identified on the preregistered refinement grid.",
        }
    summary = {
        "terminal_classification": "ALL_HJB_LEGAL_CONVERGED__INTERIOR_ONLY_AT_RA_0P065_HIGHER_WAGES__WAGE_DEPENDENT_TRANSITION__RA_0P08_UPPER_BOUNDARY",
        "results_eligibility": False,
        "grid": {"rb": [0.02], "ra": [0.065, 0.0725, 0.08], "wage": [0.8, 1.05, 1.3]},
        "counts": {
            "HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX": sum(row["hjb_classification"] == "HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX" for row in rows),
            "HJB_NOT_CONVERGED": sum(row["hjb_classification"] == "HJB_NOT_CONVERGED" for row in rows),
            "HJB_CONVERGED": sum(row["hjb_classification"] == "HJB_CONVERGED" for row in rows),
            **{label: sum(row["distribution_label"] == label for row in rows) for label in sorted(LABELS)},
        },
        "wage_robust_connected_interior_ra_values": interior_ra,
        "connected_interior_candidate_band_exists": bool(interior_ra),
        "interior_candidate_aggregate_ranges": ranges,
        "recommended_next_gate": next_gate,
        "classification_semantics": {
            "post_result_numeric_cutoff": False,
            "basis": "exact modal location and top-two-bin endpoint-versus-interior ordering with full raw marginals retained",
        },
        "kfe_caveat": "Accepted standalone MATLAB-faithful contaminated-row KFE only; corrected-2018 multi-province finite-box upper-b leakage and MATLAB-style pinning remain unresolved.",
        "external_manifest": {
            "path": external_manifest["path"], "sha256": external_manifest["sha256"],
            "entry_count": external_manifest["entry_count"],
        },
    }
    coarse.write_json(compact_root / "summary.json", summary)
    coarse.write_json(compact_root / "marginals.json", marginals)
    for source, target in (
        (external_root / "source_identity.json", compact_root / "source_identity.json"),
        (external_root / "input_invariance.json", compact_root / "input_invariance_receipt.json"),
        (external_root / "final_call_ledger.json", compact_root / "call_ledger.json"),
        (external_root / "sealed_manifest_sha256.json", compact_root / "external_manifest.json"),
    ):
        coarse.write_json(target, read_json(source))
    coarse.write_json(compact_root / "point_receipts.json", points)
    with (compact_root / "points.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    seal(compact_root, "CH5_MP4C_K1_STANDALONE_HJB_RA_TRANSITION_REFINEMENT_3X3_COMPACT_V1")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("external_root", type=Path)
    parser.add_argument("compact_root", type=Path)
    args = parser.parse_args()
    return build(args.external_root, args.compact_root)


if __name__ == "__main__":
    raise SystemExit(main())
