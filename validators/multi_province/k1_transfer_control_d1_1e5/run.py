"""Fresh G2 control versus Owner-frozen D1=1e5 bounded runtime."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any

import numpy as np

REPO = Path(__file__).resolve().parents[3]
for item in (REPO / "src", REPO):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))

from ch5_two_asset_hank.multi_province.capital_allocation import CapitalAllocationInputs
from ch5_two_asset_hank.multi_province.k1a_runtime_adapter import (
    K1ARuntimeConfig,
    allocate_k1a_capital,
    load_accepted_distance_score,
)
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER
from exports import matlab_faithful_two_asset_ha as oracle
from validators.multi_province.k1_annual_hjb_g1_vs_g2 import run as accepted
from validators.multi_province.k1_g1_vs_g2_ha_hjb_instrumented import run as trace_run
from validators.multi_province.k1_g1_vs_g2_ha_hjb_instrumented.instrumented_hjb import solve_with_trace
from validators.multi_province.k1_transfer_control_raw_candidate_census.run import _result_equality

from .receipt import D1_LIMIT, write_d1_call_chunk


TASK_ID = "CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC"
PATHS = {
    "C": ("annual_g2_control", 2.0),
    "D1": ("annual_g2_d1_1e5", 2.0),
}
G2_RETURN_GUARD = (-0.10, 0.35)
WAGE_GUARD = (0.8, 1.3)
MODEL_TIME_BASE = accepted.MODEL_TIME_BASE
ANNUAL_DELTA = accepted.ANNUAL_DELTA
PAYLOAD_SHA256 = accepted.prior.PAYLOAD_SHA256


def write_json(path: Path, value: Any) -> None:
    accepted.raw.base._write_json(Path(path), value)


def focused_implementation_gate() -> dict[str, Any]:
    args = trace_run._fixture()
    oracle_result = oracle.solve_matlab_faithful_hjb(*args)
    off_observations: list[tuple[int, dict[str, np.ndarray]]] = []
    on_observations: list[tuple[int, dict[str, np.ndarray]]] = []
    off_result, _ = solve_with_trace(
        *args,
        iteration_observer=lambda number, values: off_observations.append((number, values)),
    )
    on_result, _ = solve_with_trace(
        *args,
        iteration_observer=lambda number, values: on_observations.append((number, values)),
        transfer_candidate_abs_limit=D1_LIMIT,
    )
    off_parity = _result_equality(oracle_result, off_result)
    no_hit_parity = _result_equality(off_result, on_result)
    raw_equal = all(
        off_number == on_number
        and all(np.array_equal(off_values[name], on_values[name])
                for name in ("d_bb", "d_bf", "d_fb", "d_ff"))
        for (off_number, off_values), (on_number, on_values)
        in zip(off_observations, on_observations)
    ) and len(off_observations) == len(on_observations)
    no_hit = all(
        np.max(np.abs(values[name])) <= D1_LIMIT
        for _, values in off_observations
        for name in ("d_bb", "d_bf", "d_fb", "d_ff")
    )
    pure = oracle.select_matlab_faithful_transfer_candidates_from_raw(
        -100001.0,
        100000.0,
        -20.0,
        30.0,
        at_lower_a=False,
        at_upper_a=False,
        at_lower_b=False,
        tolerance=1.0e-12,
        transfer_candidate_abs_limit=D1_LIMIT,
    )
    semantic = {
        "raw_preserved": pure.raw == (-100001.0, 100000.0, -20.0, 30.0),
        "inclusive_boundary_admissible": pure.d1_admissible == (False, True, True, True),
        "ineligible_branch_excluded": pure.d_b == 100000.0,
        "other_admissible_nonzero_remains": pure.d_f == 10.0,
        "no_clipped_endpoint": -100000.0 not in pure.raw,
        "existing_zero_available": pure.zero_transfer_available,
    }
    status = (
        all(off_parity.values())
        and all(no_hit_parity.values())
        and raw_equal
        and no_hit
        and all(semantic.values())
    )
    return {
        "schema": "CH5_K1_TRANSFER_CONTROL_D1_IMPLEMENTATION_GATE_V1",
        "status": "PASS" if status else "FAIL",
        "task_id": TASK_ID,
        "d1_limit": D1_LIMIT,
        "d1_off_oracle_exact_parity": off_parity,
        "d1_no_hit_on_off_exact_parity": no_hit_parity,
        "raw_candidates_on_off_exact_identical": raw_equal,
        "no_hit_fixture_confirmed": no_hit,
        "pure_selector_semantics": semantic,
        "fixture_hjb_invocations": 3,
        "trajectory_state_advancements": 0,
        "candidate_clipping": False,
        "manufactured_endpoint_candidate": False,
    }


def prepare(evidence_parent: Path, accepted_payload: Path, test_cases: int, test_processes: int) -> None:
    parent = Path(evidence_parent)
    parent.mkdir(parents=True, exist_ok=False)
    payload_bytes = Path(accepted_payload).read_bytes()
    if accepted.prior.sha256(payload_bytes).hexdigest().upper() != PAYLOAD_SHA256:
        raise ValueError("accepted runtime payload SHA mismatch")
    payload = json.loads(payload_bytes)
    if len(payload["states"]) != 31:
        raise ValueError("accepted payload must contain 31 province states")
    gate = focused_implementation_gate()
    write_json(parent / "d1_implementation_gate.json", gate)
    if gate["status"] != "PASS":
        raise RuntimeError("D1 implementation gate failed")
    for path_id, (folder, beta) in PATHS.items():
        root = parent / folder
        root.mkdir()
        (root / "runtime_input_payload.json").write_bytes(payload_bytes)
        write_json(root / "phase_a_zero_science_receipt.json", {
            "schema": "CH5_K1_TRANSFER_CONTROL_D1_PHASE_A_V1",
            "status": "PASS",
            "task_id": TASK_ID,
            "path_id": path_id,
            "focused_test_cases": test_cases,
            "focused_test_processes": test_processes,
            "scientific_processes": 0,
            "hjb_calls": 0,
            "kfe_calls": 0,
            "initialization_observations": 0,
            "trajectory_calls": 0,
        })
        write_json(root / "runtime_input_receipt.json", {
            "schema": "CH5_K1_TRANSFER_CONTROL_D1_RUNTIME_INPUT_V1",
            "task_id": TASK_ID,
            "path_id": path_id,
            "runtime_payload_sha256": PAYLOAD_SHA256,
            "province_order": PROVINCE_ORDER,
            "beta_distance": beta,
            "beta_return": 0.0,
            "turn1_mode": accepted.BOOTSTRAP,
            "turns_2_5_payoff_mode": accepted.ANNUAL_RAW,
            "return_guard": list(G2_RETURN_GUARD),
            "wage_guard": list(WAGE_GUARD),
            "d1_active_turns": [2, 3, 4, 5] if path_id == "D1" else [],
            "d1_limit": D1_LIMIT,
            "candidate_clipping": False,
            "model_time_base": MODEL_TIME_BASE,
            "chi0": 0.1,
            "chi1_years": 2.0,
            "source_faithful_labor": True,
            "normalized_labor": False,
            "smoothing": False,
            "partial_adjustment": False,
            "c1_rule": "GovInv=max(Ktarget-Kprivate,0)",
        })
        write_json(root / "bounded_invocation_receipt.json", {
            "schema": "CH5_K1_TRANSFER_CONTROL_D1_BOUNDED_INVOCATION_V1",
            "trajectory_invocations_maximum": 1,
            "outer_turns_maximum": 5,
            "hjb_calls_maximum": 155,
            "kfe_calls_maximum": 155,
            "scientific_retries": 0,
            "engineering_retries_maximum": 1,
            "matlab_calls": 0,
            "standalone_kfe_experiments": 0,
            "k1b_runs": 0,
            "k2_runs": 0,
            "ge_calls": 0,
            "annual_downstream_calls": 0,
            "irf_calls": 0,
            "results_calls": 0,
        })
    write_json(parent / "prepare_receipt.json", {
        "schema": "CH5_K1_TRANSFER_CONTROL_D1_PREPARE_V1",
        "status": "PASS",
        "task_id": TASK_ID,
        "path_roots": {key: value[0] for key, value in PATHS.items()},
        "payloads_byte_identical": True,
        "runtime_payload_sha256": PAYLOAD_SHA256,
        "implementation_gate": gate,
        "scientific_calls": 0,
    })
    write_json(parent / "protected_source_identity_receipt.json", accepted.raw.base.protected_science_identity())


def preflight(evidence_parent: Path) -> None:
    parent = Path(evidence_parent)
    roots = [parent / PATHS[key][0] for key in ("C", "D1")]
    if roots[0].joinpath("runtime_input_payload.json").read_bytes() != roots[1].joinpath("runtime_input_payload.json").read_bytes():
        raise ValueError("control/D1 starting payloads are not byte-identical")
    if any(root.joinpath("science_started.json").exists() for root in roots):
        raise ValueError("science already started")
    implementation = json.loads((parent / "d1_implementation_gate.json").read_text(encoding="utf-8"))
    if implementation.get("status") != "PASS":
        raise RuntimeError("D1 implementation gate is not PASS")
    payload = json.loads(roots[0].joinpath("runtime_input_payload.json").read_text(encoding="utf-8"))
    states = payload["states"]
    if len(states) != 31 or any(float(state["rb"]) != 0.02 or float(state["rb_gap"]) != 0.07 for state in states):
        raise ValueError("annual liquid-return contract mismatch")
    if any(float(state["wjtmin"]) != WAGE_GUARD[0] or float(state["wjtmax"]) != WAGE_GUARD[1] for state in states):
        raise ValueError("wage guard changed")
    if accepted.prior._sha(accepted.prior.LEGACY) != accepted.prior.LEGACY_SHA256:
        raise ValueError("legacy allocator changed")
    accepted.raw.base.protected_science_identity()
    distance = load_accepted_distance_score(accepted.DISTANCE)
    config = K1ARuntimeConfig(PROVINCE_ORDER, distance, 2.0)
    probe = CapitalAllocationInputs(
        np.linspace(1, 2, 31),
        np.linspace(10, 20, 31),
        np.linspace(0.1, 0.3, 31),
        np.linspace(0.02, 0.09, 31),
    )
    payoff = np.linspace(0.1, 1.0, 31)
    used = allocate_k1a_capital(probe, config)
    rebuilt = allocate_k1a_capital(accepted.raw._inputs_with_payoff(probe, payoff), config)
    if not np.array_equal(used.network.portfolio_shares_destination_origin,
                          rebuilt.network.portfolio_shares_destination_origin):
        raise RuntimeError("payoff source changed S")
    if not np.array_equal(used.kt_supply, rebuilt.kt_supply):
        raise RuntimeError("payoff source changed quantities")
    if not np.array_equal(rebuilt.household_illiquid_return_rah,
                          payoff @ rebuilt.network.portfolio_shares_destination_origin):
        raise RuntimeError("annual raw same-S payoff identity failed")
    gate = {
        "schema": "CH5_K1_TRANSFER_CONTROL_D1_PRE_RUN_GATE_V1",
        "status": "PASS",
        "task_id": TASK_ID,
        "live_baseline": accepted.raw.base._git_text("rev-parse", "HEAD"),
        "payloads_byte_identical": True,
        "turn1_common_bootstrap_identical": True,
        "turn1_d1_off_both_paths": True,
        "d1_treatment_turns": [2, 3, 4, 5],
        "control_d1_off_all_turns": True,
        "implementation_gate": implementation,
        "same_S_static_identity": True,
        "quantity_bit_identical_under_payoff_switch": True,
        "model_time_base": MODEL_TIME_BASE,
        "rho_per_year": 0.05,
        "rb_per_year": 0.02,
        "borrowing_gap_per_year": 0.07,
        "firm_hjb_delta_per_year": ANNUAL_DELTA,
        "q_z_off_diagonal_per_year": 1.0 / 3.0,
        "chi0": 0.1,
        "chi1_years": 2.0,
        "return_guard_both_paths": list(G2_RETURN_GUARD),
        "wage_guard_both_paths": list(WAGE_GUARD),
        "beta_distance_both": 2.0,
        "beta_return_both": 0.0,
        "source_faithful_labor": True,
        "normalized_labor": False,
        "smoothing": False,
        "partial_adjustment": False,
        "c1_formula_unchanged": True,
        "k1b_disabled": True,
        "k2_disabled": True,
        "grid_tolerance_solver_unchanged": True,
        "science_calls_before_gate": 0,
    }
    write_json(parent / "pre_run_gate.json", gate)
    for root in roots:
        shutil.copyfile(parent / "pre_run_gate.json", root / "pre_run_gate.json")


def execute(evidence_parent: Path, path_id: str) -> int:
    parent = Path(evidence_parent)
    path_id = path_id.upper()
    if path_id not in PATHS:
        raise ValueError("path_id must be C or D1")
    gate = json.loads((parent / "pre_run_gate.json").read_text(encoding="utf-8"))
    if gate.get("status") != "PASS" or gate.get("science_calls_before_gate") != 0:
        raise RuntimeError("pre-run gate missing or failed")
    root = parent / PATHS[path_id][0]
    census_root = root / "d1_cell_receipts"
    if census_root.exists() and any(census_root.iterdir()):
        raise FileExistsError("D1 cell receipts already contain scientific evidence")
    census_root.mkdir(parents=True, exist_ok=True)
    active = {"turn": 0, "province_index": 0}
    call_index = 0
    receipts: list[dict[str, Any]] = []
    original_solver = oracle.solve_matlab_faithful_hjb
    original_writer = accepted.raw.g1.write_json
    original_paths = accepted.PATHS

    def tracking_writer(path: Path, value: Any) -> None:
        if path.name == "entering_state.json" and isinstance(value, dict):
            active["turn"] = int(value["turn"])
            active["province_index"] = 0
        elif path.name in {"science_started.json", "call_ledger.json", "terminal_result.json"} and isinstance(value, dict):
            value["d1_task_id"] = TASK_ID
            value["d1_path_id"] = path_id
            value["d1_active_turns"] = [2, 3, 4, 5] if path_id == "D1" else []
            value["candidate_clipping"] = False
        original_writer(path, value)

    def solve(
        grid: Any,
        params: Any,
        inputs: Any,
        initial_value: np.ndarray,
        baseline_labor: np.ndarray,
        transfer_income: float,
        borrowing_rate_gap: float,
        numerics: Any,
    ) -> Any:
        nonlocal call_index
        turn = int(active["turn"])
        province_index = int(active["province_index"])
        if not 1 <= turn <= 5 or not 0 <= province_index < 31:
            raise RuntimeError("D1 runtime call ordering is invalid")
        province = PROVINCE_ORDER[province_index]
        d1_active = path_id == "D1" and turn >= 2
        observations: list[tuple[int, dict[str, np.ndarray]]] = []
        result, trace = solve_with_trace(
            grid,
            params,
            inputs,
            initial_value,
            baseline_labor,
            transfer_income,
            borrowing_rate_gap,
            numerics,
            checkpoint_cells=trace_run.checkpoint_cells(province, turn),
            transfer_candidate_abs_limit=D1_LIMIT if d1_active else None,
            policy_comparison_observer=lambda number, values: observations.append((number, values)),
        )
        trace.update({
            "task_id": TASK_ID,
            "path_id": path_id,
            "turn": turn,
            "province": province,
            "province_index": province_index,
            "d1_active": d1_active,
            "d1_limit": D1_LIMIT,
            "comparison_classification": (
                "COMMON_BOOTSTRAP_D1_OFF"
                if turn == 1
                else "COMMON_ENTERING_STATE_D1_IMMEDIATE_RESPONSE"
                if turn == 2
                else "PATH_HISTORY_PROPAGATION__NOT_SAME_STATE_CAUSAL"
            ),
            "nonfinite_count": trace_run._trace_nonfinite_count(trace),
        })
        if trace["nonfinite_count"]:
            raise FloatingPointError("D1 HJB trace contains NaN/Inf")
        trace_path = root / f"turn_{turn:02d}" / "d1_instrumentation" / f"p{province_index:02d}_{province}_hjb_trace.json"
        write_json(trace_path, trace)
        relative = Path(path_id) / f"turn_{turn:02d}" / f"p{province_index:02d}_{province}_hjb_call_{call_index + 1:04d}.npz"
        receipt = write_d1_call_chunk(
            census_root / relative,
            observations,
            grid=grid,
            numerics=numerics,
            metadata={
                "task_id": TASK_ID,
                "path_id": path_id,
                "turn": turn,
                "province": province,
                "province_index": province_index,
                "hjb_call_index_one_based": call_index + 1,
                "d1_active": d1_active,
                "hjb_input_r_a": float(inputs.r_a),
                "hjb_input_wage": float(inputs.wages[0]),
                "comparison_classification": trace["comparison_classification"],
            },
            d1_active=d1_active,
            final_converged=result.converged,
            final_convergence_statistic=result.convergence_statistic,
        )
        receipt["relative_path"] = relative.as_posix()
        receipts.append(receipt)
        call_index += 1
        active["province_index"] = province_index + 1
        return result

    try:
        accepted.PATHS = {"G2": PATHS[path_id]}
        oracle.solve_matlab_faithful_hjb = solve
        accepted.raw.g1.write_json = tracking_writer
        code = accepted.execute(parent, "G2")
    finally:
        accepted.PATHS = original_paths
        oracle.solve_matlab_faithful_hjb = original_solver
        accepted.raw.g1.write_json = original_writer
    if call_index != 155 or len(receipts) != 155:
        raise RuntimeError(f"expected 155 D1 HJB receipts, observed {call_index}")
    manifest = {
        "schema": "CH5_K1_TRANSFER_CONTROL_D1_PATH_MANIFEST_V1",
        "task_id": TASK_ID,
        "path_id": path_id,
        "hjb_calls": call_index,
        "completed_turns": 5,
        "scientific_retries": 0,
        "engineering_retries": 0,
        "raw_candidate_count": sum(item["raw_candidate_count"] for item in receipts),
        "d1_inadmissible_count": sum(item["d1_inadmissible_count"] for item in receipts),
        "winner_changed_count": sum(item["winner_changed_count"] for item in receipts),
        "fallback_to_existing_zero_count": sum(item["fallback_to_existing_zero_count"] for item in receipts),
        "switch_to_other_admissible_nonzero_count": sum(item["switch_to_other_admissible_nonzero_count"] for item in receipts),
        "chunks": receipts,
    }
    write_json(census_root / "path_manifest.json", manifest)
    write_json(root / "d1_runtime_completion_receipt.json", manifest | {"chunks": len(receipts), "exit_code": code})
    return code


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("evidence_parent", type=Path)
    prep.add_argument("accepted_payload", type=Path)
    prep.add_argument("--test-cases", type=int, required=True)
    prep.add_argument("--test-processes", type=int, required=True)
    gate = sub.add_parser("preflight")
    gate.add_argument("evidence_parent", type=Path)
    launch = sub.add_parser("run")
    launch.add_argument("evidence_parent", type=Path)
    launch.add_argument("path_id", choices=("C", "D1"))
    args = parser.parse_args(argv)
    if args.command == "prepare":
        prepare(args.evidence_parent, args.accepted_payload, args.test_cases, args.test_processes)
        return 0
    if args.command == "preflight":
        preflight(args.evidence_parent)
        return 0
    return execute(args.evidence_parent, args.path_id)


if __name__ == "__main__":
    raise SystemExit(main())
