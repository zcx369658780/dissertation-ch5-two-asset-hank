# Current Builder Task - output guard test/evidence correction, zero science

Task ID: `CH5_K1B_C9_POST_FAILURE_OUTPUT_GUARD_ZERO_SCIENCE_REPAIR1_20260927`
Status: `ACTIVE__TEST_AND_EVIDENCE_ONLY__NO_SOURCE_EDIT_OR_SCIENCE`
Assignee: Codex project `Zotero-Analytical-Workflow`, conversation `第五章 K1B 静态 runner 审查后接续` (`01a0dcd7-2acc-7571-b292-5807a0be0b1d`) only.
Worktree: `D:\ProjectTemp\c5k1bturn56` only. Never access `deep-learning-hank` or Zotero repository files.

## Start gate

Read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, this task, `REVIEW_GATE.md`, `AGENTS.md`, the rejected repair review, candidate report/receipt and the accepted diagnosis. Require the issuing Work commit as `HEAD`, tracked/index clean, `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`, and exactly six protected untracked output roots. Recheck all six protected manifest hashes and new partial readback hash recorded in the rejected repair receipt. Stop on mismatch. The old and new C9 attempts remain consumed; neither actual call ledger is resolved.

## Allowed work and stop conditions

The delegate `validators/multi_province/k1b_turn9_post_failure_new_attempt_outer_r2/run.py` is frozen in this task. Modify only `tests/test_mp4c_k1b_turn9_post_failure_new_attempt_preflight.py`; create only `docs/CH5_K1B_C9_POST_FAILURE_OUTPUT_GUARD_ZERO_SCIENCE_REPAIR1_REPORT_20260927.md` and `EVIDENCE/ch5_k1b_c9_post_failure_output_guard_zero_science_repair1_20260927/repair1_receipt.json`. Do not change `CURRENT.md`, this task, contracts, Owner/review files, R/O/T, budgets, frozen `src`, other runners or protected output roots.

Add one inert regression that replaces the owned root **after the first successful `owns_output_root` call inside `guard_output_mkdir` and before its final ownership check**, using only a disposable temporary directory. Require the guard to block before original `Path.mkdir` can mutate the replacement root; assert bounded `root_not_owned` failure detail. Do not mislabel this as atomic safety against a replacement after the final check. If the regression fails, stop and report the defect without editing the delegate or using a second test invocation.

At most one focused inert test invocation is allowed for this task; no preflight, `--execute`, wrapper launch, model import or scientific entry. The new report must qualify the prior candidate's root-replacement guarantee as detection at the tested checks only, explicitly retain the post-final-check TOCTOU risk, and note that non-`mkdir` output-guard diagnostics remain outside scope. Report the previous `7 passed, 1 skipped` as historical candidate evidence, not this task's result; preserve the real-symlink environmental skip, both original prohibited `--execute` probes and all historical REJECT verdicts without reclassification. Include exact candidate/parent/tree/`HEAD:src`, raw changed-file/report/receipt SHA-256, one-test result, clean tracked/index status and protected hash identities.

The project multi-subagent rule applies: use at least three active agents for this code/test/Git work, with disjoint write ownership and separate implementation/review roles. The main Codex agent retains the sole Git, integration and handoff authority. Stage only the three allowed paths and make one local candidate commit. Stop for independent GPT Work ACCEPT/REJECT; no push or successor. This task grants no scientific execution, retry, partial resume, C10, Results claim or budget reset. Results eligibility remains `FALSE`; future science requires a fresh explicit Owner decision and new independently reviewed R/C/O/T chain.
