"""Repair gate, 1,227-map historical parity, and one bounded turn4 reexecution."""
from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from typing import Any, Callable, Mapping

import numpy as np

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPOSITORY_ROOT))
sys.path.insert(0, str(REPOSITORY_ROOT / "src"))

from ch5_two_asset_hank.corrected_diagnostic import nonlinear_continuation as nlc
from ch5_two_asset_hank.corrected_diagnostic import optionb_initial_turn_integration as turn1
from ch5_two_asset_hank.corrected_diagnostic import optionb_turn2_household_integration as base
from ch5_two_asset_hank.corrected_diagnostic.contracts import CorrectedDiagnosticGrid
from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import FailClosed
from ch5_two_asset_hank.corrected_diagnostic.selector import (
    CellDerivatives,
    CorrectedSelectorCell,
    CorrectedSelectorParameters,
    SelectorBudget,
    select_constrained_policy,
)
from ch5_two_asset_hank.multi_province.one_turn import PreFrozenHouseholdOutputBatch
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER
from validators.multi_province.k1b_turn3_corrected_household_kfe_and_one_turn_integration import run as turn3
from validators.multi_province.k1b_turn4_corrected_household_kfe_and_one_turn_integration import run as prior_turn4
from validators.multi_province.turn2_f0364_negative_ratio_switching_forensic import run as beijing


TASK_ID = "CH5_MP4C_K1B_TURN4_ANHUI_F0364_POSITIVE_DOMAIN_INTERSECTION_REPAIR_HISTORICAL_PARITY_AND_REEXECUTION_20260921"
BASELINE = "1843bd413ee019b04c6937abd1e89cf044e62241"
PASS_TERMINAL = (
    "PASS__ANHUI_F0364_POSITIVE_DOMAIN_INTERSECTION_REPAIR__HISTORICAL_POLICY_"
    "PARITY_PASS__K1B_TURN4_31_PROVINCE_HJB_KFE_AND_ONE_INTEGRATION__TURN5_"
    "K1B_INPUT_READY__TURN5_NOT_RUN"
)
BLOCKED_FOCUSED = "BLOCKED__ANHUI_F0364_POSITIVE_DOMAIN_INTERSECTION_REPAIR__FOCUSED_PARITY_FAILED"
BLOCKED_HISTORY = "BLOCKED__ANHUI_F0364_POSITIVE_DOMAIN_INTERSECTION_REPAIR__HISTORICAL_POLICY_IDENTITY_MISMATCH"

OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_k1b_turn4_anhui_f0364_positive_domain_intersection_repair_reexecution_20260921_run001"
)
TASK_RELATIVE = Path(
    "tasks/CH5_MP4C_K1B_TURN4_ANHUI_F0364_POSITIVE_DOMAIN_INTERSECTION_REPAIR_HISTORICAL_PARITY_AND_REEXECUTION_20260921.md"
)
SELECTOR_RELATIVE = Path("src/ch5_two_asset_hank/corrected_diagnostic/selector.py")
TEST_RELATIVE = Path("tests/test_mp4c_k1b_turn4_anhui_f0364_positive_domain_intersection_repair.py")
RUNNER_RELATIVE = Path(
    "validators/multi_province/k1b_turn4_anhui_f0364_positive_domain_intersection_repair/run.py"
)
ANHUI_CELL = Path(
    "reports/ch5_mp4c_k1b_turn4_corrected_household_kfe_and_one_turn_integration_20260921_run001/"
    "household/p11_安徽/checkpoint_004/cell_0364.json"
)

TURN1_ROOT = Path("reports/ch5_mp4c_corrected_optionb_initial_turn_unique_closed_class_kfe_20260920_run004")
TURN2_ROOT = Path("reports/ch5_mp4c_monotonicity_preserving_hjb_relaxation_fresh_turn2_run005_20260921")
TURN3_ROOT = Path("reports/ch5_mp4c_k1b_turn3_corrected_household_kfe_and_one_turn_integration_20260921_run001")
MANIFESTS = {
    "turn1_run004": (TURN1_ROOT, "CF70E7D6A62A35F461D1A75B28F8F502B2CBDD2D94ED5D9DDFA099D821CC5EC6", 4353),
    "turn2_run005": (TURN2_ROOT, "C93BF19DB7C909A50C2753B0EA06FD4735F48A4C41C5A4C9CA6F8817B693B72F", 4752),
    "turn3_accepted": (TURN3_ROOT, "776F348F4BBF36587E2B484A10A00F96F6D01689322207A52A3770B93CDC03D9", 4724),
}
EXPECTED_MAPS = {"turn1_run004": 408, "turn2_run005": 411, "turn3_accepted": 408}

PARAMETERS = CorrectedSelectorParameters(2.0, 5.0, 1.0, 0.1, 2.0, 1.0e-6)


def git(repository: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repository, text=True).strip()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def write_json(path: Path, payload: Any) -> None:
    base._write_json(path, payload)


def verify_manifest(root: Path, expected_sha: str, expected_entries: int) -> dict[str, Any]:
    manifest_path = root / "sealed_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bad = []
    for row in manifest["entries"]:
        target = root / row["path"]
        if not target.is_file() or target.stat().st_size != int(row["bytes"]) or sha256(target) != row["sha256"]:
            bad.append(row["path"])
    readback = json.loads((root / "independent_readback_receipt.json").read_text(encoding="utf-8"))
    checks = {
        "manifest_sha256": sha256(manifest_path) == expected_sha,
        "entry_count": int(manifest["entry_count"]) == expected_entries,
        "all_entries_read_back": not bad,
        "accepted_readback": readback.get("status") == "PASS" and not readback.get("bad_paths"),
    }
    receipt = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "root": root.name,
        "manifest_sha256": sha256(manifest_path),
        "entry_count": int(manifest["entry_count"]),
        "total_bytes": int(manifest["total_bytes"]),
        "checks": checks,
        "bad_paths": bad,
    }
    if receipt["status"] != "PASS":
        raise FailClosed("BLOCKED__ACCEPTED_PREDECESSOR_MANIFEST_MISMATCH", receipt)
    return receipt


def inventory(repository: Path, root: Path) -> list[dict[str, Any]]:
    rows = []
    household = repository / root / "household"
    for province_index, province in enumerate(PROVINCE_ORDER):
        province_root = household / f"p{province_index:02d}_{province}"
        for directory in sorted(province_root.glob("checkpoint_[0-9][0-9][0-9]")):
            manifest_path = directory / "checkpoint_manifest.json"
            arrays_path = directory / "checkpoint_arrays.npz"
            if not manifest_path.is_file() or not arrays_path.is_file():
                continue
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            checkpoint = int(directory.name.rsplit("_", 1)[1])
            if int(manifest["province_index"]) != province_index or manifest["province"] != province or int(manifest["checkpoint"]) != checkpoint:
                raise FailClosed("BLOCKED__HISTORICAL_MAP_ORDER_MISMATCH", {"path": manifest_path.as_posix()})
            rows.append({
                "province_index": province_index,
                "province": province,
                "checkpoint": checkpoint,
                "directory": directory,
                "accepted_policy_identity": manifest["policy_identity_sha256"],
                "accepted_value_sha256": manifest["value_sha256"],
            })
    return rows


def anhui_cell(repository: Path) -> CorrectedSelectorCell:
    payload = json.loads((repository / ANHUI_CELL).read_text(encoding="utf-8"))
    raw = payload["selector_cell"]
    names = (
        "cell_id", "b", "a", "z", "b_lower", "b_upper", "a_lower", "a_upper",
        "net_wage", "effective_r_b", "transfer_income", "effective_r_a",
    )
    return CorrectedSelectorCell(
        **{name: raw[name] for name in names},
        derivatives=CellDerivatives(**raw["derivatives"]),
    )


def selector_once(cell: CorrectedSelectorCell, parameters: CorrectedSelectorParameters) -> tuple[Any, SelectorBudget]:
    budget = SelectorBudget(1, 0, 0, 0, 0)
    return select_constrained_policy(cell, parameters, budget=budget), budget


def focused_parity(repository: Path) -> dict[str, Any]:
    ah_result, ah_budget = selector_once(anhui_cell(repository), PARAMETERS)
    _, bj_cell, bj_binding = beijing.load_cell(repository)
    bj_result, bj_budget = selector_once(bj_cell, beijing.PARAMETERS)
    ah = ah_result.selected
    bj = bj_result.selected
    ah_checks = {
        "selected_unique_switching": ah is not None and ah_result.outcome == "SELECTED_ADMISSIBLE"
        and sum(row.interior_a_switching_receipt is not None for row in ah_result.candidates) == 1,
        "branches": ah is not None and ah.derivative_branches == {"b": "backward", "a": "zero"},
        "q_b": ah is not None and ah.q_b == 0.0015039676061569449,
        "q_a": ah is not None and ah.q_a == -0.0005008835855672058,
        "d": ah is not None and ah.d == -5.840722762648187,
        "g_a": ah is not None and ah.g_a == 0.0,
        "g_b": ah is not None and ah.g_b == -17.978717494437753,
        "kkt_within_existing_arithmetic_tolerance": ah is not None
        and ah.transfer_kkt_residual is not None and ah.arithmetic_tolerance is not None
        and ah.transfer_kkt_residual <= ah.arithmetic_tolerance,
        "hamiltonian": ah is not None and ah.hamiltonian == -0.06734914681687235,
        "admissible": ah is not None and ah.admissible and not ah.rejection_reasons,
        "no_root": ah_budget.root_invocations == 0,
    }
    bj_checks = {
        "cell_binding": all(bj_binding.values()),
        "selected": bj is not None and bj_result.outcome == "SELECTED_ADMISSIBLE",
        "branches": bj is not None and bj.derivative_branches == {"b": "backward", "a": "zero"},
        "q_b": bj is not None and bj.q_b == 0.006091715618507631,
        "q_a": bj is not None and bj.q_a == -0.0045978913784868415,
        "d": bj is not None and bj.d == -7.8384208979658965,
        "g_a": bj is not None and bj.g_a == 0.0,
        "g_b": bj is not None and bj.g_b == -4.227123020026542,
        "kkt": bj is not None and bj.transfer_kkt_residual == 0.0,
        "hamiltonian": bj is not None and bj.hamiltonian == -0.11188508398929994,
        "no_root": bj_budget.root_invocations == 0,
    }
    status = "PASS" if all(ah_checks.values()) and all(bj_checks.values()) else "FAIL"
    return {
        "status": status,
        "anhui": {"checks": ah_checks, "selected": None if ah is None else asdict(ah),
                  "raw_kkt_residual": None if ah is None else ah.transfer_kkt_residual},
        "beijing": {"checks": bj_checks, "selected": None if bj is None else asdict(bj)},
        "selector_evaluations": ah_budget.selector_evaluations + bj_budget.selector_evaluations,
        "root_invocations": ah_budget.root_invocations + bj_budget.root_invocations,
    }


def replay_turn(
    repository: Path,
    label: str,
    rows: list[dict[str, Any]],
    states: tuple[dict[str, Any], ...],
    province_inputs: Callable[[Path, Mapping[str, Any], np.ndarray, CorrectedDiagnosticGrid], Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    expected = EXPECTED_MAPS[label]
    if len(rows) != expected:
        raise FailClosed("BLOCKED__HISTORICAL_MAP_COUNT_MISMATCH", {"turn": label, "expected": expected, "actual": len(rows)})
    native_grid = base.oracle.MatlabFaithfulHJBGrid(
        np.linspace(-2, 5, 20), np.linspace(0, 10, 20), np.array([0.8, 1.3]),
        np.array([[-1 / 3, 1 / 3], [1 / 3, -1 / 3]]),
    )
    grid = CorrectedDiagnosticGrid(native_grid.b, native_grid.a, native_grid.z)
    budget = SelectorBudget(expected * 800, 20_000_000, expected * 800, expected * 800, expected * 800)
    accepted_ids, replayed_ids, map_rows, mismatches = [], [], [], []
    for ordinal, row in enumerate(rows):
        directory = Path(row["directory"])
        with np.load(directory / "checkpoint_arrays.npz", allow_pickle=False) as payload:
            value = np.asarray(payload["value"], dtype=np.float64)
        value_sha = nlc._field_sha256(value)
        inputs = province_inputs(repository, states[int(row["province_index"])], value, grid)
        fields = nlc.raw_derivative_fields(value, grid)
        identities = []
        error = None
        for flat, index in enumerate(nlc.iter_f_order_indices(nlc.SHAPE)):
            try:
                derivatives, _ = nlc.boundary_cell_derivatives(fields, index, grid)
                cell = nlc._cell(inputs, index, derivatives, int(row["checkpoint"]), flat)
                result = select_constrained_policy(cell, inputs.parameters, budget=budget)
                if result.outcome != "SELECTED_ADMISSIBLE" or result.selected is None:
                    error = {"flat": flat, "index": list(index), "outcome": result.outcome}
                    break
                identities.append(nlc._selected_identity(asdict(result.selected)))
            except Exception as exc:
                error = {"flat": flat, "index": list(index), "exception": type(exc).__name__, "message": str(exc)}
                break
        replayed = nlc._canonical_sha256(identities) if error is None and len(identities) == nlc.N else None
        accepted = str(row["accepted_policy_identity"])
        matched = value_sha == row["accepted_value_sha256"] and replayed == accepted
        receipt = {
            "map_ordinal": ordinal, "province_index": row["province_index"], "province": row["province"],
            "checkpoint": row["checkpoint"], "accepted_value_sha256": row["accepted_value_sha256"],
            "replayed_value_sha256": value_sha, "accepted_policy_identity": accepted,
            "replayed_policy_identity": replayed, "exact_match": matched, "error": error,
        }
        map_rows.append(receipt)
        accepted_ids.append(accepted)
        replayed_ids.append(replayed or "MISSING")
        if not matched:
            mismatches.append(receipt)
            break
    exact = len(map_rows) == expected and budget.selector_evaluations == expected * 800 and not mismatches
    receipt = {
        "status": "PASS" if exact else "FAIL", "turn": label, "maps_replayed": len(map_rows),
        "exact_matches": len(map_rows) - len(mismatches), "mismatch_count": len(mismatches),
        "mismatches": mismatches, "first_mismatch_stop": bool(mismatches),
        "accepted_ordered_policy_digest": nlc._canonical_sha256(accepted_ids),
        "replayed_ordered_policy_digest": nlc._canonical_sha256(replayed_ids),
        "ordered_map_receipts": map_rows,
    }
    ledger = {
        "policy_maps_replayed": len(map_rows), "selector_evaluations": budget.selector_evaluations,
        "scalar_root_invocations": budget.root_invocations,
        "interior_z_root_invocations": budget.interior_z_root_invocations,
        "interior_a_switching_root_invocations": budget.interior_a_switching_root_invocations,
        "joint_switching_root_invocations": budget.joint_switching_root_invocations,
        "hjb_direct_solves_or_updates": 0, "d2_q": 0, "kfe_svd": 0,
        "aggregate_integration": 0, "retry_tuning": 0,
    }
    return receipt, ledger


def source_freeze(repository: Path) -> dict[str, str]:
    paths = list((repository / "src/ch5_two_asset_hank/corrected_diagnostic").glob("*.py"))
    paths.extend(repository / path for path in (TEST_RELATIVE, RUNNER_RELATIVE, TASK_RELATIVE))
    return {path.relative_to(repository).as_posix(): sha256(path) for path in sorted(set(paths))}


def capture_anhui_runtime(output: Path) -> tuple[Callable[..., Any], dict[str, Any]]:
    original = base._map_checkpoint
    state: dict[str, Any] = {"capture_count": 0, "receipt": None}

    def wrapped(*args, **kwargs):
        result = original(*args, **kwargs)
        checkpoint = int(args[2])
        province_root = Path(args[1])
        if checkpoint == 4 and province_root.name == "p11_安徽":
            cell_path = province_root / "checkpoint_004/cell_0364.json"
            payload = json.loads(cell_path.read_text(encoding="utf-8"))
            selected = payload["selector_result"].get("selected")
            same_derivatives = payload["selector_cell"]["derivatives"] == {
                "p_a_backward": 8.895604077208148e-05,
                "p_a_forward": -0.000536125311776913,
                "p_b_backward": 0.0015039676061569449,
                "p_b_forward": 0.008487587452625978,
            }
            checks = {
                "same_derivatives": same_derivatives,
                "selected": selected is not None and payload["selector_result"]["outcome"] == "SELECTED_ADMISSIBLE",
                "branches": selected is not None and selected["derivative_branches"] == {"a": "zero", "b": "backward"},
                "q_b": selected is not None and selected["q_b"] == 0.0015039676061569449,
                "q_a": selected is not None and selected["q_a"] == -0.0005008835855672058,
                "d": selected is not None and selected["d"] == -5.840722762648187,
                "g_a": selected is not None and selected["g_a"] == 0.0,
                "g_b": selected is not None and selected["g_b"] == -17.978717494437753,
                "kkt_within_tolerance": selected is not None
                and selected["transfer_kkt_residual"] <= selected["arithmetic_tolerance"],
                "hamiltonian": selected is not None and selected["hamiltonian"] == -0.06734914681687235,
            }
            receipt = {"status": "PASS" if all(checks.values()) else "FAIL", "checks": checks,
                       "source": cell_path.as_posix(), "selected": selected,
                       "no_additional_selector_call": True}
            write_json(output / "anhui_f0364_in_path_repair_parity_receipt.json", receipt)
            state.update({"capture_count": 1, "receipt": receipt})
            if receipt["status"] != "PASS":
                raise FailClosed("FAIL__ANHUI_F0364_IN_PATH_REPAIR_PARITY_MISMATCH", receipt)
        return result

    return wrapped, state


def combined_history(turn_receipts: dict[str, dict[str, Any]], ledgers: dict[str, dict[str, Any]]) -> tuple[dict[str, Any], dict[str, Any]]:
    total_maps = sum(row["maps_replayed"] for row in turn_receipts.values())
    total_exact = sum(row["exact_matches"] for row in turn_receipts.values())
    total_evaluations = sum(row["selector_evaluations"] for row in ledgers.values())
    mismatch = [item for row in turn_receipts.values() for item in row["mismatches"]]
    accepted = [turn_receipts[label]["accepted_ordered_policy_digest"] for label in turn_receipts]
    replayed = [turn_receipts[label]["replayed_ordered_policy_digest"] for label in turn_receipts]
    status = "PASS" if total_maps == total_exact == 1227 and total_evaluations == 981_600 and not mismatch else "FAIL"
    receipt = {
        "status": status, "maps_replayed": total_maps, "exact_matches": total_exact,
        "selector_evaluations": total_evaluations, "mismatch_count": len(mismatch), "mismatches": mismatch,
        "accepted_ordered_turn_digest": nlc._canonical_sha256(accepted),
        "replayed_ordered_turn_digest": nlc._canonical_sha256(replayed),
    }
    ledger = {
        "policy_maps_replayed": total_maps, "selector_evaluations": total_evaluations,
        "scalar_root_invocations": sum(row["scalar_root_invocations"] for row in ledgers.values()),
        "interior_z_root_invocations": sum(row["interior_z_root_invocations"] for row in ledgers.values()),
        "interior_a_switching_root_invocations": sum(row["interior_a_switching_root_invocations"] for row in ledgers.values()),
        "joint_switching_root_invocations": sum(row["joint_switching_root_invocations"] for row in ledgers.values()),
        "hjb_direct_solves_or_updates": 0, "d2_q": 0, "kfe_svd": 0,
        "aggregate_integration": 0, "retry_tuning": 0,
    }
    return receipt, ledger


def finalize(
    repository: Path, output: Path, pre_freeze: dict[str, str], scientific_ledger: dict[str, Any],
    relaxation: dict[str, Any], terminal: str, detail: dict[str, Any], started: float,
) -> str:
    for key in (
        "authorized_k1b_turn4_household_batches",
        "frozen_k1b_turn4_quantity_allocations",
        "completed_turn4_raw_ra0_vectors",
        "deterministic_turn5_k1b_preparations",
        "turn4_household_calls",
        "fourth_outer_turns",
        "turn5_household_calls",
    ):
        scientific_ledger.setdefault(key, 0)
    post_freeze = source_freeze(repository)
    if post_freeze != pre_freeze:
        terminal = "BLOCKED__SCIENTIFIC_CODE_CHANGED_AFTER_FREEZE"
        detail = {"prior_detail": detail}
    prior_turn4.task_ledger_check(scientific_ledger, relaxation)
    scientific_ledger["wall_seconds"] = float(time.perf_counter() - started)
    scientific_ledger["terminal_verdict"] = terminal
    write_json(output / "scientific_ledger.json", scientific_ledger)
    write_json(output / "relaxation_arithmetic_ledger.json", relaxation)
    write_json(output / "reached_province_hjb_kfe_status.json", prior_turn4.reached_province_status(output, terminal, detail))
    write_json(output / "post_execution_code_freeze.json", {
        "status": "PASS" if post_freeze == pre_freeze else "FAIL",
        "source_sha256_after": post_freeze, "matches_pre_execution_freeze": post_freeze == pre_freeze,
    })
    write_json(output / "terminal_receipt.json", {
        "terminal_verdict": terminal, "detail": detail, "turn5_household_run": False,
        "k2": 0, "matlab": 0, "ge_results": 0, "successor_published": False,
        "results_eligibility": False,
    })
    base._manifest(output)
    base._readback(output)
    return terminal


def execute(repository: Path, focused_test_junit: Path) -> str:
    repository = repository.resolve(strict=True)
    output = repository / OUTPUT_RELATIVE
    if output.exists():
        raise FailClosed("BLOCKED__FRESH_EVIDENCE_ROOT_ALREADY_EXISTS", {"path": output.as_posix()})
    started = time.perf_counter()
    focused_tests = base._read_junit(focused_test_junit)
    manifests = {
        label: verify_manifest(repository / root, expected_sha, expected_entries)
        for label, (root, expected_sha, expected_entries) in MANIFESTS.items()
    }
    focused = focused_parity(repository)
    states1, binding1 = turn1.load_initial_states(repository)
    states2, binding2 = base.load_initial_states(repository)
    states3, _, binding3 = turn3.load_entering_and_shares(repository)
    states4, frozen_shares, entering4 = prior_turn4.load_entering_and_shares(repository)
    prior_turn4.load_prior_diagnostics(repository)
    inventories = {label: inventory(repository, root) for label, (root, _, _) in MANIFESTS.items()}
    startup = {
        "origin_main_exact_baseline": git(repository, "rev-parse", "origin/main") == BASELINE,
        "baseline_is_ancestor": subprocess.run(["git", "merge-base", "--is-ancestor", BASELINE, "HEAD"], cwd=repository).returncode == 0,
        "selector_pre_repair_blob": git(repository, "rev-parse", f"{BASELINE}:{SELECTOR_RELATIVE.as_posix()}") == "e8a1d72e23661576f14ac42b7dff6e3001837206",
        "focused_tests": focused_tests["status"] == "PASS",
        "focused_selector_parity": focused["status"] == "PASS",
        "accepted_manifests": all(row["status"] == "PASS" for row in manifests.values()),
        "map_counts": {label: len(rows) for label, rows in inventories.items()} == EXPECTED_MAPS,
        "turn4_entering_and_share_binding": entering4["status"] == "PASS",
    }
    output.mkdir(parents=True, exist_ok=False)
    write_json(output / "authority_source_binding.json", {
        "status": "PASS" if all(startup.values()) else "FAIL", "task_id": TASK_ID,
        "baseline": BASELINE, "execution_head": git(repository, "rev-parse", "HEAD"),
        "checks": startup, "manifests": manifests,
    })
    write_json(output / "focused_test_receipt.json", focused_tests)
    write_json(output / "focused_anhui_beijing_selector_parity.json", focused)
    write_json(output / "selector_diff_contract.json", {
        "status": "PASS", "scope": "INTERIOR_B_INTERIOR_A_STRICT_CROSSING_FINITE_NEGATIVE_NONZERO_R",
        "mapped_interval": "PRESERVED", "q_b_domain": "OPEN_POSITIVE_INTERSECTION_AND_BRANCH_MEMBERSHIP",
        "q_a_domain": "ORIGINAL_CLOSED_ILLIQUID_DERIVATIVE_INTERVAL",
        "positive_ratio": "UNCHANGED", "active_liquid_negative_ratio": "UNCHANGED_FAIL_CLOSED",
        "ratio_zero": "UNCHANGED_FAIL_CLOSED", "downstream_rules": "UNCHANGED",
    })
    if not all(startup.values()):
        write_json(output / "terminal_receipt.json", {"terminal_verdict": BLOCKED_FOCUSED, "detail": startup})
        base._manifest(output); base._readback(output)
        return BLOCKED_FOCUSED

    pre_freeze = source_freeze(repository)
    write_json(output / "pre_execution_code_freeze.json", {"status": "PASS", "source_sha256_before": pre_freeze})
    write_json(output / "historical_entering_state_bindings.json", {
        "turn1": binding1, "turn2": binding2, "turn3": binding3,
    })
    turn_receipts, history_ledgers = {}, {}
    replay_specs = (
        ("turn1_run004", states1, turn1._province_inputs),
        ("turn2_run005", states2, base._province_inputs),
        ("turn3_accepted", states3, base._province_inputs),
    )
    for label, states, inputs in replay_specs:
        receipt, ledger = replay_turn(repository, label, inventories[label], states, inputs)
        turn_receipts[label], history_ledgers[label] = receipt, ledger
        write_json(output / f"{label}_historical_policy_identity_receipt.json", receipt)
        write_json(output / f"{label}_historical_replay_ledger.json", ledger)
        if receipt["status"] != "PASS":
            combined, combined_ledger = combined_history(turn_receipts, history_ledgers)
            write_json(output / "combined_1227_map_historical_policy_identity_receipt.json", combined)
            write_json(output / "combined_historical_replay_ledger.json", combined_ledger)
            return finalize(repository, output, pre_freeze, base._new_ledger(), prior_turn4.new_relaxation_ledger(),
                            BLOCKED_HISTORY, {"failed_turn": label, "mismatch": receipt["mismatches"]}, started)
    combined, combined_ledger = combined_history(turn_receipts, history_ledgers)
    write_json(output / "combined_1227_map_historical_policy_identity_receipt.json", combined)
    write_json(output / "combined_historical_replay_ledger.json", combined_ledger)
    if combined["status"] != "PASS":
        return finalize(repository, output, pre_freeze, base._new_ledger(), prior_turn4.new_relaxation_ledger(),
                        BLOCKED_HISTORY, combined, started)

    base.TASK_RELATIVE = TASK_RELATIVE
    base.ENTERING_STATE_RELATIVE = prior_turn4.ENTERING_RELATIVE
    write_json(output / "fresh_turn4_entering_state_and_share_binding.json", entering4)
    scientific_ledger = base._new_ledger()
    scientific_ledger.update({
        "authorized_k1b_turn4_household_batches": 0,
        "frozen_k1b_turn4_quantity_allocations": 0,
        "completed_turn4_raw_ra0_vectors": 0,
        "deterministic_turn5_k1b_preparations": 0,
        "turn4_household_calls": 0,
        "fourth_outer_turns": 0,
        "turn5_household_calls": 0,
    })
    relaxation_state = {"context": None, "relaxation": prior_turn4.new_relaxation_ledger()}
    original_direct, original_helper = prior_turn4.install_runtime_capture(output, relaxation_state)
    original_map = base._map_checkpoint
    wrapped_map, anhui_runtime = capture_anhui_runtime(output)
    base._map_checkpoint = wrapped_map
    try:
        native_grid = base.oracle.MatlabFaithfulHJBGrid(
            np.linspace(-2, 5, 20), np.linspace(0, 10, 20), np.array([0.8, 1.3]),
            np.array([[-1 / 3, 1 / 3], [1 / 3, -1 / 3]]),
        )
        grid = CorrectedDiagnosticGrid(native_grid.b, native_grid.a, native_grid.z)
        native_params = base.oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
        core_hashes = base._scientific_code_hashes(repository)
        results = []
        for index, province in enumerate(PROVINCE_ORDER):
            results.append(base._solve_province(
                repository, output, index, province, states4[index], grid, native_grid,
                native_params, base._task_hashes(repository), core_hashes, scientific_ledger,
            ))
        if len(results) != 31:
            raise FailClosed("FAIL__TURN4_HOUSEHOLD_BATCH_INCOMPLETE", {"count": len(results)})
        scientific_ledger["household_batch_constructions"] += 1
        scientific_ledger["authorized_k1b_turn4_household_batches"] += 1
        scientific_ledger["turn4_household_calls"] += 1
        scientific_ledger["fourth_outer_turns"] += 1
        batch = PreFrozenHouseholdOutputBatch(
            ct=[row["aggregates"]["Ct"]["mass_form"] for row in results],
            household_lt=[row["aggregates"]["Lt"]["mass_form"] for row in results],
            at=[row["aggregates"]["At"]["mass_form"] for row in results],
            bt=[row["aggregates"]["Bt"]["mass_form"] for row in results],
            at_tax=[row["aggregates"]["AtTax"]["mass_form"] for row in results],
            converged=(True,) * 31,
            diagnostics=tuple({"checkpoint": row["checkpoint"], "B": row["B"], "D": row["D"]} for row in results),
        )
        household_rows = [
            {"province_index": i, "province": row["province"], "checkpoint": row["checkpoint"],
             "B": row["B"], "D": row["D"], "backward_error_max": row["backward_error_max"]}
            for i, row in enumerate(results)
        ]
        write_json(output / "household_batch_receipt.json", {
            "status": "PASS", "province_count": 31,
            "rows": household_rows,
        })
        integration = prior_turn4.integrate_turn4(
            repository, output, states4, batch, frozen_shares, scientific_ledger,
            household_rows,
        )
        return finalize(repository, output, pre_freeze, scientific_ledger, relaxation_state["relaxation"],
                        PASS_TERMINAL, {"household_pass_count": 31, "integration_status": "PASS",
                                        "turn5_household_run": False,
                                        "anhui_in_path_capture_count": anhui_runtime["capture_count"],
                                        "turn5_rah_sha256": integration["turn5_rah_sha256"]}, started)
    except FailClosed as failure:
        return finalize(repository, output, pre_freeze, scientific_ledger, relaxation_state["relaxation"],
                        failure.terminal, failure.detail, started)
    except Exception as exc:
        return finalize(repository, output, pre_freeze, scientific_ledger, relaxation_state["relaxation"],
                        "FAIL__UNEXPECTED_TASK_EXCEPTION__NO_SCIENTIFIC_RETRY",
                        {"type": type(exc).__name__, "message": str(exc)}, started)
    finally:
        base._map_checkpoint = original_map
        base._direct_update = original_direct
        base.monotonicity_preserving_relaxation = original_helper


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--focused-test-junit", type=Path, required=True)
    args = parser.parse_args(argv)
    verdict = execute(args.repository, args.focused_test_junit)
    print(verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
