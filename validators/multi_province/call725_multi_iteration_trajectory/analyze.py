"""Sparse, solve-free comparison of captured independent/replay trajectories."""
import argparse
import csv
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.io import loadmat,savemat

REPO=Path(__file__).resolve().parents[3]
ROOT=Path(r'D:\ProjectTemp\ch5-call725-multi-iteration-trajectory-20260907-001')
PRE=Path(r'D:\ProjectTemp\ch5-mp4c-2018-call725-postcall-residual-vectorization-repair-20260904-001')
spec=importlib.util.spec_from_file_location('first_step_compare',REPO/'validators/multi_province/call725_first_iteration_closure/compare.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)


def write(path,data):
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')


def validate_steps(files):
    numbers=[int(path.stem.split('_')[1]) for path in files]
    if numbers!=list(range(1,len(files)+1)):raise ValueError(f'non-contiguous step sequence: {numbers}')
    return files


def sparse_compare(left,right):
    left,right=c.canonical_sparse(left),c.canonical_sparse(right)
    if left.shape!=right.shape or left.shape!=(800,800):
        return {'available':True,'passed':False,'shape_pass':False,'left_shape':list(left.shape),'right_shape':list(right.shape)}
    def mapping(matrix):
        coo=matrix.tocoo();return {(int(i),int(j)):float(v) for i,j,v in zip(coo.row,coo.col,coo.data)}
    x,y=mapping(left),mapping(right); coordinates=sorted(x.keys()|y.keys())
    result=c.compare_dense(np.array([x.get(k,0.) for k in coordinates]),np.array([y.get(k,0.) for k in coordinates]),(len(coordinates),))
    result['support_mismatch_count']=len(x.keys()^y.keys()); result['passed'] &= result['support_mismatch_count']==0
    result['matrix_shape']=[800,800];result['left_nnz']=len(x);result['right_nnz']=len(y)
    for example in result.get('representative_coordinates',[]):example['matrix_coordinate']=list(coordinates[example['index_zero_based'][0]])
    result['support_examples']=[list(k) for k in sorted(x.keys()^y.keys())[:5]]
    return result


def load(language,path):
    if language=='matlab':
        container=loadmat(path)
        values={name:container[mk] for _,name,mk,_,_ in c.DENSE_FIELDS}
        values.update({name:container[mk] for _,mk,name in c.SPARSE_FIELDS})
        values.update({name:container[name] for name in ('Ic_B','Ic_F','Ic_0','Idh_B','Idh_F')})
        values.update(l0=container['l0'],b=c.vector(container['b'],20),a=c.vector(container['ah'],20),z=c.vector(container['z'],2))
        values['raw_vb_f_interior']=container['raw_VbF'][:-1];values['raw_vb_b_interior']=container['raw_VbB'][1:]
        values['raw_va_f']=container['raw_VahF'];values['raw_va_b']=container['raw_VahB']
    else:
        with np.load(path,allow_pickle=False) as loaded:container={k:loaded[k] for k in loaded.files}
        values={name:container[pk] for _,name,_,pk,_ in c.DENSE_FIELDS}
        for name in ('liquid_label','transfer_label'):values[name]=c.labels(values[name])
        values.update({name:sparse.load_npz(path.with_name(path.stem+'_'+name+'.npz')) for _,_,name in c.SPARSE_FIELDS})
        values.update({mk:container[pk]==label for mk,pk,label in [('Ic_B','liquid_label','B'),('Ic_F','liquid_label','F'),('Ic_0','liquid_label','0'),('Idh_B','transfer_label','B'),('Idh_F','transfer_label','F')]})
        values.update({name:container[name] for name in ('l0','b','a','z')})
        values['raw_vb_f_interior']=container['raw_vb_f'][:-1];values['raw_vb_b_interior']=container['raw_vb_b'][1:]
        values['raw_va_f']=container['raw_va_f'];values['raw_va_b']=container['raw_va_b']
    values['RHS']=c.vector(values['RHS'],800);values['first_iteration_statistic']=c.vector(values['first_iteration_statistic'],1)
    return values


FIELDS=[(1,name,shape,True) for name,shape in [('l0',c.SHAPE),('b',(20,)),('a',(20,)),('z',(2,))]]+[(stage,name,shape,stage==3) for stage,name,_,_,shape in c.DENSE_FIELDS]+[(2,name,c.SHAPE,False) for name in ('raw_va_f','raw_va_b')]+[(3,name,c.SHAPE,True) for name in ('Ic_B','Ic_F','Ic_0','Idh_B','Idh_F')]+[(stage,name,None,False) for stage,_,name in c.SPARSE_FIELDS]
FIELDS.sort(key=lambda item:item[0])


def pair(left,right):
    rows=[]
    for stage,name,shape,exact in FIELDS:
        result=sparse_compare(left[name],right[name]) if shape is None else c.compare_dense(left[name],right[name],shape,exact=exact)
        rows.append(dict(stage=stage,name=name,**result))
    first=next((r for r in rows if not r['passed']),None)
    generated=next((r for r in rows if r['stage']>1 and not r['passed']),None)
    return {'passed':first is None,'first_mismatch':first,'first_generated_mismatch':generated,'rows':rows,
            'raw_interior_diagnostics':{name:c.compare_dense(left[name],right[name],(19,20,2)) for name in ('raw_vb_f_interior','raw_vb_b_interior')},
            'residuals':{side:c.residual(values['M'],values['RHS'],values['V1']) for side,values in [('matlab',left),('python',right)]}}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--replay',action='store_true');args=parser.parse_args()
    if args.replay:
        result=pair(load('matlab',ROOT/'matlab_replay/step_0001.mat'),load('python',ROOT/'python_replay/step_0001.npz'))
        write(ROOT/'common_state_comparison.json',result)
        print(json.dumps({k:result[k] for k in ('passed','first_mismatch','first_generated_mismatch')},indent=2));return
    matlab=validate_steps(sorted((ROOT/'matlab_trajectory').glob('step_*.mat')))
    python=validate_steps(sorted(p for p in (ROOT/'python_trajectory').glob('step_*.npz') if len(p.stem)==9))
    first_checks={}
    for language,new,old in [('matlab',matlab[0],PRE/'matlab_core_stagewise.mat'),('python',python[0],PRE/'python_strict_stagewise.npz')]:
        first_checks[language]=pair(load(language,new),load(language,old))
    write(ROOT/'fresh_first_step_acceptance_comparison.json',first_checks)
    summary=[];earliest=None;first_incoming=None;first_generated=None
    with (ROOT/'full_stage_comparison.jsonl').open('w',encoding='utf-8') as full, (ROOT/'stage_summary.csv').open('w',encoding='utf-8',newline='') as csvfile:
        writer=csv.writer(csvfile);writer.writerow(['iteration','stage','name','passed','max_abs','max_scaled','mismatches','support_mismatches'])
        for iteration,(mp,pp) in enumerate(zip(matlab,python),1):
            if mp.stem!=pp.stem:raise ValueError('cross-language iteration numbering mismatch')
            result=pair(load('matlab',mp),load('python',pp))
            full.write(json.dumps(dict(iteration=iteration,diagnostic_continuation=iteration>100,**result),allow_nan=False)+'\n')
            for row in result['rows']:writer.writerow([iteration,row['stage'],row['name'],row['passed'],row.get('max_abs'),row.get('max_scaled'),row.get('material_mismatch_count'),row.get('support_mismatch_count',0)])
            compact={'iteration':iteration,'diagnostic_continuation':iteration>100,'passed':result['passed'],'failed_fields':[r['name'] for r in result['rows'] if not r['passed']], 'incoming_state_pass':next(r['passed'] for r in result['rows'] if r['name']=='old/V0'), 'max_scaled':max(r.get('max_scaled') or 0 for r in result['rows'])}
            summary.append(compact)
            if earliest is None and not result['passed']:
                earliest={'iteration':iteration,'first_mismatch':result['first_mismatch'],'first_generated_mismatch':result['first_generated_mismatch']}
                write(ROOT/'earliest_step_comparison.json',dict(iteration=iteration,**result))
                state=loadmat(mp)
                state_path=ROOT/'common_state.mat'
                payload={k:state[k] for k in ('b','ah','z','l0')};payload['v0']=state['initial_value']
                if not state_path.exists():savemat(state_path,payload,do_compression=True)
                restored=loadmat(state_path)
                if not all(np.array_equal(restored[k],v) for k,v in payload.items()):raise RuntimeError('state readback')
                write(ROOT/'replay_state_identity.json',{'iteration':iteration,'path':str(state_path),'sha256':hashlib.sha256(state_path.read_bytes()).hexdigest().upper(),'source_step':str(mp),'source_sha256':hashlib.sha256(mp.read_bytes()).hexdigest().upper(),'fields':list(payload),'all_fields_exact_readback':True})
            if first_incoming is None and not compact['incoming_state_pass']:first_incoming=iteration
            if first_generated is None and result['first_generated_mismatch']:first_generated=iteration
    ledgers={language:json.loads((ROOT/f'{language}_trajectory/ledger.json').read_text()) for language in ('matlab','python')}
    traces={language:[json.loads(line) for line in (ROOT/f'{language}_trajectory/trace.jsonl').read_text().splitlines()] for language in ledgers}
    for language,files in [('matlab',matlab),('python',python)]:
        if ledgers[language]['completed_updates']!=len(files) or len(traces[language])!=len(files):raise ValueError('ledger/trace/core count mismatch: '+language)
    result={'first_step_matches_accepted':{k:v['passed'] for k,v in first_checks.items()},'common_iterations':len(summary),'earliest_divergence':earliest,'first_incoming_state_difference':first_incoming,'first_generated_stage_difference':first_generated,'ledgers':ledgers,'at_100':{k:next((r for r in t if r['iteration']==100),None) for k,t in traces.items()},'iterations':summary,'comparison_stop':'compare only shared iterations; never extend a converged side'}
    write(ROOT/'trajectory_summary.json',result)
    print(json.dumps({k:v for k,v in result.items() if k!='iterations'},indent=2))


if __name__=='__main__':main()
