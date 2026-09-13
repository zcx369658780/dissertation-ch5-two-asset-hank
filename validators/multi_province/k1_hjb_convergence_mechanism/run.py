"""Exact-input turn-1/turn-2 replay and convergence-mechanism analysis."""

from __future__ import annotations

import argparse
import csv
import json
import os
import platform
import sys
import time
from dataclasses import asdict
from hashlib import sha256
from pathlib import Path
from typing import Any

import numpy as np
from scipy import sparse

REPO = Path(__file__).resolve().parents[3]
for item in (REPO / "src", REPO):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))

from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER  # noqa: E402
from exports import matlab_faithful_two_asset_ha as oracle  # noqa: E402
from validators.multi_province.corrected_2018_single_turn import run as single  # noqa: E402
from validators.multi_province.k1_annual_hjb_g1_vs_g2 import run as accepted  # noqa: E402
from validators.multi_province.k1_hjb_convergence_mechanism.instrumented_hjb import solve_with_observations  # noqa: E402

TASK_ID = "CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC"
ACCEPTED_MANIFEST_SHA256 = "C60C353FE1ABC24509F5753E808F837BA19C9856B98FAE9998AB59DAC9BCE6BE"
RETURN_GUARD = (-0.10, 0.35)
SCIENTIFIC_FIELDS = (
    "value", "initial_value", "consumption", "labor", "transfer", "adjustment_cost",
    "effective_illiquid_return", "mu_a", "mu_b", "utility", "liquid_label", "transfer_label",
)


def _sha_file(path: Path) -> str:
    return sha256(Path(path).read_bytes()).hexdigest().upper()


def _sha_array(value: Any) -> str:
    array = np.asarray(value)
    header = f"{array.dtype.str}|{array.shape}|C|".encode("ascii")
    return sha256(header + np.ascontiguousarray(array).tobytes()).hexdigest().upper()


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _objects() -> tuple[Any, Any, Any]:
    grid = oracle.MatlabFaithfulHJBGrid(np.linspace(-2, 5, 20), np.linspace(0, 10, 20),
        np.array([0.8, 1.3]), np.array([[-1 / 3, 1 / 3], [1 / 3, -1 / 3]]))
    params = oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
    numerics = oracle.MatlabFaithfulHJBNumerics(1000.0, 1e-7, 100, 1e-12)
    return grid, params, numerics


def _manifest_map(accepted_parent: Path) -> tuple[Path, dict[str, dict[str, Any]]]:
    manifest_path = accepted_parent / "sealed_manifest_sha256.json"
    if _sha_file(manifest_path) != ACCEPTED_MANIFEST_SHA256:
        raise ValueError("accepted sealed manifest SHA mismatch")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    return manifest_path, {str(item["path"]): item for item in manifest["entries"]}


def _verify_manifest_entry(accepted_parent: Path, mapping: dict[str, dict[str, Any]], relative: str) -> str:
    item = mapping.get(relative)
    if item is None:
        raise ValueError(f"accepted manifest entry missing: {relative}")
    actual = _sha_file(accepted_parent / relative)
    if actual != item["sha256"]:
        raise ValueError(f"accepted artifact SHA mismatch: {relative}")
    return actual


def _call_inputs(root: Path, turn: int, index: int, grid: Any, params: Any, numerics: Any) -> tuple[tuple[Any, ...], dict[str, Any]]:
    entering_path = root / f"turn_{turn:02d}" / "entering_state.json"
    entering = json.loads(entering_path.read_text(encoding="utf-8"))
    state = entering["states"][index]
    initial, labor = single.source_initial_arrays(state, grid, params)
    raw_ra = float(state["rah"])
    consumed_ra = raw_ra if turn == 1 else float(np.clip(raw_ra, *RETURN_GUARD))
    guard_state = "NOT_APPLIED_BOOTSTRAP" if turn == 1 else (
        "LOWER" if raw_ra < RETURN_GUARD[0] else "UPPER" if raw_ra > RETURN_GUARD[1] else "UNSATURATED")
    inputs = oracle.HouseholdInputs(consumed_ra, float(state["rb"]), float(state["tau"]),
        np.array([state["w"]]), np.array([0.0]), np.array([1.0]))
    trace_path = root / f"turn_{turn:02d}" / "d1_instrumentation" / f"p{index:02d}_{PROVINCE_ORDER[index]}_hjb_trace.json"
    hjb_path = root / f"turn_{turn:02d}" / "household" / f"p{index:02d}_{PROVINCE_ORDER[index]}" / "hjb_return.npz"
    args = (grid, params, inputs, initial, labor, float(state["Tt"]), float(state["rb_gap"]), numerics)
    identity = {
        "turn": turn, "province_index": index, "province": PROVINCE_ORDER[index],
        "entering_state_path": str(entering_path), "trace_path": str(trace_path), "accepted_hjb_path": str(hjb_path),
        "initial_value_sha256": _sha_array(initial), "baseline_labor_sha256": _sha_array(labor),
        "grid_sha256": {"b": _sha_array(grid.b), "a": _sha_array(grid.a), "z": _sha_array(grid.z),
                        "switch_matrix": _sha_array(grid.switch_matrix)},
        "params": asdict(params), "numerics": asdict(numerics),
        "raw_entering_r_a": raw_ra, "consumed_r_a": consumed_ra, "return_guard_state": guard_state,
        "wage": float(state["w"]), "guarded_wjt": float(state["wjt"]), "wage_guard_state": (
            "LOWER" if float(state["wjt"]) == 0.8 else "UPPER" if float(state["wjt"]) == 1.3 else "UNSATURATED"),
        "r_b": float(state["rb"]), "tau": float(state["tau"]),
        "transfer_income": float(state["Tt"]), "borrowing_rate_gap": float(state["rb_gap"]),
        "transfer_control_state": "D1_OFF", "source_faithful_labor": True,
    }
    return args, identity


def _accepted_npz_equal(result: Any, path: Path) -> tuple[bool, list[str]]:
    mismatches: list[str] = []
    with np.load(path, allow_pickle=False) as stored:
        for name in SCIENTIFIC_FIELDS:
            if not np.array_equal(np.asarray(getattr(result, name)), stored[name]):
                mismatches.append(name)
        for name in ("iterations", "converged", "convergence_statistic"):
            actual = getattr(result, name)
            expected = stored[name].item()
            if actual != expected:
                mismatches.append(name)
    return not mismatches, mismatches


def _accepted_final_operator_hash(trace_path: Path) -> str:
    trace = json.loads(Path(trace_path).read_text(encoding="utf-8"))
    return str(trace["iterations"][-1]["operator_sha256"])


def _result_equal(left: Any, right: Any) -> tuple[bool, list[str]]:
    mismatches = [name for name in SCIENTIFIC_FIELDS
                  if not np.array_equal(np.asarray(getattr(left, name)), np.asarray(getattr(right, name)))]
    for name in ("iterations", "converged", "convergence_statistic"):
        if getattr(left, name) != getattr(right, name): mismatches.append(name)
    for prefix, lop, rop in (("operator", left.operator.full, right.operator.full),
                             ("post_convergence_operator", left.post_convergence_operator.full, right.post_convergence_operator.full)):
        difference = (lop - rop).tocsr()
        if difference.nnz and np.any(difference.data != 0): mismatches.append(prefix)
    return not mismatches, mismatches


def preflight(accepted_parent: Path, output_root: Path) -> int:
    accepted_parent = Path(accepted_parent); output_root = Path(output_root)
    if output_root.exists(): raise FileExistsError("fresh no-overwrite evidence root already exists")
    output_root.mkdir(parents=True)
    manifest_path, mapping = _manifest_map(accepted_parent)
    root = accepted_parent / "annual_g2_control"
    grid, params, numerics = _objects()
    receipts: list[dict[str, Any]] = []
    relevant = ["annual_g2_control/runtime_input_payload.json", "annual_g2_control/runtime_input_receipt.json"]
    for turn in (1, 2):
        relevant.append(f"annual_g2_control/turn_{turn:02d}/entering_state.json")
        for index, province in enumerate(PROVINCE_ORDER):
            relevant.extend([
                f"annual_g2_control/turn_{turn:02d}/d1_instrumentation/p{index:02d}_{province}_hjb_trace.json",
                f"annual_g2_control/turn_{turn:02d}/household/p{index:02d}_{province}/hjb_return.npz",
            ])
    verified = {path: _verify_manifest_entry(accepted_parent, mapping, path) for path in relevant}
    for turn in (1, 2):
        for index in range(31):
            _, identity = _call_inputs(root, turn, index, grid, params, numerics)
            trace = json.loads(Path(identity["trace_path"]).read_text(encoding="utf-8"))
            with np.load(identity["accepted_hjb_path"], allow_pickle=False) as stored:
                checks = {
                    "trace_initial_value_sha256": trace["initial_value_sha256"] == identity["initial_value_sha256"],
                    "npz_initial_value_exact": np.array_equal(stored["initial_value"], _call_inputs(root, turn, index, grid, params, numerics)[0][3]),
                    "grid_sha256_exact": trace["grid_sha256"] == identity["grid_sha256"],
                    "params_exact": trace["params"] == identity["params"],
                    "numerics_exact": trace["numerics"] == identity["numerics"],
                    "consumed_r_a_exact": trace["inputs"]["r_a"] == identity["consumed_r_a"],
                    "wage_exact": trace["inputs"]["wages"] == [identity["wage"]],
                    "transfer_income_exact": trace["inputs"]["transfer_income"] == identity["transfer_income"],
                    "borrowing_rate_gap_exact": trace["inputs"]["borrowing_rate_gap"] == identity["borrowing_rate_gap"],
                    "d1_off": trace.get("d1_active") is False,
                }
                identity["accepted_iterations"] = int(stored["iterations"].item())
                identity["accepted_converged"] = bool(stored["converged"].item())
                identity["accepted_convergence_statistic"] = float(stored["convergence_statistic"].item())
            identity["checks"] = checks
            identity["status"] = "PROVEN_EXACT" if all(checks.values()) else "REPLAY_INPUT_IDENTITY_UNPROVEN"
            receipts.append(identity)
    proven = sum(item["status"] == "PROVEN_EXACT" for item in receipts)
    source_paths = [
        REPO / "exports/matlab_faithful_two_asset_ha.py",
        REPO / "validators/multi_province/corrected_2018_single_turn/run.py",
        REPO / "validators/multi_province/k1_annual_hjb_g1_vs_g2/run.py",
    ]
    _write_json(output_root / "identity_receipts.json", receipts)
    _write_json(output_root / "preflight.json", {
        "schema": "CH5_MP4C_K1_HJB_MECHANISM_PREFLIGHT_V1", "task_id": TASK_ID,
        "status": "PASS" if proven == 62 else "PARTIAL_REPLAY_IDENTITY",
        "accepted_manifest_path": str(manifest_path), "accepted_manifest_sha256": ACCEPTED_MANIFEST_SHA256,
        "verified_relevant_manifest_entries": verified, "exact_input_coverage": proven,
        "unproven_calls": 62 - proven, "science_calls_before_gate": 0,
        "engineering_retries_consumed": 1,
        "source_sha256": {str(path.relative_to(REPO)).replace("\\", "/"): _sha_file(path) for path in source_paths},
        "scientific_budget": {"parity_hjb_exactly": 2, "replay_hjb_maximum": 62, "total_hjb_maximum": 64,
                                "kfe": 0, "matlab": 0, "outer_trajectory_advancements": 0, "scientific_retries": 0},
    })
    return 0


def run(accepted_parent: Path, output_root: Path) -> int:
    accepted_parent = Path(accepted_parent); output_root = Path(output_root)
    preflight_path = output_root / "preflight.json"
    if not preflight_path.exists(): raise FileNotFoundError("preflight must complete before scientific calls")
    preflight_receipt = json.loads(preflight_path.read_text(encoding="utf-8"))
    identities = json.loads((output_root / "identity_receipts.json").read_text(encoding="utf-8"))
    proven = [item for item in identities if item["status"] == "PROVEN_EXACT"]
    if not proven: raise RuntimeError("no proven-exact replay inputs")
    if (output_root / "science_started.json").exists(): raise FileExistsError("scientific execution is no-overwrite and non-retryable")
    _write_json(output_root / "science_started.json", {
        "schema": "CH5_MP4C_K1_HJB_MECHANISM_SCIENCE_STARTED_V1", "task_id": TASK_ID,
        "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "process_id": os.getpid(),
        "python": sys.version, "platform": platform.platform(), "proven_exact_calls": len(proven),
        "scientific_retries": 0,
    })
    root = accepted_parent / "annual_g2_control"
    grid, params, numerics = _objects()
    ledger: list[dict[str, Any]] = []

    parity_identity = proven[0]
    parity_args, _ = _call_inputs(root, parity_identity["turn"], parity_identity["province_index"], grid, params, numerics)
    off = oracle.solve_matlab_faithful_hjb(*parity_args)
    ledger.append({"call": 1, "phase": "PARITY_OFF", "turn": parity_identity["turn"], "province": parity_identity["province"], "consumed": True})
    on, parity_trace = solve_with_observations(*parity_args)
    ledger.append({"call": 2, "phase": "PARITY_ON", "turn": parity_identity["turn"], "province": parity_identity["province"], "consumed": True})
    parity_ok, parity_mismatches = _result_equal(off, on)
    accepted_ok, accepted_mismatches = _accepted_npz_equal(off, Path(parity_identity["accepted_hjb_path"]))
    parity = {"status": "PASS" if parity_ok and accepted_ok else "FAIL", "off_on_exact": parity_ok,
              "off_on_mismatches": parity_mismatches, "off_accepted_exact": accepted_ok,
              "off_accepted_mismatches": accepted_mismatches, "call_identity": parity_identity,
              "off_iterations": off.iterations, "on_iterations": on.iterations,
              "off_converged": off.converged, "on_converged": on.converged,
              "diagnostic_iterations": len(parity_trace["iterations"])}
    _write_json(output_root / "instrumentation_parity.json", parity)
    if parity["status"] != "PASS":
        _write_json(output_root / "call_ledger.json", {"hjb_calls": 2, "replay_hjb_calls": 0, "calls": ledger})
        return 2

    replay_rows: list[dict[str, Any]] = []
    for call_number, identity in enumerate(proven, start=3):
        args, _ = _call_inputs(root, identity["turn"], identity["province_index"], grid, params, numerics)
        result, trace = solve_with_observations(*args)
        exact, mismatches = _accepted_npz_equal(result, Path(identity["accepted_hjb_path"]))
        trace.update({
            "task_id": TASK_ID, "turn": identity["turn"], "province": identity["province"],
            "province_index": identity["province_index"], "input_identity_status": identity["status"],
            "consumed_r_a": identity["consumed_r_a"], "raw_entering_r_a": identity["raw_entering_r_a"],
            "return_guard_state": identity["return_guard_state"], "wage": identity["wage"],
            "wage_guard_state": identity["wage_guard_state"], "d1_active": False,
            "final_converged": bool(result.converged), "final_iterations": int(result.iterations),
            "final_convergence_statistic": float(result.convergence_statistic),
            "accepted_scientific_output_exact": exact, "accepted_scientific_output_mismatches": mismatches,
        })
        expected_operator_hash = _accepted_final_operator_hash(Path(identity["trace_path"]))
        trace["accepted_final_operator_sha256"] = expected_operator_hash
        trace["final_operator_exact"] = trace["iterations"][-1]["operator"]["full_sha256"] == expected_operator_hash
        trace_path = output_root / "traces" / f"turn_{identity['turn']:02d}" / f"p{identity['province_index']:02d}_{identity['province']}.json"
        _write_json(trace_path, trace)
        ledger.append({"call": call_number, "phase": "REPLAY_ON", "turn": identity["turn"],
                       "province": identity["province"], "consumed": True, "accepted_output_exact": exact,
                       "final_operator_exact": trace["final_operator_exact"]})
        replay_rows.append({"turn": identity["turn"], "province_index": identity["province_index"],
                            "province": identity["province"], "converged": bool(result.converged),
                            "iterations": int(result.iterations), "statistic": float(result.convergence_statistic),
                            "accepted_output_exact": exact, "final_operator_exact": trace["final_operator_exact"],
                            "trace_path": str(trace_path)})
    _write_json(output_root / "replay_summary.json", replay_rows)
    _write_json(output_root / "call_ledger.json", {
        "schema": "CH5_MP4C_K1_HJB_MECHANISM_CALL_LEDGER_V1", "hjb_calls": len(ledger),
        "parity_hjb_calls": 2, "replay_hjb_calls": len(replay_rows), "scientific_retries": 0,
        "kfe_calls": 0, "matlab_calls": 0, "outer_trajectory_advancements": 0,
        "household_steady_state_calls": 0, "firm_calls": 0, "calls": ledger,
    })
    _write_json(output_root / "terminal_result.json", {
        "status": "REPLAY_COMPLETE", "hjb_calls": len(ledger), "exact_input_coverage": len(proven),
        "accepted_output_exact_count": sum(row["accepted_output_exact"] for row in replay_rows),
        "final_operator_exact_count": sum(row["final_operator_exact"] for row in replay_rows),
        "turn1_converged": sum(row["turn"] == 1 and row["converged"] for row in replay_rows),
        "turn2_converged": sum(row["turn"] == 2 and row["converged"] for row in replay_rows),
        "results_eligible": False,
    })
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("preflight", "run"):
        item = sub.add_parser(name); item.add_argument("accepted_parent", type=Path); item.add_argument("output_root", type=Path)
    args = parser.parse_args(argv)
    return preflight(args.accepted_parent, args.output_root) if args.command == "preflight" else run(args.accepted_parent, args.output_root)


if __name__ == "__main__":
    raise SystemExit(main())
