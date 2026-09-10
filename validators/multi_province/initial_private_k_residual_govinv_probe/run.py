"""Run one corrected-2018 household observation and residual-GovInv accounting probe.

The scientific entrypoint performs exactly 31 HJB/KFE/aggregate observations,
then exactly one call to the existing At-only productive-capital allocation.
It deliberately imports no migration, firm, wage, controller, or trajectory route.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import platform
import sys
import time
from collections import Counter
from hashlib import sha256
from pathlib import Path
from typing import Any

import numpy as np

REPO = Path(__file__).resolve().parents[3]
for item in (REPO / "src", REPO):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))

from ch5_two_asset_hank.multi_province.capital_allocation import (  # noqa: E402
    CapitalAllocationInputs,
    allocate_productive_capital,
)
from ch5_two_asset_hank.multi_province.corrected_2018_runtime import (  # noqa: E402
    ASSET_BRIDGE_RULE,
    validate_serialized_payload,
)
from validators.multi_province.corrected_2018_hjb_propagation_25turn_kl import run as accepted  # noqa: E402
from validators.multi_province.corrected_2018_single_turn import run as single  # noqa: E402

VERDICT_PASS = "INITIAL_PRIVATE_K_RESIDUAL_GOVINV_PROBE_PASS__ONE_PASS_PRIVATE_K_OBSERVED_AND_RESIDUAL_INITIALIZATION_ACCOUNTING_VALIDATED"
VERDICT_PARTIAL = "INITIAL_PRIVATE_K_RESIDUAL_GOVINV_PROBE_PARTIAL__HOUSEHOLD_OR_KFE_VALIDITY_LIMITS_NUMERICAL_OBSERVATION"
VERDICT_BLOCKED = "INITIAL_PRIVATE_K_RESIDUAL_GOVINV_PROBE_BLOCKED__PRIVATE_K_BRIDGE_OR_ALLOCATION_NOT_OBSERVABLE_WITH_CURRENT_AUTHORITY"
THREAD_ENV = ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS")


def file_sha256(path: Path) -> str:
    digest = sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def write_json(path: Path, value: Any) -> None:
    single.write_json(path, value)


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        raise ValueError("cannot write an empty ledger")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def distribution(values: np.ndarray) -> dict[str, float]:
    values = np.asarray(values, dtype=float)
    if values.ndim != 1 or values.size == 0 or not np.isfinite(values).all():
        raise ValueError("distribution requires a nonempty finite vector")
    return {
        "min": float(np.min(values)),
        "median": float(np.median(values)),
        "mean": float(np.mean(values)),
        "max": float(np.max(values)),
    }


def residual_govinv_accounting(
    ktarget: np.ndarray, private_k_beta1: np.ndarray
) -> dict[str, np.ndarray]:
    """Pure G0/G1 accounting; this does not mutate or enter a runtime state."""
    target = np.asarray(ktarget, dtype=float)
    private = np.asarray(private_k_beta1, dtype=float)
    if target.ndim != 1 or target.shape != private.shape or target.size < 2:
        raise ValueError("target and private capital must share one province vector")
    if not np.isfinite(target).all() or not np.isfinite(private).all():
        raise ValueError("capital accounting inputs must be finite")
    if np.any(target <= 0.0) or np.any(private < 0.0):
        raise ValueError("targets must be positive and private capital non-negative")
    g0 = target.copy()
    g0_total = target + private
    g1 = np.maximum(target - private, 0.0)
    g1_total = private + g1
    beta_star = np.divide(target, private, out=np.full_like(target, np.inf), where=private > 0.0)
    return {
        "govinv_g0": g0,
        "g0_total": g0_total,
        "govinv_g1": g1,
        "g1_total": g1_total,
        "beta_star": beta_star,
    }


def prepare(distance_workbook: Path, evidence_root: Path) -> None:
    root = Path(evidence_root)
    root.mkdir(parents=True, exist_ok=False)
    payload = single.build_runtime_payload(Path(distance_workbook))
    payload["schema"] = "CH5_INITIAL_PRIVATE_K_RESIDUAL_GOVINV_PROBE_INPUT_V1"
    payload_path = root / "runtime_input_payload.json"
    write_json(payload_path, payload)
    loaded = json.loads(payload_path.read_text(encoding="utf-8"))
    validate_serialized_payload(loaded)
    write_json(root / "runtime_input_receipt.json", {
        "schema": "CH5_INITIAL_PRIVATE_K_RESIDUAL_GOVINV_RUNTIME_INPUT_RECEIPT_V1",
        "runtime_payload_sha256": file_sha256(payload_path),
        "province_count": 31,
        "province_order": payload["province_order"],
        "pre_science_assertion": payload["pre_science_assertion"],
        "metadata": payload["metadata"],
        "source_identities": payload["source_identities"],
        "distance_workbook": payload["distance_workbook"],
        "scientific_calls": 0,
    })
    source_paths = (
        Path(__file__),
        REPO / "src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py",
        REPO / "src/ch5_two_asset_hank/multi_province/capital_allocation.py",
        Path(single.__file__),
        Path(accepted.__file__),
        REPO / "exports/matlab_faithful_two_asset_ha.py",
        REPO / "src/ch5_two_asset_hank/matlab_faithful_hjb.py",
        REPO / "src/ch5_two_asset_hank/matlab_faithful_kfe.py",
    )
    write_json(root / "source_hash_receipt.json", {
        "schema": "CH5_INITIAL_PRIVATE_K_RESIDUAL_GOVINV_SOURCE_HASH_V1",
        "files": {str(path.relative_to(REPO)).replace("\\", "/"): file_sha256(path) for path in source_paths},
        "scientific_calls": 0,
    })
    write_json(root / "one_pass_invocation_receipt.json", {
        "schema": "CH5_INITIAL_PRIVATE_K_RESIDUAL_GOVINV_ONE_PASS_INVOCATION_V1",
        "prepare_entrypoint": "validators/multi_province/initial_private_k_residual_govinv_probe/run.py prepare",
        "science_entrypoint": "validators/multi_province/initial_private_k_residual_govinv_probe/run.py run",
        "scientific_processes_maximum": 1,
        "household_observations_maximum": 31,
        "hjb_returns_maximum": 31,
        "kfe_returns_maximum": 31,
        "aggregate_returns_maximum": 31,
        "at_only_capital_allocation_calls_exact": 1,
        "scientific_retry_maximum": 0,
        "second_household_pass_authorized": False,
        "migration_firm_wage_controller_trajectory_authorized": False,
        "scientific_calls_at_prepare": 0,
    })


def execute(evidence_root: Path) -> int:
    root = Path(evidence_root)
    payload_path = root / "runtime_input_payload.json"
    required = (payload_path, root / "runtime_input_receipt.json", root / "source_hash_receipt.json")
    if not all(path.is_file() for path in required):
        raise ValueError("prepared probe inputs are missing")
    if (root / "science_started.json").exists():
        raise RuntimeError("scientific execution already started; retry prohibited")
    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    validate_serialized_payload(payload)
    counters = {
        "scientific_processes": 1,
        "household_observations_attempted": 0,
        "household_observations_returned": 0,
        "native_initializations_attempted": 0,
        "native_initializations_returned": 0,
        "labor_roots_attempted": 0,
        "labor_roots_returned": 0,
        "brentq_calls_attempted": 0,
        "brentq_calls_returned": 0,
        "hjb_calls": 0,
        "hjb_returns": 0,
        "hjb_direct_solves": 0,
        "kfe_calls": 0,
        "kfe_returns": 0,
        "kfe_direct_solves": 0,
        "aggregate_calls": 0,
        "aggregate_returns": 0,
        "at_only_capital_allocation_calls": 0,
        "migration_calls": 0,
        "normalized_migration_calls": 0,
        "firm_calls": 0,
        "wage_calls": 0,
        "controller_calls": 0,
        "outer_turn_calls": 0,
        "steady_state_calls": 0,
        "scientific_retries": 0,
    }
    write_json(root / "science_started.json", {
        "schema": "CH5_INITIAL_PRIVATE_K_RESIDUAL_GOVINV_SCIENCE_STARTED_V1",
        "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "runtime_payload_sha256": file_sha256(payload_path),
        "process_id": os.getpid(),
        "python": sys.version,
        "platform": platform.platform(),
        "thread_environment": {key: os.environ.get(key) for key in THREAD_ENV},
        "authorized_household_observation_passes": 1,
        "scientific_retries": 0,
    })
    started = time.monotonic()
    states = tuple(dict(item) for item in payload["states"])
    grid = single.oracle.MatlabFaithfulHJBGrid(
        np.linspace(-2, 5, 20), np.linspace(0, 10, 20),
        np.array([0.8, 1.3]), np.array([[-1 / 3, 1 / 3], [1 / 3, -1 / 3]]),
    )
    params = single.oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
    numerics = single.oracle.MatlabFaithfulHJBNumerics(1000.0, 1e-7, 100, 1e-12)
    original_spsolve = single.oracle.linalg.spsolve
    original_brentq = single.LABOR_BRENTQ
    current_stage = "PRE_HOUSEHOLD"

    def counted_spsolve(*args, **kwargs):
        key = "hjb_direct_solves" if current_stage == "HJB" else "kfe_direct_solves"
        counters[key] += 1
        return original_spsolve(*args, **kwargs)

    def counted_brentq(*args, **kwargs):
        counters["brentq_calls_attempted"] += 1
        value = original_brentq(*args, **kwargs)
        counters["brentq_calls_returned"] += 1
        return value

    single.oracle.linalg.spsolve = counted_spsolve
    single.LABOR_BRENTQ = counted_brentq
    outputs: list[dict[str, Any]] = []
    error: dict[str, Any] | None = None
    verdict = VERDICT_BLOCKED
    try:
        for index, state in enumerate(states):
            province = payload["province_order"][index]
            counters["household_observations_attempted"] += 1
            counters["native_initializations_attempted"] += 1

            def root_enter() -> None:
                counters["labor_roots_attempted"] += 1

            def root_return() -> None:
                counters["labor_roots_returned"] += 1

            current_stage = "NATIVE_INITIALIZATION"
            initial, labor = single.source_initial_arrays(state, grid, params, root_enter, root_return)
            counters["native_initializations_returned"] += 1
            current_stage = "HJB"
            counters["hjb_calls"] += 1
            hjb = single.oracle.solve_matlab_faithful_hjb(
                grid,
                params,
                single.oracle.HouseholdInputs(
                    float(state["rah"]), float(state["rb"]), float(state["tau"]),
                    np.array([state["w"]]), np.array([0.0]), np.array([1.0]),
                ),
                initial,
                labor,
                float(state["Tt"]),
                float(state["rb_gap"]),
                numerics,
            )
            counters["hjb_returns"] += 1
            hjb_classification = accepted.validate_hjb_return_for_continuation(hjb)
            province_root = root / "household" / f"p{index:02d}_{province}"
            single._save_hjb(province_root / "hjb_return.npz", hjb)
            current_stage = "KFE"
            counters["kfe_calls"] += 1
            kfe = single.oracle.solve_matlab_faithful_stationary_kfe(
                hjb.post_convergence_operator.full,
                shape=(20, 20, 2),
                db=float(grid.b[1] - grid.b[0]),
                da=float(grid.a[1] - grid.a[0]),
            )
            counters["kfe_returns"] += 1
            accepted.validate_kfe_return_for_continuation(kfe)
            single._save_kfe(province_root / "kfe_return.npz", kfe)
            kfe_diagnostic = accepted.kfe_distribution_diagnostics(hjb, kfe)
            current_stage = "AGGREGATE"
            counters["aggregate_calls"] += 1
            aggregate = single.oracle.aggregate_stationary_household(
                grid, hjb.consumption, hjb.labor, kfe.density
            )
            counters["aggregate_returns"] += 1
            row = {
                "province_index": index,
                "province": province,
                "hjb_converged": bool(hjb.converged),
                "hjb_iterations": int(hjb.iterations),
                "hjb_statistic": float(hjb.convergence_statistic),
                "hjb_classification": hjb_classification,
                "kfe_classification": kfe_diagnostic["classification"],
                "kfe_source_free_ratio": kfe_diagnostic["source_free_residual_ratio"],
                "kfe_upper_b_max_outward_leak_rate": kfe_diagnostic["boundary_outward_leak"]["upper_b"]["max_outward_leak_rate"],
                "At_initial": float(aggregate.a_ss),
                "Bt_initial": float(aggregate.b_ss),
                "Lt_initial": float(aggregate.l_ss),
                "Ct_initial": float(aggregate.c_ss),
            }
            if not all(np.isfinite(value) for key, value in row.items() if key.endswith("_initial")):
                raise ValueError(f"{province}: nonfinite household aggregate")
            write_json(province_root / "household_observation.json", row)
            outputs.append(row)
            counters["household_observations_returned"] += 1

        current_stage = "AT_ONLY_CAPITAL_ALLOCATION"
        counters["at_only_capital_allocation_calls"] += 1
        allocation = allocate_productive_capital(CapitalAllocationInputs(
            illiquid_assets_at=[row["At_initial"] for row in outputs],
            population=[state["N"] for state in states],
            inter_province_ratio=[state["inter_prv_ratio"] for state in states],
            old_firm_return_ra=[state["ra"] for state in states],
        ))
        if counters["at_only_capital_allocation_calls"] != 1:
            raise RuntimeError("At-only allocation call count violated")
        target = np.asarray([state["Kt0"] for state in states], dtype=float)
        private = np.asarray(allocation.kt_supply, dtype=float)
        accounting = residual_govinv_accounting(target, private)
        at_times_n = np.asarray(
            [outputs[index]["At_initial"] * states[index]["N"] for index in range(31)],
            dtype=float,
        )
        productive_contribution = np.asarray(allocation.productive_contribution, dtype=float)
        ratios = private / target
        beta_star = accounting["beta_star"]
        ledger: list[dict[str, Any]] = []
        validity: list[dict[str, Any]] = []
        for index, (state, observation) in enumerate(zip(states, outputs)):
            private_at_or_above = bool(private[index] >= target[index])
            overall = "DIAGNOSTIC_ONLY" if (
                observation["hjb_classification"] != "HJB_CONVERGED"
                or observation["kfe_classification"] != "VALID"
                or ASSET_BRIDGE_RULE == "SOURCE_FAITHFUL_DIAGNOSTIC_ONLY"
            ) else "VALID"
            row = {
                "province_index": index,
                "province": state["name"],
                "Ktarget_2018_MU": target[index],
                "HJB_converged": observation["hjb_converged"],
                "HJB_iterations": observation["hjb_iterations"],
                "HJB_statistic": observation["hjb_statistic"],
                "HJB_classification": observation["hjb_classification"],
                "KFE_classification": observation["kfe_classification"],
                "At_initial": observation["At_initial"],
                "Bt_initial": observation["Bt_initial"],
                "Lt_initial": observation["Lt_initial"],
                "Ct_initial": observation["Ct_initial"],
                "N_NU": state["N"],
                "At_times_N_beta1_preallocation": at_times_n[index],
                "inter_province_productive_contribution_beta1": productive_contribution[index],
                "Kt_supply_initial_MU_beta1": private[index],
                "private_K_over_target_beta1": ratios[index],
                "GovInv0_G0_MU": accounting["govinv_g0"][index],
                "firm_K_accounting_G0_MU": accounting["g0_total"][index],
                "firm_K_G0_over_target": accounting["g0_total"][index] / target[index],
                "GovInv0_G1_residual_MU": accounting["govinv_g1"][index],
                "firm_K_accounting_G1_MU": accounting["g1_total"][index],
                "firm_K_G1_over_target": accounting["g1_total"][index] / target[index],
                "beta_a_star": beta_star[index],
                "G1_binding_status": "PRIVATE_AT_OR_ABOVE_TARGET" if private_at_or_above else "PRIVATE_BELOW_TARGET",
                "asset_bridge_validity": ASSET_BRIDGE_RULE,
                "overall_validity": overall,
            }
            ledger.append(row)
            validity.append({
                "province_index": index,
                "province": state["name"],
                "HJB_converged": observation["hjb_converged"],
                "HJB_classification": observation["hjb_classification"],
                "KFE_classification": observation["kfe_classification"],
                "KFE_source_free_ratio": observation["kfe_source_free_ratio"],
                "KFE_upper_b_max_outward_leak_rate": observation["kfe_upper_b_max_outward_leak_rate"],
                "asset_bridge_validity": ASSET_BRIDGE_RULE,
                "overall_validity": overall,
            })
        write_csv(root / "province_initial_private_k_ledger.csv", ledger)
        write_csv(root / "household_validity_ledger.csv", validity)
        write_csv(root / "bridge_sensitivity_beta_star.csv", [{
            "province_index": row["province_index"],
            "province": row["province"],
            "Kt_supply_initial_MU_beta1": row["Kt_supply_initial_MU_beta1"],
            "Ktarget_2018_MU": row["Ktarget_2018_MU"],
            "beta_a_star": row["beta_a_star"],
            "interpretation": "DIAGNOSTIC_GEOMETRY_NOT_ESTIMATED_BETA",
        } for row in ledger])
        g0_ratio = accounting["g0_total"] / target
        g1_ratio = accounting["g1_total"] / target
        summary = {
            "schema": "CH5_INITIAL_PRIVATE_K_RESIDUAL_GOVINV_NATIONAL_SUMMARY_V1",
            "province_observations": len(ledger),
            "national_sums": {
                "Ktarget_MU": float(np.sum(target)),
                "private_K_beta1_MU": float(np.sum(private)),
                "G0_GovInv_MU": float(np.sum(accounting["govinv_g0"])),
                "G0_firm_K_accounting_MU": float(np.sum(accounting["g0_total"])),
                "G1_residual_GovInv_MU": float(np.sum(accounting["govinv_g1"])),
                "G1_firm_K_accounting_MU": float(np.sum(accounting["g1_total"])),
            },
            "private_K_over_target_beta1": distribution(ratios),
            "G0_total_over_target": distribution(g0_ratio),
            "G1_total_over_target": distribution(g1_ratio),
            "beta_a_star": distribution(beta_star[np.isfinite(beta_star)]),
            "private_K_at_or_above_target_count": int(np.count_nonzero(private >= target)),
            "G1_residual_zero_count": int(np.count_nonzero(accounting["govinv_g1"] == 0.0)),
            "HJB_classification_counts": dict(Counter(row["HJB_classification"] for row in ledger)),
            "KFE_classification_counts": dict(Counter(row["KFE_classification"] for row in ledger)),
            "accounting_identity_max_abs_error": float(np.max(np.abs(
                accounting["g1_total"] - np.maximum(target, private)
            ))),
            "homogeneity_contract": "Kt_supply_initial(beta_a)=beta_a*Kt_supply_initial(beta_a=1)",
            "homogeneity_basis": "algebraic inspection of linear At*N contributions; no second allocation or beta cell",
            "asset_bridge_validity": ASSET_BRIDGE_RULE,
            "results_eligible": False,
        }
        write_json(root / "national_capital_initialization_summary.json", summary)
        anhui = dict(ledger[11])
        anhui.update({
            "Y0": states[11]["Yt0"],
            "N0": states[11]["N"],
            "alpha": states[11]["alpha"],
            "Zt0": states[11]["Zt"],
            "fixed_initial_rah": states[11]["rah"],
            "fixed_initial_rb": states[11]["rb"],
            "fixed_initial_w": states[11]["w"],
            "fixed_initial_wjt": states[11]["wjt"],
            "fixed_initial_ra": states[11]["ra"],
            "fixed_initial_tau": states[11]["tau"],
            "fixed_initial_Tt": states[11]["Tt"],
        })
        write_json(root / "anhui_initialization_receipt.json", anhui)
        verdict = VERDICT_PASS
    except Exception as exc:
        error = {"type": type(exc).__name__, "message": str(exc), "stage": current_stage}
        write_json(root / "scientific_failure.json", error)
    finally:
        single.oracle.linalg.spsolve = original_spsolve
        single.LABOR_BRENTQ = original_brentq
    counters["household_observations_failed"] = (
        counters["household_observations_attempted"] - counters["household_observations_returned"]
    )
    write_json(root / "call_ledger.json", {
        "schema": "CH5_INITIAL_PRIVATE_K_RESIDUAL_GOVINV_CALL_LEDGER_V1",
        "counts": counters,
        "elapsed_seconds": time.monotonic() - started,
        "failed_calls_counted": True,
        "engineering_retry_count": 0,
        "second_household_passes": 0,
        "beta_parameter_cells": 0,
        "matlab_calls": 0,
        "ge_calls": 0,
        "annual_calls": 0,
        "irf_calls": 0,
        "results_calls": 0,
    })
    write_json(root / "terminal_result.json", {
        "schema": "CH5_INITIAL_PRIVATE_K_RESIDUAL_GOVINV_TERMINAL_V1",
        "verdict": verdict,
        "error": error,
        "one_pass_completed": verdict == VERDICT_PASS,
        "production_govinv_changed": False,
        "trajectory_authorized": False,
        "results_eligible": False,
    })
    return 0 if verdict == VERDICT_PASS else 2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)
    prepare_parser = commands.add_parser("prepare")
    prepare_parser.add_argument("distance_workbook", type=Path)
    prepare_parser.add_argument("evidence_root", type=Path)
    run_parser = commands.add_parser("run")
    run_parser.add_argument("evidence_root", type=Path)
    args = parser.parse_args(argv)
    if args.command == "prepare":
        prepare(args.distance_workbook, args.evidence_root)
        return 0
    return execute(args.evidence_root)


if __name__ == "__main__":
    raise SystemExit(main())
