# Independent Work review: turn6 same-frozen-input repeat runner

Date: 2026-09-24 (Asia/Shanghai)

Verdict: `REJECT__TURN6_SAME_FROZEN_INPUT_REPEAT_RUNNER__EXECUTION_GUARDS_INCOMPLETE__ZERO_SCIENCE`

## Candidate and valid work

Work dispatch `b0bd3eb981a0c8848666d4ebae86d045875dddd1`; initial Builder candidate `071839ec14b280550621fbf43852a184e6154d7f`; allowed-path continuation `c2a413c3` is current HEAD. The combined candidate changes only the four paths authorized by the preparation task. Worktree is clean and `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`. Seven focused static tests passed. Literal scientific/model call ledger is zero; no replay or turn7 household has run.

The intended object is correctly bound: sealed entering-turn6 C5 is evaluated once as turn6 to form C6-prime, compared against sealed C6. The nine carrier fields and four static difference formulas preserve the accepted proposal. No `1e-6` repeatability threshold, stopping law, MATLAB original predicate, GE or Results claim was introduced.

## Blocking findings

1. `validators/multi_province/k1b_turn6_same_frozen_input_repeat/run.py` leaves `base.TASK_RELATIVE` at the older task when it calls `base._task_hashes()` and `_solve_province`. The new execution task is therefore absent from the source solver's continuing task-hash gate and source binding. Bind the exact future task path before the scientific call and restore the original global in `finally`; bind its hash in preflight and post-execution checks.
2. The runner reserves an aggregate integration envelope but does not place every labor/K1B/C1/firm/wage/monetary/fiscal/raw-next operation behind a separate entry-before-call guard. Its `finally` copies ledger counts directly into the guard without a ceiling check. A repeated category could exceed its ceiling and still proceed. Add reversible per-category entry wrappers or equivalent pre-call guards, preserve failed attempts, and reconcile against ceilings on every exit.
3. `compare_intermediates()` derives KFE paths by glob instead of requiring the canonical 31 provinces; a missing province can be silently omitted. It compares only selected JSON numeric fields, excluding available KFE distribution arrays and source labor, firm raw/used return, and next K1B receipt data. Reference intermediate files are not all bound to the accepted sealed manifest. Missing/nonfinite/shape-conflicting data need explicit `UNAVAILABLE` or legality failure; an `EXACT_BITWISE_MATCH` label must state precisely which numerical objects it covers.
4. A preflight or future-task gate failure happens before the runner creates a persistent first-failure receipt. Specify and implement a disjoint local failure evidence path with a zero-call ledger. The preparation receipt also omits its own required output readback, `git diff --check` and clean-after-commit evidence; repair the report/receipt accordingly.

## Terminal and next gate

This is a bounded engineering repair within the already authorized zero-science preparation route. The four paths may be repaired under a new task. No scientific execution, replay, new tolerance or additional budget is authorized by this verdict. Work must independently review the repaired candidate before issuing a distinct one-shot execution task. Results eligibility remains `FALSE`.
