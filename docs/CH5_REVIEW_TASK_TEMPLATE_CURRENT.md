<!-- LOCAL_FIRST_CLASSIFICATION_20261101 -->
> **适用范围：SUPERSEDED_WORKFLOW（普通工程派单模板）＋ SCIENTIFIC_CONSTRAINT（有界证据要素）**
>
> 当前执行入口：[AGENTS](../AGENTS.md) → [唯一短状态](CH5_LOCAL_FIRST_STATUS_CURRENT.md) → [唯一工作流](CH5_ASTRA_WORKFLOW_CURRENT.md)。Owner 决策见 [2026-11-01 决策记录](OWNER_LOCAL_FIRST_CODEX_20261101.md)。
>
> 此历史模板不是普通工程启动或网页终验的必填表。任务账本由 Local Codex 按实际授权维护；不得机械要求 GPT 发单、默认离线 ZIP 或每步新增报告。
> 未来具体科学合同若明确采用其中的来源/白名单/预算/原件/隐私/独立见证要求，仍须遵守；填写模板本身不产生 Owner 授权，不恢复旧额度。科学接受与普通工程验收分层。
> 下方模板及零预算默认原样保留，历史占位符不是当前待执行任务。

---

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