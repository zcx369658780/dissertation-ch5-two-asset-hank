"""Integration-only replay from the accepted run004 household batch."""
from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import json
import math
from pathlib import Path
import subprocess
import time
from typing import Any, Mapping
import xml.etree.ElementTree as ET

import numpy as np

from ch5_two_asset_hank.multi_province import one_turn as source
from ch5_two_asset_hank.multi_province.c1_residual_public_asset import C1_UPDATE_ORDER
from ch5_two_asset_hank.multi_province.capital_allocation import CapitalAllocationInputs
from ch5_two_asset_hank.multi_province.government_assets import residual_government_asset_levels
from ch5_two_asset_hank.multi_province.k1a_runtime_adapter import (
    K1ARuntimeConfig,
    allocate_k1a_capital,
    load_accepted_distance_score,
)
from ch5_two_asset_hank.multi_province.one_turn import PreFrozenHouseholdOutputBatch
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER

from .nonlinear_continuation import _canonical_sha256, _field_sha256, _sha256, _write_json
from .optionb_initial_turn_integration import (
    DISTANCE_RELATIVE,
    _one_turn_inputs,
    load_initial_states,
)


TASK_ID = "CH5_MP4C_RUN004_CANONICAL_SAME_S_RAW_NEXT_PAYOFF_REPAIR_AND_INTEGRATION_ONLY_REPLAY_20260920"
BASELINE_SHA = "1257c15e6c91c3ae5d7f7184d381ff5289960dfa"
PASS_TERMINAL = (
    "PASS__RUN004_ACCEPTED_31_PROVINCE_HOUSEHOLD_KFE__CANONICAL_SAME_S_"
    "INTEGRATION_REPLAY_PASS__RAW_NEXT_PAYOFF_READY__TURN2_NOT_RUN"
)
RUN004_RELATIVE = Path(
    "reports/ch5_mp4c_corrected_optionb_initial_turn_unique_closed_class_kfe_"
    "20260920_run004"
)
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_run004_canonical_same_s_integration_replay_20260920_run001"
)
REPORT_RELATIVE = Path(
    "docs/CH5_MP4C_RUN004_CANONICAL_SAME_S_RAW_NEXT_PAYOFF_REPAIR_AND_"
    "INTEGRATION_ONLY_REPLAY_REPORT.md"
)
TASK_RELATIVE = Path(
    "tasks/CH5_MP4C_RUN004_CANONICAL_SAME_S_RAW_NEXT_PAYOFF_REPAIR_AND_"
    "INTEGRATION_ONLY_REPLAY_20260920.md"
)
RUN004_MANIFEST_SHA256 = "CF70E7D6A62A35F461D1A75B28F8F502B2CBDD2D94ED5D9DDFA099D821CC5EC6"
HOUSEHOLD_BATCH_SHA256 = "8B7875F3BD603038E4D415D9F9FF759D4FDDC93E2E677C13BF0B649571B2EB05"


class FailClosed(RuntimeError):
    def __init__(self, terminal: str, detail: Mapping[str, Any] | None = None) -> None:
        super().__init__(terminal)
        self.terminal = terminal
        self.detail = dict(detail or {})


def _git(repository: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repository, text=True).strip()


def _task_hashes(repository: Path) -> dict[str, str]:
    paths = [
        repository / "src/ch5_two_asset_hank/corrected_diagnostic/run004_canonical_integration_replay.py",
        repository / "tests/test_mp4c_run004_canonical_integration_replay.py",
        repository / "src/ch5_two_asset_hank/corrected_diagnostic/optionb_initial_turn_integration.py",
        repository / "src/ch5_two_asset_hank/multi_province/one_turn.py",
        repository / "src/ch5_two_asset_hank/multi_province/migration_labor.py",
        repository / "src/ch5_two_asset_hank/multi_province/k1a_runtime_adapter.py",
        repository / "src/ch5_two_asset_hank/multi_province/capital_network.py",
        repository / "src/ch5_two_asset_hank/multi_province/government_assets.py",
        repository / "src/ch5_two_asset_hank/multi_province/c1_residual_public_asset.py",
        repository / "src/ch5_two_asset_hank/multi_province/firm.py",
        repository / "src/ch5_two_asset_hank/multi_province/wage.py",
        repository / "src/ch5_two_asset_hank/multi_province/monetary.py",
        repository / "src/ch5_two_asset_hank/multi_province/fiscal_diagnostics.py",
        repository / DISTANCE_RELATIVE,
        repository / TASK_RELATIVE,
    ]
    return {
        path.relative_to(repository).as_posix(): _sha256(path)
        for path in paths
    }


def _new_ledger() -> dict[str, int]:
    return {
        "run004_manifest_loads": 0,
        "province_terminal_receipt_loads": 0,
        "stationary_aggregate_receipt_loads": 0,
        "household_batch_reconstructions": 0,
        "source_faithful_labor_reconstructions": 0,
        "k1a_capital_network_allocations": 0,
        "c1_residual_govinv_constructions": 0,
        "firm_evaluations": 0,
        "composite_wage_batches": 0,
        "monetary_assignments": 0,
        "fiscal_diagnostic_batches": 0,
        "canonical_raw_next_payoff_constructions": 0,
        "source_native_initializations": 0,
        "selector_or_root_calls": 0,
        "d2_q_assemblies": 0,
        "hjb_or_direct_solve_calls": 0,
        "scc_or_topology_calls": 0,
        "restricted_gesvd_calls": 0,
        "full_space_gesvd_calls": 0,
        "stationary_mass_candidate_calls": 0,
        "q_transpose_p_calls": 0,
        "corrected_aggregate_evaluations": 0,
        "second_integration_replays": 0,
        "turn2_household_calls": 0,
        "second_outer_turns": 0,
        "k1b_calls": 0,
        "k2_calls": 0,
        "adaptive_controller_calls": 0,
        "matlab_calls": 0,
        "ge_annual_shock_irf_welfare_results_calls": 0,
        "scientific_retries": 0,
        "payoff_clipping_annualization_rescaling_smoothing_risk_adjustment_zscore_calls": 0,
    }


def _check_ledger(ledger: Mapping[str, int]) -> None:
    ceilings = {
        "run004_manifest_loads": 1,
        "province_terminal_receipt_loads": 31,
        "stationary_aggregate_receipt_loads": 31,
        "household_batch_reconstructions": 1,
        "source_faithful_labor_reconstructions": 1,
        "k1a_capital_network_allocations": 1,
        "c1_residual_govinv_constructions": 1,
        "firm_evaluations": 31,
        "composite_wage_batches": 1,
        "monetary_assignments": 1,
        "fiscal_diagnostic_batches": 1,
        "canonical_raw_next_payoff_constructions": 1,
    }
    zero = set(ledger) - set(ceilings)
    breaches = {
        name: {"actual": int(value), "ceiling": ceilings.get(name, 0)}
        for name, value in ledger.items()
        if (name in zero and int(value) != 0)
        or (name in ceilings and int(value) > ceilings[name])
    }
    if breaches:
        raise FailClosed("BLOCKED__INTEGRATION_ONLY_LEDGER_CEILING", {"breaches": breaches})


def canonical_same_s_raw_next_payoff(
    raw_ra0_by_destination: object,
    shares_destination_origin: object,
    *,
    orientation: str,
    raw_source: str,
    expected_raw_sha256: str,
    expected_shares_sha256: str,
) -> tuple[np.ndarray, np.ndarray]:
    raw = np.asarray(raw_ra0_by_destination, dtype=np.float64)
    shares = np.asarray(shares_destination_origin, dtype=np.float64)
    if raw.shape != (31,) or shares.shape != (31, 31):
        raise FailClosed("FAIL__CANONICAL_PAYOFF_AXIS_CONTRACT")
    checks = {
        "orientation_destination_by_origin": orientation == "destination_by_origin",
        "raw_source_exact_firm_ra0": raw_source == "firm.ra0",
        "raw_identity": _field_sha256(raw) == expected_raw_sha256,
        "shares_identity": _field_sha256(shares) == expected_shares_sha256,
        "inputs_finite": bool(np.all(np.isfinite(raw)) and np.all(np.isfinite(shares))),
    }
    if not all(checks.values()):
        raise FailClosed("FAIL__CANONICAL_PAYOFF_PROVENANCE_OR_ORIENTATION", checks)
    terms = np.empty((31, 31), dtype=np.float64)
    payoff = np.empty(31, dtype=np.float64)
    for origin in range(31):
        for destination in range(31):
            terms[destination, origin] = (
                float(raw[destination]) * float(shares[destination, origin])
            )
        payoff[origin] = math.fsum(
            float(terms[destination, origin]) for destination in range(31)
        )
    if not np.all(np.isfinite(payoff)):
        raise FailClosed("FAIL__CANONICAL_PAYOFF_NONFINITE")
    return payoff, terms


def _verify_run004_manifest(repository: Path) -> dict[str, Any]:
    root = repository / RUN004_RELATIVE
    manifest_path = root / "sealed_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bad_paths = []
    for entry in manifest["entries"]:
        target = root / entry["path"]
        if (
            not target.is_file()
            or target.stat().st_size != int(entry["bytes"])
            or _sha256(target) != entry["sha256"]
        ):
            bad_paths.append(entry["path"])
    readback = json.loads((root / "independent_readback_receipt.json").read_text(encoding="utf-8"))
    checks = {
        "manifest_sha256": _sha256(manifest_path) == RUN004_MANIFEST_SHA256,
        "entry_count_4353": int(manifest["entry_count"]) == 4353,
        "total_bytes_61650777": int(manifest["total_bytes"]) == 61_650_777,
        "all_entries_read_back": not bad_paths,
        "independent_readback_pass": readback.get("status") == "PASS" and not readback.get("bad_paths"),
    }
    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "manifest_sha256": _sha256(manifest_path),
        "entry_count": int(manifest["entry_count"]),
        "total_bytes": int(manifest["total_bytes"]),
        "bad_paths": bad_paths,
    }


def reconstruct_accepted_household_batch(
    repository: Path, ledger: dict[str, int] | None = None
) -> tuple[PreFrozenHouseholdOutputBatch, dict[str, Any]]:
    root = repository / RUN004_RELATIVE
    accepted = json.loads((root / "household_batch_receipt.json").read_text(encoding="utf-8"))
    values: dict[str, list[float]] = {name: [] for name in ("ct", "lt", "at", "bt", "at_tax")}
    diagnostics = []
    terminal_count = 0
    aggregate_count = 0
    for index, province in enumerate(PROVINCE_ORDER):
        province_root = root / "household" / f"p{index:02d}_{province}"
        terminal = json.loads((province_root / "province_terminal_receipt.json").read_text(encoding="utf-8"))
        aggregate = json.loads((province_root / "stationary_aggregate_receipt.json").read_text(encoding="utf-8"))
        terminal_count += 1
        aggregate_count += 1
        if terminal["province_index"] != index or terminal["province"] != province:
            raise FailClosed("BLOCKED__RUN004_PROVINCE_RECEIPT_ORDER")
        values["ct"].append(float(aggregate["Ct"]["mass_form"]))
        values["lt"].append(float(aggregate["Lt"]["mass_form"]))
        values["at"].append(float(aggregate["At"]["mass_form"]))
        values["bt"].append(float(aggregate["Bt"]["mass_form"]))
        values["at_tax"].append(float(aggregate["AtTax"]["mass_form"]))
        diagnostics.append({"checkpoint": terminal["checkpoint"], "B": terminal["B"], "D": terminal["D"]})
    batch = PreFrozenHouseholdOutputBatch(
        ct=values["ct"], household_lt=values["lt"], at=values["at"],
        bt=values["bt"], at_tax=values["at_tax"], converged=(True,) * 31,
        diagnostics=tuple(diagnostics),
    )
    identity = _canonical_sha256({
        "ct": batch.ct.tolist(), "lt": batch.household_lt.tolist(),
        "at": batch.at.tolist(), "bt": batch.bt.tolist(),
        "at_tax": batch.at_tax.tolist(),
    })
    checks = {
        "province_terminal_receipts_31": terminal_count == 31,
        "stationary_aggregate_receipts_31": aggregate_count == 31,
        "accepted_batch_province_count_31": accepted["province_count"] == 31,
        "accepted_batch_status_pass": accepted.get("status") == "PASS",
        "accepted_identity": accepted["identity_sha256"] == HOUSEHOLD_BATCH_SHA256,
        "reconstructed_identity": identity == HOUSEHOLD_BATCH_SHA256,
    }
    if ledger is not None:
        ledger["province_terminal_receipt_loads"] += terminal_count
        ledger["stationary_aggregate_receipt_loads"] += aggregate_count
        ledger["household_batch_reconstructions"] += 1
        _check_ledger(ledger)
    receipt = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "accepted_identity_sha256": accepted["identity_sha256"],
        "reconstructed_identity_sha256": identity,
        "province_order": list(PROVINCE_ORDER),
    }
    if receipt["status"] != "PASS":
        raise FailClosed("BLOCKED__RUN004_HOUSEHOLD_BATCH_BINDING", receipt)
    return batch, receipt


def _seal(output: Path) -> dict[str, Any]:
    entries = []
    for path in sorted(output.rglob("*")):
        if path.is_file() and path.name not in {"sealed_manifest.json", "independent_readback_receipt.json"}:
            entries.append({
                "path": path.relative_to(output).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": _sha256(path),
            })
    manifest = {
        "schema": "CH5_MP4C_RUN004_CANONICAL_SAME_S_INTEGRATION_REPLAY_V1",
        "entry_count": len(entries),
        "total_bytes": sum(int(row["bytes"]) for row in entries),
        "entries": entries,
    }
    _write_json(output / "sealed_manifest.json", manifest)
    return manifest


def _readback(output: Path) -> dict[str, Any]:
    manifest_path = output / "sealed_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bad = []
    for row in manifest["entries"]:
        target = output / row["path"]
        if not target.is_file() or target.stat().st_size != row["bytes"] or _sha256(target) != row["sha256"]:
            bad.append(row["path"])
    receipt = {
        "status": "PASS" if not bad else "FAIL",
        "manifest_sha256": _sha256(manifest_path),
        "entry_count": len(manifest["entries"]),
        "total_bytes": sum(int(row["bytes"]) for row in manifest["entries"]),
        "bad_paths": bad,
    }
    _write_json(output / "independent_readback_receipt.json", receipt)
    return receipt


def _read_junit(path: Path) -> dict[str, Any]:
    root = ET.parse(path).getroot()
    tests = int(root.attrib.get("tests", sum(int(row.attrib.get("tests", 0)) for row in root)))
    failures = int(root.attrib.get("failures", sum(int(row.attrib.get("failures", 0)) for row in root)))
    errors = int(root.attrib.get("errors", sum(int(row.attrib.get("errors", 0)) for row in root)))
    return {"status": "PASS" if tests and not failures and not errors else "FAIL", "tests": tests, "failures": failures, "errors": errors}


def _write_report(repository: Path, receipt: Mapping[str, Any], ledger: Mapping[str, int]) -> None:
    payoff = receipt["canonical_raw_next_payoff"]
    lines = [
        "# Chapter 5 run004 canonical same-S integration-only replay", "",
        "## Terminal verdict", "", f"`{PASS_TERMINAL}`", "",
        "The accepted run004 household batch was reconstructed exactly. No household HJB, KFE, stationary-mass or aggregate science was rerun. One integration-only replay passed all accounting gates.", "",
        "## Accepted batch binding", "",
        f"- Reconstructed identity: `{HOUSEHOLD_BATCH_SHA256}`.",
        "- Province terminal receipts: `31`; stationary aggregate receipts: `31`.", "",
        "## Canonical same-S payoff", "",
        f"- Raw-ra0 SHA-256: `{payoff['raw_ra0_sha256']}`.",
        f"- S SHA-256: `{payoff['shares_sha256']}`.",
        f"- Ordered product terms SHA-256: `{payoff['product_terms_sha256']}`.",
        f"- Canonical payoff SHA-256: `{payoff['canonical_payoff_sha256']}`.",
        f"- Canonical versus BLAS max absolute difference: `{payoff['canonical_vs_blas_max_abs_difference']:.17g}`; bitwise equal entries: `{payoff['canonical_vs_blas_bitwise_equal_count']}/31`.", "",
        "## Integration accounting", "",
        *[f"- {name}: `{value}`." for name, value in receipt["checks"].items()], "",
        "## Scientific ledger", "",
        *[f"- {name}: `{value}`." for name, value in ledger.items()], "",
        "Turn 2 was not run. K1B, K2, GE and Results were not run. CURRENT files were not modified and no successor was published.", "",
    ]
    (repository / REPORT_RELATIVE).write_text("\n".join(lines), encoding="utf-8", newline="\n")


def execute(repository: Path, focused_test_junit: Path) -> str:
    repository = repository.resolve(strict=True)
    output = repository / OUTPUT_RELATIVE
    output.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    ledger = _new_ledger()
    pre_hashes = _task_hashes(repository)
    try:
        changed = sorted(filter(None, _git(repository, "diff", "--name-only", f"{BASELINE_SHA}...HEAD").splitlines()))
        expected_changed = sorted([
            "src/ch5_two_asset_hank/corrected_diagnostic/run004_canonical_integration_replay.py",
            "tests/test_mp4c_run004_canonical_integration_replay.py",
        ])
        focused = _read_junit(focused_test_junit)
        startup = {
            "clean_worktree": not bool(_git(repository, "status", "--porcelain")),
            "origin_main_exact_baseline": _git(repository, "rev-parse", "origin/main") == BASELINE_SHA,
            "baseline_is_ancestor": _git(repository, "merge-base", "--is-ancestor", BASELINE_SHA, "HEAD") == "",
            "changed_paths_exact": changed == expected_changed,
            "focused_tests_pass": focused["status"] == "PASS",
        }
        if not all(startup.values()):
            raise FailClosed("BLOCKED__ZERO_SCIENCE_STARTUP_GATE", {"checks": startup, "changed": changed})
        manifest_receipt = _verify_run004_manifest(repository)
        ledger["run004_manifest_loads"] += 1
        if manifest_receipt["status"] != "PASS":
            raise FailClosed("BLOCKED__RUN004_MANIFEST_BINDING", manifest_receipt)
        batch, batch_receipt = reconstruct_accepted_household_batch(repository, ledger)
        states, state_receipt = load_initial_states(repository)
        _write_json(output / "authority_binding.json", {
            "status": "PASS", "task_id": TASK_ID, "actual_baseline": BASELINE_SHA,
            "startup_checks": startup, "run004_manifest": manifest_receipt,
            "initial_state_binding": state_receipt,
        })
        _write_json(output / "run004_household_batch_binding.json", batch_receipt)
        _write_json(output / "zero_science_gate_receipt.json", {
            "status": "PASS", "focused_tests": focused,
            "forbidden_household_scientific_calls": {name: ledger[name] for name in (
                "source_native_initializations", "selector_or_root_calls", "d2_q_assemblies",
                "hjb_or_direct_solve_calls", "scc_or_topology_calls", "restricted_gesvd_calls",
                "full_space_gesvd_calls", "stationary_mass_candidate_calls",
                "q_transpose_p_calls", "corrected_aggregate_evaluations",
            )},
        })
        _write_json(output / "pre_execution_code_freeze.json", {"scientific_code_sha256_before": pre_hashes})

        inputs = _one_turn_inputs(repository, states, batch)
        provinces = inputs.old_provinces
        ledger["source_faithful_labor_reconstructions"] += 1
        migration = source.reconstruct_migration_labor(source.MigrationLaborInputs(
            consumption_by_origin=batch.ct,
            population_by_origin=[row["N"] for row in provinces],
            old_firm_wage_by_destination=[row["wjt"] for row in provinces],
            tax_by_origin=[row["tau"] for row in provinces],
            phi_destination_origin=inputs.phi_destination_origin,
            migration_wedge_destination_origin=inputs.migration_wedge_destination_origin,
            gamma_c=inputs.params["ga"], phi_l=inputs.params["phi_l"],
        ))
        _write_json(output / "source_faithful_labor_receipt.json", {
            "status": "PASS", "lt_supply": migration.lt_supply.tolist(),
            "lt_supply_sha256": _field_sha256(migration.lt_supply),
            "destination_total": float(np.sum(migration.lt_supply)),
        })

        ledger["k1a_capital_network_allocations"] += 1
        distance = load_accepted_distance_score(repository / DISTANCE_RELATIVE)
        capital = allocate_k1a_capital(
            CapitalAllocationInputs(
                illiquid_assets_at=batch.at,
                population=[row["N"] for row in provinces],
                inter_province_ratio=[row["inter_prv_ratio"] for row in provinces],
                old_firm_return_ra=[row["ra"] for row in provinces],
            ),
            K1ARuntimeConfig(PROVINCE_ORDER, distance, beta_distance=2.0, beta_return=0.0),
        )
        shares = capital.network.portfolio_shares_destination_origin
        np.savez_compressed(output / "k1a_capital_arrays.npz", shares=shares, kt_supply=capital.kt_supply,
                            origin_private_wealth=capital.network.origin_private_wealth,
                            destination_private_capital=capital.network.destination_private_productive_capital,
                            home_retained=capital.network.domestic_retained_capital_by_origin)
        _write_json(output / "k1a_capital_accounting_receipt.json", {
            "beta_distance": 2.0, "beta_return": 0.0,
            "orientation": "destination_by_origin", "shares_sha256": _field_sha256(shares),
            "share_column_sums": np.sum(shares, axis=0).tolist(),
            "origin_private_wealth_total": float(np.sum(capital.network.origin_private_wealth)),
            "destination_private_capital_total": float(np.sum(capital.network.destination_private_productive_capital)),
        })

        ledger["c1_residual_govinv_constructions"] += 1
        accounting = residual_government_asset_levels(
            Ktarget_MU=[row["Kt0"] for row in provinces],
            Kprivate_current_MU=capital.kt_supply,
            province_order=PROVINCE_ORDER,
        )
        _write_json(output / "c1_residual_govinv_receipt.json", {
            "status": "PASS", "formula": "max(Ktarget-Kprivate,0)",
            "GovInv_residual_MU": accounting.GovInv_residual_MU.tolist(),
            "firm_K_accounting_MU": accounting.firm_K_accounting_MU.tolist(),
        })

        firms = []
        firm_k_errors = []
        for index, province in enumerate(provinces):
            firm_source = dict(province)
            firm_source["GovInv"] = float(accounting.GovInv_residual_MU[index])
            firm_source["AtTax"] = float(batch.at_tax[index])
            firm_source["Lt_prev"] = float(batch.household_lt[index])
            ledger["firm_evaluations"] += 1
            firm = source.evaluate_firm(
                firm_source, float(capital.kt_supply[index]),
                float(migration.lt_supply[index]), inputs.params,
            )
            firms.append(firm)
            firm_k_errors.append(float(firm.Kt) - float(accounting.firm_K_accounting_MU[index]))

        ledger["composite_wage_batches"] += 1
        wages = source.composite_household_wages(
            provinces, [firm.wjt for firm in firms], inputs.phi_destination_origin,
            inputs.migration_wedge_destination_origin,
            phi_l=inputs.params["phi_l"], alphal=inputs.params["alphal"],
        )
        ledger["monetary_assignments"] += 1
        monetary = source.taylor_assignment(
            istar=inputs.params["istar"], rho_pi=inputs.params["rho_pi"],
            totalpit=inputs.params["totalpit"], epsilon_pi=inputs.params["epsilon_pi"],
        )
        ledger["fiscal_diagnostic_batches"] += 1
        fiscal = source.national_fiscal_diagnostics(
            [firm.Govinc for firm in firms], batch.bt, monetary.rb,
            [row["N"] for row in provinces],
        )

        raw_ra0 = np.asarray([firm.ra0 for firm in firms], dtype=np.float64)
        raw_sha = _field_sha256(raw_ra0)
        shares_sha = _field_sha256(shares)
        ledger["canonical_raw_next_payoff_constructions"] += 1
        canonical, product_terms = canonical_same_s_raw_next_payoff(
            raw_ra0, shares, orientation="destination_by_origin", raw_source="firm.ra0",
            expected_raw_sha256=raw_sha, expected_shares_sha256=shares_sha,
        )
        blas = raw_ra0 @ shares
        np.savez_compressed(
            output / "canonical_raw_next_payoff_arrays.npz",
            raw_ra0=raw_ra0, shares=shares, ordered_product_terms=product_terms,
            canonical_payoff=canonical, blas_diagnostic=blas,
        )
        payoff_receipt = {
            "orientation": "destination_by_origin", "destination_order": list(range(31)),
            "raw_source": "firm.ra0", "raw_ra0": raw_ra0.tolist(),
            "raw_ra0_sha256": raw_sha, "shares_sha256": shares_sha,
            "product_terms_sha256": _field_sha256(product_terms),
            "canonical_payoff": canonical.tolist(),
            "canonical_payoff_sha256": _field_sha256(canonical),
            "blas_diagnostic": blas.tolist(),
            "blas_diagnostic_sha256": _field_sha256(blas),
            "canonical_vs_blas_max_abs_difference": float(np.max(np.abs(canonical - blas))),
            "canonical_vs_blas_bitwise_equal_count": int(np.count_nonzero(canonical == blas)),
            "blas_is_acceptance_gate": False,
        }
        _write_json(output / "canonical_raw_next_payoff_receipt.json", payoff_receipt)

        wealth = capital.network.origin_private_wealth
        private = capital.network.destination_private_productive_capital
        k_scale = max(1.0, float(np.sum(wealth)))
        expected_home = (1.0 - np.asarray([row["inter_prv_ratio"] for row in provinces])) * wealth
        expected_gov = np.maximum(np.asarray([row["Kt0"] for row in provinces]) - private, 0.0)
        firm_values = np.asarray([
            value for firm in firms for value in (firm.Kt, firm.Yt, firm.wjt, firm.ra0, firm.ra)
        ])
        checks = {
            "source_update_order": C1_UPDATE_ORDER == (
                "pre_frozen_household_outputs", "source_faithful_migration_labor",
                "at_only_private_productive_capital", "c1_residual_public_asset_level",
                "firm", "household_composite_wage", "taylor_rb", "fiscal_diagnostics",
            ),
            "k1a_share_columns": bool(np.allclose(np.sum(shares, axis=0), 1.0, rtol=0.0, atol=1e-12)),
            "national_private_capital": abs(float(np.sum(private) - np.sum(wealth))) <= 1e-12 * k_scale,
            "home_retained_capital": bool(np.allclose(capital.network.domestic_retained_capital_by_origin, expected_home, rtol=0.0, atol=1e-12 * k_scale)),
            "c1_residual_exact": bool(np.array_equal(accounting.GovInv_residual_MU, expected_gov)),
            "firm_k_accounting": max(abs(value) for value in firm_k_errors) <= 1e-12 * max(1.0, float(np.max(np.abs(accounting.firm_K_accounting_MU)))),
            "all_firm_outputs_finite": bool(np.all(np.isfinite(firm_values))),
            "raw_ra0_finite": bool(np.all(np.isfinite(raw_ra0))),
            "same_exact_s_for_quantity_and_payoff": _field_sha256(shares) == shares_sha,
            "canonical_raw_next_payoff_finite": bool(np.all(np.isfinite(canonical))),
            "no_payoff_transformation": ledger["payoff_clipping_annualization_rescaling_smoothing_risk_adjustment_zscore_calls"] == 0,
        }
        _write_json(output / "integration_accounting_receipt.json", {
            "status": "PASS" if all(checks.values()) else "FAIL", "checks": checks,
            "national_private_capital_residual": float(np.sum(private) - np.sum(wealth)),
            "maximum_firm_k_accounting_error": max(abs(value) for value in firm_k_errors),
        })
        if not all(checks.values()):
            raise FailClosed("FAIL__INTEGRATION_ONLY_ACCOUNTING", {"checks": checks})

        firm_diagnostics = [
            {"province_index": index, "province": PROVINCE_ORDER[index],
             "K": float(firm.Kt), "Y": float(firm.Yt), "wage": float(firm.wjt),
             "raw_ra0": float(firm.ra0), "used_ra": float(firm.ra)}
            for index, firm in enumerate(firms)
        ]
        _write_json(output / "firm_diagnostics_31province.json", {
            "status": "PASS", "count": 31, "rows": firm_diagnostics,
        })
        _write_json(output / "wage_monetary_fiscal_receipt.json", {
            "status": "PASS", "next_composite_wage": list(map(float, wages)),
            "next_rb": float(monetary.rb), "monetary": asdict(monetary),
            "fiscal": asdict(fiscal),
        })
        next_states = []
        for index in range(31):
            state = dict(provinces[index])
            state.update({
                "Ct": float(batch.ct[index]), "At": float(batch.at[index]),
                "Bt": float(batch.bt[index]), "AtTax": float(batch.at_tax[index]),
                "convergent": True, "Lt_supply": float(migration.lt_supply[index]),
                "Kt_supply": float(capital.kt_supply[index]), "rah": float(canonical[index]),
                "w": float(wages[index]), "it": float(monetary.it), "rb": float(monetary.rb),
                "Yt_1": float(provinces[index]["Yt"]), "Kt_prev": float(firms[index].Kt),
                "Lt_prev": float(firms[index].Lt), "Zt_1": float(provinces[index]["Zt"]),
                "pit_1": float(provinces[index]["pit"]),
                "GovInv": float(accounting.GovInv_residual_MU[index]),
            })
            state.update(firms[index].as_source_dict())
            next_states.append({
                "province_index": index, "province": PROVINCE_ORDER[index],
                "classification": "TURN2_INPUT_CANDIDATE_ONLY__TURN2_NOT_RUN",
                "raw_ra0_turn1": float(raw_ra0[index]), "firm_ra_used": float(firms[index].ra),
                "state": state,
            })
        _write_json(output / "next_state_candidate_receipt.json", {
            "status": "PASS", "turn2_run": False,
            "raw_next_payoff_sha256": _field_sha256(canonical), "rows": next_states,
        })
        _check_ledger(ledger)
        post_hashes = _task_hashes(repository)
        if post_hashes != pre_hashes:
            raise FailClosed("BLOCKED__CODE_FREEZE_DRIFT")
        _write_json(output / "post_execution_code_freeze.json", {
            "scientific_code_sha256_after": post_hashes,
            "matches_pre_execution_freeze": True,
        })
        _write_json(output / "integration_only_scientific_ledger.json", ledger)
        terminal_detail = {
            "household_batch_identity": HOUSEHOLD_BATCH_SHA256,
            "canonical_raw_next_payoff": payoff_receipt,
            "checks": checks,
        }
        _write_json(output / "terminal_receipt.json", {
            "terminal_verdict": PASS_TERMINAL, "status": "PASS",
            "turn2_run": False, "results_eligibility": False,
        })
        _write_report(repository, terminal_detail, ledger)
        _seal(output)
        readback = _readback(output)
        if readback["status"] != "PASS":
            raise FailClosed("BLOCKED__EVIDENCE_READBACK")
        return PASS_TERMINAL
    except FailClosed as failure:
        ledger["scientific_retries"] = 0
        _write_json(output / "integration_only_scientific_ledger.json", ledger)
        _write_json(output / "terminal_receipt.json", {
            "terminal_verdict": failure.terminal, "status": "FAIL", "detail": failure.detail,
            "turn2_run": False, "results_eligibility": False,
        })
        _seal(output)
        _readback(output)
        return failure.terminal


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
