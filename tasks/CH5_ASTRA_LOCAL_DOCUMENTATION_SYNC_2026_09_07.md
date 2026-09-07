# Chapter 5 Astra workflow — local documentation sync

Date: 2026-09-07.
Task ID: `CH5_ASTRA_LOCAL_DOCUMENTATION_SYNC_2026_09_07`.
Type: documentation/local-instruction synchronization; zero scientific execution.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Owner authorization: the Owner approved the proposed governance simplification, directly authorized GitHub document updates, and requested a Codex task to align local documents including AGENTS.md.
Issuer: ChatGPT reviewer/task authority.

## 1. Goal
Bring the local Chapter 5 checkout and its repository-scoped instructions into agreement with the live Owner-approved `CH5_ASTRA_WORKFLOW_2026_09_07` documents.
Finish discovery, safe synchronization, necessary local instruction edits, verification and reporting in this single task.
This task changes workflow documents, not scientific semantics, model/provider configuration or experiment state.

## 2. Authority and reading
Fresh-fetch the target repository. Verify this task exists on live main and has not been superseded or completed.
Read root AGENTS.md, project_rules/PROJECT_RULE_INDEX_CURRENT.md, the workflow/local-file rules, and docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md.
Read other relevant current rules as needed; do not reread the entire historical task chain.
Science checkpoint: e98bfad214b0c85005fac2ce23b1e4585a20e634. The task publication is later; use fresh live main, not the checkpoint as a checkout target.
Unrelated later commits do not block this task. If its scope, relevant instructions or active authority changed, inspect the actual change before proceeding.
If the completion report already shows this task completed and no relevant local discrepancy remains, report that fact instead of generating a duplicate commit.

## 3. Find and preserve the local checkout
Use the current workspace first; otherwise inspect only known Chapter 5 checkout candidates from local context, such as D:\ResearchCode\dissertation-ch5-two-asset-hank. Verify git remote; never infer identity from folder name alone.
Do not scan every drive. If no accessible checkout is available, report the missing location. Do not create or modify another project.
Record absolute repository root, remote, branch, HEAD, origin/main and tracked/untracked status.
Preserve unrelated changes. If a clean main worktree can fast-forward, use the normal fast-forward update. Do not reset/clean/stash/force-push.
If a branch or dirty state prevents safe synchronization, create a dedicated clean worktree from fresh origin/main. This is authorized; report the worktree that is actually updated and any original checkout left unchanged.
Do not claim the original checkout was updated if only the isolated copy was updated.

## 4. Allowed documentation changes
Within the verified target checkout only:
- root AGENTS.md and existing repository-scoped nested AGENTS.md / AGENTS.override.md;
- project_rules/*.md: synchronize current indexed documents and annotate obsolete local route/workflow copies when needed;
- the four current state/roadmap/handoff documents published with this task;
- existing repository-local Codex instruction Markdown, only if discovered and actually applied to this checkout;
- docs/CH5_ASTRA_LOCAL_DOCUMENTATION_SYNC_REPORT_2026_09_07.md (required completion/partial report).

Review applied instructions along the ancestry of the checkout to understand precedence, but do not edit any file outside the repository. Higher-scope restrictions still apply. If they prevent the requested behavior, explain the exact file/rule and leave it unchanged.

Synchronize the GitHub-published docs through Git. Do not regenerate them from this prompt.
For local-only applicable instruction files, remove or replace ONLY obsolete workflow clauses that demand a new task for each engineering failure, require identical publication-parent main for every start, restart historical R5/R1A stages, forbid task-authorized draft edits, or ask Owner to decide representation-only naming.
Preserve scientific protections, valid scope constraints, user-specific paths, unrelated instructions and existing content.
Add concise references to the central workflow instead of copying the full rules into every nested file. Do not create a new network of instruction files.
If a local unique instruction must be edited, preserve a backup/diff in a task-specific folder under D:\ProjectTemp or another verified writable scratch root outside tracked source. Do not overwrite existing backups. The task authorizes these bounded backups without additional confirmation.
Do not edit historical completed task files or scientific reports. Stale local handoffs can remain history; the current index and a clear supersession note resolve ambiguity.

## 5. Scope of the new working style
- One task covers a complete logical problem.
- Continue routine engineering fixes anticipated by the task within allowed paths.
- Ordinary checks may be rerun after bounded fixes. Actual model calls still require explicit scientific budgets.
- Preserve and reuse unchanged accepted evidence; test only the affected behavior/invariants.
- Owner handles substantive science; reviewer/Builder handle implementation and presentation choices within scope.
- Protect MATLAB originals, accepted evidence, scientific ledgers and Results claims.
- Do not edit global/user-level AGENTS, ~/.codex/config.toml, provider/model settings, accounts, skills, other repositories, Windows junctions or MATLAB search paths.
- Do not install dependencies or tools for this documentation-only task.

## 6. Budget and checks
New MATLAB, Python HJB, KFE, direct-solver, household, GE, annual, shock/IRF and Results calls: zero.
No pytest/model regression, MATLAB, notebooks or scientific entrypoints. Git, file reads/diffs, Markdown/path checks and ordinary hash calculations are allowed.
Verify:
1. published current files exist and match origin/main before any documented local-only adaptation;
2. root AGENTS and any applied nested instructions use the revised workflow consistently;
3. rules index links resolve;
4. superseded R5/R1A material is not designated active;
5. changed paths are documentation-only and within this task;
6. no production code, tests, configurations or scientific fixtures changed.
A targeted text search is enough to locate suspect clauses; inspect context before modifying. Historical quotations of old constraints are not failures.
No exhaustive cache inventory, recursive self-hashing, proof-of-zero instrumentation framework or new certification task is required.

## 7. Report and publication
Write a concise report with actual checkout/worktree, baseline, docs synchronized, local instructions inspected/changed, relevant checks, original dirty state preserved, zero new scientific calls, and any remaining external instruction conflict.
Use status COMPLETE, ALREADY_CURRENT, or PARTIAL with specific reason. A truthful partial report may be published.
If repository-tracked changes or the report are new, stage only those explicit paths and create one docs-only commit.
A non-force push of a dedicated branch (for example codex/ch5-astra-local-doc-sync-20260907) is authorized; report remote branch and commit. Do not merge to main under this task.
If a dedicated branch already exists, inspect it; reuse only if it belongs to this task and is safe, otherwise use a unique suffix.
Check final diff scope and remote commit once after push. Do not invent a commit hash in a report before the commit exists; return it in the final message.

Stop after synchronization/report publication. Do not create or execute a scientific successor. Return a short outcome-first completion message for reviewer acceptance.
