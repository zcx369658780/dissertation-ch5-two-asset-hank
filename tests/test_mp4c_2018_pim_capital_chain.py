"""Synthetic tests only; no protected workbook or scientific entry point is used."""

import sys
import unittest
from pathlib import Path


MODULE_DIR = Path(__file__).resolve().parents[1] / "validators" / "multi_province" / "pim_capital_chain"
sys.path.insert(0, str(MODULE_DIR))

from core import binary64_equal, direction, first_binary64_divergence, pim_path


class PimCapitalChainTests(unittest.TestCase):
    def test_source_timing_uses_previous_flow(self):
        # K2000=10/.1; K2001=.904*K2000+I2000; K2002 uses I2001.
        path = pim_path([10.0, 20.0])
        self.assertEqual(path[0], 100.0)
        self.assertEqual(path[1], 100.4)
        self.assertAlmostEqual(path[2], 110.7616)

    def test_last_flow_builds_next_year_capital(self):
        self.assertEqual(len(pim_path([10.0, 20.0, 30.0])), 4)

    def test_binary64_identity_is_bitwise(self):
        self.assertTrue(binary64_equal(1.0, 1.0))
        self.assertFalse(binary64_equal(0.0, -0.0))

    def test_first_divergence(self):
        self.assertIsNone(first_binary64_divergence([1.0, 2.0], [1.0, 2.0], [2000, 2001]))
        self.assertEqual(first_binary64_divergence([1.0, 2.0], [1.0, 3.0], [2000, 2001]), 2001)

    def test_direction(self):
        self.assertEqual(direction(2.0, 1.0), "UP")
        self.assertEqual(direction(1.0, 2.0), "DOWN")
        self.assertEqual(direction(1.0, 1.0), "FLAT")

    def test_invalid_sequences_fail_closed(self):
        with self.assertRaises(ValueError):
            pim_path([])
        with self.assertRaises(ValueError):
            pim_path([float("nan")])

    def test_import_surface_has_no_scientific_entry_point(self):
        import core

        names = {name.lower() for name in core.__dict__}
        for forbidden in ("solve", "brentq", "eig", "hjb", "kfe", "matlab"):
            self.assertNotIn(forbidden, names)


if __name__ == "__main__":
    unittest.main(verbosity=2)
