"""Build compact evidence for the frozen finer illiquid-grid ladder."""
from __future__ import annotations

import argparse
import copy
import csv
import json
from pathlib import Path
from typing import Any

import numpy as np

from validators.multi_province.k1_household_asset_grid_precision_sensitivity import (
    finalize as accepted_finalize,
)
from validators.multi_province.k1_household_illiquid_grid_finer_precision_escalation import (
    run,
)
from validators.multi_province.k1_household_k_unit_asset_domain_stagewise.finalize import (
    classify_a,
    classify_b,
)
from validators.multi_province.k1_standalone_hjb_ra_wage_frontier_narrow_3x3.finalize import (
    seal,
)


signed_cdf_l1_distance = accepted_finalize.signed_cdf_l1_distance


def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def accepted_reference() -> dict[str, Any]:
    points = read_json(run.ACCEPTED_COMPACT / "point_receipts.json")
    selected = [point for point in points if point["specification"]["I"] == 20 and point["specification"]["J"] == 160]
    if len(selected) != 1:
        raise ValueError("accepted I20/J160 reference is not unique")
    point = copy.deepcopy(selected[0])
    point["phase"] = "REFERENCE"
    point["accepted_evidence_reused_without_runtime"] = True
    point["accepted_source_point_id"] = point["point_id"]
    point["point_id"] = "accepted_i020_j0160"
    return point


def upper_quantile_locations(
    grid_values: np.ndarray, marginal_mass: np.ndarray
) -> dict[str, float] | None:
    grid = np.asarray(grid_values, dtype=float)
    mass = np.asarray(marginal_mass, dtype=float)
    if (
        grid.ndim != 1
        or mass.shape != grid.shape
        or grid.size < 2
        or not np.isfinite(grid).all()
        or not np.isfinite(mass).all()
        or not np.all(np.diff(grid) > 0.0)
        or np.any(mass < 0.0)
        or float(np.sum(mass)) <= 0.0
    ):
        return None
    cdf = np.cumsum(mass)
    total = float(cdf[-1])
    return {
        name: float(grid[min(int(np.searchsorted(cdf, q * total, side="left")), grid.size - 1)])
        for name, q in (("p90", 0.90), ("p95", 0.95), ("p99", 0.99))
    }


def _raw_points(root: Path) -> list[dict[str, Any]]:
    points = [read_json(path) for path in sorted(Path(root).glob("finer_i*_j*_result.json"))]
    actual = [(point["specification"]["I"], point["specification"]["J"]) for point in points]
    expected = list(run.POINTS[: len(points)])
    if actual != expected:
        raise ValueError("finer point ladder is not an exact authorized prefix")
    return points


def _decorate(point: dict[str, Any]) -> dict[str, Any]:
    point = copy.deepcopy(point)
    kfe = point.get("kfe", {})
    if not kfe.get("completed"):
        point["a_domain_classification"] = None
        point["b_domain_classification"] = None
        return point
    spec = point["specification"]
    distribution = kfe["distribution"]
    a_grid = np.linspace(spec["amin"], spec["amax"], spec["J"])
    b_grid = np.linspace(spec["bmin"], spec["bmax"], spec["I"])
    a_mass = np.asarray(distribution["a_marginal_mass"], dtype=float)
    b_mass = np.asarray(distribution["b_marginal_mass"], dtype=float)
    distribution["upper_quantile_locations"] = {
        "a": upper_quantile_locations(a_grid, a_mass),
        "b": upper_quantile_locations(b_grid, b_mass),
    }
    point["a_domain_classification"] = classify_a(a_mass, distribution)
    point["b_domain_classification"] = classify_b(b_mass, distribution)
    return point


def _delta(old: Any, new: Any) -> dict[str, float]:
    old_value, new_value = float(old), float(new)
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
    old_ag = np.linspace(old_spec["amin"], old_spec["amax"], old_spec["J"])
    new_ag = np.linspace(new_spec["amin"], new_spec["amax"], new_spec["J"])
    old_bg = np.linspace(old_spec["bmin"], old_spec["bmax"], old_spec["I"])
    new_bg = np.linspace(new_spec["bmin"], new_spec["bmax"], new_spec["I"])
    old_am = np.asarray(old_dist["a_marginal_mass"], dtype=float)
    new_am = np.asarray(new_dist["a_marginal_mass"], dtype=float)
    old_bm = np.asarray(old_dist["b_marginal_mass"], dtype=float)
    new_bm = np.asarray(new_dist["b_marginal_mass"], dtype=float)
    old_q = old_dist.get("upper_quantile_locations", {})
    new_q = new_dist.get("upper_quantile_locations", {})
    quantile_movement: dict[str, Any] = {}
    for axis in ("a", "b"):
        if old_q.get(axis) is None or new_q.get(axis) is None:
            quantile_movement[axis] = None
        else:
            quantile_movement[axis] = {
                name: _delta(old_q[axis][name], new_q[axis][name])
                for name in ("p90", "p95", "p99")
            }
    return {
        "old_point_id": old["point_id"],
        "new_point_id": new["point_id"],
        "available": True,
        "grid_change": {
            "I": _delta(old_spec["I"], new_spec["I"]),
            "J": _delta(old_spec["J"], new_spec["J"]),
            "da": _delta(old_spec["da"], new_spec["da"]),
            "db": _delta(old_spec["db"], new_spec["db"]),
        },
        "aggregates": {
            name: _delta(old_agg[name], new_agg[name])
            for name in ("Ct", "Lt", "At", "Bt")
        },
        "modal_a": {"old": old_dist["modal_a"], "new": new_dist["modal_a"]},
        "modal_b": {"old": old_dist["modal_b"], "new": new_dist["modal_b"]},
        "endpoint_masses": {
            name: _delta(
                old_dist["boundary_mass_shares"][name],
                new_dist["boundary_mass_shares"][name],
            )
            for name in ("amin", "amax", "bmin", "bmax")
        },
        "a_marginal_signed_cdf_l1_width_normalized": signed_cdf_l1_distance(
            old_ag, old_am, new_ag, new_am
        ),
        "b_marginal_signed_cdf_l1_width_normalized": signed_cdf_l1_distance(
            old_bg, old_bm, new_bg, new_bm
        ),
        "a_marginal_direct_raw_mass_l1": None,
        "b_marginal_direct_raw_mass_l1": float(np.sum(np.abs(old_bm - new_bm))),
        "upper_quantile_movement": quantile_movement,
        "signed_mass_clipped": False,
        "signed_mass_renormalized": False,
    }


def comparisons(raw_root: Path) -> dict[str, Any]:
    points = [_decorate(accepted_reference()), *[_decorate(p) for p in _raw_points(raw_root)]]
    return {
        "schema": "CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_COMPARISON_V1",
        "method": {
            "mass": "raw signed marginal node mass",
            "cdf": "cumulative node mass, piecewise-linear interpolation on union of grid nodes",
            "distance": "integral absolute CDF difference divided by common support width",
            "clipping": False,
            "renormalization": False,
            "post_result_pass_threshold": False,
            "upper_quantiles": "first grid node at or above raw cumulative q*total; unavailable if any marginal node mass is negative",
        },
        "comparisons": [_comparison(old, new) for old, new in zip(points, points[1:])],
    }


def _marginal(point: dict[str, Any]) -> dict[str, Any]:
    spec = point["specification"]
    dist = point["kfe"]["distribution"]
    return {
        "point_id": point["point_id"],
        "I": spec["I"],
        "J": spec["J"],
        "a_grid": np.linspace(spec["amin"], spec["amax"], spec["J"]).tolist(),
        "a_marginal_mass": dist["a_marginal_mass"],
        "b_grid": np.linspace(spec["bmin"], spec["bmax"], spec["I"]).tolist(),
        "b_marginal_mass": dist["b_marginal_mass"],
        "upper_quantile_locations": dist.get("upper_quantile_locations"),
    }


def _row(point: dict[str, Any]) -> dict[str, Any]:
    spec, hjb, kfe = point["specification"], point["hjb"], point.get("kfe", {})
    dist, agg = kfe.get("distribution", {}), kfe.get("aggregates", {})
    boundary = dist.get("boundary_mass_shares", {})
    quantiles = dist.get("upper_quantile_locations", {}).get("a") if dist else None
    return {
        "phase": point["phase"],
        "point_id": point["point_id"],
        "I": spec["I"],
        "J": spec["J"],
        "da": spec["da"],
        "db": spec["db"],
        "hjb_classification": hjb["classification"],
        "iterations": hjb["iterations_used"],
        "final_statistic": hjb["final_convergence_statistic"],
        "maximum_A2max": hjb["maximum_a2max"],
        "first_illegal_iteration": hjb["first_illegal_iteration"],
        "kfe_ran": kfe.get("ran", False),
        "Ct": agg.get("Ct"),
        "Lt": agg.get("Lt"),
        "At": agg.get("At"),
        "Bt": agg.get("Bt"),
        "Bt_pos": dist.get("Bt_pos"),
        "Bt_neg": dist.get("Bt_neg"),
        "modal_a": json.dumps(dist.get("modal_a"), separators=(",", ":")),
        "modal_b": json.dumps(dist.get("modal_b"), separators=(",", ":")),
        "a_p90": quantiles.get("p90") if quantiles else None,
        "a_p95": quantiles.get("p95") if quantiles else None,
        "a_p99": quantiles.get("p99") if quantiles else None,
        "amin_mass": boundary.get("amin"),
        "amax_mass": boundary.get("amax"),
        "bmin_mass": boundary.get("bmin"),
        "bmax_mass": boundary.get("bmax"),
        "total_mass": dist.get("total_mass"),
        "kfe_residual": kfe.get("kfe", {}).get("raw_residual_inf"),
        "density_min": dist.get("density_min"),
        "negative_count": dist.get("density_negative_count"),
        "a_classification": point.get("a_domain_classification"),
        "b_classification": point.get("b_domain_classification"),
    }


def build(raw_root: Path, compact_root: Path, decision: str, rationale: str) -> int:
    raw_root, compact_root = Path(raw_root), Path(compact_root)
    execution = read_json(raw_root / "execution_complete.json")
    raw_points = _raw_points(raw_root)
    points = [_decorate(accepted_reference()), *[_decorate(point) for point in raw_points]]
    comparison = comparisons(raw_root)
    complete = bool(
        len(raw_points) == 3
        and all(
            point["hjb"]["classification"] == "HJB_CONVERGED"
            and point.get("kfe", {}).get("completed")
            for point in raw_points
        )
        and all(item["available"] for item in comparison["comparisons"])
    )
    if not complete:
        terminal = "ILLIQUID_GRID_FINER_PRECISION_NUMERICAL_FAILURE__NO_SCIENTIFIC_RETRY_AUTHORIZED"
        next_gate = "REVIEWER_NUMERICAL_FAILURE_ROUTE_DECISION"
        smallest = None
    elif decision == "stable":
        terminal = "ILLIQUID_GRID_PRECISION_PROVISIONALLY_STABILIZED_BY_J1280"
        next_gate = "BOUNDED_LIQUID_I_OR_CROSS_STATE_CONFIRMATION"
        smallest = "J1280_FOR_BOUNDED_CONFIRMATION_ONLY"
    else:
        terminal = "ILLIQUID_GRID_PRECISION_NOT_STABILIZED_BY_J1280__DOMAIN_OR_SCALE_REVIEW_REQUIRED"
        next_gate = "DOMAIN_OR_HOUSEHOLD_SCALE_REVIEW"
        smallest = None

    compact_root.mkdir(parents=True, exist_ok=False)
    external_manifest = seal(raw_root, "CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_EXTERNAL_V1")
    source = read_json(raw_root / "source_identity.json")
    source["actual_baseline"] = "3f4a87af4927643f2f80f407ed8b207d41fb8718"
    source["accepted_precision_candidate"] = "de4994c22303e30be9cd4c22c0a5c7f7a00db88a"
    input_receipt = read_json(raw_root / "input_invariance_receipt.json")
    ledger = read_json(raw_root / "final_call_ledger.json")
    ledger["accepted_reference_science_calls"] = {"hjb": 0, "kfe": 0}
    summary = {
        "schema": "CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_SUMMARY_V1",
        "terminal_classification": terminal,
        "descriptive_decision": decision,
        "descriptive_basis": rationale,
        "all_new_hjb_converged_and_kfe_valid": complete,
        "smallest_defensible_tested_J": smallest,
        "exactly_one_next_reviewer_gate": next_gate,
        "results_eligibility": False,
        "old_to_expanded_domain_interpretation": "DOMINANT_DOMAIN_RESPONSE_ESTABLISHED__CONVERGED_DISCRETIZATION_COMPONENT_DEPENDS_ON_FINER_PRECISION_DECISION",
        "kfe_caveat": "Accepted standalone contaminated-row KFE only; raw signed density is not clipped or smoothed; corrected-2018 multi-province finite-box/pinning remains separate.",
        "execution_status": execution["status"],
    }
    run.accepted.coarse.write_json(compact_root / "source_identity.json", source)
    run.accepted.coarse.write_json(compact_root / "input_invariance_receipt.json", input_receipt)
    run.accepted.coarse.write_json(compact_root / "point_receipts.json", points)
    run.accepted.coarse.write_json(
        compact_root / "marginals.json",
        [_marginal(point) for point in points if point.get("kfe", {}).get("completed")],
    )
    run.accepted.coarse.write_json(compact_root / "precision_comparison.json", comparison)
    run.accepted.coarse.write_json(compact_root / "call_ledger.json", ledger)
    run.accepted.coarse.write_json(compact_root / "external_manifest.json", external_manifest)
    run.accepted.coarse.write_json(compact_root / "summary.json", summary)
    rows = [_row(point) for point in points]
    with (compact_root / "precision_points.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    seal(compact_root, "CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_COMPACT_V1")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    preview = subparsers.add_parser("preview")
    preview.add_argument("raw_root", type=Path)
    finish = subparsers.add_parser("build")
    finish.add_argument("raw_root", type=Path)
    finish.add_argument("compact_root", type=Path)
    finish.add_argument("decision", choices=("stable", "unstable"))
    finish.add_argument("rationale")
    args = parser.parse_args()
    if args.command == "preview":
        print(json.dumps(comparisons(args.raw_root), indent=2))
        return 0
    return build(args.raw_root, args.compact_root, args.decision, args.rationale)


if __name__ == "__main__":
    raise SystemExit(main())
