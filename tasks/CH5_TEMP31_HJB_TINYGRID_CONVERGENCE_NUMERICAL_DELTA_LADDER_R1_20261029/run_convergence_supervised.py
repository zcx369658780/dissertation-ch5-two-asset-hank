"""One fixed arm per command; authenticated prior Job/timeout helper, no retry."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,os
from pathlib import Path
import subprocess,sys,time
from datetime import datetime,timezone
REPORT=Path(__file__).resolve().parent;WORK=REPORT.parents[1];EV=REPORT/'evidence'
ENTRY='validators/multi_province/temp31_hjb_convergence_delta_ladder_isolated.py'
THREAD_KEYS=('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS','BLIS_NUM_THREADS')
def read(path):return json.loads(path.read_text(encoding='utf-8'))
def write(path,data):
    with path.open('x',encoding='utf-8',newline='\n') as f:json.dump(data,f,indent=2);f.write('\n')
def sha(raw):return hashlib.sha256(raw).hexdigest()
def old_supervisor(identity):
    row=identity['authenticated_previous_helpers'][1];path=WORK/row['path'];raw=path.read_bytes()
    assert sha(raw)==row['sha256'] and len(raw)==row['bytes']
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==row['git_blob']
    spec=importlib.util.spec_from_file_location('temp31_previous_authenticated_supervisor',path)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
    return module
def main(arm,source_root):
    number={'A':1,'B':2,'C':3}[arm];budget_path=REPORT/'test_command_budget.json';budget=read(budget_path)
    assert budget['commands_started']==number-1 and not budget.get('stop_ladder',False),'STOP_ARM_ORDER_OR_CLOSED_BUDGET'
    if number>1:
        previous='ABC'[number-2];prior=read(EV/f'arm_{previous}_receipt.json')
        assert prior['transition_outcome']=='NOT_CONVERGED_FINITE' and prior['exit_code']==0 and not prior['timed_out']
        assert prior['final_event']['actual_iterations']==80 and prior['final_event']['result_converged'] is False
        assert prior['final_event']['implicit_consistent'] and all(prior['final_event']['finite_return_arrays'].values())
    identity=read(REPORT/'source_identity.json');old=old_supervisor(identity);tuning=read(REPORT/'numerical_tuning_contract.json')
    command=[sys.executable,'-B',ENTRY,'--arm',arm,'--source-root',str(source_root)]
    claim={'arm':arm,'command_number':number,'command':['python','-B',*command[2:]],'working_directory':'<ISOLATED_CANDIDATE_ROOT>',
      'delta':tuning['arms'][arm]['delta'],'max_iterations':80,'hard_timeout_seconds':30,'science_child_processes':1,'retry_allowed':False,
      'source_commit':identity['source']['commit'],'entry_sha256':sha((WORK/ENTRY).read_bytes()),
      'supervisor_sha256':sha(Path(__file__).read_bytes()),'tuning_contract_sha256':sha((REPORT/'numerical_tuning_contract.json').read_bytes()),
      'previous_supervisor_git_blob':identity['authenticated_previous_helpers'][1]['git_blob'],
      'declared_at_utc':datetime.now(timezone.utc).isoformat(),
      'call_limits':{'initializer_batches':1,'root_cells':8,'hjb_driver_calls':1,'hjb_iterations':80,'hjb_policy_cells':640,'operator_assemblies':81,'linear_solves':80,'KFE_GE_IRF':0}}
    write(EV/f'arm_{arm}_claim.json',claim)
    budget['commands_started']=number
    budget_path.write_text(json.dumps(budget,indent=2)+'\n',encoding='utf-8',newline='\n')
    env=dict(os.environ,**{key:'1' for key in THREAD_KEYS},PYTHONDONTWRITEBYTECODE='1',PYTHONNOUSERSITE='1')
    env.pop('PYTHONPATH',None)
    remaining_total=90-budget['total_elapsed_seconds'];assert remaining_total>0
    start=time.monotonic();process=subprocess.Popen(command,cwd=WORK,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env)
    timed_out=False;close_job=None;memory={'status':'MEMORY_HARD_LIMIT_UNAVAILABLE'};pre_import_block=False
    try:
        _,memory,close_job=old.restrict_memory(process)
        if memory['status']!='PROCESS_MEMORY_HARD_LIMIT_ENFORCED':
            pre_import_block=True;process.kill();stdout,stderr=process.communicate()
        else:
            stdout,stderr=process.communicate(input=b'GO\n',timeout=max(.001,min(30,remaining_total)-(time.monotonic()-start)))
    except subprocess.TimeoutExpired:
        timed_out=True;process.kill();stdout,stderr=process.communicate()
    except BaseException:
        process.kill();process.communicate();raise
    finally:
        if close_job is not None:memory['observed_peak_process_committed_bytes']=close_job()
    elapsed=time.monotonic()-start
    (EV/f'LOCAL_ONLY_arm_{arm}_stdout_raw.txt').write_bytes(stdout);(EV/f'LOCAL_ONLY_arm_{arm}_stderr_raw.txt').write_bytes(stderr)
    out,changes_out=old.redact(stdout);err,changes_err=old.redact(stderr)
    (EV/f'arm_{arm}_stdout_public.txt').write_bytes(out);(EV/f'arm_{arm}_stderr_public.txt').write_bytes(err)
    events=[json.loads(line) for line in out.decode('utf-8','replace').splitlines() if line.startswith('{"event":')]
    final=next((e for e in reversed(events) if e['event']=='arm_result'),None)
    trajectory=[{k:v for k,v in e.items() if k not in ['event','arm','observed_counts']} for e in events if e['event']=='iteration']
    success_exit=process.returncode==0 and not timed_out and not pre_import_block and final is not None
    outcome=final['outcome'] if final is not None else 'STOP_RESULT_NOT_CAPTURED'
    if timed_out:outcome='STOP_HARD_TIMEOUT'
    elif pre_import_block:outcome='STOP_MEMORY_LIMIT_UNAVAILABLE_BEFORE_IMPORT'
    elif not success_exit and outcome in ('NOT_CONVERGED_FINITE','PASS_BOUNDED_NUMERICAL_FIXED_POINT__STALE_POLICY_RESIDUAL_CHECKED'):
        outcome='STOP_NONZERO_EXIT'
    if success_exit and number>1:
        first=read(EV/'arm_A_receipt.json')['final_event']['original_initialization_hashes']
        if first!=final['original_initialization_hashes']:outcome='STOP_ORIGINAL_INITIALIZATION_IDENTITY_DRIFT'
    counts=final.get('observed_counts',{}) if final else {}
    for key,value in counts.items():budget['total_observed_calls'][key]=budget['total_observed_calls'].get(key,0)+value
    budget['total_elapsed_seconds']+=elapsed;budget['arms'][arm]=outcome
    assert budget['total_observed_calls'].get('hjb_driver_calls',0)<=3 and budget['total_observed_calls'].get('hjb_iteration_entries',0)<=240 and budget['total_observed_calls'].get('hjb_policy_cells',0)<=1920
    stop=outcome!='NOT_CONVERGED_FINITE' or arm=='C'
    if stop:
        budget['stop_ladder']=True
        for skipped in 'ABC'[number:]:budget['arms'][skipped]='NOT_EXECUTED_AFTER_'+arm+'_'+('BOUNDED_PASS' if outcome.startswith('PASS_BOUNDED') else 'HARD_STOP')
    budget_path.write_text(json.dumps(budget,indent=2)+'\n',encoding='utf-8',newline='\n')
    redaction={'transformation':'exact workspace/runtime prefix replacement; raw originals retained LOCAL_ONLY',
      'stdout':{'raw_bytes':len(stdout),'raw_sha256':sha(stdout),'public_bytes':len(out),'public_sha256':sha(out),'changes':changes_out},
      'stderr':{'raw_bytes':len(stderr),'raw_sha256':sha(stderr),'public_bytes':len(err),'public_sha256':sha(err),'changes':changes_err}}
    write(EV/f'arm_{arm}_redaction_record.json',redaction)
    write(EV/f'arm_{arm}_trajectory.json',{'arm':arm,'delta':tuning['arms'][arm]['delta'],'completed_iterations':len(trajectory),'trajectory':trajectory,
      'full_nonlinear_Bellman_residual':'NOT_EVALUATED_NO_POLICY_REOPTIMIZATION'})
    receipt={'arm':arm,'command_number':number,'delta':tuning['arms'][arm]['delta'],'max_iterations':80,'exit_code':process.returncode,
      'timed_out':timed_out,'hard_timeout_seconds':30,'elapsed_seconds':elapsed,'memory_limit':memory,
      'transition_outcome':outcome,'final_event':final,'completed_iteration_metrics':len(trajectory),'stop_ladder':stop,
      'redaction':redaction,'retries':0,'science_child_processes':1,
      'counter_capture':'actual final profile counters' if final else 'FINAL_COUNTS_NOT_CAPTURED; progress events are lower bounds only'}
    write(EV/f'arm_{arm}_receipt.json',receipt)
    print(json.dumps({'arm':arm,'transition_outcome':outcome,'exit_code':process.returncode,'elapsed_seconds':elapsed,
      'timed_out':timed_out,'final_event':final,'completed_iteration_metrics':len(trajectory),'stop_ladder':stop,'memory_limit':memory}),flush=True)
    if err:print(err.decode('utf-8','replace'),file=sys.stderr)
    return 0 if success_exit and outcome in ('NOT_CONVERGED_FINITE','PASS_BOUNDED_NUMERICAL_FIXED_POINT__STALE_POLICY_RESIDUAL_CHECKED') else 1
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--arm',choices=('A','B','C'),required=True)
    parser.add_argument('--source-root',type=Path,default=Path('src'));args=parser.parse_args()
    raise SystemExit(main(args.arm,args.source_root))
