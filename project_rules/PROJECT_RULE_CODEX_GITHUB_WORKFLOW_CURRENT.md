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

After recording ACCEPT/REJECT, Work prepares the next bounded task automatically if existing authority determines the next action and no substantive Owner choice is needed. A rejected candidate receives a scoped repair or design task only when its target behavior is already authorized. Handoff defers task issuance to the resumed conversation; it does not grant execution authority by itself.

## Local backup

- Use the Owner-designated destination on a different volume when available. A temporary `C:` destination is acceptable until replaced by an independent device or location.
- Back up at scientific milestones and before high-risk source changes, not after every small edit. First commit the intended local state and check for unrelated dirty files.
- Create a Git bundle covering the current branch history, record HEAD/tree, bundle SHA-256, source tree, and evidence identities, then run `git bundle verify` and a restore check in an isolated directory.
- Git does not include untracked or ignored evidence. Copy only necessary named artifacts separately with relative paths, byte sizes, SHA-256, and readback; do not silently include secrets or unrelated files.
- Backup failure is reported as a backup problem. It neither converts a scientific result to failure nor grants authority to bypass a required pre-change preservation gate.
