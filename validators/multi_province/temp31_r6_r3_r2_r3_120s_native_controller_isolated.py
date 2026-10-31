"""One-shot isolated-prefdir native startup; stdlib and Win32 only."""
from __future__ import annotations
import ast,ctypes,hashlib,json,os,stat,subprocess,time
from ctypes import wintypes as w
from datetime import datetime,timezone
from pathlib import Path
TASK="CH5_TEMP31_R6_R3_R2_R3_EXPLICIT_NATIVE_120S_20261031"
W=Path(os.path.abspath(__file__)).parents[2]
R=W/"tasks"/TASK
L=R/"LOCAL_ONLY"
RT=L/"R3_NATIVE_RUNTIME"
PREF=RT/"matlab_prefdir_fresh"
TOKEN="TEMP31_R3_ee813324476a4bcebabe8fd1c223a7ec"
LIMIT=1073741824
FLAGS=0x2308
SUSPENDED=4
UNICODE_ENV=0x400
NO_WINDOW=0x08000000
ACTIVE=259
MSG={1:"END_OF_JOB_TIME",2:"END_OF_PROCESS_TIME",3:"ACTIVE_PROCESS_LIMIT",4:"ACTIVE_PROCESS_ZERO",6:"NEW_PROCESS",7:"EXIT_PROCESS",8:"ABNORMAL_EXIT_PROCESS",9:"PROCESS_MEMORY_LIMIT",10:"JOB_MEMORY_LIMIT",11:"NOTIFICATION_LIMIT"}
events=[];notifications=[];markers=[];k=None;trace=None
def stamp():return dict(monotonic_ns=time.monotonic_ns(),utc=datetime.now(timezone.utc).isoformat(),clock_pair_order="monotonic_then_UTC")
def event(name,at=None,**data):
    e=dict(event=name,**(at or stamp()),**data);events.append(e)
    if trace:trace.write(json.dumps(e,allow_nan=False)+"\n");trace.flush()
    return e
def ident(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest())
def dump(p,obj):
    with p.open("x",encoding="utf-8",newline="\n") as f:json.dump(obj,f,indent=2,allow_nan=False);f.write("\n")
def safe(p):
    p=Path(os.path.abspath(p))
    for q in reversed([p,*p.parents]):
        st=os.lstat(q)
        if stat.S_ISLNK(st.st_mode) or getattr(st,"st_file_attributes",0)&0x400:raise RuntimeError("REPARSE_PATH_REJECTED")
    return p
class IO(ctypes.Structure):
    _fields_=[(n,ctypes.c_ulonglong) for n in ("ReadOperationCount","WriteOperationCount","OtherOperationCount","ReadTransferCount","WriteTransferCount","OtherTransferCount")]
class BASIC(ctypes.Structure):
    _fields_=[("PerProcessUserTimeLimit",ctypes.c_longlong),("PerJobUserTimeLimit",ctypes.c_longlong),("LimitFlags",w.DWORD),("MinimumWorkingSetSize",ctypes.c_size_t),("MaximumWorkingSetSize",ctypes.c_size_t),("ActiveProcessLimit",w.DWORD),("Affinity",ctypes.c_size_t),("PriorityClass",w.DWORD),("SchedulingClass",w.DWORD)]
class EXT(ctypes.Structure):
    _fields_=[("BasicLimitInformation",BASIC),("IoInfo",IO),("ProcessMemoryLimit",ctypes.c_size_t),("JobMemoryLimit",ctypes.c_size_t),("PeakProcessMemoryUsed",ctypes.c_size_t),("PeakJobMemoryUsed",ctypes.c_size_t)]
class SA(ctypes.Structure):
    _fields_=[("nLength",w.DWORD),("lpSecurityDescriptor",ctypes.c_void_p),("bInheritHandle",w.BOOL)]
class SI(ctypes.Structure):
    _fields_=[("cb",w.DWORD),("lpReserved",w.LPWSTR),("lpDesktop",w.LPWSTR),("lpTitle",w.LPWSTR),("dwX",w.DWORD),("dwY",w.DWORD),("dwXSize",w.DWORD),("dwYSize",w.DWORD),("dwXCountChars",w.DWORD),("dwYCountChars",w.DWORD),("dwFillAttribute",w.DWORD),("dwFlags",w.DWORD),("wShowWindow",w.WORD),("cbReserved2",w.WORD),("lpReserved2",ctypes.POINTER(ctypes.c_ubyte)),("hStdInput",w.HANDLE),("hStdOutput",w.HANDLE),("hStdError",w.HANDLE)]
class PI(ctypes.Structure):
    _fields_=[("hProcess",w.HANDLE),("hThread",w.HANDLE),("dwProcessId",w.DWORD),("dwThreadId",w.DWORD)]
class IDS(ctypes.Structure):
    _fields_=[("NumberOfAssignedProcesses",w.DWORD),("NumberOfProcessIdsInList",w.DWORD),("ProcessIdList",ctypes.c_size_t*8)]
class PORT(ctypes.Structure):
    _fields_=[("CompletionKey",ctypes.c_void_p),("CompletionPort",w.HANDLE)]
def bind(name,args,ret):
    f=getattr(k,name);f.argtypes=args;f.restype=ret
def setup():
    global k
    assert os.name=="nt" and ctypes.sizeof(ctypes.c_void_p)==8,"WINDOWS_X64_REQUIRED"
    k=ctypes.WinDLL("kernel32",use_last_error=True)
    bind("CreateJobObjectW",[ctypes.c_void_p,w.LPCWSTR],w.HANDLE)
    bind("SetInformationJobObject",[w.HANDLE,ctypes.c_int,ctypes.c_void_p,w.DWORD],w.BOOL)
    bind("QueryInformationJobObject",[w.HANDLE,ctypes.c_int,ctypes.c_void_p,w.DWORD,ctypes.c_void_p],w.BOOL)
    bind("AssignProcessToJobObject",[w.HANDLE,w.HANDLE],w.BOOL)
    bind("IsProcessInJob",[w.HANDLE,w.HANDLE,ctypes.POINTER(w.BOOL)],w.BOOL)
    bind("CreateIoCompletionPort",[w.HANDLE,w.HANDLE,ctypes.c_size_t,w.DWORD],w.HANDLE)
    bind("GetQueuedCompletionStatus",[w.HANDLE,ctypes.POINTER(w.DWORD),ctypes.POINTER(ctypes.c_size_t),ctypes.POINTER(ctypes.c_void_p),w.DWORD],w.BOOL)
    bind("CreateProcessW",[w.LPCWSTR,w.LPWSTR,ctypes.c_void_p,ctypes.c_void_p,w.BOOL,w.DWORD,ctypes.c_void_p,w.LPCWSTR,ctypes.POINTER(SI),ctypes.POINTER(PI)],w.BOOL)
    bind("CreateFileW",[w.LPCWSTR,w.DWORD,w.DWORD,ctypes.POINTER(SA),w.DWORD,w.DWORD,w.HANDLE],w.HANDLE)
    bind("ResumeThread",[w.HANDLE],w.DWORD)
    bind("GetExitCodeProcess",[w.HANDLE,ctypes.POINTER(w.DWORD)],w.BOOL)
    bind("WaitForSingleObject",[w.HANDLE,w.DWORD],w.DWORD)
    bind("TerminateJobObject",[w.HANDLE,w.UINT],w.BOOL)
    bind("TerminateProcess",[w.HANDLE,w.UINT],w.BOOL)
    bind("CloseHandle",[w.HANDLE],w.BOOL)
    assert (ctypes.sizeof(EXT),ctypes.sizeof(SI),ctypes.sizeof(PI),ctypes.sizeof(PORT))==(144,104,24,16),"WIN32_ABI"
def checked(ok,name):
    err=0 if ok else ctypes.get_last_error();event(name,ok=bool(ok),win32_error=err)
    if not ok:raise OSError(err,name)
def close(h,role):
    if not h:return True
    ok=k.CloseHandle(h);event("CloseHandle",role=role,ok=bool(ok),win32_error=0 if ok else ctypes.get_last_error());return bool(ok)
def pref_preflight():
    safe(L)
    if os.path.lexists(RT) or os.path.lexists(PREF):raise RuntimeError("FRESH_RUNTIME_OR_PREFDIR_ALREADY_EXISTS")
    os.mkdir(RT);safe(RT)
    if os.path.lexists(PREF):raise RuntimeError("FRESH_PREFDIR_ALREADY_EXISTS")
    os.mkdir(PREF);safe(PREF)
    canonical=os.path.realpath(PREF);root=os.path.realpath(L)
    assert os.path.commonpath((canonical,root))==root and os.path.normcase(canonical)==os.path.normcase(str(PREF)),"CANONICAL_CONTAINMENT"
    assert not os.path.splitdrive(canonical)[0].startswith(chr(92)*2),"NETWORK_PATH_REJECTED"
    old_role=os.path.normcase(os.path.abspath(W/"tasks/CH5_TEMP31_R6_R1_MATLAB_LAUNCH_CONTROLLER_RECOVERY_20261030"))
    assert not os.path.normcase(canonical).startswith(old_role+os.sep),"HISTORICAL_PATH_REJECTED"
    assert not list(os.scandir(PREF)),"NEW_PREFDIR_NOT_EMPTY"
    h=k.CreateFileW(canonical,0x2,7,None,3,0x02000000,None)
    checked(h and h!=ctypes.c_void_p(-1).value,"prefdir_open_directory_FILE_ADD_FILE")
    assert close(h,"prefdir_write_permission_directory_handle"),"PREFDIR_HANDLE_CLOSE"
    safe(PREF);assert not list(os.scandir(PREF)),"NEW_PREFDIR_CHANGED_BEFORE_LAUNCH"
    rec=dict(status="PASS",role="NEW_TASK_LOCAL_ONLY_FRESH_PREFDIR",created_exclusively=True,existed_before=False,empty_after_create=True,empty_after_permission_check=True,directory_FILE_ADD_FILE_access=True,no_reparse=True,canonical_within_new_LOCAL_ONLY=True,historical_alias_excluded=True,path_bytes_sha256=hashlib.sha256(os.fsencode(canonical)).hexdigest(),child_only_override=True,old_prefdir_reads=0,old_prefdir_enumerations=0,old_prefdir_copies=0,old_prefdir_writes=0)
    dump(L/"strategy_b_prefdir_preflight.json",rec)
    event("prefdir_preflight_pass",**rec)
    return canonical
class Native:
    def __init__(self):
        self.job=None;self.port=None;self.pi=PI();self.files=[];self.created=False;self.assigned=False;self.resumed=False;self.cleaned=False;self.deadline=None
        self.record=dict(launch_attempts=0,created=False,resumed=False,forced_termination=False,handles=[],watcher_threads=0,watcher_join="NOT_APPLICABLE_NONBLOCKING_POLL",port_empty_polls=0)
    def limits(self):
        info=EXT()
        checked(k.QueryInformationJobObject(self.job,9,ctypes.byref(info),ctypes.sizeof(info),None),"QueryJobLimits")
        fl=int(info.BasicLimitInformation.LimitFlags)
        assert fl==FLAGS and not fl&(0x800|0x1000) and info.ProcessMemoryLimit==LIMIT and info.JobMemoryLimit==LIMIT and info.BasicLimitInformation.ActiveProcessLimit==1,"JOB_LIMIT_READBACK"
        return dict(flags=fl,process_commit_limit=int(info.ProcessMemoryLimit),job_commit_limit=int(info.JobMemoryLimit),active_process_limit=1,breakaway_allowed=False,kill_on_job_close=True,peak_process_commit=int(info.PeakProcessMemoryUsed),peak_job_commit=int(info.PeakJobMemoryUsed))
    def members(self):
        ids=IDS()
        checked(k.QueryInformationJobObject(self.job,3,ctypes.byref(ids),ctypes.sizeof(ids),None),"QueryJobMembers")
        return [int(ids.ProcessIdList[i]) for i in range(ids.NumberOfProcessIdsInList)]
    def drain(self,maximum=32):
        if not self.port:return
        for unused in range(maximum):
            msg=w.DWORD();key=ctypes.c_size_t();subject=ctypes.c_void_p();ctypes.set_last_error(0)
            ok=k.GetQueuedCompletionStatus(self.port,ctypes.byref(msg),ctypes.byref(key),ctypes.byref(subject),0)
            if not ok and not subject.value and ctypes.get_last_error()==258:
                self.record["port_empty_polls"]+=1;break
            checked(ok,"GetQueuedCompletionStatus_message")
            assert key.value==1,"COMPLETION_KEY_MISMATCH"
            role="NO_PROCESS_ID" if not subject.value else ("OWNED_MATLAB" if subject.value==self.pi.dwProcessId else "OTHER_JOB_REPORTED_PROCESS")
            note=event("Job_notification_received",message_id=int(msg.value),message=MSG.get(int(msg.value),"UNKNOWN_MESSAGE"),subject_role=role,occurrence_timestamp="NOT_PROVIDED_BY_API")
            notifications.append(note)
    def start(self,argv,env):
        self.job=k.CreateJobObjectW(None,None);checked(bool(self.job),"CreateJobObject")
        info=EXT();info.BasicLimitInformation.LimitFlags=FLAGS;info.BasicLimitInformation.ActiveProcessLimit=1;info.ProcessMemoryLimit=LIMIT;info.JobMemoryLimit=LIMIT
        checked(k.SetInformationJobObject(self.job,9,ctypes.byref(info),ctypes.sizeof(info)),"SetJobLimits")
        self.limits();assert self.members()==[],"JOB_NOT_EMPTY_BEFORE_PORT_ASSOCIATION"
        self.port=k.CreateIoCompletionPort(ctypes.c_void_p(-1).value,None,0,1);checked(bool(self.port),"CreateIoCompletionPort")
        port=PORT();port.CompletionKey=1;port.CompletionPort=self.port
        checked(k.SetInformationJobObject(self.job,7,ctypes.byref(port),ctypes.sizeof(port)),"associate_completion_port_before_assignment")
        assert self.members()==[],"JOB_NOT_EMPTY_AFTER_PORT_ASSOCIATION"
        sa=SA();sa.nLength=ctypes.sizeof(sa);sa.bInheritHandle=True
        for role,access,creation in (("stdin",0x80000000,3),("stdout",0x40000000,1),("stderr",0x40000000,1)):
            target="NUL" if role=="stdin" else str(RT/("native_"+role+".txt"))
            h=k.CreateFileW(target,access,3,ctypes.byref(sa),creation,0x80,None)
            checked(h and h!=ctypes.c_void_p(-1).value,"create_stdio_"+role);self.files.append(h)
        si=SI();si.cb=ctypes.sizeof(si);si.dwFlags=0x100;si.hStdInput,si.hStdOutput,si.hStdError=self.files
        line=ctypes.create_unicode_buffer(subprocess.list2cmdline(argv))
        envblock=ctypes.create_unicode_buffer("\0".join(a+"="+b for a,b in sorted(env.items(),key=lambda t:t[0].upper()))+"\0\0")
        self.record["launch_attempts"]=1;event("suspended_CreateProcess_begin",creation_flags=SUSPENDED|UNICODE_ENV|NO_WINDOW)
        ok=k.CreateProcessW(argv[0],line,None,None,True,SUSPENDED|UNICODE_ENV|NO_WINDOW,ctypes.cast(envblock,ctypes.c_void_p),str(RT),ctypes.byref(si),ctypes.byref(self.pi))
        checked(ok,"suspended_CreateProcess_return");self.created=True;self.record["created"]=True
        dump(L/"owned_process_private_identity.json",dict(pid=int(self.pi.dwProcessId),tid=int(self.pi.dwThreadId)))
        checked(k.AssignProcessToJobObject(self.job,self.pi.hProcess),"assign_job");self.assigned=True
        member=w.BOOL();checked(k.IsProcessInJob(self.pi.hProcess,self.job,ctypes.byref(member)),"IsProcessInJob")
        assert member.value and self.members()==[self.pi.dwProcessId],"JOB_MEMBER_IDENTITY"
        limits=self.limits();assert self.exitcode()==ACTIVE,"CHILD_NOT_ACTIVE_WHILE_SUSPENDED"
        self.record["pre_execution_gate"]=dict(**limits,membership=True,single_member_is_owned=True,completion_port_associated_before_assignment=True,source_route_identity_pass=True)
        dump(L/"job_gate_completion_port_receipt.json",dict(status="PASS_BEFORE_RESUME",**self.record["pre_execution_gate"]))
        self.drain()
        event("ResumeThread_begin")
        prior=k.ResumeThread(self.pi.hThread);at=stamp();self.deadline=at["monotonic_ns"]+120_000_000_000
        event("ResumeThread_return",at=at,previous_suspend_count=int(prior),ok=prior==1)
        assert prior==1,"RESUME_THREAD_COUNT"
        self.resumed=True;self.record["resumed"]=True;self.record["resume_observed"]=at
        self.record["deadline_monotonic_ns"]=self.deadline
        event("deadline_set",origin_monotonic_ns=at["monotonic_ns"],deadline_monotonic_ns=self.deadline,maximum_seconds=120)
        assert close(self.pi.hThread,"native_primary_thread"),"THREAD_HANDLE_CLOSE"
        self.pi.hThread=None
    def exitcode(self):
        code=w.DWORD()
        ok=k.GetExitCodeProcess(self.pi.hProcess,ctypes.byref(code))
        if not ok:checked(ok,"GetExitCodeProcess_API")
        return int(code.value)
    def timeout_stop(self):
        event("native_window_timeout",maximum_seconds=120)
        code=self.exitcode()
        event("deadline_process_status",exit_code=code)
        if code==ACTIVE:
            checked(k.TerminateJobObject(self.job,0xE0000001),"deadline_TerminateOwnedJob")
            self.record["forced_termination"]=True
            self.record["timeout_termination_requested"]=stamp()
        return code
    def cleanup(self):
        if self.cleaned:return
        self.cleaned=True
        try:
            if self.created:
                initial=self.exitcode();self.record["exit_code_before_cleanup"]=initial
                if initial==ACTIVE and not self.record["forced_termination"]:
                    checked(k.TerminateJobObject(self.job,0xE0000001) if self.assigned else k.TerminateProcess(self.pi.hProcess,0xE0000001),"TerminateOwnedJob_or_suspended_owned_process")
                    self.record["forced_termination"]=True
                wait=k.WaitForSingleObject(self.pi.hProcess,5000);event("WaitForSingleObject_reaping",result=int(wait),maximum_ms=5000)
                self.record["reaped_wait_result"]=int(wait);assert wait==0,"OWNED_PROCESS_REAP_FAILED"
                self.record["exit_code_after_cleanup"]=self.exitcode()
                if self.assigned:self.record["final_limits_and_memory"]=self.limits()
                self.drain(128)
        finally:
            for h,role in [(self.pi.hThread,"primary_thread"),(self.pi.hProcess,"native_process"),(self.job,"owned_job")]:
                if h:self.record["handles"].append(dict(role=role,closed=close(h,role)))
            if self.port:
                try:self.drain(128)
                finally:self.record["handles"].append(dict(role="completion_port",closed=close(self.port,"completion_port")))
            for i,h in enumerate(self.files):self.record["handles"].append(dict(role="stdio_"+str(i),closed=close(h,"stdio_"+str(i))))
        self.record["all_handles_closed"]=all(r["closed"] for r in self.record["handles"])
def read_markers(nat):
    stages=("ENTERED_MATLAB_USER_SCRIPT","PREFDIR_MATCH","PREFDIR_MISMATCH","MATLAB_VERSION","SPARSE_PROBE_PASS")
    known={m["stage"] for m in markers}
    for stage in stages:
        if stage in known:continue
        p=RT/(stage+".json")
        if not p.is_file():continue
        safe(p);raw=p.read_bytes();assert len(raw)<=32768,"MARKER_TOO_LARGE"
        data=json.loads(raw);assert data["task_id"]==TASK and data["run_token"]==TOKEN and data["stage"]==stage,"MARKER_IDENTITY"
        datetime.fromisoformat(data["utc"].replace("Z","+00:00"))
        at=stamp();entry=dict(stage=stage,MATLAB_utc=data["utc"],observed=at,seconds_after_resume=(at["monotonic_ns"]-nat.record["resume_observed"]["monotonic_ns"])/1e9,raw_identity=ident(raw))
        if stage=="ENTERED_MATLAB_USER_SCRIPT":assert not markers,"MARKER_ORDER"
        elif stage in ("PREFDIR_MATCH","PREFDIR_MISMATCH"):
            assert markers and markers[-1]["stage"]=="ENTERED_MATLAB_USER_SCRIPT","PREFDIR_MARKER_ORDER"
            actual=data["data"]["actual_prefdir"];expected=data["data"]["expected_prefdir"]
            same=os.path.normcase(os.path.abspath(os.path.normpath(actual)))==os.path.normcase(os.path.abspath(os.path.normpath(expected)))
            same=same and os.path.normcase(expected)==os.path.normcase(str(PREF))
            entry.update(PREFDIR_EQUALS_EXPECTED=bool(data["data"]["equals_expected"]) and same,actual_path_sha256=hashlib.sha256(actual.encode()).hexdigest(),expected_path_sha256=hashlib.sha256(expected.encode()).hexdigest())
            assert entry["PREFDIR_EQUALS_EXPECTED"]==(stage=="PREFDIR_MATCH"),"PREFDIR_DECLARATION_INCONSISTENT"
        elif stage=="MATLAB_VERSION":
            assert markers and markers[-1]["stage"]=="PREFDIR_MATCH"
            entry.update(version=data["data"]["version"],release=data["data"]["release"]);assert entry["release"]=="2022b","RUNTIME_RELEASE_MISMATCH"
        else:
            assert markers and markers[-1]["stage"]=="MATLAB_VERSION"
            assert data["data"]==dict(rows=1,cols=1,nnz=1,value=1),"SPARSE_PROBE_CONTENT"
            entry["sparse"]=data["data"]
        markers.append(entry);event("MATLAB_marker_observed",**entry)
        if stage=="PREFDIR_MISMATCH":return False
    return True

_CALLED=False

def run_once(sealed_plan):
    """Sole native function, called directly from the verified explicit entry."""
    global trace,_CALLED
    assert not _CALLED,"CONTROLLER_REPLAY_REJECTED"
    _CALLED=True
    native=None;phase="SOURCE_PREFLIGHT";error=None;cleanup_error=None;safety=False;timed_out=False;natural=None;pref_safe=False
    terminal="STOP__R6_R3_R2_R3_RUNTIME_ROUTE_OR_PREEXECUTION_GATE_BLOCKED"
    checkpoints=[];parent_environment=dict(os.environ)
    with (L/"controller_run_claim.json").open("x",encoding="utf-8") as f:json.dump(dict(attempt=1,maximum=1,retries=0,started=stamp()),f)
    trace=(L/"native_trace.jsonl").open("x",encoding="utf-8",newline="\n")
    try:
        assert type(sealed_plan).__name__=="mappingproxy","SEALED_PLAN_REQUIRED"
        cfg=sealed_plan
        assert cfg["authority_pass"] is True and cfg["source_route_gate_pass"] is True and cfg["run_token"]==TOKEN
        assert cfg["owner_authorization"]=="2026-10-31__NEW_EXPLICIT_RUNTIME_ROUTE_WITH_PREEXECUTION_HARD_GATES__ONE_120S_NATIVE_MATLAB_MINIMAL_PROBE"
        assert cfg["task_id"]==TASK and cfg["governance_commit"]=="582396de2a67826a6ec0f90701aa066d05eb6850"
        assert cfg["scientific_parent"]=="56447829ce0e6c3c85552c53c351b26a2452a4bd"
        assert cfg["native_seconds"]==120 and cfg["memory_limit"]==LIMIT and cfg["active_processes"]==1
        assert cfg["controller_identity"]==ident(Path(__file__).read_bytes()),"CONTROLLER_IDENTITY"
        script=W/"validators/multi_province/temp31_r6_r3_r2_r3_120s_native_probe_isolated.m"
        safe(script);assert cfg["probe_identity"]==ident(script.read_bytes()),"PROBE_IDENTITY"
        executable=Path(cfg["matlab_executable"]);safe(executable)
        assert ident(executable.read_bytes())==cfg["executable_identity"],"EXECUTABLE_IDENTITY"
        assert cfg["executable_identity"]["sha256"]=="4d251e680b8409d76d0524a1eb716de3c9e747386d3101e10f6ce1405ad1a59d"
        safe(R);safe(L)
        event("initial_config_verify",source_route_identity_pass=True,executable_sha256=cfg["executable_identity"]["sha256"],old_prefdir_entry_accesses=0)
        setup();phase="PREFDIR_PREFLIGHT";target=pref_preflight();pref_safe=True
        env=dict(os.environ)
        for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS","BLIS_NUM_THREADS","VECLIB_MAXIMUM_THREADS"):env[key]="1"
        env["MATLABPATH"]="";env["MATLAB_PREFDIR"]=target;env["PYTHONDONTWRITEBYTECODE"]="1";env["PYTHONNOUSERSITE"]="1";env.pop("PYTHONPATH",None)
        dump(L/"child_execution_configuration.json",dict(MATLAB_PREFDIR=target,explicit_child_only_overrides={key:env[key] for key in ("MATLAB_PREFDIR","MATLABPATH","OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS","BLIS_NUM_THREADS","VECLIB_MAXIMUM_THREADS")},parent_environment_modified=False))
        argv=[cfg["matlab_executable"],"-nodesktop","-nosplash","-singleCompThread","-logfile",str(RT/"native_matlab.log"),"-batch","run('"+script.as_posix()+"')"]
        assert "-nojvm" not in argv and len(argv)==8
        dump(L/"actual_argv.json",dict(argv=argv,removed=["-nojvm"],compatible_baseline="R6_R3_R1"))
        dump(L/"pre_native_source_and_configuration_gate.json",dict(status="PASS_BEFORE_PROCESS_CREATION",task_id=TASK,run_token=TOKEN,source_route_gate=True,controller_identity=cfg["controller_identity"],probe_identity=cfg["probe_identity"],executable_identity=cfg["executable_identity"],planned_argv=argv,native_seconds=120,job_process_memory=LIMIT,job_memory=LIMIT,active_process_limit=1,breakaway=False))
        phase="JOB_AND_SUSPENDED_PROCESS_GATE";native=Native();native.start(argv,env);safety=True
        phase="NATIVE_MINIMAL_PROBE";mismatch=False;next_regular=0;next_checkpoint=30
        origin=native.record["resume_observed"]["monotonic_ns"]
        def snapshot(name,nominal=None):
            at=stamp();code=native.exitcode();lim=native.limits()
            e=event(name,at=at,seconds_after_resume=(at["monotonic_ns"]-origin)/1e9,nominal_seconds=nominal,process_exit_code=code,markers=[m["stage"] for m in markers],resource=lim,termination_already_requested=native.record["forced_termination"])
            if nominal is not None:checkpoints.append(e)
        while True:
            now=time.monotonic_ns()
            if now>=native.deadline:
                code=native.timeout_stop()
                timed_out=code==ACTIVE
                if not timed_out:natural=code;event("natural_exit_observed_at_deadline",exit_code=code)
                snapshot("native_checkpoint",120)
                if not timed_out:read_markers(native)
                break
            native.drain()
            if not read_markers(native):mismatch=True;break
            code=native.exitcode()
            if code!=ACTIVE:
                natural=code
                if not read_markers(native):mismatch=True
                event("natural_exit_observed",exit_code=code);break
            elapsed=(now-origin)/1e9
            if next_checkpoint<=90 and elapsed>=next_checkpoint:
                snapshot("native_checkpoint",next_checkpoint);next_checkpoint+=30
            if elapsed>=next_regular:
                snapshot("native_activity_snapshot");next_regular=elapsed+1
            remain=max(0,(native.deadline-time.monotonic_ns())/1e9);time.sleep(min(.01,remain))
        if mismatch:terminal="STOP__R6_R3_R2_R3_PREFDIR_RUNTIME_MISMATCH"
        elif not timed_out and natural==0 and [m["stage"] for m in markers]==["ENTERED_MATLAB_USER_SCRIPT","PREFDIR_MATCH","MATLAB_VERSION","SPARSE_PROBE_PASS"]:terminal="STOP__AWAITING_GPT_INDEPENDENT_ABC"
        else:terminal="STOP__R6_R3_R2_R3_NATIVE_GATE_FAILED_REQUIRES_REVIEW"
    except BaseException as exc:
        error=dict(type=type(exc).__name__,phase=phase,private_message=str(exc))
        terminal="STOP__R6_R3_R2_R3_NATIVE_GATE_FAILED_REQUIRES_REVIEW" if native and native.resumed else "STOP__R6_R3_R2_R3_RUNTIME_ROUTE_OR_PREEXECUTION_GATE_BLOCKED"
        event("controller_exception",error_type=type(exc).__name__,phase=phase)
    finally:
        if native is not None:
            try:native.cleanup()
            except BaseException as exc:cleanup_error=dict(type=type(exc).__name__,private_message=str(exc));safety=False;terminal="STOP__R6_R3_R2_R3_SOURCE_PRIVACY_OR_DELIVERY_BLOCKED"
        if trace:trace.flush();trace.close();trace=None
        logs={}
        for name in ("native_stdout.txt","native_stderr.txt","native_matlab.log"):
            p=RT/name
            logs[name]=ident(p.read_bytes()) if p.is_file() else dict(status="NOT_CREATED")
        entries=[]
        if pref_safe:
            try:
                safe(PREF)
                for e in os.scandir(PREF):
                    st=e.stat(follow_symlinks=False);entries.append(dict(name=e.name,size=st.st_size,is_dir=stat.S_ISDIR(st.st_mode),reparse=bool(getattr(st,"st_file_attributes",0)&0x400)))
                assert not any(e["reparse"] for e in entries),"NEW_PREFDIR_CHILD_REPARSE"
            except BaseException as exc:cleanup_error=dict(type=type(exc).__name__,private_message=str(exc));safety=False;terminal="STOP__R6_R3_R2_R3_SOURCE_PRIVACY_OR_DELIVERY_BLOCKED"
        assert dict(os.environ)==parent_environment,"PARENT_ENVIRONMENT_MUTATED"
        dump(L/"new_prefdir_entries_private.json",dict(entries=entries,contents_read=False,no_cleanup=True))
        raw=dict(task_id=TASK,terminal=terminal,phase=phase,safety_gate_pass=safety,error=error,cleanup_error=cleanup_error,timed_out=timed_out,natural_exit_code=natural,native=native.record if native else None,markers=markers,events=events,checkpoints=checkpoints,job_notifications=notifications,log_identities=logs,new_prefdir_entry_count_after=len(entries),old_prefdir_accesses=0,parent_environment_modified=False,new_controller_runs=1,retries=0,model_calls=0,NPZ_reads=0,post_operator_comparisons=0,historical_timeout_root_cause="UNKNOWN")
        dump(L/"native_execution_receipt_raw.json",raw)
        print(json.dumps(dict(terminal=terminal,safety_gate_pass=safety,launch_attempts=native.record["launch_attempts"] if native else 0,created=int(native.created) if native else 0,resumed=native.resumed if native else False,timed_out=timed_out,natural_exit_code=natural,markers=[m["stage"] for m in markers],Job_notifications=[m["message"] for m in notifications],error_type=error["type"] if error else None,error_phase=phase,cleanup_error_type=cleanup_error["type"] if cleanup_error else None)),flush=True)
    return 0 if safety and terminal=="STOP__AWAITING_GPT_INDEPENDENT_ABC" else 1

if __name__=="__main__":raise SystemExit("EXPLICIT_VERIFIED_ENTRY_REQUIRED")
