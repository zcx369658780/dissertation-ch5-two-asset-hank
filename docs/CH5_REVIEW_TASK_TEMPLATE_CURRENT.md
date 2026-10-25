# CH5 GitHub 任务单模板 V3
TASK_ID=
STATUS=ISSUED_ONLY_AFTER_OWNER_AUTHORIZATION
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=
CANDIDATE_BRANCH=
FIXED_PARENT=
SOURCE_COMMIT=
SOURCE_TREE=
TASK_PATH=tasks/<TASK_ID>/
DELIVERY_MODE=GITHUB_CANDIDATE_BRANCH_SSH
AUTO_ISSUE=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## Goal and acceptance question
<one bounded purpose and decision the evidence should enable>

## Frozen source identity
<repository, commit, tree, path, Blob; distinguish candidate from formal source>

## Authorized scope and protected paths
<exact read/write allowlist>

## Budgets
SCIENCE_BUDGET=0
TEST_BUDGET=0
PREFLIGHT_BUDGET=0
MODEL_CALLS=0
HA_HJB_KFE_GE_IRF=0
FORMAL_SOURCE_WRITES=0

## Required evidence
result.md; manifest.json (path, bytes, SHA-256, Git Blob, provenance, purpose); sufficient actual source/evidence context; gap register; privacy report; DELIVERY_FINAL_RECEIPT.json with commit/parent/tree/readback/budgets. INDEPENDENT_COMPLETION_EVENT remains UNKNOWN unless a genuinely independent witness exists.

## Privacy and STOP
No secrets/private keys/tokens/credentials or irrelevant personal data. Redacted copies preserve original identity and transformation notes. Stop after remote readback. No automatic next task, merge, cleanup or scientific execution.
Acceptance fields: artifact_integrity; source_identity; numeric_review; implementation_review; scientific_review; privacy_review; actual_terminal; delivery; cleanup; not_completed.