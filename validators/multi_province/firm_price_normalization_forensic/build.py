from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import shutil
from pathlib import Path
from statistics import median


VERDICT = "FIRM_PRICE_NORMALIZATION_FORENSIC_PASS__WAGE_UNIT_MISMATCH_AND_RETURN_LEVEL_EFFECTS_SEPARATED"
ALPHA = 0.7380939146868483
MT = 0.92
DELTA_FIRM = 0.025
CORPTAU = 0.25
THETA = 100.0
PIT = 0.02
RA_UPPER = 0.09
WAGE_UPPER = 1.3
SOURCE_HASHES = {
    "HANK_firm.m": "EE02C15414ADF9F99AADE04F1F22E64FA7094C8AB77753B6130BC4BFA6CE7BD5",
    "HANK_mp_1turn.m": "D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF",
    "wage_caculate.m": "0FB84B51E2BE50CD3D065D33385882311A31E12596AEEB0CE2C808A8C36B6A63",
    "HANK_2ASSETS_HJB.m": "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE",
    "multi_prov_HANK_12sts.m": "3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97",
    "mpHANK_equilibrium_2000.m": "26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5",
    "load_GDPdata.m": "DECA8AF3F22097550B8957FE848989E6342619CB9929A1C00076E020549366C5",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def extrema(rows: list[dict], field: str) -> dict:
    low = min(rows, key=lambda row: row[field])
    high = max(rows, key=lambda row: row[field])
    values = [row[field] for row in rows]
    return {
        "min": min(values), "min_province": low["province_name"],
        "median": median(values),
        "max": max(values), "max_province": high["province_name"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--protected-root", type=Path, required=True)
    parser.add_argument("--evidence-root", type=Path, required=True)
    parser.add_argument("--session-build-processes", type=int, default=1)
    parser.add_argument("--session-focused-test-processes", type=int, default=1)
    parser.add_argument("--session-compile-processes", type=int, default=1)
    parser.add_argument("--session-finalize-processes", type=int, default=1)
    args = parser.parse_args()
    repo = args.repo_root.resolve()
    protected = args.protected_root.resolve()
    evidence = args.evidence_root.resolve()
    if evidence.exists() and any(evidence.iterdir()):
        raise FileExistsError(f"refusing to overwrite non-empty evidence root: {evidence}")
    evidence.mkdir(parents=True, exist_ok=True)

    protected_receipt = []
    for name, expected in SOURCE_HASHES.items():
        path = protected / name
        actual = sha256(path)
        if actual != expected:
            raise ValueError(f"protected source mismatch: {name}: {actual}")
        protected_receipt.append({"file": name, "path": str(path), "sha256": actual, "match": True})

    accepted_dir = repo / "reports/mp4c_unit_normalized_initialization_probe_20260910"
    input_path = accepted_dir / "province_initialization_receipt.csv"
    bridge_path = accepted_dir / "asset_bridge_scale_diagnostic.csv"
    with input_path.open("r", encoding="utf-8-sig", newline="") as handle:
        source_rows = list(csv.DictReader(handle))
    with bridge_path.open("r", encoding="utf-8-sig", newline="") as handle:
        bridge_rows = list(csv.DictReader(handle))
    if len(source_rows) != 31 or len(bridge_rows) != 31:
        raise ValueError("accepted baseline is not a complete 31-province receipt")
    if [row["province_name"] for row in source_rows] != [row["province_name"] for row in bridge_rows]:
        raise ValueError("accepted receipt and bridge province orders differ")

    rows = []
    for src in source_rows:
        y = float(src["Y0_MU"]); k = float(src["K0_MU"]); labor = float(src["L0"])
        y_l = y / labor; y_k = y / k
        wage = MT * (1.0 - ALPHA) * y_l
        mpk = MT * ALPHA * y_k
        theta_cost = THETA / 2.0 * PIT**2 * y
        gross_profit_before_adjustment = (1.0 - MT) * y
        profit = max(gross_profit_before_adjustment - theta_cost, 0.0)
        corporate_tax = profit * CORPTAU
        dividend = profit * (1.0 - CORPTAU) / k
        other = 0.0
        raw_ra = mpk - DELTA_FIRM + dividend + other
        accepted_wage = float(src["raw_wjt0"]); accepted_ra = float(src["raw_ra0"])
        if not math.isclose(wage, accepted_wage, rel_tol=1e-14, abs_tol=1e-14):
            raise ValueError(f"wage identity mismatch for {src['province_name']}")
        if not math.isclose(raw_ra, accepted_ra, rel_tol=1e-14, abs_tol=1e-14):
            raise ValueError(f"return decomposition mismatch for {src['province_name']}")
        rows.append({
            "province_index": int(src["province_index"]), "province_name": src["province_name"],
            "Y0_MU": y, "L0_NU": labor, "K0_MU": k,
            "Y_over_L_MU_per_NU": y_l, "mt": MT, "labor_share_1_minus_alpha": 1.0 - ALPHA,
            "wage_raw_identity": wage, "wage_raw_accepted": accepted_wage,
            "wage_identity_abs_error": abs(wage - accepted_wage),
            "wage_used": float(src["used_wjt0"]), "wage_raw_to_1p3": wage / WAGE_UPPER,
            "wage_bound_status": src["wage_bound_status"],
            "Y_over_K": y_k, "mpk_component_mt_alpha_Y_over_K": mpk,
            "firm_depreciation_component": -DELTA_FIRM,
            "gross_profit_before_adjustment_MU": gross_profit_before_adjustment,
            "price_adjustment_cost_Thetat_MU": theta_cost,
            "profit_floor_applied": gross_profit_before_adjustment - theta_cost < 0,
            "PIt_after_floor_MU": profit, "Corptax_before_clipping_MU": corporate_tax,
            "profit_dividend_after_tax_component": dividend,
            "other_additive_return_component": other,
            "ra_raw_component_sum": raw_ra, "ra_raw_accepted": accepted_ra,
            "ra_identity_abs_error": abs(raw_ra - accepted_ra),
            "ra_used": float(src["used_ra0"]), "ra_raw_to_0p09": raw_ra / RA_UPPER,
            "ra_bound_status": src["ra_bound_status"],
            "wage_classification": "PRICE_BOUND_HITS_PRIMARILY_UNIT_NORMALIZATION_MISMATCH",
            "return_classification": "PRICE_BOUND_HITS_PRIMARILY_ECONOMIC_RATIO_LEVELS",
        })

    out = repo / "reports/mp4c_firm_price_normalization_forensic_20260910"
    out.mkdir(parents=True, exist_ok=True)
    csv_path = out / "province_price_component_decomposition.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)

    bridge_ratios = [float(row["AtN_to_K0"]) for row in bridge_rows]
    bridge_low = min(bridge_rows, key=lambda row: float(row["AtN_to_K0"]))
    bridge_high = max(bridge_rows, key=lambda row: float(row["AtN_to_K0"]))
    coefficient = MT * ALPHA + (1.0 - CORPTAU) * ((1.0 - MT) - THETA / 2.0 * PIT**2)
    summary = {
        "schema": "CH5_FIRM_PRICE_NORMALIZATION_FORENSIC_SUMMARY_V1",
        "verdict": VERDICT,
        "wage_conclusion": "PRICE_BOUND_HITS_PRIMARILY_UNIT_NORMALIZATION_MISMATCH",
        "return_conclusion": "PRICE_BOUND_HITS_PRIMARILY_ECONOMIC_RATIO_LEVELS",
        "household_currency_conclusion": "HOUSEHOLD_CURRENCY_NORMALIZATION_UNRESOLVED",
        "wage": {
            "identity": "w_raw=mt*(1-alpha)*Y/L",
            "Y_over_L": extrema(rows, "Y_over_L_MU_per_NU"),
            "raw": extrema(rows, "wage_raw_identity"),
            "raw_to_upper_bound": extrema(rows, "wage_raw_to_1p3"),
            "bound_counts": {key: sum(row["wage_bound_status"] == key for row in rows) for key in ("below", "inside", "above")},
        },
        "return": {
            "identity": "ra_raw=mt*alpha*Y/K-delta_firm+PIt*(1-corptau)/K",
            "collapsed_identity": f"ra_raw={coefficient}*Y/K-{DELTA_FIRM}",
            "Y_over_K": extrema(rows, "Y_over_K"),
            "mpk_component": extrema(rows, "mpk_component_mt_alpha_Y_over_K"),
            "depreciation_component": extrema(rows, "firm_depreciation_component"),
            "dividend_component": extrema(rows, "profit_dividend_after_tax_component"),
            "other_additive_component": extrema(rows, "other_additive_return_component"),
            "raw": extrema(rows, "ra_raw_component_sum"),
            "raw_to_upper_bound": extrema(rows, "ra_raw_to_0p09"),
            "bound_counts": {key: sum(row["ra_bound_status"] == key for row in rows) for key in ("below", "inside", "above")},
            "Y_over_K_coefficient": coefficient,
            "mpk_share_of_positive_Y_over_K_coefficient": MT * ALPHA / coefficient,
            "dividend_share_of_positive_Y_over_K_coefficient": (coefficient - MT * ALPHA) / coefficient,
            "K_over_Y_threshold_for_ra_0p09": coefficient / (RA_UPPER + DELTA_FIRM),
        },
        "asset_bridge_beta_a_1_descriptive": {
            "status": "SOURCE_FAITHFUL_BASELINE_ONLY__BETA_A_NOT_IDENTIFIED",
            "AtN_to_K0_min": min(bridge_ratios), "min_province": bridge_low["province_name"],
            "AtN_to_K0_median": median(bridge_ratios),
            "AtN_to_K0_max": max(bridge_ratios), "max_province": bridge_high["province_name"],
        },
        "results_eligible": False,
    }
    write_json(out / "national_forensic_summary.json", summary)
    source_receipt = {
        "schema": "CH5_FIRM_PRICE_NORMALIZATION_FORENSIC_SOURCE_RECEIPT_V1",
        "base_main": "d9faf96d75db5a561b562700a10f075ff36eddff",
        "accepted_probe": {
            "candidate": "ff2a32e6c6eb799931b741c9a8557afdaa5c8bfa",
            "province_receipt": {"path": str(input_path), "sha256": sha256(input_path), "rows": 31},
            "asset_bridge_receipt": {"path": str(bridge_path), "sha256": sha256(bridge_path), "rows": 31},
            "manifest_readback": {"path": str(accepted_dir / "manifest_readback.json"), "sha256": sha256(accepted_dir / "manifest_readback.json")},
        },
        "protected_sources": protected_receipt,
        "graph_discovery": "FILE_LEVEL_ONLY__EXACT_PATH_STATIC_READ_FALLBACK_USED",
    }
    write_json(out / "source_hash_receipt.json", source_receipt)
    zero_calls = {
        "schema": "CH5_FIRM_PRICE_NORMALIZATION_FORENSIC_ZERO_CALL_LEDGER_V1",
        "accounting_scope": "CUMULATIVE_CURRENT_TASK_SESSION_INCLUDING_PRESERVED_PRELIMINARY_EVIDENCE_RUNS",
        "deterministic_builder_processes": args.session_build_processes,
        "province_formula_decomposition_rows": 31 * args.session_build_processes,
        "pre_builder_static_readback_analysis_processes": 2,
        "codebase_graph_read_calls": 2,
        "focused_test_processes": args.session_focused_test_processes,
        "focused_test_cases_executed": 5 * args.session_focused_test_processes,
        "python_compile_processes": args.session_compile_processes,
        "evidence_finalize_processes": args.session_finalize_processes,
        "preserved_preliminary_evidence_roots": [
            "D:/ProjectTemp/ch5-firm-price-normalization-forensic-20260910-001"
        ] if args.session_build_processes > 1 else [],
        "matlab_model_calls": 0, "python_household_hjb_kfe_control": 0,
        "HANK_firm_runtime_calls": 0, "Lt_seperate_calls": 0,
        "capital_allocation_runtime_calls": 0, "outer_turns": 0, "steady_state": 0,
        "ge": 0, "annual": 0, "irf": 0, "results": 0,
        "root_direct_iterative_eigen_solves": 0, "parameter_tuning": 0,
    }
    write_json(out / "zero_scientific_call_ledger.json", zero_calls)
    write_json(evidence / "run_receipt.json", {"verdict": VERDICT, "summary": summary, "zero_scientific_call_ledger": zero_calls})
    shutil.copy2(csv_path, evidence / csv_path.name)
    shutil.copy2(out / "national_forensic_summary.json", evidence / "national_forensic_summary.json")
    print(json.dumps({"verdict": VERDICT, "evidence_root": str(evidence), "rows": 31}, ensure_ascii=False))


if __name__ == "__main__":
    main()
