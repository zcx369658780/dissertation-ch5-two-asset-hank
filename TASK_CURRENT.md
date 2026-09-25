# Current Builder Task

Task ID: `CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_REPAIR1_ZERO_SCIENCE_20260925`

Status: `ISSUED__ZERO_SCIENCE_NARROW_REPAIR__WORK_REVIEW_PENDING`

GPT Work issues this repair only to “第五章 K1B 跨天继续接续” (`01a0d867-be22-7d93-b2fb-0ddff659b686`) in `D:\ProjectTemp\c5k1bturn56`. The post-commit static check passed, but independent code review kept the runner **REJECTED** for two exact defects in `docs/CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_POSTCOMMIT_STATIC_VERIFICATION_INDEPENDENT_REVIEW_20260925.md`. Do not access `deep-learning-hank` or send another conversation to write this tree.

## Entry gate

Verify HEAD is a committed descendant of `861789ed1dadedc40448443744309c43df63eba3`, `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`, no tracked dirt, and exactly the protected C6-prime/C7/C8 untracked output roots with full manifest hashes from `docs/CH5_K1B_CODEX_SESSION_HANDOFF_20260925.md`. Verify the measurement output root is absent. Read the current independent review and the existing runner/test; stop at the first mismatch. Preserve all protected roots and the accepted C8 runner/test.

## Exact four-path write allowlist

1. `validators/multi_province/k1b_turn8_same_frozen_timing_measurement/run.py`
2. `tests/test_mp4c_k1b_turn8_same_frozen_timing_measurement_preflight.py`
3. `docs/CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_REPAIR1_20260925.md`
4. `EVIDENCE/ch5_k1b_turn8_same_frozen_timing_runner_repair1_20260925/repair_receipt.json`

Fix only these two defects:

1. A future execute gate must bind the **new measurement wrapper's exact committed SHA-256** to a separate committed independent GPT Work `ACCEPT` review for that same wrapper and to the future Owner adoption, measurement contract and active task. A merely committed or self-declared wrapper is insufficient. Use a deterministic later review-document path and explicit exact hash/identity checks before output creation or science; if the review or bindings do not yet exist, fail closed. Do not loosen the accepted C8 delegate's existing hash gate.
2. Preserve the accepted C8 runner's original numerical terminal unchanged in the sealed science output and in the recorded `source_terminal`. Keep `COMPLETE_OBSERVED_ELAPSED_SAMPLE_ONLY` solely as the timing receipt's separate classification. Do not override `c8.turn8_terminal` or silently rewrite a failed/valid C8 numerical result.

Add inert/static tests for stale or missing independent review, mismatched wrapper hash in task/Owner contract, default no-science behavior, and preservation of an inert original terminal. Ensure tests of a future task gate explicitly isolate the pre-commit wrapper identity check when the runner is still being edited; do not misreport an expected pre-commit refusal as a science test. Existing output ownership, C7 entering identity, separate budget namespace, attempted-call accounting and other behavior must remain intact. Run only the named static test file at most **two** times with `python -B -m pytest -q -p no:cacheprovider`; if the second run fails, preserve the first defect, stop testing and report. No `--execute`, model import/call, measurement output creation or science.

The report and receipt must record the precise diff, source and protected-manifest hashes, candidate artifact hashes, test invocations/results, all-zero task scientific/model/failed/retry ledger, and first remaining gate. Verify JSON, hashes, only four changed paths and `git diff --check`; stage and commit exactly these four paths. Return commit, parent, tree, blobs, checks and unresolved gate for independent GPT Work `ACCEPT/REJECT`. Do not self-accept or issue a successor.

## Hard boundaries

No economic, solver, grid, tolerance, accepted C8 runner/test, frozen `src`, governance, or task-sheet edit. No Owner measurement budget/resource adoption or one-shot science authorization is implied. The C9/C10 duration prelaunch block remains `BLOCKED__DURATION_BOUND_UNAVAILABLE`; `Results eligibility = FALSE`.
