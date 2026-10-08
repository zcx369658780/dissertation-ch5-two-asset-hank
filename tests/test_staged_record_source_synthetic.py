"""Pure synthetic record adapter tests integrated with the accepted A/A2 code."""

import ast
import builtins
import contextlib
import copy
import importlib.util
import io
import math
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parent.parent
MODULE_DIR = ROOT / 'validators' / 'multi_province' / 'annual_observed_labor_diagnostic'


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, MODULE_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


source_api = load('_a3_records', 'staged_record_source.py')
carrier_api = load('_a3_carrier', 'staged_frozen_carrier.py')
pipeline_api = load('_a3_pipeline', 'staged_frozen_pipeline.py')


def fixture():
    rows = [{'ext-ID': 700 - i, 'ext-name': f'neutral-{30 - i}', 'position': i,
             'value-Y': i + 0.125, 'value-X': 30 - i} for i in range(31)]
    rows[0]['value-Y'] = -0.0
    rows[1]['value-Y'] = 17
    rows[2]['value-Y'] = -2.5
    declarations = {
        'columns': {'source_id': 'ext-ID', 'name': 'ext-name', 'order': 'position',
                    'values': {'neutral_x': 'value-X', 'neutral_y': 'value-Y'}},
        'field_names': ['neutral_y', 'neutral_x'],
        'units': {'neutral_x': 'unit-X', 'neutral_y': 'unit-Y'},
        'calendar': {'target_year': 2018, 'observation_year': 2017, 'label': 'declared-only'},
        'source': {'source_id': 'synthetic-records', 'label': 'not-authenticated'},
    }
    expected = {
        'axes': [{'source_id': r['ext-ID'], 'name': r['ext-name'], 'order': r['position']}
                 for r in rows],
        **{k: copy.deepcopy(declarations[k]) for k in ('field_names', 'units', 'calendar', 'source')},
    }
    assert len(repr((rows, declarations, expected)).encode('utf-8')) < 1048576
    return rows, declarations, expected


class Integration:
    def __init__(self, rows=None, declarations=None):
        default_rows, default_declarations, self.expected = fixture()
        self.rows = default_rows if rows is None else rows
        self.declarations = default_declarations if declarations is None else declarations
        self.source = source_api.RecordSource(self.rows, **self.declarations)
        self.events, self.seen, self.handles = [], [], []

    def provide(self):
        self.events.append('provider')
        return self.source()

    def close_source(self):
        self.events.append('provider-close')
        self.source.close()

    def freeze(self, **payload):
        self.events.append('factory')
        return carrier_api.create_carrier(**payload)

    def handle_factory(self, carrier):
        self.events.append('handle-factory')
        handle = carrier_api.CarrierHandle(carrier)
        self.handles.append(handle)
        return handle

    def acquire(self, handle):
        self.events.append('acquire')
        return handle.acquire()

    def close_handle(self, handle):
        self.events.append('handle-close')
        handle.close()

    def first(self, carrier):
        self.events.append('first')
        self.seen.append(carrier)
        return tuple(v.values for v in carrier.vectors)

    def second(self, carrier):
        self.events.append('second')
        self.seen.append(carrier)
        return tuple(a.source_id for a in carrier.axes)

    def pipeline(self, **overrides):
        options = dict(provider=self.provide, provider_close=self.close_source,
                       carrier_factory=self.freeze, handle_factory=self.handle_factory,
                       handle_acquire=self.acquire, handle_close=self.close_handle,
                       expected=self.expected)
        options.update(overrides)
        return pipeline_api.SharedInputPipeline(**options)


class RecordSourceTests(unittest.TestCase):
    def assert_closed(self, case, pipeline):
        self.assertEqual(case.source.state, 'closed')
        self.assertEqual(case.source.close_count, 1)
        self.assertEqual(case.events.count('provider-close'), 1)
        self.assertEqual(pipeline.state, 'closed')
        self.assertTrue(all(h.closed for h in case.handles))
        with self.assertRaises(source_api.RecordSourceStateError):
            case.source()
        with self.assertRaises(pipeline_api.PipelineStateError):
            pipeline.acquire()

    def test_full_integration_one_supply_one_freeze_and_shared_object(self):
        case = Integration()
        pipeline = case.pipeline()
        pipeline.run((case.first, case.second))
        self.assertEqual(case.events, ['provider', 'factory', 'handle-factory', 'acquire',
                                       'acquire', 'first', 'acquire', 'second',
                                       'handle-close', 'provider-close'])
        self.assertEqual(case.source.supply_attempts, 1)
        first, second = case.seen
        self.assertIs(first, second)
        self.assertEqual(tuple(a.source_id for a in first.axes), tuple(range(700, 669, -1)))
        self.assertEqual(tuple(a.name for a in first.axes), tuple(f'neutral-{i}' for i in range(30, -1, -1)))
        self.assertEqual(tuple(a.order for a in first.axes), tuple(range(31)))
        self.assertEqual(tuple(v.field for v in first.vectors), ('neutral_y', 'neutral_x'))
        self.assertEqual(tuple(v.unit for v in first.vectors), ('unit-Y', 'unit-X'))
        for vector, column in zip(first.vectors, ('value-Y', 'value-X')):
            expected = tuple(row[column] for row in case.rows)
            self.assertEqual(vector.values, expected)
            self.assertEqual(tuple(map(type, vector.values)), tuple(map(type, expected)))
        self.assertEqual(math.copysign(1, first.vectors[0].values[0]), -1)
        self.assertEqual(first.calendar.target_year, 2018)
        self.assertEqual(first.calendar.observation_year, 2017)
        self.assertEqual(first.source.source_id, 'synthetic-records')
        self.assert_closed(case, pipeline)

    def test_schema_snapshot_at_constructor_and_rows_at_supply(self):
        rows, declaration, _ = fixture()
        provider = source_api.RecordSource(rows, **declaration)
        declaration['columns']['values'].clear()
        declaration['columns']['source_id'] = 'wrong'
        declaration['field_names'].clear()
        declaration['units'].clear()
        declaration['calendar'].clear()
        declaration['source'].clear()
        rows[0]['value-X'] = 777  # Before supply: explicitly visible.
        payload = provider()
        self.assertEqual(payload['vectors']['neutral_x']['values'][0], 777)
        rows[0]['value-X'] = 888
        rows[0]['ext-ID'] = 999
        rows.clear()
        self.assertEqual(payload['vectors']['neutral_x']['values'][0], 777)
        self.assertEqual(payload['axes'][0]['source_id'], 700)
        self.assertEqual(payload['calendar']['target_year'], 2018)
        provider.close()

    def test_prepared_carrier_survives_original_and_payload_mutations(self):
        case = Integration()
        supplied = []

        def provide():
            payload = case.provide()
            supplied.append(payload)
            return payload

        pipeline = case.pipeline(provider=provide).prepare()
        retained = pipeline.acquire()
        case.rows[0].clear()
        case.rows.clear()
        case.declarations['units'].clear()
        case.declarations['calendar'].clear()
        payload = supplied[0]
        payload['axes'][0]['source_id'] = 999
        payload['vectors']['neutral_y']['values'] = (999,) * 31
        payload['vectors']['neutral_y']['calendar'].clear()
        payload['calendar'].clear()
        pipeline.run((case.first, case.second))
        self.assertIs(case.seen[0], retained)
        self.assertIs(case.seen[1], retained)
        self.assertEqual(retained.axes[0].source_id, 700)
        self.assertEqual(retained.calendar.target_year, 2018)
        self.assertEqual(math.copysign(1, retained.vectors[0].values[0]), -1)
        self.assertEqual(case.source.supply_attempts, 1)
        self.assert_closed(case, pipeline)

    def test_tuple_rows_and_string_identifiers_supported(self):
        rows, declaration, _ = fixture()
        for index, row in enumerate(rows):
            row['ext-ID'] = f'id-{30 - index}'
        provider = source_api.RecordSource(tuple(rows), **declaration)
        obj = carrier_api.create_carrier(**provider())
        self.assertEqual(tuple(a.source_id for a in obj.axes), tuple(f'id-{i}' for i in range(30, -1, -1)))
        provider.close()

    def test_missing_extra_and_wrong_key_types_in_rows_rejected_with_cleanup(self):
        for operation in ('missing', 'extra', 'wrong-key-type'):
            with self.subTest(operation=operation):
                case = Integration()
                if operation == 'missing':
                    del case.rows[5]['value-X']
                elif operation == 'extra':
                    case.rows[5]['other'] = 0
                else:
                    case.rows[5][True] = 0
                pipeline = case.pipeline()
                with self.assertRaises(source_api.RecordContractError):
                    pipeline.run((case.first, case.second))
                self.assertEqual(case.events, ['provider', 'provider-close'])
                self.assert_closed(case, pipeline)

    def test_non31_rows_rejected(self):
        for size in (0, 30, 32):
            with self.subTest(size=size):
                case = Integration()
                case.rows[:] = (case.rows * 2)[:size]
                pipeline = case.pipeline()
                with self.assertRaisesRegex(source_api.RecordContractError, '31 rows'):
                    pipeline.run((case.first, case.second))
                self.assertEqual(case.events, ['provider', 'provider-close'])
                self.assert_closed(case, pipeline)

    def test_axis_id_name_and_order_rejections(self):
        cases = [('ext-ID', True), ('ext-ID', 700.0), ('ext-ID', '700'),
                 ('ext-ID', 699), ('ext-ID', ''), ('ext-name', ''),
                 ('ext-name', 'neutral-29'), ('position', True),
                 ('position', 0.0), ('position', 1)]
        for column, value in cases:
            with self.subTest(column=column, value=value):
                case = Integration()
                case.rows[0][column] = value
                pipeline = case.pipeline()
                with self.assertRaises(source_api.RecordContractError):
                    pipeline.run((case.first, case.second))
                self.assertEqual(case.events, ['provider', 'provider-close'])
                self.assert_closed(case, pipeline)

    def test_reversed_rows_not_silently_sorted(self):
        case = Integration()
        case.rows.reverse()
        pipeline = case.pipeline()
        with self.assertRaisesRegex(source_api.RecordContractError, 'input position'):
            pipeline.run((case.first, case.second))
        self.assert_closed(case, pipeline)

    def test_bad_numbers_rejected_without_conversion(self):
        for value in (True, False, None, '1', complex(1), float('nan'), float('inf'), -float('inf')):
            with self.subTest(value=repr(value)):
                case = Integration()
                case.rows[8]['value-Y'] = value
                pipeline = case.pipeline()
                with self.assertRaises(source_api.RecordContractError):
                    pipeline.run((case.first, case.second))
                self.assertEqual(case.events, ['provider', 'provider-close'])
                self.assert_closed(case, pipeline)

    def test_mapping_conflicts_empty_and_missing_columns(self):
        for change in ('duplicate-axis', 'axis-value-conflict', 'duplicate-values',
                       'blank', 'missing-axis', 'extra-axis', 'missing-value', 'extra-value'):
            with self.subTest(change=change):
                rows, declaration, _ = fixture()
                columns = declaration['columns']
                if change == 'duplicate-axis':
                    columns['name'] = columns['source_id']
                elif change == 'axis-value-conflict':
                    columns['values']['neutral_x'] = columns['source_id']
                elif change == 'duplicate-values':
                    columns['values']['neutral_x'] = columns['values']['neutral_y']
                elif change == 'blank':
                    columns['order'] = ' '
                elif change == 'missing-axis':
                    del columns['order']
                elif change == 'extra-axis':
                    columns['guess'] = 'not-allowed'
                elif change == 'missing-value':
                    del columns['values']['neutral_x']
                else:
                    columns['values']['extra'] = 'extra-column'
                with self.assertRaises(source_api.RecordContractError):
                    source_api.RecordSource(rows, **declaration)

    def test_fields_and_units_must_match_explicit_schema(self):
        for key, value in (('field_names', []), ('field_names', ['neutral_x', 'neutral_x']),
                           ('field_names', ['']), ('field_names', [True]),
                           ('units', {'neutral_x': 'unit-X'}),
                           ('units', {'neutral_x': 'unit-X', 'neutral_y': ''}),
                           ('units', {'neutral_x': 'unit-X', 'neutral_y': 'unit-Y', 'extra': 'u'})):
            with self.subTest(key=key, value=value):
                rows, declaration, _ = fixture()
                declaration[key] = value
                with self.assertRaises(source_api.RecordContractError):
                    source_api.RecordSource(rows, **declaration)

    def test_declaration_keys_and_types_rejected(self):
        for mapping, key, value in (('calendar', 'target_year', True),
                                    ('calendar', 'observation_year', 2017.0),
                                    ('calendar', 'label', ''), ('source', 'source_id', 1),
                                    ('source', 'label', None)):
            with self.subTest(mapping=mapping, key=key):
                rows, declaration, _ = fixture()
                declaration[mapping][key] = value
                with self.assertRaises(source_api.RecordContractError):
                    source_api.RecordSource(rows, **declaration)
        for mapping in ('calendar', 'source'):
            for change in ('missing', 'extra'):
                with self.subTest(mapping=mapping, change=change):
                    rows, declaration, _ = fixture()
                    if change == 'missing':
                        declaration[mapping].pop(next(iter(declaration[mapping])))
                    else:
                        declaration[mapping]['extra'] = 1
                    with self.assertRaises(source_api.RecordContractError):
                        source_api.RecordSource(rows, **declaration)

    def test_exact_container_and_scalar_types(self):
        class Row(dict):
            pass

        class Number(int):
            pass

        rows, declaration, _ = fixture()
        with self.assertRaises(source_api.RecordContractError):
            source_api.RecordSource(iter(rows), **declaration)
        for change in ('row-subclass', 'value-subclass'):
            with self.subTest(change=change):
                case = Integration()
                if change == 'row-subclass':
                    case.rows[0] = Row(case.rows[0])
                else:
                    case.rows[0]['value-X'] = Number(30)
                pipeline = case.pipeline()
                with self.assertRaises(source_api.RecordContractError):
                    pipeline.run((case.first, case.second))
                self.assert_closed(case, pipeline)

    def test_source_single_use_after_success_failure_and_close(self):
        for state in ('success', 'failure', 'closed'):
            with self.subTest(state=state):
                rows, declaration, _ = fixture()
                provider = source_api.RecordSource(rows, **declaration)
                if state == 'success':
                    provider()
                elif state == 'failure':
                    rows.clear()
                    with self.assertRaises(source_api.RecordContractError):
                        provider()
                else:
                    provider.close()
                with self.assertRaises(source_api.RecordSourceStateError):
                    provider()
                self.assertEqual(provider.supply_attempts, int(state != 'closed'))
                provider.close()
                provider.close()
                self.assertEqual(provider.close_count, 1)

    def test_expectation_mismatch_rejected_by_actual_pipeline(self):
        for field in ('units', 'calendar', 'source'):
            with self.subTest(field=field):
                case = Integration()
                if field == 'units':
                    case.expected[field]['neutral_y'] = 'another-unit'
                elif field == 'calendar':
                    case.expected[field]['observation_year'] = 2016
                else:
                    case.expected[field]['label'] = 'another-source'
                pipeline = case.pipeline()
                with self.assertRaises(pipeline_api.PipelineContractError):
                    pipeline.run((case.first, case.second))
                self.assertEqual(case.events, ['provider', 'factory', 'provider-close'])
                self.assert_closed(case, pipeline)

    def test_actual_carrier_validation_failure_after_payload_return(self):
        case = Integration()

        def corrupt_payload():
            payload = case.provide()
            payload['vectors']['neutral_y']['unit'] = 'inconsistent'
            return payload

        pipeline = case.pipeline(provider=corrupt_payload)
        with self.assertRaises(carrier_api.ContractError):
            pipeline.run((case.first, case.second))
        self.assertEqual(case.events, ['provider', 'factory', 'provider-close'])
        self.assert_closed(case, pipeline)

    def test_each_consumer_failure_closes_resources_once(self):
        for which in ('first', 'second'):
            with self.subTest(which=which):
                case = Integration()
                primary = RuntimeError(which + '-original')

                def fail(carrier):
                    case.events.append(which)
                    raise primary

                consumers = (fail, case.second) if which == 'first' else (case.first, fail)
                pipeline = case.pipeline()
                with self.assertRaises(RuntimeError) as caught:
                    pipeline.run(consumers)
                self.assertIs(caught.exception, primary)
                if which == 'first':
                    self.assertNotIn('second', case.events)
                self.assertEqual(case.events.count('handle-close'), 1)
                self.assert_closed(case, pipeline)

    def test_mapping_error_not_masked_by_cleanup_error(self):
        case = Integration()
        del case.rows[0]['value-X']
        cleanup = RuntimeError('provider-close-error')

        def close():
            case.close_source()
            raise cleanup

        pipeline = case.pipeline(provider_close=close)
        with self.assertRaises(source_api.RecordContractError) as caught:
            pipeline.run((case.first, case.second))
        self.assertIn('declared keys', str(caught.exception))
        self.assertEqual(pipeline.cleanup_errors, (cleanup,))
        self.assertTrue(any('cleanup also failed' in note for note in caught.exception.__notes__))
        self.assert_closed(case, pipeline)

    def test_consumer_primary_not_masked_by_handle_cleanup(self):
        case = Integration()
        primary, cleanup = RuntimeError('first-error'), RuntimeError('handle-error')

        def fail(carrier):
            raise primary

        def close(handle):
            case.close_handle(handle)
            raise cleanup

        pipeline = case.pipeline(handle_close=close)
        with self.assertRaises(RuntimeError) as caught:
            pipeline.run((fail, case.second))
        self.assertIs(caught.exception, primary)
        self.assertEqual(pipeline.cleanup_errors, (cleanup,))
        self.assertEqual(case.events.count('handle-close'), 1)
        self.assert_closed(case, pipeline)

    def test_provider_cancellation_uses_existing_pipeline_state_guard(self):
        case = Integration()

        def cancel():
            payload = case.provide()
            pipeline.close()
            return payload

        pipeline = case.pipeline(provider=cancel)
        with self.assertRaises(pipeline_api.PipelineStateError):
            pipeline.run((case.first, case.second))
        self.assertEqual(case.events, ['provider', 'provider-close'])
        self.assert_closed(case, pipeline)

    def test_late_handle_after_cancellation_uses_existing_cleanup_contract(self):
        case = Integration()

        def cancel(carrier):
            pipeline.close()
            return case.handle_factory(carrier)

        pipeline = case.pipeline(handle_factory=cancel)
        with self.assertRaises(pipeline_api.PipelineStateError):
            pipeline.run((case.first, case.second))
        self.assertEqual(case.events, ['provider', 'factory', 'provider-close',
                                       'handle-factory', 'handle-close'])
        self.assert_closed(case, pipeline)

    def test_factory_partial_resource_responsibility_is_explicit(self):
        case = Integration()
        resource = {'open': False}
        primary = RuntimeError('partial-factory')

        def factory(**payload):
            case.events.append('factory')
            resource['open'] = True
            try:
                raise primary
            finally:
                resource['open'] = False

        pipeline = case.pipeline(carrier_factory=factory)
        with self.assertRaises(RuntimeError) as caught:
            pipeline.run((case.first, case.second))
        self.assertIs(caught.exception, primary)
        self.assertFalse(resource['open'])
        self.assert_closed(case, pipeline)

    def test_invalid_consumer_never_calls_source_caller_retains_ownership(self):
        case = Integration()
        pipeline = case.pipeline()
        with self.assertRaises(pipeline_api.PipelineContractError):
            pipeline.run((case.first, None))
        self.assertEqual(case.events, [])
        self.assertEqual(case.source.supply_attempts, 0)
        self.assertEqual(case.source.state, 'new')
        # A2 only owns attempted provider resources; unused source stays caller-owned.
        case.source.close()
        self.assertEqual(case.source.close_count, 1)

    def test_import_inert_no_carrier_or_pipeline_discovery(self):
        path = MODULE_DIR / 'staged_record_source.py'
        tree = ast.parse(path.read_text(encoding='utf-8'))
        self.assertEqual([n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)],
                         ['dataclasses', 'math'])
        self.assertFalse(any(isinstance(n, ast.Import) for n in ast.walk(tree)))
        output = io.StringIO()
        try:
            with patch.object(builtins, 'open', side_effect=AssertionError('unexpected file read')), \
                    patch.object(os, 'getenv', side_effect=AssertionError('unexpected env read')), \
                    contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
                load('_a3_inert_probe', 'staged_record_source.py')
            self.assertEqual(output.getvalue(), '')
        finally:
            sys.modules.pop('_a3_inert_probe', None)


if __name__ == '__main__':
    unittest.main(verbosity=2)
