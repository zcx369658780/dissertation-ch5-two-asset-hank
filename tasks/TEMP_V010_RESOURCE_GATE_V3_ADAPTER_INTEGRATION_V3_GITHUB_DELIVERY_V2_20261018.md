# Delivery-only recovery V2: TEMP V010 ResourceGate V3 adapter evidence

TASK_ID=TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_V2_20261018
STATUS=ISSUED_NOT_STARTED
SCOPE=DELIVERY_ONLY / ZERO_SCIENCE / NO_TEST_RERUN / NO_RUNNER

## Predecessor
The predecessor task TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_20261018, run_id 6568ae4f4d134f3b9459e47d983f2acc, stopped at SOURCE_FINAL_RECEIPT_IDENTITY before ZIP audit, fake-bare, SSH, fetch, push or publication. Do not resume or rewrite that run. The wrong 65-character expected receipt hash was manually copied and was not frozen in the predecessor contract; this does not prove source corruption.

## Fixed source identities
These are the only expected values for this task. Read source bytes first, compute actual length/SHA256, then compare. Do not add manually copied expectations from chat or summaries.

- delivery/evidence_sanitized.zip — 332933 bytes — SHA256 fc7a846d09758590dbd268b430ffd8c2c47aa0b2c63e307b510586f2443fafa0 — expected source: prior result + manifest.
- delivery/manifest.json — 239695 bytes — SHA256 1086f3b04166d406fdb4a87b684f06fb37dd34ff733728510003dfff0d635bbd — expected source: prior delivery source identity report.
- delivery/FINAL_RECEIPT.json — 9339 bytes — SHA256 14ca468c0c9b4339cea7a8bc91578fc899b88a4be7a9c96d4d7d552945d599f5 — expected source: Owner's corrected identity explicitly fixed in this contract.

All SHA256 strings must be validated as exactly 64 hexadecimal characters. Report expected value, expected source, actual value, actual length and decision. If a value is not in this contract or its stated source, classify VALIDATOR_EXPECTATION_DEFECT and STOP; do not classify the source as modified. Missing source bytes => SOURCE_BYTES_UNAVAILABLE. Mismatch against a fixed trusted value => SOURCE_IDENTITY_MISMATCH. The source task contract remains CONNECTOR_TEXT_VERIFIED, not RAW_GIT_OBJECT_VERIFIED.

## Remote publication
Review branch: review/ch5-temp-v010-resource-gate-v3-adapter-v2-20261018
Fixed parent: 37271647c5818731231b6d95854174ca1dcef3ce
Only path: _review_tmp/ch5/TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_V2_20261018/
Only files: result.md, manifest.json, evidence_sanitized.zip
Exactly one parent equal to fixed parent. At most one successful ordinary non-force publication. Never create _review_tmp in local worktree/index.

## Budgets
Fake-bare preflight <=3 local attempts; existing SSH/443 preflight <=1; GitHub read/fetch CLI <=2 total; ordinary non-force push <=2 total and <=1 successful publication; delivery batches <=5; wall clock <=60 minutes; at most one deterministic E1 argv/path/syntax repair with first error preserved. One ordinary cleanup commit after Astra permanent archive/readback, deleting only the three allowlisted files, followed by one readback.

No PAT/new credentials, force push, global/system Git config changes, extra clone/fetch, worktree, shared objects, alternates, or reference-sharing. Use exclusive bare object storage outside protected worktrees/indexes. If object completeness cannot be proven without unauthorized fetch, STOP. SCIENCE_BUDGET=0; ENGINEERING_TEST_BUDGET=0; MODEL_OR_RUNNER_BUDGET=0.

## Required prepublication audit
Audit every ZIP member and bounded nested archives: CRC, inventory, case-insensitive duplicates, absolute/drive/UNC/ADS paths, traversal, links, compression ratios, credentials, private absolute paths and unauthorized real research data. Never execute archive contents. If any member is uninspectable or sensitive data cannot be ruled out, STOP before publication. Preserve RAW source artifacts unchanged; publish only sanitized derivatives, keeping RAW_EXACT and SANITIZED_DERIVATIVE distinct. Manifest lists all three remote files with length/SHA256 and each ZIP member with path/length/SHA/classification. Limits: result <=128 KiB; manifest <=1 MiB; compressed ZIP <=32 MiB; uncompressed <=256 MiB; <=3000 members.

Fake-bare preflight must test argv tokenization, blob/tree/commit and sole parent, non-force push, raw ZIP byte readback, and cleanup-tree readback. Only after it and source/sanitization checks pass may one SSH/443 publication be attempted. Then read back exact ref/commit/tree/parent and all three files, including actual ZIP bytes and independently computed SHA256/length. If binary bytes cannot be obtained, BINARY_NOT_INDEPENDENTLY_READABLE; no ZIP acceptance claim.

Astra permanently archives verdict and reads it back before cleanup. Git deletion does not erase history. Any identity, source, privacy, parent, permission or budget issue => FAIL_CLOSED / STOP.

No tests or runner reruns. No model/science calls. Keep model_activation=False; REAL_GE=False; Results=FALSE; V011=NOT_STARTED; FULL_RUNNER_IO_CLOSURE=BLOCKED. Final stop WAIT_ASTRA_INDEPENDENT_REVIEW_AND_PERMANENT_ARCHIVE.
