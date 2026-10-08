"""Exact-path, pure stdlib tests of synthetic pipeline integration and ownership."""

import ast
import builtins
import contextlib
import copy
from dataclasses import replace
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


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


carrier_api = load_module('_stage_a2_carrier', MODULE_DIR / 'staged_frozen_carrier.py')
pipeline_api = load_module('_stage_a2_pipeline', MODULE_DIR / 'staged_frozen_pipeline.py')


def fixture():
    calendar = {'target_year': 2018, 'observation_year': 2017, 'label': 'synthetic-calendar'}
    source = {'source_id': 'only-memory-fixture', 'label': 'unverified'}
    axes = [{'source_id': 200 - i, 'name': f'neutral-{i}', 'order': i} for i in range(31)]
    units = {'neutral_y': 'unit-y', 'neutral_x': 'unit-x'}
    numbers = [i + 0.125 for i in range(31)]
    numbers[0:3] = [7, -0.0, -2.5]
    payload = {
        'axes': axes, 'field_names': ['neutral_y', 'neutral_x'], 'units': units,
        'calendar': calendar, 'source': source,
        'vectors': {name: {'values': list(numbers), 'unit': unit,
                           'calendar': dict(calendar), 'source': dict(source)}
                    for name, unit in units.items()},
    }
    expected = {key: copy.deepcopy(payload[key]) for key in
                ('axes', 'field_names', 'units', 'calendar', 'source')}
    # Budget check uses only the in-memory synthetic fixture, never real data.
    assert len(repr((payload, expected)).encode('utf-8')) < 1048576
    return payload, expected


class Harness:
    def __init__(self):
        self.payload, self.expected = fixture()
        self.events = []
        self.handles = []
        self.seen = []
        self.provider_resource_open = False

    def provider(self):
        self.events.append('provider')
        self.provider_resource_open = True
        return self.payload

    def provider_close(self):
        self.events.append('provider-close')
        self.provider_resource_open = False

    def factory(self, **payload):
        self.events.append('factory')
        return carrier_api.create_carrier(**payload)

    def handle_factory(self, carrier):
        self.events.append('handle-factory')
        handle = carrier_api.CarrierHandle(carrier)
        self.handles.append(handle)
        return handle

    def handle_acquire(self, handle):
        self.events.append('acquire')
        return handle.acquire()

    def handle_close(self, handle):
        self.events.append('handle-close')
        handle.close()

    def first(self, carrier):
        self.events.append('first')
        self.seen.append(carrier)
        return 'first-result'

    def second(self, carrier):
        self.events.append('second')
        self.seen.append(carrier)
        return 'second-result'

    def kwargs(self):
        return dict(provider=self.provider, provider_close=self.provider_close,
                    carrier_factory=self.factory, handle_factory=self.handle_factory,
                    handle_acquire=self.handle_acquire, handle_close=self.handle_close,
                    expected=self.expected)

    def pipeline(self, **overrides):
        kwargs = self.kwargs()
        kwargs.update(overrides)
        return pipeline_api.SharedInputPipeline(**kwargs)


class PipelineTests(unittest.TestCase):
    def assert_closed(self, pipeline, harness):
        self.assertEqual(pipeline.state, 'closed')
        self.assertFalse(harness.provider_resource_open)
        self.assertTrue(all(handle.closed for handle in harness.handles))
        with self.assertRaises(pipeline_api.PipelineStateError):
            pipeline.acquire()
        with self.assertRaises(pipeline_api.PipelineStateError):
            pipeline.prepare()
        with self.assertRaises(pipeline_api.PipelineStateError):
            pipeline.run((harness.first, harness.second))

    def test_success_sequence_single_freeze_and_shared_identity(self):
        harness = Harness()
        pipeline = harness.pipeline()
        self.assertEqual(pipeline.run((harness.first, harness.second)),
                         ('first-result', 'second-result'))
        self.assertEqual(harness.events, ['provider', 'factory', 'handle-factory', 'acquire',
                                         'acquire', 'first', 'acquire', 'second',
                                         'handle-close', 'provider-close'])
        first, second = harness.seen
        self.assertIs(first, second)
        self.assertEqual(tuple(a.source_id for a in first.axes), tuple(range(200, 169, -1)))
        self.assertEqual(tuple(a.name for a in first.axes), tuple(f'neutral-{i}' for i in range(31)))
        self.assertEqual(tuple(a.order for a in first.axes), tuple(range(31)))
        self.assertEqual(tuple(v.field for v in first.vectors), ('neutral_y', 'neutral_x'))
        self.assertEqual(tuple(v.unit for v in first.vectors), ('unit-y', 'unit-x'))
        self.assertEqual((first.calendar.target_year, first.calendar.observation_year), (2018, 2017))
        for vector in first.vectors:
            original = harness.payload['vectors'][vector.field]['values']
            self.assertEqual(vector.values, tuple(original))
            self.assertEqual(tuple(map(type, vector.values)), tuple(map(type, original)))
            self.assertEqual(math.copysign(1, vector.values[1]), -1)
        self.assert_closed(pipeline, harness)
        self.assertEqual(pipeline.cleanup_errors, ())

    def test_prepare_then_run_does_not_reload(self):
        harness = Harness()
        pipeline = harness.pipeline()
        self.assertIs(pipeline.prepare(), pipeline)
        retained = pipeline.acquire()
        harness.payload['axes'].clear()
        harness.payload['vectors']['neutral_y']['values'].clear()
        pipeline.run([harness.first, harness.second])
        self.assertIs(harness.seen[0], retained)
        self.assertEqual(len(retained.axes), 31)
        self.assertEqual(len(retained.vectors[0].values), 31)
        self.assertEqual(harness.events.count('provider'), 1)
        self.assertEqual(harness.events.count('factory'), 1)
        self.assert_closed(pipeline, harness)

    def test_expectations_snapshotted_before_provider(self):
        harness = Harness()
        pipeline = harness.pipeline()
        harness.expected['axes'][0]['source_id'] = 999
        harness.expected['field_names'].reverse()
        harness.expected['units'].clear()
        harness.expected['calendar'].clear()
        harness.expected['source'].clear()
        pipeline.run((harness.first, harness.second))
        self.assertIs(harness.seen[0], harness.seen[1])
        self.assert_closed(pipeline, harness)

    def test_every_noncallable_dependency_rejected_before_provider(self):
        names = ('provider', 'provider_close', 'carrier_factory', 'handle_factory',
                 'handle_acquire', 'handle_close')
        for name in names:
            for value in (None, False, 'auto-discovery-forbidden'):
                with self.subTest(name=name, value=value):
                    harness = Harness()
                    with self.assertRaisesRegex(pipeline_api.PipelineContractError, name):
                        harness.pipeline(**{name: value})
                    self.assertEqual(harness.events, [])

    def test_missing_dependency_is_constructor_error_without_provider(self):
        harness = Harness()
        kwargs = harness.kwargs()
        del kwargs['provider_close']
        with self.assertRaises(TypeError):
            pipeline_api.SharedInputPipeline(**kwargs)
        self.assertEqual(harness.events, [])

    def test_bad_expectations_rejected_without_any_callback(self):
        cases = [
            ('axes', []), ('field_names', []), ('field_names', ['neutral_y', 'neutral_y']),
            ('units', {}), ('calendar', {}), ('source', None),
        ]
        for key, value in cases:
            with self.subTest(key=key, value=value):
                harness = Harness()
                harness.expected[key] = value
                with self.assertRaises(pipeline_api.PipelineContractError):
                    harness.pipeline()
                self.assertEqual(harness.events, [])

    def test_expected_axis_id_order_and_name_rejections(self):
        for key, value in (('source_id', True), ('source_id', 200.0), ('source_id', '200'),
                           ('source_id', 199), ('name', ''), ('name', 'neutral-1'),
                           ('order', True), ('order', 1)):
            with self.subTest(key=key, value=value):
                harness = Harness()
                harness.expected['axes'][0][key] = value
                with self.assertRaises(pipeline_api.PipelineContractError):
                    harness.pipeline()
                self.assertEqual(harness.events, [])

    def test_expected_metadata_types_are_exact(self):
        for mapping, key, value in (('calendar', 'target_year', True),
                                    ('calendar', 'observation_year', 2017.0),
                                    ('source', 'source_id', 7), ('source', 'label', ''),
                                    ('units', 'neutral_y', ' ')):
            with self.subTest(mapping=mapping, key=key):
                harness = Harness()
                harness.expected[mapping][key] = value
                with self.assertRaises(pipeline_api.PipelineContractError):
                    harness.pipeline()
                self.assertEqual(harness.events, [])

    def test_invalid_consumers_rejected_before_loading(self):
        for consumers in ([], [lambda obj: None], [None, lambda obj: None],
                          [lambda obj: None, False], iter([])):
            with self.subTest(consumers=type(consumers)):
                harness = Harness()
                pipeline = harness.pipeline()
                with self.assertRaises(pipeline_api.PipelineContractError):
                    pipeline.run(consumers)
                self.assertEqual(harness.events, [])
                self.assert_closed(pipeline, harness)

    def test_invalid_consumers_after_prepare_close_without_consumption(self):
        harness = Harness()
        pipeline = harness.pipeline().prepare()
        with self.assertRaises(pipeline_api.PipelineContractError):
            pipeline.run([harness.first, None])
        self.assertNotIn('first', harness.events)
        self.assertNotIn('second', harness.events)
        self.assertEqual(harness.events.count('provider-close'), 1)
        self.assert_closed(pipeline, harness)

    def test_all_expected_metadata_mismatches_reject_consumers(self):
        for mismatch in ('axes', 'fields', 'units', 'calendar', 'source'):
            with self.subTest(mismatch=mismatch):
                harness = Harness()
                if mismatch == 'axes':
                    harness.expected['axes'][0]['source_id'] = 900
                elif mismatch == 'fields':
                    harness.expected['field_names'].reverse()
                elif mismatch == 'units':
                    harness.expected['units']['neutral_x'] = 'another-unit'
                elif mismatch == 'calendar':
                    harness.expected['calendar']['observation_year'] = 2016
                else:
                    harness.expected['source']['label'] = 'different-label'
                pipeline = harness.pipeline()
                with self.assertRaisesRegex(pipeline_api.PipelineContractError, mismatch + ' mismatch'):
                    pipeline.run((harness.first, harness.second))
                self.assertEqual(harness.events, ['provider', 'factory', 'provider-close'])
                self.assert_closed(pipeline, harness)

    def test_provider_failure_registered_cleanup_and_original_exception(self):
        harness = Harness()
        original = RuntimeError('provider-failure')

        def fail():
            harness.provider()
            raise original

        pipeline = harness.pipeline(provider=fail)
        with self.assertRaises(RuntimeError) as caught:
            pipeline.run((harness.first, harness.second))
        self.assertIs(caught.exception, original)
        self.assertEqual(harness.events, ['provider', 'provider-close'])
        self.assert_closed(pipeline, harness)

    def test_provider_wrong_payload_rejected_and_closed(self):
        harness = Harness()

        def wrong():
            harness.provider()
            return []

        pipeline = harness.pipeline(provider=wrong)
        with self.assertRaisesRegex(pipeline_api.PipelineContractError, 'exact payload dict'):
            pipeline.run((harness.first, harness.second))
        self.assertEqual(harness.events, ['provider', 'provider-close'])
        self.assert_closed(pipeline, harness)

    def test_actual_carrier_factory_validation_failure(self):
        harness = Harness()
        harness.payload['vectors']['neutral_y']['values'][0] = float('nan')
        pipeline = harness.pipeline()
        with self.assertRaises(carrier_api.ContractError):
            pipeline.run((harness.first, harness.second))
        self.assertEqual(harness.events, ['provider', 'factory', 'provider-close'])
        self.assert_closed(pipeline, harness)

    def test_injected_factory_exception_preserved(self):
        harness = Harness()
        original = RuntimeError('factory-failure')

        def fail(**payload):
            harness.events.append('factory')
            raise original

        pipeline = harness.pipeline(carrier_factory=fail)
        with self.assertRaises(RuntimeError) as caught:
            pipeline.run((harness.first, harness.second))
        self.assertIs(caught.exception, original)
        self.assertEqual(harness.events, ['provider', 'factory', 'provider-close'])
        self.assert_closed(pipeline, harness)

    def test_factory_result_missing_metadata_rejected(self):
        harness = Harness()

        def wrong(**payload):
            harness.events.append('factory')
            return object()

        pipeline = harness.pipeline(carrier_factory=wrong)
        with self.assertRaisesRegex(pipeline_api.PipelineContractError, 'missing carrier metadata'):
            pipeline.run((harness.first, harness.second))
        self.assertEqual(harness.events, ['provider', 'factory', 'provider-close'])
        self.assert_closed(pipeline, harness)

    def test_factory_partial_resources_owned_by_factory(self):
        harness = Harness()
        resource = {'open': False}
        original = RuntimeError('partial-factory-failure')

        def fail(**payload):
            harness.events.append('factory')
            resource['open'] = True
            try:
                raise original
            finally:
                resource['open'] = False
                harness.events.append('factory-partial-close')

        pipeline = harness.pipeline(carrier_factory=fail)
        with self.assertRaises(RuntimeError) as caught:
            pipeline.run((harness.first, harness.second))
        self.assertIs(caught.exception, original)
        self.assertFalse(resource['open'])
        self.assertEqual(harness.events[-2:], ['factory-partial-close', 'provider-close'])
        self.assert_closed(pipeline, harness)

    def test_handle_factory_partial_resources_owned_by_factory(self):
        harness = Harness()
        original = RuntimeError('handle-factory-failure')

        def fail(carrier):
            handle = harness.handle_factory(carrier)
            try:
                raise original
            finally:
                handle.close()
                harness.events.append('handle-factory-partial-close')

        pipeline = harness.pipeline(handle_factory=fail)
        with self.assertRaises(RuntimeError) as caught:
            pipeline.run((harness.first, harness.second))
        self.assertIs(caught.exception, original)
        self.assertNotIn('handle-close', harness.events)
        self.assertEqual(harness.events[-2:], ['handle-factory-partial-close', 'provider-close'])
        self.assert_closed(pipeline, harness)

    def test_initial_handle_acquisition_failure_closes_both_resources(self):
        harness = Harness()
        original = RuntimeError('acquire-failure')

        def fail(handle):
            harness.events.append('acquire')
            raise original

        pipeline = harness.pipeline(handle_acquire=fail)
        with self.assertRaises(RuntimeError) as caught:
            pipeline.run((harness.first, harness.second))
        self.assertIs(caught.exception, original)
        self.assertEqual(harness.events[-2:], ['handle-close', 'provider-close'])
        self.assert_closed(pipeline, harness)

    def test_handle_must_preserve_exact_identity(self):
        harness = Harness()

        def wrong(handle):
            harness.events.append('acquire')
            return carrier_api.create_carrier(**harness.payload)

        pipeline = harness.pipeline(handle_acquire=wrong)
        with self.assertRaisesRegex(pipeline_api.PipelineContractError, 'identical carrier'):
            pipeline.run((harness.first, harness.second))
        self.assertNotIn('first', harness.events)
        self.assert_closed(pipeline, harness)

    def test_later_acquire_identity_change_closes_prepared_pipeline(self):
        harness = Harness()

        def changing(handle):
            carrier = harness.handle_acquire(handle)
            if harness.events.count('acquire') > 1:
                return carrier_api.create_carrier(**harness.payload)
            return carrier

        pipeline = harness.pipeline(handle_acquire=changing).prepare()
        with self.assertRaisesRegex(pipeline_api.PipelineContractError, 'identity changed'):
            pipeline.acquire()
        self.assert_closed(pipeline, harness)

    def test_each_consumer_failure_stops_sequence_and_preserves_exception(self):
        for which in ('first', 'second'):
            with self.subTest(which=which):
                harness = Harness()
                original = RuntimeError(which + '-failure')

                def fail(carrier):
                    harness.events.append(which)
                    raise original

                consumers = (fail, harness.second) if which == 'first' else (harness.first, fail)
                pipeline = harness.pipeline()
                with self.assertRaises(RuntimeError) as caught:
                    pipeline.run(consumers)
                self.assertIs(caught.exception, original)
                if which == 'first':
                    self.assertNotIn('second', harness.events)
                self.assertEqual(harness.events.count('provider'), 1)
                self.assertEqual(harness.events.count('factory'), 1)
                self.assertEqual(harness.events[-2:], ['handle-close', 'provider-close'])
                self.assert_closed(pipeline, harness)

    def test_cleanup_failures_do_not_mask_consumer_primary(self):
        harness = Harness()
        primary = RuntimeError('first-consumer-original')
        handle_error = RuntimeError('handle-cleanup')
        provider_error = RuntimeError('provider-cleanup')

        def fail(carrier):
            harness.events.append('first')
            raise primary

        def handle_close(handle):
            harness.handle_close(handle)
            raise handle_error

        def provider_close():
            harness.provider_close()
            raise provider_error

        pipeline = harness.pipeline(handle_close=handle_close, provider_close=provider_close)
        with self.assertRaises(RuntimeError) as caught:
            pipeline.run((fail, harness.second))
        self.assertIs(caught.exception, primary)
        self.assertEqual(pipeline.cleanup_errors, (handle_error, provider_error))
        self.assertTrue(any('cleanup also failed' in note for note in primary.__notes__))
        self.assertNotIn('second', harness.events)
        self.assert_closed(pipeline, harness)
        before = list(harness.events)
        pipeline.close()
        self.assertEqual(harness.events, before)

    def test_provider_cleanup_failure_does_not_mask_provider_primary(self):
        harness = Harness()
        primary = RuntimeError('provider-original')
        cleanup = RuntimeError('provider-cleanup')

        def fail():
            harness.provider()
            raise primary

        def close():
            harness.provider_close()
            raise cleanup

        pipeline = harness.pipeline(provider=fail, provider_close=close)
        with self.assertRaises(RuntimeError) as caught:
            pipeline.run((harness.first, harness.second))
        self.assertIs(caught.exception, primary)
        self.assertEqual(pipeline.cleanup_errors, (cleanup,))
        self.assert_closed(pipeline, harness)

    def test_cleanup_only_failure_is_visible_and_both_cleanups_attempted(self):
        harness = Harness()
        cleanup = RuntimeError('close-only-failure')

        def close(handle):
            harness.handle_close(handle)
            raise cleanup

        pipeline = harness.pipeline(handle_close=close)
        with self.assertRaises(pipeline_api.CleanupError) as caught:
            pipeline.run((harness.first, harness.second))
        self.assertEqual(caught.exception.errors, (cleanup,))
        self.assertIn('second', harness.events)
        self.assertEqual(harness.events[-2:], ['handle-close', 'provider-close'])
        self.assert_closed(pipeline, harness)

    def test_close_new_and_prepared_are_idempotent(self):
        for prepare in (False, True):
            with self.subTest(prepare=prepare):
                harness = Harness()
                pipeline = harness.pipeline()
                if prepare:
                    pipeline.prepare()
                pipeline.close()
                before = list(harness.events)
                pipeline.close()
                self.assertEqual(harness.events, before)
                self.assertEqual(harness.events.count('provider-close'), int(prepare))
                self.assert_closed(pipeline, harness)

    def test_acquire_before_prepare_and_duplicate_prepare(self):
        harness = Harness()
        pipeline = harness.pipeline()
        with self.assertRaises(pipeline_api.PipelineStateError):
            pipeline.acquire()
        self.assertEqual(harness.events, [])
        pipeline.prepare()
        with self.assertRaises(pipeline_api.PipelineStateError):
            pipeline.prepare()
        self.assertEqual(harness.events.count('provider'), 1)
        pipeline.close()
        self.assert_closed(pipeline, harness)

    def test_context_cleanup_preserves_body_exception(self):
        harness = Harness()
        primary = RuntimeError('context-body-original')
        cleanup = RuntimeError('context-cleanup')

        def close(handle):
            harness.handle_close(handle)
            raise cleanup

        pipeline = harness.pipeline(handle_close=close)
        with self.assertRaises(RuntimeError) as caught:
            with pipeline as prepared:
                self.assertIs(prepared, pipeline)
                raise primary
        self.assertIs(caught.exception, primary)
        self.assertEqual(pipeline.cleanup_errors, (cleanup,))
        self.assert_closed(pipeline, harness)

    def test_context_normal_exit_closes(self):
        harness = Harness()
        pipeline = harness.pipeline()
        with pipeline as prepared:
            retained = prepared.acquire()
        self.assert_closed(pipeline, harness)
        self.assertEqual(retained.axes[0].source_id, 200)  # Prior ref is not revoked.

    def test_pipeline_import_inert_and_no_implicit_carrier_discovery(self):
        path = MODULE_DIR / 'staged_frozen_pipeline.py'
        tree = ast.parse(path.read_text(encoding='utf-8'))
        self.assertEqual([n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)],
                         ['dataclasses'])
        self.assertFalse(any(isinstance(n, ast.Import) for n in ast.walk(tree)))
        output = io.StringIO()
        try:
            with patch.object(builtins, 'open', side_effect=AssertionError('unexpected file read')), \
                    patch.object(os, 'getenv', side_effect=AssertionError('unexpected env read')), \
                    contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
                load_module('_stage_a2_import_probe', path)
            self.assertEqual(output.getvalue(), '')
        finally:
            sys.modules.pop('_stage_a2_import_probe', None)

    def test_provider_close_cancels_without_revival_or_later_dependencies(self):
        harness = Harness()
        states = []

        def cancel():
            payload = harness.provider()
            pipeline.close()
            states.append(pipeline.state)
            return payload

        pipeline = harness.pipeline(provider=cancel)
        with self.assertRaisesRegex(pipeline_api.PipelineStateError, 'cancelled during provider'):
            pipeline.run((harness.first, harness.second))
        self.assertEqual(states, ['closed'])
        self.assertEqual(harness.events, ['provider', 'provider-close'])
        self.assertEqual(harness.seen, [])
        self.assert_closed(pipeline, harness)
        pipeline.close()
        self.assertEqual(harness.events.count('provider-close'), 1)

    def test_handle_factory_close_then_returned_handle_is_released(self):
        harness = Harness()
        states = []

        def cancel(carrier):
            pipeline.close()
            states.append(pipeline.state)
            return harness.handle_factory(carrier)

        pipeline = harness.pipeline(handle_factory=cancel)
        with self.assertRaisesRegex(pipeline_api.PipelineStateError, 'cancelled during handle_factory'):
            pipeline.run((harness.first, harness.second))
        self.assertEqual(states, ['closed'])
        self.assertEqual(harness.events, ['provider', 'factory', 'provider-close',
                                         'handle-factory', 'handle-close'])
        self.assertEqual(harness.seen, [])
        self.assert_closed(pipeline, harness)
        pipeline.close()
        self.assertEqual(harness.events.count('provider-close'), 1)
        self.assertEqual(harness.events.count('handle-close'), 1)

    def test_carrier_factory_close_stops_before_handle_factory(self):
        harness = Harness()

        def cancel(**payload):
            carrier = harness.factory(**payload)
            pipeline.close()
            return carrier

        pipeline = harness.pipeline(carrier_factory=cancel)
        with self.assertRaisesRegex(pipeline_api.PipelineStateError, 'cancelled during carrier_factory'):
            pipeline.run((harness.first, harness.second))
        self.assertEqual(harness.events, ['provider', 'factory', 'provider-close'])
        self.assert_closed(pipeline, harness)

    def test_handle_acquire_close_cancels_during_prepare_and_later_acquire(self):
        for cancel_at in (1, 2):
            with self.subTest(cancel_at=cancel_at):
                harness = Harness()

                def cancel(handle):
                    carrier = harness.handle_acquire(handle)
                    if harness.events.count('acquire') == cancel_at:
                        pipeline.close()
                    return carrier

                pipeline = harness.pipeline(handle_acquire=cancel)
                if cancel_at == 2:
                    pipeline.prepare()
                with self.assertRaisesRegex(pipeline_api.PipelineStateError, 'cancelled during handle_acquire'):
                    if cancel_at == 1:
                        pipeline.prepare()
                    else:
                        pipeline.acquire()
                self.assertEqual(harness.seen, [])
                self.assertEqual(harness.events.count('provider-close'), 1)
                self.assertEqual(harness.events.count('handle-close'), 1)
                self.assert_closed(pipeline, harness)

    def test_consumer_close_cancellation_stops_remaining_work(self):
        for which in ('first', 'second'):
            with self.subTest(which=which):
                harness = Harness()

                def cancel(carrier):
                    harness.events.append(which)
                    pipeline.close()
                    return 'cancelled-result'

                pipeline = harness.pipeline()
                consumers = (cancel, harness.second) if which == 'first' else (harness.first, cancel)
                with self.assertRaisesRegex(pipeline_api.PipelineStateError, 'cancelled during ' + which):
                    pipeline.run(consumers)
                if which == 'first':
                    self.assertNotIn('second', harness.events)
                self.assertEqual(harness.events.count('provider-close'), 1)
                self.assertEqual(harness.events.count('handle-close'), 1)
                self.assert_closed(pipeline, harness)

    def test_late_handle_cleanup_failure_preserves_cancellation(self):
        harness = Harness()
        cleanup = RuntimeError('late-handle-cleanup')

        def cancel(carrier):
            pipeline.close()
            return harness.handle_factory(carrier)

        def close(handle):
            harness.handle_close(handle)
            raise cleanup

        pipeline = harness.pipeline(handle_factory=cancel, handle_close=close)
        with self.assertRaises(pipeline_api.PipelineStateError) as caught:
            pipeline.run((harness.first, harness.second))
        self.assertIn('cancelled during handle_factory', str(caught.exception))
        self.assertEqual(pipeline.cleanup_errors, (cleanup,))
        self.assertTrue(any('cleanup also failed' in note for note in caught.exception.__notes__))
        self.assertEqual(harness.events.count('provider-close'), 1)
        self.assertEqual(harness.events.count('handle-close'), 1)
        self.assert_closed(pipeline, harness)

    def test_callback_close_then_original_exception_keeps_first_error(self):
        harness = Harness()
        original = RuntimeError('original-after-cancel')

        def cancel_then_raise():
            harness.provider()
            pipeline.close()
            raise original

        pipeline = harness.pipeline(provider=cancel_then_raise)
        with self.assertRaises(RuntimeError) as caught:
            pipeline.run((harness.first, harness.second))
        self.assertIs(caught.exception, original)
        self.assertEqual(harness.events, ['provider', 'provider-close'])
        self.assert_closed(pipeline, harness)

    def test_cleanup_reentrant_close_does_not_repeat_ownership_tokens(self):
        harness = Harness()

        def close(handle):
            harness.handle_close(handle)
            pipeline.close()

        pipeline = harness.pipeline(handle_close=close)
        pipeline.run((harness.first, harness.second))
        self.assertEqual(harness.events.count('handle-close'), 1)
        self.assertEqual(harness.events.count('provider-close'), 1)
        self.assert_closed(pipeline, harness)

    def test_factory_result_type_collisions_rejected_before_handle_or_consumers(self):
        for mismatch in ('bool-id', 'float-year', 'bool-order'):
            with self.subTest(mismatch=mismatch):
                harness = Harness()
                if mismatch == 'bool-id':
                    harness.payload['axes'][0]['source_id'] = 1
                    harness.expected['axes'][0]['source_id'] = 1

                def fake(**payload):
                    carrier = harness.factory(**payload)
                    if mismatch == 'bool-id':
                        return replace(carrier, axes=(replace(carrier.axes[0], source_id=True),)
                                       + carrier.axes[1:])
                    if mismatch == 'float-year':
                        return replace(carrier, calendar=replace(carrier.calendar, target_year=2018.0))
                    return replace(carrier, axes=(carrier.axes[0], replace(carrier.axes[1], order=True))
                                   + carrier.axes[2:])

                pipeline = harness.pipeline(carrier_factory=fake)
                with self.assertRaisesRegex(pipeline_api.PipelineContractError, 'mismatch'):
                    pipeline.run((harness.first, harness.second))
                self.assertEqual(harness.events, ['provider', 'factory', 'provider-close'])
                self.assert_closed(pipeline, harness)


if __name__ == '__main__':
    unittest.main(verbosity=2)
