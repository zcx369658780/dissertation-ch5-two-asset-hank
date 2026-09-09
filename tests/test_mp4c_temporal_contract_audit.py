"""Synthetic-only temporal contract tests; no scientific inputs or solves."""
import importlib.util
import sys
import unittest
from pathlib import Path

DIR = Path(__file__).resolve().parents[1] / "validators/multi_province/temporal_contract_audit"
sys.path.insert(0, str(DIR))
from contract import annual_mapping, classify_time_labels, expected_plm_sheets, zt_from_levels


class TemporalContractTests(unittest.TestCase):
    def test_ii_1_contract(self):
        row = annual_mapping(1)
        self.assertEqual((row["steady_year"], row["plm_vintage"]), (2009, 10))
        self.assertEqual((row["current_level_year"], row["candidate_level_row_1based"]), (2000, 10))

    def test_ii_10_contract(self):
        row = annual_mapping(10)
        self.assertEqual((row["steady_year"], row["plm_vintage"]), (2018, 19))
        self.assertEqual((row["current_level_year"], row["candidate_level_year"]), (2009, 2018))
        self.assertEqual((row["current_zt_year"], row["candidate_zt_row_1based"]), (2020, 19))

    def test_plm_sheet_contract(self):
        sheets = expected_plm_sheets(10)
        self.assertEqual(len(sheets), 8)
        self.assertIn("总面板回归系数_19_行业4", sheets)

    def test_fixed_window_layout_classification(self):
        labels = ["Coefficient", *(f"time{i}" for i in range(1, 10)), "log(pcap)"]
        self.assertEqual(classify_time_labels(labels), "FIXED_TEN_PERIOD_WINDOW_EVIDENCE")

    def test_static_zt_arithmetic(self):
        self.assertAlmostEqual(zt_from_levels(100.0, 25.0, 4.0, 0.5), 10.0)
        with self.assertRaises(ValueError):
            zt_from_levels(100.0, -25.0, 10.0, 0.5)

    def test_import_time_zero_science(self):
        spec = importlib.util.spec_from_file_location("temporal_contract", DIR / "contract.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for forbidden in ("matlab", "solve", "brentq", "spsolve", "eig"):
            self.assertNotIn(forbidden, module.__dict__)


if __name__ == "__main__":
    unittest.main(verbosity=2)
