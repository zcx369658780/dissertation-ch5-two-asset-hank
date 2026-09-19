"""Bounded continuation from exact accepted checkpoint 10 through checkpoint 12."""

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

from .checkpoint2_to_checkpoint6 import _load_accepted_checkpoint2, _solve_update
from .checkpoint3_to_checkpoint6 import (
    ACCEPTED_CHECKPOINT3_IDENTITY,
    _load_accepted_checkpoint3,
    _read_focused_tests,
    _write_root_manifest,
)
from .checkpoint3_to_checkpoint6_resume import _checkpoint_metrics
from .checkpoint6_to_checkpoint10 import (
    ACCEPTED_CHECKPOINT_IDENTITIES as ACCEPTED_CHECKPOINT4_TO_6_IDENTITIES,
    _load_accepted_checkpoint6,
    _new_ledger as _prior_ledger,
)
from .nonlinear_continuation import (
    N,
    SHAPE,
    FailClosed,
    _canonical_sha256,
    _field_sha256,
    _map_checkpoint,
    _policy_arrays,
    _scientific_code_hashes,
    _seal_directory,
    _selected_identity,
    _sha256,
    _sparse_identity,
    _verify_manifest_files,
    _write_json,
    checkpoint_identity,
)
from .option_a_step import _input_receipt, bind_option_a_inputs
from .selector import SelectorBudget


TASK_ID = (
    "CH5_MP4C_2018_KFE_D123_CHECKPOINT10_TO_CHECKPOINT12_"
    "BOUNDED_NONLINEAR_CONTINUATION_20260920"
)
BASELINE_SHA = "6D6D07110B886C24AACF9AB28E77EAEDB8EF0C82"
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_checkpoint10_to_checkpoint12_"
    "bounded_nonlinear_continuation_20260920_run001"
)
ACCEPTED_ROOT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_checkpoint6_to_checkpoint10_"
    "bounded_nonlinear_continuation_20260919_run001"
)

ACCEPTED_SEALED_MANIFEST_SHA256 = (
    "1959B54DB2EC27BA1F12493F71E9E8AAD5F5442D20099D77EC84C0C2AE902EAC"
)
ACCEPTED_MANIFEST_ENTRY_COUNT = 3249
ACCEPTED_CHECKPOINT_ARRAYS_SHA256 = (
    "BEA1D08A10C53E4EF3246A413A9446633DAAD6A4ACCAD4E34463BB74756C5512"
)
ACCEPTED_VALUE_SHA256 = {
    7: "2D15DBC6839F3653D3497946758735BD4D8C8F4ED8DF8B487C5BDB3B211F9A48",
    8: "9D0C136B68269C305C64C4CAE82B8548DB4B0D224611B666C1AF6D4C54841A7A",
    9: "EC5B3BA1BA65559FE468A3B9821D4D13356D8966631AC338BE08E37863F6732D",
    10: "AE1610BA320F57AF73EE3C5411C298BF00610606B13B5185F2CD65BF1736FB24",
}
ACCEPTED_CHECKPOINT_IDENTITIES = {
    7: "D8C18DFF8EFB21D16F01B7A51E0B2EEAD81976B0221097C800E86C8820C718B2",
    8: "692BB36DE8B44FD0994AA8B933E4B0FC11930860CE84F0F6FDC9BBFD49CE23F2",
    9: "C36F00DF696D4C16B8FCE581D47B2AC396413996911F264543E3325FFFA63653",
    10: "4FC2855AB4102AEAE8B173D0EBBBF40FCD334583A039BE4AE65C8DE2B1145C8D",
}
ACCEPTED_P10_IDENTITY = "89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3"
ACCEPTED_U10_SHA256 = "215BEC4AABBC337147D73A227751CD6A89CC483E3CA056470A2AEF161AA41F38"
ACCEPTED_Q10_ARTIFACT_SHA256 = (
    "917479763C4690FEAB358098D7F1CE2EBB4DD7C4939A7060156E7A4FCDEE59BD"
)
ACCEPTED_Q10_IDENTITY = {
    "data": "B9B180F2ACF9082B5B23C1C52A27652B4FB6CD5215B7DB4816B1102400C720D2",
    "indices": "9A1E128BD9B13A6711B20FB992699DB405DEF5450543921ACAB69B57FA5474E6",
    "indptr": "63190CF1D9F4C98D89C81A9990736462F19170B45F97E03AD7B507D492D9C327",
}
ACCEPTED_B10 = 3.874510913493001e-08
ACCEPTED_D10 = 5.8692895192891115e-06

MAX_NEW_UPDATES = 2
MAX_NEW_POLICY_MAPS = 2
MAX_SELECTOR_EVALUATIONS = 1600
MAX_ROOT_INVOCATIONS = 622_512
MAX_INTERIOR_Z_ROOT_INVOCATIONS = 570_240
MAX_INTERIOR_A_ROOT_INVOCATIONS = 1600
MAX_JOINT_ROOT_INVOCATIONS = 1600


def _new_ledger() -> dict[str, Any]:
    ledger = _prior_ledger()
    ledger.update(
        accepted_v7_loads=0,
        accepted_v8_loads=0,
        accepted_v9_loads=0,
        accepted_v10_loads=0,
        accepted_p10_loads=0,
        accepted_u10_loads=0,
        accepted_q10_loads=0,
        accepted_checkpoint10_manifest_loads=0,
        v10_policy_map_reruns=0,
        q10_assembly_reruns=0,
    )
    return ledger


def _check_task_ledger(ledger: dict[str, Any]) -> None:
    ceilings = {
        "v2_policy_map_reruns": 0,
        "q2_assembly_reruns": 0,
        "v3_policy_map_reruns": 0,
        "q3_assembly_reruns": 0,
        "v6_policy_map_reruns": 0,
        "q6_assembly_reruns": 0,
        "v10_policy_map_reruns": 0,
        "q10_assembly_reruns": 0,
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


def _apply_checkpoint12_ceiling(checkpoint: int, terminal: str | None) -> str | None:
    if terminal is not None:
        return terminal
    if checkpoint == 12:
        return "COMPLETE_CHECKPOINT12_NONCONVERGED__TERMINAL_GATE_NOT_RUN"
    return None


def _load_accepted_checkpoint10(repository: Path) -> dict[str, Any]:
    root = repository / ACCEPTED_ROOT_RELATIVE
    manifest_path = root / "sealed_manifest.json"
    if _sha256(manifest_path) != ACCEPTED_SEALED_MANIFEST_SHA256:
        raise FailClosed(
            "BLOCKED__ACCEPTED_CHECKPOINT10_PROVENANCE_DRIFT",
            {"stage": "accepted_sealed_manifest_hash"},
        )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    _verify_manifest_files(root, manifest)
    if int(manifest.get("entry_count", -1)) != ACCEPTED_MANIFEST_ENTRY_COUNT:
        raise FailClosed(
            "BLOCKED__ACCEPTED_CHECKPOINT10_PROVENANCE_DRIFT",
            {"stage": "accepted_manifest_entry_count"},
        )

    values: dict[int, np.ndarray] = {}
    checkpoint_manifests: dict[int, dict[str, Any]] = {}
    for checkpoint in range(7, 11):
        directory = root / f"checkpoint_{checkpoint:03d}"
        arrays_path = directory / "checkpoint_arrays.npz"
        checkpoint_manifest = json.loads(
            (directory / "checkpoint_manifest.json").read_text(encoding="utf-8")
        )
        with np.load(arrays_path, allow_pickle=False) as loaded:
            value = np.array(loaded["value"], dtype=float, copy=True, order="F")
        checks = {
            "shape": value.shape == SHAPE,
            "finite": bool(np.all(np.isfinite(value))),
            "value_exact": _field_sha256(value) == ACCEPTED_VALUE_SHA256[checkpoint],
            "manifest_value_exact": checkpoint_manifest.get("value_sha256")
            == ACCEPTED_VALUE_SHA256[checkpoint],
            "checkpoint_identity_exact": checkpoint_manifest.get(
                "checkpoint_identity_sha256"
            )
            == ACCEPTED_CHECKPOINT_IDENTITIES[checkpoint],
            "primary_nonconverged": checkpoint_manifest.get(
                "primary_convergence_pass"
            )
            is False,
            "d2_pass": checkpoint_manifest.get("d2_receipt_status") == "PASS",
        }
        if checkpoint == 10:
            checks["arrays_artifact_exact"] = (
                _sha256(arrays_path) == ACCEPTED_CHECKPOINT_ARRAYS_SHA256
            )
        if not all(checks.values()):
            raise FailClosed(
                "BLOCKED__ACCEPTED_CHECKPOINT10_PROVENANCE_DRIFT",
                {
                    "stage": "accepted_history_binding",
                    "checkpoint": checkpoint,
                    "checks": checks,
                },
            )
        values[checkpoint] = value
        checkpoint_manifests[checkpoint] = checkpoint_manifest

    checkpoint10_root = root / "checkpoint_010"
    rows: list[dict[str, Any]] = []
    for flat in range(N):
        receipt = json.loads(
            (checkpoint10_root / f"cell_{flat:04d}.json").read_text(encoding="utf-8")
        )
        result = receipt.get("selector_result", {})
        if (
            int(receipt.get("flat_index_f_zero_based", -1)) != flat
            or result.get("outcome") != "SELECTED_ADMISSIBLE"
            or not isinstance(result.get("selected"), dict)
        ):
            raise FailClosed(
                "BLOCKED__ACCEPTED_CHECKPOINT10_PROVENANCE_DRIFT",
                {"stage": "accepted_p10_receipt", "flat": flat},
            )
        rows.append(result["selected"])
    arrays = _policy_arrays(rows)
    policy_identity = _canonical_sha256([_selected_identity(row) for row in rows])
    arrays_path = checkpoint10_root / "checkpoint_arrays.npz"
    q10_path = checkpoint10_root / "q_generator.npz"
    with np.load(arrays_path, allow_pickle=False) as loaded:
        utility = np.array(loaded["utility"], dtype=float, copy=True, order="F")
        mu_b = np.array(loaded["mu_b"], dtype=float, copy=True, order="F")
        mu_a = np.array(loaded["mu_a"], dtype=float, copy=True, order="F")
    q10 = sparse.csr_matrix(sparse.load_npz(q10_path))
    checkpoint10_manifest = checkpoint_manifests[10]
    cycle = json.loads(
        (checkpoint10_root / "cycle_detection_receipt.json").read_text(encoding="utf-8")
    )
    checks = {
        "p10_exact": policy_identity == ACCEPTED_P10_IDENTITY,
        "u10_exact": _field_sha256(utility) == ACCEPTED_U10_SHA256,
        "utility_rows_equal": np.array_equal(arrays["utility"], utility),
        "mu_b_rows_equal": np.array_equal(arrays["g_b"], mu_b),
        "mu_a_rows_equal": np.array_equal(arrays["g_a"], mu_a),
        "q10_artifact_exact": _sha256(q10_path) == ACCEPTED_Q10_ARTIFACT_SHA256,
        "q10_shape": q10.shape == (N, N),
        "q10_identity_exact": _sparse_identity(q10) == ACCEPTED_Q10_IDENTITY,
        "checkpoint10_identity_recomputed": checkpoint_identity(
            ACCEPTED_VALUE_SHA256[10], policy_identity, _sparse_identity(q10)
        )
        == ACCEPTED_CHECKPOINT_IDENTITIES[10],
        "checkpoint10_b_exact": float(
            checkpoint10_manifest["bellman_residual_inf"]
        )
        == ACCEPTED_B10,
        "checkpoint10_d_exact": float(checkpoint10_manifest["value_change_inf"])
        == ACCEPTED_D10,
        "checkpoint10_exact_cycle_none": cycle.get("exact_period") is None,
        "checkpoint10_approximate_cycle_none": cycle.get(
            "approximate_period_2_or_3"
        )
        is None,
    }
    if not all(checks.values()):
        raise FailClosed(
            "BLOCKED__ACCEPTED_CHECKPOINT10_PROVENANCE_DRIFT",
            {"stage": "accepted_checkpoint10_binding", "checks": checks},
        )
    return {
        "values": values,
        "checkpoint_manifests": checkpoint_manifests,
        "p10_rows": rows,
        "p10_arrays": arrays,
        "q10": q10,
        "checks": checks,
        "manifest_entry_count": int(manifest["entry_count"]),
        "v10_policy_map_rerun": False,
        "q10_assembly_rerun": False,
    }


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
            "accepted_checkpoint10_identity": ACCEPTED_CHECKPOINT_IDENTITIES[10],
            "accepted_checkpoint10_reused_without_policy_map_or_q10_assembly": True,
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
        accepted3 = _load_accepted_checkpoint3(repository)
        accepted6 = _load_accepted_checkpoint6(repository)
        accepted = _load_accepted_checkpoint10(repository)
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
            accepted_v4_loads=1,
            accepted_v5_loads=1,
            accepted_v6_loads=1,
            accepted_p6_loads=1,
            accepted_u6_loads=1,
            accepted_q6_loads=1,
            accepted_checkpoint6_manifest_loads=1,
            accepted_v7_loads=1,
            accepted_v8_loads=1,
            accepted_v9_loads=1,
            accepted_v10_loads=1,
            accepted_p10_loads=1,
            accepted_u10_loads=1,
            accepted_q10_loads=1,
            accepted_checkpoint10_manifest_loads=1,
        )
        values = [
            prior["v0"],
            prior["v1"],
            prior["v2"],
            accepted3["v3"],
            accepted6["values"][4],
            accepted6["values"][5],
            accepted6["values"][6],
            accepted["values"][7],
            accepted["values"][8],
            accepted["values"][9],
            accepted["values"][10],
        ]
        identities = [
            prior["checkpoint1_identity"],
            prior["checkpoint2_identity"],
            ACCEPTED_CHECKPOINT3_IDENTITY,
            ACCEPTED_CHECKPOINT4_TO_6_IDENTITIES[4],
            ACCEPTED_CHECKPOINT4_TO_6_IDENTITIES[5],
            ACCEPTED_CHECKPOINT4_TO_6_IDENTITIES[6],
            ACCEPTED_CHECKPOINT_IDENTITIES[7],
            ACCEPTED_CHECKPOINT_IDENTITIES[8],
            ACCEPTED_CHECKPOINT_IDENTITIES[9],
            ACCEPTED_CHECKPOINT_IDENTITIES[10],
        ]
        _write_json(
            output / "accepted_checkpoint10_binding.json",
            {
                "status": "PASS",
                "input_identity": _input_receipt(inputs),
                "accepted_checkpoint2_identities": prior["identities"],
                "accepted_checkpoint3_identities": accepted3["identities"],
                "accepted_checkpoint4_to_6_identities": ACCEPTED_CHECKPOINT4_TO_6_IDENTITIES,
                "accepted_checkpoint7_to_10_identities": ACCEPTED_CHECKPOINT_IDENTITIES,
                "accepted_checkpoint10_checks": accepted["checks"],
                "accepted_manifest_entry_count": accepted["manifest_entry_count"],
                "history_value_sha256": {
                    str(index): _field_sha256(value)
                    for index, value in enumerate(values)
                },
                "history_checkpoint_identities_1_to_10": identities,
                "v10_policy_map_rerun": False,
                "q10_assembly_rerun": False,
            },
        )
        previous_rows = accepted["p10_rows"]
        previous_arrays = accepted["p10_arrays"]
        previous_q = accepted["q10"]
        checkpoint10_dir = output / "checkpoint_010"
        checkpoint10_dir.mkdir(parents=False, exist_ok=False)
        _write_json(
            checkpoint10_dir / "accepted_source_receipt.json",
            {
                "checkpoint": 10,
                "accepted_checkpoint_identity": ACCEPTED_CHECKPOINT_IDENTITIES[10],
                "accepted_bellman_residual_inf": ACCEPTED_B10,
                "accepted_value_change_inf": ACCEPTED_D10,
                "v10_policy_map_rerun": False,
                "q10_assembly_rerun": False,
            },
        )
        current_value = _solve_update(
            checkpoint10_dir,
            10,
            accepted["values"][10],
            accepted["p10_arrays"]["utility"],
            accepted["q10"],
            float(inputs.scalars["rho"]),
            ledger,
        )
        _check_task_ledger(ledger)
        _seal_directory(
            checkpoint10_dir, "CH5_D123_ACCEPTED_CHECKPOINT10_UPDATE_TO_11_V1"
        )
        values.append(current_value)
        budget = SelectorBudget(
            max_selector_evaluations=MAX_SELECTOR_EVALUATIONS,
            max_root_invocations=MAX_ROOT_INVOCATIONS,
            max_interior_z_root_invocations=MAX_INTERIOR_Z_ROOT_INVOCATIONS,
            max_interior_a_switching_root_invocations=MAX_INTERIOR_A_ROOT_INVOCATIONS,
            max_joint_switching_root_invocations=MAX_JOINT_ROOT_INVOCATIONS,
        )
        for checkpoint in range(11, 13):
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
            terminal = _apply_checkpoint12_ceiling(checkpoint, terminal)
            if terminal is not None:
                metrics["disposition"] = terminal
                _write_json(directory / "checkpoint_manifest.json", metrics)
                _seal_directory(
                    directory, "CH5_D123_CHECKPOINT10_TO_12_CHECKPOINT_V1"
                )
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
            _seal_directory(directory, "CH5_D123_CHECKPOINT10_TO_12_CHECKPOINT_V1")
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
        return _finalize(
            repository, output, pre_hashes, ledger, failure.terminal, failure.detail, started
        )
    except Exception as exc:
        terminal = (
            "FAIL__SCIENTIFIC_GATE_AFTER_ENTRY"
            if ledger.get("direct_hjb_solves", 0)
            or ledger.get("new_corrected_policy_maps", 0)
            else "BLOCKED__ENGINEERING_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE"
        )
        return _finalize(
            repository,
            output,
            pre_hashes,
            ledger,
            terminal,
            {
                "stage": "unhandled_exception",
                "type": type(exc).__name__,
                "message": str(exc),
            },
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
        "COMPLETE_CHECKPOINT12_NONCONVERGED__TERMINAL_GATE_NOT_RUN",
    }
    return 0 if terminal in successful else 2


if __name__ == "__main__":
    sys.exit(main())
