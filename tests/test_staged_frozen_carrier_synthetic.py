"""Standalone stdlib synthetic tests; loads only the new module by exact path."""

import ast
import builtins
import contextlib
import copy
from dataclasses import FrozenInstanceError, fields, is_dataclass
import importlib.util
import io
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


MODULE_PATH = (Path(__file__).resolve().parent.parent / 'validators' /
               'multi_province' / 'annual_observed_labor_diagnostic' /
               'staged_frozen_carrier.py')
SPEC = importlib.util.spec_from_file_location('_stage_a_inert_carrier', MODULE_PATH)
carrier_api = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = carrier_api
SPEC.loader.exec_module(carrier_api)


def synthetic_input():
    """Neutral synthetic labels, deliberately unsorted external IDs and values."""
    calendar = {'target_year': 2018, 'observation_year': 2017, 'label': 'declared-only'}
    source = {'source_id': 'synthetic-memory', 'label': 'unverified-test-fixture'}
    values = [(-1) ** i * (i + 0.25) for i in range(31)]
    values[0] = 7  # Must remain int, with no numeric coercion.
    return {
        'axes': [{'source_id': 100 - i, 'name': f'neutral-{30 - i}', 'order': i}
                 for i in range(31)],
        'field_names': ['neutral_b', 'neutral_a'],
        'vectors': {
            'neutral_a': {'values': list(reversed(values)), 'unit': 'unit-a',
                          'calendar': copy.deepcopy(calendar), 'source': dict(source)},
            'neutral_b': {'values': values, 'unit': 'unit-b',
                          'calendar': copy.deepcopy(calendar), 'source': dict(source)},
        },
        'units': {'neutral_a': 'unit-a', 'neutral_b': 'unit-b'},
        'calendar': calendar,
        'source': source,
    }


def consumer_one(handle):
    obj = handle.acquire()
    return obj, tuple(a.source_id for a in obj.axes), obj.calendar, tuple(v.unit for v in obj.vectors)


def consumer_two(handle):
    obj = handle.acquire()
    return obj, tuple(a.source_id for a in obj.axes), obj.calendar, tuple(v.unit for v in obj.vectors)


class CarrierTests(unittest.TestCase):
    def reject(self, payload, message):
        with self.assertRaisesRegex(carrier_api.ContractError, message):
            carrier_api.create_carrier(**payload)

    def test_order_values_and_types_preserved(self):
        payload = synthetic_input()
        obj = carrier_api.create_carrier(**payload)
        self.assertEqual(tuple(a.source_id for a in obj.axes), tuple(range(100, 69, -1)))
        self.assertEqual(tuple(a.name for a in obj.axes), tuple(f'neutral-{i}' for i in range(30, -1, -1)))
        self.assertEqual(tuple(a.order for a in obj.axes), tuple(range(31)))
        self.assertEqual(tuple(v.field for v in obj.vectors), ('neutral_b', 'neutral_a'))
        for vector in obj.vectors:
            expected = payload['vectors'][vector.field]['values']
            self.assertEqual(vector.values, tuple(expected))
            self.assertEqual(tuple(map(type, vector.values)), tuple(map(type, expected)))
        self.assertEqual(obj.calendar.target_year, 2018)
        self.assertEqual(obj.calendar.observation_year, 2017)
        self.assertEqual(obj.source.source_id, 'synthetic-memory')

    def test_string_ids_and_tuple_inputs(self):
        payload = synthetic_input()
        payload['axes'] = tuple(dict(axis, source_id=f'key-{i}')
                                for i, axis in enumerate(payload['axes']))
        payload['field_names'] = tuple(payload['field_names'])
        for vector in payload['vectors'].values():
            vector['values'] = tuple(vector['values'])
        obj = carrier_api.create_carrier(**payload)
        self.assertEqual(tuple(a.source_id for a in obj.axes), tuple(f'key-{i}' for i in range(31)))

    def test_snapshot_survives_all_original_container_mutations(self):
        payload = synthetic_input()
        obj = carrier_api.create_carrier(**payload)
        expected = carrier_api.create_carrier(**copy.deepcopy(payload))
        payload['axes'][0].update(source_id=999, name='changed', order=99)
        payload['axes'].clear()
        payload['field_names'].clear()
        for vector in payload['vectors'].values():
            vector['values'].clear()
            vector['calendar'].clear()
            vector['source'].clear()
            vector['unit'] = 'changed'
        payload['vectors'].clear()
        payload['units'].clear()
        payload['calendar'].clear()
        payload['source'].clear()
        self.assertEqual(obj, expected)

    def test_public_data_transitively_immutable(self):
        obj = carrier_api.create_carrier(**synthetic_input())

        def check(value):
            if is_dataclass(value):
                self.assertFalse(hasattr(value, '__dict__'))
                for field in fields(value):
                    with self.assertRaises((FrozenInstanceError, AttributeError)):
                        setattr(value, field.name, None)
                    check(getattr(value, field.name))
            elif type(value) is tuple:
                if value:
                    with self.assertRaises(TypeError):
                        value[0] = None
                for item in value:
                    check(item)
            else:
                self.assertIn(type(value), (str, int, float))

        check(obj)

    def test_axis_lengths(self):
        for size in (0, 30, 32):
            with self.subTest(size=size):
                payload = synthetic_input()
                payload['axes'] = (payload['axes'] * 2)[:size]
                self.reject(payload, 'exactly 31')

    def test_duplicate_and_empty_axis_identifiers(self):
        for key, value in (('source_id', 99), ('name', 'neutral-29'),
                           ('source_id', ''), ('source_id', '   '), ('name', '')):
            with self.subTest(key=key, value=value):
                payload = synthetic_input()
                payload['axes'][0][key] = value
                self.reject(payload, 'duplicate|nonblank')

    def test_id_type_collisions_and_mixed_types(self):
        for value in (True, False, 100.0, None, [], '100'):
            with self.subTest(value=value):
                payload = synthetic_input()
                payload['axes'][0]['source_id'] = value
                self.reject(payload, 'source_id|mixed source-ID')

    def test_wrong_order_rejected_without_sorting(self):
        for value in (1, True, 0.0, '0'):
            with self.subTest(value=value):
                payload = synthetic_input()
                payload['axes'][0]['order'] = value
                self.reject(payload, 'zero-based input position')
        payload = synthetic_input()
        payload['axes'].reverse()
        self.reject(payload, 'zero-based input position')

    def test_vector_lengths(self):
        for values in ([], [1] * 30, [1] * 32):
            with self.subTest(size=len(values)):
                payload = synthetic_input()
                payload['vectors']['neutral_a']['values'] = values
                self.reject(payload, 'exactly 31 values')

    def test_invalid_and_nonfinite_numbers(self):
        for value in (True, False, None, '1', complex(1), float('nan'), float('inf'), -float('inf')):
            with self.subTest(value=repr(value)):
                payload = synthetic_input()
                payload['vectors']['neutral_b']['values'][4] = value
                self.reject(payload, 'exact int or float|nonfinite')

    def test_field_schema_rejections(self):
        for names in ([], ['neutral_a', 'neutral_a'], [''], [True]):
            with self.subTest(names=names):
                payload = synthetic_input()
                payload['field_names'] = names
                self.reject(payload, 'field_names')
        for mapping in ('vectors', 'units'):
            for operation in ('missing', 'extra'):
                with self.subTest(mapping=mapping, operation=operation):
                    payload = synthetic_input()
                    if operation == 'missing':
                        del payload[mapping]['neutral_a']
                    else:
                        payload[mapping]['extra'] = 'no-inference'
                    self.reject(payload, 'exact keys')

    def test_missing_and_extra_declaration_keys(self):
        for key in ('calendar', 'source'):
            for operation in ('missing', 'extra'):
                with self.subTest(key=key, operation=operation):
                    payload = synthetic_input()
                    if operation == 'missing':
                        payload[key].pop(next(iter(payload[key])))
                    else:
                        payload[key]['extra'] = 'unsupported'
                    self.reject(payload, 'exact keys')
        payload = synthetic_input()
        del payload['vectors']['neutral_a']['source']
        self.reject(payload, 'exact keys')
        payload = synthetic_input()
        payload['axes'][0]['extra'] = None
        self.reject(payload, 'exact keys')

    def test_inconsistent_vector_declarations(self):
        for key in ('unit', 'calendar', 'source'):
            with self.subTest(key=key):
                payload = synthetic_input()
                vector = payload['vectors']['neutral_b']
                if key == 'unit':
                    vector[key] = 'another-unit'
                elif key == 'calendar':
                    vector[key]['observation_year'] = 2016
                else:
                    vector[key]['source_id'] = 'another-source'
                self.reject(payload, 'inconsistent declarations')

    def test_declaration_types_and_blanks(self):
        cases = [('calendar', 'target_year', True), ('calendar', 'observation_year', 2017.0),
                 ('calendar', 'label', ''), ('source', 'source_id', 3),
                 ('source', 'label', '   '), ('units', 'neutral_a', '')]
        for mapping, key, value in cases:
            with self.subTest(mapping=mapping, key=key, value=value):
                payload = synthetic_input()
                payload[mapping][key] = value
                self.reject(payload, 'exact int|nonblank exact str')

    def test_exact_types_only(self):
        class DictSubclass(dict):
            pass

        class IntSubclass(int):
            pass

        class ListSubclass(list):
            pass

        payload = synthetic_input()
        payload['axes'][0] = DictSubclass(payload['axes'][0])
        self.reject(payload, 'exact dict')
        payload = synthetic_input()
        payload['axes'][0]['source_id'] = IntSubclass(100)
        self.reject(payload, 'exact int or str')
        payload = synthetic_input()
        payload['vectors']['neutral_a']['values'] = ListSubclass([1] * 31)
        self.reject(payload, 'exact list or tuple')
        payload = synthetic_input()
        payload['vectors']['neutral_a']['values'] = iter([1] * 31)
        self.reject(payload, 'exact list or tuple')

    def test_declarations_not_normalized_or_scientifically_interpreted(self):
        payload = synthetic_input()
        payload['calendar'] = {'target_year': -10, 'observation_year': 9000, 'label': ' raw '}
        payload['source'] = {'source_id': ' raw-id ', 'label': ' unverified '}
        for name, vector in payload['vectors'].items():
            payload['units'][name] = ' raw-unit '
            vector.update(unit=' raw-unit ', calendar=dict(payload['calendar']),
                          source=dict(payload['source']))
        obj = carrier_api.create_carrier(**payload)
        self.assertEqual(obj.calendar.observation_year, 9000)
        self.assertEqual(obj.calendar.label, ' raw ')
        self.assertEqual(obj.vectors[0].unit, ' raw-unit ')
        self.assertEqual(obj.source.source_id, ' raw-id ')

    def test_two_consumers_same_object_and_metadata(self):
        obj = carrier_api.create_carrier(**synthetic_input())
        handle = carrier_api.CarrierHandle(obj)
        first, second = consumer_one(handle), consumer_two(handle)
        self.assertIs(first[0], obj)
        self.assertIs(second[0], first[0])
        self.assertEqual(first[1:], second[1:])
        self.assertIs(first[2], second[2])
        self.assertEqual(first[3], ('unit-b', 'unit-a'))

    def test_close_blocks_new_access_without_revoking_prior_reference(self):
        obj = carrier_api.create_carrier(**synthetic_input())
        handle = carrier_api.CarrierHandle(obj)
        retained = handle.acquire()
        handle.close()
        handle.close()
        self.assertTrue(handle.closed)
        with self.assertRaises(carrier_api.ClosedCarrierError):
            handle.acquire()
        with self.assertRaises(carrier_api.ClosedCarrierError):
            handle.__enter__()
        self.assertIs(retained, obj)
        self.assertEqual(retained.axes[0].source_id, 100)

    def test_context_closes_on_normal_and_exceptional_exit(self):
        for fail in (False, True):
            with self.subTest(fail=fail):
                handle = carrier_api.CarrierHandle(carrier_api.create_carrier(**synthetic_input()))
                if fail:
                    with self.assertRaisesRegex(RuntimeError, 'consumer-failure'):
                        with handle as active:
                            self.assertIs(active.acquire(), handle.acquire())
                            raise RuntimeError('consumer-failure')
                else:
                    with handle as active:
                        self.assertFalse(active.closed)
                self.assertTrue(handle.closed)
                with self.assertRaises(carrier_api.ClosedCarrierError):
                    handle.acquire()

    def test_handle_rejects_noncarrier(self):
        with self.assertRaises(carrier_api.ContractError):
            carrier_api.CarrierHandle({})

    def test_import_inert_and_only_declared_stdlib_imports(self):
        # Static imports plus denied ordinary file/env access and captured output
        # are bounded checks, not proof against hostile code or platform access.
        tree = ast.parse(MODULE_PATH.read_text(encoding='utf-8'))
        imported = [node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]
        self.assertEqual(imported, ['dataclasses', 'math'])
        self.assertFalse(any(isinstance(node, ast.Import) for node in ast.walk(tree)))
        spec = importlib.util.spec_from_file_location('_stage_a_import_probe', MODULE_PATH)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        output = io.StringIO()
        try:
            with patch.object(builtins, 'open', side_effect=AssertionError('unexpected file read')), \
                    patch.object(os, 'getenv', side_effect=AssertionError('unexpected env read')), \
                    contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
                spec.loader.exec_module(module)
            self.assertEqual(output.getvalue(), '')
        finally:
            del sys.modules[spec.name]


if __name__ == '__main__':
    unittest.main(verbosity=2)
