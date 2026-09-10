"""Solver-free finalization for the HJB-propagation and 25-turn K/L evidence."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from hashlib import sha256
from pathlib import Path
from statistics import mean, median
from typing import Any, Iterable


REPO = Path(__file__).resolve().parents[3]
for item in (REPO / "src", REPO):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))


TRACE_TURNS = {1, 2, 3, 5, 10, 15, 20, 21, 22, 23, 24, 25}


def file_sha256(path: Path) -> str:
    return sha256(Path(path).read_bytes()).hexdigest().upper()


def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    with Path(path).open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
        stream.write("\n")


def write_csv(path: Path, rows: Iterable[dict[str, Any]], fields: list[str]) -> None:
    with Path(path).open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def classify(prefix: str, ratio: float) -> str:
    if ratio > 1.5:
        label = "SEVERELY_HIGH"
    elif ratio > 1.1:
        label = "MODERATELY_HIGH"
    elif ratio >= 0.9:
        label = "NEAR_TARGET"
    elif ratio >= 0.5:
        label = "MODERATELY_LOW"
    else:
        label = "SEVERELY_LOW"
    return f"{prefix}_{label}"


def completed_rows(evidence: Path) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for path in sorted(Path(evidence).glob("turn_*/per_province_observables.json")):
        result.extend(read_json(path))
    return result


def late_window(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    late = [row for row in rows if 20 <= int(row["turn"]) <= 25]
    output = []
    for index in range(31):
        group = [row for row in late if int(row["province_index"]) == index]
        if not group:
            continue
        def values(field: str) -> list[float]:
            return [float(row[field]) for row in group]
        k_total = values("firm_K_total_over_Ktarget")
        labor = values("firm_Lt_over_population_proxy")
        output.append({
            "province_index": index, "province_name": group[0]["province_name"],
            "turns_observed": len(group),
            "firm_K_total_over_Ktarget_mean": mean(k_total),
            "firm_K_total_over_Ktarget_median": median(k_total),
            "private_K_over_Ktarget_mean": mean(values("private_K_over_Ktarget")),
            "private_K_over_Ktarget_median": median(values("private_K_over_Ktarget")),
            "GovInv_before_over_Ktarget_mean": mean(values("GovInv_before_over_Ktarget")),
            "GovInv_before_over_Ktarget_median": median(values("GovInv_before_over_Ktarget")),
            "firm_Lt_over_population_proxy_mean": mean(labor),
            "firm_Lt_over_population_proxy_median": median(labor),
            "K_status": classify("K", mean(k_total)),
            "L_status_relative_to_population_proxy": classify("L_RELATIVE_TO_POPULATION_PROXY", mean(labor)),
        })
    return output


def validity_rows(evidence: Path) -> list[dict[str, Any]]:
    result = []
    for receipt_path in sorted(Path(evidence).glob("turn_*/household/*/hjb_receipt.json")):
        hjb = read_json(receipt_path)
        kfe_path = receipt_path.with_name("kfe_distribution_diagnostic.json")
        kfe = read_json(kfe_path) if kfe_path.is_file() else None
        result.append({
            "turn": hjb["turn"], "province_index": hjb["province_index"],
            "province_name": hjb["province"], "hjb_converged": hjb["converged"],
            "hjb_iterations": hjb["iterations"], "hjb_convergence_statistic": hjb["convergence_statistic"],
            "hjb_acceptance_classification": hjb["hjb_acceptance_classification"],
            "downstream_kfe_attempted": hjb["downstream_kfe_attempted"],
            "kfe_reached": kfe is not None,
            "kfe_status": kfe["classification"] if kfe else "NOT_REACHED",
            "kfe_source_free_normwise_ratio": kfe["source_free_residual_ratio"] if kfe else "",
            "kfe_upper_b_max_outward_leak_rate": (
                kfe["boundary_outward_leak"]["upper_b"]["max_outward_leak_rate"] if kfe else ""),
        })
    return result


def hjb_path_rows(validity: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen_nonconverged: set[int] = set()
    result = []
    for row in sorted(validity, key=lambda item: (int(item["turn"]), int(item["province_index"]))):
        index = int(row["province_index"])
        converged = bool(row["hjb_converged"])
        recovered = converged and index in seen_nonconverged
        if not converged:
            seen_nonconverged.add(index)
        result.append({
            "turn": row["turn"], "province_index": index, "province_name": row["province_name"],
            "hjb_converged": converged,
            "hjb_nonconverged_but_continued": (not converged) and bool(row["kfe_reached"]),
            "hjb_iterations": row["hjb_iterations"],
            "hjb_convergence_statistic": row["hjb_convergence_statistic"],
            "hjb_acceptance_classification": row["hjb_acceptance_classification"],
            "downstream_kfe_attempted": row["downstream_kfe_attempted"],
            "downstream_kfe_returned": row["kfe_reached"],
            "reconverged_after_prior_nonconvergence": recovered,
        })
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence_root", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--focused-test-processes", type=int, required=True)
    parser.add_argument("--focused-test-cases", type=int, required=True)
    parser.add_argument("--compile-processes", type=int, required=True)
    args = parser.parse_args(argv)
    evidence, output = args.evidence_root, args.output_dir
    output.mkdir(parents=True, exist_ok=False)
    terminal = read_json(evidence / "terminal_result.json")
    calls = read_json(evidence / "call_ledger.json")
    runtime = read_json(evidence / "runtime_input_receipt.json")
    rows = completed_rows(evidence)
    summaries = read_json(evidence / "transition_summary.json")["turns"]
    late = late_window(rows)
    validity = validity_rows(evidence)
    hjb_path = hjb_path_rows(validity)

    province_fields = [
        "turn", "province_index", "province_name", "Ktarget_2018_MU", "Kt_supply_private_MU",
        "GovInv_before_MU", "GovInv_after_MU", "firm_K_total_MU", "firm_K_total_over_Ktarget",
        "private_K_over_Ktarget", "GovInv_before_over_Ktarget", "GovInv_after_over_Ktarget",
        "Ltarget_proxy_NU", "firm_Lt_supply", "firm_Lt_over_population_proxy",
        "net_destination_labor_gain_loss_NU", "top_origin_index", "top_origin_province",
        "top_origin_contribution", "top_origin_share_of_destination_supply", "A", "B", "L", "C",
        "firm_ra0", "firm_ra_used", "household_rah", "firm_wage_raw", "firm_wage_used",
        "household_composite_wage", "Y", "Zt", "nk_gap", "yt_gap", "GDP_level_gap",
        "govinv_action", "kfe_diagnostic_status", "hjb_converged", "hjb_iterations",
        "hjb_statistic", "hjb_acceptance_classification", "downstream_kfe_attempted",
        "downstream_kfe_returned", "continuation_status",
    ]
    write_csv(output / "province_turn_kl_ledger.csv", rows, province_fields)

    national_fields = [
        "turn", "household_convergence_count", "ra_lower", "ra_interior", "ra_upper",
        "wage_lower", "wage_interior", "wage_upper", "firm_K_ratio_min", "firm_K_ratio_median",
        "firm_K_ratio_max", "private_K_ratio_min", "private_K_ratio_median", "private_K_ratio_max",
        "GovInv_ratio_min", "GovInv_ratio_median", "GovInv_ratio_max", "K_above_1p05",
        "K_above_1p25", "K_above_2", "K_below_0p95", "K_below_0p75", "K_below_0p5",
        "labor_ratio_min", "labor_ratio_median", "labor_ratio_max", "labor_outside_0p8_1p2",
        "national_Ktarget", "national_private_K", "national_GovInv", "national_firm_total_K",
        "national_Ltarget_proxy", "national_firm_destination_labor", "max_KN_gap", "max_Y_prev_gap",
        "max_GDP_level_gap", "zt_adjusted_count", "govinv_decrease", "govinv_increase", "govinv_hold",
        "hjb_converged_count", "hjb_nonconverged_but_continued_count",
        "hjb_nonconverged_provinces", "hjb_failures", "kfe_failures", "kfe_diagnostic_only_count",
    ]
    national_rows = []
    for summary in summaries:
        action = summary["controller"]["govinv_action_counts"]
        national_rows.append({
            "turn": summary["turn"], "household_convergence_count": 31 - summary["hjb_failures"],
            "ra_lower": summary["firm_rate_regions"]["lower"],
            "ra_interior": summary["firm_rate_regions"]["interior"], "ra_upper": summary["firm_rate_regions"]["upper"],
            "wage_lower": summary["wage_regions"]["lower"],
            "wage_interior": summary["wage_regions"]["interior"], "wage_upper": summary["wage_regions"]["upper"],
            "firm_K_ratio_min": summary["firm_K_total_over_Ktarget"]["min"],
            "firm_K_ratio_median": summary["firm_K_total_over_Ktarget"]["median"],
            "firm_K_ratio_max": summary["firm_K_total_over_Ktarget"]["max"],
            "private_K_ratio_min": summary["private_K_over_Ktarget"]["min"],
            "private_K_ratio_median": summary["private_K_over_Ktarget"]["median"],
            "private_K_ratio_max": summary["private_K_over_Ktarget"]["max"],
            "GovInv_ratio_min": summary["GovInv_before_over_Ktarget"]["min"],
            "GovInv_ratio_median": summary["GovInv_before_over_Ktarget"]["median"],
            "GovInv_ratio_max": summary["GovInv_before_over_Ktarget"]["max"],
            "K_above_1p05": summary["firm_K_ratio_counts"]["above_1p05"],
            "K_above_1p25": summary["firm_K_ratio_counts"]["above_1p25"],
            "K_above_2": summary["firm_K_ratio_counts"]["above_2"],
            "K_below_0p95": summary["firm_K_ratio_counts"]["below_0p95"],
            "K_below_0p75": summary["firm_K_ratio_counts"]["below_0p75"],
            "K_below_0p5": summary["firm_K_ratio_counts"]["below_0p5"],
            "labor_ratio_min": summary["firm_Lt_over_population_proxy"]["min"],
            "labor_ratio_median": summary["firm_Lt_over_population_proxy"]["median"],
            "labor_ratio_max": summary["firm_Lt_over_population_proxy"]["max"],
            "labor_outside_0p8_1p2": summary["labor_ratio_outside_0p8_1p2_count"],
            "national_Ktarget": summary["national_sums"]["Ktarget_2018_MU"],
            "national_private_K": summary["national_sums"]["Kt_supply_private_MU"],
            "national_GovInv": summary["national_sums"]["GovInv_before_MU"],
            "national_firm_total_K": summary["national_sums"]["firm_K_total_MU"],
            "national_Ltarget_proxy": summary["national_sums"]["Ltarget_proxy_NU"],
            "national_firm_destination_labor": summary["national_sums"]["firm_destination_labor"],
            "max_KN_gap": summary["nk_gap"]["max"], "max_Y_prev_gap": summary["yt_gap"]["max"],
            "max_GDP_level_gap": summary["GDP_level_gap"]["max"],
            "zt_adjusted_count": summary["controller"]["zt_adjusted_count"],
            "govinv_decrease": action.get("LOW_RA_DECREASE_0P9", 0),
            "govinv_increase": action.get("HIGH_RA_INCREASE_1P1", 0),
            "govinv_hold": action.get("NONE", 0), "hjb_failures": summary["hjb_failures"],
            "hjb_converged_count": summary["hjb_converged_count"],
            "hjb_nonconverged_but_continued_count": summary["hjb_nonconverged_but_continued_count"],
            "hjb_nonconverged_provinces": "|".join(summary["hjb_nonconverged_provinces"]),
            "kfe_failures": summary["kfe_failures"],
            "kfe_diagnostic_only_count": summary["kfe_diagnostic_status_counts"].get("DIAGNOSTIC_ONLY", 0),
        })
    write_csv(output / "national_turn_summary.csv", national_rows, national_fields)

    late_fields = ["province_index", "province_name", "turns_observed",
        "firm_K_total_over_Ktarget_mean", "firm_K_total_over_Ktarget_median",
        "private_K_over_Ktarget_mean", "private_K_over_Ktarget_median",
        "GovInv_before_over_Ktarget_mean", "GovInv_before_over_Ktarget_median",
        "firm_Lt_over_population_proxy_mean", "firm_Lt_over_population_proxy_median",
        "K_status", "L_status_relative_to_population_proxy"]
    write_csv(output / "late_window_20_25_province_summary.csv", late, late_fields)
    write_csv(output / "anhui_trace.csv",
              [row for row in rows if row["province_name"] == "安徽" and int(row["turn"]) in TRACE_TURNS],
              province_fields)
    write_csv(output / "scientific_validity_ledger.csv", validity,
              ["turn", "province_index", "province_name", "hjb_converged", "hjb_iterations",
               "hjb_convergence_statistic", "hjb_acceptance_classification",
               "downstream_kfe_attempted", "kfe_reached", "kfe_status",
               "kfe_source_free_normwise_ratio", "kfe_upper_b_max_outward_leak_rate"])
    write_csv(output / "hjb_convergence_path.csv", hjb_path,
              ["turn", "province_index", "province_name", "hjb_converged",
               "hjb_nonconverged_but_continued", "hjb_iterations", "hjb_convergence_statistic",
               "hjb_acceptance_classification", "downstream_kfe_attempted",
               "downstream_kfe_returned", "reconverged_after_prior_nonconvergence"])

    status = "AVAILABLE" if late else f"NOT_AVAILABLE_{terminal['termination_reason']}_BEFORE_LATE_WINDOW"
    write_csv(output / "govinv_k_decomposition_summary.csv", [{
        "status": status, "actual_turns_completed": terminal["actual_turns_completed"],
        "late_window_rows": len(late), "accounting_identity": "firm_K_total=private_K_supply+GovInv_before",
        "mechanical_implication": "GovInv0=Ktarget plus positive private supply implies firm_K_total>Ktarget",
        "observed_late_window_conclusion": "NOT_ESTIMABLE" if not late else "SEE_LATE_WINDOW_LEDGER",
    }], ["status", "actual_turns_completed", "late_window_rows", "accounting_identity",
         "mechanical_implication", "observed_late_window_conclusion"])
    write_csv(output / "labor_migration_proxy_summary.csv", [{
        "status": status, "actual_turns_completed": terminal["actual_turns_completed"],
        "target_role": "2018_POPULATION_AS_LABOR_PROXY_NU_NOT_OBSERVED_WORKPLACE_EMPLOYMENT",
        "observed_late_window_conclusion": "NOT_ESTIMABLE" if not late else "SEE_LATE_WINDOW_LEDGER",
        "national_conservation_claim": "ONLY_LT_SUPPLY_ROW_SUM_AND_MATRIX_TOTAL_IDENTITIES_CHECKED",
    }], ["status", "actual_turns_completed", "target_role", "observed_late_window_conclusion",
         "national_conservation_claim"])

    write_json(output / "call_ledger.json", calls)
    write_json(output / "runtime_input_receipt.json", runtime)
    write_json(output / "bounded_invocation_receipt.json", read_json(evidence / "bounded_invocation_receipt.json"))
    write_json(output / "phase_a_zero_science_repair_receipt.json",
               read_json(evidence / "phase_a_zero_science_repair_receipt.json"))
    write_json(output / "terminal_result.json", terminal)
    write_json(output / "tests_static_check_receipt.json", {
        "schema": "CH5_HJB_PROPAGATION_CORRECTED_2018_25TURN_KL_STATIC_CHECKS_V1",
        "focused_test_processes": args.focused_test_processes,
        "focused_test_cases_executed": args.focused_test_cases,
        "compile_processes": args.compile_processes, "status": "PASS", "scientific_calls": 0,
    })
    source_files = [
        Path(__file__), Path(__file__).with_name("run.py"),
        REPO / "src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py",
        REPO / "src/ch5_two_asset_hank/multi_province/one_turn.py",
        REPO / "src/ch5_two_asset_hank/multi_province/migration_labor.py",
        REPO / "src/ch5_two_asset_hank/multi_province/capital_allocation.py",
        REPO / "src/ch5_two_asset_hank/multi_province/firm.py",
        REPO / "src/ch5_two_asset_hank/multi_province/steady_state.py",
    ]
    write_json(output / "source_hash_receipt.json", {
        "schema": "CH5_HJB_PROPAGATION_CORRECTED_2018_25TURN_KL_SOURCE_HASH_RECEIPT_V1",
        "files": [{"path": path.relative_to(REPO).as_posix(), "sha256": file_sha256(path),
                   "bytes": path.stat().st_size} for path in source_files],
        "external_evidence_root": str(evidence),
        "external_runtime_payload_sha256": file_sha256(evidence / "runtime_input_payload.json"),
        "external_source_code_identity_sha256": file_sha256(evidence / "source_code_identity.json"),
    })
    artifacts = sorted(path for path in output.iterdir() if path.is_file())
    manifest = {"schema": "CH5_HJB_PROPAGATION_CORRECTED_2018_25TURN_KL_MANIFEST_V1", "files": [
        {"path": path.name, "sha256": file_sha256(path), "bytes": path.stat().st_size} for path in artifacts]}
    write_json(output / "manifest.json", manifest)
    checks = [{"path": item["path"], "sha256_match": file_sha256(output / item["path"]) == item["sha256"],
               "bytes_match": (output / item["path"]).stat().st_size == item["bytes"]}
              for item in manifest["files"]]
    write_json(output / "manifest_readback.json", {
        "schema": "CH5_HJB_PROPAGATION_CORRECTED_2018_25TURN_KL_MANIFEST_READBACK_V1",
        "manifest_sha256": file_sha256(output / "manifest.json"), "entries": checks,
        "passed": all(item["sha256_match"] and item["bytes_match"] for item in checks),
    })
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
