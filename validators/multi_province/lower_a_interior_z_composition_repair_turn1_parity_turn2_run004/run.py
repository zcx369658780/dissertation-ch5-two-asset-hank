"""Bounded lower-a/interior-Z repair, turn-1 parity, and turn-2 run004."""
from __future__ import annotations

import argparse
from dataclasses import asdict
import json
import math
from pathlib import Path
import subprocess
import time
from typing import Any, Mapping

import numpy as np

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
from validators.multi_province.turn2_f0364_negative_ratio_switching_forensic import (
    run as f0364,
)
from validators.multi_province.turn2_hebei_f0005_lower_a_liquid_switch_forensic import (
    run as f0005,
)


TASK_ID = "CH5_MP4C_LOWER_A_INTERIOR_Z_COMPOSITION_REPAIR_TURN1_PARITY_AND_TURN2_RUN004_20260921"
BASELINE_SHA = "79649059282540d6bdd4192ecc3b01771a7152bc"
PASS_PARITY = "PASS__TURN1_ACCEPTED_POLICY_IDENTITY_PARITY_UNDER_LOWER_A_INTERIOR_Z_COMPOSITION_REPAIR"
BLOCKED_PARITY = "BLOCKED__LOWER_A_INTERIOR_Z_COMPOSITION_REPAIR_TURN1_POLICY_PARITY_MISMATCH"
PASS_TERMINAL = (
    "PASS__LOWER_A_INTERIOR_Z_COMPOSITION_REPAIR__TURN1_POLICY_PARITY_PASS__"
    "CORRECTED_TURN2_31_PROVINCE_HJB_KFE_AND_INTEGRATION__RAW_TURN3_PAYOFF_READY__"
    "TURN3_NOT_RUN"
)
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_lower_a_interior_z_composition_repair_turn1_parity_turn2_run004_20260921"
)
TASK_RELATIVE = Path(
    "tasks/CH5_MP4C_LOWER_A_INTERIOR_Z_COMPOSITION_REPAIR_TURN1_PARITY_AND_TURN2_RUN004_20260921.md"
)
SELECTOR_RELATIVE = Path("src/ch5_two_asset_hank/corrected_diagnostic/selector.py")
FOCUSED_TEST_RELATIVE = Path(
    "tests/test_mp4c_lower_a_interior_z_composition_repair.py"
)
RUNNER_RELATIVE = Path(
    "validators/multi_province/lower_a_interior_z_composition_repair_turn1_parity_turn2_run004/run.py"
)
RUNNER_TEST_RELATIVE = Path(
    "tests/test_mp4c_lower_a_interior_z_composition_repair_turn1_parity_turn2_run004.py"
)
TURN1_ROOT = Path(
    "reports/ch5_mp4c_corrected_optionb_initial_turn_unique_closed_class_kfe_20260920_run004"
)
RUN003_ROOT = Path(
    "reports/ch5_mp4c_interior_b_negative_ratio_repair_turn1_parity_turn2_run003_20260921"
)
F0005_FORENSIC_ROOT = Path(
    "reports/ch5_mp4c_turn2_hebei_f0005_lower_a_liquid_switch_forensic_20260921_run001"
)
INTEGRATION_ROOT = base.ENTERING_STATE_RELATIVE.parent
TURN1_MANIFEST = "CF70E7D6A62A35F461D1A75B28F8F502B2CBDD2D94ED5D9DDFA099D821CC5EC6"
RUN003_MANIFEST = "E1DBBDF7E86B8F11A4DDB646A1CBD53259E5182D6EFE6A0D2679314874B8A403"
F0005_FORENSIC_MANIFEST = "039E74760D6FFAC8DD3177723B6F7EE9FFC9CFE2BD6C192EF4EB34160DAD026A"
INTEGRATION_MANIFEST = "79C6B15340AF641A736C79D0ED7C6450E39EA495263943280B6DDBD1B094F28D"

EXPECTED_CHANGED_PATHS = sorted(
    path.as_posix()
    for path in (
        SELECTOR_RELATIVE,
        FOCUSED_TEST_RELATIVE,
        RUNNER_RELATIVE,
        RUNNER_RELATIVE.parent / "__init__.py",
        RUNNER_TEST_RELATIVE,
    )
)
UNCHANGED_SCIENTIFIC_PATHS = (
    Path("src/ch5_two_asset_hank/corrected_diagnostic/cost.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/optionb_initial_turn_integration.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/generator.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/run004_canonical_integration_replay.py"),
)


def _git(repository: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repository, text=True).strip()


def _verify_manifest(
    root: Path, expected_sha256: str, expected_entries: int
) -> dict[str, Any]:
    manifest_path = root / "sealed_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bad_paths = []
    for row in manifest["entries"]:
        path = root / row["path"]
        if (
            not path.is_file()
            or path.stat().st_size != int(row["bytes"])
            or base._sha256(path) != row["sha256"]
        ):
            bad_paths.append(row["path"])
    readback = json.loads(
        (root / "independent_readback_receipt.json").read_text(encoding="utf-8")
    )
    checks = {
        "manifest_sha256": base._sha256(manifest_path) == expected_sha256,
        "entry_count": int(manifest["entry_count"]) == expected_entries,
        "all_entries_read_back": not bad_paths,
        "accepted_readback": readback.get("status") == "PASS"
        and not readback.get("bad_paths"),
    }
    receipt = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "root": root.name,
        "manifest_sha256": base._sha256(manifest_path),
        "entry_count": int(manifest["entry_count"]),
        "total_bytes": int(manifest["total_bytes"]),
        "checks": checks,
        "bad_paths": bad_paths,
    }
    if receipt["status"] != "PASS":
        raise FailClosed("BLOCKED__ACCEPTED_PREDECESSOR_MANIFEST_MISMATCH", receipt)
    return receipt


def accepted_turn1_map_inventory(repository: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    household = repository / TURN1_ROOT / "household"
    for province_index, province in enumerate(PROVINCE_ORDER):
        province_root = household / f"p{province_index:02d}_{province}"
        for directory in sorted(province_root.glob("checkpoint_[0-9][0-9][0-9]")):
            manifest_path = directory / "checkpoint_manifest.json"
            arrays_path = directory / "checkpoint_arrays.npz"
            if not manifest_path.is_file() or not arrays_path.is_file():
                continue
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            checkpoint = int(directory.name.rsplit("_", 1)[1])
            if (
                int(manifest["province_index"]) != province_index
                or manifest["province"] != province
                or int(manifest["checkpoint"]) != checkpoint
            ):
                raise FailClosed(
                    "BLOCKED__TURN1_ACCEPTED_MAP_ORDER_MISMATCH",
                    {"path": manifest_path.relative_to(repository).as_posix()},
                )
            rows.append(
                {
                    "province_index": province_index,
                    "province": province,
                    "checkpoint": checkpoint,
                    "directory": directory,
                    "accepted_policy_identity": manifest["policy_identity_sha256"],
                    "accepted_value_sha256": manifest["value_sha256"],
                }
            )
    return rows


def _source_freeze(repository: Path) -> dict[str, str]:
    paths = (
        SELECTOR_RELATIVE,
        FOCUSED_TEST_RELATIVE,
        RUNNER_RELATIVE,
        RUNNER_RELATIVE.parent / "__init__.py",
        RUNNER_TEST_RELATIVE,
        *UNCHANGED_SCIENTIFIC_PATHS,
    )
    return {path.as_posix(): base._sha256(repository / path) for path in paths}


def _unchanged_blobs(repository: Path) -> dict[str, Any]:
    rows = {}
    for path in UNCHANGED_SCIENTIFIC_PATHS:
        head = _git(repository, "rev-parse", f"HEAD:{path.as_posix()}")
        baseline = _git(repository, "rev-parse", f"{BASELINE_SHA}:{path.as_posix()}")
        rows[path.as_posix()] = {
            "head_blob": head,
            "baseline_blob": baseline,
            "unchanged": head == baseline,
        }
    return rows


def _f0364_focused_parity(repository: Path) -> dict[str, Any]:
    _, cell, checks = f0364.load_cell(repository)
    budget = SelectorBudget(
        max_selector_evaluations=1,
        max_root_invocations=0,
        max_interior_z_root_invocations=0,
        max_interior_a_switching_root_invocations=0,
        max_joint_switching_root_invocations=0,
    )
    result = select_constrained_policy(cell, f0364.PARAMETERS, budget=budget)
    selected = result.selected
    forward_switching = [
        row
        for row in result.candidates
        if row.transfer_branch == "negative"
        and row.derivative_branches == {"b": "forward", "a": "zero"}
    ]
    parity = {
        "cell_binding": all(checks.values()),
        "selected": selected is not None and result.outcome == "SELECTED_ADMISSIBLE",
        "transfer_regime": selected is not None and selected.transfer_branch == "negative",
        "branches": selected is not None
        and selected.derivative_branches == {"b": "backward", "a": "zero"},
        "q_b": selected is not None and selected.q_b == 0.006091715618507631,
        "q_a": selected is not None and selected.q_a == -0.0045978913784868415,
        "d": selected is not None and selected.d == -7.8384208979658965,
        "g_a": selected is not None and selected.g_a == 0.0,
        "g_b": selected is not None and selected.g_b == -4.227123020026542,
        "kkt": selected is not None and selected.transfer_kkt_residual == 0.0,
        "hamiltonian": selected is not None
        and selected.hamiltonian == -0.11188508398929994,
        "admissible": selected is not None
        and selected.admissible
        and not selected.rejection_reasons,
        "forward_switching_not_emitted_without_crossing": not forward_switching,
        "no_root": budget.root_invocations == 0,
    }
    return {
        "status": "PASS" if all(parity.values()) else "FAIL",
        "checks": parity,
        "selector_evaluations": budget.selector_evaluations,
        "root_invocations": budget.root_invocations,
        "selected": asdict(selected) if selected is not None else None,
    }


def _f0005_cell(repository: Path) -> tuple[CorrectedSelectorCell, CorrectedSelectorParameters]:
    _, payload = f0005.load_cell(repository)
    row = dict(payload["selector_cell"])
    derivatives = CellDerivatives(**row.pop("derivatives"))
    cell = CorrectedSelectorCell(**row, derivatives=derivatives)
    parameters = CorrectedSelectorParameters(
        **{key: float(value) for key, value in f0005.PARAMETERS.items()}
    )
    return cell, parameters


def _f0005_focused_parity(repository: Path) -> dict[str, Any]:
    cell, parameters = _f0005_cell(repository)
    budget = SelectorBudget(
        max_selector_evaluations=1,
        max_root_invocations=64,
        max_interior_z_root_invocations=32,
        max_interior_a_switching_root_invocations=32,
        max_joint_switching_root_invocations=32,
    )
    result = select_constrained_policy(cell, parameters, budget=budget)
    selected = result.selected
    lower_a = None if selected is None else selected.lower_a_zero_kink_multiplier_receipt
    checks = {
        "selected": selected is not None and result.outcome == "SELECTED_ADMISSIBLE",
        "active": selected is not None and selected.active_constraints == ("lower_a",),
        "transfer": selected is not None and selected.transfer_branch == "zero_kink",
        "branches": selected is not None
        and selected.derivative_branches == {"b": "zero", "a": "forward"},
        "q_b_forensic_binary64_within_frozen_brent_bound": selected is not None
        and math.isclose(selected.q_b, 0.012085132579009488, rel_tol=0.0, abs_tol=2e-17),
        "kink_interval": lower_a is not None
        and all(
            math.isclose(actual, expected, rel_tol=0.0, abs_tol=4e-18)
            for actual, expected in zip(
                lower_a.raw_kink_interval,
                (0.01087661932110854, 0.013293645836910438),
            )
        ),
        "q_a": selected is not None
        and math.isclose(selected.q_a, 0.01087661932110854, rel_tol=0.0, abs_tol=4e-18),
        "lambda_a": selected is not None
        and math.isclose(
            selected.multipliers.get("lower_a", math.nan),
            0.00028489863234105843,
            rel_tol=0.0,
            abs_tol=4e-18,
        ),
        "zero_drifts": selected is not None
        and selected.d == 0.0
        and selected.g_a == 0.0
        and selected.g_b == 0.0,
        "kkt": selected is not None
        and selected.transfer_kkt_residual == 0.0
        and selected.complementarity_residuals.get("lower_a") == 0.0,
        "hamiltonian": selected is not None
        and math.isclose(
            selected.hamiltonian,
            -0.1280816705218543,
            rel_tol=0.0,
            abs_tol=3e-17,
        ),
        "admissible": selected is not None
        and selected.admissible
        and not selected.rejection_reasons,
    }
    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "accepted_forensic_q_b_binary64": 0.012085132579009488,
        "frozen_screened_brent_q_b": None if selected is None else selected.q_b,
        "binary64_ulp_offset": None
        if selected is None
        else (selected.q_b - 0.012085132579009488) / np.spacing(0.012085132579009488),
        "selector_evaluations": budget.selector_evaluations,
        "root_invocations": budget.root_invocations,
        "selected": asdict(selected) if selected is not None else None,
    }


def replay_turn1_policy_identities(
    repository: Path, inventory: list[dict[str, Any]]
) -> tuple[dict[str, Any], dict[str, Any]]:
    if len(inventory) != 408:
        raise FailClosed(
            "BLOCKED__TURN1_ACCEPTED_MAP_COUNT_MISMATCH",
            {"expected": 408, "actual": len(inventory)},
        )
    states, state_receipt = turn1.load_initial_states(repository)
    native_grid = base.oracle.MatlabFaithfulHJBGrid(
        np.linspace(-2, 5, 20),
        np.linspace(0, 10, 20),
        np.array([0.8, 1.3]),
        np.array([[-1 / 3, 1 / 3], [1 / 3, -1 / 3]]),
    )
    grid = CorrectedDiagnosticGrid(native_grid.b, native_grid.a, native_grid.z)
    budget = SelectorBudget(
        max_selector_evaluations=326_400,
        max_root_invocations=2_000_000,
        max_interior_z_root_invocations=326_400,
        max_interior_a_switching_root_invocations=326_400,
        max_joint_switching_root_invocations=326_400,
    )
    accepted_ids: list[str] = []
    replayed_ids: list[str] = []
    map_rows: list[dict[str, Any]] = []
    mismatches: list[dict[str, Any]] = []

    for map_ordinal, row in enumerate(inventory):
        directory = Path(row["directory"])
        with np.load(directory / "checkpoint_arrays.npz", allow_pickle=False) as payload:
            value = np.asarray(payload["value"], dtype=np.float64)
        value_sha256 = nlc._field_sha256(value)
        inputs = turn1._province_inputs(
            repository, states[int(row["province_index"])], value, grid
        )
        fields = nlc.raw_derivative_fields(value, grid)
        selected_identities = []
        map_error: dict[str, Any] | None = None
        for flat, index in enumerate(nlc.iter_f_order_indices(nlc.SHAPE)):
            try:
                derivatives, _ = nlc.boundary_cell_derivatives(fields, index, grid)
                cell = nlc._cell(
                    inputs,
                    index,
                    derivatives,
                    int(row["checkpoint"]),
                    flat,
                )
                result = select_constrained_policy(
                    cell, inputs.parameters, budget=budget
                )
                if result.outcome != "SELECTED_ADMISSIBLE" or result.selected is None:
                    map_error = {
                        "flat": flat,
                        "index_b_a_z_zero_based": list(index),
                        "outcome": result.outcome,
                    }
                    break
                selected_identities.append(nlc._selected_identity(asdict(result.selected)))
            except Exception as exc:
                map_error = {
                    "flat": flat,
                    "index_b_a_z_zero_based": list(index),
                    "exception": type(exc).__name__,
                    "message": str(exc),
                }
                break
        replayed = (
            nlc._canonical_sha256(selected_identities)
            if map_error is None and len(selected_identities) == nlc.N
            else None
        )
        accepted = str(row["accepted_policy_identity"])
        matched = (
            value_sha256 == row["accepted_value_sha256"]
            and replayed == accepted
        )
        receipt = {
            "map_ordinal": map_ordinal,
            "province_index": row["province_index"],
            "province": row["province"],
            "checkpoint": row["checkpoint"],
            "accepted_value_sha256": row["accepted_value_sha256"],
            "replayed_value_sha256": value_sha256,
            "accepted_policy_identity": accepted,
            "replayed_policy_identity": replayed,
            "exact_match": matched,
            "error": map_error,
        }
        map_rows.append(receipt)
        accepted_ids.append(accepted)
        replayed_ids.append(replayed or "MISSING")
        if not matched:
            mismatches.append(receipt)
            break

    ledger = {
        "policy_maps_replayed": len(map_rows),
        "selector_evaluations": budget.selector_evaluations,
        "scalar_root_invocations": budget.root_invocations,
        "interior_z_root_invocations": budget.interior_z_root_invocations,
        "interior_a_switching_root_invocations": budget.interior_a_switching_root_invocations,
        "joint_switching_root_invocations": budget.joint_switching_root_invocations,
        "hjb_direct_updates": 0,
        "d2_q_assemblies": 0,
        "scc_kfe_svd": 0,
        "aggregates_integration": 0,
        "scientific_retries": 0,
    }
    exact = (
        len(map_rows) == 408
        and budget.selector_evaluations == 326_400
        and not mismatches
    )
    receipt = {
        "status": "PASS" if exact else "FAIL",
        "terminal": PASS_PARITY if exact else BLOCKED_PARITY,
        "state_binding": state_receipt,
        "maps_replayed": len(map_rows),
        "exact_matches": len(map_rows) - len(mismatches),
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
        "first_mismatch_stop": bool(mismatches),
        "accepted_ordered_policy_digest": nlc._canonical_sha256(accepted_ids),
        "replayed_ordered_policy_digest": nlc._canonical_sha256(replayed_ids),
        "ordered_map_receipts": map_rows,
    }
    return receipt, ledger


def _capture_runtime_parity(output: Path) -> tuple[Any, dict[str, Any]]:
    original = base._map_checkpoint
    state: dict[str, Any] = {"f0364_capture_count": 0, "f0005_capture_count": 0}

    def wrapped(*args, **kwargs):
        result = original(*args, **kwargs)
        checkpoint = int(args[2])
        province_root = Path(args[1])
        if checkpoint == 5 and province_root.name == "p00_北京":
            cell_path = province_root / "checkpoint_005/cell_0364.json"
            payload = json.loads(cell_path.read_text(encoding="utf-8"))
            selector = payload["selector_result"]
            selected = selector.get("selected")
            checks = {
                "selected": selector["outcome"] == "SELECTED_ADMISSIBLE"
                and selected is not None,
                "branches": selected is not None
                and selected["derivative_branches"] == {"a": "zero", "b": "backward"},
                "transfer": selected is not None
                and selected["transfer_branch"] == "negative",
                "q_b": selected is not None
                and selected["q_b"] == 0.006091715618507631,
                "q_a": selected is not None
                and selected["q_a"] == -0.0045978913784868415,
                "d": selected is not None
                and selected["d"] == -7.8384208979658965,
                "g_a": selected is not None and selected["g_a"] == 0.0,
                "g_b": selected is not None
                and selected["g_b"] == -4.227123020026542,
                "kkt": selected is not None
                and selected["transfer_kkt_residual"] == 0.0,
                "hamiltonian": selected is not None
                and selected["hamiltonian"] == -0.11188508398929994,
            }
            receipt = {
                "status": "PASS" if all(checks.values()) else "FAIL",
                "source": cell_path.as_posix(),
                "checks": checks,
                "selected": selected,
                "no_additional_selector_call": True,
            }
            base._write_json(output / "f0364_normal_map_repair_parity_receipt.json", receipt)
            state.update({"f0364_capture_count": 1, "f0364_receipt": receipt})
            if receipt["status"] != "PASS":
                raise FailClosed("FAIL__F0364_NORMAL_MAP_REPAIR_PARITY_MISMATCH", receipt)
        if checkpoint == 1 and province_root.name == "p02_河北":
            cell_path = province_root / "checkpoint_001/cell_0005.json"
            payload = json.loads(cell_path.read_text(encoding="utf-8"))
            selector = payload["selector_result"]
            selected = selector.get("selected")
            lower_a = None if selected is None else selected.get(
                "lower_a_zero_kink_multiplier_receipt"
            )
            checks = {
                "selected": selector["outcome"] == "SELECTED_ADMISSIBLE"
                and selected is not None,
                "active": selected is not None
                and selected["active_constraints"] == ["lower_a"],
                "branches": selected is not None
                and selected["derivative_branches"] == {"a": "forward", "b": "zero"},
                "transfer": selected is not None
                and selected["transfer_branch"] == "zero_kink",
                "q_b_forensic_binary64_within_frozen_brent_bound": selected is not None
                and math.isclose(
                    selected["q_b"], 0.012085132579009488, rel_tol=0.0, abs_tol=2e-17
                ),
                "kink_interval": lower_a is not None
                and all(
                    math.isclose(actual, expected, rel_tol=0.0, abs_tol=4e-18)
                    for actual, expected in zip(
                        lower_a["raw_kink_interval"],
                        (0.01087661932110854, 0.013293645836910438),
                    )
                ),
                "q_a": selected is not None
                and math.isclose(
                    selected["q_a"], 0.01087661932110854, rel_tol=0.0, abs_tol=4e-18
                ),
                "lambda_a": selected is not None
                and math.isclose(
                    selected["multipliers"]["lower_a"],
                    0.00028489863234105843,
                    rel_tol=0.0,
                    abs_tol=4e-18,
                ),
                "zero_drifts": selected is not None
                and selected["d"] == 0.0
                and selected["g_a"] == 0.0
                and selected["g_b"] == 0.0,
                "kkt": selected is not None
                and selected["transfer_kkt_residual"] == 0.0
                and selected["complementarity_residuals"]["lower_a"] == 0.0,
                "hamiltonian": selected is not None
                and math.isclose(
                    selected["hamiltonian"],
                    -0.1280816705218543,
                    rel_tol=0.0,
                    abs_tol=3e-17,
                ),
                "admissible": selected is not None
                and selected["admissible"]
                and not selected["rejection_reasons"],
            }
            receipt = {
                "status": "PASS" if all(checks.values()) else "FAIL",
                "source": cell_path.as_posix(),
                "checks": checks,
                "accepted_forensic_q_b_binary64": 0.012085132579009488,
                "frozen_screened_brent_q_b": None if selected is None else selected["q_b"],
                "selected": selected,
                "no_additional_selector_call": True,
            }
            base._write_json(output / "f0005_normal_map_repair_parity_receipt.json", receipt)
            state.update({"f0005_capture_count": 1, "f0005_receipt": receipt})
            if receipt["status"] != "PASS":
                raise FailClosed("FAIL__F0005_NORMAL_MAP_REPAIR_PARITY_MISMATCH", receipt)
        return result

    return wrapped, state


def _finalize(
    repository: Path,
    output: Path,
    pre_freeze: dict[str, str],
    turn2_ledger: dict[str, Any],
    terminal: str,
    detail: dict[str, Any],
    started: float,
) -> str:
    post_freeze = _source_freeze(repository)
    if post_freeze != pre_freeze:
        terminal = "BLOCKED__SCIENTIFIC_CODE_CHANGED_AFTER_FREEZE"
        detail = {"prior_detail": detail}
    base._check_ledger(turn2_ledger)
    turn2_ledger["wall_seconds"] = float(time.perf_counter() - started)
    turn2_ledger["terminal_verdict"] = terminal
    base._write_json(output / "turn2_run004_scientific_ledger.json", turn2_ledger)
    base._write_json(
        output / "post_execution_code_freeze.json",
        {
            "status": "PASS" if post_freeze == pre_freeze else "FAIL",
            "source_sha256_after": post_freeze,
            "matches_pre_execution_freeze": post_freeze == pre_freeze,
        },
    )
    base._write_json(
        output / "terminal_receipt.json",
        {
            "terminal_verdict": terminal,
            "detail": detail,
            "turn3_household_run": False,
            "k1b": 0,
            "k2": 0,
            "successor_published": False,
            "results_eligibility": False,
        },
    )
    base._manifest(output)
    base._readback(output)
    return terminal


def execute(repository: Path, focused_test_junit: Path) -> str:
    repository = repository.resolve(strict=True)
    output = repository / OUTPUT_RELATIVE
    if output.exists():
        raise FailClosed(
            "BLOCKED__FRESH_EVIDENCE_ROOT_ALREADY_EXISTS",
            {"path": output.as_posix()},
        )
    started = time.perf_counter()
    turn2_ledger = base._new_ledger()
    base.TASK_RELATIVE = TASK_RELATIVE
    focused = base._read_junit(focused_test_junit)
    changed_paths = sorted(
        filter(
            None,
            _git(
                repository,
                "diff",
                "--name-only",
                f"{BASELINE_SHA}...HEAD",
            ).splitlines(),
        )
    )
    manifests = {
        "turn1_run004": _verify_manifest(repository / TURN1_ROOT, TURN1_MANIFEST, 4353),
        "accepted_turn2_run003": _verify_manifest(
            repository / RUN003_ROOT, RUN003_MANIFEST, 306
        ),
        "f0005_forensic": _verify_manifest(
            repository / F0005_FORENSIC_ROOT, F0005_FORENSIC_MANIFEST, 11
        ),
        "canonical_initial_integration": _verify_manifest(
            repository / INTEGRATION_ROOT, INTEGRATION_MANIFEST, 17
        ),
    }
    unchanged = _unchanged_blobs(repository)
    inventory = accepted_turn1_map_inventory(repository)
    f0364_parity = _f0364_focused_parity(repository)
    f0005_parity = _f0005_focused_parity(repository)
    startup_checks = {
        "origin_main_exact_baseline": _git(repository, "rev-parse", "origin/main")
        == BASELINE_SHA,
        "baseline_is_ancestor": subprocess.run(
            ["git", "merge-base", "--is-ancestor", BASELINE_SHA, "HEAD"],
            cwd=repository,
            check=False,
        ).returncode
        == 0,
        "clean_code_freeze_worktree": not _git(repository, "status", "--porcelain"),
        "changed_paths_exact": changed_paths == EXPECTED_CHANGED_PATHS,
        "focused_tests": focused["status"] == "PASS",
        "manifests": all(row["status"] == "PASS" for row in manifests.values()),
        "unchanged_scientific_sources": all(
            row["unchanged"] for row in unchanged.values()
        ),
        "accepted_turn1_map_count_408": len(inventory) == 408,
        "f0364_exact_normal_selector_parity": f0364_parity["status"] == "PASS",
        "f0005_normal_selector_composition_parity": f0005_parity["status"] == "PASS",
    }
    if not all(startup_checks.values()):
        raise FailClosed(
            "BLOCKED__LOWER_A_INTERIOR_Z_COMPOSITION_REPAIR_ENGINEERING_GATE",
            {"checks": startup_checks},
        )

    pre_freeze = _source_freeze(repository)
    core_hashes = base._scientific_code_hashes(repository)
    task_hashes = base._task_hashes(repository)
    output.mkdir(parents=True, exist_ok=False)
    base._write_json(
        output / "authority_binding.json",
        {
            "status": "PASS",
            "task_id": TASK_ID,
            "actual_live_main_baseline": BASELINE_SHA,
            "execution_head": _git(repository, "rev-parse", "HEAD"),
            "checks": startup_checks,
            "manifests": manifests,
            "unchanged_scientific_blobs": unchanged,
            "changed_paths": changed_paths,
        },
    )
    base._write_json(output / "focused_test_receipt.json", focused)
    base._write_json(output / "f0364_focused_selector_parity_receipt.json", f0364_parity)
    base._write_json(output / "f0005_focused_selector_parity_receipt.json", f0005_parity)
    base._write_json(
        output / "selector_repair_contract.json",
        {
            "status": "PASS",
            "active_lower_a_zero_kink_interior_liquid_z": (
                "RAW_ENDPOINT_LIQUID_DRIFT_SCREEN_THEN_EXISTING_INTERIOR_Z_ROOT_"
                "AND_FULL_ROOT_CANDIDATE_RECONSTRUCTION"
            ),
            "ordinary_endpoint_admissibility": "UNCHANGED",
            "active_liquid_faces": "UNCHANGED",
            "interior_b_negative_nonzero_ratio": "UNCHANGED",
            "ratio_zero": "FAIL_CLOSED",
            "d3_kkt_direction_finite_hamiltonian": "UNCHANGED",
        },
    )
    base._write_json(
        output / "pre_execution_code_freeze.json",
        {
            "status": "PASS",
            "source_sha256_before": pre_freeze,
            "core_corrected_code_sha256_before": core_hashes,
            "task_hashes": task_hashes,
        },
    )

    try:
        parity, compatibility_ledger = replay_turn1_policy_identities(
            repository, inventory
        )
        base._write_json(output / "turn1_compatibility_replay_receipt.json", parity)
        base._write_json(
            output / "turn1_compatibility_replay_ledger.json",
            compatibility_ledger,
        )
        if parity["status"] != "PASS":
            return _finalize(
                repository,
                output,
                pre_freeze,
                turn2_ledger,
                BLOCKED_PARITY,
                {
                    "mismatch_count": parity["mismatch_count"],
                    "turn2_started": False,
                },
                started,
            )

        states, entering = base.load_initial_states(repository)
        base._write_json(output / "turn2_entering_state_binding.json", entering)
        original_map = base._map_checkpoint
        wrapped_map, runtime_parity = _capture_runtime_parity(output)
        base._map_checkpoint = wrapped_map
        try:
            native_grid = base.oracle.MatlabFaithfulHJBGrid(
                np.linspace(-2, 5, 20),
                np.linspace(0, 10, 20),
                np.array([0.8, 1.3]),
                np.array([[-1 / 3, 1 / 3], [1 / 3, -1 / 3]]),
            )
            grid = CorrectedDiagnosticGrid(native_grid.b, native_grid.a, native_grid.z)
            native_params = base.oracle.EconomicParams(
                0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0
            )
            results = []
            for index, province in enumerate(PROVINCE_ORDER):
                results.append(
                    base._solve_province(
                        repository,
                        output,
                        index,
                        province,
                        states[index],
                        grid,
                        native_grid,
                        native_params,
                        task_hashes,
                        core_hashes,
                        turn2_ledger,
                    )
                )
            if (
                len(results) != 31
                or runtime_parity["f0364_capture_count"] != 1
                or runtime_parity["f0005_capture_count"] != 1
            ):
                raise FailClosed(
                    "FAIL__TURN2_HOUSEHOLD_OR_RUNTIME_REPAIR_PARITY_INCOMPLETE",
                    {
                        "household_count": len(results),
                        "f0364_capture_count": runtime_parity["f0364_capture_count"],
                        "f0005_capture_count": runtime_parity["f0005_capture_count"],
                    },
                )
            turn2_ledger["household_batch_constructions"] += 1
            batch = PreFrozenHouseholdOutputBatch(
                ct=[row["aggregates"]["Ct"]["mass_form"] for row in results],
                household_lt=[
                    row["aggregates"]["Lt"]["mass_form"] for row in results
                ],
                at=[row["aggregates"]["At"]["mass_form"] for row in results],
                bt=[row["aggregates"]["Bt"]["mass_form"] for row in results],
                at_tax=[
                    row["aggregates"]["AtTax"]["mass_form"] for row in results
                ],
                converged=(True,) * 31,
                diagnostics=tuple(
                    {
                        "checkpoint": row["checkpoint"],
                        "B": row["B"],
                        "D": row["D"],
                    }
                    for row in results
                ),
            )
            base._write_json(
                output / "household_batch_receipt.json",
                {
                    "status": "PASS",
                    "province_count": 31,
                    "identity_sha256": base._canonical_sha256(
                        {
                            "ct": batch.ct.tolist(),
                            "lt": batch.household_lt.tolist(),
                            "at": batch.at.tolist(),
                            "bt": batch.bt.tolist(),
                            "at_tax": batch.at_tax.tolist(),
                        }
                    ),
                    "rows": [
                        {
                            "province_index": i,
                            "province": row["province"],
                            "checkpoint": row["checkpoint"],
                            "B": row["B"],
                            "D": row["D"],
                            "backward_error_max": row["backward_error_max"],
                        }
                        for i, row in enumerate(results)
                    ],
                },
            )
            integration = base.integrate_one_turn(
                repository, states, batch, turn2_ledger
            )
            shares = np.asarray(
                integration.pop("portfolio_shares_destination_origin"),
                dtype=np.float64,
            )
            terms = np.asarray(
                integration.pop("ordered_product_terms"), dtype=np.float64
            )
            raw_ra0 = np.asarray(
                integration["raw_ra0_turn2_by_destination"], dtype=np.float64
            )
            rah_turn3 = np.asarray(
                integration["rah_turn3_raw_by_origin"], dtype=np.float64
            )
            blas = np.asarray(integration["blas_diagnostic"], dtype=np.float64)
            np.savez_compressed(
                output / "canonical_turn3_raw_payoff_arrays.npz",
                raw_ra0_turn2=raw_ra0,
                shares_destination_origin=shares,
                ordered_product_terms=terms,
                canonical_rah_turn3=rah_turn3,
                blas_diagnostic=blas,
            )
            base._write_json(output / "one_turn_integration_receipt.json", integration)
            base._write_json(
                output / "turn3_next_state_candidate_receipt.json",
                {
                    "status": "PASS",
                    "classification": "TURN3_INPUT_CANDIDATE_ONLY__TURN3_NOT_RUN",
                    "raw_next_payoff_sha256": integration["rah_turn3_sha256"],
                    "rows": integration["next_states"],
                },
            )
            return _finalize(
                repository,
                output,
                pre_freeze,
                turn2_ledger,
                PASS_TERMINAL,
                {
                    "household_pass_count": 31,
                    "integration_status": "PASS",
                    "turn3_payoff_sha256": integration["rah_turn3_sha256"],
                    "turn3_household_run": False,
                },
                started,
            )
        finally:
            base._map_checkpoint = original_map
    except FailClosed as failure:
        return _finalize(
            repository,
            output,
            pre_freeze,
            turn2_ledger,
            failure.terminal,
            failure.detail,
            started,
        )
    except Exception as exc:
        return _finalize(
            repository,
            output,
            pre_freeze,
            turn2_ledger,
            "FAIL__UNEXPECTED_TASK_EXCEPTION__NO_SCIENTIFIC_RETRY",
            {"type": type(exc).__name__, "message": str(exc)},
            started,
        )


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
