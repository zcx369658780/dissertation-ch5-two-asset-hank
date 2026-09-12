"""Five-turn annual K1A G1/G2 diagnostic with a common turn-1 bootstrap."""

from __future__ import annotations

import argparse
import json
import shutil
from dataclasses import replace
from pathlib import Path
from typing import Any, Mapping

import numpy as np

from ch5_two_asset_hank.multi_province.capital_allocation import CapitalAllocationInputs
from ch5_two_asset_hank.multi_province.k1a_runtime_adapter import (
    K1ARuntimeConfig, allocate_k1a_capital, load_accepted_distance_score,
)
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER
from validators.multi_province.k1_annual_hjb_g1_guard import run as prior
from validators.multi_province.k1_raw_ra0_payoff_bootstrap_safety import run as raw


REPO = Path(__file__).resolve().parents[3]
DISTANCE = REPO / "docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv"
PATHS = {"G1": ("annual_g1_guarded", 2.0), "G2": ("annual_g2_guarded", 2.0)}
RETURN_GUARDS = {"G1": (-0.05, 0.20), "G2": (-0.10, 0.35)}
WAGE_GUARD = (0.8, 1.3)
BOOTSTRAP = prior.BOOTSTRAP
ANNUAL_RAW = prior.ANNUAL_RAW
ANNUAL_DELTA = prior.ANNUAL_DELTA
MODEL_TIME_BASE = prior.MODEL_TIME_BASE
WAGE_HIT_CRITERION = "EXACT_EQUALITY_OF_GUARDED_WJT__TASK_SECTION_7"


annual_model_params = prior.annual_model_params
annual_ra0_residual = prior.annual_ra0_residual


def wage_boundary_flags(guarded_wjt: float) -> tuple[bool, bool, bool]:
    """Implement the task's literal wjt == bound monitoring criterion."""

    wage = float(guarded_wjt)
    if not np.isfinite(wage):
        raise ValueError("guarded wjt must be finite")
    lower, upper = wage == WAGE_GUARD[0], wage == WAGE_GUARD[1]
    return lower, upper, not lower and not upper


def hjb_consumed_return(path_id: str, turn: int, raw_converted_rah: float) -> tuple[float, str]:
    value = float(raw_converted_rah)
    if path_id not in PATHS:
        raise ValueError("path_id must be G1 or G2")
    if not np.isfinite(value):
        raise ValueError("converted annual rah must be finite")
    if turn <= 1:
        return value, "NOT_APPLIED_BOOTSTRAP"
    lower, upper = RETURN_GUARDS[path_id]
    consumed = float(np.clip(value, lower, upper))
    hit = "LOWER" if value < lower else "UPPER" if value > upper else "UNSATURATED"
    return consumed, hit


def select_allocation_payoff(
    *, path_id: str, allocation_turn: int, inputs: CapitalAllocationInputs,
    prior_firms: list[tuple[Any, float]] | None,
) -> tuple[str, str, int | None, np.ndarray]:
    if path_id not in PATHS:
        raise ValueError("path_id must be G1 or G2")
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
    if prior.sha256(payload_bytes).hexdigest().upper() != prior.PAYLOAD_SHA256:
        raise ValueError("accepted runtime payload SHA mismatch")
    payload = json.loads(payload_bytes)
    if len(payload["states"]) != 31:
        raise ValueError("accepted payload must contain 31 province states")
    for path_id, (name, beta) in PATHS.items():
        root = parent / name
        root.mkdir()
        (root / "runtime_input_payload.json").write_bytes(payload_bytes)
        raw.base._write_json(root / "phase_a_zero_science_receipt.json", {
            "schema": "CH5_K1_ANNUAL_G1_VS_G2_PHASE_A_V1", "status": "PASS",
            "focused_test_cases": test_cases, "focused_test_processes": test_processes,
            "scientific_processes": 0, "hjb_calls": 0, "kfe_calls": 0,
            "initialization_observations": 0, "trajectory_calls": 0,
        })
        raw.base._write_json(root / "runtime_input_receipt.json", {
            "schema": "CH5_K1_ANNUAL_G1_VS_G2_RUNTIME_INPUT_V1", "path_id": path_id,
            "runtime_payload_sha256": prior.PAYLOAD_SHA256, "province_order": PROVINCE_ORDER,
            "beta_distance": beta, "beta_return": 0.0, "turn1_mode": BOOTSTRAP,
            "turns_2_5_payoff_mode": ANNUAL_RAW,
            "hjb_guard_mode": f"{path_id}_ONLY_TURNS_2_5",
            "hjb_guard_bounds": list(RETURN_GUARDS[path_id]),
            "model_time_base": MODEL_TIME_BASE, "rho_per_year": 0.05,
            "rb_per_year": 0.02, "borrowing_gap_per_year": 0.07,
            "firm_hjb_delta_per_year": ANNUAL_DELTA,
            "q_z_off_diagonal_per_year": 1.0 / 3.0,
            "chi0": 0.1, "chi1_years": 2.0, "wage_guard": list(WAGE_GUARD),
            "wage_hit_criterion": WAGE_HIT_CRITERION,
            "wage_guard_classification": "TEMPORARY_NUMERICAL_DIAGNOSTIC_SCAFFOLDING",
            "source_faithful_labor": True, "normalized_labor": False,
            "c1_rule": "GovInv=max(Ktarget-Kprivate,0)",
            "portfolio_smoothing": False, "partial_adjustment": False,
        })
        raw.base._write_json(root / "bounded_invocation_receipt.json", {
            "schema": "CH5_K1_ANNUAL_G1_VS_G2_BOUNDED_INVOCATION_V1", "path_id": path_id,
            "trajectory_invocations_maximum": 1, "outer_turns_maximum": 5,
            "province_hjb_calls_maximum": 155, "province_kfe_calls_maximum": 155,
            "scientific_retries": 0, "engineering_retries_maximum": 1,
            "matlab_calls": 0, "standalone_kfe_experiments": 0, "k1b_runs": 0,
            "k2_runs": 0, "ge_calls": 0, "annual_downstream_calls": 0,
            "irf_calls": 0, "results_calls": 0,
        })
    raw.base._write_json(parent / "prepare_receipt.json", {
        "schema": "CH5_K1_ANNUAL_G1_VS_G2_PREPARE_V1", "status": "PASS",
        "path_roots": {key: name for key, (name, _) in PATHS.items()},
        "runtime_payload_sha256": prior.PAYLOAD_SHA256, "payloads_byte_identical": True,
        "initial_state_ra0_count": sum("ra0" in state for state in payload["states"]),
        "initial_state_ra_count": sum("ra" in state for state in payload["states"]),
        "scientific_calls": 0,
    })
    raw.base._write_json(parent / "protected_source_identity_receipt.json", raw.base.protected_science_identity())


def preflight(evidence_parent: Path) -> None:
    parent = Path(evidence_parent)
    roots = [parent / PATHS[key][0] for key in ("G1", "G2")]
    if roots[0].joinpath("runtime_input_payload.json").read_bytes() != roots[1].joinpath("runtime_input_payload.json").read_bytes():
        raise ValueError("G1/G2 starting payloads are not byte-identical")
    if any(root.joinpath("science_started.json").exists() for root in roots):
        raise ValueError("science already started")
    payload = json.loads(roots[0].joinpath("runtime_input_payload.json").read_text(encoding="utf-8"))
    states = payload["states"]
    if len(states) != 31 or any(float(s["rb"]) != 0.02 or float(s["rb_gap"]) != 0.07 for s in states):
        raise ValueError("annual liquid-return contract mismatch")
    if any(float(s["wjtmin"]) != WAGE_GUARD[0] or float(s["wjtmax"]) != WAGE_GUARD[1] for s in states):
        raise ValueError("wage guard changed")
    if prior._sha(prior.LEGACY) != prior.LEGACY_SHA256:
        raise ValueError("legacy allocator changed")
    raw.base.protected_science_identity()
    distance = load_accepted_distance_score(DISTANCE)
    config = K1ARuntimeConfig(PROVINCE_ORDER, distance, 2.0)
    probe = CapitalAllocationInputs(np.linspace(1, 2, 31), np.linspace(10, 20, 31),
                                    np.linspace(0.1, 0.3, 31), np.linspace(0.02, 0.09, 31))
    payoff = np.linspace(0.1, 1.0, 31)
    used = allocate_k1a_capital(probe, config)
    rebuilt = allocate_k1a_capital(raw._inputs_with_payoff(probe, payoff), config)
    if not np.array_equal(used.network.portfolio_shares_destination_origin, rebuilt.network.portfolio_shares_destination_origin):
        raise RuntimeError("payoff source changed S")
    if not np.array_equal(used.kt_supply, rebuilt.kt_supply):
        raise RuntimeError("payoff source changed quantities")
    if not np.array_equal(rebuilt.household_illiquid_return_rah, payoff @ rebuilt.network.portfolio_shares_destination_origin):
        raise RuntimeError("annual raw same-S payoff identity failed")
    firm_text = (REPO / "src/ch5_two_asset_hank/multi_province/firm.py").read_text(encoding="utf-8")
    c1_text = (REPO / "src/ch5_two_asset_hank/multi_province/c1_residual_public_asset.py").read_text(encoding="utf-8")
    if "ra0 = rk - delta + profit * (1.0 - corptau) / kt" not in firm_text:
        raise RuntimeError("raw ra0 formula identity changed")
    if "residual_government_asset_levels" not in c1_text or "reconstruct_migration_labor" not in c1_text:
        raise RuntimeError("C1 or source-faithful labor marker missing")
    gate = {
        "schema": "CH5_K1_ANNUAL_G1_VS_G2_PRE_RUN_GATE_V1", "status": "PASS",
        "live_baseline": raw.base._git_text("rev-parse", "HEAD"),
        "task_id": "CH5_MP4C_K1_ANNUAL_HJB_G1_VS_G2_PRICE_GUARD_CONTINUATION_DIAGNOSTIC",
        "payloads_byte_identical_except_path_guard_metadata": True,
        "turn1_common_bootstrap_identical": True, "model_time_base": MODEL_TIME_BASE,
        "rho_per_year": 0.05, "rb_per_year": 0.02, "borrowing_gap_per_year": 0.07,
        "firm_hjb_delta_both_paths": ANNUAL_DELTA, "q_z_off_diagonal_per_year": 1.0 / 3.0,
        "chi0": 0.1, "chi1_years": 2.0, "no_divide_or_multiply_by_four": True,
        "no_compounding_or_log_conversion": True,
        "raw_ra0_formula": "rk_annual + after_tax_profit_over_K_annual - 0.10",
        "raw_ra0_legacy_0p02_0p09_clip_before_aggregation": False,
        "g1_turn2_source": "clip(same_path.completed_turn_1.firm.ra0_annual @ S,-0.05,0.20)_AT_HJB_INTERFACE_ONLY",
        "g2_turn2_source": "clip(same_path.completed_turn_1.firm.ra0_annual @ S,-0.10,0.35)_AT_HJB_INTERFACE_ONLY",
        "same_S_static_identity": True, "quantity_bit_identical_under_payoff_switch": True,
        "wage_guard": list(WAGE_GUARD), "wage_guard_unchanged": True,
        "wage_hit_monitoring": WAGE_HIT_CRITERION,
        "return_hit_monitoring": "RAW_CONVERTED_GUARDED_WITH_EXPLICIT_FLAGS_AND_NAMES",
        "beta_distance_both": 2.0, "beta_return_both": 0.0, "k1b_disabled": True,
        "k2_disabled": True, "source_faithful_labor": True, "normalized_labor": False,
        "smoothing": False, "partial_adjustment": False, "c1_formula_unchanged": True,
        "grid_tolerance_solver_unchanged": True, "science_calls_before_gate": 0,
    }
    raw.base._write_json(parent / "pre_run_gate.json", gate)
    for root in roots:
        shutil.copyfile(parent / "pre_run_gate.json", root / "pre_run_gate.json")


def execute(evidence_parent: Path, path_id: str) -> int:
    path_id = path_id.upper()
    if path_id not in PATHS:
        raise ValueError("path_id must be G1 or G2")
    active: dict[str, Any] = {"turn": 0, "province_index": 0, "guard": {}}
    g1, oracle, base = raw.g1, raw.g1.single.oracle, raw.base
    original = {"paths": raw.PATHS, "selector": raw.select_allocation_payoff,
                "mapping_proxy": g1.MappingProxyType, "solver": oracle.solve_matlab_faithful_hjb,
                "writer": g1.write_json, "augment": base._augment_turn_rows}

    def mapping_proxy(values: Mapping[str, float]):
        return annual_model_params(values)

    def write_json(path: Path, value: Any) -> None:
        if path.name == "entering_state.json" and isinstance(value, dict):
            active["turn"], active["province_index"] = int(value["turn"]), 0
        elif path.name == "science_started.json" and isinstance(value, dict):
            value.update({"schema": "CH5_K1_ANNUAL_G1_VS_G2_SCIENCE_STARTED_V1", "path_id": path_id,
                          "model_time_base": MODEL_TIME_BASE, "firm_hjb_delta_per_year": ANNUAL_DELTA})
        elif path.name == "call_ledger.json" and isinstance(value, dict):
            value.update({"schema": "CH5_K1_ANNUAL_G1_VS_G2_CALL_LEDGER_V1", "path_id": path_id,
                          "trajectory_invocations": 1, "scientific_retries": 0,
                          "annual_downstream_calls": 0, "return_guard": list(RETURN_GUARDS[path_id])})
        elif path.name == "terminal_result.json" and isinstance(value, dict):
            value.update({"schema": "CH5_K1_ANNUAL_G1_VS_G2_TERMINAL_V1", "path_id": path_id,
                          "model_time_base": MODEL_TIME_BASE, "results_eligible": False,
                          "guard_treatment_turns": [2, 3, 4, 5]})
        original["writer"](path, value)

    def solve(grid, params, inputs, initial_value, baseline_labor, transfer_income,
              borrowing_rate_gap, numerics):
        turn, index = int(active["turn"]), int(active["province_index"])
        consumed, hit = hjb_consumed_return(path_id, turn, float(inputs.r_a))
        lower, upper = RETURN_GUARDS[path_id]
        if turn >= 1:
            active["guard"][(turn, index)] = {
                "raw_converted_rah_annual": float(inputs.r_a), "hjb_consumed_r_a": consumed,
                "guard_hit": hit, "return_guard_lower_hit": hit == "LOWER",
                "return_guard_upper_hit": hit == "UPPER", "return_guard_unsaturated": hit == "UNSATURATED",
                "guard_lower": lower, "guard_upper": upper,
                "guard_scope": "PROVINCE_SCALAR_HJB_INPUT__GRID_CELL_NOT_APPLICABLE",
            }
            active["province_index"] = index + 1
        return original["solver"](grid, params, replace(inputs, r_a=consumed), initial_value,
                                  baseline_labor, transfer_income, borrowing_rate_gap, numerics)

    def augment(rows: list[dict[str, Any]], recorder: Any, turn: int) -> None:
        original["augment"](rows, recorder, turn)
        for index, row in enumerate(rows):
            receipt = active["guard"].get((turn, index))
            if receipt is None:
                raise RuntimeError("HJB return receipt missing")
            component = float(row["firm_after_tax_profit_component_over_K"])
            annual_residual = annual_ra0_residual(row["firm_rk"], component, row["firm_ra0"])
            wage_lower, wage_upper, wage_unsaturated = wage_boundary_flags(row["firm_wage_used"])
            row.update(receipt)
            row.update({
                "model_time_base": MODEL_TIME_BASE, "firm_hjb_delta_per_year": ANNUAL_DELTA,
                "raw_ra0_formula_reconstruction": float(row["firm_rk"]) + component - ANNUAL_DELTA,
                "raw_ra0_formula_abs_residual": abs(annual_residual),
                "firm_ra0_reconstruction_residual": annual_residual,
                "firm_ra0_reconstruction_definition": "ra0_annual-(rk_annual+after_tax_profit_over_K_annual-0.10)",
                "wage_guard_lower_hit": wage_lower, "wage_guard_upper_hit": wage_upper,
                "wage_guard_unsaturated": wage_unsaturated,
                "wage_clip_activated_lower": bool(row["wage_clipped_lower"]),
                "wage_clip_activated_upper": bool(row["wage_clipped_upper"]),
                "wage_hit_criterion": WAGE_HIT_CRITERION,
                "wage_guard_classification": "TEMPORARY_NUMERICAL_DIAGNOSTIC_SCAFFOLDING",
            })

    try:
        raw.PATHS, raw.select_allocation_payoff = PATHS, select_allocation_payoff
        g1.MappingProxyType, oracle.solve_matlab_faithful_hjb = mapping_proxy, solve
        g1.write_json, base._augment_turn_rows = write_json, augment
        return raw.execute(Path(evidence_parent), path_id)
    finally:
        raw.PATHS, raw.select_allocation_payoff = original["paths"], original["selector"]
        g1.MappingProxyType, oracle.solve_matlab_faithful_hjb = original["mapping_proxy"], original["solver"]
        g1.write_json, base._augment_turn_rows = original["writer"], original["augment"]


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
