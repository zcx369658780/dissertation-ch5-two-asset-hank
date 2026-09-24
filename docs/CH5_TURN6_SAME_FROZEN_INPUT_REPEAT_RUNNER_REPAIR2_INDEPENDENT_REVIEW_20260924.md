# Independent Work review: second turn6 repeat-runner repair

Date: 2026-09-24 (Asia/Shanghai)

Verdict: `REJECT__TURN6_SAME_FROZEN_INPUT_REPEAT_RUNNER_REPAIR2__COMPARISON_AND_EVIDENCE_OWNERSHIP__ZERO_SCIENCE`

## Candidate and verified repairs

Reviewed local candidate `b178c2f5c6d149f7a254f07bef02c396db417232`, parent `4f3e0e905a916fa5d4536c30596cf175976c125b`. The worktree is clean. Its changed paths are exactly the four allowed paths; `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`; the future output root is absent. `git diff --check` passes and the focused zero-science suite passes 19/19. No replay, model call or turn7 household ran.

The prior NumPy index serialization, finite subtraction overflow, orientation/structure mismatch, raw-vector pre-construction guard, integration category guards and post-gate failure boundary are substantially repaired. Seventy sealed C6 old-versus-old intermediate comparisons are exact for their stated scope and strictly JSON serializable. This is a comparator check only, not repeatability evidence.

## Remaining blockers

1. `run.py:318-321`: `structural_conflict()` accepts any pair of 64-character hexadecimal SHA strings as equal. Changing only the labor receipt's `lt_matrix_sha256` to another valid digest still makes `compare_receipt()` report `EXACT_BITWISE_MATCH`. The labor matrix is not separately numerically compared among the 70 reference artifacts. Record a changed digest as a distinct array identity difference or `UNAVAILABLE` for the unverified array; do not present the whole receipt as exact. Test this concrete negative case.
2. `run.py:400-410`: `compare_array()` accepts `int64` but converts both arrays to `float64` before subtraction. `2**53` versus `2**53+1` produces a bitwise mismatch with `max_absolute_difference: 0.0`. Use exact integer difference arithmetic with a finite serializable result, or classify unsupported integer differences `UNAVAILABLE`; test the boundary. This is material to the accuracy of the promised numerical receipts.
3. `run.py:649-674`: `run_after_valid_gate()` checks that the output root is absent, but does not track whether this execution created it. If another process creates the root before the action does, the action's exclusive mkdir fails; the outer exception handler then sees the existing root and writes `first_failure.json` into a directory it does not own. This violates the no-overwrite/disjoint-evidence rule. Record exclusive ownership of the root and write failure evidence only when ownership has been established; if another process wins, stop without touching its files. Use an inert stub to test this race path.

The first two findings have direct static reproductions; the third follows from the explicit check/create/error branch and can be reproduced with a stub. The current 19 tests do not cover them. No substantive science decision is needed for these mechanical fixes.

## Next gate

Issue only a four-path, zero-science repair task. Do not issue the one-shot repeat execution task or use its proposed call ceilings yet. After a new Builder candidate, Work must independently ACCEPT/REJECT it. Results eligibility remains `FALSE`.
