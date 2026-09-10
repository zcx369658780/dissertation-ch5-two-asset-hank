import ast
import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports/mp4c_unit_normalized_initialization_probe_20260910"


def rows():
    with (OUT / "province_initialization_receipt.csv").open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def test_receipt_has_ordered_31_provinces_and_frozen_units():
    data = rows()
    assert len(data) == 31
    assert [int(row["province_index"]) for row in data] == list(range(1, 32))
    anhui = data[11]
    assert anhui["province_name"] == "安徽"
    assert math.isclose(float(anhui["Y0_MU"]), 34_010_900.0)
    assert math.isclose(float(anhui["N0_NU"]), 607_600.0)
    assert math.isclose(float(anhui["K0_MU"]), 70_182_433.35888097)
    assert [row["province_name"] for row in data] == [
        "北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江", "上海", "江苏",
        "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "广西",
        "海南", "重庆", "四川", "贵州", "云南", "西藏", "陕西", "甘肃", "青海", "宁夏", "新疆",
    ]


def test_source_faithful_mt_and_firm_equation_identities():
    for row in rows():
        y, k, l = (float(row[key]) for key in ("Y0_MU", "K0_MU", "L0"))
        alpha, z, mt = (float(row[key]) for key in ("alpha_used", "Zt0", "mt0"))
        assert math.isclose(mt, 0.92, abs_tol=1e-15)
        assert math.isclose(z, y / (k**alpha * l**(1-alpha)), rel_tol=1e-14)
        assert math.isclose(float(row["raw_wjt0"]), mt*(1-alpha)*z*(k/l)**alpha, rel_tol=1e-14)
        expected_ra = float(row["rk_new"]) - 0.025 + float(row["divrate"])
        assert math.isclose(float(row["raw_ra0"]), expected_ra, rel_tol=1e-14)


def test_clipping_and_corptax_compensation_are_exact():
    for row in rows():
        raw_ra, used_ra = float(row["raw_ra0"]), float(row["used_ra0"])
        raw_w, used_w = float(row["raw_wjt0"]), float(row["used_wjt0"])
        k, l = float(row["K0_MU"]), float(row["L0"])
        before = float(row["Corptax_before_clipping"])
        assert math.isclose(used_ra, min(max(raw_ra, .02), .09))
        assert math.isclose(used_w, min(max(raw_w, .8), 1.3))
        after_ra = before + (raw_ra-used_ra)*k
        assert math.isclose(float(row["Corptax_after_ra_clip"]), after_ra, rel_tol=1e-14, abs_tol=1e-7)
        assert math.isclose(float(row["Corptax_after_ra_and_wage_clip"]), after_ra+(raw_w-used_w)*l, rel_tol=1e-14, abs_tol=1e-7)


def test_static_composites_and_bridge_are_complete():
    data = rows()
    assert all(math.isfinite(float(row["rah0"])) and float(row["rah0"]) > 0 for row in data)
    assert all(math.isfinite(float(row["w0"])) and float(row["w0"]) > 0 for row in data)
    assert all(row["composite_seed_policy"] == "INITIAL_COMPOSITE_NO_DAMPING_BASE" for row in data)
    with (OUT / "asset_bridge_scale_diagnostic.csv").open("r", encoding="utf-8-sig", newline="") as handle:
        bridge = list(csv.DictReader(handle))
    assert len(bridge) == 31
    assert all(row["bridge_status"] == "SOURCE_FAITHFUL_BASELINE_ONLY" for row in bridge)
    assert all(row["authority"] == "NO_REPLACEMENT_BRIDGE_SELECTED" for row in bridge)


def test_call_ledger_and_results_boundary():
    ledger = json.loads((OUT / "call_ledger.json").read_text(encoding="utf-8"))
    assert ledger["firm_equation_row_evaluations"] == 31
    for key in ("matlab", "household_hjb", "kfe", "household_control_solve", "outer_turn", "steady_state", "ge", "annual", "irf", "results", "parameter_tuning"):
        assert ledger[key] == 0
    summary = json.loads((OUT / "national_initialization_summary.json").read_text(encoding="utf-8"))
    assert summary["results_eligible"] is False
    assert summary["verdict"] == "UNIT_NORMALIZED_INITIALIZATION_PROBE_PASS__DATA_CONSISTENT_PRICE_RECEIPT_COMPLETE"


def test_helper_imports_no_model_or_solver_entrypoints():
    path = ROOT / "validators/multi_province/unit_normalized_initialization_probe/build.py"
    tree = ast.parse(path.read_text(encoding="utf-8"))
    modules = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            modules.append(node.module or "")
    forbidden = ("hank", "hjb", "kfe", "firm", "root", "scipy", "matlab")
    assert all(not any(token in module.lower() for token in forbidden) for module in modules)
