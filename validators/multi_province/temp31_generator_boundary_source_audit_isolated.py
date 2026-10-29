"""Four pure synthetic operator fixtures only; no household modules imported."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,os
from pathlib import Path
import sys,traceback

TASK='CH5_TEMP31_HJB_GENERATOR_BOUNDARY_MATLAB_PROVENANCE_ISOLATED_AUDIT_R1_20261029'
SOURCE='56447829ce0e6c3c85552c53c351b26a2452a4bd'
WORK=Path(__file__).resolve().parents[2];REPORT=WORK/'tasks'/TASK
THREAD_KEYS=('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS','BLIS_NUM_THREADS')
def emit(event,**data):print(json.dumps(dict(event=event,**data),allow_nan=False),flush=True)
def verified_bytes(path,row):
    current=path.absolute()
    while current!=WORK.parent:
        s=os.lstat(current);assert not(getattr(s,'st_file_attributes',0)&0x400) and not current.is_symlink()
        current=current.parent
    raw=path.read_bytes()
    assert len(raw)==row['bytes'] and hashlib.sha256(raw).hexdigest()==row['sha256']
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==row['git_blob']
    return raw

def analytic_components(spec,switch):
    """Independent dense scalar definition; does not use the tested assembler."""
    matrices={key:[[0.0]*8 for _ in range(8)] for key in ('BB','AAH','Bswitch')}
    losses=[]
    for r in range(8):
        i=r%2;j=(r//2)%2;nz=r//4;dropped=[]
        for name,back,fwd,position,step in (
            ('BB',spec['b_backward'][r],spec['b_forward'][r],i,1),
            ('AAH',spec['a_backward'][r],spec['a_forward'][r],j,2)):
            M=matrices[name];M[r][r]=-float(back)-float(fwd)
            if position==1:M[r][r-step]=float(back)
            elif back!=0:dropped.append({'component':name,'direction':'backward','rate':back,'row_sum_contribution':-back,'reason':'lower boundary neighbor outside grid'})
            if position==0:M[r][r+step]=float(fwd)
            elif fwd!=0:dropped.append({'component':name,'direction':'forward','rate':fwd,'row_sum_contribution':-fwd,'reason':'upper boundary neighbor outside grid'})
        matrices['Bswitch'][r][r]=switch[nz][nz]
        matrices['Bswitch'][r][i+2*j+4*(1-nz)]=switch[nz][1-nz]
        losses.append(dropped)
    return matrices,losses

def run(group):
    counts={'fixtures':0,'assemble_source_operator':0,'assemble_source_axis':0,'forbidden_model_calls':0}
    results=[];stage='SUPERVISOR_HANDSHAKE'
    try:
        assert sys.stdin.readline().strip()=='GO'
        assert all(os.environ.get(k)=='1' for k in THREAD_KEYS)
        identity=json.loads((REPORT/'source_identity.json').read_text(encoding='utf-8'))
        frozen=json.loads((REPORT/'synthetic_fixture_contract.json').read_text(encoding='utf-8'))
        assert identity['source']['commit']==SOURCE and frozen['shape']==[2,2,2]
        assert len(frozen['fixtures'])==4 and len(frozen['fixture_groups'][group])==2
        stage='SOURCE_IDENTITY'
        for row in identity['source_files']:verified_bytes(WORK/row['cache_path'],row)
        operator_row=next(row for row in identity['source_files'] if row['role']=='pure_operator_runtime')
        operator_path=WORK/operator_row['cache_path']
        stage='PURE_OPERATOR_IMPORT'
        name='temp31_fixed_pure_operator_source'
        spec=importlib.util.spec_from_file_location(name,operator_path)
        module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
        assert isinstance(module.__loader__,importlib.machinery.SourceFileLoader)
        assert Path(module.__file__)==operator_path
        assert not any(name.startswith('ch5_two_asset_hank') for name in sys.modules)
        import numpy as np
        import scipy
        targets={module.assemble_source_operator.__code__:'assemble_source_operator',module.assemble_source_axis.__code__:'assemble_source_axis'}
        forbidden={'temp31_netwage_initial_arrays','_temp31_source_labor_root','select_temp31_netwage_local_policy','solve_temp31_netwage_hjb','spsolve','brentq'}
        def profile(frame,event,arg):
            if event!='call':return
            if frame.f_code.co_name in forbidden:
                counts['forbidden_model_calls']+=1
                raise AssertionError('FORBIDDEN_HA_SOLVER_CALL')
            key=targets.get(frame.f_code)
            if key:
                counts[key]+=1;assert counts[key]<=(2 if key=='assemble_source_operator' else 4),'FIXTURE_CALL_BUDGET'
        emit('import',group=group,operator_file=module.__file__,git_blob=operator_row['git_blob'],bytes=operator_row['bytes'],sha256=operator_row['sha256'],
             numpy=np.__version__,scipy=scipy.__version__,static_only_sources=[r['path'] for r in identity['source_files'] if r['role']!='pure_operator_runtime'],
             project_package_imports=0,BLAS_environment={k:os.environ[k] for k in THREAD_KEYS},native_thread_measurement='NOT_AVAILABLE_NO_EXTRA_DEPENDENCY')
        sys.setprofile(profile)
        for fixture_id in frozen['fixture_groups'][group]:
            stage='FIXTURE_'+fixture_id
            spec=next(item for item in frozen['fixtures'] if item['id']==fixture_id)
            before=counts['assemble_source_operator'];counts['fixtures']+=1;assert counts['fixtures']<=2
            vectors={key:np.array(spec[key],dtype=float).reshape((2,2,2),order='F') for key in ('b_backward','b_forward','a_backward','a_forward')}
            actual=module.assemble_source_operator(**vectors,switch_matrix=np.array(frozen['switch_matrix'],dtype=float))
            assert counts['assemble_source_operator']==before+1
            references,dropped=analytic_components(spec,frozen['switch_matrix'])
            dense={key:getattr(actual,attr).toarray() for key,attr in [('BB','bb'),('AAH','aah'),('Bswitch','bswitch'),('G','full')]}
            errors={key:float(np.max(np.abs(dense[key]-np.array(ref)))) for key,ref in references.items()}
            assert all(error<=frozen['matrix_comparison_atol'] for error in errors.values())
            assert np.allclose(dense['G'],dense['BB']+dense['AAH']+dense['Bswitch'],rtol=0,atol=5e-15)
            row_sums={key:matrix.sum(axis=1) for key,matrix in dense.items()}
            assert np.allclose(row_sums['G'],spec['expected_row_sum'],rtol=0,atol=5e-15)
            row_records=[]
            for r in range(8):
                i=r%2;j=(r//2)%2;nz=r//4
                components={}
                for key,matrix in dense.items():
                    assert matrix.shape==(8,8) and np.isfinite(matrix).all()
                    components[key]={'nonzero_entries':[{'column0':c,'column1':c+1,'value':float(matrix[r,c])} for c in range(8) if matrix[r,c]!=0],
                                     'row_sum':float(row_sums[key][r])}
                for key in ('BB','AAH'):
                    loss=sum(item['row_sum_contribution'] for item in dropped[r] if item['component']==key)
                    assert abs(row_sums[key][r]-loss)<=5e-15
                assert abs(row_sums['Bswitch'][r])<=5e-15
                row_records.append({'row0':r,'row1':r+1,'coordinate0':[i,j,nz],
                    'actual_input_rates':{key:spec[key][r] for key in vectors},'components':components,
                    'dropped_outward_rates':dropped[r],
                    'analytic_row_sum_from_dropped_rates':sum(item['row_sum_contribution'] for item in dropped[r]),
                    'causal_scope':'synthetic input-to-builder causality only; not a historical household rate'})
            offdiag=dense['G'][~np.eye(8,dtype=bool)];row_norm=float(np.max(np.abs(row_sums['G'])))
            min_off=float(offdiag.min());homecrit_pass=row_norm<=.01
            if fixture_id.startswith('F1'):
                assert row_norm<=5e-15 and min_off>=-5e-15
            elif fixture_id.startswith('F2'):
                epsilon=spec['b_forward'][1]
                assert abs(dense['BB'][1,1]+epsilon)<=5e-15 and dense['BB'][1,2]==0
                assert row_norm>1e-12 and homecrit_pass and min_off>=-5e-15
            elif fixture_id.startswith('F3'):
                assert row_norm<=5e-15 and min_off<0 and homecrit_pass
                for r in (2,3,6,7):assert abs(dense['AAH'][r,r-2]+.081)<=5e-15 and abs(dense['AAH'][r,r]-.081)<=5e-15
            else:
                assert row_norm>1e-12 and min_off<0 and row_sums['G'][4]>0 and row_sums['G'][1]<0 and row_sums['G'][3]<0
                assert abs(row_sums['G'][4]-.004)<=5e-15
            result={'fixture_id':fixture_id,'is_historical_matrix':False,'shape':[2,2,2],'state_cells':8,'inputs':spec,
              'component_reference_errors':errors,'row_sum_abs_max':row_norm,'max_signed_row_sum':float(row_sums['G'].max()),
              'min_offdiagonal_including_implicit_zeros':min_off,'original_homecrit_1e_minus2_would_pass':homecrit_pass,
              'conservative_generator_math_checks_pass':row_norm<=5e-15 and min_off>=-5e-15,
              'expected_counterexample_detected':not fixture_id.startswith('F1'),'rows':row_records}
            results.append(result);emit('fixture',**result)
        sys.setprofile(None)
        assert counts=={'fixtures':2,'assemble_source_operator':2,'assemble_source_axis':4,'forbidden_model_calls':0}
        assert not any(name.startswith('ch5_two_asset_hank') for name in sys.modules)
        emit('test_result',group=group,status='PASS_PURE_SYNTHETIC_OPERATOR_MECHANISM_CHECKS',actual_counts=counts,fixture_ids=[r['fixture_id'] for r in results],
             HA_HJB_policy_initializer_root_KFE_GE_IRF_firm_calls=0,LAST_ITERATION_EXACT_RATE_ATTRIBUTION='BLOCKED_NOT_ARCHIVED')
        return 0
    except BaseException as exc:
        sys.setprofile(None);traceback.print_exc()
        emit('test_result',group=group,status='STOP_EXCEPTION',failed_stage=stage,error_type=type(exc).__name__,error=str(exc),actual_counts=counts)
        return 1
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--group',choices=('conservation','signs'),required=True)
    raise SystemExit(run(parser.parse_args().group))
