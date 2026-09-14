"""Build compact evidence for the frozen household asset-grid precision ladder."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

import numpy as np

from validators.multi_province.k1_household_asset_grid_precision_sensitivity import run
from validators.multi_province.k1_household_k_unit_asset_domain_stagewise.finalize import (
    classify_a,
    classify_b,
)
from validators.multi_province.k1_standalone_hjb_ra_wage_3x3 import run as coarse
from validators.multi_province.k1_standalone_hjb_ra_wage_frontier_narrow_3x3.finalize import (
    seal,
)


def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def signed_cdf_l1_distance(
    first_grid: np.ndarray,
    first_mass: np.ndarray,
    second_grid: np.ndarray,
    second_mass: np.ndarray,
) -> float:
    """Width-normalized integral distance between raw signed node-mass CDFs.

    Cumulative node masses are linearly interpolated on the union of grid nodes.
    Input masses are neither clipped nor renormalized.
    """
    x1 = np.asarray(first_grid, dtype=float)
    m1 = np.asarray(first_mass, dtype=float)
    x2 = np.asarray(second_grid, dtype=float)
    m2 = np.asarray(second_mass, dtype=float)
    for grid, mass in ((x1, m1), (x2, m2)):
        if (
            grid.ndim != 1
            or mass.ndim != 1
            or grid.size != mass.size
            or grid.size < 2
            or not np.isfinite(grid).all()
            or not np.isfinite(mass).all()
            or not np.all(np.diff(grid) > 0.0)
        ):
            raise ValueError("grid and raw signed mass must be finite aligned vectors")
    if x1[0] != x2[0] or x1[-1] != x2[-1]:
        raise ValueError("CDF comparison requires a common support")
    common = np.union1d(x1, x2)
    cdf1 = np.interp(common, x1, np.cumsum(m1))
    cdf2 = np.interp(common, x2, np.cumsum(m2))
    width = float(common[-1] - common[0])
    return float(np.trapezoid(np.abs(cdf1 - cdf2), common) / width)


def _top_bins(grid: np.ndarray, mass: np.ndarray) -> list[dict[str, Any]]:
    indices = np.argsort(-np.asarray(mass), kind="stable")[:3]
    return [
        {"index": int(i), "grid_value": float(grid[i]), "mass": float(mass[i])}
        for i in indices
    ]


def _accepted_reference() -> dict[str, Any]:
    point = run._accepted_central_point()
    distribution = point["kfe"]["distribution"]
    return {
        "point_id": "accepted_i020_j020",
        "phase": "REFERENCE",
        "specification": {
            "phase": "REFERENCE",
            "phase_point_index": 0,
            "I": 20,
            "J": 20,
            "Nz": 2,
            "amin": 0.0,
            "amax": 100.0,
            "bmin": -2.0,
            "bmax": 20.0,
            "da": 100.0 / 19.0,
            "db": 22.0 / 19.0,
            "rb": 0.02,
            "ra": 0.0675,
            "wage": 15.5,
            "h": 1.0,
        },
        "fresh_initialization": point["fresh_initialization"],
        "hjb": point["hjb"],
        "kfe": point["kfe"],
        "a_domain_classification": point["a_domain_classification"],
        "b_domain_classification": point["b_domain_classification"],
        "accepted_evidence_reused_without_runtime": True,
        "accepted_source_point_id": point["point_id"],
        "accepted_distribution_total_mass": distribution["total_mass"],
    }


def _raw_points(root: Path, phase: str) -> list[dict[str, Any]]:
    points = [read_json(path) for path in sorted(Path(root).glob(f"{phase.lower()}_i*_j*_result.json"))]
    if len(points) != len(run.PHASE_POINTS[phase]):
        raise ValueError(f"expected exactly {len(run.PHASE_POINTS[phase])} {phase} point receipts")
    actual = [(p["specification"]["I"], p["specification"]["J"]) for p in points]
    if actual != list(run.PHASE_POINTS[phase]):
        raise ValueError(f"{phase} point ladder is not exact")
    return points


def _decorate(point: dict[str, Any]) -> dict[str, Any]:
    if not point.get("kfe", {}).get("ran") or not point["kfe"].get("completed"):
        point["a_domain_classification"] = None
        point["b_domain_classification"] = None
        return point
    spec = point["specification"]
    distribution = point["kfe"]["distribution"]
    a_grid = np.linspace(spec["amin"], spec["amax"], spec["J"])
    b_grid = np.linspace(spec["bmin"], spec["bmax"], spec["I"])
    a_mass = np.asarray(distribution["a_marginal_mass"], dtype=float)
    b_mass = np.asarray(distribution["b_marginal_mass"], dtype=float)
    distribution["top_3_a_bins"] = _top_bins(a_grid, a_mass)
    distribution["top_3_b_bins"] = _top_bins(b_grid, b_mass)
    distribution["interior_a_mass"] = float(np.sum(a_mass[1:-1]))
    distribution["interior_b_mass"] = float(np.sum(b_mass[1:-1]))
    point["a_domain_classification"] = classify_a(a_mass, distribution)
    point["b_domain_classification"] = classify_b(b_mass, distribution)
    return point


def _marginal(point: dict[str, Any]) -> dict[str, Any]:
    spec = point["specification"]
    distribution = point["kfe"]["distribution"]
    return {
        "point_id": point["point_id"],
        "phase": point["phase"],
        "I": spec["I"],
        "J": spec["J"],
        "a_grid": np.linspace(spec["amin"], spec["amax"], spec["J"]).tolist(),
        "a_marginal_mass": distribution["a_marginal_mass"],
        "b_grid": np.linspace(spec["bmin"], spec["bmax"], spec["I"]).tolist(),
        "b_marginal_mass": distribution["b_marginal_mass"],
    }


def _delta(old: Any, new: Any) -> dict[str, float]:
    old_value = float(old)
    new_value = float(new)
    return {"old": old_value, "new": new_value, "delta": new_value - old_value}


def _comparison(old: dict[str, Any], new: dict[str, Any]) -> dict[str, Any]:
    if not old.get("kfe", {}).get("completed") or not new.get("kfe", {}).get("completed"):
        return {
            "old_point_id": old["point_id"],
            "new_point_id": new["point_id"],
            "available": False,
            "reason": "KFE_NOT_COMPLETED_FOR_BOTH_POINTS",
        }
    old_spec, new_spec = old["specification"], new["specification"]
    old_dist, new_dist = old["kfe"]["distribution"], new["kfe"]["distribution"]
    old_agg, new_agg = old["kfe"]["aggregates"], new["kfe"]["aggregates"]
    old_a = np.asarray(old_dist["a_marginal_mass"], dtype=float)
    new_a = np.asarray(new_dist["a_marginal_mass"], dtype=float)
    old_b = np.asarray(old_dist["b_marginal_mass"], dtype=float)
    new_b = np.asarray(new_dist["b_marginal_mass"], dtype=float)
    old_ag = np.linspace(old_spec["amin"], old_spec["amax"], old_spec["J"])
    new_ag = np.linspace(new_spec["amin"], new_spec["amax"], new_spec["J"])
    old_bg = np.linspace(old_spec["bmin"], old_spec["bmax"], old_spec["I"])
    new_bg = np.linspace(new_spec["bmin"], new_spec["bmax"], new_spec["I"])
    result = {
        "old_point_id": old["point_id"],
        "new_point_id": new["point_id"],
        "available": True,
        "grid_change": {
            "I": _delta(old_spec["I"], new_spec["I"]),
            "J": _delta(old_spec["J"], new_spec["J"]),
            "da": _delta(old_spec["da"], new_spec["da"]),
            "db": _delta(old_spec["db"], new_spec["db"]),
        },
        "aggregates": {name: _delta(old_agg[name], new_agg[name]) for name in ("Ct", "Lt", "At", "Bt")},
        "modal_a": {"old": old_dist["modal_a"], "new": new_dist["modal_a"]},
        "modal_b": {"old": old_dist["modal_b"], "new": new_dist["modal_b"]},
        "endpoint_masses": {
            name: _delta(old_dist["boundary_mass_shares"][name], new_dist["boundary_mass_shares"][name])
            for name in ("amin", "amax", "bmin", "bmax")
        },
        "a_marginal_signed_cdf_l1_width_normalized": signed_cdf_l1_distance(old_ag, old_a, new_ag, new_a),
        "b_marginal_signed_cdf_l1_width_normalized": signed_cdf_l1_distance(old_bg, old_b, new_bg, new_b),
        "signed_mass_clipped": False,
        "signed_mass_renormalized": False,
    }
    result["a_marginal_direct_raw_mass_l1"] = float(np.sum(np.abs(old_a - new_a))) if np.array_equal(old_ag, new_ag) else None
    result["b_marginal_direct_raw_mass_l1"] = float(np.sum(np.abs(old_b - new_b))) if np.array_equal(old_bg, new_bg) else None
    return result


def comparisons(p1_root: Path, p2_root: Path | None = None) -> dict[str, Any]:
    reference = _decorate(_accepted_reference())
    p1 = [_decorate(point) for point in _raw_points(p1_root, "P1")]
    p1_sequence = [reference, *p1]
    output = {
        "schema": "CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_COMPARISON_V1",
        "method": {
            "mass": "raw signed marginal node mass",
            "cdf": "cumulative node mass, piecewise-linear interpolation on union of grid nodes",
            "distance": "integral absolute CDF difference divided by common support width",
            "clipping": False,
            "renormalization": False,
            "post_result_pass_threshold": False,
        },
        "P1": [_comparison(old, new) for old, new in zip(p1_sequence, p1_sequence[1:])],
        "P2": None,
    }
    if p2_root is not None:
        p2 = [_decorate(point) for point in _raw_points(p2_root, "P2")]
        p2_sequence = [p1[-1], *p2]
        output["P2"] = [_comparison(old, new) for old, new in zip(p2_sequence, p2_sequence[1:])]
    return output


def write_p1_trigger(root: Path, trigger: bool, rationale: str) -> int:
    root = Path(root)
    if (root / "stage_trigger_receipt.json").exists():
        raise FileExistsError("P1 stage trigger receipt already exists")
    phase_comparison = comparisons(root)["P1"]
    valid = all(item["available"] for item in phase_comparison)
    if trigger and not valid:
        raise ValueError("P2 cannot trigger unless every P1 comparison is available")
    classification = (
        "ILLIQUID_GRID_PRECISION_PROVISIONALLY_STABILIZED"
        if trigger
        else (
            "ILLIQUID_GRID_PRECISION_NOT_STABILIZED"
            if valid
            else "ILLIQUID_GRID_PRECISION_UNRESOLVED__KFE_EVIDENCE_UNAVAILABLE"
        )
    )
    receipt = {
        "schema": "CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_P1_TRIGGER_V1",
        "trigger": bool(trigger),
        "p1_classification": classification,
        "descriptive_basis": rationale,
        "all_p1_pairwise_comparisons_available": valid,
        "post_result_numeric_threshold_introduced": False,
        "p2_authorized": bool(trigger),
        "p2_runtime_at_receipt": {"hjb": 0, "kfe": 0},
    }
    coarse.write_json(root / "stage_trigger_receipt.json", receipt)
    return 0


def _row(point: dict[str, Any]) -> dict[str, Any]:
    spec, hjb, kfe = point["specification"], point["hjb"], point.get("kfe", {})
    dist, agg = kfe.get("distribution", {}), kfe.get("aggregates", {})
    boundary = dist.get("boundary_mass_shares", {})
    return {
        "phase": point["phase"], "point_id": point["point_id"], "I": spec["I"], "J": spec["J"],
        "da": spec["da"], "db": spec["db"], "rb": spec["rb"], "ra": spec["ra"], "wage": spec["wage"],
        "hjb_classification": hjb["classification"], "iterations": hjb["iterations_used"],
        "final_statistic": hjb["final_convergence_statistic"], "maximum_A2max": hjb["maximum_a2max"],
        "first_illegal_iteration": hjb["first_illegal_iteration"], "kfe_ran": kfe.get("ran", False),
        "Ct": agg.get("Ct"), "Lt": agg.get("Lt"), "At": agg.get("At"), "Bt": agg.get("Bt"),
        "Bt_pos": dist.get("Bt_pos"), "Bt_neg": dist.get("Bt_neg"),
        "modal_a": json.dumps(dist.get("modal_a"), separators=(",", ":")),
        "modal_b": json.dumps(dist.get("modal_b"), separators=(",", ":")),
        "amin_mass": boundary.get("amin"), "amax_mass": boundary.get("amax"),
        "bmin_mass": boundary.get("bmin"), "bmax_mass": boundary.get("bmax"),
        "total_mass": dist.get("total_mass"), "kfe_residual": kfe.get("kfe", {}).get("raw_residual_inf"),
        "density_min": dist.get("density_min"), "negative_count": dist.get("density_negative_count"),
        "a_classification": point.get("a_domain_classification"), "b_classification": point.get("b_domain_classification"),
    }


def _aggregate_ledger(p1_root: Path, p2_root: Path | None) -> dict[str, Any]:
    p1 = read_json(Path(p1_root) / "final_call_ledger.json")
    p2 = read_json(Path(p2_root) / "final_call_ledger.json") if p2_root is not None else None
    return {
        "schema": "CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_AGGREGATE_LEDGER_V1",
        "accepted_reference_science_calls": {"hjb": 0, "kfe": 0},
        "P1": p1,
        "P2": p2,
        "totals": {
            "hjb_calls_started": p1["hjb_calls_started"] + (p2["hjb_calls_started"] if p2 else 0),
            "hjb_calls_completed": p1["hjb_calls_completed"] + (p2["hjb_calls_completed"] if p2 else 0),
            "kfe_calls_started": p1["kfe_calls_started"] + (p2["kfe_calls_started"] if p2 else 0),
            "kfe_calls_completed": p1["kfe_calls_completed"] + (p2["kfe_calls_completed"] if p2 else 0),
            "scientific_retries": 0, "engineering_retries": 0, "matlab_runtime_calls": 0,
            "global_outer_turns": 0, "firm_runtime_calls": 0, "results_writes": 0,
        },
    }


def build(p1_root: Path, compact_root: Path, p2_root: Path | None, p2_stable: bool | None) -> int:
    p1_root, compact_root = Path(p1_root), Path(compact_root)
    trigger = read_json(p1_root / "stage_trigger_receipt.json")
    if trigger["trigger"] != (p2_root is not None):
        raise ValueError("P2 root presence must exactly match the frozen P1 trigger")
    if trigger["trigger"] != (p2_stable is not None):
        raise ValueError("P2 stability decision must exist exactly when P2 ran")
    if not (p1_root / "execution_complete.json").is_file() or (p2_root is not None and not (Path(p2_root) / "execution_complete.json").is_file()):
        raise ValueError("phase execution is incomplete")
    compact_root.mkdir(parents=True, exist_ok=False)

    p1_manifest = seal(p1_root, "CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_P1_EXTERNAL_V1")
    p2_manifest = seal(Path(p2_root), "CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_P2_EXTERNAL_V1") if p2_root is not None else None
    reference = _decorate(_accepted_reference())
    p1 = [_decorate(point) for point in _raw_points(p1_root, "P1")]
    p2 = [_decorate(point) for point in _raw_points(Path(p2_root), "P2")] if p2_root is not None else []
    points = [reference, *p1, *p2]
    comparison = comparisons(p1_root, Path(p2_root) if p2_root is not None else None)
    all_valid = all(point["hjb"]["classification"] == "HJB_CONVERGED" and point.get("kfe", {}).get("completed") for point in points)

    if not trigger["trigger"] and not trigger["all_p1_pairwise_comparisons_available"]:
        terminal = "P1_KFE_EVIDENCE_UNAVAILABLE__NO_SCIENTIFIC_RETRY_AUTHORIZED"
        next_gate = "REVIEWER_ROUTE_REPAIR_DECISION"
        recommended_grid = "UNRESOLVED__NO_MINIMUM_NUMERICALLY_DEFENSIBLE_GRID_YET"
    elif not trigger["trigger"]:
        terminal = "ILLIQUID_GRID_PRECISION_NOT_STABILIZED"
        next_gate = "FINER_PRECISION_ESCALATION"
        recommended_grid = "UNRESOLVED__NO_MINIMUM_NUMERICALLY_DEFENSIBLE_GRID_YET"
    elif not p2_stable:
        terminal = "LIQUID_GRID_PRECISION_NOT_STABILIZED"
        next_gate = "FINER_PRECISION_ESCALATION"
        recommended_grid = "UNRESOLVED__NO_MINIMUM_NUMERICALLY_DEFENSIBLE_GRID_YET"
    elif all_valid:
        terminal = "ASSET_GRID_PRECISION_PROVISIONALLY_STABILIZED_AT_REPRESENTATIVE_STATE"
        next_gate = "BOUNDED_MULTI_STATE_CONFIRMATION"
        recommended_grid = "I=80,J=160_FOR_BOUNDED_MULTI_STATE_CONFIRMATION_ONLY"
    else:
        terminal = "ASSET_GRID_PRECISION_OR_KFE_VALIDITY_UNRESOLVED"
        next_gate = "UNRESOLVED_RECALIBRATION"
        recommended_grid = "UNRESOLVED"

    source = read_json(p1_root / "source_identity.json")
    source["p2_source_identity"] = read_json(Path(p2_root) / "source_identity.json") if p2_root is not None else None
    input_receipt = {
        "schema": "CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_INPUT_INVARIANCE_V1",
        "frozen_representative_state": {"rb": 0.02, "ra": 0.0675, "wage": 15.5, "amin": 0.0, "amax": 100.0, "bmin": -2.0, "bmax": 20.0, "h": 1.0},
        "accepted_reference_reused_without_runtime": True,
        "P1": read_json(p1_root / "input_invariance.json"),
        "P2": read_json(Path(p2_root) / "input_invariance.json") if p2_root is not None else None,
        "no_warm_start": True,
    }
    summary = {
        "schema": "CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SUMMARY_V1",
        "terminal_classification": terminal,
        "p1_classification": trigger["p1_classification"],
        "p2_trigger": trigger["trigger"],
        "p2_stable": p2_stable,
        "all_hjb_converged_and_kfe_completed": all_valid,
        "recommended_minimum_next_grid": recommended_grid,
        "exactly_one_next_reviewer_gate": next_gate,
        "results_eligibility": False,
        "domain_response_conclusion": "OLD_TO_EXPANDED_DOMAIN_AT_JUMP_IS_PRIMARILY_DOMAIN_RESPONSE_BUT_GRID_COMPONENT_REMAINS_RESOLVED_ONLY_BY_THIS_PRECISION_SEQUENCE",
        "kfe_caveat": "Accepted standalone contaminated-row KFE only; raw signed density is not clipped; corrected-2018 multi-province finite-box/pinning remains separate.",
    }

    coarse.write_json(compact_root / "source_identity.json", source)
    coarse.write_json(compact_root / "input_invariance_receipt.json", input_receipt)
    coarse.write_json(compact_root / "point_receipts.json", points)
    coarse.write_json(compact_root / "marginals.json", [_marginal(point) for point in points if point.get("kfe", {}).get("completed")])
    coarse.write_json(compact_root / "precision_comparison.json", comparison)
    coarse.write_json(compact_root / "stage_trigger_receipt.json", trigger)
    coarse.write_json(compact_root / "call_ledger.json", _aggregate_ledger(p1_root, Path(p2_root) if p2_root is not None else None))
    coarse.write_json(compact_root / "external_manifests.json", {"P1": p1_manifest, "P2": p2_manifest})
    coarse.write_json(compact_root / "summary.json", summary)
    rows = [_row(point) for point in points]
    with (compact_root / "precision_points.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    seal(compact_root, "CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_COMPACT_V1")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    assess = subparsers.add_parser("assess-p1")
    assess.add_argument("p1_root", type=Path)
    assess.add_argument("decision", choices=("stable", "unstable"))
    assess.add_argument("rationale")
    preview = subparsers.add_parser("preview")
    preview.add_argument("p1_root", type=Path)
    preview.add_argument("p2_root", type=Path, nargs="?")
    finish = subparsers.add_parser("build")
    finish.add_argument("p1_root", type=Path)
    finish.add_argument("compact_root", type=Path)
    finish.add_argument("--p2-root", type=Path)
    finish.add_argument("--p2-decision", choices=("stable", "unstable"))
    args = parser.parse_args()
    if args.command == "assess-p1":
        return write_p1_trigger(args.p1_root, args.decision == "stable", args.rationale)
    if args.command == "preview":
        print(json.dumps(comparisons(args.p1_root, args.p2_root), indent=2))
        return 0
    return build(args.p1_root, args.compact_root, args.p2_root, None if args.p2_decision is None else args.p2_decision == "stable")


if __name__ == "__main__":
    raise SystemExit(main())
