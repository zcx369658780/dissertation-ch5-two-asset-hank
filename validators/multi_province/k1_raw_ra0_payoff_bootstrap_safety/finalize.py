"""Finalize compact evidence for the five-turn common-bootstrap safety diagnostic."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from hashlib import sha256
from pathlib import Path
from typing import Any

import numpy as np


PATHS = {"C": "control_beta2", "R": "raw_beta2"}


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


def _rows(root: Path, turn: int) -> list[dict[str, Any]]:
    rows = read_json(root / f"turn_{turn:02d}" / "per_province_observables.json")
    if len(rows) != 31:
        raise ValueError("every completed turn must contain 31 province rows")
    return rows


def _turn_summary(path_id: str, root: Path, turn: int) -> dict[str, Any]:
    rows = _rows(root, turn)
    application = read_json(root / "payoff_application" / f"completed_turn_{turn:02d}_for_entering_turn_{turn + 1:02d}.json")
    return {
        "path_id": path_id,
        "turn": turn,
        "entering_payoff_mode": rows[0]["entering_payoff_mode"],
        "allocation_payoff_mode": rows[0]["allocation_payoff_mode"],
        "next_payoff_mode": rows[0]["next_payoff_mode"],
        "entering_rah": stats([row["household_rah"] for row in rows]),
        "next_network_rah": stats([row["next_network_rah"] for row in rows]),
        "payoff_source_by_destination": stats(application["payoff_source_by_destination"]),
        "hjb_converged_count": sum(bool(row["hjb_converged"]) for row in rows),
        "hjb_iterations": stats([row["hjb_iterations"] for row in rows]),
        "hjb_statistic": stats([row["hjb_statistic"] for row in rows]),
        "consumption": stats([row["C"] for row in rows]),
        "household_A": stats([row["A"] for row in rows]),
        "household_B": stats([row["B"] for row in rows]),
        "illiquid_transfer_abs_max": max(float(row["hjb_transfer_abs_max"]) for row in rows),
        "illiquid_adjustment_cost_abs_max": max(float(row["hjb_adjustment_cost_abs_max"]) for row in rows),
        "illiquid_drift_abs_max": max(float(row["hjb_mu_a_abs_max"]) for row in rows),
        "liquid_drift_abs_max": max(float(row["hjb_mu_b_abs_max"]) for row in rows),
        "saved_hjb_nonfinite_count": sum(int(row["hjb_saved_array_nonfinite_count"]) for row in rows),
        "hjb_boundary_outward_counts": {
            field: sum(int(row[field]) for row in rows)
            for field in ("hjb_lower_a_outward_count", "hjb_upper_a_outward_count",
                          "hjb_lower_b_outward_count", "hjb_upper_b_outward_count")
        },
        "kkt_diagnostic": "UNAVAILABLE_IN_ACCEPTED_RETURN_OBJECT",
        "kfe_classification_counts": dict(Counter(row["kfe_diagnostic_status"] for row in rows)),
        "capital_column_residual_abs_max": max(abs(float(row["capital_column_residual_MU"])) for row in rows),
        "national_private_capital_conservation_abs_max": max(abs(float(row["national_private_capital_conservation_residual_MU"])) for row in rows),
        "c1_accounting_abs_residual_max": max(abs(float(row["c1_accounting_abs_residual_MU"])) for row in rows),
        "total_K_over_target": stats([row["firm_K_total_over_Ktarget"] for row in rows]),
        "private_K_over_target": stats([row["private_K_over_Ktarget"] for row in rows]),
        "firm_raw_ra0": stats([row["firm_ra0"] for row in rows]),
        "firm_used_ra": stats([row["firm_ra_used"] for row in rows]),
        "firm_rk": stats([row["firm_rk"] for row in rows]),
        "firm_after_tax_profit_over_K": stats([row["firm_after_tax_profit_component_over_K"] for row in rows]),
        "Y": stats([row["Y"] for row in rows]),
        "wage": stats([row["firm_wage_used"] for row in rows]),
        "nk_gap": stats([row["nk_gap"] for row in rows]),
        "yt_gap": stats([row["yt_gap"] for row in rows]),
        "same_S_all": all(bool(row["quantity_and_rah_same_S"]) for row in rows),
        "same_turn_feedback_count": sum(bool(row["same_turn_household_feedback"]) for row in rows),
        "source_faithful_labor_all": all(bool(row["source_faithful_labor_route"]) for row in rows),
    }


def _max_diff(c_rows: list[dict[str, Any]], r_rows: list[dict[str, Any]], fields: tuple[str, ...]) -> dict[str, float]:
    return {field: max(abs(float(c[field]) - float(r[field])) for c, r in zip(c_rows, r_rows)) for field in fields}


def _turn1_hjb_arrays_equal(control_root: Path, raw_root: Path) -> tuple[bool, dict[str, int]]:
    names = ("value", "consumption", "labor", "transfer", "adjustment_cost",
             "effective_illiquid_return", "mu_a", "mu_b", "utility",
             "liquid_label", "transfer_label")
    changed = {name: 0 for name in names}
    for index in range(31):
        province = _rows(control_root, 1)[index]["province"]
        c_path = control_root / "turn_01" / "household" / f"p{index:02d}_{province}" / "hjb_return.npz"
        r_path = raw_root / "turn_01" / "household" / f"p{index:02d}_{province}" / "hjb_return.npz"
        with np.load(c_path, allow_pickle=False) as c_data, np.load(r_path, allow_pickle=False) as r_data:
            for name in names:
                changed[name] += int(np.count_nonzero(c_data[name] != r_data[name]))
    return not any(changed.values()), changed


def _external_manifest(external_root: Path) -> tuple[Path, str, int]:
    manifest_path = external_root / "manifest_sha256.json"
    if manifest_path.exists():
        raise FileExistsError(manifest_path)
    entries = []
    for path in sorted(item for item in external_root.rglob("*") if item.is_file()):
        relative = path.relative_to(external_root).as_posix()
        entries.append({"path": relative, "bytes": path.stat().st_size,
                        "sha256": sha256(path.read_bytes()).hexdigest().upper()})
    write_json(manifest_path, {"schema": "CH5_K1_RAW_RA0_BOOTSTRAP_EXTERNAL_MANIFEST_V1",
                               "file_count": len(entries), "files": entries})
    observed = sha256(manifest_path.read_bytes()).hexdigest().upper()
    verify = read_json(manifest_path)
    for entry in verify["files"]:
        path = external_root / entry["path"]
        if path.stat().st_size != entry["bytes"] or sha256(path.read_bytes()).hexdigest().upper() != entry["sha256"]:
            raise RuntimeError(f"external manifest readback failed: {entry['path']}")
    return manifest_path, observed, len(entries)


def finalize(external_root: Path, output_root: Path) -> None:
    ext = Path(external_root)
    output = Path(output_root)
    output.mkdir(parents=True, exist_ok=False)
    terminals, ledgers, summaries = {}, {}, {}
    for path_id, name in PATHS.items():
        root = ext / name
        terminal = read_json(root / "terminal_result.json")
        ledger = read_json(root / "call_ledger.json")
        if terminal.get("actual_turns_completed") != 5 or terminal.get("error") is not None:
            raise ValueError(f"{path_id}: completed five-turn evidence is required")
        counts = ledger["counts"]
        if counts["hjb_calls"] != 155 or counts["kfe_calls"] != 155:
            raise ValueError(f"{path_id}: exact 155/155 HJB/KFE calls required")
        terminals[path_id], ledgers[path_id] = terminal, ledger
        summaries[path_id] = [_turn_summary(path_id, root, turn) for turn in range(1, 6)]

    c1_rows, r1_rows = _rows(ext / PATHS["C"], 1), _rows(ext / PATHS["R"], 1)
    equivalence_fields = (
        "household_rah", "C", "L", "A", "B", "Kt_supply_private_MU", "GovInv_C1_MU",
        "firm_K_total_MU", "firm_ra0", "firm_ra_used", "Y", "firm_wage_used",
        "hjb_statistic", "hjb_iterations",
    )
    turn1_diff = _max_diff(c1_rows, r1_rows, equivalence_fields)
    turn1_arrays_equal, turn1_array_changed_counts = _turn1_hjb_arrays_equal(
        ext / PATHS["C"], ext / PATHS["R"],
    )
    treatment = []
    for turn in range(2, 6):
        c, r = summaries["C"][turn - 1], summaries["R"][turn - 1]
        treatment.append({
            "turn": turn,
            "control_entering_rah_median": c["entering_rah"]["median"],
            "raw_entering_rah_median": r["entering_rah"]["median"],
            "raw_minus_control_entering_rah_median": r["entering_rah"]["median"] - c["entering_rah"]["median"],
            "raw_over_control_entering_rah_median": r["entering_rah"]["median"] / c["entering_rah"]["median"],
            "control_hjb_converged_count": c["hjb_converged_count"],
            "raw_hjb_converged_count": r["hjb_converged_count"],
            "control_hjb_statistic_max": c["hjb_statistic"]["max"],
            "raw_hjb_statistic_max": r["hjb_statistic"]["max"],
            "control_consumption_median": c["consumption"]["median"],
            "raw_consumption_median": r["consumption"]["median"],
            "control_illiquid_drift_abs_max": c["illiquid_drift_abs_max"],
            "raw_illiquid_drift_abs_max": r["illiquid_drift_abs_max"],
            "control_liquid_drift_abs_max": c["liquid_drift_abs_max"],
            "raw_liquid_drift_abs_max": r["liquid_drift_abs_max"],
            "control_nonfinite_count": c["saved_hjb_nonfinite_count"],
            "raw_nonfinite_count": r["saved_hjb_nonfinite_count"],
            "control_capital_residual_abs_max": c["capital_column_residual_abs_max"],
            "raw_capital_residual_abs_max": r["capital_column_residual_abs_max"],
            "control_c1_residual_abs_max": c["c1_accounting_abs_residual_max"],
            "raw_c1_residual_abs_max": r["c1_accounting_abs_residual_max"],
        })

    manifest_path, manifest_sha, manifest_count = _external_manifest(ext)
    totals = {
        key: sum(int(ledgers[path]["counts"].get(key, 0)) for path in PATHS)
        for key in ("hjb_calls", "hjb_direct_solves", "kfe_calls", "kfe_direct_solves",
                    "labor_roots_attempted", "brentq_calls_attempted", "province_updates_completed")
    }
    summary = {
        "schema": "CH5_K1_RAW_RA0_BOOTSTRAP_SAFETY_SUMMARY_V1",
        "classification": "RAW_RA0_PAYOFF_SHORT_HORIZON_RUNTIME_SAFETY_SUPPORTED_WITH_COMMON_TURN1_BOOTSTRAP",
        "completed_turns": {path: terminals[path]["actual_turns_completed"] for path in PATHS},
        "turn1_bootstrap_equivalence_max_abs_differences": turn1_diff,
        "turn1_hjb_array_changed_counts": turn1_array_changed_counts,
        "turn1_bootstrap_equivalent": all(value == 0.0 for value in turn1_diff.values()) and turn1_arrays_equal,
        "treatment_turns": treatment,
        "per_path_turn_summaries": summaries,
        "total_call_ledger": totals,
        "trajectory_invocations": 2, "scientific_retries": 0,
        "matlab_calls": 0, "standalone_kfe_experiments": 0, "k1b_runs": 0,
        "k2_runs": 0, "ge_calls": 0, "annual_calls": 0, "irf_calls": 0, "results_calls": 0,
        "kkt_diagnostic": "UNAVAILABLE_IN_ACCEPTED_RETURN_OBJECT",
        "kfe_classification": "DIAGNOSTIC_ONLY",
        "results_eligible": False,
        "external_manifest": {"path": str(manifest_path), "sha256": manifest_sha,
                              "file_count_excluding_manifest": manifest_count, "readback": "PASS"},
    }
    if any(item["raw_nonfinite_count"] for item in treatment):
        raise RuntimeError("Raw treatment evidence contains nonfinite HJB arrays")
    if not summary["turn1_bootstrap_equivalent"]:
        raise RuntimeError("Control/Raw turn-1 bootstrap was not exactly reproducible")
    if any(not row["same_S_all"] or row["same_turn_feedback_count"] for row in summaries["R"]):
        raise RuntimeError("Raw same-S/provenance gate failed")
    write_json(output / "summary.json", summary)
    write_json(output / "call_ledger_summary.json", {"per_path": ledgers, "totals": totals})
    write_json(output / "turn1_bootstrap_equivalence.json", {"max_abs_differences": turn1_diff,
                                                               "equivalent": summary["turn1_bootstrap_equivalent"]})
    with (output / "treatment_turn_comparison.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(treatment[0]))
        writer.writeheader()
        writer.writerows(treatment)
    write_json(output / "external_manifest_receipt.json", summary["external_manifest"])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("external_root", type=Path)
    parser.add_argument("output_root", type=Path)
    args = parser.parse_args(argv)
    finalize(args.external_root, args.output_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
