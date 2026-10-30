"""R4: one supervised read-only diagnostic of four authenticated R3 archives.
No model imports, policy selection, initialization, operator generation or solves.
All state indices are zero based; flattening is Fortran (b,a,z).
"""
from __future__ import annotations
import hashlib,json,os,sys
from pathlib import Path
THREAD_KEYS=('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS','BLIS_NUM_THREADS')
TASK='CH5_TEMP31_R3_E03_E04_ARCHIVED_POLICY_DRIFT_POSTG_DIAGNOSTIC_R4_20261030'
WORK=Path(__file__).resolve().parents[2];REPORT=WORK/'tasks'/TASK
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def dump(name,x):
 with (REPORT/name).open('x',encoding='utf-8',newline=chr(10)) as f:json.dump(x,f,indent=2,allow_nan=False);f.write(chr(10))
def sha(b):return hashlib.sha256(b).hexdigest()
def safe(p):
 for q in [p,*p.parents]:assert not os.lstat(q).st_file_attributes&1024,'UNSAFE_ARCHIVE_PATH'
def main():
 assert sys.stdin.buffer.readline()==b'GO'+bytes([10]),'SUPERVISOR_HANDSHAKE_REQUIRED'
 assert all(os.environ.get(k)=='1' for k in THREAD_KEYS)
 assert read(REPORT/'evidence/LOCAL_ONLY_preflight_pass.json')['passed']
 import numpy as np
 import scipy
 from scipy.sparse import csr_matrix
 auth=read(REPORT/'archive_authentication.json');inv=read(REPORT/'npz_member_inventory.json')
 assert auth['passed'] and len(auth['archives'])==4
 data={};before={}
 for row in auth['archives']:
  p=WORK/row['task_relative_path'];safe(p);raw=p.read_bytes()
  assert len(raw)==row['bytes'] and sha(raw)==row['sha256']
  key=(row['point'],row['kind']);members=next(r['members'] for r in inv['inventory'] if (r['point'],r['kind'])==key)
  with np.load(p,allow_pickle=False) as z:
   assert set(z.files)=={m['member'][:-4] for m in members}
   arrays={}
   for m in members:
    name=m['member'][:-4];x=z[name]
    assert list(x.shape)==m['shape'] and x.dtype.str==m['dtype'] and not x.dtype.hasobject and np.isfinite(x).all()
    x.flags.writeable=False;arrays[name]=x
   data[key]=arrays
   before[row['task_relative_path']]=dict(file_sha256=sha(raw),arrays={n:sha(x.tobytes(order='F')) for n,x in arrays.items()})
 b=np.linspace(-2.,5.,20);a=np.linspace(0.,10.,20);z=np.array([.8,1.3]);weight=(7/19)*(10/19)
 bi,ai,zi=np.unravel_index(np.arange(800),(20,20,2),order='F');bv=b[bi];av=a[ai]
 masks={}
 for name,ix in (('b',bi),('a',ai)):
  masks[name+'_lower']=ix==0;masks[name+'_interior']=(ix>0)&(ix<19);masks[name+'_upper']=ix==19
 masks['z0']=zi==0;masks['z1']=zi==1;masks['high_b_last4']=bi>=16;masks['a_lower_near_first2']=ai<=1
 joint={}
 for bn,bm in [('lower',bi==0),('interior',(bi>0)&(bi<19)),('upper',bi==19)]:
  for an,am in [('lower',ai==0),('interior',(ai>0)&(ai<19)),('upper',ai==19)]:
   for k in (0,1):joint['b_'+bn+'__a_'+an+'__z'+str(k)]=bm&am&(zi==k)
 def flat(x):return x.ravel(order='F')
 def norm(x):return float(np.max(np.abs(x))) if np.size(x) else 0.
 def stats(x):
  x=np.asarray(x)
  return dict(count=int(x.size),min=float(x.min()) if x.size else None,max=float(x.max()) if x.size else None,mean_signed=float(x.mean()) if x.size else None,mean_absolute=float(np.abs(x).mean()) if x.size else None,max_absolute=norm(x),sum=float(x.sum()),quantiles=dict(zip(('q0','q10','q25','q50','q75','q90','q100'),[float(v) for v in np.quantile(x,[0,.1,.25,.5,.75,.9,1])])) if x.size else {})
 def grouped(x,groups=masks):return {k:stats(x[m]) for k,m in groups.items()}
 def state(i):return dict(index0=int(i),b_index0=int(bi[i]),a_index0=int(ai[i]),z_index0=int(zi[i]),b=float(bv[i]),a=float(av[i]),z=float(z[zi[i]]))
 def top(x):
  # Only three positive and three negative archived-state locations per quantity.
  pos=np.flatnonzero(x>0);neg=np.flatnonzero(x<0)
  return dict(positive=[dict(**state(i),contribution=float(x[i])) for i in pos[np.argsort(x[pos])[-3:][::-1]]],negative=[dict(**state(i),contribution=float(x[i])) for i in neg[np.argsort(x[neg])[:3]]])
 expected={'E03':('aca1857db0415b5df48df5722ad54e55e609740eaed51a4d8b1e7364598d1a85','6f80f95f976d76ca3432aace8edc45e1edc820b50cfe9d2b8973432b57ab3b72'),'E04':('45a872e8b7808b7d04729b09ba41c076def94474afe018dce23cfbee787fe97b','57d6579203f030c0fb869dd39e2d4af4195023c2817864b986528bd0390d1d3e')}
 matrices={};matrix_records={}
 def matrix_metrics(M):
  co=M.tocoo(copy=True);off=co.row!=co.col;rows=np.asarray(M.sum(axis=1)).ravel();neg=off&(co.data<0)
  grouped_rows={}
  for label,mask in masks.items():
   grouped_rows[label]=dict(row_count=int(mask.sum()),row_sums=stats(rows[mask]),negative_offdiagonal_entries=int((neg&mask[co.row]).sum()),stored_entries=int(mask[co.row].sum()))
  return dict(shape=list(M.shape),stored_nnz=int(M.nnz),numerical_nonzero=int(np.count_nonzero(M.data)),max_absolute=norm(M.data),row_sums=stats(rows),negative_offdiagonal_count=int(neg.sum()),min_offdiagonal_including_implicit_zeros=min(0.,float(co.data[off].min())) if off.any() else 0.,by_source_row=grouped_rows)
 for point in ('E03','E04'):
  h=data[(point,'arrays_and_rates')]
  for j,phase in enumerate(('iteration_G','post_G')):
   values=h[phase+'_data'];indices=h[phase+'_indices'];ptr=h[phase+'_indptr']
   assert values.ndim==indices.ndim==ptr.ndim==1 and values.size==indices.size and ptr.shape==(801,)
   assert ptr[0]==0 and ptr[-1]==values.size and (np.diff(ptr)>=0).all() and (indices>=0).all() and (indices<800).all()
   identity=sha(ptr.tobytes()+indices.tobytes()+values.tobytes());assert identity==expected[point][j]
   M=csr_matrix((values.copy(),indices.copy(),ptr.copy()),shape=(800,800),copy=True);M.check_format(full_check=True)
   matrices[(point,phase)]=M;name=point+'_'+phase
   matrix_records[name]=dict(evidence='DIRECT_ARCHIVE_OBSERVATION',original_CSR_SHA256=identity,original_order_preserved=True,sorted_indices=bool(M.has_sorted_indices),canonical_format=bool(M.has_canonical_format),**matrix_metrics(M))
 differences={}
 for name,left,right in [('E03_post_minus_iteration',('E03','post_G'),('E03','iteration_G')),('E04_post_minus_iteration',('E04','post_G'),('E04','iteration_G')),('E04_post_minus_E03_post',('E04','post_G'),('E03','post_G'))]:
  D=matrices[left]-matrices[right];D.eliminate_zeros();co=D.tocoo();ix=np.argsort(np.abs(co.data))[-3:][::-1]
  differences[name]=dict(evidence='PURE_ARCHIVE_ALGEBRA',**matrix_metrics(D),top_absolute_changes=[dict(source=state(co.row[i]),destination=state(co.col[i]),change=float(co.data[i])) for i in ix])
 fields={};h3=data[('E03','arrays_and_rates')];h4=data[('E04','arrays_and_rates')]
 def signs(x):return np.where(x>1e-12,1,np.where(x< -1e-12,-1,0))
 def transitions(s,t,m):
  return {str(i)+'_to_'+str(j):int(((s==i)&(t==j)&m).sum()) for i in (-1,0,1) for j in (-1,0,1)}
 for name in ('value','consumption','labor','utility','mu_a','mu_b','b_backward','b_forward','a_backward','a_forward'):
  x=flat(h3[name]);y=flat(h4[name]);diff=y-x
  fields[name]=dict(evidence='PURE_ARCHIVE_ALGEBRA',E03=stats(x),E04=stats(y),E04_minus_E03=stats(diff),difference_by_group=grouped(diff))
  if name in ('mu_a','mu_b'):
   s=signs(x);t=signs(y)
   fields[name]['sign_tolerance']=1e-12;fields[name]['sign_transitions']=transitions(s,t,np.ones(800,dtype=bool))
   fields[name]['sign_transitions_by_group']={label:transitions(s,t,m) for label,m in {**masks,**joint}.items()}
  if name.endswith(('backward','forward')):
   fields[name]['E03_by_group']=grouped(x);fields[name]['E04_by_group']=grouped(y)
   fields[name]['meaning']='saved last HJB iteration rates; not recomputed post policy'
 point_checks={};residuals={};masses={}
 for point in ('E03','E04'):
  h=data[(point,'arrays_and_rates')];k=data[(point,'KFE_density')];g=k['density'];gv=flat(g);mass=g*weight;mf=flat(mass);masses[point]=mf
  published=read(WORK/('tasks/CH5_TEMP31_MATLAB800_PRICE_NEIGHBORHOOD_DISTRIBUTION_SWITCH_R3_20261030/evidence/'+point+'_result.json'))['KFE']
  am=mass.sum(axis=(0,2));bm=mass.sum(axis=(1,2));zm=mass.sum(axis=(0,1))
  calc=dict(At=float((g*a[None,:,None]).sum()*weight),Bt=float((g*b[:,None,None]).sum()*weight),Lt=float((g*h['labor']*z[None,None,:]).sum()*weight),Ct=float((g*h['consumption']).sum()*weight),total_probability=float(mass.sum()),negative_probability_mass=float(np.maximum(-g,0).sum()*weight),negative_density_cells=int((g<0).sum()),density_min=float(g.min()),density_max=float(g.max()),a_lower_mass=float(am[0]),a_upper_mass=float(am[-1]),a_internal_mass=float(am[1:-1].sum()),b_lower_mass=float(bm[0]),b_upper_mass=float(bm[-1]),b_internal_mass=float(bm[1:-1].sum()))
  errors={name:abs(v-published[name]) for name,v in calc.items()};assert max(errors.values())<=1e-12
  marginal_errors=dict(a_vs_archive=norm(am-k['a_mass']),b_vs_archive=norm(bm-k['b_mass']),a_vs_published=norm(am-np.array(published['a_mass20'])),b_vs_published=norm(bm-np.array(published['b_mass20'])))
  assert max(marginal_errors.values())<=1e-12
  normalization_error=norm(flat(k['raw'])/published['normalization_factor']-gv);assert normalization_error<=1e-12
  point_checks[point]=dict(evidence='PURE_ARCHIVE_ALGEBRA',recomputed=calc,absolute_errors_vs_R3=errors,marginal_absolute_max_errors=marginal_errors,a_mass20=am.tolist(),b_mass20=bm.tolist(),z_mass2=zm.tolist(),raw_to_density_normalization_error=normalization_error,source_KFE_status=published['status'],source_method_previously_executed=published['source_method_executed'],strict_stationarity_certified=False)
  M=matrices[(point,'post_G')];rr=np.asarray(M.sum(axis=1)).ravel();r=M.T@gv;loss=gv*rr;lhs=float(r.sum());rhs=float(gv@(M@np.ones(800)));err=abs(lhs-rhs)
  assert np.isfinite(r).all() and err<=1e-12
  rrcheck=dict(stationary_residual_abs_error=abs(norm(r)-published['stationary_residual']),pin295_abs_error=abs(float(r[295])-published['original_residual_at_pin_row295']),other799_abs_error=abs(norm(np.delete(r,295))-published['non_pin799_residual_max']))
  assert max(rrcheck.values())<=1e-12
  residuals[point]=dict(evidence='PURE_ARCHIVE_ALGEBRA',original_stationarity_inf=norm(r),destination_equation_pin295=dict(**state(295),residual=float(r[295])),other799_inf=norm(np.delete(r,295)),source_row_pin295_row_sum=float(rr[295]),source_row_pin295_g_row_sum=float(loss[295]),source_rows_nonconserving_count_tol1e12=int((np.abs(rr)>1e-12).sum()),source_loss_contributions=stats(loss),source_loss_contributions_mass_weighted=stats(loss*weight),loss_by_source_row_group=grouped(loss),loss_by_disjoint_joint_partition=grouped(loss,joint),mass_weighted_loss_by_disjoint_joint_partition=grouped(loss*weight,joint),top_source_row_loss=top(loss),destination_residual_top=top(r),sum_destination_residual=lhs,sum_source_g_rowsum=float(loss.sum()),g_dot_Gones=rhs,identity_abs_error=err,mass_weighted_sum_residual=lhs*weight,mass_weighted_g_dot_Gones=rhs*weight,R3_residual_crosschecks=rrcheck,interpretation='destination equation residual indices differ from source-row loss origins; no solver or repair')
 dm=masses['E04']-masses['E03'];dA=dm*av;dB=dm*bv
 am3=point_checks['E03']['a_mass20'];am4=point_checks['E04']['a_mass20'];bm3=point_checks['E03']['b_mass20'];bm4=point_checks['E04']['b_mass20']
 dam=np.array(am4)-np.array(am3);dbm=np.array(bm4)-np.array(bm3)
 contrast=dict(delta_At=float(dA.sum()),delta_Bt=float(dB.sum()),delta_b_upper_mass=float(dm[bi==19].sum()),a_marginal_half_L1=float(.5*np.abs(dam).sum()),b_marginal_half_L1=float(.5*np.abs(dbm).sum()))
 frozen=dict(delta_At=2.184072629709945,delta_Bt=2.887900475653729,delta_b_upper_mass=.4393009995569363,a_marginal_half_L1=.5507289161806087,b_marginal_half_L1=.6423866234047643)
 ce={k:abs(contrast[k]-v) for k,v in frozen.items()};assert max(ce.values())<=1e-12
 redistribution=dict(evidence='PURE_ARCHIVE_ALGEBRA',distance_label='SIGNED_SOURCE_OUTPUT_DISTANCE',full800_half_L1=float(.5*np.abs(dm).sum()),signed_mass_change=float(dm.sum()),positive_mass_change=float(dm[dm>0].sum()),negative_mass_change=float(dm[dm<0].sum()),contrast=contrast,delta_a_mass20=dam.tolist(),delta_b_mass20=dbm.tolist(),delta_z_mass2=(np.array(point_checks['E04']['z_mass2'])-np.array(point_checks['E03']['z_mass2'])).tolist(),mass_change_by_group=grouped(dm),mass_change_by_disjoint_joint_partition=grouped(dm,joint),delta_At_by_group=grouped(dA),delta_Bt_by_group=grouped(dB),delta_At_by_disjoint_joint_partition=grouped(dA,joint),delta_Bt_by_disjoint_joint_partition=grouped(dB,joint),top_signed_mass_change=top(dm),top_At_contributions=top(dA),top_Bt_contributions=top(dB),probability_TV_certification=False)
 after={};immutability=[]
 for row in auth['archives']:
  p=WORK/row['task_relative_path'];key=(row['point'],row['kind']);after[row['task_relative_path']]=dict(file_sha256=sha(p.read_bytes()),arrays={n:sha(x.tobytes(order='F')) for n,x in data[key].items()})
  assert before[row['task_relative_path']]==after[row['task_relative_path']]
  immutability.append(dict(path=row['task_relative_path'],sha256=row['sha256'],all_array_hashes_unchanged=True))
 dump('evidence/policy_drift_metrics.json',dict(fields=fields,direction='E04 minus E03',POLICY_LABELS_NOT_ARCHIVED=True,groups='a and b masks overlap; joint partition is disjoint; high_b_last4 and a_lower_near_first2 are additional overlapping masks'))
 dump('evidence/operator_metrics.json',dict(matrices=matrix_records,differences=differences,component_BB_AAH_decomposition='NOT_AVAILABLE'))
 dump('evidence/kfe_residual_metrics.json',dict(points=residuals,nonconservation_direction='source rows; stationarity equations are destination columns of G'))
 dump('evidence/density_reallocation_metrics.json',redistribution)
 dump('numeric_crosschecks.json',dict(points=point_checks,contrast=contrast,frozen_R3= frozen,absolute_errors=ce,all_within_1e12=True,archives_unchanged=immutability,model_solver_calls=0))
 dump('evidence/LOCAL_ONLY_array_hashes_before_after.json',dict(before=before,after=after))
 print(json.dumps(dict(event='readonly_diagnostic_complete',passed=True,archives=4,numpy=np.__version__,scipy=scipy.__version__,model_solver_calls=0,diagnostic_processes=1,contrast=contrast,full800_half_L1_SIGNED_SOURCE_OUTPUT_DISTANCE=redistribution['full800_half_L1'],stationarity={p:residuals[p]['original_stationarity_inf'] for p in residuals},POLICY_LABELS_NOT_ARCHIVED=True),allow_nan=False),flush=True)
if __name__=='__main__':main()
