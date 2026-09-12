"""Five-turn K1 raw-ra0 payoff safety runner with a common clipped-ra bootstrap."""

from __future__ import annotations

import argparse
import builtins
import json
import shutil
import sys
from dataclasses import replace
from hashlib import sha256
from pathlib import Path
from typing import Any

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
from validators.multi_province.c1_residual_public_asset_25turn import run as c1  # noqa: E402
from validators.multi_province.g1_residual_govinv_25turn_isolated import run as g1  # noqa: E402
from validators.multi_province.k1a_equal_share_vs_beta2 import run as base  # noqa: E402


DISTANCE = REPO / "docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv"
INITIALIZATION = REPO / "reports/mp4c_c1_residual_public_asset_25turn_20260911/initialization_receipt_31province.csv"
LEGACY = REPO / "src/ch5_two_asset_hank/multi_province/capital_allocation.py"
LEGACY_SHA256 = "BB3F283BD782399A5C1C9AEE06DC50BBA61A0599BF062669DE0B1EBBB01AEE40"
PAYLOAD_SHA256 = "EBB9FD91F3D3CE5D46476FE7BF1D0662E26EEA5C87357E4B13907CC76EBE9355"
PATHS = {"C": ("control_beta2", 2.0), "R": ("raw_beta2", 2.0)}
BOOTSTRAP = "BOOTSTRAP_CLIPPED_RA"
CONTROL = "CONTROL_CLIPPED_RA"
RAW = "RAW_PRIOR_COMPLETED_RA0"
PATH_VERDICT = "K1_RAW_RA0_PAYOFF_BOOTSTRAP_PATH_COMPLETED_5_TURNS"


def _sha(path: Path) -> str:
    return sha256(Path(path).read_bytes()).hexdigest().upper()


def _array_sha(value: object) -> str:
    array = np.asarray(value, dtype="<f8")
    return sha256(array.tobytes(order="C")).hexdigest().upper()


def _inputs_with_payoff(inputs: CapitalAllocationInputs, payoff: object) -> CapitalAllocationInputs:
    return CapitalAllocationInputs(
        illiquid_assets_at=inputs.illiquid_assets_at,
        population=inputs.population,
        inter_province_ratio=inputs.inter_province_ratio,
        old_firm_return_ra=payoff,
    )


def select_allocation_payoff(
    *, path_id: str, allocation_turn: int, inputs: CapitalAllocationInputs,
    prior_firms: list[tuple[Any, float]] | None,
) -> tuple[str, str, int | None, np.ndarray]:
    """Select the frozen payoff source; no fallback is permitted after bootstrap."""

    if allocation_turn <= 1:
        return BOOTSTRAP, "entering_state.ra", None, np.array(inputs.old_firm_return_ra, copy=True)
    if prior_firms is None or len(prior_firms) != 31:
        raise ValueError("prior-completed same-path firm vector is unavailable")
    if path_id == "C":
        values = np.array([firm.ra for firm, _ in prior_firms], dtype=float)
        field = "ra"
        mode = CONTROL
    elif path_id == "R":
        values = np.array([firm.ra0 for firm, _ in prior_firms], dtype=float)
        field = "ra0"
        mode = RAW
    else:
        raise ValueError("path_id must be C or R")
    if values.shape != (31,) or not np.all(np.isfinite(values)):
        raise ValueError("selected prior-completed payoff vector must be finite and 31-dimensional")
    return mode, f"same_path.completed_turn_{allocation_turn - 1}.firm.{field}", allocation_turn - 1, values


class PayoffRecorder(base.AllocationRecorder):
    def __init__(self, root: Path, config: K1ARuntimeConfig, path_id: str) -> None:
        super().__init__(root, config)
        self.path_id = path_id
        self.inputs: dict[int, CapitalAllocationInputs] = {}
        self.allocation_networks: dict[int, Any] = {}
        self.selection: dict[int, dict[str, Any]] = {}
        self.next_payoff: dict[int, dict[str, Any]] = {}

    def allocate(self, inputs: CapitalAllocationInputs):
        turn = self.calls
        if turn > 5:
            raise RuntimeError("five-turn allocation ceiling exceeded")
        prior = self.firms.get(turn - 1) if turn >= 2 else None
        mode, source, source_turn, payoff = select_allocation_payoff(
            path_id=self.path_id, allocation_turn=turn, inputs=inputs, prior_firms=prior,
        )
        if self.path_id == "C" and not np.array_equal(payoff, inputs.old_firm_return_ra):
            raise RuntimeError("Control payoff differs from entering same-path used ra")
        selected = _inputs_with_payoff(inputs, payoff)
        result = super().allocate(selected)
        self.inputs[turn] = selected
        self.allocation_networks[turn] = result.network
        self.selection[turn] = {
            "allocation_turn": turn, "payoff_mode": mode, "source": source,
            "source_completed_firm_turn": source_turn, "payoff_source_by_destination": payoff,
            "payoff_source_sha256": _array_sha(payoff),
            "portfolio_shares_sha256": _array_sha(result.network.portfolio_shares_destination_origin),
            "network_rah_by_origin": result.network.household_portfolio_return_by_origin,
        }
        base._write_json(self.root / "payoff_selection" / f"allocation_turn_{turn:02d}.json", self.selection[turn])
        return result

    def materialize_next_household_payoff(self, turn: Any) -> Any:
        """Apply a completed firm vector to this turn's already-frozen same-S network."""

        completed_turn = max(self.allocation_networks)
        if completed_turn < 1 or len(turn.firms) != 31:
            raise ValueError("completed firm turn is unavailable for next-household payoff")
        field = "ra" if self.path_id == "C" else "ra0"
        mode = CONTROL if self.path_id == "C" else RAW
        payoff = np.array([getattr(firm, field) for firm in turn.firms], dtype=float)
        if not np.all(np.isfinite(payoff)):
            raise ValueError("completed firm payoff contains NaN/Inf")
        effective = allocate_k1a_capital(_inputs_with_payoff(self.inputs[completed_turn], payoff), self.config)
        allocated = self.allocation_networks[completed_turn]
        if not np.array_equal(
            effective.network.portfolio_shares_destination_origin,
            allocated.portfolio_shares_destination_origin,
        ):
            raise RuntimeError("payoff application did not use the allocation's identical S")
        if not np.array_equal(effective.kt_supply, allocated.destination_private_productive_capital):
            raise RuntimeError("payoff-only materialization changed private-capital quantity")
        rebuilt = payoff @ allocated.portfolio_shares_destination_origin
        if not np.array_equal(rebuilt, effective.household_illiquid_return_rah):
            raise RuntimeError("same-S payoff reconstruction failed")
        self.networks[completed_turn] = effective.network
        self.next_payoff[completed_turn] = {
            "completed_firm_turn": completed_turn,
            "target_entering_household_turn": completed_turn + 1,
            "payoff_mode": mode,
            "source": f"same_path.completed_turn_{completed_turn}.firm.{field}",
            "payoff_source_field": field,
            "payoff_source_by_destination": payoff,
            "payoff_source_sha256": _array_sha(payoff),
            "portfolio_shares_sha256": _array_sha(allocated.portfolio_shares_destination_origin),
            "next_rah_by_origin": effective.household_illiquid_return_rah,
            "same_S_as_quantity": True,
            "quantity_bit_identical": True,
            "same_turn_household_feedback": False,
        }
        base._write_json(
            self.root / "payoff_application" / f"completed_turn_{completed_turn:02d}_for_entering_turn_{completed_turn + 1:02d}.json",
            self.next_payoff[completed_turn],
        )
        return replace(turn, capital=effective)


def _hjb_array_summary(turn_root: Path, index: int, province: str) -> dict[str, Any]:
    path = turn_root / "household" / f"p{index:02d}_{province}" / "hjb_return.npz"
    names = ("value", "consumption", "labor", "transfer", "adjustment_cost", "effective_illiquid_return", "mu_a", "mu_b", "utility")
    result: dict[str, Any] = {}
    total_nonfinite = 0
    with np.load(path, allow_pickle=False) as data:
        for name in names:
            array = np.asarray(data[name])
            nonfinite = int(array.size - np.count_nonzero(np.isfinite(array)))
            total_nonfinite += nonfinite
            result[f"hjb_{name}_min"] = float(np.min(array))
            result[f"hjb_{name}_max"] = float(np.max(array))
            result[f"hjb_{name}_abs_max"] = float(np.max(np.abs(array)))
            result[f"hjb_{name}_nonfinite_count"] = nonfinite
        mu_a = np.asarray(data["mu_a"], dtype=float)
        mu_b = np.asarray(data["mu_b"], dtype=float)
        result.update({
            "hjb_lower_a_outward_count": int(np.count_nonzero(mu_a[:, 0, :] < 0.0)),
            "hjb_upper_a_outward_count": int(np.count_nonzero(mu_a[:, -1, :] > 0.0)),
            "hjb_lower_b_outward_count": int(np.count_nonzero(mu_b[0, :, :] < 0.0)),
            "hjb_upper_b_outward_count": int(np.count_nonzero(mu_b[-1, :, :] > 0.0)),
        })
    result["hjb_saved_array_nonfinite_count"] = total_nonfinite
    result["hjb_kkt_diagnostic"] = "UNAVAILABLE_IN_ACCEPTED_RETURN_OBJECT"
    return result


def prepare(evidence_parent: Path, accepted_payload: Path, test_cases: int, test_processes: int) -> None:
    parent = Path(evidence_parent)
    parent.mkdir(parents=True, exist_ok=False)
    payload_bytes = Path(accepted_payload).read_bytes()
    if sha256(payload_bytes).hexdigest().upper() != PAYLOAD_SHA256:
        raise ValueError("accepted runtime payload SHA mismatch")
    payload = json.loads(payload_bytes)
    if len(payload["states"]) != 31:
        raise ValueError("accepted payload must contain 31 province states")
    protected = base.protected_science_identity()
    for path_id, (name, beta) in PATHS.items():
        root = parent / name
        root.mkdir()
        (root / "runtime_input_payload.json").write_bytes(payload_bytes)
        base._write_json(root / "phase_a_zero_science_receipt.json", {
            "schema": "CH5_K1_RAW_RA0_BOOTSTRAP_PHASE_A_V1", "status": "PASS",
            "focused_test_cases": test_cases, "focused_test_processes": test_processes,
            "scientific_processes": 0, "hjb_calls": 0, "kfe_calls": 0,
            "initialization_observations": 0, "trajectory_calls": 0,
        })
        base._write_json(root / "runtime_input_receipt.json", {
            "schema": "CH5_K1_RAW_RA0_BOOTSTRAP_RUNTIME_INPUT_V1", "path_id": path_id,
            "runtime_payload_sha256": PAYLOAD_SHA256, "province_order": PROVINCE_ORDER,
            "beta_distance": beta, "beta_return": 0.0, "turn1_mode": BOOTSTRAP,
            "turns_2_5_mode": CONTROL if path_id == "C" else RAW,
            "source_faithful_labor": True, "c1_rule": "GovInv=max(Ktarget-Kprivate,0)",
            "portfolio_smoothing": False, "partial_adjustment": False,
        })
        base._write_json(root / "bounded_invocation_receipt.json", {
            "schema": "CH5_K1_RAW_RA0_BOOTSTRAP_BOUNDED_INVOCATION_V1", "path_id": path_id,
            "trajectory_invocations_maximum": 1, "outer_turns_maximum": 5,
            "province_hjb_calls_maximum": 155, "province_kfe_calls_maximum": 155,
            "scientific_retries": 0, "matlab_calls": 0, "standalone_kfe_experiments": 0,
            "k1b_runs": 0, "k2_runs": 0, "ge_calls": 0, "annual_calls": 0,
            "irf_calls": 0, "results_calls": 0,
        })
    base._write_json(parent / "prepare_receipt.json", {
        "schema": "CH5_K1_RAW_RA0_BOOTSTRAP_PREPARE_V1", "status": "PASS",
        "path_roots": {key: name for key, (name, _) in PATHS.items()},
        "runtime_payload_sha256": PAYLOAD_SHA256, "payloads_byte_identical": True,
        "initial_state_ra0_count": sum("ra0" in state for state in payload["states"]),
        "initial_state_ra_count": sum("ra" in state for state in payload["states"]),
        "scientific_calls": 0,
    })
    base._write_json(parent / "protected_source_identity_receipt.json", protected)


def preflight(evidence_parent: Path) -> None:
    parent = Path(evidence_parent)
    roots = [parent / PATHS[key][0] for key in ("C", "R")]
    if roots[0].joinpath("runtime_input_payload.json").read_bytes() != roots[1].joinpath("runtime_input_payload.json").read_bytes():
        raise ValueError("C/R starting payloads are not byte-identical")
    if any(root.joinpath("science_started.json").exists() for root in roots):
        raise ValueError("science already started")
    payload = json.loads(roots[0].joinpath("runtime_input_payload.json").read_text(encoding="utf-8"))
    if sum("ra0" in state for state in payload["states"]) != 0 or sum("ra" in state for state in payload["states"]) != 31:
        raise ValueError("accepted initialization/bootstrap identity mismatch")
    if _sha(LEGACY) != LEGACY_SHA256:
        raise ValueError("legacy allocator changed")
    base.protected_science_identity()
    distance = load_accepted_distance_score(DISTANCE)
    config = K1ARuntimeConfig(PROVINCE_ORDER, distance, 2.0)
    probe = CapitalAllocationInputs(np.linspace(1, 2, 31), np.linspace(10, 20, 31),
                                    np.linspace(0.1, 0.3, 31), np.linspace(0.02, 0.09, 31))
    c1_result = allocate_k1a_capital(probe, config)
    raw = np.linspace(0.1, 1.0, 31)
    raw_result = allocate_k1a_capital(_inputs_with_payoff(probe, raw), config)
    if not np.array_equal(c1_result.network.portfolio_shares_destination_origin,
                          raw_result.network.portfolio_shares_destination_origin):
        raise RuntimeError("payoff source changed S")
    if not np.array_equal(c1_result.kt_supply, raw_result.kt_supply):
        raise RuntimeError("payoff source changed quantities")
    if not np.array_equal(raw_result.household_illiquid_return_rah,
                          raw @ raw_result.network.portfolio_shares_destination_origin):
        raise RuntimeError("raw same-S payoff identity failed")
    c1_text = (REPO / "src/ch5_two_asset_hank/multi_province/c1_residual_public_asset.py").read_text(encoding="utf-8")
    if "reconstruct_migration_labor" not in c1_text or "residual_government_asset_levels" not in c1_text:
        raise RuntimeError("source-faithful labor or C1 marker missing")
    gate = {
        "schema": "CH5_K1_RAW_RA0_BOOTSTRAP_PRE_RUN_GATE_V1", "status": "PASS",
        "live_baseline": base._git_text("rev-parse", "HEAD"),
        "payloads_byte_identical": True, "accepted_initialization_ra0_count": 0,
        "accepted_initialization_ra_count": 31, "owner_bootstrap_freeze_active": True,
        "turn1_both_modes": BOOTSTRAP, "control_turn2_source": "same_path.completed_turn_1.firm.ra",
        "raw_turn2_source": "same_path.completed_turn_1.firm.ra0",
        "same_S_static_identity": True, "quantity_bit_identical_under_payoff_switch": True,
        "beta_distance_both": 2.0, "beta_return_both": 0.0, "k1b_disabled": True,
        "source_faithful_labor": True, "c1_formula_unchanged": True,
        "raw_payoff_unclipped_unscaled_unnormalized_unannualized_unsmoothed": True,
        "outer_turn_ceiling": 5, "science_calls_before_gate": 0,
    }
    base._write_json(parent / "pre_run_gate.json", gate)
    for root in roots:
        shutil.copyfile(parent / "pre_run_gate.json", root / "pre_run_gate.json")


def execute(evidence_parent: Path, path_id: str) -> int:
    global_active: dict[str, PayoffRecorder] = {}
    path_id = path_id.upper()
    if path_id not in PATHS:
        raise ValueError("path_id must be C or R")
    parent = Path(evidence_parent)
    gate = json.loads((parent / "pre_run_gate.json").read_text(encoding="utf-8"))
    if gate.get("status") != "PASS" or gate.get("science_calls_before_gate") != 0:
        raise ValueError("pre-run gate is missing or failed")

    originals = {
        "paths": base.PATHS, "recorder": base.AllocationRecorder,
        "augment": base._augment_turn_rows, "g1_write": g1.write_json,
        "c1_source_post": c1._SOURCE_POST_TURN,
        "g1_range_present": "range" in g1.__dict__, "g1_range": g1.__dict__.get("range"),
    }
    original_augment = base._augment_turn_rows
    original_post = c1._SOURCE_POST_TURN

    def recorder_factory(root: Path, config: K1ARuntimeConfig) -> PayoffRecorder:
        recorder = PayoffRecorder(root, config, path_id)
        global_active["recorder"] = recorder
        return recorder

    def bounded_range(*args: int):
        return builtins.range(1, 6) if args == (1, 26) else builtins.range(*args)

    def payoff_post(states, batch, turn):
        effective_turn = global_active["recorder"].materialize_next_household_payoff(turn)
        return original_post(states, batch, effective_turn)

    def augment(rows: list[dict[str, Any]], recorder: PayoffRecorder, turn: int) -> None:
        original_augment(rows, recorder, turn)
        application = recorder.next_payoff[turn]
        selection = recorder.selection[turn]
        turn_root = recorder.root / f"turn_{turn:02d}"
        for index, row in enumerate(rows):
            row.update({
                "entering_payoff_mode": BOOTSTRAP if turn == 1 else recorder.next_payoff[turn - 1]["payoff_mode"],
                "allocation_payoff_mode": selection["payoff_mode"],
                "allocation_payoff_source_destination": float(selection["payoff_source_by_destination"][index]),
                "next_payoff_mode": application["payoff_mode"],
                "next_payoff_source_field": application["payoff_source_field"],
                "next_payoff_source_destination": float(application["payoff_source_by_destination"][index]),
                "next_network_rah": float(application["next_rah_by_origin"][index]),
                "payoff_source_completed_firm_turn": application["completed_firm_turn"],
                "payoff_targets_entering_household_turn": application["target_entering_household_turn"],
                "same_turn_household_feedback": False,
                "portfolio_shares_sha256": application["portfolio_shares_sha256"],
            })
            row.update(_hjb_array_summary(turn_root, index, str(row["province"])))

    def task_write_json(path: Path, value: Any) -> None:
        recorder = global_active.get("recorder")
        if path.name == "entering_state.json" and isinstance(value, dict) and recorder is not None:
            turn = int(value["turn"])
            if turn == 1:
                value["payoff_mode"] = BOOTSTRAP
                value["payoff_provenance"] = "accepted_initialization.rah; turn1 allocation selects accepted entering ra"
            else:
                prior = recorder.next_payoff[turn - 1]
                expected = np.asarray(prior["next_rah_by_origin"], dtype=float)
                actual = np.array([float(state["rah"]) for state in value["states"]])
                if not np.array_equal(actual, expected):
                    raise ValueError("entering rah differs from prior completed same-path payoff application")
                value["rah_provenance"] = [{
                    "entering_state_field": "rah",
                    "source": prior["source"],
                    "formula": f"{prior['payoff_source_field']}_by_destination @ S_destination_origin",
                    "payoff_mode": prior["payoff_mode"],
                    "source_completed_firm_turn": turn - 1,
                    "quantity_and_rah_same_S": True,
                    "value": float(actual[index]),
                    "manual_override": False,
                    "same_turn_household_feedback": False,
                } for index in range(31)]
                value["payoff_mode"] = prior["payoff_mode"]
                value["payoff_provenance"] = prior["source"]
                value["source_completed_firm_turn"] = turn - 1
                value["payoff_source_sha256"] = prior["payoff_source_sha256"]
                value["portfolio_shares_sha256"] = prior["portfolio_shares_sha256"]
                value["same_S_as_quantity"] = True
                value["same_turn_household_feedback"] = False
        elif path.name == "science_started.json" and isinstance(value, dict):
            value.update({"schema": "CH5_K1_RAW_RA0_BOOTSTRAP_SCIENCE_STARTED_V1",
                          "authorized_turns_maximum": 5, "authorized_province_updates_maximum": 155,
                          "path_id": path_id, "turn1_mode": BOOTSTRAP})
        elif path.name == "transition_summary.json" and isinstance(value, dict):
            value.update({"schema": "CH5_K1_RAW_RA0_BOOTSTRAP_TRANSITION_V1",
                          "turn5_completed": value.get("actual_turns_completed") == 5,
                          "turn25_completed": False,
                          "termination_reason": "AUTHORIZED_5_TURN_CEILING_REACHED"})
        elif path.name == "call_ledger.json" and isinstance(value, dict):
            counts = value["counts"]
            if counts["hjb_calls"] > 155 or counts["kfe_calls"] > 155:
                raise RuntimeError("per-path HJB/KFE ceiling exceeded")
            value.update({"schema": "CH5_K1_RAW_RA0_BOOTSTRAP_CALL_LEDGER_V1",
                          "path_id": path_id, "trajectory_invocations": 1,
                          "outer_turn_ceiling": 5, "hjb_ceiling": 155, "kfe_ceiling": 155,
                          "engineering_retries": 1 if path_id == "C" else 0,
                          "k1b_runs": 0, "k2_runs": 0})
        elif path.name == "terminal_result.json" and isinstance(value, dict):
            if value.get("actual_turns_completed") == 5 and value.get("error") is None:
                value["verdict"] = PATH_VERDICT
                value["termination_reason"] = "AUTHORIZED_5_TURN_CEILING_REACHED"
            value.update({"schema": "CH5_K1_RAW_RA0_BOOTSTRAP_TERMINAL_V1",
                          "path_id": path_id, "turn1_bootstrap": True,
                          "raw_treatment_turns": [2, 3, 4, 5] if path_id == "R" else [],
                          "results_eligible": False})
        originals["g1_write"](path, value)

    try:
        base.PATHS = PATHS
        base.AllocationRecorder = recorder_factory
        base._augment_turn_rows = augment
        g1.write_json = task_write_json
        c1._SOURCE_POST_TURN = payoff_post
        g1.range = bounded_range
        code = base.execute(parent, path_id)
    finally:
        base.PATHS = originals["paths"]
        base.AllocationRecorder = originals["recorder"]
        base._augment_turn_rows = originals["augment"]
        g1.write_json = originals["g1_write"]
        c1._SOURCE_POST_TURN = originals["c1_source_post"]
        if originals["g1_range_present"]:
            g1.range = originals["g1_range"]
        else:
            delattr(g1, "range")
    terminal = json.loads((parent / PATHS[path_id][0] / "terminal_result.json").read_text(encoding="utf-8"))
    return 0 if terminal.get("actual_turns_completed") == 5 and terminal.get("error") is None else code


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
    launch.add_argument("path_id", choices=("C", "R"))
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
