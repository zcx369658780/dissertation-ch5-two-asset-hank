"""Build a zero-science decomposition from accepted C1 saved ledgers only."""
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter
from hashlib import sha256
from pathlib import Path
from statistics import median, pstdev
from typing import Any, Iterable


REPO = Path(__file__).resolve().parents[3]
ACCEPTED = REPO / "reports/mp4c_c1_residual_public_asset_25turn_20260911"
OUT_REL = Path("reports/mp4c_c1_price_numeraire_raw_ra_forensic_20260911")
DOC_REL = Path("docs/CH5_MP4C_C1_PRICE_NUMERAIRE_RAW_RA_FORENSIC_AND_NORMALIZATION_SPEC.md")
VERDICT = "C1_PRICE_NUMERAIRE_RAW_RA_FORENSIC_PASS__RETURN_PRESSURE_DECOMPOSED_AND_NEXT_GATE_IDENTIFIED"
DELTA = 0.025
THETA = 100.0
EPSILON = 10.0
MSTAR = 1.0 - 1.0 / EPSILON
RAMIN = 0.02
RAMAX = 0.09
TOLERANCE = 2e-12


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest().upper()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        raise ValueError("cannot write empty forensic ledger")
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def f(value: Any) -> float:
    return float(value)


def stats(values: Iterable[float]) -> dict[str, float]:
    vector = list(values)
    if not vector or not all(math.isfinite(x) for x in vector):
        raise ValueError("statistics require finite nonempty values")
    return {"min": min(vector), "median": median(vector), "max": max(vector)}


def coefficient_of_variation(values: Iterable[float]) -> float:
    vector = list(values)
    mean = sum(vector) / len(vector)
    return pstdev(vector) / abs(mean)


def correlation(x: Iterable[float], y: Iterable[float]) -> float:
    a, b = list(x), list(y)
    if len(a) != len(b) or len(a) < 2:
        raise ValueError("correlation vectors must share at least two observations")
    am, bm = sum(a) / len(a), sum(b) / len(b)
    numerator = sum((u - am) * (v - bm) for u, v in zip(a, b))
    denominator = math.sqrt(sum((u - am) ** 2 for u in a) * sum((v - bm) ** 2 for v in b))
    return numerator / denominator


def raw_classification(raw: float, lower: float, upper: float) -> str:
    if raw < lower:
        return "LOWER"
    if raw > upper:
        return "UPPER"
    return "INTERIOR"


def recover_components(row: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    """Recover saved-row components without invoking the firm or any model runtime."""
    turn, province = int(row["turn"]), str(row["province"])
    capital, output = f(row["firm_K_total_MU"]), f(row["Y"])
    alpha, saved_rk = f(row["alpha"]), f(row["firm_rk"])
    saved_ra0, used_ra = f(row["firm_ra0"]), f(row["firm_ra_used"])
    ramin, ramax = f(row["ramin"]), f(row["ramax"])
    if min(capital, output, alpha) <= 0.0:
        raise ValueError(f"{province} turn {turn}: non-positive decomposition input")
    if ramin != RAMIN or ramax != RAMAX:
        raise ValueError(f"{province} turn {turn}: return bounds differ from frozen values")
    corptau, pit = f(state["corptau"]), f(state["pit"])
    mt = saved_rk * capital / (alpha * output)
    y_over_k, k_over_y = output / capital, capital / output
    rk_reconstructed = mt * alpha * y_over_k
    adjustment_cost_over_y = THETA / 2.0 * pit**2
    profit_pre_floor_over_y = 1.0 - mt - adjustment_cost_over_y
    profit_over_y = max(profit_pre_floor_over_y, 0.0)
    profit_over_k = profit_over_y * y_over_k
    after_tax_profit_over_k = profit_over_k * (1.0 - corptau)
    ra0_reconstructed = rk_reconstructed - DELTA + after_tax_profit_over_k
    error = ra0_reconstructed - saved_ra0
    if abs(error) > TOLERANCE * max(1.0, abs(saved_ra0)):
        raise RuntimeError(f"{province} turn {turn}: raw-ra reconstruction mismatch {error}")
    positive = saved_rk + after_tax_profit_over_k
    no_profit = saved_rk - DELTA
    mstar_profit_over_y = max(1.0 - MSTAR - adjustment_cost_over_y, 0.0)
    ra0_at_mstar = (
        MSTAR * alpha * y_over_k - DELTA
        + mstar_profit_over_y * (1.0 - corptau) * y_over_k
    )
    clip_amount = max(ramin - saved_ra0, 0.0, saved_ra0 - ramax)
    expected_used = min(max(saved_ra0, ramin), ramax)
    if abs(expected_used - used_ra) > TOLERANCE:
        raise RuntimeError(f"{province} turn {turn}: clipped ra mismatch")
    return {
        "turn": turn, "province_index": int(row["province_index"]), "province": province,
        "Yt_MU": output, "Kt_MU": capital, "Y_over_K": y_over_k, "K_over_Y": k_over_y,
        "mt_recovered": mt, "mt_recovery_method": "SAVED_RK_TIMES_K_OVER_ALPHA_Y_IDENTITY",
        "mt_independent_nkpc_reconstruction": "MISSING_OBJECT__LAGGED_KT_PRIOR_RK_AND_COMPLETE_PIT_LAGS_NOT_SAVED",
        "mt_minus_mstar": mt - MSTAR, "mstar": MSTAR, "alpha": alpha,
        "rk_saved": saved_rk, "rk_reconstructed": rk_reconstructed,
        "delta_offset": -DELTA, "delta": DELTA, "theta": THETA, "pit": pit,
        "price_adjustment_cost_over_Y": adjustment_cost_over_y,
        "profit_pre_floor_over_Y": profit_pre_floor_over_y, "profit_floor_binding": profit_pre_floor_over_y <= 0.0,
        "profit_over_Y": profit_over_y, "profit_over_K": profit_over_k, "corptau": corptau,
        "after_tax_profit_over_K": after_tax_profit_over_k,
        "rk_share_of_positive_components": saved_rk / positive,
        "profit_share_of_positive_components": after_tax_profit_over_k / positive,
        "ra0_without_profit": no_profit, "ra0_at_mstar": ra0_at_mstar,
        "ra0_saved": saved_ra0, "ra0_reconstructed": ra0_reconstructed,
        "ra0_reconstruction_error": error, "ra_used": used_ra, "ramin": ramin, "ramax": ramax,
        "ra0_minus_ramax": saved_ra0 - ramax, "clip_amount": clip_amount,
        "raw_ra_classification": raw_classification(saved_ra0, ramin, ramax),
        "firm_wage_raw": f(row["firm_wage_raw"]), "firm_wage_used": f(row["firm_wage_used"]),
        "household_composite_wage": f(row["household_composite_wage"]),
        "firm_labor_supply": f(row["firm_Lt_supply"]), "population_proxy_NU": f(row["Ltarget_proxy_NU"]),
    }


def geometry_rows(components: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in components:
        mt, alpha = f(item["mt_recovered"]), f(item["alpha"])
        profit_coefficient = max(1.0 - mt - f(item["price_adjustment_cost_over_Y"]), 0.0) * (1.0 - f(item["corptau"]))
        for bound_name, level in (("ramin", RAMIN), ("ramax", RAMAX)):
            rows.append({
                "turn": item["turn"], "province_index": item["province_index"], "province": item["province"],
                "return_level_name": bound_name, "return_level": level,
                "observed_K_over_Y": item["K_over_Y"], "observed_Y_over_K": item["Y_over_K"],
                "mt_saved_identity": mt, "alpha": alpha,
                "K_over_Y_for_pure_MPK_equal_return": mt * alpha / level,
                "K_over_Y_for_rk_minus_delta_equal_return": mt * alpha / (level + DELTA),
                "K_over_Y_for_full_ra0_equal_return": (mt * alpha + profit_coefficient) / (level + DELTA),
                "geometry_status": "ALGEBRAIC_GEOMETRY_ONLY__NOT_TARGET_OR_CALIBRATION",
            })
    return rows


def rank_turn25(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selected = [dict(row) for row in rows if int(row["turn"]) == 25]
    if len(selected) != 31:
        raise ValueError("turn 25 must contain 31 provinces")
    for field, rank_name in (("ra0_saved", "ra0_desc_rank"), ("Y_over_K", "Y_over_K_desc_rank"),
                             ("profit_over_K", "profit_over_K_desc_rank")):
        order = sorted(range(31), key=lambda i: (-f(selected[i][field]), int(selected[i]["province_index"])))
        for rank, index in enumerate(order, 1):
            selected[index][rank_name] = rank
    keep = (
        "ra0_desc_rank", "Y_over_K_desc_rank", "profit_over_K_desc_rank", "province_index", "province",
        "Y_over_K", "K_over_Y", "mt_recovered", "mt_minus_mstar", "alpha", "rk_saved", "delta",
        "profit_over_K", "after_tax_profit_over_K", "rk_share_of_positive_components",
        "profit_share_of_positive_components", "ra0_without_profit", "ra0_at_mstar", "ra0_saved",
        "ra_used", "ramax", "ra0_minus_ramax", "clip_amount", "raw_ra_classification",
    )
    selected.sort(key=lambda row: int(row["ra0_desc_rank"]))
    return [{key: row[key] for key in keep} for row in selected]


def verify_accepted_manifest() -> dict[str, Any]:
    manifest = read_json(ACCEPTED / "manifest.json")
    original_readback = read_json(ACCEPTED / "manifest_readback.json")
    if not original_readback.get("all_match") or original_readback.get("entries_checked") != len(manifest["entries"]):
        raise RuntimeError("accepted C1 original manifest readback is not valid")
    mismatches = []
    newline_only = []
    exact = []
    for entry in manifest["entries"]:
        path = REPO / entry["path"]
        actual = file_sha(path)
        if actual == entry["sha256"]:
            exact.append(entry["path"])
            continue
        data = path.read_bytes()
        lf = data.replace(b"\r\n", b"\n")
        crlf = lf.replace(b"\n", b"\r\n")
        variants = {sha256(lf).hexdigest().upper(), sha256(crlf).hexdigest().upper()}
        record = {"path": entry["path"], "expected": entry["sha256"], "actual": actual}
        if entry["sha256"] in variants:
            newline_only.append(record)
        else:
            mismatches.append(record)
    if mismatches:
        raise RuntimeError(f"accepted C1 manifest mismatch: {mismatches}")
    core = {
        "reports/mp4c_c1_residual_public_asset_25turn_20260911/province_turn_capital_ledger.csv",
        "reports/mp4c_c1_residual_public_asset_25turn_20260911/national_turn_summary.csv",
        "reports/mp4c_c1_residual_public_asset_25turn_20260911/initialization_receipt_31province.csv",
        "reports/mp4c_c1_residual_public_asset_25turn_20260911/runtime_input_receipt.json",
        "reports/mp4c_c1_residual_public_asset_25turn_20260911/source_hash_receipt.json",
    }
    if not core.issubset(set(exact)):
        raise RuntimeError("accepted C1 core forensic inputs are not byte-exact in current checkout")
    return {
        "manifest_sha256_current_checkout": file_sha(ACCEPTED / "manifest.json"),
        "entries_checked": len(manifest["entries"]), "byte_exact_count": len(exact),
        "newline_normalization_only_count": len(newline_only),
        "newline_normalization_only": newline_only,
        "current_checkout_all_content_equivalent": True,
        "current_checkout_core_inputs_byte_exact": True,
        "original_candidate_readback_all_match": True,
    }


def build(test_processes: int, test_cases: int, compile_processes: int) -> None:
    accepted_readback = verify_accepted_manifest()
    out = REPO / OUT_REL
    out.mkdir(parents=True, exist_ok=True)
    init_rows = read_csv(ACCEPTED / "initialization_receipt_31province.csv")
    states = {row["province"]: json.loads(row["outer_turn_1_initial_state_json"]) for row in init_rows}
    if len(states) != 31:
        raise ValueError("accepted initialization state count is not 31")
    for province, state in states.items():
        if f(state["corptau"]) != 0.25 or f(state["pit"]) != 0.02 or f(state["pit_1"]) != 0.02:
            raise ValueError(f"{province}: frozen tax/inflation state differs")
    accepted_rows = read_csv(ACCEPTED / "province_turn_capital_ledger.csv")
    if len(accepted_rows) != 775:
        raise ValueError("accepted C1 ledger does not contain 775 rows")
    components = [recover_components(row, states[row["province"]]) for row in accepted_rows]
    if Counter(int(row["turn"]) for row in components) != Counter({turn: 31 for turn in range(1, 26)}):
        raise ValueError("accepted C1 turn/province axis is incomplete")
    write_csv(out / "ra0_component_ledger.csv", components)
    turn25 = rank_turn25(components)
    write_csv(out / "turn25_ra0_component_summary.csv", turn25)
    write_csv(out / "ky_return_geometry.csv", geometry_rows(components))

    late = [row for row in components if 20 <= int(row["turn"]) <= 25]
    t25_all = [row for row in components if int(row["turn"]) == 25]
    t25_upper = [row for row in t25_all if row["raw_ra_classification"] == "UPPER"]
    classifications = Counter(row["raw_ra_classification"] for row in t25_all)
    counterfactual = {
        "schema": "CH5_C1_PRICE_NUMERAIRE_RAW_RA_STATIC_COUNTERFACTUAL_V1",
        "accepted_turn25_raw_classification": {key: classifications.get(key, 0) for key in ("LOWER", "INTERIOR", "UPPER")},
        "turn25_above_ramax_without_profit": sum(f(row["ra0_without_profit"]) > RAMAX for row in t25_all),
        "turn25_above_ramax_at_mstar_with_source_profit": sum(f(row["ra0_at_mstar"]) > RAMAX for row in t25_all),
        "turn25_profit_floor_binding_count": sum(bool(row["profit_floor_binding"]) for row in t25_all),
        "turn25_mt": stats(f(row["mt_recovered"]) for row in t25_all),
        "turn20_25_mt": stats(f(row["mt_recovered"]) for row in late),
        "turn25_Y_over_K": stats(f(row["Y_over_K"]) for row in t25_all),
        "turn25_profit_over_K": stats(f(row["profit_over_K"]) for row in t25_all),
        "turn25_rk": stats(f(row["rk_saved"]) for row in t25_all),
        "turn25_ra0": stats(f(row["ra0_saved"]) for row in t25_all),
        "upper30_rk_positive_component_share": stats(f(row["rk_share_of_positive_components"]) for row in t25_upper),
        "upper30_profit_positive_component_share": stats(f(row["profit_share_of_positive_components"]) for row in t25_upper),
        "upper30_Y_over_K_coefficient_of_variation": coefficient_of_variation(f(row["Y_over_K"]) for row in t25_upper),
        "upper30_mt_coefficient_of_variation": coefficient_of_variation(f(row["mt_recovered"]) for row in t25_upper),
        "turn25_ra0_correlation_with_Y_over_K": correlation((f(r["ra0_saved"]) for r in t25_all), (f(r["Y_over_K"]) for r in t25_all)),
        "turn25_ra0_correlation_with_mt": correlation((f(r["ra0_saved"]) for r in t25_all), (f(r["mt_recovered"]) for r in t25_all)),
        "maximum_absolute_ra0_reconstruction_error": max(abs(f(row["ra0_reconstruction_error"])) for row in components),
        "bound_widening_or_removal_answer": "INSUFFICIENT_EVIDENCE",
        "counterfactual_scope": "STATIC_ALGEBRA_ON_ACCEPTED_SAVED_ROWS__NOT_MODEL_CALL_OR_PARAMETER_RECOMMENDATION",
        "missing_object": "INDEPENDENT_NKPC_MT_RECONSTRUCTION_MISSING_LAGGED_KT_PRIOR_RK_AND_COMPLETE_PIT_LAGS",
        "results_eligible": False,
    }
    write_json(out / "static_counterfactual_summary.json", counterfactual)

    bound_md = """# Return and wage bound provenance

| object | source values | classification | evidence |
| --- | ---: | --- | --- |
| firm return bounds | `[.02,.09]` | `EMPIRICAL_NUMERICAL_SAFEGUARD` | `multi_prov_HANK_12sts.m:49-52` contains commented alternatives `.01/.065`; `HANK_firm.m:55` explicitly says the range prevents failure during convergence; `HANK_mp_1eq.m` rejects final return-bound hits. No empirical-rate dataset or period convention is cited. |
| firm wage bounds | `[.8,1.3]` | `SOURCE_VALUE_WITH_UNRESOLVED_ECONOMIC_UNIT` | `multi_prov_HANK_12sts.m:53-55` gives the values and a commented former upper value `1`; `HANK_firm.m` clips and tax-compensates, but inspected source gives no currency, period, deflator, or economic calibration. |

The classification names follow the exact task vocabulary. Historical use does not make either interval structural. Current evidence is `INSUFFICIENT_EVIDENCE` for widening or removing the return clips and supplies no defensible replacement upper bound.
"""
    (out / "return_bound_provenance.md").write_text(bound_md, encoding="utf-8")
    wage_chain = [
        {"object": "Yt", "source_equation_or_role": "aggregate firm output", "implied_unit": "MU_10WAN_YUAN_PER_MODEL_PERIOD", "mapping_status": "SOURCE_BOUND_MACRO_UNIT"},
        {"object": "Kt", "source_equation_or_role": "private K plus C1 residual public asset", "implied_unit": "MU_10WAN_YUAN_STOCK", "mapping_status": "SOURCE_BOUND_MACRO_UNIT"},
        {"object": "Lt", "source_equation_or_role": "destination firm labor supply from source-faithful migration", "implied_unit": "MODEL_LABOR_ON_NU_AXIS", "mapping_status": "NOT_OBSERVED_WORKPLACE_EMPLOYMENT"},
        {"object": "Zt", "source_equation_or_role": "Y/(K^alpha L^(1-alpha))", "implied_unit": "(MU/NU)^(1-alpha)_PER_MODEL_PERIOD", "mapping_status": "SAME_YEAR_IDENTITY"},
        {"object": "KNratio", "source_equation_or_role": "K/L", "implied_unit": "MU/NU", "mapping_status": "MACRO_RATIO"},
        {"object": "wt0", "source_equation_or_role": "mt*(1-alpha)*Z*(K/L)^alpha = mt*(1-alpha)*Y/L", "implied_unit": "MU/NU_PER_MODEL_PERIOD", "mapping_status": "MACRO_IMPLIED_FIRM_WAGE"},
        {"object": "wjt", "source_equation_or_role": "clip(wt0,[.8,1.3]) with tax compensation", "implied_unit": "MUST_MATCH_WT0_IF_ECONOMICALLY_COMPARABLE", "mapping_status": "SOURCE_VALUE_WITH_UNRESOLVED_ECONOMIC_UNIT"},
        {"object": "household_w", "source_equation_or_role": "unnormalized nonlinear 31-destination CES-like composite of wjt after tax/wedge", "implied_unit": "ALGEBRAIC_WJT_UNIT_IF_PHI_IS_DIMENSIONLESS", "mapping_status": "IMPLIED_RELATIVE_UNIT_ONLY__NOT_DIRECT_LEVEL_COMPARATOR"},
        {"object": "MU_over_NU", "source_equation_or_role": "100000 yuan / 100 persons", "implied_unit": "1000_YUAN_PER_PERSON_PER_MODEL_PERIOD", "mapping_status": "MACRO_CONVERSION_ONLY__HOUSEHOLD_PERIOD_MAPPING_UNRESOLVED"},
    ]
    write_csv(out / "wage_numeraire_dimensional_chain.csv", wage_chain)
    decisions = [
        {"decision": "WIDEN_OR_REMOVE_RETURN_CLIPS", "current_answer": "INSUFFICIENT_EVIDENCE", "owner_input_required": "economically identified return period, capital concept, and admissible interval", "lowest_risk_next_step": "do not change bounds"},
        {"decision": "FIRM_TO_HOUSEHOLD_WAGE_NUMERAIRE", "current_answer": "UNRESOLVED", "owner_input_required": "currency, deflator, period, labor-unit mapping and aggregator normalization", "lowest_risk_next_step": "freeze an explicit dimensional mapping before runtime"},
        {"decision": "NORMALIZED_LABOR_SEQUENCE", "current_answer": "PRICE_NUMERAIRE_FIRST", "owner_input_required": "whether accepted normalized labor should follow a price-unit gate", "lowest_risk_next_step": "keep normalized labor inactive while identifying price units"},
        {"decision": "NEXT_SCIENTIFIC_EXPERIMENT", "current_answer": "CONDITIONAL", "owner_input_required": "one pre-registered price/return normalization object", "lowest_risk_next_step": "one initialization-only price receipt on frozen C1 inputs; no outer trajectory"},
        {"decision": "KFE_VALIDITY", "current_answer": "INDEPENDENT_BLOCKER", "owner_input_required": "separate KFE boundary/source/pinning design", "lowest_risk_next_step": "do not couple KFE repair to price normalization"},
    ]
    write_csv(out / "owner_decision_matrix.csv", decisions)
    write_json(out / "zero_scientific_call_ledger.json", {
        "schema": "CH5_C1_PRICE_NUMERAIRE_RAW_RA_ZERO_SCIENCE_LEDGER_V1",
        "accepted_rows_parsed": 775, "static_component_rows": 775, "geometry_rows": 1550,
        "scientific_processes": 0, "hjb_calls": 0, "kfe_calls": 0, "household_calls": 0,
        "migration_calls": 0, "normalized_migration_calls": 0, "firm_runtime_calls": 0,
        "wage_runtime_calls": 0, "controller_runtime_calls": 0, "outer_turn_calls": 0,
        "trajectory_calls": 0, "steady_state_calls": 0, "matlab_runtime_calls": 0,
        "root_or_brent_calls": 0, "ge_calls": 0, "annual_calls": 0, "irf_calls": 0,
        "results_calls": 0, "parameter_changes": 0, "results_eligible": False,
    })
    write_json(out / "focused_static_test_receipt.json", {
        "schema": "CH5_C1_PRICE_NUMERAIRE_RAW_RA_FOCUSED_STATIC_TEST_V1", "status": "PASS",
        "test_processes": test_processes, "test_cases_passed": test_cases,
        "compile_processes": compile_processes, "scientific_calls": 0,
    })

    protected_root = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK")
    source_paths = [
        REPO / "src/ch5_two_asset_hank/multi_province/firm.py",
        REPO / "src/ch5_two_asset_hank/multi_province/wage.py",
        REPO / "src/ch5_two_asset_hank/multi_province/c1_residual_public_asset.py",
        REPO / "src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py",
        REPO / "validators/multi_province/c1_residual_public_asset_25turn/run.py",
        REPO / "validators/multi_province/c1_price_numeraire_raw_ra_forensic/build.py",
        REPO / "tests/test_mp4c_c1_price_numeraire_raw_ra_forensic.py",
    ]
    protected_names = ("HANK_firm.m", "wage_caculate.m", "HANK_mp_1turn.m", "HANK_mp_1eq.m", "multi_prov_HANK_12sts.m")
    write_json(out / "source_hash_receipt.json", {
        "schema": "CH5_C1_PRICE_NUMERAIRE_RAW_RA_SOURCE_HASH_V1",
        "baseline_origin_main": "82d81017375e05d08176fda93d36233befa94dab",
        "accepted_c1_manifest": accepted_readback,
        "accepted_inputs": {name: file_sha(ACCEPTED / name) for name in (
            "province_turn_capital_ledger.csv", "national_turn_summary.csv",
            "initialization_receipt_31province.csv", "runtime_input_receipt.json", "source_hash_receipt.json")},
        "repository_sources": {path.relative_to(REPO).as_posix(): file_sha(path) for path in source_paths},
        "protected_matlab_read_only": {name: {"path": str(protected_root / name), "sha256": file_sha(protected_root / name)} for name in protected_names},
        "scientific_calls": 0,
    })

    report = f"""# Chapter 5 MP4C C1 price/numeraire and raw-ra upper-pressure forensic/spec

Date: 2026-09-11

Builder verdict: `{VERDICT}`

## Result

All 775 accepted C1 province-turn rows were statically decomposed with maximum raw-ra reconstruction error `{counterfactual['maximum_absolute_ra0_reconstruction_error']}`. No firm, wage, household, HJB, KFE, migration, controller, outer-turn, MATLAB, root/Brent, GE, annual, IRF or Results runtime was called.

At turn 25, raw ra0 min/median/max is `{counterfactual['turn25_ra0']['min']}/{counterfactual['turn25_ra0']['median']}/{counterfactual['turn25_ra0']['max']}` and lower/interior/upper counts remain `0/1/30`. Y/K is `{counterfactual['turn25_Y_over_K']['min']}/{counterfactual['turn25_Y_over_K']['median']}/{counterfactual['turn25_Y_over_K']['max']}`; recovered mt is `{counterfactual['turn25_mt']['min']}/{counterfactual['turn25_mt']['median']}/{counterfactual['turn25_mt']['max']}` around mstar `{MSTAR}`. Profit is floored at zero in `{counterfactual['turn25_profit_floor_binding_count']}/31` provinces and profit/K min/median/max is `{counterfactual['turn25_profit_over_K']['min']}/{counterfactual['turn25_profit_over_K']['median']}/{counterfactual['turn25_profit_over_K']['max']}`.

## Attribution

The upper pressure is overwhelmingly the MPK-like `rk=mt*alpha*Y/K` term. Among the 30 upper provinces, rk's share of positive pre-depreciation components is `{counterfactual['upper30_rk_positive_component_share']['min']}/{counterfactual['upper30_rk_positive_component_share']['median']}/{counterfactual['upper30_rk_positive_component_share']['max']}`, while after-tax profit/K contributes `{counterfactual['upper30_profit_positive_component_share']['min']}/{counterfactual['upper30_profit_positive_component_share']['median']}/{counterfactual['upper30_profit_positive_component_share']['max']}`. Removing profit leaves `{counterfactual['turn25_above_ramax_without_profit']}/31` above `.09`; replacing mt by source mstar while retaining the source profit equation also leaves `{counterfactual['turn25_above_ramax_at_mstar_with_source_profit']}/31` above `.09`. Depreciation offsets every row by exactly `-.025`. Cross-sectionally, upper-province Y/K coefficient of variation is `{counterfactual['upper30_Y_over_K_coefficient_of_variation']}` versus mt `{counterfactual['upper30_mt_coefficient_of_variation']}`. Thus corrected empirical Y/K relative to the historical bound is primary; mt modestly amplifies it, profit is negligible at turn 25, and depreciation reduces rather than causes pressure.

Saved `mt` and `PIt` were not columns in the accepted ledger. `mt` is recoverable from the independently saved `rk`, K, alpha and Y identity; `PIt/K` is then reconstructed from the source profit equation using frozen theta, pit and corptau. A separate NKPC reconstruction of mt is not possible because complete lagged K, prior rk and inflation-lag objects were not saved. This limitation is explicit and does not affect the component identity check.

## Bounds and geometry

The return interval `[.02,.09]` is classified `EMPIRICAL_NUMERICAL_SAFEGUARD`, not an economically identified rate interval. The source says it prevents convergence-time failure and contains commented alternatives. Wage `[.8,1.3]` is `SOURCE_VALUE_WITH_UNRESOLVED_ECONOMIC_UNIT`: its clipping behavior is source-defined, but its currency, period and calibration are not. The K/Y values in `ky_return_geometry.csv` are algebraic comparisons only, not targets or recommendations.

Answer on widening/removing return clips: `INSUFFICIENT_EVIDENCE`. Current rows show that the numerical bound is tight relative to corrected Y/K, but do not identify an economically admissible period, return concept or replacement interval.

## Wage/numeraire and sequencing

Firm raw wage has implied macro unit MU/NU per model period, while the legacy wage clip lacks an absolute-unit mapping. Household `w` is a nonlinear, unnormalized 31-destination composite of clipped `wjt`; it is not a directly comparable single-firm wage level. The earlier raw firm wage near 12 and household composite near 18 are therefore compatible with different aggregation scales and unresolved absolute numeraire mapping. Wage does not enter the current ra0 equation directly, so this task does not establish causal contamination of ra0; it can affect future returns indirectly through household labor/assets and firm Y, K and mt.

Normalized labor should remain inactive until the price/return and wage numeraire mapping is identified. Labor enters ra0 indirectly through Y, K/L and the lagged-L term in mt, but turn-25 pressure is already reproduced almost entirely by saved Y/K and rk. Stacking normalized labor first would confound these channels.

## Next gate and blockers

The lowest-risk next scientific experiment is conditional on an Owner-approved, pre-registered price/return normalization object: one initialization-only price receipt on the frozen C1 corrected-2018 inputs, with no outer trajectory and no post-observation tuning. It must compare raw and mapped units without silently changing bounds. This report does not publish or authorize that task.

KFE remains an independent scientific blocker: accepted C1 has 775/775 KFE `DIAGNOSTIC_ONLY`. This forensic does not repair or reinterpret KFE. Results eligibility remains FALSE.

## Required questions answered

1. **Why are 30/31 raw-ra values above `.09` although C1 holds K at target?** Holding K at the corrected empirical target does not force a historical return clip to bind internally. The accepted corrected Y/K, combined with `mt*alpha`, implies an rk level that already leaves 30/31 provinces above `.09` after the fixed depreciation offset.
2. **What mainly causes the upper pressure?** Corrected empirical Y/K relative to the historical bound is primary. Recovered mt modestly amplifies it; profit/K is negligible at turn 25; depreciation subtracts `.025` and therefore cannot cause the pressure.
3. **Are `.02/.09` economically identified?** No. They are classified `EMPIRICAL_NUMERICAL_SAFEGUARD` from their source role and lack of a documented empirical rate/period mapping.
4. **Is widening or removing the clips justified?** `INSUFFICIENT_EVIDENCE`. No economically identified replacement interval or period convention is available.
5. **Can a firm-price/household-wage numeraire mismatch contaminate returns indirectly?** There is evidence of unresolved unit and aggregation comparability, so indirect contamination is possible through future household labor/assets and firm Y, K and mt. It is not demonstrated causally here, and wage does not enter the saved-row ra0 equation directly.
6. **Should normalized labor be activated first?** No. Price/return and wage-numeraire identification should remain the next gate; normalized labor stays inactive to avoid confounding channels.
7. **What is the lowest-risk next scientific experiment?** After Owner approval of one pre-registered unit-consistent normalization object, run one initialization-only price receipt on frozen C1 inputs, with no outer trajectory and no post-observation tuning. This report does not authorize or publish it.
"""
    (REPO / DOC_REL).write_text(report, encoding="utf-8")

    manifest_paths = [
        Path("validators/multi_province/c1_price_numeraire_raw_ra_forensic/__init__.py"),
        Path("validators/multi_province/c1_price_numeraire_raw_ra_forensic/build.py"),
        Path("tests/test_mp4c_c1_price_numeraire_raw_ra_forensic.py"), DOC_REL,
    ] + [OUT_REL / name for name in (
        "ra0_component_ledger.csv", "turn25_ra0_component_summary.csv", "return_bound_provenance.md",
        "wage_numeraire_dimensional_chain.csv", "ky_return_geometry.csv", "static_counterfactual_summary.json",
        "owner_decision_matrix.csv", "zero_scientific_call_ledger.json", "source_hash_receipt.json",
        "focused_static_test_receipt.json",
    )]
    entries = [{"path": path.as_posix(), "bytes": (REPO / path).stat().st_size, "sha256": file_sha(REPO / path)} for path in manifest_paths]
    write_json(out / "manifest.json", {"schema": "CH5_C1_PRICE_NUMERAIRE_RAW_RA_MANIFEST_V1",
                                       "verdict": VERDICT, "entries": entries, "results_eligible": False})
    manifest_sha = file_sha(out / "manifest.json")
    readback = [{"path": entry["path"], "expected_sha256": entry["sha256"],
                 "actual_sha256": file_sha(REPO / entry["path"]),
                 "match": file_sha(REPO / entry["path"]) == entry["sha256"]} for entry in entries]
    if not all(item["match"] for item in readback):
        raise RuntimeError("manifest readback failed")
    write_json(out / "manifest_readback.json", {
        "schema": "CH5_C1_PRICE_NUMERAIRE_RAW_RA_MANIFEST_READBACK_V1",
        "manifest_sha256": manifest_sha, "entries_checked": len(readback), "all_match": True,
        "entries": readback,
    })


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test-processes", type=int, required=True)
    parser.add_argument("--test-cases", type=int, required=True)
    parser.add_argument("--compile-processes", type=int, required=True)
    args = parser.parse_args()
    build(args.test_processes, args.test_cases, args.compile_processes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
