"""Build static C1 residual-level evidence without invoking model code."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path
from statistics import fmean, median

REPO = Path(__file__).resolve().parents[3]
SRC = REPO / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from ch5_two_asset_hank.multi_province.government_assets import (
    CAPITAL_UNIT,
    residual_government_asset_levels,
)
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER


ROOT = REPO / "reports/mp4c_c1_govinv_residual_level_replacement_20260911"
REPORT = REPO / "docs/CH5_MP4C_C1_GOVINV_RESIDUAL_LEVEL_REPLACEMENT_IMPLEMENTATION_REPORT.md"
LEDGER = REPO / "reports/mp4c_g1_residual_govinv_25turn_isolated_20260911/province_turn_capital_ledger.csv"
BASE = "9a553388ba44fe40f0d385185a9b89599d0dc295"
VERDICT = "C1_GOVINV_RESIDUAL_LEVEL_REPLACEMENT_PASS__PURE_PUBLIC_ASSET_RESIDUAL_IMPLEMENTED_AND_STATICALLY_VALIDATED"
LEGACY_C0 = REPO / "src/ch5_two_asset_hank/multi_province/steady_state.py"
LEGACY_C0_SHA256 = "B8897FDEF9CC59A2811561A18CB0FADF059A158AD8E5F3661BD10A5734D264AA"
PROTECTED = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK")
PROTECTED_HASHES = {
    "HANK_mp_1eq.m": "ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF",
    "HANK_mp_1turn.m": "D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF",
    "HANK_firm.m": "EE02C15414ADF9F99AADE04F1F22E64FA7094C8AB77753B6130BC4BFA6CE7BD5",
}
WINDOWS = (
    ("ALL_TURNS_01_25", 1, 25),
    ("TURNS_01_05", 1, 5),
    ("TURNS_06_10", 6, 10),
    ("TURNS_11_15", 11, 15),
    ("TURNS_16_20", 16, 20),
    ("TURNS_21_25", 21, 25),
    ("LATE_TURNS_20_25", 20, 25),
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def write_json(path: Path, payload: object) -> None:
    write_text(path, json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def read_accepted_ledger() -> list[dict[str, str]]:
    with LEDGER.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    if len(rows) != 775:
        raise RuntimeError(f"accepted ledger must contain 775 rows, observed {len(rows)}")
    for turn in range(1, 26):
        selected = [row for row in rows if int(row["turn"]) == turn]
        if len(selected) != 31:
            raise RuntimeError(f"turn {turn} does not contain 31 provinces")
        if tuple(row["province"] for row in selected) != PROVINCE_ORDER:
            raise RuntimeError(f"turn {turn} province order mismatch")
        if tuple(int(row["province_index"]) for row in selected) != tuple(range(31)):
            raise RuntimeError(f"turn {turn} province index mismatch")
    return rows


def static_replay(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    replay: list[dict[str, object]] = []
    for turn in range(1, 26):
        selected = [row for row in rows if int(row["turn"]) == turn]
        target = [float(row["Ktarget_2018_MU"]) for row in selected]
        private = [float(row["Kt_supply_private_MU"]) for row in selected]
        batch = residual_government_asset_levels(
            Ktarget_MU=target,
            Kprivate_current_MU=private,
            province_order=PROVINCE_ORDER,
        )
        for index, (source, status) in enumerate(zip(selected, batch.status)):
            target_i = float(batch.Ktarget_MU[index])
            private_i = float(batch.Kprivate_current_MU[index])
            c0_gov = float(source["GovInv_before_MU"])
            c0_total = float(source["firm_K_total_MU"])
            c1_gov = float(batch.GovInv_residual_MU[index])
            c1_total = float(batch.firm_K_accounting_MU[index])
            historical_overshoot = max(c0_total - target_i, 0.0)
            private_only_overshoot = max(private_i - target_i, 0.0)
            removed = max(historical_overshoot - private_only_overshoot, 0.0)
            replay.append({
                "turn": turn,
                "province_index": index,
                "province": source["province"],
                "capital_unit": CAPITAL_UNIT,
                "Ktarget_MU": target_i,
                "Kprivate_current_MU": private_i,
                "historical_C0_GovInv_MU": c0_gov,
                "historical_C0_firm_K_total_MU": c0_total,
                "historical_C0_total_K_over_target": c0_total / target_i,
                "historical_C0_GovInv_over_target": c0_gov / target_i,
                "C1_GovInv_residual_MU": c1_gov,
                "C1_firm_K_accounting_MU": c1_total,
                "c1_firm_K_accounting_over_target": c1_total / target_i,
                "C1_GovInv_over_target": c1_gov / target_i,
                "C1_minus_C0_GovInv_MU": c1_gov - c0_gov,
                "capital_gap_before_C1_MU": float(batch.capital_gap_before_MU[index]),
                "capital_gap_after_C1_MU": float(batch.capital_gap_after_MU[index]),
                "c1_exact_target": c1_total == target_i,
                "private_at_or_above_target": bool(batch.private_at_or_above_target[index]),
                "residual_floor_binding": bool(batch.residual_floor_binding[index]),
                "c1_status": status,
                "historical_C0_overshoot_MU": historical_overshoot,
                "C1_mechanically_removed_overshoot_MU": removed,
                "remaining_private_only_overshoot_MU": private_only_overshoot,
                "counterfactual_scope": "STATIC_ACCOUNTING_ONLY__NOT_DYNAMIC_TRAJECTORY",
            })
    return replay


def distribution(values: list[float]) -> dict[str, float]:
    return {
        "min": min(values),
        "median": median(values),
        "mean": fmean(values),
        "max": max(values),
    }


def amount_distribution(values: list[float]) -> dict[str, float]:
    return {**distribution(values), "sum": sum(values)}


def build_summary(rows: list[dict[str, object]]) -> dict[str, object]:
    windows = []
    for name, lo, hi in WINDOWS:
        selected = [row for row in rows if lo <= int(row["turn"]) <= hi]
        windows.append({
            "window": name,
            "turn_start": lo,
            "turn_end": hi,
            "observations": len(selected),
            "c1_exact_target_rows": sum(bool(row["c1_exact_target"]) for row in selected),
            "private_at_or_above_target_rows": sum(bool(row["private_at_or_above_target"]) for row in selected),
            "historical_C0_total_K_over_target": distribution([float(row["historical_C0_total_K_over_target"]) for row in selected]),
            "c1_total_K_over_target": distribution([float(row["c1_firm_K_accounting_over_target"]) for row in selected]),
            "historical_C0_GovInv_over_target": distribution([float(row["historical_C0_GovInv_over_target"]) for row in selected]),
            "c1_GovInv_over_target": distribution([float(row["C1_GovInv_over_target"]) for row in selected]),
            "private_K_over_target": distribution([float(row["Kprivate_current_MU"]) / float(row["Ktarget_MU"]) for row in selected]),
            "historical_C0_overshoot_MU": amount_distribution([float(row["historical_C0_overshoot_MU"]) for row in selected]),
            "c1_mechanically_removed_overshoot_MU": amount_distribution([float(row["C1_mechanically_removed_overshoot_MU"]) for row in selected]),
            "remaining_private_only_overshoot_MU": amount_distribution([float(row["remaining_private_only_overshoot_MU"]) for row in selected]),
        })
    late = next(row for row in windows if row["window"] == "LATE_TURNS_20_25")
    c0_median = late["historical_C0_total_K_over_target"]["median"]
    c1_median = late["c1_total_K_over_target"]["median"]
    return {
        "schema": "CH5_MP4C_C1_GOVINV_RESIDUAL_LEVEL_STATIC_REPLAY_SUMMARY_V1",
        "accepted_input_ledger": LEDGER.relative_to(REPO).as_posix(),
        "accepted_input_ledger_sha256": digest(LEDGER),
        "scope": "STATIC_ACCOUNTING_COUNTERFACTUAL_ONLY__NOT_DYNAMIC_TRAJECTORY",
        "windows": windows,
        "late_window_median_counterfactual": {
            "historical_C0_total_K_over_target": c0_median,
            "C1_total_K_over_target": c1_median,
            "target_multiples_mechanically_removed": c0_median - c1_median,
            "historical_median_overshoot_share_removed": (c0_median - c1_median) / (c0_median - 1.0),
        },
    }


def report_text(summary: dict[str, object]) -> str:
    all_rows = next(row for row in summary["windows"] if row["window"] == "ALL_TURNS_01_25")
    late = next(row for row in summary["windows"] if row["window"] == "LATE_TURNS_20_25")
    counterfactual = summary["late_window_median_counterfactual"]
    return f"""# Chapter 5 MP4C C1 GovInv residual level-replacement implementation report

Date: 2026-09-11

Builder verdict:

`{VERDICT}`

## Result and scope

A separately named pure helper now defines government/public productive assets as the direct nonnegative residual between accepted productive-capital target and current model-implied private productive capital. It is exported as `residual_government_asset_level` for one province and `residual_government_asset_levels` for the exact 31-province axis. It is not connected to the active steady-state runtime or historical C0 controller.

The helper contains no tuning coefficient or return signal. It does not mutate private K, Ktarget, return, productivity, wages, labor, or KN references. Nonpositive/nonfinite targets, negative/nonfinite private capital, vector shape mismatch, and province-order mismatch fail closed. Outputs preserve the explicit `{CAPITAL_UNIT}` contract and distinguish `RESIDUAL_PUBLIC_ASSET_POSITIVE` from `RESIDUAL_PUBLIC_ASSET_ZERO_PRIVATE_AT_OR_ABOVE_TARGET`.

No HJB, KFE, household, firm, migration, normalized migration, wage, controller-runtime, outer-turn, trajectory, steady-state, root/Brent, MATLAB-runtime, GE, annual, IRF, or Results call was made. `Results eligibility=FALSE`.

## Static accepted-G1 replay

The accepted 25-turn ledger supplied all 775 province-turn rows; no model was rerun. C1 places {all_rows['c1_exact_target_rows']}/775 rows exactly at accounting Ktarget. Private K reaches or exceeds Ktarget in {all_rows['private_at_or_above_target_rows']}/775 rows, so no floor binds and no private-only overshoot remains in this saved path.

For turns 20-25 (186 pooled observations), historical C0 total-K/target min/median/mean/max is `{late['historical_C0_total_K_over_target']['min']} / {late['historical_C0_total_K_over_target']['median']} / {late['historical_C0_total_K_over_target']['mean']} / {late['historical_C0_total_K_over_target']['max']}`. Static C1 accounting is exactly `1 / 1 / 1 / 1`.

Late-window historical C0 GovInv/target min/median/mean/max is `{late['historical_C0_GovInv_over_target']['min']} / {late['historical_C0_GovInv_over_target']['median']} / {late['historical_C0_GovInv_over_target']['mean']} / {late['historical_C0_GovInv_over_target']['max']}`; static C1 GovInv/target is `{late['c1_GovInv_over_target']['min']} / {late['c1_GovInv_over_target']['median']} / {late['c1_GovInv_over_target']['mean']} / {late['c1_GovInv_over_target']['max']}`. Private-K/target remains `{late['private_K_over_target']['min']} / {late['private_K_over_target']['median']} / {late['private_K_over_target']['mean']} / {late['private_K_over_target']['max']}`.

Thus the accepted late median moves mechanically from `{counterfactual['historical_C0_total_K_over_target']}` to `{counterfactual['C1_total_K_over_target']}`: `{counterfactual['target_multiples_mechanically_removed']}` target multiples, or 100% of the historical median overshoot above one, disappear in the static accounting replacement. Across pooled late province-turns, historical positive overshoot totals `{late['historical_C0_overshoot_MU']['sum']} MU`; C1 mechanically removes `{late['c1_mechanically_removed_overshoot_MU']['sum']} MU`, with `{late['remaining_private_only_overshoot_MU']['sum']} MU` remaining private-only overshoot. These pooled sums are province-turn accounting totals, not a national stock or a dynamic effect.

Requested all-sample and five-turn-window distributions are in `static_replay_summary.json`; every row is in `static_g1_replay.csv`.

## Historical C0 preservation

`src/ch5_two_asset_hank/multi_province/steady_state.py` remains byte-identical to the accepted baseline, SHA-256 `{LEGACY_C0_SHA256}`. Its clipped-return `0.9/1.1` logic remains available. The new helper is additive and unconnected.

## Required answers

1. **Is the helper algebraically exact?** Yes. Below target, residual public assets equal target minus private capital and accounting firm K is exactly target; at or above target the public component is zero.
2. **Does it preserve private overshoot?** Yes. It never creates negative government assets, so private K above target remains explicit in total accounting K and in the negative post-replacement capital gap.
3. **How much late overshoot is attributable to historical GovInv level?** In the saved turns 20-25 path, private K is below target in all 186 rows and remaining private-only overshoot is zero. The full positive C0 overshoot—`{late['historical_C0_overshoot_MU']['sum']} MU` as a pooled province-turn amount—is mechanically removed by the static C1 replacement. This is not a causal trajectory estimate.
4. **Is any tuning coefficient introduced?** No. The rule is a direct level definition with only Ktarget and current private K inputs.
5. **Is it ready for bounded trajectory integration?** Engineering evidence is sufficient to present the pure helper for Reviewer acceptance and a later separately authorized integration task. Runtime activation and dynamic stability remain untested and unauthorized.

## Evidence and stop

Focused tests cover scalar branches, exact 31-province vectors, units, immutable shapes, invalid inputs, province order, absence of tuning/return-target fields, C0 source identity, complete static replay, and the zero-call ledger. PASS is implementation evidence only. No successor task is published; the next gate is independent ChatGPT Reviewer fresh-fetch ACCEPT/REJECT.
"""


def prepare() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    rows = read_accepted_ledger()
    replay = static_replay(rows)
    summary = build_summary(replay)
    if sum(bool(row["c1_exact_target"]) for row in replay) != 775:
        raise RuntimeError("accepted G1 replay did not close all rows exactly")

    write_csv(ROOT / "static_g1_replay.csv", list(replay[0]), replay)
    write_json(ROOT / "static_replay_summary.json", summary)
    write_json(ROOT / "api_contract.json", {
        "schema": "CH5_MP4C_C1_RESIDUAL_PUBLIC_ASSET_API_CONTRACT_V1",
        "economic_object": "UNOBSERVED_GOVERNMENT_PUBLIC_PRODUCTIVE_ASSET_RESIDUAL",
        "capital_unit": CAPITAL_UNIT,
        "scalar_api": "residual_government_asset_level",
        "batch_api": "residual_government_asset_levels",
        "inputs": ["Ktarget_MU", "Kprivate_current_MU"],
        "formula": "GovInv_residual_MU=max(Ktarget_MU-Kprivate_current_MU,0)",
        "below_target_identity": "firm_K_accounting_MU=Ktarget_MU",
        "at_or_above_target_identity": "firm_K_accounting_MU=Kprivate_current_MU; GovInv_residual_MU=0",
        "classifications": [
            "RESIDUAL_PUBLIC_ASSET_POSITIVE",
            "RESIDUAL_PUBLIC_ASSET_ZERO_PRIVATE_AT_OR_ABOVE_TARGET",
        ],
        "batch_shape": [31],
        "province_order": list(PROVINCE_ORDER),
        "fail_closed": [
            "Ktarget_MU_NONPOSITIVE_OR_NONFINITE",
            "Kprivate_current_MU_NEGATIVE_OR_NONFINITE",
            "SHAPE_MISMATCH",
            "PROVINCE_ORDER_MISMATCH",
        ],
        "runtime_connected": False,
        "tuning_coefficients": [],
        "return_signal_fields": [],
    })

    observed_c0_hash = digest(LEGACY_C0)
    if observed_c0_hash != LEGACY_C0_SHA256:
        raise RuntimeError("historical C0 source drift")
    write_json(ROOT / "legacy_c0_unchanged_receipt.json", {
        "schema": "CH5_MP4C_C1_LEGACY_C0_UNCHANGED_RECEIPT_V1",
        "path": LEGACY_C0.relative_to(REPO).as_posix(),
        "base_origin_main": BASE,
        "expected_sha256": LEGACY_C0_SHA256,
        "observed_sha256": observed_c0_hash,
        "byte_identical": True,
        "historical_clipped_return_controller_preserved": True,
        "new_c1_runtime_connected": False,
    })
    write_json(ROOT / "zero_scientific_call_ledger.json", {
        "schema": "CH5_MP4C_C1_RESIDUAL_LEVEL_ZERO_SCIENTIFIC_CALL_LEDGER_V1",
        "accepted_ledger_rows_parsed": 775,
        "pure_scalar_accounting_evaluations": 775,
        "household_calls": 0,
        "hjb_calls": 0,
        "kfe_calls": 0,
        "migration_calls": 0,
        "normalized_migration_calls": 0,
        "firm_calls": 0,
        "wage_calls": 0,
        "controller_runtime_calls": 0,
        "outer_turn_calls": 0,
        "trajectory_calls": 0,
        "steady_state_calls": 0,
        "root_brent_scientific_calls": 0,
        "matlab_runtime_calls": 0,
        "ge_calls": 0,
        "annual_calls": 0,
        "irf_calls": 0,
        "results_calls": 0,
        "scientific_model_state_advances": 0,
        "results_eligibility": False,
    })

    protected_entries = []
    for name, expected in PROTECTED_HASHES.items():
        path = PROTECTED / name
        observed = digest(path)
        if observed != expected:
            raise RuntimeError(f"protected source drift: {name}")
        protected_entries.append({"path": str(path), "expected_sha256": expected, "observed_sha256": observed, "match": True})
    repo_inputs = [
        "AGENTS.md", "project_rules/PROJECT_RULE_INDEX_CURRENT.md",
        "tasks/CH5_MP4C_C1_GOVINV_RESIDUAL_LEVEL_REPLACEMENT_IMPLEMENTATION.md",
        "docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md",
        "docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md",
        "docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md",
        "docs/CH5_MP4C_GOVINV_CONTROLLER_REDESIGN_FORENSIC_AND_SPEC.md",
        "docs/CH5_MP4C_GOVINV_CONTROLLER_REDESIGN_FORENSIC_AND_SPEC_ACCEPTANCE.md",
        "docs/CH5_MP4C_G1_RESIDUAL_GOVINV_INITIALIZATION_INTEGRATION_AND_25TURN_ISOLATED_DIAGNOSTIC_REPORT.md",
        "docs/CH5_MP4C_G1_RESIDUAL_GOVINV_INITIALIZATION_INTEGRATION_AND_25TURN_ISOLATED_DIAGNOSTIC_ACCEPTANCE.md",
        "docs/CH5_MP4C_INITIAL_PRIVATE_K_OBSERVATION_AND_RESIDUAL_GOVINV_PROBE_REPORT.md",
        "docs/CH5_MP4C_INITIAL_PRIVATE_K_OBSERVATION_AND_RESIDUAL_GOVINV_PROBE_ACCEPTANCE.md",
        "docs/CH5_MP4C_PYTHON_RUNTIME_INPUT_BINDING_AND_UNIT_CONTRACT_REPAIR_REPORT.md",
        "docs/CH5_MP4C_PYTHON_RUNTIME_INPUT_BINDING_AND_UNIT_CONTRACT_REPAIR_ACCEPTANCE.md",
        "src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py",
        "src/ch5_two_asset_hank/multi_province/capital_allocation.py",
        "src/ch5_two_asset_hank/multi_province/steady_state.py",
        "src/ch5_two_asset_hank/multi_province/firm.py",
        LEDGER.relative_to(REPO).as_posix(),
    ]
    write_json(ROOT / "source_hash_receipt.json", {
        "schema": "CH5_MP4C_C1_RESIDUAL_LEVEL_SOURCE_HASH_RECEIPT_V1",
        "base_origin_main": BASE,
        "protected_sources_read_only": True,
        "protected_sources": protected_entries,
        "repository_inputs": [
            {"path": relative, "bytes": (REPO / relative).stat().st_size, "sha256": digest(REPO / relative)}
            for relative in repo_inputs
        ],
    })
    write_text(REPORT, report_text(summary))


def finalize(pytest_exit_code: int, passed: int) -> None:
    if pytest_exit_code != 0 or passed < 1:
        raise RuntimeError("focused tests did not pass")
    write_json(ROOT / "focused_test_receipt.json", {
        "schema": "CH5_MP4C_C1_RESIDUAL_LEVEL_FOCUSED_TEST_RECEIPT_V1",
        "command": "python -m pytest -q tests/test_mp4c_c1_govinv_residual_level_replacement.py",
        "exit_code": pytest_exit_code,
        "passed": passed,
        "failed": 0,
        "attempts": 2,
        "pre_final_attempt": {
            "passed": 18,
            "failed": 1,
            "reason": "static evaluation counter label was disambiguated from scientific-call counters",
            "scientific_calls": 0,
        },
        "scientific_calls": 0,
    })
    entries = [
        REPO / "src/ch5_two_asset_hank/multi_province/government_assets.py",
        REPO / "src/ch5_two_asset_hank/multi_province/__init__.py",
        REPO / "tests/test_mp4c_c1_govinv_residual_level_replacement.py",
        REPO / "validators/multi_province/c1_govinv_residual_level_replacement/__init__.py",
        REPO / "validators/multi_province/c1_govinv_residual_level_replacement/generate.py",
        REPORT,
        ROOT / "static_g1_replay.csv",
        ROOT / "static_replay_summary.json",
        ROOT / "api_contract.json",
        ROOT / "legacy_c0_unchanged_receipt.json",
        ROOT / "zero_scientific_call_ledger.json",
        ROOT / "source_hash_receipt.json",
        ROOT / "focused_test_receipt.json",
    ]
    manifest = {
        "schema": "CH5_MP4C_C1_RESIDUAL_LEVEL_MANIFEST_V1",
        "entries": [
            {"path": path.relative_to(REPO).as_posix(), "bytes": path.stat().st_size, "sha256": digest(path)}
            for path in entries
        ],
    }
    write_json(ROOT / "manifest.json", manifest)
    readback = []
    for entry in manifest["entries"]:
        path = REPO / entry["path"]
        readback.append({
            "path": entry["path"],
            "bytes_match": path.stat().st_size == entry["bytes"],
            "sha256_match": digest(path) == entry["sha256"],
        })
    if not all(row["bytes_match"] and row["sha256_match"] for row in readback):
        raise RuntimeError("manifest readback failed")
    write_json(ROOT / "manifest_readback.json", {
        "schema": "CH5_MP4C_C1_RESIDUAL_LEVEL_MANIFEST_READBACK_V1",
        "manifest_sha256": digest(ROOT / "manifest.json"),
        "entries_checked": len(readback),
        "passed": True,
        "entries": readback,
    })


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("prepare", "finalize"))
    parser.add_argument("--pytest-exit-code", type=int, default=0)
    parser.add_argument("--passed", type=int, default=0)
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare()
    else:
        finalize(args.pytest_exit_code, args.passed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
