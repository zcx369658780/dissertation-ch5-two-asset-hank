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
from validators.multi_province.mp4b_matlab_source_postloop_household_adapter import solve_matlab_source_postloop_household
import exports.matlab_faithful_two_asset_ha as faithful
from ch5_two_asset_hank.multi_province.one_turn import PreFrozenHouseholdOutputBatch
from ch5_two_asset_hank.multi_province.stationary_runtime import OnlineStationaryInputs,run_online_stationary

EXPECTED='F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0'
ENV={x:'1' for x in ('OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS','NUMEXPR_NUM_THREADS')}
def sha(p):
 h=hashlib.sha256();
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest().upper()
def j(path,x):
 path=Path(path)
 with path.open('x',encoding='utf-8',newline='\n') as f:json.dump(x,f,ensure_ascii=False,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
def mat(path,m):
 if Path(path).exists():raise FileExistsError(path)
 sparse.save_npz(path,m)
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
  try:return original()
  except Exception:
   if hasattr(self,'raw') and (warning or not np.isfinite(self.raw).all()):self.persist(warning)
   raise
  finally:ex.linalg.spsolve=old
 def persist(self,warn):
  if self.done:return
  self.done=True;mat(self.root/'first_singularity_operator_A.npz',self.a);mat(self.root/'first_singularity_operator_transpose.npz',self.at);mat(self.root/'first_singularity_contaminated_matrix.npz',self.cont);np.save(self.root/'first_singularity_rhs.npy',self.rhs)
  j(self.root/'first_singularity_localization.json',self.ctx);j(self.root/'first_singularity_hjb_status.json',self.hjb)
  row=int(np.flatnonzero(self.rhs)[0]);j(self.root/'first_singularity_operator_summary.json',summary(self.a));j(self.root/'first_singularity_scc_closed_classes.json',summary(self.a));j(self.root/'first_singularity_rank_nullity.json',{'transpose':svd(self.at),'contaminated_matrix':svd(self.cont),'contaminated_row_index_0based':row,'rhs_value':float(self.rhs[row]),'warning_records':warn,'raw_nonfinite_count':int(np.count_nonzero(~np.isfinite(self.raw)))} )
def run(inp,root):
 root=Path(root)
 allowed={'phase_a_dummy','phase_a_zero_science_test_receipt.json','first_singularity_stdout.log','first_singularity_stderr.log'}
 if root.exists() and any(p.name not in allowed for p in root.iterdir()):raise FileExistsError(root)
 root.mkdir(exist_ok=True); raw=Path(inp).read_bytes();
 if hashlib.sha256(raw).hexdigest().upper()!=EXPECTED:raise ValueError('input SHA mismatch')
 payload=json.loads(raw);owner_a.validate(payload)
 if payload['binding']!={'steady_state_calendar_year':2018,'rolling_window_entry_index':10,'regression_vintage_index':19,'calendar_level_row_index':19,'rolling_window_start_year':2009,'rolling_window_end_year':2018}:raise ValueError('input binding mismatch')
 j(root/'input_2018_identity.json',{'path':str(Path(inp)),'sha256':EXPECTED,'bytes':len(raw),'binding':payload['binding'],'source_fields':payload['source_fields'],'scalars':payload['scalars'],'no_2023_scientific_input':True})
 j(root/'scientific_code_identity_manifest.json',{str(p.relative_to(ROOT)).replace('\\','/'):sha(p) for p in (ROOT/'exports/matlab_faithful_two_asset_ha.py',ROOT/'validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py',ROOT/'src/ch5_two_asset_hank/multi_province/stationary_runtime.py',Path(__file__))})
 cap=Capture(root);ledger=(root/'household_call_ledger.csv').open('x',encoding='utf-8',newline='');writer=None;calls=0
 grid=anchor.MatlabFaithfulHJBGrid(np.linspace(-2,5,20),np.linspace(0,10,20),np.array([.8,1.3]),np.array([[-1/3,1/3],[1/3,-1/3]]));params=anchor.EconomicParams(.05,2.,5.,.1,2.,1e-6,0.,0.);num=anchor.MatlabFaithfulHJBNumerics(1000.,1e-7,100,1e-12);states=owner_a.entry_states(payload,asdict(empirical.accepted_source_scalars()));phi=np.ones((31,31))
 def batch(snapshot,iteration):
  nonlocal calls,writer
  out=[]
  for ix,state in enumerate(snapshot):
   calls+=1;cap.ctx={'outer_iteration':iteration,'province_index_0based':ix,'province':str(state['name']),'global_household_call_number':calls,**{k:float(state[k]) for k in ('rah','rb','tau','w','Tt','rb_gap','Yt','Lt','Kt','Zt','GovInv')}}
   if writer is None:writer=csv.DictWriter(ledger,fieldnames=list(cap.ctx));writer.writeheader()
   writer.writerow(cap.ctx);ledger.flush();os.fsync(ledger.fileno())
   initial,labor=anchor._source_initial_arrays(state,grid,params)
   def hs(*args):
    h=faithful.solve_matlab_faithful_hjb(*args);cap.hjb={'hjb_converged':bool(h.converged),'hjb_iterations':h.iterations,'hjb_convergence_statistic':h.convergence_statistic,'kfe_path':'HJB_CONVERGED' if h.converged else 'MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE'};return h
   def ks(a,**kw):cap.before(a);return cap.solve(lambda:faithful.solve_matlab_faithful_stationary_kfe(a,**kw))
   r=solve_matlab_source_postloop_household(grid,params,anchor.HouseholdInputs(float(state['rah']),float(state['rb']),float(state['tau']),np.array([state['w']]),np.array([0.]),np.array([1.])),initial,labor,float(state['Tt']),float(state['rb_gap']),num,hjb_solver=hs,kfe_solver=ks);ag=r.aggregates;out.append((ag.c_ss,ag.l_ss,ag.a_ss,ag.b_ss,0.,r.hjb.converged,r.hjb.iterations,r.hjb.convergence_statistic))
  return PreFrozenHouseholdOutputBatch(ct=[x[0] for x in out],household_lt=[x[1] for x in out],at=[x[2] for x in out],bt=[x[3] for x in out],at_tax=[x[4] for x in out],converged=tuple(x[5] for x in out),diagnostics=tuple({'hjb_converged':x[5],'hjb_iterations':x[6],'hjb_statistic':x[7],'iteration':iteration} for x in out))
 try:run_online_stationary(OnlineStationaryInputs(tuple(payload['province_order']),states,{'ga':2.,'phi_l':5.,'alphal':1.,'epsilon':10.,'theta':100.,'delta':.025,'istar':.015,'rho_pi':1.25,'totalpit':.02,'epsilon_pi':0.},phi,np.array(payload['runtime_support']['sigmau_destination_origin']),batch,1e-9,empirical.MAX_OUTER_TURNS,True))
 except Exception:
  (root/'first_singularity_traceback.txt').write_text(traceback.format_exc(),encoding='utf-8');
  if not cap.done:raise
 finally:ledger.close()
 j(root/'diagnostic_execution_receipt.json',{'year':2018,'subprocesses':1,'workers':1,'automatic_reruns':0,'household_calls_started':calls,'first_capture':cap.done,'thread_environment':ENV});j(root/'zero_or_bounded_science_ledger.json',{'phase_a_science_calls':0,'diagnostic_run_count':1,'household_calls_started':calls,'reruns':0})
def phase(root):
 root=Path(root);root.mkdir(exist_ok=True);d=root/'phase_a_dummy';d.mkdir(exist_ok=False)
 a=sparse.csr_matrix([[-1.,1.,0.],[0.,-1.,1.],[0.,0.,0.]]);c=Capture(d);c.ctx={'outer_iteration':0,'province_index_0based':0,'province':'DUMMY','global_household_call_number':1};c.hjb={'hjb_converged':False,'hjb_iterations':100,'hjb_convergence_statistic':1.,'kfe_path':'MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE'};c.before(a);c.cont=a.transpose().tolil();c.cont[0,:]=0.;c.cont[0,0]=1.;c.cont=c.cont.tocsr();c.rhs=np.array([.007,0.,0.]);c.raw=np.array([np.nan,0.,0.]);c.persist([{'category':'MatrixRankWarning','message':'dummy exactly singular'}])
 required=('first_singularity_operator_A.npz','first_singularity_operator_transpose.npz','first_singularity_contaminated_matrix.npz','first_singularity_rhs.npy','first_singularity_rank_nullity.json')
 if not all((d/x).is_file() for x in required):raise RuntimeError('phase A persistence failure')
 j(root/'phase_a_zero_science_test_receipt.json',{'dummy_matrix_only':True,'scientific_calls':{'stationary':0,'household':0,'HJB':0,'KFE':0,'MATLAB':0,'R_PLM':0},'no_overwrite_verified':True,'required_files':list(required)})
def main():
 p=argparse.ArgumentParser();p.add_argument('input',nargs='?');p.add_argument('root');p.add_argument('--phase-a',action='store_true');a=p.parse_args();[os.environ.__setitem__(k,v) for k,v in ENV.items()];phase(a.root) if a.phase_a else run(a.input,a.root)
if __name__=='__main__':main()
