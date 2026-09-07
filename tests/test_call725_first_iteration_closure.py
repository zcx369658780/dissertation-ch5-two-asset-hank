"""Synthetic comparator invariants only; no production imports or model calls."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

import numpy as np
from scipy import sparse

SOURCE = Path(__file__).resolve().parents[1] / "validators/multi_province/call725_first_iteration_closure/compare.py"
SPEC = importlib.util.spec_from_file_location("call725_compare", SOURCE)
comparator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(comparator)


class ComparatorTests(unittest.TestCase):
    def test_shape_mismatch_is_not_flattened_away(self):
        result = comparator.compare_dense(np.zeros((2, 3)), np.zeros((3, 2)), (2, 3))
        self.assertFalse(result["passed"])

    def test_nonfinite_never_passes(self):
        for value in (np.nan, np.inf, -np.inf):
            self.assertFalse(comparator.compare_dense([value], [value], (1,))["passed"])

    def test_continuous_fixed_rule_and_exact_categories(self):
        bound = comparator.EPS_SCALE
        self.assertTrue(comparator.compare_dense([0.0], [bound], (1,))["passed"])
        self.assertFalse(comparator.compare_dense([0.0], [2 * bound], (1,))["passed"])
        self.assertFalse(comparator.compare_dense([0.0], [bound], (1,), exact=True)["passed"])

    def test_large_signed_values_use_relative_scale(self):
        for value in (1e10, -1e10):
            self.assertTrue(comparator.compare_dense([value], [value + 1e-4], (1,))["passed"])
            self.assertFalse(comparator.compare_dense([value], [value + 1e-3], (1,))["passed"])

    def test_sparse_exact_stored_zero_is_ignored(self):
        left = sparse.coo_matrix(([1., -0.], ([0, 1], [0, 1])), shape=(2, 2))
        right = sparse.coo_matrix(([1.], ([0], [0])), shape=(2, 2))
        self.assertTrue(comparator.compare_sparse(left, right, (2, 2))["passed"])

    def test_tiny_support_difference_still_fails(self):
        left = sparse.coo_matrix(([1e-100], ([0], [1])), shape=(2, 2))
        result = comparator.compare_sparse(left, sparse.csr_matrix((2, 2)), (2, 2))
        self.assertEqual(result["material_mismatch_count"], 0)
        self.assertEqual(result["support_mismatch_count"], 1)
        self.assertFalse(result["passed"])

    def test_sparse_coordinate_order_and_duplicates(self):
        left = sparse.coo_matrix(([2., 1., -1.], ([1, 0, 1], [0, 1, 0])), shape=(2, 2))
        right = sparse.coo_matrix(([1., 1.], ([0, 1], [1, 0])), shape=(2, 2))
        self.assertTrue(comparator.compare_sparse(left, right, (2, 2))["passed"])

    def test_sparse_nonfinite_and_shape_rejected(self):
        bad = sparse.csr_matrix([[np.nan]])
        self.assertFalse(comparator.compare_sparse(bad, bad, (1, 1))["passed"])
        self.assertFalse(comparator.compare_sparse(sparse.eye(2), sparse.eye(3), (2, 2))["passed"])

    def test_labels_are_validated(self):
        np.testing.assert_array_equal(comparator.labels(np.array(["B", "0", "F"])), [-1, 0, 1])
        with self.assertRaises(ValueError):
            comparator.labels(np.array(["X"]))

    def test_vector_normalization_rejects_tensor(self):
        np.testing.assert_array_equal(comparator.vector(np.array([[1., 2.]]), 2), [1., 2.])
        with self.assertRaises(ValueError):
            comparator.vector(np.zeros((2, 2)), 4)

    def test_residual_uses_f_order_without_solve(self):
        tensor = np.array([[1., 3.], [2., 4.]])
        matrix = sparse.diags([1., 2., 3., 4.])
        result = comparator.residual(matrix, np.array([1., 4., 9., 16.]), tensor)
        self.assertEqual(result["residual_inf"], 0.)
        self.assertEqual(result["normwise_backward_error"], 0.)
        self.assertEqual(result["backward_error_scale"], 32.)

    def test_residual_overflow_cannot_pass(self):
        result = comparator.residual(sparse.diags([1e308]), np.array([0.]), np.array([1e308]))
        self.assertFalse(result["passed"])
        self.assertFalse(result["finite"])

    def test_missing_required_objects_fail_closed(self):
        for field in ("old", "M", "raw_va_f"):
            with self.assertRaisesRegex(comparator.EvidenceIncomplete, field):
                comparator.require_fields({}, [field], "fixture")

    def test_manifest_output_readback_detects_corruption(self):
        with tempfile.TemporaryDirectory(dir=SOURCE.parent, prefix="io_test_") as temporary:
            root = Path(temporary)
            payload = root / "summary.json"
            comparator.write_json(payload, {"passed": True})
            manifest = root / "manifest.json"
            comparator.write_json(manifest, {"outputs": [{"path": str(payload), "sha256": comparator.digest(payload), "bytes": payload.stat().st_size}]})
            comparator.verify_manifest_outputs(manifest)
            payload.write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "readback mismatch"):
                comparator.verify_manifest_outputs(manifest)

    def test_incomplete_and_mismatch_cannot_pass(self):
        self.assertEqual(comparator.outcome([{"available": False, "passed": False}]), "FIRST_ITERATION_EVIDENCE_INCOMPLETE")
        self.assertEqual(comparator.outcome([{"available": True, "passed": False}]), "FIRST_ITERATION_MATERIAL_MISMATCH")


if __name__ == "__main__":
    unittest.main(verbosity=2)
