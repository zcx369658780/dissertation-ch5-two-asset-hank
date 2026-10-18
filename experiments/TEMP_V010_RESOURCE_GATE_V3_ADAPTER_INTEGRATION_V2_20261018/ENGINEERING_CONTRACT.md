# TEMP V010 Resource Gate V3 Adapter Integration — Immutable Contract Task

TASK_ID=TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V2_20261018
STATUS=ISSUED_NOT_STARTED
SCOPE=ENGINEERING_ONLY / NO_SCIENCE / NO_HA

## 1. Immutable identity rule

This file is the fixed read-only contract. Do not rewrite, template-render, regex-replace, normalize or reassemble its body for identity validation. Historical V3 references below are immutable provenance, not fields to replace:
- accepted V3 task commit: 09e073ee69b34fc22dd5448a6a39156a0cd11775
- accepted V3 contract blob: f323a5855600b5dc4ef715a73533421dc09d1e99
- accepted V3 run_id: 49b82ce3c2554dbeb0aa2fb6b0b2f067
- accepted V3 result: PASS_BOUNDED_NATIVE_SINGLE_CHILD_LOCAL

The current task issue commit/blob/SHA/length are held in CURRENT.md and TASK_CURRENT.md only; they are not embedded in this body. Git Blob SHA and file SHA256 are different identities and must never be substituted for one another.

## 2. Startup protocol — read-only until identity passes

1. Read current governance HEAD, CURRENT.md and TASK_CURRENT.md.
2. Read this contract directly from its fixed issue commit and path; preserve the connector-returned content unchanged. Do not create a transformed verification text.
3. Compare task ID, fixed path, issue commit, contract Blob, byte length, SHA256 and scope fields against CURRENT/TASK_CURRENT. Mark evidence level accurately: CONNECTOR_TEXT_VERIFIED if only decoded connector text is available; RAW_GIT_OBJECT_VERIFIED only when raw Git object bytes are actually verified.
4. Any mismatch means TASK_RAW_IDENTITY / STOP. Report expected vs actual field and source. Do not correct the contract, replace historical hashes, change branch/path, or retry via a different path. No files or scratch before identity passes.
5. Only after identity passes, run existing BOOTSTRAP 0/1/2. If protected roots or independent scratch cannot be authenticated, stop read-only without trying another path.

## 3. Accepted baseline and limits

Accepted V3 run: 49b82ce3c2554dbeb0aa2fb6b0b2f067. It validates one direct child created suspended, assigned to a Job, identity-checked before resume, plus one second suspended direct child rejected at Job assignment and never resumed. It does not prove CreateProcess-before-creation denial, arbitrary descendant control, lifetime cumulative process limits or full Runner I/O closure. The standalone original final receipt was not separately supplied to Astra.

Prior resource repair run 977d18ebe6e14a91bb049924cae715e4 remains FAIL_CLOSED_UNRESERVED_REAL_DESCENDANT. Prior TEMP price tuning remains FAIL_CLOSED and not resumable. Never rewrite historical results or reuse closed budgets.

## 4. Objective

Integrate the accepted bounded SingleChildGateV3 primitive into the existing resource-gate executor via a narrow adapter, then verify only the integrated bounded execution path. Preserve fail-closed behavior. No HA/HJB/KFE/selector/root solver, TEMP price tuning, GE, IRF or any scientific/model execution. Formal V010 unchanged; V011 NOT_STARTED; model_activation=False; REAL_GE=False; Results=FALSE; FULL_RUNNER_IO_CLOSURE=BLOCKED.

## 5. Scope

A. Read-only inspect V3 implementation and ResourceGateV2 interface; document the adapter boundary before edits.
B. Implement only the single-direct-child topology:
- each launch uses a single-use lease bound to task/run/gate/domain, executable identity/hash and one concrete launch;
- create child suspended, assign to intended Job, verify membership/identity, then resume;
- assignment/identity/resume failure records exact error and latches STOP before any next backend invocation;
- reconcile reservation, creation, Job membership, ActiveProcesses/TotalProcesses and confirmed exit without double count;
- cumulative created count never decreases after reap; active count decreases only after confirmed exit;
- separate controller, direct child, Python, worker thread and tool-observed intake.
C. Nested bundle and arbitrary descendant topologies must be blocked explicitly as UNSUPPORTED_DESCENDANT_TOPOLOGY. Do not claim compatibility.
D. Keep synthetic tests distinct from real OS evidence. No broad refactor and no scientific source edits.
E. At most one real Windows integration smoke after static and synthetic checks pass: one direct dummy child accepted/resumed; second suspended probe rejected at Job admission and never resumed. Dummy must not spawn descendants. Any unknown PID/parent, unexpected descendant, Job/lease mismatch or STOP failure triggers immediate E2 STOP with no further tests.
F. Reuse prior V3 evidence read-only; distinguish it from new integration evidence.

## 6. Budget

Engineering processes and all descendants <=192; Python/focused pytest starts <=48; simultaneously active Python <=8; active worker threads across Python processes <=64; active engineering time <=3 hours; batches <=8; new non-Git bytes <=512 MiB. No Git fetch/push, no network publication, no review cleanup. No budget carry-forward. Enforce limits before launch/activation. ActiveProcessLimit is concurrency control, not lifetime cumulative creation control.

## 7. Acceptance

P0 identity and protection: fixed raw contract read unchanged; metadata matches; BOOTSTRAP and scratch identity pass; old V3 and failures unchanged.
P1 static/adapter: no bypass for supported topology; nested/arbitrary descendants blocked; lease single-use; assignment/identity/resume failure stops before next backend call; counters monotonic and domain-separated.
P2 synthetic: adapter denial, lease replay, wrong hash/task/run/domain, assignment failure, resume failure, child exit, checkpoint failure and STOP propagation. Exact denominator; synthetic is not OS proof.
P3 real Windows: one direct child assigned and identity-checked before resume; second suspended probe rejected by Job admission and never resumed; no descendants; raw Job/process evidence reconciles; all children/controller reaped.
P4 delivery: local result, manifest, sanitized ZIP and final receipt; reproducible inventory/hashes; no network publishing. Do not claim Astra independently verified OS facts until original evidence is uploaded.

## 8. Terminal

Any P0/P1/P2/P3 failure, unknown real PID, unaccounted child, cap violation or broken STOP => FAIL_CLOSED / STOP. Do not continue after E2 or retry in the same stop chain. PASS means only the supported single-direct-child path is integrated and tested; it does not enable arbitrary descendants or authorize science.

Final state: prior TEMP remains FAIL_CLOSED and not resumable; current science calls=0; formal V010 unchanged; V011 NOT_STARTED; model_activation=False; REAL_GE=False; Results=FALSE; FULL_RUNNER_IO_CLOSURE=BLOCKED. Final stop: WAIT_ASTRA_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_REVIEW.
