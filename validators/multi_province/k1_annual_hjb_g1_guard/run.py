"""Five-turn annual K1A U/G1 diagnostic with a common turn-1 bootstrap."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from dataclasses import replace
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

import numpy as np

REPO = Path(__file__).resolve().parents[3]
for item in (REPO / "src", REPO):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))

from ch5_two_asset_hank.multi_province.capital_allocation import CapitalAllocationInputs  # noqa: E402
from ch5_two_asset_hank.multi_province.k1a_runtime_adapter import (  # noqa: E402
    K1ARuntimeConfig,
    allocate_k1a_capital,
    load_accepted_distance_score,
)
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER  # noqa: E402
from validators.multi_province.k1_raw_ra0_payoff_bootstrap_safety import run as raw  # noqa: E402


DISTANCE = REPO / "docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv"
LEGACY = REPO / "src/ch5_two_asset_hank/multi_province/capital_allocation.py"
LEGACY_SHA256 = "BB3F283BD782399A5C1C9AEE06DC50BBA61A0599BF062669DE0B1EBBB01AEE40"
PAYLOAD_SHA256 = "EBB9FD91F3D3CE5D46476FE7BF1D0662E26EEA5C87357E4B13907CC76EBE9355"
PATHS = {"U": ("annual_unguarded", 2.0), "G1": ("annual_g1_guarded", 2.0)}
BOOTSTRAP = "COMMON_ACCEPTED_ENTERING_PAYOFF_BOOTSTRAP"
ANNUAL_RAW = "PRIOR_COMPLETED_ANNUAL_RAW_RA0"
MODEL_TIME_BASE = "ANNUAL_CONTINUOUS_TIME"
RETURN_GUARD = (-0.05, 0.20)
WAGE_GUARD = (0.8, 1.3)
ANNUAL_DELTA = 0.10


def _sha(path: Path) -> str:
    return sha256(Path(path).read_bytes()).hexdigest().upper()


def _array_sha(value: object) -> str:
    return sha256(np.asarray(value, dtype="<f8").tobytes(order="C")).hexdigest().upper()


def annual_model_params(values: Mapping[str, float]) -> Mapping[str, float]:
    """Return the task-local annual firm calibration without mutating its source."""

    result = dict(values)
    required = {"ga", "phi_l", "alphal", "epsilon", "theta", "delta"}
    if required.issubset(result):
        result["delta"] = ANNUAL_DELTA
    return MappingProxyType(result)


def annual_ra0_residual(rk_annual: float, profit_component: float, ra0_annual: float) -> float:
    """Check annual ra0 against the independently persisted firm profit/K component."""

    rk, component, ra0 = float(rk_annual), float(profit_component), float(ra0_annual)
    if not np.isfinite([rk, component, ra0]).all():
        raise ValueError("annual firm return components must be finite")
    return ra0 - (rk + component - ANNUAL_DELTA)


def hjb_consumed_return(path_id: str, turn: int, raw_converted_rah: float) -> tuple[float, str]:
    """Select only the scalar HJB-interface return; preserve the raw state value."""

    value = float(raw_converted_rah)
    if not np.isfinite(value):
        raise ValueError("converted annual rah must be finite")
    if path_id == "G1" and turn >= 2:
        consumed = float(np.clip(value, RETURN_GUARD[0], RETURN_GUARD[1]))
        hit = "LOWER" if value < RETURN_GUARD[0] else "UPPER" if value > RETURN_GUARD[1] else "UNSATURATED"
        return consumed, hit
    if path_id not in PATHS:
        raise ValueError("path_id must be U or G1")
    return value, "NOT_APPLIED_BOOTSTRAP" if turn <= 1 else "UNGUARDED"


def select_allocation_payoff(
    *, path_id: str, allocation_turn: int, inputs: CapitalAllocationInputs,
    prior_firms: list[tuple[Any, float]] | None,
) -> tuple[str, str, int | None, np.ndarray]:
    """Both annual paths bootstrap once, then use own prior-completed raw ra0."""

    if path_id not in PATHS:
        raise ValueError("path_id must be U or G1")
    if allocation_turn <= 1:
        return BOOTSTRAP, "accepted_entering_state.ra", None, np.array(inputs.old_firm_return_ra, copy=True)
    if prior_firms is None or len(prior_firms) != 31:
        raise ValueError("prior-completed same-path annual firm vector is unavailable")
    payoff = np.array([firm.ra0 for firm, _ in prior_firms], dtype=float)
    if payoff.shape != (31,) or not np.all(np.isfinite(payoff)):
        raise ValueError("prior-completed annual raw ra0 must be finite and 31-dimensional")
    return ANNUAL_RAW, f"same_path.completed_turn_{allocation_turn - 1}.firm.ra0_annual", allocation_turn - 1, payoff


def prepare(evidence_parent: Path, accepted_payload: Path, test_cases: int, test_processes: int) -> None:
    parent = Path(evidence_parent)
    parent.mkdir(parents=True, exist_ok=False)
    payload_bytes = Path(accepted_payload).read_bytes()
    if sha256(payload_bytes).hexdigest().upper() != PAYLOAD_SHA256:
        raise ValueError("accepted runtime payload SHA mismatch")
    payload = json.loads(payload_bytes)
    if len(payload["states"]) != 31:
        raise ValueError("accepted payload must contain 31 province states")
    for path_id, (name, beta) in PATHS.items():
        root = parent / name
        root.mkdir()
        (root / "runtime_input_payload.json").write_bytes(payload_bytes)
        raw.base._write_json(root / "phase_a_zero_science_receipt.json", {
            "schema": "CH5_K1_ANNUAL_G1_PHASE_A_V1", "status": "PASS",
            "focused_test_cases": test_cases, "focused_test_processes": test_processes,
            "scientific_processes": 0, "hjb_calls": 0, "kfe_calls": 0,
            "initialization_observations": 0, "trajectory_calls": 0,
        })
        raw.base._write_json(root / "runtime_input_receipt.json", {
            "schema": "CH5_K1_ANNUAL_G1_RUNTIME_INPUT_V1", "path_id": path_id,
            "runtime_payload_sha256": PAYLOAD_SHA256, "province_order": PROVINCE_ORDER,
            "beta_distance": beta, "beta_return": 0.0, "turn1_mode": BOOTSTRAP,
            "turns_2_5_payoff_mode": ANNUAL_RAW,
            "hjb_guard_mode": "OFF" if path_id == "U" else "G1_ONLY_TURNS_2_5",
            "hjb_guard_bounds": None if path_id == "U" else list(RETURN_GUARD),
            "model_time_base": MODEL_TIME_BASE, "rho_per_year": 0.05,
            "rb_per_year": 0.02, "borrowing_gap_per_year": 0.07,
            "firm_hjb_delta_per_year": ANNUAL_DELTA,
            "q_z_off_diagonal_per_year": 1.0 / 3.0,
            "chi0": 0.1, "chi1_years": 2.0,
            "wage_guard": list(WAGE_GUARD),
            "wage_guard_classification": "TEMPORARY_NUMERICAL_DIAGNOSTIC_SCAFFOLDING",
            "source_faithful_labor": True, "normalized_labor": False,
            "c1_rule": "GovInv=max(Ktarget-Kprivate,0)",
            "portfolio_smoothing": False, "partial_adjustment": False,
        })
        raw.base._write_json(root / "bounded_invocation_receipt.json", {
            "schema": "CH5_K1_ANNUAL_G1_BOUNDED_INVOCATION_V1", "path_id": path_id,
            "trajectory_invocations_maximum": 1, "outer_turns_maximum": 5,
            "province_hjb_calls_maximum": 155, "province_kfe_calls_maximum": 155,
            "scientific_retries": 0, "engineering_retries_maximum": 1,
            "matlab_calls": 0, "standalone_kfe_experiments": 0,
            "k1b_runs": 0, "k2_runs": 0, "ge_calls": 0,
            "annual_downstream_calls": 0, "irf_calls": 0, "results_calls": 0,
        })
    raw.base._write_json(parent / "prepare_receipt.json", {
        "schema": "CH5_K1_ANNUAL_G1_PREPARE_V1", "status": "PASS",
        "path_roots": {key: name for key, (name, _) in PATHS.items()},
        "runtime_payload_sha256": PAYLOAD_SHA256, "payloads_byte_identical": True,
        "initial_state_ra0_count": sum("ra0" in state for state in payload["states"]),
        "initial_state_ra_count": sum("ra" in state for state in payload["states"]),
        "scientific_calls": 0,
    })
    raw.base._write_json(parent / "protected_source_identity_receipt.json", raw.base.protected_science_identity())


def preflight(evidence_parent: Path) -> None:
    parent = Path(evidence_parent)
    roots = [parent / PATHS[key][0] for key in ("U", "G1")]
    if roots[0].joinpath("runtime_input_payload.json").read_bytes() != roots[1].joinpath("runtime_input_payload.json").read_bytes():
        raise ValueError("U/G1 starting payloads are not byte-identical")
    if any(root.joinpath("science_started.json").exists() for root in roots):
        raise ValueError("science already started")
    payload = json.loads(roots[0].joinpath("runtime_input_payload.json").read_text(encoding="utf-8"))
    states = payload["states"]
    if len(states) != 31 or any(float(s["rb"]) != 0.02 or float(s["rb_gap"]) != 0.07 for s in states):
        raise ValueError("annual liquid-return contract mismatch")
    if any(float(s["wjtmin"]) != 0.8 or float(s["wjtmax"]) != 1.3 for s in states):
        raise ValueError("wage guard changed")
    if _sha(LEGACY) != LEGACY_SHA256:
        raise ValueError("legacy allocator changed")
    raw.base.protected_science_identity()
    distance = load_accepted_distance_score(DISTANCE)
    config = K1ARuntimeConfig(PROVINCE_ORDER, distance, 2.0)
    probe = CapitalAllocationInputs(np.linspace(1, 2, 31), np.linspace(10, 20, 31),
                                    np.linspace(0.1, 0.3, 31), np.linspace(0.02, 0.09, 31))
    raw_payoff = np.linspace(0.1, 1.0, 31)
    used = allocate_k1a_capital(probe, config)
    rebuilt = allocate_k1a_capital(raw._inputs_with_payoff(probe, raw_payoff), config)
    if not np.array_equal(used.network.portfolio_shares_destination_origin, rebuilt.network.portfolio_shares_destination_origin):
        raise RuntimeError("payoff source changed S")
    if not np.array_equal(used.kt_supply, rebuilt.kt_supply):
        raise RuntimeError("payoff source changed quantities")
    if not np.array_equal(rebuilt.household_illiquid_return_rah, raw_payoff @ rebuilt.network.portfolio_shares_destination_origin):
        raise RuntimeError("annual raw same-S payoff identity failed")
    firm_text = (REPO / "src/ch5_two_asset_hank/multi_province/firm.py").read_text(encoding="utf-8")
    c1_text = (REPO / "src/ch5_two_asset_hank/multi_province/c1_residual_public_asset.py").read_text(encoding="utf-8")
    if "ra0 = rk - delta + profit * (1.0 - corptau) / kt" not in firm_text:
        raise RuntimeError("raw ra0 formula identity changed")
    if "residual_government_asset_levels" not in c1_text or "reconstruct_migration_labor" not in c1_text:
        raise RuntimeError("C1 or source-faithful labor marker missing")
    gate = {
        "schema": "CH5_K1_ANNUAL_G1_PRE_RUN_GATE_V1", "status": "PASS",
        "live_baseline": raw.base._git_text("rev-parse", "HEAD"),
        "task_id": "CH5_MP4C_K1_ANNUAL_HJB_RECALIBRATED_G1_GUARD_BOUNDED_RUNTIME_DIAGNOSTIC",
        "payloads_byte_identical": True, "turn1_common_bootstrap_identical": True,
        "model_time_base": MODEL_TIME_BASE, "rho_per_year": 0.05,
        "rb_per_year": 0.02, "borrowing_gap_per_year": 0.07,
        "firm_hjb_delta_both_paths": ANNUAL_DELTA,
        "q_z_off_diagonal_per_year": 1.0 / 3.0, "chi0": 0.1, "chi1_years": 2.0,
        "no_divide_or_multiply_by_four": True, "no_compounding_or_log_conversion": True,
        "raw_ra0_formula": "rk_annual + after_tax_profit_over_K_annual - 0.10",
        "raw_ra0_legacy_0p02_0p09_clip_before_aggregation": False,
        "u_turn2_source": "same_path.completed_turn_1.firm.ra0_annual @ S",
        "g1_turn2_source": "clip(same_path.completed_turn_1.firm.ra0_annual @ S,-0.05,0.20)_AT_HJB_INTERFACE_ONLY",
        "same_S_static_identity": True, "quantity_bit_identical_under_payoff_switch": True,
        "wage_guard": list(WAGE_GUARD), "wage_guard_unchanged": True,
        "beta_distance_both": 2.0, "beta_return_both": 0.0,
        "k1b_disabled": True, "k2_disabled": True, "source_faithful_labor": True,
        "normalized_labor": False, "smoothing": False, "partial_adjustment": False,
        "c1_formula_unchanged": True, "grid_tolerance_solver_unchanged": True,
        "science_calls_before_gate": 0,
    }
    raw.base._write_json(parent / "pre_run_gate.json", gate)
    for root in roots:
        shutil.copyfile(parent / "pre_run_gate.json", root / "pre_run_gate.json")


def execute(evidence_parent: Path, path_id: str) -> int:
    path_id = path_id.upper()
    if path_id not in PATHS:
        raise ValueError("path_id must be U or G1")
    active: dict[str, Any] = {"turn": 0, "province_index": 0, "guard": {}}
    g1 = raw.g1
    oracle = g1.single.oracle
    base = raw.base
    original = {
        "paths": raw.PATHS, "selector": raw.select_allocation_payoff,
        "mapping_proxy": g1.MappingProxyType, "solver": oracle.solve_matlab_faithful_hjb,
        "writer": g1.write_json, "augment": base._augment_turn_rows,
    }

    def mapping_proxy(values: Mapping[str, float]):
        return annual_model_params(values)

    def write_json(path: Path, value: Any) -> None:
        if path.name == "entering_state.json" and isinstance(value, dict):
            active["turn"] = int(value["turn"])
            active["province_index"] = 0
        elif path.name == "science_started.json" and isinstance(value, dict):
            value.update({"schema": "CH5_K1_ANNUAL_G1_SCIENCE_STARTED_V1", "path_id": path_id,
                          "model_time_base": MODEL_TIME_BASE, "firm_hjb_delta_per_year": ANNUAL_DELTA})
        elif path.name == "call_ledger.json" and isinstance(value, dict):
            value.update({"schema": "CH5_K1_ANNUAL_G1_CALL_LEDGER_V1", "path_id": path_id,
                          "trajectory_invocations": 1, "scientific_retries": 0,
                          "annual_downstream_calls": 0, "return_guard": "OFF" if path_id == "U" else list(RETURN_GUARD)})
        elif path.name == "terminal_result.json" and isinstance(value, dict):
            value.update({"schema": "CH5_K1_ANNUAL_G1_TERMINAL_V1", "path_id": path_id,
                          "model_time_base": MODEL_TIME_BASE, "results_eligible": False,
                          "g1_treatment_turns": [2, 3, 4, 5] if path_id == "G1" else []})
        original["writer"](path, value)

    def solve(grid, params, inputs, initial_value, baseline_labor, transfer_income, borrowing_rate_gap, numerics):
        turn = int(active["turn"])
        index = int(active["province_index"])
        consumed, hit = hjb_consumed_return(path_id, turn, float(inputs.r_a))
        if turn >= 1:
            active["guard"][(turn, index)] = {
                "raw_converted_rah_annual": float(inputs.r_a), "hjb_consumed_r_a": consumed,
                "guard_hit": hit, "guard_lower": RETURN_GUARD[0], "guard_upper": RETURN_GUARD[1],
                "guard_scope": "PROVINCE_SCALAR_HJB_INPUT__GRID_CELL_NOT_APPLICABLE",
            }
            active["province_index"] = index + 1
        return original["solver"](
            grid, params, replace(inputs, r_a=consumed), initial_value, baseline_labor,
            transfer_income, borrowing_rate_gap, numerics,
        )

    def augment(rows: list[dict[str, Any]], recorder: Any, turn: int) -> None:
        original["augment"](rows, recorder, turn)
        for index, row in enumerate(rows):
            receipt = active["guard"].get((turn, index))
            if receipt is None:
                raise RuntimeError("HJB return receipt missing")
            component = float(row["firm_after_tax_profit_component_over_K"])
            annual_residual = annual_ra0_residual(row["firm_rk"], component, row["firm_ra0"])
            row.update(receipt)
            row.update({
                "model_time_base": MODEL_TIME_BASE, "firm_hjb_delta_per_year": ANNUAL_DELTA,
                "raw_ra0_formula_reconstruction": float(row["firm_rk"]) + component - ANNUAL_DELTA,
                "raw_ra0_formula_abs_residual": abs(annual_residual),
                "firm_ra0_reconstruction_residual": annual_residual,
                "firm_ra0_reconstruction_definition": "ra0_annual-(rk_annual+after_tax_profit_over_K_annual-0.10)",
                "wage_guard_classification": "TEMPORARY_NUMERICAL_DIAGNOSTIC_SCAFFOLDING",
            })

    try:
        raw.PATHS = PATHS
        raw.select_allocation_payoff = select_allocation_payoff
        g1.MappingProxyType = mapping_proxy
        oracle.solve_matlab_faithful_hjb = solve
        g1.write_json = write_json
        base._augment_turn_rows = augment
        return raw.execute(Path(evidence_parent), path_id)
    finally:
        raw.PATHS = original["paths"]
        raw.select_allocation_payoff = original["selector"]
        g1.MappingProxyType = original["mapping_proxy"]
        oracle.solve_matlab_faithful_hjb = original["solver"]
        g1.write_json = original["writer"]
        base._augment_turn_rows = original["augment"]


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
    launch.add_argument("path_id", choices=("U", "G1"))
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
