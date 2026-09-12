"""Bounded annual G1/G2 runtime with observation-only HJB instrumentation."""

from __future__ import annotations

import argparse
import json
from hashlib import sha256
from pathlib import Path
from typing import Any

import numpy as np

from exports import matlab_faithful_two_asset_ha as oracle
from validators.multi_province.corrected_2018_single_turn.run import source_initial_arrays
from validators.multi_province.k1_annual_hjb_g1_vs_g2 import run as base
from .instrumented_hjb import array_hash, solve_with_trace


TASK_ID = "CH5_MP4C_K1_G1_VS_G2_HA_HJB_INSTRUMENTED_BOUNDED_DIAGNOSTIC"
PATHS = base.PATHS
PRIORITY = {
    ("湖北", 2): ((1, 18, 0),),
    ("四川", 4): ((19, 16, 1),),
    ("云南", 4): ((10, 9, 0),),
}


def _json_safe(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    if isinstance(value, (np.floating, float)) and not np.isfinite(value):
        return "NONFINITE_NAN" if np.isnan(value) else (
            "NONFINITE_POSITIVE_INFINITY" if value > 0 else "NONFINITE_NEGATIVE_INFINITY")
    if isinstance(value, np.generic):
        return value.item()
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(_json_safe(value), stream, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        stream.write("\n")


def checkpoint_cells(province: str, turn: int) -> tuple[tuple[int, int, int], ...]:
    return PRIORITY.get((province, int(turn)), ())


def _fixture() -> tuple[Any, ...]:
    grid = oracle.MatlabFaithfulHJBGrid(
        np.array([-2.0, 5.0]), np.array([0.0, 10.0]), np.array([0.8, 1.3]),
        np.array([[-1 / 3, 1 / 3], [1 / 3, -1 / 3]]),
    )
    params = oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
    state = {"rah": 0.2, "rb": 0.02, "rb_gap": 0.07, "Tt": 0.1, "tau": 0.05, "w": 1.1}
    initial, labor = source_initial_arrays(state, grid, params, lambda: None)
    inputs = oracle.HouseholdInputs(0.2, 0.02, 0.05, np.array([1.1]), np.zeros(1), np.ones(1))
    numerics = oracle.MatlabFaithfulHJBNumerics(1000.0, 1e-7, 2, 1e-12)
    return grid, params, inputs, initial, labor, state["Tt"], state["rb_gap"], numerics


def focused_parity_gate() -> dict[str, Any]:
    args = _fixture()
    expected = oracle.solve_matlab_faithful_hjb(*args)
    actual, trace = solve_with_trace(*args, checkpoint_cells=((1, 1, 0),))
    array_fields = (
        "value", "initial_value", "consumption", "labor", "transfer", "adjustment_cost",
        "effective_illiquid_return", "mu_a", "mu_b", "utility", "liquid_label", "transfer_label",
    )
    equality = {name: bool(np.array_equal(getattr(expected, name), getattr(actual, name)))
                for name in array_fields}
    equality.update({
        "operator": bool(np.array_equal(expected.operator.full.toarray(), actual.operator.full.toarray())),
        "post_convergence_operator": bool(np.array_equal(
            expected.post_convergence_operator.full.toarray(), actual.post_convergence_operator.full.toarray())),
        "iterations": expected.iterations == actual.iterations,
        "converged": expected.converged == actual.converged,
        "convergence_statistic": expected.convergence_statistic == actual.convergence_statistic,
    })
    passed = all(equality.values())
    return {
        "schema": "CH5_K1_G1_VS_G2_HA_HJB_INSTRUMENTATION_PARITY_V1",
        "status": "PASS" if passed else "FAIL",
        "task_id": TASK_ID,
        "scientific_outputs_exactly_equal": passed,
        "field_equality": equality,
        "fixture_initial_value_sha256": array_hash(args[3]),
        "instrumented_trace_iterations": len(trace["iterations"]),
        "fixture_hjb_evaluations": 2,
        "fixture_role": "FOCUSED_PRE_RUN_PARITY__NOT_A_TRAJECTORY_OR_PROVINCE_SCIENTIFIC_CALL",
        "budgeted_trajectory_calls": 0,
        "budgeted_province_hjb_calls": 0,
    }


def prepare(evidence_parent: Path, accepted_payload: Path, test_cases: int, test_processes: int) -> None:
    base.prepare(evidence_parent, accepted_payload, test_cases, test_processes)
    parent = Path(evidence_parent)
    gate = focused_parity_gate()
    write_json(parent / "instrumentation_parity_gate.json", gate)
    if gate["status"] != "PASS":
        raise RuntimeError("instrumentation parity gate failed")
    for path_id, (name, _) in PATHS.items():
        write_json(parent / name / "instrumentation_contract.json", {
            "schema": "CH5_K1_G1_VS_G2_HA_HJB_INSTRUMENTATION_CONTRACT_V1",
            "task_id": TASK_ID, "path_id": path_id, "observation_only": True,
            "return_guard": list(base.RETURN_GUARDS[path_id]), "wage_guard": list(base.WAGE_GUARD),
            "scientific_retry_after_state_advancement": 0,
            "engineering_retry_before_state_update_maximum": 1,
        })


def preflight(evidence_parent: Path) -> None:
    parent = Path(evidence_parent)
    parity = json.loads((parent / "instrumentation_parity_gate.json").read_text(encoding="utf-8"))
    if parity.get("status") != "PASS" or not parity.get("scientific_outputs_exactly_equal"):
        raise RuntimeError("instrumentation parity not proven")
    base.preflight(parent)
    base_gate = json.loads((parent / "pre_run_gate.json").read_text(encoding="utf-8"))
    required = (
        base_gate.get("payloads_byte_identical_except_path_guard_metadata"),
        base_gate.get("turn1_common_bootstrap_identical"), base_gate.get("same_S_static_identity"),
        base_gate.get("quantity_bit_identical_under_payoff_switch"), base_gate.get("wage_guard_unchanged"),
        base_gate.get("k1b_disabled"), base_gate.get("k2_disabled"),
        base_gate.get("source_faithful_labor"), base_gate.get("grid_tolerance_solver_unchanged"),
    )
    if base_gate.get("status") != "PASS" or not all(required):
        raise RuntimeError("inherited frozen-science gate failed")
    write_json(parent / "instrumented_pre_run_gate.json", {
        "schema": "CH5_K1_G1_VS_G2_HA_HJB_INSTRUMENTED_PRE_RUN_GATE_V1",
        "status": "PASS", "task_id": TASK_ID, "live_baseline": base_gate["live_baseline"],
        "instrumentation_parity": parity, "inherited_frozen_science_gate": base_gate,
        "science_calls_before_gate": 0,
    })


def _trace_nonfinite_count(trace: dict[str, Any]) -> int:
    total = 0
    for item in trace["iterations"]:
        total += int(item["value_new"]["nonfinite_count"])
        for group in ("derivatives", "candidate_objects", "selected_objects"):
            total += sum(int(value["nonfinite_count"]) for value in item[group].values())
    return total


def execute(evidence_parent: Path, path_id: str) -> int:
    parent, path_id = Path(evidence_parent), path_id.upper()
    if path_id not in PATHS:
        raise ValueError("path_id must be G1 or G2")
    gate = json.loads((parent / "instrumented_pre_run_gate.json").read_text(encoding="utf-8"))
    if gate.get("status") != "PASS":
        raise RuntimeError("pre-run gate is not PASS")
    root = parent / PATHS[path_id][0]
    original = oracle.solve_matlab_faithful_hjb
    call_index = 0

    def instrumented(grid, params, inputs, initial_value, baseline_labor,
                     transfer_income, borrowing_rate_gap, numerics):
        nonlocal call_index
        turn, province_index = divmod(call_index, 31)
        turn += 1
        province = base.PROVINCE_ORDER[province_index]
        result, trace = solve_with_trace(
            grid, params, inputs, initial_value, baseline_labor, transfer_income,
            borrowing_rate_gap, numerics,
            checkpoint_cells=checkpoint_cells(province, turn),
        )
        trace.update({
            "path_id": path_id, "turn": turn, "province": province,
            "province_index": province_index,
            "comparison_classification": "COMMON_ENTERING_STATE_IMMEDIATE_RESPONSE" if turn == 2 else
                "COMMON_BOOTSTRAP" if turn == 1 else "PATH_HISTORY_PROPAGATION__NOT_SAME_STATE_CAUSAL",
            "nonfinite_count": _trace_nonfinite_count(trace),
        })
        write_json(root / f"turn_{turn:02d}" / "instrumentation" /
                   f"p{province_index:02d}_{province}_hjb_trace.json", trace)
        if trace["nonfinite_count"]:
            raise FloatingPointError("instrumented HJB trace contains NaN/Inf")
        call_index += 1
        return result

    try:
        oracle.solve_matlab_faithful_hjb = instrumented
        result = base.execute(parent, path_id)
        if call_index != 155:
            raise RuntimeError(f"expected 155 instrumented HJB calls, observed {call_index}")
        write_json(root / "instrumentation_completion_receipt.json", {
            "schema": "CH5_K1_G1_VS_G2_HA_HJB_INSTRUMENTATION_COMPLETION_V1",
            "path_id": path_id, "instrumented_hjb_calls": call_index,
            "completed_turns": 5, "scientific_retries": 0, "nonfinite_count": 0,
        })
        return result
    finally:
        oracle.solve_matlab_faithful_hjb = original


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("evidence_parent", type=Path); prep.add_argument("accepted_payload", type=Path)
    prep.add_argument("--test-cases", type=int, required=True); prep.add_argument("--test-processes", type=int, required=True)
    gate = sub.add_parser("preflight"); gate.add_argument("evidence_parent", type=Path)
    run = sub.add_parser("run"); run.add_argument("evidence_parent", type=Path); run.add_argument("path_id", choices=("G1", "G2"))
    args = parser.parse_args(argv)
    if args.command == "prepare":
        prepare(args.evidence_parent, args.accepted_payload, args.test_cases, args.test_processes); return 0
    if args.command == "preflight":
        preflight(args.evidence_parent); return 0
    return execute(args.evidence_parent, args.path_id)


if __name__ == "__main__":
    raise SystemExit(main())
