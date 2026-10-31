# Observation grades and unresolved mechanism

DIRECT_SYSTEM_READ: one fixed Application query for IDs1000/1001 in UTC00:26-01:01 returned NoMatchingEventsFound, candidates0. No new fault-module or exception field was available. This does not establish global absence or diagnose log configuration.

DIRECT_FILESYSTEM_METADATA: one standard CrashDumps file matched MATLAB basename and time; size23219990 bytes, creation UTC00:31:33.828285 and mtime UTC00:31:35.037390. Its last-write time is13.032ms before the prior exit observation; this is filesystem correlation, not a call-stack or exact fault-time witness. Body was not opened, hashed, copied or uploaded. Filename/PID stay private; only basename hash is public. Exact process/dump body association remains unverified.

DIRECT_PERMISSION_LIMIT: a matching ProgramData ReportArchive directory was created UTC00:31:35.988366, after the exit observation, but direct child enumeration raised PermissionError. Directory stat bytes0 does not mean empty. Report.wer or dump children inside it were not observed. No elevation, ACL change, fallback or retry occurred. The exact permission-blocked terminal is retained even though other allowed observations completed.

DIRECT_READONLY_REGISTRY: HKLM64 global LocalDumps key exists, DumpType/DumpCount/DumpFolder NOT_SET; MATLAB.exe-specific key NOT_FOUND. No other hive/view or custom folder was followed. This does not prove whether the discovered file came from default WER or another crash mechanism.

DIRECT_LATEST_PREFDIR_METADATA: four direct files, sizes50/1/0/2837 bytes, metadata only. File count/timestamps do not prove user-level code entry or runtime prefdir match. Earlier preferences stayed closed.

FIXED_HISTORICAL_SOURCE:0xC00000FD=STATUS_STACK_OVERFLOW and the prior memory-limit notification remain supported by frozen review/native receipts. Windows semantic definition is source context, not newly observed exception record. Unique memory-limit-to-stack-failure causality, stack frames, precise internal startup state and old30-second timeout causes remain UNKNOWN. STACK_TRACE=NOT_OBSERVED; no dump-body permission exists in this task.

NOT_COMPLETED: denied WER directory children; dump/Report.wer content and call-stack/exception context; new Event1000/1001 exception/module fields; actual MATLAB prefdir/version/sparse stage; sustained120-second startup; economic/operator parity, strict stationarity and real31 GE/IRF. No resource relaxation or future experiment is authorized. Wait for independent GPT A/B/C and new Owner authority.
