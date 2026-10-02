"""One synthetic process: unchanged old43 plus inactive data-only contracts.

No real seven-pin match, authenticated token, observed conversion or real matrix.
"""
import ast
import copy
import csv
from dataclasses import replace
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import struct
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def direct(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


old43 = direct('data_entry_prior43', 'tests/test_ch5_annual_k1b_middle_stage.py')
entry = direct('data_entry_inactive', 'validators/multi_province/annual_observed_labor_diagnostic/data_only.py')
context, adapter = old43.context, old43.adapter
AXIS, MAPPING = old43.AXIS, old43.MAPPING


class DataOnlyTests(unittest.TestCase):
    def invented_carrier(self):
        raw, sha = old43.previous.old.fixture()
        ctx = context.prepare_synthetic_context(raw, expected_fixture_sha256=sha,
            province_axis=AXIS, target_year=2018)
        carrier = adapter.prepare_annual_array(ctx, target_year=2018, province_axis=AXIS,
            source_sha256=sha, input_kind='synthetic', price_basis='synthetic_fixture',
            price_verified=False, province_mapping=MAPPING)
        return ctx, carrier

    def invoke(self, argv):
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch.object(sys, 'stdout', stdout), patch.object(sys, 'stderr', stderr):
            code = entry.main(argv)
        self.assertEqual(len(stdout.getvalue().splitlines()), 1)
        return code, json.loads(stdout.getvalue()), stderr.getvalue()

    def test_missing_flag_before_every_file_read_and_one_failure_json(self):
        with patch.object(Path, 'read_bytes', side_effect=AssertionError('no file reads')) as reader:
            code, payload, err = self.invoke(['--task-sha256', '0'*64])
        self.assertEqual(code, 1); reader.assert_not_called()
        self.assertEqual(payload['status'], 'DATA_ONLY_FAILURE')
        self.assertEqual(payload['execution_ledger']['first_failure']['phase'], 'cli_flag')
        self.assertEqual(payload['execution_ledger']['authentication']['attempted'], 0)
        self.assertNotIn('annual_phi_csv', payload)
        self.assertIn('cli_flag', err)

    def test_no_path_pin_metadata_or_output_override_flags(self):
        for option in ('--root', '--pins', '--metadata', '--output', '--province-axis', '--data'):
            with self.subTest(option=option), patch.object(Path, 'read_bytes') as reader:
                code, payload, _ = self.invoke(['--data-only', '--task-sha256', '0'*64, option, 'invented'])
                self.assertEqual(code, 1); reader.assert_not_called()
                self.assertEqual(payload['execution_ledger']['first_failure']['phase'], 'cli_flag')

    def test_wrong_unique_root_fails_before_task_and_raw_reads(self):
        with (patch.object(entry, '__file__', str(ROOT / 'invented_wrong_entry.py')),
                patch.object(Path, 'read_bytes') as reader):
            code, payload, _ = self.invoke(['--data-only', '--task-sha256', '0'*64])
        self.assertEqual(code, 1); reader.assert_not_called()
        self.assertEqual(payload['execution_ledger']['first_failure']['phase'], 'administrative_execution_gate')

    def test_task_hash_mismatch_never_reads_raw(self):
        reads = []
        def administrative_read(path):
            reads.append(path)
            self.assertEqual(path, ROOT / 'TASK_CURRENT.md')
            return b'invented administrative task bytes'
        with patch.object(Path, 'read_bytes', administrative_read):
            code, payload, _ = self.invoke(['--data-only', '--task-sha256', '0'*64])
        self.assertEqual(code, 1); self.assertEqual(len(reads), 1)
        self.assertIn('task raw identity mismatch', payload['execution_ledger']['first_failure']['message'])

    def test_engineering_task_cannot_activate_real_entry(self):
        raw = b'Status: ISSUED__INACTIVE_DATA_ONLY_PUBLIC_ENTRY_ENGINEERING__ZERO_REAL_EXECUTION.\n'
        with patch.object(Path, 'read_bytes', return_value=raw) as reader:
            code, payload, _ = self.invoke(['--data-only', '--task-sha256', entry.digest(raw)])
        self.assertEqual(code, 1); self.assertEqual(reader.call_count, 1)
        self.assertIn('separate one-shot', payload['execution_ledger']['first_failure']['message'])

    def test_missing_work_binding_fails_before_raw_reads(self):
        raw = (entry.EXECUTION_STATUS + '\n').encode()
        with patch.object(Path, 'read_bytes', return_value=raw) as reader:
            code, payload, _ = self.invoke(['--data-only', '--task-sha256', entry.digest(raw)])
        self.assertEqual(code, 1); self.assertEqual(reader.call_count, 1)
        self.assertIn('exact Work execution binding', payload['execution_ledger']['first_failure']['message'])

    def test_wrong_receipt_pin_stops_at_administrative_receipt(self):
        binding = dict(schema=entry.BINDING_SCHEMA, work_receipt_sha256='0'*64,
            independent_review_sha256='0'*64, candidate_sha256={})
        raw = (entry.EXECUTION_STATUS + '\nDataOnlyExecutionBinding: ' + json.dumps(binding) + '\n').encode()
        reads = []
        def administrative_read(path):
            reads.append(path)
            if path == ROOT / 'TASK_CURRENT.md':
                return raw
            self.assertEqual(path, ROOT / entry.RECEIPT_PATH)
            return b'invented administrative receipt'
        with patch.object(Path, 'read_bytes', administrative_read):
            code, payload, _ = self.invoke(['--data-only', '--task-sha256', entry.digest(raw)])
        self.assertEqual(code, 1); self.assertEqual(len(reads), 2)
        self.assertIn('Work receipt identity mismatch', payload['execution_ledger']['first_failure']['message'])

    def test_exact_fixed_seven_locators_and_pins(self):
        self.assertEqual(dict(entry.PINS), dict(context.PINS))
        self.assertEqual(set(entry.LOCATORS), set(context.PINS))
        self.assertEqual(entry.LOCATORS['audit'], 'EVIDENCE/ch5_revised_data_table_20260930/data_audit.json')
        self.assertEqual(entry.LOCATORS['gdp'], 'EVIDENCE/ch5_revised_data_table_20260930/nbs_gdp_display.json')
        self.assertEqual(entry.LOCATORS['population'], 'EVIDENCE/ch5_revised_data_table_20260930/nbs_population_display.json')
        self.assertEqual(entry.LOCATORS['manifest'], context._OBSERVED_MANIFEST_IDENTIFIER)
        self.assertEqual(entry.LOCATORS['attribution'], 'EVIDENCE/ch5_methodological_price_binding_20260930/attribution_record.json')
        self.assertEqual(entry.LOCATORS['adapter'], 'EVIDENCE/ch5_inactive_gdp_data_adapter_20260930/adapter.py')
        self.assertEqual(entry.LOCATORS['helper'], 'src/ch5_two_asset_hank/corrected_diagnostic/lagged_observed_gdp_wedge.py')
        self.assertEqual(tuple((i, full) for i, full, _ in adapter.CANONICAL_PROVINCE_MAPPING), context.CANONICAL_AXIS)
        self.assertEqual(len(adapter.CANONICAL_PROVINCE_MAPPING), 31)
        with self.assertRaises(TypeError): entry.PINS['audit'] = '0'*64
        with self.assertRaises(TypeError): entry.LOCATORS['audit'] = 'invented'

    def test_bad_raw_hash_retains_attempt_suppresses_parse_and_conversion(self):
        progress = ['administrative.saved_before_failure']
        raw = {key: b'invented wrong raw bytes only' for key in context.PINS}
        with (patch.object(context, '_json', side_effect=AssertionError('no parse')) as parser,
                patch.object(context, '_prepare_authenticated_observed_context',
                             side_effect=AssertionError('no conversion')) as kernel):
            with self.assertRaisesRegex(ValueError, 'raw source identity mismatch'):
                context.prepare_observed_data_only_context(raw, data_only=True, progress=progress)
        parser.assert_not_called(); kernel.assert_not_called()
        self.assertEqual(progress, ['administrative.saved_before_failure', 'data_only.authentication_attempted'])
        ledger = entry.execution_ledger(progress, first_failure={'phase': 'authentication'})
        self.assertEqual(ledger['authentication'], {'attempted': 1, 'completed': 0})
        self.assertEqual(ledger['annual_conversion'], {'attempted': 0, 'completed': 0})
        self.assertEqual(ledger['accepted_helper'], {'attempted': 0, 'completed': 0})
        with self.assertRaisesRegex(ValueError, 'already attempted'):
            context.prepare_observed_data_only_context(raw, data_only=True, progress=progress)
        self.assertEqual(progress.count('data_only.authentication_attempted'), 1)

    def test_explicit_public_api_types_before_authentication(self):
        raw = {key: b'invented' for key in context.PINS}
        with patch.object(context, 'authenticate_observed_binding', side_effect=AssertionError('no auth')) as auth:
            for bad in (False, 1, 'True', None):
                with self.assertRaises(context.ProductionBlocked):
                    context.prepare_observed_data_only_context(raw, data_only=bad, progress=[])
            for bad in ((), ['string', 1], None):
                with self.assertRaises(ValueError):
                    context.prepare_observed_data_only_context(raw, data_only=True, progress=bad)
        auth.assert_not_called()

    def test_public_routes_structure_and_old_production_block_preserved(self):
        source = (ROOT / entry.CONTEXT_PATH).read_text(encoding='utf-8')
        tree = ast.parse(source)
        functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
        old = functions['prepare_observed_context']
        self.assertTrue(any(isinstance(node, ast.Raise) and isinstance(node.exc, ast.Call)
                            and isinstance(node.exc.func, ast.Name) and node.exc.func.id == 'ProductionBlocked'
                            for node in ast.walk(old)))
        new = functions['prepare_observed_data_only_context']
        calls = [node.func.id for node in ast.walk(new)
                 if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)]
        self.assertEqual(calls.count('authenticate_observed_binding'), 1)
        self.assertEqual(calls.count('_prepare_authenticated_observed_context'), 1)
        self.assertLess(calls.index('authenticate_observed_binding'), calls.index('_prepare_authenticated_observed_context'))
        self.assertFalse(any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(new)))
        self.assertNotIn('_prepare_authenticated_observed_context', [node.func.id for node in ast.walk(old)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)])

    def test_genuine_synthetic_carrier_csv_roundtrip_direction_and_hash(self):
        ctx, carrier = self.invented_carrier()
        master = carrier.phi_destination_origin
        payload = entry.serialize_prepared_carrier(ctx, carrier, adapter, [])
        rows = list(csv.DictReader(io.StringIO(payload['annual_phi_csv'])))
        decoded = [[0.]*3 for _ in range(3)]
        for row in rows:
            j, i = int(row['destination_index'])-1, int(row['origin_index'])-1
            self.assertEqual(row['destination_source_name'], AXIS[j][1])
            self.assertEqual(row['origin_source_name'], AXIS[i][1])
            decoded[j][i] = float(row['phi'])
        self.assertEqual(len(rows), 9)
        self.assertEqual(tuple(map(tuple, decoded)), ctx.phi_destination_origin)
        self.assertGreater(decoded[0][1], 1.); self.assertLess(decoded[1][0], 1.)
        little_c = b''.join(struct.pack('<d', value) for row in decoded for value in row)
        expected = hashlib.sha256(little_c).hexdigest().upper()
        manifest = payload['annual_context_manifest']
        self.assertEqual(manifest['numerical_sha256'], expected)
        self.assertEqual(manifest['tuple_sha256'], expected)
        self.assertEqual(manifest['master_sha256'], expected)
        self.assertEqual(manifest['shape'], [3, 3])
        self.assertEqual(manifest['csv_sha256'], entry.digest(payload['annual_phi_csv'].encode('utf-8')))
        self.assertIs(carrier.phi_destination_origin, master)
        self.assertIs(carrier.annual_context, ctx)
        self.assertFalse(manifest['frozen_k1b_field_hash_equivalence'])
        summary = manifest['master_validation']
        self.assertEqual(summary['shape'], [3, 3]); self.assertEqual(summary['entry_count'], 9)
        self.assertIs(summary['finite'], True); self.assertIs(summary['diagonal_exact_one'], True)
        self.assertEqual(summary['min'], min(value for row in decoded for value in row))
        self.assertEqual(summary['max'], max(value for row in decoded for value in row))

    def test_serializer_preserves_synthetic_provenance_activation_and_units(self):
        ctx, carrier = self.invented_carrier()
        payload = entry.serialize_prepared_carrier(ctx, carrier, adapter, [])
        meta = payload['snapshot_metadata']
        self.assertEqual(meta['input_kind'], 'synthetic')
        self.assertEqual(meta['price_basis'], 'synthetic_fixture')
        self.assertEqual(meta['provenance'], dict(ctx.provenance))
        self.assertEqual(meta['expected_pins'], {})
        self.assertEqual(meta['information_set'], 'synthetic_fixture')
        self.assertEqual((meta['target_year'], meta['observation_year']), (2018, 2017))
        self.assertEqual((meta['gdp_unit'], meta['population_unit']), ('亿元', '万人'))
        self.assertEqual(meta['official_release_date'], 'UNKNOWN')
        self.assertIs(meta['price_verified'], False)
        self.assertIs(meta['model_activation'], False)
        self.assertIs(meta['results_eligibility'], False)
        self.assertEqual(json.loads(json.dumps(payload, allow_nan=False))['snapshot_metadata']['province_mapping'], [list(row) for row in MAPPING])

    def test_serializer_rejects_copied_or_replaced_carrier(self):
        ctx, carrier = self.invented_carrier()
        for bad in (copy.copy(carrier), replace(carrier)):
            with self.assertRaises(ValueError):
                entry.serialize_prepared_carrier(ctx, bad, adapter, [])

    def test_once_synthetic_helper_and_no_serializer_recomputation(self):
        helper = context._helper()
        with patch.object(helper, 'build_annual_labor_wedge', wraps=helper.build_annual_labor_wedge) as build:
            ctx, carrier = self.invented_carrier()
            entry.serialize_prepared_carrier(ctx, carrier, adapter, [])
            entry.serialize_prepared_carrier(ctx, carrier, adapter, [])
        self.assertEqual(build.call_count, 1)

    def test_failure_ledger_preserves_events_and_unknown_inner_attempts(self):
        events = ['data_only.raw_read.manifest_attempted', 'data_only.raw_read.manifest_completed',
            'data_only.raw_read.attribution_attempted']
        failure = {'phase': 'raw_read.attribution', 'type': 'OSError', 'message': 'invented failure'}
        ledger = entry.execution_ledger(events, first_failure=failure)
        self.assertEqual(ledger['events'], events)
        self.assertEqual(ledger['raw_reads']['attribution'], {'attempted': 1, 'completed': 0})
        self.assertEqual(ledger['raw_reads']['audit'], {'attempted': 0, 'completed': 0})
        self.assertEqual(ledger['first_failure'], failure)
        events += ['data_only.authentication_attempted', 'data_only.authentication_completed',
                   'data_only.annual_conversion_attempted']
        ledger = entry.execution_ledger(events, first_failure={'phase': 'annual_conversion'})
        self.assertEqual(ledger['annual_conversion'], {'attempted': 1, 'completed': 0})
        self.assertEqual(ledger['accepted_helper'], {'attempted': 'UNKNOWN', 'completed': 'UNKNOWN'})
        self.assertEqual(ledger['annual_master'], {'attempted': 'UNKNOWN', 'completed': 'UNKNOWN'})
        self.assertEqual(ledger['array'], {'attempted': 0, 'completed': 0})
        self.assertIs(ledger['objective_a_window_accepted'], False)
        self.assertEqual(ledger['objective_a'], 'RETAINED')
        self.assertEqual(ledger['historical_actual_ledgers'], 'CALL_LEDGER_UNRESOLVED')

    def test_retained_verified_bytes_execute_without_path_or_pyc_reads(self):
        source = b'from dataclasses import dataclass\n@dataclass\nclass Owned:\n    value: str = "verified-source"\n'
        with patch.object(Path, 'read_bytes', side_effect=AssertionError('no path reread')) as reader:
            module = entry.direct_module('_data_only_verified_fixture', 'invented_loader_fixture.py', source)
        reader.assert_not_called()
        self.assertEqual(module.Owned().value, 'verified-source')
        self.assertEqual(module.__file__, str(ROOT / 'invented_loader_fixture.py'))
        self.assertIs(sys.modules['_data_only_verified_fixture'], module)
        with self.assertRaises(ValueError):
            entry.direct_module('_data_only_wrong_bytes', 'invented_loader_fixture.py', bytearray(source))

    def test_helper_preload_rejects_invented_bytes_before_execution(self):
        with patch.object(Path, 'read_bytes', side_effect=AssertionError('no path read')) as reader:
            with self.assertRaisesRegex(ValueError, 'helper'):
                context._preload_data_only_helper(b'invented wrong helper bytes')
        reader.assert_not_called()

    def test_exact_original_helper_source_preloaded_without_unbound_cache(self):
        # Source-code provenance only, no observed sources or authentication success.
        raw_helper = (ROOT / entry.LOCATORS['helper']).read_bytes()
        self.assertEqual(entry.digest(raw_helper), context.PINS['helper'])
        with patch.object(Path, 'read_bytes', side_effect=AssertionError('no path reread')) as reader:
            context._preload_data_only_helper(raw_helper)
        reader.assert_not_called()
        helper = sys.modules['_annual_accepted_wedge_helper']
        self.assertEqual(helper.__file__, str(ROOT / entry.LOCATORS['helper']))
        self.assertEqual(helper.build_annual_labor_wedge.__code__.co_filename, helper.__file__)
        # The genuine synthetic API continues to use this exact compiled helper.
        ctx, carrier = self.invented_carrier()
        self.assertEqual(ctx.input_kind, 'synthetic')
        self.assertIs(carrier.annual_context, ctx)

    def test_gate_retains_hash_checked_sources_and_loader_never_uses_path_loader(self):
        tree = ast.parse((ROOT / entry.ENTRY_PATH).read_text(encoding='utf-8'))
        functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
        loader = functions['direct_module']
        calls = [node.func.id if isinstance(node.func, ast.Name) else getattr(node.func, 'attr', '')
                 for node in ast.walk(loader) if isinstance(node, ast.Call)]
        self.assertIn('compile', calls); self.assertIn('exec', calls); self.assertIn('ModuleType', calls)
        self.assertFalse(set(calls) & {'read_bytes', 'exec_module', 'spec_from_file_location'})
        gate = ast.get_source_segment((ROOT / entry.ENTRY_PATH).read_text(encoding='utf-8'),
                                      functions['check_execution_gate'])
        self.assertIn('verified_sources[relative] = source_bytes', gate)
        self.assertIn('verified_sources[ADAPTER_PATH] = adapter_bytes', gate)

    def test_completed_inner_stages_only_after_conversion_return(self):
        empty = entry.execution_ledger([])
        self.assertEqual(empty['accepted_helper'], {'attempted': 0, 'completed': 0})
        self.assertEqual(empty['annual_master'], {'attempted': 0, 'completed': 0})
        # Ledger-only invented evidence, not a simulated observed token or successful API.
        events = ['data_only.annual_conversion_attempted', 'data_only.annual_conversion_completed']
        complete = entry.execution_ledger(events)
        self.assertEqual(complete['accepted_helper'], {'attempted': 1, 'completed': 1})
        self.assertEqual(complete['annual_master'], {'attempted': 1, 'completed': 1})

    def test_standalone_source_has_no_filesystem_writes_or_science_dependencies(self):
        tree = ast.parse((ROOT / entry.ENTRY_PATH).read_text(encoding='utf-8'))
        forbidden = {'open', 'mkdir', 'write_text', 'write_bytes', 'replace', 'unlink', 'rename',
                     'remove', 'rmdir', 'mkstemp', 'TemporaryDirectory', 'NamedTemporaryFile'}
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                name = node.func.id if isinstance(node.func, ast.Name) else getattr(node.func, 'attr', '')
                self.assertNotIn(name, forbidden)
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                names = [alias.name for alias in node.names] if isinstance(node, ast.Import) else [node.module]
                self.assertFalse(any(name and ('ch5_two_asset_hank' in name or 'scipy' in name
                    or 'integration' in name or 'middle_stage' in name) for name in names))
        self.assertFalse(any(name == 'ch5_two_asset_hank' or name.startswith('ch5_two_asset_hank.') for name in sys.modules))
        self.assertEqual(entry.execution_ledger([])['filesystem_writes'], 0)
        self.assertIs(sys.dont_write_bytecode, True)
        prefix = (ROOT / entry.ENTRY_PATH).read_text(encoding='utf-8')
        self.assertLess(prefix.index('sys.dont_write_bytecode = True'), prefix.index('import argparse'))


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    suite.addTests(old43.load_tests(loader, None, None))
    suite.addTests(loader.loadTestsFromTestCase(DataOnlyTests))
    return suite


if __name__ == '__main__':
    unittest.main(verbosity=2)
