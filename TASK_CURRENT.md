# Current Builder Task - C9 second stale inert assertion repair

Task ID: `CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_INACTIVE_AST_TEST_REPAIR_20260926`
Status: `ACTIVE__ZERO_SCIENCE_TEST_AND_EVIDENCE_ONLY`
Assignee: Codex project `Zotero-Analytical-Workflow`, conversation `第五章 K1B 静态 runner 审查后接续` (`01a0dcd7-2acc-7571-b292-5807a0be0b1d`) only.
Worktree: `D:\ProjectTemp\c5k1bturn56` only. Never access `deep-learning-hank` or Zotero repository files.

## Start gate

Read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, this task, `REVIEW_GATE.md`, `AGENTS.md`, and `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_FULL_INERT_TEST_FAILURE_INDEPENDENT_REVIEW_20260926.md`. Confirm task-issuance HEAD is a direct child of `a2b36768`, `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`, and the only tracked worktree change is the preserved one-hunk test edit with raw SHA-256 `23D4CF2BC92A50E022BE3B1EAFC6958E7815B452C8B3A7F3C1FCF90A50E5EFC9`. Confirm only the five protected untracked output roots remain and their manifest hashes match the review; confirm the new C9 root, live contract, Owner execution adoption/task and runner-recognized ACCEPT review are absent. Stop on mismatch. Do not revert the preserved test edit.

## Allowed work

Modify only these three existing paths:

- `tests/test_mp4c_k1b_turn9_post_failure_new_attempt_preflight.py`
- `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_STATIC_RUNNER_CANDIDATE_20260926.md`
- `EVIDENCE/ch5_k1b_c9_post_failure_new_attempt_static_runner_20260926/static_receipt.json`

Preserve the already-made `execute_once` source-order assertion repair. Replace only the stale direct-`lexists` demand in `test_repair3_preflight_has_distinct_fail_closed_inactive_and_active_branches` with a check that the inactive branch calls `authority_file_absent` for its future authority paths. Retain the other inactive/active separation and no-execution assertions. Do not edit either runner or broaden behavior. Inspect the test file for prohibited execution calls before testing. At most one new inert full-file run is authorized: `python -m pytest -q tests/test_mp4c_k1b_turn9_post_failure_new_attempt_preflight.py`. Do not run it if inspection shows it would call a prohibited entry. On any failure, record the exact result and stop without a retry or further code edit.

If the check passes, update only necessary test counters, historical verdict/probe preservation, raw hashes, and candidate report/receipt evidence. Distinguish the prior failed full-file run from the new run. Do not claim whole-runner ACCEPT. Stage only the three allowed paths, make one local candidate commit, and deliver commit, parent, tree, `HEAD:src`, post-commit raw SHA-256 of all three paths, exact test result, tracked cleanliness, five protected manifest hashes and absent-authority/root checks. No push or successor.

## Hard stop

No `--execute`, `execute_once`, `load_delegate`, `run_timed_action`, `assert_active_authority`, model/scientific entrypoint, new C9 output root, live contract, Owner execution adoption/task, runner-recognized ACCEPT review, or protected-output mutation. No C9/C10 call, retry, or partial resume. The old actual call ledger remains `CALL_LEDGER_UNRESOLVED`, the full-old-turn charge is governance accounting only, and Results eligibility is `FALSE`. Stop for fresh independent GPT Work ACCEPT/REJECT. Any later C9 scientific attempt requires separate explicit Owner one-shot authorization and final dispatch review.
