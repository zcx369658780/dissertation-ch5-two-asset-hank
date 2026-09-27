# Chapter 5 Two-Asset HANK — Local Working Agreement

Updated: 2026-09-25. Workflow authority: `LOCAL_WORK_WORKFLOW_V1`.

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
- After reviewing a completed task, Work records ACCEPT/REJECT and issues the next bounded `TASK_CURRENT.md` automatically when no substantive Owner decision is needed. A rejection may lead only to a scoped repair or design task under existing authority; it does not reset consumed calls or authorize a new scientific law.

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
- At scientific milestones and before high-risk source changes, make a verified local backup at the Owner-designated destination. A Git bundle covers committed history; separately include necessary untracked or ignored evidence with a manifest. A backup is not scientific acceptance.
- Store concise machine-readable evidence under the task's authorized location. Follow `EVIDENCE/README.md`.
- Historical Git data and reports remain archive/evidence; workflow migration does not rewrite accepted scientific history.

## Recovery and handoff

- If a project document cannot be recovered from GitHub, Work may assign Codex a bounded local recovery task without requesting fresh permission. Recover only from identifiable project-local or Owner-provided sources, preserve provenance, and mark unavailable content unresolved rather than reconstructing it from memory. Recovery does not authorize model changes or scientific calls.
- Work chooses a handoff point while the current conversation still has enough context. At handoff, send the Owner only a copyable handoff prompt; do not issue an additional task sheet in the same handoff. After the new conversation starts, verify the local state and automatically issue the next task sheet if no Owner decision is pending.
- GPT Work must stop its current objective and hand off when this Work conversation exceeds 30 dialogue records or becomes long enough that reliable continuation is at risk. Before giving the Owner a copyable prompt for manual handoff to the next GPT Work conversation, Work must first save the current task progress, key decisions, evidence identities, consumed budgets, and pending gates in a local project document. A handoff does not authorize new science or reset any call budget; any in-flight scientific operation still follows its authorized stop and accounting rules.
- For Codex execution, Work uses the latest project Codex conversation designated under the Owner's standing 2026-09-27 direct handoff authorization. At 30 dialogue records, unreliable context, or a conversation error requiring replacement, Work proactively saves the current verdict, task, evidence identities, protected roots, consumed budgets, call ledger and next gate; it then creates a successor inside the named Codex app project and requests a read-only intake. A repeated Owner designation is not required for this conversation-lifecycle action. Otherwise continue in the current conversation; do not create another merely for a new task. This is Work-orchestrated handoff, not an unattended hook or scheduler. The current handed-off conversation is “第五章 K1B A 路线零科学交接接续” (`01a0e046-973a-7bb1-b071-0305ebe541cf`). The previous conversations `01a0dcd7-2acc-7571-b292-5807a0be0b1d`, `01a0d867-be22-7d93-b2fb-0ddff659b686`, and `01a0cce5-241d-7ab3-b87c-e0a41628572e` must not receive another writing task in this worktree. No conversation other than the verified current successor may receive a writing task without another bounded handoff.
- Chapter 5 Codex conversations must remain inside the Codex app project `Zotero-Analytical-Workflow` (`local-0758adfaed355d5be608096cdf92a3a2`) so the project conversation context is retained. Before dispatching a writing task to a handed-off successor, Work verifies its app-project membership; if it was created outside the project, have it moved into this project first. The current successor was created with this project as its target on 2026-09-27 and completed a read-only entry check. Its project membership was subsequently verified by the Owner's matching Codex UI screenshot and explicit confirmation, preserved at `EVIDENCE/ch5_k1b_codex_project_membership_owner_ui_20260927/`; app API metadata still lacks a thread `projectId` and must not be claimed otherwise. App-project membership supplies conversation context only and does not expand the allowed repository or file scope: this Chapter 5 task still uses only `D:\ProjectTemp\c5k1bturn56` and must never access `deep-learning-hank`.
- Automatic conversation handoff transfers context only. It never issues or renews a scientific budget, resolves an unknown call ledger, authorizes a retry, creates an output root, weakens an Owner safety objective, accepts a candidate, or bypasses independent review. Work may automatically issue the next bounded `TASK_CURRENT.md` only after read-only intake and membership verification, and only when no substantive Owner decision or protected authorization remains pending. See `docs/CH5_K1B_CODEX_AUTOMATIC_HANDOFF_RULE_20260927.md`.

## Reporting

Report outcome, evidence, changed paths, checks, local commit, limitations, and the next gate. Keep scientific PASS, implementation fidelity, numerical validity, Reviewer acceptance, and Results eligibility distinct.
