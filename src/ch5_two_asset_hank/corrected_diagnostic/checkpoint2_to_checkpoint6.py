"""Bounded accepted-checkpoint-2 continuation through checkpoint 6 only."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time
from typing import Any
import warnings
import xml.etree.ElementTree as ET

import numpy as np
from scipy import sparse
from scipy.sparse import linalg as sparse_linalg

from .checkpoint2_reexecution import _load_sources
from .nonlinear_continuation import (
    BACKWARD_ERROR_TOLERANCE,
    BELLMAN_TOLERANCE,
    CYCLE_TOLERANCE,
    DELTA,
    N,
    SHAPE,
    VALUE_TOLERANCE,
    V1_FIELD_SHA256,
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
    detect_approximate_cycle,
    detect_exact_cycle,
    normwise_backward_error,
    primary_converged,
)
from .option_a_step import _input_receipt, bind_option_a_inputs
from .selector import SelectorBudget


TASK_ID = (
    "CH5_MP4C_2018_KFE_D123_CHECKPOINT2_TO_CHECKPOINT6_"
    "BOUNDED_NONLINEAR_CONTINUATION_20260919"
)
BASELINE_SHA = "AAC2C854A8A208F4ABB469CE310B3347195F4DF7"
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_checkpoint2_to_checkpoint6_"
    "bounded_nonlinear_continuation_20260919_run001"
)
ACCEPTED_ROOT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_simultaneous_two_axis_zero_drift_"
    "switching_implementation_v2_checkpoint2_reexecution_20260919_run001"
)

V0_FIELD_SHA256 = "564B95B818713477691389903C3CFF72B5A7F991B924D52FBEB23D5A3675D665"
V2_FIELD_SHA256 = "A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1"
P2_IDENTITY_SHA256 = "EBCBABC0593EF163D2E7FA300F6FFEB6E3C187D232D4CCEA5D59AB7180CD1D95"
U2_FIELD_SHA256 = "C222F4B147F48EA177A28AAF289F3ED5EA76F531BC08201070DD63698BF98D73"
Q2_ARTIFACT_SHA256 = "346DBCDA13392DAF6897DC185767B0E7C5961AA76A9AAA686053AEDA33C02F9F"
Q2_IDENTITY = {
    "data": "3278FFDA5ABA29E8C8E7ECC84649DF7A787AD7BDA5E936657F585B65A9844BEB",
    "indices": "6FF05054740279B563416E942AFEC958804FBD1AF63C660C9877D3175FB5B066",
    "indptr": "180A552000B935F15F1934266DE86FF9E3D7550005366AB92B312793648F0200",
}
CHECKPOINT2_IDENTITY_SHA256 = (
    "71DC6975E814060A4F63961A736E6E9DDF766C51CE4672C3EF777E5E15B80C2C"
)
CHECKPOINT2_ARRAYS_SHA256 = (
    "F55C1A37BF16720AA1BC61DC4BA42A410BD9DCA5399A2C38EC19D2AE295B8612"
)
ACCEPTED_SEALED_MANIFEST_SHA256 = (
    "B3CC70792E41E0EBDDE138057406C86D07063AD44959B595FA1B503B9D5AE2EA"
)
ACCEPTED_B2 = 0.006582827785543588
ACCEPTED_D2 = 0.05439336697877817

MAX_NEW_UPDATES = 4
MAX_NEW_POLICY_MAPS = 4
MAX_SELECTOR_EVALUATIONS = 3200
MAX_ROOT_INVOCATIONS = 1_245_024
MAX_INTERIOR_Z_ROOT_INVOCATIONS = 1_140_480
MAX_INTERIOR_A_ROOT_INVOCATIONS = 3200
MAX_JOINT_ROOT_INVOCATIONS = 3200

EXPECTED_CORE_SHA256 = {
    "src/ch5_two_asset_hank/corrected_diagnostic/selector.py": (
        "9FDE6B0CA44779DAB8A9EBBA093ABCEB1B8B3E746E0F94A7194B4EC8AE8DEEE0"
    ),
    "src/ch5_two_asset_hank/corrected_diagnostic/generator.py": (
        "F52451213E04EA999FE132B77AA92D1B66819B4D36BA5C539E9DD5EED4A63DB3"
    ),
    "src/ch5_two_asset_hank/corrected_diagnostic/option_a_step.py": (
        "9AB40DE5C621F8C0D508DCFD8556B40B3709CE0DAA4F18C5A408FCAA1CDD2A47"
    ),
    "src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py": (
        "F779CBC09CAB580A08FA783D51CBF158F29228F941AABC467AE107C36896A075"
    ),
    "src/ch5_two_asset_hank/corrected_diagnostic/checkpoint2_reexecution.py": (
        "78E5EA34026C51DA54C27BF11911339FEC9A03975D9E2CAE9F933845C7A576A4"
    ),
}


def _git_head(repository: Path) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=repository, text=True
    ).strip()


def _new_ledger() -> dict[str, Any]:
    return {
        "accepted_v0_loads": 0,
        "accepted_v1_loads": 0,
        "accepted_q1_loads": 0,
        "accepted_v2_loads": 0,
        "accepted_p2_loads": 0,
        "accepted_u2_loads": 0,
        "accepted_q2_loads": 0,
        "accepted_checkpoint2_manifest_loads": 0,
        "v2_policy_map_reruns": 0,
        "q2_assembly_reruns": 0,
        "new_corrected_policy_maps": 0,
        "selector_evaluations": 0,
        "scalar_root_invocations": 0,
        "interior_z_root_invocations": 0,
        "interior_a_switching_root_invocations": 0,
        "joint_switching_root_invocations": 0,
        "d2_assemblies": 0,
        "checkpoint_evaluations": 0,
        "direct_hjb_solves": 0,
        "hjb_updates": 0,
        "ordinary_graph_scc_summaries": 0,
        "terminal_topology_gates": 0,
        "terminal_dense_gesvd": 0,
        "terminal_normalized_stationary_candidates": 0,
        "terminal_q_transpose_times_p": 0,
        "terminal_kfe_svd_eigen_nullspace_qtp_calls": 0,
        "scientific_retries": 0,
        "solver_substitutions": 0,
        "damping_relaxation_adaptive_delta_continuation_calls": 0,
        "parameter_continuation_clipping_artificial_diffusion_calls": 0,
        "matlab_production_ge_irf_results_calls": 0,
        "matlab_production_outer_firm_ge_annual_shock_irf_results_calls": 0,
    }


def _check_task_ledger(ledger: dict[str, Any]) -> None:
    ceilings = {
        "v2_policy_map_reruns": 0,
        "q2_assembly_reruns": 0,
        "new_corrected_policy_maps": MAX_NEW_POLICY_MAPS,
        "selector_evaluations": MAX_SELECTOR_EVALUATIONS,
        "scalar_root_invocations": MAX_ROOT_INVOCATIONS,
        "interior_z_root_invocations": MAX_INTERIOR_Z_ROOT_INVOCATIONS,
        "interior_a_switching_root_invocations": MAX_INTERIOR_A_ROOT_INVOCATIONS,
        "joint_switching_root_invocations": MAX_JOINT_ROOT_INVOCATIONS,
        "d2_assemblies": MAX_NEW_POLICY_MAPS,
        "checkpoint_evaluations": MAX_NEW_POLICY_MAPS,
        "direct_hjb_solves": MAX_NEW_UPDATES,
        "hjb_updates": MAX_NEW_UPDATES,
        "ordinary_graph_scc_summaries": 0,
        "terminal_topology_gates": 0,
        "terminal_dense_gesvd": 0,
        "terminal_normalized_stationary_candidates": 0,
        "terminal_q_transpose_times_p": 0,
        "terminal_kfe_svd_eigen_nullspace_qtp_calls": 0,
        "scientific_retries": 0,
        "solver_substitutions": 0,
        "damping_relaxation_adaptive_delta_continuation_calls": 0,
        "parameter_continuation_clipping_artificial_diffusion_calls": 0,
        "matlab_production_ge_irf_results_calls": 0,
        "matlab_production_outer_firm_ge_annual_shock_irf_results_calls": 0,
    }
    breaches = {
        key: {"actual": int(ledger[key]), "ceiling": ceiling}
        for key, ceiling in ceilings.items()
        if int(ledger[key]) > ceiling
    }
    if breaches:
        raise FailClosed(
            "BLOCKED__TASK_SCIENTIFIC_LEDGER_CEILING",
            {"stage": "scientific_ledger_ceiling", "breaches": breaches},
        )


def classify_checkpoint(
    *,
    checkpoint: int,
    bellman_residual: float,
    value_change: float,
    exact_period: int | None,
    approximate_cycle: dict[str, Any] | None,
) -> str | None:
    """Apply the Owner gate order without evaluating later gates early."""
    if primary_converged(bellman_residual, value_change):
        return "HJB_CONVERGENCE_CANDIDATE__TERMINAL_GATE_NOT_RUN"
    if exact_period is not None:
        return "EXACT_CYCLE"
    if approximate_cycle is not None:
        return f"APPROXIMATE_PERIOD_{int(approximate_cycle['period'])}_CYCLE"
    if checkpoint == 6:
        return "COMPLETE_CHECKPOINT6_NONCONVERGED__TERMINAL_GATE_NOT_RUN"
    return None


def detect_authorized_approximate_cycle(
    values: list[np.ndarray], *, checkpoint: int
) -> dict[str, Any] | None:
    """Expose only the task-authorized windows: P2 at V4 and P3 at V6."""
    if checkpoint < 4:
        return None
    if checkpoint < 6:
        return detect_approximate_cycle(values[-4:], tolerance=CYCLE_TOLERANCE)
    return detect_approximate_cycle(values, tolerance=CYCLE_TOLERANCE)


def _read_focused_tests(path: Path) -> dict[str, Any]:
    root = ET.parse(path).getroot()
    suites = [root] if root.tag == "testsuite" else list(root.findall("testsuite"))
    totals = {
        key: sum(int(float(suite.attrib.get(key, "0"))) for suite in suites)
        for key in ("tests", "failures", "errors", "skipped")
    }
    if totals["tests"] < 1 or totals["failures"] or totals["errors"]:
        raise FailClosed(
            "BLOCKED__ENGINEERING_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE",
            {"stage": "focused_tests_not_green", "totals": totals},
        )
    return {
        "status": "PASS",
        "totals": totals,
        "source_path": str(path.resolve()),
        "source_sha256": _sha256(path),
    }


def _load_rows(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for flat in range(N):
        receipt = json.loads((root / f"cell_{flat:04d}.json").read_text(encoding="utf-8"))
        result = receipt.get("selector_result", {})
        if (
            int(receipt.get("flat_index_f_zero_based", -1)) != flat
            or result.get("outcome") != "SELECTED_ADMISSIBLE"
            or not isinstance(result.get("selected"), dict)
        ):
            raise FailClosed(
                "BLOCKED__ACCEPTED_CHECKPOINT2_PROVENANCE_DRIFT",
                {"stage": "accepted_p2_receipt", "flat": flat},
            )
        rows.append(result["selected"])
    return rows


def _load_accepted_checkpoint2(repository: Path, inputs: Any) -> dict[str, Any]:
    source = _load_sources(repository, inputs)
    root = repository / ACCEPTED_ROOT_RELATIVE
    manifest_path = root / "sealed_manifest.json"
    checkpoint_root = root / "checkpoint_002"
    arrays_path = checkpoint_root / "checkpoint_arrays.npz"
    q2_path = checkpoint_root / "q_generator.npz"
    checkpoint_manifest_path = checkpoint_root / "checkpoint_manifest.json"
    if _sha256(manifest_path) != ACCEPTED_SEALED_MANIFEST_SHA256:
        raise FailClosed(
            "BLOCKED__ACCEPTED_CHECKPOINT2_PROVENANCE_DRIFT",
            {"stage": "accepted_sealed_manifest_hash"},
        )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    _verify_manifest_files(root, manifest)
    if _sha256(arrays_path) != CHECKPOINT2_ARRAYS_SHA256:
        raise FailClosed(
            "BLOCKED__ACCEPTED_CHECKPOINT2_PROVENANCE_DRIFT",
            {"stage": "accepted_checkpoint2_arrays_hash"},
        )
    if _sha256(q2_path) != Q2_ARTIFACT_SHA256:
        raise FailClosed(
            "BLOCKED__ACCEPTED_CHECKPOINT2_PROVENANCE_DRIFT",
            {"stage": "accepted_q2_artifact_hash"},
        )
    rows = _load_rows(checkpoint_root)
    policy_arrays = _policy_arrays(rows)
    policy_identity = _canonical_sha256([_selected_identity(row) for row in rows])
    with np.load(arrays_path, allow_pickle=False) as loaded:
        v2 = np.array(loaded["value"], dtype=float, copy=True, order="F")
        utility = np.array(loaded["utility"], dtype=float, copy=True, order="F")
        mu_b = np.array(loaded["mu_b"], dtype=float, copy=True, order="F")
        mu_a = np.array(loaded["mu_a"], dtype=float, copy=True, order="F")
    q2 = sparse.csr_matrix(sparse.load_npz(q2_path))
    checkpoint_manifest = json.loads(checkpoint_manifest_path.read_text(encoding="utf-8"))
    checks = {
        "v0_exact": _field_sha256(source["v0"]) == V0_FIELD_SHA256,
        "v1_exact": _field_sha256(source["v1"]) == V1_FIELD_SHA256,
        "v2_source_exact": _field_sha256(source["v2"]) == V2_FIELD_SHA256,
        "v2_checkpoint_exact": _field_sha256(v2) == V2_FIELD_SHA256,
        "v2_arrays_equal": np.array_equal(source["v2"], v2),
        "p2_exact": policy_identity == P2_IDENTITY_SHA256,
        "u2_exact": _field_sha256(utility) == U2_FIELD_SHA256,
        "utility_rows_equal": np.array_equal(policy_arrays["utility"], utility),
        "mu_b_rows_equal": np.array_equal(policy_arrays["g_b"], mu_b),
        "mu_a_rows_equal": np.array_equal(policy_arrays["g_a"], mu_a),
        "q2_shape": q2.shape == (N, N),
        "q2_identity_exact": _sparse_identity(q2) == Q2_IDENTITY,
        "checkpoint2_identity_exact": checkpoint_identity(
            V2_FIELD_SHA256, policy_identity, _sparse_identity(q2)
        )
        == CHECKPOINT2_IDENTITY_SHA256,
        "checkpoint2_b_exact": float(checkpoint_manifest["bellman_residual_inf"])
        == ACCEPTED_B2,
        "checkpoint2_d_exact": float(checkpoint_manifest["value_change_inf"])
        == ACCEPTED_D2,
        "checkpoint2_nonconverged": checkpoint_manifest["primary_convergence_pass"]
        is False,
    }
    if not all(checks.values()):
        raise FailClosed(
            "BLOCKED__ACCEPTED_CHECKPOINT2_PROVENANCE_DRIFT",
            {"stage": "accepted_checkpoint2_binding", "checks": checks},
        )
    p1_identity = _canonical_sha256(
        [_selected_identity(row) for row in source["p1_rows"]]
    )
    checkpoint1_identity = checkpoint_identity(
        V1_FIELD_SHA256, p1_identity, _sparse_identity(source["q1"])
    )
    return {
        "v0": source["v0"],
        "v1": source["v1"],
        "v2": v2,
        "p1_rows": source["p1_rows"],
        "q1": source["q1"],
        "p2_rows": rows,
        "p2_arrays": policy_arrays,
        "q2": q2,
        "checkpoint1_identity": checkpoint1_identity,
        "checkpoint2_identity": CHECKPOINT2_IDENTITY_SHA256,
        "v2_policy_map_rerun": False,
        "q2_assembly_rerun": False,
        "checks": checks,
        "manifest_entry_count": int(manifest["entry_count"]),
        "identities": {
            "v0": V0_FIELD_SHA256,
            "v1": V1_FIELD_SHA256,
            "q1": source["identities"]["q1_artifact"],
            "v2": V2_FIELD_SHA256,
            "p2": P2_IDENTITY_SHA256,
            "u2": U2_FIELD_SHA256,
            "q2": Q2_ARTIFACT_SHA256,
            "q2_components": Q2_IDENTITY,
            "checkpoint2": CHECKPOINT2_IDENTITY_SHA256,
            "checkpoint2_arrays": CHECKPOINT2_ARRAYS_SHA256,
            "sealed_manifest": ACCEPTED_SEALED_MANIFEST_SHA256,
        },
    }


def _switching_statistics(directory: Path) -> dict[str, Any]:
    categories = {
        "interior_a": "interior_a_switching_receipt",
        "joint": "joint_switching_receipt",
    }
    result: dict[str, Any] = {
        name: {
            "candidate_attempt_count": 0,
            "admissible_candidate_count": 0,
            "selected_policy_count": 0,
            "selected_flat_indices_f_zero_based": [],
            "root_status_counts": {},
        }
        for name in categories
    }
    selected_liquid_z: list[int] = []
    for flat in range(N):
        receipt = json.loads((directory / f"cell_{flat:04d}.json").read_text(encoding="utf-8"))
        selector_result = receipt["selector_result"]
        selected = selector_result.get("selected")
        if selected and selected.get("interior_z_receipt") is not None:
            selected_liquid_z.append(flat)
        for name, field in categories.items():
            candidates = [row for row in selector_result["candidates"] if row.get(field) is not None]
            summary = result[name]
            summary["candidate_attempt_count"] += len(candidates)
            summary["admissible_candidate_count"] += sum(
                bool(row["admissible"]) for row in candidates
            )
            counts = Counter(str(row["root_status"]) for row in candidates)
            prior = Counter(summary["root_status_counts"])
            summary["root_status_counts"] = dict(sorted((prior + counts).items()))
            if selected and selected.get(field) is not None:
                summary["selected_policy_count"] += 1
                summary["selected_flat_indices_f_zero_based"].append(flat)
    result["liquid_z"] = {
        "selected_policy_count": len(selected_liquid_z),
        "selected_flat_indices_f_zero_based": selected_liquid_z,
    }
    return result


def _solve_update(
    directory: Path,
    checkpoint: int,
    value: np.ndarray,
    utility: np.ndarray,
    q: sparse.csr_matrix,
    rho: float,
    ledger: dict[str, Any],
) -> np.ndarray:
    matrix = (rho + 1.0 / DELTA) * sparse.eye(N, format="csr") - q
    rhs = utility.ravel(order="F") + value.ravel(order="F") / DELTA
    ledger["direct_hjb_solves"] += 1
    ledger["hjb_updates"] += 1
    _check_task_ledger(ledger)
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
            "FAIL__DIRECT_HJB_SOLVE_ACCURACY_GATE",
            {"checkpoint_from": checkpoint, "stage": "direct_solve_exception"},
        ) from exc
    warning_rows = [
        {"category": row.category.__name__, "message": str(row.message)} for row in caught
    ]
    if warning_rows or next_flat.shape != (N,) or not np.all(np.isfinite(next_flat)):
        _write_json(
            directory / "direct_solve_receipt.json",
            {
                "status": "FAIL",
                "solver": "scipy.sparse.linalg.spsolve",
                "checkpoint_from": checkpoint,
                "checkpoint_to": checkpoint + 1,
                "warnings": warning_rows,
                "shape": list(next_flat.shape),
                "finite": bool(np.all(np.isfinite(next_flat))),
            },
        )
        raise FailClosed(
            "FAIL__DIRECT_HJB_SOLVE_ACCURACY_GATE",
            {
                "checkpoint_from": checkpoint,
                "stage": "warning_shape_or_nonfinite",
                "warnings": warning_rows,
                "shape": list(next_flat.shape),
            },
        )
    backward = normwise_backward_error(matrix, next_flat, rhs)
    residual = backward.pop("residual")
    next_value = next_flat.reshape(SHAPE, order="F")
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
        next_value=next_value,
        residual=residual,
    )
    receipt = {
        "status": "PASS" if passed else "FAIL",
        "solver": "scipy.sparse.linalg.spsolve",
        "checkpoint_from": checkpoint,
        "checkpoint_to": checkpoint + 1,
        "delta": DELTA,
        "warnings": warning_rows,
        **backward,
        "backward_error_threshold_inclusive": BACKWARD_ERROR_TOLERANCE,
        "matrix_identity": _sparse_identity(matrix),
        "rhs_sha256": _field_sha256(rhs),
        "next_value_sha256": _field_sha256(next_value),
        "residual_sha256": _field_sha256(residual),
        "arrays_artifact": {
            "path": "direct_update_arrays.npz",
            "bytes": (directory / "direct_update_arrays.npz").stat().st_size,
            "sha256": _sha256(directory / "direct_update_arrays.npz"),
        },
    }
    _write_json(directory / "direct_solve_receipt.json", receipt)
    if not passed:
        raise FailClosed(
            "FAIL__DIRECT_HJB_SOLVE_ACCURACY_GATE",
            {"checkpoint_from": checkpoint, "direct_solve": receipt},
        )
    return next_value


def _write_root_manifest(output: Path) -> None:
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
    _write_json(
        output / "sealed_manifest.json",
        {
            "schema": "CH5_D123_CHECKPOINT2_TO_CHECKPOINT6_CONTINUATION_V1",
            "entry_count": len(entries),
            "total_bytes": sum(int(row["bytes"]) for row in entries),
            "entries": entries,
        },
    )


def _finalize(
    repository: Path,
    output: Path,
    pre_hashes: dict[str, str],
    ledger: dict[str, Any],
    terminal: str,
    detail: dict[str, Any],
    started: float,
) -> str:
    _check_task_ledger(ledger)
    post_hashes = _scientific_code_hashes(repository)
    if post_hashes != pre_hashes:
        terminal = "BLOCKED__SCIENTIFIC_CODE_CHANGED_AFTER_FREEZE"
        detail = {"stage": "post_execution_code_hash", "prior_detail": detail}
    ledger["terminal_classification"] = terminal
    ledger["wall_seconds"] = float(time.perf_counter() - started)
    _write_json(output / "scientific_ledger.json", ledger)
    _write_json(
        output / "post_execution_code_freeze.json",
        {
            "scientific_code_sha256_after": post_hashes,
            "matches_pre_execution_freeze": post_hashes == pre_hashes,
        },
    )
    _write_json(
        output / "terminal_receipt.json",
        {"terminal_classification": terminal, "detail": detail},
    )
    _write_root_manifest(output)
    return terminal


def execute(
    repository: Path,
    seed_path: Path,
    binding_path: Path,
    focused_test_junit: Path,
) -> str:
    repository = repository.resolve(strict=True)
    output = repository / OUTPUT_RELATIVE
    clean_before_evidence = not subprocess.check_output(
        ["git", "status", "--porcelain"], cwd=repository, text=True
    ).strip()
    output.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    ledger = _new_ledger()
    pre_hashes = _scientific_code_hashes(repository)
    _write_json(
        output / "startup_manifest.json",
        {
            "task_id": TASK_ID,
            "execution_head": _git_head(repository),
            "baseline_live_main": BASELINE_SHA,
            "accepted_checkpoint2_identity": CHECKPOINT2_IDENTITY_SHA256,
            "accepted_checkpoint2_reused_without_policy_map_or_q2_assembly": True,
            "scientific_code_sha256_before": pre_hashes,
            "budget": {
                "direct_hjb_solves": MAX_NEW_UPDATES,
                "fresh_policy_maps": MAX_NEW_POLICY_MAPS,
                "selector_evaluations": MAX_SELECTOR_EVALUATIONS,
                "d2_q_assemblies": MAX_NEW_POLICY_MAPS,
                "checkpoint_evaluations": MAX_NEW_POLICY_MAPS,
                "terminal_topology_kfe_svd_eigen_nullspace_qtp": 0,
                "scientific_retries": 0,
            },
        },
    )
    try:
        core_checks = {
            relative: _sha256(repository / relative) == expected
            for relative, expected in EXPECTED_CORE_SHA256.items()
        }
        preflight = {
            "worktree_clean_before_evidence": clean_before_evidence,
            "origin_main_exact_baseline": subprocess.check_output(
                ["git", "rev-parse", "origin/main"], cwd=repository, text=True
            ).strip().upper()
            == BASELINE_SHA,
            "core_scientific_hashes_exact": all(core_checks.values()),
            "core_scientific_hash_checks": core_checks,
        }
        if not all(
            value for key, value in preflight.items() if key != "core_scientific_hash_checks"
        ):
            raise FailClosed(
                "BLOCKED__ENGINEERING_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE",
                {"stage": "git_or_scientific_code_binding", "checks": preflight},
            )
        focused = _read_focused_tests(focused_test_junit.resolve(strict=True))
        shutil.copyfile(focused_test_junit, output / "focused_tests.xml")
        focused["copied_sha256"] = _sha256(output / "focused_tests.xml")
        _write_json(output / "focused_test_receipt.json", focused)
        inputs = bind_option_a_inputs(seed_path, binding_path)
        accepted = _load_accepted_checkpoint2(repository, inputs)
        ledger.update(
            accepted_v0_loads=1,
            accepted_v1_loads=1,
            accepted_q1_loads=1,
            accepted_v2_loads=1,
            accepted_p2_loads=1,
            accepted_u2_loads=1,
            accepted_q2_loads=1,
            accepted_checkpoint2_manifest_loads=1,
        )
        _write_json(
            output / "accepted_checkpoint2_binding.json",
            {
                "status": "PASS",
                "input_identity": _input_receipt(inputs),
                "identities": accepted["identities"],
                "checks": accepted["checks"],
                "accepted_manifest_entry_count": accepted["manifest_entry_count"],
                "v2_policy_map_rerun": False,
                "q2_assembly_rerun": False,
            },
        )
        values = [accepted["v0"], accepted["v1"], accepted["v2"]]
        identities = [
            accepted["checkpoint1_identity"],
            accepted["checkpoint2_identity"],
        ]
        previous_rows = accepted["p2_rows"]
        previous_arrays = accepted["p2_arrays"]
        previous_q = accepted["q2"]
        checkpoint2_dir = output / "checkpoint_002"
        checkpoint2_dir.mkdir(parents=False, exist_ok=False)
        _write_json(
            checkpoint2_dir / "accepted_source_receipt.json",
            {
                "checkpoint": 2,
                "accepted_checkpoint_identity": CHECKPOINT2_IDENTITY_SHA256,
                "accepted_bellman_residual_inf": ACCEPTED_B2,
                "accepted_value_change_inf": ACCEPTED_D2,
                "v2_policy_map_rerun": False,
                "q2_assembly_rerun": False,
            },
        )
        current_value = _solve_update(
            checkpoint2_dir,
            2,
            accepted["v2"],
            accepted["p2_arrays"]["utility"],
            accepted["q2"],
            float(inputs.scalars["rho"]),
            ledger,
        )
        _seal_directory(checkpoint2_dir, "CH5_D123_ACCEPTED_CHECKPOINT2_UPDATE_TO_3_V1")
        values.append(current_value)
        budget = SelectorBudget(
            max_selector_evaluations=MAX_SELECTOR_EVALUATIONS,
            max_root_invocations=MAX_ROOT_INVOCATIONS,
            max_interior_z_root_invocations=MAX_INTERIOR_Z_ROOT_INVOCATIONS,
            max_interior_a_switching_root_invocations=MAX_INTERIOR_A_ROOT_INVOCATIONS,
            max_joint_switching_root_invocations=MAX_JOINT_ROOT_INVOCATIONS,
        )
        final_metrics: dict[str, Any] = {}
        for checkpoint in range(3, 7):
            rows, arrays, q, d2_receipt = _map_checkpoint(
                repository,
                output,
                checkpoint,
                current_value,
                inputs,
                budget,
                ledger,
                pre_hashes,
            )
            ledger["checkpoint_evaluations"] += 1
            _check_task_ledger(ledger)
            directory = output / f"checkpoint_{checkpoint:03d}"
            policy_diagnostics = _policy_diagnostics(
                rows, previous_rows, arrays, previous_arrays
            )
            operator_diagnostics = _operator_diagnostics(q, previous_q)
            switching = _switching_statistics(directory)
            _write_json(directory / "switching_statistics.json", switching)
            bellman = (
                float(inputs.scalars["rho"]) * current_value.ravel(order="F")
                - arrays["utility"].ravel(order="F")
                - np.asarray(q @ current_value.ravel(order="F")).ravel()
            )
            value_change = current_value - values[-2]
            if not np.all(np.isfinite(bellman)) or not np.all(np.isfinite(value_change)):
                raise FailClosed(
                    "FAIL__NONFINITE_OR_PROVENANCE_GATE",
                    {"checkpoint": checkpoint, "stage": "checkpoint_metric_nonfinite"},
                )
            bellman_inf = float(np.linalg.norm(bellman, ord=np.inf))
            value_change_inf = float(
                np.linalg.norm(value_change.ravel(order="F"), ord=np.inf)
            )
            q_identity = _sparse_identity(q)
            identity = checkpoint_identity(
                _field_sha256(current_value),
                str(policy_diagnostics["identity_sha256"]),
                q_identity,
            )
            identities.append(identity)
            converged = primary_converged(bellman_inf, value_change_inf)
            exact_period = None
            approximate = None
            if not converged:
                exact_period = detect_exact_cycle(identities)
                if exact_period is None:
                    approximate = detect_authorized_approximate_cycle(
                        values, checkpoint=checkpoint
                    )
            cycle_receipt = {
                "checkpoint": checkpoint,
                "primary_convergence_evaluated_first": True,
                "primary_convergence_pass": converged,
                "exact_evaluated_only_after_primary_failure": not converged,
                "exact_period": exact_period,
                "approximate_evaluated_only_after_primary_and_exact_nonterminal": (
                    not converged and exact_period is None
                ),
                "approximate_period_2_or_3": approximate,
                "approximate_period_2_window_available": checkpoint >= 4,
                "approximate_period_3_window_available": checkpoint >= 6,
            }
            _write_json(directory / "cycle_detection_receipt.json", cycle_receipt)
            terminal = classify_checkpoint(
                checkpoint=checkpoint,
                bellman_residual=bellman_inf,
                value_change=value_change_inf,
                exact_period=exact_period,
                approximate_cycle=approximate,
            )
            np.savez_compressed(
                directory / "checkpoint_arrays.npz",
                value=current_value,
                utility=arrays["utility"],
                mu_b=arrays["g_b"],
                mu_a=arrays["g_a"],
                bellman_residual=bellman,
                value_change=value_change,
            )
            metrics = {
                "checkpoint": checkpoint,
                "value_sha256": _field_sha256(current_value),
                "policy_identity_sha256": policy_diagnostics["identity_sha256"],
                "utility_sha256": _field_sha256(arrays["utility"]),
                "q_artifact_sha256": d2_receipt["q_artifact"]["sha256"],
                "q_identity": q_identity,
                "checkpoint_identity_sha256": identity,
                "bellman_residual_inf": bellman_inf,
                "bellman_threshold_inclusive": BELLMAN_TOLERANCE,
                "value_change_inf": value_change_inf,
                "value_change_threshold_inclusive": VALUE_TOLERANCE,
                "primary_convergence_pass": converged,
                "policy_diagnostics": policy_diagnostics,
                "operator_diagnostics": operator_diagnostics,
                "switching_statistics": switching,
                "cycle_diagnostics": cycle_receipt,
                "d2_receipt_status": d2_receipt["status"],
                "cumulative_scientific_ledger": dict(ledger),
                "checkpoint_arrays": {
                    "path": "checkpoint_arrays.npz",
                    "bytes": (directory / "checkpoint_arrays.npz").stat().st_size,
                    "sha256": _sha256(directory / "checkpoint_arrays.npz"),
                    "bellman_residual_sha256": _field_sha256(bellman),
                    "value_change_sha256": _field_sha256(value_change),
                },
            }
            final_metrics = metrics
            if terminal is not None:
                metrics["disposition"] = terminal
                _write_json(directory / "checkpoint_manifest.json", metrics)
                _seal_directory(directory, "CH5_D123_BOUNDED_CONTINUATION_CHECKPOINT_V1")
                return _finalize(
                    repository,
                    output,
                    pre_hashes,
                    ledger,
                    terminal,
                    {"final_checkpoint": checkpoint, "terminal_metrics": metrics},
                    started,
                )
            next_value = _solve_update(
                directory,
                checkpoint,
                current_value,
                arrays["utility"],
                q,
                float(inputs.scalars["rho"]),
                ledger,
            )
            metrics["disposition"] = "CONTINUE_TO_NEXT_CHECKPOINT"
            metrics["direct_solve"] = json.loads(
                (directory / "direct_solve_receipt.json").read_text(encoding="utf-8")
            )
            _write_json(directory / "checkpoint_manifest.json", metrics)
            _seal_directory(directory, "CH5_D123_BOUNDED_CONTINUATION_CHECKPOINT_V1")
            if _scientific_code_hashes(repository) != pre_hashes:
                raise FailClosed(
                    "BLOCKED__SCIENTIFIC_CODE_CHANGED_AFTER_FREEZE",
                    {"checkpoint": checkpoint, "stage": "post_update_code_hash"},
                )
            previous_rows = rows
            previous_arrays = arrays
            previous_q = q
            current_value = next_value
            values.append(current_value)
        raise FailClosed(
            "BLOCKED__UNREACHABLE_CONTINUATION_STATE",
            {"stage": "loop_exhausted", "terminal_metrics": final_metrics},
        )
    except FailClosed as failure:
        return _finalize(
            repository,
            output,
            pre_hashes,
            ledger,
            failure.terminal,
            failure.detail,
            started,
        )
    except Exception as exc:
        terminal = (
            "FAIL__SCIENTIFIC_GATE_AFTER_ENTRY"
            if ledger["direct_hjb_solves"] or ledger["new_corrected_policy_maps"]
            else "BLOCKED__ENGINEERING_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE"
        )
        return _finalize(
            repository,
            output,
            pre_hashes,
            ledger,
            terminal,
            {"stage": "unhandled_exception", "type": type(exc).__name__, "message": str(exc)},
            started,
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--seed", type=Path, required=True)
    parser.add_argument("--binding", type=Path, required=True)
    parser.add_argument("--focused-test-junit", type=Path, required=True)
    args = parser.parse_args(argv)
    terminal = execute(
        args.repository, args.seed, args.binding, args.focused_test_junit
    )
    print(terminal)
    successful = {
        "HJB_CONVERGENCE_CANDIDATE__TERMINAL_GATE_NOT_RUN",
        "COMPLETE_CHECKPOINT6_NONCONVERGED__TERMINAL_GATE_NOT_RUN",
    }
    return 0 if terminal in successful else 2


if __name__ == "__main__":
    sys.exit(main())
