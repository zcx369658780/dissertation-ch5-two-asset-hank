"""Saved-array diagnostics only: no model, evaluator, root, or solve calls."""
import csv
import json
import math
from pathlib import Path
import sys

import numpy as np
from scipy import sparse

from evidence import decode_saved

BASELINE = Path(r"D:\ProjectTemp\ch5-2018-observable-prefix-replay-20260908-001")


def finite_stats(value):
    array = np.asarray(value)
    finite = np.isfinite(array)
    result = {"shape": list(array.shape), "size": int(array.size), "finite_count": int(finite.sum()), "nonfinite_count": int((~finite).sum())}
    if finite.any():
        result.update(min=float(array[finite].min()), max=float(array[finite].max()), norm_inf=float(np.max(np.abs(array[finite]))), norm_2=float(np.linalg.norm(array[finite].ravel())))
    return result


def comparison(new, old):
    left = np.asarray(new)
    right = np.asarray(old)
    finite = np.isfinite(left) & np.isfinite(right)
    delta = left - right
    return {"shape_equal": left.shape == right.shape, "new": finite_stats(left), "baseline_09": finite_stats(right), "finite_pair_count": int(finite.sum()), "difference": finite_stats(delta), "exact_equal_count": int(np.equal(left, right).sum())}


def operator_diagnostics(operator, shape, drift=None):
    matrix = sparse.csr_matrix(operator)
    coo = matrix.tocoo()
    off = coo.row != coo.col
    values = coo.data[off]
    rows = np.asarray(matrix.sum(axis=1)).ravel()
    stable_rows = np.array([math.fsum(matrix.data[matrix.indptr[index]:matrix.indptr[index + 1]]) for index in range(matrix.shape[0])])
    row_abs = np.asarray(abs(matrix).sum(axis=1)).ravel()
    result = {
        "shape": list(matrix.shape), "nnz": int(matrix.nnz), "data_finite": bool(np.isfinite(matrix.data).all()),
        "negative_offdiagonal_count": int(np.sum(values < 0)), "negative_offdiagonal_min": float(min(0.0, values.min(initial=0.0))),
        "positive_offdiagonal_max": float(max(0.0, values.max(initial=0.0))), "row_sum_max_abs": float(np.max(np.abs(rows))),
        "row_sum_fsum_max_abs": float(np.max(np.abs(stable_rows))), "matrix_norm_inf": float(row_abs.max()),
        "matrix_implied_omitted_rate_positive_count": int(np.sum(-stable_rows > 0)), "matrix_implied_omitted_rate_max": float(max(0.0, np.max(-stable_rows))),
        "matrix_implied_note": "-stable row sum is reported as a matrix-implied omitted outward rate; exact drift reconstruction is separate when available.",
    }
    if drift is not None:
        mu_b, mu_a, db, da = drift
        leak = np.zeros(shape)
        leak[0, :, :] += np.maximum(-mu_b[0, :, :], 0.0) / db
        leak[-1, :, :] += np.maximum(mu_b[-1, :, :], 0.0) / db
        leak[:, 0, :] += np.maximum(-mu_a[:, 0, :], 0.0) / da
        leak[:, -1, :] += np.maximum(mu_a[:, -1, :], 0.0) / da
        flat = leak.ravel(order="F")
        result["post_drift_boundary_leak"] = {"exact_positive_count": int(np.sum(flat > 0)), "max": float(flat.max()), "sum": float(flat.sum()), "row_sum_plus_leak_max_abs": float(np.max(np.abs(stable_rows + flat)))}
    return result


def boundary_drifts(hjb):
    mu_b = hjb["mu_b"]
    mu_a = hjb["mu_a"]
    return {
        "lower_b": {"inward_positive": finite_stats(np.maximum(mu_b[0], 0.0)), "outward_negative": finite_stats(np.minimum(mu_b[0], 0.0)), "outward_exact_count": int(np.sum(mu_b[0] < 0))},
        "upper_b": {"inward_negative": finite_stats(np.minimum(mu_b[-1], 0.0)), "outward_positive": finite_stats(np.maximum(mu_b[-1], 0.0)), "outward_exact_count": int(np.sum(mu_b[-1] > 0))},
        "lower_a": {"inward_positive": finite_stats(np.maximum(mu_a[:, 0], 0.0)), "outward_negative": finite_stats(np.minimum(mu_a[:, 0], 0.0)), "outward_exact_count": int(np.sum(mu_a[:, 0] < 0))},
        "upper_a": {"inward_negative": finite_stats(np.minimum(mu_a[:, -1], 0.0)), "outward_positive": finite_stats(np.maximum(mu_a[:, -1], 0.0)), "outward_exact_count": int(np.sum(mu_a[:, -1] > 0))},
    }


def write(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main(root, output):
    root = Path(root)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    new_hjb = decode_saved(root / "science/hjb_return_before_kfe.json")
    old_hjb = decode_saved(BASELINE / "capture/call_0725/hjb_return_before_kfe.json")
    new_init = decode_saved(root / "science/native_initialization_return.json")
    old_init_raw = decode_saved(BASELINE / "capture/call_0725/native_initialization_return.json")
    old_init = {"initial_value": old_init_raw["V0"], "baseline_labor": old_init_raw["l0"]}
    kfe = decode_saved(root / "science/kfe_return.json")
    raw = decode_saved(root / "science/kfe_direct_return.json")["raw"]
    aggregate = decode_saved(root / "science/aggregate_return.json")
    binding = decode_saved(root / "science/binding.json")
    terminal = decode_saved(root / "science/terminal.json")
    state_changes = [name for name in binding["state_09"] if binding["state_09"][name] != binding["state_07"][name]]
    assert state_changes == ["rah"]
    assert binding["state_07"]["rah"] == float("0.07") and binding["state_07"]["rah"] != .09 - .02
    assert binding["state_07"]["ra"] == .09 and binding["state_07"]["ramax"] == .09
    assert binding["baseline_context"] == {"step": 24, "province_index_0": 11, "province": "安徽", "call": 725}
    input_changes = [name for name in binding["inputs_09"] if not np.array_equal(np.asarray(binding["inputs_09"][name]), np.asarray(binding["inputs_07"][name]))]
    assert input_changes == ["r_a"]
    assert binding["inputs_07"]["r_a"] == float("0.07")
    assert binding["state_07"]["w"] == 16.82014806560587 and binding["state_07"]["rb"] == .02
    assert binding["state_07"]["rb_gap"] == .07 and binding["state_07"]["tau"] == .05 and binding["state_07"]["Tt"] == .1
    assert binding["params"] == {"rho": .05, "gamma_c": 2., "phi": 5., "chi_0": .1, "chi_1": 2., "a_bar": 1e-6, "mu_z": 0., "sigma_z": 0.}
    assert binding["numerics"] == {"delta": 1000., "convergence_tolerance": 1e-7, "max_iterations": 100, "drift_tolerance": 1e-12}
    shape = tuple(new_hjb["value"].shape)
    db = float(binding["grid"]["b"][1] - binding["grid"]["b"][0])
    da = float(binding["grid"]["a"][1] - binding["grid"]["a"][0])
    fields = ("value", "initial_value", "consumption", "labor", "transfer", "adjustment_cost", "effective_illiquid_return", "mu_a", "mu_b", "utility")
    arrays = {name: comparison(new_hjb[name], old_hjb[name]) for name in fields}
    arrays["native_initial_value"] = comparison(new_init["initial_value"], old_init["initial_value"])
    arrays["native_baseline_labor"] = comparison(new_init["baseline_labor"], old_init["baseline_labor"])
    arrays["liquid_label"] = {"shape": list(new_hjb["liquid_label"].shape), "changed_count": int(np.sum(new_hjb["liquid_label"] != old_hjb["liquid_label"])), "new_counts": {str(key): int(value) for key, value in zip(*np.unique(new_hjb["liquid_label"], return_counts=True))}}
    arrays["transfer_label"] = {"shape": list(new_hjb["transfer_label"].shape), "changed_count": int(np.sum(new_hjb["transfer_label"] != old_hjb["transfer_label"])), "new_counts": {str(key): int(value) for key, value in zip(*np.unique(new_hjb["transfer_label"], return_counts=True))}}
    operators = {
        "HJB_iteration_operator": operator_diagnostics(new_hjb["operator"]["full"], shape),
        "post_loop_KFE_operator": operator_diagnostics(new_hjb["post_convergence_operator"]["full"], shape, (new_hjb["mu_b"], new_hjb["mu_a"], db, da)),
        "baseline_09_HJB_iteration_operator": operator_diagnostics(old_hjb["operator"]["full"], shape),
        "baseline_09_post_loop_KFE_operator": operator_diagnostics(old_hjb["post_convergence_operator"]["full"], shape, (old_hjb["mu_b"], old_hjb["mu_a"], db, da)),
    }
    contaminated = kfe["contaminated_matrix"]
    rhs = kfe["rhs"]
    raw_residual = contaminated @ raw - rhs
    raw_denom = float(np.max(np.asarray(abs(contaminated).sum(axis=1)).ravel()) * np.linalg.norm(raw, ord=np.inf) + np.linalg.norm(rhs, ord=np.inf))
    stationary = kfe["transpose"] @ kfe["density_vector"]
    stationary_denom = float(np.max(np.asarray(abs(kfe["transpose"]).sum(axis=1)).ravel()) * np.linalg.norm(kfe["density_vector"], ord=np.inf))
    density = kfe["density_vector"]
    distribution = {
        "normalization_factor": kfe["normalization_factor"], "cell_weight": kfe["cell_weight"],
        "normalized_total_mass": float(np.sum(density) * kfe["cell_weight"]), "density_min": float(density.min()),
        "density_max": float(density.max()), "negative_density_exact_count": int(np.sum(density < 0)),
        "weighted_negative_mass": float(np.sum(np.minimum(density, 0.0)) * kfe["cell_weight"]),
        "contaminated_raw_residual_inf": float(np.linalg.norm(raw_residual, ord=np.inf)), "contaminated_raw_scale_denominator": raw_denom,
        "contaminated_raw_normwise_ratio": float(np.linalg.norm(raw_residual, ord=np.inf) / raw_denom) if raw_denom else None,
        "source_reported_raw_residual_inf": kfe["raw_residual_inf"],
        "unmodified_transpose_stationary_residual_inf": float(np.linalg.norm(stationary, ord=np.inf)),
        "unmodified_transpose_scale_denominator": stationary_denom,
        "unmodified_transpose_normwise_ratio": float(np.linalg.norm(stationary, ord=np.inf) / stationary_denom) if stationary_denom else None,
        "residual_note": "The contaminated-row raw residual and A.T@normalized_density stationary residual are distinct diagnostics; neither is an added solve or acceptance tolerance.",
    }
    old_raw = decode_saved(BASELINE / "capture/call_0725/kfe_direct_return.json")["raw"]
    baseline = {"rah": 0.09, "HJB_converged": old_hjb["converged"], "HJB_iterations": old_hjb["iterations"], "HJB_statistic": old_hjb["convergence_statistic"], "KFE_status": "ORIGINAL_EXCEPTION_NONFINITE_RAW", "KFE_raw": finite_stats(old_raw), "aggregates": "MISSING"}
    new = {"rah": float("0.07"), "HJB_converged": new_hjb["converged"], "HJB_iterations": new_hjb["iterations"], "HJB_statistic": new_hjb["convergence_statistic"], "KFE_status": "RETURNED", "KFE_raw": finite_stats(raw), "aggregates": aggregate}
    summary = {
        "diagnostic_completion": "COMPLETE", "input_binding": "EXACT_ONE_FACTOR_RAH_AND_MAPPED_R_A", "outcome": "HJB_CONVERGED_AND_KFE_RETURNED",
        "HJB_status": {"baseline_09": baseline, "new_07": new}, "KFE_status": {"baseline_09": baseline["KFE_status"], "new_07": "RETURNED"},
        "generator_diagnostics": operators, "distribution_diagnostics": distribution, "boundary_drifts": boundary_drifts(new_hjb),
        "aggregates_available": True, "local_rate_sensitivity_conclusion": "At this one saved input, changing only rah/r_a to float('0.07') and regenerating the native initializer changed the chain from HJB100 nonconvergence plus nonfinite KFE failure to HJB26 convergence plus a finite KFE and aggregate return. This does not identify a unique cause or authorize production change.",
        "array_comparisons": arrays, "call_ledger": terminal["counts"], "warnings": terminal["warnings"], "Results_eligible": False,
    }
    write(output / "summary.json", summary)
    write(output / "array_comparison.json", arrays)
    write(output / "operator_diagnostics.json", operators)
    write(output / "distribution_diagnostics.json", distribution)
    write(output / "boundary_drift_diagnostics.json", summary["boundary_drifts"])
    write(output / "intervention_binding.json", {"context": binding["baseline_context"], "state_changed_fields": state_changes, "mapped_input_changed_fields": input_changes, "rah": binding["state_diff"]["rah"], "r_a": binding["mapped_input_diff"]["r_a"], "unchanged_checks": {"carried_ra": binding["state_07"]["ra"], "ramax": binding["state_07"]["ramax"], "wage": binding["state_07"]["w"], "rb": binding["state_07"]["rb"], "rb_gap": binding["state_07"]["rb_gap"], "tau": binding["state_07"]["tau"], "Tt": binding["state_07"]["Tt"], "params": binding["params"], "numerics": binding["numerics"], "grid_shapes": {name: list(np.asarray(value).shape) for name, value in binding["grid"].items()}}})
    write(output / "call_ledger.json", {"new_07": terminal["counts"], "per_call": terminal["per_call"], "scientific_processes": 1, "workers": 1, "scientific_restarts": 0, "external_launch_retries": 0, "baseline_09_new_scientific_calls": 0, "zeros": {"additional_policy_or_evaluator": 0, "diagnostic_condition_high_precision_solves": 0, "firm": 0, "one_turn_controller": 0, "GE_annual_other_provinces_years": 0, "R_PLM": 0, "dynamics_IRF_Results": 0, "MATLAB_startups": 0}, "counts_include_failed_entries": True})
    with (output / "baseline_09_vs_new_07.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=("case", "rah", "HJB_converged", "HJB_iterations", "HJB_statistic", "KFE_status", "aggregate_C", "aggregate_L", "aggregate_A", "aggregate_B", "aggregate_total_assets", "density_normalization"))
        writer.writeheader()
        writer.writerow({"case": "SAVED_BASELINE_09", "rah": .09, "HJB_converged": baseline["HJB_converged"], "HJB_iterations": baseline["HJB_iterations"], "HJB_statistic": baseline["HJB_statistic"], "KFE_status": baseline["KFE_status"]})
        writer.writerow({"case": "NEW_NATIVE_INIT_07", "rah": .07, "HJB_converged": new["HJB_converged"], "HJB_iterations": new["HJB_iterations"], "HJB_statistic": new["HJB_statistic"], "KFE_status": new["KFE_status"], "aggregate_C": aggregate["c_ss"], "aggregate_L": aggregate["l_ss"], "aggregate_A": aggregate["a_ss"], "aggregate_B": aggregate["b_ss"], "aggregate_total_assets": aggregate["total_assets"], "density_normalization": aggregate["density_normalization"]})
    print(json.dumps({"outcome": summary["outcome"], "HJB": new_hjb["converged"], "iterations": new_hjb["iterations"], "statistic": new_hjb["convergence_statistic"], "negative_density": distribution["negative_density_exact_count"]}))


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
