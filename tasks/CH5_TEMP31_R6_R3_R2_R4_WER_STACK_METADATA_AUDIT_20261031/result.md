# TEMP31 bounded WER and metadata audit with a permission gap

TASK_ID=CH5_TEMP31_R6_R3_R2_R4_WER_STACK_METADATA_AUDIT_20261031
GOVERNANCE_COMMIT=83e17a51b3d4ff41280a4b8ed684867fe34cfac2
FIXED_SCIENTIFIC_PARENT=56447829ce0e6c3c85552c53c351b26a2452a4bd
CANDIDATE_BRANCH=codex/ch5-temp31-r6-r3-r2-r4-wer-stack-metadata-audit-20261031
ACTUAL_TERMINAL=STOP__R6_R3_R2_R4_WER_PERMISSION_OR_SCOPE_BLOCKED
MATLAB_PROCESS_CREATIONS=0
STACK_TRACE=NOT_OBSERVED

One actual auditor invocation, exit1, elapsed1.203s, runtime retries0. One no-profile noninteractive PowerShell child queried Application IDs1000/1001 in UTC2026-10-31T00:26:00Z to01:01:00Z; Get-WinEvent returned NoMatchingEventsFound, candidate_count0. New event exception/module fields are unobserved. This is a bounded no-match, not system-wide absence.

Five standard roots were checked shallowly. ProgramData ReportArchive and ReportQueue and user CrashDumps exist; user WER Archive/Queue roots were not found. One name/time-matching MATLAB ReportArchive directory has stat metadata but direct child enumeration was denied. It was not retried, elevated or traversed by another route. One name/time-matching.dmp exists in the allowed CrashDumps root:23219990 bytes, creation UTC00:31:33.828285, mtime UTC00:31:35.037390. Its contents were not read, hashed, copied or uploaded. This is metadata correlation, not dump-body or stack identity authentication.

HKLM64 global LocalDumps exists with DumpType/DumpCount/DumpFolder NOT_SET; MATLAB.exe-specific key NOT_FOUND. No registry changes or custom-folder traversal occurred. The exact latest R3 prefdir contains four direct child stat records; contents and earlier preferences were not read. Counts/times do not prove first MATLAB user-code entry or runtime prefdir match.

Frozen sources independently rehashed: current contract16714 bytes/Blob f19e426387864ce78d701487627692c9af10ac1f, prior review14629 bytes/Blob a427021db7371a3314fee0d9eeecc5a832ff238f, and fixed prior native event/cleanup/runtime receipts. They preserve prior PROCESS_MEMORY_LIMIT,1GiB peaks,0xC00000FD and original native failure STOP. A local pre-audit default-GBK preparation read error was preserved and corrected to explicit UTF8 before any system query; source connector and auditor retries stayed0.

No dump/Report.wer/preference body reads, MATLAB/Job experiment, new dump, model/NPZ/operator call, resource change, old-source/global-index write or filesystem cleanup occurred. The precise current/old failure causality remains UNKNOWN. The permission-blocked result is delivered as a bounded partial audit, awaiting independent GPT A/B/C and new Owner authorization. manifest.json plus DELIVERY_FINAL_RECEIPT.json/external LOCAL_ONLY final receipt identify two-stage delivery. No auto Issue/PR/merge/cleanup/next task.

P3=BLOCKED; V010=UNCHANGED; V011=NOT_STARTED; Results=FALSE; FORMAL_SOURCE_FREEZE=FALSE; FULL_RUNNER_IO_CLOSURE=BLOCKED; STRICT_KFE_STATIONARITY=FALSE_INHERITED_R3_R4_R5. Numeric/scientific review=NOT_TESTED_BY_DESIGN.
