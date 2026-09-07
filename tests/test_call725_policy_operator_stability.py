"""Focused task-only instrumentation and solve-free diagnostic tests."""
import ast
import importlib.util
from pathlib import Path
import sys
import unittest
import numpy as np
from scipy import sparse
HERE=Path(__file__).resolve().parents[1]/'validators/multi_province/call725_policy_operator_stability'
sys.path.insert(0,str(HERE))
import common
import diagnose

class StabilityTests(unittest.TestCase):
    def test_unchanged_scientific_bodies(self):
        for name in ('python_trajectory.py','matlab_trajectory.m'):
            old=(common.PRE/name).read_text(encoding='utf-8')
            expected=old.replace('1 <= max_updates <= 500','max_updates == 1').replace('max_updates<1 || max_updates>500','max_updates~=1')
            self.assertEqual((HERE/name).read_text(encoding='utf-8'),expected)
    def test_launch_binding(self):
        text=(HERE/'launch.py').read_text(encoding='utf-8'); ast.parse(text)
        self.assertIn('limit=1',text); self.assertIn('timeout=900',text)
        self.assertNotIn("choices=['trajectory','replay']",text)
        self.assertIn("[args.kind]['sha256']",text)
    def test_fixed_case_fields(self):
        self.assertEqual(common.CASES['P32'],('python',32,'old'))
        self.assertEqual(common.CASES['M143_FINAL'],('matlab',143,'updated'))
    def test_sparse_exact_support(self):
        a=sparse.eye(800,format='csr'); b=a.copy().tolil(); b[0,1]=1e-30
        result=common.analysis.sparse_compare(a,b.tocsr())
        self.assertFalse(result['passed']); self.assertEqual(result['support_mismatch_count'],1)

    def test_generator_signed_entries_and_leakage(self):
        A=sparse.lil_matrix((800,800)); A[0,0]=-2.; A[0,1]=2.; A[1,0]=-1.; A[1,1]=1.; A[19,19]=-3.
        v={'A':A.tocsr(),'M':.051*sparse.eye(800)-A.tocsr(),**{name:np.zeros((20,20,2)) for name in ('bb','bf','ab','af')}}
        v['bf'][19,0,0]=3.
        r=diagnose.generator(v)
        self.assertEqual(r['negative_offdiag_count'],1)
        self.assertEqual(r['offdiag_min_coordinate'],[1,0])
        self.assertEqual(r['nonzero_leak_cells'],1)
        self.assertEqual(r['row_sum_plus_outward_max_abs'],0.)
        self.assertAlmostEqual(r['M_diagonal_dominance_margin']['min'],-.051)

    def test_f_order_coordinate(self):
        self.assertEqual(diagnose.coord(385),[5,19,0])
        self.assertEqual(diagnose.coord(704),[4,15,1])

    def test_diagnostics_do_not_evaluate_or_solve(self):
        tree=ast.parse((HERE/'diagnose.py').read_text(encoding='utf-8'))
        calls=[ast.unparse(n.func) for n in ast.walk(tree) if isinstance(n,ast.Call)]
        self.assertFalse(any('solve' in name or 'select_matlab_faithful' in name for name in calls))

    def test_reconstruction_at_upper_a(self):
        v={k:np.zeros((20,20,2)) for k in ('post_boundary_vb_b','post_boundary_vb_f','va_b','va_f','liquid_label','transfer_label','consumption','labor','transfer','adjustment_cost','bb','bf','ab','af','effective_illiquid_return')}
        v.update(b=np.linspace(-2,5,20),a=np.linspace(0,10,20),z=np.array([.8,1.3]))
        idx=(5,19,0)
        v['post_boundary_vb_b'][idx]=1.; v['post_boundary_vb_f'][idx]=1.;v['va_b'][idx]=.8
        r=diagnose.branch(v,np.array(idx,dtype=np.int64))
        import json
        json.dumps(r,allow_nan=False)
        self.assertAlmostEqual(r['candidates']['FB']['candidate'],-.5)
        self.assertEqual(r['reconstructed_transfer_label'],1)
        self.assertFalse(r['transfer_denominator_clamped'])

if __name__=='__main__': unittest.main()
