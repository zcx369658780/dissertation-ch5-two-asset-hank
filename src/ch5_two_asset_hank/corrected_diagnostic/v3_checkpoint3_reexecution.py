"""Single accepted-V3 checkpoint-3 reexecution for the bounded repair task."""

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
import xml.etree.ElementTree as ET

import numpy as np

from .checkpoint2_to_checkpoint6 import (
    _load_accepted_checkpoint2,
    _new_ledger,
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
    _sha256,
    _sparse_identity,
    _verify_manifest_files,
    checkpoint_identity,
    detect_exact_cycle,
    primary_converged,
    _write_json,
)
from .option_a_step import _input_receipt, bind_option_a_inputs
from .selector import SelectorBudget


TASK_ID = (
    "CH5_MP4C_2018_KFE_D123_V3_CELL100_LOWER_B_NEGATIVE_FORWARD_A_"
    "PRE_SCREEN_REPAIR_AND_CHECKPOINT3_REEXECUTION_20260919"
)
BASELINE_SHA = "3B3193607B72E0648C886F7FEF52CA31F04A38D4"
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_v3_cell100_lower_b_negative_forward_a_"
    "prescreen_repair_checkpoint3_reexecution_20260919_run001"
)
ACCEPTED_CONTINUATION_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_checkpoint2_to_checkpoint6_"
    "bounded_nonlinear_continuation_20260919_run001"
)
ACCEPTED_V3_SHA256 = "4FDB36C17ACDC60B56661AEE1C0437B65EC4A871FD4E5E08A9A996FB10EF85EF"
ACCEPTED_V3_ARTIFACT_SHA256 = (
    "17F330AB0A226EE826880039055B9EA16FB93DD7B02F36F820D078178C6E4CCF"
)
ACCEPTED_CONTINUATION_MANIFEST_SHA256 = (
    "9F772B9CEF73E15F0443952B25989BB6D644D73B9E04CB93B5AD047E1FBB7700"
)
MAX_SELECTOR_EVALUATIONS = 800
MAX_ROOT_INVOCATIONS = 311_256
MAX_INTERIOR_Z_ROOT_INVOCATIONS = 285_120
MAX_INTERIOR_A_ROOT_INVOCATIONS = 800
MAX_JOINT_ROOT_INVOCATIONS = 800


def _check_task_ledger(ledger: dict[str, Any]) -> None:
    ceilings = {
        "v2_policy_map_reruns": 0,
        "q2_assembly_reruns": 0,
        "new_corrected_policy_maps": 1,
        "selector_evaluations": MAX_SELECTOR_EVALUATIONS,
        "scalar_root_invocations": MAX_ROOT_INVOCATIONS,
        "interior_z_root_invocations": MAX_INTERIOR_Z_ROOT_INVOCATIONS,
        "interior_a_switching_root_invocations": MAX_INTERIOR_A_ROOT_INVOCATIONS,
        "joint_switching_root_invocations": MAX_JOINT_ROOT_INVOCATIONS,
        "d2_assemblies": 1,
        "checkpoint_evaluations": 1,
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


def _load_accepted_v3(repository: Path) -> tuple[np.ndarray, dict[str, Any]]:
    root = repository / ACCEPTED_CONTINUATION_RELATIVE
    manifest_path = root / "sealed_manifest.json"
    artifact_path = root / "checkpoint_002/direct_update_arrays.npz"
    if _sha256(manifest_path) != ACCEPTED_CONTINUATION_MANIFEST_SHA256:
        raise FailClosed(
            "BLOCKED__ACCEPTED_V3_PROVENANCE_DRIFT",
            {"stage": "accepted_continuation_manifest_hash"},
        )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    _verify_manifest_files(root, manifest)
    if _sha256(artifact_path) != ACCEPTED_V3_ARTIFACT_SHA256:
        raise FailClosed(
            "BLOCKED__ACCEPTED_V3_PROVENANCE_DRIFT",
            {"stage": "accepted_v3_artifact_hash"},
        )
    with np.load(artifact_path, allow_pickle=False) as loaded:
        value = np.array(loaded["next_value"], dtype=float, copy=True, order="F")
    if (
        value.shape != SHAPE
        or not np.all(np.isfinite(value))
        or _field_sha256(value) != ACCEPTED_V3_SHA256
    ):
        raise FailClosed(
            "BLOCKED__ACCEPTED_V3_PROVENANCE_DRIFT",
            {"stage": "accepted_v3_field"},
        )
    return value, {
        "value_sha256": _field_sha256(value),
        "artifact_sha256": _sha256(artifact_path),
        "accepted_continuation_manifest_sha256": _sha256(manifest_path),
        "accepted_continuation_manifest_entry_count": int(manifest["entry_count"]),
        "v2_to_v3_rerun": False,
    }


def _switching_statistics(directory: Path) -> dict[str, Any]:
    fields = {
        "interior_a": "interior_a_switching_receipt",
        "joint": "joint_switching_receipt",
    }
    output: dict[str, Any] = {}
    for name, field in fields.items():
        candidates = 0
        admissible = 0
        selected: list[int] = []
        statuses: Counter[str] = Counter()
        for flat in range(N):
            receipt = json.loads((directory / f"cell_{flat:04d}.json").read_text(encoding="utf-8"))
            result = receipt["selector_result"]
            rows = [row for row in result["candidates"] if row.get(field) is not None]
            candidates += len(rows)
            admissible += sum(bool(row["admissible"]) for row in rows)
            statuses.update(str(row["root_status"]) for row in rows)
            if result["selected"].get(field) is not None:
                selected.append(flat)
        output[name] = {
            "candidate_attempt_count": candidates,
            "admissible_candidate_count": admissible,
            "selected_policy_count": len(selected),
            "selected_flat_indices_f_zero_based": selected,
            "root_status_counts": dict(sorted(statuses.items())),
        }
    liquid = []
    for flat in range(N):
        receipt = json.loads((directory / f"cell_{flat:04d}.json").read_text(encoding="utf-8"))
        if receipt["selector_result"]["selected"].get("interior_z_receipt") is not None:
            liquid.append(flat)
    output["liquid_z"] = {
        "selected_policy_count": len(liquid),
        "selected_flat_indices_f_zero_based": liquid,
    }
    return output


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
            "schema": "CH5_D123_V3_CHECKPOINT3_REEXECUTION_V1",
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
    ledger["accepted_v3_loads"] = 0
    ledger["v2_to_v3_reruns"] = 0
    pre_hashes = _scientific_code_hashes(repository)
    _write_json(
        output / "startup_manifest.json",
        {
            "task_id": TASK_ID,
            "execution_head": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=repository, text=True
            ).strip(),
            "baseline_live_main": BASELINE_SHA,
            "accepted_v3_sha256": ACCEPTED_V3_SHA256,
            "scientific_code_sha256_before": pre_hashes,
            "budget": {
                "v2_to_v3_reruns": 0,
                "fresh_v3_policy_maps": 1,
                "selector_evaluations": MAX_SELECTOR_EVALUATIONS,
                "q3_assemblies": 1,
                "checkpoint3_evaluations": 1,
                "direct_hjb_solves": 0,
                "terminal_topology_kfe": 0,
                "scientific_retries": 0,
            },
        },
    )
    try:
        checks = {
            "worktree_clean_before_evidence": clean_before_evidence,
            "origin_main_exact_baseline": subprocess.check_output(
                ["git", "rev-parse", "origin/main"], cwd=repository, text=True
            ).strip().upper()
            == BASELINE_SHA,
        }
        if not all(checks.values()):
            raise FailClosed(
                "BLOCKED__ENGINEERING_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE",
                {"stage": "git_binding", "checks": checks},
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
        v3, v3_binding = _load_accepted_v3(repository)
        ledger["accepted_v3_loads"] = 1
        _write_json(
            output / "accepted_v3_binding.json",
            {
                "status": "PASS",
                "input_identity": _input_receipt(inputs),
                "accepted_checkpoint2_identities": accepted["identities"],
                **v3_binding,
            },
        )
        budget = SelectorBudget(
            max_selector_evaluations=MAX_SELECTOR_EVALUATIONS,
            max_root_invocations=MAX_ROOT_INVOCATIONS,
            max_interior_z_root_invocations=MAX_INTERIOR_Z_ROOT_INVOCATIONS,
            max_interior_a_switching_root_invocations=MAX_INTERIOR_A_ROOT_INVOCATIONS,
            max_joint_switching_root_invocations=MAX_JOINT_ROOT_INVOCATIONS,
        )
        rows, arrays, q3, d2_receipt = _map_checkpoint(
            repository, output, 3, v3, inputs, budget, ledger, pre_hashes
        )
        _check_task_ledger(ledger)
        ledger["checkpoint_evaluations"] += 1
        _check_task_ledger(ledger)
        directory = output / "checkpoint_003"
        policy = _policy_diagnostics(
            rows, accepted["p2_rows"], arrays, accepted["p2_arrays"]
        )
        operator = _operator_diagnostics(q3, accepted["q2"])
        switching = _switching_statistics(directory)
        _write_json(directory / "switching_statistics.json", switching)
        bellman = (
            float(inputs.scalars["rho"]) * v3.ravel(order="F")
            - arrays["utility"].ravel(order="F")
            - np.asarray(q3 @ v3.ravel(order="F")).ravel()
        )
        value_change = v3 - accepted["v2"]
        if not np.all(np.isfinite(bellman)) or not np.all(np.isfinite(value_change)):
            raise FailClosed(
                "FAIL__NONFINITE_OR_PROVENANCE_GATE",
                {"checkpoint": 3, "stage": "checkpoint_metric_nonfinite"},
            )
        bellman_inf = float(np.linalg.norm(bellman, ord=np.inf))
        value_change_inf = float(np.linalg.norm(value_change.ravel(order="F"), ord=np.inf))
        q_identity = _sparse_identity(q3)
        identity = checkpoint_identity(ACCEPTED_V3_SHA256, policy["identity_sha256"], q_identity)
        converged = primary_converged(bellman_inf, value_change_inf)
        exact_period = None
        if not converged:
            exact_period = detect_exact_cycle(
                [accepted["checkpoint1_identity"], accepted["checkpoint2_identity"], identity]
            )
        cycle = {
            "checkpoint": 3,
            "primary_convergence_evaluated_first": True,
            "primary_convergence_pass": converged,
            "exact_evaluated_only_after_primary_failure": not converged,
            "exact_period": exact_period,
            "approximate_period_2_window_available": False,
            "approximate_period_3_window_available": False,
            "approximate_cycle_evaluated": False,
            "approximate_cycle_tolerance": CYCLE_TOLERANCE,
        }
        _write_json(directory / "cycle_detection_receipt.json", cycle)
        np.savez_compressed(
            directory / "checkpoint_arrays.npz",
            value=v3,
            utility=arrays["utility"],
            mu_b=arrays["g_b"],
            mu_a=arrays["g_a"],
            bellman_residual=bellman,
            value_change=value_change,
        )
        if converged:
            terminal = "HJB_CONVERGENCE_CANDIDATE__TERMINAL_GATE_NOT_RUN"
        elif exact_period is not None:
            terminal = "EXACT_CYCLE"
        else:
            terminal = "COMPLETE_CHECKPOINT3_NONCONVERGED__STOP_BEFORE_V3_TO_V4"
        metrics = {
            "checkpoint": 3,
            "value_sha256": ACCEPTED_V3_SHA256,
            "policy_identity_sha256": policy["identity_sha256"],
            "utility_sha256": _field_sha256(arrays["utility"]),
            "q_artifact_sha256": d2_receipt["q_artifact"]["sha256"],
            "q_identity": q_identity,
            "checkpoint_identity_sha256": identity,
            "bellman_residual_inf": bellman_inf,
            "bellman_threshold_inclusive": BELLMAN_TOLERANCE,
            "value_change_inf": value_change_inf,
            "value_change_threshold_inclusive": VALUE_TOLERANCE,
            "primary_convergence_pass": converged,
            "policy_diagnostics": policy,
            "operator_diagnostics": operator,
            "switching_statistics": switching,
            "cycle_diagnostics": cycle,
            "d2_receipt_status": d2_receipt["status"],
            "disposition": terminal,
            "v3_to_v4_hjb_update_run": False,
            "checkpoint_arrays": {
                "path": "checkpoint_arrays.npz",
                "bytes": (directory / "checkpoint_arrays.npz").stat().st_size,
                "sha256": _sha256(directory / "checkpoint_arrays.npz"),
            },
        }
        _write_json(directory / "checkpoint_manifest.json", metrics)
        _seal_directory(directory, "CH5_D123_V3_CHECKPOINT3_REEXECUTION_CHECKPOINT_V1")
        return _finalize(
            repository,
            output,
            pre_hashes,
            ledger,
            terminal,
            {"final_checkpoint": 3, "terminal_metrics": metrics},
            started,
        )
    except FailClosed as failure:
        return _finalize(
            repository, output, pre_hashes, ledger, failure.terminal, failure.detail, started
        )
    except Exception as exc:
        terminal = (
            "FAIL__SCIENTIFIC_GATE_AFTER_ENTRY"
            if ledger["new_corrected_policy_maps"]
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
    return 0 if terminal.startswith(("COMPLETE_", "HJB_CONVERGENCE_")) else 2


if __name__ == "__main__":
    sys.exit(main())
