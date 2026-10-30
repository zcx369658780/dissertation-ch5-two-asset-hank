"""Single archive diagnostic child; 180 seconds, 1GiB commit, no retry."""
from pathlib import Path
import ast,hashlib,importlib.util,json,os,subprocess,sys,time
from datetime import datetime,timezone
REPORT=Path(__file__).resolve().parent;WORK=REPORT.parents[1];EV=REPORT/'evidence'
ENTRY='validators/multi_province/temp31_r3_e03_e04_readonly_archive_mechanism_r4_isolated.py'
KEYS=('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS','BLIS_NUM_THREADS')
def dump(p,x):
 with p.open('x',encoding='utf-8',newline=chr(10)) as f:json.dump(x,f,indent=2,allow_nan=False);f.write(chr(10))
def sha(b):return hashlib.sha256(b).hexdigest()
def main():
 assert json.loads((EV/'LOCAL_ONLY_preflight_pass.json').read_text(encoding='utf-8'))['passed']
 raw=(WORK/ENTRY).read_bytes();tree=ast.parse(raw);compile(tree,ENTRY,'exec')
 imports=[]
 for node in ast.walk(tree):
  if isinstance(node,ast.Import):imports.extend(a.name for a in node.names)
  elif isinstance(node,ast.ImportFrom):imports.append(node.module)
 assert set(imports)=={'__future__','hashlib','json','os','sys','pathlib','numpy','scipy','scipy.sparse'}
 forbidden={'spsolve','solve','gmres','eig','eigs','odeint','solve_ivp','select_temp31_netwage_local_policy','solve_temp31_netwage_hjb'}
 assert not any((isinstance(n,ast.Name) and n.id in forbidden) or (isinstance(n,ast.Attribute) and n.attr in forbidden) for n in ast.walk(tree))
 helper=WORK/'tasks/CH5_TEMP31_REAL_HA_RUNTIME_TINYGRID_SMOKE_R1_20261029/run_controlled_smoke.py'
 b=helper.read_bytes();assert sha(b)=='6ba5caeb1d96596f88b62022a25c3f7488b82eb53daa1a67b9c61edb0b2cb0d8' and len(b)==11051
 spec=importlib.util.spec_from_file_location('r4_authenticated_resource_helper',helper);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
 command=[sys.executable,'-B',ENTRY]
 dump(EV/'diagnostic_claim.json',dict(task_id=REPORT.name,started_at_utc=datetime.now(timezone.utc).isoformat(),diagnostic_number=1,maximum=1,retry=False,entry_sha256=sha(raw),supervisor_sha256=sha(Path(__file__).read_bytes()),command=['python','-B',ENTRY],cwd='<ISOLATED_CANDIDATE_ROOT>',timeout_seconds=180,process_commit_limit=1073741824,active_child_limit=1,thread_environment={k:'1' for k in KEYS},static_import_whitelist=imports,forbidden_model_and_solver_AST_symbols_absent=True))
 env=dict(os.environ,**{k:'1' for k in KEYS},PYTHONDONTWRITEBYTECODE='1',PYTHONNOUSERSITE='1');env.pop('PYTHONPATH',None)
 start=time.monotonic();p=subprocess.Popen(command,cwd=WORK,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env)
 close=None;timed_out=False;memory={};blocked=False
 try:
  _,memory,close=old.restrict_memory(p)
  if memory['status']!='PROCESS_MEMORY_HARD_LIMIT_ENFORCED':
   blocked=True;p.kill();out,err=p.communicate()
  else:out,err=p.communicate(input=b'GO'+bytes([10]),timeout=max(.001,180-(time.monotonic()-start)))
 except subprocess.TimeoutExpired:
  timed_out=True;p.kill();out,err=p.communicate()
 except BaseException:
  p.kill();p.communicate();raise
 finally:
  if close is not None:memory['observed_peak_process_committed_bytes']=close()
 elapsed=time.monotonic()-start
 for name,rawlog in [('stdout',out),('stderr',err)]:
  with (EV/('LOCAL_ONLY_diagnostic_'+name+'_raw.txt')).open('xb') as f:f.write(rawlog)
  public,changes=old.redact(rawlog)
  with (EV/('diagnostic_'+name+'_public.txt')).open('xb') as f:f.write(public)
  dump(EV/(name+'_redaction_record.json'),dict(raw_bytes=len(rawlog),raw_sha256=sha(rawlog),public_bytes=len(public),public_sha256=sha(public),transformations=changes,original_retained_local_only=True,numeric_fields_modified=False))
 final=json.loads(out.decode('utf-8')) if p.returncode==0 else None
 passed=p.returncode==0 and not timed_out and not blocked and final is not None and final.get('passed') is True
 receipt=dict(task_id=REPORT.name,passed=passed,exit_code=p.returncode,timed_out=timed_out,memory_preimport_block=blocked,elapsed_seconds=elapsed,hard_timeout_seconds=180,memory=memory,diagnostic_processes_started=1,maximum_diagnostic_processes=1,diagnostic_budget_closed=True,model_solver_calls=0,scientific_functions_imported=0,archive_files=4,attempts=1,retries=0,final_event=final,scope='read-only archive algebra; no scientific solver')
 dump(REPORT/'readonly_diagnostic_receipt.json',receipt)
 print(json.dumps(dict(passed=passed,elapsed_seconds=elapsed,memory=memory,final=final)))
 return 0 if passed else 1
if __name__=='__main__':raise SystemExit(main())
