"""R11: exact three authorized receipt fields and at most two read-only exe identities."""
from __future__ import annotations
import argparse,ctypes,hashlib,json,msvcrt,os,re,stat,sys
from ctypes import wintypes as w
from datetime import datetime,timezone
from pathlib import Path
TASK="CH5_TEMP31_R6_R3_R2_R11_EXE_LOCATOR_READONLY_AUDIT_20261031"
GOV="83eb289a1d0c3923b841e3a4b4a3fed3cdcd988f"
BASE="56447829ce0e6c3c85552c53c351b26a2452a4bd"
OWNER="2026-10-31__NEW_SEPARATE_READONLY_R8_VS_R10_EXACT_EXECUTABLE_LOCATOR_AND_FILE_IDENTITY_AUDIT__ZERO_MATLAB_PROCESS__NO_ALTERNATE_EXECUTION"
W=Path(os.path.abspath(__file__)).parents[2]
L=W/"tasks"/TASK/"LOCAL_ONLY"
ALLOWED={
"R8_LOCATOR":"tasks/CH5_TEMP31_R6_R3_R2_R8_SHORT_PROBE_2GIB_20261031/LOCAL_ONLY/executable_configuration_raw.json",
"R8_ARGV0":"tasks/CH5_TEMP31_R6_R3_R2_R8_SHORT_PROBE_2GIB_20261031/LOCAL_ONLY/actual_argv.json",
"R10_LOCATOR":"tasks/CH5_TEMP31_R6_R3_R2_R10_FIXED_INPUT_NATIVE_OPERATOR_PARITY_20261031/LOCAL_ONLY/executable_identity_failure_raw.json"}
H8=dict(bytes=235648,sha256="4d251e680b8409d76d0524a1eb716de3c9e747386d3101e10f6ce1405ad1a59d",git_blob="5a86b6a05b04b64e64272a30dba725eeee12bfee")
H10=dict(bytes=327408,sha256="79ab79050fd8d79e0b57632efb3a600e682af08ab9c32947d1c5d942e5af7059",git_blob="5a5fff0ed12140d9497a1a6f00b7f91763dd2dd1")
budget=dict(old_receipts_opened=0,old_receipt_bytes=0,target_files_opened=0,target_bytes_read=0,target_hash_passes=0,explicit_Windows_file_id_queries=0,drive_type_queries=0,retries=0)
receipts=[];targets=[];events=[];drives={};seen_canonical={};seen_ids={}
k=None;_CALLED=False
class ReceiptBlocked(RuntimeError):pass
class TargetBlocked(RuntimeError):pass
class INFO(ctypes.Structure):
    _fields_=[("dwFileAttributes",w.DWORD),("ftCreationTime",w.FILETIME),("ftLastAccessTime",w.FILETIME),("ftLastWriteTime",w.FILETIME),("dwVolumeSerialNumber",w.DWORD),("nFileSizeHigh",w.DWORD),("nFileSizeLow",w.DWORD),("nNumberOfLinks",w.DWORD),("nFileIndexHigh",w.DWORD),("nFileIndexLow",w.DWORD)]
def ident(raw):return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),git_blob=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest())
def dump(path,data):
    with path.open("x",encoding="utf-8",newline="\n") as f:json.dump(data,f,indent=2,allow_nan=False);f.write("\n")
def event(stage,**data):events.append(dict(stage=stage,**data))
def signature(st):return dict(size=st.st_size,device=st.st_dev,inode=st.st_ino,mtime_ns=st.st_mtime_ns,ctime_ns=st.st_ctime_ns,attributes=getattr(st,"st_file_attributes",0))
def safe(path):
    path=Path(os.path.abspath(path))
    for p in reversed([path,*path.parents]):
        st=os.lstat(p)
        if stat.S_ISLNK(st.st_mode) or getattr(st,"st_file_attributes",0)&0x400:raise TargetBlocked("REPARSE_PATH")
    return path
def read_authorized_receipt(role):
    if role not in ALLOWED:raise ReceiptBlocked("UNAUTHORIZED_RECEIPT_ROLE")
    path=W/ALLOWED[role]
    rec=dict(role=role,authorized_relative_path=ALLOWED[role],fields_present=False,opened=False,bytes_read=0)
    receipts.append(rec)
    try:
        safe(path);before=os.lstat(path)
        if not stat.S_ISREG(before.st_mode) or not 0<before.st_size<=131072:raise ReceiptBlocked("RECEIPT_TYPE_OR_SIZE")
        assert budget["old_receipts_opened"]<3,"RECEIPT_OPEN_BUDGET"
        with path.open("rb",buffering=0) as f:
            rec["opened"]=True;budget["old_receipts_opened"]+=1
            raw=f.read(131072);rec["bytes_read"]=len(raw);budget["old_receipt_bytes"]+=len(raw)
            opened=os.fstat(f.fileno())
        after=os.lstat(path)
        if signature(before)!=signature(opened) or signature(before)!=signature(after) or len(raw)!=before.st_size:raise ReceiptBlocked("RECEIPT_READ_RACE")
        obj=json.loads(raw.decode("utf-8"))
        rec.update(raw_receipt_identity=ident(raw),read_only=True,stat_stable=True,raw_JSON_copied=False)
        if role=="R8_LOCATOR":
            extracted=dict(locator=obj["matlab_executable"],historical_identity=obj["executable_identity"])
            fields=["matlab_executable","executable_identity"]
            if extracted["historical_identity"]!=H8:raise ReceiptBlocked("R8_PRIVATE_PUBLIC_IDENTITY_CONFLICT")
        elif role=="R8_ARGV0":
            argv=obj["argv"]
            if type(argv) is not list or not argv:raise ReceiptBlocked("R8_ARGV0_MISSING")
            extracted=dict(locator=argv[0]);fields=["argv[0]"];del argv
        else:
            extracted=dict(locator=obj["selected_executable"],historical_identity=obj["selected_actual_identity"])
            fields=["selected_executable","selected_actual_identity"]
            if extracted["historical_identity"]!=H10:raise ReceiptBlocked("R10_PRIVATE_PUBLIC_IDENTITY_CONFLICT")
        del obj,raw
        if type(extracted["locator"]) is not str or not extracted["locator"]:raise ReceiptBlocked("EXACT_LOCATOR_MISSING")
        rec.update(fields_present=True,extracted_field_names=fields,extracted=extracted)
        event("authorized_receipt_field_extracted",role=role,fields=fields)
        return extracted
    except BaseException as exc:
        rec["error_type"]=type(exc).__name__
        if isinstance(exc,ReceiptBlocked):raise
        raise ReceiptBlocked("AUTHORIZED_RECEIPT_MISSING_UNREADABLE_OR_FIELD_MISSING_"+role) from exc
def setup_readonly_api():
    global k
    assert os.name=="nt" and ctypes.sizeof(ctypes.c_void_p)==8 and ctypes.sizeof(INFO)==52,"WINDOWS_ABI"
    k=ctypes.WinDLL("kernel32",use_last_error=True)
    k.GetFileInformationByHandle.argtypes=[w.HANDLE,ctypes.POINTER(INFO)];k.GetFileInformationByHandle.restype=w.BOOL
    k.GetDriveTypeW.argtypes=[w.LPCWSTR];k.GetDriveTypeW.restype=w.UINT
def canonical_local(locator):
    if type(locator) is not str or not os.path.isabs(locator):raise TargetBlocked("NOT_ABSOLUTE")
    drive,tail=os.path.splitdrive(locator)
    if not re.fullmatch(r"[A-Za-z]:",drive) or ":" in tail or any(c in locator for c in ("*", "?",chr(0),chr(10),chr(13),'"')):raise TargetBlocked("NOT_PLAIN_LOCAL_PATH")
    root=drive+os.sep
    if root.casefold() not in drives:
        dtype=int(k.GetDriveTypeW(root));budget["drive_type_queries"]+=1;drives[root.casefold()]=dtype
        if dtype!=3:raise TargetBlocked("NOT_FIXED_LOCAL_DRIVE")
    if drives[root.casefold()]!=3:raise TargetBlocked("REMOTE_OR_UNSUPPORTED_DRIVE")
    path=safe(Path(os.path.abspath(os.path.normpath(locator))))
    st=os.lstat(path)
    if not stat.S_ISREG(st.st_mode) or path.suffix.casefold()!=".exe":raise TargetBlocked("NOT_REGULAR_EXECUTABLE_FILE")
    canonical=os.path.normcase(os.path.realpath(path))
    if os.path.splitdrive(canonical)[0].startswith(chr(92)*2):raise TargetBlocked("REMOTE_CANONICAL_PATH")
    return path,canonical
def read_target(role,path,canonical,history):
    if canonical in seen_canonical:
        rec=dict(seen_canonical[canonical]);rec.update(role=role,canonical_alias_reused=True,historical_identity=history,history_matches_current=rec["identity"]==history,opened=False,bytes_read=0,hash_passes=0,handle_closed=True)
        targets.append(rec);return rec
    before=os.lstat(path);size=before.st_size
    if not 0<=size<=1048576 or budget["target_bytes_read"]+size>2097152:raise TargetBlocked("TARGET_READ_SIZE_BUDGET")
    rec=dict(role=role,locator=str(path),canonical=canonical,historical_identity=history,opened=False,bytes_read=0,hash_passes=0,handle_closed=False)
    targets.append(rec)
    f=None
    try:
        if budget["target_files_opened"]>=2:raise TargetBlocked("TARGET_OPEN_BUDGET")
        with path.open("rb",buffering=0) as f:
            budget["target_files_opened"]+=1;rec["opened"]=True
            pre=os.fstat(f.fileno())
            if signature(pre)!=signature(before):raise TargetBlocked("PATH_TO_HANDLE_RACE")
            if budget["explicit_Windows_file_id_queries"]>=2:raise TargetBlocked("FILE_ID_QUERY_BUDGET")
            budget["explicit_Windows_file_id_queries"]+=1
            info=INFO();ctypes.set_last_error(0)
            if not k.GetFileInformationByHandle(msvcrt.get_osfhandle(f.fileno()),ctypes.byref(info)):raise OSError(ctypes.get_last_error(),"READONLY_FILE_ID_QUERY")
            fid=(int(info.dwVolumeSerialNumber),(int(info.nFileIndexHigh)<<32)|int(info.nFileIndexLow))
            if int(pre.st_ino)!=fid[1] or ((int(info.nFileSizeHigh)<<32)|int(info.nFileSizeLow))!=size:raise TargetBlocked("STAT_WINDOWS_FILE_ID_CONFLICT")
            rec["Windows_file_id_private"]=list(fid)
            if fid in seen_ids:
                previous=seen_ids[fid]
                if signature(pre)!=previous["post_fstat_private"]:raise TargetBlocked("SAME_ID_CHANGED_SINCE_PRIOR_HASH")
                actual=previous["identity"];rec["same_OS_file_id_hash_reused"]=True
            else:
                sha=hashlib.sha256();blob=hashlib.sha1(b"blob "+str(size).encode()+b"\0")
                remaining=size;budget["target_hash_passes"]+=1;rec["hash_passes"]=1
                while remaining:
                    chunk=f.read(min(65536,remaining))
                    if not chunk:raise TargetBlocked("UNEXPECTED_EOF")
                    sha.update(chunk);blob.update(chunk);remaining-=len(chunk)
                    rec["bytes_read"]+=len(chunk);budget["target_bytes_read"]+=len(chunk)
                    if rec["bytes_read"]>1048576 or budget["target_bytes_read"]>2097152:raise TargetBlocked("READ_BUDGET_EXCEEDED")
                actual=dict(bytes=rec["bytes_read"],sha256=sha.hexdigest(),git_blob=blob.hexdigest())
            post=os.fstat(f.fileno());path_after=os.lstat(path)
            if signature(pre)!=signature(post) or signature(pre)!=signature(path_after) or int(post.st_ino)!=fid[1]:raise TargetBlocked("TARGET_POST_READ_RACE")
            safe(path)
            rec.update(identity=actual,history_matches_current=actual==history,pre_fstat_private=signature(pre),post_fstat_private=signature(post),path_stat_and_file_id_stable=True,regular=True,no_reparse=True,local_fixed_drive=True,read_only=True)
        rec["handle_closed"]=f.closed
        seen_canonical[canonical]=rec;seen_ids[fid]=rec
        event("target_identity_read",role=role,bytes_read=rec["bytes_read"],hash_passes=rec["hash_passes"],history_matches_current=rec["history_matches_current"])
        return rec
    finally:
        if f is not None:rec["handle_closed"]=f.closed
def main():
    global _CALLED
    if _CALLED:raise RuntimeError("AUDIT_REPLAY")
    _CALLED=True;safe(L)
    dump(L/"audit_invocation_claim.json",dict(task_id=TASK,invocations=1,retries=0,UTC_date=datetime.now(timezone.utc).date().isoformat()))
    parser=argparse.ArgumentParser(allow_abbrev=False)
    for key in ("task_id","governance","contract_blob","scientific_parent","owner","script_sha256","source_gate_sha256","run_mode"):parser.add_argument("--"+key.replace("_","-"),required=True)
    parser.add_argument("--contract-bytes",type=int,required=True)
    phase="SOURCE_AUTHORITY";terminal="STOP__R11_SOURCE_PRIVACY_OR_DELIVERY_BLOCKED";grade="NOT_COMPLETED";error=None;summary={}
    try:
        a=vars(parser.parse_args());plan=json.loads((L/"audit_execution_plan_frozen_raw.json").read_bytes())
        if a!=plan:raise RuntimeError("EXPLICIT_PLAN_MISMATCH")
        assert a["task_id"]==TASK and a["governance"]==GOV and a["contract_blob"]=="7c31a4261bac18ebb315a0c8faf1e4ee668d74e3" and a["contract_bytes"]==16060 and a["scientific_parent"]==BASE and a["owner"]==OWNER and a["run_mode"]=="READONLY_EXACT_THREE_RECEIPTS_TWO_TARGETS"
        assert ident(Path(__file__).read_bytes())["sha256"]==a["script_sha256"]
        contract=(L/"contract_fixed_utf8.txt").read_bytes()
        assert ident(contract)["git_blob"]==a["contract_blob"] and len(contract)==a["contract_bytes"]
        gr=(L/"source_gates_checked.json").read_bytes();assert ident(gr)["sha256"]==a["source_gate_sha256"]
        gate=json.loads(gr);assert gate["status"]=="PASS" and gate["governance"]==GOV and gate["candidate_absent"] is True
        for s in gate["sources"]:assert ident((L/(s["role"]+"_fixed_utf8.txt")).read_bytes())=={key:s[key] for key in ("bytes","sha256","git_blob")}
        head=json.loads(json.loads((L/"pre_execution_head_raw.json").read_bytes())["structuredContent"]["content"])
        absent=json.loads(json.loads((L/"pre_execution_candidate_raw.json").read_bytes())["structuredContent"]["content"])
        assert head["object"]["sha"]==GOV and absent==[]
        assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
        phase="EXACT_PRIVATE_RECEIPT_FIELDS";terminal="STOP__R11_PRIVATE_RECEIPT_LOCATOR_UNAVAILABLE_OR_CONFLICT"
        r8=read_authorized_receipt("R8_LOCATOR");argv=read_authorized_receipt("R8_ARGV0");r10=read_authorized_receipt("R10_LOCATOR")
        phase="EXACT_LOCAL_TARGET_PATH_SAFETY";terminal="STOP__R11_TARGET_IDENTITY_OR_READONLY_SCOPE_BLOCKED"
        setup_readonly_api()
        p8,c8=canonical_local(r8["locator"]);pa,ca=canonical_local(argv["locator"])
        if c8!=ca:raise ReceiptBlocked("R8_ARGV0_AND_CONFIGURATION_CANONICAL_LOCATOR_CONFLICT")
        p10,c10=canonical_local(r10["locator"])
        dump(L/"receipt_field_extraction_private.json",dict(receipts=receipts,R8_argv_matches_configuration_canonical=True,raw_R8_locator_equals_argv0=r8["locator"]==argv["locator"],raw_JSON_copied=False))
        phase="EXACT_TARGET_READONLY_IDENTITIES";terminal="STOP__R11_TARGET_IDENTITY_OR_READONLY_SCOPE_BLOCKED"
        t8=read_target("R8_SUCCESS_TARGET",p8,c8,H8);t10=read_target("R10_SELECTED_TARGET",p10,c10,H10)
        same_id=t8["Windows_file_id_private"]==t10["Windows_file_id_private"]
        matched=t8["history_matches_current"] and t10["history_matches_current"]
        grade="PASS_BOUNDED_TWO_EXACT_LOCATORS_AND_FILE_IDENTITIES" if matched else "PASS_BOUNDED_LOCATOR_AUDIT_WITH_HISTORIC_CURRENT_DIVERGENCE"
        summary=dict(grade=grade,UTC_date=datetime.now(timezone.utc).date().isoformat(),R8_argv0_matches_configuration_canonical_path=True,R8_argv0_and_locator_bound_to_same_Windows_file_id=True,R8_binding_grade="SAME_CANONICAL_LOCATOR_TIED_TO_ONE_READONLY_HANDLE_FILE_ID; not independent historical-process file-ID capture",R8_R10_same_canonical_path=c8==c10,R8_R10_same_Windows_file_id=same_id,R8_R10_same_recorded_locator=r8["locator"]==r10["locator"],R8_R10_same_content=t8["identity"]==t10["identity"],targets=[dict(role=t["role"],historical_identity=t["historical_identity"],current_identity=t["identity"],current_matches_historical=t["history_matches_current"],file_stable=t["path_stat_and_file_id_stable"],read_only=t["read_only"],regular=t["regular"],no_reparse=t["no_reparse"],local_fixed_drive=t["local_fixed_drive"],bytes_read=t["bytes_read"],hash_passes=t["hash_passes"]) for t in (t8,t10)],budget=budget.copy(),locators_from_exact_authorized_fields=True,all_opened_handles_closed=all(t["handle_closed"] for t in targets),causal_limit="does not establish launcher/shim function, installation health or a startup permission; no executable launched")
        dump(L/"audit_public_summary_raw.json",summary)
        terminal="STOP__AWAITING_GPT_INDEPENDENT_ABC"
    except BaseException as exc:
        if isinstance(exc,ReceiptBlocked):terminal="STOP__R11_PRIVATE_RECEIPT_LOCATOR_UNAVAILABLE_OR_CONFLICT"
        error=dict(type=type(exc).__name__,private_message=str(exc),phase=phase)
    finally:
        dump(L/"audit_execution_receipt_raw.json",dict(task_id=TASK,terminal=terminal,grade=grade,phase=phase,error=error,receipts=receipts,targets=targets,events=events,budget=budget,summary=summary,MATLAB_processes=0,Jobs=0,prefdirs=0,memory_samples=0,scientific_calls=0,retries=0))
        print(json.dumps(dict(terminal=terminal,grade=grade,error_type=error["type"] if error else None,phase=phase,budget=budget,same_canonical_path=summary.get("R8_R10_same_canonical_path"),same_file_id=summary.get("R8_R10_same_Windows_file_id"),targets=summary.get("targets",[]),MATLAB_processes=0,Jobs=0,scientific_calls=0)),flush=True)
    return 0 if error is None and terminal=="STOP__AWAITING_GPT_INDEPENDENT_ABC" else 1
if __name__=="__main__":raise SystemExit(main())
