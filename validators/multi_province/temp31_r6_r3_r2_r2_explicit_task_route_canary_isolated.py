"""Explicit identity route canary; no target execution or default task route.

One real CLI invocation contains one positive and three in-memory rejections.
Only two fixed task-local connector receipts are read after argument validation.
The audit hook observes the canary body after standard-library imports, and
rejects other file opens and process/network/native-library launch facilities.
This hook is in-process instrumentation, not independent OS enforcement.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
from datetime import datetime, timezone

TASK = 'CH5_TEMP31_R6_R3_R2_R2_EXPLICIT_RUNTIME_ROUTER_CANARY_20261031'
TARGET = 'CH5_TEMP31_R6_R3_R2_120S_ISOLATED_PREFDIR_NATIVE_STARTUP_20261030'
GOVERNANCE = 'c98f0bb543b1f4f9be48094f1d5935e534af7e4a'
R40_AUTHORITY = 'POST_R5_R6_HJB_TRAJECTORY_R40_TARGET_HJB_NONCONVERGENCE_DECOMPOSITION'
EXPECTED = {
    'diagnostic_task_id': TASK,
    'target_task_id': TARGET,
    'target_contract_commit': '40e7b2e1ee93973ca63b509f53f20e21c6f149ad',
    'target_contract_path': 'tasks/' + TARGET + '/CONTRACT.md',
    'target_contract_blob': '1d7c4c960b9b6d47cc9e8182afd2859372caa168',
    'target_contract_bytes': 15857,
    'governance_commit': GOVERNANCE,
    'governance_contract_path': 'tasks/' + TASK + '/CONTRACT.md',
    'governance_contract_blob': '4983caae325d3a7fc3e7042b3f0428b69d604e3f',
    'governance_contract_bytes': 13558,
    'scientific_parent': '56447829ce0e6c3c85552c53c351b26a2452a4bd',
    'matlab_budget': 0,
    'can_execute': 'false',
    'authority_mode': 'DRY_RUN_ONLY',
}


class RouteRejected(ValueError):
    def __init__(self, fields):
        super().__init__('Explicit route identity rejected')
        self.fields = sorted(fields)


def validate_identity(values):
    """Pure in-memory exact comparison; no file or external action."""
    wrong = [key for key, expected in EXPECTED.items()
             if key not in values or type(values[key]) is not type(expected)
             or values[key] != expected]
    wrong.extend(sorted(set(values) - set(EXPECTED) - {'invocation_mode'}))
    if values.get('invocation_mode') not in ('dry-run', 'verify-route'):
        wrong.append('invocation_mode')
    if wrong:
        raise RouteRejected(wrong)
    return {'selected_target': values['target_task_id'],
            'can_execute': False, 'matlab_budget': 0,
            'authority_mode': 'DRY_RUN_ONLY'}


def parse_explicit_cli():
    parser = argparse.ArgumentParser(prog='TEMP31_EXPLICIT_ROUTE_CANARY',
                                     allow_abbrev=False, add_help=False)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--dry-run', action='store_true')
    mode.add_argument('--verify-route', action='store_true')
    for field in EXPECTED:
        parser.add_argument('--' + field.replace('_', '-'), required=True,
                            type=int if field.endswith('_bytes') or field == 'matlab_budget' else str)
    values = vars(parser.parse_args())
    dry_run = values.pop('dry_run')
    values.pop('verify_route')
    values['invocation_mode'] = 'dry-run' if dry_run else 'verify-route'
    return values


def identity(raw):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(raw)).encode()
                                    + b'\0' + raw).hexdigest()}


def main():
    start_ns = time.monotonic_ns()
    start_utc = datetime.now(timezone.utc).isoformat()
    values = parse_explicit_cli()
    positive = validate_identity(values)
    source_path = Path(__file__).resolve()
    local_root = source_path.parents[2] / 'tasks' / TASK / 'LOCAL_ONLY'
    for component in [local_root, *local_root.parents]:
        if component.is_symlink() or getattr(component.lstat(), 'st_file_attributes', 0) & 0x400:
            raise ValueError('Unsafe receipt ancestry')
    allowed = {
        local_root / 'contract_call_raw.json': 'GOVERNANCE_CONTRACT_CONNECTOR_RECEIPT',
        local_root / 'target_call_raw.json': 'TARGET_CONTRACT_CONNECTOR_RECEIPT',
    }
    for path in allowed:
        if path.is_symlink() or getattr(path.lstat(), 'st_file_attributes', 0) & 0x400:
            raise ValueError('Unsafe receipt entry')
        if path.resolve().parent != local_root.resolve():
            raise ValueError('Unsafe receipt containment')
    opened = []
    denied = []

    def audit(event, args):
        if event == 'open':
            path, mode, flags = args
            if not isinstance(path, (str, bytes)):
                denied.append({'event': event, 'reason': 'UNEXPECTED_DESCRIPTOR'})
                raise PermissionError('Unapproved file access')
            candidate = Path(path)
            if candidate not in allowed or mode not in ('r', 'rb'):
                denied.append({'event': event, 'reason': 'OUTSIDE_FIXED_READONLY_RECEIPTS'})
                raise PermissionError('Unapproved file access')
            opened.append({'role': allowed[candidate], 'mode': 'READ_ONLY',
                           'event_index': len(opened), 'monotonic_ns': time.monotonic_ns()})
        elif (event.startswith(('subprocess.', 'socket.', 'ctypes.'))
              or event in ('os.system', 'os.exec', 'os.posix_spawn', 'os.spawn', 'os.fork')):
            denied.append({'event': event, 'reason': 'NO_EXTERNAL_ACTION_AUTHORITY'})
            raise PermissionError('External action rejected')

    sys.addaudithook(audit)
    source_results = []
    for prefix, name, ref in (
            ('governance', 'contract_call_raw.json', GOVERNANCE),
            ('target', 'target_call_raw.json', EXPECTED['target_contract_commit'])):
        receipt = json.loads((local_root / name).read_bytes().decode('utf-8', errors='strict'))
        expected_request = {
            'repository_full_name': 'zcx369658780/dissertation-ch5-two-asset-hank',
            'ref': ref, 'path': EXPECTED[prefix + '_contract_path'], 'encoding': 'utf-8'}
        if receipt['args'] != expected_request or receipt['result'].get('isError') is not False:
            raise ValueError('Fixed connector source request mismatch')
        body = receipt['result']['structuredContent']
        if body['encoding'] != 'utf-8':
            raise ValueError('Unexpected source encoding')
        raw = body['content'].encode('utf-8', errors='strict')
        actual = identity(raw)
        if (actual['bytes'] != EXPECTED[prefix + '_contract_bytes']
                or actual['git_blob'] != EXPECTED[prefix + '_contract_blob']
                or actual['git_blob'] != body['sha']):
            raise ValueError('Fixed source byte identity mismatch')
        source_results.append({'role': prefix, 'fixed_ref': ref,
                               'request_matched': True, **actual})
    negatives = []
    missing = dict(values)
    missing.pop('target_contract_blob')
    r40 = dict(values, target_task_id=R40_AUTHORITY)
    wrong_source = dict(values, target_contract_commit='0' * 40,
                        target_contract_blob='f' * 40)
    for name, mutated, expected_fields in (
            ('MISSING_REQUIRED_TARGET_IDENTITY', missing, ['target_contract_blob']),
            ('R40_TARGET_SUBSTITUTION', r40, ['target_task_id']),
            ('WRONG_CONTRACT_COMMIT_AND_BLOB', wrong_source,
             ['target_contract_blob', 'target_contract_commit'])):
        reads_before = len(opened)
        try:
            validate_identity(mutated)
        except RouteRejected as rejected:
            if rejected.fields != expected_fields or len(opened) != reads_before:
                raise ValueError('Negative case rejected inconsistently')
            negatives.append({'case': name, 'result': 'REJECTED',
                              'rejected_fields': rejected.fields,
                              'level': 'PURE_IN_MEMORY_VALIDATOR',
                              'file_opens_during_case': 0, 'external_actions': 0})
        else:
            raise ValueError('Negative case incorrectly accepted')
    if len(opened) != 2 or denied:
        raise ValueError('Unexpected canary body access observation')
    report = {
        'task_id': TASK, 'status': 'EXPLICIT_TASK_SCOPED_CANARY_ROUTE_VALIDATED',
        'source_grade': 'DIRECT_EXECUTED_ZERO_RUNTIME_CANARY',
        'invocation_mode': values['invocation_mode'], 'explicit_identity': values,
        'positive': dict(result='ACCEPTED', **positive), 'negative_controls': negatives,
        'sources': source_results, 'body_file_reads': opened, 'body_file_writes': [],
        'body_denied_actions': denied,
        'audit_scope': 'AFTER_STANDARD_LIBRARY_IMPORTS; IN_PROCESS_OBSERVATION_NOT_OS_ENFORCEMENT',
        'global_index_reads_by_canary': 0, 'r40_payload_reads_or_executions': 0,
        'target_runtime_executions': 0, 'matlab_creations': 0,
        'job_experiments': 0, 'prefdir_accesses_or_creations': 0,
        'scientific_or_npz_calls': 0, 'global_launcher_precedence': 'UNTESTED_NOT_REPAIRED',
        'future_matlab_120s_target_runtime': 'NOT_AUTHORIZED_NOT_TESTED',
        'start_utc': start_utc, 'finish_utc': datetime.now(timezone.utc).isoformat(),
        'start_monotonic_ns': start_ns, 'finish_monotonic_ns': time.monotonic_ns(),
    }
    print(json.dumps(report, indent=2))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (RouteRejected, ValueError, OSError, KeyError, TypeError) as error:
        print(json.dumps({'task_id': TASK, 'status': 'REJECTED_OR_FAILED',
                          'error_class': type(error).__name__,
                          'rejected_fields': getattr(error, 'fields', []),
                          'can_execute': False}), file=sys.stderr)
        raise SystemExit(2)
