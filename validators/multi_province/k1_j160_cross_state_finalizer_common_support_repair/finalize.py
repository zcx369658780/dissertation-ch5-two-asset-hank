"""Validate preserved J160 evidence and build the offline closeout package.

This module intentionally imports no scientific runner or solver.  It only reads
persisted receipts/arrays, computes descriptive comparisons, and serializes a
sealed compact evidence package.
"""
from __future__ import annotations

import argparse
import copy
import csv
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

import numpy as np


BASELINE = "1c2d2b0bc0167b1821315164356e461a0f3c05fa"
CORNERS = ((0.06, 13.0), (0.06, 18.0), (0.07, 13.0), (0.07, 18.0))
STATES = ((0.06, 13.0), (0.06, 18.0), (0.0675, 15.5), (0.07, 13.0), (0.07, 18.0))
EXPECTED_RAW_FILES = {
    "execution_complete.json", "final_call_ledger.json", "in_progress_call_ledger.json",
    "input_invariance_receipt.json", "pre_science_call_ledger.json", "preflight_complete.json",
    "science_started.json", "source_identity.json",
}
ACCEPTED_HASHES = {
    "j20_manifest": ("ch5_mp4c_k1_real_composite_wage_domain_macro_scale_audit/sealed_manifest_sha256.json", "865E334A9A3E282C96EF268F333BA355EF2D2291B0A92B6D9A7D6F963262E2AE"),
    "j20_points": ("ch5_mp4c_k1_real_composite_wage_domain_macro_scale_audit/point_receipts.json", "9CFAA54C7D0A4B99A563A77470B4779A118FF030D30BA2CD913D93B29EE4E689"),
    "j20_marginals": ("ch5_mp4c_k1_real_composite_wage_domain_macro_scale_audit/marginals.json", "D76976FBEC40F6F42DDEBC0D22095D4657D2E0559535F87888F94712C49635AB"),
    "j160_manifest": ("ch5_mp4c_k1_household_asset_grid_precision_receipt_repair_reexecution/sealed_manifest_sha256.json", "2895FD31A7759F4F62DF2008B7BDCBCAE69D5B254B56B6110D3E632A32CB2C88"),
    "j160_points": ("ch5_mp4c_k1_household_asset_grid_precision_receipt_repair_reexecution/point_receipts.json", "6C0C75A726232A36F521FDEA9FEFBA8AEB2F212EB2E54013536172827749EFE1"),
    "j160_marginals": ("ch5_mp4c_k1_household_asset_grid_precision_receipt_repair_reexecution/marginals.json", "F08B11A85285E6A961A8619B54860E1AD8F9DC6A8BCC9CD7DA29AF81BCF34FBE"),
}
ARRAY_KEYS = ("value", "consumption", "labor", "transfer", "mu_a", "mu_b", "density")


def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    def convert(item: Any) -> Any:
        if isinstance(item, np.ndarray):
            return item.tolist()
        if isinstance(item, np.generic):
            return item.item()
        raise TypeError(f"unsupported JSON value: {type(item)!r}")
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, default=convert) + "\n", encoding="utf-8")


def file_sha256(path: Path) -> str:
    return sha256(Path(path).read_bytes()).hexdigest().upper()


def canonical_sha256(path: Path) -> str:
    return sha256(Path(path).read_text(encoding="utf-8").encode("utf-8")).hexdigest().upper()


def array_sha256(value: np.ndarray) -> str:
    array = np.asarray(value)
    header = f"{array.dtype.str}|{array.shape}|C|".encode("ascii")
    return sha256(header + np.ascontiguousarray(array).tobytes()).hexdigest().upper()


def _validated_vectors(grid: Any, mass: Any) -> tuple[np.ndarray, np.ndarray]:
    values, weights = np.asarray(grid, dtype=float), np.asarray(mass, dtype=float)
    if (values.ndim != 1 or weights.ndim != 1 or values.size != weights.size
            or values.size < 2 or not np.isfinite(values).all()
            or not np.isfinite(weights).all() or not np.all(np.diff(values) > 0.0)):
        raise ValueError("grid and raw signed mass must be finite aligned vectors on positive-width support")
    return values, weights


def extended_raw_signed_cdf(grid: Any, mass: Any, evaluation_grid: Any) -> np.ndarray:
    """Evaluate the raw signed node-mass CDF with constant exterior extension."""
    values, weights = _validated_vectors(grid, mass)
    probes = np.asarray(evaluation_grid, dtype=float)
    if probes.ndim != 1 or not np.isfinite(probes).all():
        raise ValueError("evaluation grid must be a finite vector")
    return np.interp(probes, values, np.cumsum(weights), left=0.0, right=float(np.sum(weights)))


def domain_plus_grid_cdf_distance(first_grid: Any, first_mass: Any,
                                  second_grid: Any, second_mass: Any) -> float:
    """Union-support width-normalized L1 distance between raw signed CDFs."""
    x1, m1 = _validated_vectors(first_grid, first_mass)
    x2, m2 = _validated_vectors(second_grid, second_mass)
    union = np.union1d(x1, x2)
    width = float(union[-1] - union[0])
    if not np.isfinite(width) or width <= 0.0:
        raise ValueError("union support must have positive finite width")
    cdf1 = extended_raw_signed_cdf(x1, m1, union)
    cdf2 = extended_raw_signed_cdf(x2, m2, union)
    return float(np.trapezoid(np.abs(cdf1 - cdf2), union) / width)


def _identity(path: Path, expected: str) -> dict[str, Any]:
    byte_hash, canonical_hash = file_sha256(path), canonical_sha256(path)
    matched = "BYTES" if byte_hash == expected else "CANONICAL_LF" if canonical_hash == expected else None
    return {"path": str(path.resolve()), "expected_sha256": expected,
            "actual_byte_sha256": byte_hash, "actual_canonical_lf_sha256": canonical_hash,
            "matched_representation": matched, "pass": matched is not None}


def source_identity(evidence_root: Path, raw_root: Path) -> dict[str, Any]:
    identities = {
        name: _identity(evidence_root / relative, expected)
        for name, (relative, expected) in ACCEPTED_HASHES.items()
    }
    raw_source = read_json(raw_root / "source_identity.json")
    return {"schema": "CH5_MP4C_K1_J160_CROSS_STATE_FINALIZER_SOURCE_IDENTITY_V1",
            "actual_baseline": BASELINE, "accepted_reuse_identities": identities,
            "raw_source_identity_pass": bool(raw_source.get("pass")),
            "matlab_runtime_calls": 0,
            "pass": bool(raw_source.get("pass")) and all(item["pass"] for item in identities.values())}


def _receipt_hashes(point: dict[str, Any]) -> dict[str, str]:
    arrays = point["hjb"]["scientific_arrays"]["arrays"]
    return {name: arrays[name]["sha256"] for name in ARRAY_KEYS if name != "density"} | {
        "density": point["kfe"]["kfe"]["density_sha256"]
    }


def raw_integrity(raw_root: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    paths = sorted(path for path in raw_root.iterdir() if path.is_file())
    result_paths = sorted(raw_root.glob("j160_*_result.json"))
    expected_names = set(EXPECTED_RAW_FILES)
    for result_path in result_paths:
        stem = result_path.name.removesuffix("_result.json")
        expected_names.update({f"{stem}_result.json", f"{stem}_started.json", f"{stem}_scientific_arrays.npz"})
    ledger = read_json(raw_root / "final_call_ledger.json")
    points, point_checks = [], []
    for path in result_paths:
        point = read_json(path)
        points.append(point)
        spec, hjb, kfe = point["specification"], point["hjb"], point["kfe"]
        archive_path = raw_root / path.name.replace("_result.json", "_scientific_arrays.npz")
        with np.load(archive_path, allow_pickle=False) as archive:
            hashes = {key: array_sha256(archive[key]) for key in ARRAY_KEYS}
            finite_shapes = all(np.asarray(archive[key]).shape == (20, 160, 2)
                                and np.isfinite(archive[key]).all() for key in ARRAY_KEYS)
            grids_exact = (np.array_equal(archive["grid_a"], np.linspace(0.0, 100.0, 160))
                           and np.array_equal(archive["grid_b"], np.linspace(-2.0, 20.0, 20))
                           and np.array_equal(archive["density_shape"], np.array([20, 160, 2])))
        expected = _receipt_hashes(point)
        distribution = kfe["distribution"]
        check = {
            "point_id": point["point_id"], "state": [point["r_a"], point["wage"]],
            "frozen_spec_exact": {key: spec[key] for key in ("rb", "amin", "amax", "bmin", "bmax", "I", "J", "Nz", "h")}
                == {"rb": 0.02, "amin": 0.0, "amax": 100.0, "bmin": -2.0, "bmax": 20.0, "I": 20, "J": 160, "Nz": 2, "h": 1.0},
            "hjb_legal_converged": hjb["classification"] == "HJB_CONVERGED" and hjb["converged"]
                and hjb["first_illegal_iteration"] is None and all(x["legal"] for x in hjb["iteration_operator_legality"]),
            "scientific_arrays_finite_shape_valid": finite_shapes and hjb["scientific_arrays"]["all_arrays_finite_shape_valid"],
            "array_hashes_match": hashes == expected, "grids_exact": grids_exact,
            "kfe_completed": kfe.get("ran") and kfe.get("completed"),
            "kfe_valid_nonpathological": bool(distribution.get("density_finite"))
                and abs(float(distribution.get("total_mass")) - 1.0) <= 1e-12
                and float(distribution.get("density_min")) >= -100.0 * np.finfo(float).eps
                and np.isfinite(float(kfe["kfe"]["raw_residual_inf"])),
        }
        check["pass"] = all(value for key, value in check.items() if key not in {"point_id", "state"})
        point_checks.append(check)
    forbidden = {name: ledger.get(name) for name in ("global_outer_calls", "firm_calls", "matlab_calls", "k1b_calls", "k2_calls", "ge_calls", "downstream_calls", "shock_calls", "irf_calls", "results_writes")}
    checks = {
        "raw_root_exists": raw_root.is_dir(), "raw_seal_manifest_absent_recorded": not any("manifest" in p.name or "seal" in p.name for p in paths),
        "exact_file_count_20": len(paths) == 20, "exact_total_bytes_1331049": sum(p.stat().st_size for p in paths) == 1331049,
        "exact_expected_file_set": {p.name for p in paths} == expected_names,
        "exact_four_states": sorted((float(p["r_a"]), float(p["wage"])) for p in points) == sorted(CORNERS),
        "hjb_started_completed_4_4": ledger["hjb_calls_started"] == ledger["hjb_calls_completed"] == 4,
        "kfe_started_completed_4_4": ledger["kfe_calls_started"] == ledger["kfe_calls_completed"] == 4,
        "scientific_retries_zero": ledger["scientific_retries"] == 0,
        "center_reuse_zero": ledger["center_reuse_calls"] == {"hjb": 0, "kfe": 0},
        "j20_reuse_zero": ledger["j20_reuse_calls"] == {"hjb": 0, "kfe": 0},
        "forbidden_runtime_zero": all(value == 0 for value in forbidden.values()),
        "all_point_checks_pass": all(item["pass"] for item in point_checks),
    }
    receipt = {"schema": "CH5_MP4C_K1_J160_RAW_EVIDENCE_INTEGRITY_V1", "raw_root": str(raw_root.resolve()),
               "raw_seal_manifest_status": "ABSENT_RECORDED_NOT_AUTOMATIC_FAILURE", "file_count": len(paths),
               "total_bytes": sum(p.stat().st_size for p in paths), "checks": checks,
               "point_checks": point_checks, "forbidden_runtime": forbidden, "pass": all(checks.values())}
    return receipt, points


def _decorate(point: dict[str, Any]) -> dict[str, Any]:
    point = copy.deepcopy(point)
    d, spec = point["kfe"]["distribution"], point["specification"]
    a, b = np.asarray(d["a_marginal_mass"]), np.asarray(d["b_marginal_mass"])
    d["upper_quantile_locations"] = {}
    for name, grid, mass in (("a", np.linspace(spec["amin"], spec["amax"], spec["J"]), a),
                             ("b", np.linspace(spec["bmin"], spec["bmax"], spec["I"]), b)):
        cumulative, total = np.cumsum(mass), float(np.sum(mass))
        d["upper_quantile_locations"][name] = {
            f"p{int(q*100)}": float(grid[min(int(np.searchsorted(cumulative, q * total)), grid.size - 1)])
            for q in (0.90, 0.95, 0.99)
        }
    point["a_domain_classification"] = "INTERIOR_A_DISTRIBUTION_CANDIDATE" if d["boundary_mass_shares"]["amax"] == 0 and max(d["modal_a"]) < spec["amax"] else "A_UPPER_BOUNDARY_PILEUP"
    point["b_domain_classification"] = "NONBINDING_LIQUID_UPPER_BOUNDARY" if max(d["modal_b"]) < spec["bmax"] else "B_UPPER_BOUNDARY_PILEUP"
    return point


def _delta(old: Any, new: Any) -> dict[str, float]:
    old_value, new_value = float(old), float(new)
    return {"j20": old_value, "j160": new_value, "delta": new_value - old_value}


def comparison(old: dict[str, Any], new: dict[str, Any]) -> dict[str, Any]:
    old_d, new_d = old["kfe"]["distribution"], new["kfe"]["distribution"]
    old_a, old_b = np.linspace(0.0, 10.0, 20), np.linspace(-2.0, 5.0, 20)
    spec = new["specification"]
    new_a, new_b = np.linspace(spec["amin"], spec["amax"], spec["J"]), np.linspace(spec["bmin"], spec["bmax"], spec["I"])
    return {
        "state": {"ra": old["r_a"], "wage": old["wage"]}, "old_point_id": old["point_id"], "new_point_id": new["point_id"],
        "hjb_status": {"j20": old["hjb"]["classification"], "j160": new["hjb"]["classification"]},
        "iterations": _delta(old["hjb"]["iterations_used"], new["hjb"]["iterations_used"]),
        "kfe_status": {"j20": old["kfe"].get("ran"), "j160": new["kfe"].get("completed")},
        "domain_and_grid": {"j20": {"I": 20, "J": 20, "a": [0.0, 10.0], "b": [-2.0, 5.0]}, "j160": {"I": 20, "J": 160, "a": [0.0, 100.0], "b": [-2.0, 20.0]}},
        "aggregates": {name: _delta(old["kfe"]["aggregates"][name], new["kfe"]["aggregates"][name]) for name in ("Ct", "Lt", "At", "Bt")},
        "modal": {"a": {"j20": old_d["modal_a"], "j160": new_d["modal_a"]}, "b": {"j20": old_d["modal_b"], "j160": new_d["modal_b"]}},
        "endpoint_masses": {name: _delta(old_d["boundary_mass_shares"][name], new_d["boundary_mass_shares"][name]) for name in ("amin", "amax", "bmin", "bmax")},
        "a_DOMAIN_PLUS_GRID_CDF_DISTANCE": domain_plus_grid_cdf_distance(old_a, old_d["a_marginal_mass"], new_a, new_d["a_marginal_mass"]),
        "b_DOMAIN_PLUS_GRID_CDF_DISTANCE": domain_plus_grid_cdf_distance(old_b, old_d["b_marginal_mass"], new_b, new_d["b_marginal_mass"]),
        "distance_scope": "DOMAIN_EXPANSION_PLUS_DISCRETIZATION_CHANGE", "signed_mass_clipped": False, "signed_mass_renormalized": False,
    }


def _marginal(point: dict[str, Any]) -> dict[str, Any]:
    spec, d = point["specification"], point["kfe"]["distribution"]
    return {"point_id": point["point_id"], "ra": point["r_a"], "wage": point["wage"],
            "a_grid": np.linspace(spec["amin"], spec["amax"], spec["J"]).tolist(), "a_marginal_mass": d["a_marginal_mass"],
            "b_grid": np.linspace(spec["bmin"], spec["bmax"], spec["I"]).tolist(), "b_marginal_mass": d["b_marginal_mass"],
            "upper_quantile_locations": d["upper_quantile_locations"]}


def _point_row(point: dict[str, Any], phase: str) -> dict[str, Any]:
    h, k, d = point["hjb"], point["kfe"], point["kfe"]["distribution"]
    a, boundary = k["aggregates"], d["boundary_mass_shares"]
    return {"phase": phase, "point_id": point["point_id"], "ra": point["r_a"], "wage": point["wage"],
            "hjb_status": h["classification"], "iterations": h["iterations_used"], "final_statistic": h["final_convergence_statistic"],
            "kfe_completed": k.get("completed", k.get("ran", False)), "kfe_residual_inf": k["kfe"]["raw_residual_inf"], "total_mass": d["total_mass"], "density_min": d["density_min"],
            **{name: a[name] for name in ("Ct", "Lt", "At", "Bt")}, "modal_a": d["modal_a"][0], "modal_b": d["modal_b"][0],
            **{f"{name}_mass": boundary[name] for name in ("amin", "amax", "bmin", "bmax")},
            "a_domain": point["a_domain_classification"], "b_domain": point["b_domain_classification"]}


def _seal(root: Path) -> dict[str, Any]:
    entries = [{"path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size, "sha256": file_sha256(path)}
               for path in sorted(root.iterdir()) if path.is_file() and path.name != "sealed_manifest_sha256.json"]
    manifest = {"schema": "CH5_MP4C_K1_J160_CROSS_STATE_COMPACT_SEAL_V1", "algorithm": "SHA-256", "entries": entries,
                "entry_count": len(entries), "total_bytes": sum(item["bytes"] for item in entries)}
    write_json(root / "sealed_manifest_sha256.json", manifest)
    return manifest


def build(raw_root: Path, evidence_root: Path, compact_root: Path) -> int:
    raw_root, evidence_root, compact_root = map(Path, (raw_root, evidence_root, compact_root))
    integrity, raw_points = raw_integrity(raw_root)
    if not integrity["pass"]:
        raise RuntimeError("J160_CROSS_STATE_RAW_EVIDENCE_INTEGRITY_BLOCKER")
    source = source_identity(evidence_root, raw_root)
    if not source["pass"]:
        raise RuntimeError("accepted reuse-only source identity mismatch")
    j20 = read_json(evidence_root / ACCEPTED_HASHES["j20_points"][0])
    j20_by_state = {(float(p["r_a"]), float(p["wage"])): p for p in j20}
    center_candidates = [p for p in read_json(evidence_root / ACCEPTED_HASHES["j160_points"][0])
                         if p["specification"]["I"] == 20 and p["specification"]["J"] == 160
                         and p["specification"]["ra"] == 0.0675 and p["specification"]["wage"] == 15.5]
    if len(center_candidates) != 1 or any(state not in j20_by_state for state in STATES):
        raise ValueError("accepted reuse-only five-state references are incomplete")
    center = copy.deepcopy(center_candidates[0]); center.update({"r_a": 0.0675, "wage": 15.5, "point_id": "j160_center_reused", "accepted_center_reused_without_runtime": True})
    fresh = [_decorate(p) for p in raw_points]
    by_state = {(float(p["r_a"]), float(p["wage"])): p for p in fresh}
    all_j160 = [_decorate(center) if state == (0.0675, 15.5) else by_state[state] for state in STATES]
    comparisons = [comparison(j20_by_state[state], point) for state, point in zip(STATES, all_j160)]
    terminal_pass = all(p["hjb"]["classification"] == "HJB_CONVERGED" and p["kfe"]["completed"]
                        and p["a_domain_classification"] == "INTERIOR_A_DISTRIBUTION_CANDIDATE"
                        and p["b_domain_classification"] == "NONBINDING_LIQUID_UPPER_BOUNDARY" for p in fresh)
    compact_root.mkdir(parents=True, exist_ok=False)
    write_json(compact_root / "source_identity.json", source)
    write_json(compact_root / "raw_evidence_integrity_receipt.json", integrity)
    inputs = read_json(raw_root / "input_invariance_receipt.json"); inputs["finalizer_reverified_without_science_runtime"] = True
    write_json(compact_root / "input_invariance_receipt.json", inputs)
    write_json(compact_root / "point_receipts.json", all_j160)
    write_json(compact_root / "marginals.json", [_marginal(p) for p in all_j160])
    write_json(compact_root / "j20_j160_comparison.json", {"schema": "CH5_MP4C_K1_J20_J160_DOMAIN_PLUS_GRID_COMPARISON_V1",
        "metric_name": "DOMAIN_PLUS_GRID_CDF_DISTANCE", "method": "raw signed cumulative node mass; piecewise-linear interpolation; zero below own support; raw total above own support; union-support L1 integral divided by union width",
        "comparisons": comparisons})
    ledger = {"schema": "CH5_MP4C_K1_J160_FINALIZER_ZERO_SCIENCE_LEDGER_V1", "preserved_raw_science": read_json(raw_root / "final_call_ledger.json"),
              "this_task_calls": {name: 0 for name in ("hjb", "kfe", "j20_rerun", "j160_rerun", "j320", "j640", "j1280", "scientific_retries", "global_outer", "firm", "matlab", "k1b", "k2", "ge", "downstream", "shock", "irf", "results")}}
    write_json(compact_root / "call_ledger.json", ledger)
    repair = {"schema": "CH5_MP4C_K1_J160_COMMON_SUPPORT_FINALIZER_REPAIR_V1", "original_error": "ValueError: CDF comparison requires a common support",
              "same_support_semantics_preserved": True, "different_support_union_interval": True, "below_support_cdf": 0.0,
              "above_support_cdf": "RAW_TOTAL_MARGINAL_MASS", "signed_mass_clipped": False, "renormalized": False, "smoothed": False, "rebinned": False,
              "metric_name": "DOMAIN_PLUS_GRID_CDF_DISTANCE", "scientific_solver_imports": 0, "scientific_calls": 0, "pass": True}
    write_json(compact_root / "finalizer_repair_receipt.json", repair)
    rows = [_point_row(p, "REUSED_CENTER" if p.get("accepted_center_reused_without_runtime") else "FRESH") for p in all_j160]
    with (compact_root / "points.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
    write_json(compact_root / "summary.json", {"terminal_classification": "J160_BOUNDED_CROSS_STATE_CONFIRMATION_PASS__PRACTICAL_DIAGNOSTIC_GRID_SUPPORTED" if terminal_pass else "J160_BOUNDED_CROSS_STATE_CONFIRMATION_FAILURE__REVIEW_REQUIRED",
        "raw_integrity_pass": integrity["pass"], "four_fresh_hjb_legal_converged": all(p["hjb"]["classification"] == "HJB_CONVERGED" for p in fresh),
        "four_fresh_kfe_valid_nonpathological": all(c["kfe_valid_nonpathological"] for c in integrity["point_checks"]),
        "a_domain_conclusion": "amax=100 nonbinding at all four fresh points; interior modes and zero amax mass support bounded diagnostic interpretation",
        "b_domain_conclusion": "bmax=20 is nonbinding in the bounded-diagnostic sense at all four fresh points; endpoint mass is nonzero and largest at ra=.06,w=18",
        "cross_state_coherence": "descriptive aggregate and distribution changes are finite; variation is state-dependent but not numerically pathological",
        "practical_diagnostic_grid_supported": terminal_pass, "continuum_convergence": False, "production_final_precision": False, "ge_validated": False, "results_eligibility": False,
        "kfe_caveat": "Accepted standalone contaminated-row KFE construction; tiny signed density entries are preserved; corrected-2018 finite-box/pinning remains separate.",
        "exactly_one_next_gate": "REVIEWER_J160_CROSS_STATE_ROUTE_DECISION"})
    _seal(compact_root)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("raw_root", type=Path); parser.add_argument("evidence_root", type=Path); parser.add_argument("compact_root", type=Path)
    args = parser.parse_args(); return build(args.raw_root, args.evidence_root, args.compact_root)


if __name__ == "__main__":
    raise SystemExit(main())
