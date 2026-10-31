"""R7 explicit one-shot route; no default index, shell or scientific execution."""
from __future__ import annotations
import argparse,hashlib,json,os,stat,sys,time
from datetime import datetime,timezone
from pathlib import Path
from types import MappingProxyType
TASK="CH5_TEMP31_R6_R3_R2_R7_RELEASED_MEMORY_TWO_GIB_NATIVE_20261031"
GOV="4f42ea162178647473b2730749d6c3c4f816a051"
SCIENCE="56447829ce0e6c3c85552c53c351b26a2452a4bd"
OWNER="2026-10-31__MEMORY_RELEASED_BY_OWNER__NEW_SINGLE_HOST_PREFLIGHT_AND_IF_PASS_ONE_2GIB_NATIVE_MATLAB_PROBE__NOT_MAIN2"
W=Path(os.path.abspath(__file__)).parents[2]
L=W/"tasks"/TASK/"LOCAL_ONLY"
CONTROLLER=W/"validators/multi_province/temp31_r6_r3_r2_r7_released_memory_two_gib_native_controller_isolated.py"
PROBE=W/"validators/multi_province/temp31_r6_r3_r2_r7_released_memory_two_gib_minimal_probe_isolated.m"
FIXED=dict(task_id=TASK,governance_commit=GOV,contract_commit=GOV,contract_path="tasks/"+TASK+"/CONTRACT.md",contract_blob="0f57e68432a2b3a33eed72bca088448a9551ff40",contract_bytes=17149,contract_sha256="6644b31493c118b035663d63afa44b8c8a745e8525c306a1ada417b0930e0aba",scientific_parent=SCIENCE,owner_authorization=OWNER,controller_sha256="8774b39ff86136fd0a0b6757598054485155610548ad4188e1814b44e92638d7",controller_bytes=28742,probe_sha256="cf9ee6d7e371e2a82dcde0f867304ba6903b621fe1b1e01543b6d6b772a7ae72",probe_bytes=1822,reference_r3="29ec5f7466da1ec951f491650fc27ca3f59ce02b",reference_r6="7af91f7923c8161953d11e2f6daf870c33c19be7",reference_r6_review="d9380912094fee0f08a98c78453a93502610c892",memory_limit=2147483648,native_seconds=120,active_processes=1,run_mode="ONE_MINIMAL_PROBE_ONLY")
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
    if set(candidate)!=set(expected):raise ValueError("MISSING_OR_EXTRA_IDENTITY_FIELD")
    for key,value in expected.items():
        if type(candidate[key]) is not type(value) or candidate[key]!=value:raise ValueError("EXACT_IDENTITY_MISMATCH_"+key)
    for key,value in FIXED.items():
        if type(candidate[key]) is not type(value) or candidate[key]!=value:raise ValueError("FIXED_IDENTITY_MISMATCH_"+key)
    if candidate["executable_sha256"]!="4d251e680b8409d76d0524a1eb716de3c9e747386d3101e10f6ce1405ad1a59d":raise ValueError("EXECUTABLE_FIXED_IDENTITY")
    if not candidate["run_token"].startswith("TEMP31_R7_") or len(candidate["run_token"])!=42:raise ValueError("NEW_PRIVATE_NONCE")
    return True
def main():
    global _CALLED
    if _CALLED:raise RuntimeError("ENTRY_REPLAY")
    _CALLED=True
    safe(L)
    dump(L/"entry_invocation_claim.json",dict(started=stamp(),maximum=1,retries=0))
    parser=argparse.ArgumentParser(allow_abbrev=False)
    for key,value in FIXED.items():parser.add_argument("--"+key.replace("_","-"),required=True,type=type(value))
    for key,kind in DYNAMIC.items():parser.add_argument("--"+key.replace("_","-"),required=True,type=kind)
    started=stamp();called=False;error=None;rc=1
    try:
        args=vars(parser.parse_args())
        expected=json.loads(safe(L/"explicit_cli_expected_raw.json").read_bytes())
        exact(args,expected)
        negative=[]
        for label,mutate in (("MISSING_TARGET_IDENTITY",lambda v:v.pop("contract_blob")),("R40_TASK_REPLACEMENT",lambda v:v.update(task_id="R40")),("WRONG_COMMIT_AND_BLOB",lambda v:v.update(contract_commit="0"*40,contract_blob="f"*40))):
            trial=dict(args);mutate(trial)
            try:exact(trial,expected)
            except ValueError as exc:negative.append(dict(case=label,rejected=True,error=str(exc),side_effects=0))
            else:raise ValueError("NEGATIVE_ROUTE_NOT_REJECTED")
        dump(L/"route_negative_controls_raw.json",dict(same_process=True,cases=negative,model_calls=0,job_creations=0))
        raw_entry=safe(Path(__file__)).read_bytes()
        assert ident(raw_entry)["sha256"]==args["entry_sha256"] and len(raw_entry)==args["entry_bytes"],"ENTRY_IDENTITY"
        contract=safe(L/"contract_fixed_utf8.txt").read_bytes()
        assert ident(contract)==dict(bytes=args["contract_bytes"],sha256=args["contract_sha256"],git_blob=args["contract_blob"]),"CONTRACT_BYTES"
        gate_raw=safe(L/"source_gates_checked.json").read_bytes()
        assert ident(gate_raw)["sha256"]==args["source_gate_sha256"],"SOURCE_GATE_HASH"
        gate=json.loads(gate_raw)
        assert gate["status"]=="PASS" and gate["governance"]==GOV and gate["candidate_absent"] is True and gate["scientific_parent"]==SCIENCE
        for source in gate["sources"]:
            raw=safe(L/(source["role"]+"_fixed_utf8.txt")).read_bytes()
            assert ident(raw)=={key:source[key] for key in ("bytes","sha256","git_blob")},"FIXED_REFERENCE_BYTES"
        head=json.loads(json.loads(safe(L/"pre_execution_head_raw.json").read_bytes())["structuredContent"]["content"])
        candidate=json.loads(json.loads(safe(L/"pre_execution_candidate_raw.json").read_bytes())["structuredContent"]["content"])
        assert head["object"]["sha"]==GOV and candidate==[],"PRE_EXECUTION_REMOTE_GATES"
        cb=safe(CONTROLLER).read_bytes();pb=safe(PROBE).read_bytes()
        assert len(cb)==args["controller_bytes"] and ident(cb)["sha256"]==args["controller_sha256"],"CONTROLLER_FIXED_SOURCE"
        assert len(pb)==args["probe_bytes"] and ident(pb)["sha256"]==args["probe_sha256"],"PROBE_FIXED_SOURCE"
        eb=safe(Path(args["matlab_executable"])).read_bytes()
        assert len(eb)==args["executable_bytes"] and ident(eb)["sha256"]==args["executable_sha256"],"EXECUTABLE_IDENTITY"
        nonce=json.loads(safe(L/"run_token_raw.json").read_bytes())["run_token"]
        assert nonce==args["run_token"],"RUN_NONCE"
        pre=dict(task_id=TASK,at=stamp(),negative_cases_rejected=3,source_route_gate="PASS_BEFORE_CONTROLLER",controller_identity=ident(cb),probe_identity=ident(pb),entry_identity=ident(raw_entry),contract_identity=ident(contract),source_gate_identity=ident(gate_raw),explicit_r40_invocations=0,shell_invocations=0,default_route_reads=0)
        dump(L/"explicit_route_pre_execution_gate_raw.json",pre)
        plan=MappingProxyType(dict(task_id=TASK,governance_commit=GOV,scientific_parent=SCIENCE,authority_pass=True,source_route_gate_pass=True,owner_authorization=OWNER,run_token=nonce,memory_limit=2147483648,native_seconds=120,active_processes=1,controller_identity=ident(cb),probe_identity=ident(pb),executable_identity=ident(eb),matlab_executable=args["matlab_executable"]))
        namespace={"__name__":"R7_verified_native_controller","__file__":str(CONTROLLER)}
        exec(compile(cb,str(CONTROLLER),"exec"),namespace)
        called=True
        rc=namespace["run_once"](plan)
    except BaseException as exc:
        error=dict(type=type(exc).__name__,private_message=str(exc))
        rc=1
        print(json.dumps(dict(terminal="STOP__R6_R3_R2_R7_SOURCE_PRIVACY_OR_DELIVERY_BLOCKED",entry_error_type=type(exc).__name__,controller_called=called)),flush=True)
    finally:
        dump(L/"explicit_entry_execution_receipt_raw.json",dict(task_id=TASK,started=started,finished=stamp(),exit_code=rc,controller_function_called=called,entry_invocations=1,retries=0,error=error))
    return rc
if __name__=="__main__":raise SystemExit(main())
