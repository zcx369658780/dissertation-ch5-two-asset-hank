# Current Builder Task

Task ID: `CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_POSTCOMMIT_STATIC_VERIFICATION_20260925`

Status: `ISSUED__ONE_STATIC_TEST_ONLY__NO_CODE_EDIT__WORK_REVIEW_PENDING`

GPT Work issues this task only to “第五章 K1B 跨天继续接续” (`01a0d867-be22-7d93-b2fb-0ddff659b686`) in `D:\ProjectTemp\c5k1bturn56`. The prior runner candidate `45ba72ea611af9a72fb23f33b4f3cf8b5b13b2cf` was independently REJECTED because its two-run static test budget ended without PASS. This new task is a separate, explicit **one-run post-commit verification**, not an extension of the old budget. Never access `deep-learning-hank`.

## Entry gate

Before testing, verify HEAD is a committed descendant of `45ba72ea611af9a72fb23f33b4f3cf8b5b13b2cf`; the exact runner and test blobs still equal those in that candidate; `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`; no tracked dirt; exactly the protected C6-prime, C7 and C8 untracked roots with full manifest hashes from `docs/CH5_K1B_CODEX_SESSION_HANDOFF_20260925.md`; and the candidate measurement output root is absent. Read the current independent REJECT review. Stop at the first mismatch.

## One verification and exact write allowlist

Run **exactly once**, and only after the entry gate passes:

`python -B -m pytest -q -p no:cacheprovider tests/test_mp4c_k1b_turn8_same_frozen_timing_measurement_preflight.py`

Do not run any other test, `--execute`, model, or scientific call. Capture the command's exact exit code, pass/fail/skip count and the first failure if any. Verify that the test did not create the candidate measurement root or change protected outputs. Then write only:

1. `docs/CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_POSTCOMMIT_STATIC_VERIFICATION_20260925.md`
2. `EVIDENCE/ch5_k1b_turn8_same_frozen_timing_runner_postcommit_static_verification_20260925/verification_receipt.json`

Record the unchanged runner/test commit/tree/blob and SHA-256 identities, dispatch HEAD/parent, protected manifest hashes, test result, all-zero task scientific/model/failed/retry ledger, report hash, and the exact next independent Work gate. If the test fails, preserve the first defect without editing or rerunning; do not reinterpret a failure as PASS. If it passes, state only static verification PASS, not scientific or runner acceptance. Verify JSON, hashes, two-path diff and `git diff --check`; stage and commit exactly the two allowlisted paths and return the candidate to GPT Work for independent `ACCEPT/REJECT`.

## Hard boundaries

No runner or test edits, no output root creation, no repair, no science, no retry, no Owner budget adoption, no automatic successor. This task does not authorize a C8 measurement or C9/C10. `BLOCKED__DURATION_BOUND_UNAVAILABLE` and `Results eligibility = FALSE` remain.
