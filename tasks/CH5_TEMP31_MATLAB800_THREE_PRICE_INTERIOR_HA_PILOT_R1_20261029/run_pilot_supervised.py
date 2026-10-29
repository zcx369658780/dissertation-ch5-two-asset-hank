"""Exactly one bounded real scientific child for each frozen price point."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,os
from pathlib import Path
import subprocess,sys,time
from datetime import datetime,timezone
REPORT=Path(__file__).resolve().parent;WORK=REPORT.parents[1];EV=REPORT/'evidence'
ENTRY='validators/multi_province/temp31_matlab800_three_price_ha_pilot_isolated.py'
THREAD_KEYS=('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS','BLIS_NUM_THREADS')
def read(path):return json.loads(path.read_text(encoding='utf-8'))
def write(path,data):
    with path.open('x',encoding='utf-8',newline='\n') as f:json.dump(data,f,indent=2);f.write('\n')
def sha(raw):return hashlib.sha256(raw).hexdigest()
def authenticate_helper(identity):
    row=identity['authenticated_supervisor_helper'];path=WORK/row['path'];raw=path.read_bytes()
    assert sha(raw)==row['sha256'] and len(raw)==row['bytes'] and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==row['git_blob']
    spec=importlib.util.spec_from_file_location('temp31_matlab800_authentic_supervisor',path);module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
    return module
def main(point_id):
    index=int(point_id[1:]);budget_path=REPORT/'budget.json';budget=read(budget_path);config=read(REPORT/'point_grid.json')
    assert budget['point_commands_started']==index and not budget['task_stopped'],'STOP_POINT_ORDER_OR_CLOSED_BUDGET'
    if index:
        prior=read(EV/f'P{index-1}_receipt.json');assert prior['exit_code']==0 and not prior['timed_out'] and not prior['fatal_to_task']
        assert read(EV/'global_wage_and_negative_guard_preflight.json')['passed']
    identity=read(REPORT/'source_identity.json');old=authenticate_helper(identity)
    command=[sys.executable,'-B',ENTRY,'--point',point_id]
    point=config['points'][index];assert point['id']==point_id
    write(EV/f'{point_id}_claim.json',{'point':point_id,'prices':point,'command_number':index+1,'command':['python','-B',*command[2:]],'working_directory':'<ISOLATED_CANDIDATE_ROOT>',
      'claimed_at_utc':datetime.now(timezone.utc).isoformat(),'hard_timeout_seconds':180,'max_science_processes':1,'process_committed_memory_max':1073741824,
      'source_commit':identity['source']['commit'],'entry_sha256':sha((WORK/ENTRY).read_bytes()),'supervisor_sha256':sha(Path(__file__).read_bytes()),'point_grid_sha256':sha((REPORT/'point_grid.json').read_bytes()),
      'call_limits':{'initializer_calls':1,'root_cells':800,'hjb_calls':1,'hjb_iterations':100,'hjb_policy_cells':80000,'kfe_calls':1},
      'retry_allowed':False,'KFE_gate':'real HJB converged True and convergence_statistic<1e-7 only; use unchanged returned post operator'})
    budget['point_commands_started']=index+1
    budget_path.write_text(json.dumps(budget,indent=2)+'\n',encoding='utf-8',newline='\n')
    env=dict(os.environ,**{key:'1' for key in THREAD_KEYS},PYTHONDONTWRITEBYTECODE='1',PYTHONNOUSERSITE='1');env.pop('PYTHONPATH',None)
    start=time.monotonic();process=subprocess.Popen(command,cwd=WORK,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env)
    close_job=None;timed_out=False;memory={'status':'MEMORY_HARD_LIMIT_UNAVAILABLE'};pre_import_block=False
    try:
        _,memory,close_job=old.restrict_memory(process)
        if memory['status']!='PROCESS_MEMORY_HARD_LIMIT_ENFORCED':pre_import_block=True;process.kill();out,err=process.communicate()
        else:out,err=process.communicate(input=b'GO\n',timeout=max(.001,180-(time.monotonic()-start)))
    except subprocess.TimeoutExpired:
        timed_out=True;process.kill();out,err=process.communicate()
    except BaseException:
        process.kill();process.communicate();raise
    finally:
        if close_job is not None:memory['observed_peak_process_committed_bytes']=close_job()
    elapsed=time.monotonic()-start
    (EV/f'LOCAL_ONLY_{point_id}_stdout_raw.txt').write_bytes(out);(EV/f'LOCAL_ONLY_{point_id}_stderr_raw.txt').write_bytes(err)
    public_out,changes_out=old.redact(out);public_err,changes_err=old.redact(err)
    (EV/f'{point_id}_stdout_public.txt').write_bytes(public_out);(EV/f'{point_id}_stderr_public.txt').write_bytes(public_err)
    events=[json.loads(line) for line in public_out.decode('utf-8','replace').splitlines() if line.startswith('{"event":')]
    final=next((event for event in reversed(events) if event['event']=='point_result'),None)
    if point_id=='P0':
        preflight=next((event for event in events if event['event']=='all_price_wage_and_negative_guard_preflight'),None)
        if preflight is not None:write(EV/'global_wage_and_negative_guard_preflight.json',preflight)
    trajectory=[{key:value for key,value in event.items() if key not in ('event','observed_counts')} for event in events if event['event']=='hjb_iteration']
    write(EV/f'{point_id}_iteration_trajectory.json',{'point':point_id,'completed_iteration_metrics':len(trajectory),'trajectory':trajectory,'no_hidden_HJB_rerun':True})
    fatal=timed_out or pre_import_block or process.returncode!=0 or final is None or final.get('fatal_to_task',True)
    classification=final['classification'] if final else 'EXECUTION_BLOCKED'
    counts=final.get('observed_counts') if final else None
    if counts:
        for key,value in counts.items():budget['total_observed_calls'][key]=budget['total_observed_calls'].get(key,0)+value
    else:
        budget['incomplete_counter_capture_at']=point_id
        budget['counter_capture_note']='final counters unavailable after termination; latest trajectory counters provide lower bounds, not fabricated zeros'
    assert budget['total_observed_calls'].get('initializer_calls',0)<=7 and budget['total_observed_calls'].get('hjb_calls',0)<=7 and budget['total_observed_calls'].get('hjb_iterations',0)<=700 and budget['total_observed_calls'].get('kfe_calls',0)<=7
    budget['points'][point_id]=classification;budget['total_science_wall_seconds']=budget.get('total_science_wall_seconds',0.0)+elapsed
    budget['task_stopped']=fatal
    if fatal:
        for n in range(index+1,7):budget['points']['P'+str(n)]='NOT_EXECUTED_AFTER_'+point_id+'_GLOBAL_STOP'
    budget_path.write_text(json.dumps(budget,indent=2)+'\n',encoding='utf-8',newline='\n')
    redaction={'transformation':'exact workspace/runtime prefix replacement only; raw originals stay LOCAL_ONLY',
      'stdout':{'raw_bytes':len(out),'raw_sha256':sha(out),'public_bytes':len(public_out),'public_sha256':sha(public_out),'changes':changes_out},
      'stderr':{'raw_bytes':len(err),'raw_sha256':sha(err),'public_bytes':len(public_err),'public_sha256':sha(public_err),'changes':changes_err}}
    write(EV/f'{point_id}_redaction_record.json',redaction)
    result={'point':point_id,'classification':classification,'fatal_to_task':fatal,'exit_code':process.returncode,'timed_out':timed_out,'pre_import_memory_block':pre_import_block,
      'elapsed_seconds':elapsed,'hard_timeout_seconds':180,'memory_limit':memory,'science_child_processes':1,'final_event':final,'raw_public_log_identity':redaction,'retries':0,
      'actual_counts':counts,'completed_iteration_metrics':len(trajectory)}
    write(EV/f'{point_id}_receipt.json',result)
    if final:write(EV/f'{point_id}_result.json',final)
    print(json.dumps({'point':point_id,'classification':classification,'fatal_to_task':fatal,'exit_code':process.returncode,'timed_out':timed_out,'elapsed_seconds':elapsed,'memory_limit':memory,
      'HJB':final.get('HJB') if final else None,'KFE':final.get('KFE') if final else None,'actual_counts':counts}),flush=True)
    if public_err:print(public_err.decode('utf-8','replace'),file=sys.stderr)
    return 1 if fatal else 0
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--point',choices=tuple('P'+str(n) for n in range(7)),required=True)
    raise SystemExit(main(parser.parse_args().point))
