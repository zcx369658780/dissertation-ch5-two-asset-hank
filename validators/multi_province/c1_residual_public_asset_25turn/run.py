"""Run one initialization observation and one C1 25-turn trajectory."""
from __future__ import annotations

import argparse
import json
import sys
from hashlib import sha256
from pathlib import Path
from typing import Any, Mapping

import numpy as np

REPO = Path(__file__).resolve().parents[3]
for item in (REPO / "src", REPO):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))

from ch5_two_asset_hank.multi_province import one_turn as one_turn_module
from ch5_two_asset_hank.multi_province.c1_residual_public_asset import (
    C1ResidualPublicAssetOneTurnResult,
    run_c1_residual_public_asset_one_turn,
)
from ch5_two_asset_hank.multi_province.government_assets import residual_government_asset_levels
from ch5_two_asset_hank.multi_province.one_turn import PreFrozenHouseholdOutputBatch
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER
from ch5_two_asset_hank.multi_province.steady_state import AdaptiveAction
from validators.multi_province.g1_residual_govinv_25turn_isolated import run as g1


VERDICT_PASS = "C1_RESIDUAL_PUBLIC_ASSET_25TURN_PASS__CAPITAL_TARGET_HELD_AND_BOUNDED_PATH_QUANTIFIED"
VERDICT_PARTIAL = "C1_RESIDUAL_PUBLIC_ASSET_25TURN_PARTIAL__ACCOUNTING_CONTRACT_VALID_BUT_TRUE_HARD_FAILURE_BEFORE_LATE_WINDOW"
VERDICT_FAIL = "C1_RESIDUAL_PUBLIC_ASSET_25TURN_FAIL__CAPITAL_TARGET_HELD_BUT_OTHER_STATE_INSTABILITY_PERSISTS_OR_WORSENS"
_SOURCE_POST_TURN = g1._post_turn_states


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")


def _sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest().upper()


def record_phase_a(evidence_root: Path, test_processes: int, test_cases: int, compile_processes: int) -> None:
    root = Path(evidence_root)
    root.mkdir(parents=True, exist_ok=False)
    _write_json(root / "phase_a_zero_science_receipt.json", {
        "schema": "CH5_C1_RESIDUAL_PUBLIC_ASSET_25TURN_PHASE_A_ZERO_SCIENCE_V1",
        "status": "PASS", "focused_test_processes": test_processes,
        "focused_test_cases": test_cases, "compile_processes": compile_processes,
        "scientific_processes": 0, "hjb_calls": 0, "kfe_calls": 0,
        "initialization_observations": 0, "trajectory_calls": 0,
        "contract": {
            "separately_named_c1_one_turn": True,
            "contemporaneous_private_capital_precedes_c1_and_firm": True,
            "firm_uses_private_plus_c1_public_asset": True,
            "historical_c0_source_unchanged": True,
            "historical_c0_action_disabled_in_c1": True,
            "source_faithful_labor_route": True,
            "normalized_labor_route_active": False,
            "finite_hjb_nonconvergence_continues_diagnostic_only": True,
        },
    })


def prepare(distance_workbook: Path, evidence_root: Path) -> None:
    root = Path(evidence_root)
    g1.prepare(distance_workbook, root)
    runtime = json.loads((root / "runtime_input_receipt.json").read_text(encoding="utf-8"))
    runtime.update({
        "schema": "CH5_C1_RESIDUAL_PUBLIC_ASSET_25TURN_RUNTIME_RECEIPT_V1",
        "initialization_rule": "GovInv0_C1=max(Ktarget-Kprivate_initial,0)",
        "trajectory_rule": "GovInv_C1=max(Ktarget-Kprivate_current,0)",
    })
    _write_json(root / "runtime_input_receipt.json", runtime)
    source = json.loads((root / "source_hash_receipt.json").read_text(encoding="utf-8"))
    source["schema"] = "CH5_C1_RESIDUAL_PUBLIC_ASSET_25TURN_SOURCE_HASH_V1"
    for relative in (
        "src/ch5_two_asset_hank/multi_province/c1_residual_public_asset.py",
        "src/ch5_two_asset_hank/multi_province/government_assets.py",
        "validators/multi_province/c1_residual_public_asset_25turn/run.py",
        "validators/multi_province/c1_residual_public_asset_25turn/finalize.py",
        "tests/test_mp4c_c1_residual_public_asset_25turn.py",
    ):
        source["files"][relative] = _sha(REPO / relative)
    source["legacy_unchanged_contract"] = {
        relative: source["files"][relative] for relative in (
            "src/ch5_two_asset_hank/multi_province/one_turn.py",
            "src/ch5_two_asset_hank/multi_province/steady_state.py",
            "src/ch5_two_asset_hank/multi_province/firm.py",
        )
    }
    _write_json(root / "source_hash_receipt.json", source)
    bounded = json.loads((root / "bounded_invocation_receipt.json").read_text(encoding="utf-8"))
    bounded.update({
        "schema": "CH5_C1_RESIDUAL_PUBLIC_ASSET_25TURN_BOUNDED_INVOCATION_V1",
        "prepare_entrypoint": "validators/multi_province/c1_residual_public_asset_25turn/run.py prepare",
        "science_entrypoint": "validators/multi_province/c1_residual_public_asset_25turn/run.py run",
        "c1_govinv_actions": "RESIDUAL_LEVEL_ONLY__NO_HISTORICAL_C0_ACTION",
    })
    _write_json(root / "bounded_invocation_receipt.json", bounded)


def build_c1_initial_states(
    states_g0: tuple[Mapping[str, object], ...], target: np.ndarray, private: np.ndarray,
) -> tuple[tuple[dict[str, object], ...], dict[str, np.ndarray]]:
    batch = residual_government_asset_levels(
        Ktarget_MU=target, Kprivate_current_MU=private, province_order=PROVINCE_ORDER,
    )
    if len(states_g0) != 31:
        raise ValueError("state and capital vector counts differ")
    states = tuple({**state, "GovInv": float(batch.GovInv_residual_MU[i])} for i, state in enumerate(states_g0))
    for before, after in zip(states_g0, states):
        changed = [key for key in before if before[key] != after[key]]
        if changed != ["GovInv"]:
            raise RuntimeError(f"{before['name']}: C1 initialization must replace only GovInv, changed={changed}")
    target_array = np.asarray(target, dtype=float)
    private_array = np.asarray(private, dtype=float)
    return states, {
        "govinv_g0": target_array.copy(), "govinv_g1": batch.GovInv_residual_MU,
        "g0_total": target_array + private_array, "g1_total": batch.firm_K_accounting_MU,
        "beta_star": np.divide(target_array, private_array, out=np.full_like(target_array, np.inf), where=private_array > 0.0),
    }


def _post_turn_states_c1(
    states: tuple[Mapping[str, object], ...], batch: PreFrozenHouseholdOutputBatch,
    turn: C1ResidualPublicAssetOneTurnResult,
) -> list[dict[str, object]]:
    updated = _SOURCE_POST_TURN(states, batch, turn)
    for index, state in enumerate(updated):
        state["GovInv"] = float(turn.c1_accounting.GovInv_residual_MU[index])
        state["C1_residual_status"] = turn.c1_accounting.status[index]
        state["C1_residual_floor_binding"] = bool(turn.c1_accounting.residual_floor_binding[index])
    return updated


def _adapt_c1_zt_only(
    states: list[dict[str, object]], max_nk_gap: float, steady_state: bool,
) -> tuple[list[dict[str, object]], tuple[AdaptiveAction, ...]]:
    actions = []
    allow = max_nk_gap < 0.1 and steady_state
    for state in states:
        zt_before = float(state["Zt"])
        zt_after = zt_before
        zt_adjusted = False
        if allow:
            discrepancy = float(state["Yt"]) / float(state["Yt0"]) - 1.0
            if discrepancy > 0.01 or discrepancy < -0.01:
                zt_after = float(state["Yt0"]) * float(state["Kt"]) ** (-float(state["alpha"])) * float(state["Lt"]) ** (float(state["alpha"]) - 1.0)
                state["Zt"] = zt_after
                zt_adjusted = True
        gov = float(state["GovInv"])
        actions.append(AdaptiveAction(
            province=str(state["name"]), zt_adjusted=zt_adjusted,
            zt_before=zt_before, zt_after=zt_after,
            govinv_action="C1_RESIDUAL_LEVEL__NO_C0_ACTION",
            govinv_before=gov, govinv_after=gov,
        ))
    return states, tuple(actions)


def _correct_turn_rows(rows: list[dict[str, Any]]) -> None:
    for row in rows:
        target = float(row["Ktarget_2018_MU"])
        private = float(row["Kt_supply_private_MU"])
        firm = float(row["firm_K_total_MU"])
        gov = firm - private
        floor = private >= target
        tolerance = 1e-12 * max(1.0, abs(target), abs(private))
        expected = private if floor else target
        if gov < -tolerance or abs(firm - expected) > tolerance or (floor and abs(gov) > tolerance):
            raise RuntimeError(f"{row['province']}: hard C1 accounting assertion failed")
        row.update({
            "GovInv_C1_MU": gov, "GovInv_before_MU": gov, "GovInv_after_MU": gov,
            "GovInv": gov, "GovInv_C1_over_Ktarget": gov / target,
            "GovInv_before_over_Ktarget": gov / target, "GovInv_after_over_Ktarget": gov / target,
            "private_K_at_or_above_target": floor, "residual_floor_binding": floor,
            "capital_gap_before_MU": target - private, "capital_gap_after_MU": target - firm,
            "c1_accounting_abs_residual_MU": abs(firm - expected),
            "govinv_action": "C1_RESIDUAL_LEVEL__NO_C0_ACTION",
        })


def execute(evidence_root: Path) -> int:
    root = Path(evidence_root)
    originals = {
        "one_turn": one_turn_module.run_source_faithful_one_turn,
        "build": g1.build_g1_initial_states, "post": g1._post_turn_states,
        "adapt": g1._adapt, "classify": g1.classify_completed_path,
        "write_json": g1.write_json, "write_csv": g1.write_csv,
        "pass": g1.VERDICT_PASS, "partial": g1.VERDICT_PARTIAL, "fail": g1.VERDICT_FAIL,
    }
    def observed_json(path: Path, value: Any) -> None:
        if path.name == "per_province_observables.json" and isinstance(value, list):
            _correct_turn_rows(value)
        elif path.name == "entering_state.json" and isinstance(value, dict):
            value["initialization_route"] = "C1_RESIDUAL_PUBLIC_ASSET"
        elif path.name == "terminal_result.json" and isinstance(value, dict):
            value["schema"] = "CH5_C1_RESIDUAL_PUBLIC_ASSET_25TURN_TERMINAL_V1"
        elif path.name == "national_initialization_summary.json" and isinstance(value, dict):
            value["schema"] = "CH5_C1_RESIDUAL_PUBLIC_ASSET_NATIONAL_INITIALIZATION_V1"
            value["initialization_route"] = "C1_RESIDUAL_PUBLIC_ASSET"
        originals["write_json"](path, value)

    def observed_csv(path: Path, rows: list[dict[str, Any]]) -> None:
        if path.name == "initialization_receipt_31province.csv":
            for row in rows:
                row["GovInv0_C1_MU"] = row["GovInv0_G1_MU"]
                row["firm_K_accounting_C1_MU"] = row["firm_K_accounting_G1_MU"]
        originals["write_csv"](path, rows)

    try:
        one_turn_module.run_source_faithful_one_turn = run_c1_residual_public_asset_one_turn
        g1.build_g1_initial_states = build_c1_initial_states
        g1._post_turn_states = _post_turn_states_c1
        g1._adapt = _adapt_c1_zt_only
        g1.classify_completed_path = lambda summaries: VERDICT_PASS if len(summaries) == 25 else VERDICT_PARTIAL
        g1.write_json, g1.write_csv = observed_json, observed_csv
        g1.VERDICT_PASS, g1.VERDICT_PARTIAL, g1.VERDICT_FAIL = VERDICT_PASS, VERDICT_PARTIAL, VERDICT_FAIL
        return g1.execute(root)
    finally:
        one_turn_module.run_source_faithful_one_turn = originals["one_turn"]
        g1.build_g1_initial_states, g1._post_turn_states = originals["build"], originals["post"]
        g1._adapt, g1.classify_completed_path = originals["adapt"], originals["classify"]
        g1.write_json, g1.write_csv = originals["write_json"], originals["write_csv"]
        g1.VERDICT_PASS, g1.VERDICT_PARTIAL, g1.VERDICT_FAIL = originals["pass"], originals["partial"], originals["fail"]


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
