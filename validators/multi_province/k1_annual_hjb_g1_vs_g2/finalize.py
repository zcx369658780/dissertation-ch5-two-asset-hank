"""Finalize compact evidence for the annual K1A G1/G2 guard diagnostic."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from hashlib import sha256
from pathlib import Path
from typing import Any

import numpy as np

from validators.multi_province.k1_annual_hjb_g1_vs_g2.run import WAGE_HIT_CRITERION


PATHS = {"G1": "annual_g1_guarded", "G2": "annual_g2_guarded"}


def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        stream.write("\n")


def stats(values: object) -> dict[str, float]:
    a = np.asarray(values, dtype=float)
    if not np.all(np.isfinite(a)):
        raise ValueError("summary input contains NaN/Inf")
    return {"min": float(np.min(a)), "median": float(np.median(a)), "max": float(np.max(a))}


def rows(root: Path, turn: int) -> list[dict[str, Any]]:
    value = read_json(root / f"turn_{turn:02d}" / "per_province_observables.json")
    if len(value) != 31:
        raise ValueError("every completed turn must contain 31 province rows")
    return value


def envelope(rr: list[dict[str, Any]], field: str) -> dict[str, float]:
    return {"min": min(float(r[f"hjb_{field}_min"]) for r in rr),
            "max": max(float(r[f"hjb_{field}_max"]) for r in rr),
            "abs_max": max(float(r[f"hjb_{field}_abs_max"]) for r in rr)}


def hit_summary(rr: list[dict[str, Any]], prefix: str, *, allow_not_applied: bool = False) -> dict[str, Any]:
    groups = {
        "lower": [r["province"] for r in rr if bool(r[f"{prefix}_lower_hit"])],
        "upper": [r["province"] for r in rr if bool(r[f"{prefix}_upper_hit"])],
        "unsaturated": [r["province"] for r in rr if bool(r[f"{prefix}_unsaturated"])],
    }
    classified = sum(len(v) for v in groups.values())
    if allow_not_applied and classified == 0:
        groups["not_applied_bootstrap"] = [r["province"] for r in rr]
    elif classified != 31:
        raise ValueError(f"{prefix} hit flags are not exhaustive and exclusive")
    return {key: {"count": len(names), "share": len(names) / 31.0, "provinces": names}
            for key, names in groups.items()}


def turn_summary(path_id: str, root: Path, turn: int) -> dict[str, Any]:
    rr = rows(root, turn)
    converted = np.array([r["raw_converted_rah_annual"] for r in rr], dtype=float)
    consumed = np.array([r["hjb_consumed_r_a"] for r in rr], dtype=float)
    return {
        "path_id": path_id, "turn": turn,
        "entering_payoff_mode": rr[0]["entering_payoff_mode"],
        "allocation_payoff_mode": rr[0]["allocation_payoff_mode"],
        "raw_firm_ra0_annual": stats([r["firm_ra0"] for r in rr]),
        "firm_rk_annual": stats([r["firm_rk"] for r in rr]),
        "after_tax_profit_over_K_annual": stats([r["firm_after_tax_profit_component_over_K"] for r in rr]),
        "firm_delta_per_year": stats([r["firm_hjb_delta_per_year"] for r in rr]),
        "raw_ra0_formula_abs_residual_max": max(float(r["raw_ra0_formula_abs_residual"]) for r in rr),
        "converted_rah_annual_raw": stats(converted),
        "converted_rah_distinct_count": int(np.unique(converted).size),
        "hjb_consumed_r_a": stats(consumed),
        "hjb_consumed_r_a_distinct_count": int(np.unique(consumed).size),
        "return_hits": hit_summary(rr, "return_guard", allow_not_applied=turn == 1),
        "wage_raw": stats([r["firm_wage_raw"] for r in rr]),
        "wage_guarded_wjt": stats([r["firm_wage_used"] for r in rr]),
        "wage_hits": hit_summary(rr, "wage_guard"),
        "wage_hit_criterion": rr[0]["wage_hit_criterion"],
        "hjb_converged_count": sum(bool(r["hjb_converged"]) for r in rr),
        "hjb_statistic": stats([r["hjb_statistic"] for r in rr]),
        "hjb_iterations": stats([r["hjb_iterations"] for r in rr]),
        "consumption": stats([r["C"] for r in rr]),
        "transfer_d": envelope(rr, "transfer"),
        "adjustment_cost": envelope(rr, "adjustment_cost"),
        "effective_illiquid_return": envelope(rr, "effective_illiquid_return"),
        "mu_a_liquid_drift": envelope(rr, "mu_a"),
        "mu_b_illiquid_drift": envelope(rr, "mu_b"),
        "boundary_outward_counts": {field: sum(int(r[field]) for r in rr) for field in (
            "hjb_lower_a_outward_count", "hjb_upper_a_outward_count",
            "hjb_lower_b_outward_count", "hjb_upper_b_outward_count")},
        "saved_hjb_nonfinite_count": sum(int(r["hjb_saved_array_nonfinite_count"]) for r in rr),
        "kfe_classification_counts": dict(Counter(r["kfe_diagnostic_status"] for r in rr)),
        "capital_column_residual_abs_max_MU": max(abs(float(r["capital_column_residual_MU"])) for r in rr),
        "national_capital_residual_abs_max_MU": max(abs(float(r["national_private_capital_conservation_residual_MU"])) for r in rr),
        "c1_accounting_abs_residual_max_MU": max(abs(float(r["c1_accounting_abs_residual_MU"])) for r in rr),
        "private_K_over_target": stats([r["private_K_over_Ktarget"] for r in rr]),
        "total_K_over_target": stats([r["firm_K_total_over_Ktarget"] for r in rr]),
        "GovInv_C1_MU": stats([r["GovInv_C1_MU"] for r in rr]),
        "Y": stats([r["Y"] for r in rr]), "nk_gap": stats([r["nk_gap"] for r in rr]),
        "yt_gap": stats([r["yt_gap"] for r in rr]),
        "same_S_all": all(bool(r["quantity_and_rah_same_S"]) for r in rr),
        "same_turn_feedback_count": sum(bool(r["same_turn_household_feedback"]) for r in rr),
        "source_faithful_labor_all": all(bool(r["source_faithful_labor_route"]) for r in rr),
    }


def turn1_equivalence(a_root: Path, b_root: Path) -> dict[str, Any]:
    aa, bb = rows(a_root, 1), rows(b_root, 1)
    fields = ("household_rah", "raw_converted_rah_annual", "hjb_consumed_r_a", "C", "L", "A", "B",
              "Kt_supply_private_MU", "GovInv_C1_MU", "firm_K_total_MU", "firm_ra0", "firm_ra_used",
              "Y", "firm_wage_raw", "firm_wage_used", "hjb_statistic", "hjb_iterations")
    differences = {f: max(abs(float(a[f]) - float(b[f])) for a, b in zip(aa, bb)) for f in fields}
    names = ("value", "consumption", "labor", "transfer", "adjustment_cost", "effective_illiquid_return",
             "mu_a", "mu_b", "utility", "liquid_label", "transfer_label")
    changed = {name: 0 for name in names}
    for index, row in enumerate(aa):
        province = row["province"]
        ap = a_root / "turn_01" / "household" / f"p{index:02d}_{province}" / "hjb_return.npz"
        bp = b_root / "turn_01" / "household" / f"p{index:02d}_{province}" / "hjb_return.npz"
        with np.load(ap, allow_pickle=False) as ax, np.load(bp, allow_pickle=False) as bx:
            for name in names:
                changed[name] += int(np.count_nonzero(ax[name] != bx[name]))
    equivalent = all(v == 0.0 for v in differences.values()) and not any(changed.values())
    return {"equivalent": equivalent, "max_abs_differences": differences,
            "hjb_array_changed_counts": changed}


def repeated_hits(summaries: list[dict[str, Any]], kind: str, side: str) -> dict[str, int]:
    counter: Counter[str] = Counter()
    for summary in summaries[1:]:
        counter.update(summary[f"{kind}_hits"][side]["provinces"])
    return dict(sorted((name, count) for name, count in counter.items() if count >= 2))


def aggregate_hits(summaries: list[dict[str, Any]], kind: str) -> dict[str, Any]:
    result: dict[str, Any] = {"province_turns": 124}
    for side in ("lower", "upper", "unsaturated"):
        names = [name for summary in summaries[1:] for name in summary[f"{kind}_hits"][side]["provinces"]]
        result[side] = {"count": len(names), "share": len(names) / 124.0,
                        "province_counts": dict(sorted(Counter(names).items()))}
    return result


def route_decision(g1: list[dict[str, Any]], g2: list[dict[str, Any]], g2_unsaturated_share: float) -> str:
    """Do not encode an unfrozen materiality or deterioration threshold."""

    del g1, g2, g2_unsaturated_share
    return "REVIEW_REQUIRED__NO_AUTOMATIC_LONGER_G2_ROUTE"


def external_manifest(root: Path) -> dict[str, Any]:
    path = root / "manifest_sha256.json"
    if path.exists():
        raise FileExistsError(path)
    entries = [{"path": p.relative_to(root).as_posix(), "bytes": p.stat().st_size,
                "sha256": sha256(p.read_bytes()).hexdigest().upper()}
               for p in sorted(x for x in root.rglob("*") if x.is_file())]
    write_json(path, {"schema": "CH5_K1_ANNUAL_G1_VS_G2_EXTERNAL_MANIFEST_V1",
                      "file_count": len(entries), "files": entries})
    for e in read_json(path)["files"]:
        p = root / e["path"]
        if p.stat().st_size != e["bytes"] or sha256(p.read_bytes()).hexdigest().upper() != e["sha256"]:
            raise RuntimeError(f"manifest readback failed: {e['path']}")
    return {"path": str(path), "sha256": sha256(path.read_bytes()).hexdigest().upper(),
            "file_count_excluding_manifest": len(entries), "readback": "PASS"}


def finalize(external_root: Path, output_root: Path) -> None:
    ext, out = Path(external_root), Path(output_root)
    out.mkdir(parents=True, exist_ok=False)
    terminals: dict[str, Any] = {}; ledgers: dict[str, Any] = {}; summaries: dict[str, Any] = {}
    for path_id, name in PATHS.items():
        root = ext / name
        terminal, ledger = read_json(root / "terminal_result.json"), read_json(root / "call_ledger.json")
        if terminal.get("actual_turns_completed") != 5 or terminal.get("error") is not None:
            raise ValueError(f"{path_id}: completed five-turn evidence required")
        if ledger["counts"]["hjb_calls"] != 155 or ledger["counts"]["kfe_calls"] != 155:
            raise ValueError(f"{path_id}: exact 155/155 HJB/KFE calls required")
        terminals[path_id], ledgers[path_id] = terminal, ledger
        summaries[path_id] = [turn_summary(path_id, root, t) for t in range(1, 6)]
    equivalence = turn1_equivalence(ext / PATHS["G1"], ext / PATHS["G2"])
    if not equivalence["equivalent"]:
        raise RuntimeError("turn-1 G1/G2 equivalence failed")
    all_summaries = summaries["G1"] + summaries["G2"]
    if any(s["saved_hjb_nonfinite_count"] or not s["same_S_all"] or s["same_turn_feedback_count"]
           or not s["source_faithful_labor_all"] for s in all_summaries):
        raise RuntimeError("nonfinite, same-S, provenance, or labor-route failure")
    comparison = []
    for turn in range(2, 6):
        a, b = summaries["G1"][turn - 1], summaries["G2"][turn - 1]
        comparison.append({
            "turn": turn, "g1_return_upper_hits": a["return_hits"]["upper"]["count"],
            "g2_return_upper_hits": b["return_hits"]["upper"]["count"],
            "g1_return_unsaturated": a["return_hits"]["unsaturated"]["count"],
            "g2_return_unsaturated": b["return_hits"]["unsaturated"]["count"],
            "g1_consumed_distinct": a["hjb_consumed_r_a_distinct_count"],
            "g2_consumed_distinct": b["hjb_consumed_r_a_distinct_count"],
            "g1_hjb_converged": a["hjb_converged_count"], "g2_hjb_converged": b["hjb_converged_count"],
            "g1_hjb_statistic_max": a["hjb_statistic"]["max"], "g2_hjb_statistic_max": b["hjb_statistic"]["max"],
            "g1_transfer_abs_max": a["transfer_d"]["abs_max"], "g2_transfer_abs_max": b["transfer_d"]["abs_max"],
            "g1_adjustment_cost_abs_max": a["adjustment_cost"]["abs_max"],
            "g2_adjustment_cost_abs_max": b["adjustment_cost"]["abs_max"],
            "g1_mu_a_abs_max": a["mu_a_liquid_drift"]["abs_max"], "g2_mu_a_abs_max": b["mu_a_liquid_drift"]["abs_max"],
            "g1_mu_b_abs_max": a["mu_b_illiquid_drift"]["abs_max"], "g2_mu_b_abs_max": b["mu_b_illiquid_drift"]["abs_max"],
            "g1_wage_lower_hits": a["wage_hits"]["lower"]["count"], "g2_wage_lower_hits": b["wage_hits"]["lower"]["count"],
            "g1_wage_upper_hits": a["wage_hits"]["upper"]["count"], "g2_wage_upper_hits": b["wage_hits"]["upper"]["count"],
        })
    totals = {key: sum(int(ledgers[p]["counts"].get(key, 0)) for p in PATHS) for key in (
        "hjb_calls", "hjb_direct_solves", "kfe_calls", "kfe_direct_solves",
        "labor_roots_attempted", "brentq_calls_attempted", "province_updates_completed")}
    return_totals = {p: aggregate_hits(summaries[p], "return") for p in PATHS}
    wage_totals = {p: aggregate_hits(summaries[p], "wage") for p in PATHS}
    g2_unsat_share = return_totals["G2"]["unsaturated"]["share"]
    route = route_decision(summaries["G1"], summaries["G2"], g2_unsat_share)
    manifest = external_manifest(ext)
    summary = {
        "schema": "CH5_K1_ANNUAL_G1_VS_G2_SUMMARY_V1",
        "classification": "ANNUAL_K1A_G1_VS_G2_PRICE_GUARD_CONTINUATION_DIAGNOSTIC_COMPLETED",
        "completed_turns": {p: terminals[p]["actual_turns_completed"] for p in PATHS},
        "pre_run_gate": read_json(ext / "pre_run_gate.json"), "turn1_equivalence": equivalence,
        "per_path_turn_summaries": summaries, "treatment_comparison": comparison,
        "return_guard_treatment_totals": return_totals, "wage_guard_treatment_totals": wage_totals,
        "repeated_return_hits": {p: {s: repeated_hits(summaries[p], "return", s) for s in ("lower", "upper")} for p in PATHS},
        "repeated_wage_hits": {p: {s: repeated_hits(summaries[p], "wage", s) for s in ("lower", "upper")} for p in PATHS},
        "wage_hit_criterion": WAGE_HIT_CRITERION,
        "route_decision_status": "REVIEW_REQUIRED__NO_AUTOMATIC_LONGER_G2_ROUTE",
        "adjudication_files_if_post_execution_judgment_is_added": {
            "route": "route_adjudication.json", "wage_criterion": "wage_criterion_adjudication.json"
        },
        "zero_diagnostic_price_guard_hits": {p: return_totals[p]["lower"]["count"] == 0 and
             return_totals[p]["upper"]["count"] == 0 and wage_totals[p]["lower"]["count"] == 0 and
             wage_totals[p]["upper"]["count"] == 0 for p in PATHS},
        "g2_provisional_longer_horizon_route": route,
        "total_call_ledger": totals, "trajectory_invocations": 2, "scientific_retries": 0,
        "matlab_calls": 0, "standalone_kfe_experiments": 0, "k1b_runs": 0, "k2_runs": 0,
        "ge_calls": 0, "annual_downstream_calls": 0, "shock_irf_calls": 0, "results_calls": 0,
        "kfe_classification": "DIAGNOSTIC_ONLY", "results_eligible": False,
        "external_manifest": manifest,
    }
    write_json(out / "summary.json", summary)
    write_json(out / "call_ledger_summary.json", {"per_path": ledgers, "totals": totals})
    write_json(out / "turn1_equivalence.json", equivalence)
    write_json(out / "external_manifest_receipt.json", manifest)
    with (out / "treatment_turn_comparison.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(comparison[0])); writer.writeheader(); writer.writerows(comparison)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("external_root", type=Path); parser.add_argument("output_root", type=Path)
    args = parser.parse_args(argv); finalize(args.external_root, args.output_root); return 0


if __name__ == "__main__":
    raise SystemExit(main())
