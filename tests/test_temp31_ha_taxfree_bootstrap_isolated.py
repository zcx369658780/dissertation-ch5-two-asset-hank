"""Scalar/AST-only checks; never calls initializer, local policy or HJB solver."""
from __future__ import annotations

import ast
import copy
import dataclasses
from functools import lru_cache
import hashlib
import importlib.util
import inspect
import json
import os
from pathlib import Path
import subprocess
import sys
from types import ModuleType, SimpleNamespace
import unittest

import numpy as np

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'src/ch5_two_asset_hank'
REPORT=ROOT/'tasks/CH5_TEMP31_HA_TAU_REMOVAL_NUMERICAL_BOOTSTRAP19_ISOLATED_R1_20261029'
NS='temp31_bootstrap19_sandbox'
BLOBS={'contracts':'c746b616bec38531a7d96da81a54e2899d8aba53','hjb':'e06f9871b361c8e1c8df7aab5c43c2dbd3b09b50',
 'policy':'2021db630f3057026ffc37d375a43aaddbccec48','economics':'810e0875febc873ae85bef7e88edd4de349b00b2',
 'anchor':'b1710ae3c5d8d7baf96e85c932d777fa5f3b908c'}

@lru_cache(None)
def pinned(name):
    blob=BLOBS[name]
    p=subprocess.run(['git','--git-dir='+str(ROOT.parent/'objects.git'),'cat-file','blob',blob],
        capture_output=True,check=True,env=dict(os.environ,GIT_NO_LAZY_FETCH='1'))
    assert hashlib.sha1(b'blob '+str(len(p.stdout)).encode()+b'\0'+p.stdout).hexdigest()==blob
    return p.stdout.decode('utf-8')

def module(name, relative=None, text=None):
    full=NS+'.'+name
    if full in sys.modules:return sys.modules[full]
    for suffix,path in (('',SOURCE),('.multi_province',SOURCE/'multi_province')):
        if NS+suffix not in sys.modules:
            package=ModuleType(NS+suffix);package.__path__=[str(path)];sys.modules[NS+suffix]=package
    result=ModuleType(full);result.__package__=full.rpartition('.')[0]
    result.__file__=str(SOURCE/relative) if relative else 'PINNED_SOURCE/'+name+'.py'
    sys.modules[full]=result
    exec(compile(text if text is not None else (SOURCE/relative).read_text(),result.__file__,'exec'),result.__dict__)
    return result

def defs(text):return {n.name:n for n in ast.parse(text).body if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
def dump(node):return ast.dump(node,include_attributes=False)
def expr(text):return ast.parse(text,mode='eval').body
def assignment(function,name):
    return next(n.value for n in ast.walk(function) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets))
def evaluate(node,env):return eval(compile(ast.fix_missing_locations(ast.Expression(copy.deepcopy(node))),'<SCALAR_SOURCE_EXPRESSION>','eval'),{'__builtins__':{'float':float},'np':np},env)
def forbidden_tax_references(node):
    return [n for n in ast.walk(node) if
        isinstance(n,ast.Attribute) and n.attr in ('tau','migration_costs') or
        isinstance(n,ast.Subscript) and isinstance(n.slice,ast.Constant) and n.slice.value=='tau']

RENAME={'Temp31NetWageInputs':'HouseholdInputs','Temp31NetWageHJBGrid':'MatlabFaithfulHJBGrid',
 'Temp31NetWageHJBNumerics':'MatlabFaithfulHJBNumerics','Temp31NetWageHJBResult':'MatlabFaithfulHJBResult',
 'solve_temp31_netwage_hjb':'solve_matlab_faithful_hjb','Temp31NetWageLocalPolicy':'MatlabFaithfulLocalPolicy',
 'select_temp31_netwage_local_policy':'select_matlab_faithful_local_policy','_temp31_source_labor_root':'_source_labor_root'}

class RestoreHistorical(ast.NodeTransformer):
    """Invert only declared wage/interface edits, then compare all other AST."""
    def __init__(self,kind):self.kind=kind
    def visit_Name(self,node):node.id=RENAME.get(node.id,node.id);return node
    def visit_ClassDef(self,node):node.name=RENAME.get(node.name,node.name);return self.generic_visit(node)
    def visit_FunctionDef(self,node):node.name=RENAME.get(node.name,node.name);return self.generic_visit(node)
    def visit_Expr(self,node):
        if isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Name) and node.value.func.id=='require_netwage_inputs':return None
        return self.generic_visit(node)
    def visit_ImportFrom(self,node):
        if self.kind=='initial' and node.module=='temp31_netwage_economics':return None
        return node
    def visit_Assign(self,node):
        name=node.targets[0].id if len(node.targets)==1 and isinstance(node.targets[0],ast.Name) else None
        if self.kind=='economics' and name=='net_wage':node.value=expr('inputs.wages * (1.0 - inputs.tau - inputs.migration_costs) * z')
        if self.kind=='economics' and name=='labor_income':node.value=expr('float(np.sum(inputs.wages * (1.0 - inputs.tau - inputs.migration_costs) * z * labor))')
        if self.kind=='hjb' and name=='resources':node.value=expr('(1-inputs.tau)*inputs.wages[0]*z*labor0[i,j,nz] + transfer_income + rb*grid.b[i]')
        if self.kind=='policy' and name=='net_wage':node.value=expr('float(local_inputs.wages[0] * (1.0-local_inputs.tau-local_inputs.migration_costs[0]) * z)')
        if self.kind=='policy' and name=='local_inputs':
            args=node.value.args
            assert len(args)==8
            node.value.args=[args[0],args[1],expr('inputs.tau'),args[2],expr('inputs.migration_costs'),args[3]]
        if self.kind=='initial' and name=='wage':node.value=expr('(1-float(state["tau"]))*float(state["w"])*z')
        return self.generic_visit(node)

class Common(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contracts=module('contracts',text=pinned('contracts'))
        cls.r4=module('multi_province.temp31_worksite_tax','multi_province/temp31_worksite_tax.py')
        cls.r5=module('multi_province.temp31_ha_wage_debug','multi_province/temp31_ha_wage_debug.py')
        cls.boot=module('multi_province.temp31_ha_taxfree_bootstrap','multi_province/temp31_ha_taxfree_bootstrap.py')
    def first(self,**changes):
        return self.boot.numerical_bootstrap19(**(dict(context_id='SYNTHETIC_A',province_order=('A','B'),
            tax_by_destination=(0.2,0.6),sigma_destination_origin=((0,0.8),(0.1,0)))|changes))
    def inputs(self,record=None,origin=0,**changes):
        return self.boot.netwage_inputs(record or self.first(),**(dict(origin_index=origin,r_a=.09,r_b=.02,
            expected_context_id='SYNTHETIC_A',expected_province_order=('A','B'))|changes))
    def later(self,**changes):
        calc=self.r5.SyntheticNetWageCalculation((5,10),(.2,.6),((1,1),(1,1)),((0,.8),(.1,0)),1,1,('A','B'),'SYNTHETIC_A',1)
        record=self.r5.calculated_round_record(calc,2)
        return self.boot.later_net_wage_record(dataclasses.replace(record,**changes))
    def sources(self):
        return {kind:defs((SOURCE/('temp31_netwage_'+kind+'.py')).read_text()) for kind in ('hjb','policy','economics')}

class BootstrapContractTests(Common):
    def test_19_guess_preserves_state_and_real_mechanism(self):
        state={'w':20.,'tau':.05};before=dict(state);r=self.first(w_initial=state['w'],tau_legacy_reference=state['tau'])
        self.assertEqual(r.effective_wages_by_origin,(19,19));self.assertEqual(state,before)
        self.assertEqual(r.semantics,self.boot.NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL)
        self.assertEqual(r.tax_by_destination,(.2,.6));self.assertEqual(r.sigma_destination_origin,((0,.8),(.1,0)))
    def test_changed_initial_contract_rejected(self):
        for change in ({'w_initial':21},{'tau_legacy_reference':.04}):
            with self.assertRaises(ValueError):self.first(**change)
    def test_first_and_later_sources_distinct(self):
        first,later=self.first(),self.later()
        self.assertNotEqual(first.semantics,later.semantics);self.assertAlmostEqual(later.effective_wages_by_origin[0],5)
        self.assertAlmostEqual(later.effective_wages_by_origin[1],4)
        with self.assertRaises(ValueError):dataclasses.replace(first,semantics=self.r5.CALCULATED_NET_AFTER_DESTINATION_TAU_AND_SIGMA)
    def test_context_order_and_origin_guard(self):
        for change in ({'expected_context_id':'OTHER'},{'expected_province_order':('B','A')},{'origin_index':2}):
            with self.assertRaises(ValueError):self.inputs(**change)
    def test_later_wrong_producer_or_source_rejected(self):
        for change in ({'context_id':'OTHER'},{'province_order':('B','A')},{'entering_iteration':3},{'wage_by_origin':(19,19)}):
            with self.assertRaises(ValueError):self.later(**change)
        with self.assertRaises(ValueError):dataclasses.replace(self.first(),source_commit='0'*40)
    def test_corrected_type_has_no_tax_or_migration_parameter(self):
        inputs=self.inputs();self.assertEqual(inputs.wages[0],19)
        self.assertFalse(hasattr(inputs,'tau'));self.assertFalse(hasattr(inputs,'migration_costs'))
        self.assertNotIn('tau',inspect.signature(self.boot.Temp31NetWageInputs).parameters)
        with self.assertRaises(TypeError):self.boot.Temp31NetWageInputs(.09,.02,np.array([19]),np.array([1]),self.first(),0,'SYNTHETIC_A',('A','B'),tau=0)
    def test_double_wage_wedge_and_global_tax_zeroing_rejected(self):
        for factor in (.8,.9):
            with self.assertRaises(ValueError):dataclasses.replace(self.inputs(),wages=np.array([19*factor]))
        with self.assertRaises(ValueError):dataclasses.replace(self.later(),tax_by_destination=(0,0))
        with self.assertRaises(TypeError):self.boot.require_netwage_inputs(self.contracts.HouseholdInputs(.09,.02,.05,np.array([20]),np.array([0]),np.array([1])))
    def test_original_and_prior_candidates_unchanged(self):
        identity=json.loads((REPORT/'source_identity.json').read_text())
        for entry in identity['required_source_files']:
            raw=subprocess.run(['git','--git-dir='+str(ROOT.parent/'objects.git'),'cat-file','blob',entry['git_blob']],capture_output=True,check=True).stdout
            self.assertEqual(len(raw),entry['bytes']);self.assertEqual(hashlib.sha256(raw).hexdigest(),entry['sha256'])
        for entry in identity['previous_preservation']['r5_published_files']+identity['previous_preservation']['r4_published_files']:
            raw=(ROOT/entry['path']).read_bytes();self.assertEqual(hashlib.sha256(raw).hexdigest(),entry['sha256'])

class SourceAlgebraTests(Common):
    def test_six_consumer_sites_have_no_extra_tax_fields(self):
        trees=self.sources();initial=defs((SOURCE/'multi_province/temp31_ha_taxfree_bootstrap.py').read_text())
        sites=[initial['temp31_netwage_initial_arrays'],trees['hjb']['solve_temp31_netwage_hjb'],trees['policy']['select_temp31_netwage_local_policy']]
        sites += [trees['economics'][name] for name in ('labor_from_vb','asset_drifts','asset_drifts_matlab_faithful')]
        for node in sites:self.assertEqual(forbidden_tax_references(node),[])
    def test_static_gate_detects_omitted_tax_factor_injection(self):
        injected=expr('inputs.wages[0]*(1-inputs.tau)')
        self.assertTrue(forbidden_tax_references(injected))
        self.assertTrue(forbidden_tax_references(expr('inputs.wages*(1-inputs.migration_costs)')))
    def test_non_tax_algorithm_ast_preserved_in_all_three_copies(self):
        for kind,newnodes in self.sources().items():
            old=defs(pinned(kind));normalized={RENAME.get(name,name):RestoreHistorical(kind).visit(copy.deepcopy(node)) for name,node in newnodes.items()}
            self.assertEqual(set(old),set(normalized))
            for name in old:self.assertEqual(dump(normalized[name]),dump(old[name]),(kind,name))
    def test_initialization_root_and_non_wage_body_preserved(self):
        new=defs((SOURCE/'multi_province/temp31_ha_taxfree_bootstrap.py').read_text());old=defs(pinned('anchor'))
        root=RestoreHistorical('initial').visit(copy.deepcopy(new['_temp31_source_labor_root']))
        self.assertEqual(dump(root),dump(old['_source_labor_root']))
        initial=RestoreHistorical('initial').visit(copy.deepcopy(new['temp31_netwage_initial_arrays']))
        self.assertEqual([dump(x) for x in initial.body],[dump(x) for x in old['_source_initial_arrays'].body])
    def coefficients(self,inputs,legacy=False):
        trees={k:defs(pinned(k)) for k in ('hjb','policy','economics')} if legacy else self.sources()
        initial=defs(pinned('anchor'))['_source_initial_arrays'] if legacy else defs((SOURCE/'multi_province/temp31_ha_taxfree_bootstrap.py').read_text())['temp31_netwage_initial_arrays']
        env={'inputs':inputs,'local_inputs':inputs,'z':1.5,'state':{'w':20.,'tau':.05},'labor':np.array([1.]),
             'labor0':np.ones((1,1,1)),'i':0,'j':0,'nz':0,'grid':SimpleNamespace(b=np.array([0.])),
             'transfer_income':0.,'rb':0.}
        targets=[(initial,'wage'),(trees['hjb']['solve_matlab_faithful_hjb' if legacy else 'solve_temp31_netwage_hjb'],'resources'),
                 (trees['policy']['select_matlab_faithful_local_policy' if legacy else 'select_temp31_netwage_local_policy'],'net_wage'),
                 (trees['economics']['labor_from_vb'],'net_wage'),(trees['economics']['asset_drifts'],'labor_income'),(trees['economics']['asset_drifts_matlab_faithful'],'labor_income')]
        return [float(np.asarray(evaluate(assignment(node,target),env)).ravel()[0]) for node,target in targets]
    def test_initial_legacy_single_tax_algebra_matches_19_six_sites(self):
        old=self.contracts.HouseholdInputs(.09,.02,.05,np.array([20.]),np.array([0.]),np.array([1.]))
        self.assertEqual(self.coefficients(old,True),[28.5]*6);self.assertEqual(self.coefficients(self.inputs()),[28.5]*6)
    def test_later_destination_net_not_origin_tau_all_six_sites(self):
        record=self.later()
        for origin,wanted in ((0,5.),(1,4.)):
            inputs=self.inputs(record,origin)
            for value in self.coefficients(inputs):self.assertAlmostEqual(value,1.5*wanted)
        record=self.later();self.assertNotAlmostEqual(record.effective_wages_by_origin[0]*(1-record.tax_by_destination[0]),5.)
    def test_foc_and_both_liquid_budgets_are_pure_algebra(self):
        nodes=self.sources()['economics'];inputs=self.inputs();params=SimpleNamespace(phi=2)
        labor=evaluate(assignment(nodes['labor_from_vb'],'labor'),{'np':np,'inputs':inputs,'params':params,'v_b':4.,'net_wage':np.array([9.5])})
        self.assertAlmostEqual(float(labor[0]),np.sqrt(38.))
        env={'inputs':inputs,'b':10.,'labor_income':19.,'transfer':3.,'cost':2.,'consumption':5.}
        for name in ('asset_drifts','asset_drifts_matlab_faithful'):
            self.assertAlmostEqual(evaluate(assignment(nodes[name],'mu_b'),env),9.2)
    def test_corrected_dependency_bindings_and_operator_unchanged(self):
        hjb=ast.parse((SOURCE/'temp31_netwage_hjb.py').read_text());policy=ast.parse((SOURCE/'temp31_netwage_policy.py').read_text())
        old=ast.parse(pinned('hjb'))
        op=lambda tree:next(n for n in tree.body if isinstance(n,ast.ImportFrom) and n.module=='matlab_faithful_operator')
        self.assertEqual(dump(op(hjb)),dump(op(old)))
        self.assertTrue(any(isinstance(n,ast.ImportFrom) and n.module=='temp31_netwage_policy' for n in hjb.body))
        self.assertTrue(any(isinstance(n,ast.ImportFrom) and n.module=='temp31_netwage_economics' for n in policy.body))
