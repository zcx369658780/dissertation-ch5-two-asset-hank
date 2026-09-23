# Optional GitHub Backup and Publication

Updated: 2026-09-23.

GitHub is an optional remote backup and milestone-publication channel. It is not the task queue, current-state authority, Reviewer communication channel, or scientific acceptance gate.

## When GitHub is used

- Use it only when `TASK_CURRENT.md`, Work, or Owner requests backup/publication.
- Inspect access and remote state immediately before that action.
- Push only ordinary non-force updates.
- Perform remote SHA/tree readback only for the requested publication or backup milestone.
- Report transport or account failures as Git delivery failures; do not recast them as scientific failures.

## Authority

- Local `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, `TASK_CURRENT.md`, local commits, and local evidence govern daily work.
- GitHub write access never grants scientific authority.
- Historical branch, issue, pull request, or remote CURRENT content cannot override newer accepted local state.
- No workflow may require GitHub merely to prove that local evidence exists.
