"""Bounded continuation from exact accepted checkpoint 3 through checkpoint 6."""

from __future__ import annotations

import argparse
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

from .checkpoint2_to_checkpoint6 import (
    _load_accepted_checkpoint2,
    _new_ledger as _base_ledger,
    _solve_update,
    _switching_statistics,
    classify_checkpoint,
    detect_authorized_approximate_cycle,
)
from .nonlinear_continuation import (
    BELLMAN_TOLERANCE,
    CYCLE_TOLERANCE,
    N,
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
    _seal_directory,
    _selected_identity,
    _sha256,
    _sparse_identity,
    _verify_manifest_files,
    _write_json,
    checkpoint_identity,
    detect_exact_cycle,
    primary_converged,
)
from .option_a_step import _input_receipt, bind_option_a_inputs
from .selector import SelectorBudget


TASK_ID = (
    "CH5_MP4C_2018_KFE_D123_CHECKPOINT3_TO_CHECKPOINT6_"
    "BOUNDED_NONLINEAR_CONTINUATION_20260919"
)
BASELINE_SHA = "28E74C0CFAFD6826EA7F5600897D58608C58F44A"
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_checkpoint3_to_checkpoint6_"
    "bounded_nonlinear_continuation_20260919_run001"
)
ACCEPTED_ROOT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_v3_cell100_lower_b_negative_forward_a_"
    "prescreen_repair_checkpoint3_reexecution_20260919_run001"
)

ACCEPTED_V3_SHA256 = "4FDB36C17ACDC60B56661AEE1C0437B65EC4A871FD4E5E08A9A996FB10EF85EF"
ACCEPTED_P3_IDENTITY = "06062946687922E1FAC83E8D4B1B19101469CC284339522595A19F4DECB6B07B"
ACCEPTED_U3_SHA256 = "9BB321A63A92154D4B733B28126AF29DC1441B95D44517D884F4C858AECFE6F4"
ACCEPTED_Q3_ARTIFACT_SHA256 = (
    "4085E0D1B166E72650CA1E74E5CF9462F6677EEAFA8CDEF1FBD153F14088C255"
)
ACCEPTED_Q3_IDENTITY = {
    "data": "13CA224BF05EADD453078A6A6A54A87EADC0C76C4753A0577703298C1767A521",
    "indices": "AFB69E0EF55C1E8CEBAF4040485297B8CAE211F85451AC4B89E9B27CED97FBD0",
    "indptr": "BC95DE3B2915B44B63AEC514B67F12005964891E1E78AAB43C6FD38370ABA495",
}
ACCEPTED_CHECKPOINT3_IDENTITY = (
    "0DEEF7E54C4972BFF7BB67AE6B67BA5E54B588F3EEF5ACDE85048F3E02FE715D"
)
ACCEPTED_CHECKPOINT3_ARRAYS_SHA256 = (
    "B4024EC1202533982BAF9C893F946D20B871B76B3BD369DD4F19B34BF1DD99BD"
)
ACCEPTED_SEALED_MANIFEST_SHA256 = (
    "01FB50C300936B76F7C56CBD0BBFDF8A91ABFDDF5180FE5AB77FA7341DD8D1F6"
)
ACCEPTED_B3 = 0.1291770476282596
ACCEPTED_D3 = 0.05315900863346279

MAX_NEW_UPDATES = 3
MAX_NEW_POLICY_MAPS = 3
MAX_SELECTOR_EVALUATIONS = 2400
MAX_ROOT_INVOCATIONS = 933_768
MAX_INTERIOR_Z_ROOT_INVOCATIONS = 855_360
MAX_INTERIOR_A_ROOT_INVOCATIONS = 2400
MAX_JOINT_ROOT_INVOCATIONS = 2400


def _new_ledger() -> dict[str, Any]:
    ledger = _base_ledger()
    ledger.update(
        accepted_v3_loads=0,
        accepted_p3_loads=0,
        accepted_u3_loads=0,
        accepted_q3_loads=0,
        accepted_checkpoint3_manifest_loads=0,
        v3_policy_map_reruns=0,
        q3_assembly_reruns=0,
    )
    return ledger


def _check_task_ledger(ledger: dict[str, Any]) -> None:
    ceilings = {
        "v2_policy_map_reruns": 0,
        "q2_assembly_reruns": 0,
        "v3_policy_map_reruns": 0,
        "q3_assembly_reruns": 0,
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


def _load_accepted_checkpoint3(repository: Path) -> dict[str, Any]:
    root = repository / ACCEPTED_ROOT_RELATIVE
    manifest_path = root / "sealed_manifest.json"
    checkpoint_root = root / "checkpoint_003"
    arrays_path = checkpoint_root / "checkpoint_arrays.npz"
    q3_path = checkpoint_root / "q_generator.npz"
    checkpoint_manifest_path = checkpoint_root / "checkpoint_manifest.json"
    if _sha256(manifest_path) != ACCEPTED_SEALED_MANIFEST_SHA256:
        raise FailClosed(
            "BLOCKED__ACCEPTED_CHECKPOINT3_PROVENANCE_DRIFT",
            {"stage": "accepted_sealed_manifest_hash"},
        )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    _verify_manifest_files(root, manifest)
    if _sha256(arrays_path) != ACCEPTED_CHECKPOINT3_ARRAYS_SHA256:
        raise FailClosed(
            "BLOCKED__ACCEPTED_CHECKPOINT3_PROVENANCE_DRIFT",
            {"stage": "accepted_checkpoint3_arrays_hash"},
        )
    if _sha256(q3_path) != ACCEPTED_Q3_ARTIFACT_SHA256:
        raise FailClosed(
            "BLOCKED__ACCEPTED_CHECKPOINT3_PROVENANCE_DRIFT",
            {"stage": "accepted_q3_artifact_hash"},
        )
    rows: list[dict[str, Any]] = []
    for flat in range(N):
        receipt = json.loads(
            (checkpoint_root / f"cell_{flat:04d}.json").read_text(encoding="utf-8")
        )
        result = receipt.get("selector_result", {})
        if (
            int(receipt.get("flat_index_f_zero_based", -1)) != flat
            or result.get("outcome") != "SELECTED_ADMISSIBLE"
            or not isinstance(result.get("selected"), dict)
        ):
            raise FailClosed(
                "BLOCKED__ACCEPTED_CHECKPOINT3_PROVENANCE_DRIFT",
                {"stage": "accepted_p3_receipt", "flat": flat},
            )
        rows.append(result["selected"])
    policy_arrays = _policy_arrays(rows)
    policy_identity = _canonical_sha256([_selected_identity(row) for row in rows])
    with np.load(arrays_path, allow_pickle=False) as loaded:
        value = np.array(loaded["value"], dtype=float, copy=True, order="F")
        utility = np.array(loaded["utility"], dtype=float, copy=True, order="F")
        mu_b = np.array(loaded["mu_b"], dtype=float, copy=True, order="F")
        mu_a = np.array(loaded["mu_a"], dtype=float, copy=True, order="F")
    q3 = sparse.csr_matrix(sparse.load_npz(q3_path))
    checkpoint_manifest = json.loads(checkpoint_manifest_path.read_text(encoding="utf-8"))
    checks = {
        "v3_shape": value.shape == SHAPE,
        "v3_finite": bool(np.all(np.isfinite(value))),
        "v3_exact": _field_sha256(value) == ACCEPTED_V3_SHA256,
        "p3_exact": policy_identity == ACCEPTED_P3_IDENTITY,
        "u3_exact": _field_sha256(utility) == ACCEPTED_U3_SHA256,
        "utility_rows_equal": np.array_equal(policy_arrays["utility"], utility),
        "mu_b_rows_equal": np.array_equal(policy_arrays["g_b"], mu_b),
        "mu_a_rows_equal": np.array_equal(policy_arrays["g_a"], mu_a),
        "q3_shape": q3.shape == (N, N),
        "q3_identity_exact": _sparse_identity(q3) == ACCEPTED_Q3_IDENTITY,
        "checkpoint3_identity_exact": checkpoint_identity(
            ACCEPTED_V3_SHA256, policy_identity, _sparse_identity(q3)
        )
        == ACCEPTED_CHECKPOINT3_IDENTITY,
        "checkpoint3_b_exact": float(checkpoint_manifest["bellman_residual_inf"])
        == ACCEPTED_B3,
        "checkpoint3_d_exact": float(checkpoint_manifest["value_change_inf"])
        == ACCEPTED_D3,
        "checkpoint3_nonconverged": checkpoint_manifest["primary_convergence_pass"]
        is False,
    }
    if not all(checks.values()):
        raise FailClosed(
            "BLOCKED__ACCEPTED_CHECKPOINT3_PROVENANCE_DRIFT",
            {"stage": "accepted_checkpoint3_binding", "checks": checks},
        )
    return {
        "v3": value,
        "p3_rows": rows,
        "p3_arrays": policy_arrays,
        "q3": q3,
        "checks": checks,
        "manifest_entry_count": int(manifest["entry_count"]),
        "v3_policy_map_rerun": False,
        "q3_assembly_rerun": False,
        "identities": {
            "v3": ACCEPTED_V3_SHA256,
            "p3": ACCEPTED_P3_IDENTITY,
            "u3": ACCEPTED_U3_SHA256,
            "q3": ACCEPTED_Q3_ARTIFACT_SHA256,
            "q3_components": ACCEPTED_Q3_IDENTITY,
            "checkpoint3": ACCEPTED_CHECKPOINT3_IDENTITY,
            "checkpoint3_arrays": ACCEPTED_CHECKPOINT3_ARRAYS_SHA256,
            "sealed_manifest": ACCEPTED_SEALED_MANIFEST_SHA256,
        },
    }


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
            "schema": "CH5_D123_CHECKPOINT3_TO_CHECKPOINT6_CONTINUATION_V1",
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
            "execution_head": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=repository, text=True
            ).strip(),
            "baseline_live_main": BASELINE_SHA,
            "accepted_checkpoint3_identity": ACCEPTED_CHECKPOINT3_IDENTITY,
            "accepted_checkpoint3_reused_without_policy_map_or_q3_assembly": True,
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
        preflight = {
            "worktree_clean_before_evidence": clean_before_evidence,
            "origin_main_exact_baseline": subprocess.check_output(
                ["git", "rev-parse", "origin/main"], cwd=repository, text=True
            ).strip().upper()
            == BASELINE_SHA,
        }
        if not all(preflight.values()):
            raise FailClosed(
                "BLOCKED__ENGINEERING_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE",
                {"stage": "git_binding", "checks": preflight},
            )
        focused = _read_focused_tests(focused_test_junit.resolve(strict=True))
        shutil.copyfile(focused_test_junit, output / "focused_tests.xml")
        focused["copied_sha256"] = _sha256(output / "focused_tests.xml")
        _write_json(output / "focused_test_receipt.json", focused)
        inputs = bind_option_a_inputs(seed_path, binding_path)
        prior = _load_accepted_checkpoint2(repository, inputs)
        accepted = _load_accepted_checkpoint3(repository)
        ledger.update(
            accepted_v0_loads=1,
            accepted_v1_loads=1,
            accepted_q1_loads=1,
            accepted_v2_loads=1,
            accepted_p2_loads=1,
            accepted_u2_loads=1,
            accepted_q2_loads=1,
            accepted_checkpoint2_manifest_loads=1,
            accepted_v3_loads=1,
            accepted_p3_loads=1,
            accepted_u3_loads=1,
            accepted_q3_loads=1,
            accepted_checkpoint3_manifest_loads=1,
        )
        _write_json(
            output / "accepted_checkpoint3_binding.json",
            {
                "status": "PASS",
                "input_identity": _input_receipt(inputs),
                "accepted_checkpoint2_identities": prior["identities"],
                "accepted_checkpoint3_identities": accepted["identities"],
                "accepted_checkpoint3_checks": accepted["checks"],
                "accepted_manifest_entry_count": accepted["manifest_entry_count"],
                "v3_policy_map_rerun": False,
                "q3_assembly_rerun": False,
            },
        )
        values = [prior["v0"], prior["v1"], prior["v2"], accepted["v3"]]
        identities = [
            prior["checkpoint1_identity"],
            prior["checkpoint2_identity"],
            ACCEPTED_CHECKPOINT3_IDENTITY,
        ]
        previous_rows = accepted["p3_rows"]
        previous_arrays = accepted["p3_arrays"]
        previous_q = accepted["q3"]
        checkpoint3_dir = output / "checkpoint_003"
        checkpoint3_dir.mkdir(parents=False, exist_ok=False)
        _write_json(
            checkpoint3_dir / "accepted_source_receipt.json",
            {
                "checkpoint": 3,
                "accepted_checkpoint_identity": ACCEPTED_CHECKPOINT3_IDENTITY,
                "accepted_bellman_residual_inf": ACCEPTED_B3,
                "accepted_value_change_inf": ACCEPTED_D3,
                "v3_policy_map_rerun": False,
                "q3_assembly_rerun": False,
            },
        )
        current_value = _solve_update(
            checkpoint3_dir,
            3,
            accepted["v3"],
            accepted["p3_arrays"]["utility"],
            accepted["q3"],
            float(inputs.scalars["rho"]),
            ledger,
        )
        _check_task_ledger(ledger)
        _seal_directory(checkpoint3_dir, "CH5_D123_ACCEPTED_CHECKPOINT3_UPDATE_TO_4_V1")
        values.append(current_value)
        budget = SelectorBudget(
            max_selector_evaluations=MAX_SELECTOR_EVALUATIONS,
            max_root_invocations=MAX_ROOT_INVOCATIONS,
            max_interior_z_root_invocations=MAX_INTERIOR_Z_ROOT_INVOCATIONS,
            max_interior_a_switching_root_invocations=MAX_INTERIOR_A_ROOT_INVOCATIONS,
            max_joint_switching_root_invocations=MAX_JOINT_ROOT_INVOCATIONS,
        )
        final_metrics: dict[str, Any] = {}
        for checkpoint in range(4, 7):
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
            _check_task_ledger(ledger)
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
                "approximate_tolerance": CYCLE_TOLERANCE,
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
            _check_task_ledger(ledger)
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
            repository, output, pre_hashes, ledger, failure.terminal, failure.detail, started
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
    terminal = execute(args.repository, args.seed, args.binding, args.focused_test_junit)
    print(terminal)
    successful = {
        "HJB_CONVERGENCE_CANDIDATE__TERMINAL_GATE_NOT_RUN",
        "COMPLETE_CHECKPOINT6_NONCONVERGED__TERMINAL_GATE_NOT_RUN",
    }
    return 0 if terminal in successful else 2


if __name__ == "__main__":
    sys.exit(main())
