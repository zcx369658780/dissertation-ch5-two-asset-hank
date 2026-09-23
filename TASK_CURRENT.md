# Current Builder Task — Codex local workflow binding

Task ID: `CH5_CODEX_LOCAL_WORKFLOW_BINDING_AND_FRESH_TASK_VERIFICATION_20260923`
Status: `ACTIVE`
Risk: low, project workflow only. Scientific calls: `0`. Results eligibility: `FALSE`.

## Objective

Make the approved local Work → Codex workflow operative in a new Codex task launched from `D:\ProjectTemp\c5k1bturn56`. Verify that project-root `AGENTS.md` is the active Codex instruction entry and directs the Builder to `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, this task, and `REVIEW_GATE.md`. Repair only an evidenced project-local instruction or routing gap. If current files already work, deliver verification without redundant configuration.

After independent Work acceptance, return to the Chapter 5 scientific route. This task grants no turn7 or convergence execution authority.

## Baseline and required reads

- Root: `D:\ProjectTemp\c5k1bturn56`.
- Dispatch baseline HEAD: `c059b40a45cda00e76bd0b63aecff30a11b5b088`; production `src` tree: `00682b2e1a7ba23665f6e16f6acf48ad35874883`.
- Read in order: `AGENTS.md`, `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, `TASK_CURRENT.md`, `REVIEW_GATE.md`, then directly relevant current workflow rules under `project_rules/`.
- Approved workflow: local state/commits/evidence authority; `TASK_CURRENT.md` as sole Builder entry; Work-owned acceptance and automatic next task when no Owner decision remains; handoff response containing only the prompt, with task issuance after resumption; bounded Codex help recovering named project documents when GitHub is unavailable; verified local backup at the Owner-designated destination.
- Accepted turn5-turn6 science and migration reviews remain unchanged. The sealed turn7 input is provenance only.

## Allowed work

1. Confirm cwd, Git root, HEAD, worktree state, and which project instruction file this fresh Codex task received. Distinguish session-provided instructions from files read explicitly. If automatic discovery cannot be established, record `UNVERIFIED`.
2. Audit only the project-local instruction chain. Check seven static scenarios: waiting task ⇒ no science; completed task ⇒ Builder does not self-accept; no Owner decision after Work review ⇒ Work issues next task; handoff ⇒ prompt now and task after resumption; GitHub outage ⇒ no daily block; named missing GitHub document ⇒ bounded recovery with provenance; milestone backup ⇒ Git bundle and restore check, not a science PASS gate.
3. Make the smallest project-local documentation change needed for a demonstrated gap. Do not add a skill, hook, config layer, script, or test merely to duplicate `AGENTS.md`. Do not edit global Codex settings, instructions, skills, or plugins.
4. Persist a concise report and machine-readable verification receipt. Run only relevant static checks, including `git diff --check`, referenced-path checks, and source/evidence diff. Commit only authorized paths locally with explicit staging. Do not push.

## Allowed write paths

- `AGENTS.md`
- `project_rules/PROJECT_RULE_CODEX_GITHUB_WORKFLOW_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `project_rules/PROJECT_RULE_PROMPT_AND_HANDOFF_FORMAT_CURRENT.md`
- `project_rules/PROJECT_RULE_OVERVIEW_CURRENT.md`
- `docs/CH5_CODEX_LOCAL_WORKFLOW_BINDING_VERIFICATION_REPORT.md`
- `EVIDENCE/codex_local_workflow_binding_20260923/**`

Report-only completion is valid. `TASK_CURRENT.md` and `CURRENT.md` are Work-owned dispatch/state files; Builder must not modify them.

## Preservation and stop conditions

- No changes to `src/`, `reports/`, `tests/`, `validators/`, accepted evidence, `SCIENTIFIC_DECISIONS.md`, or `REVIEW_GATE.md`. Production `src` tree remains `00682b2e1a7ba23665f6e16f6acf48ad35874883`.
- Scientific HJB/KFE, selector, root, D2/Q, integration, firm, K1B, K2, MATLAB, GE, annual, shock, IRF, welfare, and Results calls: `0`. No nested Codex model invocation is required.
- GitHub fetch/push, remote readback, branch/issue/PR creation, global setting edit, destructive cleanup, and access to the separate forbidden project: `0`.
- Explain any workflow mismatch with exact file/line evidence before a scoped edit. Preserve the first unresolved blocker; do not broaden scope.

## Evidence and terminal

Write `EVIDENCE/codex_local_workflow_binding_20260923/verification.json` and `docs/CH5_CODEX_LOCAL_WORKFLOW_BINDING_VERIFICATION_REPORT.md`. Include dispatch baseline, changed paths, source tree, seven scenario results, zero scientific call ledger, and any unverified discovery claim. Report the final commit in the terminal response after committing; do not attempt to embed a commit ID in a receipt contained by that same commit.

Success: `PASS__CH5_CODEX_LOCAL_WORKFLOW_BINDING__PROJECT_SCOPED__ZERO_SCIENCE__AWAITING_WORK_REVIEW`.

If a required instruction source or scenario cannot be verified within scope, return `BLOCKED__CH5_CODEX_LOCAL_WORKFLOW_BINDING__EXACT_GAP_RECORDED` and stop. Codex must not self-accept or issue the next scientific task.
