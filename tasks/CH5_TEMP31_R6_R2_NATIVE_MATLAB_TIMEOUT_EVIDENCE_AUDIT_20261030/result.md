# TEMP31 R6-R2: bounded original-evidence timeout audit

TASK_ID=CH5_TEMP31_R6_R2_NATIVE_MATLAB_TIMEOUT_EVIDENCE_AUDIT_20261030
AUDIT_STATUS=COMPLETED_BOUNDED
ROOT_CAUSE_CERTIFICATION=NOT_COMPLETED
ROOT_CAUSE=UNKNOWN
NUMERIC_REVIEW=NOT_TESTED_BY_DESIGN
FINAL_TERMINAL_AFTER_LEGAL_DELIVERY=STOP__R6_R2_ROOT_CAUSE_UNKNOWN_EVIDENCE_BOUNDED

## Findings

The current auditor independently read and recomputed original bytes/SHA256/Git Blob: R6=19 VERIFIED of20 declared, R6-R1=25 VERIFIED of26 declared. Each manifest has one directory-external source not among the two R6-R1 source paths explicitly permitted by this contract. Those two items are MISSING_OR_OUT_OF_SCOPE, never opened; they are not missing-file or hash failures. In-scope missing/inaccessible=0; hash mismatch=0. Complete20/20 and26/26 independent authentication remains REVIEW_PENDING_IO. This does not remove the required timeout controller, MATLAB recipe, native receipt, Job gate or raw stdout/stderr from the audit. The detailed per-item table is original_manifest_readback.json. Forty-six unique permitted originals, including both manifests, were rechecked unchanged after auditing. The old STOP values were not rewritten.

Governance HEAD strictly334b7206df54bd5d1985201fa73af15e75e86ba3; sole parent9d73fb5946f7a4c740e45b60da8d2b0c9b21791f; treeb42f771cbf8ecdabda3d53921a933d1ae973df8c; only addition is this contract, Blob2ffeee35358e528e06a5a3d126913f13df559a00. New remote candidate exact-ref initially404. The two original contracts, R5 review, and four frozen Python sources were obtained at their proper fixed commits and their byte-derived Blobs verified. No scientific module was imported. Fixed scientific base56447829ce0e6c3c85552c53c351b26a2452a4bd, tree7b7cb29dd5b37be92561e7f1bc688c0d29789732.

## A-H diagnostic answers

A. Source lines175-177 start the30-second deadline only after native.start returns. That function has already resumed the primary thread and closed its handle. Waiting polls the native_probe_ready file and GetExitCodeProcess with25ms sleeps, not stdout. No old per-event timestamp, absolute wall-clock start, timezone or underlying monotonic counter was saved. The total30.18700000003446 seconds starts earlier, before configuration/AST/binary hashing/API setup, and ends after cleanup/log hashing. It is not a measured duration of MATLAB initialization. The exact amount of initialization progress/time inside that window is UNKNOWN.

B. The verified code directly supplies its configured executable to CreateProcessW and builds flags -nojvm -nodesktop -nosplash -singleCompThread -batch run(ISOLATED_RECIPE). No shell invocation or -logfile is in that argv. Actual private config/environment values were hash-checked only, not semantically opened. Old source_identity records R2022b9.13.0.2049777 and executable235648 bytes/SHA2564d251e680b8409d76d0524a1eb716de3c9e747386d3101e10f6ce1405ad1a59d; it is a static executor identity receipt, not a new process-image or native version observation. Internal launcher/shim behavior is UNRESOLVED.

C. Source/receipt ordering supports CreateProcess suspended, successful Job assignment, limit/membership query, then ResumeThread previous count1. The recorded pre-resume commit limits are1073741824 bytes for process and Job, active-process limit1, no breakaway, kill-on-close. These historical API results remain EXECUTOR_RECEIPT_ONLY even though this auditor independently authenticated their files and source consistency. Peak966209536 bytes was recorded after forced termination/reaping. No limit-violation notification, denied allocation event, denied child-create record or completion-port log exists here. The below-cap peak neither proves nor rules out limit-induced failure.

D. Actual original stdout and stderr are each0 bytes, matching their separate receipt identities. No independent logfile or license/configuration/startup diagnostic was supplied. LICENSE_CAUSE=UNKNOWN. Empty output does not establish no MATLAB activity.

E. No pipe-read/communicate call is involved in the wait loop, so a pipe-fill deadlock is not supported by this code. The stdio files and inherited handle assignments are present in code and successful CreateFile/CreateProcess are attested. Whether MATLAB used/flushed those handles is not directly observed. Missing early phase markers and no independent logfile weaken visibility. Static risk: snapshot enumeration does not distinguish Process32First/Next failure from normal end; self.cleaned is set before cleanup completes; broad inheritable handles lack an explicit handle allow-list. None is established as the30-second timeout cause.

F. The receipt and code support owned-Job termination after timeout, wait status0, final forced exit0xE0000001, successful handle closure and cleanup_errors=[]. That forced code is not a natural MATLAB diagnostic code; prior numeric GetExitCodeProcess values were not logged. Empty old PID snapshots and orphan=false are executor observations, with the enumeration caveat above. R2 did not scan or terminate any OS process. Owned-handle wait/exit evidence is stronger than an empty global list alone.

G. The old probe object is empty and stage is MATLAB_NATIVE_PROBE. The code grants the synthetic permission marker only after a valid native marker/version check; recipe post assembly follows that permission. Synthetic assembly remains NOT_TESTED on bounded receipt-plus-static-code evidence. No new marker search, synthetic calculation or matrix comparison was performed.

H. ROOT_CAUSE=UNKNOWN. There is no direct evidence discriminating slow initialization, resource-denied work, licensing/configuration, output visibility or failure before marker creation. No new run was authorized or used to fill those gaps.

## Evidence and execution

controller_code_evidence.md contains selected actual source snippets with original line numbers and original/public fragment identities. startup_event_timeline.json preserves recorded event-array order without inventing timestamps. Historical API outcomes, verified current bytes, static control-flow facts and untested hypotheses are classified separately.

The standard-library auditor ran once, exit0, about0.238 seconds. New MATLAB processes/runtime commands/Job experiments/OS process scans/model calls/NPZ reads/old writes=0. The executed auditor source hash is in audit_execution_receipt.json. Before publication two Python string literal spellings were made scanner-safe using equivalent octal escapes; a reversible token-hex map and equal AST hash bind actual executed and public source versions. The public version was not reexecuted and is not misrepresented as an extra run. No old controller, recipe or receipt changed.

## Delivery, limits and next action

The original mandatory privacy predicate is unchanged and is evaluated over every exact proposed public file including manifest and, separately, the seal. Detailed fixed-source responses, operational config, original executed auditor preimage, and a redundant JSON-escaped snippet working ledger stay LOCAL_ONLY. The public Markdown excerpts retain sufficient actual control flow and fragment hash identities.

The candidate is built solely from the fixed scientific parent with one payload and a seal adding only DELIVERY_FINAL_RECEIPT.json. Actual candidate commit/parent/tree, privacy results and remote bytes/Blob/SHA checks are bound in that receipt and an external LOCAL_ONLY final readback; no third commit, Issue/PR/merge/cleanup or successor.

NOT_COMPLETED: root-cause confirmation, actual initialization state/time, limit/license event attribution, full20/20 and26/26 scope authentication, native recipe/elementwise parity, original policy/runtime equivalence and scientific stationarity. Next Owner options are proposals only; none is executed.

P3=BLOCKED
FORMAL_SOURCE_FREEZE=FALSE
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE
FULL_RUNNER_IO_CLOSURE=BLOCKED
STRICT_KFE_STATIONARITY=FALSE_INHERITED_R3_R4_R5
ORIGINAL_R5_BATCH_FAILURE_ROOT_CAUSE=UNKNOWN
OLD_R6_AND_R6_R1_STOPS=IMMUTABLE
AUTO_NEXT=FALSE
