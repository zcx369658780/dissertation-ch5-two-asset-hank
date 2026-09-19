"""Resume bounded checkpoint-3 continuation from the sealed checkpoint-4 prefix.

The first process completed the V3->V4 solve, V4 policy map, and Q4 assembly,
then stopped in a representation-only approximate-cycle diagnostic.  This
module verifies and loads that immutable prefix; it never recomputes it.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time
from typing import Any

import numpy as np
from scipy import sparse

from .checkpoint2_to_checkpoint6 import (
    _load_accepted_checkpoint2,
    _solve_update,
    _switching_statistics,
    classify_checkpoint,
    detect_authorized_approximate_cycle,
)
from .checkpoint3_to_checkpoint6 import (
    ACCEPTED_B3,
    ACCEPTED_CHECKPOINT3_IDENTITY,
    ACCEPTED_D3,
    ACCEPTED_V3_SHA256,
    BASELINE_SHA,
    MAX_INTERIOR_A_ROOT_INVOCATIONS,
    MAX_INTERIOR_Z_ROOT_INVOCATIONS,
    MAX_JOINT_ROOT_INVOCATIONS,
    MAX_NEW_POLICY_MAPS,
    MAX_NEW_UPDATES,
    MAX_ROOT_INVOCATIONS,
    MAX_SELECTOR_EVALUATIONS,
    TASK_ID,
    _check_task_ledger,
    _load_accepted_checkpoint3,
    _read_focused_tests,
    _write_root_manifest,
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


PREFIX_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_checkpoint3_to_checkpoint6_"
    "bounded_nonlinear_continuation_20260919_run001"
)
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_checkpoint3_to_checkpoint6_"
    "bounded_nonlinear_continuation_20260919_resume001"
)
ACCEPTED_PREFIX_MANIFEST_SHA256 = (
    "7BE53C6075C3B34680100921E65A3F98BEEE15C348681B2A241A2E6557C95030"
)
ACCEPTED_V4_SHA256 = "938682CEA35E4ED77F02087AB6BDE9204A0B4C00B9E898E3200799D1367C149B"
ACCEPTED_V4_ARTIFACT_SHA256 = (
    "FBDFEDD274B5325282848E8A52E5595361173E7ACEEA65CB11A27DCAC689E7DE"
)
ACCEPTED_Q4_ARTIFACT_SHA256 = (
    "94432703101724F6F76317A00F9DDCA7583065AB7094416BDC03E85DDEB9AE91"
)
ACCEPTED_Q4_IDENTITY = {
    "data": "0045B749D8A2B45A62F39199CD6585859768D7F81D61B5AF451CF85A41A69048",
    "indices": "73252567816C2D2A31FFEC2A4BB0CF7DC4B01B2B4CCD0A67FAFEA2F6C5FA58E5",
    "indptr": "FF3AD7DF179363B15AC8792BC6B9A2AF6F132FA0BCC02FC91487C828BA41D4CF",
}


def _load_resume_prefix(repository: Path) -> dict[str, Any]:
    root = repository.resolve(strict=True) / PREFIX_RELATIVE
    manifest_path = root / "sealed_manifest.json"
    if _sha256(manifest_path) != ACCEPTED_PREFIX_MANIFEST_SHA256:
        raise FailClosed(
            "BLOCKED__SEALED_RESUME_PREFIX_PROVENANCE_DRIFT",
            {"stage": "prefix_manifest_hash"},
        )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    _verify_manifest_files(root, manifest)
    if int(manifest.get("entry_count", -1)) != 815:
        raise FailClosed(
            "BLOCKED__SEALED_RESUME_PREFIX_PROVENANCE_DRIFT",
            {"stage": "prefix_manifest_entry_count"},
        )
    terminal = json.loads((root / "terminal_receipt.json").read_text(encoding="utf-8"))
    expected_detail = {
        "stage": "unhandled_exception",
        "type": "ValueError",
        "message": "Improper number of dimensions to norm.",
    }
    pre = json.loads((root / "startup_manifest.json").read_text(encoding="utf-8"))
    post = json.loads(
        (root / "post_execution_code_freeze.json").read_text(encoding="utf-8")
    )
    if (
        terminal.get("terminal_classification") != "FAIL__SCIENTIFIC_GATE_AFTER_ENTRY"
        or terminal.get("detail") != expected_detail
        or post.get("matches_pre_execution_freeze") is not True
        or post.get("scientific_code_sha256_after")
        != pre.get("scientific_code_sha256_before")
    ):
        raise FailClosed(
            "BLOCKED__SEALED_RESUME_PREFIX_PROVENANCE_DRIFT",
            {"stage": "prefix_terminal_or_code_freeze"},
        )
    update_path = root / "checkpoint_003" / "direct_update_arrays.npz"
    q_path = root / "checkpoint_004" / "q_generator.npz"
    if (
        _sha256(update_path) != ACCEPTED_V4_ARTIFACT_SHA256
        or _sha256(q_path) != ACCEPTED_Q4_ARTIFACT_SHA256
    ):
        raise FailClosed(
            "BLOCKED__SEALED_RESUME_PREFIX_PROVENANCE_DRIFT",
            {"stage": "prefix_v4_or_q4_artifact"},
        )
    with np.load(update_path, allow_pickle=False) as loaded:
        v4 = np.array(loaded["next_value"], dtype=float, copy=True, order="F")
    rows: list[dict[str, Any]] = []
    checkpoint_root = root / "checkpoint_004"
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
                "BLOCKED__SEALED_RESUME_PREFIX_PROVENANCE_DRIFT",
                {"stage": "prefix_p4_receipt", "flat": flat},
            )
        rows.append(result["selected"])
    arrays = _policy_arrays(rows)
    q4 = sparse.csr_matrix(sparse.load_npz(q_path))
    d2 = json.loads((checkpoint_root / "d2_receipt.json").read_text(encoding="utf-8"))
    ledger = json.loads((root / "scientific_ledger.json").read_text(encoding="utf-8"))
    checks = {
        "v4_shape": v4.shape == SHAPE,
        "v4_finite": bool(np.all(np.isfinite(v4))),
        "v4_exact": _field_sha256(v4) == ACCEPTED_V4_SHA256,
        "q4_shape": q4.shape == (N, N),
        "q4_identity_exact": _sparse_identity(q4) == ACCEPTED_Q4_IDENTITY,
        "d2_pass": d2.get("status") == "PASS",
        "d2_q_identity_exact": d2.get("q_identity") == ACCEPTED_Q4_IDENTITY,
        "ledger_update_exact": int(ledger.get("direct_hjb_solves", -1)) == 1,
        "ledger_map_exact": int(ledger.get("new_corrected_policy_maps", -1)) == 1,
        "ledger_selector_exact": int(ledger.get("selector_evaluations", -1)) == 800,
        "ledger_d2_exact": int(ledger.get("d2_assemblies", -1)) == 1,
        "ledger_checkpoint_evaluation_exact": int(ledger.get("checkpoint_evaluations", -1)) == 1,
        "ledger_retry_zero": int(ledger.get("scientific_retries", -1)) == 0,
    }
    if not all(checks.values()):
        raise FailClosed(
            "BLOCKED__SEALED_RESUME_PREFIX_PROVENANCE_DRIFT",
            {"stage": "prefix_scientific_binding", "checks": checks},
        )
    ledger.pop("terminal_classification", None)
    prefix_wall_seconds = float(ledger.pop("wall_seconds"))
    return {
        "root": root,
        "manifest_sha256": ACCEPTED_PREFIX_MANIFEST_SHA256,
        "manifest_entry_count": 815,
        "terminal_classification": terminal["terminal_classification"],
        "terminal_message": terminal["detail"]["message"],
        "checks": checks,
        "v4": v4,
        "p4_rows": rows,
        "p4_arrays": arrays,
        "p4_identity": _canonical_sha256([_selected_identity(row) for row in rows]),
        "q4": q4,
        "d2_receipt": d2,
        "ledger": ledger,
        "prefix_wall_seconds": prefix_wall_seconds,
        "v4_policy_map_rerun": False,
        "q4_assembly_rerun": False,
    }


def _finalize_resume(
    repository: Path,
    output: Path,
    pre_hashes: dict[str, str],
    ledger: dict[str, Any],
    terminal: str,
    detail: dict[str, Any],
    started: float,
    prefix_wall_seconds: float,
) -> str:
    _check_task_ledger(ledger)
    post_hashes = _scientific_code_hashes(repository)
    if post_hashes != pre_hashes:
        terminal = "BLOCKED__SCIENTIFIC_CODE_CHANGED_AFTER_FREEZE"
        detail = {"stage": "post_execution_code_hash", "prior_detail": detail}
    ledger["terminal_classification"] = terminal
    ledger["prefix_wall_seconds"] = prefix_wall_seconds
    ledger["resume_wall_seconds"] = float(time.perf_counter() - started)
    ledger["wall_seconds"] = prefix_wall_seconds + ledger["resume_wall_seconds"]
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


def _checkpoint_metrics(
    *,
    checkpoint: int,
    directory: Path,
    current_value: np.ndarray,
    previous_value: np.ndarray,
    rows: list[dict[str, Any]],
    arrays: dict[str, np.ndarray],
    q: sparse.csr_matrix,
    previous_rows: list[dict[str, Any]],
    previous_arrays: dict[str, np.ndarray],
    previous_q: sparse.csr_matrix,
    values: list[np.ndarray],
    identities: list[str],
    rho: float,
    d2_receipt: dict[str, Any],
    ledger: dict[str, Any],
    switching_source: Path,
) -> tuple[dict[str, Any], str | None]:
    policy = _policy_diagnostics(rows, previous_rows, arrays, previous_arrays)
    operator = _operator_diagnostics(q, previous_q)
    switching = _switching_statistics(switching_source)
    _write_json(directory / "switching_statistics.json", switching)
    bellman = (
        rho * current_value.ravel(order="F")
        - arrays["utility"].ravel(order="F")
        - np.asarray(q @ current_value.ravel(order="F")).ravel()
    )
    value_change = current_value - previous_value
    if not np.all(np.isfinite(bellman)) or not np.all(np.isfinite(value_change)):
        raise FailClosed(
            "FAIL__NONFINITE_OR_PROVENANCE_GATE",
            {"checkpoint": checkpoint, "stage": "checkpoint_metric_nonfinite"},
        )
    bellman_inf = float(np.linalg.norm(bellman, ord=np.inf))
    value_change_inf = float(np.linalg.norm(value_change.ravel(order="F"), ord=np.inf))
    q_identity = _sparse_identity(q)
    identity = checkpoint_identity(
        _field_sha256(current_value), str(policy["identity_sha256"]), q_identity
    )
    identities.append(identity)
    converged = primary_converged(bellman_inf, value_change_inf)
    exact_period = None
    approximate = None
    if not converged:
        exact_period = detect_exact_cycle(identities)
        if exact_period is None:
            approximate = detect_authorized_approximate_cycle(values, checkpoint=checkpoint)
    cycle = {
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
    _write_json(directory / "cycle_detection_receipt.json", cycle)
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
        "cumulative_scientific_ledger": dict(ledger),
        "checkpoint_arrays": {
            "path": "checkpoint_arrays.npz",
            "bytes": (directory / "checkpoint_arrays.npz").stat().st_size,
            "sha256": _sha256(directory / "checkpoint_arrays.npz"),
            "bellman_residual_sha256": _field_sha256(bellman),
            "value_change_sha256": _field_sha256(value_change),
        },
    }
    terminal = classify_checkpoint(
        checkpoint=checkpoint,
        bellman_residual=bellman_inf,
        value_change=value_change_inf,
        exact_period=exact_period,
        approximate_cycle=approximate,
    )
    return metrics, terminal


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
    pre_hashes = _scientific_code_hashes(repository)
    ledger: dict[str, Any] = {}
    prefix_wall_seconds = 0.0
    _write_json(
        output / "startup_manifest.json",
        {
            "task_id": TASK_ID,
            "execution_head": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=repository, text=True
            ).strip(),
            "baseline_live_main": BASELINE_SHA,
            "resume_prefix_manifest_sha256": ACCEPTED_PREFIX_MANIFEST_SHA256,
            "v3_to_v4_v4_map_q4_reused_without_reexecution": True,
            "scientific_code_sha256_before": pre_hashes,
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
        prefix = _load_resume_prefix(repository)
        ledger = dict(prefix["ledger"])
        prefix_wall_seconds = float(prefix["prefix_wall_seconds"])
        _check_task_ledger(ledger)
        _write_json(
            output / "resume_prefix_binding.json",
            {
                "status": "PASS",
                "input_identity": _input_receipt(inputs),
                "accepted_checkpoint3_identity": ACCEPTED_CHECKPOINT3_IDENTITY,
                "prefix_manifest_sha256": prefix["manifest_sha256"],
                "prefix_manifest_entry_count": prefix["manifest_entry_count"],
                "prefix_checks": prefix["checks"],
                "v3_to_v4_update_rerun": False,
                "v4_policy_map_rerun": False,
                "q4_assembly_rerun": False,
            },
        )
        values = [prior["v0"], prior["v1"], prior["v2"], accepted["v3"], prefix["v4"]]
        identities = [
            prior["checkpoint1_identity"],
            prior["checkpoint2_identity"],
            ACCEPTED_CHECKPOINT3_IDENTITY,
        ]
        directory = output / "checkpoint_004"
        directory.mkdir(parents=False, exist_ok=False)
        _write_json(
            directory / "accepted_prefix_receipt.json",
            {
                "checkpoint": 4,
                "v4_sha256": ACCEPTED_V4_SHA256,
                "prefix_manifest_sha256": ACCEPTED_PREFIX_MANIFEST_SHA256,
                "v3_to_v4_update_rerun": False,
                "v4_policy_map_rerun": False,
                "q4_assembly_rerun": False,
                "checkpoint_evaluation_counted_in_prefix": True,
            },
        )
        metrics, terminal = _checkpoint_metrics(
            checkpoint=4,
            directory=directory,
            current_value=prefix["v4"],
            previous_value=accepted["v3"],
            rows=prefix["p4_rows"],
            arrays=prefix["p4_arrays"],
            q=prefix["q4"],
            previous_rows=accepted["p3_rows"],
            previous_arrays=accepted["p3_arrays"],
            previous_q=accepted["q3"],
            values=values,
            identities=identities,
            rho=float(inputs.scalars["rho"]),
            d2_receipt=prefix["d2_receipt"],
            ledger=ledger,
            switching_source=prefix["root"] / "checkpoint_004",
        )
        if terminal is not None:
            metrics["disposition"] = terminal
            _write_json(directory / "checkpoint_manifest.json", metrics)
            _seal_directory(directory, "CH5_D123_RESUMED_CHECKPOINT4_V1")
            return _finalize_resume(
                repository, output, pre_hashes, ledger, terminal,
                {"final_checkpoint": 4, "terminal_metrics": metrics},
                started, prefix_wall_seconds,
            )
        next_value = _solve_update(
            directory, 4, prefix["v4"], prefix["p4_arrays"]["utility"],
            prefix["q4"], float(inputs.scalars["rho"]), ledger,
        )
        _check_task_ledger(ledger)
        metrics["disposition"] = "CONTINUE_TO_NEXT_CHECKPOINT"
        metrics["direct_solve"] = json.loads(
            (directory / "direct_solve_receipt.json").read_text(encoding="utf-8")
        )
        _write_json(directory / "checkpoint_manifest.json", metrics)
        _seal_directory(directory, "CH5_D123_RESUMED_CHECKPOINT4_V1")
        if _scientific_code_hashes(repository) != pre_hashes:
            raise FailClosed(
                "BLOCKED__SCIENTIFIC_CODE_CHANGED_AFTER_FREEZE",
                {"checkpoint": 4, "stage": "post_update_code_hash"},
            )
        previous_rows = prefix["p4_rows"]
        previous_arrays = prefix["p4_arrays"]
        previous_q = prefix["q4"]
        current_value = next_value
        values.append(current_value)
        budget = SelectorBudget(
            max_selector_evaluations=MAX_SELECTOR_EVALUATIONS,
            max_root_invocations=MAX_ROOT_INVOCATIONS,
            max_interior_z_root_invocations=MAX_INTERIOR_Z_ROOT_INVOCATIONS,
            max_interior_a_switching_root_invocations=MAX_INTERIOR_A_ROOT_INVOCATIONS,
            max_joint_switching_root_invocations=MAX_JOINT_ROOT_INVOCATIONS,
            selector_evaluations=int(ledger["selector_evaluations"]),
            root_invocations=int(ledger["scalar_root_invocations"]),
            interior_z_root_invocations=int(ledger["interior_z_root_invocations"]),
            interior_a_switching_root_invocations=int(
                ledger["interior_a_switching_root_invocations"]
            ),
            joint_switching_root_invocations=int(
                ledger["joint_switching_root_invocations"]
            ),
        )
        for checkpoint in range(5, 7):
            rows, arrays, q, d2_receipt = _map_checkpoint(
                repository, output, checkpoint, current_value, inputs, budget,
                ledger, pre_hashes,
            )
            _check_task_ledger(ledger)
            ledger["checkpoint_evaluations"] += 1
            _check_task_ledger(ledger)
            directory = output / f"checkpoint_{checkpoint:03d}"
            metrics, terminal = _checkpoint_metrics(
                checkpoint=checkpoint,
                directory=directory,
                current_value=current_value,
                previous_value=values[-2],
                rows=rows,
                arrays=arrays,
                q=q,
                previous_rows=previous_rows,
                previous_arrays=previous_arrays,
                previous_q=previous_q,
                values=values,
                identities=identities,
                rho=float(inputs.scalars["rho"]),
                d2_receipt=d2_receipt,
                ledger=ledger,
                switching_source=directory,
            )
            if terminal is not None:
                metrics["disposition"] = terminal
                _write_json(directory / "checkpoint_manifest.json", metrics)
                _seal_directory(directory, "CH5_D123_RESUMED_CONTINUATION_CHECKPOINT_V1")
                return _finalize_resume(
                    repository, output, pre_hashes, ledger, terminal,
                    {"final_checkpoint": checkpoint, "terminal_metrics": metrics},
                    started, prefix_wall_seconds,
                )
            next_value = _solve_update(
                directory, checkpoint, current_value, arrays["utility"], q,
                float(inputs.scalars["rho"]), ledger,
            )
            _check_task_ledger(ledger)
            metrics["disposition"] = "CONTINUE_TO_NEXT_CHECKPOINT"
            metrics["direct_solve"] = json.loads(
                (directory / "direct_solve_receipt.json").read_text(encoding="utf-8")
            )
            _write_json(directory / "checkpoint_manifest.json", metrics)
            _seal_directory(directory, "CH5_D123_RESUMED_CONTINUATION_CHECKPOINT_V1")
            if _scientific_code_hashes(repository) != pre_hashes:
                raise FailClosed(
                    "BLOCKED__SCIENTIFIC_CODE_CHANGED_AFTER_FREEZE",
                    {"checkpoint": checkpoint, "stage": "post_update_code_hash"},
                )
            previous_rows, previous_arrays, previous_q = rows, arrays, q
            current_value = next_value
            values.append(current_value)
        raise FailClosed(
            "BLOCKED__UNREACHABLE_CONTINUATION_STATE", {"stage": "loop_exhausted"}
        )
    except FailClosed as failure:
        return _finalize_resume(
            repository, output, pre_hashes, ledger, failure.terminal, failure.detail,
            started, prefix_wall_seconds,
        )
    except Exception as exc:
        terminal = (
            "FAIL__SCIENTIFIC_GATE_AFTER_ENTRY"
            if ledger.get("direct_hjb_solves", 0) or ledger.get("new_corrected_policy_maps", 0)
            else "BLOCKED__ENGINEERING_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE"
        )
        return _finalize_resume(
            repository, output, pre_hashes, ledger, terminal,
            {"stage": "unhandled_exception", "type": type(exc).__name__, "message": str(exc)},
            started, prefix_wall_seconds,
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
    return 0 if terminal in {
        "HJB_CONVERGENCE_CANDIDATE__TERMINAL_GATE_NOT_RUN",
        "COMPLETE_CHECKPOINT6_NONCONVERGED__TERMINAL_GATE_NOT_RUN",
    } else 2


if __name__ == "__main__":
    sys.exit(main())
