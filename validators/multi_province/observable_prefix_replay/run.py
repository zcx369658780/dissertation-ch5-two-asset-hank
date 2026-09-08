"""One original annual-worker invocation with observational dispatch wrappers."""
import dataclasses
import inspect
import io
import contextlib
import json
import os
from pathlib import Path
import platform
import sys
import time
import traceback

ROOT=Path(os.environ.get("CH5_OBSERVATION_RUNTIME", Path(__file__).resolve().parents[3]))


def run(root):
    # Imports are delayed: importing this observer cannot start science.
    sys.path[:0]=[str(ROOT),str(ROOT/'src')]
    import numpy as np
    import scipy
    from validators.multi_province import mp4c_python_annual_production as worker
    import ch5_two_asset_hank.multi_province.stationary_runtime as runtime
    import ch5_two_asset_hank.multi_province.one_turn as one
    import exports.matlab_faithful_two_asset_ha as faithful
    from observer import Store,Budget,PrefixLimit,ObservationTimeout,delegate

    root=Path(root);store=Store(root/'capture');budget=Budget();phase='prelaunch';step=0;province=-1
    current={};completed=set();restores=[];in_brent=False
    original_input=Path(r'D:\ProjectTemp\ch5-mp4c-owner-a-corrected-2009-2022-8worker-20260902-001\year_2018\calendar_2018_matlab_runtime_cache_input.json')
    cache=Path('D:/MatlabProgram/2023年12月2日 多省份神经网络HANK/数据估计结果_1000_100_0.mat')
    def patch(module,name,value):
        old=getattr(module,name);restores.append((module,name,old));setattr(module,name,value);return old
    def save(name,obj):return store.save(name,obj)
    def callname(suffix):return f'call_{budget.call:04d}/{suffix}'
    def turnname(suffix):return f'turn_{step:04d}/{suffix}'

    online=worker.run_online_stationary
    def observed_online(inputs):
        original_batch=inputs.household_solver
        def batch(snapshot,iteration):
            nonlocal step,province,phase
            step=iteration;province=-1;budget.enter('outer_entry');phase='common_entering'
            frame=inspect.currentframe().f_back
            tkn=frame.f_locals['tkn_ratio']
            save(turnname('common_entering'),{'iteration':step,'state':snapshot,'tKN':tkn,
                'params':inputs.params,'phi_entering_callback':inputs.phi_destination_origin,
                'migration_wedges':inputs.migration_wedge_destination_origin,
                'reg_threshold':inputs.reg_threshold,'max_iterations_native':inputs.max_iterations,
                'steady_state':inputs.steady_state,'source_identity':'../../preflight.json'})
            result=original_batch(snapshot,iteration)
            save(turnname('household_batch_return'),result)
            return result
        # Only replace the dispatch callable; all scientific fields retain their object identity.
        observed=dataclasses.replace(inputs,household_solver=batch)
        for f in dataclasses.fields(inputs):
            if f.name!='household_solver':assert getattr(observed,f.name) is getattr(inputs,f.name)
        return online(observed)
    patch(worker,'run_online_stationary',observed_online)

    initial=worker.anchor._source_initial_arrays
    def initializer(state,grid,params):
        nonlocal province,phase,current
        budget.enter('native_initialization');province+=1;phase='native_initialization';current={'step':step,'province_index_0':province,'province':state['name'],'call':budget.call}
        save(callname('entry'),{'context':current,'state':state,'grid':grid,'params':params,'counter_before_initializer':dict(budget.counts)})
        if province==0:
            # The worker recomputed phi before calling the original initializer.
            frame=inspect.currentframe().f_back
            save(turnname('phi_before_first_household'),{'phi':frame.f_locals['phi'],'context':current})
        result=initial(state,grid,params)
        save(callname('native_initialization_return'),{'V0':result[0],'l0':result[1],'counts':dict(budget.counts)})
        return result
    patch(worker.anchor,'_source_initial_arrays',initializer)

    labor=worker.anchor._source_labor_root
    residual_codes={c for c in labor.__code__.co_consts if inspect.iscode(c) and c.co_name=='residual'}
    def profile(frame,event,arg):
        if event=='call' and frame.f_code in residual_codes:
            budget.counts['root_residual']+=1
            budget.counts['root_brentq_residual' if in_brent else 'root_bracketing_residual']+=1
    def root_entry(*args,**kwargs):
        budget.enter('labor_root');old_profile=sys.getprofile();sys.setprofile(profile)
        try:return labor(*args,**kwargs)
        finally:sys.setprofile(old_profile)
    patch(worker.anchor,'_source_labor_root',root_entry)
    brent=worker.anchor.brentq
    def brent_entry(*args,**kwargs):
        nonlocal in_brent
        budget.enter('brentq');in_brent=True
        try:return brent(*args,**kwargs)
        finally:in_brent=False
    patch(worker.anchor,'brentq',brent_entry)

    original_post=worker.anchor.solve_matlab_source_postloop_household
    defaults=original_post.__kwdefaults__
    def hjb(*args,**kwargs):
        nonlocal phase
        budget.enter('HJB');phase='HJB'
        save(callname('hjb_entry'),{'context':current,'numerics':args[7],'inputs':args[2],'counts':dict(budget.counts)})
        result=defaults['hjb_solver'](*args,**kwargs)
        budget.counts['HJB_returns']+=1
        save(callname('hjb_return_before_kfe'),result)
        phase='HJB_RETURN_PERSISTED'
        return result
    def kfe(*args,**kwargs):
        nonlocal phase
        budget.enter('KFE');phase='KFE'
        save(callname('kfe_entry'),{'context':current,'kwargs':kwargs,'counts':dict(budget.counts)})
        result=defaults['kfe_solver'](*args,**kwargs)
        budget.counts['KFE_returns']+=1
        save(callname('kfe_return'),result)
        return result
    def household(*args,**kwargs):
        nonlocal phase
        budget.enter('household');phase='household'
        assert not kwargs, 'original annual worker passes only positional household arguments'
        result=original_post(*args,**kwargs,hjb_solver=hjb,kfe_solver=kfe)
        save(callname('household_return'),{'context':current,'aggregates':result.aggregates,
             'hjb_converged':result.hjb.converged,'hjb_iterations':result.hjb.iterations,
             'hjb_statistic':result.hjb.convergence_statistic,'counts':dict(budget.counts)})
        phase='HOUSEHOLD_RETURN_PERSISTED'
        budget.after_household()
        return result
    patch(worker.anchor,'solve_matlab_source_postloop_household',household)
    solve=faithful.linalg.spsolve
    def direct(*args,**kwargs):
        key='HJB_direct_solve' if phase=='HJB' else 'KFE_direct_solve' if phase=='KFE' else None
        if key is None:raise RuntimeError('unexpected direct-solver entry outside original HJB/KFE')
        budget.enter(key)
        if phase=='KFE':save(callname('kfe_direct_input'),{'matrix':args[0],'rhs':args[1]})
        result=solve(*args,**kwargs)
        if phase=='KFE':save(callname('kfe_direct_return'),{'raw':result,'counts':dict(budget.counts)})
        return result
    patch(faithful.linalg,'spsolve',direct)

    def before_turn(inputs):
        nonlocal phase
        budget.enter('one_turn');phase='one_turn';save(turnname('one_turn_input'),inputs)
    def after_turn(result,*args,**kwargs):
        budget.counts['one_turn_returns']+=1;save(turnname('one_turn_return'),result)
    patch(runtime,'run_source_faithful_one_turn',delegate(runtime.run_source_faithful_one_turn,before_turn,after_turn))
    def firm_before(province_state,kt_supply,lt_supply,params):
        budget.enter('firm');idx=(budget.counts['firm']-1)%31
        save(turnname(f'firm_{idx:02d}_input'),{'province':province_state,'kt_supply':kt_supply,'lt_supply':lt_supply,'params':params})
    def firm_after(result,*args,**kwargs):
        idx=(budget.counts['firm']-1)%31;save(turnname(f'firm_{idx:02d}_return'),result)
    patch(one,'evaluate_firm',delegate(one.evaluate_firm,firm_before,firm_after))
    for name in ('allocate_productive_capital','reconstruct_migration_labor','composite_household_wages'):
        def before(*args,_name=name,**kwargs):save(turnname(_name+'_input'),{'args':args,'kwargs':kwargs})
        def after(result,*args,_name=name,**kwargs):save(turnname(_name+'_return'),result)
        patch(one,name,delegate(getattr(one,name),before,after))
    def diag_before(*args,**kwargs):
        nonlocal phase
        budget.enter('controller_decision');phase='controller';save(turnname('diagnostics_input'),{'args':args,'kwargs':kwargs})
    def diag_after(result,*args,**kwargs):
        save(turnname('diagnostics_return'),{'native_tuple':result,
            'max_nk':float(np.max(result[0])),'max_nk_ties_0':np.flatnonzero(result[0]==np.max(result[0])),
            'max_yt':float(np.max(result[1])),'max_yt_ties_0':np.flatnonzero(result[1]==np.max(result[1]))})
    patch(runtime,'_diagnostics',delegate(runtime._diagnostics,diag_before,diag_after))
    def adapt_before(*args,**kwargs):
        budget.counts['adaptive_blocks']+=1;save(turnname('adapt_before'),{'args':args,'kwargs':kwargs})
    def adapt_after(result,*args,**kwargs):save(turnname('adapt_return'),{'next_states':result[0],'actual_actions':result[1]})
    patch(runtime,'_adapt',delegate(runtime._adapt,adapt_before,adapt_after))
    freeze=runtime._freeze_state
    def freeze_observer(*args,**kwargs):
        result=freeze(*args,**kwargs)
        loc=inspect.currentframe().f_back.f_locals
        record=loc.get('record');history=loc.get('history')
        if record is not None and history and history[-1] is record and record.iteration not in completed:
            completed.add(record.iteration);budget.counts['completed_turns']+=1
            save(turnname('completed_record'),record)
            print(json.dumps({'completed_turn':record.iteration,'calls':budget.call,'counts':budget.counts}),flush=True)
        return result
    patch(runtime,'_freeze_state',freeze_observer)

    config=io.StringIO()
    with contextlib.redirect_stdout(config):np.show_config()
    save('environment',{'pid':os.getpid(),'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,
        'platform':platform.platform(),'blas':config.getvalue(),'threads':{k:os.environ.get(k) for k in ('OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS','NUMEXPR_NUM_THREADS')}})
    terminal='PRELAUNCH_BLOCKED';error=None;started=time.monotonic()
    try:
        status=worker.run_year(original_input,cache,root/'worker_outputs')
        terminal='ORIGINAL_EARLY_CONVERGENCE' if status==0 else 'ORIGINAL_NORMAL_FAILURE'
    except PrefixLimit as exc:terminal='PREFIX_LIMIT';error={'type':type(exc).__name__,'message':str(exc),'traceback':traceback.format_exc()}
    except ObservationTimeout as exc:terminal='TIMEOUT';error={'type':type(exc).__name__,'message':str(exc),'traceback':traceback.format_exc()}
    except BaseException as exc:
        terminal='ORIGINAL_EXCEPTION' if budget.counts['native_initialization'] else 'PRELAUNCH_BLOCKED'
        error={'type':type(exc).__name__,'message':str(exc),'traceback':traceback.format_exc()}
    finally:
        save('terminal',{'terminal':terminal,'error':error,'current':current,'phase':phase,'last_durable_stage':store.last,
            'counts':budget.counts,'per_call':budget.per_call,'wall_seconds':time.monotonic()-started,
            'scientific_seconds':time.monotonic()-budget.start if budget.start else 0.,'scientific_processes':1,
            'scientific_restarts':0,'Results_eligible':False})
        for module,name,old in reversed(restores):setattr(module,name,old)
        store.close()
    print(json.dumps({'terminal':terminal,'counts':budget.counts,'call':budget.call}),flush=True)


if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8');run(Path(sys.argv[1]))
