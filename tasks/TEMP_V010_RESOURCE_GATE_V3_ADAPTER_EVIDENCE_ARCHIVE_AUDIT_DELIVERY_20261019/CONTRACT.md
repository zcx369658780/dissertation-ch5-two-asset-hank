# TEMP_V010_RESOURCE_GATE_V3_ADAPTER_EVIDENCE_ARCHIVE_AUDIT_DELIVERY_20261019

Status: ISSUED / NOT STARTED
Scope: BOUNDED_ENGINEERING_AND_DELIVERY_ONLY / ZERO_SCIENCE
Owner: Owner retains scientific and irreversible-decision authority.
Executor: local Codex.
Reviewer/orchestrator: Astra.

## 1. Purpose and exact prior state

This is a NEW task to complete the evidence chain after:
- local engineering result PASS_BOUNDED_ADAPTER_INTEGRATION_LOCAL, run_id 33f2b49ddc274e868956f6480d5f3a3a;
- failed earlier publication attempt run_id 447f9775e1b5482f9e3add9344742017, where path classification stopped at 17/491 members and full archive safety remained UNKNOWN;
- accepted bounded synthetic classifier evidence run_id 06ed068da2d948649f463889051ea157;
- completed delivery/acceptance/cleanup of the classifier's own 44-member evidence package.

This task does not reopen or overwrite either old delivery attempt, does not alter their receipts, and does not claim the synthetic classifier has already passed on the 491-member archive.

## 2. Immutable source roots and identity anchors

Source root:
D:\ProjectTemp\ch5_temp_resource_gate_v3_adapter_integration_v3_20261018_01\delivery

Read-only allowed source files only:
- result.md
- manifest.json
- evidence_sanitized.zip
- FINAL_RECEIPT.json

No recursive discovery outside these four named files. No modification/deletion/rename of source files.

Hard anchors from preserved prior evidence:
- ZIP bytes: 332933
- ZIP SHA256: fc7a846d09758590dbd268b430ffd8c2c47aa0b2c63e307b510586f2443fafa0
- ZIP reported member count: 491
- FINAL_RECEIPT bytes: 9339
- FINAL_RECEIPT SHA256: 14ca468c0c9b4339cea7a8bc91578fc899b88a4be7a9c96d4d7d552945d599f5

First verify these two hard anchors byte-for-byte. Parse FINAL_RECEIPT and manifest as structured data; derive expected identities for result.md and manifest.json from cross-referenced fields, not manually transcribed values. Require agreement among receipt, manifest, actual local bytes, lengths and SHA256. If a source index is present, use it as a cross-check, not as replacement for hard anchors.

If either hard anchor fails, expected identities conflict, or source root is not the exact specified root, STOP before reading ZIP members or creating artifacts. Preserve the original error; do not try alternate folders.

## 3. Scientific and model prohibitions

SCIENCE_BUDGET=0
MODEL_RUNNER_BUDGET=0
REAL_GE_BUDGET=0
FORMAL_V010_WRITES=0
V011_START=PROHIBITED
HA/HJB/KFE/selector/root/GE/IRF calls=0

Do not invoke the HA black box or any economic-model solver. Do not modify V010 equations, selectors, MATLAB-faithful HA code, or scientific contracts. Do not treat this engineering task as evidence of scientific convergence. Formal model_activation=False; REAL_GE=False; Results=FALSE; V011=NOT_STARTED; FULL_RUNNER_IO_CLOSURE=BLOCKED remain invariant.

## 4. Engineering objective

A. Reconcile and preserve the four source files using byte hashes and a structured source ledger.

B. Audit the 491-member ZIP without executing or importing archive content:
- validate central directory, entry count, CRC/length, compression method and total expansion limits before extracting;
- reject absolute paths, drive-qualified names, UNC names, traversal components, symlinks, duplicate paths and case-fold collisions;
- enforce per-member expanded size <= 16 MiB, total expanded size <= 64 MiB, compression ratio <= 100:1; if the original ZIP exceeds these bounds, STOP without extraction and report the exact entry;
- extract only to a new authorized private scratch after all names validate; never extract over an existing directory;
- never execute binaries, scripts, tests or commands from the ZIP.

C. Use the accepted V1.9 classifier implementation as an inspection helper only after confirming exact source SHA256 from the accepted classifier evidence. Do not compile it or rerun its 91-sample suite. Running its existing read-only byte-analysis entry point on archive member bytes is authorized only for this task and must be counted as ENGINEERING, not SCIENCE. If it cannot be loaded without compilation/import side effects or exact source identity cannot be confirmed, STOP classifier application; preserve any already completed safe static inventory.

D. Classify every member by actual content type and review text-like members plus all candidate findings. Distinguish URI, path candidate, JSON escaped representation, credential candidate, ordinary text and UNKNOWN. UNKNOWN, unresolved content, executable/binary payload, or credible secret/private data blocks publication of the affected raw member. Synthetic labels are not proof that real data is safe.

E. Produce a safe review package preserving original evidence identity separately from any sanitized derivative. Do not change engineering outcomes, test assertions, source code, fixtures or original error conclusions. If safe sanitization cannot be proven, do not publish affected members or a ZIP containing them; deliver a redacted audit report only, with delivery state explicitly blocked.

## 5. Scratch and protected boundaries

Create only one new private scratch:
D:\ProjectTemp\ch5_temp_resource_gate_v3_adapter_archive_audit_20261019_01

This path is authorized as a new target only if it is absent and finite protected-root/path-chain checks pass. Bootstrap 0/1/2 must run before writing. Do not reuse old scratch, source root, protected worktree/index, backups, old runner directories or any path not listed here. Do not create _review_tmp locally.

## 6. Independent budgets and resource gates

ENGINEERING:
- maximum elapsed time 60 minutes;
- at most 4 batches;
- at most 64 total accounted processes including child processes and observed tool starts;
- Python starts <= 8; concurrent Python <= 2;
- worker threads <= 8;
- maximum new non-Git bytes <= 128 MiB;
- archive members inspected <= 491, only after anchor verification and ZIP preflight.

DELIVERY:
- maximum elapsed time 30 minutes, independent of engineering;
- at most 3 delivery batches and 2 E1 repair batches;
- fake-bare publisher self-test <= 1;
- SSH preflight <= 1;
- fetch <= 2;
- push attempts <= 1 and successful publication <= 1;
- read-only GET <= 32;
- maximum published ZIP <= 16 MiB and expanded member bytes <= 64 MiB.

Budgets are creation-time hard gates. Count wrapper/tool starts separately from kernel-confirmed processes; never silently reconcile UNKNOWN as zero. Python threads may use the stated allowance, but thread allowance does not increase process budgets. Any resource mismatch, unreserved process, protected-path uncertainty, source identity mismatch, unexpected network, STOP propagation failure or budget overrun is E2 STOP. Preserve first error; no alternate path or retry outside explicit E1 budget.

## 7. Mandatory GitHub delivery and cleanup

Delivery is explicitly authorized after local engineering inventory; do not apply execution-time no-network to the independent delivery phase.

REVIEW_BRANCH=review/ch5-temp-resource-gate-v3-adapter-archive-audit-20261019
TEMP_PATH=_review_tmp/ch5/temp-resource-gate-v3-adapter-archive-audit-20261019/
FIXED_PARENT=ISSUE_COMMIT_TO_BE_FROZEN_IN_ISSUE_MANIFEST
REMOTE_ALLOWLIST=result.md;manifest.json;evidence_sanitized.zip

Before issuing, the planner must replace FIXED_PARENT with a concrete commit SHA and freeze exact file byte/size ceilings in ISSUE_MANIFEST. If any field remains a placeholder, do not execute.

Codex must generate result.md, manifest.json and evidence_sanitized.zip automatically. ZIP must contain the required safe copies of the adapter evidence, content inventory, classifier findings, per-member disposition and all relevant error/resource/identity evidence. The package may not omit unresolved items silently. Source FINAL_RECEIPT is included as a reviewed sanitized derivative or retained privately with an explicit public derivative and source SHA/length mapping.

Before real publish, run one fake-bare end-to-end self-test using the same publisher, including binary ZIP push/readback and cleanup. Then perform one ordinary non-force publication, with existing SSH Key/443 and project-external isolated bare object store; do not create _review_tmp in protected local worktree/index, add credentials, change global/system Git configuration or force-push.

Read back exact branch/ref, candidate commit/tree/sole parent, the three remote files and actual ZIP bytes. Verify lengths and SHA256; compare every ZIP member against manifest, including size and SHA256. Final external receipt must be delivered by exact Base64 + byte length + SHA256, plus the external controller completion receipt. Do not claim success from URLs or Git blob IDs alone.

Astra is the cleanup owner. After Astra completes review, permanently archives the verdict and reads it back, Astra must delete only the three allowlisted files from the review branch current tree in one ordinary non-force commit and read back their absence. Do not delete before Astra review. Git history remains; current-tree deletion is not historical erasure.

If source identity or safety blocks publication, do not publish the ZIP. Publish only a safe blocked-result package if that package itself passes content review, or stop with DELIVERY_BLOCKED if even that is unsafe. Never weaken gates to force success.

## 8. Final stop and deliverables

Expected stop: WAIT_ASTRA_TEMP_V3_ADAPTER_ARCHIVE_AUDIT_REVIEW.

Return:
- concise result.md;
- manifest with source RAW identity versus sanitized derivative identity;
- safe ZIP if and only if all publication gates pass;
- exact source reconciliation and per-member inventory;
- classifier version/source SHA, invocation count and per-member decisions;
- FIRST and FINAL_PROTECTION;
- resource ledger, all first errors and repair links;
- external DELIVERY_FINAL_RECEIPT exact Base64, byte length and SHA256;
- external controller completion receipt.

No next task may start automatically. Keep the original local PASS_BOUNDED_ADAPTER_INTEGRATION_LOCAL as an engineering report only, not an Astra acceptance until its evidence is reviewed. Preserve all prior FAIL_CLOSED records unchanged.
