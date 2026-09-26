"""Static preflight and future one-shot sealed C8 -> C9 turn.

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
import importlib.util
from types import SimpleNamespace
from pathlib import Path
from typing import Any, Mapping

import numpy as np

REPOSITORY = Path(__file__).resolve().parents[3]
FUTURE_TASK_ID = "CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION"
FUTURE_STATUS = "ACTIVE__ONE_SHOT_NEW_C9_POST_FAILURE"
FUTURE_TASK_RELATIVE = Path("tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION.md")
TIMED_CONTRACT = Path("tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_CONTRACT.json")
NEW_EXECUTION_ID = "C9_POST_FAILURE_NEW_ATTEMPT_001"
NEW_BUDGET_NAMESPACE = "C8_START_C9_POST_FAILURE_NEW_ATTEMPT_001_C10_PROSPECTIVE"
BUDGET_PROPOSAL = Path("EVIDENCE/ch5_k1b_c9_new_budget_failed_ledger_policy_zero_science_proposal_20260926/proposed_budget.json")
BUDGET_PROPOSAL_SHA = "66C2C028B07E2CB41FFBB05B643C6EF644291A0FC94C8DAF2FE888518D240460"
BUDGET_ADOPTION = Path("docs/CH5_K1B_C9_NEW_BUDGET_FAILED_LEDGER_POLICY_OWNER_ADOPTION_20260926.md")
BUDGET_ADOPTION_SHA = "C1D88891C08D7526996F72DE6F77AA6D0FA2C593BAD91017877C8B8A0A51573D"
OLD_FAILED_OUTPUT = Path("reports/ch5_k1b_turn9_timed_risk_exception_run001")
OLD_FAILURE_SHA = "21D7579449AD0DCDE532B9D7695E83FF188AD3E09D9D02A798D574000DEED2E0"
MANIFEST_SHA = "5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301"
ENTERING_MANIFEST_SHA = "40200B60729A5B4173E24661843980851F8610A9FA2186F7E411B7FE9E5CDC65"
PRIOR_COMPARISON_SHA = "7F70FB73EAAE0D2BA4C2F60AC5FE071AA963D42EA77A64950D4F94562CB364FC"
PRIOR_TERMINAL_SHA = "01BBF375DA61B387F697A581A9137C57FC87A3DC7CBC937838933A25F7297A7D"
OLD_ROOT = Path("reports/ch5_k1b_turn8_outer_r2_20260925_run001")
OUTPUT = Path("reports/ch5_k1b_turn9_post_failure_new_attempt_001")
PROTECTED_MANIFESTS = {
    Path("reports/ch5_turn6_same_frozen_input_repeat_20260923_run001/execution_artifact_manifest.json"):
        "7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61",
    Path("reports/ch5_k1b_turn7_outer_r2_20260925_run001/execution_artifact_manifest.json"):
        "413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91",
    Path("reports/ch5_k1b_turn8_outer_r2_20260925_run001/execution_artifact_manifest.json"):
        "5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301",
    Path("reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/science_artifact_manifest.json"):
        "5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D",
    Path("reports/ch5_k1b_turn9_timed_risk_exception_run001/partial_artifact_manifest.json"):
        "80BD0D42CB73B4E39B811E759505480542D5A73227014F30B732C34A8AC1FDC3",
}
TIMED_WRAPPER_RELATIVE = Path("validators/multi_province/k1b_turn9_post_failure_new_attempt_timed/run.py")
_active_timed_runtime_ids: set[int] = set()
DISTANCE = Path("docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv")
SRC_TREE = "00682b2e1a7ba23665f6e16f6acf48ad35874883"
OLD_RUNNER_SHA = "92018027502FFA5281F9BFAC91EE70D2BED17876B65100B3321819B2C0C59DB6"
DISTANCE_SHA = "51A04FCAA1FA519B142BE2A155640F77E8746493AFDF4865ED243B96526E550D"
REPEAT_RUNNER = Path("validators/multi_province/k1b_turn6_same_frozen_input_repeat/run.py")
REPEAT_RUNNER_SHA = "E362B921D4984669C3257A671684F55809702531522D253C26D80886786880B2"
TURN7_RUNNER = Path("validators/multi_province/k1b_turn7_outer_r2/run.py")
TURN7_RUNNER_SHA = "B9632DDA56AF9C875B444B3448FFB231B46D113A48756023C6D3A02D8D1E1AFA"
TURN8_RUNNER = Path("validators/multi_province/k1b_turn8_outer_r2/run.py")
TURN8_RUNNER_SHA = "10920535BD50E688D1794B7E69C34F8A5C3C56456CAF6E8DF52FA8D9DFE31831"
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
    "turn9_k1b_input_candidate.json": "FBB18A5B8B4FD94F337510DBB4E62F94188C27863EED1F79FE2E1A71B5BC39AB",
    "turn9_k1b_frozen_share_payoff_plan.npz": "E7E6AF79864F67A28386ECF8BEB3B71C6080E9A6C6E64F4CBA8125E1C19D34DD",
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
    "raw_next_payoff_same_s_constructions":1,"turn8_household_calls":0,"turn9_household_calls":1,
    "turn10_household_calls":0,
    "full_space_800_dense_scipy_linalg_svd_gesvd":0,"scientific_retries":0,
    "solver_substitutions":0,"k2_calls":0,"ge_annual_shock_irf_welfare_results_calls":0,
    "matlab_scientific_calls":0,
}
PER_PROVINCE = {"corrected_policy_maps":51,"selector_evaluations":40800,
                "scalar_selector_root_invocations":20000000,"direct_hjb_updates":50,
                "terminal_kfe_attempts":1}
TWO_TURN_CEILINGS = {key: 2*value for key,value in CEILINGS.items()}
TWO_TURN_CEILINGS.update(turn8_household_calls=0,turn9_household_calls=1,
                         turn10_household_calls=1)
OLD_GOVERNANCE_CHARGE = dict(CEILINGS)  # Administrative full-turn charge, never actual calls.
PROJECT_LIFETIME_GOVERNANCE = {key: OLD_GOVERNANCE_CHARGE[key]+TWO_TURN_CEILINGS[key]
                               for key in CEILINGS}
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
        except FileNotFoundError:return component==path
        except OSError:return False
        if stat.S_ISLNK(identity.st_mode):return False
        attributes=getattr(identity,"st_file_attributes",None)
        if attributes is not None and attributes & getattr(stat,"FILE_ATTRIBUTE_REPARSE_POINT",0):return False
        if os.name=="nt" and attributes is None:return False
    return True

def protected_manifest_checks(repo:Path)->dict[str,bool]:
    checks={}
    for relative,expected in PROTECTED_MANIFESTS.items():
        path=repo/relative
        try:checks[relative.as_posix()]=path_components_safe(path) and path.is_file() and sha(path)==expected
        except OSError:checks[relative.as_posix()]=False
    return checks

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
    """Bind the complete accepted C8 output and sealed entering-C9 bundle."""
    root=repo/OLD_ROOT
    if not path_components_safe(root):
        raise RepeatBlocked("BLOCKED__PRIOR_C8_REPARSE_POINT",str(root))
    manifest_path=root/"execution_artifact_manifest.json"
    entering_path=root/"turn9_entering_bundle_manifest.json"
    readback_path=root/"turn9_entering_bundle_readback.json"
    comparison_path=root/"comparison_receipt.json"
    terminal_path=root/"terminal_receipt.json"
    checks={"full_manifest_hash":sha(manifest_path)==MANIFEST_SHA,
            "entering_manifest_hash":sha(entering_path)==ENTERING_MANIFEST_SHA,
            "entering_readback_hash":sha(readback_path)=="E428D105600D091979B526ADD6BF61E0FC294050B9FAB97FE8B87A29A1012F85",
            "prior_comparison_hash":sha(comparison_path)==PRIOR_COMPARISON_SHA,
            "prior_terminal_hash":sha(terminal_path)==PRIOR_TERMINAL_SHA}
    if not all(checks.values()):raise RepeatBlocked("BLOCKED__PRIOR_C8_IDENTITY",checks)
    manifest=json.loads(manifest_path.read_text(encoding="utf-8"))
    entries=manifest.get("entries",[])
    names=[row.get("path") for row in entries]
    actual=sorted(p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()
                  and p!=manifest_path)
    checks["full_manifest_complete"]=(len(entries)==manifest.get("entry_count")
        and len(names)==len(set(names)) and sorted(names)==actual
        and path_components_safe(root)
        and all(path_components_safe(p) for p in root.rglob("*"))
        and sum(row.get("bytes",-1) for row in entries)==manifest.get("total_bytes")
        and all((root/name).is_file() and path_components_safe(root/name)
                and (root/name).stat().st_size==row["bytes"] and sha(root/name)==row["sha256"]
                for name,row in zip(names,entries)))
    entering=json.loads(entering_path.read_text(encoding="utf-8"))
    readback=json.loads(readback_path.read_text(encoding="utf-8"))
    checks["entering_seal"]=(entering.get("turn")==9 and entering.get("sealed_before_household") is True
        and entering.get("entry_count")==4 and readback.get("status")=="PASS"
        and readback.get("bad_paths")==[] and readback.get("manifest_sha256")==ENTERING_MANIFEST_SHA
        and sha(readback_path) in {row["sha256"] for row in entries
                                  if row["path"]=="turn9_entering_bundle_readback.json"})
    prior=json.loads(terminal_path.read_text(encoding="utf-8"))
    carrier=json.loads(comparison_path.read_text(encoding="utf-8"))["current_C7_to_C8"]
    checks["prior_terminal"]=(prior.get("terminal")=="VALID__LEVEL_NOT_MET_AT_BUDGET"
        and prior.get("call_ledger_resolved") is True and prior.get("guard_denied")==[]
        and prior.get("source_ledger",{}).get("turn8_household_calls")==1
        and prior.get("source_ledger",{}).get("turn9_household_calls")==0)
    checks["prior_comparison"]=(carrier.get("classification")=="LEGAL_DIFFERENCE_OBSERVED"
        and carrier.get("all_nine_strictly_below_level") is False
        and len(carrier.get("components",{}))==9)
    if not all(checks.values()):raise RepeatBlocked("BLOCKED__PRIOR_C8_READBACK",checks)
    return {"checks":checks,"prior_carrier":carrier,"prior_terminal":prior["terminal"],
            "manifest_sha256":MANIFEST_SHA,"prior_attempted":{k:0 for k in CEILINGS}}


def environment_snapshot() -> dict[str,Any]:
    try:scipy=importlib.metadata.version("scipy")
    except importlib.metadata.PackageNotFoundError:scipy=None
    return {"python":sys.version,"numpy":np.__version__,"scipy":scipy,
            "platform":platform.platform(),"machine":platform.machine(),
            "thread_environment":{k:os.environ.get(k) for k in
                ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS",
                 "VECLIB_MAXIMUM_THREADS","NUMEXPR_NUM_THREADS","BLIS_NUM_THREADS")},
            "blas_configuration":np.__config__.show(mode="dicts")}


def budget_binding(repo:Path)->dict[str,Any]:
    """Read adopted maps without treating the historical proposal as self-adopted."""
    if sha(repo/BUDGET_PROPOSAL)!=BUDGET_PROPOSAL_SHA or sha(repo/BUDGET_ADOPTION)!=BUDGET_ADOPTION_SHA:
        raise RepeatBlocked("BLOCKED__NEW_C9_BUDGET_SOURCE_IDENTITY")
    proposal=json.loads((repo/BUDGET_PROPOSAL).read_text(encoding="utf-8"))
    maps=(proposal["proposed_c9_per_category_attempt_ceiling"],
          proposal["proposed_c9_per_province_attempt_ceiling"],
          proposal["proposed_c9_plus_future_c10_cumulative_ceiling"],
          proposal["full_old_turn_charge_project_lifetime_governance_ceiling_if_new_grant_adopted_not_calls"])
    if (maps!=(CEILINGS,PER_PROVINCE,TWO_TURN_CEILINGS,PROJECT_LIFETIME_GOVERNANCE) or
        proposal.get("adopted") is not False or
        proposal.get("old_execution",{}).get("attempt_consumed") is not True or
        proposal.get("old_execution",{}).get("old_namespace_reset") is not False or
        proposal.get("C10_authorized") is not False or
        proposal.get("retries_allowed")!=0 or
        proposal.get("proposed_new_execution_id")!=NEW_EXECUTION_ID or
        proposal.get("proposed_new_budget_namespace")!=NEW_BUDGET_NAMESPACE or
        proposal.get("old_execution",{}).get("terminal")!="CALL_LEDGER_UNRESOLVED"):
        raise RepeatBlocked("BLOCKED__NEW_C9_BUDGET_MAP_IDENTITY")
    return proposal


def preflight(repo: Path = REPOSITORY) -> dict[str,Any]:
    repo=repo.resolve()
    protected=protected_manifest_checks(repo)
    if not all(protected.values()):raise RepeatBlocked("BLOCKED__PROTECTED_MANIFEST_IDENTITY",protected)
    budget=budget_binding(repo)
    checks={"root":git(repo,"rev-parse","--show-toplevel").replace("\\","/").casefold()==repo.as_posix().casefold(),
            "src_tree":git(repo,"rev-parse","HEAD:src")==SRC_TREE,
            "src_worktree_clean":not git(repo,"status","--porcelain=v1","--","src"),
            "old_runner":sha(repo/"validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py")==OLD_RUNNER_SHA,
            "distance":sha(repo/DISTANCE)==DISTANCE_SHA,
            "helper_hashes":all(sha(repo/name)==digest for name,digest in HELPER_SHA.items()),
            "new_output_absent":not os.path.lexists(repo/OUTPUT) and path_components_safe(repo/OUTPUT),
             "full_prior_manifest":sha(repo/OLD_ROOT/"execution_artifact_manifest.json")==MANIFEST_SHA,
             "accepted_repeat_runner":sha(repo/REPEAT_RUNNER)==REPEAT_RUNNER_SHA,
             "accepted_turn7_runner":sha(repo/TURN7_RUNNER)==TURN7_RUNNER_SHA,
             "accepted_turn8_runner":sha(repo/TURN8_RUNNER)==TURN8_RUNNER_SHA,
             "owner_adoption":sha(repo/ADOPTION)==ADOPTION_SHA,
             "accepted_proposal":sha(repo/PROPOSAL)==PROPOSAL_SHA,
             "new_budget_owner_adoption":sha(repo/BUDGET_ADOPTION)==BUDGET_ADOPTION_SHA,
             "new_budget_proposal":sha(repo/BUDGET_PROPOSAL)==BUDGET_PROPOSAL_SHA,
             "old_failure_unresolved":sha(repo/OLD_FAILED_OUTPUT/"timing_failure.json")==OLD_FAILURE_SHA,
             "old_governance_lifetime":budget["full_old_turn_charge_project_lifetime_governance_ceiling_if_new_grant_adopted_not_calls"]==PROJECT_LIFETIME_GOVERNANCE}
    if not all(checks.values()):raise RepeatBlocked("BLOCKED__STATIC_PREFLIGHT",checks)
    prior=prior_output_binding(repo)
    c8=load_bundle(repo,9)
    return {"status":"BLOCKED__NEW_LIVE_AUTHORITY_ABSENT__PREPARATION_ONLY","checks":checks,
            "C8_entering":c8["hashes"],"prior_C7_to_C8":prior["prior_terminal"],
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
        self.old_governance=dict(OLD_GOVERNANCE_CHARGE)
        self.lifetime_governance=dict(PROJECT_LIFETIME_GOVERNANCE)
        self.prior={k:int((prior or {}).get(k,0)) for k in ceilings}
        self.attempted={k:0 for k in ceilings};self.per_province={};self.denied=[]
        self.province_baseline={}
        self.reserved_exposure={}
    def begin_province(self,province:int,ledger:Mapping[str,Any],envelope:Mapping[str,int])->None:
        if province in self.province_baseline or not 0<=province<31:
            raise RepeatBlocked("BLOCKED__PROVINCE_ENTRY_STATE",province)
        self.province_baseline[province]={key:int(ledger.get(key,0)) for key in PER_PROVINCE}
        self.reserved_exposure[province]=dict(envelope)
    def reconcile_province(self,province:int,ledger:Mapping[str,Any])->None:
        if province not in self.province_baseline:
            raise RepeatBlocked("CALL_LEDGER_UNRESOLVED",{"province":province,"reason":"missing_baseline"})
        row=self.per_province.setdefault(province,{})
        baseline=self.province_baseline[province]
        for key,limit in PER_PROVINCE.items():
            actual=int(ledger[key])-baseline[key]
            if actual<0:
                raise RepeatBlocked("CALL_LEDGER_UNRESOLVED",{"province":province,"category":key})
            # Repeated map returns report cumulative source totals. Never add
            # the same source counts twice or erase a pre-entry attempt.
            row[key]=max(row.get(key,0),actual)
            if row[key]>limit:
                self.denied.append({"category":key,"actual":row[key],"province":province})
                raise RepeatBlocked("BLOCKED__PROVINCE_BUDGET",self.denied[-1])
    def reserve(self,amounts:Mapping[str,int],province:int|None=None)->None:
        for key,n in amounts.items():
            if (key not in self.ceilings or not isinstance(n,int) or n<0 or
                self.attempted[key]+n>self.ceilings[key] or
                self.prior[key]+self.attempted[key]+n>self.combined[key] or
                self.old_governance[key]+self.prior[key]+self.attempted[key]+n>
                    self.lifetime_governance[key]):
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
    def reconcile(self,ledger:Mapping[str,Any],province:int|None=None)->None:
        keys=("source_native_initializations","scalar_labor_roots_attempted","scalar_labor_roots_returned",
              "corrected_policy_maps","selector_evaluations","scalar_selector_root_invocations",
              "d2_q_assemblies","direct_hjb_updates","hjb_checkpoint_evaluations_after_update",
              "scc_decompositions","restricted_dense_scipy_linalg_svd_gesvd",
              "normalized_stationary_candidates","q_transpose_times_p","corrected_aggregate_evaluations")
        for key in keys:
            n=int(ledger[key])
            if (n>self.ceilings[key] or self.prior[key]+n>self.combined[key] or
                self.old_governance[key]+self.prior[key]+n>self.lifetime_governance[key]):
                raise RepeatBlocked("BLOCKED__CONSUMED_CALL_BUDGET",{"category":key,"actual":n})
            # A guarded attempt can fail before the source records its local
            # count; never erase that already consumed entry on reconciliation.
            self.attempted[key]=max(self.attempted[key],n)
        if province is not None:
            self.reconcile_province(province,ledger)
    def reconcile_all(self,ledger:Mapping[str,Any])->None:
        for key,ceiling in self.ceilings.items():
            if key not in ledger:continue
            n=int(ledger[key])
            if (n<0 or n>ceiling or self.prior[key]+n>self.combined[key] or
                self.old_governance[key]+self.prior[key]+n>self.lifetime_governance[key]):
                raise RepeatBlocked("BLOCKED__CONSUMED_CALL_BUDGET",{"category":key,"actual":n})
            self.attempted[key]=max(self.attempted[key],n)

BASE_BUDGET_GUARD=BudgetGuard

def _arrays(bundle:Mapping[str,Any],turn:int)->dict[str,np.ndarray]:
    rows=bundle["rows"]
    out={k:np.asarray([r["state"][k] for r in rows],dtype=np.float64)
         for k in FIELDS if k not in ("raw_ra0","S")}
    out["raw_ra0"]=np.asarray([r[f"raw_ra0_turn{turn-1}"] for r in rows],dtype=np.float64)
    out["S"]=np.asarray(bundle["S"],dtype=np.float64)
    return out

def compare_carrier(ref:Mapping[str,Any],new:Mapping[str,Any])->dict[str,Any]:
    """Compare complete C8 and C9 checkpoints under the Owner-adopted law."""
    a=_arrays(ref,9);b=_arrays(new,10);rows={}
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
            "prospective_C8_start_first_comparison":True,"consecutive_new_passes":1 if passed else 0}

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

def turn9_terminal(carrier:Mapping[str,Any])->str:
    if carrier["classification"]=="UNAVAILABLE":
        raise RepeatBlocked("FAIL__OUTER_COMPARISON_UNAVAILABLE",carrier)
    return ("VALID__C9_NINE_COMPONENT_LEVEL_MET" if
            carrier["all_nine_strictly_below_level"] else
            "VALID__C9_NINE_COMPONENT_LEVEL_NOT_MET")


def source_snapshot(repo:Path)->dict[str,str]:
    tracked_src=[Path(name) for name in git(repo,"ls-files","src/ch5_two_asset_hank").splitlines()]
    paths=[*(OLD_ROOT/name for name in SEALED),DISTANCE,Path("TASK_CURRENT.md"),FUTURE_TASK_RELATIVE,
        Path("validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py"),
        REPEAT_RUNNER,Path("validators/multi_province/k1b_turn7_outer_r2/run.py"),
        Path("validators/multi_province/k1b_turn8_outer_r2/run.py"),
        Path("validators/multi_province/k1b_turn9_post_failure_new_attempt_outer_r2/run.py"),
        Path("validators/multi_province/k1b_turn9_post_failure_new_attempt_timed/run.py"),
        Path("tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_CONTRACT.json"),
        Path("docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_RUNNER_INDEPENDENT_REVIEW.md"),
        Path("docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION_OWNER_ADOPTION.md"),
        Path("docs/CH5_K1B_C9_SINGLE_TURN_TIMED_RISK_EXCEPTION_OWNER_SELECTION_20260926.md"),
        Path("docs/CH5_K1B_C9_C10_CALL_CEILINGS_OWNER_ADOPTION_20260925.md"),
        BUDGET_PROPOSAL,BUDGET_ADOPTION,OLD_FAILED_OUTPUT/"timing_failure.json",
        OLD_FAILED_OUTPUT/"partial_artifact_manifest.json",
        ADOPTION,PROPOSAL,
         OLD_ROOT/"execution_artifact_manifest.json",OLD_ROOT/"turn9_entering_bundle_manifest.json",
         OLD_ROOT/"comparison_receipt.json",OLD_ROOT/"terminal_receipt.json",
        *(Path(name) for name in HELPER_SHA),*tracked_src]
    return {p.as_posix():sha(repo/p) for p in paths}

def future_gate(repo:Path,execution_id:str|None)->None:
    if not all(protected_manifest_checks(repo).values()):
        raise RepeatBlocked("BLOCKED__PROTECTED_MANIFEST_IDENTITY")
    if os.path.lexists(repo/OUTPUT) or not path_components_safe(repo/OUTPUT):
        raise RepeatBlocked("BLOCKED__FUTURE_EVIDENCE_PATH_EXISTS_OR_UNSAFE")
    if execution_id!=NEW_EXECUTION_ID:
        raise RepeatBlocked("BLOCKED__NEW_C9_EXECUTION_ID")
    if not (repo/TIMED_CONTRACT).is_file():
        raise RepeatBlocked("BLOCKED__NEW_LIVE_CONTRACT_ABSENT")
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

def assert_active_authority(repo:Path,execution_id:str)->dict[str,Any]:
    """Recheck the committed one-shot authority on every delegate route."""
    if not all(protected_manifest_checks(repo).values()):
        raise RepeatBlocked("BLOCKED__PROTECTED_MANIFEST_IDENTITY")
    if os.path.lexists(repo/OUTPUT) or not path_components_safe(repo/OUTPUT):
        raise RepeatBlocked("BLOCKED__FUTURE_EVIDENCE_PATH_EXISTS_OR_UNSAFE")
    if execution_id!=NEW_EXECUTION_ID or not (repo/TIMED_CONTRACT).is_file():
        raise RepeatBlocked("BLOCKED__NEW_LIVE_AUTHORITY_ABSENT")
    contract=json.loads((repo/TIMED_CONTRACT).read_text(encoding="utf-8"))
    if contract.get("active") is not True or contract.get("resource_wall_seconds") is None:
        raise RepeatBlocked("BLOCKED__INACTIVE_CONTRACT")
    wrapper=repo/TIMED_WRAPPER_RELATIVE
    relative=TIMED_WRAPPER_RELATIVE.as_posix()
    if (git(repo,"status","--porcelain=v1","--",relative) or
        git(repo,"hash-object",f"--path={relative}",relative)!=
            git(repo,"rev-parse",f"HEAD:{relative}")):
        raise RepeatBlocked("BLOCKED__C9_WRAPPER_AUTHORITY_NOT_COMMITTED")
    spec=importlib.util.spec_from_file_location("c9_authority_recheck",wrapper)
    if spec is None or spec.loader is None:
        raise RepeatBlocked("BLOCKED__C9_WRAPPER_AUTHORITY_LOAD")
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    delegate=SimpleNamespace(CEILINGS=CEILINGS,PER_PROVINCE=PER_PROVINCE,
                             TWO_TURN_CEILINGS=TWO_TURN_CEILINGS,
                             path_components_safe=path_components_safe)
    return module.future_gate(repo,execution_id,delegate)


def _execute_after_gate(repo:Path,execution_id:str,runtime:dict[str,Any])->str:
    authority=assert_active_authority(repo,execution_id)
    if (runtime.get("c9_wrapper_contract_sha256")!=authority["contract_sha256"] or
        runtime.get("c9_wrapper_execution_id")!=execution_id):
        raise RepeatBlocked("BLOCKED__C9_WRAPPER_ACTIVE_GATE_REQUIRED")
    if id(runtime) not in _active_timed_runtime_ids:
        raise RepeatBlocked("BLOCKED__C9_TIMED_WRAPPER_RUNTIME_REQUIRED")
    measured=runtime.get("c9_timed_guard")
    resource_check=getattr(type(measured),"resource_check",None)
    wrapper_path=repo/"validators/multi_province/k1b_turn9_post_failure_new_attempt_timed/run.py"
    if (BudgetGuard is BASE_BUDGET_GUARD or type(measured) is not BudgetGuard or
        not issubclass(BudgetGuard,BASE_BUDGET_GUARD) or
        getattr(getattr(resource_check,"__code__",None),"co_filename",None)!=str(wrapper_path) or
        getattr(getattr(resource_check,"__code__",None),"co_qualname",None)!=
            "run_timed_action.<locals>.instrumented_action.<locals>.MeasuredGuard.resource_check"):
        raise RepeatBlocked("BLOCKED__C9_TIMED_WRAPPER_GUARD_REQUIRED")
    output=repo/OUTPUT
    pre=preflight(repo)
    prior=prior_output_binding(repo)
    before=source_snapshot(repo)
    entering=load_bundle(repo,9)
    guard=measured
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
    ledger=old.new_ledger(9)
    runtime["ledger"]=ledger
    ledger.update(terminal_kfe_attempts=0,full_integrations=0,turn8_household_calls=0,
                  turn9_household_calls=0,turn10_household_calls=0,
                  relaxation_helper_invocations=0,alpha_candidates=0)
    def map_hook(*args:Any,**kwargs:Any):
        local=args[6];budget=args[5];prior=dict(local);province=state["province"]
        guard.enter("corrected_policy_maps",province)
        guard.reserve({"selector_evaluations":800},province)
        try:
            result=originals[0](*args,**kwargs)
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
                guard.reconcile(ledger,province)
            except BaseException as exc:
                state["ledger_unresolved"]=True
                state["original_terminal"]=getattr(original_failure,"terminal",type(original_failure).__name__)
                raise RepeatBlocked("CALL_LEDGER_UNRESOLVED",{"stage":"map","cause":str(exc),
                    "original_terminal":state["original_terminal"]}) from exc
            raise
        projected=dict(ledger)
        projected["selector_evaluations"]+=int(local["selector_evaluations"])-int(prior["selector_evaluations"])
        projected["scalar_selector_root_invocations"]+=int(local["scalar_root_invocations"])-int(prior["scalar_root_invocations"])
        guard.reconcile_province(province,projected)
        return result
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
        base.ENTERING_STATE_RELATIVE=OLD_ROOT/"turn9_k1b_input_candidate.json"
        bind_future_task(base)
        task_hashes=base._task_hashes(repo)
        core_hashes=base._scientific_code_hashes(repo)
        native_grid=base.oracle.MatlabFaithfulHJBGrid(np.linspace(-2,5,20),np.linspace(0,10,20),
            np.array([0.8,1.3]),np.array([[-1/3,1/3],[1/3,-1/3]]))
        grid=CorrectedDiagnosticGrid(native_grid.b,native_grid.a,native_grid.z)
        params=base.oracle.EconomicParams(0.05,2.0,5.0,0.1,2.0,1e-6,0.0,0.0)
        results=[]
        guard.enter("turn9_household_calls")
        ledger["turn9_household_calls"]+=1
        for i,province in enumerate(canonical_order(repo)):
            state["province"]=i
            # Reserve the *maximum* bounded child envelope before entry. The
            # frozen source's province-local selector/root ceilings constrain
            # every nested invocation. Actual counts are reconciled on return
            # and on the first exceptional exit.
            envelope={"source_native_initializations":1,"scalar_labor_roots_attempted":800,
                "scalar_labor_roots_returned":800,"corrected_policy_maps":51,
                "d2_q_assemblies":51,"selector_evaluations":40800,
                "scalar_selector_root_invocations":20000000,"direct_hjb_updates":50,
                "hjb_checkpoint_evaluations_after_update":50,
                "relaxation_helper_invocations":50,"alpha_candidates":2650,
                "terminal_kfe_attempts":1,"scc_decompositions":1,
                "restricted_dense_scipy_linalg_svd_gesvd":1,
                "normalized_stationary_candidates":1,"q_transpose_times_p":1,
                "corrected_aggregate_evaluations":1}
            guard.begin_province(i,ledger,envelope)
            guard.reserve(envelope,i)
            runtime["inflight_province"]=i
            runtime["inflight_reserved_envelope"]=dict(envelope)
            runtime["province_science_entered"]=False
            try:
                guard_output_mutation(output,runtime,output/"turn9")
                runtime["scientific_started"]=True
                runtime["province_science_entered"]=True
                result=base._solve_province(repo,output/"turn9",i,province,
                    entering["states"][i],grid,native_grid,params,
                    task_hashes,core_hashes,ledger)
            except BaseException as solve_failure:
                if runtime["province_science_entered"]:
                    mark_interrupted_province(runtime,solve_failure)
                else:
                    state["original_terminal"]=getattr(solve_failure,"terminal",type(solve_failure).__name__)
                raise
            else:
                # Direct/root/KFE counts mutate the shared ledger on attempts;
                # exceptional map exits were recovered by map_hook.
                guard.reconcile(ledger,i)
                runtime["inflight_province"]=None
                runtime["inflight_reserved_envelope"]=None
                runtime["province_science_entered"]=False
            results.append(result)
        if len(results)!=31:raise RepeatBlocked("FAIL__HOUSEHOLD_BATCH_INCOMPLETE")
        integration_envelope={"household_batch_constructions":1,"full_integrations":1,
            "source_faithful_labor_reconstructions":1,"frozen_k1b_quantity_allocations":1,
            "k1b_feedback_calls":1,"c1_residual_govinv_constructions":1,
            "firm_evaluations":31,"composite_wage_batches":1,"monetary_assignments":1,
            "fiscal_diagnostic_batches":1,"completed_raw_ra0_vectors":1,
            "deterministic_next_k1b_preparations":1,"raw_next_payoff_same_s_constructions":1}
        guard.reserve(integration_envelope)
        guard_output_mutation(output,runtime,output/"turn9")
        guard.enter("household_batch_constructions")
        ledger["household_batch_constructions"]+=1
        rows=[{"province_index":i,"province":row["province"],"checkpoint":row["checkpoint"],
               "B":row["B"],"D":row["D"],"backward_error_max":row["backward_error_max"]}
              for i,row in enumerate(results)]
        write_output_json(output,runtime,output/"turn9/household_batch_receipt.json",
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
            integration=old.integrate_turn(repo,output,output/"turn9",9,entering["states"],
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
        write_output_json(output,runtime,output/"turn9_scientific_ledger.json",ledger)
        old.seal_generated_bundle(output,integration,10)
        replay=load_bundle(repo,10,OUTPUT)
        reference=load_bundle(repo,9)
        comparison={"prior_C7_to_C8":prior["prior_carrier"],
                    "current_C8_to_C9":compare_carrier(reference,replay),
                    "clipped_ra_upper":{"C8":clipped_ra_upper_summary(reference),
                                        "C9":clipped_ra_upper_summary(replay)},
                    "C10_started":False,"prospective_window_starts_at_C8":True}
        if source_snapshot(repo)!=before or prior_output_binding(repo)["checks"]!=prior["checks"]:
            raise RepeatBlocked("BLOCKED__POST_EXECUTION_SOURCE_OR_INPUT_HASH_CHANGED")
        write_output_json(output,runtime,output/"comparison_receipt.json",comparison)
        state["terminal"]=turn9_terminal(comparison["current_C8_to_C9"])
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
                "per_province_attempted":guard.per_province,
                "reserved_exposure":runtime.get("inflight_reserved_envelope"),
                "call_ledger_resolved":not state["ledger_unresolved"],
                "turn7_household_calls":ledger["turn7_household_calls"],
                "turn8_household_calls":ledger["turn8_household_calls"],
                "turn9_household_calls":ledger["turn9_household_calls"],
                "turn10_household_calls":ledger["turn10_household_calls"],
                "prior_C8_start_attempted":guard.prior,
                "combined_attempted":{k:guard.prior[k]+guard.attempted[k] for k in guard.attempted}})
        except BaseException:
            if not pending_failure:raise

def mark_interrupted_province(runtime:dict[str,Any],failure:BaseException)->None:
    """Keep confirmed counts and exposure separate after an in-flight failure."""
    state=runtime["state"]
    guard=runtime["guard"]
    province=runtime.get("inflight_province")
    original=state.get("original_terminal") or getattr(failure,"terminal",type(failure).__name__)
    state["original_terminal"]=original
    state["ledger_unresolved"]=True
    try:
        guard.reconcile(runtime["ledger"],province)
    except BaseException as reconcile_failure:
        runtime["reconciliation_failure"]=getattr(reconcile_failure,"terminal",type(reconcile_failure).__name__)
    runtime["confirmed_attempted_at_interruption"]=dict(guard.attempted)
    runtime["per_province_at_interruption"]={key:dict(value) for key,value in guard.per_province.items()}
    runtime["reserved_exposure_at_interruption"]=dict(runtime.get("inflight_reserved_envelope") or {})
    if hasattr(guard,"journal"):
        try:
            guard.journal("province_interrupted_unresolved",{
                "province":province,"original_terminal":original,
                "reserved_exposure":runtime["reserved_exposure_at_interruption"],
                "confirmed_attempted":runtime["confirmed_attempted_at_interruption"],
                "retry_allowed":False})
        except BaseException:
            state["ledger_unresolved"]=True

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
            "confirmed_attempted_at_interruption":runtime.get("confirmed_attempted_at_interruption"),
            "per_province_attempted":({key:dict(value) for key,value in guard.per_province.items()}
                                       if guard is not None else None),
            "reserved_exposure_at_interruption":runtime.get("reserved_exposure_at_interruption"),
            "inflight_province":runtime.get("inflight_province"),
            "retry_allowed":False,
            "prior_C8_start_attempted":dict(guard.prior) if guard is not None else None,
            "combined_attempted":({k:guard.prior[k]+guard.attempted[k]
                                   for k in guard.attempted} if guard is not None else None),
            "call_ledger_resolved":not unresolved,
            "old_execution_id":"C9_TIMED_RISK_RUN001",
            "old_actual_ledger":"CALL_LEDGER_UNRESOLVED",
            "old_governance_charge_not_calls":dict(OLD_GOVERNANCE_CHARGE),
            "project_lifetime_governance_ceiling_not_calls":dict(PROJECT_LIFETIME_GOVERNANCE)}

def run_after_valid_gate(repo:Path,execution_id:str,action:Any)->str:
    """Protect a future authorized action; tests pass only inert stubs."""
    assert_active_authority(repo,execution_id)
    code=getattr(action,"__code__",None)
    if (getattr(code,"co_filename",None)!=str(repo/TIMED_WRAPPER_RELATIVE) or
        getattr(code,"co_qualname",None)!="run_timed_action.<locals>.invoke"):
        raise RepeatBlocked("BLOCKED__C9_TIMED_WRAPPER_ACTION_REQUIRED")
    output=repo/OUTPUT
    if os.path.lexists(output) or not path_components_safe(output):
        raise RepeatBlocked("BLOCKED__FUTURE_EVIDENCE_PATH_EXISTS_OR_UNSAFE")
    prior_path=list(sys.path)
    prior_trace=sys.gettrace()
    prior_modules=set(sys.modules)
    runtime:dict[str,Any]={"guard":None,"ledger":None,"state":None,"scientific_started":False,
                           "output_identity":None}
    _active_timed_runtime_ids.add(id(runtime))
    try:
        return action(runtime)
    except BaseException as exc:
        state=runtime["state"] or {}
        original=state.get("original_terminal") or getattr(exc,"terminal",type(exc).__name__)
        detail=failure_detail(runtime,original,execution_id)
        if runtime["output_identity"] is None and not runtime["scientific_started"]:
            raise
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
        _active_timed_runtime_ids.discard(id(runtime))
        sys.path[:]=prior_path
        sys.settrace(prior_trace)
        for name in set(sys.modules)-prior_modules:
            if name=="ch5_two_asset_hank" or name.startswith("ch5_two_asset_hank.") or name in ("validators","validators.multi_province") or name.startswith("validators.multi_province."):
                sys.modules.pop(name,None)

def execute_once(repo:Path,execution_id:str|None)->str:
    """No direct science entry: the separately reviewed timed wrapper owns the gate."""
    raise RepeatBlocked("BLOCKED__C9_WRAPPER_REQUIRED")


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
