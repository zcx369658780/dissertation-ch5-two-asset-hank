# Current Builder Task - repair committed-file dependency wording

Task ID: `CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_IDENTITY_CHAIN_PREPARATION_REPAIR2_ZERO_SCIENCE_20260926`
Status: `ACTIVE__NONAUTHORITY_COMMITTED_FILE_WORDING_ONLY__NO_SCIENCE`
Assignee: Codex project `Zotero-Analytical-Workflow`, conversation `第五章 K1B 静态 runner 审查后接续` (`01a0dcd7-2acc-7571-b292-5807a0be0b1d`) only.
Worktree: `D:\ProjectTemp\c5k1bturn56` only. Never access `deep-learning-hank` or Zotero repository files.

## Start gate

Read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, this task, `REVIEW_GATE.md`, `AGENTS.md`, `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_IDENTITY_CHAIN_REPAIR1_INDEPENDENT_REVIEW_20260926.md`, the three rejected Repair1 files, and only timed runner lines `161-175` and `352-444` needed for this wording. Verify task-issuance HEAD is a direct child of rejected candidate `4811fcc4a6e19af8f19295ee2993d3378e87b864`, `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`, tracked files/index clean, exactly five protected untracked roots with the review-recorded manifest hashes, and absence of R/C/O/future execution task-copy/new C9 root. Stop on mismatch.

## Only allowed changes

Edit only these three existing **non-authoritative** paths:

- `tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_IDENTITY_CHAIN_PREPARATION_20260926.json`
- `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_IDENTITY_CHAIN_PREPARATION_ZERO_SCIENCE_20260926.md`
- `EVIDENCE/ch5_k1b_c9_post_failure_new_attempt_identity_chain_preparation_zero_science_20260926/preparation_receipt.json`

In the matrix's R/C/O/T prerequisites or a shared exact-runner gate, and in the report, state that each future runner-recognized authority file checked by `committed_file` must have safe path components, be a regular file, have clean path-specific Git status, and have a filtered worktree blob equal to `HEAD:path`. For T specifically, both future execution-version `TASK_CURRENT.md` and future task-copy must separately pass that gate and then have equal raw SHA-256 values. Preserve the Repair1 acyclic Owner sequence and the distinction between present zero-science `TASK_CURRENT.md` and absent future execution content/task-copy. Do not assert that the current zero-science task already passes future execution requirements.

Preserve distinct non-authority schema, `active=false`, `execution_authorized=false`, all future authority hashes `PENDING/ABSENT`, exact current protected/source hashes, all historical REJECTs and limited ACCEPT scopes, two prohibited `--execute` probes, old consumed attempt and `CALL_LEDGER_UNRESOLVED`, zero new C9/C10/retry/resume/model/science calls, and Results eligibility `FALSE`. At most **one** no-model, read-only structural check may verify the added committed-file wording, both T checks, preserved order/absence and nonauthority state using structured JSON parsing; record command, exit code and result. On failure stop without a second run or further edit. Stage only the three paths, make one local candidate commit, and report commit/parent/tree, `HEAD:src`, three post-commit raw SHA-256 values, clean tracked/index state, protected hashes and absent authority paths. Stop for independent GPT Work ACCEPT/REJECT; no push or successor.

## Hard stop

Do not edit runner/source/tests, accepted proposal, Owner/review authority files, `CURRENT.md`, this task or protected outputs. Do not create R, C, O, future execution task-copy or new C9 root. Do not call runner static preflight, `--execute`, `execute_once`, `load_delegate`, `run_timed_action`, model or science. Owner A remains zero-science preparation only; no C9/C10 scientific attempt, retry or partial resume is authorized.
