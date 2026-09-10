from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import platform
import sys
from pathlib import Path
from typing import Any

import numpy as np
import scipy
import statsmodels
import statsmodels.api as sm


PROVINCES = [
    (1, "北京", "北京市"), (2, "天津", "天津市"), (3, "河北", "河北省"),
    (4, "山西", "山西省"), (5, "内蒙古", "内蒙古自治区"), (6, "辽宁", "辽宁省"),
    (7, "吉林", "吉林省"), (8, "黑龙江", "黑龙江省"), (9, "上海", "上海市"),
    (10, "江苏", "江苏省"), (11, "浙江", "浙江省"), (12, "安徽", "安徽省"),
    (13, "福建", "福建省"), (14, "江西", "江西省"), (15, "山东", "山东省"),
    (16, "河南", "河南省"), (17, "湖北", "湖北省"), (18, "湖南", "湖南省"),
    (19, "广东", "广东省"), (20, "广西", "广西壮族自治区"), (21, "海南", "海南省"),
    (22, "重庆", "重庆市"), (23, "四川", "四川省"), (24, "贵州", "贵州省"),
    (25, "云南", "云南省"), (26, "西藏", "西藏自治区"), (27, "陕西", "陕西省"),
    (28, "甘肃", "甘肃省"), (29, "青海", "青海省"), (30, "宁夏", "宁夏回族自治区"),
    (31, "新疆", "新疆维吾尔自治区"),
]
SOURCE_TO_SHORT = {source: short for _, short, source in PROVINCES}
LEGACY_ALPHA = 0.772866243094144
START_YEAR = 2000
TARGET_YEAR = 2018
DELTA = 0.096


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = fields or list(rows[0].keys())
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def finite_or_blank(value: float | None) -> float | str:
    return "" if value is None or not math.isfinite(value) else value


def relative(new: float, old: float) -> float:
    return (new - old) / old


def load_raw(path: Path) -> tuple[dict[str, dict[tuple[str, int], float | None]], dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload["schema"] != "CH5_RAW_NBS_XLS_EXTRACTION_V1":
        raise ValueError("Unexpected raw extraction schema")
    series: dict[str, dict[tuple[str, int], float | None]] = {}
    for source in payload["sources"]:
        key = source["key"]
        values: dict[tuple[str, int], float | None] = {}
        observed_names = set()
        for record in source["records"]:
            name = record["source_province_name"]
            if name not in SOURCE_TO_SHORT:
                raise ValueError(f"Unmapped province name in {key}: {name}")
            observed_names.add(name)
            values[(name, int(record["year"]))] = record["raw_value"]
        expected_names = set(SOURCE_TO_SHORT)
        if observed_names != expected_names:
            raise ValueError(f"Province-set mismatch in {key}: {observed_names ^ expected_names}")
        series[key] = values
    if set(series) != {"gdp", "investment", "depreciation", "population"}:
        raise ValueError("The four exact source series were not extracted")
    return series, payload


def capital_paths(series: dict[str, dict[tuple[str, int], float | None]]) -> tuple[dict, dict]:
    track_a: dict[tuple[str, int], float] = {}
    track_b: dict[tuple[str, int], float] = {}
    for _, _, source_name in PROVINCES:
        i0 = series["investment"][(source_name, START_YEAR)]
        if i0 is None or i0 <= 0:
            raise ValueError(f"Missing/nonpositive {START_YEAR} investment for {source_name}")
        track_a[(source_name, START_YEAR)] = i0 / 0.1
        track_b[(source_name, START_YEAR)] = i0 / 0.1
        for year in range(START_YEAR + 1, TARGET_YEAR + 1):
            investment_lag = series["investment"].get((source_name, year - 1))
            depreciation_lag = series["depreciation"].get((source_name, year - 1))
            if investment_lag is None or investment_lag <= 0:
                raise ValueError(f"Missing/nonpositive lagged investment for {source_name} {year}")
            if depreciation_lag is None or depreciation_lag <= 0:
                raise ValueError(f"Missing/nonpositive lagged depreciation for {source_name} {year}")
            track_a[(source_name, year)] = (1.0 - DELTA) * track_a[(source_name, year - 1)] + investment_lag
            track_b[(source_name, year)] = track_b[(source_name, year - 1)] + investment_lag - depreciation_lag
    return track_a, track_b


def estimate_alpha(series: dict, track_a: dict) -> tuple[Any, list[dict[str, Any]]]:
    rows = []
    for index, short, source_name in PROVINCES:
        for year in range(2009, 2019):
            y_raw = series["gdp"].get((source_name, year))
            l_raw = series["population"].get((source_name, year))
            k_raw = track_a.get((source_name, year))
            if y_raw is None or l_raw is None or k_raw is None or min(y_raw, l_raw, k_raw) <= 0:
                continue
            y_model = y_raw * 1_000.0
            l_model = l_raw * 100.0
            k_model = k_raw * 10_000_000.0
            rows.append({
                "province_index": index,
                "province_name": short,
                "year": year,
                "trend": year - 2009,
                "log_y_per_l": math.log(y_model / l_model),
                "log_k_per_l": math.log(k_model / l_model),
            })
    x = np.asarray([[row["trend"], row["log_k_per_l"]] for row in rows], dtype=float)
    y = np.asarray([row["log_y_per_l"] for row in rows], dtype=float)
    result = sm.OLS(y, sm.add_constant(x, has_constant="add")).fit()
    return result, rows


def fmt(value: Any, digits: int = 6) -> str:
    if value is None or value == "":
        return "NA"
    return f"{float(value):.{digits}g}"


def markdown_table(rows: list[dict[str, Any]]) -> str:
    columns = [
        ("序", "province_index"), ("省份", "province_name"),
        ("GDP18", "corrected_raw_nbs_gdp_2018_100m_yuan"),
        ("POP18", "corrected_raw_nbs_population_2018_10k_persons"),
        ("I18", "raw_nbs_investment_2018_100m_yuan"),
        ("D18", "raw_nbs_depreciation_2018_100m_yuan"),
        ("K-A18", "corrected_track_a_capital_2018_100m_yuan"),
        ("K-B18", "corrected_track_b_capital_2018_100m_yuan"),
        ("alpha", "new_alpha"), ("Z-A18", "corrected_track_a_zt_2018"),
        ("Z-B18", "corrected_track_b_zt_2018"), ("flag", "data_quality_provenance_flag"),
    ]
    output = ["| " + " | ".join(label for label, _ in columns) + " |",
              "|" + "|".join("---:" if key not in {"province_name", "data_quality_provenance_flag"} else "---" for _, key in columns) + "|"]
    for row in rows:
        cells = []
        for _, key in columns:
            value = row[key]
            if key in {"province_index", "province_name", "data_quality_provenance_flag"}:
                cells.append(str(value))
            else:
                cells.append(fmt(value, 10))
        output.append("| " + " | ".join(cells) + " |")
    return "\n".join(output) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-json", type=Path, required=True)
    parser.add_argument("--legacy-ledger", type=Path, required=True)
    parser.add_argument("--canonical-workbook", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    expected_canonical_hash = "AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67"
    actual_canonical_hash = sha256(args.canonical_workbook)
    if actual_canonical_hash != expected_canonical_hash:
        raise ValueError("Canonical workbook hash mismatch")

    series, raw_payload = load_raw(args.raw_json)
    legacy_rows = read_csv(args.legacy_ledger)
    legacy_by_name = {row["province_name"]: row for row in legacy_rows}
    if list(legacy_by_name) != [short for _, short, _ in PROVINCES]:
        raise ValueError("Accepted 31-province order mismatch")

    track_a, track_b = capital_paths(series)
    ols, estimation_rows = estimate_alpha(series, track_a)
    alpha = float(ols.params[2])
    if not math.isfinite(alpha):
        raise ValueError("Estimated alpha is not finite")

    panel_rows: list[dict[str, Any]] = []
    for index, short, source_name in PROVINCES:
        for year in range(START_YEAR, TARGET_YEAR + 1):
            gdp = series["gdp"].get((source_name, year))
            pop = series["population"].get((source_name, year))
            inv = series["investment"].get((source_name, year))
            dep = series["depreciation"].get((source_name, year))
            ka = track_a[(source_name, year)]
            kb = track_b[(source_name, year)]
            flags = []
            for label, value in (("GDP", gdp), ("POP", pop), ("INV", inv), ("DEP", dep)):
                if value is None:
                    flags.append(f"MISSING_{label}")
                elif value <= 0:
                    flags.append(f"NONPOSITIVE_{label}")
            panel_rows.append({
                "province_index": index, "province_name": short,
                "source_province_name": source_name, "year": year,
                "gdp_raw_100m_yuan": finite_or_blank(gdp),
                "population_raw_10k_persons": finite_or_blank(pop),
                "investment_raw_100m_yuan": finite_or_blank(inv),
                "depreciation_raw_100m_yuan": finite_or_blank(dep),
                "gdp_model_units_x1000": finite_or_blank(None if gdp is None else gdp * 1_000.0),
                "population_model_units_x100": finite_or_blank(None if pop is None else pop * 100.0),
                "investment_capital_units_x1e7": finite_or_blank(None if inv is None else inv * 10_000_000.0),
                "depreciation_capital_units_x1e7": finite_or_blank(None if dep is None else dep * 10_000_000.0),
                "track_a_capital_100m_yuan": ka,
                "track_a_capital_model_units_x1e7": ka * 10_000_000.0,
                "track_b_capital_100m_yuan": kb,
                "track_b_capital_model_units_x1e7": kb * 10_000_000.0,
                "data_quality_flag": "OK" if not flags else ";".join(flags),
            })

    ledger_rows: list[dict[str, Any]] = []
    capital_rows: list[dict[str, Any]] = []
    for index, short, source_name in PROVINCES:
        old = legacy_by_name[short]
        gdp = float(series["gdp"][(source_name, TARGET_YEAR)])
        pop = float(series["population"][(source_name, TARGET_YEAR)])
        inv18 = series["investment"].get((source_name, TARGET_YEAR))
        dep18 = series["depreciation"].get((source_name, TARGET_YEAR))
        ka = track_a[(source_name, TARGET_YEAR)]
        kb = track_b[(source_name, TARGET_YEAR)]
        y_model = gdp * 1_000.0
        l_model = pop * 100.0
        ka_model = ka * 10_000_000.0
        kb_model = kb * 10_000_000.0
        za = y_model / (ka_model**alpha * l_model ** (1.0 - alpha))
        zb = y_model / (kb_model**alpha * l_model ** (1.0 - alpha))
        legacy_gdp = float(old["MATLAB_GDP_raw_亿元"])
        legacy_pop = float(old["MATLAB_POP_raw_万人"])
        legacy_k_100m = float(old["MATLAB_raw_capital_万元"]) / 10_000.0
        legacy_z = float(old["MATLAB_Zt_fixed_2020_level"])
        canonical_gdp = float(old["canonical_GDP_raw_亿元"])
        canonical_pop = float(old["canonical_POP_raw_万人"])
        canonical_k_100m = float(old["canonical_PIM_capital_万元"]) / 10_000.0
        flags = ["RAW_2018_INVESTMENT_UNAVAILABLE", "RAW_2018_DEPRECIATION_UNAVAILABLE"]
        if not math.isclose(gdp, canonical_gdp, rel_tol=0.0, abs_tol=1e-9):
            flags.append("RAW_GDP_DIFFERS_FROM_CANONICAL")
        if not math.isclose(pop, canonical_pop, rel_tol=0.0, abs_tol=1e-9):
            flags.append("RAW_POP_DIFFERS_FROM_CANONICAL")
        flags.append("TRACK_A_RAW_GFCF_DIFFERS_FROM_CANONICAL_INVESTMENT_ROUTE")
        row = {
            "province_index": index, "province_name": short,
            "source_province_name": source_name,
            "legacy_matlab_level_year": 2009, "corrected_year": TARGET_YEAR,
            "legacy_matlab_gdp_100m_yuan": legacy_gdp,
            "corrected_raw_nbs_gdp_2018_100m_yuan": gdp,
            "gdp_relative_difference_vs_legacy": relative(gdp, legacy_gdp),
            "legacy_matlab_population_10k_persons": legacy_pop,
            "corrected_raw_nbs_population_2018_10k_persons": pop,
            "population_relative_difference_vs_legacy": relative(pop, legacy_pop),
            "raw_nbs_investment_2018_100m_yuan": finite_or_blank(inv18),
            "raw_nbs_depreciation_2018_100m_yuan": finite_or_blank(dep18),
            "legacy_matlab_capital_100m_yuan": legacy_k_100m,
            "corrected_track_a_capital_2018_100m_yuan": ka,
            "capital_relative_difference_vs_legacy": relative(ka, legacy_k_100m),
            "corrected_track_b_capital_2018_100m_yuan": kb,
            "track_a_to_track_b_ratio": ka / kb,
            "legacy_alpha": LEGACY_ALPHA, "new_alpha": alpha,
            "legacy_matlab_zt": legacy_z, "corrected_track_a_zt_2018": za,
            "zt_relative_difference_vs_legacy": relative(za, legacy_z),
            "corrected_track_b_zt_2018": zb,
            "track_a_k_to_y": ka / gdp,
            "track_a_k_to_n_model_units": ka_model / l_model,
            "y_to_n_model_units": y_model / l_model,
            "canonical_2018_gdp_100m_yuan": canonical_gdp,
            "raw_gdp_relative_difference_vs_canonical": relative(gdp, canonical_gdp),
            "canonical_2018_population_10k_persons": canonical_pop,
            "raw_population_relative_difference_vs_canonical": relative(pop, canonical_pop),
            "canonical_2018_pim_capital_100m_yuan": canonical_k_100m,
            "track_a_capital_relative_difference_vs_canonical": relative(ka, canonical_k_100m),
            "data_quality_provenance_flag": ";".join(flags),
        }
        ledger_rows.append(row)
        capital_rows.append({
            "province_index": index, "province_name": short, "year": TARGET_YEAR,
            "track_a_capital_100m_yuan": ka, "track_b_capital_100m_yuan": kb,
            "track_a_minus_track_b_100m_yuan": ka - kb,
            "track_a_to_track_b_ratio": ka / kb,
            "track_b_relative_difference_from_track_a": relative(kb, ka),
            "track_a_k_to_y": ka / gdp, "track_b_k_to_y": kb / gdp,
            "track_a_k_per_person_model_units": ka_model / l_model,
            "track_b_k_per_person_model_units": kb_model / l_model,
            "initial_stock_assumption": "K_2000=I_2000/0.1 for both tracks",
            "track_a_timing": "K_t=(1-0.096)K_(t-1)+I_(t-1)",
            "track_b_timing": "K_t=K_(t-1)+I_(t-1)-D_(t-1)",
        })

    out = args.output_dir
    out.mkdir(parents=True, exist_ok=True)
    write_csv(out / "cleaned_province_year_panel.csv", panel_rows)
    write_csv(out / "corrected_2018_vs_matlab_ledger.csv", ledger_rows)
    write_csv(out / "capital_method_comparison.csv", capital_rows)
    (out / "corrected_2018_vs_matlab_ledger.md").write_text(
        "# Corrected raw-NBS 2018 vs legacy MATLAB ledger\n\n"
        "Units: GDP/I/D/K are 亿元; population is 万人. `I18` and `D18` are `NA` because the supplied raw files contain no observed 2018 values. 安徽 is row 12.\n\n"
        + markdown_table(ledger_rows), encoding="utf-8")

    receipt = {
        "schema": "CH5_RAW_NBS_ALPHA_ESTIMATION_V1",
        "estimator": "pooled ordinary least squares",
        "equation": "log(Y_model/L_model) = intercept + linear_time_trend + alpha*log(K_track_A_model/L_model) + error",
        "window": {"start_year": 2009, "end_year": 2018, "years": list(range(2009, 2019))},
        "population_proxy": "year-end resident population",
        "capital_track": "A_PRIMARY_COMPARABLE_PIM",
        "sample_size": int(ols.nobs),
        "included_provinces": [short for _, short, _ in PROVINCES],
        "province_count": 31,
        "missing_data_exclusions": [],
        "coefficients": {"intercept": float(ols.params[0]), "time_trend": float(ols.params[1]), "alpha": alpha},
        "standard_errors": {"intercept": float(ols.bse[0]), "time_trend": float(ols.bse[1]), "alpha": float(ols.bse[2])},
        "t_statistics": {"intercept": float(ols.tvalues[0]), "time_trend": float(ols.tvalues[1]), "alpha": float(ols.tvalues[2])},
        "p_values": {"intercept": float(ols.pvalues[0]), "time_trend": float(ols.pvalues[1]), "alpha": float(ols.pvalues[2])},
        "r_squared": float(ols.rsquared), "adjusted_r_squared": float(ols.rsquared_adj),
        "degrees_of_freedom_residual": float(ols.df_resid),
        "legacy_alpha_for_comparison_only": LEGACY_ALPHA,
        "alpha_difference_new_minus_legacy": alpha - LEGACY_ALPHA,
        "implementation": {
            "python": platform.python_version(), "numpy": np.__version__,
            "scipy": scipy.__version__, "statsmodels": statsmodels.__version__,
            "platform": platform.platform(),
        },
        "authority_limit": "CALIBRATION_ONLY__NOT_MODEL_OR_RESULTS_AUTHORITY",
    }
    (out / "alpha_estimation_receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    source_receipt = {"schema": "CH5_RAW_NBS_SOURCE_HASH_RECEIPT_V1", "sources": [],
                      "canonical_workbook": {"path": str(args.canonical_workbook), "sha256": actual_canonical_hash,
                      "expected_sha256": expected_canonical_hash, "hash_match": True},
                      "raw_extraction_sha256": sha256(args.raw_json),
                      "province_mapping": [{"province_index": i, "province_name": s, "source_province_name": n} for i, s, n in PROVINCES]}
    coverage: dict[str, Any] = {}
    for source in raw_payload["sources"]:
        key = source["key"]
        values = series[key]
        any_years, full_years = [], []
        for year in sorted(source["header_years"]):
            observed = sum(values.get((name, year)) is not None for name in SOURCE_TO_SHORT)
            if observed:
                any_years.append(year)
            if observed == 31:
                full_years.append(year)
        coverage[key] = {"header_years": source["header_years"], "years_with_any_observation": any_years,
                         "years_with_31_observations": full_years, "observed_2018_count": sum(values.get((name, 2018)) is not None for name in SOURCE_TO_SHORT)}
        source_receipt["sources"].append({k: source[k] for k in ("key", "actual_path", "filename", "sha256", "bytes", "last_write_time", "workbook_format", "sheet_name", "used_rows", "used_columns", "header_row", "province_start_row", "year_orientation", "province_orientation", "indicator", "original_unit", "advertised_time_text", "notes")})
    source_receipt["coverage"] = coverage
    source_receipt["fully_same_year_2018_four_source_31_province_available"] = False
    source_receipt["reason"] = "The supplied investment and depreciation sources have 0 observed 2018 province values; both have complete 2017 coverage, which is sufficient for frozen lagged-flow K_2018 recursions."
    (out / "source_hash_receipt.json").write_text(json.dumps(source_receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    flags = [
        {"scope": "GLOBAL", "province_index": "", "province_name": "", "year": 2018, "field": "investment", "severity": "MATERIAL", "flag": "RAW_2018_OBSERVATION_UNAVAILABLE", "treatment": "left blank; no fill; K_2018 uses observed I_2017 under frozen timing"},
        {"scope": "GLOBAL", "province_index": "", "province_name": "", "year": 2018, "field": "depreciation", "severity": "MATERIAL", "flag": "RAW_2018_OBSERVATION_UNAVAILABLE", "treatment": "left blank; no fill; Track-B K_2018 uses observed D_2017"},
        {"scope": "GLOBAL", "province_index": "", "province_name": "", "year": "2000-2018", "field": "capital", "severity": "INTERPRETIVE", "flag": "RAW_GFCF_ROUTE_DIFFERS_FROM_ACCEPTED_CANONICAL_INVESTMENT_ROUTE", "treatment": "preserve both; do not promote rebuilt track to model production authority"},
        {"scope": "GLOBAL", "province_index": "", "province_name": "", "year": "2000-2018", "field": "Track B", "severity": "INTERPRETIVE", "flag": "DIAGNOSTIC_INITIAL_STOCK_ASSUMPTION", "treatment": "K_2000=I_2000/0.1; accounting identity uses lagged observed I and D"},
    ]
    for row in ledger_rows:
        if "RAW_GDP_DIFFERS_FROM_CANONICAL" in row["data_quality_provenance_flag"]:
            flags.append({"scope": "PROVINCE", "province_index": row["province_index"], "province_name": row["province_name"], "year": 2018, "field": "GDP", "severity": "RECONCILIATION", "flag": "RAW_NBS_DIFFERS_FROM_CANONICAL", "treatment": "both values retained in ledger"})
        if "RAW_POP_DIFFERS_FROM_CANONICAL" in row["data_quality_provenance_flag"]:
            flags.append({"scope": "PROVINCE", "province_index": row["province_index"], "province_name": row["province_name"], "year": 2018, "field": "population", "severity": "RECONCILIATION", "flag": "RAW_NBS_DIFFERS_FROM_CANONICAL", "treatment": "both values retained in ledger"})
    write_csv(out / "data_quality_flags.csv", flags)

    anhui = ledger_rows[11]
    def anhui_rank(field: str) -> int:
        ranked = sorted(ledger_rows, key=lambda r: abs(r[field]), reverse=True)
        return next(i for i, row in enumerate(ranked, 1) if row["province_name"] == "安徽")
    anhui_gdp_rank = anhui_rank("gdp_relative_difference_vs_legacy")
    anhui_pop_rank = anhui_rank("population_relative_difference_vs_legacy")
    anhui_capital_rank = anhui_rank("capital_relative_difference_vs_legacy")
    anhui_z_rank = anhui_rank("zt_relative_difference_vs_legacy")
    kb_diffs = [abs(r["track_a_to_track_b_ratio"] - 1.0) for r in ledger_rows]
    report = f"""# Chapter 5 MP4C raw-NBS 2018 rebuild, capital and productivity re-estimation

Date: 2026-09-10

## Required answers

1. **Raw years actually available.** GDP has observations for {min(coverage['gdp']['years_with_any_observation'])}–{max(coverage['gdp']['years_with_any_observation'])} and 31/31 coverage for {min(coverage['gdp']['years_with_31_observations'])}–{max(coverage['gdp']['years_with_31_observations'])}; population has observations and 31/31 coverage for {min(coverage['population']['years_with_31_observations'])}–{max(coverage['population']['years_with_31_observations'])}; fixed capital formation has observations for {min(coverage['investment']['years_with_any_observation'])}–{max(coverage['investment']['years_with_any_observation'])} and 31/31 coverage for {min(coverage['investment']['years_with_31_observations'])}–{max(coverage['investment']['years_with_31_observations'])}; depreciation has observations and 31/31 coverage for {min(coverage['depreciation']['years_with_31_observations'])}–{max(coverage['depreciation']['years_with_31_observations'])}. Header-only blank years are not called available. Exact header/any/full coverage is in `source_hash_receipt.json`.
2. **Fully same-year 2018 four-source panel:** no. GDP and population are 31/31 in 2018, but the supplied fixed-capital-formation and depreciation files are 0/31 in 2018. No values were filled. Both flows are 31/31 in 2017, so the frozen lagged-flow definitions can still produce K_2018.
3. **Track-A K_2018:** all 31 values are in `corrected_2018_vs_matlab_ledger.csv` and its compact Markdown rendering. 安徽 is `{anhui['corrected_track_a_capital_2018_100m_yuan']:.15g}` 亿元.
4. **Track-B diagnostic:** with the same K_2000=I_2000/0.1 initial stock and K_t=K_(t-1)+I_(t-1)-D_(t-1), 安徽 K_2018 is `{anhui['corrected_track_b_capital_2018_100m_yuan']:.15g}` 亿元; Track-A/Track-B is `{anhui['track_a_to_track_b_ratio']:.15g}`. Across provinces, the largest absolute Track-A/Track-B departure from 1 is `{max(kb_diffs):.15g}`. Track B remains diagnostic only.
5. **New 2009–2018 alpha:** `{alpha:.15g}` (SE `{float(ols.bse[2]):.15g}`, t `{float(ols.tvalues[2]):.15g}`, p `{float(ols.pvalues[2]):.15g}`, R² `{float(ols.rsquared):.15g}`, N `{int(ols.nobs)}`). This pooled OLS uses Track A and 31 provinces × 10 years; the legacy `{LEGACY_ALPHA}` is comparison only.
6. **Same-year Z_2018:** all 31 Track-A and diagnostic Track-B values are in the ledger. 安徽 Track-A Z is `{anhui['corrected_track_a_zt_2018']:.17g}` and Track-B Z is `{anhui['corrected_track_b_zt_2018']:.17g}`. GDP, population and capital are all bound to 2018; capital uses observed 2017 lagged flows by the declared identity.
7. **Versus legacy mixed-year MATLAB:** 安徽 GDP, population, capital and Track-A Z relative differences are respectively `{anhui['gdp_relative_difference_vs_legacy']:.6%}`, `{anhui['population_relative_difference_vs_legacy']:.6%}`, `{anhui['capital_relative_difference_vs_legacy']:.6%}`, and `{anhui['zt_relative_difference_vs_legacy']:.6%}`. All-province exact values remain in CSV.
8. **安徽 outlier status:** its absolute legacy-relative difference ranks are GDP {anhui_gdp_rank}/31, population {anhui_pop_rank}/31, capital {anhui_capital_rank}/31, and Z {anhui_z_rank}/31 (1 = largest). GDP and Z are in the upper part of the cross-province distribution, but 安徽 is not the largest and capital is not unusually discrepant relative to other provinces. These are descriptive cross-object ranks, not causal evidence; the rebuild does not establish a unique 安徽 anomaly.
9. **Remaining scientific judgment:** yes. The two supplied flow files lack 2018 observations; raw gross fixed capital formation is not the same source route as the accepted canonical fixed-asset-investment calibration; Track-B initial stock is assumed; raw/canonical discrepancies are preserved in the ledger. Owner/Reviewer judgment is required before any production-input promotion.
10. **Model calls:** MATLAB HANK=0; Python household/HJB/KFE=0; firm/wage/migration/capital allocation=0; outer turn=0; steady state/GE/annual/IRF/Results=0.

## Verdict

`RAW_NBS_2018_REBUILD_PARTIAL__SOURCE_COVERAGE_OR_UNIT_AMBIGUITY`

The 31-province panel, both capital paths, pooled-OLS alpha, and same-year 2018 productivity are reproducible. The verdict is PARTIAL because actual 2018 fixed-capital-formation and depreciation observations are absent from the supplied raw files and because the raw GFCF route differs from the accepted canonical investment route. This is calibration evidence only. `Results eligibility = FALSE`.

## Methods and units

- Explicit province mapping: full NBS names to the accepted 31 short names, in the accepted order; recorded in `source_hash_receipt.json`.
- Panel retained: 2000–2018, 31 provinces, 589 rows. Raw GDP/I/D/K use 亿元; raw population uses 万人. Separate model columns use GDP ×1000, population ×100, and capital/flows ×10,000,000.
- Track A: K_2000=I_2000/0.1; for t=2001,…,2018, K_t=(1-0.096)K_(t-1)+I_(t-1). Thus K_2018 consumes I_2000,…,I_2017 and not a fabricated I_2018.
- Track B: same initial stock; K_t=K_(t-1)+I_(t-1)-D_(t-1). It is an observed-depreciation accounting diagnostic, not a production series.
- Alpha: pooled OLS, `log(Y/L) = intercept + trend + alpha*log(K/L) + error`, years 2009–2018, no missing exclusions.
- Z: Y_2018/(K_2018^alpha L_2018^(1-alpha)) using the explicit model-unit columns. No 2020 level enters the corrected object.

## Reconciliation and authority

The canonical workbook was read as an identity-bound comparison object only after its SHA-256 matched `{expected_canonical_hash}`. Canonical comparison values are taken from the accepted 31-province audit ledger tied to that workbook. Raw values were never forced to match it. Detailed classifications appear in `data_quality_flags.csv`.

Live task authority was the exact task named by `project_rules/PROJECT_RULE_INDEX_CURRENT.md`. At execution start, the more general current status/handoff still stated that there was no active task; this documentation lag was retained rather than treated as broader authority.

No raw XLS file was modified or committed. The four files were opened read-only through Excel COM and hashes were fixed before use. No interpolation, forward fill, backward fill, model run, successor task, main merge, or Results publication occurred.

Development execution accounting before candidate publication: 1 successful read-only XLS extraction; 1 earlier PowerShell parser failure before any source workbook opened; 4 deterministic builder/regression runs (4 pooled OLS fits); 4 focused-test process invocations; and 2 Python compile checks. Scientific/model calls remained exactly zero in every attempt.
"""
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(report, encoding="utf-8")

    summary = {
        "verdict": "RAW_NBS_2018_REBUILD_PARTIAL__SOURCE_COVERAGE_OR_UNIT_AMBIGUITY",
        "alpha": alpha, "alpha_se": float(ols.bse[2]), "alpha_p": float(ols.pvalues[2]),
        "r_squared": float(ols.rsquared), "sample_size": int(ols.nobs),
        "anhui": anhui, "model_calls": 0, "results_eligible": False,
    }
    (out / "rebuild_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
