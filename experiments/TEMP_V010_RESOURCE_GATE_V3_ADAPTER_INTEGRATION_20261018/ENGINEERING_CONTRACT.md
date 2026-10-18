# TEMP V010 Resource Gate — V3 Adapter Integration Task

TASK_ID=TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_20261018
STATUS=ISSUED_NOT_STARTED
SCOPE=ENGINEERING_ONLY / NO_SCIENCE / NO_HA
AUTHORITY=Owner explicitly authorized continuing after Astra accepted TEMP_V010_RESOURCE_GATE_NATIVE_SINGLE_CHILD_V3_20261018 as PASS_BOUNDED_NATIVE_SINGLE_CHILD_LOCAL.

## 1. Accepted baseline and limitations

Accepted bounded local test:
- run_id: 49b82ce3c2554dbeb0aa2fb6b0b2f067
- governance HEAD reported at start: 93007440c392b5f8e66256a2d440bfff3a15ef9a
- task commit: 09e073ee69b34fc22dd5448a6a39156a0cd11775
- task blob: f323a5855600b5dc4ef715a73533421dc09d1e99
- outcome: PASS_BOUNDED_NATIVE_SINGLE_CHILD_LOCAL
- synthetic: 31/31 reported pass
- real bounded Windows tests: 3/3 reported pass
- ZIP SHA256: 2cc4bc2a9000d725408d8bc77e108592b9dc3ff8245e719378cd51cdd150c3b4
- final receipt SHA256 was reported as b6bd8c16820487b2c2247a717c2ea839892d5be1219e6af79983ecdb19a2eb2d but its original standalone file was not independently supplied to Astra.

Acceptance scope is deliberately narrow: one direct child created suspended, assigned to a Job, membership verified before resume; a second suspended direct child was rejected at Job assignment under ActiveProcessLimit=1 and never resumed. This does NOT prove CreateProcess-before-creation denial, arbitrary descendant control, lifetime cumulative process limits, or full Runner I/O closure.

Prior failed resource task run_id 977d18ebe6e14a91bb049924cae715e4 remains FAIL_CLOSED_UNRESERVED_REAL_DESCENDANT. Prior scientific TEMP price tuning remains FAIL_CLOSED and not resumable. Do not rewrite history or reuse prior budgets.

## 2. Objective

Integrate the accepted bounded SingleChildGateV3 primitive into the existing resource-gate executor through a narrow adapter, then verify only the integrated, bounded execution path. Preserve fail-closed behavior. Do not broaden the claim to arbitrary child trees or cumulative process creation. Do not run HA/HJB/KFE/selector/root solver, TEMP price tuning, GE, IRF, or any scientific/model execution.

Formal V010 remains unchanged; V011 NOT_STARTED; model_activation=False; REAL_GE=False; Results=FALSE; FULL_RUNNER_IO_CLOSURE=BLOCKED.

## 3. Mandatory bootstrap and source integrity

1. Read current governance CURRENT.md, TASK_CURRENT.md, DOC_INDEX_CURRENT.md, V1.4 policy, this contract, V3 source/test/receipt/index materials.
2. Validate this task's fixed identity and current authorization.
3. Follow existing V1.3 BOOTSTRAP 0/1/2. Do not create logs/scripts/directories before root, scratch, worktree, index, common-dir, protected run roots, mirror and backup identities are established.
4. Use a fresh independent scratch for implementation. If the exact scratch and protected roots cannot be authenticated, read-only report and STOP; do not retry in another path.
5. Keep all accepted V3 source, old failure evidence, prior scratch, project model source, index/common-dir and backups byte-identical.
6. Record before/after hashes and changed paths; no silent copy-back into protected source trees.

## 4. Integration scope

A. Inspect V3 implementation and the prior ResourceGateV2 interface. Document the narrow adapter boundary before editing.
B. Integrate only the one-direct-child native primitive into the existing executor:
- each launch requires a single-use lease bound to task/run/gate/domain, executable identity/hash and one concrete launch;
- create direct child suspended, assign to the intended Job, verify membership/identity, then resume;
- second concurrent child must be denied by the tested Job admission path before its code executes;
- after assignment/resume failure, preserve exact error, terminate/reap as appropriate, latch STOP before any next backend call;
- reconcile reservation, actual creation, Job membership, ActiveProcesses/TotalProcesses and confirmed exit without double counting;
- cumulative created count never decreases after reap; active count decreases only after confirmed exit;
- distinguish controller, direct child, Python process, worker thread and tool-observed intake.
C. If ResourceGateV2 relies on nested bundles or arbitrary descendants, do not claim compatibility. Keep those paths disabled/blocked behind explicit UNSUPPORTED_DESCENDANT_TOPOLOGY until a separate architecture and authorization exist.
D. Keep existing synthetic tests and add adapter-level synthetic tests. No broad refactor, no generic process-tree control claims, no scientific source edits.
E. One bounded real Windows integration smoke test may run only after all synthetic and static checks pass. It must use a fresh isolated Job and a dummy executable with no child-spawn capability. It may create at most two direct suspended children total: one accepted-and-resumed child and one rejected-at-assignment probe that never resumes. If any unexpected descendant, unknown PID/parent, Job/lease mismatch, or STOP failure occurs, immediate E2 STOP and no further tests.
F. Do not re-run old failed scenarios merely for coverage. Reuse V3 accepted evidence read-only where valid; clearly distinguish reused baseline evidence from new integration evidence.

## 5. Budget and execution controls

- Total engineering processes and all descendants: <=192.
- Python/focused pytest starts: <=48.
- Simultaneously active Python processes: <=8.
- Active worker threads across all Python processes: <=64.
- Active engineering time: <=3 hours.
- Repair/validation batches: <=8.
- New non-Git bytes: <=512 MiB.
- No Git fetch/push, no network publication, no review cleanup. Do not spend closed prior budgets.
- Enforce every limit before launch/activation. Job ActiveProcessLimit is only a concurrency control; do not present it as lifetime cumulative creation control.
- If OS evidence cannot be captured or reconciled, mark UNKNOWN and fail closed.

## 6. Acceptance gates

P0 source/protection:
- task/authority identity verified;
- fresh scratch and protected paths authenticated;
- old accepted V3 source and all old failure evidence unchanged.

P1 static/adapter:
- no direct access path bypasses the gate for the supported single-child topology;
- unsupported descendant/nested topology is blocked explicitly;
- lease is bound to one launch and cannot be reused;
- assignment/identity/resume failures latch STOP before any subsequent backend invocation;
- counters are monotonic and domain-separated.

P2 synthetic:
- adapter denial, lease replay, wrong executable hash, wrong task/run/domain, assignment failure, resume failure, child exit, checkpoint failure and STOP propagation cases tested;
- exact denominator and results recorded;
- synthetic evidence is not presented as OS proof.

P3 real Windows integration:
- one direct child assigned and identity-checked before resume;
- one second suspended probe denied by Job admission and never resumed;
- no unexpected descendants;
- raw Job and process evidence reconciles with reservations and exits;
- all child/controller processes reaped at terminal seal.

P4 delivery:
- local report, manifest, sanitized evidence ZIP and final receipt;
- ZIP member inventory and hashes independently reproducible;
- no network publish. Do not claim Astra has independently checked OS facts until the original files are uploaded.

## 7. Terminal result

PASS means only the existing executor's supported single-direct-child launch path is integrated with the tested V3 gate and passes the stated tests. It does not enable nested bundles/arbitrary descendants or authorize scientific execution.

Any P0/P1/P2/P3 failure, unknown real PID, unaccounted child, resource cap violation, or broken STOP => FAIL_CLOSED / STOP. Do not continue after E2; no retries in the same stop chain.

Final state:
- prior TEMP price tuning remains FAIL_CLOSED, not resumable;
- prior V2 resource repair remains FAIL_CLOSED_UNRESERVED_REAL_DESCENDANT;
- current task science calls=0;
- formal V010 unchanged;
- V011 NOT_STARTED;
- model_activation=False; REAL_GE=False; Results=FALSE;
- FULL_RUNNER_IO_CLOSURE=BLOCKED;
- final stop: WAIT_ASTRA_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_REVIEW.
