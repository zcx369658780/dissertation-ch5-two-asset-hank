"""Synthetic diagnostics only: no saved state evaluation or solver."""
import ast
from decimal import Decimal
import importlib.util
from pathlib import Path
import sys
import unittest
import numpy as np
from scipy.sparse import csr_matrix

ROOT = Path(__file__).resolve().parents[1]
NEW = ROOT / 'validators/multi_province/call725_boundary_generator_repair_spec'
sys.path.insert(0, str(NEW))
spec = importlib.util.spec_from_file_location('boundary_diagnostics', NEW / 'analyze.py')
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)


class Diagnostics(unittest.TestCase):
    def test_f_order_association(self):
        x = np.arange(800).reshape((20, 20, 2), order='F')
        self.assertEqual(d.coord(704), (4, 15, 1))
        self.assertEqual(d.coord(799), (19, 19, 1))
        np.testing.assert_array_equal(d.vec(x), np.arange(800))

    def test_exact_snapshot_scope(self):
        from common import snapshots
        rows = snapshots()
        self.assertEqual(len(rows), 14)
        self.assertEqual(len({r['path'] for r in rows}), 14)
        self.assertEqual([r['id'] for r in rows[8:]], [
            'matlab_trajectory_52', 'matlab_trajectory_57',
            'python_trajectory_146', 'python_trajectory_401',
            'python_trajectory_424', 'python_trajectory_500'])

    def test_closed_generator_maximum_principle(self):
        q = np.array([[-2., 2., 0.], [1., -4., 3.], [0., 5., -5.]])
        x = np.array([0., 1., 2.])
        np.testing.assert_array_equal(q.sum(axis=1), 0)
        self.assertGreaterEqual((q @ x)[0], 0)
        self.assertLessEqual((q @ x)[-1], 0)

    def test_net_inward_does_not_certify_rates(self):
        # Upper coordinate 2: negative rate to 1, positive rate to 0.
        rates = np.array([2., -1.])
        drift = rates @ (np.array([0., 1.]) - 2.)
        self.assertLess(drift, 0)
        self.assertTrue(np.any(rates < 0))

    def test_omitted_edge_contaminates_other_coordinate(self):
        q = csr_matrix(([-3., 1.], ([0, 0], [0, 1])), shape=(800, 800))
        a = np.full(800, 7.)
        action, centered, sums = d.reductions(q, a)
        self.assertEqual(centered[0], 0)
        self.assertEqual(sums[0], -2)
        self.assertEqual(action[0], -14)

    def test_joint_corner_feasibility(self):
        z = np.zeros((20, 20, 2)); b = z.copy(); a = z.copy()
        b[19, 19, 0] = -2; a[19, 19, 0] = .81
        bb, aa, violation = d.face_incompatibility(z, z, b, a)
        self.assertFalse(bb[19, 19, 0])
        self.assertTrue(aa[19, 19, 0])
        self.assertEqual(violation[19, 19, 0], .81)
        self.assertEqual(violation[0, 0, 0], 0)

    def test_synthetic_budget_and_decomposition(self):
        shape = (20, 20, 2); ones = np.ones(shape); zeros = np.zeros(shape)
        v = dict(b=np.arange(20.), a=np.arange(20.), z=np.array([1., 2.]),
                 labor=ones, consumption=ones, transfer=zeros, adjustment_cost=zeros,
                 effective_illiquid_return=zeros, A=csr_matrix((800, 800)),
                 bb=zeros, bf=zeros, ab=zeros, af=zeros,
                 mu_b=np.broadcast_to(np.array([0., 1.]), shape), mu_a=zeros)
        p = dict(tau=0., wage=1., r_b=0., borrowing_rate_gap=0., transfer_income=0.)
        r = d.snapshot(v, p)
        np.testing.assert_array_equal(r['budget_b'], r['captured_b'])
        np.testing.assert_array_equal(r['budget_a'], r['captured_a'])
        np.testing.assert_array_equal(r['decomposition_residual_b'], 0)

    def test_decimal_preserves_stored_cancellation(self):
        q = csr_matrix(([1e20, 1., -1e20], ([0, 0, 0], [0, 1, 2])), shape=(800, 800))
        x = np.ones(800)
        r = d.decimal_row(q, 0, x, x)
        self.assertEqual(Decimal(r['row_sum']), Decimal(1))
        self.assertEqual(Decimal(r['a_centered']), Decimal(0))
        self.assertEqual(d.reductions(q, x)[2][0], 1)

    def test_unchanged_128_eps_rule(self):
        eps = np.finfo(float).eps
        self.assertFalse(d.materially_different(0., 128 * eps))
        self.assertTrue(d.materially_different(0., 129 * eps))

    def test_local_branch_is_accepted_expression_copy(self):
        old = ast.parse((ROOT / 'validators/multi_province/call725_policy_operator_stability/diagnose.py').read_text())
        new = ast.parse((NEW / 'legacy.py').read_text())
        a = next(n for n in old.body if isinstance(n, ast.FunctionDef) and n.name == 'branch')
        b = next(n for n in new.body if isinstance(n, ast.FunctionDef) and n.name == 'branch')
        # Only the explicit binding locator changes; semicolons are separate AST statements.
        for node in ast.walk(a):
            if isinstance(node, ast.Name) and node.id == 'BINDING':
                node.id = 'binding_path'
        self.assertEqual(ast.dump(ast.Module(body=a.body, type_ignores=[])),
                         ast.dump(ast.Module(body=b.body, type_ignores=[])))


if __name__ == '__main__':
    unittest.main(verbosity=2)
