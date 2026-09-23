# Chapter 5 Two-Asset HANK — Local Working Agreement

Updated: 2026-09-23. Workflow authority: `LOCAL_WORK_WORKFLOW_V1`.

## Project boundary

- The only active project is this local `dissertation-ch5-two-asset-hank` repository.
- Never enter, read, search, cite, use, or modify `deep-learning-hank`.
- The current local working tree, local commits, and local evidence are repository-state authority.
- GitHub is optional backup and milestone publication. Fetch, push, remote readback, issues, branches, and pull requests are not routine scientific gates.

## Startup order

Read only what the current task needs, in this order:

1. `CURRENT.md`
2. `SCIENTIFIC_DECISIONS.md`
3. `TASK_CURRENT.md`
4. `REVIEW_GATE.md`
5. source and evidence directly named by `TASK_CURRENT.md`

Use historical reports only for a specific provenance question. Do not recursively reread the task archive, reports, or rule archive.

## Roles

- Owner is final scientific authority.
- GPT Work is Project Lead, L3 independent Reviewer, scientific-route advisor, and Orchestrator.
- Codex is bounded Builder and executor. Codex implements `TASK_CURRENT.md`, runs authorized checks or science, persists evidence, and reports the first failure.
- Codex does not self-accept high scientific risk changes or create a scientific successor without Work/Owner authority.

## Execution contract

- `TASK_CURRENT.md` is Codex's only default execution entry.
- Honor exact allowed paths, call budgets, stop conditions, and forbidden work.
- Preserve first-failure discipline. Bounded debugging is allowed only inside the task's stated scope and budgets.
- Do not change equations, KKT or boundary economics, calibration, timing, payoff law, solver semantics, grids, or tolerances unless the task explicitly authorizes it.
- A completed or waiting `TASK_CURRENT.md` authorizes no scientific execution.
- Model calls, including failed calls, count. A new conversation does not reset budgets.

## Local Git and evidence

- Inspect local HEAD and worktree status before edits. Preserve unrelated user files; use an isolated worktree when needed.
- Stage explicit paths. Do not use `git add .`, `git add -A`, destructive cleanup, reset, stash, or force push for convenience.
- A clean local commit plus local evidence is sufficient for day-to-day completion. Push only when a task or the Owner requests backup/publication.
- Store concise machine-readable evidence under the task's authorized location. Follow `EVIDENCE/README.md`.
- Historical Git data and reports remain archive/evidence; workflow migration does not rewrite accepted scientific history.

## Reporting

Report outcome, evidence, changed paths, checks, local commit, limitations, and the next gate. Keep scientific PASS, implementation fidelity, numerical validity, Reviewer acceptance, and Results eligibility distinct.
