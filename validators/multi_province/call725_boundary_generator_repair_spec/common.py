"""Exact 14-snapshot evidence intake. No production imports or evaluations."""
import hashlib
import importlib.util
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
POL=Path(r'D:\ProjectTemp\ch5-call725-policy-operator-stability-20260907-001')
TRA=Path(r'D:\ProjectTemp\ch5-call725-multi-iteration-trajectory-20260907-001')
LIN=Path(r'D:\ProjectTemp\ch5-call725-frozen-linear-system-20260907-001')
BASE=Path(r'D:\ProjectTemp\ch5-call725-boundary-generator-repair-spec-20260907-001')
def read(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()
def identity(p):return {'path':str(p),'sha256':sha(p),'bytes':Path(p).stat().st_size}
spec=importlib.util.spec_from_file_location('accepted_array_comparator',REPO/'validators/multi_province/call725_multi_iteration_trajectory/analyze.py')
analysis=importlib.util.module_from_spec(spec);spec.loader.exec_module(analysis)

class Evidence:
    def __init__(self):
        self.used={};self.index={};self.receipts=[]
        for root,expected in [(LIN,'A0FF925E71273345043ACE4F666E07A4C990116E7F7BF6BDC1011853A1C64BDD'),(POL,'EB213BD4174AB1145A332674D5D49326A7A5B4B51C17839524DA12A992203C23')]:
            m=root/'manifest.json';r=root/'manifest_readback.json';obj=read(m);receipt=read(r)
            actual=receipt.get('manifest_sha256',receipt.get('manifest',{}).get('sha256'))
            assert sha(m)==expected==actual and receipt['passed']
            self.receipts.extend([identity(m),identity(r)])
            self.index.update({x['path']:x for x in obj['artifacts']})
            if root==POL:
                self.index.update({x['path']:x for x in obj['frozen_inputs']})
                trajectory_manifest=obj['predecessor_manifest'];assert sha(trajectory_manifest['path'])==trajectory_manifest['sha256']
        inventory=TRA/'artifact_inventory.json';assert sha(inventory)=='6D77926997A566E94FE3F016E2BD632042D22276D20D07997DCAB287749E46FC'
        assert read(TRA/'manifest.json')['artifact_inventory']['sha256']==sha(inventory)
        self.receipts.extend([identity(inventory),identity(TRA/'manifest.json')]);self.index.update({x['path']:x for x in read(inventory)['entries']})
    def verify(self,p):
        p=Path(p)
        if str(p) not in self.used:
            r=self.index[str(p)];assert sha(p)==r['sha256'],str(p);self.used[str(p)]=identity(p)
        return p
    def load(self,language,path):
        self.verify(path)
        if language=='python':
            for name in ('BB','AAH','Bswitch','A','M'):self.verify(path.with_name(path.stem+'_'+name+'.npz'))
        return analysis.load(language,path)
    def receipt(self):return {'manifest_relationships_verified':self.receipts,'consumed_entries':list(self.used.values()),'scope':'14 named snapshots; no all-trajectory recomputation; historical CURRENT hashes not checked against live files'}
def snapshots():
    result=[]
    for case in ('M24','P24','P32','M143_FINAL'):
        for lang in ('matlab','python'):
            result.append({'id':lang+'_'+case,'language':lang,'path':str(POL/f'{lang}_{case}'/('step_0001.mat' if lang=='matlab' else 'step_0001.npz'))})
    for lang,steps in [('matlab',(52,57)),('python',(146,401,424,500))]:
        for n in steps:result.append({'id':f'{lang}_trajectory_{n}','language':lang,'path':str(TRA/f'{lang}_trajectory'/f'step_{n:04d}.{ "mat" if lang=="matlab" else "npz"}')})
    return result
def prepare():
    root=BASE;n=1
    while root.exists():n+=1;root=BASE.with_name(BASE.name[:-3]+f'{n:03d}')
    root.mkdir();ev=Evidence();binding=next(Path(x) for x in ev.index if x.endswith('call725_first_iteration_scalar_binding.json'))
    ev.verify(binding);assert sha(binding)=='A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6'
    write(root/'binding_identity.json',identity(binding));rows=[]
    for row in snapshots():
        try:ev.load(row['language'],Path(row['path']));row['eligible']=True
        except Exception as exc:row['eligible']=False;row['error']=repr(exc)
        rows.append(row)
    for p in (POL/'generator_summary.json',POL/'tail_switch_coordinates.json',LIN/'representation.json',TRA/'state_schema.json'):
        ev.verify(p);write(root/p.name,{'provenance':'accepted saved summary copied; not newly recomputed','source':identity(p),'data':read(p)})
    write(root/'snapshots.json',rows);write(root/'consumed_inputs.json',ev.receipt())
    print(root);print({'snapshots':len(rows),'eligible':sum(r['eligible'] for r in rows)})
if __name__=='__main__':prepare()
