"""Bounded selector-repair gate and fresh corrected turn-2 run002."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import time
from typing import Any, Iterable

import numpy as np

from ch5_two_asset_hank.corrected_diagnostic import optionb_turn2_household_integration as base
from ch5_two_asset_hank.corrected_diagnostic.contracts import CorrectedDiagnosticGrid
from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import FailClosed
from ch5_two_asset_hank.multi_province.one_turn import PreFrozenHouseholdOutputBatch
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER


TASK_ID = "CH5_MP4C_ACTIVE_UPPER_B_NEGATIVE_BRANCH_ENUMERATION_REPAIR_AND_TURN2_RUN002_20260920"
BASELINE_SHA = "f0885e30832f30f3259f0549f6831fa9c17f6905"
PASS_TERMINAL = (
    "PASS__ACTIVE_UPPER_B_NEGATIVE_BRANCH_ENUMERATION_REPAIR__CORRECTED_TURN2_"
    "31_PROVINCE_HOUSEHOLD_HJB_KFE_AND_INTEGRATION__RAW_TURN3_PAYOFF_READY__TURN3_NOT_RUN"
)
BLOCKED_IMPACT = "BLOCKED__UPPER_B_NEGATIVE_REPAIR_PREDECESSOR_IMPACT_SET_NONEMPTY"
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_corrected_optionb_turn2_upper_b_negative_repair_20260920_run002"
)
TASK_RELATIVE = Path(
    "tasks/CH5_MP4C_ACTIVE_UPPER_B_NEGATIVE_BRANCH_ENUMERATION_REPAIR_AND_TURN2_RUN002_20260920.md"
)
RUNNER_RELATIVE = Path(
    "validators/multi_province/active_upper_b_negative_repair_turn2_run002/run.py"
)
RUNNER_TEST_RELATIVE = Path(
    "tests/test_mp4c_active_upper_b_negative_repair_turn2_run002.py"
)
SELECTOR_RELATIVE = Path("src/ch5_two_asset_hank/corrected_diagnostic/selector.py")
FOCUSED_TEST_RELATIVE = Path(
    "tests/test_mp4c_active_upper_b_negative_branch_enumeration_repair.py"
)
FORENSIC_ROOT = Path(
    "reports/ch5_mp4c_turn2_beijing_f0579_upper_b_negative_branch_forensic_20260920_run002"
)
TURN2_RUN001_ROOT = Path(
    "reports/ch5_mp4c_corrected_optionb_turn2_unique_closed_class_kfe_20260920_run001"
)
TURN1_RUN004_ROOT = Path(
    "reports/ch5_mp4c_corrected_optionb_initial_turn_unique_closed_class_kfe_20260920_run004"
)
INTEGRATION_ROOT = base.ENTERING_STATE_RELATIVE.parent
FORENSIC_MANIFEST_SHA256 = "0DB648C10B42F5A8A187334FACEC123F9FD231999E09F650FE19C33114F420B4"
TURN2_RUN001_MANIFEST_SHA256 = "50D2E87C94E762D3936C64E3AAD416F600118AEBB8DCE1588DB369938FA2351A"
INTEGRATION_MANIFEST_SHA256 = "79C6B15340AF641A736C79D0ED7C6450E39EA495263943280B6DDBD1B094F28D"
TARGET_REJECTION = "DERIVATIVE_BRANCH_NOT_UNIQUE_BEFORE_ROOT"
EXPECTED_CHANGED_PATHS = sorted(
    path.as_posix()
    for path in (
        SELECTOR_RELATIVE,
        FOCUSED_TEST_RELATIVE,
        RUNNER_RELATIVE,
        RUNNER_TEST_RELATIVE,
        RUNNER_RELATIVE.parent / "__init__.py",
    )
)
UNCHANGED_SCIENTIFIC_PATHS = (
    Path("src/ch5_two_asset_hank/corrected_diagnostic/cost.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/generator.py"),
)


def _git(repository: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repository, text=True).strip()


def _verify_manifest(root: Path, expected_sha256: str, expected_entries: int) -> dict[str, Any]:
    manifest_path = root / "sealed_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bad_paths = []
    for row in manifest["entries"]:
        path = root / row["path"]
        if (
            not path.is_file()
            or path.stat().st_size != int(row["bytes"])
            or base._sha256(path) != row["sha256"]
        ):
            bad_paths.append(row["path"])
    readback = json.loads((root / "independent_readback_receipt.json").read_text(encoding="utf-8"))
    checks = {
        "manifest_sha256": base._sha256(manifest_path) == expected_sha256,
        "entry_count": int(manifest["entry_count"]) == expected_entries,
        "all_entries_read_back": not bad_paths,
        "accepted_readback": readback.get("status") == "PASS" and not readback.get("bad_paths"),
    }
    receipt = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "root": root.name,
        "manifest_sha256": base._sha256(manifest_path),
        "entry_count": int(manifest["entry_count"]),
        "total_bytes": int(manifest["total_bytes"]),
        "checks": checks,
        "bad_paths": bad_paths,
    }
    if receipt["status"] != "PASS":
        raise FailClosed("BLOCKED__ACCEPTED_PREDECESSOR_MANIFEST_MISMATCH", receipt)
    return receipt


def _walk_dicts(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from _walk_dicts(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_dicts(child)


def predecessor_impact_audit(repository: Path) -> dict[str, Any]:
    targets = (
        ("accepted_turn1_run004", repository / TURN1_RUN004_ROOT / "household"),
        (
            "reached_turn2_run001_checkpoint0_1",
            repository / TURN2_RUN001_ROOT / "household/p00_北京",
        ),
    )
    summaries = []
    matches = []
    for label, root in targets:
        if label.startswith("reached_turn2"):
            json_paths = sorted(
                path
                for checkpoint in (root / "checkpoint_000", root / "checkpoint_001")
                for path in checkpoint.rglob("*.json")
            )
        else:
            json_paths = sorted(root.rglob("*.json"))
        cell_paths = [path for path in json_paths if path.name.startswith("cell_")]
        candidate_dict_count = 0
        exact_token_file_count = 0
        for path in json_paths:
            text = path.read_text(encoding="utf-8")
            if TARGET_REJECTION in text:
                exact_token_file_count += 1
            payload = json.loads(text)
            for candidate in _walk_dicts(payload):
                if "active_constraints" not in candidate or "rejection_reasons" not in candidate:
                    continue
                candidate_dict_count += 1
                if (
                    "upper_b" in candidate.get("active_constraints", [])
                    and candidate.get("transfer_branch") == "negative"
                    and TARGET_REJECTION in candidate.get("rejection_reasons", [])
                ):
                    matches.append(
                        {
                            "target": label,
                            "path": path.relative_to(repository).as_posix(),
                            "cell_id": candidate.get("cell_id"),
                            "candidate": candidate,
                        }
                    )
        summaries.append(
            {
                "target": label,
                "root": root.relative_to(repository).as_posix(),
                "persisted_json_receipts_scanned": len(json_paths),
                "persisted_cell_receipts_scanned": len(cell_paths),
                "persisted_candidate_dictionaries": candidate_dict_count,
                "exact_target_token_file_count": exact_token_file_count,
                "representation": "compact_checkpoint_receipts_without_rejected_candidates"
                if not cell_paths
                else "cell_receipts_present",
            }
        )
    receipt = {
        "status": "PASS" if not matches else "FAIL",
        "gate": "TARGET_OCCURRENCE_SET_MUST_BE_EMPTY",
        "targets": summaries,
        "exact_matching_cell_list": matches,
        "match_count": len(matches),
        "checkpoint2_f0579_partial_receipt_excluded": True,
        "science_calls": 0,
    }
    return receipt


def _source_freeze(repository: Path) -> dict[str, str]:
    paths = (
        SELECTOR_RELATIVE,
        FOCUSED_TEST_RELATIVE,
        RUNNER_RELATIVE,
        RUNNER_TEST_RELATIVE,
        RUNNER_RELATIVE.parent / "__init__.py",
        *UNCHANGED_SCIENTIFIC_PATHS,
    )
    return {path.as_posix(): base._sha256(repository / path) for path in paths}


def _unchanged_scientific_blobs(repository: Path) -> dict[str, Any]:
    rows = {}
    for path in UNCHANGED_SCIENTIFIC_PATHS:
        current = _git(repository, "rev-parse", f"HEAD:{path.as_posix()}")
        baseline = _git(repository, "rev-parse", f"{BASELINE_SHA}:{path.as_posix()}")
        rows[path.as_posix()] = {"head_blob": current, "baseline_blob": baseline, "unchanged": current == baseline}
    return rows


def _capture_f0579(repository: Path, output: Path) -> tuple[Any, dict[str, Any]]:
    original = base._map_checkpoint
    state: dict[str, Any] = {"capture_count": 0}

    def wrapped(*args, **kwargs):
        result = original(*args, **kwargs)
        checkpoint = int(args[2])
        province_root = Path(args[1])
        if checkpoint == 2 and province_root.name == "p00_北京":
            cell_path = province_root / "checkpoint_002/cell_0579.json"
            payload = json.loads(cell_path.read_text(encoding="utf-8"))
            selector = payload["selector_result"]
            negative = [
                row
                for row in selector["candidates"]
                if row["active_constraints"] == ["upper_b"]
                and row["transfer_branch"] == "negative"
            ]
            if len(negative) != 2:
                raise FailClosed(
                    "FAIL__F0579_REPAIR_PARITY_MISMATCH",
                    {"negative_branch_count": len(negative)},
                )
            backward, forward = negative
            selected = selector["selected"]
            checks = {
                "two_negative_branches": len(negative) == 2,
                "backward_only_a_direction_failure": backward["rejection_reasons"] == ["A_DERIVATIVE_DIRECTION_INCONSISTENT"],
                "forward_unique_selected": selector["outcome"] == "SELECTED_ADMISSIBLE" and selector["admissible_comparison_count"] == 1 and selected == forward,
                "q_b": selected["q_b"] == 0.00470259773014529,
                "q_a": selected["q_a"] == -0.0004814219651986697,
                "d": selected["d"] == -2.1102602580753396,
                "g_a": selected["g_a"] == 1.6015031989929152,
                "transfer_kkt_residual": selected["transfer_kkt_residual"] == 6.505213034913027e-19,
                "hamiltonian": selected["hamiltonian"] == -0.07995936564187259,
                "root_invocations": selector["root_invocations"] == 4,
            }
            receipt = {
                "status": "PASS" if all(checks.values()) else "FAIL",
                "source": cell_path.relative_to(repository).as_posix(),
                "checks": checks,
                "backward": backward,
                "forward": forward,
                "selected": selected,
                "no_additional_selector_or_root_call": True,
            }
            base._write_json(output / "f0579_repair_parity_receipt.json", receipt)
            state.update({"capture_count": 1, "receipt": receipt})
            if receipt["status"] != "PASS":
                raise FailClosed("FAIL__F0579_REPAIR_PARITY_MISMATCH", receipt)
        return result

    return wrapped, state


def _finalize(
    repository: Path,
    output: Path,
    pre_freeze: dict[str, str],
    ledger: dict[str, Any],
    terminal: str,
    detail: dict[str, Any],
    started: float,
) -> str:
    post_freeze = _source_freeze(repository)
    if post_freeze != pre_freeze:
        terminal = "BLOCKED__SCIENTIFIC_CODE_CHANGED_AFTER_FREEZE"
        detail = {"prior_detail": detail}
    base._check_ledger(ledger)
    ledger["wall_seconds"] = float(time.perf_counter() - started)
    ledger["terminal_verdict"] = terminal
    base._write_json(output / "scientific_ledger.json", ledger)
    base._write_json(
        output / "post_execution_code_freeze.json",
        {
            "status": "PASS" if post_freeze == pre_freeze else "FAIL",
            "source_sha256_after": post_freeze,
            "matches_pre_execution_freeze": post_freeze == pre_freeze,
        },
    )
    base._write_json(
        output / "terminal_receipt.json",
        {
            "terminal_verdict": terminal,
            "detail": detail,
            "turn3_household_run": False,
            "successor_published": False,
            "results_eligibility": False,
        },
    )
    base._manifest(output)
    base._readback(output)
    return terminal


def execute(repository: Path, focused_test_junit: Path) -> str:
    repository = repository.resolve(strict=True)
    output = repository / OUTPUT_RELATIVE
    started = time.perf_counter()
    ledger = base._new_ledger()
    base.TASK_RELATIVE = TASK_RELATIVE
    impact = predecessor_impact_audit(repository)
    focused = base._read_junit(focused_test_junit)
    changed_paths = sorted(filter(None, _git(repository, "diff", "--name-only", f"{BASELINE_SHA}...HEAD").splitlines()))
    manifests = {
        "f0579_forensic_run002": _verify_manifest(repository / FORENSIC_ROOT, FORENSIC_MANIFEST_SHA256, 16),
        "turn2_run001": _verify_manifest(repository / TURN2_RUN001_ROOT, TURN2_RUN001_MANIFEST_SHA256, 612),
        "canonical_initial_integration": _verify_manifest(repository / INTEGRATION_ROOT, INTEGRATION_MANIFEST_SHA256, 17),
    }
    unchanged = _unchanged_scientific_blobs(repository)
    startup_checks = {
        "origin_main_exact_baseline": _git(repository, "rev-parse", "origin/main") == BASELINE_SHA,
        "baseline_is_ancestor": subprocess.run(["git", "merge-base", "--is-ancestor", BASELINE_SHA, "HEAD"], cwd=repository).returncode == 0,
        "clean_code_freeze_worktree": not _git(repository, "status", "--porcelain"),
        "changed_paths_exact": changed_paths == EXPECTED_CHANGED_PATHS,
        "focused_tests": focused["status"] == "PASS",
        "predecessor_impact_empty": impact["status"] == "PASS",
        "manifests": all(row["status"] == "PASS" for row in manifests.values()),
        "cost_hjb_kfe_sources_unchanged": all(row["unchanged"] for row in unchanged.values()),
    }
    if not startup_checks["predecessor_impact_empty"]:
        raise FailClosed(BLOCKED_IMPACT, impact)
    if not all(startup_checks.values()):
        raise FailClosed("BLOCKED__UPPER_B_REPAIR_ZERO_SCIENCE_GATE", {"checks": startup_checks})

    states, entering = base.load_initial_states(repository)
    pre_freeze = _source_freeze(repository)
    core_hashes = base._scientific_code_hashes(repository)
    task_hashes = base._task_hashes(repository)
    output.mkdir(parents=True, exist_ok=False)
    base._write_json(output / "authority_binding.json", {
        "status": "PASS", "task_id": TASK_ID, "execution_head": _git(repository, "rev-parse", "HEAD"),
        "actual_live_main_baseline": BASELINE_SHA, "checks": startup_checks,
        "manifests": manifests, "unchanged_scientific_blobs": unchanged,
        "entering_state": entering,
    })
    base._write_json(output / "predecessor_impact_audit.json", impact)
    base._write_json(output / "focused_test_receipt.json", {**focused, "scientific_calls": 0})
    base._write_json(output / "pre_execution_code_freeze.json", {
        "status": "PASS", "source_sha256_before": pre_freeze,
        "base_task_hashes": task_hashes, "core_corrected_code_sha256_before": core_hashes,
    })
    base._write_json(output / "zero_science_preexecution_gate_receipt.json", {
        "status": "PASS", "checks": startup_checks, "scientific_calls": 0,
        "predecessor_impact_match_count": impact["match_count"],
    })
    base._write_json(output / "turn2_entering_state_receipt_31province.json", entering)
    base._write_json(output / "historical_lineage_receipt.json", {
        "status": "PASS", "turn2_run001_manifest": TURN2_RUN001_MANIFEST_SHA256,
        "forensic_run002_manifest": FORENSIC_MANIFEST_SHA256,
        "historical_consumption_merged_into_run002_ledger": False,
    })

    original_map = base._map_checkpoint
    wrapped_map, parity_state = _capture_f0579(repository, output)
    base._map_checkpoint = wrapped_map
    try:
        native_grid = base.oracle.MatlabFaithfulHJBGrid(
            np.linspace(-2, 5, 20), np.linspace(0, 10, 20), np.array([0.8, 1.3]),
            np.array([[-1 / 3, 1 / 3], [1 / 3, -1 / 3]]),
        )
        grid = CorrectedDiagnosticGrid(native_grid.b, native_grid.a, native_grid.z)
        native_params = base.oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
        results = []
        for index, province in enumerate(PROVINCE_ORDER):
            results.append(base._solve_province(
                repository, output, index, province, states[index], grid, native_grid,
                native_params, task_hashes, core_hashes, ledger,
            ))
        if len(results) != 31 or parity_state["capture_count"] != 1:
            raise FailClosed("FAIL__TURN2_HOUSEHOLD_OR_F0579_PARITY_INCOMPLETE", {
                "household_count": len(results), "f0579_capture_count": parity_state["capture_count"],
            })

        ledger["household_batch_constructions"] += 1
        batch = PreFrozenHouseholdOutputBatch(
            ct=[row["aggregates"]["Ct"]["mass_form"] for row in results],
            household_lt=[row["aggregates"]["Lt"]["mass_form"] for row in results],
            at=[row["aggregates"]["At"]["mass_form"] for row in results],
            bt=[row["aggregates"]["Bt"]["mass_form"] for row in results],
            at_tax=[row["aggregates"]["AtTax"]["mass_form"] for row in results],
            converged=(True,) * 31,
            diagnostics=tuple({"checkpoint": row["checkpoint"], "B": row["B"], "D": row["D"]} for row in results),
        )
        base._write_json(output / "household_batch_receipt.json", {
            "status": "PASS", "province_count": 31,
            "identity_sha256": base._canonical_sha256({
                "ct": batch.ct.tolist(), "lt": batch.household_lt.tolist(),
                "at": batch.at.tolist(), "bt": batch.bt.tolist(), "at_tax": batch.at_tax.tolist(),
            }),
            "rows": [
                {"province_index": i, "province": row["province"], "checkpoint": row["checkpoint"],
                 "B": row["B"], "D": row["D"], "backward_error_max": row["backward_error_max"]}
                for i, row in enumerate(results)
            ],
        })
        integration = base.integrate_one_turn(repository, states, batch, ledger)
        shares = np.asarray(integration.pop("portfolio_shares_destination_origin"), dtype=np.float64)
        terms = np.asarray(integration.pop("ordered_product_terms"), dtype=np.float64)
        raw_ra0 = np.asarray(integration["raw_ra0_turn2_by_destination"], dtype=np.float64)
        rah_turn3 = np.asarray(integration["rah_turn3_raw_by_origin"], dtype=np.float64)
        blas = np.asarray(integration["blas_diagnostic"], dtype=np.float64)
        np.savez_compressed(output / "canonical_turn3_raw_payoff_arrays.npz", raw_ra0_turn2=raw_ra0,
                           shares_destination_origin=shares, ordered_product_terms=terms,
                           canonical_rah_turn3=rah_turn3, blas_diagnostic=blas)
        base._write_json(output / "one_turn_integration_receipt.json", integration)
        base._write_json(output / "canonical_turn3_raw_payoff_receipt.json", {
            key: integration[key] for key in (
                "orientation", "portfolio_shares_sha256", "raw_ra0_turn2_sha256",
                "ordered_product_terms_sha256", "rah_turn3_sha256",
                "raw_ra0_turn2_by_destination", "rah_turn3_raw_by_origin", "blas_diagnostic",
                "canonical_vs_blas_max_abs_difference", "canonical_vs_blas_bitwise_equal_count",
                "blas_is_acceptance_gate",
            )
        })
        base._write_json(output / "turn_to_turn_movement_diagnostics.json", integration["movement_diagnostics"])
        base._write_json(output / "turn3_next_state_candidate_receipt.json", {
            "status": "PASS", "classification": "TURN3_INPUT_CANDIDATE_ONLY__TURN3_NOT_RUN",
            "raw_next_payoff_sha256": integration["rah_turn3_sha256"], "rows": integration["next_states"],
        })
        return _finalize(repository, output, pre_freeze, ledger, PASS_TERMINAL, {
            "household_pass_count": 31, "integration_status": "PASS",
            "turn3_payoff_sha256": integration["rah_turn3_sha256"], "turn3_household_run": False,
        }, started)
    except FailClosed as failure:
        return _finalize(repository, output, pre_freeze, ledger, failure.terminal, failure.detail, started)
    except Exception as exc:
        return _finalize(repository, output, pre_freeze, ledger,
                         "FAIL__UNEXPECTED_TASK_EXCEPTION__NO_SCIENTIFIC_RETRY",
                         {"type": type(exc).__name__, "message": str(exc)}, started)
    finally:
        base._map_checkpoint = original_map


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
