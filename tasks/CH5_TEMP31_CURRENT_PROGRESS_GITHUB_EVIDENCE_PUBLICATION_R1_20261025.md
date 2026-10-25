# CH5_TEMP31_CURRENT_PROGRESS_GITHUB_EVIDENCE_PUBLICATION_R1_20261025

STATUS=ISSUED__OWNER_EXPLICITLY_AUTHORIZED
TASK_TYPE=GOVERNANCE_AND_EVIDENCE_PUBLICATION_ONLY
OWNER_AUTHORIZATION=2026-10-25_USER_EXPLICIT
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=abc45bcbc6cb2084afa4a56e75a50d5b32c4a180
BASELINE_CANDIDATE_COMMIT=ba98537fd5ae004f0aa37d319865da1f1739e503
BASELINE_CANDIDATE_TREE=f432f0acb5d94e0f60cd976b74a236be883e0db3
ACTIVE_RESEARCH_TASK=NONE
SCIENCE_BUDGET=0
TEST_BUDGET=0
PREFLIGHT_BUDGET=0
MODEL_CALLS=0
HA_HJB_KFE_GE_IRF=0
FORMAL_SOURCE_WRITES=0
FORMAL_SOURCE_FREEZE=FALSE
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=False
REAL_GE=False
FULL_RUNNER_IO_CLOSURE=BLOCKED
AUTO_NEXT=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE

## 1. Goal

Publish the current TEMP31 research/implementation state and its critical evidence to GitHub so GPT/Astra can independently review the actual uploaded evidence directly from the fixed candidate commit. This is evidence packaging and publication only, not a new model implementation or scientific experiment.

## 2. Fixed context

- Latest governance HEAD before this task: abc45bcbc6cb2084afa4a56e75a50d5b32c4a180
- Historical baseline candidate commit: ba98537fd5ae004f0aa37d319865da1f1739e503
- Historical baseline candidate tree: f432f0acb5d94e0f60cd976b74a236be883e0db3
- Latest completed static audit reported in governance: `CH5_TEMP31_CANONICAL_INPUT_SOURCE_AND_UNITS_AUDIT_R1`, run `0e5c56f56a7f446d9748212738b509ee`, ZIP 100834 bytes, SHA-256 `00ecaf1cf987956d48379e440015dd39963c84779bc5ba9f94ca2ee2e38431fa`.
- The previous audit conclusions remain bounded: canonical wage source, real 31-province ID/order join, authoritative units/vintage, and production callback are unresolved/blocked.
- Owner decisions D1=B, D2, D3=B remain target contracts only; they do not prove production implementation.

## 3. Required execution

1. Read the local project's effective `AGENTS.md`, current workflow rules, CURRENT/TASK_CURRENT, TEMP31 route status, and this task sheet. Identify the active local TEMP31 worktree from local evidence; do not guess its path.
2. Read-only inspect current git status, branch, HEAD, relevant commit/tree and existing TEMP31 artifacts. Preserve all working-tree state. Do not reset, checkout destructively, clean, or modify scientific source.
3. Create a new dedicated candidate branch from the verified current governance parent or the correct frozen TEMP31 source parent as appropriate. Record exactly which parent was used and why. Do not update the governance branch or default branch with research artifacts.
4. Publish a narrowly scoped evidence directory under `tasks/CH5_TEMP31_CURRENT_PROGRESS_GITHUB_EVIDENCE_PUBLICATION_R1_20261025/` on the candidate branch. Use a manifest and an explanatory result report. Include the actual critical evidence files necessary for independent review, not only hashes or summaries.
5. Evidence should include, where locally available and privacy-safe:
   - Current TEMP31 status and provenance: worktree identity, git status, HEAD/parent/tree, task/run IDs, current route and STOP state.
   - Latest canonical-source/units audit ZIP or its exact original bytes, receipt, manifest, and independent report; confirm the ZIP's actual size and SHA-256 before publishing.
   - The field ledger, all 98 source excerpts with source member/line mappings, tax-base matrix, vintage-conflict table, Owner decision brief, and any source maps needed to interpret them.
   - The exact frozen source identities for the 31-province wage/tax/matrix/phi paths and their critical source context.
   - A concise inventory of prior TEMP31 evidence artifacts and their role/status, clearly separating original artifacts from summaries and historical receipts.
   - An explicit evidence-gap register for anything unavailable. Never synthesize missing raw files, claim that a historical receipt was reverified if it was not, or promote UNKNOWN/BLOCKED to PASS.
6. The package must be independently auditable from GitHub: list each included file's repository-relative path, byte length, SHA-256, provenance, and why it is necessary. Record excluded evidence and reason where exclusion affects review.
7. Run only packaging/integrity/privacy checks needed to safely publish the evidence package. Do not run project code, imports, tests, preflights, HJB/KFE/HA/GE/IRF, calibration, outer loops, parameter sweeps, or scientific calculations.
8. Before publishing, apply a finite privacy scan and remove secrets, tokens, credentials, private local usernames/absolute paths, and irrelevant personal data from the public copy. Preserve scientific source and evidence semantics; document redactions. If sanitization could change source identity, include the original source identity separately and clearly mark the public copy as sanitized.
9. Publish only to the new candidate branch and the exact task evidence directory. Do not write to `CURRENT.md`, `TASK_CURRENT.md`, formal model sources, V010, V011, source-freeze markers, old review directories, or protected paths as part of the candidate branch's evidence task. Do not open Issue/PR unless a separate task explicitly authorizes it.
10. After upload, read back the actual GitHub commit, parent, tree, paths, blob SHA, content/bytes and size. Verify the remote objects match the local package manifest. If write/read is refused, stop without trying another credential, protocol, account, or path to bypass the refusal.

## 4. Required deliverables

Under `tasks/CH5_TEMP31_CURRENT_PROGRESS_GITHUB_EVIDENCE_PUBLICATION_R1_20261025/` on the candidate branch:
- `result.md`: concise state, evidence inventory, known gaps, exact scope executed, and truthful STOP status.
- `manifest.json`: every package file's relative path, byte length, SHA-256, provenance, and purpose.
- `evidence/`: actual required source/evidence files, arranged without redundant duplicates.
- `DELIVERY_FINAL_RECEIPT.json`: candidate branch, parent, commit, tree, every relevant Blob SHA, sizes/hashes, upload/readback checks, and execution budgets.
- `INDEPENDENT_COMPLETION_EVENT.json`: only if a genuinely separate completion event exists; otherwise record UNKNOWN and explain. Do not self-certify independent completion.

## 5. STOP and acceptance boundary

Stop after the candidate evidence publication and remote readback. Do not begin the next research task. GPT/Astra will independently review the uploaded candidate from GitHub and issue a separate verdict. Candidate delivery success is not scientific acceptance.

Report separately:
- artifact_integrity
- source_identity
- numeric_review (should be NOT_RUN for this publication-only task)
- implementation_review (evidence packaging/provenance only)
- scientific_review (NOT_RUN)
- privacy_review
- actual_terminal
- delivery
- cleanup
- not_completed

If any required critical evidence is unavailable, publish the gap register if safe, mark the relevant item BLOCKED/UNKNOWN, and STOP. Do not inflate the scope to fix unrelated missing evidence.
