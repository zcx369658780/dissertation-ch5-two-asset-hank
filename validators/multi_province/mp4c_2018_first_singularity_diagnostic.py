"""One-shot MP4C 2018 KFE singularity capture; no repair/fallback path."""
from __future__ import annotations
import argparse,csv,hashlib,json,os,sys,time,traceback,warnings
from dataclasses import asdict
from pathlib import Path
from typing import Any
import numpy as np
from scipy import sparse
from scipy.sparse import csgraph

ROOT=Path(__file__).resolve().parents[2]
sys.path[:0]=[str(ROOT/'src'),str(ROOT)]
from validators.multi_province import mp4b_python_empirical as anchor
from validators.multi_province import mp4c_python_annual_empirical as empirical
from validators.multi_province import mp4c_owner_a_2009_2022 as owner_a
from validators.multi_province.mp4c_python_annual_production import FINAL_FIELDS,serialize_final_state
from validators.multi_province.mp4b_matlab_source_postloop_household_adapter import solve_matlab_source_postloop_household
import exports.matlab_faithful_two_asset_ha as faithful
from ch5_two_asset_hank.multi_province.one_turn import PreFrozenHouseholdOutputBatch
from ch5_two_asset_hank.multi_province.stationary_runtime import OnlineStationaryInputs,run_online_stationary
from ch5_two_asset_hank.multi_province.steady_state import TERMINATION_CONVERGED

EXPECTED='F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0'
ENV={x:'1' for x in ('OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS','NUMEXPR_NUM_THREADS')}
def sha(p):
 h=hashlib.sha256();
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest().upper()
def j(path,x):
 path=Path(path)
 with path.open('x',encoding='utf-8',newline='\n') as f:
  json.dump(x,f,ensure_ascii=False,indent=2,sort_keys=True,allow_nan=False);f.write('\n');f.flush();os.fsync(f.fileno())
def txt(path,value):
 with Path(path).open('x',encoding='utf-8',newline='\n') as f:
  f.write(value);f.flush();os.fsync(f.fileno())
def mat(path,m):
 with Path(path).open('xb') as f:
  sparse.save_npz(f,m);f.flush();os.fsync(f.fileno())
def arr(path,value):
 with Path(path).open('xb') as f:
  np.save(f,value);f.flush();os.fsync(f.fileno())
def svd(m):
 s=np.linalg.svdvals(sparse.csr_matrix(m).toarray());tol=max(m.shape)*np.finfo(float).eps*(float(s[0]) if s.size else 0.0);rank=int(np.count_nonzero(s>tol))
 return {'method':'numpy.linalg.svdvals_dense_float64','shape':list(m.shape),'tolerance':tol,'rank':rank,'nullity':int(m.shape[1]-rank),'smallest_singular_values':[float(x) for x in s[-16:]]}
def summary(a):
 a=sparse.csr_matrix(a); off=a.copy();off.setdiag(0);off.eliminate_zeros();d=a.diagonal(); data=off.data
 scale=max(1.0,float(np.max(np.abs(data))) if data.size else 0.0);tol=np.finfo(float).eps*scale
 edge=off.multiply(off>tol).tocsr(); ncomp,lab=csgraph.connected_components(edge,directed=True,connection='strong',return_labels=True)
 closed=[]
 for c in range(ncomp):
  ind=np.flatnonzero(lab==c); target=set(lab[edge[ind].indices]);
  if target<={c}:closed.append({'component':int(c),'size':int(len(ind)),'state_indices_0based':ind.tolist()})
 out=np.diff(edge.indptr); inn=np.bincount(edge.indices,minlength=a.shape[0])
 return {'shape':list(a.shape),'nnz':int(a.nnz),'finite_data':bool(np.isfinite(a.data).all()),'max_abs_row_sum':float(np.max(np.abs(a.sum(axis=1)))), 'max_abs_column_sum_transpose':float(np.max(np.abs(a.transpose().sum(axis=0)))), 'diagonal_min':float(d.min()),'diagonal_max':float(d.max()),'offdiagonal_min':float(data.min()) if data.size else None,'offdiagonal_max':float(data.max()) if data.size else None,'positive_offdiagonal_count':int(np.count_nonzero(data>0)),'graph_threshold':tol,'scc_count':int(ncomp),'closed_scc_count':len(closed),'closed_sccs':closed,'multiple_closed_sccs':len(closed)>1,'zero_outflow_states':np.flatnonzero(out==0).tolist(),'isolated_states':np.flatnonzero((out==0)&(inn==0)).tolist(),'state_index_order':'0-based Fortran flatten: b + a*Nb + z*Nb*Na'}
class FirstSingularityCaptured(RuntimeError):
 pass
class DurableCsvLedger:
 """Diagnostic-only CSV lifecycle with one header and durable appends."""
 def __init__(self,path):
  self.path=Path(path);self.file=self.path.open('x',encoding='utf-8',newline='');self.writer=None;self.fieldnames=None;self.rows=0
 def append(self,row):
  fields=list(row)
  if self.writer is None:
   self.fieldnames=fields;self.writer=csv.DictWriter(self.file,fieldnames=fields);self.writer.writeheader()
  elif fields!=self.fieldnames:raise ValueError('durable ledger field order changed')
  self.writer.writerow(row);self.file.flush();os.fsync(self.file.fileno());self.rows+=1
 def close(self):
  if not self.file.closed:self.file.close()
class Capture:
 def __init__(self,root):self.root=root;self.ctx=None;self.hjb=None;self.done=False
 def before(self,a):self.a=sparse.csr_matrix(a);self.at=self.a.transpose().tocsr()
 def solve(self,original):
  import exports.matlab_faithful_two_asset_ha as ex
  old=ex.linalg.spsolve; warning=[]
  def hooked(m,r):
   self.cont=sparse.csr_matrix(m);self.rhs=np.asarray(r,float).copy()
   with warnings.catch_warnings(record=True) as got:
    warnings.simplefilter('always'); raw=old(m,r)
   for w in got:
    warning.append({'category':w.category.__name__,'message':str(w.message)})
    warnings.showwarning(w.message,w.category,w.filename,w.lineno)
   self.raw=np.asarray(raw,float).copy();return raw
  ex.linalg.spsolve=hooked
  try:
   result=original()
   if self._is_singularity(warning):
    self.persist(warning,'KFE solve returned after a singularity signal.\n'+''.join(traceback.format_stack()))
    raise FirstSingularityCaptured('first KFE singularity captured; child must stop')
   return result
  except Exception:
   if not self.done and self._is_singularity(warning):
    self.persist(warning,traceback.format_exc())
    raise FirstSingularityCaptured('first KFE singularity captured; child must stop')
   raise
  finally:ex.linalg.spsolve=old
 def _is_singularity(self,warn):
  return hasattr(self,'raw') and (any(x['category']=='MatrixRankWarning' for x in warn) or not np.isfinite(self.raw).all())
 def persist(self,warn,trace):
  if self.done:return
  # These writes deliberately precede all dense/SCC postmortem work.
  j(self.root/'first_singularity_localization.json',self.ctx);j(self.root/'first_singularity_hjb_status.json',self.hjb)
  mat(self.root/'first_singularity_operator_A.npz',self.a);mat(self.root/'first_singularity_operator_transpose.npz',self.at);mat(self.root/'first_singularity_contaminated_matrix.npz',self.cont);arr(self.root/'first_singularity_rhs.npy',self.rhs);arr(self.root/'first_singularity_raw_solve_vector.npy',self.raw)
  txt(self.root/'first_singularity_warning_and_traceback.txt','warning_records='+json.dumps(warn,ensure_ascii=False,sort_keys=True)+'\n\n'+trace)
  self.done=True
def recompute_phi_destination_origin(snapshot,phi):
 prod=np.array([float(state['Yt'])/float(state['Lt']) for state in snapshot])
 phi[:]=1+0.3*(prod[:,None]-prod[None,:])/(prod[:,None]+prod[None,:])
 return phi
def production_literal_at_tax(grid,state,result):
 rah=float(state['rah']);effective=faithful.matlab_faithful_illiquid_return(grid.a,grid.a[-1],rah)
 return result.aggregates.a_ss*rah-float(np.sum(grid.a[None,:,None]*effective[None,:,None]*result.kfe.density)*result.kfe.cell_weight)
def pre_frozen_household_output_batch(grid,completed,iteration):
 outputs=[]
 for state,result in completed:
  aggregate=result.aggregates
  outputs.append((aggregate.c_ss,aggregate.l_ss,aggregate.a_ss,aggregate.b_ss,production_literal_at_tax(grid,state,result),result.hjb.converged,result.hjb.iterations,result.hjb.convergence_statistic))
 return PreFrozenHouseholdOutputBatch(ct=[x[0] for x in outputs],household_lt=[x[1] for x in outputs],at=[x[2] for x in outputs],bt=[x[3] for x in outputs],at_tax=[x[4] for x in outputs],converged=tuple(x[5] for x in outputs),diagnostics=tuple({'hjb_converged':x[5],'hjb_iterations':x[6],'hjb_statistic':x[7],'iteration':iteration} for x in outputs))
def normal_completion_summary(root,result,household_call_count,province_order):
 order=tuple(province_order)
 if not result.converged or result.termination_reason!=TERMINATION_CONVERGED:raise ValueError('normal completion requires accepted source convergence')
 if int(result.iteration_count)<1 or len(result.history)!=int(result.iteration_count) or int(household_call_count)!=len(order)*int(result.iteration_count):raise ValueError('normal completion iteration or household-call contract failed')
 if tuple(str(state['name']) for state in result.final_state)!=order:raise ValueError('normal completion province order mismatch')
 rows=serialize_final_state(result.final_state);last=result.history[-1]
 scalars=(last.household_converged_count,last.ra_upper_count,last.ra_lower_count,last.wage_upper_count,last.wage_lower_count,float(np.max(last.nk_ratio_gap)),float(np.max(last.yt_gap)))
 if not np.isfinite(scalars).all():raise ValueError('normal completion diagnostics are non-finite')
 payload={'schema':'MP4C_2018_NORMAL_COMPLETION_SUMMARY_V1','converged':bool(result.converged),'termination_reason':result.termination_reason,'iteration_count':int(result.iteration_count),'household_call_count':int(household_call_count),'household_converged_count':int(last.household_converged_count),'ra_upper_count':int(last.ra_upper_count),'ra_lower_count':int(last.ra_lower_count),'wage_upper_count':int(last.wage_upper_count),'wage_lower_count':int(last.wage_lower_count),'max_final_nk_ratio_gap':float(np.max(last.nk_ratio_gap)),'max_final_yt_gap':float(np.max(last.yt_gap)),'province_order':list(order),'final_31x20':rows,'final_state_fields':list(FINAL_FIELDS)}
 path=Path(root)/'normal_completion_summary.json';j(path,payload);return sha(path)
def run(inp,root):
 root=Path(root)
 allowed={'durable_execution_preflight.json','diagnostic_child_launch_receipt.json','first_singularity_stdout.log','first_singularity_stderr.log'}
 if root.exists() and any(p.name not in allowed for p in root.iterdir()):raise FileExistsError(root)
 root.mkdir(exist_ok=True); raw=Path(inp).read_bytes();
 if hashlib.sha256(raw).hexdigest().upper()!=EXPECTED:raise ValueError('input SHA mismatch')
 payload=json.loads(raw);owner_a.validate(payload)
 if payload['binding']!={'steady_state_calendar_year':2018,'rolling_window_entry_index':10,'regression_vintage_index':19,'calendar_level_row_index':19,'rolling_window_start_year':2009,'rolling_window_end_year':2018}:raise ValueError('input binding mismatch')
 j(root/'input_2018_identity.json',{'path':str(Path(inp)),'sha256':EXPECTED,'bytes':len(raw),'binding':payload['binding'],'source_fields':payload['source_fields'],'scalars':payload['scalars'],'no_2023_scientific_input':True})
 j(root/'scientific_code_identity_manifest.json',{str(p.relative_to(ROOT)).replace('\\','/'):sha(p) for p in (ROOT/'exports/matlab_faithful_two_asset_ha.py',ROOT/'validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py',ROOT/'src/ch5_two_asset_hank/multi_province/stationary_runtime.py',Path(__file__))})
 cap=Capture(root);ledger=(root/'household_call_ledger.csv').open('x',encoding='utf-8',newline='');hjb_ledger=DurableCsvLedger(root/'hjb_return_ledger.csv');writer=None;calls=0
 grid=anchor.MatlabFaithfulHJBGrid(np.linspace(-2,5,20),np.linspace(0,10,20),np.array([.8,1.3]),np.array([[-1/3,1/3],[1/3,-1/3]]));params=anchor.EconomicParams(.05,2.,5.,.1,2.,1e-6,0.,0.);num=anchor.MatlabFaithfulHJBNumerics(1000.,1e-7,100,1e-12);states=owner_a.entry_states(payload,asdict(empirical.accepted_source_scalars()));phi=np.ones((31,31))
 def batch(snapshot,iteration):
  nonlocal calls,writer
  recompute_phi_destination_origin(snapshot,phi)
  out=[]
  for ix,state in enumerate(snapshot):
   calls+=1;cap.ctx={'outer_iteration':iteration,'province_index_0based':ix,'province':str(state['name']),'global_household_call_number':calls,**{k:float(state[k]) for k in ('rah','rb','tau','w','Tt','rb_gap','Yt','Lt','Kt','Zt','GovInv')}}
   if writer is None:writer=csv.DictWriter(ledger,fieldnames=list(cap.ctx));writer.writeheader()
   writer.writerow(cap.ctx);ledger.flush();os.fsync(ledger.fileno())
   initial,labor=anchor._source_initial_arrays(state,grid,params)
   def hs(*args):
    h=faithful.solve_matlab_faithful_hjb(*args);cap.hjb={'hjb_converged':bool(h.converged),'hjb_iterations':h.iterations,'hjb_convergence_statistic':h.convergence_statistic,'kfe_path':'HJB_CONVERGED' if h.converged else 'MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE'}
    hjb_row={**cap.ctx,**cap.hjb}
    hjb_ledger.append(hjb_row)
    return h
   def ks(a,**kw):cap.before(a);return cap.solve(lambda:faithful.solve_matlab_faithful_stationary_kfe(a,**kw))
   r=solve_matlab_source_postloop_household(grid,params,anchor.HouseholdInputs(float(state['rah']),float(state['rb']),float(state['tau']),np.array([state['w']]),np.array([0.]),np.array([1.])),initial,labor,float(state['Tt']),float(state['rb_gap']),num,hjb_solver=hs,kfe_solver=ks);out.append((state,r))
  return pre_frozen_household_output_batch(grid,out,iteration)
 terminal='COMPLETED_WITHOUT_FIRST_SINGULARITY';failure=None;normal_summary_sha256=None
 try:
  result=run_online_stationary(OnlineStationaryInputs(tuple(payload['province_order']),states,{'ga':2.,'phi_l':5.,'alphal':1.,'epsilon':10.,'theta':100.,'delta':.025,'istar':.015,'rho_pi':1.25,'totalpit':.02,'epsilon_pi':0.},phi,np.array(payload['runtime_support']['sigmau_destination_origin']),batch,1e-9,empirical.MAX_OUTER_TURNS,True))
  normal_summary_sha256=normal_completion_summary(root,result,calls,payload['province_order']);terminal='COMPLETED_SOURCE_CONVERGED'
 except FirstSingularityCaptured:
  terminal='FIRST_SINGULARITY_CAPTURED_FAIL_CLOSED'
 except BaseException as exc:
  terminal='UNHANDLED_EXCEPTION';failure=exc;txt(root/'diagnostic_child_unhandled_traceback.txt',traceback.format_exc())
 finally:ledger.close();hjb_ledger.close()
 j(root/'diagnostic_execution_receipt.json',{'year':2018,'subprocesses':1,'workers':1,'automatic_reruns':0,'household_calls_started':calls,'first_capture':cap.done,'normal_completion_summary_sha256':normal_summary_sha256,'child_terminal_status':terminal,'thread_environment':ENV});j(root/'zero_or_bounded_science_ledger.json',{'phase_a_science_calls':0,'diagnostic_run_count':1,'household_calls_started':calls,'reruns':0});j(root/'diagnostic_child_terminal_sentinel.json',{'child_terminal_status':terminal,'first_capture':cap.done,'normal_completion_summary_sha256':normal_summary_sha256,'household_calls_started':calls})
 if failure is not None:raise failure
def postmortem(root):
 root=Path(root);required=('first_singularity_operator_A.npz','first_singularity_operator_transpose.npz','first_singularity_contaminated_matrix.npz','first_singularity_rhs.npy','first_singularity_raw_solve_vector.npy')
 if not all((root/x).is_file() for x in required):raise FileNotFoundError('raw first-singularity evidence incomplete')
 a=sparse.load_npz(root/required[0]);at=sparse.load_npz(root/required[1]);cont=sparse.load_npz(root/required[2]);rhs=np.load(root/required[3]);raw=np.load(root/required[4]);operator=summary(a);row=np.flatnonzero(rhs)
 j(root/'postmortem_operator_summary.json',operator)
 j(root/'postmortem_scc_closed_classes.json',{k:operator[k] for k in ('graph_threshold','scc_count','closed_scc_count','closed_sccs','multiple_closed_sccs','zero_outflow_states','isolated_states','state_index_order')})
 j(root/'postmortem_rank_nullity.json',{'transpose':svd(at),'contaminated_matrix':svd(cont),'contaminated_row_indices_0based':row.tolist(),'rhs_nonzero_values':[float(rhs[x]) for x in row],'raw_nonfinite_count':int(np.count_nonzero(~np.isfinite(raw)))})
def phase(root):
 root=Path(root);root.mkdir(exist_ok=True);d=root/'phase_a_dummy';d.mkdir(exist_ok=False)
 a=sparse.csr_matrix([[-1.,1.,0.],[0.,-1.,1.],[0.,0.,0.]]);c=Capture(d);c.ctx={'outer_iteration':0,'province_index_0based':0,'province':'DUMMY','global_household_call_number':1};c.hjb={'hjb_converged':False,'hjb_iterations':100,'hjb_convergence_statistic':1.,'kfe_path':'MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE'};c.before(a);c.cont=a.transpose().tolil();c.cont[0,:]=0.;c.cont[0,0]=1.;c.cont=c.cont.tocsr();c.rhs=np.array([.007,0.,0.]);c.raw=np.array([np.nan,0.,0.]);c.persist([{'category':'MatrixRankWarning','message':'dummy exactly singular'}],'dummy zero-science capture')
 required=('first_singularity_operator_A.npz','first_singularity_operator_transpose.npz','first_singularity_contaminated_matrix.npz','first_singularity_rhs.npy','first_singularity_raw_solve_vector.npy','first_singularity_warning_and_traceback.txt')
 if not all((d/x).is_file() for x in required):raise RuntimeError('phase A persistence failure')
 grid=faithful.MatlabFaithfulHJBGrid(np.array([0.,7.]),np.array([0.,10.]),np.array([.8,1.3]),np.array([[-1/3,1/3],[1/3,-1/3]]));seen=[];op=type('O',(),{'full':sparse.eye(8,format='csr')})();hjb_ledger=DurableCsvLedger(root/'hjb_return_ledger.csv');contexts=[{'outer_iteration':1,'province_index_0based':0,'province':'DUMMY_A','global_household_call_number':1,'rah':.09,'rb':.02,'tau':.05,'w':20.,'Tt':.1,'rb_gap':.07,'Yt':1000.,'Lt':100.,'Kt':500.,'Zt':1.,'GovInv':500.},{'outer_iteration':1,'province_index_0based':1,'province':'DUMMY_B','global_household_call_number':2,'rah':.09,'rb':.02,'tau':.05,'w':20.,'Tt':.1,'rb_gap':.07,'Yt':1001.,'Lt':101.,'Kt':501.,'Zt':1.1,'GovInv':501.}]
 def dh(*args):
  index=sum(x=='hjb' for x in seen);status={'hjb_converged':index==0,'hjb_iterations':11+index,'hjb_convergence_statistic':.001*(index+1),'kfe_path':'HJB_CONVERGED' if index==0 else 'MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE'};hjb_ledger.append({**contexts[index],**status});seen.append('hjb');return type('H',(),{'post_convergence_operator':op,'consumption':np.ones((2,2,2)),'labor':np.ones((2,2,2))})()
 def dk(x,*,shape,db,da):
  rows=list(csv.DictReader((root/'hjb_return_ledger.csv').open(encoding='utf-8')));assert x is op.full and shape==(2,2,2) and db==7 and da==10 and len(rows)==sum(item=='hjb' for item in seen) and rows[-1]['province']==contexts[-1 if len(rows)==2 else 0]['province'];seen.append('kfe');return type('K',(),{'density':np.ones((2,2,2))})()
 def agg(*args):seen.append('aggregate');return type('G',(),{})()
 try:
  solve_matlab_source_postloop_household(grid,None,None,None,None,0.,0.,None,hjb_solver=dh,kfe_solver=dk,aggregator=agg);solve_matlab_source_postloop_household(grid,None,None,None,None,0.,0.,None,hjb_solver=dh,kfe_solver=dk,aggregator=agg)
 finally:hjb_ledger.close()
 if seen!=['hjb','kfe','aggregate','hjb','kfe','aggregate']:raise RuntimeError('dummy adapter injection flow failed')
 header,first,second=(root/'hjb_return_ledger.csv').read_text(encoding='utf-8').splitlines()
 if header.split(',').count('province')!=1 or len((header,first,second))!=3:raise RuntimeError('dummy HJB ledger header/row count failed')
 j(root/'phase_a_zero_science_test_receipt.json',{'marker':'MP4C_2018_HJB_LEDGER_CLOSURE_REPAIR_ZERO_SCIENCE_PASS__ONE_DURABLE_2018_CHILD_AUTHORIZED','dummy_matrix_only':True,'actual_production_grid_interface':True,'adapter_dummy_sequence':seen,'hjb_ledger_header_count':1,'hjb_ledger_row_count':2,'first_hjb_row_context':contexts[0],'second_hjb_row_context':contexts[1],'faithful_hjb_identity':faithful.solve_matlab_faithful_hjb.__module__,'faithful_kfe_identity':faithful.solve_matlab_faithful_stationary_kfe.__module__,'scientific_calls':{'stationary':0,'household':0,'HJB':0,'KFE':0,'MATLAB':0,'R_PLM':0},'no_overwrite_verified':True,'required_files':list(required)})
def main():
 p=argparse.ArgumentParser();p.add_argument('input',nargs='?');p.add_argument('root');p.add_argument('--phase-a',action='store_true');p.add_argument('--postmortem',action='store_true');a=p.parse_args();[os.environ.__setitem__(k,v) for k,v in ENV.items()]
 if a.phase_a:phase(a.root)
 elif a.postmortem:postmortem(a.root)
 elif a.input is None:p.error('input is required unless --phase-a or --postmortem is selected')
 else:run(a.input,a.root)
if __name__=='__main__':main()
