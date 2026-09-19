"""Bounded continuation from exact accepted checkpoint 6 through checkpoint 10."""

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
)
from .checkpoint3_to_checkpoint6 import (
    ACCEPTED_CHECKPOINT3_IDENTITY,
    _load_accepted_checkpoint3,
    _new_ledger as _prior_ledger,
    _read_focused_tests,
    _write_root_manifest,
)
from .checkpoint3_to_checkpoint6_resume import _checkpoint_metrics
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
    "CH5_MP4C_2018_KFE_D123_CHECKPOINT6_TO_CHECKPOINT10_"
    "BOUNDED_NONLINEAR_CONTINUATION_20260919"
)
BASELINE_SHA = "C852473A3123513E26493DB1FEF75A65A8680B0D"
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_checkpoint6_to_checkpoint10_"
    "bounded_nonlinear_continuation_20260919_run001"
)
ACCEPTED_ROOT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_checkpoint3_to_checkpoint6_"
    "bounded_nonlinear_continuation_20260919_resume001"
)

ACCEPTED_SEALED_MANIFEST_SHA256 = (
    "1BFAB497357EE2740B259E23AD970EEB927799D9FD37A60A7D30E544E1970725"
)
ACCEPTED_CHECKPOINT_ARRAYS_SHA256 = {
    6: "C703E99742D87565D3FB15EDE4091B265EF36B47D6109DA44052B5290DC4F98D",
}
ACCEPTED_VALUE_SHA256 = {
    4: "938682CEA35E4ED77F02087AB6BDE9204A0B4C00B9E898E3200799D1367C149B",
    5: "34077AE29E144E3BC5773A830A7577419EEE19B41424A7771C74E46554DECD6B",
    6: "69865ACDD71A26A3E3F4A8DAD55C964F826D34C774C9B8193FE997973EE6D89F",
}
ACCEPTED_CHECKPOINT_IDENTITIES = {
    4: "69BA60083B3D96CDCFF1BE935AC425C04F68DF44A9FDB545209FA4280742F420",
    5: "1CACE68D0BD30F24F16FB032ECCB6BCA2B2F939AF3A6B4556098DB1CBF577080",
    6: "B26177C216DA6902226BD93E802A2B1FE0E794B29BE14EA1A1BCBFFD8F8691A1",
}
ACCEPTED_P6_IDENTITY = "63026FBE8BE72E3B29B5FC44EBD100C01C146179D05B55C779E9E232AEA435A3"
ACCEPTED_U6_SHA256 = "09D5A6622535709146751865931109F058FED3688FAE755C5EF9A0E00AD8B89E"
ACCEPTED_Q6_ARTIFACT_SHA256 = (
    "039734AF0BC38AD3BD0FF38854CBE8B4B0B93BA415EC2A47B1C09F827EA7F454"
)
ACCEPTED_Q6_IDENTITY = {
    "data": "CE091A208909AEA1D71637DD269FF5D98A59CE5785F90870212D453F86DBFDC9",
    "indices": "B44ED2AC2E4E86E01B040089645FE66EEC5CFB7874E6DCDA6A307803632B70E4",
    "indptr": "DC38CF83DFC0A6F522020AC8DBC16EDBEB4E1D273A59EDCA6697CD721E3593F2",
}
ACCEPTED_B6 = 0.005940678766947715
ACCEPTED_D6 = 0.010000685482095761

MAX_NEW_UPDATES = 4
MAX_NEW_POLICY_MAPS = 4
MAX_SELECTOR_EVALUATIONS = 3200
MAX_ROOT_INVOCATIONS = 1_245_024
MAX_INTERIOR_Z_ROOT_INVOCATIONS = 1_140_480
MAX_INTERIOR_A_ROOT_INVOCATIONS = 3200
MAX_JOINT_ROOT_INVOCATIONS = 3200


def _new_ledger() -> dict[str, Any]:
    ledger = _prior_ledger()
    ledger.update(
        accepted_v4_loads=0,
        accepted_v5_loads=0,
        accepted_v6_loads=0,
        accepted_p6_loads=0,
        accepted_u6_loads=0,
        accepted_q6_loads=0,
        accepted_checkpoint6_manifest_loads=0,
        v6_policy_map_reruns=0,
        q6_assembly_reruns=0,
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


def _apply_checkpoint10_ceiling(checkpoint: int, terminal: str | None) -> str | None:
    if terminal is not None:
        return terminal
    if checkpoint == 10:
        return "COMPLETE_CHECKPOINT10_NONCONVERGED__TERMINAL_GATE_NOT_RUN"
    return None


def _load_accepted_checkpoint6(repository: Path) -> dict[str, Any]:
    root = repository / ACCEPTED_ROOT_RELATIVE
    manifest_path = root / "sealed_manifest.json"
    if _sha256(manifest_path) != ACCEPTED_SEALED_MANIFEST_SHA256:
        raise FailClosed(
            "BLOCKED__ACCEPTED_CHECKPOINT6_PROVENANCE_DRIFT",
            {"stage": "accepted_sealed_manifest_hash"},
        )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    _verify_manifest_files(root, manifest)

    values: dict[int, np.ndarray] = {}
    checkpoint_manifests: dict[int, dict[str, Any]] = {}
    for checkpoint in range(4, 7):
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
            "manifest_value_exact": (
                checkpoint_manifest.get("value_sha256")
                == ACCEPTED_VALUE_SHA256[checkpoint]
            ),
            "checkpoint_identity_exact": (
                checkpoint_manifest.get("checkpoint_identity_sha256")
                == ACCEPTED_CHECKPOINT_IDENTITIES[checkpoint]
            ),
            "primary_nonconverged": (
                checkpoint_manifest.get("primary_convergence_pass") is False
            ),
        }
        if checkpoint == 6:
            checks["arrays_artifact_exact"] = (
                _sha256(arrays_path) == ACCEPTED_CHECKPOINT_ARRAYS_SHA256[6]
            )
        if not all(checks.values()):
            raise FailClosed(
                "BLOCKED__ACCEPTED_CHECKPOINT6_PROVENANCE_DRIFT",
                {"stage": "accepted_history_binding", "checkpoint": checkpoint, "checks": checks},
            )
        values[checkpoint] = value
        checkpoint_manifests[checkpoint] = checkpoint_manifest

    checkpoint6_root = root / "checkpoint_006"
    rows: list[dict[str, Any]] = []
    for flat in range(N):
        receipt = json.loads(
            (checkpoint6_root / f"cell_{flat:04d}.json").read_text(encoding="utf-8")
        )
        result = receipt.get("selector_result", {})
        if (
            int(receipt.get("flat_index_f_zero_based", -1)) != flat
            or result.get("outcome") != "SELECTED_ADMISSIBLE"
            or not isinstance(result.get("selected"), dict)
        ):
            raise FailClosed(
                "BLOCKED__ACCEPTED_CHECKPOINT6_PROVENANCE_DRIFT",
                {"stage": "accepted_p6_receipt", "flat": flat},
            )
        rows.append(result["selected"])
    arrays = _policy_arrays(rows)
    policy_identity = _canonical_sha256([_selected_identity(row) for row in rows])
    arrays_path = checkpoint6_root / "checkpoint_arrays.npz"
    q6_path = checkpoint6_root / "q_generator.npz"
    with np.load(arrays_path, allow_pickle=False) as loaded:
        utility = np.array(loaded["utility"], dtype=float, copy=True, order="F")
        mu_b = np.array(loaded["mu_b"], dtype=float, copy=True, order="F")
        mu_a = np.array(loaded["mu_a"], dtype=float, copy=True, order="F")
    q6 = sparse.csr_matrix(sparse.load_npz(q6_path))
    checkpoint6_manifest = checkpoint_manifests[6]
    cycle = json.loads(
        (checkpoint6_root / "cycle_detection_receipt.json").read_text(encoding="utf-8")
    )
    checks = {
        "p6_exact": policy_identity == ACCEPTED_P6_IDENTITY,
        "u6_exact": _field_sha256(utility) == ACCEPTED_U6_SHA256,
        "utility_rows_equal": np.array_equal(arrays["utility"], utility),
        "mu_b_rows_equal": np.array_equal(arrays["g_b"], mu_b),
        "mu_a_rows_equal": np.array_equal(arrays["g_a"], mu_a),
        "q6_artifact_exact": _sha256(q6_path) == ACCEPTED_Q6_ARTIFACT_SHA256,
        "q6_shape": q6.shape == (N, N),
        "q6_identity_exact": _sparse_identity(q6) == ACCEPTED_Q6_IDENTITY,
        "checkpoint6_identity_recomputed": checkpoint_identity(
            ACCEPTED_VALUE_SHA256[6], policy_identity, _sparse_identity(q6)
        )
        == ACCEPTED_CHECKPOINT_IDENTITIES[6],
        "checkpoint6_b_exact": (
            float(checkpoint6_manifest["bellman_residual_inf"]) == ACCEPTED_B6
        ),
        "checkpoint6_d_exact": (
            float(checkpoint6_manifest["value_change_inf"]) == ACCEPTED_D6
        ),
        "checkpoint6_exact_cycle_none": cycle.get("exact_period") is None,
        "checkpoint6_approximate_cycle_none": (
            cycle.get("approximate_period_2_or_3") is None
        ),
    }
    if not all(checks.values()):
        raise FailClosed(
            "BLOCKED__ACCEPTED_CHECKPOINT6_PROVENANCE_DRIFT",
            {"stage": "accepted_checkpoint6_binding", "checks": checks},
        )
    return {
        "values": values,
        "checkpoint_manifests": checkpoint_manifests,
        "p6_rows": rows,
        "p6_arrays": arrays,
        "q6": q6,
        "checks": checks,
        "manifest_entry_count": int(manifest["entry_count"]),
        "v6_policy_map_rerun": False,
        "q6_assembly_rerun": False,
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
            "accepted_checkpoint6_identity": ACCEPTED_CHECKPOINT_IDENTITIES[6],
            "accepted_checkpoint6_reused_without_policy_map_or_q6_assembly": True,
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
        accepted = _load_accepted_checkpoint6(repository)
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
        )
        values = [
            prior["v0"],
            prior["v1"],
            prior["v2"],
            accepted3["v3"],
            accepted["values"][4],
            accepted["values"][5],
            accepted["values"][6],
        ]
        identities = [
            prior["checkpoint1_identity"],
            prior["checkpoint2_identity"],
            ACCEPTED_CHECKPOINT3_IDENTITY,
            ACCEPTED_CHECKPOINT_IDENTITIES[4],
            ACCEPTED_CHECKPOINT_IDENTITIES[5],
            ACCEPTED_CHECKPOINT_IDENTITIES[6],
        ]
        _write_json(
            output / "accepted_checkpoint6_binding.json",
            {
                "status": "PASS",
                "input_identity": _input_receipt(inputs),
                "accepted_checkpoint2_identities": prior["identities"],
                "accepted_checkpoint3_identities": accepted3["identities"],
                "accepted_checkpoint4_to_6_identities": ACCEPTED_CHECKPOINT_IDENTITIES,
                "accepted_checkpoint6_checks": accepted["checks"],
                "accepted_manifest_entry_count": accepted["manifest_entry_count"],
                "history_value_sha256": {
                    str(index): _field_sha256(value)
                    for index, value in enumerate(values)
                },
                "history_checkpoint_identities_1_to_6": identities,
                "v6_policy_map_rerun": False,
                "q6_assembly_rerun": False,
            },
        )
        previous_rows = accepted["p6_rows"]
        previous_arrays = accepted["p6_arrays"]
        previous_q = accepted["q6"]
        checkpoint6_dir = output / "checkpoint_006"
        checkpoint6_dir.mkdir(parents=False, exist_ok=False)
        _write_json(
            checkpoint6_dir / "accepted_source_receipt.json",
            {
                "checkpoint": 6,
                "accepted_checkpoint_identity": ACCEPTED_CHECKPOINT_IDENTITIES[6],
                "accepted_bellman_residual_inf": ACCEPTED_B6,
                "accepted_value_change_inf": ACCEPTED_D6,
                "v6_policy_map_rerun": False,
                "q6_assembly_rerun": False,
            },
        )
        current_value = _solve_update(
            checkpoint6_dir,
            6,
            accepted["values"][6],
            accepted["p6_arrays"]["utility"],
            accepted["q6"],
            float(inputs.scalars["rho"]),
            ledger,
        )
        _check_task_ledger(ledger)
        _seal_directory(checkpoint6_dir, "CH5_D123_ACCEPTED_CHECKPOINT6_UPDATE_TO_7_V1")
        values.append(current_value)
        budget = SelectorBudget(
            max_selector_evaluations=MAX_SELECTOR_EVALUATIONS,
            max_root_invocations=MAX_ROOT_INVOCATIONS,
            max_interior_z_root_invocations=MAX_INTERIOR_Z_ROOT_INVOCATIONS,
            max_interior_a_switching_root_invocations=MAX_INTERIOR_A_ROOT_INVOCATIONS,
            max_joint_switching_root_invocations=MAX_JOINT_ROOT_INVOCATIONS,
        )
        for checkpoint in range(7, 11):
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
            terminal = _apply_checkpoint10_ceiling(checkpoint, terminal)
            if terminal is not None:
                metrics["disposition"] = terminal
                _write_json(directory / "checkpoint_manifest.json", metrics)
                _seal_directory(directory, "CH5_D123_CHECKPOINT6_TO_10_CHECKPOINT_V1")
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
            _seal_directory(directory, "CH5_D123_CHECKPOINT6_TO_10_CHECKPOINT_V1")
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
        "COMPLETE_CHECKPOINT10_NONCONVERGED__TERMINAL_GATE_NOT_RUN",
    }
    return 0 if terminal in successful else 2


if __name__ == "__main__":
    sys.exit(main())
