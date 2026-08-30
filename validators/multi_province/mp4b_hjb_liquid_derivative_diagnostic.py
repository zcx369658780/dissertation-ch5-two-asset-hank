"""Observability-only reconstruction of the first Beijing initial HJB iterate."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

import numpy as np

REPO_ROOT=Path(__file__).resolve().parents[2]
SRC_ROOT=REPO_ROOT/"src"
for root in (str(SRC_ROOT),str(REPO_ROOT)):
    if root not in sys.path:
        sys.path.insert(0,root)

from validators.multi_province.mp4b_python_empirical import (
    _source_initial_arrays, _write_json, load_entry_state,
)
from exports.matlab_faithful_two_asset_ha import (
    EconomicParams, HouseholdInputs, MATLAB_DERIVATIVE_FLOOR,
    MatlabFaithfulHJBGrid,
)


ORACLE_SHA = "276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8"
HJB_SOURCE_SHA = "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def _source_transfer_candidate(pa: float, pb: float, a: float, chi0: float, chi1: float) -> dict:
    ratio=pa/pb; q=ratio-1.0
    threshold=min(q+chi0,0.0)+max(q-chi0,0.0)
    return {"pa":pa,"pb":pb,"ratio_pa_pb":ratio,"q":q,"threshold":threshold,
            "candidate":threshold*a/chi1}


def diagnose(canonical_path: Path, protected_hjb_path: Path, output_path: Path) -> dict:
    repo=REPO_ROOT
    oracle=repo/"exports"/"matlab_faithful_two_asset_ha.py"
    if _sha256(oracle)!=ORACLE_SHA or _sha256(protected_hjb_path)!=HJB_SOURCE_SHA:
        raise RuntimeError("protected scientific identity mismatch")
    canonical,states=load_entry_state(canonical_path); state=states[0]
    grid=MatlabFaithfulHJBGrid(np.linspace(-2,5,20),np.linspace(0,10,20),
        np.array([0.8,1.3]),np.array([[-1/3,1/3],[1/3,-1/3]]))
    params=EconomicParams(0.05,2.0,5.0,0.1,2.0,1e-6,0.0,0.0)
    value,labor=_source_initial_arrays(state,grid,params)
    shape=value.shape; db=float(grid.b[1]-grid.b[0]); da=float(grid.a[1]-grid.a[0])
    vbf=np.zeros(shape); vbb=np.zeros(shape); vaf=np.zeros(shape); vab=np.zeros(shape)
    vbf[:-1]=(value[1:]-value[:-1])/db; vbb[1:]=vbf[:-1]
    for j in range(grid.a.size):
        for k,z in enumerate(grid.z):
            for i in (0,grid.b.size-1):
                rb=float(state["rb"])+(float(state["rb_gap"]) if grid.b[i]<0 else 0.0)
                resources=(1-float(state["tau"]))*float(state["w"])*z*labor[i,j,k]+float(state["Tt"])+rb*grid.b[i]
                marginal=resources**(-params.gamma_c)
                if i==0: vbb[i,j,k]=marginal
                else: vbf[i,j,k]=marginal
    vaf[:,:-1]=(value[:,1:]-value[:,:-1])/da; vab[:,1:]=vaf[:,:-1]
    vbf_p=np.maximum(vbf,MATLAB_DERIVATIVE_FLOOR); vbb_p=np.maximum(vbb,MATLAB_DERIVATIVE_FLOOR)
    raw_nonfinite=~np.isfinite(vbf)|~np.isfinite(vbb)
    either=(vbf<=0)|(vbb<=0)
    counts={"cell_count":int(np.prod(shape)),"raw_vb_forward_le_zero":int(np.count_nonzero(vbf<=0)),
        "raw_vb_backward_le_zero":int(np.count_nonzero(vbb<=0)),
        "raw_either_nonpositive":int(np.count_nonzero(either)),
        "raw_both_positive":int(np.count_nonzero((vbf>0)&(vbb>0))),
        "raw_nonfinite_either":int(np.count_nonzero(raw_nonfinite)),
        "processed_vb_forward_le_zero":int(np.count_nonzero(vbf_p<=0)),
        "processed_vb_backward_le_zero":int(np.count_nonzero(vbb_p<=0)),
        "processed_either_nonpositive":int(np.count_nonzero((vbf_p<=0)|(vbb_p<=0))),
        "processed_both_positive":int(np.count_nonzero((vbf_p>0)&(vbb_p>0))),
        "processed_nonfinite_either":int(np.count_nonzero(~np.isfinite(vbf_p)|~np.isfinite(vbb_p)))}
    offending=None; minimum_cell=None; minimum_derivative=float("inf")
    for k,z in enumerate(grid.z):
        for j,a in enumerate(grid.a):
            for i,b in enumerate(grid.b):
                local_min=min(vbf[i,j,k],vbb[i,j,k])
                if local_min<minimum_derivative:
                    minimum_derivative=float(local_min)
                    minimum_cell=(i,j,k,float(b),float(a),float(z))
                if min(vbf[i,j,k],vbb[i,j,k])<=0:
                    offending=(i,j,k,float(b),float(a),float(z)); break
            if offending: break
        if offending: break
    i,j,k,b,a,z=offending if offending is not None else minimum_cell
    net_wage=(1-float(state["tau"]))*float(state["w"])*z
    rb=float(state["rb"])+(float(state["rb_gap"]) if b<0 else 0.0)
    c_b=vbb_p[i,j,k]**(-1/params.gamma_c); c_f=vbf_p[i,j,k]**(-1/params.gamma_c)
    l_b=(vbb_p[i,j,k]*net_wage)**(1/params.phi); l_f=(vbf_p[i,j,k]*net_wage)**(1/params.phi)
    resources_b=net_wage*l_b+float(state["Tt"])+rb*b
    resources_f=net_wage*l_f+float(state["Tt"])+rb*b
    foc={"BB":_source_transfer_candidate(vab[i,j,k],vbb[i,j,k],a,params.chi_0,params.chi_1),
        "BF":_source_transfer_candidate(vaf[i,j,k],vbb[i,j,k],a,params.chi_0,params.chi_1),
        "FB":_source_transfer_candidate(vab[i,j,k],vbf[i,j,k],a,params.chi_0,params.chi_1),
        "FF":_source_transfer_candidate(vaf[i,j,k],vbf[i,j,k],a,params.chi_0,params.chi_1)}
    detail={"province":canonical["province_order"][0],"indices_zero_based":{"i":i,"j":j,"k":k},
        "indices_matlab":{"i":i+1,"j":j+1,"nz":k+1},"b":b,"a":a,"z":z,
        "neighbors":{"value_current":float(value[i,j,k]),
            "value_b_forward":float(value[i+1,j,k]) if i+1<shape[0] else None,
            "value_b_backward":float(value[i-1,j,k]) if i>0 else None,
            "value_a_forward":float(value[i,j+1,k]) if j+1<shape[1] else None,
            "value_a_backward":float(value[i,j-1,k]) if j>0 else None},
        "raw_derivatives":{"vb_forward":float(vbf[i,j,k]),"vb_backward":float(vbb[i,j,k]),
            "va_forward":float(vaf[i,j,k]),"va_backward":float(vab[i,j,k])},
        "matlab_processed_derivatives":{"vb_forward":float(vbf_p[i,j,k]),
            "vb_backward":float(vbb_p[i,j,k]),"va_forward":float(vaf[i,j,k]),
            "va_backward":float(vab[i,j,k]),"floor":MATLAB_DERIVATIVE_FLOOR},
        "boundary_flags":{"lower_b":i==0,"upper_b":i+1==shape[0],
            "lower_a":j==0,"upper_a":j+1==shape[1]},
        "baseline_labor":float(labor[i,j,k]),"transfer_income":float(state["Tt"]),
        "borrowing_rate_gap":float(state["rb_gap"]),"effective_rb":rb,
        "transfer_foc_candidates_raw":foc,
        "liquid_candidates":{"backward":{"consumption":float(c_b),"labor":float(l_b),
            "resources":float(resources_b),"drift":float(resources_b-c_b)},
            "forward":{"consumption":float(c_f),"labor":float(l_f),
            "resources":float(resources_f),"drift":float(resources_f-c_f)}},
        "is_offending":offending is not None,
        "python_oracle_action":"reject_raw_pre_floor_derivative" if offending is not None else "proceed_on_initial_iterate",
        "matlab_source_action":"floor_for_consumption_labor_then_proceed_with_raw_transfer_ratio"}
    payload={"schema":"CH5_MP4B_FIRST_BEIJING_HJB_LIQUID_DERIVATIVE_DIAGNOSTIC_V1",
        "calendar_year":2009,"canonical_sha256":"507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48",
        "oracle_sha256":ORACLE_SHA,"protected_hjb_sha256":HJB_SOURCE_SHA,
        "grid":{"shape":list(shape),"db":db,"da":da,"b":grid.b,"a":grid.a,"z":grid.z},
        "initial_value_summary":{"shape":list(shape),"minimum":float(value.min()),
            "maximum":float(value.max()),"sha256":hashlib.sha256(value.tobytes()).hexdigest().upper()},
        "traversal_order":"k,j,i","counts":counts,
        "first_offending_cell":detail if offending is not None else None,
        "minimum_raw_derivative_cell":detail,"minimum_raw_liquid_derivative":minimum_derivative,
        "diagnostic_scope_result":"INITIAL_ITERATE_HAS_NO_NONPOSITIVE_RAW_LIQUID_DERIVATIVE" if offending is None else "OFFENDING_CELL_LOCALIZED",
        "static_ordering_classification":"PYTHON_IMPLEMENTATION_ERROR__NONSOURCE_PRE_FLOOR_LIQUID_DERIVATIVE_POSITIVITY_GUARD",
        "scientific_model_calls":{"python_stationary":0,"solve_household_steady_state":0,
            "hjb_iterations":0,"kfe":0,"mp2":0,"mp3":0,"matlab_model":0}}
    _write_json(output_path,payload); return payload


if __name__ == "__main__":
    import sys
    if len(sys.argv)!=4:
        raise SystemExit("usage: diagnostic.py CANONICAL_JSON PROTECTED_HJB_M OUTPUT_JSON")
    diagnose(Path(sys.argv[1]),Path(sys.argv[2]),Path(sys.argv[3]))
