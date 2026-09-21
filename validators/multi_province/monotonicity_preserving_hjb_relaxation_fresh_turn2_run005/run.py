"""Fresh canonical turn-2 run005 under the adopted HJB relaxation law."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import time
from typing import Any

import numpy as np

REPOSITORY_IMPORT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPOSITORY_IMPORT_ROOT))
sys.path.insert(0, str(REPOSITORY_IMPORT_ROOT / "src"))

from ch5_two_asset_hank.corrected_diagnostic import optionb_turn2_household_integration as base
from ch5_two_asset_hank.corrected_diagnostic.contracts import CorrectedDiagnosticGrid
from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import FailClosed
from ch5_two_asset_hank.multi_province.one_turn import PreFrozenHouseholdOutputBatch
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER


TASK_ID = "CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_FRESH_TURN2_RUN005_20260921"
BASELINE = "8e9ad015aa01ff1c7a0ca42c6cf2150942aaeca3"
ACCEPTED_IMPLEMENTATION = "5dbd04ad4aaf252381283501d762d633f504ba07"
PASS_TERMINAL = "PASS__MONOTONICITY_PRESERVING_RELAXATION_FRESH_TURN2_RUN005__31_PROVINCE_HJB_KFE_AND_INTEGRATION_PASS__RAW_TURN3_PAYOFF_READY__TURN3_NOT_RUN"
OUTPUT_RELATIVE = Path("reports/ch5_mp4c_monotonicity_preserving_hjb_relaxation_fresh_turn2_run005_20260921")
TASK_RELATIVE = Path("tasks/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_FRESH_TURN2_RUN005_20260921.md")
ENTERING_RELATIVE = Path("reports/ch5_mp4c_run004_canonical_same_s_integration_replay_20260920_run001/next_state_candidate_receipt.json")
ENTERING_BLOB = "85df3f0bdcc3b0bb3e7b12f0ba35dbb9abda764d"
ENTERING_SHA256 = "E519E468B04D7EDC631F6A931FF367A7EDE5C3D510ED4E0979AB2FC8E13C5E11"
ENTERING_PAYOFF_SHA256 = "D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414"
VALIDATOR_RELATIVE = Path("validators/multi_province/monotonicity_preserving_hjb_relaxation_fresh_turn2_run005/run.py")
TEST_RELATIVE = Path("tests/test_mp4c_monotonicity_preserving_hjb_relaxation_fresh_turn2_run005.py")

FROZEN_PATHS = (
    Path("src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/selector.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/cost.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/generator.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/option_a_step.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/q1_kfe_validation.py"),
)

HLJ_EXPECTED = {
    0: {
        "old": "7BEDB2FD4BA8DEA72095DE1F44FF6F12AF4B9008809501B7925CEC612CB0B575",
        "full": "74913F05A786569C62C6DD309F97B87F98AEDDC1474EB1AFAADE13D36E294E32",
        "accepted": "74913F05A786569C62C6DD309F97B87F98AEDDC1474EB1AFAADE13D36E294E32",
        "alpha": 1.0,
    },
    1: {
        "old": "74913F05A786569C62C6DD309F97B87F98AEDDC1474EB1AFAADE13D36E294E32",
        "full": "2C6D5FCBA2FDF64805CBE9AA9C6E414C395F1D3CB246F57278C7AD4BEEF4DEDA",
        "accepted": "2C6D5FCBA2FDF64805CBE9AA9C6E414C395F1D3CB246F57278C7AD4BEEF4DEDA",
        "alpha": 1.0,
    },
    2: {
        "old": "2C6D5FCBA2FDF64805CBE9AA9C6E414C395F1D3CB246F57278C7AD4BEEF4DEDA",
        "full": "1FA95217C9EEFDAA638F0CD07F00B59B053EB4A59E5670A0CED94852922DBFE7",
        "accepted": "987A20DE9252104ECFAB59436433F0C73EEB8C513589B8B0FA98DB64018B66BF",
        "alpha": 0.5,
        "minimum": 0.005032838660371801,
    },
}


def git(repository: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repository, text=True).strip()


def accepted_source_binding(repository: Path) -> dict[str, Any]:
    rows = []
    for path in FROZEN_PATHS:
        accepted = git(repository, "rev-parse", f"{ACCEPTED_IMPLEMENTATION}:{path.as_posix()}")
        head = git(repository, "rev-parse", f"HEAD:{path.as_posix()}")
        rows.append({"path": path.as_posix(), "accepted_blob": accepted, "head_blob": head, "exact": accepted == head})
    return {"status": "PASS" if all(row["exact"] for row in rows) else "FAIL", "rows": rows}


def entering_binding(repository: Path) -> dict[str, Any]:
    path = repository / ENTERING_RELATIVE
    payload = json.loads(path.read_text(encoding="utf-8"))
    checks = {
        "git_blob": git(repository, "rev-parse", f"HEAD:{ENTERING_RELATIVE.as_posix()}") == ENTERING_BLOB,
        "file_sha256": base._sha256(path) == ENTERING_SHA256,
        "raw_payoff_sha256": payload.get("raw_next_payoff_sha256") == ENTERING_PAYOFF_SHA256,
        "row_count": len(payload.get("rows", [])) == 31,
        "canonical_order": [row.get("province") for row in payload.get("rows", [])] == list(PROVINCE_ORDER),
    }
    return {"status": "PASS" if all(checks.values()) else "FAIL", "checks": checks, "path": ENTERING_RELATIVE.as_posix()}


def preflight(repository: Path) -> dict[str, Any]:
    source = accepted_source_binding(repository)
    entering = entering_binding(repository)
    production_diff = git(repository, "diff", "--name-only", "--", "src/ch5_two_asset_hank").splitlines()
    checks = {
        "head_exact_live_main": git(repository, "rev-parse", "HEAD") == BASELINE,
        "origin_main_exact": git(repository, "rev-parse", "origin/main") == BASELINE,
        "accepted_production_exact": source["status"] == "PASS",
        "entering_state_exact": entering["status"] == "PASS",
        "production_worktree_diff_empty": not production_diff,
    }
    return {"status": "PASS" if all(checks.values()) else "FAIL", "checks": checks, "source": source, "entering": entering, "production_diff": production_diff}


def new_relaxation_ledger() -> dict[str, Any]:
    return {
        "helper_invocations": 0,
        "alpha_candidates_evaluated": 0,
        "relaxed_updates_alpha_lt_1": 0,
        "accepted_halving_counts": {},
        "minimum_accepted_raw_b_slope_by_province": {},
        "records": [],
        "failure": None,
    }


def write_runtime_status(output: Path, state: dict[str, Any]) -> None:
    base._write_json(output / "relaxation_arithmetic_ledger.json", state["relaxation"])
    base._write_json(output / "heilongjiang_runtime_parity_receipt.json", state["heilongjiang"])


def install_runtime_capture(output: Path, state: dict[str, Any]):
    original_direct = base._direct_update
    original_helper = base.monotonicity_preserving_relaxation

    def helper(old, full, b_nodes):
        directory = state["context"]
        province_root = directory.parent
        checkpoint = int(directory.name.rsplit("_", 1)[1])
        province = province_root.name.split("_", 1)[1]
        province_index = int(province_root.name[1:3])
        state["relaxation"]["helper_invocations"] += 1
        try:
            accepted, receipt = original_helper(old, full, b_nodes)
        except FailClosed as failure:
            attempts = failure.detail.get("attempts", [])
            state["relaxation"]["alpha_candidates_evaluated"] += len(attempts)
            state["relaxation"]["failure"] = {
                "province_index": province_index, "province": province, "checkpoint": checkpoint,
                "terminal": failure.terminal, "attempts": len(attempts),
            }
            write_runtime_status(output, state)
            raise
        attempts = receipt["attempts"]
        state["relaxation"]["alpha_candidates_evaluated"] += len(attempts)
        halvings = int(receipt["accepted_halvings"])
        key = str(halvings)
        state["relaxation"]["accepted_halving_counts"][key] = state["relaxation"]["accepted_halving_counts"].get(key, 0) + 1
        if receipt["accepted_alpha"] < 1.0:
            state["relaxation"]["relaxed_updates_alpha_lt_1"] += 1
        minimum = float(attempts[-1]["minimum_raw_b_slope"])
        prior = state["relaxation"]["minimum_accepted_raw_b_slope_by_province"].get(province)
        state["relaxation"]["minimum_accepted_raw_b_slope_by_province"][province] = minimum if prior is None else min(prior, minimum)
        record = {
            "province_index": province_index, "province": province, "checkpoint_from": checkpoint,
            "old_sha256": receipt["value_old_sha256"], "full_sha256": receipt["full_candidate_sha256"],
            "accepted_sha256": receipt["accepted_next_value_sha256"],
            "alpha": receipt["accepted_alpha"], "halvings": halvings,
            "attempt_count": len(attempts), "minimum_raw_b_slope": minimum,
        }
        state["relaxation"]["records"].append(record)
        if province_index == 7 and checkpoint in HLJ_EXPECTED:
            expected = HLJ_EXPECTED[checkpoint]
            exact_pretrajectory = all(
                state["heilongjiang"]["checkpoints"].get(str(k), {}).get("trajectory_exact", False)
                for k in range(checkpoint)
            )
            trajectory_exact = record["old_sha256"] == expected["old"] and record["full_sha256"] == expected["full"]
            parity_required = checkpoint == 0 or exact_pretrajectory
            parity = (
                trajectory_exact and record["accepted_sha256"] == expected["accepted"]
                and record["alpha"] == expected["alpha"]
                and (checkpoint != 2 or minimum == expected["minimum"])
            )
            state["heilongjiang"]["checkpoints"][str(checkpoint)] = {
                **record, "trajectory_exact": trajectory_exact, "parity_required": parity_required,
                "parity_pass": parity if parity_required else None,
            }
            if not trajectory_exact and state["heilongjiang"]["first_divergence"] is None:
                state["heilongjiang"]["first_divergence"] = {"checkpoint": checkpoint, "actual": record, "expected": expected}
            if parity_required and not parity:
                write_runtime_status(output, state)
                raise FailClosed("FAIL__HEILONGJIANG_RUNTIME_RELAXATION_PARITY_MISMATCH", state["heilongjiang"])
        write_runtime_status(output, state)
        return accepted, receipt

    def direct(*args, **kwargs):
        state["context"] = Path(args[0])
        try:
            return original_direct(*args, **kwargs)
        finally:
            state["context"] = None

    base.monotonicity_preserving_relaxation = helper
    base._direct_update = direct
    return original_direct, original_helper


def reached_province_status(output: Path, terminal: str, detail: dict[str, Any]) -> dict[str, Any]:
    rows = []
    household = output / "household"
    if household.is_dir():
        for province_root in sorted(household.glob("p[0-9][0-9]_*")):
            terminal_path = province_root / "province_terminal_receipt.json"
            checkpoints = sorted(province_root.glob("checkpoint_[0-9][0-9][0-9]/checkpoint_manifest.json"))
            if terminal_path.is_file():
                receipt = json.loads(terminal_path.read_text(encoding="utf-8"))
                rows.append({"province_index": receipt["province_index"], "province": receipt["province"], "status": "HJB_KFE_PASS", "checkpoint": receipt["checkpoint"], "B": receipt["B"], "D": receipt["D"], "kfe": receipt["kfe"]})
            else:
                last = None if not checkpoints else json.loads(checkpoints[-1].read_text(encoding="utf-8"))
                rows.append({"province_index": int(province_root.name[1:3]), "province": province_root.name.split("_", 1)[1], "status": "FIRST_FAILURE_REACHED_PROVINCE", "last_checkpoint": None if last is None else last.get("checkpoint"), "last_disposition": None if last is None else last.get("disposition"), "terminal": terminal, "detail": detail})
    return {"reached_provinces": len(rows), "hjb_kfe_pass": sum(row["status"] == "HJB_KFE_PASS" for row in rows), "rows": rows}


def finalize(repository: Path, output: Path, pre_hashes: dict[str, str], ledger: dict[str, Any], state: dict[str, Any], terminal: str, detail: dict[str, Any], started: float) -> str:
    post_hashes = base._task_hashes(repository)
    if post_hashes != pre_hashes:
        terminal = "BLOCKED__SCIENTIFIC_CODE_CHANGED_AFTER_FREEZE"
        detail = {"prior_detail": detail}
    base._check_ledger(ledger)
    ledger["wall_seconds"] = float(time.perf_counter() - started)
    ledger["terminal_verdict"] = terminal
    base._write_json(output / "scientific_ledger.json", ledger)
    write_runtime_status(output, state)
    base._write_json(output / "reached_province_hjb_kfe_status.json", reached_province_status(output, terminal, detail))
    base._write_json(output / "post_execution_code_freeze.json", {"status": "PASS" if post_hashes == pre_hashes else "FAIL", "source_sha256_after": post_hashes, "matches_pre_execution_freeze": post_hashes == pre_hashes})
    base._write_json(output / "terminal_receipt.json", {"terminal_verdict": terminal, "detail": detail, "turn3_household_run": False, "k1b": 0, "k2": 0, "successor_published": False, "results_eligibility": False})
    base._manifest(output)
    base._readback(output)
    return terminal


def execute(repository: Path, focused_test_junit: Path) -> str:
    repository = repository.resolve(strict=True)
    output = repository / OUTPUT_RELATIVE
    if output.exists():
        raise FailClosed("BLOCKED__FRESH_EVIDENCE_ROOT_ALREADY_EXISTS", {"path": output.as_posix()})
    gate = preflight(repository)
    focused = base._read_junit(focused_test_junit)
    if gate["status"] != "PASS" or focused["status"] != "PASS":
        raise FailClosed("BLOCKED__RUN005_PREEXECUTION_GATE", {"preflight": gate, "focused": focused})
    base.TASK_RELATIVE = TASK_RELATIVE
    started = time.perf_counter()
    ledger = base._new_ledger()
    pre_hashes = base._task_hashes(repository)
    core_hashes = base._scientific_code_hashes(repository)
    states, entering = base.load_initial_states(repository)
    if entering["file_sha256"] != ENTERING_SHA256:
        raise FailClosed("BLOCKED__TURN2_ENTERING_STATE_FILE_SHA256_MISMATCH", entering)
    output.mkdir(parents=True, exist_ok=False)
    base._write_json(output / "authority_source_binding.json", {"status": "PASS", "task_id": TASK_ID, "baseline": BASELINE, "preflight": gate})
    base._write_json(output / "entering_state_binding.json", entering)
    base._write_json(output / "focused_test_receipt.json", focused)
    base._write_json(output / "pre_execution_code_freeze.json", {"status": "PASS", "task_source_sha256_before": pre_hashes, "core_source_sha256_before": core_hashes})
    state = {"context": None, "relaxation": new_relaxation_ledger(), "heilongjiang": {"status": "NOT_REACHED", "checkpoints": {}, "first_divergence": None}}
    original_direct, original_helper = install_runtime_capture(output, state)
    try:
        native_grid = base.oracle.MatlabFaithfulHJBGrid(np.linspace(-2, 5, 20), np.linspace(0, 10, 20), np.array([0.8, 1.3]), np.array([[-1/3, 1/3], [1/3, -1/3]]))
        grid = CorrectedDiagnosticGrid(native_grid.b, native_grid.a, native_grid.z)
        native_params = base.oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
        results = []
        for index, province in enumerate(PROVINCE_ORDER):
            results.append(base._solve_province(repository, output, index, province, states[index], grid, native_grid, native_params, pre_hashes, core_hashes, ledger))
            if index == 7:
                state["heilongjiang"]["status"] = "REACHED_AND_PROVINCE_PASS"
                write_runtime_status(output, state)
        if len(results) != 31:
            raise FailClosed("FAIL__TURN2_HOUSEHOLD_BATCH_INCOMPLETE", {"count": len(results)})
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
        base._write_json(output / "household_batch_receipt.json", {"status": "PASS", "province_count": 31, "rows": [{"province_index": i, "province": row["province"], "checkpoint": row["checkpoint"], "B": row["B"], "D": row["D"]} for i, row in enumerate(results)]})
        integration = base.integrate_one_turn(repository, states, batch, ledger)
        shares = np.asarray(integration.pop("portfolio_shares_destination_origin"), dtype=np.float64)
        terms = np.asarray(integration.pop("ordered_product_terms"), dtype=np.float64)
        np.savez_compressed(output / "canonical_turn3_raw_payoff_arrays.npz", raw_ra0_turn2=np.asarray(integration["raw_ra0_turn2_by_destination"]), shares_destination_origin=shares, ordered_product_terms=terms, canonical_rah_turn3=np.asarray(integration["rah_turn3_raw_by_origin"]), blas_diagnostic=np.asarray(integration["blas_diagnostic"]))
        base._write_json(output / "one_turn_integration_receipt.json", integration)
        base._write_json(output / "turn3_next_state_candidate_receipt.json", {"status": "PASS", "classification": "TURN3_INPUT_CANDIDATE_ONLY__TURN3_NOT_RUN", "raw_next_payoff_sha256": integration["rah_turn3_sha256"], "rows": integration["next_states"]})
        return finalize(repository, output, pre_hashes, ledger, state, PASS_TERMINAL, {"household_pass_count": 31, "integration_status": "PASS", "turn3_payoff_sha256": integration["rah_turn3_sha256"], "turn3_household_run": False}, started)
    except FailClosed as failure:
        return finalize(repository, output, pre_hashes, ledger, state, failure.terminal, failure.detail, started)
    except Exception as exc:
        return finalize(repository, output, pre_hashes, ledger, state, "FAIL__UNEXPECTED_TASK_EXCEPTION__NO_SCIENTIFIC_RETRY", {"type": type(exc).__name__, "message": str(exc)}, started)
    finally:
        base._direct_update = original_direct
        base.monotonicity_preserving_relaxation = original_helper


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--focused-test-junit", type=Path, required=True)
    args = parser.parse_args(argv)
    verdict = execute(args.repository, args.focused_test_junit)
    print(verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
