# Current Builder Task

Task ID: `CH5_K1B_TURN7_R2_RUNNER_PREPARATION_ZERO_SCIENCE_20260925`

Status: `ACTIVE__BOUNDED_TURN7_RUNNER_PREPARATION__ZERO_SCIENCE__WORK_REVIEW_REQUIRED`

## Authority and baseline

Owner adopted the future frozen bounded K1B outer criterion in `docs/CH5_FULL_OUTER_STATE_STOP_FAILURE_BUDGET_OWNER_ADOPTION_20260925.md`, committed at `2d43179bc9e9348efe8f61c19217ee10be6bd5d3`. The adopted law is nine same-stage components, every difference strictly `<1e-6` at two consecutive complete legal adjacent transitions C6→C7 and C7→C8 (R2); clipped `ra` upper hits are recorded but do not disqualify the new criterion; first failure stops with zero retries; maximum budget is the exact proposal table plus the three explicit category resolutions in the Owner adoption. This task prepares **turn7 only**, with **zero scientific/model calls**. It is not an execution authorization and does not prepare a hidden turn8 call.

Work only in `D:\ProjectTemp\c5k1bturn56`. Never access `deep-learning-hank`. Read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, this task, `REVIEW_GATE.md`, the Owner adoption, the accepted stopping/failure/budget proposal and independent review, the accepted one-shot repeat review, and directly relevant accepted turn5/6 and repeat runners/test/receipts. Before edits verify HEAD descends from `2d43179bc9e9348efe8f61c19217ee10be6bd5d3`, `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`, and the only pre-existing untracked path is the preserved `reports/ch5_turn6_same_frozen_input_repeat_20260923_run001/` output. Preserve that root byte-for-byte. The planned new turn7 output `reports/ch5_k1b_turn7_outer_r2_20260925_run001` must be absent.

## Exact Builder write allowlist

1. `validators/multi_province/k1b_turn7_outer_r2/run.py`
2. `tests/test_mp4c_k1b_turn7_outer_r2_preflight.py`
3. `docs/CH5_K1B_TURN7_OUTER_R2_RUNNER_PREPARATION_20260925.md`
4. `EVIDENCE/ch5_k1b_turn7_outer_r2_runner_preparation_20260925/preparation_receipt.json`

These four paths are the entire write set. Do not edit production `src/`, accepted old/repeat runners, accepted tests, governance files, sealed C6 input/plan/reference, the untracked repeat output, or any scientific output root. Stage only the four explicit paths for one local candidate commit. No push, PR, successor task or self-acceptance.

## Required future runner contract, without running it

1. Default CLI performs read-only static preflight only. Any future `--execute` path must require a distinct future active `TASK_CURRENT.md`, byte-identical archived task, exact task ID `CH5_K1B_TURN7_OUTER_R2_EXECUTION_20260925`, execution ID, committed unchanged runner, approved output root and a separate Work dispatch. Do not create that future task or execution ID now. Invalid gate writes nothing and imports no model.
2. Bind the **sealed completed C6** entering-turn7 JSON and NPZ in `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/`, not the new untracked C6-prime repeat output. The input hashes are JSON `D84E9D74C7E965A3B492F2F0F9A63D3320D436DD4A6D78E1E655F014C05FC059`, NPZ `37A1258F8EC87116F03084D8178C77424FDD5F3859A1BC73D9704940A3B9381E`, sealed manifest `51F636DF222DD1365B017091B6F77F78A71C606F84776CDFB62457105F2E9127`, frozen `src` tree above. Check province order, S destination-by-origin, share columns, entering state/plan bit identities, lagged raw return/rah and exact helper/runner identities before the first call and after the one turn.
3. Future turn7 may start at most once, with 31 per-province accepted household HJB/KFE paths and exactly one integration only after 31/31 PASS; no turn8 household in this runner. Encode the Owner-adopted **per-turn** ceiling table from `docs/CH5_OUTER_STOP_FAILURE_BUDGET_CONTRACT_PROPOSAL_20260923.md` SHA-256 `5D3BFE7B914DE3F6BE3B99E75E80680B18A4054FB186EBB715D865F4008DEAC6`, plus `scalar_selector_root_invocations <=20,000,000/province and <=620,000,000/turn`, `terminal_kfe_attempts <=1/province and <=31/turn`, and `k1b_feedback_calls <=1/turn` as the same frozen allocation alias. Track turn7 household batch as one allowed attempted event rather than inheriting the old turn5/6 runner's `turn7_household_calls=0`. Preserve zero retries, solver substitutions, K2/GE/MATLAB/Results and turn8 household. Failed entries consume budget; use pre-entry guards and source-ledger reconciliation, with `CALL_LEDGER_UNRESOLVED` if exact counts cannot be resolved. Do not copy the old combined ledger's turn7-zero rule into this new task.
4. Use a new, disjoint, exclusively claimed output root and root-bound exclusive JSON/NPZ writes. Cover every reachable reused-code filesystem mutation, reject symlink/reparse components, fail closed on root loss or replacement, and preserve the earliest terminal plus available guard/source ledger in raised detail if no safe receipt can be written. State the residual operating-system check-to-operation rename race honestly. Do not overwrite historical or repeat evidence.
5. Seal/read back a complete C7 entering-turn8 candidate/plan only after legal turn7. Compare the complete C6 and C7 checkpoints using the adopted nine formulas, legal denominator/shape/finite/axis checks, strict `<1e-6` per component, bitwise counts, full-precision differences and argmax. Report clipped `ra` upper hits separately and retain the original MATLAB zero-hit predicate as distinct. A legal threshold miss is `VALID__NINE_COMPONENT_LEVEL_NOT_MET`, not a failure. One turn7 pass is **not** R2 success; only a future separately tasked C7→C8 comparison can confirm the second pass. Do not infer fixed point, GE or Results.
6. Add focused inert/static tests for task-gate no-write, sealed identity rejection, exact per-province/per-turn budgets and failed attempts, ledger uncertainty, output ownership/mutation/symlink guards, C6→C7 comparator formula/strict-boundary cases and clipped-`ra` report-only separation. Preserve original source semantics. Tests must not import or invoke the model evaluation, replay, HJB/KFE, integration, firm or turn7 household.
7. Record exact code/test/report/receipt hashes, source and input identities, static test results, changed paths, planned output absence, first blocker if any, `git diff --check`, and a literal all-zero task-scoped scientific/model ledger. After commit report the candidate SHA and the expected preserved untracked repeat root separately; do not call the worktree clean while that root remains.

## Stop and terminal

If any required guarantee needs production `src/` changes, a new scientific law, a model call, an extra write path, or cannot preserve exact call accounting, stop at the first blocker. Do not weaken the adopted contract, fabricate a future task, run old `execute()`, run new `--execute`, or create the planned turn7 output. No retry or budget reset is authorized.

Success terminal: `K1B_TURN7_R2_RUNNER_CANDIDATE_READY__ZERO_SCIENCE__WORK_REVIEW_PENDING`. GPT Work must independently ACCEPT/REJECT this runner before any separate turn7 execution task. `Results eligibility = FALSE`.
