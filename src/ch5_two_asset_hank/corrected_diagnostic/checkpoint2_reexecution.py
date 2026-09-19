"""One-shot adopted interior-a switching V2 remap; no HJB/KFE continuation."""

from __future__ import annotations

import argparse
from dataclasses import asdict
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time
from typing import Any
import xml.etree.ElementTree as ET

import numpy as np
from scipy import sparse

from .nonlinear_continuation import (
    BELLMAN_TOLERANCE,
    CYCLE_TOLERANCE,
    N,
    OPTION_A_RELATIVE,
    Q1_MANIFEST_SHA256,
    Q1_SHA256,
    SHAPE,
    VALUE_TOLERANCE,
    V0_FIELD_SHA256,
    V1_FIELD_SHA256,
    V1_Q1_RELATIVE,
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
    _verify_manifest_files,
    _write_json,
    checkpoint_identity,
    detect_approximate_cycle,
    detect_exact_cycle,
    primary_converged,
)
from .option_a_step import _input_receipt, bind_option_a_inputs
from .selector import SelectorBudget


TASK_ID = (
    "CH5_MP4C_2018_KFE_D123_INTERIOR_A_ZERO_DRIFT_SWITCHING_"
    "IMPLEMENTATION_AND_V2_CHECKPOINT2_REEXECUTION_20260919"
)
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_interior_a_zero_drift_switching_"
    "implementation_v2_checkpoint2_reexecution_20260919_run001"
)
BASELINE_SHA = "869F4023AE7B674D483F926F85E0DE271479DA0E"
PRE_ADOPTION_SELECTOR_SHA256 = (
    "DBEB8EDCDA18B14579F36C2B68A50A47C9E717F49E84BC31A2E4E17180E9C327"
)
PRE_ADOPTION_SELECTOR_BLOB = "eac9b06805e2bcb69e078fd927a9a641c6cafd96"
IMPLEMENTED_SELECTOR_SHA256 = (
    "3175FBBC99120A9735287594A27602205505048BADD11A989CEAC682BE6390D8"
)
V1_ARTIFACT_SHA256 = (
    "28A27473A4C08CCD20550B9EDF1509BABB4D7D882A9429F7F54F55DE72083173"
)
V2_SOURCE_ROOT = Path(
    "reports/ch5_mp4c_2018_kfe_d123_bounded_nonlinear_hjb_kfe_"
    "continuation_20260917"
)
V2_ARTIFACT_RELATIVE = Path("checkpoint_001/direct_update_arrays.npz")
V2_ARTIFACT_SHA256 = (
    "FD8456D533A724BCD8099AF52A8AB7559EF3A99C6307E4ED85CB02A618CEFA16"
)
V2_FIELD_SHA256 = (
    "A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1"
)
V2_SOURCE_MANIFEST_SHA256 = (
    "FC323B9691E28F20305CF5F71DD379C445CB80A506313A67DBC1954E88A5E041"
)
MAX_SELECTOR_EVALUATIONS = 800
MAX_ROOT_INVOCATIONS = 311_256
MAX_INTERIOR_Z_ROOT_INVOCATIONS = 285_120
MAX_INTERIOR_A_SWITCHING_ROOT_INVOCATIONS = 800


def _git_head(repository: Path) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=repository, text=True
    ).strip()


def _git_blob(repository: Path, revision: str, relative: str) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", f"{revision}:{relative}"], cwd=repository, text=True
    ).strip()


def _new_ledger() -> dict[str, Any]:
    return {
        "accepted_v1_artifact_loads": 0,
        "accepted_v2_artifact_loads": 0,
        "accepted_q1_loads": 0,
        "new_corrected_policy_maps": 0,
        "selector_evaluations": 0,
        "scalar_root_invocations": 0,
        "interior_z_root_invocations": 0,
        "interior_a_switching_root_invocations": 0,
        "d2_assemblies": 0,
        "checkpoint2_diagnostic_evaluations": 0,
        "direct_hjb_solves": 0,
        "v2_to_v3_hjb_updates": 0,
        "ordinary_graph_scc_summaries": 0,
        "terminal_topology_gates": 0,
        "terminal_dense_gesvd": 0,
        "terminal_normalized_stationary_candidates": 0,
        "terminal_q_transpose_times_p": 0,
        "scientific_retries": 0,
        "solver_substitutions": 0,
        "damping_relaxation_adaptive_delta_continuation_calls": 0,
        "matlab_production_outer_firm_ge_annual_shock_irf_results_calls": 0,
    }


def _check_task_ledger(ledger: dict[str, Any]) -> None:
    ceilings = {
        "new_corrected_policy_maps": 1,
        "selector_evaluations": MAX_SELECTOR_EVALUATIONS,
        "scalar_root_invocations": MAX_ROOT_INVOCATIONS,
        "interior_z_root_invocations": MAX_INTERIOR_Z_ROOT_INVOCATIONS,
        "interior_a_switching_root_invocations": (
            MAX_INTERIOR_A_SWITCHING_ROOT_INVOCATIONS
        ),
        "d2_assemblies": 1,
        "checkpoint2_diagnostic_evaluations": 1,
        "direct_hjb_solves": 0,
        "v2_to_v3_hjb_updates": 0,
        "ordinary_graph_scc_summaries": 0,
        "terminal_topology_gates": 0,
        "terminal_dense_gesvd": 0,
        "terminal_normalized_stationary_candidates": 0,
        "terminal_q_transpose_times_p": 0,
        "scientific_retries": 0,
        "solver_substitutions": 0,
        "damping_relaxation_adaptive_delta_continuation_calls": 0,
        "matlab_production_outer_firm_ge_annual_shock_irf_results_calls": 0,
    }
    breaches = {
        name: {"actual": int(ledger[name]), "ceiling": ceiling}
        for name, ceiling in ceilings.items()
        if int(ledger[name]) > ceiling
    }
    if breaches:
        raise FailClosed(
            "BLOCKED__INTERIOR_A_SWITCHING_IMPLEMENTATION_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE",
            {"stage": "task_ledger_ceiling", "breaches": breaches},
        )


def _read_focused_tests(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FailClosed(
            "BLOCKED__INTERIOR_A_SWITCHING_IMPLEMENTATION_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE",
            {"stage": "focused_test_receipt_missing", "path": str(path)},
        )
    root = ET.parse(path).getroot()
    suites = [root] if root.tag == "testsuite" else list(root.findall("testsuite"))
    totals = {
        name: sum(int(float(suite.attrib.get(name, "0"))) for suite in suites)
        for name in ("tests", "failures", "errors", "skipped")
    }
    if totals["tests"] < 1 or totals["failures"] or totals["errors"]:
        raise FailClosed(
            "BLOCKED__INTERIOR_A_SWITCHING_IMPLEMENTATION_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE",
            {"stage": "focused_tests_not_green", "totals": totals},
        )
    return {
        "status": "PASS",
        "totals": totals,
        "source_path": str(path.resolve()),
        "source_sha256": _sha256(path),
    }


def _switching_statistics(directory: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    attempts = 0
    admissible = 0
    selected = 0
    root_statuses: dict[str, int] = {}
    selected_flats: list[int] = []
    cell100: dict[str, Any] | None = None
    for flat in range(N):
        receipt = json.loads(
            (directory / f"cell_{flat:04d}.json").read_text(encoding="utf-8")
        )
        result = receipt["selector_result"]
        switching = [
            row
            for row in result["candidates"]
            if row.get("interior_a_switching_receipt") is not None
        ]
        attempts += len(switching)
        admissible += sum(bool(row["admissible"]) for row in switching)
        for row in switching:
            status = str(row["root_status"])
            root_statuses[status] = root_statuses.get(status, 0) + 1
        chosen = result.get("selected")
        if chosen and chosen.get("interior_a_switching_receipt") is not None:
            selected += 1
            selected_flats.append(flat)
        if flat == 100:
            cell100 = receipt
    if cell100 is None:
        raise FailClosed(
            "FAIL__ADOPTED_INTERIOR_A_SWITCHING_V2_MAP_FIRST_FAILURE",
            {"stage": "cell100_switching_receipt_missing"},
        )
    cell100_selected = cell100["selector_result"].get("selected")
    if (
        cell100["selector_result"].get("outcome") != "SELECTED_ADMISSIBLE"
        or not cell100_selected
        or cell100_selected.get("interior_a_switching_receipt") is None
    ):
        raise FailClosed(
            "FAIL__ADOPTED_INTERIOR_A_SWITCHING_V2_MAP_FIRST_FAILURE",
            {"stage": "cell100_switching_not_selected"},
        )
    return (
        {
            "candidate_attempt_count": attempts,
            "admissible_candidate_count": admissible,
            "selected_policy_count": selected,
            "selected_flat_indices_f_zero_based": selected_flats,
            "root_status_counts": root_statuses,
        },
        cell100,
    )


def _load_sources(repository: Path, inputs: Any) -> dict[str, Any]:
    option_a = repository / OPTION_A_RELATIVE
    v1_q1 = repository / V1_Q1_RELATIVE
    v1_path = option_a / "direct_step_arrays.npz"
    q1_path = v1_q1 / "q1_generator.npz"
    q1_manifest_path = v1_q1 / "sealed_manifest.json"
    v2_root = repository / V2_SOURCE_ROOT
    v2_manifest_path = v2_root / "sealed_manifest.json"
    v2_artifact_path = v2_root / V2_ARTIFACT_RELATIVE
    expected = {
        v1_path: V1_ARTIFACT_SHA256,
        q1_path: Q1_SHA256,
        q1_manifest_path: Q1_MANIFEST_SHA256,
        v2_manifest_path: V2_SOURCE_MANIFEST_SHA256,
        v2_artifact_path: V2_ARTIFACT_SHA256,
    }
    for path, sha256 in expected.items():
        if _sha256(path) != sha256:
            raise FailClosed(
                "BLOCKED__INTERIOR_A_SWITCHING_IMPLEMENTATION_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE",
                {"stage": "accepted_artifact_hash", "path": str(path)},
            )
    q1_manifest = json.loads(q1_manifest_path.read_text(encoding="utf-8"))
    v2_manifest = json.loads(v2_manifest_path.read_text(encoding="utf-8"))
    _verify_manifest_files(v1_q1, q1_manifest)
    _verify_manifest_files(v2_root, v2_manifest)
    with np.load(v1_path, allow_pickle=False) as loaded:
        v0 = np.array(loaded["v0"], dtype=float, copy=True, order="F")
        v1 = np.array(loaded["v1"], dtype=float, copy=True, order="F")
    with np.load(v2_artifact_path, allow_pickle=False) as loaded:
        v2 = np.array(loaded["next_value"], dtype=float, copy=True, order="F")
    if (
        inputs.grid.shape != SHAPE
        or any(value.shape != SHAPE for value in (v0, v1, v2))
        or not all(np.all(np.isfinite(value)) for value in (v0, v1, v2))
        or _field_sha256(v0) != V0_FIELD_SHA256
        or _field_sha256(v1) != V1_FIELD_SHA256
        or _field_sha256(v2) != V2_FIELD_SHA256
    ):
        raise FailClosed(
            "BLOCKED__INTERIOR_A_SWITCHING_IMPLEMENTATION_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE",
            {"stage": "accepted_value_identity"},
        )
    selected_rows: list[dict[str, Any]] = []
    for flat in range(N):
        receipt = json.loads(
            (v1_q1 / f"cell_{flat:04d}.json").read_text(encoding="utf-8")
        )
        result = receipt.get("selector_result", {})
        if (
            int(receipt["flat_index_f_zero_based"]) != flat
            or result.get("outcome") != "SELECTED_ADMISSIBLE"
            or not isinstance(result.get("selected"), dict)
        ):
            raise FailClosed(
                "BLOCKED__INTERIOR_A_SWITCHING_IMPLEMENTATION_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE",
                {"stage": "accepted_p1_receipt", "flat": flat},
            )
        selected_rows.append(result["selected"])
    q1 = sparse.load_npz(q1_path)
    if getattr(q1, "format", None) != "csr" or q1.shape != (N, N):
        raise FailClosed(
            "BLOCKED__INTERIOR_A_SWITCHING_IMPLEMENTATION_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE",
            {"stage": "accepted_q1_shape_format"},
        )
    return {
        "v0": v0,
        "v1": v1,
        "v2": v2,
        "p1_rows": selected_rows,
        "p1_arrays": _policy_arrays(selected_rows),
        "q1": sparse.csr_matrix(q1),
        "identities": {
            "v1_artifact": V1_ARTIFACT_SHA256,
            "v2_artifact": V2_ARTIFACT_SHA256,
            "v2_field": V2_FIELD_SHA256,
            "q1_artifact": Q1_SHA256,
            "q1_manifest": Q1_MANIFEST_SHA256,
            "v2_source_manifest": V2_SOURCE_MANIFEST_SHA256,
        },
    }


def _write_manifest(output: Path) -> None:
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
            "schema": "CH5_D123_INTERIOR_A_SWITCHING_V2_CHECKPOINT2_REEXECUTION_V1",
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
        terminal = "BLOCKED__INTERIOR_A_SWITCHING_IMPLEMENTATION_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE"
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
    _write_manifest(output)
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
            "accepted_v2_sha256": V2_FIELD_SHA256,
            "owner_adoption": (
                "OWNER_ADOPTED__INTERIOR_A_ZERO_DRIFT_SWITCHING_LAW__"
                "BOUNDED_CORRECTED_DIAGNOSTIC_IMPLEMENTATION_AUTHORIZED"
            ),
            "pre_adoption_selector_sha256": PRE_ADOPTION_SELECTOR_SHA256,
            "implemented_selector_sha256": IMPLEMENTED_SELECTOR_SHA256,
            "scientific_code_sha256_before": pre_hashes,
            "budget": {
                "fresh_v2_policy_map_attempts": 1,
                "selector_evaluations": MAX_SELECTOR_EVALUATIONS,
                "adopted_interior_a_switching_roots": (
                    MAX_INTERIOR_A_SWITCHING_ROOT_INVOCATIONS
                ),
                "d2_assemblies_if_complete_map": 1,
                "checkpoint2_diagnostics_if_q2_exists": 1,
                "v2_to_v3_hjb_updates": 0,
                "terminal_kfe_topology_svd_eigen_nullspace_qtp": 0,
                "scientific_retries": 0,
            },
        },
    )
    try:
        selector_path = (
            repository / "src/ch5_two_asset_hank/corrected_diagnostic/selector.py"
        )
        checks = {
            "pre_adoption_selector_blob_at_baseline_exact": _git_blob(
                repository,
                BASELINE_SHA,
                "src/ch5_two_asset_hank/corrected_diagnostic/selector.py",
            )
            == PRE_ADOPTION_SELECTOR_BLOB,
            "pre_adoption_selector_authority_exact": _sha256(
                repository
                / "docs/CH5_MP4C_2018_KFE_D123_INTERIOR_A_ZERO_DRIFT_"
                "SWITCHING_OWNER_ADOPTION_20260919.md"
            )
            == "F5C4515078BBFFE32F9924758AF2DC5DD1C344A86DEB3EB596AFF91106F2FD95",
            "implemented_selector_exact": _sha256(selector_path)
            == IMPLEMENTED_SELECTOR_SHA256,
            "worktree_clean_before_evidence": clean_before_evidence,
        }
        if not all(checks.values()):
            raise FailClosed(
                "BLOCKED__INTERIOR_A_SWITCHING_IMPLEMENTATION_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE",
                {"stage": "git_or_selector_binding", "checks": checks},
            )
        focused = _read_focused_tests(focused_test_junit.resolve(strict=True))
        shutil.copyfile(focused_test_junit, output / "focused_tests.xml")
        focused["copied_sha256"] = _sha256(output / "focused_tests.xml")
        _write_json(output / "focused_test_receipt.json", focused)
        inputs = bind_option_a_inputs(seed_path, binding_path)
        sources = _load_sources(repository, inputs)
        ledger["accepted_v1_artifact_loads"] = 1
        ledger["accepted_v2_artifact_loads"] = 1
        ledger["accepted_q1_loads"] = 1
        _write_json(
            output / "accepted_v2_binding.json",
            {
                "status": "PASS",
                "input_identity": _input_receipt(inputs),
                "accepted_identities": sources["identities"],
                "p1_receipts_loaded": len(sources["p1_rows"]),
                "v1_policy_map_rerun": False,
                "v1_to_v2_hjb_solve_rerun": False,
            },
        )
        budget = SelectorBudget(
            max_selector_evaluations=MAX_SELECTOR_EVALUATIONS,
            max_root_invocations=MAX_ROOT_INVOCATIONS,
            max_interior_z_root_invocations=MAX_INTERIOR_Z_ROOT_INVOCATIONS,
            max_interior_a_switching_root_invocations=(
                MAX_INTERIOR_A_SWITCHING_ROOT_INVOCATIONS
            ),
        )
        p2_rows, p2_arrays, q2, d2_receipt = _map_checkpoint(
            repository,
            output,
            2,
            sources["v2"],
            inputs,
            budget,
            ledger,
            pre_hashes,
        )
        switching_statistics, cell100_receipt = _switching_statistics(
            output / "checkpoint_002"
        )
        _write_json(output / "switching_statistics.json", switching_statistics)
        _write_json(output / "cell100_switching_receipt.json", cell100_receipt)
        ledger["checkpoint2_diagnostic_evaluations"] = 1
        _check_task_ledger(ledger)
        policy_diagnostics = _policy_diagnostics(
            p2_rows, sources["p1_rows"], p2_arrays, sources["p1_arrays"]
        )
        operator_diagnostics = _operator_diagnostics(q2, sources["q1"])
        bellman = (
            inputs.scalars["rho"] * sources["v2"].ravel(order="F")
            - p2_arrays["utility"].ravel(order="F")
            - np.asarray(q2 @ sources["v2"].ravel(order="F")).ravel()
        )
        value_change = sources["v2"] - sources["v1"]
        if not np.all(np.isfinite(bellman)):
            raise FailClosed(
                "FAIL__ADOPTED_INTERIOR_A_SWITCHING_V2_MAP_FIRST_FAILURE",
                {"stage": "bellman_nonfinite"},
            )
        bellman_inf = float(np.linalg.norm(bellman, ord=np.inf))
        value_change_inf = float(
            np.linalg.norm(value_change.ravel(order="F"), ord=np.inf)
        )
        q1_policy_sha = _canonical_sha256(
            [_selected_identity(row) for row in sources["p1_rows"]]
        )
        q1_identity = _sparse_identity(sources["q1"])
        q2_identity = _sparse_identity(q2)
        checkpoint1_identity = checkpoint_identity(
            V1_FIELD_SHA256, q1_policy_sha, q1_identity
        )
        checkpoint2_identity = checkpoint_identity(
            V2_FIELD_SHA256,
            str(policy_diagnostics["identity_sha256"]),
            q2_identity,
        )
        identities = [checkpoint1_identity, checkpoint2_identity]
        values = [sources["v0"], sources["v1"], sources["v2"]]
        exact_period = detect_exact_cycle(identities)
        approximate = detect_approximate_cycle(values, tolerance=CYCLE_TOLERANCE)
        converged = primary_converged(bellman_inf, value_change_inf)
        directory = output / "checkpoint_002"
        np.savez_compressed(
            directory / "checkpoint_arrays.npz",
            value=sources["v2"],
            utility=p2_arrays["utility"],
            mu_b=p2_arrays["g_b"],
            mu_a=p2_arrays["g_a"],
            bellman_residual=bellman,
            value_change=value_change,
        )
        cycle_receipt = {
            "checkpoint": 2,
            "primary_convergence_evaluated_first": True,
            "exact_period": exact_period,
            "exact_cycle_window_available": False,
            "approximate_period_2_or_3": approximate,
            "approximate_period_2_window_available": False,
            "approximate_period_3_window_available": False,
        }
        _write_json(directory / "cycle_detection_receipt.json", cycle_receipt)
        metrics = {
            "checkpoint": 2,
            "value_sha256": V2_FIELD_SHA256,
            "p2_identity_sha256": policy_diagnostics["identity_sha256"],
            "u2_sha256": _field_sha256(p2_arrays["utility"]),
            "q2_identity": q2_identity,
            "q2_artifact_sha256": d2_receipt["q_artifact"]["sha256"],
            "checkpoint_identity_sha256": checkpoint2_identity,
            "bellman_residual_inf": bellman_inf,
            "bellman_threshold_inclusive": BELLMAN_TOLERANCE,
            "value_change_inf": value_change_inf,
            "value_change_threshold_inclusive": VALUE_TOLERANCE,
            "primary_convergence_pass": converged,
            "policy_diagnostics": policy_diagnostics,
            "operator_diagnostics": operator_diagnostics,
            "cycle_diagnostics": cycle_receipt,
            "d2_receipt_status": d2_receipt["status"],
            "switching_statistics": switching_statistics,
            "cumulative_scientific_ledger": dict(ledger),
            "checkpoint_arrays": {
                "path": "checkpoint_arrays.npz",
                "bytes": (directory / "checkpoint_arrays.npz").stat().st_size,
                "sha256": _sha256(directory / "checkpoint_arrays.npz"),
                "bellman_residual_sha256": _field_sha256(bellman),
                "value_change_sha256": _field_sha256(value_change),
            },
        }
        terminal = (
            "PASS__ADOPTED_INTERIOR_A_SWITCHING_V2_MAP_COMPLETE__"
            "CHECKPOINT2_HJB_CONVERGENCE_"
            "CANDIDATE__TERMINAL_GATES_NOT_RUN"
            if converged
            else "PASS__ADOPTED_INTERIOR_A_SWITCHING_V2_MAP_COMPLETE__"
            "CHECKPOINT2_NONCONVERGED__NO_V3_UPDATE"
        )
        metrics["disposition"] = terminal
        _write_json(directory / "checkpoint_manifest.json", metrics)
        return _finalize(
            repository,
            output,
            pre_hashes,
            ledger,
            terminal,
            {"final_checkpoint": 2, "terminal_metrics": metrics},
            started,
        )
    except FailClosed as failure:
        terminal = failure.terminal
        if ledger["new_corrected_policy_maps"]:
            terminal = "FAIL__ADOPTED_INTERIOR_A_SWITCHING_V2_MAP_FIRST_FAILURE"
        return _finalize(
            repository,
            output,
            pre_hashes,
            ledger,
            terminal,
            failure.detail,
            started,
        )
    except Exception as exc:
        terminal = (
            "FAIL__ADOPTED_INTERIOR_A_SWITCHING_V2_MAP_FIRST_FAILURE"
            if ledger["new_corrected_policy_maps"]
            else "BLOCKED__INTERIOR_A_SWITCHING_IMPLEMENTATION_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE"
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
        args.repository,
        args.seed,
        args.binding,
        args.focused_test_junit,
    )
    print(terminal)
    return 0 if terminal.startswith("PASS__") else 2


if __name__ == "__main__":
    sys.exit(main())
