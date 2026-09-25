"""Static preflight and future one-shot C7 -> C8 bounded R2 second comparison.

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
import stat
import subprocess
import sys
import inspect
from pathlib import Path
from typing import Any, Mapping

import numpy as np

REPOSITORY = Path(__file__).resolve().parents[3]
FUTURE_TASK_ID = "CH5_K1B_TURN8_OUTER_R2_EXECUTION_20260925"
FUTURE_STATUS = "ACTIVE__ONE_SHOT_TURN8_OUTER_R2"
FUTURE_TASK_RELATIVE = Path("tasks/CH5_K1B_TURN8_OUTER_R2_EXECUTION_20260925.md")
MANIFEST_SHA = "413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91"
ENTERING_MANIFEST_SHA = "20861D4ADDBDF1099854EB86B00D24A097C627838B3F6EF5AFAEDABFFD647E5E"
PRIOR_COMPARISON_SHA = "6DE97F35A8D599183F19F920A95B61CC01CE21B3E6E1AFAB19935FC44623835E"
PRIOR_TERMINAL_SHA = "E4753713354D54B49716574A29424D4F709A427851DE7F1CC9B7CDAA8D31D3FB"
OLD_ROOT = Path("reports/ch5_k1b_turn7_outer_r2_20260925_run001")
OUTPUT = Path("reports/ch5_k1b_turn8_outer_r2_20260925_run001")
DISTANCE = Path("docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv")
SRC_TREE = "00682b2e1a7ba23665f6e16f6acf48ad35874883"
OLD_RUNNER_SHA = "92018027502FFA5281F9BFAC91EE70D2BED17876B65100B3321819B2C0C59DB6"
DISTANCE_SHA = "51A04FCAA1FA519B142BE2A155640F77E8746493AFDF4865ED243B96526E550D"
REPEAT_RUNNER = Path("validators/multi_province/k1b_turn6_same_frozen_input_repeat/run.py")
REPEAT_RUNNER_SHA = "E362B921D4984669C3257A671684F55809702531522D253C26D80886786880B2"
TURN7_RUNNER = Path("validators/multi_province/k1b_turn7_outer_r2/run.py")
TURN7_RUNNER_SHA = "B9632DDA56AF9C875B444B3448FFB231B46D113A48756023C6D3A02D8D1E1AFA"
ADOPTION = Path("docs/CH5_FULL_OUTER_STATE_STOP_FAILURE_BUDGET_OWNER_ADOPTION_20260925.md")
ADOPTION_SHA = "57F4BED608F00AD8040CC9A2576BB3357A4470CE7FFEADC8E9BDB7EB44C86A5F"
PROPOSAL = Path("docs/CH5_OUTER_STOP_FAILURE_BUDGET_CONTRACT_PROPOSAL_20260923.md")
PROPOSAL_SHA = "5D3BFE7B914DE3F6BE3B99E75E80680B18A4054FB186EBB715D865F4008DEAC6"
STRICT_LEVEL = 1e-6
HELPER_SHA = {
    "validators/multi_province/k1b_turn3_lagged_raw_ra0_activation_safety_gate/run.py": "2A7B8B28EDB2C6D4F1DF8A1211D9CB04BF018CD1C709B8E8F2903052E3071454",
    "validators/multi_province/k1b_turn4_corrected_household_kfe_and_one_turn_integration/run.py": "098D80AAB0E91BB511F2AF05E1DBC51744979206435A4252B602B03C14DEDA59",
    "validators/multi_province/corrected_2018_single_turn/run.py": "9EAF82373EE564E5F27BEA14D49D2177E0637A6969D946C86F519608FFBAE614",
}
SEALED = {
    "turn8_k1b_input_candidate.json": "30EDAECEA59ABA03EFFD6C11530617BB7CF80FED175F58437F4DACA9E96D2F3A",
    "turn8_k1b_frozen_share_payoff_plan.npz": "E6B5D428C1070C6F9F6D9C450F7CDB0D4C2C54F0658074C9C75E60E8FDB743DB",
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
    "raw_next_payoff_same_s_constructions":1,"turn7_household_calls":0,"turn8_household_calls":1,
    "turn9_household_calls":0,
    "full_space_800_dense_scipy_linalg_svd_gesvd":0,"scientific_retries":0,
    "solver_substitutions":0,"k2_calls":0,"ge_annual_shock_irf_welfare_results_calls":0,
    "matlab_scientific_calls":0,
}
PER_PROVINCE = {"corrected_policy_maps":51,"selector_evaluations":40800,
                "scalar_selector_root_invocations":20000000,"direct_hjb_updates":50,
                "terminal_kfe_attempts":1}
TWO_TURN_CEILINGS = {key: 2*value for key,value in CEILINGS.items()}
TWO_TURN_CEILINGS.update(turn7_household_calls=1,turn8_household_calls=1,
                         turn9_household_calls=0)
FIELDS = ("Yt","Lt","wjt","rk","Kt_prev","w","raw_ra0","rah","S")

class RepeatBlocked(RuntimeError):
    def __init__(self, terminal: str, detail: Any = None):
        super().__init__(terminal)
        self.terminal, self.detail = terminal, detail


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git",*args],cwd=repo,text=True).strip()


def output_target(output:Path,runtime:Mapping[str,Any],path:Path)->Path:
    output=output.absolute()
    path=Path(path).absolute()
    try:relative=path.relative_to(output)
    except ValueError as exc:
        raise RepeatBlocked("BLOCKED__OUTPUT_PATH_OUTSIDE_OWNED_ROOT",str(path)) from exc
    if not relative.parts or not owns_output_root(output,runtime):
        raise RepeatBlocked("BLOCKED__FUTURE_EVIDENCE_ROOT_NOT_OWNED",str(path))
    parent=output
    for part in relative.parts[:-1]:
        parent=parent/part
        if not owns_output_root(output,runtime):
            raise RepeatBlocked("BLOCKED__FUTURE_EVIDENCE_ROOT_NOT_OWNED",str(path))
        if not path_components_safe(parent):
            raise RepeatBlocked("BLOCKED__OUTPUT_PARENT_REPARSE_POINT",str(parent))
        parent.mkdir(exist_ok=True)  # parents=False cannot recreate a missing root.
    if not owns_output_root(output,runtime):
        raise RepeatBlocked("BLOCKED__FUTURE_EVIDENCE_ROOT_NOT_OWNED",str(path))
    return path

def write_output_json(output:Path,runtime:Mapping[str,Any],path:Path,value:Any)->None:
    payload=json.dumps(value,ensure_ascii=True,allow_nan=False,indent=2)+"\n"
    target=output_target(output,runtime,path)
    try:
        with target.open("x",encoding="utf-8") as stream:stream.write(payload)
    except FileExistsError as exc:
        raise RepeatBlocked("BLOCKED__OUTPUT_RECEIPT_EXISTS",str(target)) from exc

def write_output_npz(output:Path,runtime:Mapping[str,Any],path:Path,
                     original_writer:Any,*args:Any,**kwargs:Any)->None:
    target=output_target(output,runtime,path)
    try:
        with target.open("xb") as stream:original_writer(stream,*args,**kwargs)
    except FileExistsError as exc:
        raise RepeatBlocked("BLOCKED__OUTPUT_ARTIFACT_EXISTS",str(target)) from exc

def source_receipt_target(path:Path,value:Any)->Path:
    # The frozen source writes a pre-relaxation solve receipt and later adds
    # checkpoint identifiers at the same name. Preserve both exclusively.
    if (path.name=="direct_solve_receipt.json" and isinstance(value,Mapping)
            and "checkpoint_from" not in value):
        return path.with_name("direct_solve_pre_relaxation_receipt.json")
    return path

def record_pre_call_failure(output:Path,exc:BaseException,execution_id:str)->None:
    runtime:dict[str,Any]={"output_identity":None}
    claim_output_root(output,runtime)
    write_output_json(output,runtime,output/"first_failure.json",{
        "terminal":getattr(exc,"terminal",type(exc).__name__),
        "literal_scientific_call_ledger":{k:0 for k in CEILINGS},
        "execution_id":execution_id})

def claim_output_root(output:Path,runtime:dict[str,Any])->None:
    if not path_components_safe(output.parent):
        raise RepeatBlocked("BLOCKED__OUTPUT_PARENT_REPARSE_POINT",str(output.parent))
    output.mkdir(parents=True,exist_ok=False)
    if not path_components_safe(output):
        raise RepeatBlocked("BLOCKED__FUTURE_EVIDENCE_ROOT_NOT_OWNED",str(output))
    identity=output.lstat()
    if not identity.st_ino:
        raise RepeatBlocked("BLOCKED__OUTPUT_IDENTITY_UNAVAILABLE",str(output))
    runtime["output_identity"]=(identity.st_dev,identity.st_ino)

def path_components_safe(path:Path)->bool:
    """Reject symlink/reparse path components; a missing final child is allowed."""
    path=path.absolute()
    for component in reversed((path,*path.parents)):
        try:identity=component.lstat()
        except FileNotFoundError:return True
        except OSError:return False
        if stat.S_ISLNK(identity.st_mode):return False
        if os.name=="nt":
            attributes=getattr(identity,"st_file_attributes",None)
            if attributes is None or attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT:return False
    return True

def owns_output_root(output:Path,runtime:Mapping[str,Any])->bool:
    expected=runtime.get("output_identity")
    if expected is None:return False
    if not path_components_safe(output):return False
    try:identity=output.lstat()
    except OSError:return False
    return bool(identity.st_ino) and stat.S_ISDIR(identity.st_mode) and (identity.st_dev,identity.st_ino)==expected

def guard_output_mutation(output:Path,runtime:Mapping[str,Any],path:Path)->None:
    """Check ownership and every existing output component before a path mutation."""
    output=output.absolute()
    path=Path(path).absolute()
    try:relative=path.relative_to(output)
    except ValueError as exc:
        raise RepeatBlocked("BLOCKED__OUTPUT_PATH_OUTSIDE_OWNED_ROOT",str(path)) from exc
    if not relative.parts or not owns_output_root(output,runtime):
        raise RepeatBlocked("BLOCKED__FUTURE_EVIDENCE_ROOT_NOT_OWNED",str(path))
    if not path_components_safe(path):
        raise RepeatBlocked("BLOCKED__OUTPUT_COMPONENT_REPARSE_POINT",str(path))

def install_output_mutation_guards(output:Path,runtime:Mapping[str,Any])->tuple[Any,Any]:
    """Intercept Path mutations in reused source for the duration of one run."""
    original_mkdir,original_unlink=Path.mkdir,Path.unlink
    def guarded_mkdir(path:Path,*args:Any,**kwargs:Any)->None:
        guard_output_mutation(output,runtime,path)
        original_mkdir(path,*args,**kwargs)
    def guarded_unlink(path:Path,*args:Any,**kwargs:Any)->None:
        guard_output_mutation(output,runtime,path)
        original_unlink(path,*args,**kwargs)
    Path.mkdir=guarded_mkdir
    Path.unlink=guarded_unlink
    return original_mkdir,original_unlink

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
        'raw = np.asarray([firm.ra0 for firm in firms], dtype=np.float64)':("completed_raw_ra0_vectors",),
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

def bind_future_task(base:Any)->Path:
    previous=base.TASK_RELATIVE
    base.TASK_RELATIVE=FUTURE_TASK_RELATIVE
    return previous

def restore_task_binding(base:Any,previous:Path)->None:
    base.TASK_RELATIVE=previous


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


def prior_output_binding(repo:Path)->dict[str,Any]:
    """Read back every accepted C7 artifact and its consumed turn7 ledger."""
    root=repo/OLD_ROOT
    if not path_components_safe(root):
        raise RepeatBlocked("BLOCKED__PRIOR_C7_REPARSE_POINT",str(root))
    manifest_path=root/"execution_artifact_manifest.json"
    entering_path=root/"turn8_entering_bundle_manifest.json"
    comparison_path=root/"comparison_receipt.json"
    terminal_path=root/"terminal_receipt.json"
    checks={"full_manifest_hash":sha(manifest_path)==MANIFEST_SHA,
            "entering_manifest_hash":sha(entering_path)==ENTERING_MANIFEST_SHA,
            "prior_comparison_hash":sha(comparison_path)==PRIOR_COMPARISON_SHA,
            "prior_terminal_hash":sha(terminal_path)==PRIOR_TERMINAL_SHA}
    if not all(checks.values()):raise RepeatBlocked("BLOCKED__PRIOR_C7_IDENTITY",checks)
    manifest=json.loads(manifest_path.read_text(encoding="utf-8"))
    entries=manifest.get("entries",[])
    names=[row.get("path") for row in entries]
    actual=sorted(p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()
                  and p!=manifest_path)
    checks["full_manifest_complete"]=(len(entries)==manifest.get("entry_count")==5141
        and len(names)==len(set(names)) and sorted(names)==actual
        and path_components_safe(root)
        and all(path_components_safe(p) for p in root.rglob("*"))
        and sum(row.get("bytes",-1) for row in entries)==manifest.get("total_bytes")
        and all((root/name).is_file() and path_components_safe(root/name)
                and (root/name).stat().st_size==row["bytes"] and sha(root/name)==row["sha256"]
                for name,row in zip(names,entries)))
    entering=json.loads(entering_path.read_text(encoding="utf-8"))
    entering_readback=json.loads((root/"turn8_entering_bundle_readback.json").read_text(encoding="utf-8"))
    checks["entering_seal"]=(entering.get("turn")==8 and entering.get("sealed_before_household") is True
        and entering.get("entry_count")==4 and
        entering_readback.get("status")=="PASS" and entering_readback.get("bad_paths")==[]
        and entering_readback.get("manifest_sha256")==ENTERING_MANIFEST_SHA and
        sha(root/"turn8_entering_bundle_readback.json") in
        {row["sha256"] for row in entries if row["path"]=="turn8_entering_bundle_readback.json"})
    prior=json.loads(terminal_path.read_text(encoding="utf-8"))
    carrier=json.loads(comparison_path.read_text(encoding="utf-8"))["carrier"]
    attempted=prior.get("guard_attempted",{})
    source=prior.get("source_ledger",{})
    checks["prior_terminal"]=(prior.get("terminal")=="VALID__NINE_COMPONENT_LEVEL_NOT_MET"
        and prior.get("call_ledger_resolved") is True and prior.get("guard_denied")==[]
        and source.get("turn7_household_calls")==1 and source.get("turn8_household_calls")==0)
    checks["prior_comparison"]=(carrier.get("classification")=="LEGAL_DIFFERENCE_OBSERVED"
        and carrier.get("all_nine_strictly_below_level") is False
        and carrier.get("r2_confirmed") is False and len(carrier.get("components",{}))==9
        and sum(bool(row.get("strictly_below_1e6")) for row in carrier["components"].values())==2)
    checks["prior_ledger"]=(set(CEILINGS)-{"turn9_household_calls"}<=set(attempted)
        and all(isinstance(n,int) and n>=0 and source.get(key,0)==n
                and n<=TWO_TURN_CEILINGS[key] for key,n in attempted.items()
                if key in TWO_TURN_CEILINGS)
        and all(attempted.get(key,0)==0 for key,value in TWO_TURN_CEILINGS.items() if value==0))
    if not all(checks.values()):raise RepeatBlocked("BLOCKED__PRIOR_C7_READBACK",checks)
    return {"checks":checks,"prior_attempted":attempted,"prior_carrier":carrier,
            "prior_terminal":prior["terminal"],"manifest_sha256":MANIFEST_SHA}


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
            "new_output_absent":not (repo/OUTPUT).exists(),
             "full_prior_manifest":sha(repo/OLD_ROOT/"execution_artifact_manifest.json")==MANIFEST_SHA,
             "accepted_repeat_runner":sha(repo/REPEAT_RUNNER)==REPEAT_RUNNER_SHA,
             "accepted_turn7_runner":sha(repo/TURN7_RUNNER)==TURN7_RUNNER_SHA,
             "owner_adoption":sha(repo/ADOPTION)==ADOPTION_SHA,
             "accepted_proposal":sha(repo/PROPOSAL)==PROPOSAL_SHA}
    if not all(checks.values()):raise RepeatBlocked("BLOCKED__STATIC_PREFLIGHT",checks)
    prior=prior_output_binding(repo)
    c7=load_bundle(repo,8)
    return {"status":"PASS__STATIC_PREFLIGHT_ONLY","checks":checks,
            "C7_entering":c7["hashes"],"prior_C6_to_C7":prior["prior_terminal"],
            "prior_output_checks":prior["checks"],
            "src_tree":SRC_TREE,"old_runner_sha256":OLD_RUNNER_SHA,
            "helper_sha256":HELPER_SHA,"distance_sha256":DISTANCE_SHA,
             "repeat_runner_sha256":REPEAT_RUNNER_SHA,"owner_adoption_sha256":ADOPTION_SHA,
            "province_count":31,"S_orientation":"destination_by_origin",
            "planned_output_root":str(repo/OUTPUT),"environment":environment_snapshot(),"scientific_calls":0}


class BudgetGuard:
    def __init__(self,ceilings:Mapping[str,int]=CEILINGS,
                 prior:Mapping[str,int]|None=None,combined:Mapping[str,int]=TWO_TURN_CEILINGS):
        self.ceilings=dict(ceilings);self.combined=dict(combined)
        self.prior={k:int((prior or {}).get(k,0)) for k in ceilings}
        self.attempted={k:0 for k in ceilings};self.per_province={};self.denied=[]
    def reserve(self,amounts:Mapping[str,int],province:int|None=None)->None:
        for key,n in amounts.items():
            if (key not in self.ceilings or not isinstance(n,int) or n<0 or
                self.attempted[key]+n>self.ceilings[key] or
                self.prior[key]+self.attempted[key]+n>self.combined[key]):
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
            if n>self.ceilings[key] or self.prior[key]+n>self.combined[key]:
                raise RepeatBlocked("BLOCKED__CONSUMED_CALL_BUDGET",{"category":key,"actual":n})
            # A guarded attempt can fail before the source records its local
            # count; never erase that already consumed entry on reconciliation.
            self.attempted[key]=max(self.attempted[key],n)
    def reconcile_all(self,ledger:Mapping[str,Any])->None:
        for key,ceiling in self.ceilings.items():
            if key not in ledger:continue
            n=int(ledger[key])
            if n<0 or n>ceiling or self.prior[key]+n>self.combined[key]:
                raise RepeatBlocked("BLOCKED__CONSUMED_CALL_BUDGET",{"category":key,"actual":n})
            self.attempted[key]=max(self.attempted[key],n)

def _arrays(bundle:Mapping[str,Any],turn:int)->dict[str,np.ndarray]:
    rows=bundle["rows"]
    out={k:np.asarray([r["state"][k] for r in rows],dtype=np.float64)
         for k in FIELDS if k not in ("raw_ra0","S")}
    out["raw_ra0"]=np.asarray([r[f"raw_ra0_turn{turn-1}"] for r in rows],dtype=np.float64)
    out["S"]=np.asarray(bundle["S"],dtype=np.float64)
    return out

def compare_carrier(ref:Mapping[str,Any],new:Mapping[str,Any])->dict[str,Any]:
    """Compare complete C7 and C8 checkpoints under the Owner-adopted law."""
    a=_arrays(ref,8);b=_arrays(new,9);rows={}
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
        difference=float(metric[ix])
        rows[key]={"status":"EXACT_BITWISE_MATCH" if not np.any(mismatch) else "LEGAL_DIFFERENCE_OBSERVED",
                    "shape":list(x.shape),"finite":True,"bitwise_mismatch_count":int(np.count_nonzero(mismatch)),
                    "diagnostic_difference":difference,"strictly_below_1e6":difference<STRICT_LEVEL,
                    "max_location":loc,
                    "max_absolute_difference":float(np.max(np.abs(y-x))),"old_at_max":float(x[ix]),"new_at_max":float(y[ix])}
    status="EXACT_BITWISE_MATCH" if all(r["status"]=="EXACT_BITWISE_MATCH" for r in rows.values()) else (
         "UNAVAILABLE" if any(r["status"]=="UNAVAILABLE" for r in rows.values()) else "LEGAL_DIFFERENCE_OBSERVED")
    legal=status!="UNAVAILABLE"
    passed=legal and all(row["strictly_below_1e6"] for row in rows.values())
    return {"classification":status,"components":rows,"strict_level":STRICT_LEVEL,
            "all_nine_strictly_below_level":passed if legal else None,
            "r2_second_comparison_only":True,"r2_confirmed":False}

def clipped_ra_upper_summary(bundle:Mapping[str,Any])->dict[str,Any]:
    """Report the firm's accepted upper clipping without using it as a criterion gate."""
    hits=[]
    for i,row in enumerate(bundle["rows"]):
        state=row["state"]
        raw,used,upper=(float(state[key]) for key in ("ra0","ra","ramax"))
        if not all(np.isfinite(value) for value in (raw,used,upper)):
            raise RepeatBlocked("FAIL__CLIPPED_RA_REPORT_UNAVAILABLE",{"province_index":i})
        if raw>upper:
            if used!=upper:
                raise RepeatBlocked("FAIL__CLIPPED_RA_REPORT_INCONSISTENT",{"province_index":i})
            hits.append(i)
    return {"upper_hit_count":len(hits),"province_indices":hits,
            "new_criterion_disqualifier":False,"original_matlab_predicate_passed":len(hits)==0}

def turn8_terminal(prior:Mapping[str,Any],carrier:Mapping[str,Any])->str:
    if prior.get("all_nine_strictly_below_level") is not False:
        raise RepeatBlocked("BLOCKED__PRIOR_FIRST_COMPARISON_NOT_FAILED")
    if carrier["classification"]=="UNAVAILABLE":
        raise RepeatBlocked("FAIL__OUTER_COMPARISON_UNAVAILABLE",carrier)
    return ("VALID__ONE_PASS_UNCONFIRMED_AT_BUDGET" if
            carrier["all_nine_strictly_below_level"] else
            "VALID__LEVEL_NOT_MET_AT_BUDGET")

def source_snapshot(repo:Path)->dict[str,str]:
    tracked_src=[Path(name) for name in git(repo,"ls-files","src/ch5_two_asset_hank").splitlines()]
    paths=[*(OLD_ROOT/name for name in SEALED),DISTANCE,Path("TASK_CURRENT.md"),FUTURE_TASK_RELATIVE,
        Path("validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py"),
        REPEAT_RUNNER,Path("validators/multi_province/k1b_turn7_outer_r2/run.py"),
        Path("validators/multi_province/k1b_turn8_outer_r2/run.py"),ADOPTION,PROPOSAL,
         OLD_ROOT/"execution_artifact_manifest.json",OLD_ROOT/"turn8_entering_bundle_manifest.json",
         OLD_ROOT/"comparison_receipt.json",OLD_ROOT/"terminal_receipt.json",
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
    if git(repo,"status","--porcelain=v1","--","TASK_CURRENT.md",str(FUTURE_TASK_RELATIVE)):
        raise RepeatBlocked("BLOCKED__EXECUTION_TASK_DIRTY")
    for task_path in (Path("TASK_CURRENT.md"),FUTURE_TASK_RELATIVE):
        try:
            blob=subprocess.check_output(["git","show",f"HEAD:{task_path.as_posix()}"],cwd=repo,
                                         stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as exc:
            raise RepeatBlocked("BLOCKED__EXECUTION_TASK_NOT_COMMITTED",task_path.as_posix()) from exc
        if sha(repo/task_path)!=hashlib.sha256(blob).hexdigest().upper():
            raise RepeatBlocked("BLOCKED__EXECUTION_TASK_NOT_COMMITTED",task_path.as_posix())
    rel=Path(__file__).relative_to(repo).as_posix()
    if git(repo,"status","--porcelain=v1","--",rel,"src",str(DISTANCE)):
        raise RepeatBlocked("BLOCKED__EXECUTION_SOURCE_DIRTY")
    blob=subprocess.check_output(["git","show",f"HEAD:{rel}"],cwd=repo)
    if sha(repo/rel)!=hashlib.sha256(blob).hexdigest().upper():
        raise RepeatBlocked("BLOCKED__EXECUTION_RUNNER_IDENTITY")


def _execute_after_gate(repo:Path,execution_id:str,runtime:dict[str,Any])->str:
    output=repo/OUTPUT
    pre=preflight(repo)
    prior=prior_output_binding(repo)
    before=source_snapshot(repo)
    entering=load_bundle(repo,8)
    guard=BudgetGuard(prior=prior["prior_attempted"])
    runtime["guard"]=guard
    claim_output_root(output,runtime)
    write_output_json(output,runtime,output/"preflight.json",pre)
    ledger:dict[str,Any]={}
    state={"province":None,"ledger_unresolved":False,"original_terminal":None,
           "terminal":"CALL_LEDGER_UNRESOLVED"}
    runtime["state"]=state
    # No model import occurs until the future task gate and exact static binding pass.
    sys.path.insert(0,str(repo));sys.path.insert(0,str(repo/"src"))
    from ch5_two_asset_hank.corrected_diagnostic import optionb_turn2_household_integration as base
    from ch5_two_asset_hank.corrected_diagnostic import nonlinear_continuation as nonlinear
    from ch5_two_asset_hank.corrected_diagnostic.contracts import CorrectedDiagnosticGrid
    from validators.multi_province.k1b_turn5_turn6_bounded_continuation import run as old
    originals=(base._map_checkpoint,base._direct_update,
               base._terminal_kfe_with_accounting,base.monotonicity_preserving_relaxation)
    original_entering=base.ENTERING_STATE_RELATIVE
    original_task=base.TASK_RELATIVE
    original_base_writer=base._write_json
    original_nonlinear_writer=nonlinear._write_json
    original_npz_writer=np.savez_compressed
    original_mkdir,original_unlink=Path.mkdir,Path.unlink
    ledger=old.new_ledger(8)
    runtime["ledger"]=ledger
    ledger.update(terminal_kfe_attempts=0,full_integrations=0,turn8_household_calls=0,
                  turn9_household_calls=0,
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
    def bound_json(path:Path,value:Any)->None:
        write_output_json(output,runtime,source_receipt_target(Path(path),value),value)
    def bound_npz(path:Path,*args:Any,**kwargs:Any)->None:
        write_output_npz(output,runtime,Path(path),original_npz_writer,*args,**kwargs)
    try:
        install_output_mutation_guards(output,runtime)
        base._write_json=bound_json
        nonlinear._write_json=bound_json
        np.savez_compressed=bound_npz
        base._map_checkpoint=map_hook
        base._direct_update=direct_hook
        base._terminal_kfe_with_accounting=kfe_hook
        base.monotonicity_preserving_relaxation=relaxation_hook
        base.ENTERING_STATE_RELATIVE=OLD_ROOT/"turn8_k1b_input_candidate.json"
        bind_future_task(base)
        task_hashes=base._task_hashes(repo)
        core_hashes=base._scientific_code_hashes(repo)
        native_grid=base.oracle.MatlabFaithfulHJBGrid(np.linspace(-2,5,20),np.linspace(0,10,20),
            np.array([0.8,1.3]),np.array([[-1/3,1/3],[1/3,-1/3]]))
        grid=CorrectedDiagnosticGrid(native_grid.b,native_grid.a,native_grid.z)
        params=base.oracle.EconomicParams(0.05,2.0,5.0,0.1,2.0,1e-6,0.0,0.0)
        results=[]
        guard.enter("turn8_household_calls")
        ledger["turn8_household_calls"]+=1
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
                guard_output_mutation(output,runtime,output/"turn8")
                runtime["scientific_started"]=True
                result=base._solve_province(repo,output/"turn8",i,province,
                    entering["states"][i],grid,native_grid,params,
                    task_hashes,core_hashes,ledger)
            except BaseException as solve_failure:
                state["original_terminal"]=getattr(solve_failure,"terminal",type(solve_failure).__name__)
                try:guard.reconcile(ledger)
                except BaseException:
                    state["ledger_unresolved"]=True
                raise
            else:
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
        guard_output_mutation(output,runtime,output/"turn8")
        guard.enter("household_batch_constructions")
        ledger["household_batch_constructions"]+=1
        rows=[{"province_index":i,"province":row["province"],"checkpoint":row["checkpoint"],
               "B":row["B"],"D":row["D"],"backward_error_max":row["backward_error_max"]}
              for i,row in enumerate(results)]
        write_output_json(output,runtime,output/"turn8/household_batch_receipt.json",
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
        integration_failure=None
        try:
            old.safety.ordered_payoff = payoff_hook
            sys.settrace(integration_trace)
            integration=old.integrate_turn(repo,output,output/"turn8",8,entering["states"],
                old._batch(results),entering["S"],entering["hashes"]["S"],ledger,rows)
        except BaseException as exc:
            integration_failure=exc
            state["original_terminal"]=getattr(exc,"terminal",type(exc).__name__)
            raise
        finally:
            sys.settrace(prior_trace)
            old.safety.ordered_payoff = original_payoff
            try:
                guard.reconcile_all(ledger)
            except BaseException:
                if integration_failure is not None:
                    state["ledger_unresolved"]=True
                else:
                    raise
        write_output_json(output,runtime,output/"turn8_scientific_ledger.json",ledger)
        old.seal_generated_bundle(output,integration,9)
        replay=load_bundle(repo,9,OUTPUT)
        reference=load_bundle(repo,8)
        comparison={"prior_C6_to_C7":prior["prior_carrier"],
                    "current_C7_to_C8":compare_carrier(reference,replay),
                    "clipped_ra_upper":{"C7":clipped_ra_upper_summary(reference),
                                        "C8":clipped_ra_upper_summary(replay)},
                    "r2_confirmed":False,"two_turn_budget_complete":True}
        if source_snapshot(repo)!=before or prior_output_binding(repo)["checks"]!=prior["checks"]:
            raise RepeatBlocked("BLOCKED__POST_EXECUTION_SOURCE_OR_INPUT_HASH_CHANGED")
        write_output_json(output,runtime,output/"comparison_receipt.json",comparison)
        state["terminal"]=turn8_terminal(prior["prior_carrier"],comparison["current_C7_to_C8"])
        return state["terminal"]
    except BaseException as exc:
        if state["original_terminal"] is None:
            state["original_terminal"]=getattr(exc,"terminal",type(exc).__name__)
        state["terminal"]="CALL_LEDGER_UNRESOLVED" if state["ledger_unresolved"] else state["original_terminal"]
        raise
    finally:
        pending_failure=sys.exc_info()[0] is not None
        Path.mkdir,Path.unlink=original_mkdir,original_unlink
        (base._map_checkpoint,base._direct_update,base._terminal_kfe_with_accounting,
         base.monotonicity_preserving_relaxation)=originals
        base.ENTERING_STATE_RELATIVE=original_entering
        restore_task_binding(base,original_task)
        base._write_json=original_base_writer
        nonlinear._write_json=original_nonlinear_writer
        np.savez_compressed=original_npz_writer
        try:
            write_output_json(output,runtime,output/"terminal_receipt.json",{"terminal":state["terminal"],
                "original_terminal":state["original_terminal"],"source_ledger":ledger,
                "guard_attempted":guard.attempted,"guard_denied":guard.denied,
                "call_ledger_resolved":not state["ledger_unresolved"],
                "turn7_household_calls":ledger["turn7_household_calls"],
                "turn8_household_calls":ledger["turn8_household_calls"],
                "turn9_household_calls":ledger["turn9_household_calls"],
                "prior_turn7_attempted":guard.prior,
                "combined_attempted":{k:guard.prior[k]+guard.attempted[k] for k in guard.attempted}})
        except BaseException:
            if not pending_failure:raise

def failure_detail(runtime:Mapping[str,Any],original:str,execution_id:str)->dict[str,Any]:
    state=runtime["state"] or {}
    guard=runtime["guard"]
    started=bool(runtime["scientific_started"])
    attempted=({k:0 for k in CEILINGS} if not started else
               (dict(guard.attempted) if guard is not None else None))
    source=(dict(runtime["ledger"]) if started and runtime["ledger"] is not None else None)
    unresolved=bool(state.get("ledger_unresolved")) or (started and (attempted is None or source is None))
    return {"terminal":"CALL_LEDGER_UNRESOLVED" if unresolved else original,
            "original_terminal":original,"execution_id":execution_id,
            "literal_scientific_call_ledger":attempted,"source_ledger":source,
            "prior_turn7_attempted":dict(guard.prior) if guard is not None else None,
            "combined_attempted":({k:guard.prior[k]+guard.attempted[k]
                                   for k in guard.attempted} if guard is not None else None),
            "call_ledger_resolved":not unresolved}

def run_after_valid_gate(repo:Path,execution_id:str,action:Any)->str:
    """Protect a future authorized action; tests pass only inert stubs."""
    output=repo/OUTPUT
    if output.exists():
        raise RepeatBlocked("BLOCKED__FUTURE_EVIDENCE_PATH_EXISTS")
    prior_path=list(sys.path)
    prior_trace=sys.gettrace()
    prior_modules=set(sys.modules)
    runtime:dict[str,Any]={"guard":None,"ledger":None,"state":None,"scientific_started":False,
                           "output_identity":None}
    try:
        return action(runtime)
    except BaseException as exc:
        state=runtime["state"] or {}
        original=state.get("original_terminal") or getattr(exc,"terminal",type(exc).__name__)
        detail=failure_detail(runtime,original,execution_id)
        if runtime["output_identity"] is None:
            try:claim_output_root(output,runtime)
            except (OSError,RepeatBlocked) as ownership_error:
                raise RepeatBlocked("BLOCKED__FUTURE_EVIDENCE_ROOT_NOT_OWNED",
                    detail) from ownership_error
        if not owns_output_root(output,runtime):
            raise RepeatBlocked("BLOCKED__FUTURE_EVIDENCE_ROOT_NOT_OWNED",
                detail) from exc
        if not (output/"first_failure.json").exists():
            write_output_json(output,runtime,output/"first_failure.json",detail)
        raise
    finally:
        sys.path[:]=prior_path
        sys.settrace(prior_trace)
        for name in set(sys.modules)-prior_modules:
            if name=="ch5_two_asset_hank" or name.startswith("ch5_two_asset_hank.") or name in ("validators","validators.multi_province") or name.startswith("validators.multi_province."):
                sys.modules.pop(name,None)

def execute_once(repo:Path,execution_id:str|None)->str:
    """Future-only; never call from the zero-science preparation task."""
    repo=repo.resolve()
    future_gate(repo,execution_id)
    return run_after_valid_gate(repo,execution_id,
        lambda runtime:_execute_after_gate(repo,execution_id,runtime))


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
