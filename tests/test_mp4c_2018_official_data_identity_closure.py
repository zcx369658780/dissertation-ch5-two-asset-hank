"""Synthetic/static tests only; importing this test cannot invoke a model or solver."""

import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_DIR = Path(__file__).resolve().parents[1] / "validators" / "multi_province" / "official_data_identity_closure"
sys.path.insert(0, str(MODULE_DIR))
from core import frozen_capital_recurrence, investment_years_for_stock, relative_difference, transformed_value


class OfficialIdentityClosureTests(unittest.TestCase):
    def test_k2018_uses_investment_through_2017(self):
        years = investment_years_for_stock(2018)
        self.assertEqual(years[0], 2000)
        self.assertEqual(years[-1], 2017)
        self.assertEqual(len(years), 18)
        self.assertNotIn(2018, years)

    def test_frozen_recurrence_timing(self):
        capital = frozen_capital_recurrence([10.0, 20.0, 30.0])
        self.assertEqual(capital[0], 100.0)
        self.assertEqual(capital[1], 100.4)
        self.assertAlmostEqual(capital[2], 110.7616)

    def test_frozen_unit_conversions(self):
        self.assertEqual(transformed_value("GDP", 34010.91), 34010910.0)
        self.assertEqual(transformed_value("POP", 6076), 607600.0)
        self.assertEqual(transformed_value("CAP", 1357314108.2013683), 1357314108201.3684)

    def test_relative_difference(self):
        self.assertAlmostEqual(relative_difference(34010.91, 30006.82), (34010.91 - 30006.82) / 30006.82)
        self.assertIsNone(relative_difference(1.0, 0.0))

    def test_import_surface_has_no_scientific_entry_point(self):
        spec = importlib.util.spec_from_file_location("official_closure_core", MODULE_DIR / "core.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        names = set(module.__dict__)
        for forbidden in ("solve", "brentq", "eig", "hjb", "kfe", "matlab"):
            self.assertNotIn(forbidden, names)


if __name__ == "__main__":
    unittest.main(verbosity=2)
