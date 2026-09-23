"""Static preflight and future one-shot C5 -> C6-prime replay.

Import and default CLI perform no model call. execute_once needs a distinct future task.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.metadata
import json
import os
import platform
import re
import subprocess
import sys
import inspect
from pathlib import Path
from typing import Any, Mapping

import numpy as np

REPOSITORY = Path(__file__).resolve().parents[3]
FUTURE_TASK_ID = "CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_EXECUTION_20260923"
FUTURE_STATUS = "ACTIVE__ONE_SHOT_SAME_FROZEN_INPUT_REPEAT"
FUTURE_TASK_RELATIVE = Path("tasks/CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_EXECUTION_20260923.md")
MANIFEST_SHA = "51F636DF222DD1365B017091B6F77F78A71C606F84776CDFB62457105F2E9127"
OLD_ROOT = Path("reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001")
OUTPUT = Path("reports/ch5_turn6_same_frozen_input_repeat_20260923_run001")
DISTANCE = Path("docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv")
SRC_TREE = "00682b2e1a7ba23665f6e16f6acf48ad35874883"
OLD_RUNNER_SHA = "92018027502FFA5281F9BFAC91EE70D2BED17876B65100B3321819B2C0C59DB6"
DISTANCE_SHA = "51A04FCAA1FA519B142BE2A155640F77E8746493AFDF4865ED243B96526E550D"
HELPER_SHA = {
    "validators/multi_province/k1b_turn3_lagged_raw_ra0_activation_safety_gate/run.py": "2A7B8B28EDB2C6D4F1DF8A1211D9CB04BF018CD1C709B8E8F2903052E3071454",
    "validators/multi_province/k1b_turn4_corrected_household_kfe_and_one_turn_integration/run.py": "098D80AAB0E91BB511F2AF05E1DBC51744979206435A4252B602B03C14DEDA59",
    "validators/multi_province/corrected_2018_single_turn/run.py": "9EAF82373EE564E5F27BEA14D49D2177E0637A6969D946C86F519608FFBAE614",
}
SEALED = {
    "turn6_k1b_input_candidate.json": "87BEB944AD35C16BAF62D35FE8DDAD3BDEBC9000DCB6CC9F7D6949A039F4B1BC",
    "turn6_k1b_frozen_share_payoff_plan.npz": "95880D37D5BBB10B95FF776E32B8B786447B20C1770117044C7735D91292ED34",
    "turn7_k1b_input_candidate.json": "D84E9D74C7E965A3B492F2F0F9A63D3320D436DD4A6D78E1E655F014C05FC059",
    "turn7_k1b_frozen_share_payoff_plan.npz": "37A1258F8EC87116F03084D8178C77424FDD5F3859A1BC73D9704940A3B9381E",
}
CEILINGS = {
    "source_native_initializations":31,"scalar_labor_roots_attempted":24800,"scalar_labor_roots_returned":24800,
    "corrected_policy_maps":1581,"d2_q_assemblies":1581,"selector_evaluations":1264800,
    "scalar_selector_root_invocations":620000000,"direct_hjb_updates":1550,
    "hjb_checkpoint_evaluations_after_update":1550,"relaxation_helper_invocations":1550,
    "alpha_candidates":82150,"terminal_kfe_attempts":31,"scc_decompositions":31,
    "restricted_dense_scipy_linalg_svd_gesvd":31,"normalized_stationary_candidates":31,
    "q_transpose_times_p":31,"corrected_aggregate_evaluations":31,"firm_evaluations":31,
    "household_batch_constructions":1,"full_integrations":1,"source_faithful_labor_reconstructions":1,
    "frozen_k1b_quantity_allocations":1,"k1b_feedback_calls":1,"c1_residual_govinv_constructions":1,
    "composite_wage_batches":1,"monetary_assignments":1,"fiscal_diagnostic_batches":1,
    "completed_raw_ra0_vectors":1,"deterministic_next_k1b_preparations":1,
    "raw_next_payoff_same_s_constructions":1,"turn7_household_calls":0,
    "full_space_800_dense_scipy_linalg_svd_gesvd":0,"scientific_retries":0,
    "solver_substitutions":0,"k2_calls":0,"ge_annual_shock_irf_welfare_results_calls":0,
    "matlab_scientific_calls":0,
}
PER_PROVINCE = {"corrected_policy_maps":51,"selector_evaluations":40800,
                "scalar_selector_root_invocations":20000000,"direct_hjb_updates":50,
                "terminal_kfe_attempts":1}
FIELDS = ("Yt","Lt","wjt","rk","Kt_prev","w","raw_ra0","rah","S")

class RepeatBlocked(RuntimeError):
    def __init__(self, terminal: str, detail: Any = None):
        super().__init__(terminal)
        self.terminal, self.detail = terminal, detail


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git",*args],cwd=repo,text=True).strip()


def save_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=True,allow_nan=False,indent=2)+"\n",encoding="utf-8")

def save_json_new(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("x",encoding="utf-8") as stream:
        json.dump(value,stream,ensure_ascii=True,allow_nan=False,indent=2)
        stream.write("\n")

def record_pre_call_failure(output:Path,exc:BaseException,execution_id:str)->None:
    output.mkdir(parents=True,exist_ok=False)
    save_json_new(output/"first_failure.json",{
        "terminal":getattr(exc,"terminal",type(exc).__name__),
        "literal_scientific_call_ledger":{k:0 for k in CEILINGS},
        "execution_id":execution_id})

def integration_entry_lines(function:Any)->dict[int,tuple[str,...]]:
    """Bind each entry guard to the frozen old integration function source."""
    markers={
        'ledger["source_faithful_labor_reconstructions"] += 1':("source_faithful_labor_reconstructions",),
        'ledger["frozen_k1b_quantity_allocations"] += 1':("frozen_k1b_quantity_allocations",),
        'ledger["k1b_feedback_calls"] += 1':("k1b_feedback_calls",),
        'ledger["c1_residual_govinv_constructions"] += 1':("c1_residual_govinv_constructions",),
        'ledger["firm_evaluations"] += 1':("firm_evaluations",),
        'ledger["composite_wage_batches"] += 1':("composite_wage_batches",),
        'ledger["monetary_assignments"] += 1':("monetary_assignments",),
        'ledger["fiscal_diagnostic_batches"] += 1':("fiscal_diagnostic_batches",),
        'ledger["completed_raw_ra0_vectors"] += 1':("completed_raw_ra0_vectors",),
        'ledger["deterministic_next_k1b_preparations"] += 1':("deterministic_next_k1b_preparations",),
    }
    lines=inspect.getsourcelines(function)
    out={}
    for marker,categories in markers.items():
        matched=[lines[1]+i for i,line in enumerate(lines[0]) if line.strip()==marker]
        if len(matched)!=1:raise RepeatBlocked("BLOCKED__INTEGRATION_ENTRY_MARKER",marker)
        out[matched[0]]=categories
    return out

def make_entry_trace(code:Any,lines:Mapping[int,tuple[str,...]],guard:Any):
    def trace(frame,event,arg):
        if event=="line" and frame.f_code is code:
            for category in lines.get(frame.f_lineno,()):
                guard.enter(category)
        return trace
    return trace


def canonical_order(repo: Path) -> tuple[str,...]:
    tree=ast.parse((repo/"src/ch5_two_asset_hank/multi_province/province_contracts.py").read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node,ast.AnnAssign) and isinstance(node.target,ast.Name) and node.target.id=="PROVINCE_ORDER":
            order=ast.literal_eval(node.value)
            if isinstance(order,tuple) and len(order)==31 and len(set(order))==31:return order
    raise RepeatBlocked("BLOCKED__CANONICAL_PROVINCE_ORDER_UNAVAILABLE")


def load_bundle(repo: Path, turn: int, root: Path = OLD_ROOT) -> dict[str,Any]:
    jp=repo/root/f"turn{turn}_k1b_input_candidate.json"
    pp=repo/root/f"turn{turn}_k1b_frozen_share_payoff_plan.npz"
    if root==OLD_ROOT and (sha(jp)!=SEALED[jp.name] or sha(pp)!=SEALED[pp.name]):
        raise RepeatBlocked("BLOCKED__SEALED_BUNDLE_HASH_MISMATCH",turn)
    doc=json.loads(jp.read_text(encoding="utf-8"));rows=doc.get("rows",[]);order=canonical_order(repo)
    if doc.get("classification")!=f"TURN{turn}_K1B_INPUT_CANDIDATE_ONLY__TURN{turn}_HOUSEHOLD_NOT_RUN":
        raise RepeatBlocked("BLOCKED__BUNDLE_CLASSIFICATION",turn)
    if len(rows)!=31 or tuple(r.get("province") for r in rows)!=order or [r.get("province_index") for r in rows]!=list(range(31)):
        raise RepeatBlocked("BLOCKED__PROVINCE_ORDER",turn)
    if any(r.get("state",{}).get("name")!=order[i] for i,r in enumerate(rows)):
        raise RepeatBlocked("BLOCKED__STATE_PROVINCE_ORDER",turn)
    with np.load(pp,allow_pickle=False) as z:
        s=np.array(z["portfolio_shares_destination_origin"],copy=True)
        raw=np.array(z[f"raw_ra0_turn{turn-1}"],copy=True)
        rah=np.array(z[f"rah_turn{turn}_by_origin"],copy=True)
    if s.shape!=(31,31) or raw.shape!=(31,) or rah.shape!=(31,):
        raise RepeatBlocked("BLOCKED__BUNDLE_SHAPE",turn)
    if any(a.dtype!=np.float64 or not np.all(np.isfinite(a)) for a in (s,raw,rah)):
        raise RepeatBlocked("BLOCKED__BUNDLE_FLOAT64_FINITE",turn)
    if np.any(s<0) or np.max(np.abs(np.sum(s,axis=0)-1))>1e-12:
        raise RepeatBlocked("BLOCKED__BUNDLE_SHARE_COLUMNS",turn)
    field=lambda a,order="C":hashlib.sha256(a.tobytes(order=order)).hexdigest().upper()
    if (field(s,"F")!=doc.get("k1b_portfolio_share_plan_sha256") or
        field(raw)!=doc.get(f"source_completed_turn{turn-1}_raw_ra0_sha256") or
        field(rah)!=doc.get("raw_next_payoff_sha256")):
        raise RepeatBlocked("BLOCKED__BUNDLE_FIELD_HASH",turn)
    rr=np.asarray([r[f"raw_ra0_turn{turn-1}"] for r in rows],dtype=np.float64)
    sr=np.asarray([r["state"]["ra0"] for r in rows],dtype=np.float64)
    rh=np.asarray([r["state"]["rah"] for r in rows],dtype=np.float64)
    if not (np.array_equal(rr.view(np.uint64),raw.view(np.uint64)) and
            np.array_equal(sr.view(np.uint64),raw.view(np.uint64)) and
            np.array_equal(rh.view(np.uint64),rah.view(np.uint64))):
        raise RepeatBlocked("BLOCKED__BUNDLE_JSON_NPZ_BIT_IDENTITY",turn)
    return {"rows":rows,"states":tuple(dict(r["state"]) for r in rows),"S":s,"raw":raw,"rah":rah,
            "hashes":{"json":sha(jp),"npz":sha(pp),"S":field(s,"F"),"raw":field(raw),"rah":field(rah)}}


def environment_snapshot() -> dict[str,Any]:
    try:scipy=importlib.metadata.version("scipy")
    except importlib.metadata.PackageNotFoundError:scipy=None
    return {"python":sys.version,"numpy":np.__version__,"scipy":scipy,
            "platform":platform.platform(),"machine":platform.machine(),
            "thread_environment":{k:os.environ.get(k) for k in
                ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS",
                 "VECLIB_MAXIMUM_THREADS","NUMEXPR_NUM_THREADS","BLIS_NUM_THREADS")},
            "blas_configuration":np.__config__.show(mode="dicts")}


def preflight(repo: Path = REPOSITORY) -> dict[str,Any]:
    repo=repo.resolve()
    checks={"root":git(repo,"rev-parse","--show-toplevel").replace("\\","/").casefold()==repo.as_posix().casefold(),
            "src_tree":git(repo,"rev-parse","HEAD:src")==SRC_TREE,
            "src_worktree_clean":not git(repo,"status","--porcelain=v1","--","src"),
            "old_runner":sha(repo/"validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py")==OLD_RUNNER_SHA,
            "distance":sha(repo/DISTANCE)==DISTANCE_SHA,
            "helper_hashes":all(sha(repo/name)==digest for name,digest in HELPER_SHA.items()),
            "new_output_absent":not (repo/OUTPUT).exists()}
    if not all(checks.values()):raise RepeatBlocked("BLOCKED__STATIC_PREFLIGHT",checks)
    c5=load_bundle(repo,6);c6=load_bundle(repo,7)
    return {"status":"PASS__STATIC_PREFLIGHT_ONLY","checks":checks,
            "C5_entering":c5["hashes"],"C6_reference":c6["hashes"],
            "src_tree":SRC_TREE,"old_runner_sha256":OLD_RUNNER_SHA,
            "helper_sha256":HELPER_SHA,"distance_sha256":DISTANCE_SHA,
            "province_count":31,"S_orientation":"destination_by_origin",
            "planned_output_root":str(repo/OUTPUT),"environment":environment_snapshot(),"scientific_calls":0}


class BudgetGuard:
    def __init__(self,ceilings:Mapping[str,int]=CEILINGS):
        self.ceilings=dict(ceilings);self.attempted={k:0 for k in ceilings};self.per_province={};self.denied=[]
    def reserve(self,amounts:Mapping[str,int],province:int|None=None)->None:
        for key,n in amounts.items():
            if key not in self.ceilings or n<0 or self.attempted[key]+n>self.ceilings[key]:
                self.denied.append({"category":key,"amount":n,"province":province})
                raise RepeatBlocked("BLOCKED__ENTRY_BEFORE_CALL_BUDGET",self.denied[-1])
            if province is not None and key in PER_PROVINCE:
                if self.per_province.get(province,{}).get(key,0)+n>PER_PROVINCE[key]:
                    self.denied.append({"category":key,"amount":n,"province":province})
                    raise RepeatBlocked("BLOCKED__PROVINCE_BUDGET",self.denied[-1])
    def enter(self,key:str,province:int|None=None)->None:
        self.reserve({key:1},province);self.attempted[key]+=1
        if province is not None:
            row=self.per_province.setdefault(province,{})
            row[key]=row.get(key,0)+1
    def reconcile(self,ledger:Mapping[str,Any])->None:
        keys=("source_native_initializations","scalar_labor_roots_attempted","scalar_labor_roots_returned",
              "corrected_policy_maps","selector_evaluations","scalar_selector_root_invocations",
              "d2_q_assemblies","direct_hjb_updates","hjb_checkpoint_evaluations_after_update",
              "scc_decompositions","restricted_dense_scipy_linalg_svd_gesvd",
              "normalized_stationary_candidates","q_transpose_times_p","corrected_aggregate_evaluations")
        for key in keys:
            n=int(ledger[key])
            if n>self.ceilings[key]:raise RepeatBlocked("BLOCKED__CONSUMED_CALL_BUDGET",{"category":key,"actual":n})
            # A guarded attempt can fail before the source records its local
            # count; never erase that already consumed entry on reconciliation.
            self.attempted[key]=max(self.attempted[key],n)

def _arrays(bundle:Mapping[str,Any],turn:int)->dict[str,np.ndarray]:
    rows=bundle["rows"]
    out={k:np.asarray([r["state"][k] for r in rows],dtype=np.float64)
         for k in FIELDS if k not in ("raw_ra0","S")}
    out["raw_ra0"]=np.asarray([r[f"raw_ra0_turn{turn-1}"] for r in rows],dtype=np.float64)
    out["S"]=np.asarray(bundle["S"],dtype=np.float64)
    return out

def compare_carrier(ref:Mapping[str,Any],new:Mapping[str,Any])->dict[str,Any]:
    a=_arrays(ref,7);b=_arrays(new,7);rows={}
    for key in FIELDS:
        x,y=a[key],b[key]
        if x.shape!=y.shape or x.shape!=((31,31) if key=="S" else (31,)):
            rows[key]={"status":"UNAVAILABLE","reason":"shape"};continue
        if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
            rows[key]={"status":"UNAVAILABLE","reason":"nonfinite"};continue
        if key in ("Yt","Lt","wjt","w"):
            if np.any(x==0):rows[key]={"status":"UNAVAILABLE","reason":"zero_denominator"};continue
            metric=np.abs(y/x-1)
        elif key=="Kt_prev":
            k0=np.asarray([r["state"]["Kt0"] for r in ref["rows"]],dtype=np.float64)
            k1=np.asarray([r["state"]["Kt0"] for r in new["rows"]],dtype=np.float64)
            if np.any(k0<=0) or not np.all(np.isfinite(k0)) or not np.array_equal(k0.view(np.uint64),k1.view(np.uint64)):
                rows[key]={"status":"UNAVAILABLE","reason":"Kt0_identity"};continue
            metric=np.abs(y-x)/k0
        else:metric=np.abs(y-x)
        if not np.all(np.isfinite(metric)):
            rows[key]={"status":"UNAVAILABLE","reason":"nonfinite_difference"};continue
        mismatch=x.view(np.uint64)!=y.view(np.uint64)
        ix=np.unravel_index(int(np.argmax(metric)),metric.shape)
        loc={"province_index":int(ix[0])} if len(ix)==1 else {"destination_index":int(ix[0]),"origin_index":int(ix[1])}
        rows[key]={"status":"EXACT_BITWISE_MATCH" if not np.any(mismatch) else "LEGAL_DIFFERENCE_OBSERVED",
                   "shape":list(x.shape),"finite":True,"bitwise_mismatch_count":int(np.count_nonzero(mismatch)),
                   "diagnostic_difference":float(metric[ix]),"max_location":loc,
                   "max_absolute_difference":float(np.max(np.abs(y-x))),"old_at_max":float(x[ix]),"new_at_max":float(y[ix])}
    status="EXACT_BITWISE_MATCH" if all(r["status"]=="EXACT_BITWISE_MATCH" for r in rows.values()) else (
        "UNAVAILABLE" if any(r["status"]=="UNAVAILABLE" for r in rows.values()) else "LEGAL_DIFFERENCE_OBSERVED")
    return {"classification":status,"components":rows,"repeatability_threshold":None,"one_pair_only":True}

def _numeric(value:Any,prefix:str="")->dict[str,float]:
    if isinstance(value,dict):
        out={}
        for k,v in value.items():out.update(_numeric(v,f"{prefix}.{k}" if prefix else k))
        return out
    if isinstance(value,list):
        out={}
        for i,v in enumerate(value):out.update(_numeric(v,f"{prefix}[{i}]"))
        return out
    return {prefix:float(value)} if isinstance(value,(int,float)) and not isinstance(value,bool) else {}

def compare_receipt(old:Path,new:Path)->dict[str,Any]:
    if not old.is_file() or not new.is_file():return {"status":"UNAVAILABLE","reason":"missing"}
    old_doc=json.loads(old.read_text(encoding="utf-8"))
    new_doc=json.loads(new.read_text(encoding="utf-8"))
    if old_doc.get("status")!="PASS" or new_doc.get("status")!="PASS":
        return {"status":"UNAVAILABLE","reason":"receipt_status"}
    a=_numeric(old_doc)
    b=_numeric(new_doc)
    if a.keys()!=b.keys():return {"status":"UNAVAILABLE","reason":"numeric_keys","old":len(a),"new":len(b)}
    if not a:return {"status":"UNAVAILABLE","reason":"no_numeric_fields"}
    if any(not np.isfinite(v) for v in (*a.values(),*b.values())):
        return {"status":"UNAVAILABLE","reason":"nonfinite"}
    bad=[k for k in a if np.float64(a[k]).view(np.uint64)!=np.float64(b[k]).view(np.uint64)]
    k=max(a,key=lambda v:abs(a[v]-b[v])) if a else None
    return {"status":"EXACT_BITWISE_MATCH" if not bad else "LEGAL_DIFFERENCE_OBSERVED",
            "scope":"numeric_json_fields_only",
            "numeric_fields":len(a),"bitwise_mismatches":len(bad),"max_field":k,
            "max_absolute_difference":abs(a[k]-b[k]) if k else 0.0}

def reference_intermediate_paths(repo:Path)->tuple[str,...]:
    names=["turn6/household_batch_receipt.json","turn6/source_faithful_labor_receipt.json",
           "turn6/turn6_one_turn_integration_receipt.json",
           "turn6/turn6_frozen_k1b_capital_receipt.json",
           "turn6/turn6_frozen_k1b_capital_arrays.npz",
           "turn6/turn6_c1_residual_govinv_receipt.json",
           "turn6/turn6_firm_raw_used_return_receipt.json",
           "turn7_k1b_zscore_share_payoff_receipt.json"]
    for i,name in enumerate(canonical_order(repo)):
        base=f"turn6/household/p{i:02}_{name}/terminal_kfe/"
        names.extend((base+"stationarity_normalization_nonnegativity_receipt.json",
                      base+"stationary_mass_arrays.npz"))
    return tuple(names)

def reference_intermediate_hashes(repo:Path)->dict[str,str]:
    manifest=repo/OLD_ROOT/"sealed_manifest.json"
    if sha(manifest)!=MANIFEST_SHA:
        raise RepeatBlocked("BLOCKED__SEALED_MANIFEST_HASH")
    entries={row["path"]:row for row in json.loads(manifest.read_text(encoding="utf-8"))["entries"]}
    result={}
    for name in reference_intermediate_paths(repo):
        path=repo/OLD_ROOT/name
        row=entries.get(name)
        if row is None or not path.is_file() or path.stat().st_size!=row["bytes"] or sha(path)!=row["sha256"]:
            raise RepeatBlocked("BLOCKED__SEALED_REFERENCE_INTERMEDIATE",name)
        result[name]=row["sha256"]
    return result

def compare_npz(old:Path,new:Path)->dict[str,Any]:
    if not new.is_file():return {"status":"UNAVAILABLE","reason":"missing_new"}
    with np.load(old,allow_pickle=False) as a, np.load(new,allow_pickle=False) as b:
        if set(a.files)!=set(b.files):return {"status":"UNAVAILABLE","reason":"array_fields",
                                             "old":sorted(a.files),"new":sorted(b.files)}
        rows={}
        for key in sorted(a.files):
            rows[key]=compare_array(np.asarray(a[key]),np.asarray(b[key]))
    status="UNAVAILABLE" if any(v["status"]=="UNAVAILABLE" for v in rows.values()) else (
        "LEGAL_DIFFERENCE_OBSERVED" if any(v["status"]=="LEGAL_DIFFERENCE_OBSERVED" for v in rows.values()) else "EXACT_BITWISE_MATCH")
    return {"status":status,"scope":"named_npz_arrays_only","arrays":rows}

def compare_array(x:np.ndarray,y:np.ndarray)->dict[str,Any]:
    if x.shape!=y.shape or x.dtype!=y.dtype or x.dtype not in (np.dtype("float64"),np.dtype("int64")):
        return {"status":"UNAVAILABLE","reason":"shape_or_dtype","old_shape":list(x.shape),"new_shape":list(y.shape)}
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        return {"status":"UNAVAILABLE","reason":"nonfinite"}
    delta=np.abs(y.astype(np.float64)-x.astype(np.float64))
    return {"status":"EXACT_BITWISE_MATCH" if np.array_equal(x.view(np.uint64),y.view(np.uint64)) else "LEGAL_DIFFERENCE_OBSERVED",
            "shape":list(x.shape),"dtype":str(x.dtype),"bitwise_mismatches":int(np.count_nonzero(x.view(np.uint64)!=y.view(np.uint64))),
            "max_absolute_difference":float(np.max(delta)) if delta.size else 0.0,
            "max_index":list(np.unravel_index(int(np.argmax(delta)),delta.shape)) if delta.size else []}

def compare_intermediates(repo:Path,output:Path,references:Mapping[str,str])->dict[str,Any]:
    if reference_intermediate_hashes(repo)!=dict(references):
        raise RepeatBlocked("BLOCKED__SEALED_REFERENCE_CHANGED")
    old=repo/OLD_ROOT
    return {name:(compare_npz(old/name,output/name) if name.endswith(".npz") else
                  compare_receipt(old/name,output/name)) for name in references}

def source_snapshot(repo:Path)->dict[str,str]:
    tracked_src=[Path(name) for name in git(repo,"ls-files","src/ch5_two_asset_hank").splitlines()]
    paths=[*(OLD_ROOT/name for name in SEALED),DISTANCE,Path("TASK_CURRENT.md"),FUTURE_TASK_RELATIVE,
        Path("validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py"),
        Path("validators/multi_province/k1b_turn6_same_frozen_input_repeat/run.py"),
        *(Path(name) for name in HELPER_SHA),*tracked_src]
    return {p.as_posix():sha(repo/p) for p in paths}

def future_gate(repo:Path,execution_id:str|None)->None:
    if not execution_id:raise RepeatBlocked("EXECUTION_AUTHORIZATION_REQUIRED")
    if re.fullmatch(r"[A-Za-z0-9_-]{1,80}",execution_id) is None:
        raise RepeatBlocked("BLOCKED__EXECUTION_ID_FORMAT")
    task=(repo/"TASK_CURRENT.md").read_text(encoding="utf-8")
    required=(f"Task ID: `{FUTURE_TASK_ID}`",f"Status: `{FUTURE_STATUS}`",
              f"Execution authorization ID: `{execution_id}`",
              f"Authorized output root: `{OUTPUT.as_posix()}`")
    if not all(x in task for x in required):
        raise RepeatBlocked("BLOCKED__FRESH_EXECUTION_TASK_GATE",FUTURE_TASK_ID)
    future=repo/FUTURE_TASK_RELATIVE
    if not future.is_file() or not all(x in future.read_text(encoding="utf-8") for x in required):
        raise RepeatBlocked("BLOCKED__FUTURE_TASK_SOURCE_BINDING")
    if sha(future)!=sha(repo/"TASK_CURRENT.md"):
        raise RepeatBlocked("BLOCKED__FUTURE_TASK_CURRENT_HASH_MISMATCH")
    rel=Path(__file__).relative_to(repo).as_posix()
    if git(repo,"status","--porcelain=v1","--",rel,"src",str(DISTANCE)):
        raise RepeatBlocked("BLOCKED__EXECUTION_SOURCE_DIRTY")
    blob=subprocess.check_output(["git","show",f"HEAD:{rel}"],cwd=repo)
    if sha(repo/rel)!=hashlib.sha256(blob).hexdigest().upper():
        raise RepeatBlocked("BLOCKED__EXECUTION_RUNNER_IDENTITY")


def execute_once(repo:Path,execution_id:str|None)->str:
    """Future-only; never call from the zero-science preparation task."""
    repo=repo.resolve()
    future_gate(repo,execution_id)
    output=repo/OUTPUT
    if output.exists():
        raise RepeatBlocked("BLOCKED__FUTURE_EVIDENCE_PATH_EXISTS")
    try:
        pre=preflight(repo)
        before=source_snapshot(repo)
        references=reference_intermediate_hashes(repo)
        entering=load_bundle(repo,6)
    except BaseException as exc:
        record_pre_call_failure(output,exc,execution_id)
        raise
    guard=BudgetGuard()
    output.mkdir(parents=True,exist_ok=False)
    save_json(output/"preflight.json",pre)
    ledger:dict[str,Any]={}
    state={"province":None,"ledger_unresolved":False,"original_terminal":None,
           "terminal":"CALL_LEDGER_UNRESOLVED"}
    # No model import occurs until the future task gate and exact static binding pass.
    sys.path.insert(0,str(repo));sys.path.insert(0,str(repo/"src"))
    from ch5_two_asset_hank.corrected_diagnostic import optionb_turn2_household_integration as base
    from ch5_two_asset_hank.corrected_diagnostic.contracts import CorrectedDiagnosticGrid
    from validators.multi_province.k1b_turn5_turn6_bounded_continuation import run as old
    originals=(base._map_checkpoint,base._direct_update,
               base._terminal_kfe_with_accounting,base.monotonicity_preserving_relaxation)
    original_entering=base.ENTERING_STATE_RELATIVE
    original_task=base.TASK_RELATIVE
    ledger=old.new_ledger(6)
    ledger.update(terminal_kfe_attempts=0,full_integrations=0,
                  relaxation_helper_invocations=0,alpha_candidates=0)
    def map_hook(*args:Any,**kwargs:Any):
        local=args[6];budget=args[5];prior=dict(local);province=state["province"]
        guard.enter("corrected_policy_maps",province)
        guard.reserve({"selector_evaluations":800},province)
        try:return originals[0](*args,**kwargs)
        except BaseException as original_failure:
            # Production merges local counts only after normal map return. The
            # selector budget object is the exact consumed counter on failure.
            local.update(selector_evaluations=int(budget.selector_evaluations),
                         scalar_root_invocations=int(budget.root_invocations),
                         interior_z_root_invocations=int(budget.interior_z_root_invocations),
                         interior_a_switching_root_invocations=int(budget.interior_a_switching_root_invocations),
                         joint_switching_root_invocations=int(budget.joint_switching_root_invocations))
            try:
                base._accumulate_local(ledger,prior,local)
                guard.reconcile(ledger)
            except BaseException as exc:
                state["ledger_unresolved"]=True
                state["original_terminal"]=getattr(original_failure,"terminal",type(original_failure).__name__)
                raise RepeatBlocked("CALL_LEDGER_UNRESOLVED",{"stage":"map","cause":str(exc),
                    "original_terminal":state["original_terminal"]}) from exc
            raise
    def direct_hook(*args:Any,**kwargs:Any):
        guard.reserve({"direct_hjb_updates":1,"relaxation_helper_invocations":1,"alpha_candidates":53},state["province"])
        guard.enter("direct_hjb_updates",state["province"])
        return originals[1](*args,**kwargs)
    def kfe_hook(*args:Any,**kwargs:Any):
        guard.enter("terminal_kfe_attempts",state["province"])
        guard.reserve({k:1 for k in ("scc_decompositions",
            "restricted_dense_scipy_linalg_svd_gesvd","normalized_stationary_candidates",
            "q_transpose_times_p","corrected_aggregate_evaluations")})
        ledger["terminal_kfe_attempts"]+=1
        return originals[2](*args,**kwargs)
    def relaxation_hook(*args:Any,**kwargs:Any):
        guard.enter("relaxation_helper_invocations")
        ledger["relaxation_helper_invocations"]+=1
        try:accepted,receipt=originals[3](*args,**kwargs)
        except BaseException as exc:
            detail=getattr(exc,"detail",None)
            attempts=detail.get("attempts") if isinstance(detail,Mapping) else None
            if not isinstance(attempts,list):
                state["ledger_unresolved"]=True
                state["original_terminal"]=getattr(exc,"terminal",type(exc).__name__)
                raise RepeatBlocked("CALL_LEDGER_UNRESOLVED",{"stage":"relaxation","cause":str(exc),
                    "original_terminal":state["original_terminal"]}) from exc
            guard.reserve({"alpha_candidates":len(attempts)})
            guard.attempted["alpha_candidates"]+=len(attempts)
            ledger["alpha_candidates"]+=len(attempts)
            raise
        attempts=receipt.get("attempts")
        if not isinstance(attempts,list):
            state["ledger_unresolved"]=True
            raise RepeatBlocked("CALL_LEDGER_UNRESOLVED",{"stage":"relaxation_receipt"})
        guard.reserve({"alpha_candidates":len(attempts)})
        guard.attempted["alpha_candidates"]+=len(attempts)
        ledger["alpha_candidates"]+=len(attempts)
        return accepted,receipt
    base._map_checkpoint=map_hook
    base._direct_update=direct_hook
    base._terminal_kfe_with_accounting=kfe_hook
    base.monotonicity_preserving_relaxation=relaxation_hook
    base.ENTERING_STATE_RELATIVE=OLD_ROOT/"turn6_k1b_input_candidate.json"
    base.TASK_RELATIVE=FUTURE_TASK_RELATIVE
    try:
        task_hashes=base._task_hashes(repo)
        core_hashes=base._scientific_code_hashes(repo)
        native_grid=base.oracle.MatlabFaithfulHJBGrid(np.linspace(-2,5,20),np.linspace(0,10,20),
            np.array([0.8,1.3]),np.array([[-1/3,1/3],[1/3,-1/3]]))
        grid=CorrectedDiagnosticGrid(native_grid.b,native_grid.a,native_grid.z)
        params=base.oracle.EconomicParams(0.05,2.0,5.0,0.1,2.0,1e-6,0.0,0.0)
        results=[]
        for i,province in enumerate(canonical_order(repo)):
            state["province"]=i
            # Reserve the *maximum* bounded child envelope before entry. The
            # frozen source's province-local selector/root ceilings constrain
            # every nested invocation. Actual counts are reconciled on return
            # and on the first exceptional exit.
            guard.reserve({"source_native_initializations":1,"scalar_labor_roots_attempted":800,
                "scalar_labor_roots_returned":800,"corrected_policy_maps":51,
                "d2_q_assemblies":51,"selector_evaluations":40800,
                "scalar_selector_root_invocations":20000000,"direct_hjb_updates":50,
                "hjb_checkpoint_evaluations_after_update":50,
                "relaxation_helper_invocations":50,"alpha_candidates":2650,
                "terminal_kfe_attempts":1,"scc_decompositions":1,
                "restricted_dense_scipy_linalg_svd_gesvd":1,
                "normalized_stationary_candidates":1,"q_transpose_times_p":1,
                "corrected_aggregate_evaluations":1},i)
            try:
                result=base._solve_province(repo,output/"turn6",i,province,
                    entering["states"][i],grid,native_grid,params,
                    task_hashes,core_hashes,ledger)
            finally:
                # Direct/root/KFE counts mutate the shared ledger on attempts;
                # exceptional map exits were recovered by map_hook.
                guard.reconcile(ledger)
            results.append(result)
        if len(results)!=31:raise RepeatBlocked("FAIL__HOUSEHOLD_BATCH_INCOMPLETE")
        integration_envelope={"household_batch_constructions":1,"full_integrations":1,
            "source_faithful_labor_reconstructions":1,"frozen_k1b_quantity_allocations":1,
            "k1b_feedback_calls":1,"c1_residual_govinv_constructions":1,
            "firm_evaluations":31,"composite_wage_batches":1,"monetary_assignments":1,
            "fiscal_diagnostic_batches":1,"completed_raw_ra0_vectors":1,
            "deterministic_next_k1b_preparations":1,"raw_next_payoff_same_s_constructions":1}
        guard.reserve(integration_envelope)
        guard.enter("household_batch_constructions")
        ledger["household_batch_constructions"]+=1
        rows=[{"province_index":i,"province":row["province"],"checkpoint":row["checkpoint"],
               "B":row["B"],"D":row["D"],"backward_error_max":row["backward_error_max"]}
              for i,row in enumerate(results)]
        save_json(output/"turn6/household_batch_receipt.json",
                  {"status":"PASS","province_count":31,"rows":rows})
        guard.enter("full_integrations")
        ledger["full_integrations"]+=1
        original_payoff = old.safety.ordered_payoff
        def payoff_hook(*args:Any,**kwargs:Any):
            guard.enter("raw_next_payoff_same_s_constructions")
            return original_payoff(*args,**kwargs)
        integration_lines=integration_entry_lines(old.integrate_turn)
        integration_trace=make_entry_trace(old.integrate_turn.__code__,integration_lines,guard)
        prior_trace=sys.gettrace()
        old.safety.ordered_payoff = payoff_hook
        sys.settrace(integration_trace)
        integration_failure=None
        try:
            integration=old.integrate_turn(repo,output,output/"turn6",6,entering["states"],
                old._batch(results),entering["S"],entering["hashes"]["S"],ledger,rows)
        except BaseException as exc:
            integration_failure=exc
            state["original_terminal"]=getattr(exc,"terminal",type(exc).__name__)
            raise
        finally:
            sys.settrace(prior_trace)
            old.safety.ordered_payoff = original_payoff
            violation=None
            for key in CEILINGS:
                if key in ledger and key not in ("raw_next_payoff_same_s_constructions",):
                    n=int(ledger[key])
                    if n>guard.ceilings[key]:
                        violation={"category":key,"actual":n}
                    guard.attempted[key]=max(guard.attempted[key],n)
            if violation is not None:
                if integration_failure is not None:
                    state["ledger_unresolved"]=True
                else:
                    raise RepeatBlocked("BLOCKED__CONSUMED_CALL_BUDGET",violation)
        save_json(output/"turn6_scientific_ledger.json",ledger)
        old.seal_generated_bundle(output,integration,7)
        replay=load_bundle(repo,7,OUTPUT)
        reference=load_bundle(repo,7)
        comparison={"carrier":compare_carrier(reference,replay),
                    "intermediates":compare_intermediates(repo,output,references),
                    "repeatability_threshold":None}
        if source_snapshot(repo)!=before or reference_intermediate_hashes(repo)!=references:
            raise RepeatBlocked("BLOCKED__POST_EXECUTION_SOURCE_OR_INPUT_HASH_CHANGED")
        save_json(output/"comparison_receipt.json",comparison)
        unavailable=[name for name,row in comparison["intermediates"].items() if row["status"]=="UNAVAILABLE"]
        if comparison["carrier"]["classification"]=="UNAVAILABLE" or unavailable:
            raise RepeatBlocked("FAIL__COMPARISON_UNAVAILABLE",{"intermediates":unavailable,
                "carrier":comparison["carrier"]["classification"]})
        state["terminal"]="PASS__TURN6_SAME_FROZEN_INPUT_REPEAT__ONE_PAIR_ONLY"
        return state["terminal"]
    except BaseException as exc:
        if state["original_terminal"] is None:
            state["original_terminal"]=getattr(exc,"terminal",type(exc).__name__)
        state["terminal"]="CALL_LEDGER_UNRESOLVED" if state["ledger_unresolved"] else state["original_terminal"]
        raise
    finally:
        (base._map_checkpoint,base._direct_update,base._terminal_kfe_with_accounting,
         base.monotonicity_preserving_relaxation)=originals
        base.ENTERING_STATE_RELATIVE=original_entering
        base.TASK_RELATIVE=original_task
        save_json(output/"terminal_receipt.json",{"terminal":state["terminal"],
            "original_terminal":state["original_terminal"],"source_ledger":ledger,
            "guard_attempted":guard.attempted,"guard_denied":guard.denied,
            "call_ledger_resolved":not state["ledger_unresolved"],"turn7_household_calls":0})


def main(argv:list[str]|None=None)->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository",type=Path,default=REPOSITORY)
    parser.add_argument("--execute",action="store_true",help="future distinct task gate required")
    parser.add_argument("--execution-id")
    args=parser.parse_args(argv)
    if not args.execute:
        print(json.dumps(preflight(args.repository),ensure_ascii=True,indent=2,default=str))
        return 0
    print(execute_once(args.repository,args.execution_id))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
