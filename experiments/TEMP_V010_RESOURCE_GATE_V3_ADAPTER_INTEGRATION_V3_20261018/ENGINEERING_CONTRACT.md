# TEMP V010 Resource Gate V3 Adapter Integration — Protected-Path Boundary Task

TASK_ID=TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_20261018
STATUS=ISSUED_NOT_STARTED
SCOPE=ENGINEERING_ONLY / NO_SCIENCE / NO_HA

## 1. Immutable contract and authority

This contract is a read-only original. Never rewrite, template, normalize, regex-replace or reconstruct its body for identity checking. Current task issue commit/blob/SHA/length live only in CURRENT.md and TASK_CURRENT.md; historical V3 provenance below is immutable.

Accepted V3 baseline: run_id 49b82ce3c2554dbeb0aa2fb6b0b2f067; task commit 09e073ee69b34fc22dd5448a6a39156a0cd11775; contract blob f323a5855600b5dc4ef715a73533421dc09d1e99; result PASS_BOUNDED_NATIVE_SINGLE_CHILD_LOCAL. Scope only one direct child assigned to Job and verified before resume, plus a suspended second direct child rejected at Job assignment and never resumed. No arbitrary descendants, lifetime cumulative process control or full Runner I/O claim.

Prior adapter attempts are closed and not resumable:
- TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_20261018: FAIL_CLOSED_TASK_RAW_IDENTITY / STOP, no writes/tests.
- TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V2_20261018: FAIL_CLOSED_PROTECTED_PATH_IDENTITY / STOP, no writes/tests; PATH_ALIAS occurred in a recursively enumerated dependency file, but final path and relation to protected roots were not established.
Do not rewrite or supersede their historical evidence.

## 2. Objective

Apply V1.5 immutable identity rules and V1.6 protected-path boundary rules, then integrate accepted SingleChildGateV3 into the existing ResourceGate executor via a narrow adapter. This is engineering-only. No HA/HJB/KFE/selector/root solver, TEMP price tuning, GE, IRF or any scientific/model execution. Formal V010 unchanged; V011 NOT_STARTED; model_activation=False; REAL_GE=False; Results=FALSE; FULL_RUNNER_IO_CLOSURE=BLOCKED.

## 3. Startup protocol

1. Read current governance HEAD, CURRENT.md, TASK_CURRENT.md, DOC_INDEX_CURRENT.md, V1.4, V1.5, V1.6 and this contract directly from the fixed issue commit/path. Preserve all returned content unchanged.
2. Compare task ID/path/issue commit/blob/length/SHA/scope fields. Blob SHA and file SHA256 are distinct. If only decoded connector text is available, label CONNECTOR_TEXT_VERIFIED. Any mismatch => TASK_RAW_IDENTITY STOP, no files, no alternate path.
3. BOOTSTRAP 0 must check a finite explicit list of protected roots and the intended scratch parent/target; do not recursively enumerate every descendant in evidence/data roots to infer protection identity.
4. Check only root identity for each protected root. Inspect path components and reparse points on the actual target and its parent chain. If recursive enumeration notices a PATH_ALIAS in an unrelated dependency file (for example node_modules), report it as PATH_ALIAS_UNRELATED_ENUMERATION and exclude it from target resolution only if it is demonstrably not the intended target, not an ancestor, and not within a protected root whose identity is being certified.
5. For each relevant alias, record original path, failed component, available canonical/final path, reparse type/tag, API/error and whether target is inside/outside/unknown relative to protected roots. If API cannot resolve it, mark PATH_ALIAS_TARGET_UNKNOWN. If its relevance to target or protected boundary cannot be disproved, STOP. Never disable alias checks, use string-prefix containment, or choose another path to evade a failure.
6. No scratch/log/script/test artifact before identity and BOOTSTRAP 0 pass. After P0 passes, follow BOOTSTRAP 1 create exclusive scratch and revalidate directory identity; then BOOTSTRAP 2 may create the first artifact.

## 4. Integration scope

A. Read-only inspect V3 implementation and ResourceGateV2 interface; document narrow adapter boundary before editing.
B. Integrate only the single-direct-child topology:
- single-use lease binds task/run/gate/domain, executable identity/hash and one launch;
- child created suspended, assigned to intended Job, identity/membership verified, then resumed;
- assignment/identity/resume failure preserves exact error and latches STOP before any next backend call;
- reconcile reservation, actual creation, Job membership, ActiveProcesses/TotalProcesses and confirmed exit without double count;
- cumulative created count never decreases after reap; active count decreases only after confirmed exit;
- distinguish controller, child, Python, threads and tool-observed intake.
C. Nested bundle and arbitrary descendant topology must be blocked as UNSUPPORTED_DESCENDANT_TOPOLOGY.
D. Run static checks and adapter synthetic tests. Only after all pass, at most one real Windows integration smoke: one accepted/resumed direct dummy child and one second suspended probe denied by Job admission and never resumed. Dummy cannot spawn descendants.
E. Any unknown PID/parent, unexpected descendant, Job/lease mismatch, unresolved relevant alias, broken checkpoint or STOP failure => immediate E2 STOP, no subsequent tests or controller restart.
F. Reuse V3 accepted evidence read-only; separate reused baseline from new integration evidence.

## 5. Budget

Engineering processes and descendants <=192; Python/focused pytest starts <=48; simultaneously active Python <=8; active worker threads across Python <=64; active engineering time <=3 hours; batches <=8; new non-Git bytes <=512 MiB. No Git fetch/push, network publication or review cleanup. No prior budget carry-forward. All limits enforced before launch/activation. ActiveProcessLimit is concurrency only, not lifetime cumulative process control.

## 6. Acceptance

P0: identity matches and protected-root/target boundaries are classified correctly without recursive unrelated-file false positives; fresh scratch and BOOTSTRAP 0/1/2 pass; old evidence unchanged.
P1: static adapter paths show no bypass for supported topology; nested/descendant topology explicitly blocked; single-use lease and STOP-before-next-call verified.
P2: synthetic adapter tests cover replay, wrong executable hash/task/run/domain, assignment/resume failure, exit, checkpoint failure and STOP; exact denominator reported, no synthetic claim presented as OS proof.
P3: one real bounded Windows integration smoke; no unexpected descendants; pre/post Job/process evidence reconciles with reservations and exits; all processes reaped.
P4: local result, manifest, sanitized ZIP, final receipt, reproducible member hashes; no network publish.

Any P0/P1/P2/P3 failure or UNKNOWN relevant path/identity/counter => FAIL_CLOSED / STOP. Do not retry within same stop chain. PASS means only supported single-direct-child executor integration is validated; no science authorization.

Final state: old TEMP tuning remains FAIL_CLOSED and not resumable; both prior adapter attempts remain closed; science calls=0; formal V010 unchanged; V011 NOT_STARTED; model_activation=False; REAL_GE=False; Results=FALSE; FULL_RUNNER_IO_CLOSURE=BLOCKED. Final stop: WAIT_ASTRA_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_REVIEW.
