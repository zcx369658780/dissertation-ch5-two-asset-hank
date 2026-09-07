"""Task-local identities and read-only predecessor access; no model evaluation."""
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
from scipy.io import loadmat, savemat

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
OLD = Path(r'D:\ProjectTemp\ch5-call725-multi-iteration-trajectory-20260907-001')
ROOT = Path(r'D:\ProjectTemp\ch5-call725-policy-operator-stability-20260907-001')
PRE = HERE.parent/'call725_multi_iteration_trajectory'
CASES = {'M24': ('matlab',24,'initial_value'), 'P24': ('python',24,'old'),
         'P32': ('python',32,'old'), 'M143_FINAL': ('matlab',143,'updated')}
BINDING = Path(r'D:\ProjectTemp\ch5-mp4c-2018-call725-first-iteration-scalar-binding-repair-20260904-001\call725_first_iteration_scalar_binding.json')
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()
def read(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def write(path,obj): Path(path).write_text(json.dumps(obj,indent=2,ensure_ascii=False,allow_nan=False)+'\n',encoding='utf-8')
def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
analysis=module(PRE/'analyze.py','accepted_analysis')
def step(language,n): return OLD/f'{language}_trajectory'/f'step_{n:04d}.{ "mat" if language=="matlab" else "npz"}'
class Evidence:
    def __init__(self):
        inventory=OLD/'artifact_inventory.json'
        assert sha(inventory)=='6D77926997A566E94FE3F016E2BD632042D22276D20D07997DCAB287749E46FC'
        self.index={r['path']:r for r in read(inventory)['entries']}; self.used={}
    def verify(self,path):
        path=Path(path); key=str(path)
        if key not in self.used:
            row=self.index[key]; assert sha(path)==row['sha256'], key
            self.used[key]=row
        return path
    def load(self,language,n):
        path=self.verify(step(language,n))
        if language=='python':
            for name in ('BB','AAH','Bswitch','A','M'): self.verify(path.with_name(path.stem+'_'+name+'.npz'))
        return analysis.load(language,path)
    def save(self,name): write(ROOT/name,list(self.used.values()))

def prepare():
    ROOT.mkdir(exist_ok=False)
    ev=Evidence()
    for name in ('state_schema.json','frozen_identities.json','trajectory_summary.json'):
        ev.verify(OLD/name)
    frozen=read(OLD/'frozen_identities.json')
    for r in frozen: assert sha(r['path'])==r['sha256'], r['path']
    write(ROOT/'frozen_identities.json',frozen)
    for row in read(OLD/'manifest.json')['sources_and_report']:
        assert sha(row['path'])==row['sha256'], row['path']
    identities={}
    for case,(lang,n,field) in CASES.items():
        path=ev.verify(step(lang,n)); v=ev.load(lang,n)
        if lang=='matlab': raw=loadmat(path); value=raw[field]
        else:
            with np.load(path,allow_pickle=False) as raw: value=raw[field].copy()
        payload={'v0':value,'l0':v['l0'],'b':v['b'][None,:],'ah':v['a'][None,:],'z':v['z'][None,:]}
        for name in ('l0','b','ah','z'):
            init=loadmat(next(r['path'] for r in frozen if r['path'].endswith('hjb100_initialization.mat')))
            assert np.array_equal(payload[name],init[name]), name
        output=ROOT/f'{case}.mat'; savemat(output,payload,do_compression=True)
        restored=loadmat(output)
        assert all(np.array_equal(restored[k],x) for k,x in payload.items())
        identities[case]={'source':str(path),'field':field,'source_sha256':sha(path),'path':str(output),'sha256':sha(output),'exact_readback':True}
    write(ROOT/'states.json',identities); ev.save('consumed_preparation.json')
    # Keep the accepted scientific body byte-for-byte at text level. Only narrow the budget.
    for name in ('python_trajectory.py','matlab_trajectory.m'):
        text=(PRE/name).read_text(encoding='utf-8')
        text=text.replace('1 <= max_updates <= 500','max_updates == 1').replace('max_updates<1 || max_updates>500','max_updates~=1')
        (HERE/name).write_text(text,encoding='utf-8')
    print(json.dumps(identities,indent=2))
if __name__=='__main__': prepare()
