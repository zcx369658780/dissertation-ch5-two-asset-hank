"""Preflight, synthetic log capture and single child launch; no scientific imports."""
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

REPO=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
INPUT=Path(r'D:\ProjectTemp\ch5-mp4c-owner-a-corrected-2009-2022-8worker-20260902-001\year_2018\calendar_2018_matlab_runtime_cache_input.json')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def git(*args):return subprocess.run(['git',*args],cwd=REPO,check=True,stdout=subprocess.PIPE).stdout


def prepare():
    base=Path(r'D:\ProjectTemp\ch5-2018-observable-prefix-replay-20260908-001');root=base;n=1
    while root.exists():n+=1;root=base.with_name(base.name[:-3]+f'{n:03d}')
    root.mkdir()
    assert sha(INPUT)=='F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0'
    source_map=read(REPO/'reports/province_price_boundary_audit_20260908/source_map.json')
    checks=list(source_map['capture_runtime_blob_checks'])
    checks.extend([{'path':'validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py','blob':'0033baee136c0328e80ffb8b794a88d4405c976c'},
                   {'path':'exports/matlab_faithful_two_asset_ha.py','blob':'9e7dc9556a2b76811e78f89999abecc045886106'}])
    for c in checks:assert git('rev-parse','HEAD:'+c['path']).decode().strip()==c['blob'],c
    for rel in ('src/ch5_two_asset_hank/multi_province/firm.py','src/ch5_two_asset_hank/multi_province/capital_allocation.py',
                'validators/multi_province/mp4b_python_empirical.py','src/ch5_two_asset_hank/multi_province/wage.py',
                'src/ch5_two_asset_hank/multi_province/migration_labor.py'):
        assert not git('diff','8ef4a2a','HEAD','--',rel).strip(),rel
        checks.append({'path':rel,'blob':git('rev-parse','HEAD:'+rel).decode().strip(),'unchanged_since_accepted_audit':True})
    protected=Path('D:/MatlabProgram/2023年12月2日 多省份神经网络HANK/HANK_2ASSETS_HJB.m')
    assert sha(protected)=='049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE'
    disk=shutil.disk_usage(root);assert disk.free>4*1024**3
    for c in checks:
        c['raw_sha256']=sha(REPO/c['path']);c['LF_sha256']=hashlib.sha256((REPO/c['path']).read_bytes().replace(b'\r\n',b'\n')).hexdigest().upper()
    write(root/'preflight.json',{'passed':True,'base_main':git('rev-parse','origin/main').decode().strip(),
        'input':{'path':str(INPUT),'sha256':sha(INPUT)},'sources':checks,
        'protected_HJB_sha256':sha(protected),'target_disk_free_bytes':disk.free,
        'expected_arrays_under_2GiB':True,'scientific_entry':0,
        'ceiling_note':'Unchanged source default is 500; original annual worker supplies MAX_OUTER_TURNS=250. Neither changed; external stop is <=24 entries/23 turns/call725.'})
    print(root)


def tests(root):
    cmd=[sys.executable,'-B',str(REPO/'tests/test_mp4c_observable_prefix_replay.py')]
    env=dict(os.environ);env['PYTHONIOENCODING']='utf-8'
    temp=root/'synthetic_tmp';temp.mkdir(exist_ok=True);env['OBS_TEST_ROOT']=str(temp)
    result=subprocess.run(cmd,cwd=REPO,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    raw=result.stdout;txt=raw.decode('utf-8').replace('\r\n','\n');number=len(list(root.glob('tests_*.raw.json')))+1
    p=root/f'tests_{number:02d}'
    write(p.with_suffix('.raw.json'),{'command':cmd,'returncode':result.returncode,'sha256':hashlib.sha256(raw).hexdigest().upper(),'base64':base64.b64encode(raw).decode()})
    p.with_suffix('.txt').write_text(txt,encoding='utf-8',newline='\n')
    m=re.search(r'Ran (\d+) tests',txt)
    r={'passed':result.returncode==0 and '\nOK\n' in txt,'ran':int(m[1]) if m else None,
       'individual_ok':len(re.findall(r' \.\.\. ok$',txt,re.M)),'lf_sha256':sha(p.with_suffix('.txt'))}
    write(p.with_suffix('.receipt.json'),r);print(txt);print(r)
    if not r['passed'] or r['ran']!=r['individual_ok']:raise SystemExit(1)


def launch(root, retry=False):
    pre=read(root/'preflight.json');assert pre['passed'] and sha(INPUT)==pre['input']['sha256']
    tests=sorted(root.glob('tests_*.receipt.json'));assert tests and read(tests[-1])['passed']
    for src in pre['sources']:assert sha(REPO/src['path'])==src['raw_sha256'],src['path']
    suffix='_retry1' if retry else ''
    runtime=root/'source_runtime'
    if retry:
        assert read(root/'process_receipt.json')['returncode']==1
        assert not (root/'capture').exists() and not (root/'worker_outputs').exists()
        error=(root/'stderr.txt').read_text()
        assert 'standalone household oracle identity mismatch' in error
        assert 'BOOTSTRAP_IDENTITY = _bootstrap_repository_imports()' in error
        identities=[]
        for src in pre['sources']:
            assert sha(runtime/src['path'])==src['LF_sha256'],src['path']
            identities.append({'path':src['path'],'raw_sha256':sha(runtime/src['path']),'matches_bound_LF':True})
        assert sha(runtime/'exports/matlab_faithful_two_asset_ha.py')=='B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3'
        write(root/'zero_entry_failure_receipt.json',{'scientific_entries':0,'reason':'Import bootstrap rejected CRLF raw bytes before Store or worker entry','prior_pid':read(root/'launch_receipt.json')['pid'],'runtime':str(runtime),'identities':identities})
    # Exclusive launch marker: this command cannot be used to restart science.
    with (root/f'launch{suffix}_marker.json').open('x',encoding='utf-8') as f:
        json.dump({'created_epoch':time.time(),'scientific_restart_authority':False},f)
    env=dict(os.environ)
    for k in ('OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS','NUMEXPR_NUM_THREADS'):env[k]='1'
    env['PYTHONIOENCODING']='utf-8';env['PYTHONDONTWRITEBYTECODE']='1'
    if retry:env['CH5_OBSERVATION_RUNTIME']=str(runtime)
    command=[sys.executable,'-B',str(HERE/'run.py'),str(root)]
    with (root/f'stdout{suffix}.txt').open('xb') as stdout,(root/f'stderr{suffix}.txt').open('xb') as stderr:
        child=subprocess.Popen(command,cwd=REPO,env=env,stdout=stdout,stderr=stderr)
        write(root/f'launch{suffix}_receipt.json',{'pid':child.pid,'command':command,'cwd':str(REPO),'start_epoch':time.time(),
            'threads':{k:env[k] for k in ('OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS','NUMEXPR_NUM_THREADS')},
            'observer_sources':{p.name:sha(p) for p in HERE.glob('*.py')}})
        print(json.dumps({'pid':child.pid,'root':str(root),'started':True}),flush=True)
        timeout=False
        try:code=child.wait(timeout=10800)
        except subprocess.TimeoutExpired:
            timeout=True;child.kill();code=child.wait()
        write(root/f'process{suffix}_receipt.json',{'returncode':code,'external_timeout':timeout,'end_epoch':time.time(),
            'terminal_saved':(root/'capture/terminal.json').exists(),'scientific_restart':False})
        print(read(root/f'process{suffix}_receipt.json'),flush=True)


if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    if sys.argv[1]=='prepare':prepare()
    else:{'tests':tests,'launch':launch,'retry1':lambda root:launch(root,True)}[sys.argv[1]](Path(sys.argv[2]))
