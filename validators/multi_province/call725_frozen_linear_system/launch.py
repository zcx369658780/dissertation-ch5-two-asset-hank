"""Task-bound single-solve launcher. Primary cases cannot be repeated."""
import argparse
import inspect
import shutil
import subprocess
import sys
import time
from pathlib import Path
from scipy.sparse import linalg
from common import HERE, REPO, read, write, sha, identity

def main():
    p=argparse.ArgumentParser();p.add_argument('root',type=Path);p.add_argument('language',choices=['matlab','python'])
    p.add_argument('case',choices=['M_ORIGINAL','M_ROW_POW2','P_ORIGINAL','P_ROW_POW2']);args=p.parse_args()
    root=args.root; key=args.language+'_'+args.case
    system=read(root/'systems.json')[args.case];payload=Path(system['file']['path'])
    assert sha(payload)==system['file']['sha256']
    receipt_path=root/f'{key}_process.json'
    if receipt_path.exists() or (root/key).exists():raise RuntimeError('already attempted; no automatic or numerical retry')
    snapshot=root/f'{key}_sources';snapshot.mkdir(exist_ok=False)
    for name in ('python_solve.py','matlab_solve.m','common.py','launch.py'):shutil.copyfile(HERE/name,snapshot/name)
    # Observe installed SciPy solver dispatch source without invoking it.
    (snapshot/'scipy_spsolve_source.txt').write_text(inspect.getsource(linalg.spsolve),encoding='utf-8')
    if args.language=='python':command=[sys.executable,'-B',str(snapshot/'python_solve.py'),str(payload),str(root/key)]
    else:
        def q(x):return "'"+str(x).replace("'","''")+"'"
        command=[r'C:\Program Files\MATLAB\R2022b\bin\matlab.exe','-batch',f'addpath({q(snapshot)}); matlab_solve({q(payload)},{q(root/key)});']
    receipt={'language':args.language,'case':args.case,'process_attempts':1,'status':'LAUNCHING','timeout_seconds':300,
        'payload':identity(payload),'sources':[identity(x) for x in snapshot.iterdir()],'command':command}
    write(receipt_path,receipt);start=time.monotonic()
    with (root/f'{key}.log').open('wb') as log:
        process=subprocess.Popen(command,cwd=REPO,stdout=log,stderr=subprocess.STDOUT)
        receipt['pid']=process.pid;receipt['status']='RUNNING';write(receipt_path,receipt)
        try:receipt['exit_code']=process.wait(timeout=300);receipt['status']='COMPLETE' if receipt['exit_code']==0 else 'FAILED'
        except subprocess.TimeoutExpired:
            subprocess.run(['taskkill','/PID',str(process.pid),'/T','/F'],capture_output=True,check=False)
            receipt['exit_code']=None;receipt['status']='TIMEOUT'
        finally:
            receipt['elapsed_seconds']=time.monotonic()-start
            receipt['worker_ledger']=read(root/key/'ledger.json') if (root/key/'ledger.json').exists() else None
            write(receipt_path,receipt)
    print(key,receipt['status'],receipt['worker_ledger'])
if __name__=='__main__':main()
