# TEMP V010 Resource Gate V3 — Native Single-Child Containment and Accounting

TASK_ID=TEMP_V010_RESOURCE_GATE_NATIVE_SINGLE_CHILD_V3_20261018
STATUS=ISSUED_NOT_STARTED
SCOPE=ENGINEERING_ONLY / NO_SCIENCE / NO_HA
ISSUE_AUTHORITY=Owner accepted the DOC_ONLY report as a compliant fail-closed stop and authorized continuing with the next task order after Project Sources synchronization.

## 1. Parent state and prior report acceptance

The previous DOC_ONLY task CH5_V14_ONE_TIME_CODEX_DOC_SYNC_20261018 did not modify the local mirror. Its terminal outcome is accepted as PROCEDURE_COMPLIANT_STOP, not as a successful local sync. The exact target was not authorized and write identity was unknown; no alternate path may be tried without a new authorization.

Previous engineering run:
- run_id: 977d18ebe6e14a91bb049924cae715e4
- terminal: FAIL_CLOSED_UNRESERVED_REAL_DESCENDANT / STOP
- kernel-only engineering 35→35; conservative 37→37
- synthetic tests 28/28 reported pass
- real Windows Job reservation 2, TotalProcesses 3, E2 STOP
- two exited descendant identities/PIDs UNKNOWN; Python actual total UNKNOWN
- real plan 6 tests: 1 pass, 1 fail, 4 NOT_RUN
- science calls 0; Git fetch/push 0; formal model writes 0.

Do not rewrite or supersede any prior result. The DOC_ONLY report did not certify the local mirror or source files as synchronized.

## 2. Authorized objective

Repair and verify only the resource gate's real Windows creation-control and accounting path. The aim is to establish a bounded, auditable, native single-child execution primitive; do not claim control over arbitrary descendants or lifetime cumulative process creation unless the implementation actually enforces that property.

This task has NO scientific authorization. HA/HJB/KFE/selector/root solver calls = 0. Do not run TEMP A1/A2/A3 or any model. Formal V010, its source, selector and frozen scientific contract remain unchanged. V011 NOT_STARTED; model_activation=False; REAL_GE=False; Results=FALSE.

## 3. Work scope

A. Read-only inspect the V2 source, test sources, failure records and source hashes. Keep original failed files byte-identical.
B. Implement changes only in a newly verified independent scratch created after the existing BOOTSTRAP 0/1/2 passes. Do not write before root/path/worktree/index/common-dir/backup identity is established. If any protected location or scratch target cannot be proven, report read-only and STOP.
C. Split the resource concepts in code and output:
- app reservation/lease;
- actual direct process creation;
- Job ActiveProcesses and TotalProcesses;
- tool-observed intake processes;
- Python starts/active Python processes;
- worker threads;
- launch denied / launch failed / process exited / identity unknown.
Cumulative created counts must never decrease after reap; active counts may decrease only after exit/reap evidence. Every lease binds task/run/gate/domain/quota/one concrete creation operation and is single-use.
D. Implement a native single-child smoke path only:
- one explicit child executable, no shell wrapper and no nested bundle;
- child must not spawn any descendants;
- create child suspended where supported;
- assign to a newly created Job Object before ResumeThread;
- verify Job membership and expected identity before resume;
- configure ActiveProcessLimit=1 to bound concurrent activity;
- capture raw Job accounting before/after, PID, parent PID, creation/exit status, reservation ID, and timestamps;
- test a second simultaneous active child is rejected before it can execute;
- clearly state this tests concurrent active containment, not lifetime cumulative TotalProcesses enforcement.
Do not claim Job ActiveProcessLimit limits cumulative lifetime process count. Do not use polling as a creation-prevention claim.
E. Test failure handling with dummy processes only. If any unexpected descendant, unknown PID/parent, reservation/Job mismatch, broken ledger/checkpoint, or STOP propagation failure occurs, E2 STOP immediately; do not restart controller or continue tests in the same stop chain.
F. Synthetic tests remain separate from real Windows tests. Report exact denominators; do not use synthetic PASS to replace real OS evidence.

## 4. Budget

- ENGINEERING total child processes/descendants hard cap: 192.
- Python/focused pytest starts hard cap: 48; reject the 49th before creation.
- Simultaneously active Python processes: 8.
- Active worker threads across all Python processes: 64.
- Active engineering wall time: 3 hours.
- Repair/validation batches: 8.
- New non-Git bytes: 512 MiB.
- This task performs no Git fetch/push, no network publication, no review-branch cleanup. No budget carry-forward from prior tasks.
- Process, Python, thread and tool-observed intake counts are distinct; don't collapse or double count them. If native OS counters cannot be captured or independently mapped, label UNKNOWN and fail closed.
- All limits must be checked before the relevant launch/operation. An application ledger reservation alone does not prove OS-level creation prevention.

## 5. Acceptance gates

P0 — source/path protection:
- original failed evidence hashes unchanged;
- new independent scratch identity verified;
- no protected worktree/index/common-dir/backup writes.

P1 — synthetic logic:
- per-lease single-use;
- 49th Python start denied before creation;
- 9th simultaneous Python process denied before creation;
- 65th active thread denied before activation;
- 193rd child process denied before creation;
- cumulative count monotonic; active count falls only with confirmed exit;
- append/checkpoint failure or STOP yields zero subsequent dummy launches.

P2 — native Windows single-child containment:
- exact OS/Job/PID evidence for one direct child;
- Job membership verified before resume;
- second simultaneous child cannot execute under ActiveProcessLimit=1;
- no unexpected descendants;
- pre/post Job counters and reservations reconcile;
- stop immediately if any descendant or identity is unknown.

P3 — result and local evidence bundle:
- report synthetic and real tests separately;
- report counts, actual vs reserved, unknowns and stop point;
- preserve first error and every failed attempt;
- no network publishing and no science.

A pass means only the bounded single-child containment primitive passed under the tested Windows conditions. It does not establish arbitrary descendant control, complete Runner I/O closure, or scientific readiness.

## 6. Terminal outcomes

Any E2/unknown real process identity/counter mismatch => FAIL_CLOSED / STOP. Do not continue to another test after E2. P0/P1 pass cannot override P2 failure. If P2 is stopped, preserve unrun tests as NOT_RUN.

Final status:
- prior TEMP tuning remains FAIL_CLOSED and not resumable;
- prior resource repair remains FAIL_CLOSED_UNRESERVED_REAL_DESCENDANT;
- current task science calls=0;
- formal V010 unchanged; V011 NOT_STARTED;
- model_activation=False; REAL_GE=False; Results=FALSE;
- FULL_RUNNER_IO_CLOSURE=BLOCKED unless independently proven;
- stop at WAIT_ASTRA_NATIVE_SINGLE_CHILD_RESOURCE_GATE_REVIEW.
