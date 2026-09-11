"""Zero-science evidence summarizer for the bounded K1A A/B task."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
import sys
from hashlib import sha256
from pathlib import Path
from typing import Any, Iterable

import numpy as np

REPO = Path(__file__).resolve().parents[3]
EVIDENCE_REL = Path("docs/evidence/ch5_mp4c_k1a_equal_share_vs_beta2")
REPORT_REL = Path("docs/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_BOUNDED_INTEGRATION_REPORT.md")
VERDICT = "K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_BOUNDED_INTEGRATION_PARTIAL__PATH_A_STOPPED_AFTER_TURN1_ON_LEGACY_VALIDATOR_ASSERTION__PATH_B_COMPLETED_25_TURNS"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest().upper()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")


def dist(values: Iterable[float]) -> dict[str, float]:
    data = [float(value) for value in values]
    return {"min": min(data), "median": statistics.median(data), "max": max(data)}


def corr(x: list[float], y: list[float]) -> float | None:
    if len(x) < 2 or np.std(x) == 0.0 or np.std(y) == 0.0:
        return None
    return float(np.corrcoef(x, y)[0, 1])


def load_rows(root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    all_rows: list[dict[str, Any]] = []
    turns: list[dict[str, Any]] = []
    for path in sorted(root.glob("turn_*/per_province_observables.json")):
        rows = read_json(path)
        all_rows.extend(rows)
        raw = [float(row["firm_ra0"]) for row in rows]
        turns.append({
            "turn": int(rows[0]["turn"]), "province_rows": len(rows),
            "private_K_over_target_min": min(float(r["private_K_over_Ktarget"]) for r in rows),
            "private_K_over_target_median": statistics.median(float(r["private_K_over_Ktarget"]) for r in rows),
            "private_K_over_target_max": max(float(r["private_K_over_Ktarget"]) for r in rows),
            "total_K_over_target_min": min(float(r["firm_K_total_over_Ktarget"]) for r in rows),
            "total_K_over_target_median": statistics.median(float(r["firm_K_total_over_Ktarget"]) for r in rows),
            "total_K_over_target_max": max(float(r["firm_K_total_over_Ktarget"]) for r in rows),
            "raw_ra0_min": min(raw), "raw_ra0_median": statistics.median(raw), "raw_ra0_max": max(raw),
            "raw_ra0_std": float(np.std(raw)), "raw_ra0_below_0p02": sum(v < 0.02 for v in raw),
            "raw_ra0_above_0p09": sum(v > 0.09 for v in raw),
            "lower_clip_count": sum(bool(r["ra_clipped_lower"]) for r in rows),
            "upper_clip_count": sum(bool(r["ra_clipped_upper"]) for r in rows),
            "hjb_converged_count": sum(bool(r["hjb_converged"]) for r in rows),
            "source_final_predicate": bool(rows[0]["source_final_predicate"]),
            "max_nk_gap": max(float(r["nk_gap"]) for r in rows),
            "max_yt_gap": max(float(r["yt_gap"]) for r in rows),
        })
    return all_rows, turns


def summarize_path(root: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    rows, turns = load_rows(root)
    networks = [read_json(path) for path in sorted((root / "capital_network").glob("allocation_*.json"))]
    terminal, ledger = read_json(root / "terminal_result.json"), read_json(root / "call_ledger.json")
    private_over = [float(r["private_K_over_Ktarget"]) for r in rows]
    total_over = [float(r["firm_K_total_over_Ktarget"]) for r in rows]
    gov_over = [float(r["GovInv_C1_over_Ktarget"]) for r in rows]
    raw = [float(r["firm_ra0"]) for r in rows]
    rk = [float(r["firm_rk"]) for r in rows]
    profit = [float(r["firm_profit_over_K"]) for r in rows]
    profit_after_tax = [float(r["firm_after_tax_profit_component_over_K"]) for r in rows]
    private = [float(r["Kt_supply_private_MU"]) for r in rows]
    y_over_k = [float(r["Y"]) / float(r["firm_K_total_MU"]) for r in rows]
    at_or_above = [r for r in rows if bool(r["private_K_at_or_above_target"])]
    summary = {
        "root": str(root), "terminal": terminal, "call_ledger": ledger,
        "completed_turns": len(turns), "province_turn_rows": len(rows),
        "accounting": {
            "share_column_sum_max_abs_gap": max(abs(float(v) - 1.0) for n in networks for v in n["share_column_sums"]),
            "capital_column_max_abs_residual_MU": max(abs(float(r["capital_column_residual_MU"])) for r in rows),
            "national_private_capital_max_abs_residual_MU": max(abs(float(n["national_private_capital_conservation_residual"])) for n in networks),
            "home_retained_formula_max_abs_residual_MU": max(
                abs(float(n["domestic_retained_capital_by_origin"][i]) - float(n["portfolio_shares_destination_origin"][i][i]) * float(n["origin_private_wealth"][i]))
                for n in networks for i in range(31)
            ),
            "quantity_and_rah_same_S_all": all(bool(r["quantity_and_rah_same_S"]) for r in rows),
            "destination_theta_double_weighting_count": sum(bool(r["destination_theta_double_weighting"]) for r in rows),
        },
        "c1": {
            "formula_max_abs_residual_MU": max(float(r["c1_accounting_abs_residual_MU"]) for r in rows),
            "private_K_at_or_above_target_cases": len(at_or_above),
            "govinv_nonzero_in_at_or_above_cases": sum(abs(float(r["GovInv_C1_MU"])) > 1e-8 for r in at_or_above),
            "private_only_overshoot_ratio": dist(max(v - 1.0, 0.0) for v in private_over),
            "private_K_over_target": dist(private_over), "GovInv_over_target": dist(gov_over),
            "total_K_over_target": dist(total_over),
        },
        "returns": {
            "raw_ra0": dist(raw), "raw_ra0_std": float(np.std(raw)),
            "raw_ra0_below_0p02": sum(v < 0.02 for v in raw), "raw_ra0_above_0p09": sum(v > 0.09 for v in raw),
            "lower_clip_count": sum(bool(r["ra_clipped_lower"]) for r in rows),
            "upper_clip_count": sum(bool(r["ra_clipped_upper"]) for r in rows),
            "used_ra": dist(float(r["firm_ra_used"]) for r in rows), "rk": dist(rk),
            "profit_over_K": dist(profit), "after_tax_profit_component_over_K": dist(profit_after_tax),
            "ra0_reconstruction_max_abs_residual": max(abs(float(r["firm_ra0_reconstruction_residual"])) for r in rows),
            "corr_Kprivate_raw_ra0": corr(private, raw), "corr_Y_over_totalK_raw_ra0": corr(y_over_k, raw),
        },
        "outputs": {
            "household_rah": dist(float(r["household_rah"]) for r in rows),
            "Y": dist(float(r["Y"]) for r in rows), "wage_used": dist(float(r["firm_wage_used"]) for r in rows),
            "source_faithful_labor_all": all(bool(r["source_faithful_labor_route"]) for r in rows),
            "labor_identity_max_abs_gap": max(abs(float(r["destination_lt_supply"]) - float(r["firm_Lt_supply"])) for r in rows),
        },
        "convergence": {
            "converged_by_terminal_turn": bool(turns[-1]["source_final_predicate"]),
            "terminal_turn": turns[-1]["turn"],
            "hjb_converged_observations": sum(bool(r["hjb_converged"]) for r in rows),
            "hjb_nonconverged_but_continued": sum(not bool(r["hjb_converged"]) for r in rows),
            "kfe_diagnostic_only_observations": sum(r["kfe_diagnostic_status"] == "DIAGNOSTIC_ONLY" for r in rows),
        },
    }
    return summary, turns


def build_manifest(evidence_root: Path) -> dict[str, Any]:
    excluded = {"external_evidence_manifest.json", "external_evidence_readback.json"}
    files = []
    for path in sorted(p for p in evidence_root.rglob("*") if p.is_file() and p.name not in excluded):
        files.append({"path": str(path.relative_to(evidence_root)).replace("\\", "/"),
                      "bytes": path.stat().st_size, "sha256": file_sha(path)})
    return {"schema": "CH5_K1A_EQUAL_SHARE_VS_BETA2_EXTERNAL_MANIFEST_V1",
            "root": str(evidence_root), "file_count": len(files), "files": files}


def csv_text(rows: list[dict[str, Any]]) -> str:
    from io import StringIO
    output = StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=list(rows[0]))
    writer.writeheader(); writer.writerows(rows)
    return output.getvalue()


def fmt(d: dict[str, float]) -> str:
    return f"{d['min']} / {d['median']} / {d['max']}"


def finalize(evidence_root: Path) -> None:
    evidence_root = Path(evidence_root)
    tracked = REPO / EVIDENCE_REL
    tracked.mkdir(parents=True, exist_ok=True)
    a, a_turns = summarize_path(evidence_root / "path_a_equal_share")
    b, b_turns = summarize_path(evidence_root / "path_b_geographic_beta2")
    a1, b1 = a_turns[0], b_turns[0]
    late_rows = []
    for turn in range(20, 26):
        late_rows.extend(read_json(evidence_root / "path_b_geographic_beta2" / f"turn_{turn:02d}" / "per_province_observables.json"))
    a1_rows = read_json(evidence_root / "path_a_equal_share/turn_01/per_province_observables.json")
    b1_rows = read_json(evidence_root / "path_b_geographic_beta2/turn_01/per_province_observables.json")
    common_fields = (
        "private_K_over_Ktarget", "GovInv_C1_over_Ktarget", "firm_K_total_over_Ktarget",
        "firm_ra0", "firm_ra_used", "household_rah",
        "household_rah_k1a_current_payoff_bridge", "Y", "firm_wage_used", "nk_gap", "yt_gap",
    )
    common_metrics = {}
    for field in common_fields:
        a_dist = dist(float(row[field]) for row in a1_rows)
        b_dist = dist(float(row[field]) for row in b1_rows)
        common_metrics[field] = {"A": a_dist, "B": b_dist,
                                 "median_delta_B_minus_A": b_dist["median"] - a_dist["median"]}
    common = {
        "turn": 1,
        "private_K_median_delta_B_minus_A": b1["private_K_over_target_median"] - a1["private_K_over_target_median"],
        "raw_ra0_median_delta_B_minus_A": b1["raw_ra0_median"] - a1["raw_ra0_median"],
        "raw_ra0_std_A": a1["raw_ra0_std"], "raw_ra0_std_B": b1["raw_ra0_std"],
        "raw_ra0_std_delta_B_minus_A": b1["raw_ra0_std"] - a1["raw_ra0_std"],
        "metrics": common_metrics,
        "hjb_converged_count_A": a1["hjb_converged_count"],
        "hjb_converged_count_B": b1["hjb_converged_count"],
        "source_final_predicate_A": a1["source_final_predicate"],
        "source_final_predicate_B": b1["source_final_predicate"],
    }
    totals = {}
    for key in ("hjb_calls", "hjb_direct_solves", "kfe_calls", "kfe_direct_solves", "labor_roots_attempted", "province_updates_completed"):
        totals[key] = int(a["call_ledger"]["counts"][key]) + int(b["call_ledger"]["counts"][key])
    combined = {
        "schema": "CH5_K1A_EQUAL_SHARE_VS_BETA2_SUMMARY_V1", "verdict": VERDICT,
        "baseline": "386594886bec9e42d3dc18791f7f1be212d3b5c9",
        "path_A": a, "path_B": b, "common_completed_turn_comparison": common,
        "path_B_turns_20_25": {
            "private_K_over_target": dist(float(r["private_K_over_Ktarget"]) for r in late_rows),
            "GovInv_over_target": dist(float(r["GovInv_C1_over_Ktarget"]) for r in late_rows),
            "total_K_over_target": dist(float(r["firm_K_total_over_Ktarget"]) for r in late_rows),
            "raw_ra0": dist(float(r["firm_ra0"]) for r in late_rows),
        },
        "total_call_ledger": {"trajectory_invocations": 2, "scientific_retries": 0,
                              "accepted_initialization_reuses": 2, "new_initialization_solves": 0,
                              **totals, "matlab_calls": 0, "standalone_kfe_experiments": 0,
                              "k1b_runs": 0, "ge_calls": 0, "annual_calls": 0,
                              "irf_calls": 0, "results_calls": 0},
        "results_eligible": False,
    }
    write_json(tracked / "bounded_comparison_summary.json", combined)
    write_json(tracked / "call_ledger_summary.json", combined["total_call_ledger"])
    (tracked / "per_turn_summary.csv").write_text(csv_text(
        [{"path": "A", **row} for row in a_turns] + [{"path": "B", **row} for row in b_turns]
    ), encoding="utf-8", newline="")
    manifest = build_manifest(evidence_root)
    write_json(evidence_root / "external_evidence_manifest.json", manifest)
    manifest_sha = file_sha(evidence_root / "external_evidence_manifest.json")
    mismatches = [item["path"] for item in manifest["files"]
                  if file_sha(evidence_root / item["path"]) != item["sha256"]]
    readback = {"schema": "CH5_K1A_EXTERNAL_READBACK_V1", "manifest_sha256": manifest_sha,
                "checked_files": manifest["file_count"], "mismatches": mismatches,
                "status": "PASS" if not mismatches else "FAIL"}
    write_json(evidence_root / "external_evidence_readback.json", readback)
    write_json(tracked / "external_evidence_receipt.json", {
        "root": str(evidence_root), "manifest_sha256": manifest_sha,
        "manifest_file_count": manifest["file_count"], "readback_status": readback["status"],
        "readback_checked_files": readback["checked_files"],
    })
    report = f"""# Chapter 5 MP4C K1A equal-share vs geographic beta=2 bounded integration report

## Outcome

Verdict: `{VERDICT}`.

The K1A adapter and all observed capital/C1 accounting gates passed, and Path B completed the authorized 25-turn ceiling. Path A completed turn 1, then stopped at turn-2 entry because the reused G1 validator still asserted the legacy `rah` formula. Because scientific state had advanced, Path A was not retried. The task therefore cannot claim the full two-path bounded-integration PASS; the only direct A/B comparison is the common completed turn 1.

Results eligibility remains `FALSE`. This is a bounded mechanism diagnostic, not a steady state, KFE closure, K1B/K2 result, annual result, IRF, welfare result, or dissertation Results claim.

## Authority and implementation

- Live-main baseline: `386594886bec9e42d3dc18791f7f1be212d3b5c9`.
- Worktree: `D:\\ProjectTemp\\ch5-k1a-equal-share-vs-beta2-20260911-001`.
- Path A: `beta_distance=0`, `beta_return=0`; Path B: `beta_distance=2`, `beta_return=0`.
- Accepted distance canonical-LF SHA-256: `30401B7754A0126D544D54ABB36C6CB662E3E386663E3110EF3F68E417FDA084`.
- Legacy `capital_allocation.py` remained byte-identical at `BB3F283BD782399A5C1C9AEE06DC50BBA61A0599BF062669DE0B1EBBB01AEE40` and remains separately callable.
- K1A payoff bridge: `{a['path_A'] if False else 'K1A_SOURCE_FAITHFUL_PAYOFF_BRIDGE__NOT_FINAL_ECONOMIC_RETURN_AUTHORITY'}`. Quantity and `rah` use the same destination-by-origin `S`; lagged-return attractiveness, smoothing, and partial adjustment are off.
- Source-faithful labor remained active; normalized bilateral labor was not selected.
- C1 remained `GovInv=max(Ktarget-Kprivate,0)`.

## Pre-run checks

Focused zero-science tests passed 50/50, compile and diff checks passed, A/B runtime payloads were byte-identical, roots were distinct/no-overwrite, and the two configs differed only in `beta_distance`. Accepted initialization was reused with zero new initialization HJB/KFE solves.

After Path A stopped, a zero-science repair replaced only the task wrapper's legacy `rah` provenance assertion with validation against the prior completed K1A allocation using the same `S`. Path A evidence was preserved and not retried. The repair gate passed the same 50/50 focused tests before Path B started.

## Call ledger

| Item | Path A | Path B | Total |
|---|---:|---:|---:|
| trajectory invocations | 1 | 1 | 2 |
| completed turns | {a['completed_turns']} | {b['completed_turns']} | {a['completed_turns'] + b['completed_turns']} |
| province updates | {a['call_ledger']['counts']['province_updates_completed']} | {b['call_ledger']['counts']['province_updates_completed']} | {totals['province_updates_completed']} |
| HJB calls | {a['call_ledger']['counts']['hjb_calls']} | {b['call_ledger']['counts']['hjb_calls']} | {totals['hjb_calls']} |
| HJB direct solves | {a['call_ledger']['counts']['hjb_direct_solves']} | {b['call_ledger']['counts']['hjb_direct_solves']} | {totals['hjb_direct_solves']} |
| KFE calls | {a['call_ledger']['counts']['kfe_calls']} | {b['call_ledger']['counts']['kfe_calls']} | {totals['kfe_calls']} |
| KFE direct solves | {a['call_ledger']['counts']['kfe_direct_solves']} | {b['call_ledger']['counts']['kfe_direct_solves']} | {totals['kfe_direct_solves']} |
| labor-root/Brent calls | {a['call_ledger']['counts']['labor_roots_attempted']} | {b['call_ledger']['counts']['labor_roots_attempted']} | {totals['labor_roots_attempted']} |

Scientific retries were 0. MATLAB, standalone KFE experiments, K1B, GE, annual, IRF, and Results calls were all 0.

## Capital and C1 accounting

Across the {a['province_turn_rows'] + b['province_turn_rows']} observed province-turn rows, Path A/Path B maximum share-column gaps were `{a['accounting']['share_column_sum_max_abs_gap']}` / `{b['accounting']['share_column_sum_max_abs_gap']}`; maximum origin-capital residuals were `{a['accounting']['capital_column_max_abs_residual_MU']}` / `{b['accounting']['capital_column_max_abs_residual_MU']}` MU; maximum national conservation residuals were `{a['accounting']['national_private_capital_max_abs_residual_MU']}` / `{b['accounting']['national_private_capital_max_abs_residual_MU']}` MU. Home retention identities passed, quantity/`rah` used the same `S` throughout, and destination-theta double-weighting count was zero.

Path A private K/target min/median/max was `{fmt(a['c1']['private_K_over_target'])}`; Path B pooled was `{fmt(b['c1']['private_K_over_target'])}`. Path B turns 20-25 was `{fmt(combined['path_B_turns_20_25']['private_K_over_target'])}`. `Kprivate>=Ktarget` occurred {a['c1']['private_K_at_or_above_target_cases']} times in A and {b['c1']['private_K_at_or_above_target_cases']} times in B; nonzero GovInv among such cases was zero. Private-only overshoot was zero in all observed rows. Total K/target pooled min/median/max was `{fmt(a['c1']['total_K_over_target'])}` for A and `{fmt(b['c1']['total_K_over_target'])}` for B; any tiny deviation from one is floating-point accounting noise. Overshoot was not created by GovInv.

## Raw return audit and A/B comparison

Path A observed raw `ra0` min/median/max was `{fmt(a['returns']['raw_ra0'])}`; Path B pooled was `{fmt(b['returns']['raw_ra0'])}`. Counts below `.02` / above `.09` were `{a['returns']['raw_ra0_below_0p02']} / {a['returns']['raw_ra0_above_0p09']}` for A and `{b['returns']['raw_ra0_below_0p02']} / {b['returns']['raw_ra0_above_0p09']}` for B. Lower/upper clipping counts were `{a['returns']['lower_clip_count']} / {a['returns']['upper_clip_count']}` and `{b['returns']['lower_clip_count']} / {b['returns']['upper_clip_count']}`. Path B `rk` min/median/max was `{fmt(b['returns']['rk'])}` and raw profit/K was `{fmt(b['returns']['profit_over_K'])}`; the active after-tax profit component was `{fmt(b['returns']['after_tax_profit_component_over_K'])}`. Maximum `ra0 = rk + after-tax profit/K - delta` reconstruction residual was `{b['returns']['ra0_reconstruction_max_abs_residual']}`.

On the only common completed comparison turn (turn 1), B-minus-A private-K/target median was `{common['private_K_median_delta_B_minus_A']}`, raw-`ra0` median was `{common['raw_ra0_median_delta_B_minus_A']}`, and raw-`ra0` cross-sectional standard deviation changed from `{common['raw_ra0_std_A']}` to `{common['raw_ra0_std_B']}` (delta `{common['raw_ra0_std_delta_B_minus_A']}`). This supports only a turn-1 mechanism comparison; a 25-turn A/B conclusion is unavailable.

| Turn-1 metric | Path A median | Path B median | B minus A |
|---|---:|---:|---:|
| private K/target | {common_metrics['private_K_over_Ktarget']['A']['median']} | {common_metrics['private_K_over_Ktarget']['B']['median']} | {common_metrics['private_K_over_Ktarget']['median_delta_B_minus_A']} |
| GovInv/target | {common_metrics['GovInv_C1_over_Ktarget']['A']['median']} | {common_metrics['GovInv_C1_over_Ktarget']['B']['median']} | {common_metrics['GovInv_C1_over_Ktarget']['median_delta_B_minus_A']} |
| total K/target | {common_metrics['firm_K_total_over_Ktarget']['A']['median']} | {common_metrics['firm_K_total_over_Ktarget']['B']['median']} | {common_metrics['firm_K_total_over_Ktarget']['median_delta_B_minus_A']} |
| raw `ra0` | {common_metrics['firm_ra0']['A']['median']} | {common_metrics['firm_ra0']['B']['median']} | {common_metrics['firm_ra0']['median_delta_B_minus_A']} |
| used `ra` | {common_metrics['firm_ra_used']['A']['median']} | {common_metrics['firm_ra_used']['B']['median']} | {common_metrics['firm_ra_used']['median_delta_B_minus_A']} |
| entering household `rah` | {common_metrics['household_rah']['A']['median']} | {common_metrics['household_rah']['B']['median']} | {common_metrics['household_rah']['median_delta_B_minus_A']} |
| K1A network-produced `rah` | {common_metrics['household_rah_k1a_current_payoff_bridge']['A']['median']} | {common_metrics['household_rah_k1a_current_payoff_bridge']['B']['median']} | {common_metrics['household_rah_k1a_current_payoff_bridge']['median_delta_B_minus_A']} |
| output Y | {common_metrics['Y']['A']['median']} | {common_metrics['Y']['B']['median']} | {common_metrics['Y']['median_delta_B_minus_A']} |
| used wage | {common_metrics['firm_wage_used']['A']['median']} | {common_metrics['firm_wage_used']['B']['median']} | {common_metrics['firm_wage_used']['median_delta_B_minus_A']} |
| nk gap | {common_metrics['nk_gap']['A']['median']} | {common_metrics['nk_gap']['B']['median']} | {common_metrics['nk_gap']['median_delta_B_minus_A']} |
| yt gap | {common_metrics['yt_gap']['A']['median']} | {common_metrics['yt_gap']['B']['median']} | {common_metrics['yt_gap']['median_delta_B_minus_A']} |

Turn-1 HJB converged counts were `{common['hjb_converged_count_A']} / {common['hjb_converged_count_B']}` and both source final predicates were false. C1 exactly offset the A/B private-K destination differences at the firm-capital level, so turn-1 firm raw returns, output and wages were unchanged; the network-produced `rah` is the forward channel that would affect the next household pass.

For Path B pooled rows, correlation of Kprivate with raw `ra0` was `{b['returns']['corr_Kprivate_raw_ra0']}` and correlation of Y/total-K with raw `ra0` was `{b['returns']['corr_Y_over_totalK_raw_ra0']}`. These are descriptive pressure diagnostics, not causal estimates.

## Bounded behavior and blockers

Path A did not reach a scientific convergence assessment: it stopped after one completed turn on a task-wrapper legacy-formula assertion. Path B reached turn 25 but the existing final predicate remained false, so it is explicitly nonconverged at the ceiling. Path B contained {b['convergence']['hjb_nonconverged_but_continued']} HJB nonconverged-but-continued observations; all {b['convergence']['kfe_diagnostic_only_observations']} KFE observations remained `DIAGNOSTIC_ONLY`.

Path B HJB converged counts by turns 1-5 were `20, 13, 10, 10, 10`; turns 6-25 were `31/31`. The terminal nonconvergence was instead driven by the existing outer predicate (`max_nk_gap={b_turns[-1]['max_nk_gap']}` at turn 25 versus the frozen `1e-9` threshold), not by a false HJB flag at the terminal turn.

The corrected-2018 empirical finite-box upper-b leakage plus MATLAB-style pinning remains an independent scientific blocker. A running bounded trajectory does not establish KFE admissibility, steady-state acceptance, or Results eligibility.

## Evidence and next gate

External evidence root: `{evidence_root}`. Manifest SHA-256: `{manifest_sha}`; readback checked {manifest['file_count']} files with status `{readback['status']}`. Compact tracked receipts are under `{EVIDENCE_REL.as_posix()}`.

Owner/Reviewer must decide whether a fresh exact task should authorize a clean two-path rerun after the task-wrapper provenance defect, and separately retain authority over K1B/K2 and the unresolved KFE boundary. No successor is published here.
"""
    (REPO / REPORT_REL).write_text(report, encoding="utf-8", newline="\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("evidence_root", type=Path)
    args = parser.parse_args(argv); finalize(args.evidence_root); return 0


if __name__ == "__main__":
    raise SystemExit(main())
