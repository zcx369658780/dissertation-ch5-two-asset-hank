"""One 180-second, 1GiB real science child per frozen E00-E11 point; no retries."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,os
from pathlib import Path
import subprocess,sys,time
from datetime import datetime,timezone
REPORT=Path(__file__).resolve().parent;WORK=REPORT.parents[1];EV=REPORT/'evidence'
ENTRY='validators/multi_province/temp31_matlab800_price_neighborhood_r3_isolated.py'
THREAD_KEYS=('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS','BLIS_NUM_THREADS')
def read(path):return json.loads(path.read_text(encoding='utf-8'))
def write(path,data):
 with path.open('x',encoding='utf-8',newline='\n') as f:json.dump(data,f,indent=2);f.write('\n')
def sha(raw):return hashlib.sha256(raw).hexdigest()
def authenticate_helper(identity):
 row=identity['authenticated_supervisor_helper'];path=WORK/row['path'];raw=path.read_bytes()
 assert sha(raw)==row['sha256'] and len(raw)==row['bytes'] and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==row['git_blob']
 spec=importlib.util.spec_from_file_location('domain_authentic_supervisor',path);m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);return m
def public_log(raw,old):
 public,prefix_changes=old.redact(raw);fields=[];lines=[]
 def normalize(node,pointer=''):
  if isinstance(node,dict):
   for k,v in node.items():
    p=pointer+'/'+k
    if k in ('file','task_relative_path','cache_path','path') and isinstance(v,str) and chr(92) in v:
     node[k]=v.replace(chr(92),'/');fields.append({'json_pointer':p,'transform':'metadata path separator normalization after exact private-prefix replacement','original_role_value_sha256':sha(v.encode())})
    else:normalize(v,p)
  elif isinstance(node,list):
   for i,v in enumerate(node):normalize(v,pointer+'/'+str(i))
 for number,line in enumerate(public.decode('utf-8','replace').splitlines(),1):
  if line.startswith('{'):
   node=json.loads(line);normalize(node,'/JSONL_record_'+str(number));lines.append(json.dumps(node,allow_nan=False)+'\n')
  else:lines.append(line+'\n')
 output=''.join(lines).encode() if public else b''
 return output,{'prefix_replacements':prefix_changes,'field_transformations':fields,'serialization':'public JSONL reserialized after metadata-only transformation; raw bytes preserved'}
def main(point_id):
 index=int(point_id[1:]);budget_path=REPORT/'budget.json';budget=read(budget_path);config=read(REPORT/'point_grid.json')
 assert budget['point_commands_started']==index and not budget['task_stopped'] and not budget['budget_closed'],'STOP_POINT_ORDER_OR_BUDGET'
 assert read(REPORT/'preflight.json')['passed']
 if index:
  prior=read(EV/f'E{index-1:02d}_receipt.json');assert prior['exit_code']==0 and not prior['timed_out'] and not prior['fatal_to_task']
  assert read(EV/'global_wage_and_negative_guard_preflight.json')['passed']
 identity=read(REPORT/'source_identity.json');old=authenticate_helper(identity);command=[sys.executable,'-B',ENTRY,'--point',point_id];point=config['points'][index];assert point['id']==point_id
 write(EV/f'{point_id}_claim.json',{'point':point_id,'prices':point,'command_number':index+1,'command':['python','-B',*command[2:]],'working_directory':'<ISOLATED_CANDIDATE_ROOT>',
  'claimed_at_utc':datetime.now(timezone.utc).isoformat(),'hard_timeout_seconds':180,'max_science_processes':1,'process_committed_memory_max':1073741824,
  'source_commit':identity['source']['commit'],'entry_sha256':sha((WORK/ENTRY).read_bytes()),'supervisor_sha256':sha(Path(__file__).read_bytes()),'point_grid_sha256':sha((REPORT/'point_grid.json').read_bytes()),
  'call_limits':{'initializer_calls':1,'root_cells':800,'hjb_calls':1,'hjb_iterations':100,'hjb_policy_cells':80000,'kfe_calls':1},'retry_allowed':False,
  'KFE_gate':'only actual source HJB converged with statistic<1e-7; unchanged returned post operator'})
 budget['point_commands_started']=index+1;budget_path.write_text(json.dumps(budget,indent=2)+'\n',encoding='utf-8',newline='\n')
 env=dict(os.environ,**{k:'1' for k in THREAD_KEYS},PYTHONDONTWRITEBYTECODE='1',PYTHONNOUSERSITE='1');env.pop('PYTHONPATH',None)
 start=time.monotonic();process=subprocess.Popen(command,cwd=WORK,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env)
 close_job=None;timed_out=False;memory={'status':'MEMORY_HARD_LIMIT_UNAVAILABLE'};pre_import_block=False
 try:
  _,memory,close_job=old.restrict_memory(process)
  if memory['status']!='PROCESS_MEMORY_HARD_LIMIT_ENFORCED':pre_import_block=True;process.kill();out,err=process.communicate()
  else:out,err=process.communicate(input=b'GO\n',timeout=max(.001,180-(time.monotonic()-start)))
 except subprocess.TimeoutExpired:timed_out=True;process.kill();out,err=process.communicate()
 except BaseException:process.kill();process.communicate();raise
 finally:
  if close_job is not None:memory['observed_peak_process_committed_bytes']=close_job()
 elapsed=time.monotonic()-start
 for suffix,raw in (('stdout',out),('stderr',err)):
  with (EV/f'LOCAL_ONLY_{point_id}_{suffix}_raw.txt').open('xb') as f:f.write(raw)
 public_out,change_out=public_log(out,old);public_err,change_err=public_log(err,old)
 for suffix,raw in (('stdout',public_out),('stderr',public_err)):
  with (EV/f'{point_id}_{suffix}_public.txt').open('xb') as f:f.write(raw)
 events=[json.loads(line) for line in public_out.decode().splitlines() if line.startswith('{"event":')]
 final=next((e for e in reversed(events) if e['event']=='point_result'),None)
 if index==0:
  preflight=next((e for e in events if e['event']=='all_price_wage_and_negative_guard_preflight'),None)
  if preflight:write(EV/'global_wage_and_negative_guard_preflight.json',preflight)
 trajectory=[{k:v for k,v in e.items() if k not in ('event','observed_counts')} for e in events if e['event']=='hjb_iteration']
 write(EV/f'{point_id}_iteration_trajectory.json',{'point':point_id,'completed_iteration_metrics':len(trajectory),'trajectory':trajectory,'no_hidden_HJB_rerun':True})
 fatal=timed_out or pre_import_block or process.returncode!=0 or final is None or final.get('fatal_to_task',True)
 counts=final.get('observed_counts') if final else None;classification=final['classification'] if final else 'EXECUTION_BLOCKED'
 if counts:
  for k,v in counts.items():budget['total_observed_calls'][k]=budget['total_observed_calls'].get(k,0)+v
 else:budget['counter_capture_note']='No final counters: latest iteration events are lower bounds, not fabricated zeros';budget['incomplete_counter_capture_at']=point_id
 for k,maximum in {'initializer_calls':12,'hjb_calls':12,'hjb_iterations':1200,'hjb_policy_cells':960000,'kfe_calls':12}.items():assert budget['total_observed_calls'].get(k,0)<=maximum
 budget['points'][point_id]=classification;budget['total_science_wall_seconds']+=elapsed;budget['task_stopped']=fatal
 if fatal:
  budget['budget_closed']=True
  for n in range(index+1,12):budget['points'][f'E{n:02d}']='NOT_EXECUTED_AFTER_GLOBAL_STOP'
 if index==11:budget['budget_closed']=True
 budget_path.write_text(json.dumps(budget,indent=2)+'\n',encoding='utf-8',newline='\n')
 redaction={'role':'PUBLICATION_DERIVATIVE_REDACTED','original_role':'EXECUTION_STDOUT_STDERR_RAW_LOCAL_ONLY',
  'stdout':{'raw_bytes':len(out),'raw_sha256':sha(out),'public_bytes':len(public_out),'public_sha256':sha(public_out),'changes':change_out},
  'stderr':{'raw_bytes':len(err),'raw_sha256':sha(err),'public_bytes':len(public_err),'public_sha256':sha(public_err),'changes':change_err},'scientific_numeric_values_modified':False}
 write(EV/f'{point_id}_redaction_record.json',redaction)
 receipt={'point':point_id,'classification':classification,'fatal_to_task':fatal,'exit_code':process.returncode,'timed_out':timed_out,'pre_import_memory_block':pre_import_block,
  'elapsed_seconds':elapsed,'hard_timeout_seconds':180,'memory_limit':memory,'science_child_processes':1,'final_event':final,'raw_public_log_identity':redaction,'retries':0,'actual_counts':counts,'completed_iteration_metrics':len(trajectory)}
 write(EV/f'{point_id}_receipt.json',receipt)
 if final:write(EV/f'{point_id}_result.json',final)
 print(json.dumps({'point':point_id,'classification':classification,'fatal_to_task':fatal,'exit_code':process.returncode,'timed_out':timed_out,'elapsed_seconds':elapsed,'memory_limit':memory,
  'HJB':{k:final['HJB'].get(k) for k in ('converged','iterations','convergence_statistic','implicit_identity_error','observed_homecrit_violation')} if final else None,
  'KFE':{k:final['KFE'].get(k) for k in ('status','At','Bt','Ct','Lt','a_internal_mass','b_internal_mass','b_upper_mass','stationary_residual','SOURCE_METHOD_INTERIOR_CANDIDATE')} if final else None,'actual_counts':counts}),flush=True)
 return 1 if fatal else 0
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--point',choices=tuple(f'E{i:02d}' for i in range(12)),required=True)
 raise SystemExit(main(parser.parse_args().point))
