# Local Task and Codex Workflow

Updated: 2026-09-23. This replaces GitHub-heavy daily workflow requirements.

## One bounded task

`TASK_CURRENT.md` is the only default Builder task. It states objective, allowed scope, inputs, checks, evidence, stop conditions, forbidden work, and expected terminal. A bounded task does not expand into a roadmap.

## Start and execute

1. Read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, `TASK_CURRENT.md`, and `REVIEW_GATE.md`.
2. Check local HEAD and worktree status.
3. Read only directly relevant source/evidence.
4. Execute the authorized scope and preserve the first scientific failure.
5. Persist focused evidence and update local current state when the task permits.

Routine imports, paths, serialization, manifest, readback, and report defects may be repaired inside a task when they preserve the accepted scientific object and allowed paths. Actual scientific calls always count.

## Local Git

- Local working tree, local commit, and local evidence are repository-state authority.
- Use explicit staging and an atomic local commit when useful.
- GitHub fetch, issue, branch, push, pull request, and remote readback are optional backup/publication actions, not daily completion or scientific acceptance gates.
- Never equate a commit or publication with scientific acceptance.
- Preserve unrelated dirty files; do not reset, clean, stash, force push, or overwrite user work for convenience.

## Review

Use `REVIEW_GATE.md`. Reuse sealed evidence when it answers the review question. A completed task cannot be rerun or expanded by historical authority alone.
