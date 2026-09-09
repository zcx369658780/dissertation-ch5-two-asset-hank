"""Synthetic arithmetic tests only; no scientific objects are assembled or solved."""

import ast
import importlib.util
from pathlib import Path
import sys
import unittest

import numpy as np
from scipy import sparse


HERE = Path(__file__).resolve().parents[1] / "validators/multi_province/call725_kfe_mass_balance"
sys.path.insert(0, str(HERE))
import ledger


class MassLedgerTests(unittest.TestCase):
    def test_f_order_pin_mapping(self):
        self.assertEqual(ledger.f_order_index(295, (20, 20, 2)), (15, 14, 0))

    def test_exact_row_replacement(self):
        q = sparse.csr_matrix([[-1.0, 1.0], [0.0, -2.0]])
        t = q.transpose().tocsr()
        b = t.tolil(copy=True)
        b[1, :] = 0.0
        b[1, 1] = 1.0
        b = b.tocsr()
        rhs = np.array([0.0, 0.007])
        result = ledger.verify_row_replacement(t, b, rhs, 1)
        self.assertEqual(result["changed_rows"], [1])
        with self.assertRaisesRegex(ValueError, "one-row"):
            ledger.verify_row_replacement(t, sparse.eye(2), rhs, 1)

    def test_raw_to_density_normalization_preserves_negative_value(self):
        raw = np.array([0.007, -1.0e-18, 0.003])
        factor, density, probability = ledger.normalize_raw(raw, 0.2)
        self.assertTrue(ledger.frozen_close(factor, 0.2 * np.sum(raw)))
        self.assertTrue(ledger.frozen_close(np.sum(probability), 1.0))
        self.assertLess(density[1], 0.0)

    def test_conservative_source_free_example(self):
        q = sparse.csr_matrix([[-1.0, 1.0], [1.0, -1.0]])
        result = ledger.build_mass_balance(q, np.array([0.5, 0.5]), 1.0, np.zeros(2), 0)
        self.assertTrue(np.array_equal(result["residual"], np.zeros(2)))
        self.assertEqual(result["escaped_mass_flow"], 0.0)
        self.assertEqual(result["candidate_pin_source"], 0.0)

    def test_nonconservative_example_keeps_off_pin_correction(self):
        q = sparse.csr_matrix([[-1.0, 1.0], [0.0, -2.0]])
        result = ledger.build_mass_balance(q, np.array([0.5, 0.5]), 1.0, np.array([0.0, 2.0]), 1)
        self.assertEqual(result["escaped_mass_flow"], 1.0)
        self.assertEqual(result["candidate_pin_source"], 0.5)
        self.assertEqual(result["off_pin_signed_correction"], -0.5)
        self.assertEqual(result["source_balance_rhs"], 0.5)

    def test_directional_corner_rates_are_added(self):
        mu_b = np.zeros((2, 2, 1))
        mu_a = np.zeros_like(mu_b)
        mu_b[-1, -1, 0] = 4.0
        mu_a[-1, -1, 0] = 6.0
        rates = ledger.directional_omitted_rates(mu_b, mu_a, 2.0, 3.0)
        self.assertEqual(rates["upper_b"][-1, -1, 0], 2.0)
        self.assertEqual(rates["upper_a"][-1, -1, 0], 2.0)
        self.assertEqual(rates["total"][-1, -1, 0], 4.0)

    def test_negative_probability_flux_is_not_clipped(self):
        parts = ledger.signed_parts(np.array([1.0, -1.0e-16]), np.array([2.0, 3.0]))
        self.assertEqual(parts["positive_probability"], 2.0)
        self.assertEqual(parts["negative_probability"], -3.0e-16)
        self.assertEqual(parts["total"], 2.0 - 3.0e-16)

    def test_sparse_orientation_mismatch_is_rejected(self):
        q = sparse.csr_matrix([[-1.0, 1.0], [0.0, -2.0]])
        self.assertTrue(ledger.require_transpose(q, q.transpose().tocsr()))
        with self.assertRaisesRegex(ValueError, "Q.T"):
            ledger.require_transpose(q, q)

    def test_frozen_rule_is_fixed(self):
        self.assertTrue(ledger.frozen_close(1.0, 1.0 + 100 * np.finfo(float).eps))
        self.assertFalse(ledger.frozen_close(1.0, 1.0 + 256 * np.finfo(float).eps))

    def test_imports_contain_no_solver_or_scientific_entry(self):
        for name in ("ledger.py", "evidence.py", "analyze.py"):
            source = (HERE / name).read_text(encoding="utf-8")
            tree = ast.parse(source)
            imported = {
                alias.name
                for node in ast.walk(tree)
                if isinstance(node, (ast.Import, ast.ImportFrom))
                for alias in node.names
            }
            self.assertFalse({"linalg", "spsolve", "eig", "eigs"} & imported)
        spec = importlib.util.spec_from_file_location("ledger_clean_import", HERE / "ledger.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertFalse(hasattr(module, "solve"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
