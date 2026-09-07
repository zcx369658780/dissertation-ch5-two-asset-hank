"""External exact-MAT, one-iteration capture fork of accepted Python HJB body."""
import hashlib,json,sys,time
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.io import loadmat
from scipy.sparse import linalg
ROOT=Path(__file__).parent; REPO=Path('D:\\ProjectTemp\\ch5-astra-local-doc-sync-20260907-001'); MAT=Path(r'D:\ProjectTemp\ch5-mp4c-2018-call725-matlab-termination-replay-after-path-recertification-20260904-001\hjb100_initialization.mat')
sys.path[:0]=[str(REPO/'src'),str(REPO)]
from exports.matlab_faithful_two_asset_ha import EconomicParams,HouseholdInputs,MatlabFaithfulHJBGrid,MatlabFaithfulHJBNumerics,select_matlab_faithful_local_policy,assemble_source_operator
def sha(p):
 h=hashlib.sha256();
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest().upper()
def main(output_dir,binding_path,initialization_path,max_updates):
 output_dir.mkdir(parents=True,exist_ok=False)
 if not max_updates == 1: raise ValueError('update budget')
 ledger={'invocations_entered':0,'iterations_entered':0,'solves_entered':0,'completed_updates':0,'converged':False,'status':'INITIALIZING'}
 def persist(): (output_dir/'ledger.json').write_text(json.dumps(ledger,indent=2),encoding='utf-8')
 persist(); started=time.monotonic()
 m=loadmat(initialization_path,squeeze_me=False); b=m['b'].reshape(-1); a=m['ah'].reshape(-1); z=m['z'].reshape(-1); old=np.asarray(m['v0'],dtype=float).copy(); l0=np.asarray(m['l0'],dtype=float)
 if old.shape!=(20,20,2) or l0.shape!=(20,20,2) or not np.isfinite(old).all() or not np.isfinite(l0).all():raise RuntimeError('MAT input')
 binding=json.loads(binding_path.read_text(encoding='utf-8')); s=binding['scalar_binding']; p0=s['parameters']; n0=s['numerics'];
 grid=MatlabFaithfulHJBGrid(b,a,z,np.asarray(s['switch_matrix'],dtype=float)); p=EconomicParams(p0['rho'],p0['gamma_c'],p0['phi'],p0['chi_0'],p0['chi_1'],p0['a_bar'],s['fixed_source_literals']['fixcost'],s['fixed_source_literals']['fixcost2']); inp=HouseholdInputs(p0['r_a'],p0['r_b'],p0['tau'],np.array([p0['wage']]),np.array([0.]),np.array([1.])); n=MatlabFaithfulHJBNumerics(n0['delta'],n0['convergence_tolerance'],1,n0['drift_tolerance']);
 ledger['invocations_entered']=1; ledger['status']='RUNNING'; persist()
 try:
  for iteration in range(1,max_updates+1):
   if time.monotonic()-started>2650: raise TimeoutError('trajectory wall budget')
   out=output_dir/f'step_{iteration:04d}.npz'
   ledger['iterations_entered']+=1; persist()
   shape=old.shape; db=b[1]-b[0]; da=a[1]-a[0]
   vb_f=np.zeros(shape);vb_b=np.zeros(shape);va_f=np.zeros(shape);va_b=np.zeros(shape); vb_f[:-1]=(old[1:]-old[:-1])/db; vb_b[1:]=vb_f[:-1]; va_f[:,:-1]=(old[:,1:]-old[:,:-1])/da;va_b[:,1:]=va_f[:,:-1]; raw=[x.copy() for x in (vb_f,vb_b,va_f,va_b)]
   for j,_a in enumerate(a):
    for k,_z in enumerate(z):
     for i in (0,len(b)-1):
      rb=inp.r_b+(p0['borrowing_rate_gap'] if b[i]<0 else 0.); r=((1-inp.tau)*inp.wages[0]*_z*l0[i,j,k]+p0['transfer_income']+rb*b[i])**(-p.gamma_c)
      if i==0:vb_b[i,j,k]=r
      else:vb_f[i,j,k]=r
   names=('consumption','labor','transfer','adjustment_cost','effective_illiquid_return','mu_a','mu_b','utility'); arrays={x:np.empty(shape) for x in names}; liquid=np.empty(shape,dtype='U1'); tl=np.empty(shape,dtype='U1'); bb=np.empty(shape);bf=np.empty(shape);ab=np.empty(shape);af=np.empty(shape)
   for k,zz in enumerate(z):
    for j,aa in enumerate(a):
     for i,bbv in enumerate(b):
      q=select_matlab_faithful_local_policy(a=float(aa),b=float(bbv),z=float(zz),v_a_forward=float(va_f[i,j,k]),v_a_backward=float(va_b[i,j,k]),v_b_forward=float(vb_f[i,j,k]),v_b_backward=float(vb_b[i,j,k]),baseline_labor=float(l0[i,j,k]),transfer_income=p0['transfer_income'],borrowing_rate_gap=p0['borrowing_rate_gap'],a_max=float(a[-1]),da=float(da),db=float(db),at_lower_a=j==0,at_upper_a=j+1==len(a),at_lower_b=i==0,at_upper_b=i+1==len(b),inputs=inp,params=p,tolerance=n.drift_tolerance)
      for x in names:arrays[x][i,j,k]=getattr(q,x)
      liquid[i,j,k]=q.liquid_label;tl[i,j,k]=q.transfer_label;bb[i,j,k]=q.iteration_b_backward_rate;bf[i,j,k]=q.iteration_b_forward_rate;ab[i,j,k]=q.a_backward_rate;af[i,j,k]=q.a_forward_rate
   op=assemble_source_operator(bb,bf,ab,af,grid.switch_matrix); M=(1/n.delta+p.rho)*sparse.eye(800,format='csr')-op.full; rhs=arrays['utility'].ravel(order='F')+old.ravel(order='F')/n.delta; ledger['solves_entered']+=1; persist(); v1=linalg.spsolve(M,rhs).reshape(shape,order='F')
   np.savez_compressed(out,old=old,l0=l0,b=b,a=a,z=z,rhs=rhs,raw_vb_f=raw[0],raw_vb_b=raw[1],raw_va_f=raw[2],raw_va_b=raw[3],vb_f=vb_f,vb_b=vb_b,va_f=va_f,va_b=va_b,liquid_label=liquid,transfer_label=tl,bb=bb,bf=bf,ab=ab,af=af,v1=v1,statistic=np.array([np.max(abs(v1-old))]),**arrays)
   sparse.save_npz(str(out).replace('.npz','_BB.npz'),op.bb);sparse.save_npz(str(out).replace('.npz','_AAH.npz'),op.aah);sparse.save_npz(str(out).replace('.npz','_Bswitch.npz'),op.bswitch);sparse.save_npz(str(out).replace('.npz','_A.npz'),op.full);sparse.save_npz(str(out).replace('.npz','_M.npz'),M)
   core=np.load(out); assert core['rhs'].shape==(800,) and core['v1'].shape==(20,20,2) and np.array_equal(core['v1'],v1); assert sparse.load_npz(str(out).replace('.npz','_M.npz')).shape==(800,800)
   v1_vec=v1.reshape(-1,order='F'); res=float(np.max(np.abs(M@v1_vec-rhs))); np.savez_compressed(str(out).replace('.npz','_diagnostics.npz'),v1_vec=v1_vec,residual_inf=np.array([res]))
   ledger['completed_updates']+=1
   finite=all(np.isfinite(x).all() for x in [old,v1,rhs,bb,bf,ab,af,*arrays.values(),op.full.data,M.data])
   statistic=float(np.max(abs(v1-old))); ledger['statistic']=statistic if np.isfinite(statistic) else None
   ledger['converged']=bool(finite and statistic<n.convergence_tolerance)
   trace={'iteration':iteration,'statistic':ledger['statistic'],'finite':bool(finite),'converged':ledger['converged'],'diagnostic_continuation':iteration>100,'value_min':float(np.min(v1)) if finite else None,'value_max':float(np.max(v1)) if finite else None}
   with (output_dir/'trace.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps(trace,allow_nan=False)+'\n'); f.flush()
   persist()
   print(json.dumps(trace),flush=True)
   if not finite: ledger['status']='NONFINITE'; break
   if ledger['converged']: ledger['status']='CONVERGED'; break
   old=v1.copy()
  else: ledger['status']='MAX_UPDATES'
 except BaseException as exc:
  ledger['status']='FAILED'; ledger['error']=repr(exc); raise
 finally:
  persist()
if __name__=='__main__': main(Path(sys.argv[1]),Path(sys.argv[2]),Path(sys.argv[3]),int(sys.argv[4]))
