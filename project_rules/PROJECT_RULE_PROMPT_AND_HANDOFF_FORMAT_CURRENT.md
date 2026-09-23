# Prompt and Handoff Format

Updated: 2026-09-23.

Do not depend on long chat history. A new session reads:

`CURRENT.md -> SCIENTIFIC_DECISIONS.md -> TASK_CURRENT.md -> REVIEW_GATE.md -> directly named source/evidence`

Work places the exact bounded objective in `TASK_CURRENT.md`. A startup message may identify the local repository and task, but it does not duplicate the whole task or create authority absent from the file.

Builder completion reports only outcome, evidence location, changed paths, checks, local commit, limitations, and next gate. Use full historical reports only when they are necessary evidence, not as routine handoff documents.
