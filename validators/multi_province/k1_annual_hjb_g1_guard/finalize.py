"""Finalize compact evidence for the annual K1A U/G1 diagnostic."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from hashlib import sha256
from pathlib import Path
from typing import Any

import numpy as np


PATHS = {"U": "annual_unguarded", "G1": "annual_g1_guarded"}
CLASSIFICATION = "ANNUAL_RECALIBRATED_K1A_G1_DIAGNOSTIC_GUARD_SHORT_HORIZON_ROUTE_SUPPORTED"


def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        stream.write("\n")


def stats(values: object) -> dict[str, float]:
    array = np.asarray(values, dtype=float)
    return {"min": float(np.min(array)), "median": float(np.median(array)), "max": float(np.max(array))}


def rows(root: Path, turn: int) -> list[dict[str, Any]]:
    value = read_json(root / f"turn_{turn:02d}" / "per_province_observables.json")
    if len(value) != 31:
        raise ValueError("every completed turn must contain 31 province rows")
    return value


def array_envelope(turn_rows: list[dict[str, Any]], field: str) -> dict[str, float]:
    return {
        "min": min(float(row[f"hjb_{field}_min"]) for row in turn_rows),
        "max": max(float(row[f"hjb_{field}_max"]) for row in turn_rows),
        "abs_max": max(float(row[f"hjb_{field}_abs_max"]) for row in turn_rows),
    }


def turn_summary(path_id: str, root: Path, turn: int) -> dict[str, Any]:
    rr = rows(root, turn)
    guard_counts = Counter(str(row["guard_hit"]) for row in rr)
    raw_converted = np.array([row["raw_converted_rah_annual"] for row in rr], dtype=float)
    consumed = np.array([row["hjb_consumed_r_a"] for row in rr], dtype=float)
    return {
        "path_id": path_id, "turn": turn,
        "entering_payoff_mode": rr[0]["entering_payoff_mode"],
        "allocation_payoff_mode": rr[0]["allocation_payoff_mode"],
        "raw_firm_ra0_annual": stats([row["firm_ra0"] for row in rr]),
        "firm_rk_annual": stats([row["firm_rk"] for row in rr]),
        "after_tax_profit_over_K_annual": stats([row["firm_after_tax_profit_component_over_K"] for row in rr]),
        "firm_delta_per_year": stats([row["firm_hjb_delta_per_year"] for row in rr]),
        "raw_ra0_formula_abs_residual_max": max(abs(float(row["firm_ra0"]) - (
            float(row["firm_rk"]) + 0.75 * float(row["firm_profit_over_K"]) - 0.10
        )) for row in rr),
        "profit_component_receipt_abs_difference_max": max(abs(
            float(row["firm_after_tax_profit_component_over_K"]) - 0.75 * float(row["firm_profit_over_K"])
        ) for row in rr),
        "converted_rah_annual_raw": stats(raw_converted),
        "converted_rah_unique_count": int(np.unique(raw_converted).size),
        "hjb_consumed_r_a": stats(consumed),
        "return_guard_counts": dict(sorted(guard_counts.items())),
        "return_guard_upper_share": guard_counts["UPPER"] / 31.0,
        "return_guard_lower_share": guard_counts["LOWER"] / 31.0,
        "return_guard_scope": rr[0]["guard_scope"],
        "wage_guard_lower_hits": sum(bool(row["wage_clipped_lower"]) for row in rr),
        "wage_guard_upper_hits": sum(bool(row["wage_clipped_upper"]) for row in rr),
        "wage_raw": stats([row["firm_wage_raw"] for row in rr]),
        "wage_used": stats([row["firm_wage_used"] for row in rr]),
        "hjb_converged_count": sum(bool(row["hjb_converged"]) for row in rr),
        "hjb_iterations": stats([row["hjb_iterations"] for row in rr]),
        "hjb_statistic": stats([row["hjb_statistic"] for row in rr]),
        "consumption": stats([row["C"] for row in rr]),
        "transfer_d": array_envelope(rr, "transfer"),
        "adjustment_cost": array_envelope(rr, "adjustment_cost"),
        "effective_illiquid_return": array_envelope(rr, "effective_illiquid_return"),
        "mu_a": array_envelope(rr, "mu_a"),
        "mu_b": array_envelope(rr, "mu_b"),
        "boundary_outward_counts": {
            field: sum(int(row[field]) for row in rr)
            for field in ("hjb_lower_a_outward_count", "hjb_upper_a_outward_count",
                          "hjb_lower_b_outward_count", "hjb_upper_b_outward_count")
        },
        "saved_hjb_nonfinite_count": sum(int(row["hjb_saved_array_nonfinite_count"]) for row in rr),
        "kfe_classification_counts": dict(Counter(row["kfe_diagnostic_status"] for row in rr)),
        "capital_column_residual_abs_max_MU": max(abs(float(row["capital_column_residual_MU"])) for row in rr),
        "national_private_capital_conservation_abs_residual_max_MU": max(abs(float(row["national_private_capital_conservation_residual_MU"])) for row in rr),
        "c1_accounting_abs_residual_max_MU": max(abs(float(row["c1_accounting_abs_residual_MU"])) for row in rr),
        "private_K_over_target": stats([row["private_K_over_Ktarget"] for row in rr]),
        "total_K_over_target": stats([row["firm_K_total_over_Ktarget"] for row in rr]),
        "Y": stats([row["Y"] for row in rr]),
        "nk_gap": stats([row["nk_gap"] for row in rr]),
        "yt_gap": stats([row["yt_gap"] for row in rr]),
        "same_S_all": all(bool(row["quantity_and_rah_same_S"]) for row in rr),
        "same_turn_feedback_count": sum(bool(row["same_turn_household_feedback"]) for row in rr),
        "source_faithful_labor_all": all(bool(row["source_faithful_labor_route"]) for row in rr),
    }


def turn1_equivalence(u_root: Path, g_root: Path) -> dict[str, Any]:
    uu, gg = rows(u_root, 1), rows(g_root, 1)
    fields = (
        "household_rah", "raw_converted_rah_annual", "hjb_consumed_r_a", "C", "L", "A", "B",
        "Kt_supply_private_MU", "GovInv_C1_MU", "firm_K_total_MU", "firm_ra0", "firm_ra_used",
        "Y", "firm_wage_used", "hjb_statistic", "hjb_iterations",
    )
    differences = {field: max(abs(float(a[field]) - float(b[field])) for a, b in zip(uu, gg)) for field in fields}
    names = ("value", "consumption", "labor", "transfer", "adjustment_cost", "effective_illiquid_return",
             "mu_a", "mu_b", "utility", "liquid_label", "transfer_label")
    changed = {name: 0 for name in names}
    for index, row in enumerate(uu):
        province = row["province"]
        up = u_root / "turn_01" / "household" / f"p{index:02d}_{province}" / "hjb_return.npz"
        gp = g_root / "turn_01" / "household" / f"p{index:02d}_{province}" / "hjb_return.npz"
        with np.load(up, allow_pickle=False) as ua, np.load(gp, allow_pickle=False) as ga:
            for name in names:
                changed[name] += int(np.count_nonzero(ua[name] != ga[name]))
    equivalent = all(value == 0.0 for value in differences.values()) and not any(changed.values())
    return {"equivalent": equivalent, "max_abs_differences": differences, "hjb_array_changed_counts": changed}


def prior_delta_comparison(external_root: Path, prior_root: Path) -> list[dict[str, Any]]:
    result = []
    for turn in range(1, 6):
        annual = rows(external_root / PATHS["U"], turn)
        prior = rows(prior_root, turn)
        gaps = np.array([float(a["firm_ra0"]) - float(p["firm_ra0"]) for a, p in zip(annual, prior)])
        result.append({"turn": turn, "annual_point10_minus_accepted_point025_ra0": stats(gaps),
                       "descriptive_only": True})
    return result


def receipt_field_adjudication(external_root: Path) -> dict[str, Any]:
    legacy = []
    annual = []
    component_differences = []
    for name in PATHS.values():
        for turn in range(1, 6):
            rr = rows(external_root / name, turn)
            legacy.extend(float(row["firm_ra0_reconstruction_residual"]) for row in rr)
            annual.extend(abs(float(row["firm_ra0"]) - (
                float(row["firm_rk"]) + 0.75 * float(row["firm_profit_over_K"]) - 0.10
            )) for row in rr)
            component_differences.extend(abs(
                float(row["firm_after_tax_profit_component_over_K"]) - 0.75 * float(row["firm_profit_over_K"])
            ) for row in rr)
    invalid = max(abs(value) for value in legacy) > 1e-12
    return {
        "status": "ADJUDICATED_ZERO_SCIENCE" if invalid else "ANNUAL_RECEIPT_VALID",
        "classification": (
            "INVALID_LEGACY_POINT025_RECEIPT_FOR_ANNUAL_TASK__SCIENTIFIC_EXECUTION_UNAFFECTED__FINAL_RUNNER_CORRECTED_ZERO_SCIENCE"
            if invalid else "ANNUAL_POINT10_RECEIPT_VALID"
        ),
        "field": "firm_ra0_reconstruction_residual", "affected_external_rows": len(legacy) if invalid else 0,
        "inherited_legacy_value_min": min(legacy), "inherited_legacy_value_max": max(legacy),
        "inherited_legacy_value_semantics": "ra0-(rk+after_tax_profit_over_K-0.025)" if invalid else None,
        "annual_delta_actually_executed": 0.10,
        "annual_raw_ra0_formula_abs_residual_max": max(annual),
        "profit_component_vs_independent_profit_over_K_times_point75_abs_difference_max": max(component_differences),
        "execution_raw_ra0_formula_abs_residual_field_was_tautological": invalid,
        "model_or_controller_consumed_field": False, "external_evidence_overwritten": False,
        "scientific_retry": False,
    }


def external_manifest(external_root: Path) -> dict[str, Any]:
    path = external_root / "manifest_sha256.json"
    if path.exists():
        raise FileExistsError(path)
    entries = []
    for item in sorted(p for p in external_root.rglob("*") if p.is_file()):
        entries.append({"path": item.relative_to(external_root).as_posix(), "bytes": item.stat().st_size,
                        "sha256": sha256(item.read_bytes()).hexdigest().upper()})
    write_json(path, {"schema": "CH5_K1_ANNUAL_G1_EXTERNAL_MANIFEST_V1", "file_count": len(entries), "files": entries})
    manifest_sha = sha256(path.read_bytes()).hexdigest().upper()
    for entry in read_json(path)["files"]:
        item = external_root / entry["path"]
        if item.stat().st_size != entry["bytes"] or sha256(item.read_bytes()).hexdigest().upper() != entry["sha256"]:
            raise RuntimeError(f"manifest readback failed: {entry['path']}")
    return {"path": str(path), "sha256": manifest_sha, "file_count_excluding_manifest": len(entries), "readback": "PASS"}


def finalize(external_root: Path, prior_point025_root: Path, output_root: Path) -> None:
    ext, prior, output = Path(external_root), Path(prior_point025_root), Path(output_root)
    output.mkdir(parents=True, exist_ok=False)
    terminals, ledgers, summaries = {}, {}, {}
    for path_id, name in PATHS.items():
        root = ext / name
        terminal, ledger = read_json(root / "terminal_result.json"), read_json(root / "call_ledger.json")
        if terminal.get("actual_turns_completed") != 5 or terminal.get("error") is not None:
            raise ValueError(f"{path_id}: completed five-turn evidence required")
        if ledger["counts"]["hjb_calls"] != 155 or ledger["counts"]["kfe_calls"] != 155:
            raise ValueError(f"{path_id}: exact 155/155 HJB/KFE calls required")
        terminals[path_id], ledgers[path_id] = terminal, ledger
        summaries[path_id] = [turn_summary(path_id, root, turn) for turn in range(1, 6)]
    equivalence = turn1_equivalence(ext / PATHS["U"], ext / PATHS["G1"])
    if not equivalence["equivalent"]:
        raise RuntimeError("turn-1 U/G1 equivalence failed")
    treatment = []
    for turn in range(2, 6):
        u, g = summaries["U"][turn - 1], summaries["G1"][turn - 1]
        treatment.append({
            "turn": turn,
            "u_hjb_converged": u["hjb_converged_count"], "g1_hjb_converged": g["hjb_converged_count"],
            "u_hjb_statistic_max": u["hjb_statistic"]["max"], "g1_hjb_statistic_max": g["hjb_statistic"]["max"],
            "u_transfer_abs_max": u["transfer_d"]["abs_max"], "g1_transfer_abs_max": g["transfer_d"]["abs_max"],
            "u_adjustment_cost_abs_max": u["adjustment_cost"]["abs_max"], "g1_adjustment_cost_abs_max": g["adjustment_cost"]["abs_max"],
            "u_mu_a_abs_max": u["mu_a"]["abs_max"], "g1_mu_a_abs_max": g["mu_a"]["abs_max"],
            "u_mu_b_abs_max": u["mu_b"]["abs_max"], "g1_mu_b_abs_max": g["mu_b"]["abs_max"],
            "g1_upper_hits": g["return_guard_counts"].get("UPPER", 0),
            "g1_lower_hits": g["return_guard_counts"].get("LOWER", 0),
            "g1_unsaturated": g["return_guard_counts"].get("UNSATURATED", 0),
        })
    all_summaries = summaries["U"] + summaries["G1"]
    if any(s["saved_hjb_nonfinite_count"] or not s["same_S_all"] or s["same_turn_feedback_count"] for s in all_summaries):
        raise RuntimeError("nonfinite, same-S, or provenance failure in completed evidence")
    totals = {key: sum(int(ledgers[p]["counts"].get(key, 0)) for p in PATHS)
              for key in ("hjb_calls", "hjb_direct_solves", "kfe_calls", "kfe_direct_solves",
                          "labor_roots_attempted", "brentq_calls_attempted", "province_updates_completed")}
    manifest = external_manifest(ext)
    adjudication = receipt_field_adjudication(ext)
    summary = {
        "schema": "CH5_K1_ANNUAL_G1_DIAGNOSTIC_SUMMARY_V1", "classification": CLASSIFICATION,
        "completed_turns": {p: terminals[p]["actual_turns_completed"] for p in PATHS},
        "pre_run_gate": read_json(ext / "pre_run_gate.json"), "turn1_equivalence": equivalence,
        "receipt_field_adjudication": {
            "path": "receipt_field_adjudication.json", "classification": adjudication["classification"],
            "affected_external_rows": adjudication["affected_external_rows"],
            "external_evidence_overwritten": False, "scientific_retry": False,
        },
        "per_path_turn_summaries": summaries, "treatment_comparison": treatment,
        "point10_vs_accepted_point025_ra0": prior_delta_comparison(ext, prior),
        "g1_treatment_guard_totals": {
            "province_turns": 124,
            "upper_hits": sum(row["g1_upper_hits"] for row in treatment),
            "lower_hits": sum(row["g1_lower_hits"] for row in treatment),
            "unsaturated": sum(row["g1_unsaturated"] for row in treatment),
        },
        "wage_guard_classification": "TEMPORARY_NUMERICAL_DIAGNOSTIC_SCAFFOLDING",
        "total_call_ledger": totals, "trajectory_invocations": 2, "scientific_retries": 0,
        "matlab_calls": 0, "standalone_kfe_experiments": 0, "k1b_runs": 0, "k2_runs": 0,
        "ge_calls": 0, "annual_downstream_calls": 0, "shock_irf_calls": 0, "results_calls": 0,
        "kfe_classification": "DIAGNOSTIC_ONLY",
        "provisional_steady_state_route": "SUPPORTED_ONLY_AS_GUARD_DEPENDENT_CANDIDATE_REQUIRING_FRESH_LONGER_BOUNDED_TASK",
        "results_eligible": False, "external_manifest": manifest,
    }
    write_json(output / "summary.json", summary)
    write_json(output / "call_ledger_summary.json", {"per_path": ledgers, "totals": totals})
    write_json(output / "turn1_equivalence.json", equivalence)
    write_json(output / "external_manifest_receipt.json", manifest)
    write_json(output / "receipt_field_adjudication.json", adjudication)
    with (output / "treatment_turn_comparison.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(treatment[0]))
        writer.writeheader()
        writer.writerows(treatment)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("external_root", type=Path)
    parser.add_argument("prior_point025_root", type=Path)
    parser.add_argument("output_root", type=Path)
    args = parser.parse_args(argv)
    finalize(args.external_root, args.prior_point025_root, args.output_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
