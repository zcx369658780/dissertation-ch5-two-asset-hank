"""Explicit R8 route: one in-process fixed controller, no default launcher."""
from __future__ import annotations
import argparse,hashlib,json,os,stat,sys,time
from datetime import datetime,timezone
from pathlib import Path
from types import MappingProxyType
TASK="CH5_TEMP31_R6_R3_R2_R8_SHORT_PROBE_2GIB_20261031"
GOV="d8bac7b4e83f8b9fe2069f751d5482e38f59de12"
SCIENCE="56447829ce0e6c3c85552c53c351b26a2452a4bd"
OWNER="2026-10-31__NEW_INDEPENDENT_R2022B_SHORT_M_PROBE_FILENAME_STATIC_HARD_GATE__IF_PASS_ONE_2GIB_120S_NATIVE_MINIMAL_PROBE__NO_MAIN2"
W=Path(os.path.abspath(__file__)).parents[2]
L=W/"tasks"/TASK/"LOCAL_ONLY"
CONTROLLER=W/"validators/multi_province/temp31_r8_native_controller_isolated.py"
PROBE=W/"validators/multi_province/temp31_r8_probe.m"
FIXED=dict(task_id=TASK,governance_commit=GOV,contract_commit=GOV,contract_path="tasks/"+TASK+"/CONTRACT.md",contract_blob="773786f094a33d19b2d34a3a48180dc94c6b6b12",contract_bytes=19802,contract_sha256="7ae1c5fcc41f7e9f7e723bc001b92baa8d0fee8165924f5e923a8632ea2eb18c",scientific_parent=SCIENCE,owner_authorization=OWNER,controller_sha256="77e40b93b1ebe5a2c18f21b0362d020d735519734c4a9df5785f8f0d726d6146",controller_bytes=33588,probe_sha256="a1c6554a792233888e3860caf957be608548011dd852af6e7e570e9465fee3c3",probe_bytes=1790,reference_r7="e3b35471eeb346df2172e0511e9f34b8ab13b8cf",reference_r7_review="6539dcfc03b0fd593e92a9ad894e5072ada3b449",reference_r3="29ec5f7466da1ec951f491650fc27ca3f59ce02b",memory_limit=2147483648,native_seconds=120,active_processes=1,run_mode="ONE_MINIMAL_PROBE_ONLY")
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
        if type(candidate[key]) is not type(value) or candidate[key]!=value:raise ValueError("EXACT_IDENTITY_"+key)
    for key,value in FIXED.items():
        if type(candidate[key]) is not type(value) or candidate[key]!=value:raise ValueError("FIXED_IDENTITY_"+key)
    if candidate["executable_sha256"]!="4d251e680b8409d76d0524a1eb716de3c9e747386d3101e10f6ce1405ad1a59d":raise ValueError("EXECUTABLE_FIXED_IDENTITY")
    if not candidate["run_token"].startswith("TEMP31_R8_") or len(candidate["run_token"])!=42:raise ValueError("NEW_PRIVATE_NONCE")
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
    began=stamp();called=False;error=None;rc=1
    try:
        assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode,"ISOLATED_PYTHON_FLAGS"
        names=sys.argv[1::2]
        assert len(sys.argv[1:])%2==0 and len(names)==len(set(names)),"DUPLICATE_OR_MALFORMED_OPTIONS"
        args=vars(parser.parse_args())
        expected=json.loads(safe(L/"explicit_cli_expected_raw.json").read_bytes())
        exact(args,expected)
        negative=[]
        for label,mutate in (("MISSING_CONTRACT_BLOB",lambda v:v.pop("contract_blob")),("R40_TASK_REPLACEMENT",lambda v:v.update(task_id="R40")),("WRONG_COMMIT_AND_BLOB",lambda v:v.update(contract_commit="0"*40,contract_blob="f"*40))):
            trial=dict(args);mutate(trial)
            try:exact(trial,expected)
            except ValueError as exc:negative.append(dict(case=label,rejected=True,error=str(exc),side_effects=0))
            else:raise ValueError("NEGATIVE_ROUTE_NOT_REJECTED")
        dump(L/"route_negative_controls_raw.json",dict(same_process=True,cases=negative,job_creations=0,model_calls=0))
        selfraw=safe(Path(__file__)).read_bytes()
        assert ident(selfraw)["sha256"]==args["entry_sha256"] and len(selfraw)==args["entry_bytes"],"ENTRY_IDENTITY"
        contract=safe(L/"contract_fixed_utf8.txt").read_bytes()
        assert ident(contract)==dict(bytes=args["contract_bytes"],sha256=args["contract_sha256"],git_blob=args["contract_blob"]),"CONTRACT_BYTES"
        gr=safe(L/"source_gates_checked.json").read_bytes()
        assert ident(gr)["sha256"]==args["source_gate_sha256"],"SOURCE_GATE_HASH"
        gate=json.loads(gr)
        assert gate["status"]=="PASS" and gate["governance"]==GOV and gate["candidate_absent"] is True and gate["scientific_parent"]==SCIENCE
        for source in gate["sources"]:
            data=safe(L/(source["role"]+"_fixed_utf8.txt")).read_bytes()
            assert ident(data)=={key:source[key] for key in ("bytes","sha256","git_blob")},"FIXED_REFERENCE_BYTES"
        head=json.loads(json.loads(safe(L/"pre_execution_head_raw.json").read_bytes())["structuredContent"]["content"])
        candidate=json.loads(json.loads(safe(L/"pre_execution_candidate_raw.json").read_bytes())["structuredContent"]["content"])
        assert head["object"]["sha"]==GOV and candidate==[],"PRE_EXECUTION_REMOTE_GATES"
        cb=safe(CONTROLLER).read_bytes();pb=safe(PROBE).read_bytes()
        assert len(cb)==args["controller_bytes"] and ident(cb)["sha256"]==args["controller_sha256"],"CONTROLLER_FIXED_SOURCE"
        assert len(pb)==args["probe_bytes"] and ident(pb)["sha256"]==args["probe_sha256"],"PROBE_FIXED_SOURCE"
        eb=safe(Path(args["matlab_executable"])).read_bytes()
        assert len(eb)==args["executable_bytes"] and ident(eb)["sha256"]==args["executable_sha256"],"EXECUTABLE_FIXED_SOURCE"
        nonce=json.loads(safe(L/"run_token_raw.json").read_bytes())["run_token"]
        assert nonce==args["run_token"],"RUN_NONCE"
        dump(L/"explicit_route_pre_execution_gate_raw.json",dict(task_id=TASK,at=stamp(),negative_cases_rejected=3,source_route_gate="PASS_BEFORE_CONTROLLER",controller_identity=ident(cb),probe_identity=ident(pb),entry_identity=ident(selfraw),contract_identity=ident(contract),source_gate_identity=ident(gr),default_router_reads=0,r40_invocations=0,shell_invocations=0,second_python_dispatches=0))
        plan=MappingProxyType(dict(task_id=TASK,governance_commit=GOV,scientific_parent=SCIENCE,authority_pass=True,source_route_gate_pass=True,owner_authorization=OWNER,run_token=nonce,memory_limit=2147483648,native_seconds=120,active_processes=1,controller_identity=ident(cb),probe_identity=ident(pb),executable_identity=ident(eb),matlab_executable=args["matlab_executable"]))
        namespace={"__name__":"R8_verified_native_controller","__file__":str(CONTROLLER)}
        exec(compile(cb,str(CONTROLLER),"exec"),namespace)
        called=True
        rc=namespace["run_once"](plan)
    except BaseException as exc:
        error=dict(type=type(exc).__name__,private_message=str(exc));rc=1
        print(json.dumps(dict(terminal="STOP__R6_R3_R2_R8_SOURCE_PRIVACY_OR_DELIVERY_BLOCKED",entry_error_type=type(exc).__name__,controller_called=called)),flush=True)
    finally:
        dump(L/"explicit_entry_execution_receipt_raw.json",dict(task_id=TASK,started=began,finished=stamp(),exit_code=rc,controller_function_called=called,entry_invocations=1,retries=0,error=error))
    return rc
if __name__=="__main__":raise SystemExit(main())
