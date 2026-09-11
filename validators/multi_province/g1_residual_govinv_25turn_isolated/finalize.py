"""Deterministically package the completed G1 run; performs no scientific solve."""
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
REPORT_REL = Path("reports/mp4c_g1_residual_govinv_25turn_isolated_20260911")
DOC_REL = Path("docs/CH5_MP4C_G1_RESIDUAL_GOVINV_INITIALIZATION_INTEGRATION_AND_25TURN_ISOLATED_DIAGNOSTIC_REPORT.md")
G0_REL = Path("reports/mp4c_corrected_2018_hjb_propagation_25turn_kl_20260910/national_turn_summary.csv")
SELECTED = (1, 2, 3, 5, 10, 15, 20, 21, 22, 23, 24, 25)
FINAL_FAIL = "G1_RESIDUAL_GOVINV_25TURN_FAIL__INITIAL_ALIGNMENT_VALID_BUT_UNCHANGED_CONTROLLER_RECREATES_OR_WORSENS_INSTABILITY"


def read_json(path: Path) -> dict[str, Any]:
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


def action_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    counts = Counter(row["govinv_action"] for row in rows)
    return {
        "decrease": counts.get("LOW_RA_DECREASE_0P9", 0),
        "increase": counts.get("HIGH_RA_INCREASE_1P1", 0),
        "hold": counts.get("NONE", 0),
    }


def rate_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    counts = Counter("lower" if f(row["firm_ra0"]) < f(row["ramin"]) else
                     "upper" if f(row["firm_ra0"]) > f(row["ramax"]) else "interior" for row in rows)
    return {key: counts.get(key, 0) for key in ("lower", "interior", "upper")}


def finalize(external_root: Path) -> None:
    ext = Path(external_root)
    terminal = read_json(ext / "terminal_result.json")
    calls = read_json(ext / "call_ledger.json")
    if terminal.get("actual_turns_completed") != 25 or terminal.get("error") is not None:
        raise ValueError("completed 25-turn evidence is required")
    counts = calls["counts"]
    required_counts = {
        "scientific_processes": 1, "initialization_observation_passes": 1,
        "initialization_observation_hjb_calls": 31, "initialization_observation_kfe_calls": 31,
        "initialization_observation_aggregate_calls": 31, "initial_at_only_capital_allocation_calls": 1,
        "trajectory_attempts": 1, "turns_completed": 25, "province_updates_completed": 775,
        "trajectory_hjb_calls": 775, "trajectory_kfe_calls": 775, "trajectory_aggregate_calls": 775,
        "scientific_retries": 0,
    }
    if any(counts.get(key) != value for key, value in required_counts.items()):
        raise ValueError("scientific call ledger does not match the authorized budget")
    out = REPO / REPORT_REL
    out.mkdir(parents=True, exist_ok=True)
    for source, destination in (
        ("initialization_receipt_31province.csv", "initialization_receipt_31province.csv"),
        ("national_initialization_summary.json", "national_initialization_summary.json"),
        ("call_ledger.json", "call_ledger.json"),
        ("runtime_input_receipt.json", "runtime_input_receipt.json"),
        ("source_hash_receipt.json", "source_hash_receipt.json"),
        ("phase_a_zero_science_receipt.json", "focused_test_receipt.json"),
        ("bounded_invocation_receipt.json", "bounded_invocation_receipt.json"),
    ):
        shutil.copyfile(ext / source, out / destination)
    source_receipt = read_json(out / "source_hash_receipt.json")
    executed_run_sha = source_receipt["files"]["validators/multi_province/g1_residual_govinv_25turn_isolated/run.py"]
    final_run_sha = file_sha(REPO / "validators/multi_province/g1_residual_govinv_25turn_isolated/run.py")
    source_receipt["executed_run_py_sha256"] = executed_run_sha
    source_receipt["final_candidate_run_py_sha256"] = final_run_sha
    source_receipt["post_science_change"] = (
        "TERMINAL_VERDICT_CLASSIFIER_ONLY__NO_SCIENTIFIC_STATE_CHANGE__NO_RERUN"
        if final_run_sha != executed_run_sha else "NONE"
    )
    write_json(out / "source_hash_receipt.json", source_receipt)
    init_rows = read_csv(ext / "initialization_receipt_31province.csv")
    init_packaged = read_json(out / "national_initialization_summary.json")
    init_packaged["national_sums_MU"] = {
        "Ktarget": sum(f(row["Ktarget_2018_MU"]) for row in init_rows),
        "private_K_beta1": sum(f(row["Kt_supply_initial_MU_beta1"]) for row in init_rows),
        "GovInv0_G0": sum(f(row["GovInv0_G0_MU"]) for row in init_rows),
        "GovInv0_G1": sum(f(row["GovInv0_G1_MU"]) for row in init_rows),
        "firm_K_accounting_G0": sum(f(row["firm_K_accounting_G0_MU"]) for row in init_rows),
        "firm_K_accounting_G1": sum(f(row["firm_K_accounting_G1_MU"]) for row in init_rows),
    }
    init_packaged["HJB_classification_counts"] = dict(Counter(row["HJB_classification"] for row in init_rows))
    init_packaged["KFE_classification_counts"] = dict(Counter(row["KFE_classification"] for row in init_rows))
    write_json(out / "national_initialization_summary.json", init_packaged)

    all_rows: list[dict[str, Any]] = []
    national_rows: list[dict[str, Any]] = []
    controller_rows: list[dict[str, Any]] = []
    for turn in range(1, 26):
        rows = read_json(ext / f"turn_{turn:02d}" / "per_province_observables.json")
        summary = read_json(ext / f"turn_{turn:02d}" / "national_summary.json")
        if len(rows) != 31:
            raise ValueError(f"turn {turn}: province count is not 31")
        all_rows.extend(rows)
        actions = action_counts(rows)
        rates = rate_counts(rows)
        total = stats([f(row["firm_K_total_over_Ktarget"]) for row in rows])
        private = stats([f(row["private_K_over_Ktarget"]) for row in rows])
        gov = stats([f(row["GovInv_before_over_Ktarget"]) for row in rows])
        rah = stats([f(row["household_rah"]) for row in rows])
        national_rows.append({
            "turn": turn, "total_K_ratio_min": total["min"], "total_K_ratio_median": total["median"],
            "total_K_ratio_max": total["max"], "GovInv_ratio_min": gov["min"],
            "GovInv_ratio_median": gov["median"], "GovInv_ratio_max": gov["max"],
            "private_K_ratio_min": private["min"], "private_K_ratio_median": private["median"],
            "private_K_ratio_max": private["max"], "rah_min": rah["min"], "rah_median": rah["median"],
            "rah_max": rah["max"], "ra_lower": rates["lower"], "ra_interior": rates["interior"],
            "ra_upper": rates["upper"], "max_KN_gap": f(summary["nk_gap"]["max"]),
            "max_Y_prev_gap": f(summary["yt_gap"]["max"]), "max_GDP_level_gap": f(summary["GDP_level_gap"]["max"]),
            "govinv_decrease": actions["decrease"], "govinv_increase": actions["increase"],
            "govinv_hold": actions["hold"], "HJB_converged_count": int(summary["hjb_converged_count"]),
            "HJB_nonconverged_count": int(summary["hjb_nonconverged_but_continued_count"]),
            "HJB_nonconverged_names": "|".join(row["province"] for row in rows if not row["hjb_converged"]),
            "KFE_diagnostic_only_count": sum(row["kfe_diagnostic_status"] == "DIAGNOSTIC_ONLY" for row in rows),
            "adaptation_gate_open": bool(rows[0]["adaptation_gate_open"]),
            "source_final_predicate": bool(rows[0]["source_final_predicate"]),
        })
        controller_rows.append({
            "turn": turn, "adaptation_gate_open": bool(rows[0]["adaptation_gate_open"]),
            "govinv_decrease": actions["decrease"], "govinv_increase": actions["increase"],
            "govinv_hold": actions["hold"], "zt_adjusted_count": sum(bool(row["zt_adjusted"]) for row in rows),
            "ra_lower": rates["lower"], "ra_interior": rates["interior"], "ra_upper": rates["upper"],
            "max_KN_gap": f(summary["nk_gap"]["max"]), "source_final_predicate": bool(rows[0]["source_final_predicate"]),
        })

    capital_fields = ("turn", "province_index", "province", "Ktarget_2018_MU", "Kt_supply_private_MU",
        "GovInv_before_MU", "GovInv_after_MU", "firm_K_total_MU", "private_K_over_Ktarget",
        "GovInv_before_over_Ktarget", "GovInv_after_over_Ktarget", "firm_K_total_over_Ktarget",
        "firm_ra0", "firm_ra_used", "household_rah", "firm_wage_raw", "firm_wage_used", "A", "B", "L", "C",
        "nk_gap", "yt_gap", "GDP_level_gap", "Zt_before", "Zt_after", "govinv_action", "adaptation_gate_open")
    write_csv(out / "province_turn_capital_ledger.csv", [{key: row[key] for key in capital_fields} for row in all_rows])
    write_csv(out / "national_turn_summary.csv", national_rows)
    write_csv(out / "controller_action_summary.csv", controller_rows)

    init_validity = [{
        "stage": "INITIALIZATION_OBSERVATION", "turn": 0, "province_index": row["province_index"],
        "province": row["province"], "HJB_converged": row["HJB_converged"],
        "HJB_classification": row["HJB_classification"], "KFE_classification": row["KFE_classification"],
        "asset_bridge": "SOURCE_FAITHFUL_DIAGNOSTIC_ONLY", "overall_validity": "DIAGNOSTIC_ONLY",
    } for row in init_rows]
    turn_validity = [{
        "stage": "OUTER_TRAJECTORY", "turn": row["turn"], "province_index": row["province_index"],
        "province": row["province"], "HJB_converged": row["hjb_converged"],
        "HJB_classification": row["hjb_acceptance_classification"],
        "KFE_classification": row["kfe_diagnostic_status"], "asset_bridge": "SOURCE_FAITHFUL_DIAGNOSTIC_ONLY",
        "overall_validity": "DIAGNOSTIC_ONLY",
    } for row in all_rows]
    write_csv(out / "scientific_validity_ledger.csv", init_validity + turn_validity)
    init_hjb = [{"stage": "INITIALIZATION_OBSERVATION", "turn": 0,
        "province_index": row["province_index"], "province": row["province"],
        "HJB_converged": row["HJB_converged"], "HJB_iterations": "", "HJB_statistic": "",
        "HJB_classification": row["HJB_classification"]} for row in init_rows]
    turn_hjb = [{"stage": "OUTER_TRAJECTORY", "turn": row["turn"],
        "province_index": row["province_index"], "province": row["province"],
        "HJB_converged": row["hjb_converged"], "HJB_iterations": row["hjb_iterations"],
        "HJB_statistic": row["hjb_statistic"], "HJB_classification": row["hjb_acceptance_classification"]}
        for row in all_rows]
    write_csv(out / "hjb_convergence_path.csv", init_hjb + turn_hjb)
    anhui_init = next(row for row in init_rows if row["province"] == "安徽")
    anhui_rows = [{"stage": "INITIALIZATION_OBSERVATION", "turn": 0,
        "Ktarget": anhui_init["Ktarget_2018_MU"], "private_K": anhui_init["Kt_supply_initial_MU_beta1"],
        "GovInv": anhui_init["GovInv0_G1_MU"], "total_K_ratio": anhui_init["firm_K_G1_over_target"],
        "rah": json.loads(anhui_init["outer_turn_1_initial_state_json"])["rah"],
        "HJB_converged": anhui_init["HJB_converged"], "HJB_iterations": "", "HJB_statistic": "",
        "HJB_classification": anhui_init["HJB_classification"],
        "KFE_classification": anhui_init["KFE_classification"], "govinv_action": "NOT_APPLICABLE"}]
    for row in all_rows:
        if row["province"] == "安徽":
            anhui_rows.append({"stage": "OUTER_TRAJECTORY", "turn": row["turn"], "Ktarget": row["Ktarget_2018_MU"],
                "private_K": row["Kt_supply_private_MU"], "GovInv": row["GovInv_before_MU"],
                "total_K_ratio": row["firm_K_total_over_Ktarget"], "rah": row["household_rah"],
                "HJB_converged": row["hjb_converged"], "HJB_iterations": row["hjb_iterations"],
                "HJB_statistic": row["hjb_statistic"], "HJB_classification": row["hjb_acceptance_classification"],
                "KFE_classification": row["kfe_diagnostic_status"], "govinv_action": row["govinv_action"]})
    write_csv(out / "anhui_trace.csv", anhui_rows)

    g0 = {int(row["turn"]): row for row in read_csv(REPO / G0_REL)}
    g1 = {int(row["turn"]): row for row in national_rows}
    comparison: list[dict[str, Any]] = []
    for turn in SELECTED:
        a, b = g0[turn], g1[turn]
        row: dict[str, Any] = {"turn": turn}
        mappings = {
            "total_K_ratio_min": "firm_K_ratio_min", "total_K_ratio_median": "firm_K_ratio_median",
            "total_K_ratio_max": "firm_K_ratio_max", "GovInv_ratio_median": "GovInv_ratio_median",
            "private_K_ratio_median": "private_K_ratio_median", "ra_lower": "ra_lower", "ra_interior": "ra_interior",
            "ra_upper": "ra_upper", "max_KN_gap": "max_KN_gap", "max_GDP_level_gap": "max_GDP_level_gap",
            "govinv_decrease": "govinv_decrease", "govinv_increase": "govinv_increase", "govinv_hold": "govinv_hold",
            "HJB_converged_count": "hjb_converged_count",
        }
        for name, g0_name in mappings.items():
            g0_value, g1_value = f(a[g0_name]), f(b[name])
            row[f"G0_{name}"] = g0_value
            row[f"G1_{name}"] = g1_value
            row[f"G1_minus_G0_{name}"] = g1_value - g0_value
        comparison.append(row)
    write_csv(out / "g0_vs_g1_selected_turn_comparison.csv", comparison)

    late = [row for row in national_rows if 20 <= int(row["turn"]) <= 25]
    late_province = [row for row in all_rows if 20 <= int(row["turn"]) <= 25]
    late_total = [f(row["total_K_ratio_median"]) for row in late]
    late_gov = [f(row["GovInv_ratio_median"]) for row in late]
    late_private = [f(row["private_K_ratio_median"]) for row in late]
    all_actions = {key: sum(int(row[f"govinv_{key}"]) for row in controller_rows) for key in ("decrease", "increase", "hold")}
    rah_all = stats([f(row["household_rah"]) for row in all_rows])
    rah_late = stats([f(row["household_rah"]) for row in late_province])
    late_pooled_total = stats([f(row["firm_K_total_over_Ktarget"]) for row in late_province])
    late_pooled_gov = stats([f(row["GovInv_before_over_Ktarget"]) for row in late_province])
    late_pooled_private = stats([f(row["private_K_over_Ktarget"]) for row in late_province])
    trajectory_hjb_nonconverged = sum(not bool(row["hjb_converged"]) for row in all_rows)
    late_hjb_nonconverged = sum(not bool(row["hjb_converged"]) for row in late_province)
    g0_province = read_csv(REPO / "reports/mp4c_corrected_2018_hjb_propagation_25turn_kl_20260910/province_turn_kl_ledger.csv")
    g0_rah = stats([f(row["household_rah"]) for row in g0_province])
    g0_actions = {key: sum(int(row[f"govinv_{key}"]) for row in g0.values()) for key in ("decrease", "increase", "hold")}
    selected_ra_counts_identical = all(
        f(row[f"G1_ra_{region}"]) == f(row[f"G0_ra_{region}"])
        for row in comparison for region in ("lower", "interior", "upper")
    )
    init_summary = read_json(ext / "national_initialization_summary.json")
    outcome = {
        "schema": "CH5_G1_RESIDUAL_GOVINV_25TURN_ISOLATED_FINAL_CLASSIFICATION_V1",
        "verdict": FINAL_FAIL,
        "runner_completion_verdict": terminal["verdict"],
        "classification_basis": "G1 aligns initial accounting, but the unchanged high-ra controller repeatedly increases GovInv and recreates material late-window overshoot.",
        "initial_alignment_count": init_summary["accounting_aligned_count"],
        "turn1_G0_total_K_ratio_median": f(g0[1]["firm_K_ratio_median"]),
        "turn1_G1_total_K_ratio_median": f(g1[1]["total_K_ratio_median"]),
        "late_turn20_25_median_total_K_ratio": stats(late_total),
        "late_turn20_25_median_GovInv_ratio": stats(late_gov),
        "late_turn20_25_median_private_K_ratio": stats(late_private),
        "late_turn20_25_pooled_total_K_ratio": late_pooled_total,
        "late_turn20_25_pooled_GovInv_ratio": late_pooled_gov,
        "late_turn20_25_pooled_private_K_ratio": late_pooled_private,
        "controller_actions_all_turns": all_actions,
        "accepted_G0_controller_actions_all_turns": g0_actions,
        "selected_turn_ra_boundary_counts_identical_to_G0": selected_ra_counts_identical,
        "trajectory_HJB_nonconverged_but_continued": trajectory_hjb_nonconverged,
        "late_turn20_25_HJB_nonconverged_but_continued": late_hjb_nonconverged,
        "trajectory_KFE_diagnostic_only": 775,
        "rah_pooled": rah_all,
        "rah_late_turn20_25_pooled": rah_late,
        "accepted_G0_rah_pooled": g0_rah,
        "results_eligible": False,
    }
    write_json(out / "final_classification.json", outcome)

    report = f"""# Chapter 5 MP4C G1 residual-GovInv initialization integration and isolated 25-turn diagnostic

Date: 2026-09-11

Baseline live `origin/main`: `1a20d535ff1626b8ae2108690e0acde6ded14839`. Branch: `codex/ch5-g1-residual-govinv-25turn-isolated-20260911`. External evidence root: `D:\\ProjectTemp\\ch5-g1-residual-govinv-25turn-isolated-evidence-20260911-001`.

Builder verdict:

`{FINAL_FAIL}`

## Outcome

The separately named G1 route completed one `INITIALIZATION_OBSERVATION` and one 25-turn corrected-2018 trajectory. G1 aligned initial accounting capital to target in {init_summary['accounting_aligned_count']}/31 provinces with zero maximum identity error. Outer turn 1 median total K/target was {f(g1[1]['total_K_ratio_median'])}, versus accepted G0 {f(g0[1]['firm_K_ratio_median'])}; the initial duplication was removed.

The unchanged historical controller did not preserve the improvement. Across 25 turns it recorded decrease/increase/hold counts {all_actions['decrease']}/{all_actions['increase']}/{all_actions['hold']}, exactly the accepted G0 totals. Repeated high-ra increases rebuilt GovInv overshoot. For the pooled 186 province-turn observations in turns 20-25, total K/target min/median/max was {late_pooled_total['min']}/{late_pooled_total['median']}/{late_pooled_total['max']}, GovInv/target was {late_pooled_gov['min']}/{late_pooled_gov['median']}/{late_pooled_gov['max']}, and private K/target was {late_pooled_private['min']}/{late_pooled_private['median']}/{late_pooled_private['max']}. Across the six turn-level medians, total K/target rose from {stats(late_total)['min']} to {stats(late_total)['max']}. The late overshoot is therefore overwhelmingly GovInv-driven.

## G0 comparison and dynamics

The selected-turn comparison is in `g0_vs_g1_selected_turn_comparison.csv`; G0 was read from accepted evidence and was not rerun. G1 starts closer to target, but the old controller erodes and then reverses that improvement. At every selected turn, lower/interior/upper raw-ra counts are identical to G0; boundary pressure did not improve. Pooled trajectory `rah` min/median/max is {rah_all['min']}/{rah_all['median']}/{rah_all['max']}, versus G0 {g0_rah['min']}/{g0_rah['median']}/{g0_rah['max']}. Thus `rah` does not collapse in G1, but it is essentially unchanged from G0 and does not establish production plausibility. KN, Y/Yprev and GDP-level gaps are slightly smaller in level at some turns but retain the same oscillatory controller-gate pattern, and the source final predicate never passes.

## Household validity

Initialization HJB convergence was {init_summary['HJB_converged_count']}/31; all 31 initialization KFE returns were `DIAGNOSTIC_ONLY`. Across the trajectory there were {trajectory_hjb_nonconverged} HJB nonconverged-but-continued observations, including {late_hjb_nonconverged} in turns 20-25; all 775 KFE classifications were independently `DIAGNOSTIC_ONLY`. Finite continuation never promotes a false HJB flag or KFE blocker to scientific validity. The beta bridge remains `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`.

## Calls and boundaries

One process made 31 initialization HJB/KFE/aggregate calls and one initial At-only allocation, followed by 775 trajectory HJB/KFE/aggregate calls and 775 province firm updates over 25/25 turns. Totals were {counts['hjb_calls']} HJB calls, {counts['hjb_direct_solves']} HJB direct solves, {counts['kfe_calls']} KFE direct solves, and {counts['brentq_calls_attempted']} labor-root/Brent calls. Scientific retries, second initialization passes, second trajectories, beta cells, MATLAB, steady-state, GE, annual, IRF and Results calls were zero.

Phase A ran the 40-case focused suite twice before science (80 cumulative cases), and two compile processes; all passed with zero scientific calls. After final deterministic packaging and verdict-classifier correction, the focused suite passed again at 41/41, compile and `git diff --check` passed, and manifest readback passed 20/20.

The raw runner terminal marked successful completion of the authorized 25-turn chain. Post-science deterministic classification applied the task's explicit economic verdict rule and superseded that completion marker with the FAIL verdict above. The candidate runner was then corrected only to apply the same classifier on future readback; no scientific state changed and no science was rerun. Executed and final runner hashes are both retained in `source_hash_receipt.json`.

The evidence is sufficient to justify a separately reviewed controller-redesign task, but this task does not publish one and does not change the controller. Normalized labor was not activated. Results eligibility remains FALSE.
"""
    (REPO / DOC_REL).write_text(report, encoding="utf-8")

    manifest_paths = [
        Path("validators/multi_province/g1_residual_govinv_25turn_isolated/__init__.py"),
        Path("validators/multi_province/g1_residual_govinv_25turn_isolated/run.py"),
        Path("validators/multi_province/g1_residual_govinv_25turn_isolated/finalize.py"),
        Path("tests/test_mp4c_g1_residual_govinv_25turn_isolated.py"), DOC_REL,
    ] + [REPORT_REL / name for name in (
        "initialization_receipt_31province.csv", "national_initialization_summary.json",
        "province_turn_capital_ledger.csv", "national_turn_summary.csv",
        "g0_vs_g1_selected_turn_comparison.csv", "anhui_trace.csv", "hjb_convergence_path.csv",
        "scientific_validity_ledger.csv", "controller_action_summary.csv", "call_ledger.json",
        "runtime_input_receipt.json", "source_hash_receipt.json", "focused_test_receipt.json",
        "bounded_invocation_receipt.json", "final_classification.json",
    )]
    entries = [{"path": path.as_posix(), "bytes": (REPO / path).stat().st_size,
                "sha256": file_sha(REPO / path)} for path in manifest_paths]
    manifest = {"schema": "CH5_G1_RESIDUAL_GOVINV_25TURN_ISOLATED_MANIFEST_V1",
                "verdict": FINAL_FAIL, "entries": entries, "results_eligible": False}
    write_json(out / "manifest.json", manifest)
    manifest_sha = file_sha(out / "manifest.json")
    readback = []
    for entry in entries:
        path = REPO / entry["path"]
        readback.append({"path": entry["path"], "expected_sha256": entry["sha256"],
                         "actual_sha256": file_sha(path), "match": file_sha(path) == entry["sha256"]})
    if not all(row["match"] for row in readback):
        raise RuntimeError("manifest readback failed")
    write_json(out / "manifest_readback.json", {
        "schema": "CH5_G1_RESIDUAL_GOVINV_25TURN_ISOLATED_MANIFEST_READBACK_V1",
        "manifest_sha256": manifest_sha, "entries_checked": len(readback), "all_match": True,
        "entries": readback,
    })


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("external_root", type=Path)
    args = parser.parse_args()
    finalize(args.external_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
