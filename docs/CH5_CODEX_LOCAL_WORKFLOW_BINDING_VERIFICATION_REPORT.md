# Chapter 5 Codex local workflow binding verification

2026-09-23 (Asia/Shanghai). Task `CH5_CODEX_LOCAL_WORKFLOW_BINDING_AND_FRESH_TASK_VERIFICATION_20260923`.

## Dispatch and instruction provenance

- Git root/cwd: `D:/ProjectTemp/c5k1bturn56`. Initial clean HEAD `ac20973fa0986088e899b1ae0b95541bdec8b2ab`; baseline `c059b40a45cda00e76bd0b63aecff30a11b5b088` is its parent. The dispatch difference changes only `CURRENT.md` and `TASK_CURRENT.md`; Builder did not modify either.
- Root `AGENTS.md` content arrived as session-supplied project instructions before any explicit read. Builder then read the tracked file explicitly. It lists `CURRENT.md -> SCIENTIFIC_DECISIONS.md -> TASK_CURRENT.md -> REVIEW_GATE.md` (`AGENTS.md:12-20`) and makes the task the sole default entry (`AGENTS.md:32-38`). Whether Codex's automatic file-discovery loader independently selected this root file is **UNVERIFIED** without a loader trace; session delivery is established, not the mechanism. No evidenced project-local routing gap requires a repair.
- Production `HEAD:src` tree: `00682b2e1a7ba23665f6e16f6acf48ad35874883`, matching the task baseline.

## Seven static scenarios

| Scenario | Result | Exact project evidence |
| --- | --- | --- |
| Waiting task: no science | PASS_STATIC | `AGENTS.md:34-39` |
| Completed task: Builder does not self-accept or rerun | PASS_STATIC | `AGENTS.md:28-30`; `project_rules/PROJECT_RULE_CODEX_GITHUB_WORKFLOW_CURRENT.md:27-31` |
| Work review, no Owner decision: next bounded task | PASS_STATIC | `AGENTS.md:30`; `project_rules/PROJECT_RULE_OVERVIEW_CURRENT.md:11-17` |
| Handoff: prompt now, task after resumed verification | PASS_STATIC | `AGENTS.md:53`; `project_rules/PROJECT_RULE_PROMPT_AND_HANDOFF_FORMAT_CURRENT.md:13` |
| GitHub outage: no daily-work block | PASS_STATIC | `AGENTS.md:9-10,43-45`; `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md:15-20` |
| Named missing GitHub document: bounded recovery with provenance | PASS_STATIC | `AGENTS.md:52`; `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md:22-24` |
| Milestone backup: bundle and restore check, not science PASS | PASS_STATIC | `AGENTS.md:46`; `project_rules/PROJECT_RULE_CODEX_GITHUB_WORKFLOW_CURRENT.md:33-39` |

Static rule checks only: no backup, recovery, scientific operation, or GitHub operation was simulated. `REVIEW_GATE.md:48` confirms the handoff exception.

## Outcome

- Changed paths: this report and `EVIDENCE/codex_local_workflow_binding_20260923/verification.json` only. No instructions, accepted evidence, or scientific source changed.
- Scientific ledger: HJB/KFE, selector, root, D2/Q, integration, firm, K1B, K2, MATLAB, GE, annual, shock, IRF, welfare, Results = **0 each**. GitHub fetch/push/readback/branch/issue/PR = **0 each**.
- Static checks before staging: referenced paths, baseline ancestry, source tree, changed-path set, and report manifest readback passed. `git diff --check` exited 0 on tracked paths, but did not include the two untracked files. The separate automatic-discovery mechanism remains **UNVERIFIED**.
- First terminal blocker: explicit-path `git add -- docs/CH5_CODEX_LOCAL_WORKFLOW_BINDING_VERIFICATION_REPORT.md EVIDENCE/codex_local_workflow_binding_20260923/verification.json` failed: `fatal: Unable to create 'D:/ResearchCode/dissertation-ch5-two-asset-hank/.git/worktrees/c5k1bturn56/index.lock': Permission denied`. The worktree's Git metadata is outside the writable root. No commit was made; staged-diff check and commit did not run. No retry, alternate index, permission change, or remote operation was attempted.
- Builder terminal: `BLOCKED__CH5_CODEX_LOCAL_WORKFLOW_BINDING__GIT_INDEX_PERMISSION_DENIED`. The seven static scenarios passed but the required local commit is absent. Next gate: provide authorized write access to this worktree's Git metadata or have an authorized operator review and commit these exact two paths. No self-acceptance, turn7/convergence authority, or Results eligibility.
