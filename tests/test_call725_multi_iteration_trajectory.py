"""Static source preservation and synthetic IO only; no scientific imports."""
import ast
import importlib.util
import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.io import loadmat, savemat

REPO=Path(__file__).resolve().parents[1]
HERE=REPO/'validators/multi_province/call725_multi_iteration_trajectory'
PRE=Path(r'D:\ProjectTemp\ch5-mp4c-2018-call725-postcall-residual-vectorization-repair-20260904-001')


class CaptureTests(unittest.TestCase):
    def test_sparse_comparison_never_densifies_and_preserves_tiny_support(self):
        spec=importlib.util.spec_from_file_location('trajectory_analyze',HERE/'analyze.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        left=sparse.csr_matrix(([1e-100],([0],[1])),shape=(800,800))
        with patch.object(sparse.csr_matrix,'toarray',side_effect=AssertionError('dense expansion')):
            result=module.sparse_compare(left,sparse.csr_matrix((800,800)))
        self.assertFalse(result['passed']);self.assertEqual(result['support_mismatch_count'],1)
        with self.assertRaises(ValueError):module.validate_steps([Path('step_0001.mat'),Path('step_0003.mat')])
        self.assertEqual(len(module.validate_steps([Path('step_0001.mat'),Path('step_0002.mat')])),2)

    def test_python_scientific_body_preserved(self):
        original=(PRE/'python_postcall_vectorized_stagewise_wrapper.py').read_text(encoding='utf-8')
        current=(HERE/'python_trajectory.py').read_text(encoding='utf-8')
        begin=original.index(' shape=old.shape')
        segment=original[begin:original.index(' np.savez_compressed(out,old=old',begin)]
        actual=current[current.index('   shape=old.shape'):current.index('   np.savez_compressed(out,old=old')]
        actual=actual.replace("; ledger['solves_entered']+=1; persist()",'')
        self.assertEqual([l.strip() for l in segment.splitlines()],[l.strip() for l in actual.splitlines()])

    def test_matlab_scientific_body_preserved(self):
        original=(PRE/'matlab_postcall_vectorized_stagewise_wrapper.m').read_text(encoding='utf-8')
        current=(HERE/'matlab_trajectory.m').read_text(encoding='utf-8')
        start='    VbF=zeros';end='    save(output_path'
        expected=original[original.index(start):original.index(end)]
        actual=current[current.index(start):current.index(end)]
        actual=actual.replace('ledger.solves_entered=ledger.solves_entered+1; write_ledger(output_dir,ledger); ','')
        self.assertEqual(actual,expected)

    def test_state_carry_and_stop(self):
        py=(HERE/'python_trajectory.py').read_text(encoding='utf-8')
        matlab=(HERE/'matlab_trajectory.m').read_text(encoding='utf-8')
        self.assertIn('old=v1.copy()',py)
        self.assertIn('V=v; initial_value=V;',matlab)
        self.assertIn("statistic<n.convergence_tolerance",py)
        self.assertIn('dist<n.convergence_tolerance',matlab)
        self.assertNotIn('BB_post',matlab)
        self.assertNotIn('solve_matlab_faithful_hjb(',py)
        self.assertLess(py.index('np.savez_compressed(out,old=old'),py.index('v1_vec=v1.reshape'))
        self.assertLess(matlab.index("save(output_path,'initial_value'"),matlab.index('updated_vec=updated(:)'))

    def test_python_parse_and_trace_newline(self):
        tree=ast.parse((HERE/'python_trajectory.py').read_text(encoding='utf-8'))
        constants=[n.value for n in ast.walk(tree) if isinstance(n,ast.Constant) and isinstance(n.value,str)]
        self.assertIn('\n',constants)
        self.assertNotIn('\\n',constants)

    def test_exact_state_and_sparse_roundtrip(self):
        with tempfile.TemporaryDirectory(dir=HERE,prefix='synthetic_') as temp:
            temp=Path(temp); value=np.arange(800,dtype=float).reshape((20,20,2),order='F')
            state={'v0':value,'l0':np.ones_like(value),'b':np.arange(20,dtype=float).reshape(1,-1),'ah':np.arange(20,dtype=float).reshape(1,-1),'z':np.array([[.8,1.3]])}
            savemat(temp/'state.mat',state)
            loaded=loadmat(temp/'state.mat')
            for name,array in state.items():np.testing.assert_array_equal(loaded[name],array)
            matrix=sparse.diags(np.arange(1,801,dtype=float),format='csr')
            sparse.save_npz(temp/'M.npz',matrix)
            np.testing.assert_array_equal((sparse.load_npz(temp/'M.npz')@value.ravel(order='F')),matrix@value.ravel(order='F'))
            line=json.dumps({'iteration':1,'converged':False})+'\n'
            (temp/'trace.jsonl').write_text(line*2,encoding='utf-8')
            self.assertEqual(len((temp/'trace.jsonl').read_text().splitlines()),2)


if __name__=='__main__':unittest.main(verbosity=2)
