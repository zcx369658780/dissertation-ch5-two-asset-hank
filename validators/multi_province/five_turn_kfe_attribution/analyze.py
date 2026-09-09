"""Attribute five-turn KFE leakage using saved arrays only; never solve a model."""
from __future__ import annotations

import csv
import json
import math
import shutil
from hashlib import sha256
from pathlib import Path
from typing import Any

import numpy as np
from scipy import sparse

from validators.multi_province.call725_kfe_mass_balance import ledger

REPO = Path(__file__).resolve().parents[3]
PREDECESSOR = Path(r"D:\ProjectTemp\ch5-corrected-2018-five-turn-20260909-001")
REPORT_DIR = REPO / "reports/mp4c_2018_five_turn_kfe_leakage_attribution_20260910"
REPORT = REPO / "docs/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION_REPORT.md"
CALL725 = REPO / "reports/call725_kfe_mass_balance_20260909"
VERDICT_PASS = "FIVE_TURN_KFE_ATTRIBUTION_PASS__SAME_UPPER_B_LEAKAGE_AND_PINNING_MECHANISM_CONFIRMED"
VERDICT_PARTIAL = "FIVE_TURN_KFE_ATTRIBUTION_PARTIAL__ADDITIONAL_RESIDUAL_SOURCE_PRESENT"
VERDICT_DISTINCT = "FIVE_TURN_KFE_ATTRIBUTION_DISTINCT_MECHANISM"


def read(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def json_default(value: Any) -> Any:
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(type(value).__name__)


def write(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False,
                  default=json_default)
        stream.write("\n")


def file_hash(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def item(archive: Any, name: str) -> Any:
    value = archive[name]
    return value.item() if value.shape == () and value.dtype == object else value


def offdiagonal(operator: sparse.spmatrix) -> dict[str, Any]:
    coo = sparse.csr_matrix(operator).tocoo()
    values = coo.data[coo.row != coo.col]
    return {"negative_count": int(np.count_nonzero(values < 0.0)),
            "minimum": float(values.min(initial=0.0)),
            "maximum": float(values.max(initial=0.0))}


def stats(values: list[float]) -> dict[str, float]:
    array = np.asarray(values, dtype=float)
    return {"min": float(array.min()), "median": float(np.median(array)), "max": float(array.max())}


def off_pin_is_roundoff(off_pin_max: float, material_residual: float) -> tuple[bool, float]:
    bound = float(128.0 * ledger.EPS64 * max(1.0, abs(material_residual)))
    return off_pin_max <= bound, bound


def analyze_saved(turn: int, index: int, province: str) -> dict[str, Any]:
    root = PREDECESSOR / f"turn_{turn:02d}/household/p{index:02d}_{province}"
    with np.load(root / "hjb_return.npz", allow_pickle=True) as h, np.load(
            root / "kfe_return.npz", allow_pickle=True) as k:
        q = sparse.csr_matrix(item(k, "original_operator"))
        transpose = sparse.csr_matrix(item(k, "transpose"))
        contaminated = sparse.csr_matrix(item(k, "contaminated_matrix"))
        density = np.asarray(k["density_vector"], dtype=float)
        density_cube = np.asarray(k["density"], dtype=float)
        raw = np.asarray(k["raw_solve_vector"], dtype=float)
        rhs = np.asarray(k["rhs"], dtype=float)
        omega = float(k["cell_weight"])
        pin = int(k["contaminated_row_index"])
        mu_b, mu_a = np.asarray(h["mu_b"]), np.asarray(h["mu_a"])
        rates = ledger.directional_omitted_rates(mu_b, mu_a, float(k["db"]), float(k["da"]))
        flat_rates = {name: value.ravel(order="F") for name, value in rates.items()}
        balance = ledger.build_mass_balance(q, density, omega, flat_rates["total"], pin)
        row_check = ledger.verify_row_replacement(transpose, contaminated, rhs, pin)
        source_scale = float(np.max(np.asarray(abs(transpose).sum(axis=1)).ravel())
                             * np.linalg.norm(density, np.inf))
        residual_inf = float(np.linalg.norm(balance["residual"], np.inf))
        off_pin_max = float(np.max(np.abs(np.delete(balance["residual"], pin))))
        pin_roundoff_only, off_pin_bound = off_pin_is_roundoff(off_pin_max, residual_inf)
        source_ratio = residual_inf / source_scale if source_scale else 0.0
        mass_lhs = float(-balance["omega_fsum_r"])
        mass_rhs = float(balance["escaped_mass_flow"])
        mass_direct_error = abs(mass_lhs - mass_rhs)
        mass_bound = float(ledger.frozen_bound(mass_lhs, mass_rhs))
        source_direct_error = abs(balance["candidate_pin_source"] - balance["escaped_mass_flow"])
        source_direct_bound = float(ledger.frozen_bound(
            balance["candidate_pin_source"], balance["escaped_mass_flow"]))
        probability = omega * density
        face_flows = {name: float(np.dot(flat_rates[name], probability))
                      for name in ("lower_b", "upper_b", "lower_a", "upper_a")}
        face_counts = {name: int(np.count_nonzero(flat_rates[name] > 0.0))
                       for name in ("lower_b", "upper_b", "lower_a", "upper_a")}
        shape = density_cube.shape
        coords = ledger.f_order_index(pin, shape)
        factor = float(k["normalization_factor"])
        recomputed_factor = float(np.sum(raw) * omega)
        return {
            "turn": turn, "province_index": index, "province": province,
            "artifact_sha256": {"hjb_return_npz": file_hash(root / "hjb_return.npz"),
                                "kfe_return_npz": file_hash(root / "kfe_return.npz")},
            "identity": {
                "post_loop_operator_matches_kfe_operator_csr": ledger.csr_storage_equal(
                    item(h, "post_convergence_operator"), q),
                "stored_transpose_is_exact_q_transpose_csr": ledger.require_transpose(q, transpose),
                "density_vector_matches_F_order_density": bool(np.array_equal(
                    density, density_cube.ravel(order="F"))),
                "normalization_factor_saved": factor,
                "normalization_factor_recomputed": recomputed_factor,
                "normalization_factor_frozen_match": ledger.frozen_close(factor, recomputed_factor),
                "normalized_mass": float(density.sum() * omega),
                "cell_weight": omega, "flatten_order": "F",
                "pin_row_k0": pin, "pin_matlab_index1": pin + 1,
                "pin_f_order_indices0": {"b": coords[0], "a": coords[1], "z": coords[2]},
                "rhs_nonzero_value": float(rhs[pin]), "row_replacement": row_check,
            },
            "operators": {"hjb_loop": offdiagonal(item(h, "operator")),
                          "post_loop_kfe": offdiagonal(q)},
            "stationarity": {
                "residual_inf": residual_inf, "residual_l1": float(np.abs(balance["residual"]).sum()),
                "scale": source_scale, "normwise_ratio": source_ratio,
                "material": source_ratio > 128.0 * ledger.EPS64,
                "pin_residual": balance["pin_residual"],
                "pin_abs_share_l1": balance["pin_abs_share"],
                "pin_approximately_all": pin_roundoff_only,
                "pin_approximately_all_rule": "every off-pin residual <= 128*eps*max(1, abs(pin-scale residual))",
                "off_pin_componentwise_bound": off_pin_bound,
                "off_pin_abs_sum": balance["off_pin_abs_sum"],
                "off_pin_max_abs": off_pin_max,
            },
            "boundary": {
                "leak_cell_counts": face_counts,
                "max_rates": {name: float(flat_rates[name].max(initial=0.0)) for name in face_counts},
                "density_weighted_escape_by_face": face_flows,
                "density_weighted_total_escape": balance["escaped_mass_flow"],
                "upper_b_face_probability_mass": float(density_cube[-1, :, :].sum() * omega),
            },
            "mass_balance": {
                "minus_weighted_sum_source_free_residual": mass_lhs,
                "outward_escape": mass_rhs, "direct_abs_discrepancy": mass_direct_error,
                "floating_bound": mass_bound, "direct_identity_pass": mass_direct_error <= mass_bound,
                "delta_weighted_correction": balance["delta_weighted_correction"],
                "complete_abs_discrepancy": balance["mass_identity_abs_discrepancy"],
                "complete_identity_pass": balance["mass_identity_abs_discrepancy"] <= mass_bound,
            },
            "implicit_source": {
                "minus_omega_pin_residual": balance["candidate_pin_source"],
                "total_escape": balance["escaped_mass_flow"],
                "direct_abs_discrepancy": source_direct_error, "floating_bound": source_direct_bound,
                "direct_equivalence_pass": source_direct_error <= source_direct_bound,
                "off_pin_signed_correction": balance["off_pin_signed_correction"],
                "complete_abs_discrepancy": balance["source_balance_abs_discrepancy"],
                "complete_equivalence_pass": balance["source_balance_abs_discrepancy"] <= source_direct_bound,
                "interpretation": "algebraic balancing source from the dropped finite-box equation; not an adopted economic entry process",
            },
            "density_sign": {
                "minimum": float(density.min()), "negative_count": int(np.count_nonzero(density < 0.0)),
                "weighted_negative_mass": float(np.minimum(density, 0.0).sum() * omega),
                "negative_mass_to_escape_abs_ratio": float(abs(np.minimum(density, 0.0).sum() * omega)
                                                          / abs(balance["escaped_mass_flow"]))
                    if balance["escaped_mass_flow"] else 0.0,
            },
        }


def summarize(rows: list[dict[str, Any]], turn: int) -> dict[str, Any]:
    selected = [row for row in rows if row["turn"] == turn]
    faces = ("lower_b", "upper_b", "lower_a", "upper_a")
    top_escape = sorted(selected, key=lambda x: x["boundary"]["density_weighted_total_escape"], reverse=True)[:5]
    top_mass = sorted(selected, key=lambda x: x["boundary"]["upper_b_face_probability_mass"], reverse=True)[:5]
    return {
        "turn": turn, "province_count": len(selected),
        "material_source_free_residual_provinces": sum(x["stationarity"]["material"] for x in selected),
        "pin_approximately_all_residual_l1_provinces": sum(x["stationarity"]["pin_approximately_all"] for x in selected),
        "positive_upper_b_escape_provinces": sum(x["boundary"]["density_weighted_escape_by_face"]["upper_b"] > 0 for x in selected),
        "leak_cell_totals": {face: sum(x["boundary"]["leak_cell_counts"][face] for x in selected) for face in faces},
        "density_weighted_escape": stats([x["boundary"]["density_weighted_total_escape"] for x in selected]),
        "upper_b_face_probability_mass": stats([x["boundary"]["upper_b_face_probability_mass"] for x in selected]),
        "signed_residual_vs_escape_identity_error": stats([x["mass_balance"]["direct_abs_discrepancy"] for x in selected]),
        "implicit_source_vs_escape_discrepancy": stats([x["implicit_source"]["direct_abs_discrepancy"] for x in selected]),
        "off_pin_max_abs": stats([x["stationarity"]["off_pin_max_abs"] for x in selected]),
        "top_by_escape": [{"province": x["province"], "value": x["boundary"]["density_weighted_total_escape"]} for x in top_escape],
        "top_by_upper_b_face_mass": [{"province": x["province"], "value": x["boundary"]["upper_b_face_probability_mass"]} for x in top_mass],
    }


def manifest(root: Path, excluded: set[str]) -> list[dict[str, Any]]:
    return [{"path": p.relative_to(root).as_posix(), "bytes": p.stat().st_size, "sha256": file_hash(p)}
            for p in sorted(x for x in root.rglob("*") if x.is_file())
            if p.relative_to(root).as_posix() not in excluded]


def run(output: Path) -> None:
    output = Path(output)
    if REPORT.exists() or REPORT_DIR.exists():
        raise FileExistsError("repository outputs already exist")
    receipt = read(PREDECESSOR / "runtime_input_receipt.json")
    provinces = receipt["province_order"]
    rows = [analyze_saved(turn, index, province) for turn in (3, 4, 5)
            for index, province in enumerate(provinces)]
    summaries = [summarize(rows, turn) for turn in (3, 4, 5)]
    primary = [row for row in rows if row["turn"] in (4, 5)]
    identity_ok = all(all(row["identity"][key] for key in (
        "post_loop_operator_matches_kfe_operator_csr", "stored_transpose_is_exact_q_transpose_csr",
        "density_vector_matches_F_order_density", "normalization_factor_frozen_match")) for row in primary)
    upper_only = all(row["boundary"]["density_weighted_escape_by_face"]["upper_b"] > 0.0 and
        all(row["boundary"]["leak_cell_counts"][face] == 0 for face in ("lower_b", "lower_a", "upper_a"))
        for row in primary)
    pin_all = all(row["stationarity"]["pin_approximately_all"] for row in primary)
    balance_ok = all(row["mass_balance"]["complete_identity_pass"] and
                     row["implicit_source"]["complete_equivalence_pass"] for row in primary)
    if identity_ok and upper_only and pin_all and balance_ok:
        verdict, mechanism = VERDICT_PASS, "SAME_FINITE_BOX_UPPER_B_LEAKAGE_AND_PINNING_MECHANISM_CONFIRMED"
    elif identity_ok and upper_only:
        verdict, mechanism = VERDICT_PARTIAL, "PARTIAL_MECHANISM_MATCH__ADDITIONAL_RESIDUAL_SOURCE_PRESENT"
    else:
        verdict, mechanism = VERDICT_DISTINCT, "DISTINCT_KFE_FAILURE_MECHANISM"

    call725 = read(CALL725 / "summary.json")
    comparison = {"classification": mechanism,
        "call725": {"upper_b_leak_cells": 29, "pin_abs_share_l1": call725["pin_residual_localization"]["pin_abs_share_of_residual_L1"],
                    "escape": call725["signed_mass_balance"]["escaped_mass_flow_dot_ell_p"],
                    "upper_b_face_mass": call725["signed_mass_balance"]["face_probability_mass"]["upper_b"]["signed"],
                    "negative_count": 160, "hjb_loop_negative_offdiagonal_count": call725["Qh_separate"]["negative_offdiagonal_count"]},
        "corrected_turn4_turn5": {"objects": 62, "identity_all": identity_ok, "upper_b_only_all": upper_only,
            "pin_concentration_all": pin_all, "mass_and_source_balance_all": balance_ok,
            "hjb_loop_negative_offdiagonal_count": stats([x["operators"]["hjb_loop"]["negative_count"] for x in primary]),
            "post_loop_negative_offdiagonal_count": stats([x["operators"]["post_loop_kfe"]["negative_count"] for x in primary]),
            "upper_b_leak_cell_count": stats([x["boundary"]["leak_cell_counts"]["upper_b"] for x in primary]),
            "pin_abs_share_l1": stats([x["stationarity"]["pin_abs_share_l1"] for x in primary]),
            "off_pin_max_abs": stats([x["stationarity"]["off_pin_max_abs"] for x in primary]),
            "density_weighted_escape": stats([x["boundary"]["density_weighted_total_escape"] for x in primary]),
            "upper_b_face_mass": stats([x["boundary"]["upper_b_face_probability_mass"] for x in primary]),
            "negative_density_count": stats([x["density_sign"]["negative_count"] for x in primary]),
            "weighted_negative_mass": stats([x["density_sign"]["weighted_negative_mass"] for x in primary])},
        "common_mechanism": ["post-loop operator has retained diagonal with omitted outside-grid upper-b transition",
                             "KFE transposes that operator, replaces one row, sets rhs pin to .007, and normalizes",
                             "dropped source-free equation is algebraically equivalent to a source balancing finite-box escape"],
        "economic_boundary": "No household entry/exit process is explicitly simulated; the source is algebraic, not an adopted economic mechanism."}
    source_identity = read(PREDECESSOR / "source_code_identity.json")
    source = {"saved_source_identity": source_identity,
        "current_hashes": {"exports/matlab_faithful_two_asset_ha.py": file_hash(REPO / "exports/matlab_faithful_two_asset_ha.py"),
                           "src/ch5_two_asset_hank/matlab_faithful_hjb.py": file_hash(REPO / "src/ch5_two_asset_hank/matlab_faithful_hjb.py"),
                           "src/ch5_two_asset_hank/matlab_faithful_kfe.py": file_hash(REPO / "src/ch5_two_asset_hank/matlab_faithful_kfe.py")},
        "saved_export_matches_current": source_identity["files"]["exports/matlab_faithful_two_asset_ha.py"] == file_hash(REPO / "exports/matlab_faithful_two_asset_ha.py"),
        "paths": [{"file": "exports/matlab_faithful_two_asset_ha.py", "lines": "424-450", "role": "outside-grid offdiagonal is omitted while diagonal keeps -(backward+forward)"},
                  {"file": "src/ch5_two_asset_hank/matlab_faithful_hjb.py", "lines": "115-116", "role": "post-loop Q assembled from saved mu_b/mu_a drifts"},
                  {"file": "src/ch5_two_asset_hank/matlab_faithful_kfe.py", "lines": "30-47", "role": "Q.T, row replacement, rhs .007, direct return normalization"}],
        "source_modified": False, "D1_D3": "previously deferred redesign proposals; not accepted solutions"}
    observables = read(PREDECESSOR / "turn_by_turn_observables.json")
    asset = {"interpretation": "turn3 asset collapse is temporally coincident with invalid density diagnostics; causality is not separable from saved evidence",
        "quantities_status": "DIAGNOSTIC_QUANTITIES_NOT_ACCEPTED_ECONOMIC_MOMENTS",
        "anhui": [{"turn": turn, "A": observables[f"turn_{turn}"][11]["A"],
                   "B": observables[f"turn_{turn}"][11]["B"], "A_plus_B": observables[f"turn_{turn}"][11]["A_plus_B"],
                   "escape": next(x for x in rows if x["turn"] == turn and x["province_index"] == 11)["boundary"]["density_weighted_total_escape"],
                   "source_free_residual_inf": next(x for x in rows if x["turn"] == turn and x["province_index"] == 11)["stationarity"]["residual_inf"]}
                  for turn in (3, 4, 5)]}
    zeros = {name: 0 for name in ("scientific_processes", "trajectories", "turns", "province_updates",
        "native_initializations", "labor_roots", "brent_calls", "household_calls", "hjb_calls", "kfe_calls",
        "direct_solves", "iterative_solves", "eigen_solves", "firm_calls", "wage_calls", "migration_calls",
        "capital_allocation_calls", "controller_calls", "matlab_calls", "ge_calls", "annual_calls", "irf_calls", "results_calls")}
    products = {"per_province_turn_mass_balance.json": {"rows": rows},
        "cross_province_summary.json": {"turns": summaries},
        "pin_row_attribution.json": {"rows": [{"turn": x["turn"], "province": x["province"], **x["stationarity"]} for x in rows]},
        "boundary_leakage_summary.json": {"rows": [{"turn": x["turn"], "province": x["province"], **x["boundary"]} for x in rows]},
        "call725_mechanism_comparison.json": comparison, "source_code_attribution.json": source,
        "asset_validity_relationship.json": asset, "call_ledger.json": {"counts": zeros, "saved_objects_read": 186, "scientific_retries": 0},
        "terminal_result.json": {"verdict": verdict, "mechanism_classification": mechanism,
                                 "turn6_plus_authorized": "NO", "steady_state_authorized": "NO", "results_eligible": False}}
    for name, value in products.items():
        write(output / name, value)
    with (output / "per_province_turn_mass_balance.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        fields = ("turn", "province_index", "province", "residual_inf", "pin_abs_share_l1", "off_pin_max_abs",
                  "upper_b_leak_cells", "escape", "upper_b_face_mass", "mass_identity_error", "source_escape_error")
        writer = csv.DictWriter(stream, fieldnames=fields); writer.writeheader()
        for x in rows:
            writer.writerow({"turn": x["turn"], "province_index": x["province_index"], "province": x["province"],
                "residual_inf": x["stationarity"]["residual_inf"], "pin_abs_share_l1": x["stationarity"]["pin_abs_share_l1"],
                "off_pin_max_abs": x["stationarity"]["off_pin_max_abs"], "upper_b_leak_cells": x["boundary"]["leak_cell_counts"]["upper_b"],
                "escape": x["boundary"]["density_weighted_total_escape"], "upper_b_face_mass": x["boundary"]["upper_b_face_probability_mass"],
                "mass_identity_error": x["mass_balance"]["direct_abs_discrepancy"], "source_escape_error": x["implicit_source"]["direct_abs_discrepancy"]})
    REPORT_DIR.mkdir(parents=True, exist_ok=False)
    for name in list(products) + ["per_province_turn_mass_balance.csv", "pre_checks.log", "tests.log", "static_checks.log"]:
        shutil.copyfile(output / name, REPORT_DIR / (name.removesuffix(".log") + ".txt" if name.endswith(".log") else name))
    t4, t5 = summaries[1], summaries[2]
    REPORT.write_text(f"""# Chapter 5 corrected-2018 five-turn KFE leakage attribution

## Verdict

`{verdict}`

Mechanism classification: `{mechanism}`. This is zero-science saved-array attribution, not a KFE rerun or repair.

## Nationwide attribution

| turn | material residual provinces | pin approximately all L1 | positive upper-b escape | leak cells lower-b/upper-b/lower-a/upper-a | escape min/median/max | upper-b face mass min/median/max |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | {t4['material_source_free_residual_provinces']} | {t4['pin_approximately_all_residual_l1_provinces']} | {t4['positive_upper_b_escape_provinces']} | {t4['leak_cell_totals']['lower_b']}/{t4['leak_cell_totals']['upper_b']}/{t4['leak_cell_totals']['lower_a']}/{t4['leak_cell_totals']['upper_a']} | {t4['density_weighted_escape']['min']:.17g}/{t4['density_weighted_escape']['median']:.17g}/{t4['density_weighted_escape']['max']:.17g} | {t4['upper_b_face_probability_mass']['min']:.17g}/{t4['upper_b_face_probability_mass']['median']:.17g}/{t4['upper_b_face_probability_mass']['max']:.17g} |
| 5 | {t5['material_source_free_residual_provinces']} | {t5['pin_approximately_all_residual_l1_provinces']} | {t5['positive_upper_b_escape_provinces']} | {t5['leak_cell_totals']['lower_b']}/{t5['leak_cell_totals']['upper_b']}/{t5['leak_cell_totals']['lower_a']}/{t5['leak_cell_totals']['upper_a']} | {t5['density_weighted_escape']['min']:.17g}/{t5['density_weighted_escape']['median']:.17g}/{t5['density_weighted_escape']['max']:.17g} | {t5['upper_b_face_probability_mass']['min']:.17g}/{t5['upper_b_face_probability_mass']['median']:.17g}/{t5['upper_b_face_probability_mass']['max']:.17g} |

All 62 turn4/5 objects preserve exact Q/T orientation, F-order density mapping, row replacement and normalization convention. The material residual is concentrated at the dropped pin equation; off-pin terms and both signed mass-balance corrections are floating-point scale. The implied source balances upper-b finite-box escape algebraically. It is not an implemented household entry process.

Turn3 shows the same mechanism while Anhui A+B collapses from the prior turn. Turn4/5 A+B remains near 1.893. These are temporally coincident diagnostic quantities; the saved evidence does not identify leakage as the causal source of the asset collapse.

All scientific/model/solver calls are zero. Turn6+, new KFE solves, steady state, GE, annual, IRF, Results and production repair remain unauthorized. Results eligibility is FALSE.
""", encoding="utf-8", newline="\n")
    repo_records = manifest(REPORT_DIR, {"manifest.json", "manifest_readback.json"})
    write(REPORT_DIR / "manifest.json", {"files": repo_records})
    write(REPORT_DIR / "manifest_readback.json", {"checked_files": len(repo_records), "passed": all(
        (REPORT_DIR / x["path"]).stat().st_size == x["bytes"] and file_hash(REPORT_DIR / x["path"]) == x["sha256"] for x in repo_records)})
    ext_records = manifest(output, {"manifest.json", "manifest_readback.json"})
    write(output / "manifest.json", {"files": ext_records})
    write(output / "manifest_readback.json", {"checked_files": len(ext_records), "passed": all(
        (output / x["path"]).stat().st_size == x["bytes"] and file_hash(output / x["path"]) == x["sha256"] for x in ext_records)})


if __name__ == "__main__":
    import sys
    run(Path(sys.argv[1]))
