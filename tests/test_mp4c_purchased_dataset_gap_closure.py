"""Synthetic tests only; importing this test cannot read purchased data or run science."""

import sys
import unittest
from pathlib import Path


MODULE_DIR = Path(__file__).resolve().parents[1] / "validators" / "multi_province" / "purchased_dataset_gap_closure"
sys.path.insert(0, str(MODULE_DIR))
from core import CITY_SUM_REQUIREMENTS, city_sum_is_authorized, classify_secondary_value, excel_column, stable_complete_panel


class PurchasedDatasetGapClosureTests(unittest.TestCase):
    def test_excel_column_for_population_cell(self):
        self.assertEqual(excel_column(31), "AE")

    def test_city_sum_requires_all_six_gates(self):
        gates = {name: True for name in CITY_SUM_REQUIREMENTS}
        self.assertTrue(city_sum_is_authorized(gates))
        gates["no_province_residual_omitted"] = False
        self.assertFalse(city_sum_is_authorized(gates))

    def test_missing_gate_fails_closed(self):
        gates = {name: True for name in CITY_SUM_REQUIREMENTS[:-1]}
        self.assertFalse(city_sum_is_authorized(gates))

    def test_revised_official_vintage_is_distinct(self):
        status = classify_secondary_value(
            6076.0,
            provisional=6076.0,
            preliminary_official=6323.6,
            traceable_official=True,
            revised_vintage=True,
        )
        self.assertEqual(status, "SECONDARY_SUPPORTS_REVISED_OFFICIAL_VINTAGE")

    def test_agreement_alone_does_not_claim_authority(self):
        status = classify_secondary_value(6076.0, provisional=6076.0, preliminary_official=6323.6)
        self.assertEqual(status, "SECONDARY_MATCHES_PROVISIONAL")

    def test_stable_panel_requires_identical_nonempty_city_sets(self):
        panel = {2009: {"A", "B"}, 2010: {"A", "B"}, 2011: {"A", "B"}}
        self.assertTrue(stable_complete_panel(panel, range(2009, 2012)))
        panel[2011] = {"A"}
        self.assertFalse(stable_complete_panel(panel, range(2009, 2012)))

    def test_import_surface_has_no_scientific_entry_point(self):
        import core

        names = {name.lower() for name in core.__dict__}
        for forbidden in ("solve", "brentq", "eig", "hjb", "kfe", "matlab"):
            self.assertNotIn(forbidden, names)


if __name__ == "__main__":
    unittest.main(verbosity=2)
