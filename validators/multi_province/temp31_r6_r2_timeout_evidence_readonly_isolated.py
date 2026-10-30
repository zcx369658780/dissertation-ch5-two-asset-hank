"""R6-R2 stdlib-only exact-path offline audit. Never execute old sources."""
from __future__ import annotations
import ast
from datetime import datetime,timezone
import hashlib,json,os,re,stat,time
from pathlib import Path
TASK="CH5_TEMP31_R6_R2_NATIVE_MATLAB_TIMEOUT_EVIDENCE_AUDIT_20261030"
W=Path(os.path.abspath(__file__)).parents[2]
R=W/"tasks"/TASK
A="tasks/CH5_TEMP31_R6_MATLAB_PYTHON_POST_OPERATOR_ELEMENTWISE_PARITY_20261030"
B="tasks/CH5_TEMP31_R6_R1_MATLAB_LAUNCH_CONTROLLER_RECOVERY_20261030"
C="validators/multi_province/temp31_r6_r1_matlab_launch_controller_isolated.py"
M="validators/multi_province/temp31_r6_r1_matlab_post_recipe_isolated.m"
READ={A+"/manifest.json",A+"/result.md",C,M}
READ.update(B+"/"+n for n in ("result.md","manifest.json","matlab_native_probe_receipt.json","windows_job_pre_execution_gate.json","controller_failure_and_repair_map.md","source_identity.json","model_budget_zero.json","gap_register.md","privacy_report.md"))
seen={}
def ident(b):
    return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest())
def safe(rel):
    assert not re.match("^[A-Za-z]:|^[/\134\134]",rel) and ".." not in Path(rel).parts
    p=W/rel
    assert p.suffix.lower()!=".npz","NPZ_FORBIDDEN"
    for q in reversed([p,*p.parents]):
        st=os.lstat(q)
        assert not stat.S_ISLNK(st.st_mode) and not getattr(st,"st_file_attributes",0)&0x400,"REPARSE_FORBIDDEN"
    return p
def read(rel,semantic=False):
    if semantic:assert rel in READ,"SEMANTIC_SCOPE"
    b=safe(rel).read_bytes();seen[rel]=ident(b);return b
def text(rel):return read(rel,True).decode("utf-8")
def dump(name,value):
    with (R/name).open("x",encoding="utf-8",newline="\n") as f:json.dump(value,f,indent=2,allow_nan=False);f.write("\n")
def write(name,value):
    with (R/name).open("x",encoding="utf-8",newline="\n") as f:f.write(value)
def check(root,role):
    raw=text(root+"/manifest.json");obj=json.loads(raw);items=[]
    for e in obj["files"]:
        p=e["path"];row=dict(path=p,expected={k:e[k] for k in ("bytes","sha256","git_blob") if k in e})
        if not (p.startswith(root+"/") or p in {C,M}):
            row.update(status="MISSING_OR_OUT_OF_SCOPE",read_attempted=False,reason="outside exact original task and not one of the two explicitly named R6-R1 source paths")
        else:
            try:
                actual=ident(read(p));ok=all(actual[k]==v for k,v in row["expected"].items())
                row.update(status="VERIFIED" if ok else "MISMATCH",actual=actual,read_attempted=True,content_scope="HASH_ONLY unless separately authorized")
            except (FileNotFoundError,PermissionError) as err:
                row.update(status="MISSING_OR_INACCESSIBLE",read_attempted=True,error_type=type(err).__name__)
        items.append(row)
    counts={s:sum(e["status"]==s for e in items) for s in ("VERIFIED","MISMATCH","MISSING_OR_INACCESSIBLE","MISSING_OR_OUT_OF_SCOPE")}
    return dict(role=role,manifest_identity=seen[root+"/manifest.json"],declared=len(items),counts=counts,items=items,old_PASS_reused=False)
def fragments(src,ranges):
    lines=src.splitlines();out=[]
    for first,last in ranges:
        raw="\n".join(lines[first-1:last])+"\n"
        public=re.sub("(?i)[A-Z]:[\134\134/][^\134\042'\134r\134n]*","<PRIVATE_PATH>",raw)
        out.append(dict(first_line=first,last_line=min(last,len(lines)),raw_fragment=ident(raw.encode()),public_fragment=ident(public.encode()),transformation="absolute drive path literal replacement only",text="\n".join(str(i)+": "+s for i,s in enumerate(public.splitlines(),first))))
    return out
def main():
    start=datetime.now(timezone.utc).isoformat();tick=time.perf_counter()
    dump("audit_execution_claim.json",dict(task_id=TASK,attempt=1,started_at_utc=start,scope="exact artifact byte/hash and offline text/AST; no child launch or OS scan"))
    r6=check(A,"R6");r1=check(B,"R6-R1")
    dump("original_manifest_readback.json",dict(R6=r6,R6_R1=r1,scope_rule="same exact old task directory hash-only; external paths restricted to R6-R1 controller and MATLAB recipe",grade="CURRENT_AUDITOR_RECOMPUTED_ORIGINAL_BYTES"))
    assert not any(r["counts"]["MISMATCH"] or r["counts"]["MISSING_OR_INACCESSIBLE"] for r in (r6,r1)),"IN_SCOPE_OLD_EVIDENCE_UNAVAILABLE_OR_CHANGED"
    c=text(C);m=text(M);ast.parse(c,filename="OLD_CONTROLLER_TEXT_NOT_EXECUTED")
    receipt=json.loads(text(B+"/matlab_native_probe_receipt.json"));gate=json.loads(text(B+"/windows_job_pre_execution_gate.json"))
    for rel in (A+"/result.md",B+"/result.md"):text(rel)
    parts=fragments(c,[(10,16),(63,82),(88,128),(130,161),(163,195),(197,226)])
    mp=fragments(m,[(7,18),(54,57)])
    fence=chr(96)*3
    body="# Actual control-flow excerpts\n\nOLD_CONTROLLER_IDENTITY="+json.dumps(seen[C],sort_keys=True)+"\nOLD_RECIPE_IDENTITY="+json.dumps(seen[M],sort_keys=True)+"\n\nSelected authentic snippets with original line numbers. Old source was read/parsed only. Historical API outcomes remain executor receipts; R2 did not rerun them.\n"
    for role,rows in (("R6_R1_CONTROLLER",parts),("R6_R1_RECIPE_PERMISSION",mp)):
        for e in rows:
            body+="\n"+role+"; original lines "+str(e["first_line"])+"-"+str(e["last_line"])+"; identities "+json.dumps({k:v for k,v in e.items() if k!="text"},sort_keys=True)+"\n\n"+fence+"text\n"+e["text"]+"\n"+fence+"\n"
    write("controller_code_evidence.md",body)
    dump("evidence/code_fragment_redaction_identities.json",dict(controller=parts,recipe=mp,full_old_sources_published=False))
    def ln(x):return next(i+1 for i,s in enumerate(c.splitlines()) if x in s)
    keys={"matlab:CreateJobObjectW","matlab:SetJobLimits","matlab:CreateProcessW","matlab:AssignProcessToJobObject","matlab:QueryJobLimits","matlab:IsProcessInJob","matlab:QueryJobMembers","matlab:ResumeThread","matlab:TerminateOwnedJobOrSuspendedChild","matlab:QueryFinalMemory"}
    milestones=[dict(original_index=i,selector="events["+str(i)+"]",event=e,timestamp=None,timezone=None,clock_source="NOT_RECORDED",grade="EXECUTOR_RECEIPT_ONLY") for i,e in enumerate(receipt["events"]) if e.get("api") in keys or e.get("handle_role")=="matlab:main_thread"]
    timeline=dict(task_id=TASK,ROOT_CAUSE="UNKNOWN",receipt_identity=seen[B+"/matlab_native_probe_receipt.json"],controller_identity=seen[C],historical_wall_clock_start=None,historical_wall_clock_end=None,historical_timezone="UNKNOWN_NOT_RECORDED",per_event_timestamps="ABSENT",original_elapsed_seconds=receipt["elapsed_seconds"],original_elapsed_clock="time.monotonic duration from before config/AST/binary hash/API setup through cleanup/log hashes; underlying counter values absent",probe_deadline_seconds=30,deadline_relation="after native.start returns, after ResumeThread and thread-handle close; exact resume-to-deadline delay absent",observable_internal_MATLAB_initialization_seconds=None,events_in_recorded_order=milestones,error=receipt["error"],code_lines={k:ln(x) for k,x in {"controller_start":"started=time.monotonic()","native_start":"native.start()","deadline":"deadline=time.monotonic()+DEADLINE_SECONDS","wait_probe":'wait_file(L/"native_probe_ready.txt"',"wait_loop":"def wait_file","timeout":'raise TimeoutError("NATIVE_WALL_TIMEOUT")'}.items()},grades=dict(actual_original_bytes="DIRECT_BYTES_AND_CODE_VERIFIED",historical_APIs="EXECUTOR_RECEIPT_ONLY",algorithm="CODE_PATH_STATIC_ONLY",internal_initialization="UNKNOWN_NO_EVIDENCE",license_or_resource_cause="HYPOTHESIS_UNTESTED"))
    dump("startup_event_timeline.json",timeline)
    logs=[]
    for stream in ("stdout","stderr"):
        rel=B+"/LOCAL_ONLY/matlab_"+stream+".txt";key="matlab_"+stream
        assert rel in {e["path"] for e in r1["items"]} and key in receipt["logs"]
        actual=ident(read(rel));assert actual==receipt["logs"][key],"RAW_LOG_IDENTITY_MISMATCH"
        logs.append(dict(role=key,path=rel,actual=actual,selector="logs."+key,grade="DIRECT_BYTES_AND_CODE_VERIFIED"))
    dump("evidence/original_raw_log_identities.json",dict(logs=logs,raw_fulltext_published=False))
    dump("evidence/selected_historical_receipt_fields.json",dict(receipt_identity=seen[B+"/matlab_native_probe_receipt.json"],job_identity=seen[B+"/windows_job_pre_execution_gate.json"],gate=gate,native=receipt["native"],probe=receipt["probe"],error=receipt["error"],elapsed_seconds=receipt["elapsed_seconds"],baseline_matlab_pids=receipt["baseline_matlab_pids"],after_matlab_pids=receipt["after_matlab_pids"],owned_orphan_matlab=receipt["owned_orphan_matlab"],cleanup_errors=receipt["cleanup_errors"],events_total=len(receipt["events"]),GetExitCodeProcess_api_successes=sum(e.get("api")=="matlab:GetExitCodeProcess" and e.get("ok",False) for e in receipt["events"]),natural_exit_code_saved=False,grade="EXECUTOR_RECEIPT_ONLY_REAUTHENTICATED_BYTES"))
    changes=[]
    for rel,before in list(seen.items()):
        if ident(safe(rel).read_bytes())!=before:changes.append(rel)
    dump("evidence/original_preservation_after_audit.json",dict(files_rechecked=len(seen),changed=changes,old_writes=0))
    assert not changes,"OLD_EVIDENCE_CHANGED_DURING_AUDIT"
    dump("model_budget_zero.json",dict(task_id=TASK,audit_executor_runs=1,new_MATLAB_processes=0,MATLAB_runtime_commands=0,new_Job_experiments=0,new_OS_process_scans=0,model_calls=0,HJB=0,KFE=0,GE=0,IRF=0,policy_calls=0,sparse_solves=0,price_points=0,NPZ_reads=0,old_task_writes=0,old_source_executions=0,scientific_source_writes=0,timeout_changes=0,resource_limit_changes=0,new_repos_worktrees=0,Issue=0,PR=0,merge=0,cleanup=0,AUTO_NEXT=False))
    done=dict(task_id=TASK,completed=True,attempts=1,script=ident(Path(__file__).read_bytes()),started_at_utc=start,ended_at_utc=datetime.now(timezone.utc).isoformat(),audit_elapsed_perf_counter_seconds=time.perf_counter()-tick,historical_timestamps_invented=False,ROOT_CAUSE="UNKNOWN",native_initialization="UNKNOWN_NO_EVIDENCE",synthetic="NOT_TESTED_RECEIPT_AND_STATIC_CONTROL_FLOW",manifest_counts={r["role"]:r["counts"] for r in (r6,r1)},originals_rechecked_unchanged=len(seen),new_MATLAB=0,new_OS_scans=0,NPZ_reads=0,numeric_review="NOT_TESTED_BY_DESIGN")
    dump("audit_execution_receipt.json",done)
    print(json.dumps(done),flush=True)
if __name__=="__main__":main()
