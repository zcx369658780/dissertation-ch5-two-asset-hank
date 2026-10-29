"""One30s/1GiB science child per authenticated archive; at most4 core KFE calls."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,os
from pathlib import Path
import subprocess,sys,time
from datetime import datetime,timezone
REPORT=Path(__file__).resolve().parent;WORK=REPORT.parents[1];EV=REPORT/'evidence';POINTS=('P0','P2','P4','P5')
ENTRY='validators/multi_province/temp31_matlab_kfe_blackbox_parity_freeze_isolated.py'
THREAD_KEYS=('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS','BLIS_NUM_THREADS')
def read(path):return json.loads(path.read_text(encoding='utf-8'))
def write(path,data):
    with path.open('x',encoding='utf-8',newline='\n') as f:json.dump(data,f,indent=2);f.write('\n')
def sha(raw):return hashlib.sha256(raw).hexdigest()
def helper(identity):
    row=identity['authenticated_supervisor_helper'];path=WORK/row['path'];raw=path.read_bytes()
    assert sha(raw)==row['sha256'] and len(raw)==row['bytes'] and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==row['git_blob']
    spec=importlib.util.spec_from_file_location('temp31_kfe_freeze_authentic_supervisor',path);module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module);return module
def main(point):
    index=POINTS.index(point);budget_path=REPORT/'budget.json';budget=read(budget_path)
    assert budget['replay_commands_started']==index and not budget['closed'],'STOP_REPLAY_BUDGET_OR_REPEAT'
    if index:
        prior=read(EV/f'{POINTS[index-1]}_receipt.json');assert prior['passed'] and prior['exit_code']==0 and not prior['timed_out']
    source=read(REPORT/'source_identity.json');old=helper(source);archives=read(REPORT/'archive_identity.json');assert archives['all_four_available_authenticated']
    command=[sys.executable,'-B',ENTRY,'--point',point]
    write(EV/f'{point}_claim.json',{'point':point,'command_number':index+1,'command':['python','-B',*command[2:]],'working_directory':'<ISOLATED_CANDIDATE_ROOT>',
      'declared_at_utc':datetime.now(timezone.utc).isoformat(),'hard_timeout_seconds':30,'committed_memory_max':1073741824,'science_processes':1,
      'source_commit':source['source']['commit'],'entry_sha256':sha((WORK/ENTRY).read_bytes()),'supervisor_sha256':sha(Path(__file__).read_bytes()),
      'replay_contract_sha256':sha((REPORT/'replay_contract.json').read_bytes()),'archive_identity_sha256':sha((REPORT/'archive_identity.json').read_bytes()),
      'max_KFE_calls':1,'HA_HJB_policy_initializer_root_price_search_calls':0,'retry_allowed':False})
    budget['replay_commands_started']=index+1;budget_path.write_text(json.dumps(budget,indent=2)+'\n',encoding='utf-8',newline='\n')
    env=dict(os.environ,**{k:'1' for k in THREAD_KEYS},PYTHONDONTWRITEBYTECODE='1',PYTHONNOUSERSITE='1');env.pop('PYTHONPATH',None)
    start=time.monotonic();p=subprocess.Popen(command,cwd=WORK,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env)
    close_job=None;timed_out=False;memory={'status':'MEMORY_HARD_LIMIT_UNAVAILABLE'};pre_import_block=False
    try:
        _,memory,close_job=old.restrict_memory(p)
        if memory['status']!='PROCESS_MEMORY_HARD_LIMIT_ENFORCED':pre_import_block=True;p.kill();out,err=p.communicate()
        else:out,err=p.communicate(input=b'GO\n',timeout=max(.001,30-(time.monotonic()-start)))
    except subprocess.TimeoutExpired:
        timed_out=True;p.kill();out,err=p.communicate()
    except BaseException:
        p.kill();p.communicate();raise
    finally:
        if close_job is not None:memory['observed_peak_process_committed_bytes']=close_job()
    elapsed=time.monotonic()-start
    (EV/f'LOCAL_ONLY_{point}_stdout_raw.txt').write_bytes(out);(EV/f'LOCAL_ONLY_{point}_stderr_raw.txt').write_bytes(err)
    public_out,changes_out=old.redact(out);public_err,changes_err=old.redact(err)
    (EV/f'{point}_stdout_public.txt').write_bytes(public_out);(EV/f'{point}_stderr_public.txt').write_bytes(public_err)
    events=[json.loads(line) for line in public_out.decode('utf-8','replace').splitlines() if line.startswith('{"event":')]
    final=next((e for e in reversed(events) if e['event']=='replay_result'),None)
    passed=p.returncode==0 and not timed_out and not pre_import_block and final is not None and final['status']=='REPLAY_MATCH'
    counts=final.get('actual_counts') if final else None
    if counts:
        for key,value in counts.items():budget['total_actual_calls'][key]=budget['total_actual_calls'].get(key,0)+value
    else:budget['counter_capture']='final counters unavailable; no fabricated completed solve counts'
    budget['points'][point]='REPLAY_MATCH' if passed else 'STOP_NO_RETRY'
    if not passed:budget['closed']=True
    assert budget['total_actual_calls'].get('KFE_calls',0)<=4 and budget['total_actual_calls'].get('forbidden_model_calls',0)==0
    budget_path.write_text(json.dumps(budget,indent=2)+'\n',encoding='utf-8',newline='\n')
    redaction={'transformation':'exact workspace/runtime prefix replacement only; raw logs retained LOCAL_ONLY',
      'stdout':{'raw_bytes':len(out),'raw_sha256':sha(out),'public_bytes':len(public_out),'public_sha256':sha(public_out),'changes':changes_out},
      'stderr':{'raw_bytes':len(err),'raw_sha256':sha(err),'public_bytes':len(public_err),'public_sha256':sha(public_err),'changes':changes_err}}
    write(EV/f'{point}_redaction_record.json',redaction)
    receipt={'point':point,'passed':passed,'exit_code':p.returncode,'timed_out':timed_out,'hard_timeout_seconds':30,'elapsed_seconds':elapsed,'memory_limit':memory,
      'science_child_processes':1,'pre_import_memory_block':pre_import_block,'final_event':final,'actual_counts':counts,'raw_public_log_identity':redaction,'retries':0}
    write(EV/f'{point}_receipt.json',receipt)
    if final:write(EV/f'{point}_result.json',final)
    print(json.dumps({'point':point,'passed':passed,'exit_code':p.returncode,'elapsed_seconds':elapsed,'timed_out':timed_out,'memory_limit':memory,'final_event':final}),flush=True)
    if public_err:print(public_err.decode('utf-8','replace'),file=sys.stderr)
    return 0 if passed else 1
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--point',choices=POINTS,required=True)
    raise SystemExit(main(parser.parse_args().point))
