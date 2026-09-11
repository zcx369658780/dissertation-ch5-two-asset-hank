"""Run one G1 initialization observation and one isolated 25-turn trajectory."""
from __future__ import annotations

import argparse
import csv
import json
import os
import platform
import sys
import time
from collections import Counter
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

import numpy as np

REPO = Path(__file__).resolve().parents[3]
for item in (REPO / "src", REPO):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))

from ch5_two_asset_hank.multi_province.capital_allocation import (  # noqa: E402
    CapitalAllocationInputs,
    allocate_productive_capital,
)
from ch5_two_asset_hank.multi_province import one_turn as one_turn_module  # noqa: E402
from ch5_two_asset_hank.multi_province.one_turn import (  # noqa: E402
    OneTurnInputs,
    PreFrozenHouseholdOutputBatch,
)
from ch5_two_asset_hank.multi_province.steady_state import (  # noqa: E402
    AdaptiveAction,
    _adapt,
    _diagnostics,
    _freeze_state,
    _post_turn_states,
)
from validators.multi_province.corrected_2018_single_turn import run as single  # noqa: E402
from validators.multi_province.corrected_2018_hjb_propagation_25turn_kl import run as g0  # noqa: E402
from validators.multi_province.initial_private_k_residual_govinv_probe.run import (  # noqa: E402
    ASSET_BRIDGE_RULE,
    residual_govinv_accounting,
)

VERDICT_PASS = "G1_RESIDUAL_GOVINV_25TURN_PASS__INITIAL_CAPITAL_ALIGNMENT_IMPROVES_AND_BOUNDED_PATH_QUANTIFIED"
VERDICT_PARTIAL = "G1_RESIDUAL_GOVINV_25TURN_PARTIAL__INITIAL_ALIGNMENT_VALID_BUT_TRUE_HARD_FAILURE_BEFORE_LATE_WINDOW"
VERDICT_FAIL = "G1_RESIDUAL_GOVINV_25TURN_FAIL__INITIAL_ALIGNMENT_VALID_BUT_UNCHANGED_CONTROLLER_RECREATES_OR_WORSENS_INSTABILITY"
THREAD_ENV = ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS")


def write_json(path: Path, value: Any) -> None:
    single.write_json(path, value)


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(single.jsonable(rows))


def record_phase_a(evidence_root: Path, test_processes: int, test_cases: int, compile_processes: int) -> None:
    root = Path(evidence_root)
    root.mkdir(parents=True, exist_ok=False)
    write_json(root / "phase_a_zero_science_receipt.json", {
        "schema": "CH5_G1_RESIDUAL_GOVINV_PHASE_A_ZERO_SCIENCE_V1",
        "status": "PASS",
        "focused_test_processes": test_processes,
        "focused_test_cases": test_cases,
        "compile_processes": compile_processes,
        "scientific_processes": 0,
        "hjb_calls": 0,
        "kfe_calls": 0,
        "initialization_observations": 0,
        "trajectory_calls": 0,
        "contract": {
            "separate_initialization_stage": "INITIALIZATION_OBSERVATION",
            "only_initial_govinv_replaced": True,
            "source_faithful_labor_route": True,
            "normalized_labor_route_active": False,
            "historical_controller_unchanged": True,
            "finite_hjb_nonconvergence_continues_diagnostic_only": True,
        },
    })


def _require_phase_a(root: Path) -> dict[str, Any]:
    path = root / "phase_a_zero_science_receipt.json"
    if not path.is_file():
        raise ValueError("Phase A zero-science receipt is missing")
    receipt = json.loads(path.read_text(encoding="utf-8"))
    if receipt.get("status") != "PASS" or receipt.get("scientific_processes") != 0:
        raise ValueError("Phase A zero-science gate did not pass")
    if any(receipt.get(key) != 0 for key in ("hjb_calls", "kfe_calls", "initialization_observations", "trajectory_calls")):
        raise ValueError("Phase A receipt records science")
    return receipt


def prepare(distance_workbook: Path, evidence_root: Path) -> None:
    root = Path(evidence_root)
    _require_phase_a(root)
    if (root / "runtime_input_payload.json").exists():
        raise FileExistsError("prepared runtime input already exists")
    payload = single.build_runtime_payload(Path(distance_workbook))
    payload["schema"] = "CH5_G1_RESIDUAL_GOVINV_25TURN_ISOLATED_RUNTIME_INPUT_V1"
    payload_path = root / "runtime_input_payload.json"
    write_json(payload_path, payload)
    single.validate_serialized_payload(json.loads(payload_path.read_text(encoding="utf-8")))
    write_json(root / "runtime_input_receipt.json", {
        "schema": "CH5_G1_RESIDUAL_GOVINV_25TURN_ISOLATED_RUNTIME_RECEIPT_V1",
        "runtime_payload_sha256": single.file_sha256(payload_path),
        "province_count": 31,
        "province_order": payload["province_order"],
        "metadata": payload["metadata"],
        "source_identities": payload["source_identities"],
        "pre_science_assertion": payload["pre_science_assertion"],
        "initialization_rule": "GovInv0_G1=max(Ktarget-Kt_supply_initial,0)",
        "asset_bridge": ASSET_BRIDGE_RULE,
        "labor_route": "SOURCE_FAITHFUL_G0_BASELINE__NORMALIZED_SUCCESSOR_NOT_ACTIVE",
        "scientific_calls": 0,
    })
    source_paths = (
        Path(__file__), Path(single.__file__), Path(g0.__file__),
        REPO / "validators/multi_province/initial_private_k_residual_govinv_probe/run.py",
        REPO / "src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py",
        REPO / "src/ch5_two_asset_hank/multi_province/capital_allocation.py",
        REPO / "src/ch5_two_asset_hank/multi_province/one_turn.py",
        REPO / "src/ch5_two_asset_hank/multi_province/steady_state.py",
        REPO / "src/ch5_two_asset_hank/multi_province/firm.py",
        REPO / "exports/matlab_faithful_two_asset_ha.py",
        REPO / "src/ch5_two_asset_hank/matlab_faithful_hjb.py",
        REPO / "src/ch5_two_asset_hank/matlab_faithful_kfe.py",
    )
    protected_root = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK")
    protected_names = ("HANK_mp_1eq.m", "HANK_mp_1turn.m", "HANK_firm.m")
    protected = {
        name: {"path": str(protected_root / name), "sha256": single.file_sha256(protected_root / name),
               "access": "READ_ONLY"}
        for name in protected_names if (protected_root / name).is_file()
    }
    write_json(root / "source_hash_receipt.json", {
        "schema": "CH5_G1_RESIDUAL_GOVINV_25TURN_ISOLATED_SOURCE_HASH_V1",
        "files": {str(path.relative_to(REPO)).replace("\\", "/"): single.file_sha256(path) for path in source_paths},
        "protected_matlab": protected,
        "scientific_calls": 0,
    })
    write_json(root / "bounded_invocation_receipt.json", {
        "schema": "CH5_G1_RESIDUAL_GOVINV_25TURN_ISOLATED_BOUNDED_INVOCATION_V1",
        "prepare_entrypoint": "validators/multi_province/g1_residual_govinv_25turn_isolated/run.py prepare",
        "science_entrypoint": "validators/multi_province/g1_residual_govinv_25turn_isolated/run.py run",
        "scientific_processes_maximum": 1,
        "initialization": {"hjb": 31, "kfe": 31, "aggregate": 31, "at_only_allocation": 1},
        "trajectory": {"count": 1, "outer_turn_ceiling": 25, "province_updates_ceiling": 775},
        "scientific_retries": 0,
        "second_initialization_passes": 0,
        "second_trajectories": 0,
        "beta_cells": 0,
        "scientific_calls_at_prepare": 0,
    })


def _household_pass(
    states: tuple[Mapping[str, object], ...], payload: dict[str, Any], grid: Any,
    params: Any, numerics: Any, root: Path, counters: dict[str, int], current: dict[str, Any],
    label: str, turn_index: int,
) -> list[dict[str, Any]]:
    outputs: list[dict[str, Any]] = []
    for index, state in enumerate(states):
        province = payload["province_order"][index]
        province_root = root / "household" / f"p{index:02d}_{province}"
        current.update(stage=f"{label}_NATIVE_INITIALIZATION", turn=turn_index,
                       province_index=index, province=province)
        counters["household_calls_attempted"] += 1
        counters[f"{label.lower()}_household_calls_attempted"] += 1
        counters["native_initializations_attempted"] += 1
        def enter_root() -> None: counters["labor_roots_attempted"] += 1
        def return_root() -> None: counters["labor_roots_returned"] += 1
        initial, labor = single.source_initial_arrays(state, grid, params, enter_root, return_root)
        counters["native_initializations_returned"] += 1
        current["stage"] = f"{label}_HJB"
        counters["hjb_calls"] += 1
        counters[f"{label.lower()}_hjb_calls"] += 1
        hjb = single.oracle.solve_matlab_faithful_hjb(
            grid, params,
            single.oracle.HouseholdInputs(float(state["rah"]), float(state["rb"]), float(state["tau"]),
                                          np.array([state["w"]]), np.array([0.0]), np.array([1.0])),
            initial, labor, float(state["Tt"]), float(state["rb_gap"]), numerics,
        )
        counters["hjb_returns"] += 1
        classification = g0.validate_hjb_return_for_continuation(hjb)
        single._save_hjb(province_root / "hjb_return.npz", hjb)
        current["stage"] = f"{label}_KFE"
        counters["kfe_calls"] += 1
        counters[f"{label.lower()}_kfe_calls"] += 1
        kfe = single.oracle.solve_matlab_faithful_stationary_kfe(
            hjb.post_convergence_operator.full, shape=(20, 20, 2),
            db=float(grid.b[1] - grid.b[0]), da=float(grid.a[1] - grid.a[0]),
        )
        counters["kfe_returns"] += 1
        g0.validate_kfe_return_for_continuation(kfe)
        single._save_kfe(province_root / "kfe_return.npz", kfe)
        kd = g0.kfe_distribution_diagnostics(hjb, kfe)
        current["stage"] = f"{label}_AGGREGATE"
        counters["aggregate_calls"] += 1
        counters[f"{label.lower()}_aggregate_calls"] += 1
        aggregate = single.oracle.aggregate_stationary_household(grid, hjb.consumption, hjb.labor, kfe.density)
        counters["aggregate_returns"] += 1
        effective = single.oracle.matlab_faithful_illiquid_return(grid.a, grid.a[-1], float(state["rah"]))
        at_tax = aggregate.a_ss * float(state["rah"]) - float(
            np.sum(grid.a[None, :, None] * effective[None, :, None] * kfe.density) * kfe.cell_weight)
        output = {
            "stage_label": label, "turn": turn_index, "province_index": index, "province": province,
            "hjb_converged": bool(hjb.converged), "hjb_iterations": int(hjb.iterations),
            "hjb_statistic": float(hjb.convergence_statistic), "hjb_acceptance_classification": classification,
            "downstream_kfe_attempted": True, "downstream_kfe_returned": True,
            "continuation_status": "CONTINUED_TO_HOUSEHOLD_BATCH", "kfe_returned": True,
            "kfe_raw_residual_inf": float(kfe.raw_residual_inf),
            "kfe_diagnostic_status": kd["classification"],
            "kfe_normalized_mass": kd["normalized_mass"], "kfe_density_min": kd["density_min"],
            "kfe_density_max": kd["density_max"], "kfe_negative_entry_count": kd["negative_entry_count"],
            "kfe_weighted_negative_mass": kd["weighted_negative_mass"],
            "kfe_source_free_residual_inf": kd["source_free_residual_numerator"],
            "kfe_source_free_residual_scale": kd["source_free_residual_scale"],
            "kfe_source_free_normwise_ratio": kd["source_free_residual_ratio"],
            "kfe_upper_b_face_mass": kd["upper_b_face_probability_mass"],
            "C": float(aggregate.c_ss), "L": float(aggregate.l_ss), "A": float(aggregate.a_ss),
            "B": float(aggregate.b_ss), "A_plus_B": float(aggregate.a_ss + aggregate.b_ss), "AtTax": at_tax,
        }
        if not all(np.isfinite(float(output[key])) for key in
                   ("hjb_statistic", "kfe_raw_residual_inf", "C", "L", "A", "B", "A_plus_B", "AtTax")):
            raise RuntimeError(f"{province}: nonfinite household or aggregate output")
        write_json(province_root / "household_return.json", output)
        outputs.append(output)
        counters["household_calls_returned"] += 1
        counters[f"{label.lower()}_household_calls_returned"] += 1
    return outputs


def _batch(outputs: list[dict[str, Any]]) -> PreFrozenHouseholdOutputBatch:
    return g0.build_household_batch(outputs)


def build_g1_initial_states(
    states_g0: tuple[Mapping[str, object], ...], target: np.ndarray, private: np.ndarray,
) -> tuple[tuple[dict[str, object], ...], dict[str, np.ndarray]]:
    """Return a new state tuple in which GovInv is the only replaced field."""
    accounting = residual_govinv_accounting(target, private)
    if len(states_g0) != target.size:
        raise ValueError("state and capital vector counts differ")
    states = tuple({**state, "GovInv": float(accounting["govinv_g1"][i])}
                   for i, state in enumerate(states_g0))
    for i, (before, after) in enumerate(zip(states_g0, states)):
        changed = [key for key in before if before[key] != after[key]]
        if changed != ["GovInv"]:
            raise RuntimeError(f"{before['name']}: G1 must replace only GovInv, changed={changed}")
        expected_total = max(float(target[i]), float(private[i]))
        if abs(float(accounting["g1_total"][i]) - expected_total) > 1e-9 * max(1.0, expected_total):
            raise RuntimeError(f"{before['name']}: initial G1 accounting assertion failed")
    return states, accounting


def classify_completed_path(summaries: list[dict[str, Any]]) -> str:
    """Apply the task's terminal verdict semantics to saved turn summaries."""
    if len(summaries) != 25:
        return VERDICT_PARTIAL
    late = summaries[19:25]
    late_overshoot = max(float(row["firm_K_total_over_Ktarget"]["median"]) for row in late) > 1.25
    controller_increases = sum(int(row["controller"]["govinv_action_counts"].get(
        "HIGH_RA_INCREASE_1P1", 0)) for row in summaries)
    if late_overshoot and controller_increases > 0:
        return VERDICT_FAIL
    return VERDICT_PASS


def execute(evidence_root: Path) -> int:
    root = Path(evidence_root)
    _require_phase_a(root)
    payload_path = root / "runtime_input_payload.json"
    if not payload_path.is_file() or not (root / "runtime_input_receipt.json").is_file():
        raise ValueError("prepared runtime input is missing")
    if (root / "science_started.json").exists():
        raise RuntimeError("scientific process already started; retry prohibited")
    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    single.validate_serialized_payload(payload)
    keys = (
        "turns_entered", "turns_completed", "province_updates_attempted", "province_updates_completed",
        "household_calls_attempted", "household_calls_returned", "household_calls_failed",
        "initialization_observation_household_calls_attempted", "initialization_observation_household_calls_returned",
        "initialization_observation_hjb_calls", "initialization_observation_kfe_calls", "initialization_observation_aggregate_calls",
        "trajectory_household_calls_attempted", "trajectory_household_calls_returned",
        "trajectory_hjb_calls", "trajectory_kfe_calls", "trajectory_aggregate_calls",
        "native_initializations_attempted", "native_initializations_returned", "labor_roots_attempted", "labor_roots_returned",
        "brentq_calls_attempted", "brentq_calls_returned", "hjb_calls", "hjb_returns", "hjb_direct_solves",
        "kfe_calls", "kfe_returns", "kfe_direct_solves", "aggregate_calls", "aggregate_returns",
        "initial_at_only_capital_allocation_calls", "one_turn_executions", "one_turn_returns", "migration_calls",
        "capital_allocation_calls", "firm_calls", "firm_returns", "wage_batch_calls", "wage_province_outputs",
        "controller_calls", "adaptation_calls", "adaptation_gate_open_count",
    )
    counters = {key: 0 for key in keys}
    counters.update({"scientific_processes": 1, "initialization_observation_passes": 1,
                     "trajectory_attempts": 1, "trajectory_returns": 0, "scientific_retries": 0})
    write_json(root / "science_started.json", {
        "schema": "CH5_G1_RESIDUAL_GOVINV_25TURN_ISOLATED_SCIENCE_STARTED_V1",
        "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "runtime_payload_sha256": single.file_sha256(payload_path),
        "process_id": os.getpid(), "python": sys.version, "platform": platform.platform(),
        "thread_environment": {key: os.environ.get(key) for key in THREAD_ENV},
        "authorized_initialization_observation_passes": 1, "authorized_trajectory_count": 1,
        "authorized_turns_maximum": 25, "authorized_province_updates_maximum": 775,
        "scientific_retries": 0,
    })
    states_g0 = tuple(dict(item) for item in payload["states"])
    grid = single.oracle.MatlabFaithfulHJBGrid(np.linspace(-2, 5, 20), np.linspace(0, 10, 20),
        np.array([0.8, 1.3]), np.array([[-1 / 3, 1 / 3], [1 / 3, -1 / 3]]))
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
    error: dict[str, Any] | None = None
    summaries: list[dict[str, Any]] = []
    termination_reason = "NOT_STARTED"
    def counted_spsolve(*args, **kwargs):
        key = "hjb_direct_solves" if "HJB" in current["stage"] else "kfe_direct_solves"
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
        init_outputs = _household_pass(states_g0, payload, grid, params, numerics,
                                       root / "initialization_observation", counters, current,
                                       "INITIALIZATION_OBSERVATION", 0)
        current["stage"] = "INITIALIZATION_AT_ONLY_CAPITAL_ALLOCATION"
        counters["initial_at_only_capital_allocation_calls"] += 1
        allocation = allocate_productive_capital(CapitalAllocationInputs(
            illiquid_assets_at=[row["A"] for row in init_outputs],
            population=[state["N"] for state in states_g0],
            inter_province_ratio=[state["inter_prv_ratio"] for state in states_g0],
            old_firm_return_ra=[state["ra"] for state in states_g0],
        ))
        target = np.asarray([state["Kt0"] for state in states_g0], dtype=float)
        private = np.asarray(allocation.kt_supply, dtype=float)
        states, accounting = build_g1_initial_states(states_g0, target, private)
        receipt_rows = []
        for i, (state, observed) in enumerate(zip(states, init_outputs)):
            receipt_rows.append({
                "province_index": i, "province": state["name"], "stage_label": "INITIALIZATION_OBSERVATION",
                "Ktarget_2018_MU": target[i], "At_initial": observed["A"], "Bt_initial": observed["B"],
                "Lt_initial": observed["L"], "Ct_initial": observed["C"],
                "HJB_converged": observed["hjb_converged"],
                "HJB_classification": observed["hjb_acceptance_classification"],
                "KFE_classification": observed["kfe_diagnostic_status"],
                "Kt_supply_initial_MU_beta1": private[i], "private_K_over_target_beta1": private[i] / target[i],
                "GovInv0_G0_MU": accounting["govinv_g0"][i], "GovInv0_G1_MU": accounting["govinv_g1"][i],
                "firm_K_accounting_G0_MU": accounting["g0_total"][i],
                "firm_K_accounting_G1_MU": accounting["g1_total"][i],
                "firm_K_G0_over_target": accounting["g0_total"][i] / target[i],
                "firm_K_G1_over_target": accounting["g1_total"][i] / target[i],
                "beta_a_star": accounting["beta_star"][i],
                "outer_turn_1_initial_state_json": json.dumps(single.jsonable(state), ensure_ascii=False, sort_keys=True),
                "only_initial_state_field_replaced": "GovInv",
            })
        write_csv(root / "initialization_receipt_31province.csv", receipt_rows)
        init_ratios = accounting["g1_total"] / target
        write_json(root / "national_initialization_summary.json", {
            "schema": "CH5_G1_RESIDUAL_GOVINV_NATIONAL_INITIALIZATION_V1",
            "stage_label": "INITIALIZATION_OBSERVATION", "not_outer_turn_1": True,
            "province_count": 31, "private_below_target_count": int(np.count_nonzero(private < target)),
            "residual_zero_count": int(np.count_nonzero(accounting["govinv_g1"] == 0.0)),
            "accounting_aligned_count": int(np.count_nonzero(init_ratios == 1.0)),
            "accounting_identity_max_abs_error": float(np.max(np.abs(accounting["g1_total"] - np.maximum(target, private)))),
            "private_K_over_target": {
                "min": float(np.min(private / target)), "median": float(np.median(private / target)), "max": float(np.max(private / target))},
            "G0_total_over_target": {"min": float(np.min(accounting["g0_total"] / target)),
                "median": float(np.median(accounting["g0_total"] / target)), "max": float(np.max(accounting["g0_total"] / target))},
            "G1_total_over_target": {"min": float(np.min(init_ratios)), "median": float(np.median(init_ratios)), "max": float(np.max(init_ratios))},
            "HJB_converged_count": sum(row["hjb_converged"] for row in init_outputs),
            "KFE_classification_counts": dict(Counter(row["kfe_diagnostic_status"] for row in init_outputs)),
            "only_initial_state_field_replaced": "GovInv", "asset_bridge": ASSET_BRIDGE_RULE,
            "results_eligible": False,
        })
        tkn_ratio = np.full(31, 3.0)
        wedges = np.array(payload["matrices"]["sigmau_destination_origin"], dtype=float)
        prior_entering_states: tuple[Mapping[str, object], ...] | None = None
        for turn_index in range(1, 26):
            current.update(stage="TURN_ENTRY", turn=turn_index, province_index=None, province=None)
            counters["turns_entered"] += 1
            turn_root = root / f"turn_{turn_index:02d}"
            provenance = [g0.rah_provenance(turn_index, i, states, prior_entering_states) for i in range(31)]
            write_json(turn_root / "entering_state.json", {"turn": turn_index, "states": states,
                "rah_provenance": provenance, "tkn_ratio": tkn_ratio,
                "initialization_route": "G1_RESIDUAL_GOVINV"})
            productivity = np.array([float(state["Yt"]) / float(state["Lt"]) for state in states])
            phi = 1.0 + 0.3 * (productivity[:, None] - productivity[None, :]) / (productivity[:, None] + productivity[None, :])
            outputs = _household_pass(states, payload, grid, params, numerics, turn_root, counters, current,
                                      "TRAJECTORY", turn_index)
            batch = _batch(outputs)
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
            before = _post_turn_states(states, batch, turn)
            nk_gap, yt_gap, household_count, ra_upper, ra_lower, wage_upper, wage_lower, converged = _diagnostics(
                before, batch, tkn_ratio, 1e-9)
            every_hjb = g0.all_household_hjb_converged(batch)
            if converged and not every_hjb:
                raise RuntimeError("source final predicate passed despite a false HJB flag")
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
            controller = {"household_converged_count": household_count, "all_household_hjb_converged": every_hjb,
                "max_nk_gap": float(np.max(nk_gap)), "max_nk_gap_province": payload["province_order"][int(np.argmax(nk_gap))],
                "max_yt_gap": float(np.max(yt_gap)), "ra_upper_count": ra_upper, "ra_lower_count": ra_lower,
                "wage_upper_count": wage_upper, "wage_lower_count": wage_lower, "source_converged": converged,
                "adaptation_allowed": float(np.max(nk_gap)) < 0.1,
                "labor_row_sum_identity_max_abs_gap": float(np.max(np.abs(np.sum(turn.migration.lt_mat, axis=1) - turn.migration.lt_supply))),
                "labor_national_matrix_vs_destination_sum_abs_gap": float(abs(np.sum(turn.migration.lt_mat) - np.sum(turn.migration.lt_supply))),
                "actions": single.jsonable(actions)}
            counters["adaptation_gate_open_count"] += int(controller["adaptation_allowed"])
            rows = []
            for i, state in enumerate(states):
                firm, action, output = turn.firms[i], actions[i], outputs[i]
                ktarget = float(payload["province_inputs"][i]["k0_mu"])
                private_k = float(turn.capital.kt_supply[i])
                firm_labor = float(turn.migration.lt_supply[i])
                row = {"turn": turn_index, "province_index": i, "province": state["name"],
                    "Ktarget_2018_MU": ktarget, "Kt_supply_private_MU": private_k,
                    "GovInv_before_MU": float(state["GovInv"]), "GovInv_after_MU": float(action.govinv_after),
                    "firm_K_total_MU": float(firm.Kt), "firm_K_total_over_Ktarget": float(firm.Kt) / ktarget,
                    "private_K_over_Ktarget": private_k / ktarget,
                    "GovInv_before_over_Ktarget": float(state["GovInv"]) / ktarget,
                    "GovInv_after_over_Ktarget": float(action.govinv_after) / ktarget,
                    "Ltarget_proxy_NU": float(payload["province_inputs"][i]["n0_nu"]),
                    "firm_Lt_supply": firm_labor,
                    "firm_Lt_over_population_proxy": firm_labor / float(payload["province_inputs"][i]["n0_nu"]),
                    "GDP": state["Yt0"], "POP": state["N"], "CAP": state["Kt0"], "alpha": state["alpha"],
                    "same_year_Zt": state["Zt"], "GovInv": state["GovInv"], "entering_Yt": state["Yt"],
                    "entering_firm_ra": state["ra"], "household_rah": state["rah"],
                    "rah_source": provenance[i]["source"], "household_rb": state["rb"],
                    "household_composite_wage": state["w"], "entering_Lt_prev": state["Lt_prev"],
                    "firm_source_Lt_prev": output["L"], "household_Lt_return": output["L"],
                    "destination_lt_supply": firm_labor, "firm_ra0": firm.ra0, "firm_ra_used": firm.ra,
                    "firm_rk": firm.rk, "firm_wage_raw": firm.wt0, "firm_wage_used": firm.wjt,
                    "ramin": state["ramin"], "ramax": state["ramax"], "wjtmin": state["wjtmin"], "wjtmax": state["wjtmax"],
                    "hjb_converged": output["hjb_converged"], "hjb_iterations": output["hjb_iterations"],
                    "hjb_statistic": output["hjb_statistic"], "hjb_acceptance_classification": output["hjb_acceptance_classification"],
                    "downstream_kfe_attempted": True, "downstream_kfe_returned": True, "continuation_status": output["continuation_status"],
                    "kfe_returned": True, "kfe_raw_residual_inf": output["kfe_raw_residual_inf"],
                    "C": output["C"], "L": output["L"], "A": output["A"], "B": output["B"], "A_plus_B": output["A_plus_B"],
                    "kfe_diagnostic_status": output["kfe_diagnostic_status"],
                    "kfe_source_free_residual_inf": output["kfe_source_free_residual_inf"],
                    "kfe_source_free_normwise_ratio": output["kfe_source_free_normwise_ratio"],
                    "Y": firm.Yt, "Zt": state["Zt"], "Zt_before": state["Zt"], "Zt_after": action.zt_after,
                    "nk_gap": nk_gap[i], "yt_gap": yt_gap[i],
                    "GDP_level_gap": abs(float(firm.Yt) / float(state["Yt0"]) - 1.0),
                    "adaptation_gate_open": controller["adaptation_allowed"],
                    "ra_clipped_lower": firm.ra == state["ramin"] and firm.ra0 < state["ramin"],
                    "ra_clipped_upper": firm.ra == state["ramax"] and firm.ra0 > state["ramax"],
                    "wage_clipped_lower": firm.wjt == state["wjtmin"] and firm.wt0 < state["wjtmin"],
                    "wage_clipped_upper": firm.wjt == state["wjtmax"] and firm.wt0 > state["wjtmax"],
                    "zt_adjusted": action.zt_adjusted, "govinv_action": action.govinv_action,
                    "source_household_count": household_count, "source_ra_upper_count": ra_upper,
                    "source_ra_lower_count": ra_lower, "source_wage_upper_count": wage_upper,
                    "source_wage_lower_count": wage_lower, "source_all_hjb_converged": every_hjb,
                    "source_final_predicate": converged}
                rows.append(row)
            write_json(turn_root / "per_province_observables.json", rows)
            write_csv(turn_root / "per_province_observables.csv", rows)
            write_json(turn_root / "controller_observables.json", controller)
            summary = g0.national_summary(turn_index, rows, controller)
            write_json(turn_root / "national_summary.json", summary)
            summaries.append(summary)
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
            verdict = classify_completed_path(summaries)
            counters["trajectory_returns"] = 1
    except Exception as exc:
        error = {"type": type(exc).__name__, "message": str(exc), "turn": current["turn"],
                 "stage": current["stage"], "province_index": current["province_index"], "province": current["province"]}
        termination_reason = "HARD_SCIENTIFIC_FAILURE"
        write_json(root / "scientific_failure.json", error)
    finally:
        single.oracle.linalg.spsolve = original_spsolve
        single.LABOR_BRENTQ = original_brentq
    counters["household_calls_failed"] = counters["household_calls_attempted"] - counters["household_calls_returned"]
    write_json(root / "transition_summary.json", {"schema": "CH5_G1_RESIDUAL_GOVINV_25TURN_ISOLATED_TRANSITION_V1",
        "turns": summaries, "actual_turns_completed": counters["turns_completed"],
        "turn25_completed": counters["turns_completed"] == 25, "termination_reason": termination_reason})
    write_json(root / "call_ledger.json", {"schema": "CH5_G1_RESIDUAL_GOVINV_25TURN_ISOLATED_CALL_LEDGER_V1",
        "counts": counters, "elapsed_seconds": time.monotonic() - started, "failed_calls_counted": True,
        "engineering_retries": 0, "scientific_retries": 0, "second_initialization_passes": 0,
        "second_trajectory_calls": 0, "beta_parameter_cells": 0, "matlab_calls": 0,
        "turn26_or_later_calls": 0, "steady_state_calls": 0, "ge_calls": 0,
        "annual_model_calls": 0, "irf_calls": 0, "results_calls": 0})
    write_json(root / "terminal_result.json", {"schema": "CH5_G1_RESIDUAL_GOVINV_25TURN_ISOLATED_TERMINAL_V1",
        "verdict": verdict, "error": error, "actual_turns_completed": counters["turns_completed"],
        "termination_reason": termination_reason, "results_eligible": False})
    return 0 if verdict in (VERDICT_PASS, VERDICT_FAIL) else 2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    phase = sub.add_parser("record-phase-a")
    phase.add_argument("evidence_root", type=Path)
    phase.add_argument("--test-processes", type=int, required=True)
    phase.add_argument("--test-cases", type=int, required=True)
    phase.add_argument("--compile-processes", type=int, required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("distance_workbook", type=Path)
    prep.add_argument("evidence_root", type=Path)
    launch = sub.add_parser("run")
    launch.add_argument("evidence_root", type=Path)
    args = parser.parse_args(argv)
    if args.command == "record-phase-a":
        record_phase_a(args.evidence_root, args.test_processes, args.test_cases, args.compile_processes)
        return 0
    if args.command == "prepare":
        prepare(args.distance_workbook, args.evidence_root)
        return 0
    return execute(args.evidence_root)


if __name__ == "__main__":
    raise SystemExit(main())
