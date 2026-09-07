"""Synthetic arithmetic and mocked solver boundaries; zero scientific solves."""
import ast
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import numpy as np
from scipy import sparse
from scipy.io import loadmat,savemat
HERE=Path(__file__).resolve().parents[1]/'validators/multi_province/call725_frozen_linear_system'
sys.path.insert(0,str(HERE))
import common
import python_solve
import analyze

class FrozenTests(unittest.TestCase):
    def test_duplicate_rejected(self):
        M=sparse.coo_matrix(([1.,2.],([0,0],[1,1])),shape=(800,800))
        with self.assertRaisesRegex(ValueError,'duplicate'):common.canonical(M)
    def test_exact_zeros_only(self):
        M=sparse.coo_matrix(([0.,-0.,1e-100],([0,1,2],[1,2,3])),shape=(800,800))
        r,c,d,receipt=common.canonical(M)
        self.assertEqual(d.tolist(),[1e-100]);self.assertEqual(receipt['stored_negative_zeros'],1)
    def test_scaling_rule_and_reverse(self):
        diag=np.ones(800);diag[:4]=[0,1,8,1e20]
        M=sparse.diags(diag,format='csr');b=np.arange(800,dtype=float)
        S,sb,k,r=common.scaled_payload(M,b)
        self.assertEqual(k[:3].tolist(),[0,0,-3]);self.assertTrue(r['exact_reverse_bits'])
        self.assertTrue(np.array_equal(common.bits(np.ldexp(sb,-k)),common.bits(b)))
        self.assertEqual(r['zero_rows'],[0])
    def test_exact_roundtrip_detects_one_ulp(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'a.mat';M=sparse.eye(800,format='csr');b=np.arange(800,dtype=float)
            b[0]=-0.;common.save_payload(path,M,b,np.zeros(800,dtype=int))
            _,loaded,_=common.load_payload(path);self.assertTrue(np.array_equal(common.bits(b),common.bits(loaded)))
            m=loadmat(path);m['rhs'][1,0]=np.nextafter(m['rhs'][1,0],np.inf);savemat(path,{k:v for k,v in m.items() if not k.startswith('__')})
            with self.assertRaises(AssertionError):common.load_payload(path)
    def test_mocked_one_solve_and_persistence(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);path=root/'input.mat';common.save_payload(path,sparse.eye(800,format='csr'),np.ones(800),np.zeros(800,dtype=int))
            with patch.object(python_solve.linalg,'spsolve',return_value=np.ones(800)) as solver:
                python_solve.main(path,root/'out');solver.assert_called_once()
                self.assertEqual(solver.call_args.args[0].format,'csr')
            ledger=common.read(root/'out/ledger.json');self.assertEqual(ledger['solves_entered'],1);self.assertEqual(ledger['durable_outputs'],1)
            self.assertTrue((root/'out/loaded_receipt.json').exists())
    def test_invalid_binding_never_enters_solver(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);path=root/'input.mat';common.save_payload(path,sparse.eye(800,format='csr'),np.ones(800),np.zeros(800,dtype=int))
            m=loadmat(path);m['ref_rhs_bits'][0,0]=0;savemat(path,{k:v for k,v in m.items() if not k.startswith('__')})
            with patch.object(python_solve.linalg,'spsolve') as solver:
                with self.assertRaises(AssertionError):python_solve.main(path,root/'out')
                solver.assert_not_called()
            self.assertEqual(common.read(root/'out/ledger.json')['solves_entered'],0)
    def test_single_solver_entrypoint(self):
        tree=ast.parse((HERE/'python_solve.py').read_text(encoding='utf-8'))
        calls=[ast.unparse(n.func) for n in ast.walk(tree) if isinstance(n,ast.Call)]
        self.assertEqual(calls.count('linalg.spsolve'),1)
        text=(HERE/'matlab_solve.m').read_text(encoding='utf-8');self.assertEqual(text.count('x=M\\rhs;'),1)
        self.assertLess(text.index('loaded_receipt.json'),text.index('x=M\\rhs;'))
    def test_residual_cancellation_three_arithmetics(self):
        M=sparse.csr_matrix([[1e16,1.,-1e16]])
        result,_=analyze.residual(M,np.array([0.]),np.ones(3))
        self.assertEqual(result['binary64']['residual_inf'],0.)
        self.assertEqual(result['compensated_rounded_products']['residual_inf'],1.)
        self.assertEqual(float(result['decimal80']['residual_inf']),1.)
    def test_decimal_products_not_fsum_of_rounded_products(self):
        a=1.+2.**-52; b=1.+2.**-51
        M=sparse.csr_matrix([[a,-b]])
        result,_=analyze.residual(M,np.array([0.]),np.array([a,1.]))
        self.assertEqual(result['compensated_rounded_products']['residual_inf'],0.)
        self.assertEqual(float(result['decimal80']['residual_inf']),2.**-104)
    def test_zero_denominator_convention(self):
        from decimal import Decimal
        self.assertEqual(analyze.ratio(Decimal(0),Decimal(0)),0)
        self.assertTrue(analyze.ratio(Decimal(1),Decimal(0)).is_infinite())
        result,_=analyze.residual(sparse.csr_matrix((1,1)),np.zeros(1),np.zeros(1))
        self.assertEqual(result['binary64']['normwise_backward_error'],0.)
        self.assertEqual(result['decimal80']['componentwise_backward_error'],'0')
    def test_no_analysis_solvers(self):
        tree=ast.parse((HERE/'analyze.py').read_text(encoding='utf-8'))
        calls=[ast.unparse(n.func) for n in ast.walk(tree) if isinstance(n,ast.Call)]
        self.assertFalse(any(any(s in name for s in ('spsolve','inv','svd','eig','factorized')) for name in calls))
if __name__=='__main__':unittest.main()
