# Actual control-flow excerpts

OLD_CONTROLLER_IDENTITY={"bytes": 17189, "git_blob": "57ea43508a8e1419862668168c617b1782dbf84d", "sha256": "919aed33544ab9bc5c8f46229b7b7308e061136178731ceb1f5c76da76dcca00"}
OLD_RECIPE_IDENTITY={"bytes": 3253, "git_blob": "7d5239dda794aa047c63574c3c9bb32bcf2a386d", "sha256": "21e96e99037fd4c4e1ac3c28c2cebca378c472ccd7d583d1f83264d50d5cd7fe"}

Selected authentic snippets with original line numbers. Old source was read/parsed only. Historical API outcomes remain executor receipts; R2 did not rerun them.

R6_R1_CONTROLLER; original lines 10-16; identities {"first_line": 10, "last_line": 16, "public_fragment": {"bytes": 174, "git_blob": "032b007db2093289a04dce638422910443ce81c1", "sha256": "5fe12534c5e974cb752663ee870704d44ab64688d3f011e3962a3fba3cab107b"}, "raw_fragment": {"bytes": 174, "git_blob": "032b007db2093289a04dce638422910443ce81c1", "sha256": "5fe12534c5e974cb752663ee870704d44ab64688d3f011e3962a3fba3cab107b"}, "transformation": "absolute drive path literal replacement only"}

```text
10: CREATE_SUSPENDED=0x00000004
11: CREATE_UNICODE_ENVIRONMENT=0x00000400
12: CREATE_NO_WINDOW=0x08000000
13: STILL_ACTIVE=259
14: LIMIT=1024**3
15: FLAGS=0x100|0x200|0x2000|0x8
16: DEADLINE_SECONDS=30
```

R6_R1_CONTROLLER; original lines 63-82; identities {"first_line": 63, "last_line": 82, "public_fragment": {"bytes": 849, "git_blob": "4fbdaca4e616ddce6e5ec744cbb8ac98dac71324", "sha256": "45bc47a20a9d8826756eeb62d0d30cade88d2d7c914c7fcc8866a50cafbe3ba9"}, "raw_fragment": {"bytes": 849, "git_blob": "4fbdaca4e616ddce6e5ec744cbb8ac98dac71324", "sha256": "45bc47a20a9d8826756eeb62d0d30cade88d2d7c914c7fcc8866a50cafbe3ba9"}, "transformation": "absolute drive path literal replacement only"}

```text
63: def checked(ok,name):
64:     err=0 if ok else ctypes.get_last_error()
65:     events.append(dict(api=name,ok=bool(ok),win32_error=err))
66:     if not ok: raise OSError(err,name)
67: def close(handle,name):
68:     if handle:
69:         ok=k.CloseHandle(handle); events.append(dict(api="CloseHandle",handle_role=name,ok=bool(ok),win32_error=0 if ok else ctypes.get_last_error()))
70:         return bool(ok)
71:     return True
72: def matlab_pids():
73:     h=k.CreateToolhelp32Snapshot(2,0)
74:     checked(h and h!=ctypes.c_void_p(-1).value,"CreateToolhelp32Snapshot")
75:     p=PE();p.dwSize=ctypes.sizeof(p);out=[]
76:     try:
77:         ok=k.Process32FirstW(h,ctypes.byref(p))
78:         while ok:
79:             if p.szExeFile.casefold()=="matlab.exe":out.append(int(p.th32ProcessID))
80:             ok=k.Process32NextW(h,ctypes.byref(p))
81:     finally: close(h,"process_snapshot")
82:     return sorted(out)
```

R6_R1_CONTROLLER; original lines 88-128; identities {"first_line": 88, "last_line": 128, "public_fragment": {"bytes": 4039, "git_blob": "e4f717f046d81f837bee41ba184f05bc4caa4d27", "sha256": "167a1ba0cb87562fa61dbf747d05e4adda4c0d1639d07ff0873f9d26eedec824"}, "raw_fragment": {"bytes": 4039, "git_blob": "e4f717f046d81f837bee41ba184f05bc4caa4d27", "sha256": "167a1ba0cb87562fa61dbf747d05e4adda4c0d1639d07ff0873f9d26eedec824"}, "transformation": "absolute drive path literal replacement only"}

```text
88:     def query(self):
89:         x=EXT()
90:         checked(k.QueryInformationJobObject(self.job,9,ctypes.byref(x),ctypes.sizeof(x),None),self.label+":QueryJobLimits")
91:         flags=int(x.BasicLimitInformation.LimitFlags)
92:         assert (flags&FLAGS)==FLAGS and not flags&(0x800|0x1000),"JOB_FLAGS_OR_BREAKAWAY"
93:         assert x.ProcessMemoryLimit==LIMIT and x.JobMemoryLimit==LIMIT and x.BasicLimitInformation.ActiveProcessLimit==1,"JOB_LIMIT_READBACK"
94:         member=w.BOOL()
95:         checked(k.IsProcessInJob(self.pi.hProcess,self.job,ctypes.byref(member)),self.label+":IsProcessInJob")
96:         assert member.value,"JOB_MEMBERSHIP_FALSE"
97:         ids=IDS()
98:         checked(k.QueryInformationJobObject(self.job,3,ctypes.byref(ids),ctypes.sizeof(ids),None),self.label+":QueryJobMembers")
99:         members=[int(ids.ProcessIdList[i]) for i in range(ids.NumberOfProcessIdsInList)]
100:         assert members==[self.pi.dwProcessId] and ids.NumberOfAssignedProcesses==1,"JOB_SINGLE_OWNED_CHILD"
101:         return dict(limit_flags=flags,process_committed_limit=int(x.ProcessMemoryLimit),job_committed_limit=int(x.JobMemoryLimit),active_process_limit=1,breakaway_allowed=False,kill_on_job_close=True,is_process_in_job=bool(member.value),members=members,peak_process_committed=int(x.PeakProcessMemoryUsed),peak_job_committed=int(x.PeakJobMemoryUsed))
102:     def start(self):
103:         self.job=k.CreateJobObjectW(None,None);checked(bool(self.job),self.label+":CreateJobObjectW")
104:         x=EXT();x.BasicLimitInformation.LimitFlags=FLAGS;x.BasicLimitInformation.ActiveProcessLimit=1;x.ProcessMemoryLimit=LIMIT;x.JobMemoryLimit=LIMIT
105:         checked(k.SetInformationJobObject(self.job,9,ctypes.byref(x),ctypes.sizeof(x)),self.label+":SetJobLimits")
106:         sa=SA();sa.nLength=ctypes.sizeof(sa);sa.bInheritHandle=True
107:         for suffix,access,creation in [("stdin",0x80000000,3),("stdout",0x40000000,1),("stderr",0x40000000,1)]:
108:             name="NUL" if suffix=="stdin" else str(L/(self.label+"_"+suffix+".txt"))
109:             h=k.CreateFileW(name,access,3,ctypes.byref(sa),creation,0x80,None)
110:             checked(h and h!=ctypes.c_void_p(-1).value,self.label+":CreateFile:"+suffix);self.files.append(h)
111:         si=SI();si.cb=ctypes.sizeof(si);si.dwFlags=0x100;si.hStdInput,si.hStdOutput,si.hStdError=self.files
112:         line=ctypes.create_unicode_buffer(subprocess.list2cmdline(self.argv))
113:         envblock=ctypes.create_unicode_buffer("\0".join(a+"="+b for a,b in sorted(self.env.items(),key=lambda t:t[0].upper()))+"\0\0")
114:         self.record["creation_attempted"]=True
115:         dump(L/(self.label+"_creation_claim.json"),dict(label=self.label,attempt=1,max_attempts=1,retries=0,creation_flags=CREATE_SUSPENDED|CREATE_UNICODE_ENVIRONMENT|CREATE_NO_WINDOW,limits=LIMIT))
116:         ok=k.CreateProcessW(self.argv[0],line,None,None,True,CREATE_SUSPENDED|CREATE_UNICODE_ENVIRONMENT|CREATE_NO_WINDOW,ctypes.cast(envblock,ctypes.c_void_p),str(L),ctypes.byref(si),ctypes.byref(self.pi))
117:         checked(ok,self.label+":CreateProcessW");self.created=True;self.record.update(created=True,pid=int(self.pi.dwProcessId),tid=int(self.pi.dwThreadId))
118:         checked(k.AssignProcessToJobObject(self.job,self.pi.hProcess),self.label+":AssignProcessToJobObject");self.assigned=True
119:         gate=self.query();assert self.exitcode()==STILL_ACTIVE,"CHILD_EXITED_WHILE_SUSPENDED"
120:         self.record.update(pre_resume_gate=gate,pre_execution_gate=True)
121:         if self.label=="matlab":dump(R/"windows_job_pre_execution_gate.json",dict(task_id=TASK,status="PASS_BEFORE_RESUME",creation_suspended=True,resume_called=False,**gate))
122:         previous=k.ResumeThread(self.pi.hThread)
123:         events.append(dict(api=self.label+":ResumeThread",previous_suspend_count=int(previous),ok=previous==1))
124:         assert previous==1,"RESUME_THREAD_COUNT_NOT_ONE"
125:         self.resumed=True;self.record["resumed"]=True;self.record["resume_previous_count"]=int(previous)
126:         assert close(self.pi.hThread,self.label+":main_thread"),"THREAD_HANDLE_CLOSE_FAILED"
127:         self.pi.hThread=None
128:         return self
```

R6_R1_CONTROLLER; original lines 130-161; identities {"first_line": 130, "last_line": 161, "public_fragment": {"bytes": 2035, "git_blob": "d5051e3c3e2ab35c55f26e2dd92469105e92305c", "sha256": "e606d7c20ffda84cf2a7f83e1393d0025ab4803b14e7fcbcbbe2c10e59857852"}, "raw_fragment": {"bytes": 2035, "git_blob": "d5051e3c3e2ab35c55f26e2dd92469105e92305c", "sha256": "e606d7c20ffda84cf2a7f83e1393d0025ab4803b14e7fcbcbbe2c10e59857852"}, "transformation": "absolute drive path literal replacement only"}

```text
130:         code=w.DWORD();checked(k.GetExitCodeProcess(self.pi.hProcess,ctypes.byref(code)),self.label+":GetExitCodeProcess")
131:         return int(code.value)
132:     def cleanup(self):
133:         if self.cleaned:return self.record
134:         self.cleaned=True
135:         try:
136:             if self.created:
137:                 code=self.exitcode()
138:                 if code==STILL_ACTIVE:
139:                     ok=k.TerminateJobObject(self.job,0xE0000001) if self.assigned else k.TerminateProcess(self.pi.hProcess,0xE0000001)
140:                     checked(ok,self.label+":TerminateOwnedJobOrSuspendedChild");self.record["forced_termination"]=True
141:                 wait=k.WaitForSingleObject(self.pi.hProcess,5000);self.record["reaped_wait_status"]=int(wait)
142:                 assert wait==0,"OWNED_CHILD_REAP_FAILED"
143:                 self.record["exit_code"]=self.exitcode()
144:                 if self.assigned:
145:                     x=EXT()
146:                     checked(k.QueryInformationJobObject(self.job,9,ctypes.byref(x),ctypes.sizeof(x),None),self.label+":QueryFinalMemory")
147:                     self.record["peak_process_committed"]=int(x.PeakProcessMemoryUsed);self.record["peak_job_committed"]=int(x.PeakJobMemoryUsed)
148:         finally:
149:             handles=[(self.pi.hThread,"main_thread"),(self.job,"job"),(self.pi.hProcess,"process")]+[(h,"stdio_"+str(i)) for i,h in enumerate(self.files)]
150:             for h,role in handles:
151:                 if h:self.record["handle_cleanup"].append(dict(role=role,closed=close(h,self.label+":"+role)))
152:         self.record["all_handles_closed"]=all(row["closed"] for row in self.record["handle_cleanup"])
153:         return self.record
154: def wait_file(p,child,deadline):
155:     while not p.is_file():
156:         if child.exitcode()!=STILL_ACTIVE:raise RuntimeError("NATIVE_EXIT_BEFORE_"+p.name)
157:         if time.monotonic()>deadline:raise TimeoutError("NATIVE_WALL_TIMEOUT")
158:         time.sleep(.025)
159: def main():
160:     stage="CONTROLLER_PREFLIGHT";native=None;compare=None;baseline=[];error=None;terminal=None;probe={}
161:     started=time.monotonic()
```

R6_R1_CONTROLLER; original lines 163-195; identities {"first_line": 163, "last_line": 195, "public_fragment": {"bytes": 2875, "git_blob": "350c84c9f0a6d058f01ef0df9367391b6206ca83", "sha256": "49249afca7bc43ce9914d3781b1a674448a844574673e8df585c5df2ff37e31c"}, "raw_fragment": {"bytes": 2875, "git_blob": "350c84c9f0a6d058f01ef0df9367391b6206ca83", "sha256": "49249afca7bc43ce9914d3781b1a674448a844574673e8df585c5df2ff37e31c"}, "transformation": "absolute drive path literal replacement only"}

```text
163:         assert not (R/"matlab_native_probe_receipt.json").exists(),"NO_RETRY_RECEIPT_ALREADY_EXISTS"
164:         cfg=json.loads((L/"run_config.json").read_text(encoding="utf-8"))
165:         for name in ("temp31_r6_r1_matlab_launch_controller_isolated.py","temp31_r6_r1_python_post_elementwise_isolated.py"):
166:             ast.parse((W/"validators/multi_province"/name).read_text(encoding="utf-8"),filename=name)
167:         assert cfg["source_gate_pass"] and cfg["old_r6_preserved"]
168:         exe=Path(cfg["matlab_executable"]);assert identity(exe.read_bytes())==cfg["matlab_executable_identity"]
169:         setup();baseline=matlab_pids()
170:         env=dict(os.environ)
171:         for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS","BLIS_NUM_THREADS","VECLIB_MAXIMUM_THREADS"):env[key]="1"
172:         env["MATLABPATH"]="";env["MATLAB_PREFDIR"]=str(L/"matlab_prefs");env["PYTHONDONTWRITEBYTECODE"]="1";env["PYTHONNOUSERSITE"]="1";env.pop("PYTHONPATH",None)
173:         script=W/"validators/multi_province/temp31_r6_r1_matlab_post_recipe_isolated.m"
174:         argv=[str(exe),"-nojvm","-nodesktop","-nosplash","-singleCompThread","-batch","run('"+script.as_posix()+"')"]
175:         stage="NATIVE_CREATION_AND_JOB_GATE";native=Child("matlab",argv,env);native.start()
176:         deadline=time.monotonic()+DEADLINE_SECONDS
177:         stage="MATLAB_NATIVE_PROBE";wait_file(L/"native_probe_ready.txt",native,deadline)
178:         lines=(L/"native_probe_ready.txt").read_text().splitlines()
179:         assert len(lines)>=3 and lines[1]=="2022b" and lines[2]=="SPARSE_PROBE_PASS","MATLAB_VERSION_OR_SPARSE_PROBE_FAILED"
180:         probe=dict(status="PASS_NATIVE_R2022B_SPARSE_PROBE",version=lines[0],release=lines[1],job_live_after_probe=native.query())
181:         dump(L/"allow_synthetic.signal",dict(allowed=True))
182:         stage="NATIVE_SYNTHETIC_ASSEMBLY";wait_file(L/"synthetic_ready.txt",native,deadline)
183:         remaining=max(0,int((deadline-time.monotonic())*1000))
184:         assert k.WaitForSingleObject(native.pi.hProcess,remaining)==0,"NATIVE_WALL_TIMEOUT"
185:         assert native.exitcode()==0,"NATIVE_SCRIPT_EXIT_NONZERO"
186:         native.cleanup()
187:         stage="PYTHON_ELEMENTWISE_COMPARISON"
188:         entry=W/"validators/multi_province/temp31_r6_r1_python_post_elementwise_isolated.py"
189:         compare=Child("comparator",[sys.executable,"-B",str(entry)],env);compare.start()
190:         assert k.WaitForSingleObject(compare.pi.hProcess,30000)==0,"COMPARATOR_WALL_TIMEOUT"
191:         code=compare.exitcode();assert code in (0,2),"COMPARATOR_IMPLEMENTATION_OR_INPUT_FAILURE"
192:         compare.cleanup()
193:         result=json.loads((R/"matlab_python_elementwise_comparison.json").read_text())
194:         assert result["completed"],"COMPARISON_INCOMPLETE"
195:         terminal="STOP__R6_R1_ELEMENTWISE_DIFFERENCE_OWNER_DECISION" if result["tolerance_mismatches_total"] else "STOP__AWAITING_GPT_INDEPENDENT_ABC"
```

R6_R1_CONTROLLER; original lines 197-224; identities {"first_line": 197, "last_line": 224, "public_fragment": {"bytes": 2528, "git_blob": "f2989289310e551d9141068b802dbcaaefab86b5", "sha256": "b5bd5e38a13faf33f0e64b18578090406f794fa71bb3bbf2783ab2e793ed91e0"}, "raw_fragment": {"bytes": 2528, "git_blob": "f2989289310e551d9141068b802dbcaaefab86b5", "sha256": "b5bd5e38a13faf33f0e64b18578090406f794fa71bb3bbf2783ab2e793ed91e0"}, "transformation": "absolute drive path literal replacement only"}

```text
197:     except BaseException as e:
198:         error=dict(type=type(e).__name__,message=str(e),stage=stage)
199:         terminal="STOP__R6_R1_CONTROLLER_PREFLIGHT_FAILED" if native is None or not native.created else "STOP__R6_R1_NATIVE_MATLAB_GATE_FAILED"
200:         if stage=="PYTHON_ELEMENTWISE_COMPARISON":terminal="STOP__R6_R1_SOURCE_PRIVACY_OR_DELIVERY_BLOCKED"
201:     finally:
202:         cleanup_errors=[]
203:         for child in (compare,native):
204:             if child is not None:
205:                 try:child.cleanup()
206:                 except BaseException as e:cleanup_errors.append(dict(type=type(e).__name__,message=str(e),label=child.label))
207:         after=[]
208:         if k is not None:
209:             try:after=matlab_pids()
210:             except BaseException as e:cleanup_errors.append(dict(type=type(e).__name__,message=str(e),label="post_process_inventory"))
211:         owned_pid=None if native is None or not native.created else int(native.pi.dwProcessId)
212:         orphan=owned_pid is not None and owned_pid in after
213:         if cleanup_errors or orphan:terminal="STOP__R6_R1_NATIVE_MATLAB_GATE_FAILED"
214:         logs={}
215:         for label in ("matlab","comparator"):
216:             for stream in ("stdout","stderr"):
217:                 p=L/(label+"_"+stream+".txt")
218:                 if p.is_file():logs[label+"_"+stream]=identity(p.read_bytes())
219:         receipt=dict(task_id=TASK,terminal=terminal,stage=stage,error=error,probe=probe,MATLAB_RUNTIME_CAPABILITY="PROBE_PASSED" if probe else ("UNTESTED" if native is None or not native.resumed else "NATIVE_GATE_FAILED"),native=native.record if native else None,comparator=compare.record if compare else None,logs=logs,elapsed_seconds=time.monotonic()-started,baseline_matlab_pids=baseline,after_matlab_pids=after,owned_orphan_matlab=bool(orphan),external_sessions_never_terminated=True,cleanup_errors=cleanup_errors,events=events,retries=0,model_calls=0,NPZ_reads=0)
220:         dump(R/"matlab_native_probe_receipt.json",receipt)
221:         if not (R/"windows_job_pre_execution_gate.json").exists():dump(R/"windows_job_pre_execution_gate.json",dict(status="NOT_PASSED",stage=stage,error=error,native=native.record if native else None))
222:         print(json.dumps(dict(terminal=terminal,stage=stage,error=error,probe=probe,native=native.record if native else None,comparator=compare.record if compare else None,owned_orphan_matlab=bool(orphan),cleanup_errors=cleanup_errors,retries=0)),flush=True)
223:     return 0 if error is None and not cleanup_errors and not orphan else 1
224: if __name__=="__main__":raise SystemExit(main())
```

R6_R1_RECIPE_PERMISSION; original lines 7-18; identities {"first_line": 7, "last_line": 18, "public_fragment": {"bytes": 740, "git_blob": "186210f247a53b97a2146a56c780e8edfad8179c", "sha256": "2aed6bc594073a0902787ac0461f0d3fc9049afb76d01a2e907b0b4e9d2beab9"}, "raw_fragment": {"bytes": 740, "git_blob": "186210f247a53b97a2146a56c780e8edfad8179c", "sha256": "2aed6bc594073a0902787ac0461f0d3fc9049afb76d01a2e907b0b4e9d2beab9"}, "transformation": "absolute drive path literal replacement only"}

```text
7: root=fileparts(fileparts(fileparts(mfilename('fullpath'))));
8: outdir=fullfile(root,'tasks','CH5_TEMP31_R6_R1_MATLAB_LAUNCH_CONTROLLER_RECOVERY_20261030','LOCAL_ONLY');
9: % Native probe occurs before the synthetic execution permission signal.
10: probe=spdiags([1;2;3],0,3,3); assert(isequal(full(probe),diag([1 2 3])));
11: f=fopen(fullfile(outdir,'native_probe_ready.txt'),'w'); assert(f~=-1);
12: fprintf(f,'%s\n%s\nSPARSE_PROBE_PASS\n',version,version('-release')); fclose(f);
13: t=tic;
14: while ~exist(fullfile(outdir,'allow_synthetic.signal'),'file')
15:     assert(toc(t)<25,'SYNTHETIC_PERMISSION_TIMEOUT'); pause(0.025);
16: end
17: X=-min(s,0)/db; Y=min(s,0)/db-max(s,0)/db; Z=max(s,0)/db;
18: chih=-min(mh,0)/dah; yyh=min(mh,0)/dah-max(mh,0)/dah; zetah=max(mh,0)/dah;
```

R6_R1_RECIPE_PERMISSION; original lines 54-57; identities {"first_line": 54, "last_line": 57, "public_fragment": {"bytes": 373, "git_blob": "3bdf95a31fdbe5c8df750c359db5efe0913446c0", "sha256": "a1035de4037168ef4c25c7d7cee60854039a445b65e39f195047db0ac57fe3b9"}, "raw_fragment": {"bytes": 373, "git_blob": "3bdf95a31fdbe5c8df750c359db5efe0913446c0", "sha256": "a1035de4037168ef4c25c7d7cee60854039a445b65e39f195047db0ac57fe3b9"}, "transformation": "absolute drive path literal replacement only"}

```text
54: f=fopen(fullfile(outdir,'matrix_stats.csv'),'w'); assert(f~=-1); fprintf(f,'%d,%d,%d,%d,%d\n',stats.'); fclose(f);
55: f=fopen(fullfile(outdir,'synthetic_ready.txt'),'w'); assert(f~=-1);
56: fprintf(f,'MATLAB_POST_ASSEMBLY_RECIPE_ORACLE\nsynthetic_cases=1\nfull_model_calls=0\ncenter_length=9\nappended_band_length=10\n'); fclose(f);
57: disp('R6_SYNTHETIC_RECIPE_ASSEMBLY_COMPLETE');
```
