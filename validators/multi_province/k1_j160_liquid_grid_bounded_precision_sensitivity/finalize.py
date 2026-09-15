"""Offline finalizer for the fixed-support I20/I40/I80 liquid-grid ladder."""
from __future__ import annotations

import argparse
import copy
import csv
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

import numpy as np

from validators.multi_province.k1_j160_liquid_grid_bounded_precision_sensitivity import run


TERMINALS = {
    "J160_LIQUID_GRID_PRECISION_PROVISIONALLY_STABILIZED",
    "J160_LIQUID_GRID_PRECISION_NOT_STABILIZED",
    "J160_LIQUID_GRID_PRECISION_UNRESOLVED__I40_HJB_INVALID_OPERATOR",
}


def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_decision(value: str) -> bool:
    if value not in TERMINALS:
        raise ValueError("decision is outside the preregistered terminal set")
    return True


def same_support_cdf_distance(first_grid: Any, first_mass: Any, second_grid: Any, second_mass: Any) -> float:
    x1, m1 = np.asarray(first_grid, dtype=float), np.asarray(first_mass, dtype=float)
    x2, m2 = np.asarray(second_grid, dtype=float), np.asarray(second_mass, dtype=float)
    for grid, mass in ((x1, m1), (x2, m2)):
        if grid.ndim != 1 or mass.shape != grid.shape or grid.size < 2 or not np.isfinite(grid).all() or not np.isfinite(mass).all() or not np.all(np.diff(grid) > 0):
            raise ValueError("grid and raw signed mass must be finite aligned increasing vectors")
    if x1[0] != x2[0] or x1[-1] != x2[-1]:
        raise ValueError("grid-precision CDF comparison requires the same support")
    common = np.union1d(x1, x2)
    return float(np.trapezoid(np.abs(np.interp(common, x1, np.cumsum(m1)) - np.interp(common, x2, np.cumsum(m2))), common) / (common[-1] - common[0]))


def accepted_reference() -> dict[str, Any]:
    points = read_json(run.ACCEPTED_POINTS)
    selected = [point for point in points if point["specification"]["I"] == 20 and point["specification"]["J"] == 160]
    if len(selected) != 1:
        raise ValueError("accepted I20/J160 reference is not unique")
    point = copy.deepcopy(selected[0])
    point["point_id"] = "accepted_i020_j160"
    point["accepted_evidence_reused_without_runtime"] = True
    return point


def _top_bins(grid: np.ndarray, mass: np.ndarray) -> list[dict[str, Any]]:
    return [{"index": int(index), "grid_value": float(grid[index]), "mass": float(mass[index])}
            for index in np.argsort(-mass, kind="stable")[:3]]


def decorate(point: dict[str, Any]) -> dict[str, Any]:
    point = copy.deepcopy(point)
    if not point.get("kfe", {}).get("completed", point.get("kfe", {}).get("ran", False)):
        point["kfe_valid_nonpathological"] = False
        return point
    spec, distribution = point["specification"], point["kfe"]["distribution"]
    a_grid, b_grid = np.linspace(0.0, 100.0, 160), np.linspace(-2.0, 20.0, spec["I"])
    a_mass, b_mass = np.asarray(distribution["a_marginal_mass"]), np.asarray(distribution["b_marginal_mass"])
    distribution["top_3_a_bins"] = _top_bins(a_grid, a_mass)
    distribution["top_3_b_bins"] = _top_bins(b_grid, b_mass)
    distribution["deterministic_quantiles"] = {}
    for name, grid, mass in (("a", a_grid, a_mass), ("b", b_grid, b_mass)):
        if np.all(mass >= 0) and float(np.sum(mass)) > 0:
            cumulative, total = np.cumsum(mass), float(np.sum(mass))
            distribution["deterministic_quantiles"][name] = {f"p{int(q*100)}": float(grid[min(np.searchsorted(cumulative, q*total), grid.size-1)]) for q in (0.9, 0.95, 0.99)}
        else:
            distribution["deterministic_quantiles"][name] = None
    band = 100.0 * np.finfo(float).eps
    point["kfe_valid_nonpathological"] = bool(distribution["density_finite"] and abs(distribution["total_mass"] - 1.0) <= 1e-12 and distribution["density_min"] >= -band and np.isfinite(point["kfe"]["kfe"]["raw_residual_inf"]))
    point["bmax_nonbinding"] = bool(max(distribution["modal_b"]) < 20.0)
    return point


def _delta(old: Any, new: Any) -> dict[str, float]:
    old_value, new_value = float(old), float(new)
    return {"old": old_value, "new": new_value, "delta": new_value - old_value, "absolute_change": abs(new_value-old_value)}


def comparison(old: dict[str, Any], new: dict[str, Any]) -> dict[str, Any]:
    if not old.get("kfe_valid_nonpathological") or not new.get("kfe_valid_nonpathological"):
        return {"old_point_id": old["point_id"], "new_point_id": new["point_id"],
                "comparison_type": "TRUE_GRID_PRECISION_COMPARISON",
                "available": False, "reason": "KFE_NOT_AVAILABLE_FOR_BOTH_POINTS",
                "post_result_threshold": False}
    ospec, nspec = old["specification"], new["specification"]
    od, nd = old["kfe"]["distribution"], new["kfe"]["distribution"]
    oa, na = old["kfe"]["aggregates"], new["kfe"]["aggregates"]
    ag = np.linspace(0.0, 100.0, 160)
    obg, nbg = np.linspace(-2.0, 20.0, ospec["I"]), np.linspace(-2.0, 20.0, nspec["I"])
    return {"old_point_id": old["point_id"], "new_point_id": new["point_id"], "comparison_type": "TRUE_GRID_PRECISION_COMPARISON", "available": True,
        "support": {"a": [0.0,100.0], "b": [-2.0,20.0]}, "I": _delta(ospec["I"], nspec["I"]), "db": _delta(ospec["db"], nspec["db"]),
        "hjb": {"old_status": old["hjb"]["classification"], "new_status": new["hjb"]["classification"], "iterations": _delta(old["hjb"]["iterations_used"], new["hjb"]["iterations_used"])},
        "aggregates": {name: _delta(oa[name], na[name]) for name in ("Ct","Lt","At","Bt")},
        "modal_a": {"old": od["modal_a"], "new": nd["modal_a"], "movement": abs(float(nd["modal_a"][0])-float(od["modal_a"][0]))},
        "modal_b": {"old": od["modal_b"], "new": nd["modal_b"], "movement": abs(float(nd["modal_b"][0])-float(od["modal_b"][0]))},
        "endpoint_masses": {name: _delta(od["boundary_mass_shares"][name], nd["boundary_mass_shares"][name]) for name in ("amin","amax","bmin","bmax")},
        "a_marginal_signed_cdf_l1_width_normalized": same_support_cdf_distance(ag, od["a_marginal_mass"], ag, nd["a_marginal_mass"]),
        "b_marginal_signed_cdf_l1_width_normalized": same_support_cdf_distance(obg, od["b_marginal_mass"], nbg, nd["b_marginal_mass"]),
        "signed_mass_clipped": False, "signed_mass_renormalized": False, "post_result_threshold": False}


def _marginal(point: dict[str, Any]) -> dict[str, Any]:
    spec, d = point["specification"], point["kfe"]["distribution"]
    return {"point_id": point["point_id"], "I": spec["I"], "J": spec["J"], "a_grid": np.linspace(0,100,160).tolist(),
            "a_marginal_mass": d["a_marginal_mass"], "b_grid": np.linspace(-2,20,spec["I"]).tolist(), "b_marginal_mass": d["b_marginal_mass"],
            "top_3_a_bins": d["top_3_a_bins"], "top_3_b_bins": d["top_3_b_bins"], "deterministic_quantiles": d["deterministic_quantiles"]}


def _row(point: dict[str, Any]) -> dict[str, Any]:
    h, k = point["hjb"], point["kfe"]
    d, a = k.get("distribution", {}), k.get("aggregates", {})
    b = d.get("boundary_mass_shares", {})
    return {"point_id": point["point_id"], "source": "REUSED" if point.get("accepted_evidence_reused_without_runtime") else "FRESH",
        "I": point["specification"]["I"], "J": 160, "db": point["specification"]["db"], "iterations": h["iterations_used"], "final_statistic": h["final_convergence_statistic"],
        "maximum_a2max": h["maximum_a2max"], "first_illegal_iteration": h["first_illegal_iteration"],
        "hjb_classification": h["classification"], "kfe_ran": k.get("ran", False), "kfe_valid": point["kfe_valid_nonpathological"],
        "kfe_residual": k.get("kfe", {}).get("raw_residual_inf"), "total_mass": d.get("total_mass"), "density_min": d.get("density_min"), "negative_count": d.get("density_negative_count"),
        **{name:a.get(name) for name in ("Ct","Lt","At","Bt")}, "Bt_pos": d.get("Bt_pos"), "Bt_neg": d.get("Bt_neg"), "modal_a": (d.get("modal_a") or [None])[0], "modal_b": (d.get("modal_b") or [None])[0],
        **{f"{name}_mass":b.get(name) for name in ("amin","amax","bmin","bmax")}, "bmax_nonbinding": point.get("bmax_nonbinding")}


def write_json(path: Path, value: Any) -> None:
    run.coarse.write_json(path, value)


def seal(root: Path) -> dict[str, Any]:
    entries = [{"path": p.relative_to(root).as_posix(), "bytes": p.stat().st_size, "sha256": run.coarse.file_sha256(p)} for p in sorted(root.iterdir()) if p.is_file() and p.name != "sealed_manifest_sha256.json"]
    manifest = {"schema": "CH5_MP4C_K1_J160_LIQUID_GRID_COMPACT_SEAL_V1", "algorithm": "SHA-256", "entry_count": len(entries), "total_bytes": sum(e["bytes"] for e in entries), "entries": entries}
    write_json(root / "sealed_manifest_sha256.json", manifest); return manifest


def build(raw_root: Path, compact_root: Path, decision: str, rationale: str, smallest_i: int | None) -> int:
    validate_decision(decision)
    raw_root, compact_root = Path(raw_root), Path(compact_root)
    raw = [read_json(path) for path in sorted(raw_root.glob("i*_j160_result.json"))]
    failure = decision.startswith("J160_LIQUID_GRID_PRECISION_UNRESOLVED")
    expected = list(run.POINTS[:len(raw)])
    if not raw or len(raw) > 2 or [(p["specification"]["I"],p["specification"]["J"]) for p in raw] != expected:
        raise ValueError("raw result ladder is not an authorized I40/I80 J160 prefix")
    if not failure and len(raw) != 2:
        raise ValueError("precision decision requires complete I40/I80 raw results")
    points = [decorate(accepted_reference()), *[decorate(p) for p in raw]]
    comparisons = [comparison(points[0],points[1])]
    if len(points) == 3:
        comparisons.append(comparison(points[1],points[2]))
    else:
        comparisons.append({"old_point_id":"i040_j160", "new_point_id":"i080_j160", "comparison_type":"TRUE_GRID_PRECISION_COMPARISON", "available":False, "reason":"I80_NOT_RUN_AFTER_I40_TERMINAL_FAILURE", "post_result_threshold":False})
    gates_pass = all(p["hjb"]["classification"] == "HJB_CONVERGED" and p["kfe_valid_nonpathological"] and p["bmax_nonbinding"] for p in points[1:])
    if not failure and not gates_pass:
        raise ValueError("fresh numerical gates do not support a precision terminal")
    if decision.endswith("PROVISIONALLY_STABILIZED") and smallest_i not in (40,80):
        raise ValueError("stabilized decision requires smallest tested I of 40 or 80")
    if not decision.endswith("PROVISIONALLY_STABILIZED") and smallest_i is not None:
        raise ValueError("unstabilized decision cannot name a defensible tested I")
    compact_root.mkdir(parents=True, exist_ok=False)
    write_json(compact_root / "source_identity.json", read_json(raw_root / "source_identity.json"))
    write_json(compact_root / "input_invariance_receipt.json", read_json(raw_root / "input_invariance_receipt.json"))
    write_json(compact_root / "point_receipts.json", points)
    write_json(compact_root / "marginals.json", [_marginal(p) for p in points if p.get("kfe_valid_nonpathological")])
    write_json(compact_root / "precision_comparison.json", {"schema":"CH5_MP4C_K1_J160_LIQUID_GRID_PRECISION_COMPARISON_V1", "method":"accepted same-support raw signed CDF distance", "comparisons":comparisons})
    ledger = read_json(raw_root / "final_call_ledger.json"); write_json(compact_root / "call_ledger.json", ledger)
    write_json(compact_root / "summary.json", {"terminal_classification":decision, "descriptive_decision_basis":rationale, "post_result_threshold_invented":False,
        "smallest_defensible_tested_I":smallest_i, "practical_bounded_diagnostics_only":True, "continuum_convergence":False, "production_final_precision":False,
        "kfe_caveat":"Accepted standalone contaminated-row KFE only; raw signed density preserved; corrected-2018 finite-box/pinning remains separate.",
        "results_eligibility":False, "exactly_one_next_gate":"REVIEWER_J160_LIQUID_GRID_ROUTE_DECISION"})
    rows=[_row(p) for p in points]
    with (compact_root / "precision_points.csv").open("x",encoding="utf-8-sig",newline="") as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    seal(compact_root)
    return 0


def main() -> int:
    parser=argparse.ArgumentParser();parser.add_argument("raw_root",type=Path);parser.add_argument("compact_root",type=Path);parser.add_argument("decision",choices=sorted(TERMINALS));parser.add_argument("rationale");parser.add_argument("--smallest-i",type=int)
    args=parser.parse_args();return build(args.raw_root,args.compact_root,args.decision,args.rationale,args.smallest_i)


if __name__ == "__main__":
    raise SystemExit(main())
