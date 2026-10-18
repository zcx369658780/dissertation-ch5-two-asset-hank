# TEMP V010 ResourceGate V3 Adapter — Delivery-Only Recovery Contract

TASK_ID=TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_20261018
SCOPE=DELIVERY_ONLY / ZERO_SCIENCE / NO_TEST_RERUN / NO_RUNNER
STATUS=ISSUED_NOT_STARTED

## 1. Authority and non-resumption

This is a new, narrowly scoped delivery task. It does not rewrite, resume, or amend the fixed contract for `TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_20261018`, whose scope prohibited network publication. The previous task's local technical result remains `PASS_BOUNDED_ADAPTER_INTEGRATION_LOCAL`; Astra independent acceptance remains pending until this delivery and review chain completes.

Immutable source task issue commit: `37271647c5818731231b6d95854174ca1dcef3ce`.
Immutable source contract blob: `489b636cba99a66ea40b85041f9bf87c7aaccfee`.
Source run ID: `33f2b49ddc274e868956f6480d5f3a3a`.
Source evidence ZIP reported SHA256: `fc7a846d09758590dbd268b430ffd8c2c47aa0b2c63e307b510586f2443fafa0`, length 332933 bytes.
Source manifest reported SHA256: `1086f3b04166d406fdb4a87b684f06fb37dd34ff733728510003dfff0d635bbd`, with 490 registered payload members plus manifest.json as the sole extra ZIP member.
Source contract text identity was CONNECTOR_TEXT_VERIFIED, not RAW_GIT_OBJECT_VERIFIED. Do not upgrade that evidence class.

This task only packages, audits, publishes, and verifies already-existing artifacts. Do not rerun static tests, synthetic tests, Windows smoke, Python, adapter, resource gate, model, HA/HJB/KFE/selector/root solver/GE/IRF, or any runner. Do not modify source implementation, source receipts, prior task evidence, V010, or model trees. Do not continue any closed budget.

## 2. Required outputs and remote identity

Create exactly one new remote review branch:
`review/ch5-temp-v010-resource-gate-v3-adapter-v3-20261018`

Fixed parent commit:
`37271647c5818731231b6d95854174ca1dcef3ce`

Only allowed remote path:
`_review_tmp/ch5/TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_20261018/`

Exact allowed files:
- `result.md`
- `manifest.json`
- `evidence_sanitized.zip`

No other path or file is permitted. Use one successful ordinary non-force publication at most. The review candidate must have exactly one parent equal to the fixed parent commit. No main/governance/model branch mutation as part of review publication. Do not create this temp directory in any local worktree or Git index.

## 3. Independent budgets

DELIVERY_BUDGET only:
- fake-bare end-to-end publisher preflight: at most 3 local attempts; must not contact GitHub and must use a new exclusive bare object store outside every protected worktree/index;
- SSH credential/connectivity preflight using existing SSH key and ssh.github.com:443: at most 1;
- GitHub read/fetch CLI attempts: at most 2 total;
- ordinary non-force push attempts: at most 2 total, with at most one successful publication;
- delivery batches: at most 5;
- wall-clock delivery window: 60 minutes;
- no more than one deterministic E1 argv/path/script-syntax repair cycle, with first error preserved;
- cleanup: one ordinary non-force commit deleting only the three allowlisted files from this review branch's current tree, then one readback.

No PAT, API token, new credentials, global/system Git config changes, force push, unbounded retries, extra clone/fetch, worktree, shared object store, alternates, or reference-sharing. If the publisher cannot safely establish complete parent/tree/blob objects without unauthorized fetch, stop. Do not invent additional budgets.

SCIENCE_BUDGET=0.
ENGINEERING_TEST_BUDGET=0.
MODEL_OR_RUNNER_BUDGET=0.
NETWORK_PUBLICATION=AUTHORIZED_ONLY_AS_SPECIFIED_ABOVE.

## 4. Pre-publication audit (mandatory)

Before any remote publication:
1. Read the exact fixed task source artifacts from the existing run root using its manifest/run ID and declared hashes. Do not recursively scan unrelated roots or guess an alternate run.
2. Verify ZIP SHA256/length, ZIP CRC/structure, all member names and sizes, case-insensitive duplicate paths, absolute/drive/UNC/ADS paths, `..` traversal, links/reparse-like entries, extreme compression ratios, nested archives, and the manifest's full member inventory.
3. Inspect every member and every nested archive within bounded depth/size/count. Do not execute archive contents. If any member/archive cannot be parsed or inspected, or sensitive material cannot be ruled out, STOP before publication.
4. Check for real absolute Windows paths/usernames, personal email, IP/internal topology, command argv/env, credentials/tokens/SSH materials, Git metadata, and non-authorized real research data. Preserve local RAW files unchanged. Publish only already-sanitized derivatives; never label RAW bytes sanitized by assumption.
5. Verify each declared original-vs-packaged SHA/length and classification. Keep `RAW_EXACT` and `SANITIZED_DERIVATIVE` distinct. If the published ZIP or manifest would exceed its limit, STOP rather than silently changing the frozen scope.

Size limits: `result.md` ≤128 KiB; `manifest.json` ≤1 MiB (explicit one-task exception to the usual 256 KiB default because this inventory contains 490 payload members); compressed ZIP ≤32 MiB; total uncompressed bytes ≤256 MiB; total members ≤3000 including nested archives within the bounded scan. Do not split archives or use compression to evade limits.

## 5. Fake-bare preflight and remote publication

The fake-bare test must verify:
- command argument tokens are separate argv elements, including Git directory/context and config flags;
- blob/tree/commit construction and sole-parent identity;
- normal non-force push to the fake remote;
- independent raw-byte readback of the binary ZIP and hash match;
- deletion of only the allowlisted current-tree files and readback of their absence.

A local E1 syntax/argv error may be fixed once within budget; retain the first error in the result. Authentication, permission, parent identity, path containment, sensitive content, object completeness, or budget failure => STOP, no real publication if not yet performed, and no fallback retry outside budget.

After the fake-bare preflight passes, publish once through the existing SSH key over port 443. Immediately read back the exact branch head, candidate commit, tree, sole parent, each of the three blobs, UTF-8 bytes for MD/manifest, and actual ZIP bytes with independently recomputed SHA256 and length. If binary raw bytes cannot be obtained, record `BINARY_NOT_INDEPENDENTLY_READABLE`; do not claim ZIP acceptance.

## 6. Result content and Astra handoff

`result.md` must include:
- task ID, run ID, source task commit/blob, fixed parent, review branch, candidate commit/tree and exact remote paths;
- pre-publication audit and fake-bare preflight outcomes;
- original and packaged hashes/lengths, archive member counts and any sanitization transformation;
- resource facts copied from the existing final receipt only; clearly distinguish reported local execution from Astra-independent verification;
- explicit statement: no tests/model/runner rerun and no scientific authorization.

`manifest.json` must list all three published files with SHA256 and byte length; ZIP payload members individually need path, byte length, SHA256 and RAW_EXACT/SANITIZED_DERIVATIVE classification, plus original and packaged hashes for derivatives. Do not place credentials, actual absolute user paths or private environment data in either file.

## 7. Astra review, permanent archive, cleanup

After Codex reports delivery, Astra independently reads the fixed remote ref/commit/tree and the exact three blobs. Astra must independently recompute the ZIP SHA256/length, inspect ZIP safety and verify every manifest member. A Git blob SHA alone is not a substitute for raw-byte SHA256. If connector/tool boundaries prevent binary byte access, acceptance remains pending.

Only after Astra's permanent review verdict is committed to the governance branch and read back may the three allowlisted files be deleted from this remote review branch via an ordinary non-force cleanup commit. Verify the latest review tree no longer contains those files. Never erase or rewrite Git history. If cleanup fails, mark `TEMP_CLEANUP_PENDING`; do not broaden deletion.

## 8. Terminal conditions and forbidden status changes

Terminal PASS means only delivery integrity and independently readable sanitized evidence are established; it does not itself mean the engineering implementation is independently accepted. Terminal STOP applies to any uninspectable archive, mismatch, sensitive-data uncertainty, unauthorized path, missing parent object, network/authentication failure, or exhausted budget.

Keep unchanged:
`model_activation=False`
`REAL_GE=False`
`Results=FALSE`
`V011=NOT_STARTED`
`FULL_RUNNER_IO_CLOSURE=BLOCKED`
`ACTIVE_RESEARCH_TASK=NONE`
`ACTIVE_SCIENCE_TASK=NONE`

Final stop for Codex:
`WAIT_ASTRA_INDEPENDENT_REVIEW_AND_PERMANENT_ARCHIVE`
