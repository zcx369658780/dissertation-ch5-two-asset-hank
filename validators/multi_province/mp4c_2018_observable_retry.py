"""One-shot, 2018-only observability harness; imports no scientific solver."""
from __future__ import annotations
import hashlib,json,os,subprocess,sys,traceback
from datetime import datetime,timezone
from pathlib import Path
REPO=Path(__file__).resolve().parents[2]; THREAD={k:'1' for k in ('OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS','NUMEXPR_NUM_THREADS')}
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest().upper()
def put(p,x):
 with Path(p).open('x',encoding='utf-8') as f: json.dump(x,f,ensure_ascii=False,indent=2,sort_keys=True);f.write('\n')
def run(input_path,cache_path,root):
 root=Path(root); root.mkdir(parents=True,exist_ok=False); inp=Path(input_path); data=json.loads(inp.read_text(encoding='utf-8'))
 b=data['binding']; assert b['steady_state_calendar_year']==2018 and b['rolling_window_entry_index']==10 and b['regression_vintage_index']==19 and b['calendar_level_row_index']==19 and data['no_2023_scientific_input']
 copy=root/inp.name;copy.write_bytes(inp.read_bytes()); env=os.environ.copy();env.update(THREAD);cmd=[sys.executable,str(REPO/'validators/multi_province/mp4c_python_annual_production.py'),str(copy),str(cache_path),str(root/'year_2018')];start=datetime.now(timezone.utc).isoformat()
 try:
  p=subprocess.run(cmd,cwd=REPO,env=env,text=True,capture_output=True); code=p.returncode;out,err=p.stdout,p.stderr
  cls='PASS' if code==0 else ('SCIENTIFIC_NONCONVERGENCE_FAIL' if code==2 and (root/'year_2018'/'FAILURE.json').is_file() else 'PROCESS_EXCEPTION_FAIL')
 except OSError:
  code=None;out='';err=traceback.format_exc();cls='INFRASTRUCTURE_FAIL'
 (root/'retry_2018_stdout.log').write_text(out,encoding='utf-8');(root/'retry_2018_stderr.log').write_text(err,encoding='utf-8')
 put(root/'retry_2018_execution_receipt.json',{'classification':cls,'exit_code':code,'command':cmd,'thread_environment':THREAD,'start':start,'end':datetime.now(timezone.utc).isoformat(),'runtime_input_sha256':sha(copy),'source_input_sha256':sha(inp),'input_identical':sha(copy)==sha(inp)})
 return 0 if cls=='PASS' else 2
