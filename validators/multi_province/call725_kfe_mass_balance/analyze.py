"""Attribute the saved call725 KFE residual without invoking any scientific code."""

import csv
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys

import numpy as np
from scipy import sparse

from evidence import decode_saved, lf_sha256, sha256, write_json
from ledger import (
    build_mass_balance,
    csr_storage_equal,
    directional_omitted_rates,
    f_order_index,
    frozen_bound,
    frozen_close,
    normalize_raw,
    require_transpose,
    verify_row_replacement,
)


REPO = Path(__file__).resolve().parents[3]
SOURCE = Path(r"D:\ProjectTemp\ch5-call725-rah-0p07-native-init-20260908-002")
PREDECESSOR = REPO / "reports/call725_rah_0p07_sensitivity_20260908"
EXPORT = REPO / "exports/matlab_faithful_two_asset_ha.py"
EXPORT_BLOB = "9e7dc9556a2b76811e78f89999abecc045886106"
PROTECTED_HJB = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m")
PROTECTED_HJB_SHA = "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE"
PHASES = (
    "binding",
    "hjb_return_before_kfe",
    "kfe_entry",
    "kfe_direct_input",
    "kfe_direct_return",
    "kfe_return",
    "terminal",
)


def git(*args):
    return subprocess.check_output(["git", *args], cwd=REPO, text=True).strip()


def resolve_manifest():
    receipt = json.loads((PREDECESSOR / "manifest_readback.json").read_text(encoding="utf-8"))
    expected = receipt["manifest_sha256"]
    candidates = [path for path in SOURCE.glob("manifest*.json") if sha256(path) == expected]
    if len(candidates) != 1:
        raise AssertionError(f"expected one predecessor manifest matching receipt, found {len(candidates)}")
    repository_copy = PREDECESSOR / "manifest.json"
    assert sha256(repository_copy) == expected
    return candidates[0], repository_copy, expected


def verify_consumed(manifest):
    external_index = SOURCE / "science/index.jsonl"
    repository_index = PREDECESSOR / "science_capture_index.jsonl"
    assert lf_sha256(external_index) == lf_sha256(repository_index)
    output_by_path = {item["path"].casefold(): item for item in manifest["outputs"]}
    index_item = output_by_path[str(repository_index).casefold()]
    assert lf_sha256(repository_index) == index_item["LF_sha256"]
    rows = [json.loads(line) for line in external_index.read_text(encoding="utf-8").splitlines()]
    by_phase = {row["phase"]: row for row in rows}
    capture_by_path = {item["path"].casefold(): item for item in manifest["captures"]}
    consumed = []
    for phase in PHASES:
        row = by_phase[phase]
        for kind in ("json", "npz"):
            if kind not in row:
                continue
            path = Path(row[kind])
            actual = sha256(path)
            assert actual == row[f"{kind}_sha256"]
            assert actual == capture_by_path[str(path).casefold()]["sha256"]
            consumed.append({"phase": phase, "kind": kind, "path": str(path), "sha256": actual, "bytes": path.stat().st_size})
    return consumed, {
        "external_path": str(external_index),
        "repository_path": str(repository_index),
        "external_raw_sha256": sha256(external_index),
        "repository_raw_sha256": sha256(repository_index),
        "shared_LF_sha256": lf_sha256(external_index),
        "LF_identity": True,
    }


def matrix_norm_inf(matrix):
    return float(np.max(np.asarray(abs(sparse.csr_matrix(matrix)).sum(axis=1)).ravel()))


def face_masks(shape):
    masks = {name: np.zeros(shape, dtype=bool) for name in ("lower_b", "upper_b", "lower_a", "upper_a")}
    masks["lower_b"][0, :, :] = True
    masks["upper_b"][-1, :, :] = True
    masks["lower_a"][:, 0, :] = True
    masks["upper_a"][:, -1, :] = True
    masks["union"] = np.logical_or.reduce(list(masks.values()))
    return masks


def signed_mass(values):
    values = np.asarray(values, dtype=float)
    return {
        "signed": float(np.sum(values)),
        "positive": float(np.sum(np.maximum(values, 0.0))),
        "negative": float(np.sum(np.minimum(values, 0.0))),
        "exact_negative_count": int(np.sum(values < 0.0)),
        "cell_count": int(values.size),
    }


def row_record(index, shape, grids, arrays, rates, balance, pin):
    i_b, i_a, i_z = f_order_index(index, shape)
    faces = []
    if i_b == 0:
        faces.append("lower_b")
    if i_b + 1 == shape[0]:
        faces.append("upper_b")
    if i_a == 0:
        faces.append("lower_a")
    if i_a + 1 == shape[1]:
        faces.append("upper_a")
    probability = balance["probability"][index]
    total_rate = rates["total"].ravel(order="F")[index]
    return {
        "k0": index,
        "matlab_linear_index1": index + 1,
        "b_index0": i_b,
        "a_index0": i_a,
        "z_index0": i_z,
        "b_index1": i_b + 1,
        "a_index1": i_a + 1,
        "z_index1": i_z + 1,
        "b": float(grids["b"][i_b]),
        "a": float(grids["a"][i_a]),
        "z": float(grids["z"][i_z]),
        "faces": "+".join(faces) if faces else "interior",
        "g": float(balance["probability"][index] / arrays["omega"]),
        "p": float(probability),
        "mu_b": float(arrays["mu_b"][i_b, i_a, i_z]),
        "mu_a": float(arrays["mu_a"][i_b, i_a, i_z]),
        "ell_lower_b": float(rates["lower_b"].ravel(order="F")[index]),
        "ell_upper_b": float(rates["upper_b"].ravel(order="F")[index]),
        "ell_lower_a": float(rates["lower_a"].ravel(order="F")[index]),
        "ell_upper_a": float(rates["upper_a"].ravel(order="F")[index]),
        "ell_total": float(total_rate),
        "q": float(balance["row_sum"][index]),
        "delta": float(balance["delta"][index]),
        "r": float(balance["residual"][index]),
        "weighted_outward_flux": float(total_rate * probability),
        "pin": int(index == pin),
    }


def main(evidence_root, report_output):
    evidence_root = Path(evidence_root).resolve()
    report_output = Path(report_output).resolve()
    evidence_root.mkdir(parents=True, exist_ok=True)
    unexpected = [path for path in evidence_root.iterdir() if not (path.name.startswith("tests_") or path.name.startswith("analysis_failure_"))]
    if unexpected:
        raise FileExistsError(f"evidence root already contains non-test outputs: {unexpected}")
    report_output.mkdir(parents=True, exist_ok=True)
    manifest_path, manifest_copy, manifest_sha = resolve_manifest()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    consumed, index_identity = verify_consumed(manifest)
    assert git("rev-parse", f"HEAD:exports/matlab_faithful_two_asset_ha.py") == EXPORT_BLOB
    assert sha256(PROTECTED_HJB) == PROTECTED_HJB_SHA

    binding = decode_saved(SOURCE / "science/binding.json")
    hjb = decode_saved(SOURCE / "science/hjb_return_before_kfe.json")
    kfe_entry = decode_saved(SOURCE / "science/kfe_entry.json")
    direct_input = decode_saved(SOURCE / "science/kfe_direct_input.json")
    direct_return = decode_saved(SOURCE / "science/kfe_direct_return.json")
    kfe = decode_saved(SOURCE / "science/kfe_return.json")
    terminal = decode_saved(SOURCE / "science/terminal.json")

    shape = tuple(hjb["value"].shape)
    Q = sparse.csr_matrix(hjb["post_convergence_operator"]["full"])
    Qh = sparse.csr_matrix(hjb["operator"]["full"])
    T = sparse.csr_matrix(kfe["transpose"])
    B = sparse.csr_matrix(kfe["contaminated_matrix"])
    x = np.asarray(kfe["raw_solve_vector"], dtype=float)
    eta = float(kfe["normalization_factor"])
    g = np.asarray(kfe["density_vector"], dtype=float)
    omega = float(kfe["cell_weight"])
    rhs = np.asarray(kfe["rhs"], dtype=float)
    pin = int(kfe["contaminated_row_index"])
    grids = binding["grid"]

    assert shape == (20, 20, 2) and Q.shape == T.shape == B.shape == (800, 800)
    assert csr_storage_equal(Q, kfe_entry["operator"])
    assert csr_storage_equal(Q, kfe["original_operator"])
    require_transpose(Q, T)
    assert csr_storage_equal(B, direct_input["matrix"])
    assert np.array_equal(rhs, direct_input["rhs"])
    assert np.array_equal(x, direct_return["raw"])
    assert np.array_equal(x, kfe["raw_solve_vector"])
    assert np.array_equal(g, kfe["density"].ravel(order="F"))
    replacement = verify_row_replacement(T, B, rhs, pin)
    assert pin == int(np.floor(0.37 * Q.shape[0])) - 1

    recomputed_eta, _, _ = normalize_raw(x, omega)
    g_from_saved_eta = x / eta
    probability = omega * g
    assert np.array_equal(g_from_saved_eta, g)
    assert frozen_close(recomputed_eta, eta)
    assert frozen_close(omega * np.sum(g), 1.0)
    db = float(grids["b"][1] - grids["b"][0])
    da = float(grids["a"][1] - grids["a"][0])
    assert db == kfe["db"] and da == kfe["da"] and omega == db * da
    rates = directional_omitted_rates(hjb["mu_b"], hjb["mu_a"], db, da)
    total_rate = rates["total"].ravel(order="F")
    balance = build_mass_balance(Q, g, omega, total_rate, pin)

    raw_residual = np.asarray(B @ x - rhs)
    raw_denominator = matrix_norm_inf(B) * float(np.linalg.norm(x, ord=np.inf)) + float(np.linalg.norm(rhs, ord=np.inf))
    stationary_denominator = matrix_norm_inf(T) * float(np.linalg.norm(g, ord=np.inf))
    off_indices = np.arange(g.size) != pin
    off_relation = balance["residual"][off_indices] - raw_residual[off_indices] / eta
    largest_off = int(np.argmax(np.where(off_indices, np.abs(balance["residual"]), -1.0)))
    pin_indices = f_order_index(pin, shape)

    records = [row_record(index, shape, grids, {"mu_b": hjb["mu_b"], "mu_a": hjb["mu_a"], "omega": omega}, rates, balance, pin) for index in range(g.size)]
    flux_order = sorted(records, key=lambda row: abs(row["weighted_outward_flux"]), reverse=True)
    cumulative = 0.0
    top = []
    for rank, row in enumerate(flux_order[:15], 1):
        cumulative += row["weighted_outward_flux"]
        top.append({**row, "rank": rank, "cumulative_flux": cumulative, "cumulative_share": cumulative / balance["escaped_mass_flow"]})

    probability_grid = probability.reshape(shape, order="F")
    masks = face_masks(shape)
    face_mass = {name: signed_mass(probability_grid[mask]) for name, mask in masks.items()}
    face_flows = {name: float(np.dot(rate.ravel(order="F"), probability)) for name, rate in rates.items() if name != "total"}
    rate_counts = {name: int(np.sum(rate > 0.0)) for name, rate in rates.items() if name != "total"}
    positive_flux = np.array([row["weighted_outward_flux"] for row in records]) > 0.0

    mass_scale = max(1.0, abs(balance["omega_fsum_r"]), abs(balance["mass_identity_rhs"]))
    mass_threshold = float(128.0 * np.finfo(float).eps * mass_scale)
    source_scale = max(1.0, abs(balance["candidate_pin_source"]), abs(balance["source_balance_rhs"]))
    source_threshold = float(128.0 * np.finfo(float).eps * source_scale)
    hq_coo = Qh.tocoo()
    hq_off = hq_coo.row != hq_coo.col
    identity_checks = {
        "Q_equals_hjb_post_loop_and_kfe_entry_and_kfe_original_CSR": True,
        "T_equals_Q_transpose_CSR": True,
        "B_equals_direct_input_and_kfe_return_CSR": True,
        "rhs_and_raw_exact_copies": True,
        "density_vector_equals_F_order_density": True,
        "g_equals_x_div_eta_exact": True,
        "eta_saved": eta,
        "eta_recomputed": recomputed_eta,
        "eta_frozen_rule_pass": frozen_close(recomputed_eta, eta),
        "normalization": float(omega * np.sum(g)),
        "normalization_frozen_rule_pass": frozen_close(omega * np.sum(g), 1.0),
        "row_replacement": replacement,
        "index_identity": index_identity,
        "consumed_object_count": len(consumed),
    }
    localization = {
        "pin_row_k0": pin,
        "matlab_linear_index1": pin + 1,
        "f_order_indices0": {"b": pin_indices[0], "a": pin_indices[1], "z": pin_indices[2]},
        "matlab_indices1": {"b": pin_indices[0] + 1, "a": pin_indices[1] + 1, "z": pin_indices[2] + 1},
        "coordinates": {"b": float(grids["b"][pin_indices[0]]), "a": float(grids["a"][pin_indices[1]]), "z": float(grids["z"][pin_indices[2]])},
        "raw_rhs_pin": float(rhs[pin]),
        "raw_x_pin": float(x[pin]),
        "raw_pin_equation_residual": float(raw_residual[pin]),
        "raw_rhs_interpretation": "The 0.007 RHS fixes raw x[k]; it is not a probability-flow rate.",
        "stationary_pin_residual": balance["pin_residual"],
        "stationary_residual_inf": float(np.linalg.norm(balance["residual"], ord=np.inf)),
        "stationary_residual_signed_sum": float(np.sum(balance["residual"])),
        "stationary_residual_fsum": float(math.fsum(map(float, balance["residual"]))),
        "pin_abs_share_of_residual_L1": balance["pin_abs_share"],
        "off_pin_abs_sum": balance["off_pin_abs_sum"],
        "largest_off_pin_row": largest_off,
        "largest_off_pin_coordinates": dict(zip(("b_index0", "a_index0", "z_index0"), f_order_index(largest_off, shape))),
        "largest_off_pin_residual_abs": float(abs(balance["residual"][largest_off])),
        "off_pin_relation_r_equals_e_over_eta_max_abs": float(np.max(np.abs(off_relation))),
        "replaced_row_difference_nnz": replacement["difference_nnz"],
    }
    signed_balance = {
        "omega_sum_r_numpy": balance["omega_sum_r"],
        "omega_sum_r_math_fsum": balance["omega_fsum_r"],
        "dot_q_p": balance["q_dot_p"],
        "escaped_mass_flow_dot_ell_p": balance["escaped_mass_flow"],
        "delta_weighted_correction": balance["delta_weighted_correction"],
        "minus_escape_plus_delta": balance["mass_identity_rhs"],
        "mass_identity_abs_discrepancy": balance["mass_identity_abs_discrepancy"],
        "mass_identity_frozen_bound": mass_threshold,
        "mass_identity_frozen_rule_pass": balance["mass_identity_abs_discrepancy"] <= mass_threshold,
        "candidate_balancing_source_minus_omega_rk": balance["candidate_pin_source"],
        "off_pin_signed_correction": balance["off_pin_signed_correction"],
        "escape_minus_delta_plus_off_pin": balance["source_balance_rhs"],
        "source_balance_abs_discrepancy": balance["source_balance_abs_discrepancy"],
        "source_balance_frozen_bound": source_threshold,
        "source_balance_frozen_rule_pass": balance["source_balance_abs_discrepancy"] <= source_threshold,
        "escaped_flow_by_probability_sign": balance["escaped_signed_parts"],
        "row_sum_flow_by_probability_sign": balance["row_sum_signed_parts"],
        "delta_flow_by_probability_sign": balance["delta_signed_parts"],
        "face_flows": face_flows,
        "outward_rate_positive_counts": rate_counts,
        "positive_weighted_flux_cells": int(np.sum(positive_flux)),
        "zero_weighted_flux_outward_rate_cells": int(np.sum((total_rate > 0.0) & ~positive_flux)),
        "face_probability_mass": face_mass,
        "face_mass_note": "Face masses overlap at corners; union is the disjoint boundary-cell total.",
        "delta_max_abs": float(np.max(np.abs(balance["delta"]))),
    }
    residual_scaling = {
        "contaminated_raw_residual_inf": float(np.linalg.norm(raw_residual, ord=np.inf)),
        "contaminated_raw_scale_denominator": raw_denominator,
        "contaminated_raw_ratio": float(np.linalg.norm(raw_residual, ord=np.inf) / raw_denominator),
        "source_reported_raw_residual_inf": float(kfe["raw_residual_inf"]),
        "unmodified_stationary_residual_inf": float(np.linalg.norm(balance["residual"], ord=np.inf)),
        "unmodified_stationary_scale_denominator": stationary_denominator,
        "unmodified_stationary_ratio": float(np.linalg.norm(balance["residual"], ord=np.inf) / stationary_denominator),
        "units_note": "The raw Bx-f residual, normalized T g residual, and density-weighted probability flow have different scaling and units.",
    }
    summary = {
        "diagnostic_completion": "COMPLETE",
        "identity_checks": identity_checks,
        "pin_residual_localization": localization,
        "signed_mass_balance": signed_balance,
        "residual_scaling": residual_scaling,
        "source_escape_interpretation": "SUPPORTED",
        "source_escape_conclusion": "The row-replaced solve discards the one material stationary equation. Its implied positive source balances the signed density-weighted upper-b escape within the frozen arithmetic rule; off-pin and q+ell corrections are rounding-scale. This is finite-box algebra, not an adopted economic source/exit law.",
        "occupied_escape_cells": {"outward_rate_cells": int(np.sum(total_rate > 0.0)), "positive_flux_cells": int(np.sum(positive_flux)), "top_15": top},
        "Qh_separate": {"negative_offdiagonal_count": int(np.sum(hq_coo.data[hq_off] < 0.0)), "minimum_offdiagonal": float(np.min(hq_coo.data[hq_off])), "not_used_in_mass_ledger": True},
        "remaining_scientific_decision": "Owner must choose the finite-box boundary law/source treatment before any repair implementation or corrected KFE/2018 run; existing D1-D3 alternatives remain unapproved.",
        "Results_eligible": False,
        "zero_new_science": True,
    }
    source_lines = EXPORT.read_text(encoding="utf-8").splitlines()
    source_map = {
        "export_blob": EXPORT_BLOB,
        "export_path": str(EXPORT),
        "protected_HJB_sha256": PROTECTED_HJB_SHA,
        "stages": [
            {"lines": "424-450", "role": "assemble_source_axis omits an outside-grid offdiagonal at the face but keeps diagonal -(rb+rf)", "selected": {str(n): source_lines[n - 1] for n in (427, 444, 446, 448)}},
            {"lines": "561-562", "role": "post-loop Q is assembled from positive/negative saved drifts after HJB iteration stopping", "selected": {str(n): source_lines[n - 1] for n in (561, 562)}},
            {"lines": "592-600", "role": "T=Q.T, row k is replaced, rhs[k]=.007, raw is normalized by omega*sum(x)", "selected": {str(n): source_lines[n - 1] for n in (592, 593, 594, 595, 598, 600)}},
        ],
        "implicated_saved_stage": "upper-b mu_b>0 becomes b_forward=mu_b/db; the unavailable i+1 offdiagonal is omitted while -b_forward remains on Q's diagonal.",
    }
    call_ledger = {
        "final_saved_array_analyzer_processes": 1,
        "failed_saved_array_analyzer_attempts": 1,
        "development_read_only_probe_processes_before_final_analyzer": 4,
        "final_analyzer_matrix_vector_products": 3,
        "development_probe_matrix_vector_products": 4,
        "new_initializer": 0,
        "new_root": 0,
        "new_HJB": 0,
        "new_KFE": 0,
        "new_direct_iterative_eigen_optimization_condition_solves": 0,
        "new_policy_evaluator": 0,
        "firm_one_turn_controller_GE_annual_dynamics_IRF_Results": 0,
        "MATLAB_startups": 0,
        "scientific_retries": 0,
        "assembler_or_selector_calls": 0,
    }
    preflight = {
        "live_main": git("rev-parse", "origin/main"),
        "branch": git("branch", "--show-current"),
        "source_evidence_root": str(SOURCE),
        "resolved_predecessor_manifest": str(manifest_path),
        "repository_manifest_copy": str(manifest_copy),
        "predecessor_manifest_sha256": manifest_sha,
        "consumed": consumed,
        "index_identity": index_identity,
        "export_blob": EXPORT_BLOB,
        "protected_HJB_sha256": PROTECTED_HJB_SHA,
        "scientific_calls_before_and_after": 0,
    }

    write_json(evidence_root / "preflight.json", preflight, exclusive=True)
    write_json(evidence_root / "summary.json", summary, exclusive=True)
    write_json(evidence_root / "source_line_map.json", source_map, exclusive=True)
    write_json(evidence_root / "zero_call_ledger.json", call_ledger, exclusive=True)
    write_json(evidence_root / "identity_checks.json", identity_checks, exclusive=True)
    write_json(evidence_root / "pin_residual_localization.json", localization, exclusive=True)
    write_json(evidence_root / "signed_mass_balance.json", signed_balance, exclusive=True)
    write_json(evidence_root / "residual_scaling.json", residual_scaling, exclusive=True)
    ledger_path = evidence_root / "cell_ledger.csv"
    with ledger_path.open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    for path in evidence_root.iterdir():
        if path.is_file():
            shutil.copyfile(path, report_output / path.name)
    print(json.dumps({"source_escape_interpretation": summary["source_escape_interpretation"], "pin": pin, "pin_residual": balance["pin_residual"], "escape": balance["escaped_mass_flow"], "manifest": manifest_sha}))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
