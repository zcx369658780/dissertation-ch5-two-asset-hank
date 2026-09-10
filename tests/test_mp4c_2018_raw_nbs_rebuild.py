import csv
import ast
import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports" / "mp4c_2018_raw_nbs_rebuild_20260910"
DOC = ROOT / "docs" / "CH5_MP4C_2018_RAW_NBS_DATA_REBUILD_CAPITAL_PRODUCTIVITY_REESTIMATION_REPORT.md"


def rows(name):
    with (REPORT_DIR / name).open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def test_clean_panel_shape_order_and_2018_identity():
    panel = rows("cleaned_province_year_panel.csv")
    assert len(panel) == 31 * 19
    slice_2018 = [row for row in panel if row["year"] == "2018"]
    assert len(slice_2018) == 31
    assert [row["province_index"] for row in slice_2018] == [str(i) for i in range(1, 32)]
    assert [row["province_name"] for row in slice_2018][11] == "安徽"
    assert all(row["investment_raw_100m_yuan"] == "" for row in slice_2018)
    assert all(row["depreciation_raw_100m_yuan"] == "" for row in slice_2018)


def test_track_a_and_b_recursion_identities():
    panel = rows("cleaned_province_year_panel.csv")
    by_key = {(row["province_name"], int(row["year"])): row for row in panel}
    for province in {row["province_name"] for row in panel}:
        base = by_key[(province, 2000)]
        assert math.isclose(float(base["track_a_capital_100m_yuan"]), float(base["investment_raw_100m_yuan"]) / 0.1, rel_tol=0, abs_tol=1e-10)
        assert math.isclose(float(base["track_b_capital_100m_yuan"]), float(base["investment_raw_100m_yuan"]) / 0.1, rel_tol=0, abs_tol=1e-10)
        for year in range(2001, 2019):
            prior = by_key[(province, year - 1)]
            current = by_key[(province, year)]
            ka_expected = 0.904 * float(prior["track_a_capital_100m_yuan"]) + float(prior["investment_raw_100m_yuan"])
            kb_expected = float(prior["track_b_capital_100m_yuan"]) + float(prior["investment_raw_100m_yuan"]) - float(prior["depreciation_raw_100m_yuan"])
            assert math.isclose(float(current["track_a_capital_100m_yuan"]), ka_expected, rel_tol=1e-14, abs_tol=1e-9)
            assert math.isclose(float(current["track_b_capital_100m_yuan"]), kb_expected, rel_tol=1e-14, abs_tol=1e-9)


def test_alpha_receipt_and_sample_contract():
    receipt = json.loads((REPORT_DIR / "alpha_estimation_receipt.json").read_text(encoding="utf-8"))
    assert receipt["sample_size"] == 310
    assert receipt["province_count"] == 31
    assert receipt["window"]["years"] == list(range(2009, 2019))
    assert receipt["missing_data_exclusions"] == []
    assert math.isclose(receipt["coefficients"]["alpha"], 0.7380939146868483, rel_tol=0, abs_tol=1e-14)
    assert receipt["authority_limit"] == "CALIBRATION_ONLY__NOT_MODEL_OR_RESULTS_AUTHORITY"


def test_alpha_recomputes_from_committed_panel():
    panel = rows("cleaned_province_year_panel.csv")
    sample = [row for row in panel if 2009 <= int(row["year"]) <= 2018]
    x = np.asarray([[1.0, int(row["year"]) - 2009,
                     math.log(float(row["track_a_capital_model_units_x1e7"]) / float(row["population_model_units_x100"]))]
                    for row in sample])
    y = np.asarray([math.log(float(row["gdp_model_units_x1000"]) / float(row["population_model_units_x100"]))
                    for row in sample])
    beta = np.linalg.lstsq(x, y, rcond=None)[0]
    receipt = json.loads((REPORT_DIR / "alpha_estimation_receipt.json").read_text(encoding="utf-8"))
    assert len(sample) == 310
    assert math.isclose(float(beta[2]), receipt["coefficients"]["alpha"], rel_tol=0, abs_tol=2e-14)


def test_same_year_zt_formula_and_positive_inputs():
    ledger = rows("corrected_2018_vs_matlab_ledger.csv")
    assert len(ledger) == 31
    alpha = float(ledger[0]["new_alpha"])
    for row in ledger:
        y = float(row["corrected_raw_nbs_gdp_2018_100m_yuan"]) * 1_000.0
        l = float(row["corrected_raw_nbs_population_2018_10k_persons"]) * 100.0
        ka = float(row["corrected_track_a_capital_2018_100m_yuan"]) * 10_000_000.0
        kb = float(row["corrected_track_b_capital_2018_100m_yuan"]) * 10_000_000.0
        assert min(y, l, ka, kb) > 0
        assert math.isclose(float(row["corrected_track_a_zt_2018"]), y / (ka**alpha * l ** (1-alpha)), rel_tol=1e-14)
        assert math.isclose(float(row["corrected_track_b_zt_2018"]), y / (kb**alpha * l ** (1-alpha)), rel_tol=1e-14)


def test_source_hashes_and_coverage_are_fail_closed():
    receipt = json.loads((REPORT_DIR / "source_hash_receipt.json").read_text(encoding="utf-8"))
    expected = {
        "gdp": "0EA17C78F60054ACCA26D0B56402977E560EE3FF4B220D666A5D0E98178F83E7",
        "investment": "4F3B880D7DD2DEB44DA5DF887088841AEF4C2EDDBD14C7F9806126138BE5CC78",
        "depreciation": "0ACBB29226E813A96CA029A26C07E954AAFE10E755F7EDD98102543F43DC062B",
        "population": "565B83873D56B8F9770F46BF897452B08A8850A3A954519643C1370188C09CAA",
    }
    assert {row["key"]: row["sha256"] for row in receipt["sources"]} == expected
    assert receipt["coverage"]["investment"]["observed_2018_count"] == 0
    assert receipt["coverage"]["depreciation"]["observed_2018_count"] == 0
    assert receipt["fully_same_year_2018_four_source_31_province_available"] is False
    assert receipt["canonical_workbook"]["hash_match"] is True


def test_report_answers_first_and_preserves_zero_model_boundary():
    text = DOC.read_text(encoding="utf-8")
    assert text.index("## Required answers") < text.index("## Verdict")
    assert "RAW_NBS_2018_REBUILD_PARTIAL__SOURCE_COVERAGE_OR_UNIT_AMBIGUITY" in text
    assert "MATLAB HANK=0" in text
    assert "HJB/KFE=0" in text
    assert "Results eligibility = FALSE" in text


def test_builder_has_no_model_entrypoint_imports():
    text = (ROOT / "validators" / "multi_province" / "raw_nbs_rebuild" / "build.py").read_text(encoding="utf-8")
    tree = ast.parse(text)
    imported = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")
    forbidden = ["ch5_two_asset_hank", "mphank", "hank3", "hjb", "kfe", "firm", "outer"]
    assert all(not any(token in module.lower() for token in forbidden) for module in imported)
