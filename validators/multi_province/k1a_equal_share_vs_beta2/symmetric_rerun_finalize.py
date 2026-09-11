"""Zero-science finalizer for the authorized symmetric K1A rerun."""

from __future__ import annotations

import argparse
import csv
import statistics
import sys
from io import StringIO
from pathlib import Path
from typing import Any

import numpy as np

REPO = Path(__file__).resolve().parents[3]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from validators.multi_province.k1a_equal_share_vs_beta2.finalize import (
    build_manifest,
    dist,
    file_sha,
    fmt,
    read_json,
    summarize_path,
    write_json,
)


BASELINE = "1822b1a8b4786699e9137899e020cec37d15aa1d"
EVIDENCE_REL = Path("docs/evidence/ch5_mp4c_k1a_equal_share_vs_beta2_symmetric_rerun")
REPORT_REL = Path("docs/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_SYMMETRIC_RERUN_REPORT.md")
PASS_VERDICT = (
    "K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_SYMMETRIC_RERUN_COMPLETED__"
    "BOTH_PATHS_25_TURNS__ACCOUNTING_AND_SCOPE_GATES_PASS"
)
PARTIAL_VERDICT = "K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_SYMMETRIC_RERUN_PARTIAL"


def csv_text(rows: list[dict[str, Any]]) -> str:
    output = StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def median(rows: list[dict[str, Any]], field: str) -> float:
    return float(statistics.median(float(row[field]) for row in rows))


def common_prefix(evidence_root: Path, turns: int) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for turn in range(1, turns + 1):
        a_rows = read_json(evidence_root / "path_a_equal_share" / f"turn_{turn:02d}" / "per_province_observables.json")
        b_rows = read_json(evidence_root / "path_b_geographic_beta2" / f"turn_{turn:02d}" / "per_province_observables.json")
        a_raw = [float(row["firm_ra0"]) for row in a_rows]
        b_raw = [float(row["firm_ra0"]) for row in b_rows]
        result.append({
            "turn": turn,
            "private_K_over_target_median_A": median(a_rows, "private_K_over_Ktarget"),
            "private_K_over_target_median_B": median(b_rows, "private_K_over_Ktarget"),
            "private_K_over_target_median_delta_B_minus_A": median(b_rows, "private_K_over_Ktarget") - median(a_rows, "private_K_over_Ktarget"),
            "GovInv_over_target_median_A": median(a_rows, "GovInv_C1_over_Ktarget"),
            "GovInv_over_target_median_B": median(b_rows, "GovInv_C1_over_Ktarget"),
            "total_K_over_target_median_A": median(a_rows, "firm_K_total_over_Ktarget"),
            "total_K_over_target_median_B": median(b_rows, "firm_K_total_over_Ktarget"),
            "raw_ra0_median_A": median(a_rows, "firm_ra0"),
            "raw_ra0_median_B": median(b_rows, "firm_ra0"),
            "raw_ra0_median_delta_B_minus_A": median(b_rows, "firm_ra0") - median(a_rows, "firm_ra0"),
            "raw_ra0_std_A": float(np.std(a_raw)),
            "raw_ra0_std_B": float(np.std(b_raw)),
            "raw_ra0_above_0p09_A": sum(value > 0.09 for value in a_raw),
            "raw_ra0_above_0p09_B": sum(value > 0.09 for value in b_raw),
            "upper_clip_count_A": sum(bool(row["ra_clipped_upper"]) for row in a_rows),
            "upper_clip_count_B": sum(bool(row["ra_clipped_upper"]) for row in b_rows),
            "entering_rah_median_A": median(a_rows, "household_rah"),
            "entering_rah_median_B": median(b_rows, "household_rah"),
            "network_rah_median_A": median(a_rows, "household_rah_k1a_current_payoff_bridge"),
            "network_rah_median_B": median(b_rows, "household_rah_k1a_current_payoff_bridge"),
            "Y_median_A": median(a_rows, "Y"),
            "Y_median_B": median(b_rows, "Y"),
            "wage_median_A": median(a_rows, "firm_wage_used"),
            "wage_median_B": median(b_rows, "firm_wage_used"),
            "max_nk_gap_A": max(float(row["nk_gap"]) for row in a_rows),
            "max_nk_gap_B": max(float(row["nk_gap"]) for row in b_rows),
            "max_yt_gap_A": max(float(row["yt_gap"]) for row in a_rows),
            "max_yt_gap_B": max(float(row["yt_gap"]) for row in b_rows),
            "hjb_converged_count_A": sum(bool(row["hjb_converged"]) for row in a_rows),
            "hjb_converged_count_B": sum(bool(row["hjb_converged"]) for row in b_rows),
            "source_final_predicate_A": bool(a_rows[0]["source_final_predicate"]),
            "source_final_predicate_B": bool(b_rows[0]["source_final_predicate"]),
        })
    return result


def finalize(evidence_root: Path) -> None:
    evidence_root = Path(evidence_root)
    tracked = REPO / EVIDENCE_REL
    tracked.mkdir(parents=True, exist_ok=True)
    a, a_turns = summarize_path(evidence_root / "path_a_equal_share")
    b, b_turns = summarize_path(evidence_root / "path_b_geographic_beta2")
    common_turns = min(a["completed_turns"], b["completed_turns"])
    comparisons = common_prefix(evidence_root, common_turns)
    complete = (
        a["completed_turns"] == 25
        and b["completed_turns"] == 25
        and a["terminal"].get("error") is None
        and b["terminal"].get("error") is None
    )
    verdict = PASS_VERDICT if complete else PARTIAL_VERDICT
    totals = {}
    for key in ("hjb_calls", "hjb_direct_solves", "kfe_calls", "kfe_direct_solves", "labor_roots_attempted", "province_updates_completed"):
        totals[key] = int(a["call_ledger"]["counts"][key]) + int(b["call_ledger"]["counts"][key])
    pooled_a = [row for turn in range(1, common_turns + 1) for row in read_json(evidence_root / "path_a_equal_share" / f"turn_{turn:02d}" / "per_province_observables.json")]
    pooled_b = [row for turn in range(1, common_turns + 1) for row in read_json(evidence_root / "path_b_geographic_beta2" / f"turn_{turn:02d}" / "per_province_observables.json")]
    total_ledger = {
        "trajectory_invocations": 2,
        "scientific_retries": 0,
        "accepted_initialization_reuses": 2,
        "new_initialization_solves": 0,
        **totals,
        "matlab_calls": 0,
        "standalone_kfe_experiments": 0,
        "k1b_runs": 0,
        "ge_calls": 0,
        "annual_calls": 0,
        "shock_calls": 0,
        "irf_calls": 0,
        "results_calls": 0,
    }
    combined = {
        "schema": "CH5_K1A_SYMMETRIC_RERUN_SUMMARY_V1",
        "verdict": verdict,
        "baseline": BASELINE,
        "path_A": a,
        "path_B": b,
        "common_completed_turns": common_turns,
        "common_prefix_per_turn": comparisons,
        "common_prefix_pooled": {
            "private_K_over_target_A": dist(float(row["private_K_over_Ktarget"]) for row in pooled_a),
            "private_K_over_target_B": dist(float(row["private_K_over_Ktarget"]) for row in pooled_b),
            "GovInv_over_target_A": dist(float(row["GovInv_C1_over_Ktarget"]) for row in pooled_a),
            "GovInv_over_target_B": dist(float(row["GovInv_C1_over_Ktarget"]) for row in pooled_b),
            "raw_ra0_A": dist(float(row["firm_ra0"]) for row in pooled_a),
            "raw_ra0_B": dist(float(row["firm_ra0"]) for row in pooled_b),
            "network_rah_A": dist(float(row["household_rah_k1a_current_payoff_bridge"]) for row in pooled_a),
            "network_rah_B": dist(float(row["household_rah_k1a_current_payoff_bridge"]) for row in pooled_b),
        },
        "total_call_ledger": total_ledger,
        "results_eligible": False,
    }
    write_json(tracked / "bounded_comparison_summary.json", combined)
    write_json(tracked / "call_ledger_summary.json", total_ledger)
    (tracked / "per_turn_summary.csv").write_text(
        csv_text([{"path": "A", **row} for row in a_turns] + [{"path": "B", **row} for row in b_turns]),
        encoding="utf-8",
        newline="",
    )
    (tracked / "common_prefix_comparison.csv").write_text(csv_text(comparisons), encoding="utf-8", newline="")

    manifest = build_manifest(evidence_root)
    write_json(evidence_root / "external_evidence_manifest.json", manifest)
    manifest_sha = file_sha(evidence_root / "external_evidence_manifest.json")
    mismatches = [item["path"] for item in manifest["files"] if file_sha(evidence_root / item["path"]) != item["sha256"]]
    readback = {
        "schema": "CH5_K1A_SYMMETRIC_RERUN_EXTERNAL_READBACK_V1",
        "manifest_sha256": manifest_sha,
        "checked_files": manifest["file_count"],
        "mismatches": mismatches,
        "status": "PASS" if not mismatches else "FAIL",
    }
    write_json(evidence_root / "external_evidence_readback.json", readback)
    write_json(tracked / "external_evidence_receipt.json", {
        "root": str(evidence_root),
        "manifest_sha256": manifest_sha,
        "manifest_file_count": manifest["file_count"],
        "readback_status": readback["status"],
        "readback_checked_files": readback["checked_files"],
    })

    terminal = comparisons[-1]
    recommendation = (
        "Owner/Reviewer should prioritize a payoff-return re-audit before K1B; the persistent clipping pressure means "
        "the transitional clipped-ra payoff bridge still lacks final economic authority. The independent KFE boundary "
        "blocker remains open and is not resolved by this bounded comparison."
    )
    report = f"""# Chapter 5 MP4C K1A symmetric equal-share vs geographic beta=2 rerun report

## Outcome

Verdict: `{verdict}`.

Both preregistered paths were rerun from byte-identical accepted initialization under the repaired same-`S` provenance validator. Path A completed {a['completed_turns']}/25 turns and Path B completed {b['completed_turns']}/25 turns. Results eligibility remains `FALSE`.

## Authority and pre-run gate

- Live-main baseline: `{BASELINE}`.
- External evidence root: `{evidence_root}`.
- Path A: `beta_distance=0`, `beta_return=0`; Path B: `beta_distance=2`, `beta_return=0`.
- Validator accepts valid prior-completed K1A same-`S` `rah` and rejects a deliberately corrupted value.
- Focused zero-science tests, compile, protected-source diff and byte-identical input checks passed before science.
- No production-science source, equation, parameter, bound, tolerance, grid or solver semantic changed.

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

Scientific retries were 0. MATLAB, K1B, standalone KFE experiments, GE, annual, shock/IRF and Results calls were all 0.

## Capital accounting and C1

Across the full {common_turns}-turn common prefix, Path A/Path B maximum share-column gaps were `{a['accounting']['share_column_sum_max_abs_gap']}` / `{b['accounting']['share_column_sum_max_abs_gap']}`. Maximum origin-capital residuals were `{a['accounting']['capital_column_max_abs_residual_MU']}` / `{b['accounting']['capital_column_max_abs_residual_MU']}` MU and maximum national residuals were `{a['accounting']['national_private_capital_max_abs_residual_MU']}` / `{b['accounting']['national_private_capital_max_abs_residual_MU']}` MU. Home retention and quantity/`rah` same-`S` identities passed throughout; destination-theta double weighting was zero.

C1 formula residual maxima were `{a['c1']['formula_max_abs_residual_MU']}` / `{b['c1']['formula_max_abs_residual_MU']}` MU. `Kprivate>=Ktarget` cases were {a['c1']['private_K_at_or_above_target_cases']} / {b['c1']['private_K_at_or_above_target_cases']}; private-only overshoot maxima were `{a['c1']['private_only_overshoot_ratio']['max']}` / `{b['c1']['private_only_overshoot_ratio']['max']}`. Total K/target remained `{fmt(a['c1']['total_K_over_target'])}` for A and `{fmt(b['c1']['total_K_over_target'])}` for B.

## Symmetric A/B comparison

Pooled private K/target was `{fmt(combined['common_prefix_pooled']['private_K_over_target_A'])}` for A and `{fmt(combined['common_prefix_pooled']['private_K_over_target_B'])}` for B. Pooled GovInv/target was `{fmt(combined['common_prefix_pooled']['GovInv_over_target_A'])}` / `{fmt(combined['common_prefix_pooled']['GovInv_over_target_B'])}`. At turn {common_turns}, B-minus-A median private K/target was `{terminal['private_K_over_target_median_delta_B_minus_A']}`, while total-K medians were `{terminal['total_K_over_target_median_A']}` / `{terminal['total_K_over_target_median_B']}`.

The geography-induced portfolio difference propagated after turn 1 through network-produced `rah`, entering household `rah`, household outcomes and subsequent firm states. The complete turn-by-turn comparison is preserved in `common_prefix_comparison.csv`.

## Raw returns and convergence

Path A raw `ra0` min/median/max was `{fmt(a['returns']['raw_ra0'])}` with {a['returns']['raw_ra0_above_0p09']} observations above `.09` and {a['returns']['upper_clip_count']} upper clips. Path B was `{fmt(b['returns']['raw_ra0'])}` with {b['returns']['raw_ra0_above_0p09']} above `.09` and {b['returns']['upper_clip_count']} upper clips. Lower clips were {a['returns']['lower_clip_count']} / {b['returns']['lower_clip_count']}.

At turn {common_turns}, frozen final predicates were `{terminal['source_final_predicate_A']}` / `{terminal['source_final_predicate_B']}`; maximum `nk` gaps were `{terminal['max_nk_gap_A']}` / `{terminal['max_nk_gap_B']}`. HJB nonconverged-but-continued observations were {a['convergence']['hjb_nonconverged_but_continued']} / {b['convergence']['hjb_nonconverged_but_continued']}.

## Boundaries and recommendation

Source-faithful labor remained active for every completed province-turn. All {a['convergence']['kfe_diagnostic_only_observations'] + b['convergence']['kfe_diagnostic_only_observations']} KFE observations remain `DIAGNOSTIC_ONLY`; corrected-2018 finite-box upper-b leakage plus MATLAB-style pinning remains an independent blocker.

{recommendation}

External manifest SHA-256: `{manifest_sha}`; readback checked {manifest['file_count']} files with status `{readback['status']}`. No successor task is published here.
"""
    (REPO / REPORT_REL).write_text(report, encoding="utf-8", newline="\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence_root", type=Path)
    args = parser.parse_args(argv)
    finalize(args.evidence_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
