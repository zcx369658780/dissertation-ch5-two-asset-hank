# TEMP_V010_RESOURCE_GATE_V3_SAFE_BLOCKED_REPORT_DELIVERY_20261019

STATUS=ISSUED_NOT_STARTED
SCOPE=SAFE_BLOCKED_REPORT_ONLY / DELIVERY_ONLY / ZERO_SCIENCE / NO_ARCHIVE_MEMBER_READ

## 1. Purpose and predecessor
This is a new task authorized by Owner to publish only a safe blocked-report package after the previous 491-member archive audit delivery timed out. It does NOT retry or resume the prior task and does NOT publish the original 491-member ZIP, any raw ZIP member, the previous candidate ZIP, or the local candidate commit.

Predecessor:
- task: TEMP_V010_RESOURCE_GATE_V3_ADAPTER_EVIDENCE_ARCHIVE_AUDIT_DELIVERY_20261019
- run_id: 44826358dcbd4de096926294160f677d
- terminal: FAIL_CLOSED / DELIVERY_CHILD_TIMEOUT_STOP
- local candidate commit: d3a2aeb6174cd14bbbef8b0a01170e9c8c9b9b13 (not found on GitHub; never claim it was published)
- remote review ref was independently checked and returned NOT_FOUND.
The predecessor's original receipts and candidate metadata remain immutable.

## 2. Exact source root and allowlist
Read only these three text sources under:
D:\ProjectTemp\ch5_temp_resource_gate_v3_adapter_integration_v3_20261018_01\delivery
- result.md — expected 6196 bytes, SHA256 457e5647be449721d9138cbab40ae4d4c788370d889229f271d36c2cb0eabaf6
- manifest.json — expected 239695 bytes, SHA256 1086f3b04166d406fdb4a87b684f06fb37dd34ff733728510003dfff0d635bbd
- FINAL_RECEIPT.json — expected 9339 bytes, SHA256 14ca468c0c9b4339cea7a8bc91578fc899b88a4be7a9c96d4d7d552945d599f5

These expected values are frozen here. Validate each SHA string is exactly 64 hex characters. Read the actual source bytes first, compute byte length and SHA256, then compare. Do not read/open/hash/extract the original evidence_sanitized.zip in this task; its identity is known but this task is deliberately report-only. Do not recursively search other folders or switch to an alternate root. If any source text is missing or fails identity, stop and return DELIVERY_BLOCKED; do not publish.

## 3. What to publish
Generate a NEW safe blocked-report package from the three validated text sources only. Do not copy original source text wholesale to public outputs. Parse the manifest and final receipt as structured data and select only the following fields for a sanitized summary:
- task/run IDs, terminal status, source archive byte count/hash/member count;
- audit counts and dispositions reported by Codex;
- classifier invocation/source-identity decision;
- delivery timeout, stdout/stderr lengths, push-attempt count, readback status;
- resource totals and known UNKNOWNs;
- explicit warning that all 491 raw members remain withheld and archive safety/content review is not Astra-independently accepted.
Exclude local absolute paths, usernames, credentials, argv/env, Git object database paths, internal machine/process topology not needed for audit, and any member contents or raw filenames beyond the single already reported malformed-JSONL relative path if needed to explain the block. Do not include the original ZIP or any of its members in the new ZIP.

ZIP payload must contain only newly generated sanitized documents:
- blocked_audit_summary.json
- blocked_audit_summary.md
- source_identity_ledger.json
No executable code, no original raw member, no nested archive. If sanitization cannot be confidently completed, do not publish the ZIP; return DELIVERY_BLOCKED.

## 4. Fixed remote identity
Review branch: review/ch5-temp-v3-safe-blocked-report-20261019
Fixed parent: bb85659984702e2229609cc3c979e8824cd89902
Remote temporary directory: _review_tmp/ch5/temp-v3-safe-blocked-report-20261019/
Exact remote allowlist:
- result.md
- manifest.json
- evidence_sanitized.zip

Only one successful ordinary non-force publication is allowed. Candidate must have exactly one parent equal to the fixed parent. Do not alter main/governance/model branches as part of publication. Never create _review_tmp in a local worktree/index.

## 5. Separate budgets
Engineering/package preparation:
- maximum 20 minutes;
- at most 2 batches;
- <=24 total accounted processes including observed tool starts;
- Python starts <=4, concurrent Python <=2, threads <=8;
- new non-Git bytes <=16 MiB;
- no archive-member reads and no classifier invocation.
Delivery:
- maximum 20 minutes;
- at most 2 batches;
- fake-bare publisher self-test <=1;
- SSH preflight <=1;
- GitHub reads/fetches <=2;
- push attempts <=1, successful publication <=1;
- read-only GET <=24.
Every cap is a creation-time hard gate. Preserve first errors. No extra fetch/push, no alternate path, no force push, no PAT/new credentials, no global/system Git configuration changes, no shared object store or alternates. Use existing SSH key/443 and an exclusive project-external bare object store. If fixed parent objects cannot be proven available without unauthorized fetch, stop.

## 6. Mandatory publish, readback and cleanup
Delivery network is explicitly authorized and separate from local package preparation. After source identities, sanitization and fake-bare preflight pass, Codex must automatically publish result.md, manifest.json and evidence_sanitized.zip to the exact remote path. Do not leave delivery as a local-only result or ask Owner to upload manually.

Read back exact branch ref, candidate commit/tree/sole parent, three remote file blobs and actual ZIP bytes. Independently compute SHA256/length and inspect all ZIP members against manifest, including CRC, size and SHA256. Git blob IDs or URLs alone are insufficient. Return DELIVERY_FINAL_RECEIPT exact Base64, byte length and SHA256 plus the external controller-completion receipt. If remote outcome cannot be read back, state UNKNOWN and STOP; do not retry the consumed push budget.

Astra is cleanup owner. Only after Astra has reviewed the remote bytes, permanently archived the verdict and read the archive back may Astra delete only the three allowlisted files from the review branch current tree in one ordinary non-force commit, then read back the branch and confirm all three paths absent. If no remote candidate was confirmed, cleanup is NOT_APPLICABLE_NO_CANDIDATE, never falsely reported as successful cleanup. Git history remains intact.

## 7. Forbidden work and terminal state
SCIENCE_BUDGET=0
MODEL_RUNNER_BUDGET=0
CLASSIFIER_COMPILE_OR_SUITE_RERUN=0
OLD_ZIP_MEMBER_READS=0
OLD_ZIP_EXTRACTION=0
FORMAL_V010_WRITES=0
V011_START=PROHIBITED

Keep model_activation=False; REAL_GE=False; Results=FALSE; V011=NOT_STARTED; FULL_RUNNER_IO_CLOSURE=BLOCKED.
Final stop: WAIT_ASTRA_SAFE_BLOCKED_REPORT_REVIEW.
