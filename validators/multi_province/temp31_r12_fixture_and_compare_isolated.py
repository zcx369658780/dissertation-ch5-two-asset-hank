"""Fixed R9 inputs; unchanged scientific functions; one real-output comparison."""
import ast
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import re
import sys

TASK = 'CH5_TEMP31_R6_R3_R2_R12_R8_EXE_FIXED_INPUT_OPERATOR_PARITY_20261031'
ROOT = Path(__file__).resolve().parents[2]
LOCAL = ROOT/'tasks'/TASK/'LOCAL_ONLY'
FIELDS = ('b_backward','b_forward','a_backward','a_forward')
NAMES = ('BB','AAH','Bswitch','A')
FROZEN = {'frozen_matlab_faithful_operator.py':'9a511e151c9bf449412dc5605dfa1a2076711277',
          'frozen_indexing_exact.py':'3aee864af5dce5128957896e5d7803c2a815aab6',
          'frozen_matlab_trajectory.m':'0e38270154ab8953290ae3ef6c92f95d38230afb',
          'frozen_r9_fixture_spec.json':'918d02947f5de5956e273c56eb120f0cdd3b3056'}

def ident(b):
    return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}

def dump(p, obj):
    with p.open('x',encoding='utf-8',newline='\n') as f:
        json.dump(obj,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')

def load_frozen(filename, name):
    p=LOCAL/filename; raw=p.read_bytes()
    assert ident(raw)['git_blob']==FROZEN[filename]
    spec=importlib.util.spec_from_file_location(name,p)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    # Execute precisely the authenticated original bytes; no rewritten functions.
    exec(compile(raw,str(p),'exec'),module.__dict__)
    return module

def static_gate():
    sources={n:(LOCAL/n).read_bytes() for n in FROZEN}
    assert all(ident(sources[n])['git_blob']==b for n,b in FROZEN.items())
    runner=ROOT/'validators/multi_province/t31_r12_op.m'
    assert runner.stem=='t31_r12_op' and len(runner.stem)==10 and runner.suffix=='.m'
    assert re.fullmatch('[A-Za-z][A-Za-z0-9_]*',runner.stem)
    text=runner.read_text(encoding='utf-8')
    axis='\n'.join(sources['frozen_matlab_trajectory.m'].decode().splitlines()[109:130])+'\n'
    actual=text[text.index('function G=axis_operator'):]
    normalize=lambda s: re.sub(r'\s+','',s)
    assert normalize(axis)==normalize(actual)
    assert normalize(axis.replace('vals(end+1)=-total;','vals(end+1)=-total+1;'))!=normalize(actual)
    funcs={x.name for x in ast.parse(sources['frozen_matlab_faithful_operator.py']).body if isinstance(x,ast.FunctionDef)}
    assert {'assemble_source_operator','assemble_source_axis'}<=funcs
    assert 'col=row-I' in axis and 'col=row+I' in axis
    report={'status':'PASS','frozen_sources':{n:ident(b) for n,b in sources.items()},
            'axis_original_lines':[110,130],'axis_identity':ident(axis.encode()),
            'axis_runner_normalized_exact':True,'mutated_axis_rejected_in_memory':True,
            'short_name':runner.name,'stem_length':10,'identifier_valid':True,
            'axis_mapping':{'MATLAB1':'Python0_stride1','MATLAB2':'Python1_strideI'},
            'boundary_rule':'truncate outward adjacency; retain -(backward+forward) diagonal',
            'Bswitch_pair':'kron(switch,speye(IJ)) vs sparse.kron(switch,eye(IJ))'}
    dump(LOCAL/'source_pair_static_gate.json',report)
    return report

def prepare_once():
    dump(LOCAL/'fixture_python_budget_claim.json',{'fixture_builds':1,'operator_calls':2,'axis_calls':4,'retries':0})
    import numpy as np
    import scipy
    op=load_frozen('frozen_matlab_faithful_operator.py','r12_frozen_operator')
    ix=load_frozen('frozen_indexing_exact.py','r12_frozen_indexing')
    spec=json.loads((LOCAL/'frozen_r9_fixture_spec.json').read_bytes())
    pool=(0.0,0.125,-0.25,0.5,-0.75,0.25,-0.125,0.75)
    counts={'assemble_source_operator':0,'assemble_source_axis':0}
    codes={op.assemble_source_operator.__code__:'assemble_source_operator',op.assemble_source_axis.__code__:'assemble_source_axis'}
    def profile(frame,event,arg):
        if event=='call' and frame.f_code in codes:counts[codes[frame.f_code]]+=1
    outputs={};records=[]
    for q,fs in enumerate(spec['fixtures'],1):
        shape=tuple(fs['shape']); size=math.prod(shape)
        fields={field:[pool[(k*(2*f+1)+f+1)%8] for k in range(size)] for f,field in enumerate(FIELDS)}
        payload=dict(fixture_id='fixture_'+str(q),shape=list(shape),flatten_order='F',dtype='float64',
                     switch_matrix=fs['switch_matrix'],vector=[((k%7)-3)/8 for k in range(size)],**fields)
        raw=json.dumps(payload,sort_keys=True,separators=(',',':'),allow_nan=False).encode('ascii')
        assert ident(raw)==fs['input_identity'],'FIXTURE_IDENTITY'
        path=LOCAL/f'fixture_{q}.json'
        with path.open('xb') as f:f.write(raw)
        common=path.read_bytes();assert common==raw
        data=json.loads(common)
        arrays=[np.asarray(data[n],dtype=np.float64).reshape(shape,order='F') for n in FIELDS]
        assert all(np.isfinite(a).all() for a in arrays)
        mapping=[]
        for k in range(size):
            coord=ix.inverse_index(k,shape);assert ix.canonical_index(*coord,shape)==k
            mapping.append([k,*coord])
        for n,a in zip(FIELDS,arrays):
            assert np.array_equal(ix.flatten(a,shape),data[n])
            assert np.array_equal(ix.unflatten(np.asarray(data[n]),shape),a)
        assert sys.getprofile() is None
        sys.setprofile(profile)
        try:built=op.assemble_source_operator(*arrays,np.asarray(data['switch_matrix'],dtype=np.float64))
        finally:sys.setprofile(None)
        mats=dict(zip(NAMES,[built.bb,built.aah,built.bswitch,built.full]))
        saved={}
        for n,m in mats.items():
            a=m.toarray();assert a.dtype==np.float64 and a.shape==(size,size) and np.isfinite(a).all()
            rr,cc=np.nonzero(a)
            saved[n]={'shape':[size,size],'stored_nnz':int(m.nnz),
                      'support0':np.column_stack((rr,cc)).tolist(),
                      'dense_F':a.ravel(order='F').tolist(),
                      'matvec':np.asarray(m@np.asarray(data['vector'])).tolist(),
                      'row_sums':np.asarray(m.sum(axis=1)).ravel().tolist()}
        outputs[data['fixture_id']]={'matrices':saved,'mapping0':mapping,'input_identity':ident(common)}
        records.append({'fixture_id':data['fixture_id'],'shape':list(shape),'states':size,'input_identity':ident(common)})
    assert counts=={'assemble_source_operator':2,'assemble_source_axis':4}
    dump(LOCAL/'python_matrices_raw.json',outputs)
    report={'status':'PASS','calls':counts,'fixtures':records,'matrix_count':8,
            'numpy_version':np.__version__,'scipy_version':scipy.__version__,
            'frozen_function_bodies_unchanged':True,'linear_solves':0}
    dump(LOCAL/'python_build_receipt.json',report)
    return report

def compare_once(native):
    assert native['exit_code']==0 and native['natural_exit'] and native['markers_complete']
    dump(LOCAL/'comparison_budget_claim.json',{'comparators':1,'matrix_pairs':8,'scalar_positions':832,'matvec_pairs':8})
    import numpy as np
    py=json.loads((LOCAL/'python_matrices_raw.json').read_bytes())
    mat=json.loads((LOCAL/'matlab_output.json').read_bytes())
    assert mat['release']=='2022b' and mat['prefdir_match'] is True and mat['complete'] is True
    results=[];boundary_checks=[];stride_checks=[];fail=False;scalar_count=0
    def metric(a,b):
        assert a.shape==b.shape and np.isfinite(a).all() and np.isfinite(b).all()
        d=np.abs(a-b); scale=np.maximum(np.abs(a),np.abs(b))
        rel=np.divide(d,scale,out=np.zeros_like(d),where=scale!=0)
        bad=d>1e-12+1e-12*scale
        return {'max_abs_error':float(d.max()),'max_rel_error':float(rel.max()),
                'tolerance_failures':int(bad.sum()),'bad_coordinates0':np.argwhere(bad).tolist()}
    for q,fixture in enumerate(mat['fixtures'],1):
        key='fixture_'+str(q);expected=py[key]; size=(8 if q==1 else 12)
        raw=(LOCAL/f'fixture_{q}.json').read_bytes();data=json.loads(raw)
        assert fixture['fixture_id']==key and fixture['input_raw_bytes']==list(raw)
        assert fixture['shape']==data['shape']
        assert fixture['mapping0']==expected['mapping0']
        for field in FIELDS:assert fixture['inputs_F'][field]==data[field]
        pmat={};mmat={}
        for name in NAMES:
            p=expected['matrices'][name];m=fixture['matrices'][name]
            assert p['shape']==m['shape']==[size,size]
            a=np.asarray(p['dense_F'],dtype=np.float64).reshape((size,size),order='F')
            b=np.asarray(m['dense_F'],dtype=np.float64).reshape((size,size),order='F')
            pmat[name]=a;mmat[name]=b
            ps=set(map(tuple,np.argwhere(a!=0)));ms=set(map(tuple,np.argwhere(b!=0)))
            rr=np.asarray(m['rows1'],dtype=int).reshape(-1)-1
            cc=np.asarray(m['cols1'],dtype=int).reshape(-1)-1
            vv=np.asarray(m['values'],dtype=float).reshape(-1)
            assert set(zip(rr.tolist(),cc.tolist()))==ms
            assert len(rr)==len(ms)==m['stored_nnz']
            assert all(b[i,j]==v for i,j,v in zip(rr,cc,vv))
            met=metric(a,b); mv=metric(np.asarray(p['matvec']),np.asarray(m['matvec']).reshape(-1))
            assert np.array_equal(a@np.asarray(data['vector']),np.asarray(p['matvec']))
            assert np.array_equal(b@np.asarray(data['vector']),np.asarray(m['matvec']).reshape(-1))
            support_diff=sorted(ps.symmetric_difference(ms));passed=not support_diff and not met['tolerance_failures'] and not mv['tolerance_failures']
            fail|=not passed;scalar_count+=size*size
            results.append({'fixture_id':key,'matrix':name,'status':'PASS' if passed else 'FAIL',
                            'shape':[size,size], 'elements':size*size,'python_stored_nnz':p['stored_nnz'],
                            'matlab_stored_nnz':m['stored_nnz'],'exact_nonzero_count':len(ps),
                            'support_difference':len(support_diff),'support_difference_coordinates0':support_diff,
                            'python_nonzero_coordinates0':sorted(ps),'matlab_nonzero_coordinates0':sorted(ms),
                            'elementwise':met,'matvec':mv,
                            'python_row_sums':a.sum(axis=1).tolist(),'matlab_row_sums':b.sum(axis=1).tolist(),
                            'python_diagonal':np.diag(a).tolist(),'matlab_diagonal':np.diag(b).tolist()})
        for matrices in (pmat,mmat):assert np.array_equal(matrices['A'],matrices['BB']+matrices['AAH']+matrices['Bswitch'])
        for name,axis,bf,ff in [('BB',0,'b_backward','b_forward'),('AAH',1,'a_backward','a_forward')]:
            stride=1 if axis==0 else data['shape'][0]
            for side,matrices in [('Python',pmat),('MATLAB',mmat)]:
                a=matrices[name];rr,cc=np.nonzero(a)
                off=[(int(i),int(j)) for i,j in zip(rr,cc) if i!=j]
                assert all(abs(i-j)==stride for i,j in off)
                stride_checks.append({'fixture':key,'matrix':name,'side':side,'stride':stride,'offdiagonal_count':len(off),'PASS':True})
                for row,coord in enumerate(expected['mapping0']):
                    rb=data[bf][row];rf=data[ff][row];position=coord[axis+1]
                    outward=(rb if position==0 else 0)+(rf if position==data['shape'][axis]-1 else 0)
                    assert a[row,row]==-(rb+rf) and a[row,:].sum()==-outward
                    if position in (0,data['shape'][axis]-1):
                        boundary_checks.append({'fixture':key,'matrix':name,'side':side,'row0':row,
                             'coordinate0':coord[1:],'backward':rb,'forward':rf,'outward':outward,
                             'diagonal':float(a[row,row]),'row_sum':float(a[row,:].sum())})
    assert scalar_count==832 and len(results)==8
    report={'status':'FAIL' if fail else 'PASS','scalar_positions':832,'matrix_pairs':8,'matvec_pairs':8,
            'atol':1e-12,'rtol':1e-12,'results':results,'Fortran_index_tables_exact':True,
            'input_raw_bytes_echo_exact':True,'A_sum_checks_pass':True,
            'boundary_checks':boundary_checks,'stride_checks':stride_checks,
            'scope':'synthetic source assembly only; no economics or solver equivalence'}
    dump(LOCAL/'comparison_result_raw.json',report)
    return report
