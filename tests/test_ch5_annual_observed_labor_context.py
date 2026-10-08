"""One bundled invented-fixture test invocation; no model or observed loader calls."""
import ast
from dataclasses import replace
import hashlib
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


def direct(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


context = direct('annual_context_test', 'src/ch5_two_asset_hank/corrected_diagnostic/annual_observed_labor_context.py')
seam = direct('annual_seam_test', 'validators/multi_province/annual_observed_labor_diagnostic/integration.py')
AXIS = ((1, 'Invented Low'), (2, 'Invented High'), (3, 'Invented Middle'))


def fixture(**changes):
    d = dict(schema='CH5_INVENTED_ANNUAL_FIXTURE_V1', input_kind='synthetic',
        target_year=2018, observation_year=2017, province_axis=[list(r) for r in AXIS],
        price_basis='synthetic_fixture', price_verified=False,
        records=[[1, 2017, 3, 2], [2, 2017, 11, 2], [3, 2017, 7, 2]])
    d.update(changes)
    raw = json.dumps(d).encode()
    return raw, hashlib.sha256(raw).hexdigest().upper()


class AnnualTests(unittest.TestCase):
    def setUp(self):
        raw, sha = fixture()
        self.ctx = context.prepare_synthetic_context(raw, expected_fixture_sha256=sha,
                                                     province_axis=AXIS, target_year=2018)
        self.events = []
        self.seen = []
        def factory(**kwargs):
            self.events.append('inputs'); return SimpleNamespace(**kwargs)
        def labor(inputs):
            self.events.append('labor'); self.seen.append(inputs.phi_destination_origin)
            return SimpleNamespace(lt_supply=(1, 2, 3))
        def firms(inputs, migration, shares, sha):
            self.events.append('firms'); return tuple(SimpleNamespace(wjt=i + 5) for i in range(3))
        def wages(provinces, firm_wages, phi, distance, *, phi_l, alphal):
            self.events.append('wages'); self.seen.append(phi); return (8, 9, 10)
        self.spies = seam.SyntheticSpies(factory, labor, firms, wages)

    def run_seam(self, **changes):
        states = changes.pop('states', tuple(dict(N=10+i, wjt=2+i, tau=.1,
            province_index=AXIS[i][0],source_province_name=AXIS[i][1]) for i in range(3)))
        kw = dict(annual_context=self.ctx, target_year=2018, province_axis=AXIS,
            source_sha256=self.ctx.source_sha256, input_kind='synthetic',
            price_basis='synthetic_fixture', price_verified=False,
            params={'ga': 2., 'phi_l': 5., 'alphal': 1., 'other': 99},
            migration_wedge_destination_origin=((0, 1, 2), (3, 0, 4), (5, 6, 0)),
            spies=self.spies)
        kw.update(changes)
        return seam.integrate_turn(None, None, None, 5,
            states,
            SimpleNamespace(ct=(1, 2, 3)), ((1, 0, 0),)*3, 'fixture_share', {}, [], **kw)

    def test_orientation_and_diagonal(self):
        p = self.ctx.phi_destination_origin
        self.assertLess(p[1][0], 1); self.assertGreater(p[0][1], 1)
        self.assertEqual(tuple(p[i][i] for i in range(3)), (1., 1., 1.))
        self.assertTrue(all(.7 < v < 1.3 for row in p for v in row))

    def test_shared_immutable_object_and_stage(self):
        result = self.run_seam()
        self.assertIs(self.seen[0], self.seen[1]); self.assertIs(self.seen[0], self.ctx.wedge.coefficients)
        with self.assertRaises(TypeError): self.seen[0][0][1] = 7
        self.assertEqual(self.events, ['inputs', 'labor', 'firms', 'wages'])
        self.assertFalse(result['full_outer_runtime_integrated']); self.assertFalse(result['model_activation'])

    def test_same_year_reuse_without_endogenous_state(self):
        a, b = self.run_seam(), self.run_seam(states=tuple(dict(N=20+i,wjt=40+i,tau=.2,Yt=999,Lt=1,
            province_index=AXIS[i][0],source_province_name=AXIS[i][1]) for i in range(3)))
        self.assertIs(a['annual_context'], b['annual_context'])
        self.assertIs(a['inputs'].phi_destination_origin, b['inputs'].phi_destination_origin)

    def test_year_failure_before_spies(self):
        with self.assertRaises(ValueError): self.run_seam(target_year=2019)
        self.assertEqual(self.events, [])

    def test_axis_failure_before_spies(self):
        with self.assertRaises(ValueError): self.run_seam(province_axis=AXIS[::-1])
        with self.assertRaises(ValueError): self.run_seam(province_axis=((1,'Other'),)+AXIS[1:])
        self.assertEqual(self.events, [])

    def test_source_failure_before_spies(self):
        with self.assertRaises(ValueError): self.run_seam(source_sha256='0'*64)
        self.assertEqual(self.events, [])

    def test_swapped_state_rows_rejected_before_spies(self):
        rows=tuple(dict(N=10+i,wjt=2+i,tau=.1,province_index=AXIS[i][0],source_province_name=AXIS[i][1]) for i in range(3))
        with self.assertRaises(ValueError): self.run_seam(states=rows[::-1])
        self.assertEqual(self.events, [])

    def test_metadata_failures_before_spies(self):
        for kw in ({'input_kind':'observed'}, {'price_basis':'current_price'}, {'price_verified':True}):
            with self.assertRaises(ValueError): self.run_seam(**kw)
        self.assertEqual(self.events, [])

    def test_context_replacement_does_not_change_binding(self):
        bad = replace(self.ctx, source_sha256='0'*64)
        with self.assertRaises(ValueError): self.run_seam(annual_context=bad, source_sha256='0'*64)
        self.assertEqual(self.events, [])

    def test_fake_or_mutable_context_rejected(self):
        fake = SimpleNamespace(validate=lambda **_:None, input_kind='synthetic', phi_destination_origin=[[1.]])
        with self.assertRaises(ValueError): self.run_seam(annual_context=fake)
        bad = replace(self.ctx, phi_destination_origin=[list(r) for r in self.ctx.phi_destination_origin])
        with self.assertRaises(ValueError): self.run_seam(annual_context=bad)
        self.assertEqual(self.events, [])
        with self.assertRaises(ValueError):
            context.AnnualContext(self.ctx.target_year,self.ctx.observation_year,AXIS,
                self.ctx.source_sha256,'synthetic','synthetic_fixture',False,
                self.ctx.provenance,self.ctx.wedge,self.ctx.phi_destination_origin)

    def test_wedge_and_nested_provenance_corruption_rejected(self):
        wrong_binding=replace(self.ctx.wedge.binding,population_basis='annual_average')
        for bad in (replace(self.ctx,provenance=(('mutable',{}),)),
                    replace(self.ctx,wedge=replace(self.ctx.wedge,observation_year=2016)),
                    replace(self.ctx,wedge=replace(self.ctx.wedge,binding=wrong_binding))):
            with self.assertRaises(ValueError): self.run_seam(annual_context=bad)
        self.assertEqual(self.events,[])

    def test_replace_coefficients_and_empty_provenance_rejected(self):
        altered=tuple(tuple(1.+(v-1.)*.5 for v in row) for row in self.ctx.phi_destination_origin)
        wedge=replace(self.ctx.wedge,coefficients=altered)
        for bad in (replace(self.ctx,wedge=wedge,phi_destination_origin=altered),
                    replace(self.ctx,provenance=())):
            with self.assertRaises(ValueError): self.run_seam(annual_context=bad)
        self.assertEqual(self.events,[])

    def test_fixture_hash_and_metadata(self):
        raw, sha = fixture()
        with self.assertRaises(ValueError): context.prepare_synthetic_context(raw, expected_fixture_sha256='0'*64, province_axis=AXIS, target_year=2018)
        for change in ({'input_kind':'observed'}, {'price_basis':'current_price_methodologically_attributed'}, {'observation_year':2016}):
            raw, sha = fixture(**change)
            with self.assertRaises(ValueError): context.prepare_synthetic_context(raw, expected_fixture_sha256=sha, province_axis=AXIS, target_year=2018)

    def test_production_fixed_pins_reject_fixture_bundle(self):
        raw, _ = fixture()
        with self.assertRaises(ValueError): context.authenticate_observed_binding({k:raw for k in context.PINS})
        with self.assertRaises(TypeError): context.PINS['manifest'] = '0'*64
        self.assertEqual(self.events, [])

    def test_provenance_retained(self):
        self.assertEqual(self.ctx.provenance, (('fixture_sha256',self.ctx.source_sha256),))
        self.assertEqual(self.ctx.observation_year, 2017)
        self.assertEqual(self.ctx.wedge.binding.population_basis, 'year_end_resident')

    def test_static_actual_seam_and_no_scientific_imports(self):
        old = ast.parse((ROOT/'validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py').read_text(encoding='utf-8-sig'))
        new_text = (ROOT/'validators/multi_province/annual_observed_labor_diagnostic/integration.py').read_text(encoding='utf-8')
        new = ast.parse(new_text)
        funcs = [next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name=='integrate_turn') for tree in (old,new)]
        self.assertEqual([a.arg for a in funcs[0].args.args], [a.arg for a in funcs[1].args.args])
        self.assertIn('annual_context', [a.arg for a in funcs[1].args.kwonlyargs])
        self.assertNotIn('_one_turn_inputs',new_text); self.assertNotIn('Yt',new_text)
        calls = lambda tree, name: [n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr==name]
        self.assertEqual({k.arg for k in calls(old,'MigrationLaborInputs')[0].keywords},
                         {k.arg for k in calls(new,'migration_inputs_factory')[0].keywords})
        self.assertEqual({k.arg for k in calls(old,'composite_household_wages')[0].keywords},
                         {k.arg for k in calls(new,'composite_household_wages')[0].keywords})
        self.assertEqual(len(calls(old,'composite_household_wages')[0].args),len(calls(new,'composite_household_wages')[0].args))
        prep_tree=ast.parse((ROOT/'src/ch5_two_asset_hank/corrected_diagnostic/annual_observed_labor_context.py').read_text(encoding='utf-8'))
        prep=next(n for n in prep_tree.body if isinstance(n,ast.FunctionDef) and n.name=='prepare_synthetic_context')
        self.assertEqual(len(calls(prep,'build_annual_labor_wedge')),1)
        self.assertEqual(len(calls(new,'build_annual_labor_wedge')),0)
        for tree in (new, prep_tree):
            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom): self.assertNotIn('ch5_two_asset_hank',node.module or '')


if __name__ == '__main__':
    unittest.main(verbosity=2)
