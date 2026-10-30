# Job enforcement and cleanup: bounded evidence

The independently authenticated receipt/code show consistent ordering: suspended CreateProcessW; AssignProcessToJobObject; QueryInformationJobObject for limits/members; IsProcessInJob; ResumeThread previous-count1; close primary-thread handle. Historical Win32 success remains EXECUTOR_RECEIPT_ONLY. Current byte hashes/source checks are DIRECT_BYTES_AND_CODE_VERIFIED. R2 did not execute these APIs.

The gate records flags8968=0x2308, process/Job commit1073741824 each, active-process1, non-breakaway, kill-on-close and a single owned member. The earlier gate snapshot resume_called=false and later resumed=true describe different points and are consistent.

Peak966209536 was recorded by QueryFinalMemory after forced termination/reaping. No event subscription, completion port, limit-violation report, denied allocation or child-create denial was logged. A below-cap peak neither confirms nor excludes a Job-induced denial; LIMIT_CAUSE=UNKNOWN.

Cleanup checks status, terminates only the owned Job (or a suspended owned child if assignment had failed), waits5000ms, saves final forced code and closes handles. The old receipt has wait status0, forced exit3758096385=0xE0000001, all handle closures successful and cleanup_errors=[]. The thread close is in the original ordered events; other handles are in native.handle_cleanup. Prior numeric exit-status return values are not preserved, so no natural MATLAB diagnostic exit is available.

Old PID snapshots are executor witnesses. Static risk: Process32First/Next errors are not distinguished from normal enumeration completion. Static risk: self.cleaned is set before cleanup work; an exception could prevent another cleanup attempt, although finally still closes handles. The recorded run reports no such error. These risks do not establish the timeout root cause; wait/exit evidence for the owned handle provides bounded reaping support without a new R2 process scan.
