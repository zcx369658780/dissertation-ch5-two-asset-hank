"""Run one corrected-2018 trajectory for at most 25 turns with K/L diagnostics."""
from __future__ import annotations

import argparse
import csv
import json
import os
import platform
import sys
import time
from collections import Counter
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

import numpy as np

REPO = Path(__file__).resolve().parents[3]
for item in (REPO / "src", REPO):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))

from validators.multi_province.corrected_2018_single_turn import run as single
from ch5_two_asset_hank.multi_province import one_turn as one_turn_module
from ch5_two_asset_hank.multi_province.one_turn import OneTurnInputs, PreFrozenHouseholdOutputBatch
from ch5_two_asset_hank.multi_province.steady_state import (
    AdaptiveAction, _adapt, _diagnostics, _freeze_state, _post_turn_states,
)

VERDICT_PASS = "CORRECTED_2018_25TURN_KL_RECONCILIATION_PASS__LATE_WINDOW_KL_GAPS_QUANTIFIED"
VERDICT_PARTIAL = "CORRECTED_2018_25TURN_KL_RECONCILIATION_PARTIAL__EARLY_HARD_FAILURE_BEFORE_LATE_WINDOW"
VERDICT_BLOCKED = "CORRECTED_2018_25TURN_KL_RECONCILIATION_BLOCKED__RUNTIME_CONTRACT_OR_LEDGER_INCOMPLETE"
THREAD_ENV = ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS")


def write_json(path: Path, value: Any) -> None:
    single.write_json(path, value)


def _canonical_bytes(value: Any) -> bytes:
    return (json.dumps(single.jsonable(value), ensure_ascii=False, sort_keys=True,
                       separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def _value_sha(value: Any) -> str:
    return sha256(_canonical_bytes(value)).hexdigest().upper()


def prepare(distance_workbook: Path, evidence_root: Path) -> None:
    root = Path(evidence_root)
    root.mkdir(parents=True, exist_ok=False)
    payload = single.build_runtime_payload(distance_workbook)
    payload["schema"] = "CH5_CORRECTED_2018_25TURN_KL_RUNTIME_INPUT_V1"
    payload_path = root / "runtime_input_payload.json"
    write_json(payload_path, payload)
    write_json(root / "runtime_input_receipt.json", {
        "schema": "CH5_CORRECTED_2018_25TURN_KL_RUNTIME_RECEIPT_V1",
        "corrected_source_identities": payload["source_identities"],
        "runtime_payload_sha256": single.file_sha256(payload_path),
        "runtime_contract": payload["metadata"], "pre_science_assertion": payload["pre_science_assertion"],
        "province_count": 31,
        "province_order": payload["province_order"],
        "grid": {"I": 20, "b": [-2.0, 5.0], "J": 20, "a": [0.0, 10.0],
                 "Nz": 2, "z": [0.8, 1.3]},
        "trajectory_budget": 1, "maximum_outer_turns": 25,
        "maximum_province_household_updates": 775,
        "scientific_calls": 0,
    })
    write_json(root / "source_code_identity.json", {
        "schema": "CH5_CORRECTED_2018_25TURN_KL_SOURCE_IDENTITY_V1",
        "files": {str(path.relative_to(REPO)).replace("\\", "/"): single.file_sha256(path)
                  for path in (Path(__file__), Path(single.__file__),
                               REPO / "exports/matlab_faithful_two_asset_ha.py",
                               REPO / "src/ch5_two_asset_hank/multi_province/one_turn.py",
                               REPO / "src/ch5_two_asset_hank/multi_province/steady_state.py",
                               REPO / "src/ch5_two_asset_hank/multi_province/firm.py")},
        "scientific_calls": 0,
    })
    write_json(root / "bounded_invocation_receipt.json", {
        "schema": "CH5_CORRECTED_2018_25TURN_KL_BOUNDED_INVOCATION_V1",
        "prepare_entrypoint": "validators/multi_province/corrected_2018_25turn_kl/run.py prepare",
        "science_entrypoint": "validators/multi_province/corrected_2018_25turn_kl/run.py run",
        "trajectory_budget": 1, "outer_turn_ceiling": 25,
        "province_household_update_ceiling": 775,
        "engineering_retry_rule": "ONLY_BEFORE_SCIENTIFIC_STATE_ADVANCES",
        "completed_scientific_trajectory_rerun_authorized": False,
        "parameter_cell_comparisons_authorized": 0,
        "scientific_calls_at_prepare": 0,
    })


def rah_provenance(turn: int, index: int, states: tuple[Mapping[str, object], ...],
                   prior_states: tuple[Mapping[str, object], ...] | None = None) -> dict[str, Any]:
    if turn == 1:
        return {"entering_state_field": "rah", "source": "accepted_corrected_2018_runtime.rah0",
                "value": float(states[index]["rah"]), "manual_override": False}
    if prior_states is None:
        raise ValueError("lagged rah provenance requires prior entering states")
    ratios = np.array([float(state["inter_prv_ratio"]) for state in prior_states])
    old_ra = np.array([float(state["ra"]) for state in prior_states])
    # Match capital_allocation.allocate_productive_capital's ordered Python
    # summation exactly; np.sum can differ by one binary64 ulp.
    weighted_total = sum(float(ratios[i] * old_ra[i]) for i in range(len(prior_states)))
    own_ratio = float(ratios[index])
    own_old_ra = float(old_ra[index])
    rebuilt = ((1.0 - own_ratio) * own_old_ra
               + own_ratio * (weighted_total - own_ratio * own_old_ra) / (len(states) - 1))
    actual = float(states[index]["rah"])
    if actual != rebuilt:
        raise ValueError("native turn-2 rah does not match capital-allocation lag formula")
    return {
        "entering_state_field": "rah",
        "source": f"turn_{turn - 1}.one_turn.capital.household_illiquid_return_rah -> steady_state._post_turn_states.rah",
        "formula": "(1-ratio_i)*old_ra_i + ratio_i*(sum_j(ratio_j*old_ra_j)-ratio_i*old_ra_i)/(n-1)",
        "source_old_ra_turn": turn - 1, "source_old_ra_field": f"turn_{turn - 1}.entering_state.ra",
        "own_inter_prv_ratio": own_ratio, "own_old_ra": own_old_ra,
        "weighted_old_ra_total": weighted_total, "value": actual,
        "source_old_ra_vector_sha256": _value_sha(old_ra.tolist()), "manual_override": False,
    }


def national_summary(turn: int, rows: list[dict[str, Any]], controller: dict[str, Any]) -> dict[str, Any]:
    raw_ra = np.array([row["firm_ra0"] for row in rows], dtype=float)
    raw_wage = np.array([row["firm_wage_raw"] for row in rows], dtype=float)
    rah = np.array([row["household_rah"] for row in rows], dtype=float)
    nk = np.array([row["nk_gap"] for row in rows], dtype=float)
    yt = np.array([row["yt_gap"] for row in rows], dtype=float)
    total_k_ratio = np.array([row["firm_K_total_over_Ktarget"] for row in rows], dtype=float)
    private_k_ratio = np.array([row["private_K_over_Ktarget"] for row in rows], dtype=float)
    gov_before_ratio = np.array([row["GovInv_before_over_Ktarget"] for row in rows], dtype=float)
    gov_after_ratio = np.array([row["GovInv_after_over_Ktarget"] for row in rows], dtype=float)
    labor_ratio = np.array([row["firm_Lt_over_population_proxy"] for row in rows], dtype=float)
    gdp_level_gap = np.array([row["GDP_level_gap"] for row in rows], dtype=float)
    rate_regions = Counter("lower" if row["firm_ra0"] < row["ramin"] else
                           "upper" if row["firm_ra0"] > row["ramax"] else "interior" for row in rows)
    wage_regions = Counter("lower" if row["firm_wage_raw"] < row["wjtmin"] else
                           "upper" if row["firm_wage_raw"] > row["wjtmax"] else "interior" for row in rows)
    def stats(values: np.ndarray) -> dict[str, float]:
        return {"min": float(np.min(values)), "median": float(np.median(values)), "max": float(np.max(values))}
    result = {
        "turn": turn,
        "firm_rate_regions": {key: rate_regions.get(key, 0) for key in ("lower", "interior", "upper")},
        "wage_regions": {key: wage_regions.get(key, 0) for key in ("lower", "interior", "upper")},
        "raw_ra0": {**stats(raw_ra), "min_province": rows[int(np.argmin(raw_ra))]["province"],
                    "max_province": rows[int(np.argmax(raw_ra))]["province"]},
        "raw_wage": stats(raw_wage), "household_rah": stats(rah),
        "nk_gap": stats(nk), "yt_gap": stats(yt),
        "hjb_iterations": stats(np.array([row["hjb_iterations"] for row in rows], dtype=float)),
        "hjb_iteration_distribution": dict(sorted(Counter(str(row["hjb_iterations"]) for row in rows).items())),
        "hjb_failures": sum(not row["hjb_converged"] for row in rows),
        "kfe_failures": sum(not row["kfe_returned"] for row in rows),
        "firm_K_total_over_Ktarget": stats(total_k_ratio),
        "private_K_over_Ktarget": stats(private_k_ratio),
        "GovInv_before_over_Ktarget": stats(gov_before_ratio),
        "GovInv_after_over_Ktarget": stats(gov_after_ratio),
        "firm_K_ratio_counts": {
            "above_1p05": int(np.count_nonzero(total_k_ratio > 1.05)),
            "above_1p25": int(np.count_nonzero(total_k_ratio > 1.25)),
            "above_2": int(np.count_nonzero(total_k_ratio > 2.0)),
            "below_0p95": int(np.count_nonzero(total_k_ratio < 0.95)),
            "below_0p75": int(np.count_nonzero(total_k_ratio < 0.75)),
            "below_0p5": int(np.count_nonzero(total_k_ratio < 0.5)),
        },
        "firm_Lt_over_population_proxy": stats(labor_ratio),
        "labor_ratio_outside_0p8_1p2_count": int(np.count_nonzero((labor_ratio < 0.8) | (labor_ratio > 1.2))),
        "GDP_level_gap": stats(gdp_level_gap),
        "national_sums": {
            "Ktarget_2018_MU": float(sum(row["Ktarget_2018_MU"] for row in rows)),
            "Kt_supply_private_MU": float(sum(row["Kt_supply_private_MU"] for row in rows)),
            "GovInv_before_MU": float(sum(row["GovInv_before_MU"] for row in rows)),
            "GovInv_after_MU": float(sum(row["GovInv_after_MU"] for row in rows)),
            "firm_K_total_MU": float(sum(row["firm_K_total_MU"] for row in rows)),
            "Ltarget_proxy_NU": float(sum(row["Ltarget_proxy_NU"] for row in rows)),
            "firm_destination_labor": float(sum(row["firm_Lt_supply"] for row in rows)),
        },
        "controller": {"adaptation_gate_open": controller["adaptation_allowed"],
                       "zt_adjusted_count": sum(action["zt_adjusted"] for action in controller["actions"]),
                       "govinv_action_counts": dict(Counter(action["govinv_action"] for action in controller["actions"])),
                       "labor_row_sum_identity_max_abs_gap": controller["labor_row_sum_identity_max_abs_gap"],
                       "labor_national_matrix_vs_destination_sum_abs_gap": controller[
                           "labor_national_matrix_vs_destination_sum_abs_gap"]},
    }
    for field in ("A", "B", "A_plus_B"):
        result[field] = stats(np.array([row[field] for row in rows], dtype=float))
    result["kfe_diagnostic_status_counts"] = dict(Counter(row["kfe_diagnostic_status"] for row in rows))
    result["kfe_source_free_residual"] = stats(
        np.array([row["kfe_source_free_residual_inf"] for row in rows], dtype=float))
    result["kfe_source_free_ratio"] = stats(
        np.array([row["kfe_source_free_normwise_ratio"] for row in rows], dtype=float))
    return result


def kfe_distribution_diagnostics(hjb: Any, kfe: Any) -> dict[str, Any]:
    """Pure post-processing of the returned operator, density, and drifts; no solve."""
    eps = np.finfo(float).eps
    density = np.asarray(kfe.density_vector, dtype=float)
    transpose = kfe.transpose.tocsr()
    stationary = np.asarray(transpose @ density, dtype=float)
    source_numerator = float(np.linalg.norm(stationary, ord=np.inf))
    source_scale = float(np.max(np.asarray(abs(transpose).sum(axis=1)).ravel())
                         * np.linalg.norm(density, ord=np.inf))
    source_ratio = source_numerator / source_scale if source_scale else 0.0
    raw_residual = np.asarray(kfe.contaminated_matrix @ kfe.raw_solve_vector - kfe.rhs)
    raw_numerator = float(np.linalg.norm(raw_residual, ord=np.inf))
    raw_scale = float(np.max(np.asarray(abs(kfe.contaminated_matrix).sum(axis=1)).ravel())
                      * np.linalg.norm(kfe.raw_solve_vector, ord=np.inf)
                      + np.linalg.norm(kfe.rhs, ord=np.inf))
    mu_b = np.asarray(hjb.mu_b, dtype=float)
    mu_a = np.asarray(hjb.mu_a, dtype=float)
    faces = {
        "lower_b": np.maximum(-mu_b[0, :, :], 0.0) / kfe.db,
        "upper_b": np.maximum(mu_b[-1, :, :], 0.0) / kfe.db,
        "lower_a": np.maximum(-mu_a[:, 0, :], 0.0) / kfe.da,
        "upper_a": np.maximum(mu_a[:, -1, :], 0.0) / kfe.da,
    }
    boundary = {name: {"outward_leak_count": int(np.count_nonzero(rate > 0.0)),
                       "max_outward_leak_rate": float(rate.max(initial=0.0)),
                       "sum_outward_leak_rate": float(rate.sum())}
                for name, rate in faces.items()}
    mass = float(density.sum() * kfe.cell_weight)
    negative_count = int(np.count_nonzero(density < 0.0))
    negative_mass = float(np.minimum(density, 0.0).sum() * kfe.cell_weight)
    finite = bool(np.isfinite(density).all() and np.isfinite(stationary).all())
    mass_ok = abs(mass - 1.0) <= 128.0 * eps
    sign_ok = float(density.min()) >= -1e-12
    stationarity_ok = source_ratio <= 128.0 * eps
    boundary_ok = not any(item["max_outward_leak_rate"] > 1e-12 for item in boundary.values())
    status = "VALID" if finite and mass_ok and sign_ok and stationarity_ok and boundary_ok else "DIAGNOSTIC_ONLY"
    return {
        "schema": "CH5_CORRECTED_2018_FIVE_TURN_KFE_DISTRIBUTION_DIAGNOSTIC_V1",
        "classification": status, "pure_post_processing": True, "additional_solves": 0,
        "normalized_mass": mass, "density_min": float(density.min()),
        "density_max": float(density.max()), "negative_entry_count": negative_count,
        "weighted_negative_mass": negative_mass,
        "contaminated_row_residual_numerator": raw_numerator,
        "contaminated_row_residual_scale": raw_scale,
        "contaminated_row_residual_ratio": raw_numerator / raw_scale if raw_scale else 0.0,
        "source_reported_contaminated_residual_inf": float(kfe.raw_residual_inf),
        "source_free_residual_numerator": source_numerator,
        "source_free_residual_scale": source_scale,
        "source_free_residual_ratio": source_ratio,
        "boundary_outward_leak": boundary,
        "upper_b_face_probability_mass": float(np.sum(kfe.density[-1, :, :]) * kfe.cell_weight),
        "checks": {"finite": finite, "normalized_mass": mass_ok, "density_sign": sign_ok,
                   "source_free_stationarity": stationarity_ok, "boundary_no_material_outward_leak": boundary_ok},
        "thresholds": {"mass_absolute": 128.0 * eps, "density_min": -1e-12,
                       "source_free_normwise_ratio": 128.0 * eps,
                       "boundary_max_outward_rate": 1e-12},
    }


def execute(evidence_root: Path) -> int:
    root = Path(evidence_root)
    payload_path = root / "runtime_input_payload.json"
    if not payload_path.is_file() or not (root / "runtime_input_receipt.json").is_file():
        raise ValueError("prepared runtime input is missing")
    if (root / "science_started.json").exists():
        raise RuntimeError("scientific trajectory already started; retry prohibited")
    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    single.validate_serialized_payload(payload)
    counters = {key: 0 for key in (
        "turns_entered", "turns_completed", "province_updates_attempted", "province_updates_completed",
        "household_calls_attempted", "household_calls_returned", "household_calls_failed",
        "native_initializations_attempted", "native_initializations_returned",
        "labor_roots_attempted", "labor_roots_returned", "brentq_calls_attempted", "brentq_calls_returned",
        "hjb_calls", "hjb_returns", "hjb_direct_solves", "kfe_calls", "kfe_returns", "kfe_direct_solves",
        "aggregate_calls", "aggregate_returns", "one_turn_executions", "one_turn_returns",
        "migration_calls", "capital_allocation_calls", "firm_calls", "firm_returns",
        "wage_batch_calls", "wage_province_outputs", "controller_calls", "adaptation_calls",
        "adaptation_gate_open_count")}
    counters.update({"scientific_processes": 1, "trajectory_attempts": 1,
                     "trajectory_returns": 0, "scientific_retries": 0})
    write_json(root / "science_started.json", {
        "schema": "CH5_CORRECTED_2018_25TURN_KL_LAUNCH_V1",
        "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "process_id": os.getpid(), "python": sys.version, "platform": platform.platform(),
        "thread_environment": {key: os.environ.get(key) for key in THREAD_ENV},
        "authorized_trajectory_count": 1, "authorized_turns_maximum": 25,
        "authorized_province_household_updates_maximum": 775, "scientific_retries": 0,
        "runtime_payload_sha256": single.file_sha256(payload_path),
    })
    states = tuple(dict(item) for item in payload["states"])
    initial_states = states
    prior_entering_states: tuple[Mapping[str, object], ...] | None = None
    tkn_ratio = np.full(31, 3.0)
    wedges = np.array(payload["matrices"]["sigmau_destination_origin"], dtype=float)
    grid = single.oracle.MatlabFaithfulHJBGrid(np.linspace(-2, 5, 20), np.linspace(0, 10, 20),
        np.array([0.8, 1.3]), np.array([[-1/3, 1/3], [1/3, -1/3]]))
    params = single.oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
    numerics = single.oracle.MatlabFaithfulHJBNumerics(1000.0, 1e-7, 100, 1e-12)
    model_params = MappingProxyType({"ga": 2.0, "phi_l": 5.0, "alphal": 1.0, "epsilon": 10.0,
        "theta": 100.0, "delta": 0.025, "istar": 0.015, "rho_pi": 1.25,
        "totalpit": 0.02, "epsilon_pi": 0.0})
    current = {"stage": "PRE_SCIENCE", "turn": 0, "province_index": None, "province": None}
    original_spsolve = single.oracle.linalg.spsolve
    original_brentq = single.LABOR_BRENTQ
    started = time.monotonic()
    verdict = VERDICT_PARTIAL
    error = None
    turn_summaries: list[dict[str, Any]] = []
    termination_reason = "NOT_STARTED"

    def counted_spsolve(*args, **kwargs):
        key = "hjb_direct_solves" if current["stage"] == "HJB" else "kfe_direct_solves"
        counters[key] += 1
        return original_spsolve(*args, **kwargs)
    def counted_brentq(*args, **kwargs):
        counters["brentq_calls_attempted"] += 1
        result = original_brentq(*args, **kwargs)
        counters["brentq_calls_returned"] += 1
        return result

    single.oracle.linalg.spsolve = counted_spsolve
    single.LABOR_BRENTQ = counted_brentq
    try:
        for turn_index in range(1, 26):
            current.update(stage="TURN_ENTRY", turn=turn_index, province_index=None, province=None)
            counters["turns_entered"] += 1
            turn_root = root / f"turn_{turn_index:02d}"
            outputs: list[dict[str, Any]] = []
            provenance = [rah_provenance(turn_index, index, states, prior_entering_states) for index in range(31)]
            write_json(turn_root / "entering_state.json", {"turn": turn_index, "states": states,
                "rah_provenance": provenance, "tkn_ratio": tkn_ratio})
            productivity = np.array([float(state["Yt"]) / float(state["Lt"]) for state in states])
            phi = 1.0 + 0.3 * (productivity[:, None] - productivity[None, :]) / (productivity[:, None] + productivity[None, :])
            for index, state in enumerate(states):
                province = payload["province_order"][index]
                province_root = turn_root / "household" / f"p{index:02d}_{province}"
                current.update(stage="NATIVE_INITIALIZATION", province_index=index, province=province)
                counters["household_calls_attempted"] += 1
                counters["native_initializations_attempted"] += 1
                def enter_root() -> None: counters["labor_roots_attempted"] += 1
                def return_root() -> None: counters["labor_roots_returned"] += 1
                initial, labor = single.source_initial_arrays(state, grid, params, enter_root, return_root)
                counters["native_initializations_returned"] += 1
                current["stage"] = "HJB"; counters["hjb_calls"] += 1
                hjb = single.oracle.solve_matlab_faithful_hjb(grid, params, single.oracle.HouseholdInputs(
                    float(state["rah"]), float(state["rb"]), float(state["tau"]),
                    np.array([state["w"]]), np.array([0.0]), np.array([1.0])), initial, labor,
                    float(state["Tt"]), float(state["rb_gap"]), numerics)
                counters["hjb_returns"] += 1
                single._save_hjb(province_root / "hjb_return.npz", hjb)
                write_json(province_root / "hjb_receipt.json", {"turn": turn_index, "province_index": index,
                    "province": province, "converged": hjb.converged, "iterations": hjb.iterations,
                    "convergence_statistic": hjb.convergence_statistic, "persisted_before_kfe": True})
                if not hjb.converged:
                    raise RuntimeError("HJB did not converge")
                current["stage"] = "KFE"; counters["kfe_calls"] += 1
                kfe = single.oracle.solve_matlab_faithful_stationary_kfe(hjb.post_convergence_operator.full,
                    shape=(20, 20, 2), db=float(grid.b[1]-grid.b[0]), da=float(grid.a[1]-grid.a[0]))
                counters["kfe_returns"] += 1
                single._save_kfe(province_root / "kfe_return.npz", kfe)
                kfe_diagnostic = kfe_distribution_diagnostics(hjb, kfe)
                write_json(province_root / "kfe_distribution_diagnostic.json", kfe_diagnostic)
                current["stage"] = "AGGREGATE"; counters["aggregate_calls"] += 1
                aggregate = single.oracle.aggregate_stationary_household(grid, hjb.consumption, hjb.labor, kfe.density)
                counters["aggregate_returns"] += 1
                effective = single.oracle.matlab_faithful_illiquid_return(grid.a, grid.a[-1], float(state["rah"]))
                at_tax = aggregate.a_ss * float(state["rah"]) - float(
                    np.sum(grid.a[None,:,None] * effective[None,:,None] * kfe.density) * kfe.cell_weight)
                output = {"hjb_converged": hjb.converged, "hjb_iterations": hjb.iterations,
                    "hjb_statistic": hjb.convergence_statistic, "kfe_returned": True,
                    "kfe_raw_residual_inf": kfe.raw_residual_inf, "C": aggregate.c_ss, "L": aggregate.l_ss,
                    "A": aggregate.a_ss, "B": aggregate.b_ss, "A_plus_B": aggregate.a_ss + aggregate.b_ss,
                    "AtTax": at_tax}
                output.update({
                    "kfe_diagnostic_status": kfe_diagnostic["classification"],
                    "kfe_normalized_mass": kfe_diagnostic["normalized_mass"],
                    "kfe_density_min": kfe_diagnostic["density_min"],
                    "kfe_density_max": kfe_diagnostic["density_max"],
                    "kfe_negative_entry_count": kfe_diagnostic["negative_entry_count"],
                    "kfe_weighted_negative_mass": kfe_diagnostic["weighted_negative_mass"],
                    "kfe_source_free_residual_inf": kfe_diagnostic["source_free_residual_numerator"],
                    "kfe_source_free_residual_scale": kfe_diagnostic["source_free_residual_scale"],
                    "kfe_source_free_normwise_ratio": kfe_diagnostic["source_free_residual_ratio"],
                    "kfe_upper_b_face_mass": kfe_diagnostic["upper_b_face_probability_mass"],
                })
                if not all(np.isfinite(float(output[key])) for key in
                           ("hjb_statistic", "kfe_raw_residual_inf", "C", "L", "A", "B", "A_plus_B", "AtTax")):
                    raise RuntimeError("nonfinite household or aggregate output")
                write_json(province_root / "household_return.json", output)
                outputs.append(output); counters["household_calls_returned"] += 1

            batch = PreFrozenHouseholdOutputBatch(
                ct=[row["C"] for row in outputs], household_lt=[row["L"] for row in outputs],
                at=[row["A"] for row in outputs], bt=[row["B"] for row in outputs],
                at_tax=[row["AtTax"] for row in outputs], converged=tuple(row["hjb_converged"] for row in outputs),
                diagnostics=tuple({"hjb_converged": row["hjb_converged"], "hjb_iterations": row["hjb_iterations"],
                    "hjb_statistic": row["hjb_statistic"], "kfe_returned": True} for row in outputs))

            original = {name: getattr(one_turn_module, name) for name in
                        ("evaluate_firm", "composite_household_wages", "reconstruct_migration_labor", "allocate_productive_capital")}
            def observed_firm(province, *args, **kwargs):
                counters["firm_calls"] += 1; counters["province_updates_attempted"] += 1
                current.update(stage="FIRM", province=province["name"], province_index=payload["province_order"].index(province["name"]))
                result = original["evaluate_firm"](province, *args, **kwargs)
                counters["firm_returns"] += 1; counters["province_updates_completed"] += 1
                return result
            def observed_wage(*args, **kwargs):
                counters["wage_batch_calls"] += 1; result = original["composite_household_wages"](*args, **kwargs)
                counters["wage_province_outputs"] += len(result); return result
            def observed_migration(*args, **kwargs):
                counters["migration_calls"] += 1; return original["reconstruct_migration_labor"](*args, **kwargs)
            def observed_capital(*args, **kwargs):
                counters["capital_allocation_calls"] += 1; return original["allocate_productive_capital"](*args, **kwargs)
            one_turn_module.evaluate_firm = observed_firm
            one_turn_module.composite_household_wages = observed_wage
            one_turn_module.reconstruct_migration_labor = observed_migration
            one_turn_module.allocate_productive_capital = observed_capital
            try:
                current.update(stage="ONE_TURN", province=None, province_index=None)
                counters["one_turn_executions"] += 1
                turn = one_turn_module.run_source_faithful_one_turn(OneTurnInputs(
                    tuple(payload["province_order"]), states, model_params, phi, wedges, batch))
                counters["one_turn_returns"] += 1
            finally:
                for name, function in original.items(): setattr(one_turn_module, name, function)

            current["stage"] = "CONTROLLER"
            lt_row_sum_gap = float(np.max(np.abs(
                np.sum(turn.migration.lt_mat, axis=1) - turn.migration.lt_supply)))
            lt_national_sum_gap = float(abs(
                np.sum(turn.migration.lt_mat) - np.sum(turn.migration.lt_supply)))
            before = _post_turn_states(states, batch, turn)
            nk_gap, yt_gap, household_count, ra_upper, ra_lower, wage_upper, wage_lower, converged = _diagnostics(
                before, batch, tkn_ratio, 1e-9)
            counters["controller_calls"] += 1
            if converged:
                next_states = before
                actions = tuple(AdaptiveAction(str(state["name"]), False, float(state["Zt"]), float(state["Zt"]),
                    "NONE", float(state["GovInv"]), float(state["GovInv"])) for state in before)
                tkn_after = np.array(tkn_ratio, copy=True)
            else:
                next_states, actions = _adapt(before, float(np.max(nk_gap)), True)
                counters["adaptation_calls"] += 1
                tkn_after = np.array([0.6 * float(state["KNratio"]) + 0.4 * tkn_ratio[i]
                                      for i, state in enumerate(next_states)])
            controller = {"household_converged_count": household_count,
                "all_household_hjb_converged": household_count == 31,
                "max_nk_gap": float(np.max(nk_gap)),
                "max_nk_gap_province": payload["province_order"][int(np.argmax(nk_gap))],
                "max_yt_gap": float(np.max(yt_gap)), "ra_upper_count": ra_upper, "ra_lower_count": ra_lower,
                "wage_upper_count": wage_upper, "wage_lower_count": wage_lower,
                "source_converged": converged, "adaptation_allowed": float(np.max(nk_gap)) < 0.1,
                "labor_row_sum_identity_max_abs_gap": lt_row_sum_gap,
                "labor_national_matrix_vs_destination_sum_abs_gap": lt_national_sum_gap,
                "actions": single.jsonable(actions)}
            counters["adaptation_gate_open_count"] += int(controller["adaptation_allowed"])
            rows = []
            for index, state in enumerate(states):
                firm = turn.firms[index]; action = actions[index]; output = outputs[index]
                target = payload["province_inputs"][index]
                ktarget = float(target["k0_mu"])
                ltarget = float(target["n0_nu"])
                private_k = float(turn.capital.kt_supply[index])
                firm_total_k = float(firm.Kt)
                firm_labor = float(turn.migration.lt_supply[index])
                origin_contributions = np.asarray(turn.migration.lt_mat[index, :], dtype=float)
                top_origin_index = int(np.argmax(origin_contributions))
                row = {"turn": turn_index, "province_index": index, "province": state["name"],
                    "province_name": state["name"],
                    "Ktarget_2018_MU": ktarget, "Kt_supply_private_MU": private_k,
                    "GovInv_before_MU": float(state["GovInv"]), "GovInv_after_MU": float(action.govinv_after),
                    "firm_K_total_MU": firm_total_k,
                    "firm_K_total_over_Ktarget": firm_total_k / ktarget,
                    "private_K_over_Ktarget": private_k / ktarget,
                    "GovInv_before_over_Ktarget": float(state["GovInv"]) / ktarget,
                    "GovInv_after_over_Ktarget": float(action.govinv_after) / ktarget,
                    "Ltarget_proxy_NU": ltarget, "firm_Lt_supply": firm_labor,
                    "firm_Lt_over_population_proxy": firm_labor / ltarget,
                    "net_destination_labor_gain_loss_NU": firm_labor - ltarget,
                    "top_origin_index": top_origin_index,
                    "top_origin_province": payload["province_order"][top_origin_index],
                    "top_origin_contribution": float(origin_contributions[top_origin_index]),
                    "top_origin_share_of_destination_supply": float(origin_contributions[top_origin_index] / firm_labor),
                    "GDP": state["Yt0"], "POP": state["N"], "CAP": state["Kt0"], "alpha": state["alpha"],
                    "same_year_Zt": state["Zt"], "GovInv": state["GovInv"], "entering_Yt": state["Yt"],
                    "entering_firm_ra": state["ra"], "household_rah": state["rah"],
                    "rah_source": provenance[index]["source"], "rah_source_value": provenance[index]["value"],
                    "household_rb": state["rb"], "household_composite_wage": state["w"],
                    "entering_Lt_prev": state["Lt_prev"], "firm_source_Lt_prev": output["L"],
                    "household_Lt_return": output["L"], "destination_lt_supply": turn.migration.lt_supply[index],
                    "firm_ra0": firm.ra0, "firm_ra_used": firm.ra, "firm_rk": firm.rk,
                    "firm_wage_raw": firm.wt0, "firm_wage_used": firm.wjt,
                    "ramin": state["ramin"], "ramax": state["ramax"],
                    "wjtmin": state["wjtmin"], "wjtmax": state["wjtmax"],
                    "hjb_converged": output["hjb_converged"], "hjb_iterations": output["hjb_iterations"],
                    "hjb_statistic": output["hjb_statistic"], "kfe_returned": True,
                    "kfe_raw_residual_inf": output["kfe_raw_residual_inf"], "C": output["C"], "L": output["L"],
                    "A": output["A"], "B": output["B"], "A_plus_B": output["A_plus_B"],
                    "kfe_diagnostic_status": output["kfe_diagnostic_status"],
                    "kfe_normalized_mass": output["kfe_normalized_mass"],
                    "kfe_density_min": output["kfe_density_min"],
                    "kfe_density_max": output["kfe_density_max"],
                    "kfe_negative_entry_count": output["kfe_negative_entry_count"],
                    "kfe_weighted_negative_mass": output["kfe_weighted_negative_mass"],
                    "kfe_source_free_residual_inf": output["kfe_source_free_residual_inf"],
                    "kfe_source_free_residual_scale": output["kfe_source_free_residual_scale"],
                    "kfe_source_free_normwise_ratio": output["kfe_source_free_normwise_ratio"],
                    "kfe_upper_b_face_mass": output["kfe_upper_b_face_mass"],
                    "Y": firm.Yt, "Zt": state["Zt"],
                    "nk_gap": nk_gap[index], "yt_gap": yt_gap[index],
                    "GDP_level_gap": abs(float(firm.Yt) / float(state["Yt0"]) - 1.0),
                    "adaptation_gate_open": controller["adaptation_allowed"],
                    "ra_clipped_lower": firm.ra == state["ramin"] and firm.ra0 < state["ramin"],
                    "ra_clipped_upper": firm.ra == state["ramax"] and firm.ra0 > state["ramax"],
                    "wage_clipped_lower": firm.wjt == state["wjtmin"] and firm.wt0 < state["wjtmin"],
                    "wage_clipped_upper": firm.wjt == state["wjtmax"] and firm.wt0 > state["wjtmax"],
                    "zt_adjusted": action.zt_adjusted, "zt_after": action.zt_after,
                    "govinv_action": action.govinv_action, "govinv_after": action.govinv_after}
                rows.append(row)
            write_json(turn_root / "per_province_observables.json", rows)
            with (turn_root / "per_province_observables.csv").open("x", encoding="utf-8-sig", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
            write_json(turn_root / "controller_observables.json", controller)
            summary = national_summary(turn_index, rows, controller)
            write_json(turn_root / "national_summary.json", summary)
            turn_summaries.append(summary)
            counters["turns_completed"] += 1
            prior_entering_states = states
            states = _freeze_state(next_states)
            tkn_ratio = tkn_after
            if converged:
                termination_reason = "SOURCE_FINAL_STEADY_STATE_PREDICATE"
                verdict = VERDICT_PASS if turn_index >= 20 else VERDICT_PARTIAL
                counters["trajectory_returns"] = 1
                break
        else:
            termination_reason = "AUTHORIZED_25_TURN_CEILING_REACHED"
            verdict = VERDICT_PASS
            counters["trajectory_returns"] = 1
    except Exception as exc:
        counters["household_calls_failed"] = counters["household_calls_attempted"] - counters["household_calls_returned"]
        error = {"type": type(exc).__name__, "message": str(exc), "turn": current["turn"],
                 "stage": current["stage"], "province_index": current["province_index"],
                 "province": current["province"]}
        verdict = VERDICT_PARTIAL
        termination_reason = "HARD_SCIENTIFIC_FAILURE"
        write_json(root / "scientific_failure.json", error)
    finally:
        single.oracle.linalg.spsolve = original_spsolve
        single.LABOR_BRENTQ = original_brentq
    counters["household_calls_failed"] = counters["household_calls_attempted"] - counters["household_calls_returned"]
    write_json(root / "transition_summary.json", {"schema": "CH5_CORRECTED_2018_25TURN_KL_TRANSITION_V1",
        "turns": turn_summaries, "actual_turns_completed": counters["turns_completed"],
        "turn25_completed": counters["turns_completed"] == 25, "termination_reason": termination_reason})
    write_json(root / "call_ledger.json", {"schema": "CH5_CORRECTED_2018_25TURN_KL_CALL_LEDGER_V1",
        "counts": counters, "elapsed_seconds": time.monotonic() - started, "failed_calls_counted": True,
        "matlab_calls": 0, "turn26_or_later_calls": 0, "second_trajectory_calls": 0,
        "parameter_cell_comparisons": 0, "steady_state_calls": 0, "ge_calls": 0,
        "annual_model_calls": 0, "irf_calls": 0, "results_calls": 0})
    write_json(root / "terminal_result.json", {"schema": "CH5_CORRECTED_2018_25TURN_KL_TERMINAL_V1",
        "verdict": verdict, "error": error, "actual_turns_completed": counters["turns_completed"],
        "termination_reason": termination_reason, "turn26_plus_authorized": "NO",
        "steady_state_authorized": "NO", "results_eligible": False})
    return 0 if verdict == VERDICT_PASS else 2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(); sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("distance_workbook", type=Path); prep.add_argument("evidence_root", type=Path)
    launch = sub.add_parser("run"); launch.add_argument("evidence_root", type=Path)
    args = parser.parse_args(argv)
    if args.command == "prepare":
        prepare(args.distance_workbook, args.evidence_root); return 0
    return execute(args.evidence_root)


if __name__ == "__main__":
    raise SystemExit(main())
