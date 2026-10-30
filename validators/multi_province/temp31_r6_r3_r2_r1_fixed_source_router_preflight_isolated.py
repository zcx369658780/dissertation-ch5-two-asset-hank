"""Read-only, task-scoped contract and non-executing handoff verification.

No network, process, model, preference-directory, or global-launcher execution.
Only the exact task-local receipt names below are read. The original index
snapshot was captured by the authorized main agent; its target is never opened.
"""
from pathlib import Path
import hashlib
import json
import re

TASK = 'CH5_TEMP31_R6_R3_R2_R1_FIXED_CONTRACT_READ_AND_ROUTER_RECOVERY_20261031'
TARGET = 'CH5_TEMP31_R6_R3_R2_120S_ISOLATED_PREFDIR_NATIVE_STARTUP_20261030'
GOV = '444c4157df866b8c4a993dfe67e321f95324f2cd'
TARGET_REF = '40e7b2e1ee93973ca63b509f53f20e21c6f149ad'
BASE = '56447829ce0e6c3c85552c53c351b26a2452a4bd'
CONTRACT_PATH = 'tasks/' + TASK + '/CONTRACT.md'
TARGET_PATH = 'tasks/' + TARGET + '/CONTRACT.md'
RECOVERY_BLOB = '6e8bc13e7955c9e3c27c6ac20669cb9b8fb68707'
TARGET_BLOB = '1d7c4c960b9b6d47cc9e8182afd2859372caa168'
ALLOWED = frozenset({
    'recovery_contract_connector.json', 'target_contract_connector.json',
    'governance_commit_connector.json', 'target_commit_connector.json',
    'governance_head_connector.json', 'governance_diff_connector.json',
    'candidate_ref_connector.json', 'target_candidate_ref_connector.json',
    'source_read_attempts.jsonl', 'prior_launcher_index_snapshot.bin',
    'task_scoped_handoff_pointer.json',
})


def identity(raw):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(raw)).encode()
                                    + b'\0' + raw).hexdigest()}


def read_exact(local_root, name):
    if name not in ALLOWED:
        raise ValueError('Receipt name outside fixed allowlist')
    path = local_root / name
    for component in (local_root, path):
        if component.is_symlink() or getattr(component.lstat(), 'st_file_attributes', 0) & 0x400:
            raise ValueError('Reparse receipt rejected')
    if path.resolve().parent != local_root:
        raise ValueError('Receipt containment failure')
    return path.read_bytes()


def document(local_root, name):
    return json.loads(read_exact(local_root, name).decode('utf-8', errors='strict'))


def metadata(local_root, name):
    result = document(local_root, name)
    if result.get('isError'):
        raise ValueError('Required metadata call failed')
    return json.loads(result['structuredContent']['content'])


def verify(local_root):
    source_records = []
    texts = {}
    for role, blob, count in [('recovery', RECOVERY_BLOB, 13734), ('target', TARGET_BLOB, 15857)]:
        reply = document(local_root, role + '_contract_connector.json')
        assert reply.get('isError') is False
        data = reply['structuredContent']
        assert data['encoding'] == 'utf-8'
        text = data['content']
        raw = text.encode('utf-8', errors='strict')
        actual = identity(raw)
        assert actual['git_blob'] == data['sha'] == blob
        assert actual['bytes'] == count
        texts[role] = text
        source_records.append(dict(role=role, status='READ_PASS', **actual))
    assert 'TASK_ID=' + TASK + '\n' in texts['recovery']
    assert 'MAX_NEW_MATLAB_PROCESS_CREATIONS=0\n' in texts['recovery']
    for literal in ('TASK_ID=' + TARGET + '\n',
                    'OWNER_APPROVAL=2026-10-30__ONE_NATIVE_MATLAB_LAUNCH_120_SECONDS_AFTER_RESUME_KEEP_STRATEGY_B_AND_JOB_LIMITS\n',
                    'MAX_NATIVE_WINDOW_AFTER_RESUME_SECONDS=120\n',
                    'CHECKPOINT_SECONDS_AFTER_RESUME=30,60,90,120\n',
                    'MAX_NEW_MATLAB_PROCESS_CREATIONS=1\n',
                    'MAX_RUNTIME_RETRIES=0\n',
                    'MAX_OLD_PREFDIR_READS_COPIES_MOVES_WRITES=0\n',
                    '1073741824', 'CREATE_SUSPENDED', 'MATLAB_PREFDIR',
                    '1GiB', 'kill-on-job-close'):
        assert literal in texts['target'], literal
    attempts = [json.loads(line) for line in read_exact(local_root, 'source_read_attempts.jsonl').decode('utf-8').splitlines()]
    assert len(attempts) == 2
    for record, role, ref, path in zip(attempts, ['recovery_contract', 'target_contract'],
                                      [GOV, TARGET_REF], [CONTRACT_PATH, TARGET_PATH]):
        assert record['role'] == role and record['attempt_index'] == 1
        assert record['method'] == 'mcp__codex_apps__github_fetch_file'
        assert record['request'] == {'repository_full_name': 'zcx369658780/dissertation-ch5-two-asset-hank',
                                     'ref': ref, 'path': path, 'encoding': 'utf-8'}
        assert record['retry_classification'] == 'SUCCESS_NO_RETRY'
    governance = metadata(local_root, 'governance_commit_connector.json')
    target = metadata(local_root, 'target_commit_connector.json')
    head = metadata(local_root, 'governance_head_connector.json')
    diff = metadata(local_root, 'governance_diff_connector.json')
    assert governance['sha'] == GOV and [p['sha'] for p in governance['parents']] == [TARGET_REF]
    assert governance['tree']['sha'] == '07921911cc6aaf90f8351849486ff14ce848925a'
    assert head['object']['sha'] == GOV
    assert target['sha'] == TARGET_REF
    assert [p['sha'] for p in target['parents']] == ['3957f405143af3d08aba70800f25b099d81d4d48']
    assert target['tree']['sha'] == '9f10a1c03e56c142eb1a3f88a2a8ee0494cff343'
    assert diff['ahead_by'] == diff['total_commits'] == 1 and diff['behind_by'] == 0
    assert [(f['filename'], f['status'], f['sha']) for f in diff['files']] == [(CONTRACT_PATH, 'added', RECOVERY_BLOB)]
    for name in ('candidate_ref_connector.json', 'target_candidate_ref_connector.json'):
        missing = document(local_root, name)
        assert missing['isError'] is True
        assert missing['structuredContent']['error_code'] == 'NOT_FOUND'
        assert missing['structuredContent']['error_data']['status'] == '404'
    index_raw = read_exact(local_root, 'prior_launcher_index_snapshot.bin')
    index_text = index_raw.decode('utf-8', errors='strict')
    matches = re.findall(r'^Current task authority: `([^`]+)`\s*$', index_text, flags=re.MULTILINE)
    assert matches == ['POST_R5_R6_HJB_TRAJECTORY_R40_TARGET_HJB_NONCONVERGENCE_DECOMPOSITION']
    pointer = document(local_root, 'task_scoped_handoff_pointer.json')
    expected = {
        'schema': 'TEMP31_STATIC_NONEXECUTING_HANDOFF_V1',
        'active_diagnostic_task': TASK,
        'active_contract': {'commit': GOV, 'path': CONTRACT_PATH, 'blob': RECOVERY_BLOB},
        'inactive_future_target': {'task_id': TARGET, 'contract_commit': TARGET_REF,
                                   'contract_path': TARGET_PATH, 'contract_blob': TARGET_BLOB},
        'route_scope': 'CURRENT_NONEXECUTING_IDENTITY_ISOLATION_ONLY',
        'global_index_role': 'GLOBAL_OR_PRIOR_LAUNCH_INDEX',
        'global_index_modified': False,
        'r40_payload_read': False, 'r40_execution': False,
        'auto_execute_target': False, 'matlab_budget': 0,
        'future_experiment_authorization': 'REQUIRES_NEW_OWNER_AUTHORIZATION_AND_APPROVED_ROUTE',
        'executable_commands': [],
    }
    assert pointer == expected
    return {
        'task_id': TASK, 'fixed_scientific_parent': BASE,
        'source_status': 'READ_PASS', 'sources': source_records,
        'fixed_source_initial_attempts': 2, 'source_retries': 0,
        'governance_status': 'PASS', 'candidate_refs_initially_absent': True,
        'prior_index': {'role': 'GLOBAL_OR_PRIOR_LAUNCH_INDEX',
                        'task_authority': matches[0], 'level': 'DIRECT_BYTE_OBSERVATION',
                        **identity(index_raw)},
        'router_status': 'READ_PASS_CURRENT_NONEXECUTING_IDENTITY_ISOLATION_ONLY',
        'global_router_repaired': False,
        'future_120s_execution_route': 'NOT_AUTHORIZED_NOT_CERTIFIED',
        'handoff_pointer_identity': identity(read_exact(local_root, 'task_scoped_handoff_pointer.json')),
        'r40_payload_accesses': 0, 'r40_executions': 0,
        'matlab_process_creations': 0, 'job_experiments': 0,
        'runtime_science_calls': 0, 'old_preference_accesses': 0,
        'numeric_review': 'NOT_TESTED_BY_DESIGN',
    }


if __name__ == '__main__':
    work = Path(__file__).resolve().parents[2]
    local = work / 'tasks' / TASK / 'LOCAL_ONLY'
    for component in [local, *local.parents]:
        assert not component.is_symlink()
        assert not getattr(component.lstat(), 'st_file_attributes', 0) & 0x400
    print(json.dumps(verify(local.resolve()), indent=2))
