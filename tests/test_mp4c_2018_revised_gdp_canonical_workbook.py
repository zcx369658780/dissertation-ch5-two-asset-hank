"""Static/synthetic checks only; no Chapter 5 model entry point is imported."""

import json
import sys
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
MODULE_DIR = REPO / "validators" / "multi_province" / "canonical_workbook"
REPORT_DIR = REPO / "reports" / "mp4c_2018_revised_gdp_canonical_workbook_20260909"
sys.path.insert(0, str(MODULE_DIR))

from core import (
    REQUIRED_SHEETS,
    matches_at_published_precision,
    pim_path,
    required_sheets_present,
    same_year_zt,
)


class CanonicalWorkbookTests(unittest.TestCase):
    def test_official_precision_match_is_explicit(self):
        self.assertTrue(matches_at_published_precision(34010.91, 34010.9, 1))
        self.assertFalse(matches_at_published_precision(34010.91, 34010.8, 1))

    def test_precision_comparison_rejects_invalid_values(self):
        with self.assertRaises(ValueError):
            matches_at_published_precision(float("nan"), 34010.9, 1)
        with self.assertRaises(ValueError):
            matches_at_published_precision(34010.91, 34010.9, -1)

    def test_pim_uses_previous_year_flow(self):
        path = pim_path([10.0, 20.0])
        self.assertEqual(path[0], 100.0)
        self.assertEqual(path[1], 100.4)
        self.assertAlmostEqual(path[2], 110.7616)

    def test_same_year_zt_matches_frozen_formula(self):
        observed = same_year_zt(34_010_900.0, 1_357_314_108_201.3684, 607_600.0, 0.772866243094144)
        self.assertAlmostEqual(observed, 0.0006934644495858679, places=18)

    def test_same_year_zt_fails_closed_on_nonpositive_capital(self):
        with self.assertRaises(ValueError):
            same_year_zt(1.0, 0.0, 1.0, 0.5)

    def test_required_sheet_contract_is_exact(self):
        self.assertTrue(required_sheets_present(REQUIRED_SHEETS))
        self.assertFalse(required_sheets_present(REQUIRED_SHEETS[:-1]))

    def test_receipts_preserve_authority_limits(self):
        receipt = json.loads((REPORT_DIR / "anhui_2018_final_input_receipt.json").read_text(encoding="utf-8"))
        self.assertEqual(receipt["gdp_identity_status"], "REVISED_GDP_MATCHES_CURRENT_PROVISIONAL")
        self.assertEqual(receipt["accepted_revised_gdp_亿元"], 34010.9)
        self.assertFalse(receipt["Results_eligible"])
        self.assertEqual(receipt["scientific_calls"], 0)

    def test_import_surface_has_no_scientific_entry_point(self):
        import core

        names = {name.lower() for name in core.__dict__}
        for forbidden in ("solve", "brentq", "eig", "hjb", "kfe", "matlab"):
            self.assertNotIn(forbidden, names)


if __name__ == "__main__":
    unittest.main(verbosity=2)
