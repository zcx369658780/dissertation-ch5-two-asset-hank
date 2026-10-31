"""One explicit two-GiB native route; no default task or arbitrary controller."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
import types
from datetime import datetime,timezone
EXPECTED={'task_id': 'CH5_TEMP31_R6_R3_R2_R6_TWO_GIB_NATIVE_STARTUP_20261031', 'runtime_target_task_id': 'CH5_TEMP31_R6_R3_R2_R6_TWO_GIB_NATIVE_STARTUP_20261031', 'contract_commit': 'ae85e7d9846642e9cbad2742651ae75994d235de', 'contract_path': 'tasks/CH5_TEMP31_R6_R3_R2_R6_TWO_GIB_NATIVE_STARTUP_20261031/CONTRACT.md', 'contract_blob': 'fe9d217ae0e2089e3b50ce9f86bfabf735c60c8d', 'contract_bytes': 19427, 'governance_commit': 'ae85e7d9846642e9cbad2742651ae75994d235de', 'scientific_parent': '56447829ce0e6c3c85552c53c351b26a2452a4bd', 'owner_authorization': '2026-10-31__ONE_NEW_TWO_GIB_PROCESS_AND_JOB_MEMORY_CAP_COMPARATIVE_MATLAB_NATIVE_STARTUP__120_SECONDS__NO_MAIN2', 'controller_sha256': 'c38b2606d48ecd8f5a9466c00a93e2b8291bdb15ccfc656155fde728076c624e', 'controller_bytes': 28530, 'probe_sha256': '886b5e6414a0a219360aff7e134189dc9609b47bdd98e9603fa49be65fe724da', 'probe_bytes': 1767, 'run_token': 'TEMP31_R6_2be4a378243547f0a6f4769ca992346a', 'run_mode': 'ONE_NATIVE_MINIMAL_PROBE', 'matlab_budget': 1, 'native_seconds': 120, 'memory_limit': 2147483648, 'active_processes': 1, 'reference_native_seal': '29ec5f7466da1ec951f491650fc27ca3f59ce02b', 'reference_r5_review_commit': 'e235b18a851bd6bce93ef9ead49a28dc4692473e'}
FROZEN_SOURCES=[('contract_raw.json', 'ae85e7d9846642e9cbad2742651ae75994d235de', 'tasks/CH5_TEMP31_R6_R3_R2_R6_TWO_GIB_NATIVE_STARTUP_20261031/CONTRACT.md', 'fe9d217ae0e2089e3b50ce9f86bfabf735c60c8d', 19427), ('r3_entry_raw.json', '29ec5f7466da1ec951f491650fc27ca3f59ce02b', 'validators/multi_province/temp31_r6_r3_r2_r3_explicit_native_entry_isolated.py', 'a03ab8aa07944bd795a52674884161ddb416cf57', 8870), ('r3_controller_raw.json', '29ec5f7466da1ec951f491650fc27ca3f59ce02b', 'validators/multi_province/temp31_r6_r3_r2_r3_120s_native_controller_isolated.py', 'dd4d0f915ea0ac3c90ee9d38dadcf304485dc2a2', 26210), ('r3_probe_raw.json', '29ec5f7466da1ec951f491650fc27ca3f59ce02b', 'validators/multi_province/temp31_r6_r3_r2_r3_120s_native_probe_isolated.m', '87d26a52386637244724f9db4cb707d8732e0970', 1757), ('r3_job_raw.json', '29ec5f7466da1ec951f491650fc27ca3f59ce02b', 'tasks/CH5_TEMP31_R6_R3_R2_R3_EXPLICIT_NATIVE_120S_20261031/native_job_event_and_resource_receipt.json', 'dee4642b194845a020e3fb6a2b685b41e0ac3fe7', 3019), ('r3_runtime_raw.json', '29ec5f7466da1ec951f491650fc27ca3f59ce02b', 'tasks/CH5_TEMP31_R6_R3_R2_R3_EXPLICIT_NATIVE_120S_20261031/native_probe_and_runtime_prefdir_receipt.json', 'acfeb2050e0b5e89a5e99740c73209869f49a66c', 1002), ('r3_cleanup_raw.json', '29ec5f7466da1ec951f491650fc27ca3f59ce02b', 'tasks/CH5_TEMP31_R6_R3_R2_R3_EXPLICIT_NATIVE_120S_20261031/owned_process_cleanup_receipt.json', 'ba095414f2ddc6a47d7cd1f568e390dbc1cb86e4', 2273), ('r3_logs_raw.json', '29ec5f7466da1ec951f491650fc27ca3f59ce02b', 'tasks/CH5_TEMP31_R6_R3_R2_R3_EXPLICIT_NATIVE_120S_20261031/stdout_stderr_logfile_summary.md', '8d24e5215dd82baedc967435c80579efbb63c683', 932), ('r3_review_raw.json', 'b3762e6696d7e3b27325a2df1166b56507743da3', 'docs/CH5_TEMP31_R6_R3_R2_R3_EXPLICIT_NATIVE_120S_MEMORY_LIMIT_STACK_OVERFLOW_20261031_INDEPENDENT_ABC_FINAL_REVIEW.md', 'a427021db7371a3314fee0d9eeecc5a832ff238f', 14629), ('r5_review_raw.json', 'e235b18a851bd6bce93ef9ead49a28dc4692473e', 'docs/CH5_TEMP31_R6_R3_R2_R5_LOCAL_MINIDUMP_EXCEPTION_20261031_INDEPENDENT_ABC_FINAL_REVIEW.md', 'b38cbe4dc5a8ae062b0fdd65b153f94e1be00b4d', 8998)]
TASK=EXPECTED['task_id']
CONTROLLER='temp31_r6_r3_r2_r6_two_gib_native_controller_isolated.py'
PROBE='temp31_r6_r3_r2_r6_two_gib_minimal_probe_isolated.m'
R40='POST_R5_R6_HJB_TRAJECTORY_R40_TARGET_HJB_NONCONVERGENCE_DECOMPOSITION'
class RouteRejected(ValueError):
    def __init__(self,fields):super().__init__('Explicit identity rejected');self.fields=sorted(fields)
def stamp():return dict(monotonic_ns=time.monotonic_ns(),utc=datetime.now(timezone.utc).isoformat())
def ident(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
def dump(p,obj):
    with p.open('x',encoding='utf-8',newline='\n') as f:json.dump(obj,f,indent=2);f.write('\n')
def safe(p):
    for q in reversed([p,*p.parents]):
        if q.is_symlink() or getattr(q.lstat(),'st_file_attributes',0)&0x400:raise ValueError('Unsafe ancestry')
def validate(v):
    bad=[k for k,x in EXPECTED.items() if k not in v or type(v[k]) is not type(x) or v[k]!=x];bad.extend(set(v)-set(EXPECTED))
    if bad:raise RouteRejected(bad)
    return True
def source(local,name,ref,path,blob,count):
    p=local/name;safe(p);r=json.loads(p.read_bytes())
    assert r['args']==dict(repository_full_name='zcx369658780/dissertation-ch5-two-asset-hank',ref=ref,path=path,encoding='utf-8')
    assert r['result'].get('isError') is False
    d=r['result']['structuredContent'];assert d['encoding']=='utf-8';i=ident(d['content'].encode('utf-8'))
    assert i['git_blob']==d['sha']==blob and i['bytes']==count
    return dict(ref=ref,path=path,**i)
def metadata(local,name):
    p=local/name;safe(p);r=json.loads(p.read_bytes())['result'];assert not r.get('isError');return json.loads(r['structuredContent']['content'])
def main():
    start=stamp();work=Path(__file__).resolve().parents[2];local=work/'tasks'/TASK/'LOCAL_ONLY'
    parser=argparse.ArgumentParser(prog='TEMP31_TWO_GIB_EXPLICIT_NATIVE_ENTRY',allow_abbrev=False,add_help=False)
    parser.add_argument('--run-authorized-native',action='store_true',required=True)
    for k,x in EXPECTED.items():parser.add_argument('--'+k.replace('_','-'),required=True,type=type(x))
    args=vars(parser.parse_args());assert args.pop('run_authorized_native') is True;validate(args);safe(local)
    dump(local/'entry_invocation_claim.json',dict(invocation_index=1,maximum=1,retries=0,run_token=args['run_token'],start=start))
    cases=[];called=False;error=None;returncode=2;source_records=[]
    try:
        missing=dict(args);missing.pop('contract_blob');r40=dict(args,runtime_target_task_id=R40);wrong=dict(args,contract_commit='0'*40,contract_blob='f'*40)
        for name,value,fields in [('MISSING_IDENTITY',missing,['contract_blob']),('R40_TARGET',r40,['runtime_target_task_id']),('WRONG_COMMIT_AND_BLOB',wrong,['contract_blob','contract_commit'])]:
            try:validate(value)
            except RouteRejected as e:assert e.fields==fields;cases.append(dict(case=name,result='REJECTED',fields=e.fields,pure_memory=True))
            else:raise ValueError('Negative case accepted')
        dump(local/'route_negative_controls_raw.json',dict(cases=cases,count=3,in_same_entry_process=True))
        for record in FROZEN_SOURCES:source_records.append(source(local,*record))
        gov=metadata(local,'governance_commit_raw.json');head=metadata(local,'pre_execution_governance_head_raw.json');diff=metadata(local,'governance_diff_raw.json');base=metadata(local,'scientific_base_raw.json')
        assert gov['sha']==head['object']['sha']==args['governance_commit']
        assert [p['sha'] for p in gov['parents']]==['e235b18a851bd6bce93ef9ead49a28dc4692473e']
        assert gov['tree']['sha']=='4d444fdc4d58acb78295789e703e84c2793164fd'
        assert diff['total_commits']==diff['ahead_by']==1 and diff['behind_by']==0
        assert [(p['filename'],p['status'],p['sha']) for p in diff['files']]==[(args['contract_path'],'added',args['contract_blob'])]
        assert base['sha']==args['scientific_parent'] and base['tree']['sha']=='7b7cb29dd5b37be92561e7f1bc688c0d29789732'
        absent=json.loads((local/'pre_execution_candidate_ref_raw.json').read_bytes())['result']
        assert absent['isError'] is True and absent['structuredContent']['error_code']=='NOT_FOUND' and absent['structuredContent']['error_data']['status']=='404'
        assert not (local/'NEW_TASK_R6_R3_R2_R6').exists(),'New runtime root exists'
        controller=Path(__file__).resolve().parent/CONTROLLER;probe=controller.parent/PROBE;safe(controller);safe(probe)
        raw=controller.read_bytes();pr=probe.read_bytes()
        assert ident(raw)['sha256']==args['controller_sha256'] and len(raw)==args['controller_bytes']
        assert ident(pr)['sha256']==args['probe_sha256'] and len(pr)==args['probe_bytes']
        config=json.loads((local/'executable_configuration_raw.json').read_bytes());exe=Path(config['matlab_executable']);safe(exe)
        assert ident(exe.read_bytes())==config['executable_identity'];assert config['executable_identity']['sha256']=='4d251e680b8409d76d0524a1eb716de3c9e747386d3101e10f6ce1405ad1a59d'
        plan=dict(args,authority_pass=True,source_route_gate_pass=True,controller_identity=ident(raw),probe_identity=ident(pr),matlab_executable=str(exe),executable_identity=config['executable_identity'])
        dump(local/'explicit_route_pre_execution_gate_raw.json',dict(status='SOURCE_IDENTITY_PASS_HOST_GATE_NOT_YET_CALLED',at=stamp(),identities=args,source_records=source_records,controller_identity=ident(raw),probe_identity=ident(pr),negative_controls_passed=3,global_launcher_used=False,arbitrary_controller_path_accepted=False,same_python_process_call=True))
        module=types.ModuleType('_temp31_r6_two_gib_fixed_native_controller');module.__file__=str(controller)
        exec(compile(raw,str(controller),'exec'),module.__dict__)
        assert module.run_once.__module__==module.__name__ and module.run_once.__code__.co_filename==str(controller)
        called=True;returncode=module.run_once(types.MappingProxyType(plan));assert returncode in (0,1)
    except BaseException as e:error=dict(type=type(e).__name__,private_message=str(e));returncode=2
    finally:dump(local/'explicit_entry_execution_receipt_raw.json',dict(task_id=TASK,start=start,finish=stamp(),controller_function_invocations=int(called),controller_called_same_python_process=called,negative_cases=cases,source_records=source_records,entry_error=error,exit_code=returncode,retries=0,global_launcher_used=False,old_controller_or_canary_called=False))
    return returncode
if __name__=='__main__':raise SystemExit(main())
