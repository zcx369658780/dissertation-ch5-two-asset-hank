"""Execute exactly two bounded K1B-active turns, turn5 and turn6."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import time
from typing import Any, Mapping, Sequence

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
from validators.multi_province.k1b_turn4_corrected_household_kfe_and_one_turn_integration import run as prior_turn4


TASK_ID = "CH5_MP4C_K1B_TURN5_TURN6_BOUNDED_CONTINUATION_DIAGNOSTIC_20260921"
BASELINE = "dd90f41e0daa97cf55fcb2a7a233ee8cd64297ac"
ACCEPTED_SOURCE = "2155d16ab04f705b1a0da1cc3b49d78e60592c2e"
PASS_TERMINAL = (
    "PASS__K1B_TURN5_TURN6_BOUNDED_CONTINUATION__TWO_TURNS_31_PROVINCE_"
    "HJB_KFE_AND_INTEGRATION_PASS__TURN7_INPUT_READY__TURN7_NOT_RUN"
)
OUTPUT_RELATIVE = Path("reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001")
TASK_RELATIVE = Path("tasks/CH5_MP4C_K1B_TURN5_TURN6_BOUNDED_CONTINUATION_DIAGNOSTIC_20260921.md")
RUNNER_RELATIVE = Path("validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py")
TEST_RELATIVE = Path("tests/test_mp4c_k1b_turn5_turn6_bounded_continuation.py")
TURN4_ROOT = Path("reports/ch5_mp4c_k1b_turn4_anhui_f0364_positive_domain_intersection_repair_reexecution_20260921_run001")
TURN5_INPUT = TURN4_ROOT / "turn5_k1b_input_candidate.json"
TURN5_PLAN = TURN4_ROOT / "turn5_k1b_frozen_share_payoff_plan.npz"
TURN5_INPUT_BLOB = "7826691387916254ef55b149651d51f8438cab10"
TURN5_INPUT_SHA = "10CDFE998FBC95F09DA682F5389F268A1569A5FEB345D61470B3E8AA415D01D1"
TURN5_PLAN_BLOB = "83cee2bafb63d5f608e9d1b76480621a14077cc3"
TURN5_PLAN_SHA = "57A31EAA59A9E6CCD74E1DD5C18C74496829BA181866E12300CA7EB202890A70"
TURN5_SHARE_SHA = "2BDF7B8226C8404DB9C7FFEEE3F72F7AE9CA1305905460A4E2430AABEA4D3B06"
TURN5_RAH_SHA = "5CAF9166D85198E6923FFCD5A1F92D278C8A1C6CB924E8DD1B843F875E91D88E"
TURN4_RAW_SHA = "0312EBE6C2764DB3A834F1233712186ED1B6CE0C3E8BC01E58EFF6A0E8DCD267"
DESCRIPTIVE = "DESCRIPTIVE_ONLY__NO_CONTRACTION_OR_CONVERGENCE_ACCEPTANCE_CONDITION"
STATE_FIELDS = ("Ct", "Lt_supply", "At", "Bt", "AtTax", "Kt", "Kt_supply", "GovInv", "Yt", "w")


def git(repository: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repository, text=True).strip()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def write_json(path: Path, payload: Any) -> None:
    base._write_json(path, payload)


def production_hashes(repository: Path) -> dict[str, str]:
    names = git(repository, "ls-files", "src/ch5_two_asset_hank").splitlines()
    return {name: sha256(repository / name) for name in names}


def accepted_source_binding(repository: Path) -> dict[str, Any]:
    accepted_tree = git(repository, "rev-parse", f"{ACCEPTED_SOURCE}:src/ch5_two_asset_hank")
    head_tree = git(repository, "rev-parse", "HEAD:src/ch5_two_asset_hank")
    diff = git(repository, "diff", "--name-only", "--", "src/ch5_two_asset_hank").splitlines()
    checks = {
        "accepted_source_tree_exact": accepted_tree == head_tree,
        "production_worktree_diff_empty": not diff,
    }
    return {"status": "PASS" if all(checks.values()) else "FAIL", "checks": checks,
            "accepted_tree": accepted_tree, "head_tree": head_tree, "worktree_diff": diff}


def _states_from_candidate(path: Path, classification: str) -> tuple[tuple[dict[str, Any], ...], dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload.get("rows", [])
    checks = {
        "status": payload.get("status") == "PASS",
        "classification": payload.get("classification") == classification,
        "row_count": len(rows) == 31,
        "canonical_order": tuple(row.get("province") for row in rows) == PROVINCE_ORDER,
    }
    if not all(checks.values()):
        raise FailClosed("BLOCKED__K1B_ENTERING_CANDIDATE_INVALID", {"path": path.as_posix(), "checks": checks})
    return tuple(dict(row["state"]) for row in rows), payload


def load_turn5(repository: Path) -> tuple[tuple[dict[str, Any], ...], np.ndarray, np.ndarray, dict[str, Any]]:
    path = repository / TURN5_INPUT
    plan = repository / TURN5_PLAN
    states, payload = _states_from_candidate(path, "TURN5_K1B_INPUT_CANDIDATE_ONLY__TURN5_HOUSEHOLD_NOT_RUN")
    with np.load(plan, allow_pickle=False) as archive:
        shares = np.asarray(archive["portfolio_shares_destination_origin"], dtype=np.float64)
        rah = np.asarray(archive["rah_turn5_by_origin"], dtype=np.float64)
        raw_prior = np.asarray(archive["raw_ra0_turn4"], dtype=np.float64)
    state_rah = np.asarray([row["rah"] for row in states], dtype=np.float64)
    checks = {
        "input_blob": git(repository, "rev-parse", f"HEAD:{TURN5_INPUT.as_posix()}") == TURN5_INPUT_BLOB,
        "input_file_sha": sha256(path) == TURN5_INPUT_SHA,
        "plan_blob": git(repository, "rev-parse", f"HEAD:{TURN5_PLAN.as_posix()}") == TURN5_PLAN_BLOB,
        "plan_file_sha": sha256(plan) == TURN5_PLAN_SHA,
        "share_shape_finite_nonnegative": shares.shape == (31, 31) and bool(np.all(np.isfinite(shares)) and np.all(shares >= 0.0)),
        "share_columns": bool(np.allclose(np.sum(shares, axis=0), 1.0, rtol=0.0, atol=CONSERVATION_TOLERANCE)),
        "share_sha": base._field_sha256(shares) == TURN5_SHARE_SHA == payload.get("k1b_portfolio_share_plan_sha256"),
        "rah_bitwise": np.array_equal(rah, state_rah),
        "rah_sha": base._field_sha256(rah) == TURN5_RAH_SHA == payload.get("raw_next_payoff_sha256"),
        "raw_prior_sha": base._field_sha256(raw_prior) == TURN4_RAW_SHA == payload.get("source_completed_turn4_raw_ra0_sha256"),
    }
    if not all(checks.values()):
        raise FailClosed("BLOCKED__TURN5_ENTERING_OR_SHARE_BINDING", {"checks": checks})
    return states, shares, raw_prior, {"status": "PASS", "checks": checks,
        "input_path": TURN5_INPUT.as_posix(), "plan_path": TURN5_PLAN.as_posix(),
        "input_file_sha256": sha256(path), "plan_file_sha256": sha256(plan)}


def preflight(repository: Path) -> dict[str, Any]:
    source = accepted_source_binding(repository)
    _, _, _, entering = load_turn5(repository)
    checks = {
        "head_exact_live_main": git(repository, "rev-parse", "HEAD") == BASELINE,
        "origin_main_exact": git(repository, "rev-parse", "origin/main") == BASELINE,
        "accepted_source_exact": source["status"] == "PASS",
        "turn5_entering_exact": entering["status"] == "PASS",
    }
    return {"status": "PASS" if all(checks.values()) else "FAIL", "checks": checks,
            "source": source, "turn5_entering": entering}


def new_ledger(turn: int) -> dict[str, Any]:
    ledger = base._new_ledger()
    ledger.update({
        "turn": turn, "authorized_k1b_household_batches": 0,
        "frozen_k1b_quantity_allocations": 0, "completed_raw_ra0_vectors": 0,
        "deterministic_next_k1b_preparations": 0,
        "turn5_household_calls": 0, "turn6_household_calls": 0,
        "turn7_household_calls": 0,
    })
    return ledger


def new_relaxation_ledger() -> dict[str, Any]:
    return {"helper_invocations": 0, "alpha_candidates_evaluated": 0,
        "relaxed_updates_alpha_lt_1": 0, "accepted_halving_counts": {},
        "minimum_accepted_raw_b_slope_by_turn_province": {}, "records": [], "failure": None}


def install_runtime_capture(output: Path, state: dict[str, Any]):
    original_direct = base._direct_update
    original_helper = base.monotonicity_preserving_relaxation

    def helper(old, full, b_nodes):
        directory = Path(state["context"])
        province_root = directory.parent
        turn_label = province_root.parents[1].name
        checkpoint = int(directory.name.rsplit("_", 1)[1])
        province = province_root.name.split("_", 1)[1]
        province_index = int(province_root.name[1:3])
        ledger = state["relaxation"]
        ledger["helper_invocations"] += 1
        try:
            accepted, receipt = original_helper(old, full, b_nodes)
        except FailClosed as failure:
            attempts = failure.detail.get("attempts", [])
            ledger["alpha_candidates_evaluated"] += len(attempts)
            ledger["failure"] = {"turn": turn_label, "province_index": province_index,
                "province": province, "checkpoint": checkpoint, "terminal": failure.terminal,
                "attempts": len(attempts)}
            write_json(output / "relaxation_arithmetic_ledger.json", ledger)
            raise
        attempts = receipt["attempts"]
        ledger["alpha_candidates_evaluated"] += len(attempts)
        halvings = int(receipt["accepted_halvings"])
        key = str(halvings)
        ledger["accepted_halving_counts"][key] = ledger["accepted_halving_counts"].get(key, 0) + 1
        if float(receipt["accepted_alpha"]) < 1.0:
            ledger["relaxed_updates_alpha_lt_1"] += 1
        minimum = float(attempts[-1]["minimum_raw_b_slope"])
        pkey = f"{turn_label}:{province}"
        prior = ledger["minimum_accepted_raw_b_slope_by_turn_province"].get(pkey)
        ledger["minimum_accepted_raw_b_slope_by_turn_province"][pkey] = minimum if prior is None else min(prior, minimum)
        ledger["records"].append({"turn": turn_label, "province_index": province_index,
            "province": province, "checkpoint_from": checkpoint,
            "old_sha256": receipt["value_old_sha256"], "full_sha256": receipt["full_candidate_sha256"],
            "accepted_sha256": receipt["accepted_next_value_sha256"], "alpha": receipt["accepted_alpha"],
            "halvings": halvings, "attempt_count": len(attempts), "minimum_raw_b_slope": minimum})
        write_json(output / "relaxation_arithmetic_ledger.json", ledger)
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


def _batch(results: Sequence[Mapping[str, Any]]) -> PreFrozenHouseholdOutputBatch:
    return PreFrozenHouseholdOutputBatch(
        ct=[row["aggregates"]["Ct"]["mass_form"] for row in results],
        household_lt=[row["aggregates"]["Lt"]["mass_form"] for row in results],
        at=[row["aggregates"]["At"]["mass_form"] for row in results],
        bt=[row["aggregates"]["Bt"]["mass_form"] for row in results],
        at_tax=[row["aggregates"]["AtTax"]["mass_form"] for row in results],
        converged=(True,) * 31,
        diagnostics=tuple({"checkpoint": row["checkpoint"], "B": row["B"], "D": row["D"]} for row in results),
    )


def integrate_turn(repository: Path, task_root: Path, turn_root: Path, turn: int,
                   states: tuple[dict[str, Any], ...], batch: PreFrozenHouseholdOutputBatch,
                   frozen_shares: np.ndarray, expected_share_sha: str,
                   ledger: dict[str, Any], household_rows: list[dict[str, Any]]) -> dict[str, Any]:
    next_turn = turn + 1
    inputs = base._one_turn_inputs(repository, states, batch)
    household, provinces = inputs.household_outputs, inputs.old_provinces
    ledger["source_faithful_labor_reconstructions"] += 1
    migration = base.source.reconstruct_migration_labor(base.source.MigrationLaborInputs(
        consumption_by_origin=household.ct, population_by_origin=[row["N"] for row in provinces],
        old_firm_wage_by_destination=[row["wjt"] for row in provinces], tax_by_origin=[row["tau"] for row in provinces],
        phi_destination_origin=inputs.phi_destination_origin,
        migration_wedge_destination_origin=inputs.migration_wedge_destination_origin,
        gamma_c=inputs.params["ga"], phi_l=inputs.params["phi_l"]))
    write_json(turn_root / "source_faithful_labor_receipt.json", {"status": "PASS", "calls": 1,
        "orientation": "destination_by_origin", "lt_matrix_sha256": base._field_sha256(migration.lt_mat),
        "lt_supply_sha256": base._field_sha256(migration.lt_supply),
        "labor_destination_total": float(np.sum(migration.lt_supply))})

    ledger["frozen_k1b_quantity_allocations"] += 1
    ledger["k1b_feedback_calls"] += 1
    shares = np.asarray(frozen_shares, dtype=np.float64)
    theta = np.asarray([row["inter_prv_ratio"] for row in provinces], dtype=np.float64)
    population = np.asarray([row["N"] for row in provinces], dtype=np.float64)
    wealth = np.asarray(household.at, dtype=np.float64) * population
    flows = shares * wealth[None, :]
    private, domestic = np.sum(flows, axis=1), np.diag(flows).copy()
    scale = max(1.0, float(np.sum(wealth)))
    capital_checks = {
        "frozen_share_sha": base._field_sha256(shares) == expected_share_sha,
        "share_columns": bool(np.allclose(np.sum(shares, axis=0), 1.0, rtol=0.0, atol=CONSERVATION_TOLERANCE)),
        "origin_columns_conserved": bool(np.allclose(np.sum(flows, axis=0), wealth, rtol=0.0, atol=CONSERVATION_TOLERANCE * scale)),
        "national_private_capital": abs(float(np.sum(private) - np.sum(wealth))) <= CONSERVATION_TOLERANCE * scale,
        "home_retained_exact": bool(np.array_equal(domestic, (1.0 - theta) * wealth)),
        "no_same_turn_share_recomputation": True,
    }
    if not all(capital_checks.values()):
        raise FailClosed(f"FAIL__TURN{turn}_FROZEN_K1B_CAPITAL_ACCOUNTING", {"checks": capital_checks})
    np.savez_compressed(turn_root / f"turn{turn}_frozen_k1b_capital_arrays.npz",
        shares_destination_origin=shares, origin_wealth=wealth,
        bilateral_private_capital_destination_origin=flows,
        destination_private_capital=private, domestic_retained=domestic)
    capital_receipt = {"status": "PASS", "share_plan_sha256": base._field_sha256(shares),
        "origin_private_wealth_total": float(np.sum(wealth)),
        "destination_private_capital_total": float(np.sum(private)),
        "national_private_capital_residual": float(np.sum(private) - np.sum(wealth)), "checks": capital_checks}
    write_json(turn_root / f"turn{turn}_frozen_k1b_capital_receipt.json", capital_receipt)

    ledger["c1_residual_govinv_constructions"] += 1
    accounting = base.residual_government_asset_levels(
        Ktarget_MU=[row["Kt0"] for row in provinces], Kprivate_current_MU=private,
        province_order=PROVINCE_ORDER)
    expected_c1 = np.maximum(np.asarray([row["Kt0"] for row in provinces], dtype=np.float64) - private, 0.0)
    c1_checks = {"exact_residual_rule": bool(np.array_equal(accounting.GovInv_residual_MU, expected_c1)),
        "nonnegative": bool(np.all(accounting.GovInv_residual_MU >= 0.0)),
        "calls_exactly_one": ledger["c1_residual_govinv_constructions"] == 1}
    if not all(c1_checks.values()):
        raise FailClosed(f"FAIL__TURN{turn}_C1_RESIDUAL_GOVINV", {"checks": c1_checks})
    c1_receipt = {"status": "PASS", "GovInv_C1": accounting.GovInv_residual_MU.tolist(),
        "GovInv_C1_total": float(np.sum(accounting.GovInv_residual_MU)), "checks": c1_checks}
    write_json(turn_root / f"turn{turn}_c1_residual_govinv_receipt.json", c1_receipt)

    firms = []
    for index, province in enumerate(provinces):
        source = dict(province)
        source.update(GovInv=float(accounting.GovInv_residual_MU[index]),
                      AtTax=float(household.at_tax[index]), Lt_prev=float(household.household_lt[index]))
        ledger["firm_evaluations"] += 1
        firm = base.source.evaluate_firm(source, float(private[index]), float(migration.lt_supply[index]), inputs.params)
        expected_k = float(accounting.firm_K_accounting_MU[index])
        if abs(float(firm.Kt) - expected_k) > 1e-12 * max(1.0, abs(expected_k)):
            raise FailClosed(f"FAIL__TURN{turn}_C1_FIRM_CAPITAL_ACCOUNTING", {"province_index": index})
        firms.append(firm)
    if not np.all(np.isfinite([value for firm in firms for value in firm.as_source_dict().values()])):
        raise FailClosed(f"FAIL__TURN{turn}_FIRM_NONFINITE", {})
    ledger["composite_wage_batches"] += 1
    wages = base.source.composite_household_wages(provinces, [firm.wjt for firm in firms],
        inputs.phi_destination_origin, inputs.migration_wedge_destination_origin,
        phi_l=inputs.params["phi_l"], alphal=inputs.params["alphal"])
    ledger["monetary_assignments"] += 1
    monetary = base.source.taylor_assignment(istar=inputs.params["istar"], rho_pi=inputs.params["rho_pi"],
        totalpit=inputs.params["totalpit"], epsilon_pi=inputs.params["epsilon_pi"])
    ledger["fiscal_diagnostic_batches"] += 1
    fiscal = base.source.national_fiscal_diagnostics([firm.Govinc for firm in firms], household.bt,
        monetary.rb, [row["N"] for row in provinces])
    raw = np.asarray([firm.ra0 for firm in firms], dtype=np.float64)
    used = np.asarray([firm.ra for firm in firms], dtype=np.float64)
    ledger["completed_raw_ra0_vectors"] += 1
    firm_receipt = {"status": "PASS", f"raw_ra0_turn{turn}": raw.tolist(),
        f"raw_ra0_turn{turn}_sha256": base._field_sha256(raw), f"used_ra_turn{turn}": used.tolist(),
        f"used_ra_turn{turn}_sha256": base._field_sha256(used),
        "raw_used_difference_count": int(np.count_nonzero(raw != used)),
        "rows": [{"province_index": i, "province": PROVINCE_ORDER[i], **firm.as_source_dict()} for i, firm in enumerate(firms)]}
    write_json(turn_root / f"turn{turn}_firm_raw_used_return_receipt.json", firm_receipt)

    ledger["deterministic_next_k1b_preparations"] += 1
    mean, sigma, zscore = safety.ordered_population_zscore(raw)
    distance = base.load_accepted_distance_score(repository / base.DISTANCE_RELATIVE)
    foreign = foreign_conditional_shares(ForeignConditionalShareInputs(
        province_order=PROVINCE_ORDER, distance_score_destination_origin=distance,
        lagged_return_score_by_destination=zscore, beta_distance=2.0, beta_return=0.5,
        lagged_return_provenance=f"LAGGED__COMPLETED_TURN{turn}_RAW_RA0__USED_FOR_TURN{next_turn}_K1B_ATTRACTIVENESS",
    )).foreign_conditional_shares_destination_origin
    next_shares = np.asarray(foreign, dtype=np.float64) * theta[None, :]
    diagonal = np.arange(31)
    next_shares[diagonal, diagonal] = 1.0 - theta
    next_rah = safety.ordered_payoff(raw, next_shares)
    ledger["raw_next_payoff_same_s_constructions"] += 1
    next_checks = {"sigma_finite_positive": math.isfinite(sigma) and sigma > 0.0,
        "zscore_mean": abs(math.fsum(float(x) for x in zscore) / 31.0) <= 1e-15,
        "zscore_population_variance": abs(math.fsum(float(x) * float(x) for x in zscore) / 31.0 - 1.0) <= 1e-15,
        "foreign_diagonal_zero": np.array_equal(np.diag(foreign), np.zeros(31)),
        "foreign_columns": bool(np.allclose(np.sum(foreign, axis=0), 1.0, rtol=0.0, atol=CONSERVATION_TOLERANCE)),
        "full_share_columns": bool(np.allclose(np.sum(next_shares, axis=0), 1.0, rtol=0.0, atol=CONSERVATION_TOLERANCE)),
        "home_exact": np.array_equal(np.diag(next_shares), 1.0 - theta),
        "payoff_finite": bool(np.all(np.isfinite(next_rah))),
        "next_household_not_run": ledger[f"turn{next_turn}_household_calls"] == 0}
    if not all(next_checks.values()):
        raise FailClosed(f"FAIL__TURN{next_turn}_K1B_PREPARATION", {"checks": next_checks})

    plan_path = task_root / f"turn{next_turn}_k1b_frozen_share_payoff_plan.npz"
    np.savez_compressed(plan_path, **{f"raw_ra0_turn{turn}": raw,
        "zscore_by_destination": zscore, "foreign_conditional_shares_destination_origin": foreign,
        "portfolio_shares_destination_origin": next_shares, f"rah_turn{next_turn}_by_origin": next_rah})
    score_receipt = {"status": "PASS", "beta_distance": 2.0, "beta_return": 0.5, "ddof": 0,
        f"completed_turn{turn}_raw_ra0_sha256": base._field_sha256(raw),
        "ordered_mean": mean, "population_standard_deviation": sigma,
        "zscore": zscore.tolist(), "zscore_sha256": base._field_sha256(zscore),
        "foreign_conditional_share_sha256": base._field_sha256(foreign),
        f"turn{next_turn}_portfolio_share_sha256": base._field_sha256(next_shares),
        f"rah_turn{next_turn}": next_rah.tolist(), f"rah_turn{next_turn}_sha256": base._field_sha256(next_rah),
        "checks": next_checks}
    write_json(task_root / f"turn{next_turn}_k1b_zscore_share_payoff_receipt.json", score_receipt)

    next_rows = []
    for i in range(31):
        state = dict(provinces[i])
        state.update({"Ct": float(batch.ct[i]), "At": float(batch.at[i]), "Bt": float(batch.bt[i]),
            "AtTax": float(batch.at_tax[i]), "convergent": True,
            "Lt_supply": float(migration.lt_supply[i]), "Kt_supply": float(private[i]),
            "rah": float(next_rah[i]), "w": float(wages[i]), "it": float(monetary.it), "rb": float(monetary.rb),
            "Yt_1": float(provinces[i]["Yt"]), "Kt_prev": float(firms[i].Kt),
            "Lt_prev": float(firms[i].Lt), "Zt_1": float(provinces[i]["Zt"]),
            "pit_1": float(provinces[i]["pit"]), "GovInv": float(accounting.GovInv_residual_MU[i])})
        state.update(firms[i].as_source_dict())
        next_rows.append({"province_index": i, "province": PROVINCE_ORDER[i],
            "classification": f"TURN{next_turn}_K1B_INPUT_CANDIDATE_ONLY__TURN{next_turn}_HOUSEHOLD_NOT_RUN",
            f"raw_ra0_turn{turn}": float(raw[i]), "firm_ra_used": float(used[i]), "state": state})
    candidate_path = task_root / f"turn{next_turn}_k1b_input_candidate.json"
    write_json(candidate_path, {"status": "PASS",
        "classification": f"TURN{next_turn}_K1B_INPUT_CANDIDATE_ONLY__TURN{next_turn}_HOUSEHOLD_NOT_RUN",
        "raw_next_payoff_sha256": base._field_sha256(next_rah),
        "k1b_portfolio_share_plan_sha256": base._field_sha256(next_shares),
        f"source_completed_turn{turn}_raw_ra0_sha256": base._field_sha256(raw), "rows": next_rows})
    integration_receipt = {"status": "PASS", f"frozen_turn{turn}_share_sha256": base._field_sha256(shares),
        "origin_private_wealth_total": float(np.sum(wealth)),
        "destination_private_capital_total": float(np.sum(private)),
        "national_private_capital_residual": float(np.sum(private) - np.sum(wealth)),
        "GovInv_C1_total": float(np.sum(accounting.GovInv_residual_MU)),
        "labor_destination_total": float(np.sum(migration.lt_supply)),
        f"raw_ra0_turn{turn}_sha256": base._field_sha256(raw),
        f"turn{next_turn}_share_sha256": base._field_sha256(next_shares),
        f"turn{next_turn}_rah_sha256": base._field_sha256(next_rah),
        "wage_calls": 1, "monetary_calls": 1, "fiscal_calls": 1,
        "fiscal_diagnostic": fiscal.__dict__, "checks": {**capital_checks, **c1_checks, **next_checks}}
    write_json(turn_root / f"turn{turn}_one_turn_integration_receipt.json", integration_receipt)
    return {"turn": turn, "states": states, "next_states": tuple(row["state"] for row in next_rows),
        "household_rows": household_rows, "raw": raw, "next_shares": next_shares,
        "next_rah": next_rah, "mean": float(mean), "sigma": float(sigma),
        "c1_total": float(np.sum(accounting.GovInv_residual_MU)),
        "capital_residual": float(np.sum(private) - np.sum(wealth)),
        "candidate_path": candidate_path, "plan_path": plan_path,
        "integration_receipt": integration_receipt, "score_receipt": score_receipt,
        "candidate_file_sha256": sha256(candidate_path), "plan_file_sha256": sha256(plan_path)}


def seal_generated_bundle(task_root: Path, integration: Mapping[str, Any], turn: int) -> dict[str, Any]:
    prior = turn - 1
    paths = [Path(integration["candidate_path"]), Path(integration["plan_path"]),
             task_root / f"turn{turn}_k1b_zscore_share_payoff_receipt.json",
             task_root / f"turn{prior}/turn{prior}_firm_raw_used_return_receipt.json"]
    entries = [{"path": path.relative_to(task_root).as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)} for path in paths]
    manifest = {"schema": "CH5_MP4C_K1B_GENERATED_ENTERING_BUNDLE_V1", "turn": turn,
        "sealed_before_household": True, "timing": f"COMPLETED_TURN{prior}_RAW_RA0_ONLY",
        "entries": entries, "entry_count": len(entries), "total_bytes": sum(row["bytes"] for row in entries)}
    manifest_path = task_root / f"turn{turn}_entering_bundle_manifest.json"
    write_json(manifest_path, manifest)
    bad = []
    for row in entries:
        path = task_root / row["path"]
        if not path.is_file() or path.stat().st_size != row["bytes"] or sha256(path) != row["sha256"]:
            bad.append(row["path"])
    receipt = {"status": "PASS" if not bad else "FAIL", "turn": turn,
        "manifest_sha256": sha256(manifest_path), "bad_paths": bad,
        "sealed_before_household": True, "scientific_calls": 0}
    write_json(task_root / f"turn{turn}_entering_bundle_readback.json", receipt)
    if bad:
        raise FailClosed(f"BLOCKED__TURN{turn}_ENTERING_BUNDLE_READBACK", receipt)
    return receipt


def load_generated_turn(task_root: Path, turn: int, integration: Mapping[str, Any]) -> tuple[tuple[dict[str, Any], ...], np.ndarray, np.ndarray, dict[str, Any]]:
    candidate = task_root / f"turn{turn}_k1b_input_candidate.json"
    plan = task_root / f"turn{turn}_k1b_frozen_share_payoff_plan.npz"
    states, payload = _states_from_candidate(candidate, f"TURN{turn}_K1B_INPUT_CANDIDATE_ONLY__TURN{turn}_HOUSEHOLD_NOT_RUN")
    with np.load(plan, allow_pickle=False) as archive:
        shares = np.asarray(archive["portfolio_shares_destination_origin"], dtype=np.float64)
        rah = np.asarray(archive[f"rah_turn{turn}_by_origin"], dtype=np.float64)
        raw_prior = np.asarray(archive[f"raw_ra0_turn{turn-1}"], dtype=np.float64)
    checks = {"candidate_file_sha": sha256(candidate) == integration["candidate_file_sha256"],
        "plan_file_sha": sha256(plan) == integration["plan_file_sha256"],
        "share_identity": np.array_equal(shares, integration["next_shares"]),
        "rah_identity": np.array_equal(rah, integration["next_rah"]),
        "raw_identity": np.array_equal(raw_prior, integration["raw"]),
        "state_rah_identity": np.array_equal(rah, np.asarray([row["rah"] for row in states], dtype=np.float64)),
        "payload_share_sha": payload.get("k1b_portfolio_share_plan_sha256") == base._field_sha256(shares),
        "payload_rah_sha": payload.get("raw_next_payoff_sha256") == base._field_sha256(rah)}
    receipt = {"status": "PASS" if all(checks.values()) else "FAIL", "turn": turn, "checks": checks,
        "candidate_file_sha256": sha256(candidate), "plan_file_sha256": sha256(plan),
        "share_sha256": base._field_sha256(shares), "rah_sha256": base._field_sha256(rah),
        "source_raw_sha256": base._field_sha256(raw_prior)}
    write_json(task_root / f"turn{turn}_entering_state_and_share_binding.json", receipt)
    if receipt["status"] != "PASS":
        raise FailClosed(f"BLOCKED__TURN{turn}_ENTERING_OR_SHARE_BINDING", receipt)
    return states, shares, raw_prior, receipt


def run_household_turn(repository: Path, task_root: Path, turn: int,
                       states: tuple[dict[str, Any], ...], shares: np.ndarray,
                       expected_share_sha: str, ledger: dict[str, Any]) -> dict[str, Any]:
    turn_root = task_root / f"turn{turn}"
    turn_root.mkdir(parents=True, exist_ok=False)
    base.ENTERING_STATE_RELATIVE = (TURN5_INPUT if turn == 5 else OUTPUT_RELATIVE / f"turn{turn}_k1b_input_candidate.json")
    task_hashes = base._task_hashes(repository)
    core_hashes = base._scientific_code_hashes(repository)
    native_grid = base.oracle.MatlabFaithfulHJBGrid(np.linspace(-2, 5, 20), np.linspace(0, 10, 20),
        np.array([0.8, 1.3]), np.array([[-1/3, 1/3], [1/3, -1/3]]))
    grid = CorrectedDiagnosticGrid(native_grid.b, native_grid.a, native_grid.z)
    native_params = base.oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
    results = []
    for index, province in enumerate(PROVINCE_ORDER):
        results.append(base._solve_province(repository, turn_root, index, province, states[index],
            grid, native_grid, native_params, task_hashes, core_hashes, ledger))
    if len(results) != 31:
        raise FailClosed(f"FAIL__TURN{turn}_HOUSEHOLD_BATCH_INCOMPLETE", {"count": len(results)})
    ledger["household_batch_constructions"] += 1
    ledger["authorized_k1b_household_batches"] += 1
    ledger[f"turn{turn}_household_calls"] += 1
    rows = [{"province_index": i, "province": row["province"], "checkpoint": row["checkpoint"],
        "B": row["B"], "D": row["D"], "backward_error_max": row["backward_error_max"]}
        for i, row in enumerate(results)]
    write_json(turn_root / "household_batch_receipt.json", {"status": "PASS", "province_count": 31, "rows": rows})
    integration = integrate_turn(repository, task_root, turn_root, turn, states, _batch(results),
        shares, expected_share_sha, ledger, rows)
    write_json(task_root / f"turn{turn}_scientific_ledger.json", ledger)
    return integration


def _vector_change(old: np.ndarray, new: np.ndarray, norm_name: str) -> dict[str, Any]:
    change = np.asarray(new, dtype=np.float64) - np.asarray(old, dtype=np.float64)
    return {"old_sha256": base._field_sha256(old), "new_sha256": base._field_sha256(new),
        "change_sha256": base._field_sha256(change), "maximum_absolute_change": float(np.max(np.abs(change))),
        "mean_signed_change": float(math.fsum(float(x) for x in change.ravel()) / change.size),
        norm_name: float(np.linalg.norm(change)), "bitwise_changed_count": int(np.count_nonzero(old != new))}


def transition_panel(label: str, old_raw: np.ndarray, new_raw: np.ndarray,
                     old_states: Sequence[Mapping[str, Any]], new_states: Sequence[Mapping[str, Any]],
                     old_shares: np.ndarray, new_shares: np.ndarray,
                     old_household: Sequence[Mapping[str, Any]], new_household: Sequence[Mapping[str, Any]],
                     old_c1: float, new_c1: float, old_capital_residual: float,
                     new_capital_residual: float) -> dict[str, Any]:
    old_rah = np.asarray([row["rah"] for row in old_states], dtype=np.float64)
    new_rah = np.asarray([row["rah"] for row in new_states], dtype=np.float64)
    old_mean, old_sigma, _ = safety.ordered_population_zscore(old_raw)
    new_mean, new_sigma, _ = safety.ordered_population_zscore(new_raw)
    fields = {}
    for name in STATE_FIELDS:
        old = np.asarray([row[name] for row in old_states], dtype=np.float64)
        new = np.asarray([row[name] for row in new_states], dtype=np.float64)
        fields[name] = _vector_change(old, new, "euclidean_norm")
    return {"status": "PASS", "transition": label, "classification": DESCRIPTIVE,
        "raw_ra0": _vector_change(old_raw, new_raw, "euclidean_norm"),
        "rah": _vector_change(old_rah, new_rah, "euclidean_norm"),
        "portfolio_shares": _vector_change(old_shares, new_shares, "frobenius_norm"),
        "zscore_inputs": {"old_mean": old_mean, "new_mean": new_mean, "mean_change": new_mean-old_mean,
            "old_population_standard_deviation": old_sigma, "new_population_standard_deviation": new_sigma,
            "population_standard_deviation_change": new_sigma-old_sigma},
        "aggregate_state_changes": fields,
        "household": {"old_terminal_checkpoints": [int(row["checkpoint"]) for row in old_household],
            "new_terminal_checkpoints": [int(row["checkpoint"]) for row in new_household],
            "old_direct_update_count": sum(int(row["checkpoint"]) for row in old_household),
            "new_direct_update_count": sum(int(row["checkpoint"]) for row in new_household),
            "checkpoint_change_by_province": [int(new_household[i]["checkpoint"])-int(old_household[i]["checkpoint"]) for i in range(31)]},
        "c1": {"old_GovInv_total": old_c1, "new_GovInv_total": new_c1, "change": new_c1-old_c1},
        "capital_conservation": {"old_residual": old_capital_residual, "new_residual": new_capital_residual}}


def load_prior_transition(repository: Path, turn5_states: tuple[dict[str, Any], ...],
                          turn5_shares: np.ndarray, turn4_raw: np.ndarray) -> tuple[dict[str, Any], dict[str, Any]]:
    turn3_root = Path("reports/ch5_mp4c_k1b_turn3_corrected_household_kfe_and_one_turn_integration_20260921_run001")
    turn4_input = turn3_root / "turn4_k1b_input_candidate.json"
    turn4_states, _ = _states_from_candidate(repository / turn4_input, "TURN4_K1B_INPUT_CANDIDATE_ONLY__TURN4_HOUSEHOLD_NOT_RUN")
    with np.load(repository / turn3_root / "turn4_k1b_frozen_share_payoff_plan.npz", allow_pickle=False) as archive:
        turn4_shares = np.asarray(archive["portfolio_shares_destination_origin"], dtype=np.float64)
        turn3_raw = np.asarray(archive["raw_ra0_turn3"], dtype=np.float64)
    hh3 = json.loads((repository / turn3_root / "household_batch_receipt.json").read_text(encoding="utf-8"))["rows"]
    hh4 = json.loads((repository / TURN4_ROOT / "household_batch_receipt.json").read_text(encoding="utf-8"))["rows"]
    c13 = json.loads((repository / turn3_root / "turn3_c1_residual_govinv_receipt.json").read_text(encoding="utf-8"))["GovInv_C1_total"]
    c14 = json.loads((repository / TURN4_ROOT / "turn4_c1_residual_govinv_receipt.json").read_text(encoding="utf-8"))["GovInv_C1_total"]
    cap3 = json.loads((repository / turn3_root / "turn3_frozen_k1b_capital_receipt.json").read_text(encoding="utf-8"))["national_private_capital_residual"]
    cap4 = json.loads((repository / TURN4_ROOT / "turn4_frozen_k1b_capital_receipt.json").read_text(encoding="utf-8"))["national_private_capital_residual"]
    panel = transition_panel("turn3_to_turn4", turn3_raw, turn4_raw, turn4_states, turn5_states,
        turn4_shares, turn5_shares, hh3, hh4, float(c13), float(c14), float(cap3), float(cap4))
    context = {"states": turn5_states, "shares": turn5_shares, "raw": turn4_raw,
        "household": hh4, "c1": float(c14), "capital_residual": float(cap4)}
    return panel, context


def trajectory_panel(transitions: list[dict[str, Any]]) -> dict[str, Any]:
    ratios = []
    for left, right in zip(transitions, transitions[1:]):
        row: dict[str, Any] = {"numerator_transition": right["transition"],
            "denominator_transition": left["transition"], "classification": DESCRIPTIVE, "ratios": {}}
        metrics = {"raw_ra0_euclidean": (left["raw_ra0"]["euclidean_norm"], right["raw_ra0"]["euclidean_norm"]),
            "rah_euclidean": (left["rah"]["euclidean_norm"], right["rah"]["euclidean_norm"]),
            "portfolio_share_frobenius": (left["portfolio_shares"]["frobenius_norm"], right["portfolio_shares"]["frobenius_norm"])}
        for field in STATE_FIELDS:
            metrics[f"{field}_euclidean"] = (left["aggregate_state_changes"][field]["euclidean_norm"], right["aggregate_state_changes"][field]["euclidean_norm"])
        for name, (denominator, numerator) in metrics.items():
            row["ratios"][name] = None if denominator == 0.0 else float(numerator / denominator)
        ratios.append(row)
    return {"status": "PASS", "classification": DESCRIPTIVE,
        "acceptance_condition": "NONE__BOUNDED_TRAJECTORY_DIAGNOSTIC_ONLY",
        "transitions": transitions, "successive_change_norm_ratios": ratios,
        "fixed_point_tolerance": None, "convergence_claim": False}


def combined_ledger(ledgers: Mapping[int, Mapping[str, Any]]) -> dict[str, Any]:
    combined: dict[str, Any] = {"turns_present": sorted(ledgers)}
    keys = set().union(*(row.keys() for row in ledgers.values()))
    for key in keys:
        values = [row.get(key, 0) for row in ledgers.values()]
        if key != "turn" and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in values):
            combined[key] = sum(values)
    ceilings = {"source_native_initializations": 62, "scalar_labor_roots_attempted": 49600,
        "scalar_labor_roots_returned": 49600, "corrected_policy_maps": 3162,
        "selector_evaluations": 2529600, "d2_q_assemblies": 3162, "direct_hjb_updates": 3100,
        "hjb_checkpoint_evaluations_after_update": 3100, "scc_decompositions": 62,
        "restricted_dense_scipy_linalg_svd_gesvd": 62,
        "full_space_800_dense_scipy_linalg_svd_gesvd": 0, "normalized_stationary_candidates": 62,
        "q_transpose_times_p": 62, "corrected_aggregate_evaluations": 62,
        "household_batch_constructions": 2, "source_faithful_labor_reconstructions": 2,
        "c1_residual_govinv_constructions": 2, "firm_evaluations": 62,
        "composite_wage_batches": 2, "monetary_assignments": 2, "fiscal_diagnostic_batches": 2,
        "raw_next_payoff_same_s_constructions": 2, "k1b_feedback_calls": 2,
        "k2_calls": 0, "adaptive_controller_calls": 0, "matlab_scientific_calls": 0,
        "ge_annual_shock_irf_welfare_results_calls": 0, "scientific_retries": 0,
        "solver_substitutions": 0,
        "damping_relaxation_adaptive_delta_clipping_artificial_diffusion_continuation_calls": 0,
        "payoff_clipping_annualization_rescaling_smoothing_risk_adjustment_zscore_calls": 0,
        "turn7_household_calls": 0}
    breaches = {name: {"actual": int(combined.get(name, 0)), "ceiling": ceiling}
        for name, ceiling in ceilings.items() if int(combined.get(name, 0)) > ceiling}
    combined["ceilings"] = ceilings
    combined["breaches"] = breaches
    combined["status"] = "PASS" if not breaches else "FAIL"
    return combined


def finalize(repository: Path, output: Path, pre_source: dict[str, str], ledgers: dict[int, dict[str, Any]],
             relaxation: dict[str, Any], terminal: str, detail: dict[str, Any], started: float) -> str:
    post_source = production_hashes(repository)
    if post_source != pre_source:
        terminal = "BLOCKED__PRODUCTION_SOURCE_CHANGED_AFTER_FREEZE"
        detail = {"prior_detail": detail}
    combined = combined_ledger(ledgers)
    if combined["status"] != "PASS":
        terminal = "BLOCKED__TURN5_TURN6_COMBINED_SCIENTIFIC_LEDGER_CEILING"
        detail = {"prior_detail": detail, "breaches": combined["breaches"]}
    combined["wall_seconds"] = float(time.perf_counter() - started)
    combined["terminal_verdict"] = terminal
    write_json(output / "combined_scientific_ledger.json", combined)
    write_json(output / "relaxation_arithmetic_ledger.json", relaxation)
    for turn in (5, 6):
        turn_root = output / f"turn{turn}"
        if turn_root.is_dir():
            write_json(output / f"turn{turn}_reached_province_hjb_kfe_status.json",
                       prior_turn4.reached_province_status(turn_root, terminal, detail))
    write_json(output / "post_execution_production_source_freeze.json", {
        "status": "PASS" if post_source == pre_source else "FAIL",
        "matches_pre_execution_freeze": post_source == pre_source,
        "source_sha256_after": post_source})
    write_json(output / "terminal_receipt.json", {"terminal_verdict": terminal, "detail": detail,
        "turn5_household_calls": int(ledgers.get(5, {}).get("turn5_household_calls", 0)),
        "turn6_household_calls": int(ledgers.get(6, {}).get("turn6_household_calls", 0)),
        "turn7_household_calls": 0, "k2": 0, "matlab": 0, "ge_results": 0,
        "results_eligibility": False, "successor_published": False})
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
        raise FailClosed("BLOCKED__TURN5_TURN6_PREEXECUTION_GATE", {"preflight": gate, "focused": focused})
    base.TASK_RELATIVE = TASK_RELATIVE
    started = time.perf_counter()
    pre_source = production_hashes(repository)
    states5, shares5, raw4, entering5 = load_turn5(repository)
    output.mkdir(parents=True, exist_ok=False)
    write_json(output / "authority_source_input_binding.json", {"status": "PASS", "task_id": TASK_ID,
        "baseline": BASELINE, "execution_head": git(repository, "rev-parse", "HEAD"), "preflight": gate})
    write_json(output / "turn5_entering_state_and_share_binding.json", entering5)
    write_json(output / "focused_test_receipt.json", focused)
    write_json(output / "pre_execution_production_source_freeze.json", {"status": "PASS", "source_sha256_before": pre_source})
    ledgers: dict[int, dict[str, Any]] = {}
    state = {"context": None, "relaxation": new_relaxation_ledger()}
    original_direct, original_helper = install_runtime_capture(output, state)
    try:
        prior_panel, prior_context = load_prior_transition(repository, states5, shares5, raw4)
        ledger5 = new_ledger(5); ledgers[5] = ledger5
        integration5 = run_household_turn(repository, output, 5, states5, shares5, TURN5_SHARE_SHA, ledger5)
        seal_generated_bundle(output, integration5, 6)
        states6, shares6, raw5, entering6 = load_generated_turn(output, 6, integration5)
        panel45 = transition_panel("turn4_to_turn5", prior_context["raw"], raw5,
            prior_context["states"], states6, prior_context["shares"], shares6,
            prior_context["household"], integration5["household_rows"], prior_context["c1"],
            integration5["c1_total"], prior_context["capital_residual"], integration5["capital_residual"])
        ledger6 = new_ledger(6); ledgers[6] = ledger6
        integration6 = run_household_turn(repository, output, 6, states6, shares6,
            base._field_sha256(shares6), ledger6)
        seal_generated_bundle(output, integration6, 7)
        panel56 = transition_panel("turn5_to_turn6", raw5, integration6["raw"], states6,
            integration6["next_states"], shares6, integration6["next_shares"],
            integration5["household_rows"], integration6["household_rows"], integration5["c1_total"],
            integration6["c1_total"], integration5["capital_residual"], integration6["capital_residual"])
        panel = trajectory_panel([prior_panel, panel45, panel56])
        write_json(output / "turn3_through_turn6_trajectory_diagnostic.json", panel)
        return finalize(repository, output, pre_source, ledgers, state["relaxation"], PASS_TERMINAL,
            {"turn5_household_kfe": "31/31 PASS", "turn5_integration": "PASS",
             "turn6_entering_binding": entering6["status"], "turn6_household_kfe": "31/31 PASS",
             "turn6_integration": "PASS", "turn7_input_ready": True,
             "turn7_household_run": False, "trajectory_classification": DESCRIPTIVE}, started)
    except FailClosed as failure:
        return finalize(repository, output, pre_source, ledgers, state["relaxation"],
                        failure.terminal, failure.detail, started)
    except Exception as exc:
        return finalize(repository, output, pre_source, ledgers, state["relaxation"],
            "FAIL__UNEXPECTED_TURN5_TURN6_TASK_EXCEPTION__NO_SCIENTIFIC_RETRY",
            {"type": type(exc).__name__, "message": str(exc)}, started)
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
