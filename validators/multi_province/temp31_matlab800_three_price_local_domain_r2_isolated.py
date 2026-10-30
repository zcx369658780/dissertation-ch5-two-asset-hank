"""Twelve frozen local 800-state prices; immutable real source, one point per child."""
from __future__ import annotations
import argparse,ast,hashlib,importlib,importlib.util,json,os
from pathlib import Path
import sys,traceback,warnings

TASK='CH5_TEMP31_MATLAB800_THREE_PRICE_LOCAL_DOMAIN_MAP_R2_20261030'
SOURCE='56447829ce0e6c3c85552c53c351b26a2452a4bd'
WORK=Path(__file__).resolve().parents[2];REPORT=WORK/'tasks'/TASK;EV=REPORT/'evidence'
THREAD_KEYS=('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS','BLIS_NUM_THREADS')
PRICES=[('D00', 0.045, 0.02, 19.0), ('D01', 0.055, 0.02, 19.0), ('D02', 0.06, 0.02, 19.0), ('D03', 0.05, 0.015, 19.0), ('D04', 0.05, 0.025, 19.0), ('D05', 0.05, 0.02, 17.0), ('D06', 0.05, 0.02, 18.0), ('D07', 0.05, 0.02, 20.0), ('D08', 0.05, 0.02, 21.0), ('D09', 0.055, 0.025, 18.0), ('D10', 0.045, 0.015, 20.0), ('D11', 0.07, 0.025, 17.0)]
def emit(event,**values):print(json.dumps(dict(event=event,**values),allow_nan=False),flush=True)
def ident(raw):return {'git_blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def safe_bytes(path,row):
    current=path
    while current!=WORK.parent:
        s=os.lstat(current);assert not(getattr(s,'st_file_attributes',0)&0x400) and not current.is_symlink(),'source reparse'
        current=current.parent
    raw=path.read_bytes();actual=ident(raw);assert all(actual[k]==row[k] for k in actual),'source bytes drift'
    return raw
def auth_helper(row,name):
    path=WORK/row['path'];safe_bytes(path,row)
    spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module);return module
def require_fresh(initialized_for,point_id,fresh,warm_start):
    if initialized_for!=point_id or not fresh or warm_start:raise ValueError('WARM_START_REJECTED')
def require_kfe_gate(converged,statistic):
    if not converged or not statistic<1e-7:raise ValueError('KFE_BEFORE_HJB_CONVERGENCE_REJECTED')

def run(point_id):
    counts={key:0 for key in ('initializer_calls','root_cells','brentq_calls','hjb_calls','hjb_iterations','hjb_policy_cells','operator_assemblies','hjb_linear_solves','kfe_calls','kfe_linear_solves','kfe_contaminated_row_index_calls')}
    active={'hjb':0,'kfe':0};trajectory=[];last={};stage='HANDSHAKE';output=None
    try:
        assert sys.stdin.readline().strip()=='GO'
        assert all(os.environ.get(k)=='1' for k in THREAD_KEYS)
        identity=json.loads((REPORT/'source_identity.json').read_text(encoding='utf-8'))
        config=json.loads((REPORT/'point_grid.json').read_text(encoding='utf-8'))
        assert identity['source']['commit']==SOURCE
        assert [(p['id'],p['rah'],p['rb'],p['wt']) for p in config['points']]==PRICES
        point=next(p for p in config['points'] if p['id']==point_id)
        stage='SOURCE_IDENTITY_AND_IMPORTS';expected={}
        for row in identity['source_files']:
            path=WORK/row['cache_path'];safe_bytes(path,row);name=row['path'].removeprefix('src/')[:-3].replace('/','.')
            expected[name]=(path,row)
        loader=auth_helper(identity['authenticated_namespace_helper'],'temp31_pilot_authentic_namespace_loader')
        cache=(WORK/identity['source_files'][0]['cache_path'])
        cache_root=REPORT/'LOCAL_ONLY_authenticated_source'
        loader.namespace('ch5_two_asset_hank',cache_root/'ch5_two_asset_hank')
        loader.namespace('ch5_two_asset_hank.multi_province',cache_root/'ch5_two_asset_hank/multi_province')
        modules={name:importlib.import_module(name) for name in expected}
        assert {name for name in sys.modules if name.startswith('ch5_two_asset_hank.')}==set(expected)|{'ch5_two_asset_hank.multi_province'}
        origins=[]
        for name,(path,row) in expected.items():
            module=modules[name];assert Path(module.__file__)==path and isinstance(module.__loader__,importlib.machinery.SourceFileLoader)
            origins.append({'module':name,'file':module.__file__,**{k:row[k] for k in ('git_blob','bytes','sha256')}})
        import numpy as np
        import scipy
        short={name.rsplit('.',1)[-1]:module for name,module in modules.items()}
        boot=short['temp31_ha_taxfree_bootstrap'];debug=short['temp31_ha_wage_debug'];hjb=short['temp31_netwage_hjb']
        policy=short['temp31_netwage_policy'];operator=short['matlab_faithful_operator'];kfe=short['matlab_faithful_kfe'];contracts=short['contracts']
        emit('imports',point=point_id,source_commit=SOURCE,modules=origins,python=sys.version.split()[0],numpy=np.__version__,scipy=scipy.__version__,
             package_initializers='two namespace shells only; no production package initializer execution',BLAS_environment={k:os.environ[k] for k in THREAD_KEYS},native_threads='NOT_INDEPENDENTLY_MEASURED')
        def norm(x):return float(np.max(np.abs(x))) if np.size(x) else 0.0
        def array_hash(x):return hashlib.sha256(np.asarray(x,dtype='<f8').tobytes(order='F')).hexdigest()
        def matrix_hash(M):
            C=M.tocsr();return hashlib.sha256(C.indptr.tobytes()+C.indices.tobytes()+C.data.tobytes()).hexdigest()
        def matrix_metrics(M):
            C=M.tocoo();mask=C.row!=C.col;data=C.data[mask]
            rows=np.asarray(M.sum(axis=1)).ravel()
            return {'shape':list(M.shape),'nnz':int(M.nnz),'finite':bool(np.isfinite(M.data).all()),'row_sum_abs_max':norm(rows),
                    'max_signed_row_sum':float(rows.max()),'min_offdiagonal_including_implicit_zeros':min(0.0,float(data.min())) if data.size else 0.0,'csr_sha256':matrix_hash(M)}
        limits={'initializer_calls':1,'root_cells':800,'brentq_calls':800,'hjb_calls':1,'hjb_iterations':100,'hjb_policy_cells':80000,'operator_assemblies':101,'hjb_linear_solves':100,'kfe_calls':1,'kfe_linear_solves':1,'kfe_contaminated_row_index_calls':1}
        targets={boot.temp31_netwage_initial_arrays.__code__:'initializer_calls',boot._temp31_source_labor_root.__code__:'root_cells',boot.brentq.__code__:'brentq_calls',
                 hjb.solve_temp31_netwage_hjb.__code__:'hjb_calls',policy.select_temp31_netwage_local_policy.__code__:'hjb_policy_cells',
                 operator.assemble_source_operator.__code__:'operator_assemblies',hjb.linalg.spsolve.__code__:'linear_solve',
                 kfe.solve_matlab_faithful_stationary_kfe.__code__:'kfe_calls',kfe.matlab_contaminated_row_index.__code__:'kfe_contaminated_row_index_calls'}
        def bump(key):counts[key]+=1;assert counts[key]<=limits[key],'CALL_BUDGET '+key
        def profile(frame,event,arg):
            name=targets.get(frame.f_code)
            if name is None:return
            if event=='call':
                if name=='linear_solve':
                    assert active['hjb']+active['kfe']==1
                    bump('hjb_linear_solves' if active['hjb'] else 'kfe_linear_solves')
                else:
                    if name=='hjb_policy_cells':assert active['hjb']==1
                    bump(name)
                if name=='hjb_calls':active['hjb']+=1
                if name=='kfe_calls':active['kfe']+=1
                if name=='root_cells':
                    wage=float(frame.f_locals['wage']);assert any(abs(wage-expected_wage*z)<=1e-12 for z in (.8,1.3)),'second wage wedge'
            elif event=='return':
                if name=='hjb_calls':active['hjb']-=1
                if name=='kfe_calls':active['kfe']-=1
        source_ast=ast.parse(Path(hjb.__file__).read_bytes().decode())
        f=next(n for n in source_ast.body if isinstance(n,ast.FunctionDef) and n.name=='solve_temp31_netwage_hjb')
        loop=next(n for n in f.body if isinstance(n,ast.For) and isinstance(n.target,ast.Name) and n.target.id=='iteration')
        entry_line=loop.body[0].lineno
        check_line=next(n.lineno for n in loop.body if isinstance(n,ast.If) and isinstance(n.test,ast.Compare) and isinstance(n.test.left,ast.Name) and n.test.left.id=='statistic')
        def trace_hjb(frame,event,arg):
            if event=='line' and frame.f_lineno==entry_line:bump('hjb_iterations')
            elif event=='line' and frame.f_lineno==check_line:
                loc=frame.f_locals;assert np.isfinite(loc['value']).all() and np.isfinite(loc['statistic']),'nonfinite HJB'
                metrics=matrix_metrics(loc['operator'].full)
                row={'iteration':int(loc['iteration']),'value_change':float(loc['statistic']),'value_min':float(loc['value'].min()),'value_max':float(loc['value'].max()),
                     'operator_row_sum_abs_max':metrics['row_sum_abs_max'],'operator_min_offdiag':metrics['min_offdiagonal_including_implicit_zeros'],
                     'homecrit_violated':metrics['row_sum_abs_max']>.01,
                     'implicit_equation_error':norm((params.rho*loc['value'].ravel(order='F')-loc['arrays']['utility'].ravel(order='F')-loc['operator'].full@loc['value'].ravel(order='F'))-(loc['old']-loc['value']).ravel(order='F')/1000.)}
                trajectory.append(row)
                last.update(old=loc['old'].copy(),utility=loc['arrays']['utility'].copy(),G=loc['operator'].full.copy(),
                            b_backward=loc['bb'].copy(),b_forward=loc['bf'].copy(),a_backward=loc['ab'].copy(),a_forward=loc['af'].copy())
                emit('hjb_iteration',point=point_id,**row,observed_counts=dict(counts))
            return trace_hjb
        def trace_calls(frame,event,arg):return trace_hjb if frame.f_code is hjb.solve_temp31_netwage_hjb.__code__ else None
        expected_wage=point['wt'];sys.setprofile(profile)
        def wage_input(p):
            context='TEMP31_MATLAB800_SYNTHETIC_LOCAL_DOMAIN_R2_20261030_'+p['id'];order=('A','B')
            if p['id'] in ('D00','D01','D02','D03','D04'):
                record=boot.numerical_bootstrap19(context_id=context,province_order=order,tax_by_destination=(.05,.05),sigma_destination_origin=((0,0),(0,0)))
                witness={'scope':'NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL','chain':['numerical_bootstrap19','netwage_inputs'],'entering_iteration':1,'synthetic_firm_wage':None}
            else:
                firm=p['wt']/(.95*2**(5/6))
                calculation=debug.SyntheticNetWageCalculation(firm_wages_by_destination=(firm,firm),tax_by_destination=(.05,.05),
                    phi_destination_origin=((1,1),(1,1)),sigma_destination_origin=((0,0),(0,0)),phi_l=5,alphal=1,
                    province_order=order,context_id=context,generated_after_iteration=1)
                producer=debug.calculated_round_record(calculation,entering_iteration=2)
                record=boot.later_net_wage_record(producer)
                witness={'scope':'COUNTERFACTUAL_SYNTHETIC_WAGE_WITNESS_NO_REAL_FIRM_EMPIRICAL_PROVENANCE',
                    'chain':['SyntheticNetWageCalculation','calculated_round_record','later_net_wage_record','netwage_inputs'],
                    'generated_after_iteration':1,'entering_iteration':2,'synthetic_firm_wage':firm,'phi_destination_origin':[[1,1],[1,1]],'phi_l':5,'alphal':1,
                    'metadata_only_no_actual_firm_or_iteration_run':True}
            inputs=boot.netwage_inputs(record,origin_index=0,r_a=p['rah'],r_b=p['rb'],expected_context_id=context,expected_province_order=order)
            assert abs(float(inputs.wages[0])-p['wt'])<=1e-12 and inputs.labor_weights.tolist()==[1.0]
            assert not hasattr(inputs,'tau') and not hasattr(inputs,'migration_costs')
            assert record.tax_by_destination==(.05,.05) and record.sigma_destination_origin==((0.0,0.0),(0.0,0.0))
            witness.update(point=p['id'],requested_effective_wage=p['wt'],actual_source_effective_wage=float(inputs.wages[0]),wage_error=abs(float(inputs.wages[0])-p['wt']),
                context_id=context,province_order=list(order),record_semantics=record.semantics,real_empirical_provenance=False,tax_background_preserved=True)
            return inputs,witness
        def require_grid(b,a,z):
            if b.shape!=(20,) or a.shape!=(20,) or z.shape!=(2,) or not np.array_equal(b,np.linspace(-2,5,20)) or not np.array_equal(a,np.linspace(0,10,20)) or not np.array_equal(z,np.array([.8,1.3])):
                raise ValueError('GRID_800_FREEZE_REJECTED')
        stage='WAGE_PROVENANCE_GATE'
        if point_id=='D00':
            witnesses=[wage_input(p)[1] for p in config['points']]
            base_inputs,_=wage_input(config['points'][0]);guards=[]
            def reject(name,call):
                try:call()
                except (ValueError,TypeError):guards.append({'test':name,'wrong_input_rejected':True});return
                raise AssertionError('negative guard accepted '+name)
            reject('less_than20_grid',lambda:require_grid(np.array([-2.,5.]),np.linspace(0,10,20),np.array([.8,1.3])))
            reject('double_tax_wage_mismatch',lambda:boot.Temp31NetWageInputs(base_inputs.r_a,base_inputs.r_b,base_inputs.wages*.95,base_inputs.labor_weights,base_inputs.wage_record,0,base_inputs.expected_context_id,('A','B')))
            bad_record=debug.WageRoundRecord(1,debug.INITIAL_DEFAULT_UNPROVEN,(19.,19.),('A','B'),base_inputs.expected_context_id)
            reject('unproven_wage_source',lambda:debug.prepare_proposed_consumers(bad_record))
            reject('source_context_mismatch',lambda:boot.Temp31NetWageInputs(base_inputs.r_a,base_inputs.r_b,base_inputs.wages,base_inputs.labor_weights,base_inputs.wage_record,0,'WRONG_CONTEXT',('A','B')))
            reject('warm_start',lambda:require_fresh('OTHER_POINT','D00',False,True))
            reject('KFE_before_HJB_converged',lambda:require_kfe_gate(False,.1))
            for name in ('temp31_netwage_hjb','temp31_netwage_policy','temp31_netwage_economics'):
                tree=ast.parse(Path(short[name].__file__).read_bytes().decode());assert not any(isinstance(n,ast.Attribute) and n.attr in ('tau','migration_costs') for n in ast.walk(tree))
            assert counts['initializer_calls']==counts['hjb_calls']==counts['kfe_calls']==0
            emit('all_price_wage_and_negative_guard_preflight',point=point_id,passed=True,witnesses=witnesses,negative_guards=guards,observed_model_calls=dict(counts),no_extra_HJB_KFE_calls=True)
        inputs,witness=wage_input(point);expected_wage=float(inputs.wages[0]);emit('point_wage_input',**witness,rah=point['rah'],rb=point['rb'])
        stage='GRID_AND_INITIALIZER'
        params=contracts.EconomicParams(**config['economic_params'])
        grid=hjb.Temp31NetWageHJBGrid(np.linspace(-2,5,20),np.linspace(0,10,20),np.array([.8,1.3]),np.array([[-1/3,1/3],[1/3,-1/3]]))
        require_grid(grid.b,grid.a,grid.z)
        value,labor=boot.temp31_netwage_initial_arrays({'rah':point['rah'],'rb':point['rb'],'rb_gap':.07,'Tt':.1},grid,params,inputs)
        require_fresh(point_id,point_id,True,False)
        assert value.shape==labor.shape==(20,20,2) and np.isfinite(value).all() and np.isfinite(labor).all() and counts['initializer_calls']==1 and counts['root_cells']==800
        initial_consumption=expected_wage*grid.z[None,None,:]*labor+grid.b[:,None,None]*(point['rb']+np.where(grid.b[:,None,None]<0,.07,0))+.1
        assert np.isfinite(initial_consumption).all() and (initial_consumption>0).all()
        initial={'consumption_shape':list(initial_consumption.shape),'consumption_min':float(initial_consumption.min()),'consumption_max':float(initial_consumption.max()),'consumption_F_sha256':array_hash(initial_consumption),'shape':[20,20,2],'states':800,'value_min':float(value.min()),'value_max':float(value.max()),'labor_min':float(labor.min()),'labor_max':float(labor.max()),
                 'finite':True,'value_F_float64_sha256':array_hash(value),'labor_F_float64_sha256':array_hash(labor),'fresh_for_point':point_id,'warm_start':False}
        emit('initialization',point=point_id,**initial,observed_counts=dict(counts))
        stage='REAL_HJB';sys.settrace(trace_calls)
        with warnings.catch_warnings(record=True) as records:
            warnings.simplefilter('always')
            result=hjb.solve_temp31_netwage_hjb(grid,params,inputs,value,labor,.1,.07,hjb.Temp31NetWageHJBNumerics(**config['numerics']))
        sys.settrace(None)
        assert result.iterations==counts['hjb_iterations']==len(trajectory)<=100 and counts['hjb_policy_cells']==800*result.iterations and counts['hjb_linear_solves']==result.iterations
        assert counts['operator_assemblies']==result.iterations+1 and np.array_equal(result.initial_value,value)
        finite={name:bool(np.isfinite(getattr(result,name)).all()) for name in ('value','initial_value','consumption','labor','transfer','adjustment_cost','effective_illiquid_return','mu_a','mu_b','utility')}
        assert all(finite.values())
        post=result.post_convergence_operator.full;metrics=matrix_metrics(result.operator.full);post_metrics=matrix_metrics(post)
        assert metrics['finite'] and post_metrics['finite'] and post.shape==(800,800)
        residual=params.rho*result.value.ravel(order='F')-result.utility.ravel(order='F')-result.operator.full@result.value.ravel(order='F')
        implicit=(last['old']-result.value).ravel(order='F')/1000.
        homecrit_max=max(row['operator_row_sum_abs_max'] for row in trajectory);homecrit_violation=homecrit_max>.01
        hjb_summary={'converged':bool(result.converged),'iterations':int(result.iterations),'convergence_statistic':float(result.convergence_statistic),'finite_return_fields':finite,
            'iteration_operator':metrics,'post_convergence_operator':post_metrics,'max_observed_iteration_row_sum_abs':homecrit_max,'MATLAB_homecrit':.01,
            'observed_homecrit_violation':homecrit_violation,'homecrit_guard_internal':'ABSENT_UNCHANGED_EXTERNAL_READONLY_OBSERVATION',
            'source_parity':'SOURCE_PARITY_BLOCKED' if homecrit_violation else 'PARITY_UNCERTIFIED_RAW_MATLAB_NOT_LOCALLY_VERIFIED',
            'stale_last_policy_residual':norm(residual),'implicit_identity_error':norm(residual-implicit),'full_nonlinear_Bellman_residual':'NOT_EVALUATED',
            'warnings':[{'type':type(w.message).__name__,'message':str(w.message)} for w in records]}
        emit('hjb_result',point=point_id,**hjb_summary,observed_counts=dict(counts))
        archive=EV/f'LOCAL_ONLY_{point_id}_true_arrays_and_rates.npz'
        with archive.open('xb') as handle:
            np.savez_compressed(handle,initial_value=value,initial_labor=labor,value=result.value,consumption=result.consumption,labor=result.labor,mu_a=result.mu_a,mu_b=result.mu_b,utility=result.utility,
              iteration_G_data=result.operator.full.data,iteration_G_indices=result.operator.full.indices,iteration_G_indptr=result.operator.full.indptr,
              post_G_data=post.data,post_G_indices=post.indices,post_G_indptr=post.indptr,
              b_backward=last['b_backward'],b_forward=last['b_forward'],a_backward=last['a_backward'],a_forward=last['a_forward'])
        archive_id={'task_relative_path':archive.relative_to(REPORT).as_posix(),'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'LOCAL_ONLY':True,'observed_new_point_not_historical_tinygrid':True}
        kfe_summary={'status':'NOT_EXECUTED_HJB_NOT_CONVERGED','source_method_executed':False,'At':None,'Bt':None,'Lt':None,'Ct':None,'a_mass20':None,'b_mass20':None}
        classification='HJB_NOT_CONVERGED';fatal=False
        if result.converged and result.convergence_statistic<1e-7:
            stage='REAL_KFE';require_kfe_gate(result.converged,result.convergence_statistic)
            before_post=matrix_hash(post)
            try:
                with warnings.catch_warnings(record=True) as kfe_warnings:
                    warnings.simplefilter('always')
                    distribution=kfe.solve_matlab_faithful_stationary_kfe(post,shape=(20,20,2),db=7/19,da=10/19)
                assert matrix_hash(post)==before_post and norm((distribution.original_operator-post).data)==0
                g=distribution.density;weight=(7/19)*(10/19);mass=g*weight
                a_mass=mass.sum(axis=(0,2));b_mass=mass.sum(axis=(1,2))
                total=float(mass.sum());negative_mass=float(np.maximum(-g,0).sum()*weight)
                original_residual=post.T@distribution.density_vector
                stationary=norm(original_residual)
                contaminated=norm(distribution.contaminated_matrix@distribution.raw_solve_vector-distribution.rhs)
                At=float((g*grid.a[None,:,None]).sum()*weight);Bt=float((g*grid.b[:,None,None]).sum()*weight)
                Lt=float((g*result.labor*grid.z[None,None,:]).sum()*weight);Ct=float((g*result.consumption).sum()*weight)
                assert all(np.isfinite(x) for x in (total,negative_mass,stationary,contaminated,At,Bt,Lt,Ct)) and np.isfinite(g).all()
                modes=np.flatnonzero(a_mass==a_mass.max()).tolist()
                certification={'density_finite':True,'total_probability_abs_error_le_1e8':abs(total-1)<=1e-8,'negative_probability_mass_le_1e8':negative_mass<=1e-8,
                  'post_stationary_residual_le_1e7':stationary<=1e-7,'contaminated_raw_system_residual_le_1e7':contaminated<=1e-7}
                interior={'At_strict_0_10':0<At<10,'a_internal_mass_ge_point10':float(a_mass[1:-1].sum())>=.10,
                  'a_lower_mass_le_point50':float(a_mass[0])<=.50,'a_upper_mass_le_point50':float(a_mass[-1])<=.50,
                  'a_modal_indices_not_only_endpoints':any(0<index<19 for index in modes),'b_internal_mass_ge_point05':float(b_mass[1:-1].sum())>=.05}
                kfe_summary={'status':'SOURCE_METHOD_COMPUTED' if all(certification.values()) else 'SOURCE_KFE_COMPUTED_WITH_STATIONARITY_WARNING','source_method_executed':True,'At':At,'Bt':Bt,'Lt':Lt,'Ct':Ct,
                  'original_residual_at_pin_row295':float(original_residual[295]),'non_pin799_residual_max':norm(np.delete(original_residual,295)),
                  'residual_argmax_index0':int(np.argmax(np.abs(original_residual))),'normalized_contaminated_equation_residual':norm(distribution.contaminated_matrix@distribution.density_vector-distribution.rhs/distribution.normalization_factor),
                  'SOURCE_METHOD_INTERIOR_CANDIDATE':bool(all(interior.values())),'STRICT_ECONOMIC_STATIONARITY_CERTIFIED':bool(all(certification.values())),
                  'B_UPPER_BOUNDARY_WARNING':bool(b_mass[-1]>=.50),'b_mode_indices0':np.flatnonzero(b_mass==b_mass.max()).tolist(),
                  'b_mode_asset_positions':[float(grid.b[i]) for i in np.flatnonzero(b_mass==b_mass.max())],
                  'a_mass20':a_mass.tolist(),'b_mass20':b_mass.tolist(),'total_probability':total,'negative_probability_mass':negative_mass,'negative_density_cells':int((g<0).sum()),
                  'density_min':float(g.min()),'density_max':float(g.max()),'a_lower_mass':float(a_mass[0]),'a_upper_mass':float(a_mass[-1]),'a_internal_mass':float(a_mass[1:-1].sum()),
                  'b_lower_mass':float(b_mass[0]),'b_upper_mass':float(b_mass[-1]),'b_internal_mass':float(b_mass[1:-1].sum()),'a_mode_indices0':modes,'a_mode_asset_positions':[float(grid.a[i]) for i in modes],
                  'At_distance_from_lower':At,'At_distance_from_upper':10-At,'stationary_residual':stationary,'contaminated_raw_system_residual':contaminated,
                  'source_raw_residual_inf':float(distribution.raw_residual_inf),'contaminated_row_index0':int(distribution.contaminated_row_index),'rhs_at_contaminated_row':float(distribution.rhs[distribution.contaminated_row_index]),
                  'normalization_factor':float(distribution.normalization_factor),'cell_weight':float(distribution.cell_weight),'certification_tests':certification,'interior_tests':interior,
                  'warnings':[{'type':type(w.message).__name__,'message':str(w.message)} for w in kfe_warnings],'signed_density_unmodified':True,'source_post_operator_passed_directly_and_unchanged':True}
                classification=kfe_summary['status']
                extra=EV/f'LOCAL_ONLY_{point_id}_true_KFE_density.npz'
                with extra.open('xb') as handle:np.savez_compressed(handle,raw=distribution.raw_solve_vector,density=g,a_mass=a_mass,b_mass=b_mass)
                kfe_summary['LOCAL_ONLY_archive']={'task_relative_path':extra.relative_to(REPORT).as_posix(),'bytes':extra.stat().st_size,'sha256':hashlib.sha256(extra.read_bytes()).hexdigest()}
            except BaseException as exc:
                traceback.print_exc();classification='SOURCE_KFE_NUMERICAL_ERROR'
                kfe_summary={'status':'SOURCE_KFE_NUMERICAL_ERROR','source_method_executed':False,'error_type':type(exc).__name__,'error':str(exc),'At':None,'Bt':None,'Lt':None,'Ct':None,'a_mass20':None,'b_mass20':None,'no_retry':True}
                if isinstance(exc,(MemoryError,PermissionError,OSError,AssertionError)):fatal=True
            emit('kfe_result',point=point_id,**kfe_summary,observed_counts=dict(counts))
        if homecrit_violation:hjb_summary['source_parity']='SOURCE_PARITY_WARNING_OR_BLOCKED'
        sys.setprofile(None);sys.settrace(None)
        output={'point':point_id,'prices':point,'classification':classification,'fatal_to_task':fatal,'wage_provenance':witness,'initialization':initial,
            'HJB_SOURCE_CONVERGED':bool(result.converged),'MATLAB_KFE_METHOD_EXECUTED':bool(kfe_summary.get('source_method_executed',False)) if result.converged else 'NOT_RUN',
            'SOURCE_METHOD_INTERIOR_CANDIDATE':kfe_summary.get('SOURCE_METHOD_INTERIOR_CANDIDATE','NOT_EVALUATED'),
            'STRICT_ECONOMIC_STATIONARITY_CERTIFIED':kfe_summary.get('STRICT_ECONOMIC_STATIONARITY_CERTIFIED','NOT_EVALUATED'),
            'HJB':hjb_summary,'KFE':kfe_summary,'observed_counts':counts,'LOCAL_ONLY_hjb_archive':archive_id,
            'MATLAB_RAW_LOCAL_VERIFICATION':'NOT_AVAILABLE','firm_GE_IRF_outer_31province_data_calls':0,'source_or_economic_parameter_changes':0}
        emit('point_result',**output)
        return 1 if fatal else 0
    except BaseException as exc:
        sys.setprofile(None);sys.settrace(None);traceback.print_exc()
        label='WAGE_PROVENANCE_GATE_BLOCKED' if stage=='WAGE_PROVENANCE_GATE' else 'EXECUTION_BLOCKED'
        emit('point_result',point=point_id,classification=label,fatal_to_task=True,failed_stage=stage,error_type=type(exc).__name__,error=str(exc),observed_counts=counts,
             HJB={'status':'NOT_COMPLETED_OR_NOT_EXECUTED'},KFE={'status':'NOT_EXECUTED'},firm_GE_IRF_outer_31province_data_calls=0)
        return 1

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--point',choices=tuple(p[0] for p in PRICES),required=True)
    raise SystemExit(run(parser.parse_args().point))
