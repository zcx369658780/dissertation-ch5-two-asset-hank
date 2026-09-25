# Current Builder Task

Task ID: `CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_RUNNER_REPAIR5_20260925`

Status: `ACTIVE__BOUNDED_RUNNER_REPAIR__ZERO_SCIENCE__WORK_REVIEW_REQUIRED`

## Authority and baseline

GPT Work independently rechecked the clean local dispatch HEAD `f2ceaf20dd8447aa0dc20c1e6455aca0953f255d`, `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`, the absent planned output root `reports/ch5_turn6_same_frozen_input_repeat_20260923_run001`, and the REJECT of candidate `ea19d0ad8131f46e3275a0d7ecc28cd596cfbf18` in `docs/CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_RUNNER_REPAIR4_INDEPENDENT_REVIEW_20260924.md`. This task is the next zero-science engineering repair under that REJECT. It does not authorize the C5-to-C6-prime repeat.

Work only in `D:\ProjectTemp\c5k1bturn56`; never access `deep-learning-hank`. Before editing, read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, this task, `REVIEW_GATE.md`, the cited REJECT, and directly relevant runner/test/report/receipt. Verify the dispatch commit is a descendant of `f2ceaf20dd8447aa0dc20c1e6455aca0953f255d`, the worktree is clean, `HEAD:src` is unchanged, and the planned output root remains absent. If any check fails, stop and report the first blocker. Local commit and evidence are authority; GitHub is not a daily gate.

## Exact Builder write allowlist

1. `validators/multi_province/k1b_turn6_same_frozen_input_repeat/run.py`
2. `tests/test_mp4c_k1b_turn6_same_frozen_input_repeat_preflight.py`
3. `docs/CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_RUNNER_PREPARATION_20260923.md`
4. `EVIDENCE/ch5_turn6_same_frozen_input_repeat_runner_preparation_20260923/preparation_receipt.json`

These four paths are the entire Builder write set. Preserve unrelated files. Do not edit production `src/`, the older turn5/6 runner, sealed inputs/reports, governance files, equations, grids, budgets, tolerances, stopping laws, or output roots. Stage explicit allowlisted paths only for one local candidate commit. No push, PR, successor task, or task-state change.

## Required repair

1. Close the root-ownership gap around every filesystem mutation reachable through the reused scientific code in the future repeat path, including province/checkpoint/terminal directory creation and compact-checkpoint deletion. Establish a bounded guard before entry and at the mutation paths so a missing or replaced claimed output root fails before recreating or touching a foreign root. Retain the existing root-bound exclusive JSON/NPZ writes, first-failure behavior, scientific semantics, and call budgets. If a safe guarantee cannot be established within this allowlist, stop and report the precise unguarded operation and residual risk; do not weaken the contract silently.
2. On an output-root ownership failure where no receipt may safely be written, raise a self-contained failure detail containing the earliest original terminal, all available `guard.attempted` and source call-ledger counts, and whether reconciliation resolved those counts. Use `CALL_LEDGER_UNRESOLVED` when accounting cannot be established; do not convert an attempted call to zero or discard an earlier terminal.
3. Reject symlink or reparse-point replacement of the claimed root before identity comparison where the host supports that check. Cover both the root and relevant path components used by mutations/writes. If the host cannot provide the necessary check or stable identity, fail closed and document the exact remaining operating-system race limit. Do not claim absolute atomicity based on `Path.stat()` or a check followed by a separate path operation.
4. Add inert static/stub tests for root loss or replacement immediately before representative reused `mkdir` and `unlink` operations, a symlink/reparse replacement that points back to the original inode when supported, and ownership loss after attempted calls with earliest terminal plus attempted/source/resolution ledger in the raised detail. Retain prior comparison, 70-item structural/digest, exact `int64`, integration guard, exclusive receipt, and first-failure regression coverage. No test may invoke model science.
5. Update the preparation report and receipt after code/tests are final with exact hashes, focused test results, changed-path readback, frozen `src` identity, absent planned output root, literal zero-science ledger, and first failure if any. Check `git diff --check` before committing; report postcommit clean state and commit SHA separately. Do not place the future commit SHA into a precommit receipt.

## Budget and stop rules

Scientific/model calls: **zero**. No replay, household HJB/KFE, integration, firm, turn7 household, K2, GE, annual dynamics, shocks, IRFs, welfare, or Results. Do not run either old `execute()` or new `--execute`; do not create the planned replay output root. Static inspection, inert stubs, focused zero-science tests, and default static preflight are allowed. If a repair needs a production-source change, a new scientific law, a scientific call, or cannot preserve call-accounting evidence, stop at the first blocker and record it within the allowlist where feasible. No retry or scientific budget reset follows from this task.

Success terminal: `TURN6_SAME_FROZEN_INPUT_REPEAT_RUNNER_REPAIR5_CANDIDATE_READY__ZERO_SCIENCE__WORK_REVIEW_PENDING`. Return the local candidate commit, exact changed paths, hashes, checks, literal zero-call ledger, and limitations. GPT Work must independently ACCEPT or REJECT this candidate before any separate one-shot repeat task can be considered. Results eligibility remains `FALSE`; `1e-6` is diagnostic precision only, not a stopping law.
