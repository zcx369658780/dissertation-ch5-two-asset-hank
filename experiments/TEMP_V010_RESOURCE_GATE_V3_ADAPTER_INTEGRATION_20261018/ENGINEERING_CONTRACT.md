# TEMP V010 Resource Gate — V3 Adapter Integration Task

TASK_ID=TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_20261018
STATUS=ISSUED_NOT_STARTED
SCOPE=ENGINEERING_ONLY / NO_SCIENCE / NO_HA
OWNER_AUTHORIZATION=Owner explicitly authorized continuing after acceptance of TEMP_V010_RESOURCE_GATE_NATIVE_SINGLE_CHILD_V3_20261018 as PASS_BOUNDED_NATIVE_SINGLE_CHILD_LOCAL.

## Accepted baseline and limits

Accepted run: 49b82ce3c2554dbeb0aa2fb6b0b2f067. Fixed V3 task commit 09e073ee69b34fc22dd5448a6a39156a0cd11775; blob f323a5855600b5dc4ef715a73533421dc09d1e99. Outcome PASS_BOUNDED_NATIVE_SINGLE_CHILD_LOCAL; synthetic 31/31 and bounded Windows tests 3/3 reported. ZIP SHA256 2cc4bc2a9000d725408d8bc77e108592b9dc3ff8245e719378cd51cdd150c3b4. The original standalone FINAL_RECEIPT was not separately supplied to Astra.

Accepted scope: one direct child created suspended, assigned to a Job, identity-checked before resume; one second suspended direct child rejected at Job assignment and never resumed. This does not prove CreateProcess-before-creation denial, arbitrary descendant control, lifetime cumulative process limits, or full Runner I/O closure.

Prior resource repair run 977d18ebe6e14a91bb049924cae715e4 remains FAIL_CLOSED_UNRESERVED_REAL_DESCENDANT. Prior scientific TEMP price tuning remains FAIL_CLOSED and not resumable. Do not rewrite history or reuse closed budgets.

## Objective

Integrate the accepted bounded SingleChildGateV3 primitive into the existing resource-gate executor through a narrow adapter, then verify only the integrated bounded execution path. Preserve fail-closed behavior. Do not broaden claims to arbitrary child trees or cumulative process creation. No HA/HJB/KFE/selector/root solver, TEMP price tuning, GE, IRF or any scientific/model execution.

Formal V010 unchanged; V011 NOT_STARTED; model_activation=False; REAL_GE=False; Results=FALSE; FULL_RUNNER_IO_CLOSURE=BLOCKED.

## Bootstrap and source integrity

1. Read latest CURRENT.md, TASK_CURRENT.md, DOC_INDEX_CURRENT.md, V1.4 policy, this contract and V3 source/test/index materials.
2. Verify task identity and authorization.
3. Follow existing V1.3 BOOTSTRAP 0/1/2. Do not create logs/scripts/directories before root, scratch, worktree, index, common-dir, protected run roots, mirror and backup identities are established.
4. Use fresh independent scratch. If target or protected roots cannot be authenticated, read-only report and STOP; do not retry another path.
5. Keep accepted V3 source, all old failure evidence, prior scratch, model source, index/common-dir and backups byte-identical.
6. Record before/after hashes and changed paths; no silent copy-back into protected source trees.

## Integration scope

A. Read-only inspect V3 implementation and prior ResourceGateV2 interface; document narrow adapter boundary before editing.
B. Integrate only the one-direct-child native primitive:
- each launch needs a single-use lease bound to task/run/gate/domain, executable identity/hash and one concrete launch;
- create direct child suspended, assign to intended Job, verify membership/identity, then resume;
- second concurrent child must be denied by tested Job admission before its code executes;
- on assignment/identity/resume failure, preserve exact error, terminate/reap where appropriate, latch STOP before any next backend invocation;
- reconcile reservation, actual creation, Job membership, ActiveProcesses/TotalProcesses and confirmed exit without double counting;
- cumulative created count never decreases after reap; active count decreases only after confirmed exit;
- distinguish controller, direct child, Python process, worker thread and tool-observed intake.
C. If ResourceGateV2 relies on nested bundles/arbitrary descendants, do not claim compatibility. Keep those paths blocked behind explicit UNSUPPORTED_DESCENDANT_TOPOLOGY until separately designed and authorized.
D. Keep existing synthetic tests and add adapter-level synthetic tests. No broad refactor, no generic process-tree claims, no scientific source edits.
E. One bounded real Windows integration smoke test may run only after static and synthetic checks pass. Fresh isolated Job, dummy executable cannot spawn children. At most two direct suspended children total: one accepted/resumed child and one rejected-at-assignment probe that never resumes. Unexpected descendant, unknown PID/parent, Job/lease mismatch or STOP failure => immediate E2 STOP and no further tests.
F. Do not re-run old failed scenarios for coverage. Reuse V3 accepted evidence read-only and distinguish it from new integration evidence.

## Budget

- Engineering processes and all descendants <=192.
- Python/focused pytest starts <=48.
- Simultaneously active Python processes <=8.
- Active worker threads across all Python processes <=64.
- Active engineering time <=3 hours.
- Repair/validation batches <=8.
- New non-Git bytes <=512 MiB.
- No Git fetch/push, network publication or review cleanup. No prior-budget carry-forward.
- Enforce every limit before launch/activation. ActiveProcessLimit is concurrency only, not lifetime cumulative creation control.
- If OS evidence cannot be captured/reconciled, label UNKNOWN and fail closed.

## Acceptance gates

P0: task identity and protected paths authenticated; fresh scratch verified; accepted V3 and old failures unchanged.

P1 static/adapter: no bypass for supported single-child topology; nested/arbitrary descendant paths explicitly blocked; lease single-use; assignment/identity/resume failure latches STOP before next backend invocation; counters monotonic and domain-separated.

P2 synthetic: adapter denial, lease replay, wrong executable hash, wrong task/run/domain, assignment failure, resume failure, child exit, checkpoint failure and STOP propagation. Exact denominator/results. Synthetic is not OS proof.

P3 real Windows integration: one direct child assigned and identity-checked before resume; second suspended probe denied by Job admission and never resumed; no unexpected descendants; raw Job/process evidence reconciles with reservations/exits; all children/controller reaped at seal.

P4 local delivery: report, manifest, sanitized evidence ZIP and final receipt; reproducible member inventory and hashes; no network publishing. Do not claim Astra independently checked OS facts until originals are uploaded.

## Terminal

PASS means only the existing executor's supported single-direct-child path is integrated and tested. It does not enable nested/arbitrary descendants or authorize science.

Any P0/P1/P2/P3 failure, unknown real PID, unaccounted child, cap violation or broken STOP => FAIL_CLOSED / STOP. Do not continue after E2 or retry in same stop chain.

Prior TEMP remains FAIL_CLOSED and not resumable. Current task science calls=0; formal V010 unchanged; V011 NOT_STARTED; model_activation=False; REAL_GE=False; Results=FALSE; FULL_RUNNER_IO_CLOSURE=BLOCKED. Final stop: WAIT_ASTRA_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_REVIEW.
