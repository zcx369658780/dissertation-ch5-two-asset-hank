"""Review-first synthetic seam tests. No CLI data path or production consumer.

Future invocation: python -I -S -B tests/test_fixed_c8_external_axis_synthetic.py
Loads four exact project source files by path, bypassing all package __init__.
This file has been prepared only; do not execute before independent review.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from dataclasses import replace
from types import SimpleNamespace
import unittest

ROOT = Path(__file__).resolve().parents[1]
SEAM = ROOT / 'validators/multi_province/annual_observed_labor_diagnostic'
CONTEXT = ROOT / 'src/ch5_two_asset_hank/corrected_diagnostic/annual_observed_labor_context.py'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


binding = load('_c8_axis_binding_test', SEAM / 'fixed_c8_input_binding.py')
integration = load('_c8_axis_integration_test', SEAM / 'integration.py')
context = load('_c8_axis_context_test', CONTEXT)


def no_observed(*args, **kwargs):
    raise AssertionError('observed/raw data entry is outside this test')


# Disable real-source entry points on this test's private module instance.
# No production module, package initializer, adapter or middle stage is loaded.
for name in ('authenticate_observed_binding', 'prepare_observed_context',
             'prepare_observed_data_only_context', '_prepare_authenticated_observed_context',
             '_preload_data_only_helper'):
    setattr(context, name, no_observed)

AXIS = ((1, 'Invented Alpha Province'), (2, 'Invented Beta Province'))
MODEL = ((0, 'Alpha'), (1, 'Beta'))
MAPPING = ((0, 'Alpha', 1, AXIS[0][1]), (1, 'Beta', 2, AXIS[1][1]))
UNITS = tuple((key, 'invented_unit') for key in binding.REQUIRED_UNITS if key != 'S') + (('S', 'dimensionless'),)


class SyntheticAxisTests(unittest.TestCase):
    def setUp(self):
        fixture = {
            'schema': 'CH5_INVENTED_ANNUAL_FIXTURE_V1', 'input_kind': 'synthetic',
            'province_axis': [list(row) for row in AXIS], 'target_year': 2018,
            'observation_year': 2017, 'price_basis': 'synthetic_fixture',
            'price_verified': False, 'records': [[1, 2017, 2.0, 4.0], [2, 2017, 3.0, 4.0]],
        }
        raw = json.dumps(fixture).encode('utf-8')
        self.sha = hashlib.sha256(raw).hexdigest().upper()
        self.annual = context.prepare_synthetic_context(raw,
            expected_fixture_sha256=self.sha, province_axis=AXIS, target_year=2018)
        # Source order deliberately differs from internal order; IDs have a gap.
        self.source = binding.ExternalSourceAxis('invented_fixture', self.sha,
            'synthetic_identifier', ((907, AXIS[1][1]), (101, AXIS[0][1])))
        self.states = tuple({'name': short, 'province_index': index,
            'source_province_name': AXIS[index][1], 'N': 4.0, 'wjt': 2.0,
            'tau': .1, 'payload': object()} for index, short in MODEL)
        self.shares = ((.8, .2), (.2, .8))
        self.batch = SimpleNamespace(ct=(1.0, 2.0), household_lt=object(),
            at=object(), bt=object(), at_tax=object())
        declarations = tuple(binding.InputDeclaration(MODEL, AXIS, stage, UNITS,
            self.source) for stage in binding.STAGES)
        self.bound = binding.FixedC8InputBinding(self.states, self.shares, self.batch,
            *declarations, MAPPING, ((0, 101, AXIS[0][1]), (1, 907, AXIS[1][1])))
        self.ledger = {'source_faithful_labor_reconstructions': 0,
                       'composite_wage_batches': 0, 'synthetic_marker': 'unchanged'}
        self.calls = []
        self.seen = []
        def factory(**kwargs):
            self.calls.append('factory')
            return kwargs
        def reconstruct(value):
            self.calls.append('migration')
            return value
        def firm(inputs, migration, shares, expected_sha):
            self.calls.append('firm')
            self.seen.append(inputs)
            self.assertIs(inputs.household_outputs, self.batch)
            self.assertIs(shares, self.shares)
            self.assertIs(inputs.phi_destination_origin, self.annual.phi_destination_origin)
            return (SimpleNamespace(wjt=2.0), SimpleNamespace(wjt=3.0))
        def wages(provinces, firm_wages, phi, distance, **kwargs):
            self.calls.append('wages')
            self.assertIs(phi, self.annual.phi_destination_origin)
            return ('invented wages',)
        self.spies = integration.SyntheticSpies(factory, reconstruct, firm, wages)

    def invoke(self, **changes):
        args = dict(repository=None, task_root=None, turn_root=None, turn=8,
            states=self.states, batch=self.batch, frozen_shares=self.shares,
            expected_share_sha='synthetic-no-file', ledger=self.ledger, household_rows=(),
            annual_context=self.annual, target_year=2018, province_axis=AXIS,
            source_sha256=self.sha, input_kind='synthetic', price_basis='synthetic_fixture',
            price_verified=False, params={'ga': .5, 'phi_l': 1.0, 'alphal': .5},
            migration_wedge_destination_origin=((1.0, 2.0), (3.0, 1.0)),
            spies=self.spies, fixed_c8_binding=self.bound,
            fixed_c8_external_source=self.source)
        args.update(changes)
        return integration.integrate_turn(**args)

    def rejected(self, *, expected_message='.+', **changes):
        self.calls.clear()
        ledger = changes.get('ledger', self.ledger)
        before = dict(ledger)
        with self.assertRaisesRegex(ValueError, expected_message):
            self.invoke(**changes)
        self.assertEqual(ledger, before, 'the passed ledger must remain unchanged')
        self.assertEqual(self.calls, [], 'rejection must precede every consumer spy')

    def test_correct_explicit_join_preserves_objects_values_and_axes(self):
        before = tuple(dict(row) for row in self.states)
        result = self.invoke()
        self.assertEqual(self.calls, ['factory', 'migration', 'firm', 'wages'])
        self.assertEqual(self.states, before)
        for index, view in enumerate(result['inputs'].old_provinces):
            self.assertIs(view['_fixed_c8_original_state'], self.states[index])
            self.assertIs(view['payload'], self.states[index]['payload'])
            self.assertEqual(view['_fixed_c8_model_identity'], MODEL[index])
            self.assertEqual(view['province_index'], index + 1)
            self.assertEqual(view['source_province_name'], AXIS[index][1])
        self.assertFalse(result['model_activation'])
        self.assertFalse(result['full_outer_runtime_integrated'])
        self.assertEqual(self.source.axis[0][0], 907)

    def test_reject_axis_order_code_name_and_duplicates(self):
        bad_sources = (
            replace(self.source, axis=tuple(reversed(self.source.axis))),
            replace(self.source, axis=((908, AXIS[1][1]), (101, AXIS[0][1]))),
            replace(self.source, axis=((907, ''), (101, AXIS[0][1]))),
            replace(self.source, axis=((101, AXIS[1][1]), (101, AXIS[0][1]))),
            replace(self.source, identifier_kind='administrative_code'),
        )
        for source in bad_sources:
            with self.subTest(source=source):
                self.rejected(fixed_c8_external_source=source)
        self.rejected(province_axis=tuple(reversed(AXIS)))
        self.rejected(fixed_c8_binding=replace(self.bound,
            external_mapping=((0, 907, AXIS[0][1]), (1, 101, AXIS[1][1]))))
        self.rejected(fixed_c8_binding=replace(self.bound, province_mapping=tuple(reversed(MAPPING))))
        # Consistent repetition of a missing name still fails full-name coverage.
        source = replace(self.source, axis=((907, 'Invented Missing'), (101, AXIS[0][1])))
        declarations = tuple(replace(d, external_source=source) for d in (
            self.bound.state_declaration, self.bound.share_declaration, self.bound.household_declaration))
        self.rejected(fixed_c8_external_source=source, fixed_c8_binding=replace(self.bound,
            state_declaration=declarations[0], share_declaration=declarations[1],
            household_declaration=declarations[2]))

    def test_reject_equal_value_identifier_type_substitution(self):
        for field in ('state_declaration', 'share_declaration', 'household_declaration'):
            declaration = getattr(self.bound, field)
            bad = replace(self.source, axis=((907, AXIS[1][1]), (101.0, AXIS[0][1])))
            with self.subTest(component=field, replacement='float101/int101'):
                self.rejected(fixed_c8_binding=replace(self.bound,
                    **{field: replace(declaration, external_source=bad)}))
        self.rejected(fixed_c8_binding=replace(self.bound,
            external_mapping=((0, 101.0, AXIS[0][1]), (1, 907, AXIS[1][1]))))
        # Use a valid integer-1 source to expose True == 1, changing one component.
        source_one = replace(self.source, axis=((907, AXIS[1][1]), (1, AXIS[0][1])))
        bound_one = replace(self.bound,
            state_declaration=replace(self.bound.state_declaration, external_source=source_one),
            share_declaration=replace(self.bound.share_declaration, external_source=source_one),
            household_declaration=replace(self.bound.household_declaration, external_source=source_one),
            external_mapping=((0, 1, AXIS[0][1]), (1, 907, AXIS[1][1])))
        for field in ('state_declaration', 'share_declaration', 'household_declaration'):
            declaration = getattr(bound_one, field)
            bad = replace(source_one, axis=((907, AXIS[1][1]), (True, AXIS[0][1])))
            with self.subTest(component=field, replacement='boolTrue/int1'):
                self.rejected(fixed_c8_external_source=source_one,
                    fixed_c8_binding=replace(bound_one,
                        **{field: replace(declaration, external_source=bad)}))
        self.rejected(fixed_c8_external_source=source_one, fixed_c8_binding=replace(bound_one,
            external_mapping=((0, True, AXIS[0][1]), (1, 907, AXIS[1][1]))))
        self.rejected(fixed_c8_binding=replace(self.bound,
            external_mapping=((False, 101, AXIS[0][1]), (1, 907, AXIS[1][1]))))

    def test_reject_source_conflicts(self):
        for source in (replace(self.source, source_sha256='0' * 64),
                       replace(self.source, source_identifier='purchased_employment_table')):
            declarations = tuple(replace(d, external_source=source) for d in (
                self.bound.state_declaration, self.bound.share_declaration, self.bound.household_declaration))
            self.rejected(fixed_c8_external_source=source, fixed_c8_binding=replace(self.bound,
                state_declaration=declarations[0], share_declaration=declarations[1],
                household_declaration=declarations[2]))
        self.rejected(fixed_c8_binding=replace(self.bound, share_declaration=replace(
            self.bound.share_declaration, external_source=replace(self.source, source_sha256='0' * 64))))

    def test_reject_stage_and_unit_conflicts(self):
        for field in ('state_declaration', 'share_declaration', 'household_declaration'):
            declaration = getattr(self.bound, field)
            self.rejected(fixed_c8_binding=replace(self.bound,
                **{field: replace(declaration, stage='different_stage')}))
            bad_units = tuple((key, 'different_unit' if key == 'N' else unit) for key, unit in UNITS)
            self.rejected(fixed_c8_binding=replace(self.bound,
                **{field: replace(declaration, unit_contract=bad_units)}))

    def test_reject_replaced_objects_and_missing_binding(self):
        self.rejected(states=tuple(dict(row) for row in self.states))
        self.rejected(batch=SimpleNamespace(**vars(self.batch)))
        self.rejected(frozen_shares=tuple(list(self.shares)))
        self.rejected(fixed_c8_binding=None)
        self.rejected(fixed_c8_external_source=None)
        self.rejected(turn=5)

    def test_turn1_and_turn5_keep_existing_interface(self):
        annual_states = tuple(dict(row, province_index=index + 1) for index, row in enumerate(self.states))
        for turn in (1, 5):
            self.calls.clear()
            result = self.invoke(turn=turn, states=annual_states,
                fixed_c8_binding=None, fixed_c8_external_source=None)
            self.assertEqual(self.calls, ['factory', 'migration', 'firm', 'wages'])
            self.assertNotIn('_fixed_c8_original_state', result['inputs'].old_provinces[0])

    def test_observed_mode_is_rejected_by_context_metadata(self):
        # This checks metadata consistency, not reachability of the production guard.
        self.rejected(input_kind='observed', expected_message='annual provenance metadata mismatch')

    def test_qualified_synthetic_context_reaches_real_execution_guard(self):
        # A valid synthetic context passes validation; wrong spy type then hits
        # the actual integration guard. No observed context or consumer is loaded.
        for invalid_spies in (None, SimpleNamespace(**vars(self.spies))):
            self.rejected(spies=invalid_spies,
                expected_message='^production consumers blocked pending science/Objective A contracts$')


if __name__ == '__main__':
    if len(sys.argv) != 1:
        raise SystemExit('This synthetic test accepts no arguments or input files.')
    unittest.main(verbosity=2)
