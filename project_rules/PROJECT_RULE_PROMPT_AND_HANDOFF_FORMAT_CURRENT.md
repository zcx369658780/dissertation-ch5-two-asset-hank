# Prompt and Handoff Format

Updated: 2026-09-23.

Do not depend on long chat history. A new session reads:

`CURRENT.md -> SCIENTIFIC_DECISIONS.md -> TASK_CURRENT.md -> REVIEW_GATE.md -> directly named source/evidence`

Work places the exact bounded objective in `TASK_CURRENT.md`. A startup message may identify the local repository and task, but it does not duplicate the whole task or create authority absent from the file.

Builder completion reports only outcome, evidence location, changed paths, checks, local commit, limitations, and next gate. Use full historical reports only when they are necessary evidence, not as routine handoff documents.

Work may choose when to hand off while the current conversation still has enough context. The handoff response contains only one copyable prompt for the next conversation, with the local repository path, exact current gate, accepted candidate and evidence identities, pending Owner decision if any, and the first permitted action. Do not attach a new task sheet or start a task in the same handoff response. In the resumed conversation, verify the local files and commit, then issue the next bounded `TASK_CURRENT.md` automatically when no Owner decision is needed.
# Prompt and Handoff Format — compact incremental recovery

Updated: 2026-10-31.

## Startup sequence
1. Read `project_rules/PROJECT_RULE_PYTHON_RESEARCH_MAINLINE_CURRENT_20261031.md`.
2. Read the compact Project Source current-state file or repository live state.
3. Read only the Owner-designated current task, fixed commit and directly relevant raw evidence.
4. Read relevant scientific decisions/source derivations only when needed for the current question.

Do not recursively scan historical docs/tasks/experiments, reproduce the full dissertation, or restate the full project history. The project knowledge base is not a checklist to reload in every conversation.

## Handoff contract
A handoff contains only:
- current bounded scientific question;
- exact Python source commit/tree and task/evidence paths;
- latest raw experiment identity and verified conclusions;
- unresolved issues and explicit UNKNOWN/NOT_CERTIFIED fields;
- Owner-approved permissions, remaining budgets and STOP conditions;
- one next permitted action (or state that no task is authorized).

Do not copy large logs, dissertation text, MATLAB history or old task summaries into routine handoffs. Link to immutable source evidence. Do not promote an assistant summary into a scientific result.

## Session length discipline
Prefer one scientific question per conversation. When a session becomes long or the next task changes domains, prepare a concise incremental handoff before context quality degrades. Never wait for truncation. A new conversation does not reset budgets, reopen STOPs or grant permissions.
