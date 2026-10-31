"""R9 explicit route; one in-process scientific helper and one owned MATLAB run."""
from __future__ import annotations
import argparse,hashlib,json,os,stat,sys,time
from datetime import datetime,timezone
from pathlib import Path
from types import MappingProxyType
TASK="CH5_TEMP31_R6_R3_R2_R9_FIXED_SMALL_OPERATOR_PARITY_20261031"
GOV="6d9aabb0a212d9dfbc6a78512fab0265c32baa43"
SCIENCE="56447829ce0e6c3c85552c53c351b26a2452a4bd"
OWNER="2026-10-31__ONE_TASK_SYNTHETIC_SOURCE_ANCHORED_MATLAB_PYTHON_SPARSE_OPERATOR_ASSEMBLY_ELEMENTWISE_PARITY__ZERO_HA_HJB_KFE_SOLVE__ZERO_MAIN2"
W=Path(os.path.abspath(__file__)).parents[2]
L=W/"tasks"/TASK/"LOCAL_ONLY"
CP=W/"validators/multi_province/temp31_r9_native_controller_isolated.py"
MP=W/"validators/multi_province/t31_r9_op.m"
HP=W/"validators/multi_province/temp31_r9_fixture_and_compare_isolated.py"
FIXED=dict(task_id=TASK,governance_commit=GOV,contract_commit=GOV,contract_path="tasks/"+TASK+"/CONTRACT.md",contract_blob="ba0a332e8c42bea76912d3c11ec2a9cddb608740",contract_bytes=22131,contract_sha256="62b97a7de3ca8025be117961a0e78ec1eeceb073442f915f089064cabf7cd9fd",scientific_parent=SCIENCE,owner_authorization=OWNER,controller_sha256="f41c94b2a30299e636a3a4daad13ed2ea1e31d0f9d6ddb3af7ce2f854f07a362",controller_bytes=34165,probe_sha256="66aa2f4779ca5abe73cec8c7fec883b336863c0f7b230a98ba6dfb3cb76a9598",probe_bytes=4252,helper_sha256="1dbcbb182c9dd8d9546bdf9799a23f5cd98e813590b54ec900b0607e516cfbc0",helper_bytes=16885,matlab_source_blob="0e38270154ab8953290ae3ef6c92f95d38230afb",python_source_blob="9a511e151c9bf449412dc5605dfa1a2076711277",indexing_source_blob="3aee864af5dce5128957896e5d7803c2a815aab6",reference_r8="09d26fe51e2ff1442c232949f89008c7ca6f42ce",memory_limit=2147483648,native_seconds=120,active_processes=1,run_mode="TWO_FIXED_SYNTHETIC_SOURCE_ASSEMBLIES_ONLY")
DYNAMIC=dict(entry_sha256=str,entry_bytes=int,source_gate_sha256=str,executable_sha256=str,executable_bytes=int,matlab_executable=str,run_token=str)
_CALLED=False
def stamp():return dict(monotonic_ns=time.monotonic_ns(),utc=datetime.now(timezone.utc).isoformat())
def ident(raw):return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),git_blob=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest())
def dump(p,data):
    with p.open("x",encoding="utf-8",newline="\n") as f:json.dump(data,f,indent=2,allow_nan=False);f.write("\n")
def safe(p):
    p=Path(os.path.abspath(p))
    for q in reversed([p,*p.parents]):
        st=os.lstat(q)
        if stat.S_ISLNK(st.st_mode) or getattr(st,"st_file_attributes",0)&0x400:raise ValueError("REPARSE_PATH")
    return p
def exact(candidate,expected):
    if set(candidate)!=set(expected):raise ValueError("MISSING_OR_EXTRA_IDENTITY")
    for key,value in expected.items():
        if type(candidate[key]) is not type(value) or candidate[key]!=value:raise ValueError("EXACT_IDENTITY_"+key)
    for key,value in FIXED.items():
        if type(candidate[key]) is not type(value) or candidate[key]!=value:raise ValueError("FIXED_IDENTITY_"+key)
    if candidate["executable_sha256"]!="4d251e680b8409d76d0524a1eb716de3c9e747386d3101e10f6ce1405ad1a59d":raise ValueError("EXECUTABLE_FIXED_IDENTITY")
    if not candidate["run_token"].startswith("TEMP31_R9_") or len(candidate["run_token"])!=42:raise ValueError("NEW_PRIVATE_NONCE")
def main():
    global _CALLED
    if _CALLED:raise RuntimeError("ENTRY_REPLAY")
    _CALLED=True;safe(L)
    dump(L/"entry_invocation_claim.json",dict(started=stamp(),maximum=1,retries=0))
    parser=argparse.ArgumentParser(allow_abbrev=False)
    for key,value in FIXED.items():parser.add_argument("--"+key.replace("_","-"),required=True,type=type(value))
    for key,kind in DYNAMIC.items():parser.add_argument("--"+key.replace("_","-"),required=True,type=kind)
    began=stamp();called=False;prepared=False;compared=False;error=None;rc=1;phase="ROUTE_SOURCE";terminal="STOP__R9_SOURCE_PRIVACY_OR_DELIVERY_BLOCKED"
    try:
        assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode,"ISOLATED_FLAGS"
        names=sys.argv[1::2];assert len(sys.argv[1:])%2==0 and len(names)==len(set(names)),"DUPLICATE_OPTIONS"
        args=vars(parser.parse_args());expected=json.loads(safe(L/"explicit_cli_expected_raw.json").read_bytes());exact(args,expected)
        negative=[]
        for label,mutate in (("MISSING_CONTRACT_BLOB",lambda v:v.pop("contract_blob")),("R40_TASK_REPLACEMENT",lambda v:v.update(task_id="R40")),("WRONG_COMMIT_AND_BLOB",lambda v:v.update(contract_commit="0"*40,contract_blob="f"*40))):
            trial=dict(args);mutate(trial)
            try:exact(trial,expected)
            except ValueError as exc:negative.append(dict(case=label,rejected=True,error=str(exc),side_effects=0))
            else:raise ValueError("NEGATIVE_ROUTE_ACCEPTED")
        dump(L/"route_negative_controls_raw.json",dict(same_process=True,cases=negative,Job_creations=0,MATLAB_creations=0))
        selfraw=safe(Path(__file__)).read_bytes();assert ident(selfraw)["sha256"]==args["entry_sha256"] and len(selfraw)==args["entry_bytes"]
        contract=safe(L/"contract_fixed_utf8.txt").read_bytes();assert ident(contract)==dict(bytes=args["contract_bytes"],sha256=args["contract_sha256"],git_blob=args["contract_blob"])
        gr=safe(L/"source_gates_checked.json").read_bytes();assert ident(gr)["sha256"]==args["source_gate_sha256"]
        gate=json.loads(gr);assert gate["status"]=="PASS" and gate["governance"]==GOV and gate["candidate_absent"] is True and gate["scientific_parent"]==SCIENCE
        for rec in gate["sources"]:
            raw=safe(L/(rec["role"]+"_fixed_utf8.txt")).read_bytes()
            assert ident(raw)=={k:rec[k] for k in ("bytes","sha256","git_blob")},"FIXED_REF_SNAPSHOT"
        head=json.loads(json.loads(safe(L/"pre_execution_head_raw.json").read_bytes())["structuredContent"]["content"])
        absent=json.loads(json.loads(safe(L/"pre_execution_candidate_raw.json").read_bytes())["structuredContent"]["content"])
        assert head["object"]["sha"]==GOV and absent==[]
        cb=safe(CP).read_bytes();mb=safe(MP).read_bytes();hb=safe(HP).read_bytes()
        for raw,key in ((cb,"controller"),(mb,"probe"),(hb,"helper")):assert len(raw)==args[key+"_bytes"] and ident(raw)["sha256"]==args[key+"_sha256"],"NEW_SOURCE_IDENTITY"
        eb=safe(Path(args["matlab_executable"])).read_bytes();assert ident(eb)["sha256"]==args["executable_sha256"] and len(eb)==args["executable_bytes"]
        nonce=json.loads(safe(L/"run_token_raw.json").read_bytes())["run_token"];assert nonce==args["run_token"]
        dump(L/"explicit_route_pre_execution_gate_raw.json",dict(task_id=TASK,at=stamp(),negative_cases_rejected=3,status="PASS_BEFORE_FIXTURES_AND_NATIVE",entry_identity=ident(selfraw),controller_identity=ident(cb),runner_identity=ident(mb),helper_identity=ident(hb),contract_identity=ident(contract),source_gate_identity=ident(gr),R40_calls=0,shell_dispatches=0,second_Python_dispatches=0))
        hn={"__name__":"R9_verified_fixture_comparator","__file__":str(HP)};exec(compile(hb,str(HP),"exec"),hn)
        phase="SOURCE_FIXTURE_AND_PYTHON_ASSEMBLY";terminal="STOP__R9_OPERATOR_SOURCE_PAIR_OR_STATIC_MAPPING_BLOCKED"
        build=hn["prepare_once"]();prepared=True
        plan=MappingProxyType(dict(task_id=TASK,governance_commit=GOV,scientific_parent=SCIENCE,authority_pass=True,source_route_gate_pass=True,owner_authorization=OWNER,run_token=nonce,memory_limit=2147483648,native_seconds=120,active_processes=1,controller_identity=ident(cb),probe_identity=ident(mb),executable_identity=ident(eb),matlab_executable=args["matlab_executable"]))
        cn={"__name__":"R9_verified_native_controller","__file__":str(CP)};exec(compile(cb,str(CP),"exec"),cn)
        phase="OWNED_MATLAB_ASSEMBLY";called=True
        native_rc=cn["run_once"](plan)
        native=json.loads((L/"native_execution_receipt_raw.json").read_bytes())
        if native_rc!=0:
            terminal=native["terminal"];rc=1
        else:
            phase="ELEMENTWISE_COMPARISON";terminal="STOP__R9_SOURCE_OPERATOR_ELEMENTWISE_MISMATCH_REQUIRES_REVIEW"
            compared=True;comparison=hn["compare_once"](build)
            assert comparison["status"]=="PASS_SYNTHETIC_TWO_FIXTURES_EIGHT_MATRICES_SOURCE_ASSEMBLY_ELEMENTWISE"
            terminal="STOP__AWAITING_GPT_INDEPENDENT_ABC";rc=0
    except BaseException as exc:
        error=dict(type=type(exc).__name__,private_message=str(exc),phase=phase);rc=1
    finally:
        receipt=dict(task_id=TASK,started=began,finished=stamp(),exit_code=rc,terminal=terminal,phase=phase,entry_invocations=1,fixture_preparation_completed=prepared,controller_called=called,comparison_entered=compared,error=error,retries=0)
        dump(L/"explicit_entry_execution_receipt_raw.json",receipt)
        print(json.dumps(dict(terminal=terminal,entry_exit=rc,prepared=prepared,controller_called=called,comparison_entered=compared,error_type=error["type"] if error else None,error_phase=phase)),flush=True)
    return rc
if __name__=="__main__":raise SystemExit(main())
