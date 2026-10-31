# New dump evidence, historical facts and remaining gaps

New direct bounded content evidence: recognizable MINIDUMP container,15 stream-directory slots, ExceptionStream code0xC00000FD and flags0. The actual stream code independently matches the prior process exit status; no field was filled from the historical expected value. Thread context descriptor exists and is file-bounded, but context/register bytes and exception parameters were deliberately skipped.

New process association: the filename PID and actual valid MiscInfo PID both match the exact prior R3 owned-process receipt; first module basename is MATLAB.exe. This strengthens file association beyond R4's name/time metadata. Original PIDs and private receipt stay LOCAL_ONLY. This is not a full-body cryptographic dump attestation or a fresh live-process inspection.

ExceptionAddress is inside the ntdll.dll range in the inspected first151 ModuleList entries, relative offset0x1C386.623 entries are declared; only16312 table bytes were read, within the16384 cap. The other472 entries were not read. The mapping is a positive range match in that prefix, not a claim of global overlap uniqueness, symbol-function resolution or a captured call-stack frame. Two short module-name strings were read solely to identify the relevant range and first image, not arbitrary strings from memory.

CDB unavailable at the single exact standard Windows Kits10 x64 location: SKIP_WITH_REASON. No debugger, signature/version/help process, symbols folder/server, alternative path scan, download or install was attempted. Call stack frames=0; no stack was manufactured. Missing at this exact path does not establish no debugger exists anywhere.

Still unresolved: call stack, precise exception instruction/function and register context, full module list, original full-body cryptographic identity, internal memory allocation/guard-page mechanism and unique1GiB-limit-to-stack-exception causality. Prior PROCESS_MEMORY_LIMIT and peak1GiB are historical fixed R3 observations, not new dump fields. The exception match alone cannot prove that cap is the sole necessary/sufficient cause or explain every old30-second timeout. Old causes remain UNKNOWN.

No MATLAB first-user marker/prefdir/version/sparse capability, sustained120-second runtime, economic policy/HJB/operator equivalence, strict KFE stationarity, full runner closure or real31 GE/IRF was tested. Independent GPT A/B/C and fresh Owner decisions remain pending. No resource relaxation, retry, cleanup or next task follows automatically.
