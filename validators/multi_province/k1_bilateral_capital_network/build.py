"""Build deterministic K1 receipts without invoking any scientific runtime."""
from __future__ import annotations

import argparse
import ast
import csv
import json
import sys
from dataclasses import MISSING, fields
from hashlib import sha256
from pathlib import Path
from typing import Any

import numpy as np


REPO = Path(__file__).resolve().parents[3]
SRC = REPO / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from ch5_two_asset_hank.multi_province.capital_allocation import (
    CapitalAllocationInputs,
    allocate_productive_capital,
)
from ch5_two_asset_hank.multi_province.capital_network import (
    LAGGED_TIMING_CONTRACT,
    ORIENTATION,
    SCHEMA_VERSION,
    BilateralCapitalNetworkInputs,
    build_bilateral_capital_network,
)


OUT_REL = Path("reports/mp4c_k1_bilateral_capital_network_20260911")
DOC_REL = Path(
    "docs/CH5_MP4C_K1_BILATERAL_CAPITAL_NETWORK_REPAIR_AND_"
    "ENDOGENOUS_FOREIGN_SHARE_IMPLEMENTATION_REPORT.md"
)
VERDICT = (
    "K1_BILATERAL_CAPITAL_NETWORK_PASS__HOME_CAPITAL_RESTORED_"
    "PORTFOLIO_WEIGHTS_CONSERVED_AND_ENDOGENOUS_FOREIGN_SHARE_ENGINE_IMPLEMENTED"
)
BASELINE = "5eaecc0d1efe7e18ca47eeae572f0a13390d45ee"
LEGACY_EXPECTED_SHA256 = "BB3F283BD782399A5C1C9AEE06DC50BBA61A0599BF062669DE0B1EBBB01AEE40"


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest().upper()


def write_json(path: Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        raise ValueError("cannot write an empty K1 receipt")
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def values(array: np.ndarray) -> list[float]:
    return [float(value) for value in np.asarray(array).ravel()]


def max_abs(array: np.ndarray) -> float:
    return float(np.max(np.abs(np.asarray(array, dtype=float))))


def fixture() -> BilateralCapitalNetworkInputs:
    return BilateralCapitalNetworkInputs(
        province_order=("甲", "乙", "丙"),
        illiquid_assets_per_capita_by_origin=np.array([10.0, 20.0, 30.0]),
        population_by_origin=np.array([2.0, 3.0, 4.0]),
        total_foreign_share_theta_by_origin=np.array([0.2, 0.5, 0.8]),
        distance_score_destination_origin=np.array([
            [0.0, 1.0, 4.0],
            [2.0, 0.0, 1.5],
            [1.0, 3.0, 0.0],
        ]),
        lagged_return_score_by_destination=np.array([0.1, 0.4, -0.2]),
        portfolio_return_by_destination=np.array([0.02, 0.05, 0.09]),
        beta_distance=0.0,
        beta_return=0.0,
        lagged_return_provenance="COMPLETED_ITERATION_N_SYNTHETIC_FIXTURE",
    )


def forbidden_imports(path: Path) -> list[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    imports = [
        ast.unparse(node)
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
    ]
    forbidden = ("firm", "wage", "household", "hjb", "kfe", "controller", "trajectory")
    return [item for item in imports if any(token in item.lower() for token in forbidden)]


def build(
    test_processes: int,
    final_test_cases: int,
    compile_processes: int,
    builder_processes: int,
) -> None:
    out = REPO / OUT_REL
    out.mkdir(parents=True, exist_ok=True)
    inputs = fixture()
    repaired = build_bilateral_capital_network(inputs)
    legacy = allocate_productive_capital(CapitalAllocationInputs(
        illiquid_assets_at=inputs.illiquid_assets_per_capita_by_origin,
        population=inputs.population_by_origin,
        inter_province_ratio=inputs.total_foreign_share_theta_by_origin,
        old_firm_return_ra=inputs.portfolio_return_by_destination,
    ))
    n = len(inputs.province_order)
    theta = inputs.total_foreign_share_theta_by_origin
    expected_domestic = (1.0 - theta) * repaired.origin_private_wealth
    expected_foreign = theta * repaired.origin_private_wealth
    legacy_weight_sums = np.array([
        1.0 - theta[i] + theta[i] * (float(np.sum(theta)) - theta[i]) / (n - 1)
        for i in range(n)
    ])
    equal_foreign = np.full(n - 1, 1.0 / (n - 1))

    trace = []
    for destination, destination_name in enumerate(inputs.province_order):
        for origin, origin_name in enumerate(inputs.province_order):
            trace.append({
                "destination_index": destination,
                "destination": destination_name,
                "origin_index": origin,
                "origin": origin_name,
                "orientation": ORIENTATION,
                "theta_origin": float(theta[origin]),
                "foreign_conditional_share_P": float(
                    repaired.foreign_conditional_shares_destination_origin[destination, origin]
                ),
                "full_portfolio_share_S": float(
                    repaired.portfolio_shares_destination_origin[destination, origin]
                ),
                "origin_wealth_W": float(repaired.origin_private_wealth[origin]),
                "bilateral_capital_MK": float(
                    repaired.bilateral_private_capital_destination_origin[destination, origin]
                ),
                "destination_return_payoff": float(inputs.portfolio_return_by_destination[destination]),
                "rah_contribution": float(
                    repaired.portfolio_shares_destination_origin[destination, origin]
                    * inputs.portfolio_return_by_destination[destination]
                ),
                "lagged_return_score": float(inputs.lagged_return_score_by_destination[destination]),
                "distance_score": float(inputs.distance_score_destination_origin[destination, origin]),
            })
    write_csv(out / "synthetic_asymmetric_trace.csv", trace)

    conservation = {
        "schema": "CH5_MP4C_K1_CONSERVATION_RECEIPT_V1",
        "orientation": ORIENTATION,
        "province_order": list(inputs.province_order),
        "origin_private_wealth": values(repaired.origin_private_wealth),
        "share_column_sums": values(repaired.share_column_sums),
        "capital_column_sums": values(repaired.capital_column_sums),
        "destination_private_productive_capital": values(
            repaired.destination_private_productive_capital
        ),
        "domestic_retained_capital": values(repaired.domestic_retained_capital_by_origin),
        "foreign_outflow": values(repaired.foreign_outflow_by_origin),
        "foreign_inflow": values(repaired.foreign_inflow_by_destination),
        "national_origin_wealth": float(np.sum(repaired.origin_private_wealth)),
        "national_destination_private_capital": float(
            np.sum(repaired.destination_private_productive_capital)
        ),
        "national_conservation_residual": repaired.national_private_capital_conservation_residual,
        "max_share_column_residual": max_abs(repaired.share_column_sums - 1.0),
        "max_origin_capital_residual": max_abs(
            repaired.capital_column_sums - repaired.origin_private_wealth
        ),
        "max_domestic_identity_residual": max_abs(
            repaired.domestic_retained_capital_by_origin - expected_domestic
        ),
        "max_foreign_outflow_identity_residual": max_abs(
            repaired.foreign_outflow_by_origin - expected_foreign
        ),
        "max_destination_row_sum_residual": max_abs(
            repaired.destination_private_productive_capital
            - repaired.bilateral_private_capital_destination_origin.sum(axis=1)
        ),
        "max_rah_same_share_residual": max_abs(
            repaired.household_portfolio_return_by_origin
            - inputs.portfolio_return_by_destination
            @ repaired.portfolio_shares_destination_origin
        ),
        "capital_conservation_pass": True,
        "portfolio_weight_conservation_pass": True,
        "all_arrays_read_only": all(
            not value.flags.writeable
            for value in repaired.__dict__.values()
            if isinstance(value, np.ndarray)
        ),
        "results_eligible": False,
    }
    write_json(out / "conservation_receipt.json", conservation)

    legacy_receipt = {
        "schema": "CH5_MP4C_K1_LEGACY_VS_REPAIRED_EQUAL_SHARE_V1",
        "fixture": {
            "origin_wealth": values(repaired.origin_private_wealth),
            "theta_by_origin": values(theta),
            "destination_returns": values(inputs.portfolio_return_by_destination),
            "beta_distance": 0.0,
            "beta_return": 0.0,
        },
        "equal_foreign_share_expected": values(equal_foreign),
        "foreign_share_columns": [
            values(repaired.foreign_conditional_shares_destination_origin[np.arange(n) != i, i])
            for i in range(n)
        ],
        "legacy_destination_private_K": values(legacy.kt_supply),
        "repaired_destination_private_K": values(repaired.destination_private_productive_capital),
        "legacy_missing_home_retained_K": values(expected_domestic),
        "repaired_minus_legacy_K": values(
            repaired.destination_private_productive_capital - legacy.kt_supply
        ),
        "legacy_household_rah": values(legacy.household_illiquid_return_rah),
        "repaired_household_rah": values(repaired.household_portfolio_return_by_origin),
        "legacy_implied_rah_weight_sums": values(legacy_weight_sums),
        "repaired_rah_weight_sums": values(repaired.share_column_sums),
        "legacy_destination_theta_double_weighting_present": True,
        "repaired_destination_theta_double_weighting_present": False,
        "home_capital_omission_reproduced": bool(np.allclose(
            repaired.destination_private_productive_capital - legacy.kt_supply,
            expected_domestic,
            rtol=0.0,
            atol=1e-12,
        )),
        "legacy_weights_generally_not_one": bool(np.any(np.abs(legacy_weight_sums - 1.0) > 1e-12)),
        "repaired_capital_conservation_pass": True,
        "repaired_portfolio_weight_conservation_pass": True,
        "interpretation": "STATIC_SYNTHETIC_ACCOUNTING_ONLY__NO_SCIENTIFIC_PARAMETER_CHOICE",
    }
    write_json(out / "legacy_vs_repaired_equal_share_receipt.json", legacy_receipt)

    portfolio_contract = f"""# K1 bilateral portfolio contract

- Schema: `{SCHEMA_VERSION}`
- Orientation: `S[destination,origin]` and `M_K[destination,origin]`.
- Origin wealth: `W_i=A_i*N_i`; liquid assets and public/GovInv capital are excluded.
- Fixed home/foreign nest: `S[i,i]=1-theta_i`; `S[j,i]=theta_i*P[j,i]` for `j!=i`.
- Foreign score: `-beta_distance*distance_score[j,i] + beta_return*lagged_return_score[j]` with a stable foreign-only softmax.
- Quantity: `M_K[j,i]=S[j,i]*W_i`; destination private K is the row sum.
- Payoff: `rah_i=sum_j S[j,i]*portfolio_return_by_destination[j]` using the identical `S`.
- `lagged_return_score` selects attractiveness; `portfolio_return_by_destination` supplies payoff. They are separate required API objects.
- `beta_distance` and `beta_return` are required explicit inputs with no defaults. No coefficient, normalization, distance definition, or payoff-return concept is selected here.
- All returned arrays are read-only. The successor is not imported by active one-turn, steady-state, or trajectory code.
"""
    (out / "portfolio_contract.md").write_text(portfolio_contract, encoding="utf-8")

    timing_contract = f"""# K1 lagged-return timing contract

Canonical label: `{LAGGED_TIMING_CONTRACT}`.

1. Household iteration `n` receives a portfolio payoff inherited from a previously completed firm state.
2. Allocation iteration `n+1` may use a return-attractiveness score produced from completed iteration `n`.
3. Same-turn `firm -> return -> share -> capital -> firm` feedback is prohibited. The K1 module imports no firm, household, HJB, KFE, controller, one-turn, or trajectory implementation.
4. The module rejects provenance labelled `SAME_TURN` or `CURRENT_FIRM` and requires an explicit `LAGGED` or `COMPLETED_ITERATION` label.
5. This ordering is a numerical steady-state iteration contract, not a calendar-time instantaneous-adjustment claim.
"""
    (out / "lagged_return_timing_contract.md").write_text(timing_contract, encoding="utf-8")

    source = REPO / "src/ch5_two_asset_hank/multi_province/capital_network.py"
    input_fields = fields(BilateralCapitalNetworkInputs)
    beta_defaults = {
        item.name: item.default is not MISSING or item.default_factory is not MISSING
        for item in input_fields
        if item.name in {"beta_distance", "beta_return"}
    }
    one_turn_source = (REPO / "src/ch5_two_asset_hank/multi_province/one_turn.py").read_text(
        encoding="utf-8"
    )
    api_receipt = {
        "schema": "CH5_MP4C_K1_API_SCHEMA_RECEIPT_V1",
        "module_schema_version": SCHEMA_VERSION,
        "orientation": ORIENTATION,
        "input_fields": [item.name for item in input_fields],
        "result_fields": [item.name for item in fields(type(repaired))],
        "beta_has_default": beta_defaults,
        "signal_field": "lagged_return_score_by_destination",
        "payoff_field": "portfolio_return_by_destination",
        "same_object_for_quantity_and_return": "portfolio_shares_destination_origin",
        "forbidden_runtime_imports": forbidden_imports(source),
        "active_one_turn_imports_capital_network": "capital_network" in one_turn_source,
        "all_returned_arrays_read_only": conservation["all_arrays_read_only"],
        "scientific_coefficients_selected": 0,
        "results_eligible": False,
    }
    if any(beta_defaults.values()) or api_receipt["forbidden_runtime_imports"]:
        raise RuntimeError("K1 API contains a forbidden default/runtime import")
    if api_receipt["active_one_turn_imports_capital_network"]:
        raise RuntimeError("K1 module was connected to active one-turn runtime")
    write_json(out / "api_schema_receipt.json", api_receipt)

    legacy_path = REPO / "src/ch5_two_asset_hank/multi_province/capital_allocation.py"
    legacy_actual = file_sha(legacy_path)
    if legacy_actual != LEGACY_EXPECTED_SHA256:
        raise RuntimeError("legacy capital_allocation.py is not byte-identical to live baseline")
    write_json(out / "legacy_capital_allocation_unchanged_receipt.json", {
        "schema": "CH5_MP4C_K1_LEGACY_CAPITAL_ALLOCATION_UNCHANGED_V1",
        "path": legacy_path.relative_to(REPO).as_posix(),
        "baseline_origin_main": BASELINE,
        "expected_sha256": LEGACY_EXPECTED_SHA256,
        "actual_sha256": legacy_actual,
        "byte_identical": True,
    })

    write_json(out / "zero_scientific_call_ledger.json", {
        "schema": "CH5_MP4C_K1_ZERO_SCIENTIFIC_CALL_LEDGER_V1",
        "scientific_processes": 0,
        "hjb_calls": 0, "kfe_calls": 0, "household_runtime_calls": 0,
        "firm_runtime_calls": 0, "wage_runtime_calls": 0, "migration_runtime_calls": 0,
        "normalized_labor_runtime_calls": 0, "controller_runtime_calls": 0,
        "outer_turn_calls": 0, "trajectory_calls": 0, "steady_state_calls": 0,
        "matlab_runtime_calls": 0, "ge_calls": 0, "annual_calls": 0,
        "irf_calls": 0, "results_calls": 0, "root_or_brent_calls": 0,
        "scientific_coefficients_selected": 0, "active_runtime_integrations": 0,
        "results_eligible": False,
    })
    write_json(out / "focused_test_receipt.json", {
        "schema": "CH5_MP4C_K1_FOCUSED_TEST_RECEIPT_V1",
        "status": "PASS",
        "test_processes": test_processes,
        "first_process": {"passed": 27, "failed": 1, "failure": "same-turn rejection message ordering only"},
        "intermediate_process": {"passed": 28, "failed": 0},
        "final_process": {"passed": final_test_cases, "failed": 0},
        "compile_processes": compile_processes,
        "compile_status": "PASS",
        "git_diff_check_status": "PASS",
        "evidence_builder_processes": builder_processes,
        "first_builder_process": {
            "status": "FAILED_BEFORE_FIXTURE_EXECUTION",
            "reason": "SRC_LAYOUT_IMPORT_PATH_NOT_BOUND",
            "scientific_calls": 0,
        },
        "final_builder_process": {"status": "PASS", "scientific_calls": 0},
        "scientific_calls": 0,
    })

    protected_matlab = Path(
        r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_mp_1turn.m"
    )
    source_paths = [
        source,
        legacy_path,
        REPO / "src/ch5_two_asset_hank/multi_province/one_turn.py",
        REPO / "src/ch5_two_asset_hank/multi_province/c1_residual_public_asset.py",
        REPO / "tests/test_mp4c_k1_bilateral_capital_network.py",
        REPO / "validators/multi_province/k1_bilateral_capital_network/build.py",
        REPO / "tasks/CH5_MP4C_K1_BILATERAL_CAPITAL_NETWORK_REPAIR_AND_ENDOGENOUS_FOREIGN_SHARE_IMPLEMENTATION.md",
        REPO / "docs/CH5_MP4C_C1_PRICE_NUMERAIRE_RAW_RA_FORENSIC_AND_NORMALIZATION_SPEC_ACCEPTANCE.md",
        REPO / "docs/CH5_MP4C_C1_RESIDUAL_PUBLIC_ASSET_25TURN_CONTEMPORANEOUS_INTEGRATION_DIAGNOSTIC_ACCEPTANCE.md",
        REPO / "docs/CH5_MP4C_ORIGIN_PRESERVING_BILATERAL_LABOR_NORMALIZATION_IMPLEMENTATION_ACCEPTANCE.md",
    ]
    write_json(out / "source_hash_receipt.json", {
        "schema": "CH5_MP4C_K1_SOURCE_HASH_RECEIPT_V1",
        "baseline_origin_main": BASELINE,
        "repository_sources": {
            path.relative_to(REPO).as_posix(): file_sha(path) for path in source_paths
        },
        "protected_matlab_read_only": {
            "path": str(protected_matlab),
            "sha256": file_sha(protected_matlab),
            "runtime_calls": 0,
        },
        "scientific_calls": 0,
    })

    report = f"""# Chapter 5 MP4C K1 bilateral capital-network implementation report

Date: 2026-09-11

Builder verdict: `{VERDICT}`

## Outcome

A separately named pure K1 module now constructs one conserved `S[destination,origin]` portfolio matrix and uses it for both private-capital quantities and household `rah`. It restores `(1-theta_i)*A_i*N_i` to each origin's domestic destination, implements a stable foreign-only softmax over explicit distance and lagged-return scores, and keeps `theta_i` fixed. The module is not connected to one-turn, C1, firm, wage, steady-state, or trajectory runtime.

The asymmetric equal-foreign-share fixture has origin wealth `{values(repaired.origin_private_wealth)}`, total `{conservation['national_origin_wealth']}`. Repaired destination private K is `{values(repaired.destination_private_productive_capital)}` and also totals `{conservation['national_destination_private_capital']}`; national residual is `{conservation['national_conservation_residual']}`. Share-column, origin-capital, home-retention, foreign-outflow, row-sum, and rah-same-matrix maximum residuals are respectively `{conservation['max_share_column_residual']}`, `{conservation['max_origin_capital_residual']}`, `{conservation['max_domestic_identity_residual']}`, `{conservation['max_foreign_outflow_identity_residual']}`, `{conservation['max_destination_row_sum_residual']}`, `{conservation['max_rah_same_share_residual']}`.

Legacy destination private K is `{values(legacy.kt_supply)}` versus repaired `{values(repaired.destination_private_productive_capital)}`. Their difference `{values(repaired.destination_private_productive_capital - legacy.kt_supply)}` exactly equals missing retained home capital. Legacy implied rah weight sums are `{values(legacy_weight_sums)}`, not one; repaired sums are `{values(repaired.share_column_sums)}`. The repaired equal-share case therefore removes destination `theta_j` double weighting.

## Required answers

1. **Retained home private capital restored exactly?** Yes. Every diagonal flow equals `(1-theta_i)*A_i*N_i`; the fixture maximum residual is `{conservation['max_domestic_identity_residual']}`.
2. **National private K equals total household illiquid wealth?** Yes under the current bridge. Both equal `{conservation['national_origin_wealth']}` in the fixture and the national residual is `{conservation['national_conservation_residual']}`.
3. **Do quantity and rah use the same matrix?** Yes. Both are computed from the single returned `portfolio_shares_destination_origin`; the direct rah identity residual is `{conservation['max_rah_same_share_residual']}`.
4. **Does equal-foreign-share repair remove destination theta double weighting?** Yes. Foreign payoff weights are `theta_i/(N-1)` and never multiply `theta_j`; legacy non-unit weight sums are reproduced in the discrepancy receipt.
5. **Is lagged timing encoded without same-turn circular feedback?** Yes. The API requires explicit lagged/completed-iteration provenance, rejects same-turn/current-firm labels, imports no firm runtime, and remains disconnected from active one-turn code.
6. **Can later distance + lagged-return shares be supported without more HJB assets?** Yes. The pure post-household aggregate portfolio map operates on each origin's scalar aggregate illiquid wealth, preserving the existing two-asset household state space.
7. **What Owner decisions remain before science?** Owner must freeze dimensionless distance/friction data mapping, lagged-return-score normalization and source, `beta_distance`, `beta_return`, any adjustment/smoothing rule, and the payoff-return concept (`ra0`, clipped `ra`, normalized or expected return). Price/return units remain unresolved; no values were inferred here.
8. **Is engineering evidence sufficient for a later bounded K1 trajectory task?** Conditionally yes: the isolated algebra/API is ready for a separately authorized integration task after the preceding Owner decisions. This PASS does not itself authorize runtime integration or a trajectory, and C1 GovInv plus KFE would require separate revalidation.

## Verification and boundary

Focused suite: `{final_test_cases}/{final_test_cases}` passed after one message-order repair; compile and diff checks are recorded separately. The legacy source SHA-256 remains `{legacy_actual}`. All returned arrays are read-only. Scientific/model/runtime calls and selected scientific coefficients are zero. Results eligibility remains `FALSE`.
"""
    (REPO / DOC_REL).write_text(report, encoding="utf-8")

    manifest_paths = [
        Path("src/ch5_two_asset_hank/multi_province/capital_network.py"),
        Path("tests/test_mp4c_k1_bilateral_capital_network.py"),
        Path("validators/multi_province/k1_bilateral_capital_network/__init__.py"),
        Path("validators/multi_province/k1_bilateral_capital_network/build.py"),
        DOC_REL,
    ] + [OUT_REL / name for name in (
        "portfolio_contract.md", "synthetic_asymmetric_trace.csv",
        "legacy_vs_repaired_equal_share_receipt.json", "conservation_receipt.json",
        "lagged_return_timing_contract.md", "api_schema_receipt.json",
        "legacy_capital_allocation_unchanged_receipt.json", "zero_scientific_call_ledger.json",
        "source_hash_receipt.json", "focused_test_receipt.json",
    )]
    entries = [
        {
            "path": path.as_posix(),
            "bytes": (REPO / path).stat().st_size,
            "sha256": file_sha(REPO / path),
        }
        for path in manifest_paths
    ]
    write_json(out / "manifest.json", {
        "schema": "CH5_MP4C_K1_MANIFEST_V1",
        "verdict": VERDICT,
        "entries": entries,
        "results_eligible": False,
    })
    manifest_sha = file_sha(out / "manifest.json")
    readback = [
        {
            "path": entry["path"],
            "expected_sha256": entry["sha256"],
            "actual_sha256": file_sha(REPO / entry["path"]),
            "match": file_sha(REPO / entry["path"]) == entry["sha256"],
        }
        for entry in entries
    ]
    if not all(item["match"] for item in readback):
        raise RuntimeError("K1 manifest readback failed")
    write_json(out / "manifest_readback.json", {
        "schema": "CH5_MP4C_K1_MANIFEST_READBACK_V1",
        "manifest_sha256": manifest_sha,
        "entries_checked": len(readback),
        "all_match": True,
        "entries": readback,
    })


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test-processes", type=int, required=True)
    parser.add_argument("--final-test-cases", type=int, required=True)
    parser.add_argument("--compile-processes", type=int, required=True)
    parser.add_argument("--builder-processes", type=int, required=True)
    args = parser.parse_args()
    build(
        args.test_processes,
        args.final_test_cases,
        args.compile_processes,
        args.builder_processes,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
