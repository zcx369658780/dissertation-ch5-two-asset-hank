# Current Builder Task — C9 Repair2 final-entry static verification

Task ID: `CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_FINAL_ENTRY_STATIC_VERIFICATION_20260926`
Status: `ACTIVE__ZERO_SCIENCE_STATIC_VERIFICATION_ONLY`
Assignee: Codex project `Zotero-Analytical-Workflow`, conversation `第五章 K1B 静态 runner 审查后接续` (`01a0dcd7-2acc-7571-b292-5807a0be0b1d`) only.
Worktree: `D:\ProjectTemp\c5k1bturn56` only. Never access `deep-learning-hank` or Zotero repository files.

## Authority and fixed baseline

Owner adopted the additional C9 budget and old-failure governance charge for zero-science preparation only. No scientific execution is authorized. The handoff commit is `d55e12d4af0e187efb68af727e16b78afec70942`; the Work task-issuance commit must be its direct child, with `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`. Repair2 candidate `e860a54ac3fed1d104009a068722b1045bd87b5f` remains independently REJECTED because its final `load_delegate` and `run_timed_action` gates were changed after the last test. Preserve that verdict, the original candidate and Repair1 REJECT verdicts, and the original two prohibited `--execute` test probes as violations. Old `C9_TIMED_RISK_RUN001` is consumed; actual calls are `CALL_LEDGER_UNRESOLVED`, while the full-old-turn charge is governance accounting only. Results eligibility is `FALSE`.

Before writing, verify the task-issuance HEAD and its parent, source tree, tracked cleanliness, exactly five protected untracked output roots and their five manifest SHA-256 values against `docs/CH5_K1B_WORK_SESSION_HANDOFF_AFTER_C9_STATIC_REPAIR2_20260926.md`. Verify the proposed new C9 output root and its live contract, execution adoption and task are absent. Stop and report any mismatch without repair.

## Allowed work

Write only these three existing paths:

- `tests/test_mp4c_k1b_turn9_post_failure_new_attempt_preflight.py`
- `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_STATIC_RUNNER_CANDIDATE_20260926.md`
- `EVIDENCE/ch5_k1b_c9_post_failure_new_attempt_static_runner_20260926/static_receipt.json`

Add focused AST/source-order tests that read the final committed wrapper bytes without calling runner functions. Verify that `load_delegate` performs sealed-evidence, protected-manifest and new-output-path gates before committed contract/delegate checks and module import/`exec`; verify that `run_timed_action` performs those gates before `load_delegate`, `future_gate`, output claim or clock sampling. Inspect the tests for prohibited calls, then run only the focused inert test selection once. If a test fails, record the observed failure and stop; do not edit either runner or repeat the test under this task. No broader suite or science call is authorized.

Update the report and receipt with the focused test command/result, zero-science ledger, unchanged protected hashes, absent authority/output paths, and distinct historical original/Repair1/Repair2 outcomes. Retain the original two-probe violation and all three independent REJECT verdicts. Do not claim that static checks prove future runtime behavior, a resolved old ledger, C9 completion or Results eligibility.

Make one local candidate commit staging only the three allowed paths. In the final delivery to GPT Work, provide candidate commit, parent and tree IDs, `HEAD:src`, and post-commit raw SHA-256 of the five original candidate paths (wrapper, delegate, test, report, receipt), including the receipt's own raw hash. Do not put a self-referential receipt hash inside that receipt. Recheck tracked cleanliness, the five protected manifest hashes and absence of the new root/live files after the commit.

## Hard stops

Do not call wrapper `--execute`, `execute_once`, `run_timed_action`, `load_delegate`, any model/scientific entrypoint, C9/C10, retry or partial resume. Do not create the new output root, live contract, execution adoption, execution task or independent-review file. Do not edit `src`, either runner, budgets, Owner decisions, protected outputs or unrelated files. Do not push or create a successor. A test failure, identity mismatch, unexpected write, or missing evidence is terminal for this task and must be reported without workaround.

The candidate remains pending a fresh independent GPT Work ACCEPT/REJECT. No new C9 execution may proceed without a later explicit Owner one-shot authorization and final dispatch review.
