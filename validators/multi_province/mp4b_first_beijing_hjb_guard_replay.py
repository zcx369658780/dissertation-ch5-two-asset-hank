"""One-shot Beijing-only HJB guard observability replay; no KFE or aggregation."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

import numpy as np
from scipy import sparse
from scipy.sparse import linalg

REPO_ROOT=Path(__file__).resolve().parents[2]
SRC_ROOT=REPO_ROOT/"src"
for root in (str(SRC_ROOT),str(REPO_ROOT)):
    if root not in sys.path: sys.path.insert(0,root)

from validators.multi_province.mp4b_python_empirical import _source_initial_arrays, _write_json, load_entry_state
from exports.matlab_faithful_two_asset_ha import (
    EconomicParams, HouseholdInputs, MATLAB_DERIVATIVE_FLOOR, MATLAB_DRIFT_TOLERANCE,
    MatlabFaithfulHJBGrid, assemble_source_operator, select_matlab_faithful_local_policy,
)

PRIOR_DIAGNOSTIC_SHA="6D9BC65657087D5DF3C17963D906EAFA93F2F5208F91D2211283B627F6C49951"
ORACLE_SHA="276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8"
INITIAL_VALUE_SHA="0B181AAD81C87DD5C13E4AB71BAF2F6B708EEEB3B71BC85331FFD6677E8AB14F"


def _sha(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest().upper()
def _array_sha(value: np.ndarray) -> str: return hashlib.sha256(value.tobytes()).hexdigest().upper()


def _derivatives(old, labor0, grid, state, params):
    shape=old.shape; db=float(grid.b[1]-grid.b[0]); da=float(grid.a[1]-grid.a[0])
    vbf=np.zeros(shape); vbb=np.zeros(shape); vaf=np.zeros(shape); vab=np.zeros(shape)
    vbf[:-1]=(old[1:]-old[:-1])/db; vbb[1:]=vbf[:-1]
    for j in range(grid.a.size):
        for k,z in enumerate(grid.z):
            for i in (0,grid.b.size-1):
                rb=float(state["rb"])+(float(state["rb_gap"]) if grid.b[i]<0 else 0.0)
                resources=(1-float(state["tau"]))*float(state["w"])*z*labor0[i,j,k]+float(state["Tt"])+rb*grid.b[i]
                marginal=resources**(-params.gamma_c)
                if i==0: vbb[i,j,k]=marginal
                else: vbf[i,j,k]=marginal
    vaf[:,:-1]=(old[:,1:]-old[:,:-1])/da; vab[:,1:]=vaf[:,:-1]
    return vbf,vbb,vaf,vab,db,da


def _first_nonpositive(vbf, vbb):
    for k in range(vbf.shape[2]):
        for j in range(vbf.shape[1]):
            for i in range(vbf.shape[0]):
                if vbf[i,j,k]<=0 or vbb[i,j,k]<=0: return i,j,k
    return None


def _counts(vbf,vbb):
    either=(vbf<=0)|(vbb<=0)
    return {"vbf_le_zero":int(np.count_nonzero(vbf<=0)),"vbb_le_zero":int(np.count_nonzero(vbb<=0)),
        "either_nonpositive":int(np.count_nonzero(either)),
        "both_positive":int(np.count_nonzero((vbf>0)&(vbb>0))),
        "nonfinite":int(np.count_nonzero(~np.isfinite(vbf)|~np.isfinite(vbb))),
        "minimum_vbf":float(np.min(vbf)),"maximum_vbf":float(np.max(vbf)),
        "minimum_vbb":float(np.min(vbb)),"maximum_vbb":float(np.max(vbb))}


def _encoded(value):
    value=float(value)
    if np.isnan(value): return {"classification":"NaN","value":None}
    if np.isposinf(value): return {"classification":"PositiveInfinity","value":None}
    if np.isneginf(value): return {"classification":"NegativeInfinity","value":None}
    return {"classification":"finite","value":value}


def _source_candidate(pa,pb,a,params):
    with np.errstate(divide="ignore",invalid="ignore"):
        ratio=np.divide(pa,pb); q=ratio-1.0
        threshold=np.minimum(q+params.chi_0,0.0)+np.maximum(q-params.chi_0,0.0)
        candidate=threshold*a/params.chi_1
    return {"pa":_encoded(pa),"pb":_encoded(pb),"ratio_pa_pb":_encoded(ratio),
        "q":_encoded(q),"threshold":_encoded(threshold),"candidate":_encoded(candidate)}


def _offending_payload(iteration,idx,old,labor0,vbf,vbb,vaf,vab,grid,state,params):
    i,j,k=idx; b=float(grid.b[i]); a=float(grid.a[j]); z=float(grid.z[k])
    vbfp=max(float(vbf[i,j,k]),MATLAB_DERIVATIVE_FLOOR); vbbp=max(float(vbb[i,j,k]),MATLAB_DERIVATIVE_FLOOR)
    net=(1-float(state["tau"]))*float(state["w"])*z
    rb=float(state["rb"])+(float(state["rb_gap"]) if b<0 else 0.0)
    def liquid(vb):
        consumption=vb**(-1/params.gamma_c); labor=(vb*net)**(1/params.phi)
        resources=net*labor+float(state["Tt"])+rb*b
        return {"processed_vb":vb,"consumption":consumption,"labor":labor,
            "resources":resources,"drift":resources-consumption}
    return {"iteration":iteration,"completed_previous_iterations":iteration-1,
        "indices_zero_based":{"i":i,"j":j,"k":k},"indices_matlab":{"i":i+1,"j":j+1,"nz":k+1},
        "b":b,"a":a,"z":z,"neighbors":{"current":float(old[i,j,k]),
            "b_forward":float(old[i+1,j,k]) if i+1<old.shape[0] else None,
            "b_backward":float(old[i-1,j,k]) if i>0 else None,
            "a_forward":float(old[i,j+1,k]) if j+1<old.shape[1] else None,
            "a_backward":float(old[i,j-1,k]) if j>0 else None},
        "raw":{"vbf":float(vbf[i,j,k]),"vbb":float(vbb[i,j,k]),
            "vaf":float(vaf[i,j,k]),"vab":float(vab[i,j,k])},
        "processed":{"vbf":vbfp,"vbb":vbbp,"floor":MATLAB_DERIVATIVE_FLOOR},
        "boundary_flags":{"lower_b":i==0,"upper_b":i+1==old.shape[0],
            "lower_a":j==0,"upper_a":j+1==old.shape[1]},
        "baseline_labor":float(labor0[i,j,k]),"transfer_income":float(state["Tt"]),
        "rb":float(state["rb"]),"borrowing_rate_gap":float(state["rb_gap"]),"effective_rb":rb,
        "transfer_candidates_raw":{"BB":_source_candidate(vab[i,j,k],vbb[i,j,k],a,params),
            "BF":_source_candidate(vaf[i,j,k],vbb[i,j,k],a,params),
            "FB":_source_candidate(vab[i,j,k],vbf[i,j,k],a,params),
            "FF":_source_candidate(vaf[i,j,k],vbf[i,j,k],a,params)},
        "liquid_candidates":{"backward":liquid(vbbp),"forward":liquid(vbfp)},
        "matlab_source_action":"process_vb_floor_for_consumption_labor_and_proceed_to_raw_transfer_ratios",
        "current_python_action":"reject_before_floor_and_before_transfer_ratios",
        "local_policy_called_for_offending_cell":False}


def replay(canonical_path: Path, prior_artifact: Path, output_path: Path):
    oracle=REPO_ROOT/"exports"/"matlab_faithful_two_asset_ha.py"
    if _sha(oracle)!=ORACLE_SHA or _sha(prior_artifact)!=PRIOR_DIAGNOSTIC_SHA:
        raise RuntimeError("accepted replay identity mismatch")
    prior=json.loads(prior_artifact.read_text(encoding="utf-8"))
    canonical,states=load_entry_state(canonical_path); state=states[0]
    grid=MatlabFaithfulHJBGrid(np.linspace(-2,5,20),np.linspace(0,10,20),np.array([0.8,1.3]),
        np.array([[-1/3,1/3],[1/3,-1/3]]))
    params=EconomicParams(0.05,2.0,5.0,0.1,2.0,1e-6,0.0,0.0)
    inputs=HouseholdInputs(float(state["rah"]),float(state["rb"]),float(state["tau"]),
        np.array([state["w"]]),np.array([0.0]),np.array([1.0]))
    value,labor0=_source_initial_arrays(state,grid,params); initial_sha=_array_sha(value)
    completed=[]; local_calls=0; offending=None; identity=None
    for iteration in range(1,101):
        old=value.copy(); vbf,vbb,vaf,vab,db,da=_derivatives(old,labor0,grid,state,params)
        count=_counts(vbf,vbb); idx=_first_nonpositive(vbf,vbb)
        if iteration==1:
            identity={"shape":list(old.shape),"initial_value_sha256":initial_sha,"counts":count,
                "minimum_cell_zero_based":[18,19,1],
                "minimum_cell_vbf":float(vbf[18,19,1]),"minimum_cell_vbb":float(vbb[18,19,1])}
            expected=prior["counts"]
            ok=(list(old.shape)==[20,20,2] and initial_sha==INITIAL_VALUE_SHA and
                count["vbf_le_zero"]==expected["raw_vb_forward_le_zero"]==0 and
                count["vbb_le_zero"]==expected["raw_vb_backward_le_zero"]==0 and
                count["either_nonpositive"]==0 and count["both_positive"]==800 and count["nonfinite"]==0 and
                np.isclose(vbf[18,19,1],0.001609918920837204,rtol=0,atol=1e-18) and
                np.isclose(vbb[18,19,1],0.001610998339912406,rtol=0,atol=1e-18))
            identity["verdict"]="MP4B_FIRST_BEIJING_HJB_REPLAY_INITIAL_ITERATE_IDENTITY_PASS" if ok else "FAIL"
            if not ok: break
        if idx is not None:
            offending=_offending_payload(iteration,idx,old,labor0,vbf,vbb,vaf,vab,grid,state,params); break
        shape=old.shape; utility=np.empty(shape); bb=np.empty(shape); bf=np.empty(shape); ab=np.empty(shape); af=np.empty(shape)
        for k,z in enumerate(grid.z):
            for j,a in enumerate(grid.a):
                for i,b in enumerate(grid.b):
                    policy=select_matlab_faithful_local_policy(a=float(a),b=float(b),z=float(z),
                        v_a_forward=float(vaf[i,j,k]),v_a_backward=float(vab[i,j,k]),
                        v_b_forward=float(vbf[i,j,k]),v_b_backward=float(vbb[i,j,k]),
                        baseline_labor=float(labor0[i,j,k]),transfer_income=float(state["Tt"]),
                        borrowing_rate_gap=float(state["rb_gap"]),a_max=float(grid.a[-1]),da=da,db=db,
                        at_lower_a=j==0,at_upper_a=j+1==grid.a.size,at_lower_b=i==0,at_upper_b=i+1==grid.b.size,
                        inputs=inputs,params=params,tolerance=MATLAB_DRIFT_TOLERANCE)
                    local_calls+=1; utility[i,j,k]=policy.utility
                    bb[i,j,k]=policy.iteration_b_backward_rate; bf[i,j,k]=policy.iteration_b_forward_rate
                    ab[i,j,k]=policy.a_backward_rate; af[i,j,k]=policy.a_forward_rate
        operator=assemble_source_operator(bb,bf,ab,af,grid.switch_matrix)
        matrix=(1/1000.0+params.rho)*sparse.eye(np.prod(shape),format="csr")-operator.full
        rhs=utility.ravel(order="F")+old.ravel(order="F")/1000.0
        value=linalg.spsolve(matrix,rhs).reshape(shape,order="F")
        completed.append({"iteration":iteration,"derivative_counts":count,
            "value_old_min":float(old.min()),"value_old_max":float(old.max()),
            "value_new_min":float(value.min()),"value_new_max":float(value.max()),
            "convergence_statistic":float(np.max(np.abs(value-old))),"value_new_sha256":_array_sha(value)})
    payload={"schema":"CH5_MP4B_FIRST_BEIJING_HJB_GUARD_OBSERVABILITY_REPLAY_V1",
        "canonical_sha256":"507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48",
        "oracle_sha256":ORACLE_SHA,"prior_diagnostic_sha256":PRIOR_DIAGNOSTIC_SHA,
        "configuration":{"province":"北京","max_value_iterations":100,"traversal_order":"k,j,i",
            "delta":1000.0,"rho":params.rho,"flatten_order":"F"},
        "initial_iterate_identity":identity,"completed_iteration_summaries":completed,
        "offending_cell":offending,
        "localization_marker":"MP4B_FIRST_BEIJING_HJB_OFFENDING_LIQUID_DERIVATIVE_EXACTLY_LOCALIZED" if offending else None,
        "diagnosis_marker":"MP4B_HJB_FIRST_DIVERGENCE_SOURCE_SEMANTICS_DIAGNOSIS_COMPLETE" if offending else None,
        "classification":"PYTHON_IMPLEMENTATION_ERROR__NONSOURCE_PRE_FLOOR_LIQUID_DERIVATIVE_POSITIVITY_GUARD" if offending else None,
        "call_ledger":{"replay_invocations":1,"beijing_households":1,"local_policy_calls_before_stop":local_calls,
            "completed_hjb_value_updates":len(completed),"python_stationary":0,"solve_household_steady_state":0,
            "kfe":0,"household_aggregation":0,"second_province":0,"mp2":0,"mp3":0,"matlab_model":0},
        "verdict":"MP4B_FIRST_BEIJING_HJB_GUARD_OBSERVABILITY_REPLAY_LOCALIZATION_PASS" if offending else "MP4B_FIRST_BEIJING_HJB_GUARD_OBSERVABILITY_REPLAY_BLOCKED"}
    _write_json(output_path,payload); return payload


if __name__=="__main__":
    if len(sys.argv)!=4: raise SystemExit("usage: replay.py CANONICAL PRIOR_DIAGNOSTIC OUTPUT_JSON")
    replay(Path(sys.argv[1]),Path(sys.argv[2]),Path(sys.argv[3]))
