"""Read persisted G1/G2 evidence and localize HA/HJB stress without model calls."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from hashlib import sha256
from pathlib import Path
from typing import Any, Iterable

import numpy as np
from scipy.stats import pearsonr, spearmanr


PATHS = {"G1": "annual_g1_guarded", "G2": "annual_g2_guarded"}
TURNS = range(2, 6)
GRID_B = np.linspace(-2.0, 5.0, 20)
GRID_A = np.linspace(0.0, 10.0, 20)
GRID_Z = np.array([0.8, 1.3])
DRIFT_TOLERANCE = 1.0e-12
ITERATION_CEILING = 100
ARRAY_FIELDS = (
    "value", "consumption", "labor", "transfer", "adjustment_cost",
    "effective_illiquid_return", "mu_a", "mu_b", "utility",
    "liquid_label", "transfer_label",
)
EXTREME_FIELDS = ("transfer", "adjustment_cost", "mu_a", "mu_b")
CLASSIFICATION = (
    "G2_STRESS_MIXED_ACROSS_NEWLY_UNSATURATED_AND_STILL_SATURATED_RETURN_REGIMES"
    "__PATH_HISTORY_AND_WAGE_INTERACTION_NOT_IDENTIFIABLE_FROM_PERSISTED_EVIDENCE"
    "__BOUNDED_INSTRUMENTATION_TASK_REQUIRED"
)


def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        stream.write("\n")


def finite_ratio(numerator: float, denominator: float) -> float | None:
    if not np.isfinite([numerator, denominator]).all() or denominator == 0.0:
        return None
    return float(numerator / denominator)


def convergence_switch(g1: bool, g2: bool) -> str:
    if g1 and g2:
        return "BOTH_CONVERGED"
    if g1 and not g2:
        return "G1_CONVERGED_G2_NONCONVERGED"
    if not g1 and g2:
        return "G1_NONCONVERGED_G2_CONVERGED"
    return "BOTH_NONCONVERGED"


def hit_state(row: dict[str, Any], prefix: str) -> str:
    active = [name for name in ("lower", "upper", "unsaturated")
              if bool(row[f"{prefix}_{name}_hit"] if name != "unsaturated" else row[f"{prefix}_unsaturated"])]
    if len(active) != 1:
        raise ValueError(f"non-exclusive or missing {prefix} status")
    return active[0].upper()


def return_regime(g1: dict[str, Any], g2: dict[str, Any]) -> str:
    a, b = hit_state(g1, "return_guard"), hit_state(g2, "return_guard")
    if b == "UPPER":
        return "A_STILL_UPPER_SATURATED"
    if a == "UPPER" and b == "UNSATURATED":
        return "B_NEWLY_UNSATURATED"
    if b == "LOWER":
        return "C_LOWER_HIT"
    return f"OTHER_{a}_TO_{b}"


def boundary_faces(index: tuple[int, int, int]) -> list[str]:
    i_b, i_a, _ = index
    faces = []
    if i_a == 0:
        faces.append("lower-a")
    if i_a == GRID_A.size - 1:
        faces.append("upper-a")
    if i_b == 0:
        faces.append("lower-b")
    if i_b == GRID_B.size - 1:
        faces.append("upper-b")
    return faces or ["interior"]


def load_arrays(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as data:
        result = {name: np.array(data[name], copy=True) for name in ARRAY_FIELDS}
    if any(value.shape != (20, 20, 2) for value in result.values()):
        raise ValueError(f"unexpected HJB array shape: {path}")
    for name, value in result.items():
        if name.endswith("label"):
            continue
        if not np.isfinite(value).all():
            raise ValueError(f"nonfinite persisted array {name}: {path}")
    return result


def verify_external_manifest(root: Path) -> dict[str, Any]:
    manifest = root / "manifest_sha256.json"
    value = read_json(manifest)
    mismatches = []
    for entry in value["files"]:
        path = root / entry["path"]
        if (not path.is_file() or path.stat().st_size != entry["bytes"] or
                sha256(path.read_bytes()).hexdigest().upper() != entry["sha256"]):
            mismatches.append(entry["path"])
    return {
        "manifest_sha256": sha256(manifest.read_bytes()).hexdigest().upper(),
        "entries_checked": len(value["files"]), "mismatches": mismatches,
        "status": "PASS" if not mismatches else "FAIL",
    }


def numeric_summary(values: Iterable[float]) -> dict[str, float | int | None]:
    a = np.asarray(list(values), dtype=float)
    finite = a[np.isfinite(a)]
    if finite.size == 0:
        return {"count": int(a.size), "finite_count": 0, "min": None, "median": None, "max": None}
    return {"count": int(a.size), "finite_count": int(finite.size), "min": float(finite.min()),
            "median": float(np.median(finite)), "max": float(finite.max())}


def group_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "province_turns": len(rows),
        "g2_converged": sum(bool(r["g2_converged"]) for r in rows),
        "g2_iteration_ceiling_hits": sum(bool(r["g2_iteration_ceiling_hit"]) for r in rows),
        "g2_hjb_statistic": numeric_summary(r["g2_hjb_statistic"] for r in rows),
        "g2_iterations": numeric_summary(r["g2_iterations"] for r in rows),
        "g2_transfer_abs_max": numeric_summary(r["g2_transfer_abs_max"] for r in rows),
        "g2_adjustment_cost_abs_max": numeric_summary(r["g2_adjustment_cost_abs_max"] for r in rows),
        "g2_mu_a_abs_max": numeric_summary(r["g2_mu_a_abs_max"] for r in rows),
        "g2_mu_b_abs_max": numeric_summary(r["g2_mu_b_abs_max"] for r in rows),
    }


def association(x: list[float], y: list[float]) -> dict[str, Any]:
    a, b = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    mask = np.isfinite(a) & np.isfinite(b)
    a, b = a[mask], b[mask]
    if a.size < 3 or np.unique(a).size < 2 or np.unique(b).size < 2:
        return {"n": int(a.size), "pearson": None, "spearman": None,
                "classification": "DESCRIPTIVE_ONLY_NOT_CAUSAL"}
    return {"n": int(a.size), "pearson": float(pearsonr(a, b).statistic),
            "spearman": float(spearmanr(a, b).statistic),
            "classification": "DESCRIPTIVE_ONLY_NOT_CAUSAL"}


def _extreme_record(field: str, index: tuple[int, int, int], g1: dict[str, np.ndarray],
                    g2: dict[str, np.ndarray], panel: dict[str, Any], rank_path: str = "G2") -> dict[str, Any]:
    i_b, i_a, i_z = index
    a, b = float(g1[field][index]), float(g2[field][index])
    return {
        "metric": field, "rank_path": rank_path, "province": panel["province"], "turn": panel["turn"],
        "grid_index_zero_based": {"i_b": i_b, "i_a": i_a, "i_z": i_z},
        "coordinate": {"b": float(GRID_B[i_b]), "a": float(GRID_A[i_a]), "z": float(GRID_Z[i_z])},
        "boundary_faces": boundary_faces(index), "g1_value": a, "g2_value": b,
        "g2_minus_g1": b - a, "g2_over_g1": finite_ratio(b, a),
        "rank_abs_value": abs(a if rank_path == "G1" else b),
        "g2_abs_value": abs(b), "liquid_label_transition": f"{g1['liquid_label'][index]}->{g2['liquid_label'][index]}",
        "transfer_label_transition": f"{g1['transfer_label'][index]}->{g2['transfer_label'][index]}",
        "return_regime": panel["g2_return_regime"], "g2_wage_status": panel["g2_wage_status"],
        "convergence_switch": panel["convergence_switch"],
        "comparison_scope": "MATCHED_PROVINCE_TURN_GRID_CELL_WITH_PATH_HISTORY_DIVERGENCE",
    }


def analyze(external_root: Path, output_root: Path) -> None:
    ext, out = Path(external_root), Path(output_root)
    out.mkdir(parents=True, exist_ok=False)
    manifest = verify_external_manifest(ext)
    if manifest["status"] != "PASS":
        raise RuntimeError("external manifest readback failed")

    path_rows = {pid: {turn: {r["province"]: r for r in read_json(
        ext / name / f"turn_{turn:02d}" / "per_province_observables.json")}
        for turn in TURNS} for pid, name in PATHS.items()}
    panel: list[dict[str, Any]] = []
    panel_index: dict[tuple[int, str], dict[str, Any]] = {}
    transition_counts: dict[str, Counter[str]] = {"liquid": Counter(), "transfer": Counter()}
    transition_by_turn: dict[str, dict[int, Counter[str]]] = {
        "liquid": defaultdict(Counter), "transfer": defaultdict(Counter)}
    outward = {pid: Counter() for pid in PATHS}
    extreme_candidates: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    global_candidates: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    threshold_regions: dict[str, dict[str, dict[str, Counter[str]]]] = {
        pid: {field: {str(level): Counter() for level in (1.0e3, 1.0e6)} for field in EXTREME_FIELDS}
        for pid in PATHS}
    distributions: dict[str, dict[str, list[np.ndarray]]] = {
        pid: {field: [] for field in EXTREME_FIELDS} for pid in PATHS}
    boundary_mask = np.zeros((20, 20, 2), dtype=bool)
    boundary_mask[0, :, :] = True; boundary_mask[-1, :, :] = True
    boundary_mask[:, 0, :] = True; boundary_mask[:, -1, :] = True

    for turn in TURNS:
        provinces = list(path_rows["G1"][turn])
        if set(provinces) != set(path_rows["G2"][turn]):
            raise ValueError("province mismatch")
        for province in provinces:
            r1, r2 = path_rows["G1"][turn][province], path_rows["G2"][turn][province]
            switch = convergence_switch(bool(r1["hjb_converged"]), bool(r2["hjb_converged"]))
            row = {
                "province": province, "turn": turn, "province_index": int(r1["province_index"]),
                "comparison_scope": "MATCHED_PROVINCE_TURN_WITH_PATH_HISTORY_DIVERGENCE",
                "convergence_switch": switch, "g1_converged": bool(r1["hjb_converged"]),
                "g2_converged": bool(r2["hjb_converged"]),
                "g1_iterations": int(r1["hjb_iterations"]), "g2_iterations": int(r2["hjb_iterations"]),
                "g1_iteration_ceiling_hit": int(r1["hjb_iterations"]) == ITERATION_CEILING,
                "g2_iteration_ceiling_hit": int(r2["hjb_iterations"]) == ITERATION_CEILING,
                "g1_hjb_statistic": float(r1["hjb_statistic"]), "g2_hjb_statistic": float(r2["hjb_statistic"]),
                "hjb_statistic_g2_minus_g1": float(r2["hjb_statistic"] - r1["hjb_statistic"]),
                "hjb_statistic_g2_over_g1": finite_ratio(float(r2["hjb_statistic"]), float(r1["hjb_statistic"])),
                "g1_raw_firm_ra0": float(r1["firm_ra0"]), "g2_raw_firm_ra0": float(r2["firm_ra0"]),
                "g1_converted_rah_raw": float(r1["raw_converted_rah_annual"]),
                "g2_converted_rah_raw": float(r2["raw_converted_rah_annual"]),
                "g1_consumed_r_a": float(r1["hjb_consumed_r_a"]), "g2_consumed_r_a": float(r2["hjb_consumed_r_a"]),
                "consumed_r_a_g2_minus_g1": float(r2["hjb_consumed_r_a"] - r1["hjb_consumed_r_a"]),
                "g1_return_status": hit_state(r1, "return_guard"), "g2_return_status": hit_state(r2, "return_guard"),
                "g2_return_regime": return_regime(r1, r2), "g2_wage_status": hit_state(r2, "wage_guard"),
                "g2_wage_raw": float(r2["firm_wage_raw"]), "g2_wage_guarded": float(r2["firm_wage_used"]),
                "g2_wage_hit": bool(r2["wage_guard_lower_hit"] or r2["wage_guard_upper_hit"]),
            }
            for prefix, source in (("g1", r1), ("g2", r2)):
                for field in ("transfer", "adjustment_cost", "mu_a", "mu_b"):
                    row[f"{prefix}_{field}_abs_max"] = float(source[f"hjb_{field}_abs_max"])
            panel.append(row); panel_index[(turn, province)] = row

            roots = {pid: ext / name / f"turn_{turn:02d}" / "household" /
                     f"p{int(path_rows[pid][turn][province]['province_index']):02d}_{province}" / "hjb_return.npz"
                     for pid, name in PATHS.items()}
            arrays = {pid: load_arrays(path) for pid, path in roots.items()}
            for label in ("liquid", "transfer"):
                left, right = arrays["G1"][f"{label}_label"], arrays["G2"][f"{label}_label"]
                pairs = np.char.add(np.char.add(left, "->"), right)
                counts = Counter(map(str, pairs.ravel()))
                transition_counts[label].update(counts); transition_by_turn[label][turn].update(counts)
                row[f"{label}_policy_transition_cell_count"] = int(np.count_nonzero(left != right))
            for pid in PATHS:
                ma, mb = arrays[pid]["mu_a"], arrays[pid]["mu_b"]
                outward[pid].update({
                    "lower-a": int(np.count_nonzero(ma[:, 0, :] < -DRIFT_TOLERANCE)),
                    "upper-a": int(np.count_nonzero(ma[:, -1, :] > DRIFT_TOLERANCE)),
                    "lower-b": int(np.count_nonzero(mb[0, :, :] < -DRIFT_TOLERANCE)),
                    "upper-b": int(np.count_nonzero(mb[-1, :, :] > DRIFT_TOLERANCE)),
                })
            row["g2_material_outward_boundary_count"] = int(sum((
                np.count_nonzero(arrays["G2"]["mu_a"][:, 0, :] < -DRIFT_TOLERANCE),
                np.count_nonzero(arrays["G2"]["mu_a"][:, -1, :] > DRIFT_TOLERANCE),
                np.count_nonzero(arrays["G2"]["mu_b"][0, :, :] < -DRIFT_TOLERANCE),
                np.count_nonzero(arrays["G2"]["mu_b"][-1, :, :] > DRIFT_TOLERANCE),
            )))
            for field in EXTREME_FIELDS:
                flat = np.abs(arrays["G2"][field]).ravel()
                top_indices = sorted(range(flat.size), key=lambda item: (-float(flat[item]), item))[:5]
                for flat_index in top_indices:
                    index = tuple(int(x) for x in np.unravel_index(flat_index, arrays["G2"][field].shape))
                    extreme_candidates[(turn, field)].append(_extreme_record(field, index, arrays["G1"], arrays["G2"], row))
                for pid in PATHS:
                    absolute = np.abs(arrays[pid][field])
                    distributions[pid][field].append(absolute.ravel())
                    for level in (1.0e3, 1.0e6):
                        selected = absolute > level
                        threshold_regions[pid][field][str(level)].update({
                            "total": int(np.count_nonzero(selected)),
                            "boundary": int(np.count_nonzero(selected & boundary_mask)),
                            "interior": int(np.count_nonzero(selected & ~boundary_mask)),
                        })
                    local_flat = absolute.ravel()
                    local_top = sorted(range(local_flat.size), key=lambda item: (-float(local_flat[item]), item))[:100]
                    for flat_index in local_top:
                        index = tuple(int(x) for x in np.unravel_index(flat_index, absolute.shape))
                        global_candidates[(pid, field)].append(
                            _extreme_record(field, index, arrays["G1"], arrays["G2"], row, rank_path=pid))

    extremes = []
    for key, values in sorted(extreme_candidates.items()):
        extremes.extend(sorted(values, key=lambda x: (-x["rank_abs_value"], x["province"],
                                                       x["grid_index_zero_based"]["i_b"],
                                                       x["grid_index_zero_based"]["i_a"],
                                                       x["grid_index_zero_based"]["i_z"]))[:5])
    global_top100 = {}
    for (pid, field), values in sorted(global_candidates.items()):
        key = f"{pid}_{field}"
        global_top100[key] = sorted(values, key=lambda x: (-x["rank_abs_value"], x["turn"],
            x["province"], x["grid_index_zero_based"]["i_b"], x["grid_index_zero_based"]["i_a"],
            x["grid_index_zero_based"]["i_z"]))[:100]
    g2_global = [x for key, values in global_top100.items() if key.startswith("G2_") for x in values]
    extreme_policy = {label: Counter(x[f"{label}_label_transition"] for x in g2_global)
                      for label in ("liquid", "transfer")}
    extreme_region = Counter("interior" if x["boundary_faces"] == ["interior"] else "boundary" for x in g2_global)
    extreme_face = Counter(face for x in g2_global for face in x["boundary_faces"] if face != "interior")
    distribution_summary = {pid: {field: {
        "count": int(np.concatenate(values).size),
        "median": float(np.median(np.concatenate(values))),
        "p99": float(np.quantile(np.concatenate(values), .99)),
        "p99_9": float(np.quantile(np.concatenate(values), .999)),
        "max": float(np.max(np.concatenate(values))),
    } for field, values in fields.items()} for pid, fields in distributions.items()}

    switch_by_turn = {turn: defaultdict(list) for turn in TURNS}
    for row in panel:
        switch_by_turn[row["turn"]][row["convergence_switch"]].append(row["province"])
    repeated_loss = Counter(r["province"] for r in panel if r["convergence_switch"] == "G1_CONVERGED_G2_NONCONVERGED")
    regime_groups = {name: group_summary([r for r in panel if r["g2_return_regime"] == name])
                     for name in sorted({r["g2_return_regime"] for r in panel})}
    joint_groups = {f"{regime}__WAGE_{wage}": group_summary([r for r in panel
                    if r["g2_return_regime"] == regime and r["g2_wage_status"] == wage])
                    for regime in sorted({r["g2_return_regime"] for r in panel})
                    for wage in ("LOWER", "UPPER", "UNSATURATED")}

    x_fields = ("consumed_r_a_g2_minus_g1", "g2_converted_rah_raw", "g2_wage_raw", "g2_wage_hit")
    y_fields = ("g2_hjb_statistic", "g2_iteration_ceiling_hit", "g2_transfer_abs_max",
                "g2_adjustment_cost_abs_max", "g2_mu_a_abs_max", "g2_mu_b_abs_max",
                "liquid_policy_transition_cell_count", "transfer_policy_transition_cell_count",
                "g2_material_outward_boundary_count")
    associations = {f"{x}__vs__{y}": association([float(r[x]) for r in panel], [float(r[y]) for r in panel])
                    for x in x_fields for y in y_fields}
    worst = [dict(r) for r in sorted(panel, key=lambda r: r["g2_hjb_statistic"], reverse=True)[:10]]
    for item in worst:
        item["cell_context"] = [x for x in extremes if x["turn"] == item["turn"] and x["province"] == item["province"]]

    science_ledger = {key: 0 for key in ("trajectory", "outer_turn", "hjb", "kfe", "household_runtime",
        "firm_runtime", "matlab_runtime", "k1b", "k2", "ge", "annual_downstream", "shock_irf", "results")}
    summary = {
        "schema": "CH5_K1_G1_VS_G2_HA_HJB_MECHANISM_ZERO_SCIENCE_V1",
        "classification": CLASSIFICATION, "external_manifest_readback": manifest,
        "scientific_call_ledger": science_ledger, "treatment_province_turns": len(panel),
        "comparison_scope": "MATCHED_PROVINCE_TURN_AND_GRID_CELL_WITH_PATH_HISTORY_DIVERGENCE__NOT_CAUSAL",
        "convergence_switch_counts": dict(Counter(r["convergence_switch"] for r in panel)),
        "convergence_switch_provinces_by_turn": {str(t): dict(v) for t, v in switch_by_turn.items()},
        "repeated_g1_converged_to_g2_nonconverged": dict(sorted((k, v) for k, v in repeated_loss.items() if v >= 2)),
        "g2_iteration_ceiling_hits": sum(r["g2_iteration_ceiling_hit"] for r in panel),
        "return_regime_partition": regime_groups, "wage_return_joint_partition": joint_groups,
        "policy_transition_counts": {label: dict(sorted(value.items())) for label, value in transition_counts.items()},
        "policy_transition_counts_by_turn": {label: {str(t): dict(sorted(c.items())) for t, c in values.items()}
                                             for label, values in transition_by_turn.items()},
        "extreme_cell_policy_transitions": {label: dict(sorted(value.items())) for label, value in extreme_policy.items()},
        "material_outward_counts_at_tolerance_1e_12": {pid: dict(value) for pid, value in outward.items()},
        "outward_face_denominator_per_path": 4960,
        "global_top100_per_metric_g2_exclusive_region_counts": dict(sorted(extreme_region.items())),
        "global_top100_per_metric_g2_boundary_face_counts_corner_may_count_twice": dict(sorted(extreme_face.items())),
        "threshold_sensitivity": threshold_regions, "absolute_cell_distribution": distribution_summary,
        "descriptive_associations": associations, "worst_g2_hjb_province_turns": worst,
        "availability": {
            "grid_coordinates": "RECOVERED_FROM_ACCEPTED_GRID_AUTHORITY",
            "value_derivatives": "UNAVAILABLE_IN_ACCEPTED_EVIDENCE",
            "raw_preselector_drifts": "UNAVAILABLE_IN_ACCEPTED_EVIDENCE",
            "standalone_kkt_residual": "UNAVAILABLE_IN_ACCEPTED_EVIDENCE",
            "saved_policy_value_timing": (
                "FINAL_SAVED_POLICY_ARRAYS_ARE_FROM_THE_LAST_POLICY_SELECTION_BEFORE_THE_SAVED_UPDATED_VALUE_SOLVE"
                "__DO_NOT_RECONSTRUCT_EXACT_POLICY_DERIVATIVES_FROM_SAVED_FINAL_VALUE"
            ),
            "saved_hjb_arrays": list(ARRAY_FIELDS),
        },
        "exactly_one_recommended_next_gate": (
            "BOUNDED_DIAGNOSTIC_RUNTIME_WITH_ADDITIONAL_DERIVATIVE_PRESELECTOR_AND_ITERATION_TRACE_INSTRUMENTATION"
            "__NO_SCIENCE_PARAMETER_CHANGE"
        ),
        "kfe_caveat": "ALL_PRIOR_KFE_RESULTS_REMAIN_DIAGNOSTIC_ONLY",
        "results_eligible": False,
    }
    write_json(out / "summary.json", summary)
    write_json(out / "province_turn_panel.json", panel)
    write_json(out / "cell_extremes.json", extremes)
    write_json(out / "global_top100_cells.json", global_top100)
    write_json(out / "descriptive_associations.json", associations)
    write_json(out / "source_availability.json", summary["availability"])
    with (out / "province_turn_panel.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(panel[0])); writer.writeheader(); writer.writerows(panel)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("external_root", type=Path)
    parser.add_argument("output_root", type=Path)
    args = parser.parse_args(argv)
    analyze(args.external_root, args.output_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
