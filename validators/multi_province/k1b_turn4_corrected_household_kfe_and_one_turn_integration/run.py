"""One bounded K1B-active corrected turn-4 household/KFE and integration."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import subprocess
import sys
import time
from typing import Any

import numpy as np

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPOSITORY_ROOT))
sys.path.insert(0, str(REPOSITORY_ROOT / "src"))

from ch5_two_asset_hank.corrected_diagnostic import optionb_turn2_household_integration as base
from ch5_two_asset_hank.corrected_diagnostic.contracts import CorrectedDiagnosticGrid
from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import FailClosed
from ch5_two_asset_hank.multi_province.capital_network import (
    CONSERVATION_TOLERANCE,
    ForeignConditionalShareInputs,
    foreign_conditional_shares,
)
from ch5_two_asset_hank.multi_province.one_turn import PreFrozenHouseholdOutputBatch
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER
from validators.multi_province.k1b_turn3_lagged_raw_ra0_activation_safety_gate import run as safety


TASK_ID = "CH5_MP4C_K1B_TURN4_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_20260921"
BASELINE = "ea2b4a99ac7ce12f950b43170bc86e8bfeede37f"
ACCEPTED_IMPLEMENTATION = "5dbd04ad4aaf252381283501d762d633f504ba07"
PASS_TERMINAL = "PASS__K1B_TURN4_31_PROVINCE_HJB_KFE_AND_ONE_INTEGRATION__TURN5_K1B_INPUT_READY__TURN5_NOT_RUN"
OUTPUT_RELATIVE = Path("reports/ch5_mp4c_k1b_turn4_corrected_household_kfe_and_one_turn_integration_20260921_run001")
TASK_RELATIVE = Path("tasks/CH5_MP4C_K1B_TURN4_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_20260921.md")
ENTERING_RELATIVE = Path("reports/ch5_mp4c_k1b_turn3_corrected_household_kfe_and_one_turn_integration_20260921_run001/turn4_k1b_input_candidate.json")
SHARE_PLAN_RELATIVE = Path("reports/ch5_mp4c_k1b_turn3_corrected_household_kfe_and_one_turn_integration_20260921_run001/turn4_k1b_frozen_share_payoff_plan.npz")
ENTERING_BLOB = "ee779174c614980a0e6182d710ea5aaec8afb6f5"
ENTERING_SHA256 = "35CA47135CF3B17ADACDD6C39FBA30CC0E55AE1C103C5F42064D6722AF28310C"
SHARE_PLAN_BLOB = "a37647bb68ed1bec6259071d7035f8de07591c9f"
SHARE_PLAN_FILE_SHA256 = "41B7DDA4DE2C33C6EADFAB3F324C3592D119B0E91DC7AE8E23968653A881522A"
TURN4_SHARE_SHA256 = "5E8FB74E547CBF776A70E908F1ECA7F8FD80DD1A7637100BBD159B7F0803028B"
TURN4_RAH_SHA256 = "7DE65A71206F52AB3D2DA98D6D01C43A8A69D8B2C423BE49A15D5D287C434BE9"
TURN3_RAW_RA0_SHA256 = "1C587932F4E8471209663D2262DB1BB308857EEEA1198D7868E4721CFB031E8F"
TURN4_CLASSIFICATION = "TURN4_K1B_INPUT_CANDIDATE_ONLY__TURN4_HOUSEHOLD_NOT_RUN"
TURN5_CLASSIFICATION = "TURN5_K1B_INPUT_CANDIDATE_ONLY__TURN5_HOUSEHOLD_NOT_RUN"
PRIOR_ROOT = Path("reports/ch5_mp4c_k1b_turn3_corrected_household_kfe_and_one_turn_integration_20260921_run001")
PRIOR_HOUSEHOLD_RELATIVE = PRIOR_ROOT / "household_batch_receipt.json"
PRIOR_FIRM_RELATIVE = PRIOR_ROOT / "turn3_firm_raw_used_return_receipt.json"
PRIOR_SCORE_RELATIVE = PRIOR_ROOT / "turn4_k1b_zscore_share_payoff_receipt.json"
PRIOR_C1_RELATIVE = PRIOR_ROOT / "turn3_c1_residual_govinv_receipt.json"

FROZEN_PATHS = (
    Path("src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/selector.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/cost.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/generator.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/option_a_step.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/q1_kfe_validation.py"),
)


def git(repository: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repository, text=True).strip()


def accepted_source_binding(repository: Path) -> dict[str, Any]:
    rows = []
    for path in FROZEN_PATHS:
        accepted = git(repository, "rev-parse", f"{ACCEPTED_IMPLEMENTATION}:{path.as_posix()}")
        head = git(repository, "rev-parse", f"HEAD:{path.as_posix()}")
        rows.append({"path": path.as_posix(), "accepted_blob": accepted, "head_blob": head, "exact": accepted == head})
    return {"status": "PASS" if all(row["exact"] for row in rows) else "FAIL", "rows": rows}


def load_entering_and_shares(repository: Path) -> tuple[tuple[dict[str, Any], ...], np.ndarray, dict[str, Any]]:
    path = repository / ENTERING_RELATIVE
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload.get("rows", [])
    states = tuple(dict(row["state"]) for row in rows)
    with np.load(repository / SHARE_PLAN_RELATIVE) as archive:
        shares = np.asarray(archive["portfolio_shares_destination_origin"], dtype=np.float64)
        persisted_rah = np.asarray(archive["rah_turn4_by_origin"], dtype=np.float64)
        persisted_raw = np.asarray(archive["raw_ra0_turn3"], dtype=np.float64)
    rah = np.asarray([state["rah"] for state in states], dtype=np.float64)
    checks = {
        "entering_git_blob": git(repository, "rev-parse", f"HEAD:{ENTERING_RELATIVE.as_posix()}") == ENTERING_BLOB,
        "entering_file_sha256": base._sha256(path) == ENTERING_SHA256,
        "share_plan_git_blob": git(repository, "rev-parse", f"HEAD:{SHARE_PLAN_RELATIVE.as_posix()}") == SHARE_PLAN_BLOB,
        "share_plan_file_sha256": base._sha256(repository / SHARE_PLAN_RELATIVE) == SHARE_PLAN_FILE_SHA256,
        "classification": payload.get("classification") == TURN4_CLASSIFICATION,
        "row_count": len(rows) == 31,
        "canonical_order": tuple(row.get("province") for row in rows) == PROVINCE_ORDER,
        "entering_rah_sha256": base._field_sha256(rah) == TURN4_RAH_SHA256 == payload.get("raw_next_payoff_sha256"),
        "persisted_rah_bitwise": np.array_equal(rah, persisted_rah),
        "frozen_share_sha256": base._field_sha256(shares) == TURN4_SHARE_SHA256 == payload.get("k1b_portfolio_share_plan_sha256"),
        "share_shape": shares.shape == (31, 31),
        "share_finite_nonnegative": bool(np.all(np.isfinite(shares)) and np.all(shares >= 0.0)),
        "share_columns": bool(np.allclose(np.sum(shares, axis=0), 1.0, rtol=0.0, atol=CONSERVATION_TOLERANCE)),
        "completed_turn3_raw_ra0": base._field_sha256(persisted_raw) == TURN3_RAW_RA0_SHA256 == payload.get("source_completed_turn3_raw_ra0_sha256"),
    }
    if not all(checks.values()):
        raise FailClosed("BLOCKED__K1B_TURN4_ENTERING_OR_SHARE_BINDING", {"checks": checks})
    return states, shares, {
        "status": "PASS", "checks": checks, "entering_path": ENTERING_RELATIVE.as_posix(),
        "share_plan_path": SHARE_PLAN_RELATIVE.as_posix(), "entering_file_sha256": base._sha256(path),
        "share_plan_file_sha256": base._sha256(repository / SHARE_PLAN_RELATIVE),
        "entering_rah_sha256": base._field_sha256(rah), "frozen_share_sha256": base._field_sha256(shares),
    }


def load_prior_diagnostics(repository: Path) -> dict[str, Any]:
    household = json.loads((repository / PRIOR_HOUSEHOLD_RELATIVE).read_text(encoding="utf-8"))
    firm = json.loads((repository / PRIOR_FIRM_RELATIVE).read_text(encoding="utf-8"))
    score = json.loads((repository / PRIOR_SCORE_RELATIVE).read_text(encoding="utf-8"))
    c1 = json.loads((repository / PRIOR_C1_RELATIVE).read_text(encoding="utf-8"))
    rows = household.get("rows", [])
    raw = np.asarray(firm.get("raw_ra0_turn3", []), dtype=np.float64)
    checks = {
        "prior_household_pass": household.get("status") == "PASS",
        "prior_household_count": len(rows) == 31,
        "prior_household_order": tuple(row.get("province") for row in rows) == PROVINCE_ORDER,
        "prior_raw_shape_finite": raw.shape == (31,) and bool(np.all(np.isfinite(raw))),
        "prior_raw_sha256": base._field_sha256(raw) == TURN3_RAW_RA0_SHA256 == firm.get("raw_ra0_turn3_sha256"),
        "prior_score_raw_binding": score.get("completed_turn3_raw_ra0_sha256") == TURN3_RAW_RA0_SHA256,
        "prior_score_share_binding": score.get("turn4_portfolio_share_sha256") == TURN4_SHARE_SHA256,
        "prior_score_finite": math.isfinite(float(score.get("ordered_mean", math.nan))) and math.isfinite(float(score.get("population_standard_deviation", math.nan))),
        "prior_c1_pass": c1.get("status") == "PASS" and math.isfinite(float(c1.get("GovInv_C1_total", math.nan))),
    }
    if not all(checks.values()):
        raise FailClosed("BLOCKED__K1B_TURN4_PRIOR_DIAGNOSTIC_BINDING", {"checks": checks})
    return {
        "status": "PASS",
        "checks": checks,
        "household": household,
        "raw_ra0_turn3": raw,
        "score": score,
        "c1": c1,
        "source_sha256": {
            "household": base._sha256(repository / PRIOR_HOUSEHOLD_RELATIVE),
            "firm": base._sha256(repository / PRIOR_FIRM_RELATIVE),
            "score": base._sha256(repository / PRIOR_SCORE_RELATIVE),
            "c1": base._sha256(repository / PRIOR_C1_RELATIVE),
        },
    }


def preflight(repository: Path) -> dict[str, Any]:
    source = accepted_source_binding(repository)
    _, _, entering = load_entering_and_shares(repository)
    prior = load_prior_diagnostics(repository)
    production_diff = git(repository, "diff", "--name-only", "--", "src/ch5_two_asset_hank").splitlines()
    checks = {
        "head_exact_live_main": git(repository, "rev-parse", "HEAD") == BASELINE,
        "origin_main_exact": git(repository, "rev-parse", "origin/main") == BASELINE,
        "accepted_production_exact": source["status"] == "PASS",
        "entering_and_share_exact": entering["status"] == "PASS",
        "prior_diagnostics_exact": prior["status"] == "PASS",
        "production_worktree_diff_empty": not production_diff,
    }
    return {"status": "PASS" if all(checks.values()) else "FAIL", "checks": checks, "source": source, "entering": entering, "prior": {"status": prior["status"], "checks": prior["checks"], "source_sha256": prior["source_sha256"]}, "production_diff": production_diff}


def new_relaxation_ledger() -> dict[str, Any]:
    return {
        "helper_invocations": 0, "alpha_candidates_evaluated": 0,
        "relaxed_updates_alpha_lt_1": 0, "accepted_halving_counts": {},
        "minimum_accepted_raw_b_slope_by_province": {}, "records": [], "failure": None,
    }


def write_relaxation(output: Path, state: dict[str, Any]) -> None:
    base._write_json(output / "relaxation_arithmetic_ledger.json", state["relaxation"])


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
            write_relaxation(output, state)
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
        state["relaxation"]["records"].append({
            "province_index": province_index, "province": province, "checkpoint_from": checkpoint,
            "old_sha256": receipt["value_old_sha256"], "full_sha256": receipt["full_candidate_sha256"],
            "accepted_sha256": receipt["accepted_next_value_sha256"], "alpha": receipt["accepted_alpha"],
            "halvings": halvings, "attempt_count": len(attempts), "minimum_raw_b_slope": minimum,
        })
        write_relaxation(output, state)
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


def task_ledger_check(ledger: dict[str, Any], relaxation: dict[str, Any]) -> None:
    inherited_view = dict(ledger)
    # K1B feedback is a zero-ceiling successor guard in the turn-2 driver.
    # This task authorizes exactly one frozen-share turn-4 K1B allocation.
    inherited_view["k1b_feedback_calls"] = 0
    base._check_ledger(inherited_view)
    ceilings = {
        "authorized_k1b_turn4_household_batches": 1,
        "frozen_k1b_turn4_quantity_allocations": 1,
        "completed_turn4_raw_ra0_vectors": 1,
        "deterministic_turn5_k1b_preparations": 1,
        "turn4_household_calls": 1,
        "fourth_outer_turns": 1,
        "turn5_household_calls": 0,
        "k1b_feedback_calls": 1,
    }
    breaches = {k: {"actual": int(ledger[k]), "ceiling": v} for k, v in ceilings.items() if int(ledger[k]) > v}
    if relaxation["helper_invocations"] > 1550 or relaxation["alpha_candidates_evaluated"] > 82150:
        breaches["relaxation"] = relaxation
    if breaches:
        raise FailClosed("BLOCKED__K1B_TURN4_SCIENTIFIC_LEDGER_CEILING", {"breaches": breaches})


def write_cross_turn_panel(
    repository: Path,
    output: Path,
    states: tuple[dict[str, Any], ...],
    next_states: list[dict[str, Any]],
    household_rows: list[dict[str, Any]],
    raw_ra0_turn4: np.ndarray,
    turn5_mean: float,
    turn5_sigma: float,
    turn5_shares: np.ndarray,
    turn4_govinv_total: float,
) -> dict[str, Any]:
    prior = load_prior_diagnostics(repository)
    prior_household = prior["household"]["rows"]
    prior_raw = prior["raw_ra0_turn3"]
    prior_score = prior["score"]
    prior_c1 = prior["c1"]
    with np.load(repository / SHARE_PLAN_RELATIVE) as archive:
        turn4_shares = np.asarray(archive["portfolio_shares_destination_origin"], dtype=np.float64)

    raw_change = np.asarray(raw_ra0_turn4, dtype=np.float64) - prior_raw
    share_change = np.asarray(turn5_shares, dtype=np.float64) - turn4_shares
    fields = ("Ct", "At", "Bt", "AtTax", "Lt_supply", "Kt_supply", "rah", "w", "rb", "Kt", "Yt", "GovInv")
    aggregate_changes: dict[str, Any] = {}
    for field in fields:
        old = np.asarray([float(state[field]) for state in states], dtype=np.float64)
        new = np.asarray([float(row["state"][field]) for row in next_states], dtype=np.float64)
        change = new - old
        index = int(np.argmax(np.abs(change)))
        aggregate_changes[field] = {
            "turn3_completed_sha256": base._field_sha256(old),
            "turn4_completed_sha256": base._field_sha256(new),
            "maximum_absolute_change": float(abs(change[index])),
            "maximum_absolute_change_province_index": index,
            "maximum_absolute_change_province": PROVINCE_ORDER[index],
            "mean_signed_change": float(math.fsum(float(x) for x in change) / 31.0),
        }

    panel = {
        "status": "PASS",
        "classification": "DESCRIPTIVE_ONLY__NO_DIRECTION_OR_IMPROVEMENT_IS_AN_ACCEPTANCE_CONDITION",
        "household": {
            "turn3_terminal_checkpoints": [int(row["checkpoint"]) for row in prior_household],
            "turn4_terminal_checkpoints": [int(row["checkpoint"]) for row in household_rows],
            "turn3_direct_update_count": int(sum(int(row["checkpoint"]) for row in prior_household)),
            "turn4_direct_update_count": int(sum(int(row["checkpoint"]) for row in household_rows)),
            "checkpoint_change_by_province": [int(household_rows[i]["checkpoint"]) - int(prior_household[i]["checkpoint"]) for i in range(31)],
        },
        "raw_ra0": {
            "turn3_sha256": base._field_sha256(prior_raw),
            "turn4_sha256": base._field_sha256(raw_ra0_turn4),
            "change_sha256": base._field_sha256(raw_change),
            "maximum_absolute_change": float(np.max(np.abs(raw_change))),
            "mean_signed_change": float(math.fsum(float(x) for x in raw_change) / 31.0),
            "euclidean_norm": float(np.linalg.norm(raw_change)),
            "bitwise_changed_count": int(np.count_nonzero(prior_raw != raw_ra0_turn4)),
        },
        "zscore_inputs": {
            "turn4_mean": float(prior_score["ordered_mean"]),
            "turn5_mean": float(turn5_mean),
            "mean_change": float(turn5_mean - float(prior_score["ordered_mean"])),
            "turn4_population_standard_deviation": float(prior_score["population_standard_deviation"]),
            "turn5_population_standard_deviation": float(turn5_sigma),
            "population_standard_deviation_change": float(turn5_sigma - float(prior_score["population_standard_deviation"])),
        },
        "portfolio_shares": {
            "turn4_sha256": base._field_sha256(turn4_shares),
            "turn5_sha256": base._field_sha256(turn5_shares),
            "change_sha256": base._field_sha256(share_change),
            "maximum_absolute_change": float(np.max(np.abs(share_change))),
            "frobenius_norm": float(np.linalg.norm(share_change)),
            "bitwise_changed_count": int(np.count_nonzero(turn4_shares != turn5_shares)),
        },
        "c1": {
            "turn3_GovInv_total": float(prior_c1["GovInv_C1_total"]),
            "turn4_GovInv_total": float(turn4_govinv_total),
            "GovInv_total_change": float(turn4_govinv_total - float(prior_c1["GovInv_C1_total"])),
        },
        "aggregate_state_changes": aggregate_changes,
        "acceptance_condition": "NONE__DESCRIPTIVE_PANEL_ONLY",
    }
    base._write_json(output / "turn3_vs_turn4_cross_turn_diagnostic_panel.json", panel)
    return panel


def integrate_turn4(
    repository: Path,
    output: Path,
    states: tuple[dict[str, Any], ...],
    batch: PreFrozenHouseholdOutputBatch,
    frozen_shares: np.ndarray,
    ledger: dict[str, Any],
    household_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    inputs = base._one_turn_inputs(repository, states, batch)
    household = inputs.household_outputs
    provinces = inputs.old_provinces
    ledger["source_faithful_labor_reconstructions"] += 1
    migration = base.source.reconstruct_migration_labor(base.source.MigrationLaborInputs(
        consumption_by_origin=household.ct,
        population_by_origin=[row["N"] for row in provinces],
        old_firm_wage_by_destination=[row["wjt"] for row in provinces],
        tax_by_origin=[row["tau"] for row in provinces],
        phi_destination_origin=inputs.phi_destination_origin,
        migration_wedge_destination_origin=inputs.migration_wedge_destination_origin,
        gamma_c=inputs.params["ga"], phi_l=inputs.params["phi_l"],
    ))
    base._write_json(output / "source_faithful_labor_receipt.json", {
        "status": "PASS", "calls": 1, "orientation": "destination_by_origin",
        "lt_matrix_sha256": base._field_sha256(migration.lt_mat),
        "lt_supply_sha256": base._field_sha256(migration.lt_supply),
        "labor_destination_total": float(np.sum(migration.lt_supply)),
    })

    ledger["frozen_k1b_turn4_quantity_allocations"] += 1
    ledger["k1b_feedback_calls"] += 1
    shares = np.asarray(frozen_shares, dtype=np.float64)
    theta = np.asarray([row["inter_prv_ratio"] for row in provinces], dtype=np.float64)
    population = np.asarray([row["N"] for row in provinces], dtype=np.float64)
    wealth = np.asarray(household.at, dtype=np.float64) * population
    flows = shares * wealth[None, :]
    capital_columns = np.sum(flows, axis=0)
    private = np.sum(flows, axis=1)
    domestic = np.diag(flows).copy()
    k_scale = max(1.0, float(np.sum(wealth)))
    capital_checks = {
        "frozen_turn4_share_sha256": base._field_sha256(shares) == TURN4_SHARE_SHA256,
        "share_columns": bool(np.allclose(np.sum(shares, axis=0), 1.0, rtol=0.0, atol=CONSERVATION_TOLERANCE)),
        "origin_columns_conserved": bool(np.allclose(capital_columns, wealth, rtol=0.0, atol=CONSERVATION_TOLERANCE * k_scale)),
        "national_private_capital": abs(float(np.sum(private) - np.sum(wealth))) <= CONSERVATION_TOLERANCE * k_scale,
        "home_retained_exact": bool(np.array_equal(domestic, (1.0 - theta) * wealth)),
        "no_same_turn_share_recomputation": True,
    }
    if not all(capital_checks.values()):
        raise FailClosed("FAIL__TURN4_FROZEN_K1B_CAPITAL_ACCOUNTING", {"checks": capital_checks})
    np.savez_compressed(output / "turn4_frozen_k1b_capital_arrays.npz", shares_destination_origin=shares, origin_wealth=wealth, bilateral_private_capital_destination_origin=flows, destination_private_capital=private, domestic_retained=domestic)
    base._write_json(output / "turn4_frozen_k1b_capital_receipt.json", {
        "status": "PASS", "share_plan_sha256": base._field_sha256(shares),
        "origin_private_wealth_total": float(np.sum(wealth)),
        "destination_private_capital_total": float(np.sum(private)),
        "national_private_capital_residual": float(np.sum(private) - np.sum(wealth)),
        "checks": capital_checks,
    })

    ledger["c1_residual_govinv_constructions"] += 1
    accounting = base.residual_government_asset_levels(
        Ktarget_MU=[row["Kt0"] for row in provinces],
        Kprivate_current_MU=private,
        province_order=PROVINCE_ORDER,
    )
    c1_expected = np.maximum(np.asarray([row["Kt0"] for row in provinces], dtype=np.float64) - private, 0.0)
    c1_checks = {
        "exact_residual_rule": bool(np.array_equal(accounting.GovInv_residual_MU, c1_expected)),
        "nonnegative": bool(np.all(accounting.GovInv_residual_MU >= 0.0)),
        "calls_exactly_one": ledger["c1_residual_govinv_constructions"] == 1,
    }
    if not all(c1_checks.values()):
        raise FailClosed("FAIL__TURN4_C1_RESIDUAL_GOVINV", {"checks": c1_checks})
    base._write_json(output / "turn4_c1_residual_govinv_receipt.json", {
        "status": "PASS", "GovInv_C1": accounting.GovInv_residual_MU.tolist(),
        "GovInv_C1_total": float(np.sum(accounting.GovInv_residual_MU)), "checks": c1_checks,
    })

    firms = []
    for index, province in enumerate(provinces):
        firm_source = dict(province)
        firm_source["GovInv"] = float(accounting.GovInv_residual_MU[index])
        firm_source["AtTax"] = float(household.at_tax[index])
        firm_source["Lt_prev"] = float(household.household_lt[index])
        ledger["firm_evaluations"] += 1
        firm = base.source.evaluate_firm(firm_source, float(private[index]), float(migration.lt_supply[index]), inputs.params)
        expected_k = float(accounting.firm_K_accounting_MU[index])
        if abs(float(firm.Kt) - expected_k) > 1e-12 * max(1.0, abs(expected_k)):
            raise FailClosed("FAIL__TURN4_C1_FIRM_CAPITAL_ACCOUNTING", {"province_index": index, "province": PROVINCE_ORDER[index]})
        firms.append(firm)
    if not np.all(np.isfinite([value for firm in firms for value in firm.as_source_dict().values()])):
        raise FailClosed("FAIL__TURN4_FIRM_NONFINITE", {})
    ledger["composite_wage_batches"] += 1
    wages = base.source.composite_household_wages(
        provinces, [firm.wjt for firm in firms], inputs.phi_destination_origin,
        inputs.migration_wedge_destination_origin, phi_l=inputs.params["phi_l"], alphal=inputs.params["alphal"],
    )
    ledger["monetary_assignments"] += 1
    monetary = base.source.taylor_assignment(
        istar=inputs.params["istar"], rho_pi=inputs.params["rho_pi"],
        totalpit=inputs.params["totalpit"], epsilon_pi=inputs.params["epsilon_pi"],
    )
    ledger["fiscal_diagnostic_batches"] += 1
    fiscal = base.source.national_fiscal_diagnostics(
        [firm.Govinc for firm in firms], household.bt, monetary.rb, [row["N"] for row in provinces],
    )
    raw_ra0 = np.asarray([firm.ra0 for firm in firms], dtype=np.float64)
    used_ra = np.asarray([firm.ra for firm in firms], dtype=np.float64)
    ledger["completed_turn4_raw_ra0_vectors"] += 1
    base._write_json(output / "turn4_firm_raw_used_return_receipt.json", {
        "status": "PASS", "raw_ra0_turn4": raw_ra0.tolist(), "raw_ra0_turn4_sha256": base._field_sha256(raw_ra0),
        "used_ra_turn4": used_ra.tolist(), "used_ra_turn4_sha256": base._field_sha256(used_ra),
        "raw_used_difference_count": int(np.count_nonzero(raw_ra0 != used_ra)),
        "rows": [{"province_index": i, "province": PROVINCE_ORDER[i], **firm.as_source_dict()} for i, firm in enumerate(firms)],
    })

    ledger["deterministic_turn5_k1b_preparations"] += 1
    mean, sigma, zscore = safety.ordered_population_zscore(raw_ra0)
    distance = base.load_accepted_distance_score(repository / base.DISTANCE_RELATIVE)
    foreign = foreign_conditional_shares(ForeignConditionalShareInputs(
        province_order=PROVINCE_ORDER, distance_score_destination_origin=distance,
        lagged_return_score_by_destination=zscore, beta_distance=2.0, beta_return=0.5,
        lagged_return_provenance="LAGGED__COMPLETED_TURN4_RAW_RA0__USED_FOR_TURN5_K1B_ATTRACTIVENESS",
    )).foreign_conditional_shares_destination_origin
    shares5 = np.asarray(foreign, dtype=np.float64) * theta[None, :]
    diagonal = np.arange(31)
    shares5[diagonal, diagonal] = 1.0 - theta
    rah5 = safety.ordered_payoff(raw_ra0, shares5)
    ledger["raw_next_payoff_same_s_constructions"] += 1
    turn5_checks = {
        "sigma_finite_positive": math.isfinite(sigma) and sigma > 0.0,
        "zscore_mean": abs(math.fsum(float(x) for x in zscore) / 31.0) <= 1e-15,
        "zscore_population_variance": abs(math.fsum(float(x) * float(x) for x in zscore) / 31.0 - 1.0) <= 1e-15,
        "foreign_diagonal_zero": np.array_equal(np.diag(foreign), np.zeros(31)),
        "foreign_columns": bool(np.allclose(np.sum(foreign, axis=0), 1.0, rtol=0.0, atol=CONSERVATION_TOLERANCE)),
        "full_share_columns": bool(np.allclose(np.sum(shares5, axis=0), 1.0, rtol=0.0, atol=CONSERVATION_TOLERANCE)),
        "home_exact": np.array_equal(np.diag(shares5), 1.0 - theta),
        "payoff_finite": bool(np.all(np.isfinite(rah5))),
        "no_turn5_household": ledger["turn5_household_calls"] == 0,
    }
    if not all(turn5_checks.values()):
        raise FailClosed("FAIL__TURN5_K1B_PREPARATION", {"checks": turn5_checks})
    np.savez_compressed(output / "turn5_k1b_frozen_share_payoff_plan.npz", raw_ra0_turn4=raw_ra0, zscore_by_destination=zscore, foreign_conditional_shares_destination_origin=foreign, portfolio_shares_destination_origin=shares5, rah_turn5_by_origin=rah5)
    base._write_json(output / "turn5_k1b_zscore_share_payoff_receipt.json", {
        "status": "PASS", "beta_distance": 2.0, "beta_return": 0.5, "ddof": 0,
        "completed_turn4_raw_ra0_sha256": base._field_sha256(raw_ra0),
        "ordered_mean": mean, "population_standard_deviation": sigma,
        "zscore": zscore.tolist(), "zscore_sha256": base._field_sha256(zscore),
        "foreign_conditional_share_sha256": base._field_sha256(foreign),
        "turn5_portfolio_share_sha256": base._field_sha256(shares5),
        "rah_turn5": rah5.tolist(), "rah_turn5_sha256": base._field_sha256(rah5),
        "checks": turn5_checks,
    })

    next_states = []
    for i in range(31):
        state = dict(provinces[i])
        state.update({
            "Ct": float(batch.ct[i]), "At": float(batch.at[i]), "Bt": float(batch.bt[i]),
            "AtTax": float(batch.at_tax[i]), "convergent": True,
            "Lt_supply": float(migration.lt_supply[i]), "Kt_supply": float(private[i]),
            "rah": float(rah5[i]), "w": float(wages[i]), "it": float(monetary.it), "rb": float(monetary.rb),
            "Yt_1": float(provinces[i]["Yt"]), "Kt_prev": float(firms[i].Kt),
            "Lt_prev": float(firms[i].Lt), "Zt_1": float(provinces[i]["Zt"]),
            "pit_1": float(provinces[i]["pit"]), "GovInv": float(accounting.GovInv_residual_MU[i]),
        })
        state.update(firms[i].as_source_dict())
        next_states.append({
            "province_index": i, "province": PROVINCE_ORDER[i], "classification": TURN5_CLASSIFICATION,
            "raw_ra0_turn4": float(raw_ra0[i]), "firm_ra_used": float(used_ra[i]), "state": state,
        })
    base._write_json(output / "turn5_k1b_input_candidate.json", {
        "status": "PASS", "classification": TURN5_CLASSIFICATION,
        "raw_next_payoff_sha256": base._field_sha256(rah5),
        "k1b_portfolio_share_plan_sha256": base._field_sha256(shares5),
        "source_completed_turn4_raw_ra0_sha256": base._field_sha256(raw_ra0), "rows": next_states,
    })
    panel = write_cross_turn_panel(
        repository, output, states, next_states, household_rows, raw_ra0,
        mean, sigma, shares5, float(np.sum(accounting.GovInv_residual_MU)),
    )
    base._write_json(output / "turn4_one_turn_integration_receipt.json", {
        "status": "PASS", "frozen_turn4_share_sha256": base._field_sha256(shares),
        "origin_private_wealth_total": float(np.sum(wealth)),
        "destination_private_capital_total": float(np.sum(private)),
        "national_private_capital_residual": float(np.sum(private) - np.sum(wealth)),
        "GovInv_C1_total": float(np.sum(accounting.GovInv_residual_MU)),
        "labor_destination_total": float(np.sum(migration.lt_supply)),
        "raw_ra0_turn4_sha256": base._field_sha256(raw_ra0),
        "turn5_share_sha256": base._field_sha256(shares5), "turn5_rah_sha256": base._field_sha256(rah5),
        "wage_calls": ledger["composite_wage_batches"], "monetary_calls": ledger["monetary_assignments"],
        "fiscal_calls": ledger["fiscal_diagnostic_batches"], "fiscal_diagnostic": fiscal.__dict__,
        "checks": {**capital_checks, **c1_checks, **turn5_checks},
        "cross_turn_diagnostic_classification": panel["classification"],
    })
    return {
        "raw_ra0_turn4_sha256": base._field_sha256(raw_ra0), "turn5_share_sha256": base._field_sha256(shares5),
        "turn5_rah_sha256": base._field_sha256(rah5), "origin_private_wealth_total": float(np.sum(wealth)),
        "destination_private_capital_total": float(np.sum(private)), "national_private_capital_residual": float(np.sum(private) - np.sum(wealth)),
        "cross_turn_diagnostic_status": panel["status"],
    }


def finalize(repository: Path, output: Path, pre_hashes: dict[str, str], ledger: dict[str, Any], state: dict[str, Any], terminal: str, detail: dict[str, Any], started: float) -> str:
    post_hashes = base._task_hashes(repository)
    if post_hashes != pre_hashes:
        terminal = "BLOCKED__SCIENTIFIC_CODE_CHANGED_AFTER_FREEZE"
        detail = {"prior_detail": detail}
    task_ledger_check(ledger, state["relaxation"])
    ledger["wall_seconds"] = float(time.perf_counter() - started)
    ledger["terminal_verdict"] = terminal
    base._write_json(output / "scientific_ledger.json", ledger)
    write_relaxation(output, state)
    base._write_json(output / "reached_province_hjb_kfe_status.json", reached_province_status(output, terminal, detail))
    base._write_json(output / "post_execution_code_freeze.json", {"status": "PASS" if post_hashes == pre_hashes else "FAIL", "source_sha256_after": post_hashes, "matches_pre_execution_freeze": post_hashes == pre_hashes})
    base._write_json(output / "terminal_receipt.json", {
        "terminal_verdict": terminal, "detail": detail,
        "turn4_household_batch_run": ledger["authorized_k1b_turn4_household_batches"] == 1,
        "turn5_household_run": False, "k2": 0, "successor_published": False, "results_eligibility": False,
    })
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
        raise FailClosed("BLOCKED__K1B_TURN4_PREEXECUTION_GATE", {"preflight": gate, "focused": focused})
    base.TASK_RELATIVE = TASK_RELATIVE
    base.ENTERING_STATE_RELATIVE = ENTERING_RELATIVE
    started = time.perf_counter()
    ledger = base._new_ledger()
    ledger.update({
        "authorized_k1b_turn4_household_batches": 0,
        "frozen_k1b_turn4_quantity_allocations": 0,
        "completed_turn4_raw_ra0_vectors": 0,
        "deterministic_turn5_k1b_preparations": 0,
        "turn4_household_calls": 0,
        "fourth_outer_turns": 0,
        "turn5_household_calls": 0,
    })
    states, frozen_shares, entering = load_entering_and_shares(repository)
    pre_hashes = base._task_hashes(repository)
    core_hashes = base._scientific_code_hashes(repository)
    output.mkdir(parents=True, exist_ok=False)
    base._write_json(output / "authority_source_binding.json", {"status": "PASS", "task_id": TASK_ID, "baseline": BASELINE, "preflight": gate})
    base._write_json(output / "entering_state_and_share_plan_binding.json", entering)
    base._write_json(output / "focused_test_receipt.json", focused)
    base._write_json(output / "pre_execution_code_freeze.json", {"status": "PASS", "task_source_sha256_before": pre_hashes, "core_source_sha256_before": core_hashes})
    state = {"context": None, "relaxation": new_relaxation_ledger()}
    original_direct, original_helper = install_runtime_capture(output, state)
    try:
        native_grid = base.oracle.MatlabFaithfulHJBGrid(np.linspace(-2, 5, 20), np.linspace(0, 10, 20), np.array([0.8, 1.3]), np.array([[-1/3, 1/3], [1/3, -1/3]]))
        grid = CorrectedDiagnosticGrid(native_grid.b, native_grid.a, native_grid.z)
        native_params = base.oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
        results = []
        for index, province in enumerate(PROVINCE_ORDER):
            results.append(base._solve_province(repository, output, index, province, states[index], grid, native_grid, native_params, pre_hashes, core_hashes, ledger))
        if len(results) != 31:
            raise FailClosed("FAIL__K1B_TURN4_HOUSEHOLD_BATCH_INCOMPLETE", {"count": len(results)})
        ledger["household_batch_constructions"] += 1
        ledger["authorized_k1b_turn4_household_batches"] += 1
        ledger["turn4_household_calls"] += 1
        ledger["fourth_outer_turns"] += 1
        batch = PreFrozenHouseholdOutputBatch(
            ct=[row["aggregates"]["Ct"]["mass_form"] for row in results],
            household_lt=[row["aggregates"]["Lt"]["mass_form"] for row in results],
            at=[row["aggregates"]["At"]["mass_form"] for row in results],
            bt=[row["aggregates"]["Bt"]["mass_form"] for row in results],
            at_tax=[row["aggregates"]["AtTax"]["mass_form"] for row in results],
            converged=(True,) * 31,
            diagnostics=tuple({"checkpoint": row["checkpoint"], "B": row["B"], "D": row["D"]} for row in results),
        )
        household_rows = [{"province_index": i, "province": row["province"], "checkpoint": row["checkpoint"], "B": row["B"], "D": row["D"]} for i, row in enumerate(results)]
        base._write_json(output / "household_batch_receipt.json", {"status": "PASS", "province_count": 31, "rows": household_rows})
        integration = integrate_turn4(repository, output, states, batch, frozen_shares, ledger, household_rows)
        return finalize(repository, output, pre_hashes, ledger, state, PASS_TERMINAL, {"household_pass_count": 31, "integration_status": "PASS", **integration, "turn5_household_run": False}, started)
    except FailClosed as failure:
        return finalize(repository, output, pre_hashes, ledger, state, failure.terminal, failure.detail, started)
    except Exception as exc:
        return finalize(repository, output, pre_hashes, ledger, state, "FAIL__UNEXPECTED_K1B_TURN4_TASK_EXCEPTION__NO_SCIENTIFIC_RETRY", {"type": type(exc).__name__, "message": str(exc)}, started)
    finally:
        base._direct_update = original_direct
        base.monotonicity_preserving_relaxation = original_helper


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--focused-test-junit", type=Path, required=True)
    args = parser.parse_args(argv)
    print(execute(args.repository, args.focused_test_junit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
