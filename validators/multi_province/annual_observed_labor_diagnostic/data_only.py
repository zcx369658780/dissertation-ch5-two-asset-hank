"""Inactive explicit data-only CLI. Filesystem reads only; one JSON to stdout.

Future execution requires a separately issued task and independent Work receipt.
No scientific entry, consumer, output directory or caller-supplied data binding.
Objective A's hostile-path/final-check window is not resolved by this module.
"""
import sys
sys.dont_write_bytecode = True

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import re
from types import MappingProxyType, ModuleType

ROOT = Path(r'D:\ProjectTemp\c5k1bturn56')
CONTEXT_PATH = 'src/ch5_two_asset_hank/corrected_diagnostic/annual_observed_labor_context.py'
ADAPTER_PATH = 'src/ch5_two_asset_hank/corrected_diagnostic/annual_labor_array_adapter.py'
ENTRY_PATH = 'validators/multi_province/annual_observed_labor_diagnostic/data_only.py'
TEST_PATH = 'tests/test_ch5_observed_annual_data_only_entry.py'
REVIEW_PATH = 'EVIDENCE/ch5_observed_annual_data_only_entry_engineering_20260930/independent_work_review.md'
RECEIPT_PATH = 'EVIDENCE/ch5_observed_annual_data_only_entry_engineering_20260930/work_execution_binding.json'
EXECUTION_STATUS = 'Status: ISSUED__ONE_SHOT_OBSERVED_ANNUAL_DATA_ONLY_EXECUTION.'
BINDING_SCHEMA = 'CH5_OBSERVED_ANNUAL_DATA_ONLY_EXECUTION_BINDING_V1'
ACCEPT_VERDICT = 'ACCEPT__INACTIVE_DATA_ONLY_PUBLIC_ENTRY_ENGINEERING_ONLY'
LOCATORS = MappingProxyType({
    'manifest': 'EVIDENCE/ch5_methodological_price_binding_20260930/source_binding_manifest.json',
    'attribution': 'EVIDENCE/ch5_methodological_price_binding_20260930/attribution_record.json',
    'audit': 'EVIDENCE/ch5_revised_data_table_20260930/data_audit.json',
    'gdp': 'EVIDENCE/ch5_revised_data_table_20260930/nbs_gdp_display.json',
    'population': 'EVIDENCE/ch5_revised_data_table_20260930/nbs_population_display.json',
    'adapter': 'EVIDENCE/ch5_inactive_gdp_data_adapter_20260930/adapter.py',
    'helper': 'src/ch5_two_asset_hank/corrected_diagnostic/lagged_observed_gdp_wedge.py',
})
PINS = MappingProxyType({
    'manifest': '4F28039F5192172E1A7524018DD6679BED1E5A1F4C837B8251B9596473C8C566',
    'attribution': 'E94C976FBD93262D98E776777E295EC9DDBA92B26E1D48A7E0D2496CC6C0E91B',
    'audit': '1D3DE27EBAE90EBE8D2F3CB42880BD2FBDB68CFA22BEBBE866479180380BC936',
    'gdp': '5129836B3781ECAE9FA21D7082193A22ACF5B1A40389605ABB0ACC30AD1127CB',
    'population': 'F837137765DDE99B56578E8404621218A4CA716FEF40BF8F16E75B8F8C79F0C3',
    'adapter': '0BEB77FA60C95227E79EFC32C497C2F28D9C2DEBADC09987A3512A96384A226D',
    'helper': '7B9A490F382E3007820E70C68D2EFB5992DE25BC8455EDE8B265CA33F384AF56',
})
ARRAY_ADAPTER_PIN = '137BFB6C3F0B3D7F4672A78ECCB006A776CB1A40B258CB30A3B18437D4BFCF41'


def digest(raw):
    return hashlib.sha256(raw).hexdigest().upper()


def strict_json(raw):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('duplicate binding field')
            result[key] = value
        return result
    return json.loads(raw, object_pairs_hook=unique)


def require_hash(value):
    if type(value) is not str or re.fullmatch('[0-9A-F]{64}', value) is None:
        raise ValueError('explicit uppercase SHA256 required')
    return value


def check_execution_gate(task_sha256):
    """All administrative authority checks precede every raw-source read.

Future TASK has one DataOnlyExecutionBinding: compact JSON line with schema,
work_receipt_sha256, independent_review_sha256 and candidate_sha256 fields.
The fixed Work receipt repeats schema/candidate_sha256/independent_review_sha256,
with verdict, real_process_max=1, repairs=0, retries=0 and zero_science=true.
The CLI task digest is supplied by Work; neither receipt nor task is created here.
"""
    if Path(__file__).resolve() != ROOT / ENTRY_PATH:
        raise ValueError('unique worktree/entry identity required')
    require_hash(task_sha256)
    task_raw = (ROOT / 'TASK_CURRENT.md').read_bytes()
    if digest(task_raw) != task_sha256:
        raise ValueError('current task raw identity mismatch')
    lines = task_raw.decode('utf-8-sig').splitlines()
    statuses = [line for line in lines if line.startswith('Status:')]
    if statuses != [EXECUTION_STATUS]:
        raise ValueError('separate one-shot actual data-only task required')
    bindings = [line.removeprefix('DataOnlyExecutionBinding: ')
                for line in lines if line.startswith('DataOnlyExecutionBinding: ')]
    if len(bindings) != 1:
        raise ValueError('exact Work execution binding required')
    binding = strict_json(bindings[0])
    if type(binding) is not dict or set(binding) != {
            'schema', 'work_receipt_sha256', 'independent_review_sha256', 'candidate_sha256'}:
        raise ValueError('execution binding schema mismatch')
    if binding['schema'] != BINDING_SCHEMA:
        raise ValueError('execution binding version mismatch')
    receipt_raw = (ROOT / RECEIPT_PATH).read_bytes()
    if digest(receipt_raw) != require_hash(binding['work_receipt_sha256']):
        raise ValueError('Work receipt identity mismatch')
    receipt = strict_json(receipt_raw.decode('utf-8-sig'))
    if type(receipt) is not dict or set(receipt) != {
            'schema', 'verdict', 'candidate_sha256', 'independent_review_sha256',
            'real_process_max', 'repairs', 'retries', 'zero_science'}:
        raise ValueError('Work receipt schema mismatch')
    if (receipt['schema'] != BINDING_SCHEMA or receipt['verdict'] != ACCEPT_VERDICT
            or type(receipt['real_process_max']) is not int or receipt['real_process_max'] != 1
            or type(receipt['repairs']) is not int or receipt['repairs'] != 0
            or type(receipt['retries']) is not int or receipt['retries'] != 0
            or receipt['zero_science'] is not True):
        raise ValueError('independent acceptance/once-only contract required')
    candidates = binding['candidate_sha256']
    if type(candidates) is not dict or set(candidates) != {CONTEXT_PATH, ENTRY_PATH, TEST_PATH}:
        raise ValueError('exact three-candidate binding required')
    if receipt['candidate_sha256'] != candidates:
        raise ValueError('task/Work candidate binding mismatch')
    review_pin = require_hash(binding['independent_review_sha256'])
    if receipt['independent_review_sha256'] != review_pin:
        raise ValueError('task/Work review binding mismatch')
    if digest((ROOT / REVIEW_PATH).read_bytes()) != review_pin:
        raise ValueError('independent Work review identity mismatch')
    verified_sources = {}
    for relative, pin in candidates.items():
        source_bytes = (ROOT / relative).read_bytes()
        if digest(source_bytes) != require_hash(pin):
            raise ValueError('reviewed candidate identity mismatch')
        verified_sources[relative] = source_bytes
    adapter_bytes = (ROOT / ADAPTER_PATH).read_bytes()
    if digest(adapter_bytes) != ARRAY_ADAPTER_PIN:
        raise ValueError('accepted array adapter identity mismatch')
    verified_sources[ADAPTER_PATH] = adapter_bytes
    return ({'task_sha256': task_sha256, 'candidate_sha256': dict(candidates),
            'independent_review_sha256': review_pin,
            'work_receipt_sha256': binding['work_receipt_sha256']}, verified_sources)


def direct_module(name, relative, verified_source_bytes):
    """Execute retained verified bytes, never a path loader or cached bytecode."""
    if type(verified_source_bytes) is not bytes:
        raise ValueError('retained verified source bytes required')
    filename = str(ROOT / relative)
    code = compile(verified_source_bytes, filename, 'exec')
    module = ModuleType(name)
    module.__file__ = filename
    module.__package__ = ''
    sys.modules[name] = module
    exec(code, module.__dict__)
    return module


def execution_ledger(events, *, first_failure=None):
    """Completed stages are never inferred from a partial result.

The unchanged conversion kernel has no inner callback: after conversion failure,
helper/master inner attempts are UNKNOWN, never falsely zero or complete.
"""
    def stage(prefix):
        return {'attempted': int(prefix + '_attempted' in events),
                'completed': int(prefix + '_completed' in events)}
    converted = 'data_only.annual_conversion_completed' in events
    converting = 'data_only.annual_conversion_attempted' in events
    return {
        'schema': 'CH5_DATA_ONLY_ATTEMPTS_V1', 'events': list(events),
        'raw_reads': {key: stage('data_only.raw_read.' + key) for key in LOCATORS},
        'authentication': stage('data_only.authentication'),
        'helper_code_binding': stage('data_only.helper_code_binding'),
        'annual_conversion': stage('data_only.annual_conversion'),
        'accepted_helper': {'attempted': 1 if converted else ('UNKNOWN' if converting else 0),
                            'completed': 1 if converted else ('UNKNOWN' if converting else 0)},
        'annual_master': {'attempted': 1 if converted else ('UNKNOWN' if converting else 0),
                          'completed': 1 if converted else ('UNKNOWN' if converting else 0)},
        'array': stage('data_only.array'), 'serialization': stage('data_only.serialization'),
        'first_failure': first_failure, 'repairs': 0, 'retries': 0,
        'scientific_calls': 0, 'model_calls': 0, 'production_calls': 0,
        'model_activation': False, 'results_eligibility': False,
        'objective_a': 'RETAINED', 'objective_a_window_accepted': False,
        'historical_actual_ledgers': 'CALL_LEDGER_UNRESOLVED', 'c9': 'PAUSED',
        'filesystem_writes': 0,
    }


def serialize_prepared_carrier(context, carrier, adapter, events):
    """Serialize the same sealed master; never recompute the annual formula.

Genuine invented carriers retain their synthetic label. Real CLI requires observed.
"""
    import numpy as np
    metadata = dict(target_year=context.target_year, province_axis=context.province_axis,
        source_sha256=context.source_sha256, input_kind=context.input_kind,
        price_basis=context.price_basis, price_verified=context.price_verified)
    adapter.AnnualArrayCarrier.validate(carrier, annual_context=context,
        province_mapping=carrier.province_mapping, **metadata)
    master = carrier.phi_destination_origin
    little_c = np.asarray(master, dtype='<f8').tobytes(order='C')
    tuple_c = np.asarray(context.phi_destination_origin, dtype='<f8').tobytes(order='C')
    if little_c != tuple_c or carrier.annual_context is not context:
        raise ValueError('same tuple/kernel/array master identity required')
    text = io.StringIO(newline='')
    writer = csv.writer(text, lineterminator='\n')
    writer.writerow(('destination_index', 'destination_source_name',
                     'origin_index', 'origin_source_name', 'phi'))
    for j, (destination, destination_name) in enumerate(context.province_axis):
        for i, (origin, origin_name) in enumerate(context.province_axis):
            writer.writerow((destination, destination_name, origin, origin_name,
                             format(float(master[j, i]), '.17g')))
    phi_csv = text.getvalue()
    synthetic = context.input_kind == 'synthetic'
    provenance = dict(context.provenance)
    details = {
        **metadata, 'observation_year': context.observation_year,
        'province_mapping': carrier.province_mapping,
        'provenance': provenance, 'expected_pins': {} if synthetic else dict(PINS),
        'information_set': 'synthetic_fixture' if synthetic else provenance['information_set'],
        'population_basis': 'year_end_resident',
        'official_release_date': 'UNKNOWN', 'price_base_year': None,
        'gdp_unit': '亿元', 'population_unit': '万人',
        'per_person_proxy': '10000*GDP(亿元)/population(万人); not official per-capita GDP',
        'formula': 'phi[j,i]=1+0.3*(q_i-q_j)/(q_i+q_j)',
        'axis_semantics': 'destination-row/origin-column',
        'model_activation': False, 'results_eligibility': False,
    }
    manifest = {
        'input_kind': context.input_kind, 'shape': list(master.shape),
        'province_axis': context.province_axis, 'province_mapping': carrier.province_mapping,
        'numerical_sha256': digest(little_c), 'tuple_sha256': digest(tuple_c),
        'master_sha256': digest(little_c), 'same_context_and_master': True,
        'hash_definition': 'SHA256 uppercase, little-endian float64, C-order bytes, no shape tag',
        'frozen_k1b_field_hash_equivalence': False,
        'csv_sha256': digest(phi_csv.encode('utf-8')), 'csv_numeric_format': '.17g float64 roundtrip',
        'expected_pins': {} if synthetic else dict(PINS),
        'filesystem_write_authority': False, 'science_consumer_authority': False,
        'master_validation': {
            'shape': list(master.shape), 'entry_count': int(master.size),
            'finite': bool(np.isfinite(master).all()),
            'diagonal_exact_one': bool((master.diagonal() == 1.).all()),
            'min': float(master.min()), 'max': float(master.max()),
            'definition': 'read-only summary of the same sealed master; no new numerical criterion',
        },
    }
    return {'snapshot_metadata': details, 'annual_phi_csv': phi_csv,
            'annual_context_manifest': manifest}


class CLIError(ValueError):
    pass


class DataOnlyParser(argparse.ArgumentParser):
    def error(self, message):
        raise CLIError(message)
    def exit(self, status=0, message=None):
        raise CLIError(message or 'no execution requested')


def main(argv=None):
    events = []
    phase = 'cli_flag'
    try:
        arguments = list(sys.argv[1:] if argv is None else argv)
        if '--data-only' not in arguments:
            raise CLIError('explicit --data-only required before all filesystem reads')
        parser = DataOnlyParser(add_help=False, allow_abbrev=False)
        parser.add_argument('--data-only', action='store_true', required=True)
        parser.add_argument('--task-sha256', required=True)
        args = parser.parse_args(arguments)
        phase = 'administrative_execution_gate'
        binding, verified_sources = check_execution_gate(args.task_sha256)
        phase = 'standalone_modules'
        context_module = direct_module('_data_only_annual_context', CONTEXT_PATH,
                                       verified_sources[CONTEXT_PATH])
        adapter = direct_module('_data_only_annual_adapter', ADAPTER_PATH,
                                verified_sources[ADAPTER_PATH])
        if dict(context_module.PINS) != dict(PINS):
            raise ValueError('context/CLI fixed pins differ')
        raw = {}
        for key, relative in LOCATORS.items():
            phase = 'raw_read.' + key
            events.append('data_only.raw_read.' + key + '_attempted')
            raw[key] = (ROOT / relative).read_bytes()
            events.append('data_only.raw_read.' + key + '_completed')
        phase = 'authentication_or_annual_conversion'
        context = context_module.prepare_observed_data_only_context(raw, data_only=True, progress=events)
        if context.input_kind != 'observed':
            raise ValueError('real CLI never accepts a synthetic replacement')
        phase = 'array'
        events.append('data_only.array_attempted')
        carrier = adapter.prepare_annual_array(context,
            target_year=2018, province_axis=context_module.CANONICAL_AXIS,
            source_sha256=PINS['manifest'], input_kind='observed',
            price_basis='current_price_methodologically_attributed', price_verified=False,
            province_mapping=adapter.CANONICAL_PROVINCE_MAPPING)
        events.append('data_only.array_completed')
        phase = 'serialization'
        events.append('data_only.serialization_attempted')
        payload = serialize_prepared_carrier(context, carrier, adapter, events)
        events.append('data_only.serialization_completed')
        payload.update(status='DATA_ONLY_SUCCESS', execution_binding=binding,
                       execution_ledger=execution_ledger(events))
        encoded = json.dumps(payload, ensure_ascii=True, allow_nan=False)
    except Exception as exc:
        if phase == 'authentication_or_annual_conversion':
            phase = ('annual_conversion' if 'data_only.annual_conversion_attempted' in events
                     else 'helper_code_binding' if 'data_only.authentication_completed' in events
                     else 'authentication')
        failure = {'phase': phase, 'type': type(exc).__name__, 'message': str(exc)}
        encoded = json.dumps({'status': 'DATA_ONLY_FAILURE',
            'execution_ledger': execution_ledger(events, first_failure=failure)},
            ensure_ascii=True, allow_nan=False)
        sys.stderr.write('data-only stopped: ' + phase + '\n')
        sys.stdout.write(encoded + '\n')
        return 1
    sys.stdout.write(encoded + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
