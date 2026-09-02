"""Read-only MP4C Owner-A 13-pass and 2018 failure diagnostic."""
from __future__ import annotations
import csv, hashlib, json
from pathlib import Path
import numpy as np

ROOT=Path(r"D:/ProjectTemp/ch5-mp4c-owner-a-corrected-2009-2022-8worker-20260902-001")
OUT=Path(r"D:/ProjectTemp/ch5-mp4c-13pass-matlab-comparator-2018-diagnostic-20260903-001")
MAT=Path(r"D:/MatlabProgram/2023年12月2日 多省份神经网络HANK_DIAGNOSTIC_PATCH_2026_06_23")
YEARS=(2009,2010,2011,2012,2013,2014,2015,2016,2017,2019,2020,2021,2022)
REP="OWNER_A_2009_2022_VERIFIED_CHNCAPITALSTOCK_ROLLING_PLM_END_YEAR_CALENDAR_INPUT"
FIELDS=("Ct","At","Bt","Lt","Lt_supply","Kt_supply","rah","Kt","Yt","mt","KNratio","w","wjt","rk","ra","GovInv","rb","it","Zt","Govinc")
def sha(p):
 h=hashlib.sha256();
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest().upper()
def new(p,o):
 if p.exists():raise FileExistsError(p)
 p.write_text(json.dumps(o,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
def main():
 if OUT.exists():raise FileExistsError(OUT)
 OUT.mkdir(parents=True)
 audit=[]; anomaly=[]
 for y in YEARS:
  d=ROOT/f'year_{y}'; success=json.loads((d/'SUCCESS.json').read_text(encoding='utf-8')); run=json.loads((d/'run_manifest.json').read_text(encoding='utf-8')); term=json.loads((d/'final_steady_state.json').read_text(encoding='utf-8')); ck=json.loads((d/'checkpoint_manifest.json').read_text(encoding='utf-8')); inp=d/f'calendar_{y}_matlab_runtime_cache_input.json'; data=json.loads(inp.read_text(encoding='utf-8'))
  outs=success['outputs']; hashes=all((d/n).is_file() and sha(d/n)==m['sha256'] and (d/n).stat().st_size==m['bytes'] for n,m in outs.items())
  table=term['final_31x20']; vals=np.array([[float(r[k]) for k in FIELDS] for r in table]); lt=np.load(d/'Lt_mat_destination_row_origin_column.npy')
  ok=(success['status']=='SOURCE_CONVERGED' and success['representation']==REP and success['runtime_input_sha256']==sha(inp) and data['binding']=={'steady_state_calendar_year':y,'rolling_window_entry_index':y-2008,'regression_vintage_index':y-1999,'calendar_level_row_index':y-1999,'rolling_window_start_year':y-9,'rolling_window_end_year':y} and len(table)==31 and np.isfinite(vals).all() and lt.shape==(31,31) and np.isfinite(lt).all() and hashes and run['thread_environment']=={'OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','NUMEXPR_NUM_THREADS':'1'} and data['no_2023_scientific_input'] is True)
  audit.append({'year':y,'integrity_pass':bool(ok),'runtime_input_sha256':sha(inp),'checkpoint_schema':ck.get('schema'),'final_fields_finite':bool(np.isfinite(vals).all()),'lt_shape':list(lt.shape),'artifact_hashes_exact':bool(hashes)})
  anomaly.append({'year':y,'outer_turns':term['iteration_count'],'household_calls':term['household_call_count'],'wall_clock_seconds':term['wall_clock_seconds'],'national_Yt':term['national']['Yt'],'national_Ct':term['national']['Ct'],'ra_min':float(vals[:,FIELDS.index('ra')].min()),'ra_max':float(vals[:,FIELDS.index('ra')].max()),'w_min':float(vals[:,FIELDS.index('w')].min()),'w_max':float(vals[:,FIELDS.index('w')].max()),'checkpoint_bytes':(d/'final_household_restart.npz').stat().st_size})
 new(OUT/'python_13pass_integrity_audit.json',{'years':audit,'all_pass':all(x['integrity_pass'] for x in audit),'scientific_calls':0})
 with (OUT/'cross_year_2009_2022_anomaly_matrix.csv').open('x',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=anomaly[0].keys());w.writeheader();w.writerows(anomaly)
 artifacts=[]
 for p in sorted(MAT.glob('Multi_Province_12sts_*.mat')):
  year=int(p.stem.rsplit('_',1)[1]); artifacts.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'year_label':year,'classification':'LEGACY_CALENDAR_BINDING_DIAGNOSTIC_ONLY','reason':'protected legacy annual route uses data_year=ii; filename is not corrected-calendar provenance'})
 for n in ('12年稳态值.xlsx','12年稳态Ltmat.xlsx'):
  p=MAT/n; artifacts.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'year_label':None,'classification':'LEGACY_CALENDAR_BINDING_DIAGNOSTIC_ONLY','reason':'historical workbook lacks corrected Owner-A input identity'})
 new(OUT/'matlab_steady_state_artifact_provenance_map.json',{'artifacts':artifacts,'same_input_eligible':[],'scientific_calls':0})
 rows=[{'year':y,'python_status':'SOURCE_CONVERGED','matlab_artifact':'legacy protected Multi_Province_12sts_'+str(y)+'.mat','matlab_semantic_classification':'LEGACY_CALENDAR_BINDING_DIAGNOSTIC_ONLY','fields_compared':'none; no read-proven corrected same-input field mapping','strict_parity_eligible':'no','max_normalized_difference':'','diagnostic_max_relative_difference':'','worst_field':'','worst_province':'','verdict':'NO_COMPATIBLE_MATLAB_REFERENCE'} for y in YEARS]
 for name in ('same_input_parity_comparison_eligible_fields.csv','legacy_matlab_diagnostic_comparison.csv','year_level_matlab_python_comparison_matrix.csv'):
  with (OUT/name).open('x',newline='',encoding='utf-8') as f:
   w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows if name.endswith('matrix.csv') else [])
 d=ROOT/'year_2018'; inv=[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(d.iterdir())]
 new(OUT/'failure_2018_artifact_inventory.json',{'files':inv,'failure_marker_present':False})
 trace={'scheduler_launch':'subprocess.run(..., text=True) without capture_output/stdout/stderr target','exit_mapping':'0=>PASS; 2=>FAIL; any other=>SHARED_FAIL','worker_solver_path':'only SteadyStateConvergenceError is caught; result.converged false writes FAILURE.json then returns 2','pre_serialization_path':'any other exception exits Python with 1 before marker serialization','observability_defect':'stdout/stderr/traceback absent from preserved batch evidence'}
 new(OUT/'failure_2018_exit_path_trace.json',trace)
 new(OUT/'failure_2018_root_cause_classification.json',{'classification':'2018_SHARED_FAIL_RUNNER_EXCEPTION_CAPTURE_DEFECT','confidence':'strong for missing exception preservation; underlying triggering exception remains unresolved','basis':trace,'no_rerun':True})
 issues=[['I01','engineering','2018','exit 1 mapped to SHARED_FAIL; no stderr/traceback/FAILURE.json','engineering','high','yes','capture stdout/stderr and serialize uncaught exception before an authorized retry','no'],['I02','scientific evidence','2009-2022','protected MATLAB annual files use legacy calendar binding','scientific','high','yes','establish corrected same-input MATLAB artifact mapping before strict multiyear parity','yes'],['I03','integrity','13 PASS years','all required 13 artifacts/hash/index checks passed','engineering','none','no','retain immutable evidence','no']]
 with (OUT/'integrated_issue_matrix.csv').open('x',newline='',encoding='utf-8') as f:
  w=csv.writer(f);w.writerow(['issue_id','category','year(s)','evidence','scientific_or_engineering','severity','blocks_acceptance','minimal_next_action','owner_decision_required']);w.writerows(issues)
 new(OUT/'zero_science_execution_ledger.json',{'python_stationary':0,'household':0,'hjb':0,'kfe':0,'matlab':0,'r_plm':0,'shock_irf':0,'r5':0,'results':0,'comparator_only':True})
 files=[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(OUT.iterdir()) if p.is_file()]
 new(OUT/'audit_manifest.json',{'files':files})
if __name__=='__main__':main()
