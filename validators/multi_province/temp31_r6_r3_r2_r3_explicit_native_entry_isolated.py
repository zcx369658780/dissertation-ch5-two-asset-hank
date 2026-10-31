"""Explicit one-shot task-local native entry; no global index or arbitrary loader."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
import types
from datetime import datetime,timezone
EXPECTED = {'task_id': 'CH5_TEMP31_R6_R3_R2_R3_EXPLICIT_NATIVE_120S_20261031', 'runtime_target_task_id': 'CH5_TEMP31_R6_R3_R2_R3_EXPLICIT_NATIVE_120S_20261031', 'original_target_task_id': 'CH5_TEMP31_R6_R3_R2_120S_ISOLATED_PREFDIR_NATIVE_STARTUP_20261030', 'contract_commit': '582396de2a67826a6ec0f90701aa066d05eb6850', 'contract_path': 'tasks/CH5_TEMP31_R6_R3_R2_R3_EXPLICIT_NATIVE_120S_20261031/CONTRACT.md', 'contract_blob': 'e76d43c3f03b8740d6c3b360c82c177ea492e43a', 'contract_bytes': 17076, 'original_target_commit': '40e7b2e1ee93973ca63b509f53f20e21c6f149ad', 'original_target_path': 'tasks/CH5_TEMP31_R6_R3_R2_120S_ISOLATED_PREFDIR_NATIVE_STARTUP_20261030/CONTRACT.md', 'original_target_blob': '1d7c4c960b9b6d47cc9e8182afd2859372caa168', 'original_target_bytes': 15857, 'governance_commit': '582396de2a67826a6ec0f90701aa066d05eb6850', 'scientific_parent': '56447829ce0e6c3c85552c53c351b26a2452a4bd', 'owner_authorization': '2026-10-31__NEW_EXPLICIT_RUNTIME_ROUTE_WITH_PREEXECUTION_HARD_GATES__ONE_120S_NATIVE_MATLAB_MINIMAL_PROBE', 'controller_sha256': '91543ddf57a22c72d0fb9bdc8b848f1ffe2a70eedbd517a240db9f880554bf16', 'controller_bytes': 26210, 'probe_sha256': 'bfdbf23c64cef41205a018c3ccff135a106494d31c3f3bd7dc6d672d52364d2a', 'probe_bytes': 1757, 'run_token': 'TEMP31_R3_ee813324476a4bcebabe8fd1c223a7ec', 'authority_mode': 'ONE_NATIVE_120S_ONLY', 'matlab_budget': 1, 'native_seconds': 120, 'memory_limit': 1073741824, 'active_processes': 1}
TASK=EXPECTED['task_id']
R40='POST_R5_R6_HJB_TRAJECTORY_R40_TARGET_HJB_NONCONVERGENCE_DECOMPOSITION'
CONTROLLER='temp31_r6_r3_r2_r3_120s_native_controller_isolated.py'
PROBE='temp31_r6_r3_r2_r3_120s_native_probe_isolated.m'
class RouteRejected(ValueError):
    def __init__(self,fields):super().__init__('Explicit identity rejected');self.fields=sorted(fields)
def stamp():return dict(monotonic_ns=time.monotonic_ns(),utc=datetime.now(timezone.utc).isoformat())
def ident(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
def dump(p,obj):
    with p.open('x',encoding='utf-8',newline='\n') as f:json.dump(obj,f,indent=2);f.write('\n')
def safe(p):
    for q in [p,*p.parents]:
        if q.is_symlink() or getattr(q.lstat(),'st_file_attributes',0)&0x400:raise ValueError('Unsafe ancestry')
def validate(v):
    bad=[k for k,x in EXPECTED.items() if k not in v or type(v[k]) is not type(x) or v[k]!=x]
    bad.extend(set(v)-set(EXPECTED))
    if bad:raise RouteRejected(bad)
    return True
def source(local,name,ref,path,blob,count):
    p=local/name;safe(p);r=json.loads(p.read_bytes().decode('utf-8'))
    assert r['args']==dict(repository_full_name='zcx369658780/dissertation-ch5-two-asset-hank',ref=ref,path=path,encoding='utf-8')
    assert r['result'].get('isError') is False
    d=r['result']['structuredContent'];assert d['encoding']=='utf-8'
    i=ident(d['content'].encode('utf-8'));assert i['git_blob']==d['sha']==blob
    if count is not None:assert i['bytes']==count
    return dict(ref=ref,path=path,**i)
def metadata(local,name):
    p=local/name;safe(p);r=json.loads(p.read_bytes())['result'];assert not r.get('isError');return json.loads(r['structuredContent']['content'])
def main():
    start=stamp();work=Path(__file__).resolve().parents[2];local=work/'tasks'/TASK/'LOCAL_ONLY'
    parser=argparse.ArgumentParser(prog='TEMP31_EXPLICIT_NATIVE_ENTRY',allow_abbrev=False,add_help=False)
    parser.add_argument('--run-authorized-native',action='store_true',required=True)
    for k,x in EXPECTED.items():parser.add_argument('--'+k.replace('_','-'),required=True,type=type(x))
    args=vars(parser.parse_args());assert args.pop('run_authorized_native') is True
    validate(args);safe(local)
    dump(local/'entry_invocation_claim.json',dict(invocation_index=1,maximum=1,retries=0,run_token=args['run_token'],start=start))
    cases=[];called=False;error=None;returncode=2;source_records=[]
    try:
        missing=dict(args);missing.pop('contract_blob')
        r40=dict(args,runtime_target_task_id=R40)
        wrong=dict(args,contract_commit='0'*40,contract_blob='f'*40)
        for name,value,fields in [('MISSING_IDENTITY',missing,['contract_blob']),('R40_TARGET',r40,['runtime_target_task_id']),('WRONG_COMMIT_AND_BLOB',wrong,['contract_blob','contract_commit'])]:
            try:validate(value)
            except RouteRejected as e:
                assert e.fields==fields;cases.append(dict(case=name,result='REJECTED',fields=e.fields,pure_memory=True))
            else:raise ValueError('Negative case accepted')
        dump(local/'route_negative_controls_raw.json',dict(cases=cases,count=3,in_same_entry_process=True))
        source_records.append(source(local,'contract_call_raw.json',args['contract_commit'],args['contract_path'],args['contract_blob'],args['contract_bytes']))
        source_records.append(source(local,'target_call_raw.json',args['original_target_commit'],args['original_target_path'],args['original_target_blob'],args['original_target_bytes']))
        source_records.append(source(local,'prior_review_call_raw.json','e54d89d37b93d619d28378ff838e09be04e4e8b8','docs/CH5_TEMP31_R6_R3_R2_R2_EXPLICIT_RUNTIME_ROUTER_CANARY_20261031_INDEPENDENT_ABC_FINAL_REVIEW.md','61ed12ed5997ee105e2a5bd9c6212836258a5db7',10706))
        gov=metadata(local,'governance_commit_raw.json');head=metadata(local,'pre_execution_governance_head_raw.json');diff=metadata(local,'governance_diff_raw.json');base=metadata(local,'scientific_base_raw.json')
        assert gov['sha']==head['object']['sha']==args['governance_commit']
        assert [p['sha'] for p in gov['parents']]==['e54d89d37b93d619d28378ff838e09be04e4e8b8']
        assert gov['tree']['sha']=='969f0f30df64046898ef70de30f75a8741313c01'
        assert diff['total_commits']==diff['ahead_by']==1 and diff['behind_by']==0
        assert [(p['filename'],p['status'],p['sha']) for p in diff['files']]==[(args['contract_path'],'added',args['contract_blob'])]
        assert base['sha']==args['scientific_parent'] and base['tree']['sha']=='7b7cb29dd5b37be92561e7f1bc688c0d29789732'
        absent=json.loads((local/'pre_execution_candidate_ref_raw.json').read_bytes())['result']
        assert absent['isError'] is True and absent['structuredContent']['error_code']=='NOT_FOUND' and absent['structuredContent']['error_data']['status']=='404'
        assert not (local/'R3_NATIVE_RUNTIME').exists(),'Runtime root already exists'
        controller=Path(__file__).resolve().parent/CONTROLLER;probe=controller.parent/PROBE
        safe(controller);safe(probe);raw=controller.read_bytes();pr=probe.read_bytes()
        assert ident(raw)['sha256']==args['controller_sha256'] and len(raw)==args['controller_bytes']
        assert ident(pr)['sha256']==args['probe_sha256'] and len(pr)==args['probe_bytes']
        config=json.loads((local/'executable_configuration_raw.json').read_bytes());exe=Path(config['matlab_executable']);safe(exe)
        assert ident(exe.read_bytes())==config['executable_identity'];assert config['executable_identity']['sha256']=='4d251e680b8409d76d0524a1eb716de3c9e747386d3101e10f6ce1405ad1a59d'
        plan=dict(args,authority_pass=True,source_route_gate_pass=True,controller_identity=ident(raw),probe_identity=ident(pr),matlab_executable=str(exe),executable_identity=config['executable_identity'])
        dump(local/'explicit_route_pre_execution_gate_raw.json',dict(status='PASS_BEFORE_CONTROLLER_CALL',at=stamp(),identities=args,source_records=source_records,controller_identity=ident(raw),probe_identity=ident(pr),negative_controls_passed=3,global_launcher_used=False,arbitrary_controller_path_accepted=False,same_python_process_call=True))
        module=types.ModuleType('_temp31_r3_fixed_native_controller');module.__file__=str(controller)
        exec(compile(raw,str(controller),'exec'),module.__dict__)
        assert module.run_once.__module__==module.__name__ and module.run_once.__code__.co_filename==str(controller)
        called=True;returncode=module.run_once(types.MappingProxyType(plan))
        assert returncode in (0,1)
    except BaseException as e:
        error=dict(type=type(e).__name__,private_message=str(e));returncode=2
    finally:
        dump(local/'explicit_entry_execution_receipt_raw.json',dict(task_id=TASK,start=start,finish=stamp(),controller_function_invocations=int(called),controller_called_same_python_process=called,negative_cases=cases,source_records=source_records,entry_error=error,exit_code=returncode,retries=0,global_launcher_used=False,legacy_canary_called=False))
    return returncode
if __name__=='__main__':raise SystemExit(main())
