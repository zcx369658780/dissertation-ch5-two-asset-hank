"""One changed-code regression process, invented fixtures only; no HANK imports."""
import ast
import copy
from dataclasses import replace
import importlib.abc
import importlib.util
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


class NoScientificImports(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split('.')[0] in {'ch5_two_asset_hank', 'scipy', 'validators'}:
            raise AssertionError('scientific package import forbidden: ' + fullname)
        return None


sys.meta_path.insert(0, NoScientificImports())
import numpy as np


def direct(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


old = direct('annual_changed_code_regression', 'tests/test_ch5_annual_observed_labor_context.py')
context, seam = old.context, old.seam
adapter = direct('annual_array_adapter_test', 'src/ch5_two_asset_hank/corrected_diagnostic/annual_labor_array_adapter.py')
AXIS = old.AXIS
MAPPING = ((1, AXIS[0][1], 'Low'), (2, AXIS[1][1], 'High'), (3, AXIS[2][1], 'Middle'))


class ArraySeamTests(unittest.TestCase):
    def setUp(self):
        raw, sha = old.fixture()
        self.ctx = context.prepare_synthetic_context(raw, expected_fixture_sha256=sha,
            province_axis=AXIS, target_year=2018)
        self.meta = dict(target_year=2018, province_axis=AXIS, source_sha256=sha,
            input_kind='synthetic', price_basis='synthetic_fixture', price_verified=False)
        self.carrier = adapter.prepare_annual_array(self.ctx, province_mapping=MAPPING, **self.meta)
        self.events, self.deliveries = [], []
        self.distance = ((0., 1., 2.), (3., 0., 4.), (5., 6., 0.))
        self.params = dict(ga=2., phi_l=5., alphal=1., other=99.)
        self.shares = ((1., 0., 0.), (0., 1., 0.), (0., 0., 1.))
        def factory(**kw):
            self.events.append('inputs')
            self.deliveries.append(kw['phi_destination_origin'])
            self.assertIs(kw['migration_wedge_destination_origin'], self.distance)
            self.assertEqual(kw['gamma_c'], self.params['ga'])
            self.assertEqual(kw['phi_l'], self.params['phi_l'])
            return SimpleNamespace(**kw)
        def labor(inputs):
            self.events.append('labor')
            return SimpleNamespace(lt_supply=(11., 22., 33.))
        def firms(inputs, migration, shares, sha):
            self.events.append('firms')
            self.assertEqual(inputs.province_order, ('Low', 'High', 'Middle'))
            self.assertEqual(tuple(row['name'] for row in inputs.old_provinces), inputs.province_order)
            self.assertEqual(tuple(row['source_province_name'] for row in inputs.old_provinces), tuple(r[1] for r in AXIS))
            self.assertEqual(dict(inputs.params), self.params)
            self.assertIs(shares, self.shares)
            self.assertEqual(sha, 'invented_share')
            return tuple(SimpleNamespace(wjt=w) for w in (4., 5., 6.))
        def wages(provinces, firm_wages, phi, distance, *, phi_l, alphal):
            self.events.append('wages')
            self.deliveries.append(phi)
            self.assertIs(distance, self.distance)
            self.assertEqual(firm_wages, [4., 5., 6.])
            self.assertEqual((phi_l, alphal), (5., 1.))
            return (101., 202., 303.)  # explicit invented origin order
        self.spies = seam.SyntheticSpies(factory, labor, firms, wages)

    def states(self):
        return tuple(dict(name=name, province_index=i, source_province_name=full,
            N=10.+i, wjt=2.+i, tau=.1, Yt=999., Lt=1.) for i, full, name in MAPPING)

    def run_seam(self, **changes):
        states = changes.pop('states', self.states())
        batch = changes.pop('batch', SimpleNamespace(ct=(1., 2., 3.)))
        kw = dict(annual_context=self.ctx, params=self.params,
            migration_wedge_destination_origin=self.distance, spies=self.spies,
            prepared_array=self.carrier, province_mapping=MAPPING, **self.meta)
        kw.update(changes)
        return seam.integrate_turn(None, None, None, 5, states,
            batch, self.shares, 'invented_share', {}, [], **kw)

    def test_single_construction_and_same_master_across_turns(self):
        helper = context._helper()
        with patch.object(helper, 'build_annual_labor_wedge', wraps=helper.build_annual_labor_wedge) as count:
            raw, sha = old.fixture()
            ctx = context.prepare_synthetic_context(raw, expected_fixture_sha256=sha,
                province_axis=AXIS, target_year=2018)
            carrier = adapter.prepare_annual_array(ctx, province_mapping=MAPPING, **self.meta)
            a = self.run_seam(annual_context=ctx, prepared_array=carrier)
            rows = self.states()
            rows[0]['Yt'] = 321.
            b = self.run_seam(annual_context=ctx, prepared_array=carrier, states=rows)
            self.assertEqual(count.call_count, 1)
        self.assertIs(a['annual_context'], b['annual_context'])
        self.assertTrue(all(item is carrier.phi_destination_origin for item in self.deliveries))
        self.assertEqual(self.events, ['inputs', 'labor', 'firms', 'wages'] * 2)
        self.assertEqual(a['wages'], (101., 202., 303.))
        self.assertFalse(a['model_activation'])
        self.assertFalse(a['full_outer_runtime_integrated'])

    def test_bytes_master_is_strong_immutable_and_exact(self):
        master = self.carrier.phi_destination_origin
        self.assertEqual(master.dtype, np.dtype('float64'))
        self.assertTrue(master.flags.c_contiguous)
        self.assertEqual(master.shape, (3, 3))
        self.assertFalse(master.flags.writeable)
        owner = master
        while isinstance(owner, np.ndarray):
            self.assertFalse(owner.flags.writeable)
            owner = owner.base
        self.assertIsInstance(owner, bytes)
        self.assertTrue(np.array_equal(master, np.asarray(self.ctx.wedge.coefficients)))
        self.assertLess(master[1, 0], 1.)
        self.assertGreater(master[0, 1], 1.)
        self.assertEqual(tuple(master.diagonal()), (1., 1., 1.))
        with self.assertRaises(ValueError): master[0, 0] = 3.
        with self.assertRaises(ValueError): master.setflags(write=True)
        with self.assertRaises(ValueError): master.base.setflags(write=True)

    def test_original_state_names_and_provenance_preserved(self):
        rows = self.states()
        original = tuple(dict(row) for row in rows)
        result = self.run_seam(states=rows)
        self.assertEqual(rows, original)
        records = result['inputs'].old_provinces
        self.assertIsInstance(records, tuple)
        self.assertEqual(tuple(row['name'] for row in records), ('Low', 'High', 'Middle'))
        with self.assertRaises(TypeError): records[0]['name'] = 'Renamed'

    def test_metadata_context_and_axis_refusal_before_spies(self):
        variants = [dict(target_year=2019), dict(province_axis=AXIS[::-1]),
            dict(source_sha256='0'*64), dict(input_kind='observed'),
            dict(price_basis='current_price'), dict(price_verified=True),
            dict(annual_context=replace(self.ctx)),
            dict(annual_context=SimpleNamespace(validate=lambda **_: None))]
        for changes in variants:
            with self.subTest(changes=changes):
                with self.assertRaises(ValueError): self.run_seam(**changes)
        self.assertEqual(self.events, [])

    def test_replaced_forged_transposed_and_mutable_carriers_refused(self):
        variants = [replace(self.carrier), copy.copy(self.carrier),
            replace(self.carrier, phi_destination_origin=self.carrier.phi_destination_origin.copy()),
            replace(self.carrier, phi_destination_origin=self.carrier.phi_destination_origin.T),
            replace(self.carrier, backing_bytes=bytearray(self.carrier.backing_bytes)),
            SimpleNamespace(validate=lambda **_: None)]
        for bad in variants:
            with self.assertRaises(ValueError): self.run_seam(prepared_array=bad)
        self.assertEqual(self.events, [])

    def test_state_types_missing_names_bool_and_order_refused(self):
        for key, val in [('name', AXIS[0][1]), ('name', 'High'), ('province_index', True),
                         ('source_province_name', 'Low')]:
            rows = self.states()
            rows[0][key] = val
            with self.assertRaises(ValueError): self.run_seam(states=rows)
        for key in ('name', 'source_province_name', 'province_index'):
            rows = self.states()
            del rows[0][key]
            with self.assertRaises(ValueError): self.run_seam(states=rows)
        with self.assertRaises(ValueError): self.run_seam(states=self.states()[::-1])
        with self.assertRaises(ValueError): self.run_seam(states=list(self.states()))
        self.assertEqual(self.events, [])

    def test_explicit_mapping_refusal(self):
        maps = [None, MAPPING[::-1], ((True, AXIS[0][1], 'Low'),)+MAPPING[1:],
            ((1, AXIS[0][1], 'High'),)+MAPPING[1:]]
        for mapping in maps:
            with self.assertRaises(ValueError): self.run_seam(province_mapping=mapping)
        with self.assertRaises(ValueError): self.run_seam(prepared_array=None)
        self.assertEqual(self.events, [])

    def test_pure_invented_record_conversion_and_refusal(self):
        rows = ((1, AXIS[0][1], 2017, 3, 2), (2, AXIS[1][1], 2017, 11, 2),
                (3, AXIS[2][1], 2017, 7, 2))
        records = context._records_to_gdp_records(rows, province_axis=AXIS, observation_year=2017)
        self.assertEqual(tuple(r.gdp_raw_100m_yuan for r in records), (3., 11., 7.))
        self.assertEqual(tuple(r.population_raw_10k_persons for r in records), (2., 2., 2.))
        for bad in (rows[::-1], ((True, AXIS[0][1], 2017, 3, 2),)+rows[1:],
                    ((1, AXIS[0][1], 2017, True, 2),)+rows[1:],
                    ((1, AXIS[0][1], 2016, 3, 2),)+rows[1:],
                    ((1, 'Other', 2017, 3, 2),)+rows[1:]):
            with self.assertRaises(ValueError):
                context._records_to_gdp_records(bad, province_axis=AXIS, observation_year=2017)

    def test_observed_constructor_replace_duck_rejected_without_authentication(self):
        forged = context.AuthenticatedObservedSnapshot(AXIS, (), ())
        for bad in (forged, replace(forged), copy.copy(forged), SimpleNamespace(province_axis=AXIS, raw_records=())):
            with self.assertRaises(ValueError): context._prepare_authenticated_observed_context(bad)
        raw, _ = old.fixture()
        with self.assertRaises(ValueError): context.prepare_observed_context({k: raw for k in context.PINS})
        self.assertFalse(any(name == 'ch5_two_asset_hank' or name.startswith('ch5_two_asset_hank.') for name in sys.modules))

    def test_literal_canonical_mapping_is_separate_from_numeric_fixture(self):
        mapping = adapter.CANONICAL_PROVINCE_MAPPING
        self.assertEqual(len(mapping), 31)
        self.assertEqual(tuple((i, full) for i, full, _ in mapping), context.CANONICAL_AXIS)
        tree = ast.parse((ROOT/'src/ch5_two_asset_hank/multi_province/province_contracts.py').read_text(encoding='utf-8-sig'))
        assign = next(n for n in tree.body if isinstance(n, ast.AnnAssign) and n.target.id == 'PROVINCE_ORDER')
        self.assertEqual(tuple(short for _, _, short in mapping), ast.literal_eval(assign.value))
        self.assertEqual(mapping[0], (1, '北京市', '北京'))
        self.assertEqual(mapping[-1], (31, '新疆维吾尔自治区', '新疆'))
        self.assertNotEqual(mapping[0][1], mapping[0][2])

    def test_dimensions_and_another_preparation_refused_before_spies(self):
        with self.assertRaises(ValueError):
            self.run_seam(migration_wedge_destination_origin=((1.,),))
        raw, sha = old.fixture()
        another = context.prepare_synthetic_context(raw, expected_fixture_sha256=sha,
            province_axis=AXIS, target_year=2018)
        with self.assertRaises(ValueError): self.run_seam(annual_context=another)
        self.assertEqual(self.events, [])
    def test_extra_dimensions_missing_params_and_master_metadata_refusal(self):
        for batch in (SimpleNamespace(ct=np.ones((3, 1))), SimpleNamespace(ct=((1.,), (2.,), (3.,)))):
            with self.assertRaises(ValueError): self.run_seam(batch=batch)
        for distance in (np.ones((3, 3, 2)), tuple(((1., 2.),) * 3 for _ in range(3))):
            with self.assertRaises(ValueError): self.run_seam(migration_wedge_destination_origin=distance)
        for key in ('ga', 'phi_l', 'alphal'):
            params = dict(self.params)
            del params[key]
            with self.assertRaises(ValueError): self.run_seam(params=params)
        self.carrier.phi_destination_origin.shape = (9,)
        with self.assertRaises(ValueError): self.run_seam()
        self.assertEqual(self.events, [])

    def test_wrong_firm_length_stops_before_wage_boundary(self):
        spies = seam.SyntheticSpies(self.spies.migration_inputs_factory,
            self.spies.reconstruct_migration_labor, lambda *args: (),
            self.spies.composite_household_wages)
        with self.assertRaises(ValueError): self.run_seam(spies=spies)
        self.assertEqual(self.events, ['inputs', 'labor'])
        self.assertEqual(len(self.deliveries), 1)
    def test_original_copy_contracts_static_only_and_no_package_imports(self):
        texts = [(ROOT/'src/ch5_two_asset_hank/multi_province'/name).read_text(encoding='utf-8-sig')
                 for name in ('one_turn.py', 'migration_labor.py', 'wage.py')]
        self.assertIn('copy=True', texts[0])
        self.assertIn('copy=True', texts[1])
        self.assertIn('np.asarray', texts[2])
        for relative in ('src/ch5_two_asset_hank/corrected_diagnostic/annual_labor_array_adapter.py',
                         'validators/multi_province/annual_observed_labor_diagnostic/integration.py'):
            tree = ast.parse((ROOT/relative).read_text(encoding='utf-8'))
            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom):
                    self.assertNotIn('ch5_two_asset_hank', node.module or '')
        self.assertFalse(any(name == 'scipy' or name.startswith('scipy.') for name in sys.modules))


def load_tests(loader, tests, pattern):
    bundled = unittest.TestSuite()
    bundled.addTests(loader.loadTestsFromTestCase(old.AnnualTests))
    bundled.addTests(loader.loadTestsFromTestCase(ArraySeamTests))
    return bundled


if __name__ == '__main__':
    unittest.main(verbosity=2)