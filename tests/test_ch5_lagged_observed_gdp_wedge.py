"""Synthetic engineering fixtures only; never reads an observed GDP panel."""
import ast
from dataclasses import FrozenInstanceError, replace
import importlib.util
from pathlib import Path
import sys
import unittest

HELPER = Path(__file__).resolve().parents[1] / 'src/ch5_two_asset_hank/corrected_diagnostic/lagged_observed_gdp_wedge.py'
spec = importlib.util.spec_from_file_location('isolated_lagged_wedge_candidate', HELPER)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
R, B = module.GDPRecord, module.ProvenanceBinding


class WedgeTests(unittest.TestCase):
    def setUp(self):
        self.records = [R(1, 2019, 1, 1), R(2, 2019, 3, 1)]
        self.binding = B('synthetic', 'synthetic-fixture-engineering-only', 'a' * 64,
                         'year_end_resident', 'synthetic_fixture', False)

    def build(self, records=None, **kwargs):
        args = dict(target_year=2020, province_order=[1, 2], binding=self.binding)
        args.update(kwargs)
        return module.build_annual_labor_wedge(self.records if records is None else records, **args)

    def test_known_direction_and_units(self):
        result = self.build()
        self.assertEqual(result.per_capita_gdp, (10000., 30000.))
        self.assertEqual(result.coefficients, ((1., 1.15), (.85, 1.)))
        self.assertEqual((result.target_year, result.observation_year), (2020, 2019))

    def test_axis_order_and_diagonal(self):
        result = self.build(list(reversed(self.records)), province_order=[2, 1])
        self.assertEqual(result.province_order, (2, 1))
        self.assertEqual(result.coefficients, ((1., .85), (1.15, 1.)))
        for i in range(2):
            self.assertEqual(result.coefficients[i][i], 1.)

    def test_scaling_and_interval(self):
        scaled = [replace(r, gdp_raw_100m_yuan=r.gdp_raw_100m_yuan * 8) for r in self.records]
        self.assertEqual(self.build(scaled).coefficients, self.build().coefficients)
        for amplitude in (.1, .3, .9):
            for row in self.build(amplitude=amplitude).coefficients:
                for coefficient in row:
                    self.assertTrue(1-amplitude < coefficient < 1+amplitude)

    def test_immutable_snapshots(self):
        order = [1, 2]
        records = self.records.copy()
        result = self.build(records, province_order=order)
        records.clear()
        order.reverse()
        self.assertEqual(result.province_order, (1, 2))
        self.assertEqual(result.per_capita_gdp, (10000., 30000.))
        for obj, attribute in ((result, 'amplitude'), (result.binding, 'source_identifier'), (self.records[0], 'observation_year')):
            with self.assertRaises(FrozenInstanceError):
                setattr(obj, attribute, 0)
        with self.assertRaises(TypeError):
            result.coefficients[0][0] = 0

    def test_province_coverage(self):
        for records in ([], self.records[:1], self.records + [self.records[0]], self.records + [R(3, 2019, 1, 1)]):
            with self.subTest(records=records), self.assertRaises(ValueError):
                self.build(records)
        for order in ([], [1, 1], [1, 3], [True, 2], [0, 2], [1., 2], ['1', 2]):
            with self.subTest(order=order), self.assertRaises(ValueError):
                self.build(province_order=order)

    def test_ids_years_and_record_types(self):
        for province in (True, 0, -1, 1., '1', None):
            with self.subTest(province=province), self.assertRaises(ValueError):
                self.build([replace(self.records[0], province_index=province), self.records[1]])
        for year in (True, 0, 10000, 2018, 2020, 2019., '2019', None):
            with self.subTest(year=year), self.assertRaises(ValueError):
                self.build([replace(self.records[0], observation_year=year), self.records[1]])
        for year in (True, 1, 10000, 2020., '2020', None):
            with self.subTest(target=year), self.assertRaises(ValueError):
                self.build(target_year=year)
        with self.assertRaises(ValueError):
            self.build([None, self.records[1]])

    def test_invalid_numerics_and_amplitudes(self):
        invalid = (True, False, None, '1', 0, -1, float('nan'), float('inf'), -float('inf'), 10**400)
        for field in ('gdp_raw_100m_yuan', 'population_raw_10k_persons'):
            for value in invalid:
                with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                    self.build([replace(self.records[0], **{field: value}), self.records[1]])
        for amplitude in invalid + (1, 2):
            with self.subTest(amplitude=amplitude), self.assertRaises(ValueError):
                self.build(amplitude=amplitude)

    def test_provenance_allowlists(self):
        edits = [('input_kind', 'unknown'), ('source_identifier', ''), ('source_identifier', ' '),
                 ('source_identifier', None), ('source_sha256', 'g'*64), ('source_sha256', 'a'*63),
                 ('source_sha256', None), ('population_basis', 'model_population'),
                 ('price_verified', 0), ('price_verified', 1), ('price_verified', True),
                 ('price_basis', 'current_price'), ('price_base_year', 2010)]
        for field, value in edits:
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                self.build(binding=replace(self.binding, **{field: value}))
        with self.assertRaises(ValueError):
            self.build(binding=None)

    def test_hypothetical_observed_metadata_only(self):
        # Invented numbers and explicit fixture identifier: validates metadata branches only.
        observed = replace(self.binding, input_kind='observed', price_basis='current_price', price_verified=True)
        self.assertEqual(self.build(binding=observed).binding, observed)
        constant = replace(observed, price_basis='constant_price', price_base_year=2010)
        self.assertEqual(self.build(binding=constant).binding, constant)
        for changes in ({'price_verified': False}, {'price_verified': 1}, {'price_basis': 'unknown'},
                        {'price_basis': 'synthetic_fixture'}, {'price_base_year': 2010}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.build(binding=replace(observed, **changes))
        for year in (None, True, 0, -1, 10000, 2010., '2010'):
            with self.subTest(base=year), self.assertRaises(ValueError):
                self.build(binding=replace(constant, price_base_year=year))

    def test_enum_fields_reject_mutable_equality_objects_and_string_subclasses(self):
        class MutableEquality:
            def __init__(self, value):
                self.value = value
                self.comparisons = 0

            def __eq__(self, other):
                self.comparisons += 1
                return self.value == other

        class StringSubclass(str):
            pass

        for field in ('input_kind', 'population_basis', 'price_basis'):
            fake = MutableEquality(getattr(self.binding, field))
            with self.subTest(field=field, kind='mutable'), self.assertRaisesRegex(ValueError, 'built-in strings'):
                self.build(binding=replace(self.binding, **{field: fake}))
            self.assertEqual(fake.comparisons, 0)
            fake.value = 'changed-after-rejection'
            with self.subTest(field=field, kind='str-subclass'), self.assertRaisesRegex(ValueError, 'built-in strings'):
                self.build(binding=replace(self.binding, **{field: StringSubclass(getattr(self.binding, field))}))

    def test_near_equal_income_rejects_direction_rounding_collapse(self):
        records = [R(1, 2019, 1.0, 1), R(2, 2019, 1.0000000000000002, 1)]
        for order in ([1, 2], [2, 1]):
            with self.subTest(order=order), self.assertRaisesRegex(ValueError, 'strict income direction'):
                self.build(records, province_order=order)

    def test_extreme_representable_per_capita(self):
        for scale in (1e305, 1e-300):
            self.assertEqual(self.build([R(1, 2019, scale, scale)], province_order=[1]).per_capita_gdp, (10000.,))

    def test_final_overflow_underflow_and_coefficient_endpoints(self):
        for gdp, population in ((1e308, 1e-300), (5e-324, 1e308)):
            with self.subTest(gdp=gdp), self.assertRaises(ValueError):
                self.build([R(1, 2019, gdp, population)], province_order=[1])
        with self.assertRaises(ValueError):
            self.build([R(1, 2019, 1e-300, 1), R(2, 2019, 1e300, 1)])
        with self.assertRaises(ValueError):
            self.build(amplitude=5e-324)

    def test_import_surface(self):
        tree = ast.parse(HELPER.read_text(encoding='utf-8'))
        imports = {node.module if isinstance(node, ast.ImportFrom) else alias.name
                   for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))
                   for alias in node.names}
        self.assertEqual(imports, {'dataclasses', 'fractions', 'math', 're'})
        self.assertFalse(any(name == 'ch5_two_asset_hank' or name.startswith('ch5_two_asset_hank.') for name in sys.modules))


if __name__ == '__main__':
    unittest.main(verbosity=2)
