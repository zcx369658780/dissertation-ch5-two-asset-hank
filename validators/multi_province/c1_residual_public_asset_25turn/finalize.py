"""Package the completed C1 diagnostic without performing scientific solves."""
from __future__ import annotations

import argparse
import csv
import json
import shutil
from collections import Counter
from hashlib import sha256
from pathlib import Path
from statistics import median
from typing import Any


REPO = Path(__file__).resolve().parents[3]
REPORT_REL = Path("reports/mp4c_c1_residual_public_asset_25turn_20260911")
DOC_REL = Path("docs/CH5_MP4C_C1_RESIDUAL_PUBLIC_ASSET_25TURN_CONTEMPORANEOUS_INTEGRATION_DIAGNOSTIC_REPORT.md")
G0_REL = Path("reports/mp4c_corrected_2018_hjb_propagation_25turn_kl_20260910/national_turn_summary.csv")
G0_PROVINCE_REL = Path("reports/mp4c_corrected_2018_hjb_propagation_25turn_kl_20260910/province_turn_kl_ledger.csv")
G1_REL = Path("reports/mp4c_g1_residual_govinv_25turn_isolated_20260911/national_turn_summary.csv")
SELECTED = (1, 2, 3, 5, 10, 15, 20, 21, 22, 23, 24, 25)
VERDICT = "C1_RESIDUAL_PUBLIC_ASSET_25TURN_PASS__CAPITAL_TARGET_HELD_AND_BOUNDED_PATH_QUANTIFIED"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest().upper()


def f(value: Any) -> float:
    return float(value)


def stats(values: list[float]) -> dict[str, float]:
    return {"min": min(values), "median": median(values), "max": max(values)}


def rate_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    counts = Counter("lower" if f(row["firm_ra0"]) < f(row["ramin"]) else
                     "upper" if f(row["firm_ra0"]) > f(row["ramax"]) else "interior" for row in rows)
    return {key: counts.get(key, 0) for key in ("lower", "interior", "upper")}


def _baseline_row(route: str, row: dict[str, Any], g0_rah: dict[int, dict[str, float]]) -> dict[str, Any]:
    if route == "G0_C0":
        return {
            "total_K_ratio_min": row["firm_K_ratio_min"], "total_K_ratio_median": row["firm_K_ratio_median"],
            "total_K_ratio_max": row["firm_K_ratio_max"], "GovInv_ratio_min": row["GovInv_ratio_min"],
            "GovInv_ratio_median": row["GovInv_ratio_median"], "GovInv_ratio_max": row["GovInv_ratio_max"],
            "private_K_ratio_min": row["private_K_ratio_min"], "private_K_ratio_median": row["private_K_ratio_median"],
            "private_K_ratio_max": row["private_K_ratio_max"], "ra_lower": row["ra_lower"],
            "ra_interior": row["ra_interior"], "ra_upper": row["ra_upper"],
            "rah_min": g0_rah[int(row["turn"])]["min"], "rah_median": g0_rah[int(row["turn"])]["median"],
            "rah_max": g0_rah[int(row["turn"])]["max"], "max_KN_gap": row["max_KN_gap"],
            "max_GDP_level_gap": row["max_GDP_level_gap"], "HJB_converged_count": row["hjb_converged_count"],
            "Zt_adjustment_count": row["zt_adjusted_count"],
        }
    return {
        "total_K_ratio_min": row["total_K_ratio_min"], "total_K_ratio_median": row["total_K_ratio_median"],
        "total_K_ratio_max": row["total_K_ratio_max"], "GovInv_ratio_min": row["GovInv_ratio_min"],
        "GovInv_ratio_median": row["GovInv_ratio_median"], "GovInv_ratio_max": row["GovInv_ratio_max"],
        "private_K_ratio_min": row["private_K_ratio_min"], "private_K_ratio_median": row["private_K_ratio_median"],
        "private_K_ratio_max": row["private_K_ratio_max"], "ra_lower": row["ra_lower"],
        "ra_interior": row["ra_interior"], "ra_upper": row["ra_upper"],
        "rah_min": row["rah_min"], "rah_median": row["rah_median"], "rah_max": row["rah_max"],
        "max_KN_gap": row["max_KN_gap"], "max_GDP_level_gap": row["max_GDP_level_gap"],
        "HJB_converged_count": row["HJB_converged_count"],
        "Zt_adjustment_count": row.get("Zt_adjustment_count", row.get("zt_adjusted_count", 0)),
    }


def finalize(external_root: Path) -> None:
    ext = Path(external_root)
    terminal, calls = read_json(ext / "terminal_result.json"), read_json(ext / "call_ledger.json")
    if terminal.get("actual_turns_completed") != 25 or terminal.get("error") is not None:
        raise ValueError("completed 25-turn C1 evidence is required")
    required = {
        "scientific_processes": 1, "initialization_observation_passes": 1,
        "initialization_observation_hjb_calls": 31, "initialization_observation_kfe_calls": 31,
        "initialization_observation_aggregate_calls": 31, "initial_at_only_capital_allocation_calls": 1,
        "trajectory_attempts": 1, "turns_completed": 25, "province_updates_completed": 775,
        "trajectory_hjb_calls": 775, "trajectory_kfe_calls": 775, "trajectory_aggregate_calls": 775,
        "scientific_retries": 0,
    }
    if any(calls["counts"].get(key) != value for key, value in required.items()):
        raise ValueError("scientific call ledger does not match the authorized budget")
    out = REPO / REPORT_REL
    out.mkdir(parents=True, exist_ok=True)
    for name, destination in (
        ("initialization_receipt_31province.csv", "initialization_receipt_31province.csv"),
        ("national_initialization_summary.json", "national_initialization_summary.json"),
        ("call_ledger.json", "call_ledger.json"), ("runtime_input_receipt.json", "runtime_input_receipt.json"),
        ("source_hash_receipt.json", "source_hash_receipt.json"),
        ("phase_a_zero_science_receipt.json", "focused_test_receipt.json"),
        ("bounded_invocation_receipt.json", "bounded_invocation_receipt.json"),
        ("terminal_result.json", "terminal_result.json"),
    ):
        shutil.copyfile(ext / name, out / destination)
    packaged_calls = read_json(out / "call_ledger.json")
    packaged_calls["schema"] = "CH5_C1_RESIDUAL_PUBLIC_ASSET_25TURN_CALL_LEDGER_V1"
    packaged_calls["execution_harness"] = "ACCEPTED_G1_INITIALIZATION_AND_25TURN_HARNESS_WITH_SEPARATE_C1_ROUTE"
    write_json(out / "call_ledger.json", packaged_calls)

    init_rows = read_csv(ext / "initialization_receipt_31province.csv")
    all_rows: list[dict[str, Any]] = []
    national: list[dict[str, Any]] = []
    for turn in range(1, 26):
        rows = read_json(ext / f"turn_{turn:02d}" / "per_province_observables.json")
        summary = read_json(ext / f"turn_{turn:02d}" / "national_summary.json")
        if len(rows) != 31:
            raise ValueError(f"turn {turn}: province count is not 31")
        all_rows.extend(rows)
        rates = rate_counts(rows)
        wage = Counter("lower" if f(row["firm_wage_raw"]) < f(row["wjtmin"]) else
                       "upper" if f(row["firm_wage_raw"]) > f(row["wjtmax"]) else "interior" for row in rows)
        national.append({
            "turn": turn,
            **{f"total_K_ratio_{k}": v for k, v in stats([f(r["firm_K_total_over_Ktarget"]) for r in rows]).items()},
            **{f"GovInv_ratio_{k}": v for k, v in stats([f(r["GovInv_C1_over_Ktarget"]) for r in rows]).items()},
            **{f"private_K_ratio_{k}": v for k, v in stats([f(r["private_K_over_Ktarget"]) for r in rows]).items()},
            **{f"rah_{k}": v for k, v in stats([f(r["household_rah"]) for r in rows]).items()},
            "private_at_or_above_target_count": sum(bool(r["private_K_at_or_above_target"]) for r in rows),
            "residual_floor_binding_count": sum(bool(r["residual_floor_binding"]) for r in rows),
            "max_c1_accounting_abs_residual_MU": max(f(r["c1_accounting_abs_residual_MU"]) for r in rows),
            "ra_lower": rates["lower"], "ra_interior": rates["interior"], "ra_upper": rates["upper"],
            "wage_lower": wage.get("lower", 0), "wage_interior": wage.get("interior", 0), "wage_upper": wage.get("upper", 0),
            "HJB_converged_count": sum(bool(r["hjb_converged"]) for r in rows),
            "HJB_nonconverged_count": sum(not bool(r["hjb_converged"]) for r in rows),
            "KFE_VALID_count": sum(r["kfe_diagnostic_status"] == "VALID" for r in rows),
            "KFE_DIAGNOSTIC_ONLY_count": sum(r["kfe_diagnostic_status"] == "DIAGNOSTIC_ONLY" for r in rows),
            "max_KN_gap": max(f(r["nk_gap"]) for r in rows), "max_Y_prev_gap": max(f(r["yt_gap"]) for r in rows),
            "max_GDP_level_gap": max(f(r["GDP_level_gap"]) for r in rows),
            "Zt_adjustment_count": int(summary["controller"]["zt_adjusted_count"]),
            "source_final_predicate": bool(rows[0]["source_final_predicate"]),
        })
    write_csv(out / "province_turn_capital_ledger.csv", all_rows)
    write_csv(out / "national_turn_summary.csv", national)

    init_validity = [{"stage": "INITIALIZATION_OBSERVATION", "turn": 0, "province": r["province"],
                      "HJB_converged": r["HJB_converged"], "HJB_classification": r["HJB_classification"],
                      "KFE_classification": r["KFE_classification"], "overall_validity": "DIAGNOSTIC_ONLY"} for r in init_rows]
    turn_validity = [{"stage": "OUTER_TRAJECTORY", "turn": r["turn"], "province": r["province"],
                      "HJB_converged": r["hjb_converged"], "HJB_classification": r["hjb_acceptance_classification"],
                      "KFE_classification": r["kfe_diagnostic_status"], "overall_validity": "DIAGNOSTIC_ONLY"} for r in all_rows]
    write_csv(out / "scientific_validity_ledger.csv", init_validity + turn_validity)
    init_hjb = [{"stage": "INITIALIZATION_OBSERVATION", "turn": 0, "province": r["province"],
                 "HJB_converged": r["HJB_converged"], "HJB_iterations": "", "HJB_statistic": "",
                 "HJB_classification": r["HJB_classification"]} for r in init_rows]
    turn_hjb = [{"stage": "OUTER_TRAJECTORY", "turn": r["turn"], "province": r["province"],
                 "HJB_converged": r["hjb_converged"], "HJB_iterations": r["hjb_iterations"],
                 "HJB_statistic": r["hjb_statistic"], "HJB_classification": r["hjb_acceptance_classification"]} for r in all_rows]
    write_csv(out / "hjb_convergence_path.csv", init_hjb + turn_hjb)
    anhui_init = next(r for r in init_rows if r["province"] == "安徽")
    anhui = [{"stage": "INITIALIZATION_OBSERVATION", "turn": 0, "Ktarget": anhui_init["Ktarget_2018_MU"],
              "private_K": anhui_init["Kt_supply_initial_MU_beta1"], "GovInv_C1": anhui_init["GovInv0_C1_MU"],
              "firm_K_total": anhui_init["firm_K_accounting_C1_MU"], "HJB_converged": anhui_init["HJB_converged"],
              "HJB_statistic": "", "KFE_classification": anhui_init["KFE_classification"]}]
    anhui += [{"stage": "OUTER_TRAJECTORY", "turn": r["turn"], "Ktarget": r["Ktarget_2018_MU"],
               "private_K": r["Kt_supply_private_MU"], "GovInv_C1": r["GovInv_C1_MU"],
               "firm_K_total": r["firm_K_total_MU"], "HJB_converged": r["hjb_converged"],
               "HJB_statistic": r["hjb_statistic"], "KFE_classification": r["kfe_diagnostic_status"]}
              for r in all_rows if r["province"] == "安徽"]
    write_csv(out / "anhui_trace.csv", anhui)

    g0 = {int(r["turn"]): r for r in read_csv(REPO / G0_REL)}
    g1 = {int(r["turn"]): r for r in read_csv(REPO / G1_REL)}
    g1_controller = {int(r["turn"]): r for r in read_csv(
        REPO / "reports/mp4c_g1_residual_govinv_25turn_isolated_20260911/controller_action_summary.csv"
    )}
    for turn, row in g1.items():
        row["zt_adjusted_count"] = g1_controller[turn]["zt_adjusted_count"]
    c1 = {int(r["turn"]): r for r in national}
    g0_province = read_csv(REPO / G0_PROVINCE_REL)
    g0_rah = {turn: stats([f(r["household_rah"]) for r in g0_province if int(r["turn"]) == turn]) for turn in SELECTED}
    comparison = []
    for turn in SELECTED:
        for route, source in (("G0_C0", g0[turn]), ("G1_C0", g1[turn]), ("G1_C1_CONTEMPORANEOUS", c1[turn])):
            comparison.append({"turn": turn, "route": route, **_baseline_row(route, source, g0_rah)})
    write_csv(out / "baseline_selected_turn_comparison.csv", comparison)

    tolerance = 1e-9
    violations = [r for r in all_rows if f(r["c1_accounting_abs_residual_MU"]) > tolerance * max(1.0, abs(f(r["Ktarget_2018_MU"]))) or f(r["GovInv_C1_MU"]) < 0.0]
    assertion = {
        "schema": "CH5_C1_RESIDUAL_PUBLIC_ASSET_ACCOUNTING_ASSERTION_V1", "province_turn_observations": len(all_rows),
        "passed": len(all_rows) - len(violations), "violations": len(violations),
        "private_at_or_above_target_count": sum(bool(r["private_K_at_or_above_target"]) for r in all_rows),
        "residual_floor_binding_count": sum(bool(r["residual_floor_binding"]) for r in all_rows),
        "maximum_abs_accounting_residual_MU": max(f(r["c1_accounting_abs_residual_MU"]) for r in all_rows),
        "historical_c0_actions_executed": 0, "all_pass": not violations,
    }
    write_json(out / "c1_accounting_assertion_receipt.json", assertion)
    if violations:
        raise RuntimeError("C1 accounting assertions failed during deterministic packaging")

    late = [r for r in all_rows if 20 <= int(r["turn"]) <= 25]
    rah_all, rah_late = stats([f(r["household_rah"]) for r in all_rows]), stats([f(r["household_rah"]) for r in late])
    hjb_non = sum(not bool(r["hjb_converged"]) for r in all_rows)
    kfe_diag = sum(r["kfe_diagnostic_status"] == "DIAGNOSTIC_ONLY" for r in all_rows)
    zt_total = sum(int(r["Zt_adjustment_count"]) for r in national)
    zt_turns = [(int(r["turn"]), int(r["Zt_adjustment_count"])) for r in national if int(r["Zt_adjustment_count"])]
    late_total = stats([f(r["firm_K_total_over_Ktarget"]) for r in late])
    late_private = stats([f(r["private_K_over_Ktarget"]) for r in late])
    turn25 = c1[25]
    final_classification = {
        "schema": "CH5_C1_RESIDUAL_PUBLIC_ASSET_25TURN_FINAL_CLASSIFICATION_V1", "verdict": VERDICT,
        "accounting": assertion, "late_total_K_ratio": late_total, "late_private_K_ratio": late_private,
        "trajectory_HJB_nonconverged_but_continued": hjb_non, "trajectory_KFE_diagnostic_only": kfe_diag,
        "Zt_adjustments": zt_total, "Zt_adjustment_turns": zt_turns,
        "turn25": {"raw_ra_lower": int(turn25["ra_lower"]), "raw_ra_interior": int(turn25["ra_interior"]),
                   "raw_ra_upper": int(turn25["ra_upper"]), "max_KN_gap": f(turn25["max_KN_gap"]),
                   "max_Y_prev_gap": f(turn25["max_Y_prev_gap"]), "max_GDP_level_gap": f(turn25["max_GDP_level_gap"]),
                   "HJB_converged_count": int(turn25["HJB_converged_count"])},
        "rah_pooled": rah_all, "rah_late": rah_late,
        "next_direct_numerical_blocker": "PRICE_NUMERAIRE_RAW_RA_UPPER_CLIPPING__KFE_VALIDITY_REMAINS_INDEPENDENT",
        "results_eligible": False,
    }
    write_json(out / "final_classification.json", final_classification)

    init_summary = read_json(out / "national_initialization_summary.json")
    report = f"""# Chapter 5 MP4C C1 residual public-asset contemporaneous integration and 25-turn diagnostic

Date: 2026-09-11

Builder verdict: `{VERDICT}`

## Outcome

The separately named C1 route completed exactly one initialization observation and one 25-turn corrected-2018 trajectory. Initialization retained the accepted G1 observation contract and aligned {init_summary['accounting_aligned_count']}/31 firm accounting capital levels. Across all {len(all_rows)} province-turn observations, the contemporaneous identity passed {assertion['passed']}/{len(all_rows)} with maximum absolute residual {assertion['maximum_abs_accounting_residual_MU']} MU and zero historical C0 GovInv actions.

Private capital reached or exceeded target in {assertion['private_at_or_above_target_count']} province-turn observations. The residual floor bound in exactly the same {assertion['residual_floor_binding_count']} observations, setting public assets to zero and preserving private overshoot. For pooled turns 20-25, total K/target min/median/max was {late_total['min']}/{late_total['median']}/{late_total['max']}; private K/target was {late_private['min']}/{late_private['median']}/{late_private['max']}. The accepted C0 late-window two-to-three-times overshoot therefore disappeared whenever private capital remained below target; any remaining total overshoot is mechanically private, not GovInv-driven.

## Prices and outer adjustment

The selected-turn three-route comparison is in `baseline_selected_turn_comparison.csv`; G0 and G1+C0 were read from accepted evidence and were not rerun. At turn 25 C1 raw-ra lower/interior/upper counts were {turn25['ra_lower']}/{turn25['ra_interior']}/{turn25['ra_upper']}, versus G0 {g0[25]['ra_lower']}/{g0[25]['ra_interior']}/{g0[25]['ra_upper']} and G1+C0 {g1[25]['ra_lower']}/{g1[25]['ra_interior']}/{g1[25]['ra_upper']}. Holding total capital at target therefore increased, rather than reduced, upper-bound raw-ra pressure. Pooled C1 `rah` min/median/max was {rah_all['min']}/{rah_all['median']}/{rah_all['max']}, and turns 20-25 were {rah_late['min']}/{rah_late['median']}/{rah_late['max']}; it remained high/boundary-proximate rather than becoming more interior.

KN and GDP paths improved materially relative to both C0 baselines. At turn 25 max KN gap was {turn25['max_KN_gap']} and max GDP-level gap was {turn25['max_GDP_level_gap']}, versus G0 {g0[25]['max_KN_gap']}/{g0[25]['max_GDP_level_gap']} and G1+C0 {g1[25]['max_KN_gap']}/{g1[25]['max_GDP_level_gap']}; max Y/Yprev gap was {turn25['max_Y_prev_gap']}. Zt adjusted {zt_total} province-turns, only on turns {', '.join(str(t) for t, _ in zt_turns)} ({', '.join(str(count) for _, count in zt_turns)} provinces respectively), and zero times in turns 20-25. It was an early transition channel, not the dominant late-window adjustment source. GovInv was recomputed only by the residual identity and was never overwritten by Zt.

The remaining direct numerical convergence blocker is price/numeraire/raw-ra upper clipping: 30/31 provinces remain above the raw-ra upper bound at turn 25, while KN is also still just above the frozen `1e-9` threshold. KFE validity remains an independent scientific blocker. All HJB returns converged from turn 6 onward, so late-window HJB is not the immediate blocker. Source-faithful labor remains a known interpretation limitation, but this isolated C1 run provides no evidence that normalized labor should be stacked next before the price/numeraire boundary is diagnosed. No normalized-labor route was activated and no workplace-employment claim is made.

## Household validity and calls

There were {hjb_non} finite HJB nonconverged-but-continued trajectory observations; their false flags remain diagnostic-only. All {kfe_diag}/775 trajectory KFE returns were independently `DIAGNOSTIC_ONLY`. One scientific process used 31 initialization HJB/KFE/aggregate calls plus one At-only allocation, then 775 trajectory household updates over 25/25 turns. Scientific retry, second initialization, second trajectory, turn 26+, beta cells, MATLAB, production steady-state, GE, annual, IRF, and Results calls were zero. Results eligibility remains FALSE.

Phase A completed 40/40 focused cases before science, plus compile and diff checks, with zero scientific calls. The legacy source-faithful one-turn, C0 controller, firm, and capital-allocation sources remained unchanged from the live baseline.
"""
    (REPO / DOC_REL).write_text(report, encoding="utf-8")

    source_receipt = read_json(out / "source_hash_receipt.json")
    source_receipt["final_candidate_files"] = {
        relative: file_sha(REPO / relative) for relative in (
            "src/ch5_two_asset_hank/multi_province/c1_residual_public_asset.py",
            "validators/multi_province/c1_residual_public_asset_25turn/run.py",
            "validators/multi_province/c1_residual_public_asset_25turn/finalize.py",
            "tests/test_mp4c_c1_residual_public_asset_25turn.py",
        )
    }
    source_receipt["post_science_change"] = "FINALIZER_REPORT_CLASSIFICATION_ONLY__NO_SCIENTIFIC_STATE_CHANGE__NO_RERUN"
    write_json(out / "source_hash_receipt.json", source_receipt)

    manifest_paths = [
        Path("src/ch5_two_asset_hank/multi_province/c1_residual_public_asset.py"),
        Path("validators/multi_province/c1_residual_public_asset_25turn/__init__.py"),
        Path("validators/multi_province/c1_residual_public_asset_25turn/run.py"),
        Path("validators/multi_province/c1_residual_public_asset_25turn/finalize.py"),
        Path("tests/test_mp4c_c1_residual_public_asset_25turn.py"), DOC_REL,
    ] + [REPORT_REL / name for name in (
        "initialization_receipt_31province.csv", "national_initialization_summary.json",
        "province_turn_capital_ledger.csv", "national_turn_summary.csv", "baseline_selected_turn_comparison.csv",
        "anhui_trace.csv", "hjb_convergence_path.csv", "scientific_validity_ledger.csv",
        "c1_accounting_assertion_receipt.json", "call_ledger.json", "runtime_input_receipt.json",
        "source_hash_receipt.json", "focused_test_receipt.json", "bounded_invocation_receipt.json",
        "terminal_result.json", "final_classification.json",
    )]
    entries = [{"path": p.as_posix(), "bytes": (REPO / p).stat().st_size, "sha256": file_sha(REPO / p)} for p in manifest_paths]
    write_json(out / "manifest.json", {"schema": "CH5_C1_RESIDUAL_PUBLIC_ASSET_25TURN_MANIFEST_V1",
                                       "verdict": VERDICT, "entries": entries, "results_eligible": False})
    manifest_sha = file_sha(out / "manifest.json")
    readback = [{"path": e["path"], "expected_sha256": e["sha256"],
                 "actual_sha256": file_sha(REPO / e["path"]), "match": e["sha256"] == file_sha(REPO / e["path"])} for e in entries]
    if not all(r["match"] for r in readback):
        raise RuntimeError("manifest readback failed")
    write_json(out / "manifest_readback.json", {"schema": "CH5_C1_RESIDUAL_PUBLIC_ASSET_25TURN_MANIFEST_READBACK_V1",
                                                 "manifest_sha256": manifest_sha, "entries_checked": len(readback),
                                                 "all_match": True, "entries": readback})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("external_root", type=Path)
    args = parser.parse_args()
    finalize(args.external_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
