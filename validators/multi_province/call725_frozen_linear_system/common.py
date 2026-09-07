"""Exact sparse IO and frozen binary row scaling. No evaluator or solve."""
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.io import loadmat, savemat

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
OLD=Path(r'D:\ProjectTemp\ch5-call725-policy-operator-stability-20260907-001')
BASE=Path(r'D:\ProjectTemp\ch5-call725-frozen-linear-system-20260907-001')
def read(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def write(p,obj):Path(p).write_text(json.dumps(obj,indent=2,ensure_ascii=False,allow_nan=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()
def identity(p):return {'path':str(p),'sha256':sha(p),'bytes':Path(p).stat().st_size}
def bits(x):return np.asarray(x,dtype=np.float64).reshape(-1).view(np.uint64)
def canonical(M):
    coo=M.tocoo(copy=True)
    if coo.shape!=(800,800) or coo.dtype!=np.float64:raise ValueError('matrix shape/dtype')
    order=np.lexsort((coo.col,coo.row)); r=coo.row[order]; c=coo.col[order]; d=coo.data[order]
    if np.any((r[1:]==r[:-1])&(c[1:]==c[:-1])):raise ValueError('duplicate sparse coordinates are ineligible')
    if not np.isfinite(d).all():raise ValueError('nonfinite matrix')
    keep=d!=0
    return r[keep],c[keep],d[keep],{'format':M.format,'dtype':str(M.dtype),'shape':list(M.shape),'stored_entries':int(len(d)),
        'stored_positive_zeros':int(np.sum((d==0)&~np.signbit(d))),'stored_negative_zeros':int(np.sum((d==0)&np.signbit(d))),
        'original_triplet_order_sha256':hashlib.sha256(coo.row.astype('<i8').tobytes()+coo.col.astype('<i8').tobytes()+coo.data.astype('<f8').tobytes()).hexdigest(),
        'duplicates':0,'canonical_order':'row then column; exact zeros removed only'}
def scaled_payload(M,b):
    r,c,d,_=canonical(M); s=np.zeros(800);np.maximum.at(s,r,abs(d))
    e=np.frexp(s)[1];k=np.where(s==0,0,1-e).astype(np.int32)
    factors=np.ldexp(np.ones(800),k)
    with np.errstate(over='raise',under='raise',invalid='raise'):
        sd=np.ldexp(d,k[r]); sb=np.ldexp(b,k)
        rd=np.ldexp(sd,-k[r]);rb=np.ldexp(sb,-k)
    if not np.isfinite(factors).all() or not np.isfinite(sd).all() or not np.isfinite(sb).all():raise ValueError('nonfinite scaling')
    if not np.array_equal(bits(rd),bits(d)) or not np.array_equal(bits(rb),bits(b)) or np.any(sd==0):raise ValueError('reverse scaling not exact/support lost')
    return sparse.csr_matrix((sd,(r,c)),shape=(800,800)),sb,k,{'exponent_min':int(k.min()),'exponent_max':int(k.max()),'zero_rows':np.flatnonzero(s==0).tolist(),'exact_reverse_bits':True,'support_unchanged':True,'underflow_overflow':False}
def save_payload(path,M,b,k):
    r,c,d,storage=canonical(M);b=np.asarray(b)
    if b.shape!=(800,) or b.dtype!=np.float64 or not np.isfinite(b).all():raise ValueError('RHS')
    matrix=sparse.csc_matrix((d,(r,c)),shape=(800,800))
    savemat(path,{'M':matrix,'rhs':b[:,None],'k':k[:,None],
        'ref_row':(r.astype(np.int64)+1)[:,None],'ref_col':(c.astype(np.int64)+1)[:,None],
        'ref_data_bits':bits(d)[:,None],'ref_rhs_bits':bits(b)[:,None]},do_compression=True)
    loaded=load_payload(path)
    assert np.array_equal(bits(loaded[1]),bits(b))
    lr,lc,ld,_=canonical(loaded[0]);assert np.array_equal(lr,r) and np.array_equal(lc,c) and np.array_equal(bits(ld),bits(d))
    return {'file':identity(path),'original_storage':storage,'common_MAT_sparse_format':'CSC','python_solver_format':'CSR',
        'RHS_shape_saved':[800,1],'RHS_dtype':'float64','RHS_negative_zeros':int(np.sum((b==0)&np.signbit(b))),
        'data_binary64_sha256':hashlib.sha256(bits(d).tobytes()).hexdigest(),'rhs_binary64_sha256':hashlib.sha256(bits(b).tobytes()).hexdigest(),
        'support_sha256':hashlib.sha256(r.astype('<i8').tobytes()+c.astype('<i8').tobytes()).hexdigest(),
        'exact_numeric_and_bit_readback':True,'byteorder':np.dtype(np.float64).byteorder}
def load_payload(path):
    m=loadmat(path);r,c,d,_=canonical(m['M']);b=m['rhs']
    if b.shape!=(800,1) or b.dtype!=np.float64:raise ValueError('RHS shape/dtype')
    assert np.array_equal(r+1,m['ref_row'].ravel()) and np.array_equal(c+1,m['ref_col'].ravel())
    assert np.array_equal(bits(d),m['ref_data_bits'].ravel()) and np.array_equal(bits(b),m['ref_rhs_bits'].ravel())
    return sparse.csr_matrix((d,(r,c)),shape=(800,800)),b.ravel(),m['k'].ravel()

def prepare():
    root=BASE; suffix=1
    while root.exists():suffix+=1;root=BASE.with_name(BASE.name[:-3]+f'{suffix:03d}')
    root.mkdir();manifest=read(OLD/'manifest.json');receipt=read(OLD/'manifest_readback.json')
    assert sha(OLD/'manifest.json')==receipt['manifest_sha256'] and receipt['passed']
    index={r['path']:r for r in manifest['artifacts']+manifest['frozen_inputs']};used={}
    def verify(p):
        p=Path(p);row=index[str(p)];assert sha(p)==row['sha256'],str(p);used[str(p)]=identity(p);return p
    common_state=verify(OLD/'P32.mat');assert sha(common_state)=='094B4B0815335B4C6257E6EE14C9FC75186CD7792BC3CD6BAC6D996486334FA4'
    binding=verify(next(Path(r['path']) for r in manifest['frozen_inputs'] if r['path'].endswith('call725_first_iteration_scalar_binding.json')))
    assert sha(binding)=='A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6'
    write(root/'binding.json',read(binding))
    for lang in ('matlab','python'):
        for row in manifest['artifacts']:
            if str(OLD/f'{lang}_P32_sources')+'\\' in row['path']:verify(row['path'])
    stage=read(verify(OLD/'replay_comparisons.json'))['P32'];fidelity=read(verify(OLD/'replay_fidelity.json'))
    write(root/'predecessor_comparisons.json',{'provenance':'copied accepted saved comparisons; no evaluator rerun','P32':stage,
        'origin_fidelity':{k:{'passed':v['passed'],'rows':v['rows']} for k,v in fidelity.items()},
        'prior_tests':'Prior checks.json counts were Builder-written summary, not parsed raw test-log evidence.'})
    systems={}; failures=[]
    for origin in ('M','P'):
        try:
            if origin=='M':
                path=verify(OLD/'matlab_P32/step_0001.mat');m=loadmat(path)
                M=m['matrix'];b=m['rhs'].ravel();x=m['updated'].ravel(order='F');A=m['A'];v=m['initial_value']
                fields={'M':'matrix','rhs':'rhs','saved_x':'updated','context_A':'A','context_V':'initial_value'}
            else:
                path=verify(OLD/'python_P32/step_0001.npz');m=np.load(path,allow_pickle=False)
                M=sparse.load_npz(verify(OLD/'python_P32/step_0001_M.npz'));A=sparse.load_npz(verify(OLD/'python_P32/step_0001_A.npz'))
                b=m['rhs'];x=m['v1'].ravel(order='F');v=m['old'];fields={'M':'step_0001_M.npz','rhs':'rhs','saved_x':'v1','context_A':'step_0001_A.npz','context_V':'old'}
            assert np.array_equal(bits(v),bits(loadmat(common_state)['v0']))
            sparse.save_npz(root/f'{origin}_A.npz',A);np.savez(root/f'{origin}_saved.npz',x=x)
            original=save_payload(root/f'{origin}_ORIGINAL.mat',M,b,np.zeros(800,dtype=np.int32))
            systems[origin+'_ORIGINAL']={'origin':origin,'representation':'ORIGINAL','source':str(path),'fields':fields,**original}
            try:
                S,sb,k,scaling=scaled_payload(M,b)
                systems[origin+'_ROW_POW2']={'origin':origin,'representation':'ROW_POW2','scaling':scaling,**save_payload(root/f'{origin}_ROW_POW2.mat',S,sb,k)}
            except Exception as exc:failures.append({'origin':origin,'representation':'ROW_POW2','reason':repr(exc)})
        except Exception as exc:failures.append({'origin':origin,'representation':'ALL','reason':repr(exc)})
    write(root/'systems.json',systems);write(root/'ineligible.json',failures)
    write(root/'consumed_inputs.json',{'predecessor_manifest':identity(OLD/'manifest.json'),'predecessor_readback':identity(OLD/'manifest_readback.json'),
        'digest_relationship_verified':True,'entries':list(used.values()),'prior_current_docs':'historical identities not compared to live updated documents'})
    print(str(root));print(json.dumps({'eligible':list(systems),'ineligible':failures},indent=2))
if __name__=='__main__':prepare()
