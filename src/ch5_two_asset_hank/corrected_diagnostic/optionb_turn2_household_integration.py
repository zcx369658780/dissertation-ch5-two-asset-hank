"""Bounded Option-B turn-2 household/KFE and one-turn integration.

This is an opt-in task driver.  It composes accepted scientific components and
does not alter any default or production runtime route.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from dataclasses import asdict
import hashlib
import json
import math
from pathlib import Path
import subprocess
import time
from types import MappingProxyType
from typing import Any, Mapping
import warnings
import xml.etree.ElementTree as ET

import numpy as np
from scipy import sparse
from scipy.sparse import linalg as sparse_linalg

from exports import matlab_faithful_two_asset_ha as oracle
from ch5_two_asset_hank.multi_province import one_turn as source
from ch5_two_asset_hank.multi_province.c1_residual_public_asset import C1_UPDATE_ORDER
from ch5_two_asset_hank.multi_province.capital_allocation import CapitalAllocationInputs
from ch5_two_asset_hank.multi_province.corrected_household_adapter import (
    CorrectedHouseholdAggregateInputs,
    evaluate_corrected_household_aggregates,
)
from ch5_two_asset_hank.multi_province.government_assets import residual_government_asset_levels
from ch5_two_asset_hank.multi_province.k1a_runtime_adapter import (
    K1ARuntimeConfig,
    allocate_k1a_capital,
    load_accepted_distance_score,
)
from ch5_two_asset_hank.multi_province.one_turn import OneTurnInputs, PreFrozenHouseholdOutputBatch
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER
from validators.multi_province.corrected_2018_single_turn.run import source_initial_arrays

from .checkpoint2_to_checkpoint6 import _switching_statistics
from .contracts import CorrectedDiagnosticGrid
from .nonlinear_continuation import (
    BACKWARD_ERROR_TOLERANCE,
    BELLMAN_TOLERANCE,
    CYCLE_TOLERANCE,
    DELTA,
    N,
    OMEGA,
    SHAPE,
    VALUE_TOLERANCE,
    FailClosed,
    _canonical_sha256,
    _field_sha256,
    _map_checkpoint,
    _operator_diagnostics,
    _policy_arrays,
    _policy_diagnostics,
    _scientific_code_hashes,
    _selected_identity,
    _sha256,
    _sparse_identity,
    _terminal_kfe,
    _write_json,
    checkpoint_identity,
    detect_approximate_cycle,
    detect_exact_cycle,
    normwise_backward_error,
    monotonicity_preserving_relaxation,
    primary_converged,
)
from .option_a_step import BoundOptionAInputs
from .selector import CorrectedSelectorParameters, SelectorBudget


TASK_ID = "CH5_MP4C_CORRECTED_OPTIONB_TURN2_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_20260920"
BASELINE_SHA = "a6fbf9d66d4d3603759e87f845e71bc4597c0e1c"
PASS_TERMINAL = (
    "PASS__CORRECTED_TURN2_31_PROVINCE_HOUSEHOLD_HJB_KFE_AND_ONE_TURN_INTEGRATION__"
    "RAW_TURN3_PAYOFF_READY__TURN3_NOT_RUN"
)
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_corrected_optionb_turn2_unique_closed_class_kfe_20260920_run001"
)
ENTERING_STATE_RELATIVE = Path(
    "reports/ch5_mp4c_run004_canonical_same_s_integration_replay_20260920_run001/"
    "next_state_candidate_receipt.json"
)
DISTANCE_RELATIVE = Path(
    "docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv"
)
TASK_RELATIVE = Path(
    "tasks/CH5_MP4C_CORRECTED_OPTIONB_TURN2_HOUSEHOLD_KFE_AND_ONE_TURN_"
    "INTEGRATION_20260920.md"
)
EXPECTED_ENTERING_STATE_BLOB = "85df3f0bdcc3b0bb3e7b12f0ba35dbb9abda764d"
EXPECTED_ENTERING_PAYOFF_SHA256 = "D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414"
EXPECTED_INTEGRATION_MANIFEST_SHA256 = "79C6B15340AF641A736C79D0ED7C6450E39EA495263943280B6DDBD1B094F28D"
EXPECTED_HOUSEHOLD_MANIFEST_SHA256 = "CF70E7D6A62A35F461D1A75B28F8F502B2CBDD2D94ED5D9DDFA099D821CC5EC6"
EXPECTED_SOURCE_INITIALIZATION_BLOB = "19ba32b0c5534f2726036ab8ba30fb204e359325"
EXPECTED_K1A_BLOB = "ac309b4dbe9f6b3ca1d3cfc691223600835d17b6"
EXPECTED_C1_BLOB = "ba717dfdada1b47ee44af5562d3ffa01a9de8cfe"
BEIJING_Q12_RELATIVE = Path(
    "reports/ch5_mp4c_corrected_optionb_initial_turn_31_province_household_kfe_"
    "k1a_c1_one_turn_integration_20260920_run003/household/p00_北京/checkpoint_012/"
    "q_generator.npz"
)
BEIJING_D2_RELATIVE = BEIJING_Q12_RELATIVE.with_name("d2_receipt.json")
BEIJING_METHOD_CANDIDATE_RELATIVE = Path(
    "reports/ch5_mp4c_corrected_optionb_beijing_unique_closed_class_kfe_candidate_"
    "20260920_run001"
)
BEIJING_Q12_SHA256 = "E1F55D0B755CB83D4F6A3CB4FEFD6DBC8CD4F05C6D23FC5DE00302E16B74BF20"
BEIJING_METHOD_MANIFEST_SHA256 = "278D5ECF2772FFD434130C8553EEDB2A99EE2B6E989D918D793DBCC0263CDDA0"
RUN003_MANIFEST_SHA256 = "18D62A1E388E17D3D0A7001D22998B86389C946B7136D481FB7DE11777A3388B"
BEIJING_SPECTRUM_SHA256 = "9981787A127FFCB774E0C6A312DF72A2D13C5385681927E2C0DBCDC9D0D082B6"
BEIJING_P_CLOSED_SHA256 = "649481483AA0DD54081ACD9C3419B926EF94D0C3CC3637F2412D13F31F0D0C48"
BEIJING_P_FULL_SHA256 = "5D7DA01D02C8EA711CD43AE5CD3FBF14107CE8394B97BE2E7AE1C904EDC658E0"
BEIJING_RESIDUAL_SHA256 = "B450EB9F97A3CDB66FDD24C7FE2DD9BB3997E834738572CFC1AA9BE69FFFDC71"
BEIJING_CLOSED_MEMBERS = tuple(range(200, 400)) + tuple(range(600, 800))
EXPECTED_RUN001_MANIFEST = "F447D5DF30D302963D81EB09E68BEC72C1B89F8C1DE227936533045F9A16F315"
EXPECTED_RUN002_MANIFEST = "D01A8A0CDF6808824735FEACABD7572249970DE97606A63BEA86209B5B6F531A"
MAX_UPDATES_PER_PROVINCE = 50
MAX_MAPS_PER_PROVINCE = 51
MAX_ROOTS_PER_PROVINCE = 20_000_000


def _jsonable(value: Any) -> Any:
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, Mapping):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jsonable(item) for item in value]
    return value


def _git(repository: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repository, text=True).strip()


def _blob(repository: Path, relative: Path) -> str:
    return _git(repository, "rev-parse", f"HEAD:{relative.as_posix()}")


def _git_blob_sha256(repository: Path, relative: Path) -> str:
    content = subprocess.check_output(
        ["git", "show", f"HEAD:{relative.as_posix()}"], cwd=repository
    )
    return hashlib.sha256(content).hexdigest().upper()


def _task_hashes(repository: Path) -> dict[str, str]:
    paths = list((repository / "src/ch5_two_asset_hank/corrected_diagnostic").glob("*.py"))
    paths.extend(
        repository / relative
        for relative in (
            "validators/multi_province/corrected_2018_single_turn/run.py",
            "src/ch5_two_asset_hank/multi_province/corrected_household_adapter.py",
            "src/ch5_two_asset_hank/multi_province/k1a_runtime_adapter.py",
            "src/ch5_two_asset_hank/multi_province/capital_network.py",
            "src/ch5_two_asset_hank/multi_province/c1_residual_public_asset.py",
            "src/ch5_two_asset_hank/multi_province/one_turn.py",
            "src/ch5_two_asset_hank/multi_province/firm.py",
            "src/ch5_two_asset_hank/multi_province/government_assets.py",
            "tests/test_mp4c_corrected_optionb_turn2_household_integration.py",
            ENTERING_STATE_RELATIVE.as_posix(),
            DISTANCE_RELATIVE.as_posix(),
            TASK_RELATIVE.as_posix(),
        )
    )
    return {
        path.relative_to(repository).as_posix(): _sha256(path)
        for path in sorted(set(paths))
    }


def load_initial_states(repository: Path) -> tuple[tuple[dict[str, Any], ...], dict[str, Any]]:
    """Bind and load the exact persisted entering-turn-2 states."""

    path = repository / ENTERING_STATE_RELATIVE
    if _blob(repository, ENTERING_STATE_RELATIVE) != EXPECTED_ENTERING_STATE_BLOB:
        raise FailClosed("BLOCKED__TURN2_ENTERING_STATE_BLOB_MISMATCH")
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload.get("rows", [])
    if payload.get("status") != "PASS" or len(rows) != 31:
        raise FailClosed(
            "BLOCKED__TURN2_ENTERING_STATE_RECEIPT_MISMATCH",
            {"status": payload.get("status"), "rows": len(rows)},
        )
    if payload.get("raw_next_payoff_sha256") != EXPECTED_ENTERING_PAYOFF_SHA256:
        raise FailClosed("BLOCKED__TURN2_ENTERING_PAYOFF_IDENTITY_MISMATCH")
    states: list[dict[str, Any]] = []
    receipts: list[dict[str, Any]] = []
    required = ("rah", "rb", "tau", "w", "Tt", "rb_gap")
    for expected_index, (row, province) in enumerate(zip(rows, PROVINCE_ORDER)):
        state = row.get("state")
        if not isinstance(state, dict):
            raise FailClosed(
                "BLOCKED__TURN2_ENTERING_STATE_PARSE_FAILURE",
                {"province_index": expected_index},
            )
        checks = {
            "province_index": int(row["province_index"]) == expected_index,
            "row_province": row["province"] == province,
            "state_province": state.get("name") == province,
            "classification": row.get("classification") == "TURN2_INPUT_CANDIDATE_ONLY__TURN2_NOT_RUN",
            "required_household_fields": all(key in state for key in required),
            "required_household_fields_finite": all(
                np.isfinite(float(state[key])) for key in required if key in state
            ),
        }
        if not all(checks.values()):
            raise FailClosed(
                "BLOCKED__TURN2_ENTERING_STATE_ORDER_OR_CONTENT_MISMATCH",
                {"province_index": expected_index, "checks": checks},
            )
        states.append(state)
        receipts.append(
            {
                "province_index": expected_index,
                "province": province,
                "state_sha256": _canonical_sha256(state),
                "household_inputs": {key: state[key] for key in required},
                "checks": checks,
            }
        )
    return tuple(states), {
        "status": "PASS",
        "path": ENTERING_STATE_RELATIVE.as_posix(),
        "git_blob": EXPECTED_ENTERING_STATE_BLOB,
        "file_sha256": _sha256(path),
        "raw_next_payoff_sha256": payload["raw_next_payoff_sha256"],
        "row_count": len(states),
        "province_order": list(PROVINCE_ORDER),
        "rows": receipts,
    }


def _verify_sealed_manifest(
    root: Path, expected_sha256: str, expected_entries: int
) -> dict[str, Any]:
    manifest_path = root / "sealed_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bad_paths: list[str] = []
    for entry in manifest["entries"]:
        target = root / entry["path"]
        if (
            not target.is_file()
            or target.stat().st_size != int(entry["bytes"])
            or _sha256(target) != entry["sha256"]
        ):
            bad_paths.append(str(entry["path"]))
    readback = json.loads(
        (root / "independent_readback_receipt.json").read_text(encoding="utf-8")
    )
    checks = {
        "manifest_sha256": _sha256(manifest_path) == expected_sha256,
        "entry_count": int(manifest["entry_count"]) == expected_entries,
        "all_entries_read_back": not bad_paths,
        "accepted_independent_readback": (
            readback.get("status") == "PASS" and not readback.get("bad_paths")
        ),
    }
    receipt = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "root": root.name,
        "manifest_sha256": _sha256(manifest_path),
        "entry_count": int(manifest["entry_count"]),
        "total_bytes": int(manifest["total_bytes"]),
        "checks": checks,
        "bad_paths": bad_paths,
    }
    if receipt["status"] != "PASS":
        raise FailClosed("BLOCKED__ACCEPTED_PREDECESSOR_MANIFEST_MISMATCH", receipt)
    return receipt


def _province_inputs(
    repository: Path,
    state: Mapping[str, Any],
    value: np.ndarray,
    grid: CorrectedDiagnosticGrid,
) -> BoundOptionAInputs:
    scalars = {
        "r_a": float(state["rah"]),
        "r_b": float(state["rb"]),
        "borrowing_rate_gap": float(state["rb_gap"]),
        "tau": float(state["tau"]),
        "wage": float(state["w"]),
        "transfer_income": float(state["Tt"]),
        "rho": 0.05,
        "gamma_c": 2.0,
        "phi": 5.0,
        "chi_0": 0.1,
        "chi_1": 2.0,
        "a_bar": 1.0e-6,
        "labor_weight": 1.0,
        "delta": DELTA,
    }
    parameters = CorrectedSelectorParameters(
        gamma_c=scalars["gamma_c"],
        phi=scalars["phi"],
        labor_weight=scalars["labor_weight"],
        chi_0=scalars["chi_0"],
        chi_1=scalars["chi_1"],
        a_bar=scalars["a_bar"],
    )
    seed = repository / ENTERING_STATE_RELATIVE
    binding = repository / TASK_RELATIVE
    return BoundOptionAInputs(
        seed_path=seed,
        seed_sha256=_sha256(seed),
        seed_bytes=seed.stat().st_size,
        v0_field_sha256=_field_sha256(value),
        binding_path=binding,
        binding_sha256=_sha256(binding),
        binding_bytes=binding.stat().st_size,
        grid=grid,
        v0=value,
        parameters=parameters,
        scalars=scalars,
        z_generator=np.array([[-1.0 / 3.0, 1.0 / 3.0], [1.0 / 3.0, -1.0 / 3.0]]),
    )


def _local_ledger() -> dict[str, int]:
    return {
        "new_corrected_policy_maps": 0,
        "selector_evaluations": 0,
        "scalar_root_invocations": 0,
        "interior_z_root_invocations": 0,
        "interior_a_switching_root_invocations": 0,
        "joint_switching_root_invocations": 0,
        "d2_assemblies": 0,
        "direct_hjb_solves": 0,
        "ordinary_graph_scc_summaries": 0,
        "terminal_topology_gates": 0,
        "terminal_restricted_dense_gesvd": 0,
        "terminal_full_space_dense_gesvd": 0,
        "terminal_normalized_stationary_candidates": 0,
        "terminal_q_transpose_times_p": 0,
        "scientific_retries": 0,
        "solver_substitutions": 0,
        "damping_relaxation_adaptive_delta_continuation_calls": 0,
        "matlab_production_ge_irf_results_calls": 0,
    }


def _new_ledger() -> dict[str, Any]:
    return {
        "source_native_initializations": 0,
        "scalar_labor_roots_attempted": 0,
        "scalar_labor_roots_returned": 0,
        "corrected_policy_maps": 0,
        "selector_evaluations": 0,
        "scalar_selector_root_invocations": 0,
        "interior_z_root_invocations": 0,
        "interior_a_switching_root_invocations": 0,
        "joint_switching_root_invocations": 0,
        "d2_q_assemblies": 0,
        "direct_hjb_updates": 0,
        "hjb_checkpoint_evaluations_after_update": 0,
        "scc_decompositions": 0,
        "restricted_dense_scipy_linalg_svd_gesvd": 0,
        "full_space_800_dense_scipy_linalg_svd_gesvd": 0,
        "normalized_stationary_candidates": 0,
        "q_transpose_times_p": 0,
        "corrected_aggregate_evaluations": 0,
        "household_batch_constructions": 0,
        "source_faithful_labor_reconstructions": 0,
        "k1a_capital_network_allocations": 0,
        "c1_residual_govinv_constructions": 0,
        "firm_evaluations": 0,
        "composite_wage_batches": 0,
        "monetary_assignments": 0,
        "fiscal_diagnostic_batches": 0,
        "raw_next_payoff_same_s_constructions": 0,
        "turn3_household_calls": 0,
        "third_outer_turns": 0,
        "k1b_feedback_calls": 0,
        "k2_calls": 0,
        "adaptive_controller_calls": 0,
        "matlab_scientific_calls": 0,
        "ge_annual_shock_irf_welfare_results_calls": 0,
        "scientific_retries": 0,
        "solver_substitutions": 0,
        "damping_relaxation_adaptive_delta_clipping_artificial_diffusion_continuation_calls": 0,
        "payoff_clipping_annualization_rescaling_smoothing_risk_adjustment_zscore_calls": 0,
    }


def _check_ledger(ledger: Mapping[str, Any]) -> None:
    ceilings = {
        "source_native_initializations": 31,
        "scalar_labor_roots_attempted": 24_800,
        "scalar_labor_roots_returned": 24_800,
        "corrected_policy_maps": 1_581,
        "selector_evaluations": 1_264_800,
        "d2_q_assemblies": 1_581,
        "direct_hjb_updates": 1_550,
        "hjb_checkpoint_evaluations_after_update": 1_550,
        "scc_decompositions": 31,
        "restricted_dense_scipy_linalg_svd_gesvd": 31,
        "full_space_800_dense_scipy_linalg_svd_gesvd": 0,
        "normalized_stationary_candidates": 31,
        "q_transpose_times_p": 31,
        "corrected_aggregate_evaluations": 31,
        "household_batch_constructions": 1,
        "source_faithful_labor_reconstructions": 1,
        "k1a_capital_network_allocations": 1,
        "c1_residual_govinv_constructions": 1,
        "firm_evaluations": 31,
        "composite_wage_batches": 1,
        "monetary_assignments": 1,
        "fiscal_diagnostic_batches": 1,
        "raw_next_payoff_same_s_constructions": 1,
        "turn3_household_calls": 0,
        "third_outer_turns": 0,
        "k1b_feedback_calls": 0,
        "k2_calls": 0,
        "adaptive_controller_calls": 0,
        "matlab_scientific_calls": 0,
        "ge_annual_shock_irf_welfare_results_calls": 0,
        "scientific_retries": 0,
        "solver_substitutions": 0,
        "damping_relaxation_adaptive_delta_clipping_artificial_diffusion_continuation_calls": 0,
        "payoff_clipping_annualization_rescaling_smoothing_risk_adjustment_zscore_calls": 0,
    }
    breaches = {
        name: {"actual": int(ledger[name]), "ceiling": ceiling}
        for name, ceiling in ceilings.items()
        if int(ledger[name]) > ceiling
    }
    if breaches:
        raise FailClosed("BLOCKED__SCIENTIFIC_LEDGER_CEILING", {"breaches": breaches})


def _accumulate_local(ledger: dict[str, Any], before: Mapping[str, int], after: Mapping[str, int]) -> None:
    mapping = {
        "new_corrected_policy_maps": "corrected_policy_maps",
        "selector_evaluations": "selector_evaluations",
        "scalar_root_invocations": "scalar_selector_root_invocations",
        "interior_z_root_invocations": "interior_z_root_invocations",
        "interior_a_switching_root_invocations": "interior_a_switching_root_invocations",
        "joint_switching_root_invocations": "joint_switching_root_invocations",
        "d2_assemblies": "d2_q_assemblies",
        "terminal_topology_gates": "scc_decompositions",
        "terminal_restricted_dense_gesvd": "restricted_dense_scipy_linalg_svd_gesvd",
        "terminal_full_space_dense_gesvd": "full_space_800_dense_scipy_linalg_svd_gesvd",
        "terminal_normalized_stationary_candidates": "normalized_stationary_candidates",
        "terminal_q_transpose_times_p": "q_transpose_times_p",
    }
    for local_name, total_name in mapping.items():
        ledger[total_name] += int(after[local_name]) - int(before[local_name])
    _check_ledger(ledger)


def _terminal_kfe_with_accounting(
    checkpoint: int,
    q: sparse.csr_matrix,
    q_one_bound: float,
    province_root: Path,
    local: dict[str, int],
    ledger: dict[str, Any],
) -> dict[str, Any]:
    """Accumulate consumed terminal-KFE calls on both return and exception paths."""

    before = dict(local)
    try:
        return _terminal_kfe(checkpoint, q, q_one_bound, province_root, local)
    finally:
        _accumulate_local(ledger, before, local)


def _compact_checkpoint(
    directory: Path,
    rows: list[dict[str, Any]],
    arrays: dict[str, np.ndarray],
    policy: Mapping[str, Any],
    operator: Mapping[str, Any],
    metrics: Mapping[str, Any],
) -> None:
    identities = [_selected_identity(row) for row in rows]
    np.savez_compressed(directory / "selected_policy_arrays.npz", **arrays)
    compact = {
        "selector_outcome_count": len(rows),
        "canonical_policy_identity": _canonical_sha256(identities),
        "selected_field_sha256": {
            name: _field_sha256(value) for name, value in sorted(arrays.items())
        },
        "active_constraint_counts": dict(sorted(Counter(
            "+".join(map(str, row.get("active_constraints", []))) or "none" for row in rows
        ).items())),
        "transfer_branch_counts": dict(sorted(Counter(str(row["transfer_branch"]) for row in rows).items())),
        "switching": _switching_statistics(directory),
        "policy_diagnostics": policy,
        "operator_diagnostics": operator,
        "checkpoint_metrics": metrics,
    }
    _write_json(directory / "compact_checkpoint_receipt.json", compact)
    for path in directory.glob("cell_*.json"):
        path.unlink()


def _checkpoint_diagnostics(
    rows: list[dict[str, Any]],
    arrays: dict[str, np.ndarray],
    q: sparse.csr_matrix,
    previous_rows: list[dict[str, Any]] | None,
    previous_arrays: dict[str, np.ndarray] | None,
    previous_q: sparse.csr_matrix | None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Route checkpoint 0 to current-only diagnostics and later checkpoints to comparisons."""

    previous = (previous_rows, previous_arrays, previous_q)
    if all(item is None for item in previous):
        identities = [_selected_identity(row) for row in rows]
        policy = {
            "diagnostic_mode": "CURRENT_ONLY__NO_PREVIOUS_CHECKPOINT",
            "identity_sha256": _canonical_sha256(identities),
            "identity_change_count": None,
            "identity_change_flat_f_zero_based": None,
            "transfer_branch_counts": dict(sorted(Counter(
                str(row["transfer_branch"]) for row in rows
            ).items())),
            "active_constraint_counts": dict(sorted(Counter(
                "+".join(map(str, row.get("active_constraints", []))) or "none"
                for row in rows
            ).items())),
            "interior_z_marker_counts": dict(sorted(Counter(
                str(identity["interior_z_marker"] or "none") for identity in identities
            ).items())),
            "selected_field_sha256": {
                name: _field_sha256(value) for name, value in sorted(arrays.items())
            },
            "continuous_field_max_abs_change": {
                name: None for name in ("c", "l", "d", "g_b", "g_a", "q_b", "q_a", "utility")
            },
            "previous_checkpoint_comparison": None,
        }
        operator = {
            "diagnostic_mode": "CURRENT_ONLY__NO_PREVIOUS_CHECKPOINT",
            "identity": _sparse_identity(q),
            "nnz": int(sparse.csr_matrix(q).nnz),
            "sparsity_pattern_same_as_previous": None,
            "sparsity_pattern_changed": None,
            "difference_nnz": None,
            "difference_max_abs_entry": None,
            "difference_inf_norm": None,
            "previous_checkpoint_comparison": None,
        }
        return policy, operator
    if any(item is None for item in previous):
        raise FailClosed(
            "BLOCKED__PARTIAL_PREVIOUS_CHECKPOINT_DIAGNOSTICS_STATE",
            {"previous_rows": previous_rows is not None,
             "previous_arrays": previous_arrays is not None,
             "previous_q": previous_q is not None},
        )
    return (
        _policy_diagnostics(rows, previous_rows, arrays, previous_arrays),
        _operator_diagnostics(q, previous_q),
    )


def _direct_update(
    directory: Path,
    value: np.ndarray,
    utility: np.ndarray,
    q: sparse.csr_matrix,
    rho: float,
    b_nodes: np.ndarray,
    ledger: dict[str, Any],
) -> tuple[np.ndarray, dict[str, Any]]:
    matrix = (rho + 1.0 / DELTA) * sparse.eye(N, format="csr") - q
    rhs = utility.ravel(order="F") + value.ravel(order="F") / DELTA
    ledger["direct_hjb_updates"] += 1
    _check_ledger(ledger)
    try:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            solved = np.asarray(sparse_linalg.spsolve(matrix, rhs), dtype=float)
    except Exception as exc:
        raise FailClosed(
            "FAIL__DIRECT_HJB_SOLVE_EXCEPTION",
            {"type": type(exc).__name__, "message": str(exc)},
        ) from exc
    warning_rows = [{"category": row.category.__name__, "message": str(row.message)} for row in caught]
    if warning_rows or solved.shape != (N,) or not np.all(np.isfinite(solved)):
        raise FailClosed(
            "FAIL__DIRECT_HJB_SOLVE_WARNING_SHAPE_OR_NONFINITE",
            {"warnings": warning_rows, "shape": list(solved.shape)},
        )
    backward = normwise_backward_error(matrix, solved, rhs)
    residual = backward.pop("residual")
    full_next_value = solved.reshape(SHAPE, order="F")
    passed = bool(
        np.isfinite(backward["normwise_backward_error"])
        and backward["normwise_backward_error"] <= BACKWARD_ERROR_TOLERANCE
    )
    np.savez_compressed(
        directory / "direct_update_arrays.npz",
        matrix_data=matrix.data,
        matrix_indices=matrix.indices,
        matrix_indptr=matrix.indptr,
        rhs=rhs,
        next_value=full_next_value,
        residual=residual,
    )
    receipt = {
        "status": "PASS" if passed else "FAIL",
        "solver": "scipy.sparse.linalg.spsolve",
        "delta": DELTA,
        "warnings": warning_rows,
        **backward,
        "backward_error_threshold_inclusive": BACKWARD_ERROR_TOLERANCE,
        "rhs_sha256": _field_sha256(rhs),
        "next_value_sha256": _field_sha256(full_next_value),
        "residual_sha256": _field_sha256(residual),
    }
    _write_json(directory / "direct_solve_receipt.json", receipt)
    if not passed:
        raise FailClosed("FAIL__DIRECT_HJB_BACKWARD_ERROR", receipt)
    accepted_next_value, relaxation_receipt = monotonicity_preserving_relaxation(
        value, full_next_value, b_nodes
    )
    _write_json(directory / "relaxation_receipt.json", relaxation_receipt)
    return accepted_next_value, receipt


def _solve_province(
    repository: Path,
    output: Path,
    index: int,
    province: str,
    state: Mapping[str, Any],
    grid: CorrectedDiagnosticGrid,
    native_grid: Any,
    native_params: Any,
    task_hashes: dict[str, str],
    core_hashes: dict[str, str],
    ledger: dict[str, Any],
) -> dict[str, Any]:
    province_root = output / "household" / f"p{index:02d}_{province}"
    province_root.mkdir(parents=True, exist_ok=False)
    ledger["source_native_initializations"] += 1

    def root_attempt() -> None:
        ledger["scalar_labor_roots_attempted"] += 1
        _check_ledger(ledger)

    def root_return() -> None:
        ledger["scalar_labor_roots_returned"] += 1
        _check_ledger(ledger)

    value, native_labor = source_initial_arrays(
        state, native_grid, native_params, root_attempt, root_return
    )
    if not np.all(np.isfinite(value)) or not np.all(np.isfinite(native_labor)):
        raise FailClosed("FAIL__SOURCE_NATIVE_INITIALIZATION_NONFINITE", {"province": province})
    np.savez_compressed(province_root / "native_initialization_arrays.npz", value=value, labor=native_labor)
    _write_json(
        province_root / "native_initialization_receipt.json",
        {
            "province_index": index,
            "province": province,
            "value_sha256": _field_sha256(value),
            "labor_sha256": _field_sha256(native_labor),
            "labor_roots": 800,
            "initialization_retries": 0,
        },
    )
    inputs = _province_inputs(repository, state, value, grid)
    budget = SelectorBudget(
        max_selector_evaluations=MAX_MAPS_PER_PROVINCE * N,
        max_root_invocations=MAX_ROOTS_PER_PROVINCE,
        max_interior_z_root_invocations=MAX_ROOTS_PER_PROVINCE,
        max_interior_a_switching_root_invocations=MAX_MAPS_PER_PROVINCE * N,
        max_joint_switching_root_invocations=MAX_MAPS_PER_PROVINCE * N,
    )
    local = _local_ledger()
    values = [np.array(value, copy=True, order="F")]
    identities: list[str] = []
    previous_rows = None
    previous_arrays = None
    previous_q = None
    final: dict[str, Any] | None = None
    for checkpoint in range(MAX_MAPS_PER_PROVINCE):
        if _task_hashes(repository) != task_hashes:
            raise FailClosed("BLOCKED__SCIENTIFIC_CODE_CHANGED_AFTER_FREEZE", {"province": province})
        directory = province_root / f"checkpoint_{checkpoint:03d}"
        before = dict(local)
        rows, arrays, q, d2 = _map_checkpoint(
            repository, province_root, checkpoint, values[-1], inputs, budget, local, core_hashes
        )
        _accumulate_local(ledger, before, local)
        policy, operator = _checkpoint_diagnostics(
            rows, arrays, q, previous_rows, previous_arrays, previous_q
        )
        b_value = float(np.linalg.norm(
            inputs.scalars["rho"] * values[-1].ravel(order="F")
            - arrays["utility"].ravel(order="F")
            - np.asarray(q @ values[-1].ravel(order="F")).ravel(),
            ord=np.inf,
        ))
        q_identity = _sparse_identity(q)
        identity = checkpoint_identity(
            _field_sha256(values[-1]), str(policy["identity_sha256"]), q_identity
        )
        identities.append(identity)
        metrics: dict[str, Any] = {
            "province_index": index,
            "province": province,
            "checkpoint": checkpoint,
            "updates_completed": checkpoint,
            "value_sha256": _field_sha256(values[-1]),
            "policy_identity_sha256": policy["identity_sha256"],
            "q_identity": q_identity,
            "checkpoint_identity_sha256": identity,
            "B_same_value": b_value,
            "D_value_change": None,
            "primary_convergence_pass": False,
            "d2_status": d2["status"],
            "d2_receipt": d2,
            "selector_root_ledger": {
                "selector_evaluations": int(local["selector_evaluations"]),
                "scalar_root_invocations": int(local["scalar_root_invocations"]),
                "interior_z_root_invocations": int(local["interior_z_root_invocations"]),
                "interior_a_switching_root_invocations": int(local["interior_a_switching_root_invocations"]),
                "joint_switching_root_invocations": int(local["joint_switching_root_invocations"]),
            },
        }
        if checkpoint > 0:
            ledger["hjb_checkpoint_evaluations_after_update"] += 1
            d_value = float(np.linalg.norm(
                (values[-1] - values[-2]).ravel(order="F"), ord=np.inf
            ))
            converged = primary_converged(b_value, d_value)
            metrics.update(
                D_value_change=d_value,
                primary_convergence_pass=converged,
                convergence_thresholds={"B": BELLMAN_TOLERANCE, "D": VALUE_TOLERANCE},
            )
            if converged:
                metrics["disposition"] = "HJB_CONVERGED__NO_FURTHER_UPDATE"
            else:
                exact = detect_exact_cycle(identities)
                approximate = detect_approximate_cycle(values, tolerance=CYCLE_TOLERANCE)
                cycle = {
                    "primary_convergence_evaluated_first": True,
                    "exact_period": exact,
                    "approximate_period_2_or_3": approximate,
                    "approximate_norm": "||vec_F(V_j-V_(j-k))||_inf",
                }
                _write_json(directory / "cycle_detection_receipt.json", cycle)
                metrics["cycle"] = cycle
                if exact is not None:
                    metrics["disposition"] = "EXACT_CYCLE"
                elif approximate is not None:
                    metrics["disposition"] = f"APPROXIMATE_PERIOD_{approximate['period']}_CYCLE"
                elif checkpoint == MAX_UPDATES_PER_PROVINCE:
                    metrics["disposition"] = "UPDATE_50_CEILING_WITHOUT_CONVERGENCE"
                else:
                    metrics["disposition"] = "CONTINUE_TO_NEXT_UPDATE"
        else:
            metrics["disposition"] = "INITIAL_MAP__UPDATE_REQUIRED"
        _compact_checkpoint(directory, rows, arrays, policy, operator, metrics)
        _write_json(directory / "checkpoint_manifest.json", metrics)
        np.savez_compressed(
            directory / "checkpoint_arrays.npz",
            value=values[-1], utility=arrays["utility"], mu_b=arrays["g_b"], mu_a=arrays["g_a"],
        )
        if checkpoint > 0 and metrics["primary_convergence_pass"]:
            kfe = _terminal_kfe_with_accounting(
                checkpoint, q, float(d2["arithmetic_tolerance"]), province_root, local, ledger
            )
            if (
                local["terminal_topology_gates"] != 1
                or local["terminal_restricted_dense_gesvd"] != 1
                or local["terminal_full_space_dense_gesvd"] != 0
            ):
                raise FailClosed("FAIL__KFE_EXACTLY_ONCE_ACCOUNTING", {"province": province})
            with np.load(province_root / "terminal_kfe/stationary_mass_arrays.npz", allow_pickle=False) as mass:
                p = np.asarray(mass["p"])
                g = np.asarray(mass["g"])
            effective = np.broadcast_to(
                float(state["rah"])
                * (1.0 - 0.1 * (grid.a[None, :, None] / 10.0) ** 9),
                SHAPE,
            )
            ledger["corrected_aggregate_evaluations"] += 1
            aggregates = evaluate_corrected_household_aggregates(
                CorrectedHouseholdAggregateInputs(
                    consumption=arrays["c"], labor=arrays["l"],
                    b_grid=grid.b, a_grid=grid.a, z_grid=grid.z,
                    effective_r_a=effective,
                    probability_mass=p.reshape(SHAPE, order="F"),
                    density=g.reshape(SHAPE, order="F"), omega=OMEGA,
                    source_r_a=float(state["rah"]),
                )
            )
            aggregate_receipt = {
                name: asdict(getattr(aggregates, name))
                for name in ("Ct", "Lt", "At", "Bt", "total_assets", "AtTax")
            }
            _write_json(province_root / "stationary_aggregate_receipt.json", aggregate_receipt)
            final = {
                "province_index": index,
                "province": province,
                "checkpoint": checkpoint,
                "updates": checkpoint,
                "B": b_value,
                "D": metrics["D_value_change"],
                "backward_error_max": max(
                    json.loads(path.read_text(encoding="utf-8"))["normwise_backward_error"]
                    for path in province_root.glob("checkpoint_*/direct_solve_receipt.json")
                ),
                "policy": policy,
                "operator": operator,
                "kfe": kfe,
                "aggregates": aggregate_receipt,
                "local_ledger": dict(local),
            }
            _write_json(province_root / "province_terminal_receipt.json", final)
            break
        if checkpoint > 0 and metrics["disposition"] != "CONTINUE_TO_NEXT_UPDATE":
            raise FailClosed(
                "FAIL__PROVINCE_HJB_TERMINAL_NONCONVERGENCE",
                {"province_index": index, "province": province, "checkpoint": checkpoint, "metrics": metrics},
            )
        next_value, solve = _direct_update(
            directory,
            values[-1],
            arrays["utility"],
            q,
            inputs.scalars["rho"],
            grid.b,
            ledger,
        )
        _write_json(directory / "direct_solve_receipt.json", {
            **solve, "checkpoint_from": checkpoint, "checkpoint_to": checkpoint + 1
        })
        values.append(next_value)
        previous_rows, previous_arrays, previous_q = rows, arrays, q
    if final is None:
        raise FailClosed("FAIL__PROVINCE_HJB_TERMINAL_NONCONVERGENCE", {"province": province})
    return final


def _one_turn_inputs(
    repository: Path,
    states: tuple[dict[str, Any], ...],
    batch: PreFrozenHouseholdOutputBatch,
) -> OneTurnInputs:
    productivity = np.array([float(state["Yt"]) / float(state["Lt"]) for state in states])
    phi = 1.0 + 0.3 * (productivity[:, None] - productivity[None, :]) / (
        productivity[:, None] + productivity[None, :]
    )
    distance = load_accepted_distance_score(repository / DISTANCE_RELATIVE)
    wedges = 0.5 * distance
    params = MappingProxyType({
        "ga": 2.0, "phi_l": 5.0, "alphal": 1.0, "epsilon": 10.0,
        "theta": 100.0, "delta": 0.025, "istar": 0.015, "rho_pi": 1.25,
        "totalpit": 0.02, "epsilon_pi": 0.0,
    })
    return OneTurnInputs(PROVINCE_ORDER, states, params, phi, wedges, batch)


def same_s_raw_next_payoff(raw_ra0_by_destination: object, shares_destination_origin: object) -> np.ndarray:
    """Canonical ordered ``math.fsum`` over destination for every origin."""

    raw = np.asarray(raw_ra0_by_destination, dtype=float)
    shares = np.asarray(shares_destination_origin, dtype=float)
    if raw.shape != (31,) or shares.shape != (31, 31):
        raise ValueError("raw-ra0 and S must use the exact 31-province axes")
    if not np.all(np.isfinite(raw)) or not np.all(np.isfinite(shares)):
        raise ValueError("raw-ra0 and S must be finite")
    result = np.asarray([
        math.fsum(float(raw[j]) * float(shares[j, i]) for j in range(31))
        for i in range(31)
    ], dtype=np.float64)
    if not np.all(np.isfinite(result)):
        raise ValueError("raw next payoff must be finite")
    return result


def _movement_diagnostics(
    old_states: tuple[dict[str, Any], ...],
    next_rows: list[dict[str, Any]],
    raw_ra0_turn2: np.ndarray,
) -> dict[str, Any]:
    """Descriptive movement only; it is never an outer-convergence gate."""

    fields = ("rah", "w", "rb", "Ct", "At", "Bt", "AtTax", "Kt", "Yt", "GovInv")
    diagnostics: dict[str, Any] = {
        "classification": "DESCRIPTIVE_ONLY__NOT_OUTER_CONVERGENCE",
        "relative_denominator": "max(abs(entering_value),1e-12)",
        "fields": {},
    }
    next_states = [row["state"] for row in next_rows]
    for field in fields:
        old = np.asarray([float(row[field]) for row in old_states], dtype=np.float64)
        new = np.asarray([float(row[field]) for row in next_states], dtype=np.float64)
        absolute = np.abs(new - old)
        relative = absolute / np.maximum(np.abs(old), 1.0e-12)
        index = int(np.argmax(absolute))
        diagnostics["fields"][field] = {
            "max_absolute_change": float(absolute[index]),
            "median_absolute_change": float(np.median(absolute)),
            "max_relative_change": float(np.max(relative)),
            "max_absolute_change_province_index": index,
            "max_absolute_change_province": PROVINCE_ORDER[index],
        }
    old_raw = np.asarray([float(row["ra0"]) for row in old_states], dtype=np.float64)
    absolute = np.abs(raw_ra0_turn2 - old_raw)
    relative = absolute / np.maximum(np.abs(old_raw), 1.0e-12)
    index = int(np.argmax(absolute))
    diagnostics["fields"]["raw_ra0"] = {
        "max_absolute_change": float(absolute[index]),
        "median_absolute_change": float(np.median(absolute)),
        "max_relative_change": float(np.max(relative)),
        "max_absolute_change_province_index": index,
        "max_absolute_change_province": PROVINCE_ORDER[index],
    }
    return diagnostics


def integrate_one_turn(
    repository: Path,
    states: tuple[dict[str, Any], ...],
    batch: PreFrozenHouseholdOutputBatch,
    ledger: dict[str, Any],
) -> dict[str, Any]:
    inputs = _one_turn_inputs(repository, states, batch)
    household = inputs.household_outputs
    provinces = inputs.old_provinces
    ledger["source_faithful_labor_reconstructions"] += 1
    migration = source.reconstruct_migration_labor(source.MigrationLaborInputs(
        consumption_by_origin=household.ct,
        population_by_origin=[row["N"] for row in provinces],
        old_firm_wage_by_destination=[row["wjt"] for row in provinces],
        tax_by_origin=[row["tau"] for row in provinces],
        phi_destination_origin=inputs.phi_destination_origin,
        migration_wedge_destination_origin=inputs.migration_wedge_destination_origin,
        gamma_c=inputs.params["ga"], phi_l=inputs.params["phi_l"],
    ))
    ledger["k1a_capital_network_allocations"] += 1
    distance = load_accepted_distance_score(repository / DISTANCE_RELATIVE)
    capital = allocate_k1a_capital(
        CapitalAllocationInputs(
            illiquid_assets_at=household.at,
            population=[row["N"] for row in provinces],
            inter_province_ratio=[row["inter_prv_ratio"] for row in provinces],
            old_firm_return_ra=[row["ra"] for row in provinces],
        ),
        K1ARuntimeConfig(PROVINCE_ORDER, distance, beta_distance=2.0, beta_return=0.0),
    )
    ledger["c1_residual_govinv_constructions"] += 1
    accounting = residual_government_asset_levels(
        Ktarget_MU=[row["Kt0"] for row in provinces],
        Kprivate_current_MU=capital.kt_supply,
        province_order=PROVINCE_ORDER,
    )
    firms = []
    for index, province in enumerate(provinces):
        firm_source = dict(province)
        firm_source["GovInv"] = float(accounting.GovInv_residual_MU[index])
        firm_source["AtTax"] = float(household.at_tax[index])
        firm_source["Lt_prev"] = float(household.household_lt[index])
        ledger["firm_evaluations"] += 1
        firms.append(source.evaluate_firm(
            firm_source, float(capital.kt_supply[index]),
            float(migration.lt_supply[index]), inputs.params,
        ))
        expected_k = float(accounting.firm_K_accounting_MU[index])
        if abs(float(firms[-1].Kt) - expected_k) > 1e-12 * max(1.0, abs(expected_k)):
            raise FailClosed(
                "FAIL__C1_FIRM_CAPITAL_ACCOUNTING",
                {"province_index": index, "province": PROVINCE_ORDER[index]},
            )
    ledger["composite_wage_batches"] += 1
    wages = source.composite_household_wages(
        provinces, [firm.wjt for firm in firms],
        inputs.phi_destination_origin, inputs.migration_wedge_destination_origin,
        phi_l=inputs.params["phi_l"], alphal=inputs.params["alphal"],
    )
    ledger["monetary_assignments"] += 1
    monetary = source.taylor_assignment(
        istar=inputs.params["istar"], rho_pi=inputs.params["rho_pi"],
        totalpit=inputs.params["totalpit"], epsilon_pi=inputs.params["epsilon_pi"],
    )
    ledger["fiscal_diagnostic_batches"] += 1
    fiscal = source.national_fiscal_diagnostics(
        [firm.Govinc for firm in firms], household.bt, monetary.rb,
        [row["N"] for row in provinces],
    )
    raw_ra0 = np.array([firm.ra0 for firm in firms])
    shares = capital.network.portfolio_shares_destination_origin
    ledger["raw_next_payoff_same_s_constructions"] += 1
    rah_next = same_s_raw_next_payoff(raw_ra0, shares)
    terms = raw_ra0[:, None] * shares
    replay = raw_ra0 @ shares
    wealth = capital.network.origin_private_wealth
    private = capital.network.destination_private_productive_capital
    k_scale = max(1.0, float(np.sum(wealth)))
    checks = {
        "source_update_order": C1_UPDATE_ORDER == (
            "pre_frozen_household_outputs", "source_faithful_migration_labor",
            "at_only_private_productive_capital", "c1_residual_public_asset_level",
            "firm", "household_composite_wage", "taylor_rb", "fiscal_diagnostics",
        ),
        "share_columns": bool(np.allclose(np.sum(shares, axis=0), 1.0, rtol=0.0, atol=1e-12)),
        "national_private_capital": abs(float(np.sum(private) - np.sum(wealth))) <= 1e-12 * k_scale,
        "home_retained": bool(np.allclose(
            capital.network.domestic_retained_capital_by_origin,
            (1.0 - np.array([row["inter_prv_ratio"] for row in provinces])) * wealth,
            rtol=0.0, atol=1e-12 * k_scale,
        )),
        "c1_residual": bool(np.array_equal(
            accounting.GovInv_residual_MU,
            np.maximum(np.array([row["Kt0"] for row in provinces]) - private, 0.0),
        )),
        "raw_next_same_s": bool(np.all(np.isfinite(rah_next))),
        "all_firm_outputs_finite": bool(np.all(np.isfinite([
            value for firm in firms for value in (firm.Kt, firm.Yt, firm.wjt, firm.ra0, firm.ra)
        ]))),
    }
    if not all(checks.values()):
        raise FailClosed("FAIL__ONE_TURN_INTEGRATION_ACCOUNTING", {"checks": checks})
    _check_ledger(ledger)
    next_states = []
    for i in range(31):
        state = dict(provinces[i])
        state.update({
            "Ct": float(batch.ct[i]), "At": float(batch.at[i]), "Bt": float(batch.bt[i]),
            "AtTax": float(batch.at_tax[i]), "convergent": True,
            "Lt_supply": float(migration.lt_supply[i]),
            "Kt_supply": float(capital.kt_supply[i]),
            "rah": float(rah_next[i]), "w": float(wages[i]),
            "it": float(monetary.it), "rb": float(monetary.rb),
            "Yt_1": float(provinces[i]["Yt"]), "Kt_prev": float(firms[i].Kt),
            "Lt_prev": float(firms[i].Lt), "Zt_1": float(provinces[i]["Zt"]),
            "pit_1": float(provinces[i]["pit"]),
            "GovInv": float(accounting.GovInv_residual_MU[i]),
        })
        state.update(firms[i].as_source_dict())
        next_states.append({
            "province_index": i, "province": PROVINCE_ORDER[i],
            "classification": "TURN3_INPUT_CANDIDATE_ONLY__TURN3_NOT_RUN",
            "raw_ra0_turn2": float(raw_ra0[i]),
            "firm_ra_used": float(firms[i].ra),
            "state": state,
        })
    movement = _movement_diagnostics(states, next_states, raw_ra0)
    return {
        "status": "PASS",
        "checks": checks,
        "beta_distance": 2.0,
        "beta_return": 0.0,
        "orientation": "destination_by_origin",
        "portfolio_shares_sha256": _field_sha256(shares),
        "portfolio_shares_destination_origin": shares.tolist(),
        "ordered_product_terms": terms.tolist(),
        "raw_ra0_turn2_by_destination": raw_ra0.tolist(),
        "raw_ra0_turn2_sha256": _field_sha256(raw_ra0),
        "portfolio_shares_sha256": _field_sha256(shares),
        "ordered_product_terms_sha256": _field_sha256(terms),
        "rah_turn3_raw_by_origin": rah_next.tolist(),
        "rah_turn3_sha256": _field_sha256(rah_next),
        "blas_diagnostic": replay.tolist(),
        "canonical_vs_blas_max_abs_difference": float(np.max(np.abs(rah_next - replay), initial=0.0)),
        "canonical_vs_blas_bitwise_equal_count": int(np.count_nonzero(rah_next == replay)),
        "blas_is_acceptance_gate": False,
        "origin_private_wealth_total": float(np.sum(wealth)),
        "destination_private_capital_total": float(np.sum(private)),
        "national_private_capital_residual": float(np.sum(private) - np.sum(wealth)),
        "GovInv_C1_total": float(np.sum(accounting.GovInv_residual_MU)),
        "next_states": next_states,
        "movement_diagnostics": movement,
        "firm_diagnostics": [
            {"province_index": i, "province": PROVINCE_ORDER[i], "K": firm.Kt,
             "Y": firm.Yt, "wage": firm.wjt, "raw_ra0": firm.ra0, "used_ra": firm.ra}
            for i, firm in enumerate(firms)
        ],
        "labor_destination_total": float(np.sum(migration.lt_supply)),
    }


def _manifest(output: Path) -> dict[str, Any]:
    entries = [
        {"path": path.relative_to(output).as_posix(), "bytes": path.stat().st_size, "sha256": _sha256(path)}
        for path in sorted(output.rglob("*"))
        if path.is_file() and path.name not in {"sealed_manifest.json", "independent_readback_receipt.json"}
    ]
    document = {
        "schema": "CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_COMPACT_EVIDENCE_V1",
        "entry_count": len(entries),
        "total_bytes": sum(int(row["bytes"]) for row in entries),
        "entries": entries,
    }
    _write_json(output / "sealed_manifest.json", document)
    return document


def _readback(output: Path) -> dict[str, Any]:
    manifest = json.loads((output / "sealed_manifest.json").read_text(encoding="utf-8"))
    bad = []
    for row in manifest["entries"]:
        path = output / row["path"]
        if not path.is_file() or path.stat().st_size != row["bytes"] or _sha256(path) != row["sha256"]:
            bad.append(row["path"])
    receipt = {
        "status": "PASS" if not bad else "FAIL",
        "manifest_sha256": _sha256(output / "sealed_manifest.json"),
        "entry_count": len(manifest["entries"]),
        "total_bytes": manifest["total_bytes"],
        "bad_paths": bad,
        "scientific_calls": 0,
    }
    _write_json(output / "independent_readback_receipt.json", receipt)
    if bad:
        raise FailClosed("BLOCKED__EVIDENCE_READBACK_FAILURE", {"bad_paths": bad})
    return receipt


def _read_junit(path: Path) -> dict[str, Any]:
    root = ET.parse(path).getroot()
    tests = int(root.attrib.get("tests", sum(int(row.attrib.get("tests", 0)) for row in root)))
    failures = int(root.attrib.get("failures", sum(int(row.attrib.get("failures", 0)) for row in root)))
    errors = int(root.attrib.get("errors", sum(int(row.attrib.get("errors", 0)) for row in root)))
    if tests <= 0 or failures or errors:
        raise FailClosed("BLOCKED__FOCUSED_TEST_GATE", {"tests": tests, "failures": failures, "errors": errors})
    return {"status": "PASS", "tests": tests, "failures": failures, "errors": errors}


def _predecessor_lineage(repository: Path) -> dict[str, Any]:
    run001_root = repository / RUN001_OUTPUT_RELATIVE
    run002_root = repository / RUN002_OUTPUT_RELATIVE

    def load(root: Path) -> tuple[Path, dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
        manifest_path = root / "sealed_manifest.json"
        return (
            manifest_path,
            json.loads(manifest_path.read_text(encoding="utf-8")),
            json.loads((root / "scientific_ledger.json").read_text(encoding="utf-8")),
            json.loads((root / "terminal_receipt.json").read_text(encoding="utf-8")),
            json.loads((root / "independent_readback_receipt.json").read_text(encoding="utf-8")),
        )

    run001_manifest_path, run001_manifest, run001_ledger, run001_terminal, run001_readback = load(run001_root)
    run002_manifest_path, run002_manifest, run002_ledger, run002_terminal, run002_readback = load(run002_root)
    run002_reconciliation = json.loads(
        (run002_root / "post_terminal_zero_science_diagnostic_receipt.json").read_text(encoding="utf-8")
    )
    expected_run001_counts = {
        "source_native_initializations": 1,
        "scalar_labor_roots_attempted": 800,
        "scalar_labor_roots_returned": 800,
        "corrected_policy_maps": 1,
        "selector_evaluations": 800,
        "scalar_selector_root_invocations": 483,
        "interior_z_root_invocations": 206,
        "d2_q_assemblies": 1,
        "direct_hjb_updates": 0,
        "scc_decompositions": 0,
        "dense_scipy_linalg_svd_gesvd": 0,
        "corrected_aggregate_evaluations": 0,
        "firm_evaluations": 0,
        "scientific_retries": 0,
        "turn2_household_calls": 0,
    }
    expected_run002_counts = {
        "source_native_initializations": 1,
        "scalar_labor_roots_attempted": 800,
        "scalar_labor_roots_returned": 800,
        "corrected_policy_maps": 13,
        "selector_evaluations": 10_400,
        "scalar_selector_root_invocations": 4_148,
        "interior_z_root_invocations": 760,
        "interior_a_switching_root_invocations": 17,
        "joint_switching_root_invocations": 1,
        "d2_q_assemblies": 13,
        "direct_hjb_updates": 12,
        "hjb_checkpoint_evaluations_after_update": 12,
        "scc_decompositions": 0,
        "dense_scipy_linalg_svd_gesvd": 0,
        "normalized_stationary_candidates": 0,
        "q_transpose_times_p": 0,
        "corrected_aggregate_evaluations": 0,
        "firm_evaluations": 0,
        "scientific_retries": 0,
        "turn2_household_calls": 0,
    }
    run001_checks = {
        "manifest_sha256": _sha256(run001_manifest_path) == EXPECTED_RUN001_MANIFEST,
        "manifest_entries": int(run001_manifest["entry_count"]) == 14,
        "manifest_bytes": int(run001_manifest["total_bytes"]) == 109_026,
        "independent_readback": run001_readback.get("status") == "PASS" and not run001_readback.get("bad_paths"),
        "terminal": run001_terminal.get("terminal_verdict") == "FAIL__UNEXPECTED_TASK_EXCEPTION__NO_SCIENTIFIC_RETRY",
        "historical_counts": all(int(run001_ledger[name]) == value for name, value in expected_run001_counts.items()),
    }
    run002_checks = {
        "manifest_sha256": _sha256(run002_manifest_path) == EXPECTED_RUN002_MANIFEST,
        "manifest_entries": int(run002_manifest["entry_count"]) == 139,
        "manifest_bytes": int(run002_manifest["total_bytes"]) == 1_949_298,
        "independent_readback": run002_readback.get("status") == "PASS" and not run002_readback.get("bad_paths"),
        "terminal": run002_terminal.get("terminal_verdict") == "FAIL__UNEXPECTED_TASK_EXCEPTION__NO_SCIENTIFIC_RETRY",
        "sealed_historical_counts": all(int(run002_ledger[name]) == value for name, value in expected_run002_counts.items()),
        "actual_scc_reconciled": (
            run002_reconciliation["accounting_reconciliation"]["persisted_global_ledger_scc_decompositions"] == 0
            and run002_reconciliation["accounting_reconciliation"]["audited_actual_scc_decompositions"] == 1
            and run002_reconciliation["call_path_audit"]["second_scc_or_topology_reconstruction_performed"] is False
        ),
    }
    if not all(run001_checks.values()) or not all(run002_checks.values()):
        raise FailClosed(
            "BLOCKED__PREDECESSOR_RUN001_RUN002_LINEAGE_MISMATCH",
            {"run001_checks": run001_checks, "run002_checks": run002_checks},
        )
    return {
        "status": "PASS",
        "classification": "ACCEPTED_RUN001_RUN002_HISTORICAL_CONSUMPTION__NOT_RUN003_COUNTS",
        "run001": {
            "root": RUN001_OUTPUT_RELATIVE.as_posix(),
            "manifest_sha256": EXPECTED_RUN001_MANIFEST,
            "manifest_entry_count": 14,
            "manifest_total_bytes": 109_026,
            "terminal_verdict": run001_terminal["terminal_verdict"],
            "historical_scientific_ledger": run001_ledger,
            "actual_scc_decompositions": 0,
            "checks": run001_checks,
        },
        "run002": {
            "root": RUN002_OUTPUT_RELATIVE.as_posix(),
            "manifest_sha256": EXPECTED_RUN002_MANIFEST,
            "manifest_entry_count": 139,
            "manifest_total_bytes": 1_949_298,
            "terminal_verdict": run002_terminal["terminal_verdict"],
            "sealed_scientific_ledger": run002_ledger,
            "sealed_scc_decompositions": 0,
            "actual_scc_decompositions": 1,
            "reconciliation": run002_reconciliation["accounting_reconciliation"],
            "checks": run002_checks,
        },
        "run001_run002_files_modified": False,
        "run003_scientific_calls": 0,
    }


def _finalize(
    repository: Path, output: Path, pre_hashes: dict[str, str], ledger: dict[str, Any],
    terminal: str, detail: dict[str, Any], started: float,
) -> str:
    post_hashes = _task_hashes(repository)
    if post_hashes != pre_hashes:
        terminal = "BLOCKED__SCIENTIFIC_CODE_CHANGED_AFTER_FREEZE"
        detail = {"prior_detail": detail}
    _check_ledger(ledger)
    ledger["wall_seconds"] = float(time.perf_counter() - started)
    ledger["terminal_verdict"] = terminal
    _write_json(output / "scientific_ledger.json", ledger)
    _write_json(output / "post_execution_code_freeze.json", {
        "scientific_code_sha256_after": post_hashes,
        "matches_pre_execution_freeze": post_hashes == pre_hashes,
    })
    _write_json(output / "terminal_receipt.json", {
        "terminal_verdict": terminal, "detail": detail,
        "turn2_household_run": int(ledger["source_native_initializations"]) > 0,
        "turn3_household_run": False, "successor_published": False,
        "results_eligibility": False,
    })
    _manifest(output)
    _readback(output)
    return terminal


def _implementation_parity_replay(repository: Path, output: Path) -> dict[str, Any]:
    """Replay the adopted implementation once on the already accepted Beijing Q12."""

    parity_root = output / "beijing_implementation_parity"
    parity_root.mkdir(parents=False, exist_ok=False)
    q_path = repository / BEIJING_Q12_RELATIVE
    d2_path = repository / BEIJING_D2_RELATIVE
    run003_manifest_relative = BEIJING_Q12_RELATIVE.parents[3] / "sealed_manifest.json"
    candidate_manifest_relative = BEIJING_METHOD_CANDIDATE_RELATIVE / "sealed_manifest.json"
    binding_checks = {
        "q12_sha256": _sha256(q_path) == BEIJING_Q12_SHA256,
        "run003_manifest_sha256": (
            _sha256(repository / run003_manifest_relative) == RUN003_MANIFEST_SHA256
        ),
        "method_candidate_manifest_sha256": (
            _git_blob_sha256(repository, candidate_manifest_relative)
            == BEIJING_METHOD_MANIFEST_SHA256
        ),
    }
    _write_json(
        parity_root / "authority_binding.json",
        {
            "status": "PASS" if all(binding_checks.values()) else "FAIL",
            "checks": binding_checks,
            "q12_path": BEIJING_Q12_RELATIVE.as_posix(),
            "q12_sha256": _sha256(q_path),
            "run003_manifest_working_tree_sealed_sha256": _sha256(
                repository / run003_manifest_relative
            ),
            "method_candidate_manifest_canonical_git_blob_sha256": _git_blob_sha256(
                repository, candidate_manifest_relative
            ),
        },
    )
    if not all(binding_checks.values()):
        raise FailClosed("BLOCKED__BEIJING_IMPLEMENTATION_PARITY_AUTHORITY_BINDING")

    parity_ledger = _local_ledger()
    q = sparse.load_npz(q_path).tocsr()
    d2_receipt = json.loads(d2_path.read_text(encoding="utf-8"))
    result = _terminal_kfe(
        12,
        q,
        float(d2_receipt["arithmetic_tolerance"]),
        parity_root,
        parity_ledger,
    )
    terminal_root = parity_root / "terminal_kfe"
    topology = json.loads((terminal_root / "topology_receipt.json").read_text(encoding="utf-8"))
    structure = json.loads((terminal_root / "q_cc_structural_receipt.json").read_text(encoding="utf-8"))
    rank = json.loads((terminal_root / "restricted_gesvd_rank_nullity_receipt.json").read_text(encoding="utf-8"))
    orientation = json.loads((terminal_root / "orientation_normalization_receipt.json").read_text(encoding="utf-8"))
    with np.load(terminal_root / "stationary_mass_arrays.npz", allow_pickle=False) as archive:
        p_closed = np.asarray(archive["p_closed"])
        p_full = np.asarray(archive["p"])
        residual = np.asarray(archive["residual"])
    checks = {
        "terminal_kfe_pass": result["status"] == "PASS",
        "closed_members_exact": tuple(topology["closed_members"][0]) == BEIJING_CLOSED_MEMBERS,
        "q_cc_shape_400x400": structure["q_cc_shape"] == [400, 400],
        "q_cc_nnz_1537": structure["q_cc_nnz"] == 1537,
        "spectrum_identity": rank["singular_values_sha256"] == BEIJING_SPECTRUM_SHA256,
        "local_rank_nullity_399_1": (
            rank["local_dimension_threshold_view"]["numerical_rank"] == 399
            and rank["local_dimension_threshold_view"]["numerical_nullity"] == 1
        ),
        "inherited_rank_nullity_399_1": (
            rank["inherited_full_space_dimension_threshold_view"]["numerical_rank"] == 399
            and rank["inherited_full_space_dimension_threshold_view"]["numerical_nullity"] == 1
        ),
        "p_closed_identity": _field_sha256(p_closed) == BEIJING_P_CLOSED_SHA256,
        "p_full_identity": _field_sha256(p_full) == BEIJING_P_FULL_SHA256,
        "residual_identity": _field_sha256(residual) == BEIJING_RESIDUAL_SHA256,
        "p_closed_strictly_positive": orientation["p_closed_strictly_positive"],
        "transient_exact_positive_zero": (
            orientation["transient_positive_zero_bit_pattern_count"] == 400
        ),
        "topology_once": parity_ledger["terminal_topology_gates"] == 1,
        "restricted_gesvd_once": parity_ledger["terminal_restricted_dense_gesvd"] == 1,
        "full_space_gesvd_zero": parity_ledger["terminal_full_space_dense_gesvd"] == 0,
        "normalization_candidate_once": (
            parity_ledger["terminal_normalized_stationary_candidates"] == 1
        ),
        "full_q_transpose_p_once": parity_ledger["terminal_q_transpose_times_p"] == 1,
        "hjb_policy_d2_calls_zero": True,
        "scientific_retries_zero": parity_ledger["scientific_retries"] == 0,
    }
    replay = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "separate_scientific_ledger": parity_ledger,
        "accepted_invariants": {
            "sigma_max": rank["sigma_max"],
            "second_smallest": rank["second_smallest"],
            "smallest": rank["smallest"],
            "minimum_p_closed": orientation["minimum_p_closed"],
            "maximum_p_closed": orientation["maximum_p_closed"],
            "full_q_residual_inf": result["stationarity"]["residual_inf"],
        },
    }
    _write_json(parity_root / "implementation_parity_receipt.json", replay)
    _write_json(parity_root / "scientific_ledger.json", parity_ledger)
    if replay["status"] != "PASS":
        raise FailClosed(
            "FAIL__BEIJING_IMPLEMENTATION_PARITY__RUN004_NOT_STARTED",
            {"checks": checks},
        )
    return replay


def execute(repository: Path, focused_test_junit: Path) -> str:
    repository = repository.resolve(strict=True)
    output = repository / OUTPUT_RELATIVE
    clean = not _git(repository, "status", "--porcelain")
    output.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    ledger = _new_ledger()
    pre_hashes = _task_hashes(repository)
    core_hashes = _scientific_code_hashes(repository)
    try:
        focused_tests = _read_junit(focused_test_junit)
        changed_paths = sorted(filter(None, _git(
            repository, "diff", "--name-only", f"{BASELINE_SHA}...HEAD"
        ).splitlines()))
        expected_engineering_paths = sorted((
            "src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py",
            "tests/test_mp4c_corrected_optionb_turn2_household_integration.py",
        ))
        blobs = {
            "entering_state": _blob(repository, ENTERING_STATE_RELATIVE),
            "source_initialization": _git(repository, "rev-parse", "HEAD:validators/multi_province/corrected_2018_single_turn/run.py"),
            "k1a": _git(repository, "rev-parse", "HEAD:src/ch5_two_asset_hank/multi_province/k1a_runtime_adapter.py"),
            "c1": _git(repository, "rev-parse", "HEAD:src/ch5_two_asset_hank/multi_province/c1_residual_public_asset.py"),
        }
        expected = {
            "entering_state": EXPECTED_ENTERING_STATE_BLOB,
            "source_initialization": EXPECTED_SOURCE_INITIALIZATION_BLOB,
            "k1a": EXPECTED_K1A_BLOB,
            "c1": EXPECTED_C1_BLOB,
        }
        startup_checks = {
            "clean_worktree": clean,
            "baseline_is_ancestor": _git(repository, "merge-base", "--is-ancestor", BASELINE_SHA, "HEAD") == "",
            "origin_main_exact_baseline": _git(repository, "rev-parse", "origin/main") == BASELINE_SHA,
            "authority_blobs": blobs == expected,
            "focused_tests": focused_tests["status"] == "PASS",
            "engineering_changed_paths_exact": changed_paths == expected_engineering_paths,
        }
        if not all(startup_checks.values()):
            raise FailClosed(
                "BLOCKED__TURN2_STARTUP_AUTHORITY_OR_ENGINEERING_GATE",
                {"checks": startup_checks, "blobs": blobs, "changed_paths": changed_paths},
            )

        states, state_receipt = load_initial_states(repository)
        integration_manifest = _verify_sealed_manifest(
            repository / ENTERING_STATE_RELATIVE.parent,
            EXPECTED_INTEGRATION_MANIFEST_SHA256,
            17,
        )
        household_manifest = _verify_sealed_manifest(
            repository / (
                "reports/ch5_mp4c_corrected_optionb_initial_turn_unique_closed_class_kfe_"
                "20260920_run004"
            ),
            EXPECTED_HOUSEHOLD_MANIFEST_SHA256,
            4353,
        )
        _write_json(output / "entering_turn2_authority_binding.json", {
            "status": "PASS",
            "task_id": TASK_ID,
            "execution_head": _git(repository, "rev-parse", "HEAD"),
            "actual_live_main_baseline": BASELINE_SHA,
            "checks": startup_checks,
            "blobs": blobs,
            "state_receipt": state_receipt,
            "canonical_integration_manifest": integration_manifest,
            "accepted_household_manifest": household_manifest,
        })
        _write_json(output / "turn2_entering_state_receipt_31province.json", state_receipt)
        _write_json(output / "focused_test_receipt.json", {**focused_tests, "scientific_calls": 0})
        _write_json(output / "pre_execution_code_freeze.json", {
            "scientific_code_sha256_before": pre_hashes,
            "core_corrected_code_sha256_before": core_hashes,
        })
        _write_json(output / "zero_science_preexecution_gate_receipt.json", {
            "status": "PASS",
            "checks": startup_checks,
            "entering_state_status": state_receipt["status"],
            "canonical_integration_manifest": integration_manifest["status"],
            "accepted_household_manifest": household_manifest["status"],
            "code_freeze_complete": True,
            "source_native_initializations": 0,
            "selector_evaluations": 0,
            "root_invocations": 0,
            "d2_q_assemblies": 0,
            "direct_hjb_updates": 0,
            "kfe_calls": 0,
        })

        native_grid = oracle.MatlabFaithfulHJBGrid(
            np.linspace(-2, 5, 20), np.linspace(0, 10, 20), np.array([0.8, 1.3]),
            np.array([[-1/3, 1/3], [1/3, -1/3]]),
        )
        grid = CorrectedDiagnosticGrid(native_grid.b, native_grid.a, native_grid.z)
        native_params = oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
        results = []
        for index, province in enumerate(PROVINCE_ORDER):
            results.append(_solve_province(
                repository, output, index, province, states[index], grid, native_grid,
                native_params, pre_hashes, core_hashes, ledger,
            ))
        if len(results) != 31:
            raise FailClosed("FAIL__TURN2_HOUSEHOLD_BATCH_INCOMPLETE", {"count": len(results)})

        ledger["household_batch_constructions"] += 1
        batch = PreFrozenHouseholdOutputBatch(
            ct=[row["aggregates"]["Ct"]["mass_form"] for row in results],
            household_lt=[row["aggregates"]["Lt"]["mass_form"] for row in results],
            at=[row["aggregates"]["At"]["mass_form"] for row in results],
            bt=[row["aggregates"]["Bt"]["mass_form"] for row in results],
            at_tax=[row["aggregates"]["AtTax"]["mass_form"] for row in results],
            converged=(True,) * 31,
            diagnostics=tuple(
                {"checkpoint": row["checkpoint"], "B": row["B"], "D": row["D"]}
                for row in results
            ),
        )
        batch_identity = _canonical_sha256({
            "ct": batch.ct.tolist(), "lt": batch.household_lt.tolist(),
            "at": batch.at.tolist(), "bt": batch.bt.tolist(),
            "at_tax": batch.at_tax.tolist(),
        })
        _write_json(output / "household_batch_receipt.json", {
            "status": "PASS", "province_count": 31,
            "identity_sha256": batch_identity,
            "rows": [
                {"province_index": i, "province": row["province"],
                 "checkpoint": row["checkpoint"], "B": row["B"], "D": row["D"]}
                for i, row in enumerate(results)
            ],
        })

        integration = integrate_one_turn(repository, states, batch, ledger)
        shares = np.asarray(integration.pop("portfolio_shares_destination_origin"), dtype=np.float64)
        terms = np.asarray(integration.pop("ordered_product_terms"), dtype=np.float64)
        raw_ra0 = np.asarray(integration["raw_ra0_turn2_by_destination"], dtype=np.float64)
        rah_turn3 = np.asarray(integration["rah_turn3_raw_by_origin"], dtype=np.float64)
        blas = np.asarray(integration["blas_diagnostic"], dtype=np.float64)
        np.savez_compressed(
            output / "canonical_turn3_raw_payoff_arrays.npz",
            raw_ra0_turn2=raw_ra0,
            shares_destination_origin=shares,
            ordered_product_terms=terms,
            canonical_rah_turn3=rah_turn3,
            blas_diagnostic=blas,
        )
        _write_json(output / "one_turn_integration_receipt.json", integration)
        _write_json(output / "canonical_turn3_raw_payoff_receipt.json", {
            key: integration[key] for key in (
                "orientation", "portfolio_shares_sha256", "raw_ra0_turn2_sha256",
                "ordered_product_terms_sha256", "rah_turn3_sha256",
                "raw_ra0_turn2_by_destination", "rah_turn3_raw_by_origin",
                "blas_diagnostic", "canonical_vs_blas_max_abs_difference",
                "canonical_vs_blas_bitwise_equal_count", "blas_is_acceptance_gate",
            )
        })
        _write_json(output / "turn_to_turn_movement_diagnostics.json", integration["movement_diagnostics"])
        _write_json(output / "turn3_next_state_candidate_receipt.json", {
            "status": "PASS",
            "classification": "TURN3_INPUT_CANDIDATE_ONLY__TURN3_NOT_RUN",
            "raw_next_payoff_sha256": integration["rah_turn3_sha256"],
            "rows": integration["next_states"],
        })
        return _finalize(repository, output, pre_hashes, ledger, PASS_TERMINAL, {
            "household_pass_count": 31,
            "integration_status": "PASS",
            "turn3_payoff_sha256": integration["rah_turn3_sha256"],
            "turn3_household_run": False,
        }, started)
    except FailClosed as failure:
        return _finalize(repository, output, pre_hashes, ledger, failure.terminal, failure.detail, started)
    except Exception as exc:
        return _finalize(
            repository, output, pre_hashes, ledger,
            "FAIL__UNEXPECTED_TASK_EXCEPTION__NO_SCIENTIFIC_RETRY",
            {"type": type(exc).__name__, "message": str(exc)}, started,
        )

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--focused-test-junit", type=Path, required=True)
    args = parser.parse_args(argv)
    verdict = execute(args.repository, args.focused_test_junit)
    print(verdict)
    return 0 if verdict == PASS_TERMINAL else 2


if __name__ == "__main__":
    raise SystemExit(main())
