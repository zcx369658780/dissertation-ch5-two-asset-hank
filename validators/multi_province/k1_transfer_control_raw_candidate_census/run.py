"""Bounded G1/G2 runtime with lossless observation-only raw-candidate census."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np

from exports import matlab_faithful_two_asset_ha as oracle
from validators.multi_province.k1_g1_vs_g2_ha_hjb_instrumented import run as accepted
from validators.multi_province.k1_g1_vs_g2_ha_hjb_instrumented.instrumented_hjb import (
    array_hash, solve_with_trace,
)

from .census import file_sha256, write_call_chunk


TASK_ID = "CH5_MP4C_K1_TRANSFER_CONTROL_RAW_CANDIDATE_CENSUS_INSTRUMENTED_BOUNDED_DIAGNOSTIC"
PATHS = accepted.PATHS


def _result_equality(left: Any, right: Any) -> dict[str, bool]:
    fields = (
        "value", "initial_value", "consumption", "labor", "transfer", "adjustment_cost",
        "effective_illiquid_return", "mu_a", "mu_b", "utility", "liquid_label", "transfer_label",
    )
    result = {name: bool(np.array_equal(getattr(left, name), getattr(right, name))) for name in fields}
    result.update({
        "operator": bool(np.array_equal(left.operator.full.toarray(), right.operator.full.toarray())),
        "post_convergence_operator": bool(np.array_equal(
            left.post_convergence_operator.full.toarray(), right.post_convergence_operator.full.toarray())),
        "iterations": left.iterations == right.iterations,
        "converged": left.converged == right.converged,
        "convergence_statistic": left.convergence_statistic == right.convergence_statistic,
    })
    return result


def focused_parity_gate(parent: Path) -> dict[str, Any]:
    args = accepted._fixture()
    expected = oracle.solve_matlab_faithful_hjb(*args)
    observations: list[tuple[int, dict[str, np.ndarray]]] = []

    def observe(number: int, values: dict[str, np.ndarray]) -> None:
        observations.append((number, values))

    actual, trace = solve_with_trace(
        *args, checkpoint_cells=((1, 1, 0),), iteration_observer=observe,
    )
    equality = _result_equality(expected, actual)
    gate = {
        "schema": "CH5_K1_TRANSFER_RAW_CANDIDATE_CENSUS_PARITY_GATE_V1",
        "status": "PASS" if all(equality.values()) else "FAIL",
        "task_id": TASK_ID,
        "baseline_oracle_vs_census_instrumentation_exact_equality": equality,
        "scientific_outputs_exactly_equal": all(equality.values()),
        "fixture_hjb_invocations": 2,
        "trajectory_state_advancements": 0,
        "observed_iterations": len(observations),
        "trace_iterations": len(trace["iterations"]),
        "observation_arrays_are_read_only": all(
            not array.flags.writeable for _, values in observations for array in values.values()
        ),
        "census_values_entered_scientific_calculation": False,
    }
    accepted.write_json(Path(parent) / "raw_candidate_census_parity_gate.json", gate)
    if gate["status"] != "PASS" or len(observations) != len(trace["iterations"]):
        raise RuntimeError("raw-candidate census instrumentation parity gate failed")
    return gate


def prepare(evidence_parent: Path, accepted_payload: Path, test_cases: int, test_processes: int) -> None:
    parent = Path(evidence_parent)
    accepted.base.prepare(parent, accepted_payload, test_cases, test_processes)
    parity = focused_parity_gate(parent)
    accepted.write_json(parent / "raw_candidate_census_prepare_receipt.json", {
        "schema": "CH5_K1_TRANSFER_RAW_CANDIDATE_CENSUS_PREPARE_V1",
        "status": "PASS", "task_id": TASK_ID,
        "instrumentation_parity": parity,
        "scientific_trajectory_calls": 0,
        "matlab_calls": 0,
    })
    for path_id, (name, _) in PATHS.items():
        accepted.write_json(parent / name / "raw_candidate_census_contract.json", {
            "schema": "CH5_K1_TRANSFER_RAW_CANDIDATE_CENSUS_CONTRACT_V1",
            "task_id": TASK_ID, "path_id": path_id,
            "observation_only": True, "raw_candidate_branches": ["d_bb", "d_bf", "d_fb", "d_ff"],
            "transfer_safeguard_active": False, "candidate_rejection": False,
            "candidate_clipping": False, "candidate_cap": False, "fallback_rule": False,
            "full_census_location": "EXTERNAL_SEALED_EVIDENCE_ONLY",
            "scientific_retries_after_state_advancement": 0,
            "pre_state_update_engineering_retries_maximum": 1,
        })


def preflight(evidence_parent: Path) -> None:
    parent = Path(evidence_parent)
    parity = json.loads((parent / "raw_candidate_census_parity_gate.json").read_text(encoding="utf-8"))
    if parity.get("status") != "PASS" or not parity.get("scientific_outputs_exactly_equal"):
        raise RuntimeError("census instrumentation parity not proven")
    accepted.base.preflight(parent)
    base_gate = json.loads((parent / "pre_run_gate.json").read_text(encoding="utf-8"))
    required = (
        base_gate.get("payloads_byte_identical_except_path_guard_metadata"),
        base_gate.get("turn1_common_bootstrap_identical"), base_gate.get("same_S_static_identity"),
        base_gate.get("quantity_bit_identical_under_payoff_switch"), base_gate.get("wage_guard_unchanged"),
        base_gate.get("k1b_disabled"), base_gate.get("k2_disabled"),
        base_gate.get("source_faithful_labor"), base_gate.get("grid_tolerance_solver_unchanged"),
    )
    if base_gate.get("status") != "PASS" or not all(required):
        raise RuntimeError("frozen-science pre-run gate failed")
    accepted.write_json(parent / "raw_candidate_census_pre_run_gate.json", {
        "schema": "CH5_K1_TRANSFER_RAW_CANDIDATE_CENSUS_PRE_RUN_GATE_V1",
        "status": "PASS", "task_id": TASK_ID, "live_baseline": base_gate["live_baseline"],
        "instrumentation_parity": parity, "inherited_frozen_science_gate": base_gate,
        "fixture_hjb_invocations_before_gate": parity["fixture_hjb_invocations"],
        "scientific_trajectory_calls_before_gate": 0,
        "transfer_safeguard_active": False,
    })


def _position(value: float, lower: float, upper: float, turn: int) -> str:
    if turn == 1:
        return "NOT_APPLIED_BOOTSTRAP"
    if value == lower:
        return "AT_LOWER_BOUND"
    if value == upper:
        return "AT_UPPER_BOUND"
    return "UNSATURATED"


def execute(evidence_parent: Path, path_id: str) -> int:
    parent, path_id = Path(evidence_parent), path_id.upper()
    if path_id not in PATHS:
        raise ValueError("path_id must be G1 or G2")
    gate = json.loads((parent / "raw_candidate_census_pre_run_gate.json").read_text(encoding="utf-8"))
    if gate.get("status") != "PASS":
        raise RuntimeError("pre-run gate is not PASS")
    root = parent / PATHS[path_id][0]
    census_root = root / "raw_candidate_census"
    census_root.mkdir(parents=True, exist_ok=False)
    original = oracle.solve_matlab_faithful_hjb
    call_index = 0
    receipts: list[dict[str, Any]] = []

    def instrumented(grid, params, inputs, initial_value, baseline_labor,
                     transfer_income, borrowing_rate_gap, numerics):
        nonlocal call_index
        turn_zero, province_index = divmod(call_index, 31)
        turn = turn_zero + 1
        province = accepted.base.PROVINCE_ORDER[province_index]
        observations: list[tuple[int, dict[str, np.ndarray]]] = []

        def observe(number: int, values: dict[str, np.ndarray]) -> None:
            observations.append((number, values))

        result, trace = solve_with_trace(
            grid, params, inputs, initial_value, baseline_labor, transfer_income,
            borrowing_rate_gap, numerics,
            checkpoint_cells=accepted.checkpoint_cells(province, turn),
            iteration_observer=observe,
        )
        trace.update({
            "path_id": path_id, "turn": turn, "province": province,
            "province_index": province_index,
            "comparison_classification": "COMMON_ENTERING_STATE_IMMEDIATE_RESPONSE" if turn == 2 else
                "COMMON_BOOTSTRAP" if turn == 1 else "PATH_HISTORY_PROPAGATION__NOT_SAME_STATE_CAUSAL",
            "nonfinite_count": accepted._trace_nonfinite_count(trace),
        })
        if trace["nonfinite_count"]:
            raise FloatingPointError("instrumented HJB trace contains NaN/Inf")
        accepted.write_json(root / f"turn_{turn:02d}" / "instrumentation" /
                            f"p{province_index:02d}_{province}_hjb_trace.json", trace)
        lower, upper = accepted.base.RETURN_GUARDS[path_id]
        wage_lower, wage_upper = accepted.base.WAGE_GUARD
        metadata = {
            "task_id": TASK_ID, "path_id": path_id, "turn": turn,
            "province": province, "province_index": province_index,
            "hjb_call_index_one_based": call_index + 1,
            "hjb_input_r_a": float(inputs.r_a),
            "hjb_return_guard_position": _position(float(inputs.r_a), lower, upper, turn),
            "return_guard_bounds": [lower, upper],
            "hjb_input_wage": float(inputs.wages[0]),
            "hjb_wage_guard_position": _position(float(inputs.wages[0]), wage_lower, wage_upper, 2),
            "wage_guard_bounds": [wage_lower, wage_upper],
            "grid_sha256": trace["grid_sha256"],
            "comparison_classification": trace["comparison_classification"],
            "transfer_safeguard_active": False,
        }
        relative = Path(path_id) / f"turn_{turn:02d}" / f"p{province_index:02d}_{province}_hjb_call_{call_index + 1:04d}.npz"
        receipt = write_call_chunk(
            census_root / relative, observations, grid=grid, numerics=numerics,
            metadata=metadata, final_converged=result.converged,
            final_convergence_statistic=result.convergence_statistic,
        )
        receipt["relative_path"] = relative.as_posix()
        receipts.append(receipt)
        call_index += 1
        return result

    try:
        oracle.solve_matlab_faithful_hjb = instrumented
        result = accepted.base.execute(parent, path_id)
        if call_index != 155:
            raise RuntimeError(f"expected 155 census HJB calls, observed {call_index}")
        manifest = {
            "schema": "CH5_K1_TRANSFER_RAW_CANDIDATE_CENSUS_PATH_MANIFEST_V1",
            "task_id": TASK_ID, "path_id": path_id,
            "chunk_count": len(receipts),
            "hjb_calls": call_index,
            "raw_candidate_count": sum(item["raw_candidate_count"] for item in receipts),
            "raw_finite_count": sum(item["raw_finite_count"] for item in receipts),
            "raw_nan_count": sum(item["raw_nan_count"] for item in receipts),
            "raw_positive_infinity_count": sum(item["raw_positive_infinity_count"] for item in receipts),
            "raw_negative_infinity_count": sum(item["raw_negative_infinity_count"] for item in receipts),
            "selected_transfer_reconstruction_equal_count": sum(
                item["selected_transfer_reconstruction_equal_count"] for item in receipts),
            "selected_transfer_cell_count": sum(item["selected_transfer_cell_count"] for item in receipts),
            "chunks": receipts,
        }
        accepted.write_json(census_root / "path_manifest.json", manifest)
        accepted.write_json(root / "raw_candidate_census_completion_receipt.json", {
            "schema": "CH5_K1_TRANSFER_RAW_CANDIDATE_CENSUS_COMPLETION_V1",
            "path_id": path_id, "instrumented_hjb_calls": call_index,
            "completed_turns": 5, "scientific_retries": 0, "engineering_retries": 0,
            "raw_candidate_count": manifest["raw_candidate_count"],
            "raw_nonfinite_count": manifest["raw_candidate_count"] - manifest["raw_finite_count"],
            "manifest_sha256": file_sha256(census_root / "path_manifest.json"),
        })
        return result
    finally:
        oracle.solve_matlab_faithful_hjb = original


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
    launch.add_argument("path_id", choices=("G1", "G2"))
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
