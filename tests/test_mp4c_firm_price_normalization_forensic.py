import ast
import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports/mp4c_firm_price_normalization_forensic_20260910"


def rows():
    with (OUT / "province_price_component_decomposition.csv").open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def test_complete_31_province_decomposition_and_exact_identities():
    data = rows()
    assert len(data) == 31
    assert [int(row["province_index"]) for row in data] == list(range(1, 32))
    for row in data:
        assert float(row["wage_identity_abs_error"]) <= 1e-13
        assert float(row["ra_identity_abs_error"]) <= 1e-13
        components = (float(row["mpk_component_mt_alpha_Y_over_K"])
                      + float(row["firm_depreciation_component"])
                      + float(row["profit_dividend_after_tax_component"])
                      + float(row["other_additive_return_component"]))
        assert math.isclose(components, float(row["ra_raw_component_sum"]), rel_tol=1e-14)


def test_national_classifications_and_bounds_are_preserved():
    summary = json.loads((OUT / "national_forensic_summary.json").read_text(encoding="utf-8"))
    assert summary["wage_conclusion"] == "PRICE_BOUND_HITS_PRIMARILY_UNIT_NORMALIZATION_MISMATCH"
    assert summary["return_conclusion"] == "PRICE_BOUND_HITS_PRIMARILY_ECONOMIC_RATIO_LEVELS"
    assert summary["household_currency_conclusion"] == "HOUSEHOLD_CURRENCY_NORMALIZATION_UNRESOLVED"
    assert summary["wage"]["bound_counts"] == {"below": 0, "inside": 0, "above": 31}
    assert summary["return"]["bound_counts"] == {"below": 0, "inside": 1, "above": 30}
    assert summary["results_eligible"] is False


def test_return_collapsed_formula_and_threshold():
    summary = json.loads((OUT / "national_forensic_summary.json").read_text(encoding="utf-8"))
    coefficient = .92 * .7380939146868483 + .75 * ((1-.92) - 100/2*.02**2)
    assert math.isclose(summary["return"]["Y_over_K_coefficient"], coefficient, abs_tol=1e-15)
    assert math.isclose(summary["return"]["K_over_Y_threshold_for_ra_0p09"], coefficient / .115, abs_tol=1e-14)


def test_beta_one_ratios_are_descriptive_only():
    summary = json.loads((OUT / "national_forensic_summary.json").read_text(encoding="utf-8"))
    bridge = summary["asset_bridge_beta_a_1_descriptive"]
    assert bridge["status"] == "SOURCE_FAITHFUL_BASELINE_ONLY__BETA_A_NOT_IDENTIFIED"
    assert 0 < bridge["AtN_to_K0_min"] <= bridge["AtN_to_K0_median"] <= bridge["AtN_to_K0_max"]


def test_zero_call_ledger_and_no_model_imports():
    ledger = json.loads((OUT / "zero_scientific_call_ledger.json").read_text(encoding="utf-8"))
    for key in ("matlab_model_calls", "python_household_hjb_kfe_control", "HANK_firm_runtime_calls", "Lt_seperate_calls", "capital_allocation_runtime_calls", "outer_turns", "steady_state", "ge", "annual", "irf", "results", "root_direct_iterative_eigen_solves", "parameter_tuning"):
        assert ledger[key] == 0
    tree = ast.parse((ROOT / "validators/multi_province/firm_price_normalization_forensic/build.py").read_text(encoding="utf-8"))
    modules = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            modules.append(node.module or "")
    forbidden = ("hank", "hjb", "kfe", "scipy", "numpy", "matlab")
    assert all(not any(token in module.lower() for token in forbidden) for module in modules)
