"""Exactly one real frozen KFE solve on one authenticated legacy post-G archive."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,os
from pathlib import Path
import sys,traceback,warnings
TASK='CH5_TEMP31_MATLAB_KFE_BLACKBOX_PARITY_FREEZE_R1_20261029';SRC='56447829ce0e6c3c85552c53c351b26a2452a4bd'
WORK=Path(__file__).resolve().parents[2];REPORT=WORK/'tasks'/TASK
THREAD_KEYS=('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS','BLIS_NUM_THREADS')
def emit(event,**data):print(json.dumps(dict(event=event,**data),allow_nan=False),flush=True)
def safe(path):
    current=path
    while current!=WORK.parent:
        s=os.lstat(current);assert not(getattr(s,'st_file_attributes',0)&0x400) and not current.is_symlink(),'STOP_ARCHIVE_OR_SOURCE_REPARSE'
        current=current.parent
    return path.read_bytes()
def identity(raw):return {'git_blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def run(point):
    stage='HANDSHAKE';counts={'KFE_calls':0,'KFE_spsolve_calls':0,'row_index_helper_calls':0,'forbidden_model_calls':0}
    try:
        assert sys.stdin.readline().strip()=='GO' and all(os.environ.get(k)=='1' for k in THREAD_KEYS)
        source=json.loads((REPORT/'source_identity.json').read_text(encoding='utf-8'));contract=json.loads((REPORT/'replay_contract.json').read_text(encoding='utf-8'))
        archive_index=json.loads((REPORT/'archive_identity.json').read_text(encoding='utf-8'))
        assert source['source']['commit']==SRC and source['source_patch_decision']=='KFE_SOURCE_MATCH_NO_CODE_CHANGE' and archive_index['all_four_available_authenticated']
        record=next(r for r in archive_index['points'] if r['point']==point);assert record['shape']==[20,20,2]
        stage='AUTHENTICATE_SOURCE_AND_ARCHIVES'
        core=next(r for r in source['source_files'] if r['role']=='KFE_RUNTIME');path=WORK/core['cache_path'];raw=safe(path)
        assert all(identity(raw)[k]==core[k] for k in identity(raw)) and core['git_blob']=='4ccb7cec8c4754e91bd8830a95dc533811784391'
        for archive in record['archives']:
            raw=safe(WORK/archive['path']);assert len(raw)==archive['bytes'] and hashlib.sha256(raw).hexdigest()==archive['sha256']
        old_raw=safe(WORK/record['source_point_result_path']);assert all(identity(old_raw)[k]==record['source_point_result_identity'][k] for k in identity(old_raw))
        old=json.loads(old_raw);assert old['point']==point and old['classification']=='KFE_NOT_CERTIFIED' and old['HJB']['converged'] and old['initialization']['shape']==[20,20,2]
        stage='IMPORT_REAL_KFE_ONLY'
        name='temp31_actual_frozen_kfe_core';spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
        assert isinstance(module.__loader__,importlib.machinery.SourceFileLoader) and Path(module.__file__)==path
        assert not any(n.startswith('ch5_two_asset_hank') for n in sys.modules)
        import numpy as np
        import scipy
        from scipy import sparse
        def norm(x):return float(np.max(np.abs(x))) if np.size(x) else 0.0
        def ahash(x):return hashlib.sha256(np.asarray(x,dtype='<f8').tobytes(order='F')).hexdigest()
        def mhash(M):
            M=M.tocsr();return hashlib.sha256(M.indptr.tobytes()+M.indices.tobytes()+M.data.tobytes()).hexdigest()
        archive_hjb=next(r for r in record['archives'] if r['kind']=='hjb_post_rates');archive_kfe=next(r for r in record['archives'] if r['kind']=='kfe_raw_density')
        with np.load(WORK/archive_hjb['path'],allow_pickle=False) as data:
            assert data['initial_value'].shape==(20,20,2)
            G=sparse.csr_matrix((data['post_G_data'].copy(),data['post_G_indices'].copy(),data['post_G_indptr'].copy()),shape=(800,800))
        with np.load(WORK/archive_kfe['path'],allow_pickle=False) as data:
            legacy_raw=data['raw'].copy();legacy_density=data['density'].copy();legacy_a=data['a_mass'].copy();legacy_b=data['b_mass'].copy()
        assert G.shape==(800,800) and mhash(G)==record['post_CSR_sha256']==old['HJB']['post_convergence_operator']['csr_sha256']
        assert legacy_raw.shape==(800,) and legacy_density.shape==(20,20,2) and legacy_a.shape==legacy_b.shape==(20,)
        emit('authenticated_replay_input',point=point,source_commit=SRC,KFE_blob=core['git_blob'],KFE_file=module.__file__,KFE_bytes=core['bytes'],KFE_sha256=core['sha256'],
             source_task=record['source_task'],source_final_commit=record['source_final_commit'],prices=record['prices'],shape=[20,20,2],post_CSR_sha256=mhash(G),
             original_archive_identities=[{k:a[k] for k in ('kind','bytes','sha256')} for a in record['archives']],legacy_density_F_sha256=ahash(legacy_density),legacy_raw_sha256=ahash(legacy_raw),
             old_R1_classification='KFE_NOT_CERTIFIED',BLAS_environment={k:os.environ[k] for k in THREAD_KEYS},native_threads='NOT_INDEPENDENTLY_MEASURED',python=sys.version.split()[0],numpy=np.__version__,scipy=scipy.__version__)
        targets={module.solve_matlab_faithful_stationary_kfe.__code__:'KFE_calls',module.matlab_contaminated_row_index.__code__:'row_index_helper_calls',module.linalg.spsolve.__code__:'KFE_spsolve_calls'}
        forbidden={'solve_temp31_netwage_hjb','select_temp31_netwage_local_policy','temp31_netwage_initial_arrays','_temp31_source_labor_root','brentq'}
        def profile(frame,event,arg):
            if event!='call':return
            if frame.f_code.co_name in forbidden:
                counts['forbidden_model_calls']+=1;raise AssertionError('FORBIDDEN_HJB_POLICY_INITIALIZER_ROOT_CALL')
            key=targets.get(frame.f_code)
            if key:counts[key]+=1;assert counts[key]<=1,'REPLAY_CALL_BUDGET'
        stage='ONE_REAL_FROZEN_KFE_CALL';sys.setprofile(profile)
        with warnings.catch_warnings(record=True) as warning_records:
            warnings.simplefilter('always')
            result=module.solve_matlab_faithful_stationary_kfe(G,shape=(20,20,2),db=7/19,da=10/19)
        sys.setprofile(None)
        assert counts=={'KFE_calls':1,'KFE_spsolve_calls':1,'row_index_helper_calls':1,'forbidden_model_calls':0}
        assert mhash(G)==record['post_CSR_sha256'] and mhash(result.original_operator)==mhash(G),'post operator modified'
        assert np.isfinite(result.raw_solve_vector).all() and np.isfinite(result.density).all() and np.isfinite(result.normalization_factor)
        stage='PURE_ARRAY_METHOD_AND_ARCHIVE_CHECKS'
        transpose=G.T.tocsr();assert norm((result.transpose-transpose).data)==0
        expected=transpose.toarray();row=295;expected[row,:]=0.;expected[row,row]=1.
        matrix_error=norm(result.contaminated_matrix.toarray()-expected)
        rhs=np.zeros(800);rhs[row]=.007;assert np.array_equal(result.rhs,rhs) and result.contaminated_row_index==row and matrix_error==0
        factor=float(np.sum(result.raw_solve_vector)*(7/19)*(10/19))
        assert result.normalization_factor==factor and result.cell_weight==(7/19)*(10/19)
        assert np.array_equal(result.density_vector,result.raw_solve_vector/factor)
        assert np.array_equal(result.density,result.density_vector.reshape((20,20,2),order='F'))
        comparison={'raw_max_abs_difference':norm(result.raw_solve_vector-legacy_raw),'density_max_abs_difference':norm(result.density-legacy_density),
          'normalization_abs_difference':abs(result.normalization_factor-old['KFE']['normalization_factor']),
          'raw_exact_array_equal':bool(np.array_equal(result.raw_solve_vector,legacy_raw)),'density_exact_array_equal':bool(np.array_equal(result.density,legacy_density)),
          'raw_F_sha256':ahash(result.raw_solve_vector),'density_F_sha256':ahash(result.density),'legacy_raw_F_sha256':ahash(legacy_raw),'legacy_density_F_sha256':ahash(legacy_density),
          'normalization_factor':float(result.normalization_factor),'original_normalization_factor':old['KFE']['normalization_factor']}
        tol=contract['comparison_tolerance']['raw_density_normalization_moments_abs']
        assert all(comparison[k]<=tol for k in ('raw_max_abs_difference','density_max_abs_difference','normalization_abs_difference')),'REPLAY_MISMATCH_NO_RETRY'
        g=result.density;weight=result.cell_weight;gvec=result.density_vector
        a=np.linspace(0,10,20);b=np.linspace(-2,5,20)
        a_mass=g.sum(axis=(0,2))*weight;b_mass=g.sum(axis=(1,2))*weight
        At=float((g*a[None,:,None]).sum()*weight);Bt=float((g*b[:,None,None]).sum()*weight)
        assert norm(a_mass-legacy_a)<=tol and norm(b_mass-legacy_b)<=tol and abs(At-old['KFE']['At'])<=tol and abs(Bt-old['KFE']['Bt'])<=tol
        original_residual=transpose@gvec;raw_residual=result.contaminated_matrix@result.raw_solve_vector-result.rhs
        total=float(gvec.sum()*weight);neg=float(np.maximum(-gvec,0).sum()*weight)
        strict_tests={'density_finite':True,'total_mass_abs_error_le_1e8':abs(total-1)<=1e-8,'negative_mass_le_1e8':neg<=1e-8,
                      'original_stationarity_le_1e7':norm(original_residual)<=1e-7,'contaminated_raw_system_le_1e7':norm(raw_residual)<=1e-7}
        rows=np.asarray(G.sum(axis=1)).ravel();coo=G.tocoo();off=coo.data[coo.row!=coo.col]
        warning=norm(original_residual)>contract['original_stationarity_warning_threshold']
        diagnostic={'original_stationarity_residual':norm(original_residual),'original_stationarity_residual_argmax_index0':int(np.argmax(np.abs(original_residual))),
          'residual_at_replaced_row':float(original_residual[row]),'non_replaced_rows_stationarity_residual_max':norm(np.delete(original_residual,row)),
          'contaminated_raw_system_residual':norm(raw_residual),'source_raw_residual_inf':float(result.raw_residual_inf),
          'normalized_contaminated_equation_residual':norm(result.contaminated_matrix@gvec-result.rhs/factor),
          'post_row_sum_abs_max':norm(rows),'post_max_signed_row_sum':float(rows.max()),'post_min_offdiagonal_including_zeros':min(0.,float(off.min())) if off.size else 0.,
          'total_probability':total,'negative_probability_mass':neg,'negative_density_cells':int((gvec<0).sum()),'density_min':float(gvec.min()),'density_max':float(gvec.max()),
          'a_mass20':a_mass.tolist(),'b_mass20':b_mass.tolist(),'At_unverified_diagnostic':At,'Bt_unverified_diagnostic':Bt,
          'a_internal_mass':float(a_mass[1:-1].sum()),'b_internal_mass':float(b_mass[1:-1].sum()),'a_lower_mass':float(a_mass[0]),'a_upper_mass':float(a_mass[-1]),
          'b_lower_mass':float(b_mass[0]),'b_upper_mass':float(b_mass[-1]),'original_R1_stationarity_residual':old['KFE']['stationary_residual'],
          'original_residual_abs_difference':abs(norm(original_residual)-old['KFE']['stationary_residual']),
          'STATIONARITY_WARNING':warning,'density_clipped_or_abs_modified':False}
        assert diagnostic['original_residual_abs_difference']<=tol
        emit('replay_result',point=point,status='REPLAY_MATCH',MATLAB_KFE_METHOD_EXECUTED=True,
             ORIGINAL_STATIONARITY_DIAGNOSTIC=diagnostic,STRICT_ECONOMIC_STATIONARITY_CERTIFIED=all(strict_tests.values()),strict_tests=strict_tests,
             compatibility_status='SOURCE_KFE_COMPUTED_WITH_STATIONARITY_WARNING' if warning else 'SOURCE_KFE_METHOD_COMPUTED',
             contract_compatibility_alias='SOURCE_METHOD_COMPUTED_WITH_STATIONARITY_WARNING' if warning else 'SOURCE_METHOD_COMPUTED',
             old_R1_classification_unchanged='KFE_NOT_CERTIFIED',archive_comparison=comparison,
             method_checks={'transpose_exact':True,'unit_row_index0':295,'MATLAB_unit_row_index1':296,'rhs_at_row':.007,'contaminated_matrix_difference':matrix_error,'normalization_exact':True,'Fortran_reshape_exact':True,'same_post_G_unmodified':True},
             warnings=[{'type':type(w.message).__name__,'message':str(w.message)} for w in warning_records],actual_counts=counts,
             MATLAB_RAW_LOCAL_VERIFICATION='NOT_AVAILABLE',MATLAB_runtime_execution=False,source_code_modified=False,price_search_calls=0,firm_GE_IRF_31province_calls=0)
        return 0
    except BaseException as exc:
        sys.setprofile(None);traceback.print_exc()
        emit('replay_result',point=point,status='STOP_EXCEPTION',failed_stage=stage,error_type=type(exc).__name__,error=str(exc),actual_counts=counts)
        return 1
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--point',choices=('P0','P2','P4','P5'),required=True)
    raise SystemExit(run(parser.parse_args().point))
