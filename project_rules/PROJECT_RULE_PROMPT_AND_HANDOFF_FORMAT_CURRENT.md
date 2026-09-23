# Prompt and Handoff Format

Updated: 2026-09-23.

Do not depend on long chat history. A new session reads:

`CURRENT.md -> SCIENTIFIC_DECISIONS.md -> TASK_CURRENT.md -> REVIEW_GATE.md -> directly named source/evidence`

Work places the exact bounded objective in `TASK_CURRENT.md`. A startup message may identify the local repository and task, but it does not duplicate the whole task or create authority absent from the file.

Builder completion reports only outcome, evidence location, changed paths, checks, local commit, limitations, and next gate. Use full historical reports only when they are necessary evidence, not as routine handoff documents.

Work may choose when to hand off while the current conversation still has enough context. The handoff response contains only one copyable prompt for the next conversation, with the local repository path, exact current gate, accepted candidate and evidence identities, pending Owner decision if any, and the first permitted action. Do not attach a new task sheet or start a task in the same handoff response. In the resumed conversation, verify the local files and commit, then issue the next bounded `TASK_CURRENT.md` automatically when no Owner decision is needed.
