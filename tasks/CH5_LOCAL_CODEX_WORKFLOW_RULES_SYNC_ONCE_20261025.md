# CH5_LOCAL_CODEX_WORKFLOW_RULES_SYNC_ONCE_20261025

STATUS=ISSUED__OWNER_EXPLICIT
TASK_TYPE=GOVERNANCE_DOCUMENT_SYNC_ONLY
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=ad1f330cfc59cc9155ab1b359cf5781d48351646
SOURCE_OF_TRUTH=GitHub files at the exact governance commit below
REQUIRED_COMMIT=ad1f330cfc59cc9155ab1b359cf5781d48351646
ACTIVE_RESEARCH_TASK=NONE
SCIENCE_BUDGET=0
TEST_BUDGET=0
PREFLIGHT_BUDGET=0
MODEL_CALLS=0
HA_HJB_KFE_GE_IRF=0
FORMAL_SOURCE_WRITES=0
AUTO_NEXT=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE

## Purpose
Synchronize the local Codex project's workflow/rule entrypoints once to the newly approved manual GitHub task-and-evidence workflow. Do not execute or modify scientific research code.

## Required reading from GitHub
- docs/CH5_GITHUB_WORKFLOW_AUTHORITY_CURRENT_20261025.md
- docs/CH5_INDEPENDENT_REVIEW_RULES_20261025.md
- docs/CH5_ASTRA_WORKFLOW_CURRENT.md
- docs/CH5_REVIEW_TASK_TEMPLATE_CURRENT.md
- docs/CH5_MANDATORY_REVIEW_DELIVERY_AND_CLEANUP_20261019.md
- docs/CH5_OFFLINE_WORKFLOW_AUTHORITY_CURRENT_20261023.md (now marked SUPERSEDED)
- AGENTS.md
- CURRENT.md
- TASK_CURRENT.md
- docs/CH5_PROJECT_MEMORY_CURRENT.md
- docs/DOC_INDEX_CURRENT.md

## Actions
1. Verify local repository/worktree identity and status before edits; never guess the worktree path.
2. Preserve dirty/untracked scientific state exactly. Do not reset, checkout destructively, clean, stage, commit, or push local changes.
3. Update only local governance/rule files that are part of the approved Project/ Codex startup contract. The current GitHub authority is the source of truth; mark the former offline-first rule as superseded, do not leave contradictory active instructions in AGENTS or local entrypoints.
4. Do not delete, move, rewrite or regenerate scientific evidence, source archives, prior STOP/PENDING reports, task evidence, or model code. If the local project layout differs, record the mismatch and stop instead of guessing.
5. Verify changed governance files by rereading them and checking the key fields: manual GitHub task sheet → local Codex → SSH candidate branch → GPT fixed-commit review → Owner decision; no automatic issue/PR, merge, cleanup, or next task; complex program projects do not default to full offline ZIP; science permission remains separate.
6. Record exact changed paths, pre/post hashes where available, unchanged worktree/index/ref evidence, any conflicts and unresolved local-vs-GitHub differences.

## STOP
This is a one-time governance synchronization only. No scientific code, tests, preflight, model, HA/HJB/KFE/GE/IRF, calibration, or parameter sweep. Do not alter GitHub; this task authorizes local documentation sync only. Do not create follow-up tasks. Report and STOP.
