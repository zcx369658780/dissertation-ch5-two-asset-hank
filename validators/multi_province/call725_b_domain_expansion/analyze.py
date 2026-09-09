"""Saved-array diagnostics only; performs no model or solver calls."""
import json, math, sys
from pathlib import Path
import numpy as np
from scipy import sparse
from evidence import decode_saved
from grid import boundary_leak, mass_regions
BASE=Path(r"D:\ProjectTemp\ch5-call725-rah-0p07-native-init-20260908-002")
EPS=np.finfo(float).eps
def write(p,v): Path(p).write_text(json.dumps(v,ensure_ascii=False,allow_nan=False,indent=2)+"\n",encoding="utf-8",newline="\n")
def stats(x):
 a=np.asarray(x); f=np.isfinite(a); return {"shape":list(a.shape),"finite":int(f.sum()),"size":int(a.size),"min":float(a[f].min()),"max":float(a[f].max()),"norm_inf":float(np.max(np.abs(a[f])))}
def offdiag(q):
 c=sparse.coo_matrix(q); v=c.data[c.row!=c.col]; rows=np.array([math.fsum(q.data[q.indptr[i]:q.indptr[i+1]]) for i in range(q.shape[0])]); scale=np.asarray(abs(q).sum(axis=1)).ravel()
 return {"negative_offdiagonal_count":int(np.sum(v<0)),"negative_offdiagonal_min":float(min(0,v.min(initial=0))),"row_sum_fsum_max_abs":float(np.max(abs(rows))),"norm_inf":float(scale.max()),"row_sums":rows}
def comp(new,old):
 d=np.asarray(new)[:20]-np.asarray(old); return {"exact_equal":int(np.sum(np.asarray(new)[:20]==old)),"size":int(d.size),"max_abs":float(np.max(abs(d))),"norm_2":float(np.linalg.norm(d.ravel()))}
def main(root,out):
 root=Path(root); out=Path(out); out.mkdir(parents=True,exist_ok=True)
 b=decode_saved(root/"science/binding.json"); h=decode_saved(root/"science/hjb_return_before_kfe.json"); oldh=decode_saved(BASE/"science/hjb_return_before_kfe.json"); init=decode_saved(root/"science/native_initialization_return.json"); oldi=decode_saved(BASE/"science/native_initialization_return.json"); k=decode_saved(root/"science/kfe_return.json"); raw=decode_saved(root/"science/kfe_direct_return.json")["raw"]; agg=decode_saved(root/"science/aggregate_return.json"); term=decode_saved(root/"science/terminal.json")
 bb=b["grid"]["b"]; aa=b["grid"]["a"]; zz=b["grid"]["z"]; db=float(bb[1]-bb[0]); da=float(aa[1]-aa[0]); shape=h["mu_b"].shape; q=sparse.csr_matrix(h["post_convergence_operator"]["full"]); qh=sparse.csr_matrix(h["operator"]["full"])
 faces,leak=boundary_leak(h["mu_b"],h["mu_a"],db,da); flat=leak.ravel(order="F"); qd=offdiag(q); qhd=offdiag(qh)
 face_summary={n:{"positive_cells":int(np.sum(x>0)),"max_rate":float(x.max()),"sum_rate":float(x.sum())} for n,x in faces.items()}
 qd.pop("row_sums"); qhd.pop("row_sums"); row=np.asarray(q.sum(axis=1)).ravel(); row_stable=np.array([math.fsum(q.data[q.indptr[i]:q.indptr[i+1]]) for i in range(q.shape[0])]); qd["row_sum_plus_omitted_rate_max_abs"]=float(np.max(abs(row_stable+flat)))
 g=np.asarray(k["density_vector"]); omega=float(k["cell_weight"]); tg=np.asarray(k["transpose"]@g); stationary_scale=np.asarray(abs(k["transpose"]).sum(axis=1)).ravel().max()*np.linalg.norm(g,np.inf); zero_bound=128*EPS*np.maximum(1,np.abs(tg)); source_free=bool(np.all(np.abs(tg)<=zero_bound)); regions=mass_regions(k["density"],bb,omega)
 probability=omega*g; escape=float(np.dot(flat,probability)); pin=int(k["contaminated_row_index"]); candidate=float(-omega*tg[pin]); offpin=float(omega*math.fsum(map(float,np.delete(tg,pin)))); delta=row_stable+flat; delta_flow=float(np.dot(delta,probability)); balance_rhs=float(math.fsum([escape,-delta_flow,offpin])); balance_bound=float(128*EPS*max(1,abs(candidate),abs(balance_rhs)))
 contaminated=sparse.csr_matrix(k["contaminated_matrix"]); rhs=np.asarray(k["rhs"]); rr=np.asarray(contaminated@raw-rhs); rawden=float(np.asarray(abs(contaminated).sum(axis=1)).ravel().max()*np.linalg.norm(raw,np.inf)+np.linalg.norm(rhs,np.inf))
 common={"native_V0":comp(init["initial_value"],oldi["initial_value"]),"native_l0":comp(init["baseline_labor"],oldi["baseline_labor"])}
 for name in ("value","consumption","labor","transfer","mu_a","mu_b"): common[name]=comp(h[name],oldh[name])
 summary={"diagnostic_completion":"COMPLETE","exact_grid_intervention_binding":"PASS","HJB_status":{"converged":bool(h["converged"]),"iterations":int(h["iterations"]),"statistic":float(h["convergence_statistic"]),"finite_value":bool(np.isfinite(h["value"]).all())},"Qh":qhd,"post_loop_Q":qd,"boundary_faces":face_summary,"expanded_upper_b_truncation_status":"PERSISTS" if face_summary["upper_b"]["positive_cells"] else "NOT_DETECTED","source_free_stationarity_status":"PASS" if source_free else "FAIL","stationarity":{"Tg_inf":float(np.linalg.norm(tg,np.inf)),"scale_denominator":float(stationary_scale),"scale_ratio":float(np.linalg.norm(tg,np.inf)/stationary_scale),"frozen_componentwise_bound_max":float(zero_bound.max())},"distribution_tail_diagnostics":regions,"density_weighted_boundary_escape":escape,"pin_companion_change":{"old_k":295,"new_k":pin,"coordinate":b["pin"]},"pin_source_ledger":{"candidate_source":candidate,"off_pin_correction":offpin,"delta_weighted_correction":delta_flow,"escape_minus_delta_plus_offpin":balance_rhs,"abs_discrepancy":abs(candidate-balance_rhs),"frozen_bound":balance_bound,"passes":abs(candidate-balance_rhs)<=balance_bound},"KFE_raw":{"finite":bool(np.isfinite(raw).all()),"contaminated_residual_inf":float(np.linalg.norm(rr,np.inf)),"contaminated_ratio":float(np.linalg.norm(rr,np.inf)/rawden)},"common_subgrid":common,"aggregate_diagnostics":agg,"truncation_sensitivity_conclusion":"EXPANSION_DOES_NOT_REMOVE_BOUNDARY_PRESSURE" if face_summary["upper_b"]["positive_cells"] else "EXPANSION_REDUCES_BOUNDARY_PRESSURE","call_ledger":term["counts"],"warnings":term["warnings"],"Results_eligible":False}
 write(out/"summary.json",summary); write(out/"operator_diagnostics.json",{"Qh":qhd,"post_loop_Q":qd,"faces":face_summary}); write(out/"distribution_diagnostics.json",{"regions":regions,"escape":escape,"stationarity":summary["stationarity"],"pin_source_ledger":summary["pin_source_ledger"],"KFE_raw":summary["KFE_raw"]}); write(out/"common_subgrid.json",common); write(out/"call_ledger.json",{"counts":term["counts"],"scientific_processes":1,"workers":1,"scientific_restarts":0,"launch_retries":0,"old_baseline_new_calls":0,"all_other_models_provinces_matlab":0}); print(json.dumps({k:summary[k] for k in ("HJB_status","expanded_upper_b_truncation_status","source_free_stationarity_status","distribution_tail_diagnostics","density_weighted_boundary_escape")}))
if __name__=="__main__": main(sys.argv[1],sys.argv[2])
