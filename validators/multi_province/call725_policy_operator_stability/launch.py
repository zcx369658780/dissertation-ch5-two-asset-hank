"""Launch exactly one explicitly requested task invocation with durable logs."""
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
ROOT=Path(r'D:\ProjectTemp\ch5-call725-policy-operator-stability-20260907-001')
BINDING=Path(r'D:\ProjectTemp\ch5-mp4c-2018-call725-first-iteration-scalar-binding-repair-20260904-001\call725_first_iteration_scalar_binding.json')
MATLAB=Path(r'C:\Program Files\MATLAB\R2022b\bin\matlab.exe')
PROTECTED=Path(r'D:\MatlabProgram\2023年12月2日 多省份神经网络HANK')


def quote(value):
    return "'"+str(value).replace("'","''")+"'"


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('language',choices=['matlab','python'])
    parser.add_argument('kind',choices=['M24','P24','P32','M143_FINAL'])
    parser.add_argument('--initialization',type=Path,required=True)
    args=parser.parse_args()
    key=f'{args.language}_{args.kind}'
    receipt_path=ROOT/f'{key}_process.json'
    if receipt_path.exists() or (ROOT/key).exists(): raise RuntimeError('invocation already present; no automatic retry')
    limit=1
    timeout=900
    snapshot=ROOT/f'{key}_sources'; snapshot.mkdir(exist_ok=False)
    names=['python_trajectory.py','matlab_trajectory.m','launch.py']
    hashes={}
    for name in names:
        shutil.copyfile(HERE/name,snapshot/name)
        hashes[name]=hashlib.sha256((snapshot/name).read_bytes()).hexdigest()
    identities=json.loads((ROOT/'frozen_identities.json').read_text(encoding='utf-8'))
    for row in identities:
        if hashlib.sha256(Path(row['path']).read_bytes()).hexdigest().upper()!=row['sha256']:
            raise RuntimeError('frozen identity drift: '+row['path'])
    binding=json.loads(BINDING.read_text(encoding='utf-8'))
    if binding['scalar_binding']['numerics']['convergence_tolerance']!=1e-7:raise RuntimeError('stop threshold drift')
    source=(REPO/'exports/matlab_faithful_two_asset_ha.py').read_bytes()
    normalized=source.replace(b'\r\n',b'\n')
    blob=hashlib.sha1(b'blob '+str(len(normalized)).encode()+b'\0'+normalized).hexdigest()
    if blob!='9e7dc9556a2b76811e78f89999abecc045886106':raise RuntimeError('Python source drift')
    (snapshot/'exports').mkdir();(snapshot/'exports/matlab_faithful_two_asset_ha.py').write_bytes(source)
    for name in ('HANK3_FOC.m','HANK3_cost.m'):shutil.copyfile(PROTECTED/name,snapshot/name)
    # Isolate runtime dependencies to these byte-verified snapshots, not mutable worktrees.
    wrapper=snapshot/'python_trajectory.py'
    wrapper.write_text(wrapper.read_text(encoding='utf-8').replace(f'REPO=Path({str(REPO)!r})','REPO=ROOT'),encoding='utf-8')
    hashes={str(p.relative_to(snapshot)):hashlib.sha256(p.read_bytes()).hexdigest() for p in snapshot.rglob('*') if p.is_file()}
    init_sha=hashlib.sha256(args.initialization.read_bytes()).hexdigest().upper()
    expected_init=json.loads((ROOT/'states.json').read_text(encoding='utf-8'))[args.kind]['sha256']
    if init_sha!=expected_init:raise RuntimeError('initialization drift')
    if args.language=='python':
        command=[sys.executable,'-B',str(snapshot/'python_trajectory.py'),str(ROOT/key),str(BINDING),str(args.initialization),str(limit)]
    else:
        script=f"addpath({quote(snapshot)}); matlab_trajectory({quote(BINDING)},{quote(args.initialization)},{quote(ROOT/key)},{quote(snapshot)},{limit});"
        command=[str(MATLAB),'-batch',script]
    receipt={'language':args.language,'kind':args.kind,'max_updates':limit,'timeout_seconds':timeout,'wrapper_hashes':hashes,'initialization':str(args.initialization),'initialization_sha256':init_sha,'frozen_python_blob':blob,'binding_sha256':hashlib.sha256(BINDING.read_bytes()).hexdigest(),'command':command,'state':'LAUNCHING'}
    def save(): receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    save(); started=time.monotonic()
    with (ROOT/f'{key}.log').open('wb') as log:
        process=subprocess.Popen(command,cwd=REPO,stdout=log,stderr=subprocess.STDOUT)
        receipt['pid']=process.pid;receipt['state']='RUNNING';save()
        print(f'{key}: pid={process.pid}',flush=True)
        try:
            receipt['exit_code']=process.wait(timeout=timeout)
            receipt['state']='SUCCEEDED' if receipt['exit_code']==0 else 'FAILED'
        except subprocess.TimeoutExpired:
            subprocess.run(['taskkill','/PID',str(process.pid),'/T','/F'],capture_output=True,check=False)
            receipt['state']='TIMEOUT';receipt['exit_code']=None
        finally:
            ledger_path=ROOT/key/'ledger.json'
            try: receipt['last_worker_ledger']=json.loads(ledger_path.read_text(encoding='utf-8'))
            except (FileNotFoundError,json.JSONDecodeError): receipt['last_worker_ledger']=None
            receipt['worker_ledger_is_terminal']=bool(receipt['last_worker_ledger'] and receipt['last_worker_ledger']['status'] not in ('RUNNING','INITIALIZING'))
            if receipt['state']=='TIMEOUT':receipt['note']='Worker ledger may be stale after tree termination; counters are last durable attempts, not an inferred successful update count.'
            receipt['elapsed_seconds']=time.monotonic()-started;save()
    print(json.dumps(receipt,ensure_ascii=False),flush=True)


if __name__=='__main__': main()
