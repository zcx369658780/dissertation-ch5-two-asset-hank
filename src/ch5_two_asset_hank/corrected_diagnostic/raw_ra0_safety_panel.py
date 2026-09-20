"""Bounded fixed-price three-point raw-ra0 corrected-household safety panel."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import asdict
from decimal import Decimal
import argparse
import csv
import json
from pathlib import Path
import shutil
import subprocess
import time
from typing import Any
import warnings
import xml.etree.ElementTree as ET

import numpy as np
from scipy import sparse
from scipy.sparse import linalg as sparse_linalg

from .checkpoint2_to_checkpoint6 import _switching_statistics
from .contracts import CorrectedDiagnosticGrid
from .nonlinear_continuation import (
    BACKWARD_ERROR_TOLERANCE,
    DELTA,
    N,
    SHAPE,
    FailClosed,
    _canonical_sha256,
    _field_sha256,
    _map_checkpoint,
    _operator_diagnostics,
    _policy_arrays,
    _policy_diagnostics,
    _scientific_code_hashes,
    _seal_directory,
    _selected_identity,
    _sha256,
    _sparse_identity,
    _verify_manifest_files,
    _write_json,
    checkpoint_identity,
    normwise_backward_error,
)
from .option_a_step import BoundOptionAInputs
from .selector import CorrectedSelectorParameters, SelectorBudget


TASK_ID = (
    "CH5_MP4C_K1A_RAW_RA0_CORRECTED_HOUSEHOLD_FIXED_PRICE_"
    "THREE_POINT_SAFETY_PANEL_20260920"
)
BASELINE_SHA = "ed17a6e30f079fe7f73dcb2214b5e1a98095c75c"
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_k1a_raw_ra0_corrected_household_fixed_price_"
    "three_point_safety_panel_20260920_run001"
)
ACCEPTED_ROOT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_checkpoint10_to_checkpoint12_"
    "bounded_nonlinear_continuation_20260920_run001"
)
CSV_RELATIVE = Path(
    "docs/evidence/ch5_mp4c_k1a_payoff_return_reaudit/"
    "static_no_feedback_payoff_counterfactual.csv"
)
EXPECTED_ROOT_MANIFEST = "5E67E595B32024213EC5E6517389A7DCA6462A24FB735B06EB2F85D6E1621E41"
EXPECTED_ROOT_ENTRIES = 819
EXPECTED_CSV_SHA256 = "5496DA47A1F06E46088D4FA80B3803654FB6C47134EE0D32F2DF79028C0FE9F9"
EXPECTED_V11 = "A097A3DDA767B979224638A51CEDC53EA635687CCDEFBE190FED0B899606921F"
EXPECTED_P11 = "89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3"
EXPECTED_U11 = "2E9A077FFA809F2DECEE385FD9E7F50C03E16750C2A074F990C0F3CBCC212648"
EXPECTED_Q11 = "33367258F3EADB1482D4A5CB30A64A8574830C993B0E5280C451499CBD6913AD"
EXPECTED_CHECKPOINT11 = "8093BE714CA83531816B20DFEB2BAB3DCB7AF9B971AD255C3596C1CA2A9E2A3B"
EXPECTED_GRID_HASHES = {
    "b": "A3FF663C18A2088A75B0E76C8ADA982EAF6D33ACFECB8DAA17C6D7DDE0533A76",
    "a": "AE3A3A789FBC0DC9900B8153DEC717264C74AAB6FDA356C21C0EB22EEAC52567",
    "z": "A35F6FAB6E4564C6F4B1962A2ADE64E477F808432F747ABC7ACCF5E70B0B39B7",
}
PANEL = (
    ("LOW", 5, 28, "青海", "0.11048158315647279"),
    ("MEDIAN", 12, 17, "湖南", "0.26259451366691877"),
    ("HIGH", 4, 0, "北京", "1.037811238406538"),
)
FROZEN_SCALARS = {
    "r_a": 0.09,
    "r_b": 0.02,
    "borrowing_rate_gap": 0.07,
    "tau": 0.05,
    "wage": 16.82014806560587,
    "transfer_income": 0.1,
    "rho": 0.05,
    "gamma_c": 2.0,
    "phi": 5.0,
    "chi_0": 0.1,
    "chi_1": 2.0,
    "a_bar": 1.0e-6,
    "labor_weight": 1.0,
    "delta": 1000.0,
}
PASS_TERMINAL = (
    "PASS__RAW_RA0_FIXED_PRICE_THREE_POINT_CORRECTED_HOUSEHOLD_"
    "ONE_STEP_SAFETY_PANEL__LONGER_RUNTIME_NOT_YET_AUTHORIZED"
)


def _new_ledger() -> dict[str, Any]:
    return {
        "accepted_checkpoint11_manifest_loads": 0,
        "accepted_v11_loads": 0,
        "accepted_p11_loads": 0,
        "accepted_u11_loads": 0,
        "accepted_q11_loads": 0,
        "accepted_csv_loads": 0,
        "new_corrected_policy_maps": 0,
        "selector_evaluations": 0,
        "scalar_root_invocations": 0,
        "interior_z_root_invocations": 0,
        "interior_a_switching_root_invocations": 0,
        "joint_switching_root_invocations": 0,
        "d2_assemblies": 0,
        "direct_hjb_solves": 0,
        "hjb_updates": 0,
        "complete_one_step_panel_evaluations": 0,
        "ordinary_graph_scc_summaries": 0,
        "terminal_topology_gates": 0,
        "terminal_dense_gesvd": 0,
        "terminal_normalized_stationary_candidates": 0,
        "terminal_q_transpose_times_p": 0,
        "scientific_retries": 0,
        "solver_substitutions": 0,
        "kfe_svd_eigen_nullspace_stationary_mass_calls": 0,
        "household_aggregate_adapter_evaluations": 0,
        "capital_network_calls": 0,
        "firm_wage_return_calls": 0,
        "outer_loop_steady_state_trajectory_calls": 0,
        "matlab_scientific_calls": 0,
        "k1b_feedback_calls": 0,
        "ge_annual_shock_irf_welfare_results_calls": 0,
        "damping_clipping_rescaling_smoothing_risk_adjustment_zscore_calls": 0,
    }


def _check_ledger(ledger: dict[str, Any]) -> None:
    ceilings = {
        "new_corrected_policy_maps": 3,
        "selector_evaluations": 2400,
        "d2_assemblies": 3,
        "direct_hjb_solves": 3,
        "hjb_updates": 3,
        "complete_one_step_panel_evaluations": 3,
        "scalar_root_invocations": 933_768,
        "interior_z_root_invocations": 855_360,
        "interior_a_switching_root_invocations": 2400,
        "joint_switching_root_invocations": 2400,
        "scientific_retries": 0,
        "solver_substitutions": 0,
        "ordinary_graph_scc_summaries": 0,
        "terminal_topology_gates": 0,
        "terminal_dense_gesvd": 0,
        "terminal_normalized_stationary_candidates": 0,
        "terminal_q_transpose_times_p": 0,
        "kfe_svd_eigen_nullspace_stationary_mass_calls": 0,
        "household_aggregate_adapter_evaluations": 0,
        "capital_network_calls": 0,
        "firm_wage_return_calls": 0,
        "outer_loop_steady_state_trajectory_calls": 0,
        "matlab_scientific_calls": 0,
        "k1b_feedback_calls": 0,
        "ge_annual_shock_irf_welfare_results_calls": 0,
        "damping_clipping_rescaling_smoothing_risk_adjustment_zscore_calls": 0,
    }
    breaches = {
        name: {"actual": int(ledger[name]), "ceiling": ceiling}
        for name, ceiling in ceilings.items()
        if int(ledger[name]) > ceiling
    }
    if breaches:
        raise FailClosed(
            "BLOCKED__TASK_SCIENTIFIC_LEDGER_CEILING",
            {"stage": "scientific_ledger", "breaches": breaches},
        )


def derive_panel(csv_path: Path) -> dict[str, Any]:
    if _sha256(csv_path) != EXPECTED_CSV_SHA256:
        raise FailClosed("BLOCKED__ACCEPTED_CSV_PANEL_VALUE_MISMATCH", {"stage": "csv_hash"})
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    path_b = [row for row in rows if row["path"] == "B_GEOGRAPHIC_BETA2"]
    ordered = sorted(path_b, key=lambda row: Decimal(row["static_raw_S_transpose_ra0"]))
    if len(ordered) != 775:
        raise FailClosed(
            "BLOCKED__ACCEPTED_CSV_PANEL_VALUE_MISMATCH",
            {"stage": "path_b_count", "actual": len(ordered)},
        )
    selected = (ordered[0], ordered[len(ordered) // 2], ordered[-1])
    receipts = []
    for (label, turn, province_index, province, value), row in zip(PANEL, selected):
        checks = {
            "label_order": label in ("LOW", "MEDIAN", "HIGH"),
            "turn": int(row["turn"]) == turn,
            "province_index": int(row["province_index"]) == province_index,
            "province": row["province"] == province,
            "value_exact_decimal_string": row["static_raw_S_transpose_ra0"] == value,
            "classification": row["classification"] == "STATIC_NO_FEEDBACK_COUNTERFACTUAL",
            "path": row["path"] == "B_GEOGRAPHIC_BETA2",
        }
        if not all(checks.values()):
            raise FailClosed(
                "BLOCKED__ACCEPTED_CSV_PANEL_VALUE_MISMATCH",
                {"stage": label, "checks": checks, "actual": row},
            )
        receipts.append(
            {
                "label": label,
                "order": len(receipts) + 1,
                "turn": turn,
                "province_index": province_index,
                "province": province,
                "r_a_decimal": value,
                "r_a_binary64": float(value),
                "checks": checks,
            }
        )
    return {
        "status": "PASS",
        "csv_path": CSV_RELATIVE.as_posix(),
        "csv_sha256": EXPECTED_CSV_SHA256,
        "total_rows": len(rows),
        "path_b_rows": len(path_b),
        "median_sorted_zero_based_index": len(ordered) // 2,
        "points": receipts,
    }


def _accepted_checkpoint11(repository: Path) -> dict[str, Any]:
    root = repository / ACCEPTED_ROOT_RELATIVE
    manifest_path = root / "sealed_manifest.json"
    if _sha256(manifest_path) != EXPECTED_ROOT_MANIFEST:
        raise FailClosed("BLOCKED__ACCEPTED_CHECKPOINT11_PROVENANCE_MISMATCH", {"stage": "manifest_hash"})
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    _verify_manifest_files(root, manifest)
    if int(manifest.get("entry_count", -1)) != EXPECTED_ROOT_ENTRIES:
        raise FailClosed("BLOCKED__ACCEPTED_CHECKPOINT11_PROVENANCE_MISMATCH", {"stage": "manifest_count"})
    checkpoint = root / "checkpoint_011"
    checkpoint_manifest = json.loads((checkpoint / "checkpoint_manifest.json").read_text(encoding="utf-8"))
    arrays_path = checkpoint / "checkpoint_arrays.npz"
    q_path = checkpoint / "q_generator.npz"
    with np.load(arrays_path, allow_pickle=False) as loaded:
        value = np.array(loaded["value"], dtype=float, copy=True, order="F")
        utility = np.array(loaded["utility"], dtype=float, copy=True, order="F")
    q = sparse.csr_matrix(sparse.load_npz(q_path))
    rows: list[dict[str, Any]] = []
    b = np.empty(SHAPE[0], dtype=float)
    a = np.empty(SHAPE[1], dtype=float)
    z = np.empty(SHAPE[2], dtype=float)
    for flat in range(N):
        receipt = json.loads((checkpoint / f"cell_{flat:04d}.json").read_text(encoding="utf-8"))
        index = tuple(map(int, receipt["index_b_a_z_zero_based"]))
        expected_index = tuple(map(int, np.unravel_index(flat, SHAPE, order="F")))
        result = receipt["selector_result"]
        if (
            int(receipt["flat_index_f_zero_based"]) != flat
            or index != expected_index
            or result["outcome"] != "SELECTED_ADMISSIBLE"
            or not isinstance(result.get("selected"), dict)
        ):
            raise FailClosed(
                "BLOCKED__ACCEPTED_CHECKPOINT11_PROVENANCE_MISMATCH",
                {"stage": "cell_receipt", "flat": flat},
            )
        cell = receipt["selector_cell"]
        b[index[0]], a[index[1]], z[index[2]] = float(cell["b"]), float(cell["a"]), float(cell["z"])
        rows.append(result["selected"])
    arrays = _policy_arrays(rows)
    grid = CorrectedDiagnosticGrid(b=b, a=a, z=z)
    grid_hashes = {"b": _field_sha256(b), "a": _field_sha256(a), "z": _field_sha256(z)}
    policy_identity = _canonical_sha256([_selected_identity(row) for row in rows])
    q_identity = _sparse_identity(q)
    identity = checkpoint_identity(EXPECTED_V11, policy_identity, q_identity)
    checks = {
        "manifest_readback": True,
        "value_shape_finite": value.shape == SHAPE and bool(np.all(np.isfinite(value))),
        "V11": _field_sha256(value) == EXPECTED_V11 == checkpoint_manifest["value_sha256"],
        "P11": policy_identity == EXPECTED_P11 == checkpoint_manifest["policy_identity_sha256"],
        "u11": _field_sha256(utility) == EXPECTED_U11 == checkpoint_manifest["utility_sha256"],
        "utility_rows_equal": np.array_equal(arrays["utility"], utility),
        "Q11": _sha256(q_path) == EXPECTED_Q11 == checkpoint_manifest["q_artifact_sha256"],
        "q_shape_finite": q.shape == (N, N) and bool(np.all(np.isfinite(q.data))),
        "checkpoint_identity": identity
        == EXPECTED_CHECKPOINT11
        == checkpoint_manifest["checkpoint_identity_sha256"],
        "grid": grid_hashes == EXPECTED_GRID_HASHES,
        "d2_pass": checkpoint_manifest["d2_receipt_status"] == "PASS",
        "primary_hjb_pass": checkpoint_manifest["primary_convergence_pass"] is True,
    }
    if not all(checks.values()):
        raise FailClosed(
            "BLOCKED__ACCEPTED_CHECKPOINT11_PROVENANCE_MISMATCH",
            {"stage": "checkpoint_binding", "checks": checks},
        )
    return {
        "root": root,
        "checkpoint": checkpoint,
        "value": value,
        "rows": rows,
        "arrays": arrays,
        "q": q,
        "grid": grid,
        "checks": checks,
        "grid_hashes": grid_hashes,
        "manifest_entry_count": int(manifest["entry_count"]),
        "identities": {
            "V11": EXPECTED_V11,
            "P11": policy_identity,
            "u11": EXPECTED_U11,
            "Q11": EXPECTED_Q11,
            "checkpoint11": identity,
            "root_manifest": EXPECTED_ROOT_MANIFEST,
        },
    }


def _point_inputs(accepted: dict[str, Any], r_a: float) -> BoundOptionAInputs:
    scalars = dict(FROZEN_SCALARS)
    scalars["r_a"] = float(r_a)
    parameters = CorrectedSelectorParameters(
        gamma_c=scalars["gamma_c"],
        phi=scalars["phi"],
        labor_weight=scalars["labor_weight"],
        chi_0=scalars["chi_0"],
        chi_1=scalars["chi_1"],
        a_bar=scalars["a_bar"],
    )
    return BoundOptionAInputs(
        seed_path=accepted["checkpoint"] / "checkpoint_arrays.npz",
        seed_sha256=_sha256(accepted["checkpoint"] / "checkpoint_arrays.npz"),
        seed_bytes=(accepted["checkpoint"] / "checkpoint_arrays.npz").stat().st_size,
        v0_field_sha256=EXPECTED_V11,
        binding_path=accepted["root"] / "accepted_checkpoint10_binding.json",
        binding_sha256=_sha256(accepted["root"] / "accepted_checkpoint10_binding.json"),
        binding_bytes=(accepted["root"] / "accepted_checkpoint10_binding.json").stat().st_size,
        grid=accepted["grid"],
        v0=accepted["value"],
        parameters=parameters,
        scalars=scalars,
        z_generator=np.array([[-1.0 / 3.0, 1.0 / 3.0], [1.0 / 3.0, -1.0 / 3.0]]),
    )


def _read_junit(path: Path) -> dict[str, Any]:
    root = ET.parse(path).getroot()
    tests = int(root.attrib.get("tests", sum(int(row.attrib.get("tests", 0)) for row in root)))
    failures = int(root.attrib.get("failures", sum(int(row.attrib.get("failures", 0)) for row in root)))
    errors = int(root.attrib.get("errors", sum(int(row.attrib.get("errors", 0)) for row in root)))
    skipped = int(root.attrib.get("skipped", sum(int(row.attrib.get("skipped", 0)) for row in root)))
    if failures or errors or tests <= 0:
        raise FailClosed(
            "BLOCKED__ENGINEERING_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE",
            {"stage": "focused_tests", "tests": tests, "failures": failures, "errors": errors},
        )
    return {"status": "PASS", "tests": tests, "failures": failures, "errors": errors, "skipped": skipped}


def _task_code_hashes(repository: Path) -> dict[str, str]:
    hashes = _scientific_code_hashes(repository)
    for relative in (
        "tests/test_mp4c_k1a_raw_ra0_fixed_price_three_point_safety_panel.py",
        CSV_RELATIVE.as_posix(),
    ):
        hashes[relative] = _sha256(repository / relative)
    return dict(sorted(hashes.items()))


def _root_manifest(output: Path) -> dict[str, Any]:
    entries = []
    for path in sorted(output.rglob("*")):
        if path.is_file() and path != output / "sealed_manifest.json":
            entries.append(
                {
                    "path": path.relative_to(output).as_posix(),
                    "bytes": path.stat().st_size,
                    "sha256": _sha256(path),
                }
            )
    document = {
        "schema": "CH5_MP4C_K1A_RAW_RA0_FIXED_PRICE_THREE_POINT_SAFETY_PANEL_V1",
        "entry_count": len(entries),
        "total_bytes": sum(int(row["bytes"]) for row in entries),
        "entries": entries,
    }
    _write_json(output / "sealed_manifest.json", document)
    return document


def _finalize(
    repository: Path,
    output: Path,
    pre_hashes: dict[str, str],
    ledger: dict[str, Any],
    terminal: str,
    detail: dict[str, Any],
    started: float,
) -> str:
    _check_ledger(ledger)
    post_hashes = _task_code_hashes(repository)
    if post_hashes != pre_hashes:
        terminal = "BLOCKED__SCIENTIFIC_CODE_CHANGED_AFTER_FREEZE"
        detail = {"stage": "post_science_code_freeze", "prior_detail": detail}
    ledger["terminal_verdict"] = terminal
    ledger["wall_seconds"] = float(time.perf_counter() - started)
    _write_json(output / "scientific_ledger.json", ledger)
    _write_json(
        output / "post_execution_code_freeze.json",
        {"scientific_code_sha256_after": post_hashes, "matches_pre_execution_freeze": post_hashes == pre_hashes},
    )
    _write_json(
        output / "terminal_receipt.json",
        {
            "terminal_verdict": terminal,
            "detail": detail,
            "convergence_classification_performed": False,
            "kfe_performed": False,
            "longer_runtime_authorized": False,
            "results_eligibility": False,
        },
    )
    _root_manifest(output)
    return terminal


def _point_budget_delta(before: dict[str, Any], after: dict[str, Any]) -> dict[str, int]:
    names = (
        "selector_evaluations",
        "root_invocations",
        "interior_z_root_invocations",
        "interior_a_switching_root_invocations",
        "joint_switching_root_invocations",
    )
    return {name: int(after[name]) - int(before[name]) for name in names}


def _solve_one_step(
    directory: Path,
    value: np.ndarray,
    utility: np.ndarray,
    q: sparse.csr_matrix,
    ledger: dict[str, Any],
) -> tuple[np.ndarray, dict[str, Any]]:
    matrix = (FROZEN_SCALARS["rho"] + 1.0 / DELTA) * sparse.eye(N, format="csr") - q
    rhs = utility.ravel(order="F") + value.ravel(order="F") / DELTA
    ledger["direct_hjb_solves"] += 1
    ledger["hjb_updates"] += 1
    _check_ledger(ledger)
    try:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            next_flat = np.asarray(sparse_linalg.spsolve(matrix, rhs), dtype=float)
    except Exception as exc:
        _write_json(
            directory / "direct_solve_receipt.json",
            {"status": "RAISED", "type": type(exc).__name__, "message": str(exc)},
        )
        raise FailClosed(
            "FAIL__RAW_RA0_PANEL_DIRECT_SOLVE_GATE",
            {"stage": "direct_solve_exception", "type": type(exc).__name__},
        ) from exc
    warning_rows = [{"category": row.category.__name__, "message": str(row.message)} for row in caught]
    if warning_rows or next_flat.shape != (N,) or not np.all(np.isfinite(next_flat)):
        _write_json(
            directory / "direct_solve_receipt.json",
            {
                "status": "FAIL",
                "warnings": warning_rows,
                "shape": list(next_flat.shape),
                "finite": bool(np.all(np.isfinite(next_flat))),
            },
        )
        raise FailClosed(
            "FAIL__RAW_RA0_PANEL_DIRECT_SOLVE_GATE",
            {"stage": "warning_shape_finite", "warnings": warning_rows, "shape": list(next_flat.shape)},
        )
    backward = normwise_backward_error(matrix, next_flat, rhs)
    residual = backward.pop("residual")
    next_value = next_flat.reshape(SHAPE, order="F")
    d_step = float(np.linalg.norm((next_value - value).ravel(order="F"), ord=np.inf))
    solve_pass = bool(
        np.isfinite(backward["normwise_backward_error"])
        and backward["normwise_backward_error"] <= BACKWARD_ERROR_TOLERANCE
    )
    np.savez_compressed(
        directory / "direct_update_arrays.npz",
        matrix_data=matrix.data,
        matrix_indices=matrix.indices,
        matrix_indptr=matrix.indptr,
        rhs=rhs,
        next_value=next_value,
        residual=residual,
    )
    receipt = {
        "status": "PASS" if solve_pass else "FAIL",
        "solver": "scipy.sparse.linalg.spsolve",
        "delta": DELTA,
        "warnings": warning_rows,
        **backward,
        "backward_error_threshold_inclusive": BACKWARD_ERROR_TOLERANCE,
        "matrix_identity": _sparse_identity(matrix),
        "rhs_sha256": _field_sha256(rhs),
        "next_value_sha256": _field_sha256(next_value),
        "residual_sha256": _field_sha256(residual),
        "D_step_vec_F_inf": d_step,
        "second_update_performed": False,
        "arrays_artifact": {
            "path": "direct_update_arrays.npz",
            "bytes": (directory / "direct_update_arrays.npz").stat().st_size,
            "sha256": _sha256(directory / "direct_update_arrays.npz"),
        },
    }
    _write_json(directory / "direct_solve_receipt.json", receipt)
    if not solve_pass:
        raise FailClosed("FAIL__RAW_RA0_PANEL_DIRECT_SOLVE_GATE", {"stage": "backward_error", "receipt": receipt})
    return next_value, receipt


def execute(repository: Path, focused_test_junit: Path) -> str:
    repository = repository.resolve(strict=True)
    output = repository / OUTPUT_RELATIVE
    clean_before = not subprocess.check_output(
        ["git", "status", "--porcelain"], cwd=repository, text=True
    ).strip()
    output.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    ledger = _new_ledger()
    core_pre_hashes = _scientific_code_hashes(repository)
    pre_hashes = _task_code_hashes(repository)
    _write_json(
        output / "startup_manifest.json",
        {
            "task_id": TASK_ID,
            "execution_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repository, text=True).strip(),
            "baseline_live_main": BASELINE_SHA,
            "worktree_clean_before_evidence": clean_before,
            "core_scientific_code_sha256_before": core_pre_hashes,
            "scientific_code_sha256_before": pre_hashes,
            "panel_order": [row[0] for row in PANEL],
            "budget": {
                "policy_maps": 3,
                "selector_evaluations": 2400,
                "d2_q_assemblies": 3,
                "direct_hjb_solves_updates": 3,
                "complete_panel_evaluations": 3,
                "scientific_retries": 0,
                "kfe": 0,
            },
        },
    )
    try:
        if not clean_before or subprocess.check_output(
            ["git", "rev-parse", "origin/main"], cwd=repository, text=True
        ).strip() != BASELINE_SHA:
            raise FailClosed(
                "BLOCKED__ENGINEERING_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE",
                {"stage": "git_binding"},
            )
        focused = _read_junit(focused_test_junit.resolve(strict=True))
        shutil.copyfile(focused_test_junit, output / "focused_tests.xml")
        focused["copied_sha256"] = _sha256(output / "focused_tests.xml")
        _write_json(output / "focused_test_receipt.json", focused)
        panel = derive_panel(repository / CSV_RELATIVE)
        ledger["accepted_csv_loads"] = 1
        _write_json(output / "accepted_csv_panel_derivation.json", panel)
        accepted = _accepted_checkpoint11(repository)
        ledger.update(
            accepted_checkpoint11_manifest_loads=1,
            accepted_v11_loads=1,
            accepted_p11_loads=1,
            accepted_u11_loads=1,
            accepted_q11_loads=1,
        )
        _write_json(
            output / "accepted_checkpoint11_binding.json",
            {
                "status": "PASS",
                "checks": accepted["checks"],
                "identities": accepted["identities"],
                "grid_hashes": accepted["grid_hashes"],
                "manifest_entry_count": accepted["manifest_entry_count"],
                "common_seed_reused_without_policy_remap_or_q_reassembly": True,
                "frozen_non_payoff_scalars": FROZEN_SCALARS,
            },
        )
        budget = SelectorBudget(
            max_selector_evaluations=2400,
            max_root_invocations=933_768,
            max_interior_z_root_invocations=855_360,
            max_interior_a_switching_root_invocations=2400,
            max_joint_switching_root_invocations=2400,
        )
        comparisons = []
        for point in panel["points"]:
            label = str(point["label"])
            point_root = output / f"point_{int(point['order']):02d}_{label.lower()}"
            point_root.mkdir(parents=False, exist_ok=False)
            inputs = _point_inputs(accepted, float(point["r_a_binary64"]))
            non_payoff = {key: value for key, value in inputs.scalars.items() if key != "r_a"}
            expected_non_payoff = {key: value for key, value in FROZEN_SCALARS.items() if key != "r_a"}
            if non_payoff != expected_non_payoff or inputs.scalars["delta"] != DELTA:
                raise FailClosed("BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT", {"stage": "non_payoff_scalars", "point": label})
            before = asdict(budget)
            rows, arrays, q, d2_receipt = _map_checkpoint(
                repository,
                point_root,
                11,
                accepted["value"],
                inputs,
                budget,
                ledger,
                core_pre_hashes,
            )
            after = asdict(budget)
            _check_ledger(ledger)
            directory = point_root / "checkpoint_011"
            policy = _policy_diagnostics(rows, accepted["rows"], arrays, accepted["arrays"])
            operator = _operator_diagnostics(q, accepted["q"])
            switching = _switching_statistics(directory)
            _write_json(directory / "policy_diagnostics.json", policy)
            _write_json(directory / "operator_diagnostics.json", operator)
            _write_json(directory / "switching_statistics.json", switching)
            seed_flat = accepted["value"].ravel(order="F")
            bellman = (
                FROZEN_SCALARS["rho"] * seed_flat
                - arrays["utility"].ravel(order="F")
                - np.asarray(q @ seed_flat).ravel()
            )
            b_seed = float(np.linalg.norm(bellman, ord=np.inf))
            _write_json(
                directory / "same_value_bellman_receipt.json",
                {
                    "B_seed": b_seed,
                    "formula": "||rho*V11-u(r_a,V11)-Q(r_a,V11)V11||inf",
                    "value_sha256": EXPECTED_V11,
                    "residual_sha256": _field_sha256(bellman),
                    "convergence_classification_performed": False,
                },
            )
            _next, solve = _solve_one_step(directory, accepted["value"], arrays["utility"], q, ledger)
            ledger["complete_one_step_panel_evaluations"] += 1
            _check_ledger(ledger)
            point_summary = {
                "label": label,
                "order": point["order"],
                "source": {
                    "turn": point["turn"],
                    "province_index": point["province_index"],
                    "province": point["province"],
                    "r_a_decimal": point["r_a_decimal"],
                    "r_a_binary64": point["r_a_binary64"],
                },
                "effective_r_a_formula": "r_a*(1-0.1*(a/10)^9)",
                "policy": policy,
                "switching": switching,
                "operator": operator,
                "d2": d2_receipt,
                "B_seed": b_seed,
                "D_step": solve["D_step_vec_F_inf"],
                "direct_solve": solve,
                "point_call_ledger": _point_budget_delta(before, after),
                "convergence_classification_performed": False,
                "second_update_performed": False,
                "kfe_performed": False,
                "status": "PASS",
            }
            _write_json(point_root / "point_summary.json", point_summary)
            _seal_directory(directory, "CH5_RAW_RA0_FIXED_PRICE_POINT_CHECKPOINT11_V1")
            comparisons.append(point_summary)
        _write_json(
            output / "panel_comparison.json",
            {
                "status": "PASS",
                "order": ["LOW", "MEDIAN", "HIGH"],
                "points": comparisons,
                "monotonicity_or_trend_inference_performed": False,
                "convergence_classification_performed": False,
            },
        )
        return _finalize(
            repository,
            output,
            pre_hashes,
            ledger,
            PASS_TERMINAL,
            {"points_completed": [row["label"] for row in comparisons]},
            started,
        )
    except FailClosed as exc:
        return _finalize(repository, output, pre_hashes, ledger, exc.terminal, exc.detail, started)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--focused-test-junit", type=Path, required=True)
    args = parser.parse_args(argv)
    terminal = execute(args.repository, args.focused_test_junit)
    print(terminal)
    return 0 if terminal == PASS_TERMINAL else 1


if __name__ == "__main__":
    raise SystemExit(main())
