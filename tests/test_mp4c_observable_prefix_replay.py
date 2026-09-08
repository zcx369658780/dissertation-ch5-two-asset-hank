"""Synthetic observer tests; no model or initializer invocations."""
import ast
from dataclasses import dataclass,replace
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
import numpy as np
from scipy import sparse

DIR=Path(__file__).resolve().parents[1]/'validators/multi_province/observable_prefix_replay'
sys.path.insert(0,str(DIR))
from observer import Budget,Store,PrefixLimit,delegate


def temporary():
    return tempfile.TemporaryDirectory(dir=os.environ.get('OBS_TEST_ROOT',str(DIR)))


class ObservationTests(unittest.TestCase):
    def test_delegates_once_identical_arguments_and_return(self):
        x=np.arange(4.);token=object();seen=[]
        def original(a,*,b):seen.append((a,b));return token
        result=delegate(original)(x,b=token)
        self.assertIs(result,token);self.assertIs(seen[0][0],x);self.assertIs(seen[0][1],token)
        self.assertEqual(len(seen),1);np.testing.assert_array_equal(x,np.arange(4.))

    def test_full_common_state_saved_before_first_call(self):
        with temporary() as tmp:
            store=Store(tmp);states=[{'index':i,'value':float(i)} for i in range(31)]
            def original(snapshot):
                saved=json.loads((Path(tmp)/'common.json').read_text())
                self.assertEqual(len(saved),31);self.assertIs(snapshot,states);return object()
            delegate(original,lambda snapshot:store.save('common',snapshot))(states);store.close()

    def test_capture_does_not_retain_mutable_references(self):
        with temporary() as tmp:
            store=Store(tmp);a=np.array([1.,2.]);states={'x':a,'sub':{'price':.09}}
            store.save('before',states);a[:]=8;states['sub']['price']=.02
            saved=json.loads((Path(tmp)/'before.json').read_text())
            self.assertEqual(saved['sub']['price'],.09)
            np.testing.assert_array_equal(np.load(Path(tmp)/'before.npz')['root_x'],[1.,2.]);store.close()

    def test_sparse_support_and_nonfinite_preserved(self):
        with temporary() as tmp:
            store=Store(tmp);a=sparse.csr_matrix(([2.,-1.],([0,1],[1,0])),shape=(2,2))
            store.save('data',{'A':a,'raw':np.array([np.nan,np.inf]),'stat':float('nan')})
            with np.load(Path(tmp)/'data.npz') as f:
                np.testing.assert_array_equal(f['root_A_indices'],a.indices)
                self.assertTrue(np.isnan(f['root_raw'][0]))
            self.assertEqual(json.loads((Path(tmp)/'data.json').read_text())['stat'],{'nonfinite':'nan'});store.close()

    def test_failed_entry_counted_and_exception_preserved(self):
        budget=Budget()
        def fail():raise ValueError('original failure')
        wrapped=delegate(fail,lambda:budget.enter('native_initialization'))
        with self.assertRaisesRegex(ValueError,'original failure'):wrapped()
        self.assertEqual(budget.counts['native_initialization'],1)

    def test_hard_stop_before_call726(self):
        budget=Budget()
        for _ in range(725):budget.enter('native_initialization')
        with self.assertRaises(PrefixLimit):budget.after_household()
        with self.assertRaises(PrefixLimit):budget.enter('native_initialization')
        self.assertEqual(budget.call,725)

    def test_per_household_solver_limits(self):
        b=Budget();b.enter('native_initialization')
        for _ in range(100):b.enter('HJB_direct_solve')
        with self.assertRaises(PrefixLimit):b.enter('HJB_direct_solve')
        b.enter('KFE_direct_solve')
        with self.assertRaises(PrefixLimit):b.enter('KFE_direct_solve')

    def test_current_household_labor_not_old_firm_labor(self):
        seen=[];old={'Lt':30.};firm={'Lt_prev':2.,'name':'synthetic'}
        def f(province,k,l,params):seen.append((province['Lt_prev'],l));return 1
        delegate(f)(firm,10.,40.,{})
        self.assertEqual(seen,[(2.,40.)]);self.assertEqual(old['Lt'],30.)

    def test_dispatch_replacement_preserves_scientific_fields(self):
        @dataclass(frozen=True)
        class Input:
            state:object
            household_solver:object
        state=np.arange(3);x=Input(state,lambda:1);y=replace(x,household_solver=lambda:2)
        self.assertIs(x.state,y.state)

    def test_original_false_hjb_still_reaches_kfe_and_persists_failure(self):
        # Compile only original composition function, injecting synthetic primitives.
        path=DIR.parents[2]/'validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py'
        tree=ast.parse(path.read_text(encoding='utf-8'))
        fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='solve_matlab_source_postloop_household')
        class Box:pass
        h=Box();h.converged=False;h.post_convergence_operator=Box();h.post_convergence_operator.full='A'
        calls=[]
        def hjb(*a):calls.append('hjb_saved');return h
        def kfe(*a,**k):calls.append('kfe');raise ValueError('KFE original exception')
        namespace={'Callable':object,'HouseholdSteadyStateResult':Box,'solve_matlab_faithful_hjb':hjb,
                   'solve_matlab_faithful_stationary_kfe':kfe,'aggregate_stationary_household':lambda *a:None}
        exec(compile(ast.Module(body=[fn],type_ignores=[]),str(path),'exec'),namespace)
        grid=Box();grid.b=np.array([0.,1.]);grid.a=np.array([0.,1.]);grid.z=np.array([1.])
        with self.assertRaisesRegex(ValueError,'KFE original exception'):
            namespace[fn.name](grid,None,None,None,None,None,None,None)
        self.assertEqual(calls,['hjb_saved','kfe'])

    def test_failure_does_not_erase_saved_hjb(self):
        with temporary() as tmp:
            store=Store(tmp);store.save('hjb_return_before_kfe',{'converged':False})
            try:raise ValueError('failure')
            except ValueError as exc:store.save('terminal',{'type':type(exc).__name__,'counts':{'KFE':1}})
            self.assertTrue((Path(tmp)/'hjb_return_before_kfe.json').exists());store.close()

    def test_import_has_no_scientific_execution(self):
        spec=importlib.util.spec_from_file_location('observation_runner',DIR/'run.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        self.assertNotIn('worker',module.__dict__)

    def test_capture_phase_and_lag_distinction(self):
        with temporary() as tmp:
            s=Store(tmp);s.save('turn23_firm_used',{'Zt':.7});s.save('turn23_after_adaptation',{'Zt':.6})
            self.assertNotEqual((Path(tmp)/'turn23_firm_used.json').read_text(),(Path(tmp)/'turn23_after_adaptation.json').read_text());s.close()



    def test_frozen_128eps_and_bound_flags(self):
        import analyze
        eps=np.finfo(float).eps
        self.assertTrue(analyze.near(1.,1.+128*eps))
        self.assertFalse(analyze.near(1.,1.+129*eps))
        self.assertFalse(analyze.near(float('nan'),1.))
        flags=analyze.flags(.09,.02,.09)
        self.assertTrue(flags['exact_upper']);self.assertFalse(flags['above'])

    def test_prefix_first_mismatch_and_complete_comparison(self):
        import analyze,csv
        with temporary() as tmp:
            root=Path(tmp);old=root/'old';old.mkdir();cap=root/'capture';cap.mkdir()
            cols=['outer_iteration','province_index_0based','province','global_household_call_number',*analyze.FIELDS]
            with (old/'household_call_ledger.csv').open('w',encoding='utf-8',newline='') as f:
                w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
                for n in (1,2,3):w.writerow(dict(zip(cols,[1,n-1,'Synthetic',n,*([1.]*len(analyze.FIELDS))])))
            for n in (1,2,3):
                d=cap/f'call_{n:04d}';d.mkdir();state={k:1. for k in analyze.FIELDS}
                if n==2:state['w']=2.
                analyze.save(d/'entry.json',{'context':{'step':1,'province_index_0':n-1,'province':'Synthetic','call':n},'state':state})
            prior=analyze.OLD
            try:
                analyze.OLD=old;summary,rows=analyze.compare(cap)
            finally:analyze.OLD=prior
            self.assertEqual(summary['matched_prefix'],1);self.assertEqual(summary['first_mismatch']['call'],2)
            self.assertEqual(summary['available_entries'],3);self.assertEqual(len(rows),33)

if __name__=='__main__':unittest.main(verbosity=2)
