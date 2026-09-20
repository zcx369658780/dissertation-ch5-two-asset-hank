"""Compact Path-B turn-1 31-province raw-ra0 one-step cross-section."""

from __future__ import annotations

from collections import Counter
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
    _scientific_code_hashes,
    _selected_identity,
    _sha256,
    _sparse_identity,
    _verify_manifest_files,
    _write_json,
    normwise_backward_error,
)
from .raw_ra0_safety_panel import (
    CSV_RELATIVE,
    EXPECTED_CSV_SHA256,
    EXPECTED_P11,
    EXPECTED_Q11,
    EXPECTED_U11,
    EXPECTED_V11,
    FROZEN_SCALARS,
    _accepted_checkpoint11,
    _point_inputs,
)
from .selector import SelectorBudget


TASK_ID = "CH5_MP4C_K1A_RAW_RA0_PATH_B_TURN1_31_PROVINCE_FIXED_PRICE_ONE_STEP_CROSS_SECTION_20260920"
BASELINE_SHA = "a2c728582ca19718270c6b2c91ea9a0bac547072"
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_k1a_raw_ra0_path_b_turn1_31_province_fixed_price_"
    "one_step_cross_section_20260920_run001"
)
ACCEPTED_PANEL_RELATIVE = Path(
    "reports/ch5_mp4c_k1a_raw_ra0_corrected_household_fixed_price_"
    "three_point_safety_panel_20260920_run001"
)
EXPECTED_PANEL_MANIFEST = "6D0A210F3979B0E0499FA8CC4C21803EB59077D655286D7119E0F85741BB5ED4"
EXPECTED_PANEL_ENTRIES = 2444
PASS_TERMINAL = (
    "PASS__PATH_B_TURN1_31_PROVINCE_RAW_RA0_FIXED_PRICE_ONE_STEP_"
    "CROSS_SECTION__PROVINCE_SPECIFIC_OUTER_INPUTS_NOT_YET_AUTHORIZED"
)

PROVINCES = (
    (0, "北京", "0.8951047990241244"),
    (1, "天津", "0.40511685922852797"),
    (2, "河北", "0.33682681151169935"),
    (3, "山西", "0.4291478483179544"),
    (4, "内蒙古", "0.3343835179213208"),
    (5, "辽宁", "0.35788915914936925"),
    (6, "吉林", "0.2826739400149174"),
    (7, "黑龙江", "0.315792897526093"),
    (8, "上海", "0.8436338107969247"),
    (9, "江苏", "0.5309391086970456"),
    (10, "浙江", "0.585387220964732"),
    (11, "安徽", "0.6239080240565922"),
    (12, "福建", "0.612400758531959"),
    (13, "江西", "0.6163318073667522"),
    (14, "山东", "0.35334433320183295"),
    (15, "河南", "0.32804592118083026"),
    (16, "湖北", "0.5255285778404981"),
    (17, "湖南", "0.4775623850053351"),
    (18, "广东", "0.5549881090546146"),
    (19, "广西", "0.38090963566299624"),
    (20, "海南", "0.6734489815056439"),
    (21, "重庆", "0.6385985431144864"),
    (22, "四川", "0.5301703013356037"),
    (23, "贵州", "0.5570443031272924"),
    (24, "云南", "0.4037818827188449"),
    (25, "西藏", "0.6268193076948068"),
    (26, "陕西", "0.4544982462398813"),
    (27, "甘肃", "0.5077975242704716"),
    (28, "青海", "0.36949073815753725"),
    (29, "宁夏", "0.41304347656460016"),
    (30, "新疆", "0.4009777871328596"),
)


def _new_ledger() -> dict[str, Any]:
    return {
        "accepted_checkpoint11_manifest_loads": 0,
        "accepted_v11_loads": 0,
        "accepted_p11_loads": 0,
        "accepted_u11_loads": 0,
        "accepted_q11_loads": 0,
        "accepted_csv_loads": 0,
        "accepted_panel_manifest_loads": 0,
        "compact_projection_recertifications": 0,
        "new_corrected_policy_maps": 0,
        "selector_evaluations": 0,
        "scalar_root_invocations": 0,
        "interior_z_root_invocations": 0,
        "interior_a_switching_root_invocations": 0,
        "joint_switching_root_invocations": 0,
        "d2_assemblies": 0,
        "direct_hjb_solves": 0,
        "hjb_updates": 0,
        "complete_one_step_cross_section_evaluations": 0,
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
        "payoff_clipping_annualization_rescaling_smoothing_risk_adjustment_zscore_calls": 0,
    }


def _check_ledger(ledger: dict[str, Any]) -> None:
    ceilings = {
        "compact_projection_recertifications": 3,
        "new_corrected_policy_maps": 31,
        "selector_evaluations": 24_800,
        "scalar_root_invocations": 9_648_936,
        "interior_z_root_invocations": 8_838_720,
        "interior_a_switching_root_invocations": 24_800,
        "joint_switching_root_invocations": 24_800,
        "d2_assemblies": 31,
        "direct_hjb_solves": 31,
        "hjb_updates": 31,
        "complete_one_step_cross_section_evaluations": 31,
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
        "payoff_clipping_annualization_rescaling_smoothing_risk_adjustment_zscore_calls": 0,
    }
    breaches = {
        name: {"actual": int(ledger[name]), "ceiling": ceiling}
        for name, ceiling in ceilings.items()
        if int(ledger[name]) > ceiling
    }
    if breaches:
        raise FailClosed("BLOCKED__TASK_SCIENTIFIC_LEDGER_CEILING", {"breaches": breaches})


def derive_cross_section(csv_path: Path) -> dict[str, Any]:
    if _sha256(csv_path) != EXPECTED_CSV_SHA256:
        raise FailClosed("BLOCKED__CSV_HASH_OR_31_ROW_DERIVATION_MISMATCH", {"stage": "csv_hash"})
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        all_rows = list(csv.DictReader(handle))
    rows = [
        row for row in all_rows
        if row["path"] == "B_GEOGRAPHIC_BETA2" and int(row["turn"]) == 1
    ]
    rows.sort(key=lambda row: int(row["province_index"]))
    checks: list[dict[str, Any]] = []
    if len(rows) != 31:
        raise FailClosed("BLOCKED__CSV_HASH_OR_31_ROW_DERIVATION_MISMATCH", {"stage": "count", "actual": len(rows)})
    for expected, row in zip(PROVINCES, rows):
        index, province, value = expected
        row_checks = {
            "province_index": int(row["province_index"]) == index,
            "province": row["province"] == province,
            "value_exact_decimal_string": row["static_raw_S_transpose_ra0"] == value,
            "classification": row["classification"] == "STATIC_NO_FEEDBACK_COUNTERFACTUAL",
            "next_allocation_validation": row["next_allocation_payoff_validation_status"]
            == "VALIDATED_SAME_S_AND_NEXT_ALLOCATION_PAYOFF",
        }
        if not all(row_checks.values()):
            raise FailClosed(
                "BLOCKED__CSV_HASH_OR_31_ROW_DERIVATION_MISMATCH",
                {"stage": "row", "province_index": index, "checks": row_checks},
            )
        checks.append({
            "province_index": index,
            "province": province,
            "r_a_decimal": value,
            "r_a_binary64": float(value),
            "checks": row_checks,
        })
    ordered_values = sorted(Decimal(row[2]) for row in PROVINCES)
    return {
        "status": "PASS",
        "csv_path": CSV_RELATIVE.as_posix(),
        "csv_sha256": EXPECTED_CSV_SHA256,
        "row_count": 31,
        "rows": checks,
        "minimum": str(ordered_values[0]),
        "median": str(ordered_values[15]),
        "maximum": str(ordered_values[-1]),
    }


def _load_rows(directory: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for flat in range(N):
        receipt = json.loads((directory / f"cell_{flat:04d}.json").read_text(encoding="utf-8"))
        result = receipt.get("selector_result", {})
        if (
            int(receipt.get("flat_index_f_zero_based", -1)) != flat
            or result.get("outcome") != "SELECTED_ADMISSIBLE"
            or not isinstance(result.get("selected"), dict)
        ):
            raise FailClosed("BLOCKED__COMPACT_POLICY_SOURCE_RECEIPT_MISMATCH", {"flat": flat})
        rows.append(result["selected"])
    return rows


def _normalized_identity(row: dict[str, Any]) -> dict[str, Any]:
    return json.loads(json.dumps(_selected_identity(row), sort_keys=True, separators=(",", ":")))


def _compact_policy_projection(
    directory: Path,
    rows: list[dict[str, Any]],
    arrays: dict[str, np.ndarray],
    accepted_rows: list[dict[str, Any]],
    accepted_arrays: dict[str, np.ndarray],
    switching: dict[str, Any],
) -> dict[str, Any]:
    identities = [_normalized_identity(row) for row in rows]
    accepted_identities = [_normalized_identity(row) for row in accepted_rows]
    changed = [i for i, (left, right) in enumerate(zip(identities, accepted_identities)) if left != right]
    array_path = directory / "selected_policy_arrays.npz"
    identity_path = directory / "selected_policy_identity.json"
    np.savez_compressed(array_path, **arrays)
    _write_json(identity_path, {"flatten_order": "F", "identities": identities})
    field_hashes = {name: _field_sha256(value) for name, value in sorted(arrays.items())}
    continuous = {
        name: float(np.linalg.norm((arrays[name] - accepted_arrays[name]).ravel(order="F"), ord=np.inf))
        for name in ("c", "l", "d", "g_b", "g_a", "q_b", "q_a", "utility")
    }
    return {
        "selector_outcome_count": len(rows),
        "identity_sha256": _canonical_sha256(identities),
        "identity_change_count": len(changed),
        "identity_change_flat_f_zero_based": changed,
        "active_constraint_counts": dict(sorted(Counter(
            "+".join(map(str, row.get("active_constraints", []))) or "none" for row in rows
        ).items())),
        "transfer_branch_counts": dict(sorted(Counter(str(row["transfer_branch"]) for row in rows).items())),
        "interior_z_marker_counts": dict(sorted(Counter(
            str(identity["interior_z_marker"] or "none") for identity in identities
        ).items())),
        "selected_field_sha256": field_hashes,
        "continuous_field_max_abs_change": continuous,
        "switching": switching,
        "arrays_artifact": {"path": array_path.name, "bytes": array_path.stat().st_size, "sha256": _sha256(array_path)},
        "identity_artifact": {"path": identity_path.name, "bytes": identity_path.stat().st_size, "sha256": _sha256(identity_path)},
    }


def compact_recertification(repository: Path, output: Path, accepted: dict[str, Any]) -> dict[str, Any]:
    root = repository / ACCEPTED_PANEL_RELATIVE
    manifest_path = root / "sealed_manifest.json"
    if _sha256(manifest_path) != EXPECTED_PANEL_MANIFEST:
        raise FailClosed("BLOCKED__COMPACT_PROJECTION_RECERTIFICATION_MISMATCH", {"stage": "manifest_hash"})
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    _verify_manifest_files(root, manifest)
    if int(manifest.get("entry_count", -1)) != EXPECTED_PANEL_ENTRIES:
        raise FailClosed("BLOCKED__COMPACT_PROJECTION_RECERTIFICATION_MISMATCH", {"stage": "manifest_count"})
    targets = (("LOW", "point_01_low"), ("MEDIAN", "point_02_median"), ("HIGH", "point_03_high"))
    receipts = []
    recert_root = output / "compact_recertification"
    recert_root.mkdir(parents=False, exist_ok=False)
    for label, relative in targets:
        source = root / relative
        checkpoint = source / "checkpoint_011"
        summary = json.loads((source / "point_summary.json").read_text(encoding="utf-8"))
        rows = _load_rows(checkpoint)
        arrays = _policy_arrays(rows)
        switching = _switching_statistics(checkpoint)
        target = recert_root / label.lower()
        target.mkdir(parents=False, exist_ok=False)
        compact = _compact_policy_projection(target, rows, arrays, accepted["rows"], accepted["arrays"], switching)
        with np.load(target / "selected_policy_arrays.npz", allow_pickle=False) as loaded:
            reload_hashes = {name: _field_sha256(np.asarray(loaded[name])) for name in loaded.files}
        identity_reload = json.loads((target / "selected_policy_identity.json").read_text(encoding="utf-8"))["identities"]
        checks = {
            "selector_count_800": compact["selector_outcome_count"] == 800,
            "policy_identity": compact["identity_sha256"] == summary["policy"]["identity_sha256"],
            "normalized_identity_change_count": compact["identity_change_count"] == summary["policy"]["identity_change_count"],
            "active_constraint_counts": compact["active_constraint_counts"] == summary["policy"]["active_constraint_counts"],
            "transfer_branch_counts": compact["transfer_branch_counts"] == summary["policy"]["transfer_branch_counts"],
            "switching": compact["switching"] == summary["switching"],
            "field_hashes_reload": reload_hashes == compact["selected_field_sha256"],
            "identity_reload": _canonical_sha256(identity_reload) == compact["identity_sha256"],
        }
        if not all(checks.values()):
            raise FailClosed("BLOCKED__COMPACT_PROJECTION_RECERTIFICATION_MISMATCH", {"stage": label, "checks": checks})
        receipt = {"label": label, "status": "PASS", "checks": checks, "compact_policy": compact, "scientific_calls": 0}
        _write_json(target / "recertification_receipt.json", receipt)
        receipts.append(receipt)
    result = {
        "status": "PASS",
        "accepted_panel_manifest_sha256": EXPECTED_PANEL_MANIFEST,
        "accepted_panel_manifest_entries": EXPECTED_PANEL_ENTRIES,
        "points": receipts,
        "selector_calls": 0,
        "q_assemblies": 0,
        "direct_solves": 0,
    }
    _write_json(output / "compact_projection_recertification.json", result)
    return result


def _local_map_ledger() -> dict[str, Any]:
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
        "terminal_dense_gesvd": 0,
        "terminal_normalized_stationary_candidates": 0,
        "terminal_q_transpose_times_p": 0,
        "scientific_retries": 0,
        "solver_substitutions": 0,
        "damping_relaxation_adaptive_delta_continuation_calls": 0,
        "matlab_production_ge_irf_results_calls": 0,
    }


def _accumulate_map_ledger(total: dict[str, Any], local: dict[str, Any]) -> None:
    for target, source in (
        ("new_corrected_policy_maps", "new_corrected_policy_maps"),
        ("selector_evaluations", "selector_evaluations"),
        ("scalar_root_invocations", "scalar_root_invocations"),
        ("interior_z_root_invocations", "interior_z_root_invocations"),
        ("interior_a_switching_root_invocations", "interior_a_switching_root_invocations"),
        ("joint_switching_root_invocations", "joint_switching_root_invocations"),
        ("d2_assemblies", "d2_assemblies"),
    ):
        total[target] += int(local[source])
    _check_ledger(total)


def _solve_one_step(directory: Path, value: np.ndarray, utility: np.ndarray, q: sparse.csr_matrix, ledger: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
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
        _write_json(directory / "direct_solve_receipt.json", {"status": "RAISED", "type": type(exc).__name__, "message": str(exc)})
        raise FailClosed("FAIL__DIRECT_HJB_SOLVE_GATE", {"stage": "exception"}) from exc
    warning_rows = [{"category": row.category.__name__, "message": str(row.message)} for row in caught]
    if warning_rows or next_flat.shape != (N,) or not np.all(np.isfinite(next_flat)):
        raise FailClosed("FAIL__DIRECT_HJB_SOLVE_GATE", {"stage": "warning_shape_finite", "warnings": warning_rows})
    backward = normwise_backward_error(matrix, next_flat, rhs)
    residual = backward.pop("residual")
    next_value = next_flat.reshape(SHAPE, order="F")
    d_step = float(np.linalg.norm((next_value - value).ravel(order="F"), ord=np.inf))
    passed = bool(np.isfinite(backward["normwise_backward_error"]) and backward["normwise_backward_error"] <= BACKWARD_ERROR_TOLERANCE)
    arrays_path = directory / "direct_update_arrays.npz"
    np.savez_compressed(arrays_path, matrix_data=matrix.data, matrix_indices=matrix.indices, matrix_indptr=matrix.indptr, rhs=rhs, next_value=next_value, residual=residual)
    receipt = {
        "status": "PASS" if passed else "FAIL",
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
        "arrays_artifact": {"path": arrays_path.name, "bytes": arrays_path.stat().st_size, "sha256": _sha256(arrays_path)},
    }
    _write_json(directory / "direct_solve_receipt.json", receipt)
    if not passed:
        raise FailClosed("FAIL__DIRECT_HJB_SOLVE_GATE", {"stage": "backward_error", "receipt": receipt})
    return next_value, receipt


def _read_junit(path: Path) -> dict[str, Any]:
    root = ET.parse(path).getroot()
    tests = int(root.attrib.get("tests", sum(int(row.attrib.get("tests", 0)) for row in root)))
    failures = int(root.attrib.get("failures", sum(int(row.attrib.get("failures", 0)) for row in root)))
    errors = int(root.attrib.get("errors", sum(int(row.attrib.get("errors", 0)) for row in root)))
    skipped = int(root.attrib.get("skipped", sum(int(row.attrib.get("skipped", 0)) for row in root)))
    if tests <= 0 or failures or errors:
        raise FailClosed("BLOCKED__FOCUSED_TEST_GATE", {"tests": tests, "failures": failures, "errors": errors})
    return {"status": "PASS", "tests": tests, "failures": failures, "errors": errors, "skipped": skipped}


def _task_code_hashes(repository: Path) -> dict[str, str]:
    hashes = _scientific_code_hashes(repository)
    for relative in (
        "src/ch5_two_asset_hank/corrected_diagnostic/raw_ra0_turn1_cross_section.py",
        "tests/test_mp4c_k1a_raw_ra0_turn1_cross_section.py",
        CSV_RELATIVE.as_posix(),
    ):
        hashes[relative] = _sha256(repository / relative)
    return dict(sorted(hashes.items()))


def _root_manifest(output: Path) -> dict[str, Any]:
    entries = [
        {"path": path.relative_to(output).as_posix(), "bytes": path.stat().st_size, "sha256": _sha256(path)}
        for path in sorted(output.rglob("*"))
        if path.is_file() and path != output / "sealed_manifest.json"
    ]
    document = {
        "schema": "CH5_MP4C_K1A_RAW_RA0_PATH_B_TURN1_31_PROVINCE_COMPACT_CROSS_SECTION_V1",
        "entry_count": len(entries),
        "total_bytes": sum(int(row["bytes"]) for row in entries),
        "entries": entries,
    }
    _write_json(output / "sealed_manifest.json", document)
    return document


def _independent_readback(output: Path) -> dict[str, Any]:
    manifest_path = output / "sealed_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bad = []
    for row in manifest["entries"]:
        path = output / row["path"]
        if not path.is_file() or path.stat().st_size != int(row["bytes"]) or _sha256(path) != row["sha256"]:
            bad.append(row["path"])
    receipt = {
        "status": "PASS" if not bad else "FAIL",
        "verified_manifest_sha256": _sha256(manifest_path),
        "verified_entry_count": len(manifest["entries"]),
        "verified_total_bytes": sum(int(row["bytes"]) for row in manifest["entries"]),
        "bad_count": len(bad),
        "bad_paths": bad,
        "scientific_calls": 0,
    }
    _write_json(output / "independent_readback_receipt.json", receipt)
    if bad:
        raise FailClosed("BLOCKED__EVIDENCE_READBACK_FAILURE", {"bad_paths": bad})
    _root_manifest(output)
    return receipt


def _remove_verbose_cells(directory: Path) -> None:
    for path in directory.glob("cell_*.json"):
        path.unlink()


def _finalize(repository: Path, output: Path, pre_hashes: dict[str, str], ledger: dict[str, Any], terminal: str, detail: dict[str, Any], started: float) -> str:
    _check_ledger(ledger)
    post_hashes = _task_code_hashes(repository)
    if post_hashes != pre_hashes:
        terminal = "BLOCKED__SCIENTIFIC_CODE_CHANGED_AFTER_FREEZE"
        detail = {"stage": "post_science_code_freeze", "prior_detail": detail}
    ledger["terminal_verdict"] = terminal
    ledger["wall_seconds"] = float(time.perf_counter() - started)
    _write_json(output / "scientific_ledger.json", ledger)
    _write_json(output / "post_execution_code_freeze.json", {"scientific_code_sha256_after": post_hashes, "matches_pre_execution_freeze": post_hashes == pre_hashes})
    _write_json(output / "terminal_receipt.json", {
        "terminal_verdict": terminal,
        "detail": detail,
        "convergence_classification_performed": False,
        "kfe_performed": False,
        "outer_loop_performed": False,
        "results_eligibility": False,
    })
    _root_manifest(output)
    _independent_readback(output)
    return terminal


def execute(repository: Path, focused_test_junit: Path) -> str:
    repository = repository.resolve(strict=True)
    output = repository / OUTPUT_RELATIVE
    clean_before = not subprocess.check_output(["git", "status", "--porcelain"], cwd=repository, text=True).strip()
    output.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    ledger = _new_ledger()
    pre_hashes = _task_code_hashes(repository)
    core_pre_hashes = _scientific_code_hashes(repository)
    _write_json(output / "startup_manifest.json", {
        "task_id": TASK_ID,
        "execution_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repository, text=True).strip(),
        "baseline_live_main": BASELINE_SHA,
        "worktree_clean_before_evidence": clean_before,
        "scientific_code_sha256_before": pre_hashes,
        "province_execution_order": list(range(31)),
        "compact_evidence_required": True,
        "budget": {"policy_maps": 31, "selector_evaluations": 24_800, "d2_q": 31, "direct_solves_updates": 31, "scientific_retries": 0},
    })
    try:
        if not clean_before or subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=repository, text=True).strip() != BASELINE_SHA:
            raise FailClosed("BLOCKED__LIVE_AUTHORITY_OR_GIT_BINDING_DRIFT", {"stage": "git_binding"})
        focused = _read_junit(focused_test_junit.resolve(strict=True))
        shutil.copyfile(focused_test_junit, output / "focused_tests.xml")
        focused["copied_sha256"] = _sha256(output / "focused_tests.xml")
        _write_json(output / "focused_test_receipt.json", focused)
        derivation = derive_cross_section(repository / CSV_RELATIVE)
        ledger["accepted_csv_loads"] = 1
        _write_json(output / "accepted_turn1_31_row_derivation.json", derivation)
        accepted = _accepted_checkpoint11(repository)
        ledger.update(accepted_checkpoint11_manifest_loads=1, accepted_v11_loads=1, accepted_p11_loads=1, accepted_u11_loads=1, accepted_q11_loads=1)
        _write_json(output / "accepted_checkpoint11_binding.json", {
            "status": "PASS", "checks": accepted["checks"], "identities": accepted["identities"],
            "grid_hashes": accepted["grid_hashes"], "manifest_entry_count": accepted["manifest_entry_count"],
            "common_seed_reused_without_policy_remap_or_q_reassembly": True,
            "frozen_non_payoff_scalars": FROZEN_SCALARS,
        })
        compact_recertification(repository, output, accepted)
        ledger["accepted_panel_manifest_loads"] = 1
        ledger["compact_projection_recertifications"] = 3
        _check_ledger(ledger)
        summaries = []
        for row in derivation["rows"]:
            index = int(row["province_index"])
            point_root = output / f"province_{index:02d}"
            point_root.mkdir(parents=False, exist_ok=False)
            inputs = _point_inputs(accepted, float(row["r_a_binary64"]))
            non_payoff = {key: value for key, value in inputs.scalars.items() if key != "r_a"}
            expected_non_payoff = {key: value for key, value in FROZEN_SCALARS.items() if key != "r_a"}
            if non_payoff != expected_non_payoff or inputs.scalars["delta"] != DELTA:
                raise FailClosed("BLOCKED__NON_PAYOFF_INPUT_DRIFT", {"province_index": index})
            budget = SelectorBudget(max_selector_evaluations=800, max_root_invocations=311_256, max_interior_z_root_invocations=285_120, max_interior_a_switching_root_invocations=800, max_joint_switching_root_invocations=800)
            local = _local_map_ledger()
            try:
                rows, arrays, q, d2 = _map_checkpoint(repository, point_root, 11, accepted["value"], inputs, budget, local, core_pre_hashes)
            except FailClosed:
                directory = point_root / "checkpoint_011"
                cells = sorted(directory.glob("cell_*.json")) if directory.is_dir() else []
                if cells:
                    failing = cells[-1]
                    for path in cells[:-1]:
                        path.unlink()
                    failing.rename(directory / "failing_cell_receipt.json")
                raise
            _accumulate_map_ledger(ledger, local)
            directory = point_root / "checkpoint_011"
            switching = _switching_statistics(directory)
            policy = _compact_policy_projection(directory, rows, arrays, accepted["rows"], accepted["arrays"], switching)
            operator = _operator_diagnostics(q, accepted["q"])
            _write_json(directory / "compact_policy_receipt.json", policy)
            _write_json(directory / "operator_diagnostics.json", operator)
            _write_json(directory / "switching_statistics.json", switching)
            seed = accepted["value"].ravel(order="F")
            residual = FROZEN_SCALARS["rho"] * seed - arrays["utility"].ravel(order="F") - np.asarray(q @ seed).ravel()
            b_seed = float(np.linalg.norm(residual, ord=np.inf))
            _write_json(directory / "same_value_bellman_receipt.json", {"B_seed": b_seed, "formula": "||rho*V11-u(r_a,V11)-Q(r_a,V11)V11||inf", "value_sha256": EXPECTED_V11, "residual_sha256": _field_sha256(residual), "convergence_classification_performed": False})
            _next, solve = _solve_one_step(directory, accepted["value"], arrays["utility"], q, ledger)
            ledger["complete_one_step_cross_section_evaluations"] += 1
            _check_ledger(ledger)
            point_call_ledger = {
                "selector_evaluations": int(local["selector_evaluations"]),
                "root_invocations": int(local["scalar_root_invocations"]),
                "interior_z_root_invocations": int(local["interior_z_root_invocations"]),
                "interior_a_switching_root_invocations": int(local["interior_a_switching_root_invocations"]),
                "joint_switching_root_invocations": int(local["joint_switching_root_invocations"]),
            }
            summary = {
                "status": "PASS", "province_index": index, "province": row["province"],
                "r_a_decimal": row["r_a_decimal"], "r_a_binary64": row["r_a_binary64"],
                "effective_r_a_formula": "r_a*(1-0.1*(a/10)^9)", "policy": policy,
                "operator": operator, "d2": d2, "B_seed": b_seed, "D_step": solve["D_step_vec_F_inf"],
                "direct_solve": solve, "point_call_ledger": point_call_ledger,
                "convergence_classification_performed": False, "second_update_performed": False, "kfe_performed": False,
            }
            _write_json(point_root / "province_summary.json", summary)
            _remove_verbose_cells(directory)
            summaries.append(summary)
        b_values = [float(row["B_seed"]) for row in summaries]
        d_values = [float(row["D_step"]) for row in summaries]
        comparison = {
            "status": "PASS", "province_count": len(summaries), "execution_order": [row["province_index"] for row in summaries],
            "provinces": summaries,
            "descriptive_summary": {
                "B_seed": {"minimum": min(b_values), "median": float(np.median(b_values)), "maximum": max(b_values)},
                "D_step": {"minimum": min(d_values), "median": float(np.median(d_values)), "maximum": max(d_values)},
            },
            "trend_threshold_or_convergence_probability_inference_performed": False,
        }
        _write_json(output / "cross_section_comparison.json", comparison)
        return _finalize(repository, output, pre_hashes, ledger, PASS_TERMINAL, {"province_indices_completed": list(range(31))}, started)
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
