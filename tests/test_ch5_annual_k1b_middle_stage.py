"""Single changed-code process: prior30 plus invented inactive middle contracts."""
import copy
from dataclasses import replace
import hashlib
import importlib.util
from pathlib import Path
import struct
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def direct(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


previous = direct('middle_previous30', 'tests/test_ch5_observed_annual_array_seam.py')
np = previous.np
context, adapter, seam = previous.context, previous.adapter, previous.seam
middle = direct('middle_fixture_test', 'validators/multi_province/annual_observed_labor_diagnostic/middle_stage.py')
AXIS, MAPPING = previous.AXIS, previous.MAPPING
KEYS = ('source_faithful_labor_reconstructions', 'frozen_k1b_quantity_allocations',
    'k1b_feedback_calls', 'c1_residual_govinv_constructions', 'firm_evaluations', 'composite_wage_batches')
FIELDS = ('Kt','Lt','Yt','mt','KNratio','wt0','wjt','rk','Thetat','It','PIt','Corptax','ra0','ra','Govinc')


def reference_hash(values):
    rows = [list(row) for row in values]
    encoded = b''.join(struct.pack('<d', float(rows[j][i]))
        for i in range(len(rows[0])) for j in range(len(rows)))
    return hashlib.sha256(encoded).hexdigest().upper()


class MiddleTests(unittest.TestCase):
    def setUp(self):
        raw, sha = previous.old.fixture()
        self.ctx = context.prepare_synthetic_context(raw, expected_fixture_sha256=sha,
            province_axis=AXIS, target_year=2018)
        self.meta = dict(target_year=2018, province_axis=AXIS, source_sha256=sha,
            input_kind='synthetic', price_basis='synthetic_fixture', price_verified=False)
        self.carrier = adapter.prepare_annual_array(self.ctx, province_mapping=MAPPING, **self.meta)
        self.events, self.deliveries, self.firm_sources = [], [], []
        self.params = dict(ga=2.,phi_l=5.,alphal=1.,epsilon=10.,theta=100.,delta=.025)
        self.distance = ((0.,1.,2.),(3.,0.,4.),(5.,6.,0.))
        self.shares = np.array(((.5,.2,.3),(.3,.5,.2),(.2,.3,.5)), dtype=float)
        self.sha = reference_hash(self.shares)
        self.batch = SimpleNamespace(ct=(1.,2.,3.),at=(2.,4.,6.),at_tax=(.1,.2,.3),household_lt=(7.,8.,9.))
        self.rows = tuple(dict(name=short,province_index=i,source_province_name=full,N=10.*i,
            wjt=3.+i,tau=.1,inter_prv_ratio=.5,Kt0=target,alpha=.3,Zt=1.,pit=.02,
            Kt_prev=50.,Zt_1=1.,pit_1=.02,rk=.01,corptau=.2,Tt=1.,ramin=0.,ramax=1.,
            wjtmin=0.,wjtmax=20.) for (i,full,short),target in zip(MAPPING,(50.,100.,100.)))
        self.ledger = self.new_ledger()
        self.dependencies = middle.FixtureDependencies(self.c1, self.firm, 'invented-three-province')
        self.stage = self.prepare(self.ledger, self.dependencies)
        def factory(**kw):
            self.events.append('inputs'); self.deliveries.append(kw['phi_destination_origin'])
            self.assertIs(kw['migration_wedge_destination_origin'], self.distance)
            return SimpleNamespace(**kw)
        def labor(inputs):
            self.events.append('labor'); return SimpleNamespace(lt_supply=(11.,22.,33.))
        def opaque(*args):
            raise AssertionError('explicit middle must not use opaque firm callback')
        def wage(provinces,firm_wages,phi,distance,*,phi_l,alphal):
            self.events.append('wages'); self.deliveries.append(phi)
            self.assertIs(distance,self.distance)
            self.assertEqual(firm_wages,[6.,7.,8.])
            return (101.,202.,303.)
        self.spies = seam.SyntheticSpies(factory,labor,opaque,wage)

    def new_ledger(self):
        return dict(engineering_fixture_label='invented-three-province', **{key:0 for key in KEYS})

    def prepare(self, ledger, deps, **changes):
        kw = dict(annual_context=self.ctx,prepared_array=self.carrier,province_mapping=MAPPING,
            ledger=ledger,dependencies=deps)
        kw.update(changes)
        return middle.prepare_middle_stage(**kw)

    def c1(self, *, Ktarget_MU, Kprivate_current_MU, province_order):
        self.events.append('c1')
        self.assertEqual(tuple(province_order),('Low','High','Middle'))
        target, private = np.asarray(Ktarget_MU), np.asarray(Kprivate_current_MU)
        return SimpleNamespace(province_order=tuple(province_order),
            GovInv_residual_MU=np.maximum(target-private,0.),
            firm_K_accounting_MU=np.maximum(target,private))

    def firm(self, source, private, labor, params):
        self.events.append('firm:'+str(source['province_index']))
        self.firm_sources.append(dict(source))
        self.assertEqual(dict(params),self.params)
        i = source['province_index']-1
        expected = dict(self.rows[i])
        expected.update(GovInv=(0.,18.,0.)[i],AtTax=self.batch.at_tax[i],Lt_prev=self.batch.household_lt[i])
        self.assertEqual(source,expected)
        values = dict.fromkeys(FIELDS,1.)
        values.update(Kt=private+source['GovInv'],Lt=labor,wjt=5.+source['province_index'],ra0=.2,ra=.1)
        return SimpleNamespace(**values,as_source_dict=lambda:dict(values))

    def run_seam(self, **changes):
        states = changes.pop('states', self.rows)
        batch = changes.pop('batch', self.batch)
        shares = changes.pop('shares', self.shares)
        ledger = changes.pop('ledger', self.ledger)
        sha = changes.pop('expected_share_sha', self.sha)
        kw = dict(annual_context=self.ctx,prepared_array=self.carrier,province_mapping=MAPPING,
            prepared_middle_stage=self.stage,params=self.params,
            migration_wedge_destination_origin=self.distance,spies=self.spies,**self.meta)
        kw.update(changes)
        return seam.integrate_turn(None,None,None,5,states,batch,shares,sha,ledger,[],**kw)

    def test_order_arithmetic_overrides_and_attempted_counts(self):
        original = tuple(dict(row) for row in self.rows)
        result = self.run_seam()
        capital, accounting = result['middle_result'].capital,result['middle_result'].c1
        self.assertEqual(tuple(capital.wealth),(20.,80.,180.))
        self.assertEqual(tuple(capital.private),(80.,82.,118.))
        self.assertEqual(tuple(capital.domestic),(10.,40.,90.))
        self.assertEqual(tuple(accounting.GovInv_residual_MU),(0.,18.,0.))
        self.assertEqual(tuple(accounting.firm_K_accounting_MU),(80.,100.,118.))
        self.assertEqual(self.events,['inputs','labor','c1','firm:1','firm:2','firm:3','wages'])
        self.assertEqual({key:self.ledger[key] for key in KEYS},dict(zip(KEYS,(1,1,1,1,3,1))))
        self.assertTrue(all(phi is self.carrier.phi_destination_origin for phi in self.deliveries))
        self.assertEqual(self.rows,original)
        self.assertFalse(result['full_outer_runtime_integrated']); self.assertFalse(result['model_activation'])

    def test_forder_hash_matches_independent_littleendian_fixture(self):
        values = np.array(((1.25,2.5,3.75),(4.125,5.25,6.5)),dtype='>f8')
        self.assertEqual(middle._field_sha256(values),reference_hash(values))
        expected = hashlib.sha256(struct.pack('<dddddd',1.25,4.125,2.5,5.25,3.75,6.5)).hexdigest().upper()
        self.assertEqual(middle._field_sha256(values),expected)
        self.assertNotEqual(expected,hashlib.sha256(values.astype('<f8').tobytes(order='C')).hexdigest().upper())

    def test_one_annual_helper_same_master_different_turn_bridges(self):
        helper = context._helper()
        with patch.object(helper,'build_annual_labor_wedge',wraps=helper.build_annual_labor_wedge) as count:
            raw,sha=previous.old.fixture()
            ctx=context.prepare_synthetic_context(raw,expected_fixture_sha256=sha,province_axis=AXIS,target_year=2018)
            carrier=adapter.prepare_annual_array(ctx,province_mapping=MAPPING,**self.meta)
            for _ in range(2):
                ledger=self.new_ledger()
                stage=self.prepare(ledger,self.dependencies,annual_context=ctx,prepared_array=carrier)
                self.run_seam(annual_context=ctx,prepared_array=carrier,prepared_middle_stage=stage,ledger=ledger)
            self.assertEqual(count.call_count,1)
            self.assertTrue(all(phi is carrier.phi_destination_origin for phi in self.deliveries))

    def test_full_required_fields_and_params_refuse_before_spies(self):
        for key in ('alpha','Zt','pit','Kt_prev','Zt_1','pit_1','rk','corptau','tau','Tt','ramin','ramax','wjtmin','wjtmax','Kt0','inter_prv_ratio','N'):
            rows=tuple(dict(row) for row in self.rows); del rows[0][key]
            with self.assertRaises(ValueError): self.run_seam(states=rows)
        for key in ('ga','phi_l','alphal','epsilon','theta','delta'):
            params=dict(self.params); del params[key]
            with self.assertRaises(ValueError): self.run_seam(params=params)
        self.assertEqual(self.events,[])

    def test_shapes_boolean_nonfinite_and_axis_refusal_before_spies(self):
        for field in ('ct','at','at_tax','household_lt'):
            for bad in ((1.,2.),np.ones((3,1)),(True,2.,3.),(float('nan'),2.,3.)):
                values=dict(vars(self.batch)); values[field]=bad
                with self.assertRaises(ValueError): self.run_seam(batch=SimpleNamespace(**values))
        for field,bad in (('ct',(0.,2.,3.)),('ct',(-1.,2.,3.)),('at',(-1.,4.,6.)),('household_lt',(-1.,8.,9.))):
            values=dict(vars(self.batch)); values[field]=bad
            with self.assertRaises(ValueError): self.run_seam(batch=SimpleNamespace(**values))
        for key,value in (('N',True),('alpha',float('inf')),('name','Invented Low'),('province_index',True)):
            rows=tuple(dict(row) for row in self.rows); rows[0][key]=value
            with self.assertRaises(ValueError): self.run_seam(states=rows)
        for shares in (np.ones((3,3,1)),np.ones((2,2)),((True,0.,0.),(0.,1.,0.),(0.,0.,1.))):
            with self.assertRaises(ValueError): self.run_seam(shares=shares)
        self.assertEqual(self.events,[])

    def test_hash_conservation_and_domestic_failures_stop_without_later_calls(self):
        with self.assertRaises(ValueError): self.run_seam(expected_share_sha='0'*64)
        bad=self.shares.copy(); bad[0,0]=.6
        with self.assertRaises(ValueError): self.run_seam(shares=bad,expected_share_sha=reference_hash(bad))
        rows=tuple(dict(row) for row in self.rows); rows[0]['inter_prv_ratio']=.4
        with self.assertRaises(ValueError): self.run_seam(states=rows)
        self.assertNotIn('c1',self.events); self.assertNotIn('wages',self.events)

    def test_factory_and_labor_failure_keep_historical_nested_attempt_timing(self):
        def fail(*args,**kwargs): raise ValueError('invented labor boundary failure')
        for at_factory in (True,False):
            ledger=self.new_ledger()
            stage=self.prepare(ledger,self.dependencies)
            spies=seam.SyntheticSpies(fail if at_factory else self.spies.migration_inputs_factory,
                self.spies.reconstruct_migration_labor if at_factory else fail,
                self.spies.firm_stage,self.spies.composite_household_wages)
            with self.assertRaises(ValueError):
                self.run_seam(prepared_middle_stage=stage,ledger=ledger,spies=spies)
            self.assertEqual(ledger['source_faithful_labor_reconstructions'],1)
            self.assertEqual(ledger['frozen_k1b_quantity_allocations'],0)
            self.assertEqual(ledger['c1_residual_govinv_constructions'],0)
            self.assertEqual(ledger['firm_evaluations'],0)
            self.assertEqual(ledger['composite_wage_batches'],0)
    def test_c1_failure_consumes_attempt_and_suppresses_firms_wages(self):
        def fail(**kw): self.events.append('c1fail'); raise ValueError('invented first failure')
        stage=self.prepare(self.ledger,middle.FixtureDependencies(fail,self.firm,'invented-failure'))
        with self.assertRaises(ValueError): self.run_seam(prepared_middle_stage=stage)
        self.assertEqual(self.ledger['c1_residual_govinv_constructions'],1)
        self.assertEqual(self.ledger['firm_evaluations'],0)
        self.assertEqual(self.ledger['composite_wage_batches'],0)
        self.assertNotIn('wages',self.events)

    def test_c1_shapes_exact_values_and_finite_refused(self):
        for change in ({'GovInv_residual_MU':(0.,17.,0.)},{'GovInv_residual_MU':((0.,),(18.,),(0.,))},
                       {'firm_K_accounting_MU':(80.,100.,float('nan'))}):
            ledger=self.new_ledger()
            def wrong(**kw):
                result=self.c1(**kw); result.__dict__.update(change); return result
            stage=self.prepare(ledger,middle.FixtureDependencies(wrong,self.firm,'invented-wrong-c1'))
            with self.assertRaises(ValueError): self.run_seam(prepared_middle_stage=stage,ledger=ledger)
        self.assertFalse(any(event.startswith('firm:') for event in self.events)); self.assertNotIn('wages',self.events)

    def test_c1_input_tamper_refused_before_firms_and_wages(self):
        for key in ('Ktarget_MU','Kprivate_current_MU'):
            ledger=self.new_ledger()
            def tamper(**kw):
                kw[key][0] += 1.
                return self.c1(**kw)
            stage=self.prepare(ledger,middle.FixtureDependencies(tamper,self.firm,'invented-tamper'))
            with self.assertRaises(ValueError): self.run_seam(prepared_middle_stage=stage,ledger=ledger)
            self.assertEqual(ledger['c1_residual_govinv_constructions'],1)
            self.assertEqual(ledger['firm_evaluations'],0)
            self.assertEqual(ledger['composite_wage_batches'],0)
        self.assertNotIn('wages',self.events)
    def test_firm_nonfinite_and_capital_mismatch_preserve_attempt(self):
        for key,value in (('Govinc',float('inf')),('Kt',999.)):
            ledger=self.new_ledger()
            def wrong(source,private,labor,params):
                result=self.firm(source,private,labor,params); setattr(result,key,value); return result
            stage=self.prepare(ledger,middle.FixtureDependencies(self.c1,wrong,'invented-wrong-firm'))
            with self.assertRaises(ValueError): self.run_seam(prepared_middle_stage=stage,ledger=ledger)
            self.assertEqual(ledger['firm_evaluations'],1); self.assertEqual(ledger['composite_wage_batches'],0)
        self.assertNotIn('wages',self.events)

    def test_ledger_and_forged_seals_refused_before_spies(self):
        for bad in (replace(self.stage),copy.copy(self.stage),SimpleNamespace(validate_pre_spy=lambda *a,**k:None)):
            with self.assertRaises(ValueError): self.run_seam(prepared_middle_stage=bad)
        for key,value in ((KEYS[0],True),(KEYS[1],-1),(KEYS[2],1.0)):
            ledger=self.new_ledger(); ledger[key]=value
            with self.assertRaises(ValueError): self.prepare(ledger,self.dependencies)
        ledger=self.new_ledger(); del ledger['engineering_fixture_label']
        with self.assertRaises(ValueError): self.prepare(ledger,self.dependencies)
        with self.assertRaises(ValueError): self.run_seam(ledger=self.new_ledger())
        self.assertEqual(self.events,[])

    def test_explicit_carrier_context_and_production_closed(self):
        with self.assertRaises(ValueError): self.run_seam(prepared_array=None)
        with self.assertRaises(ValueError): self.run_seam(input_kind='observed')
        with self.assertRaises(ValueError): self.run_seam(province_mapping=MAPPING[::-1])
        raw,sha=previous.old.fixture()
        another=context.prepare_synthetic_context(raw,expected_fixture_sha256=sha,province_axis=AXIS,target_year=2018)
        with self.assertRaises(ValueError): self.run_seam(annual_context=another)
        self.assertEqual(self.events,[])
        self.assertFalse(any(name=='ch5_two_asset_hank' or name.startswith('ch5_two_asset_hank.') for name in sys.modules))


def load_tests(loader,tests,pattern):
    suite=unittest.TestSuite()
    suite.addTests(previous.load_tests(loader,None,None))
    suite.addTests(loader.loadTestsFromTestCase(MiddleTests))
    return suite


if __name__=='__main__':
    unittest.main(verbosity=2)