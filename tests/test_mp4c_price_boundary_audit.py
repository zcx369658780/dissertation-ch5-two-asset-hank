"""Synthetic tests only. No production module or real model execution."""
import ast
import importlib.util
import math
from pathlib import Path
import sys
import unittest

DIR=Path(__file__).resolve().parents[1]/'validators/multi_province/price_boundary_audit'
sys.path.insert(0,str(DIR))
import core


class AuditTests(unittest.TestCase):
    def test_exact_contact_not_strict_excursion(self):
        r=core.classify(.09,.02,.09)
        self.assertTrue(r['exact_upper']); self.assertFalse(r['strict_above'])

    def test_roundoff_outside_remains_outside(self):
        r=core.classify(math.nextafter(.09,math.inf),.02,.09)
        self.assertTrue(r['strict_above']);self.assertTrue(r['outside_by_roundoff'])

    def test_near_inside_distinct(self):
        r=core.classify(math.nextafter(.09,0),.02,.09)
        self.assertTrue(r['near_inside']);self.assertFalse(r['exact_upper'])

    def test_missing_nonfinite_and_rounded_not_interior(self):
        for x,label in [(None,'MISSING'),(math.nan,'NONFINITE'),(math.inf,'NONFINITE')]:
            self.assertEqual(core.classify(x,.02,.09)['status'],label)
        r=core.classify(.09,.02,.09,'ROUNDED_LOG')
        self.assertEqual(r['status'],'ROUNDED_UNCERTAIN');self.assertNotIn('exact_upper',r)

    def test_initialization_separated(self):
        r=core.classify(.6,.8,1.3,phase='initialization')
        self.assertEqual(r['status'],'INITIALIZATION');self.assertTrue(r['strict_below'])

    def test_literal_global_gate(self):
        self.assertEqual(core.controller(.1,1,False),'CLOSED')
        self.assertEqual(core.controller(math.nextafter(.1,0),1,False),'ENABLED')
        self.assertEqual(core.controller(.01,0,False),'CLOSED')
        self.assertEqual(core.controller(.01,1,True),'CONVERGENCE_EXIT_FIRST')
        self.assertEqual(core.controller(None,1,False,False),'INTERRUPTED_BEFORE_CONTROLLER')

    def test_strict_trigger_thresholds(self):
        low=.02+.02; high=.09-.02
        self.assertEqual(core.gov_multiplier(low),1)
        self.assertEqual(core.gov_multiplier(high),1)
        self.assertEqual(core.gov_multiplier(math.nextafter(low,0)),.9)
        self.assertEqual(core.gov_multiplier(math.nextafter(high,math.inf)),1.1)

    def test_literal_weights_not_normalized(self):
        ratios=[0.,.3,.2]
        w=core.weight_sums(ratios)
        out=core.portfolio([.09]*3,ratios)
        self.assertEqual(w[0],1);self.assertLess(w[1],1)
        self.assertAlmostEqual(out[1],.09*w[1])

    def test_lag_changes_price_object(self):
        old=core.portfolio([.09,.04],[0.,.2])
        new=core.portfolio([.03,.05],[0.,.2])
        self.assertEqual(old[0],.09);self.assertEqual(new[0],.03)
        self.assertNotEqual(old,new)

    def test_profit_floor_and_raw_vs_clip(self):
        r=core.raw_prices(100.,100.,10.,1.2,.5,rk=.2)
        self.assertEqual(r['profit'],0);self.assertEqual(r['ra0'],.2-.025)
        self.assertEqual(r['ra'],.09);self.assertGreater(r['wt0'],r['wjt'])

    def test_missing_steps_break_contact_spell(self):
        r=core.spell([(2,True),(3,True),(5,True),(6,False),(7,True)])
        self.assertEqual(r['longest_confirmed'],2);self.assertEqual(r['contacts'],4)

    def test_no_production_import_or_scientific_call(self):
        forbidden={'evaluate_firm','run_online_stationary','run_source_faithful_one_turn',
                   'solve','spsolve','root','fsolve','load_GDPdata','entry_states','solve_matlab_faithful_hjb'}
        for file in ('core.py','audit.py'):
            tree=ast.parse((DIR/file).read_text(encoding='utf-8'))
            for node in ast.walk(tree):
                if isinstance(node,ast.ImportFrom):
                    self.assertFalse((node.module or '').startswith(('ch5_two_asset_hank','exports','validators')))
                if isinstance(node,ast.Call):
                    name=node.func.id if isinstance(node.func,ast.Name) else node.func.attr if isinstance(node.func,ast.Attribute) else ''
                    self.assertNotIn(name,forbidden)

    def test_domains_are_not_aliased(self):
        spec=importlib.util.spec_from_file_location('audit_module',DIR/'audit.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        row=module.prices({'rah':.09,'w':16.82},{'rah':'CAPTURED','w':'CAPTURED'},'household_entry')
        self.assertEqual(row['rah_constraint'],'DESCRIPTIVE_FIRM_RANGE_ONLY')
        self.assertEqual(row['w_constraint'],'COMPOSITE_NO_FIRM_CLIP')
        self.assertEqual(row['ra_status'],'MISSING')


if __name__=='__main__':unittest.main(verbosity=2)
