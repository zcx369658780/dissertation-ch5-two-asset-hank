"""Invented engineering fixtures and hypothetical metadata; no observed data reads."""
from dataclasses import FrozenInstanceError, replace
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / 'src/ch5_two_asset_hank/corrected_diagnostic/lagged_observed_gdp_wedge.py'
LEGACY_TEST = ROOT / 'tests/test_ch5_lagged_observed_gdp_wedge.py'


def direct_load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


module = direct_load('isolated_methodological_price_binding_candidate', HELPER)
legacy = direct_load('isolated_legacy_wedge_regression_tests', LEGACY_TEST)
R, B = module.GDPRecord, module.ProvenanceBinding


class MethodologicalPriceBindingTests(unittest.TestCase):
    def setUp(self):
        self.records = [R(1, 2019, 1, 1), R(2, 2019, 3, 1)]
        self.binding = B(
            'observed', 'hypothetical-methodological-metadata-invented-fixture-only',
            'a' * 64, 'year_end_resident',
            'current_price_methodologically_attributed', False,
            price_attribution_sha256='b' * 64,
        )

    def build(self, binding=None, **kwargs):
        args = dict(target_year=2020, province_order=[1, 2],
                    binding=self.binding if binding is None else binding)
        args.update(kwargs)
        return module.build_annual_labor_wedge(self.records, **args)

    def test_legacy_suite_contains_all_fourteen_tests(self):
        self.assertEqual(unittest.defaultTestLoader.loadTestsFromModule(legacy).countTestCases(), 14)

    def test_hypothetical_method_route_direction_units_and_axes(self):
        result = self.build()
        self.assertEqual(result.per_capita_gdp, (10000., 30000.))
        self.assertEqual(result.coefficients, ((1., 1.15), (.85, 1.)))
        self.assertEqual((result.target_year, result.observation_year), (2020, 2019))
        reversed_result = self.build(province_order=[2, 1])
        self.assertEqual(reversed_result.province_order, (2, 1))
        self.assertEqual(reversed_result.coefficients, ((1., .85), (1.15, 1.)))

    def test_metadata_retention_and_immutable_snapshot(self):
        result = self.build()
        self.assertEqual(result.binding, self.binding)
        self.assertIsNot(result.binding, self.binding)
        self.assertIs(result.binding.price_verified, False)
        self.assertEqual(result.binding.price_attribution_sha256, 'b' * 64)
        for field in self.binding.__dataclass_fields__:
            self.assertEqual(getattr(result.binding, field), getattr(self.binding, field))
        with self.assertRaises(FrozenInstanceError):
            result.binding.price_attribution_sha256 = 'c' * 64
        with self.assertRaises(FrozenInstanceError):
            result.binding.price_verified = True
        with self.assertRaises(TypeError):
            result.coefficients[0][0] = 0

    def test_attribution_accepts_builtin_mixed_case_hex_and_preserves_bytes(self):
        attribution = 'aB09' * 16
        binding = replace(self.binding, price_attribution_sha256=attribution)
        self.assertEqual(self.build(binding).binding.price_attribution_sha256, attribution)

    def test_missing_malformed_or_nonbuiltin_attribution_rejected(self):
        class StringSubclass(str):
            pass

        invalid = (None, '', 'a' * 63, 'a' * 65, 'g' * 64, ' ' + 'a' * 64,
                   'a' * 64 + '\n', True, False, 1, b'a' * 64,
                   StringSubclass('a' * 64), ['a' * 64], object())
        for attribution in invalid:
            with self.subTest(attribution=attribution), self.assertRaises(ValueError):
                self.build(replace(self.binding, price_attribution_sha256=attribution))

    def test_method_route_rejects_true_or_nonbool_verification(self):
        for flag in (True, 0, 1, None, 'False'):
            with self.subTest(flag=flag), self.assertRaises(ValueError):
                self.build(replace(self.binding, price_verified=flag))

    def test_method_route_rejects_every_base_year(self):
        for year in (2010, True, False, 0, -1, 10000, 2010., '2010'):
            with self.subTest(year=year), self.assertRaises(ValueError):
                self.build(replace(self.binding, price_base_year=year))

    def test_attribution_rejected_on_synthetic_and_direct_routes(self):
        routes = (
            replace(self.binding, input_kind='synthetic', price_basis='synthetic_fixture'),
            replace(self.binding, price_basis='current_price', price_verified=True),
            replace(self.binding, price_basis='constant_price', price_verified=True,
                    price_base_year=2010),
        )
        for route in routes:
            for attribution in ('b' * 64, '', False):
                with self.subTest(route=route.price_basis, attribution=attribution), self.assertRaises(ValueError):
                    self.build(replace(route, price_attribution_sha256=attribution))

    def test_method_basis_rejected_for_synthetic_or_unknown_input_kind(self):
        for kind in ('synthetic', 'unknown'):
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                self.build(replace(self.binding, input_kind=kind))
        for basis in ('unknown', 'synthetic_fixture'):
            with self.subTest(basis=basis), self.assertRaises(ValueError):
                self.build(replace(self.binding, price_basis=basis, price_verified=True))

    def test_old_positional_bindings_keep_optional_defaults(self):
        synthetic = B('synthetic', 'invented-synthetic-fixture-only', 'a' * 64,
                      'year_end_resident', 'synthetic_fixture', False)
        current = B('observed', 'hypothetical-direct-metadata-invented-fixture-only',
                    'a' * 64, 'year_end_resident', 'current_price', True)
        constant = B('observed', 'hypothetical-direct-metadata-invented-fixture-only',
                     'a' * 64, 'year_end_resident', 'constant_price', True, 2010)
        for binding in (synthetic, current, constant):
            with self.subTest(basis=binding.price_basis):
                self.assertIsNone(binding.price_attribution_sha256)
                self.assertEqual(self.build(binding).binding, binding)
        for binding in (current, constant):
            with self.subTest(basis=binding.price_basis), self.assertRaises(ValueError):
                self.build(replace(binding, price_verified=False))


def load_tests(loader, tests, pattern):
    tests.addTests(loader.loadTestsFromModule(legacy))
    return tests


if __name__ == '__main__':
    unittest.main(verbosity=2)
