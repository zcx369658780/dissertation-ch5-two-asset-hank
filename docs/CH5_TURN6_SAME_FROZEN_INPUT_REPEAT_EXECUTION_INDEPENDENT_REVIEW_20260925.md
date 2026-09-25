# Independent Work review: one-shot turn6 same-frozen-input repeat

Date: 2026-09-25 (Asia/Shanghai)

Verdict: `ACCEPT__TURN6_SAME_FROZEN_INPUT_REPEAT__ONE_PAIR_EXACT_ONLY__RESULTS_FALSE`

## Authority and outcome

Reviewed Builder evidence commit `e2791e5971eecdaa84a7bdc6fce0b7b0ffaf4f76` (parent `dca015404855fbf25fb4b496fb60ad91a1696043`) and the preserved, untracked output root `reports/ch5_turn6_same_frozen_input_repeat_20260923_run001`. The commit changes only the authorized concise execution report. The output root is deliberately untracked; the worktree is therefore **not clean**. Production `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883` remains frozen. The current and archived one-shot tasks are byte-identical. The sealed C5 input and sealed C6 reference JSON/NPZ hashes match the task.

The runner terminal is `PASS__TURN6_SAME_FROZEN_INPUT_REPEAT__ONE_PAIR_ONLY`, with no `first_failure.json`, `call_ledger_resolved=true`, and no guard denial. Thirty-one province terminal receipts and the one-turn integration receipt exist. The terminal receipt records 31 terminal KFE attempts and exactly one full integration, with turn7 household, K2, GE, scientific retries, solver substitutions, and other downstream scientific calls all zero. All 37 guarded attempted categories equal their corresponding source-ledger counts and remain within the task's explicit ceilings. No independent science was rerun during review.

## Independent artifact and comparison readback

I recomputed SHA-256 and size for all **5,141** pre-manifest files under the authorized root. The manifest's path set matches the actual pre-manifest file set exactly: no missing path, extra path or hash mismatch; total pre-manifest bytes are **63,888,760**. The manifest itself is preserved as the 5,142nd file. The default preflight receipt reports `PASS__STATIC_PREFLIGHT_ONLY`; the generated turn7 entering-bundle readback reports `PASS` and zero household calls.

The comparison receipt reports `EXACT_BITWISE_MATCH` for each of the nine outer-state components `Yt,Lt,wjt,rk,Kt_prev,w,raw_ra0,rah,S`: every bitwise mismatch count and diagnostic difference is zero. All 70 sealed-reference intermediate comparisons are also `EXACT_BITWISE_MATCH`; none is unavailable. This is a successful, bounded **one-pair** same-input repeat. It gives an observed exact pair under the recorded environment, not a general repeatability bound.

## Scientific boundary and next gate

This review accepts the execution evidence and comparison fidelity for the single authorized C5-to-C6-prime repeat. It does not adopt a stopping rule, contraction, fixed point, steady state, GE, turn7 household execution, or Results claim. `1e-6` remains diagnostic precision only. `Results eligibility = FALSE`.

The one-shot budget is consumed; no retry or second repeat is authorized. The preserved output root remains untracked but fully inventoried. The next legitimate work is zero-science synthesis of this result with the accepted outer-state stopping/failure/budget proposal for an Owner decision on the scientific stopping law and future budget. No further model call may begin before that decision and a separate bounded task.
