# C9 timed-wrapper reconcile — zero-science repair candidate

Status: **candidate pending independent GPT Work ACCEPT/REJECT**. Results eligibility remains `FALSE`. The consumed `C9_TIMED_RISK_RUN001` has not been retried or resumed; no C10 attempt was made.

## Exact change

The timed wrapper's `MeasuredGuard.reconcile` now accepts `province: int | None = None` and forwards it to `BudgetGuard.reconcile(ledger, province)` (`validators/multi_province/k1b_turn9_timed_risk_exception/run.py:398-399`). This matches the delegate's normal-return and exceptional `guard.reconcile(ledger, province)` calls. The existing parent reconciliation, subclass `reconcile_province` dispatch, journal, and timing-interval code remain in place. A signature review of `begin_province`, `reconcile_province`, `reserve`, `enter`, `reconcile`, and `reconcile_all` found no other mismatch against the delegate; no other override changed. The source delegate, budgets, tests outside the timed-wrapper test file, and live contract were not edited.

The added inert regression creates the real `MeasuredGuard` subclass through an in-memory fake delegate action. It calls `reconcile(ledger, 0)`, checks the guard's reconciled selector count, per-province count, reconciliation journals and closed province interval, then checks that an over-limit provincial selector count raises `BLOCKED__PROVINCE_BUDGET`. The fake journal is an in-memory list; its fake action does not call delegate science or create an output root. A sentinel stops the mocked wrapper flow before sealing.

## Verification and limits

First selection: `python -m pytest -q tests/test_mp4c_k1b_turn9_timed_risk_exception_preflight.py::test_measured_guard_reconcile_accepts_province_and_preserves_denial` — **failed before the fake action** because the test initially used repository `ROOT`, where the protected C9 output root already exists; the wrapper correctly returned `BLOCKED__C9_OUTPUT_EXISTS_OR_UNSAFE`. The test was changed to use pytest's temporary directory. Permitted follow-up selection: `python -m pytest -q tests/test_mp4c_k1b_turn9_timed_risk_exception_preflight.py -k measured_guard_reconcile_accepts_province_and_preserves_denial` — **1 passed, 13 deselected**. No further tests were run. The test asserts that its temporary C9 output root was not created. `git diff --check` passed.

The old wrapper raw SHA-256 was `0E43522B64F7BD34C46C92A967F41FBDD373C3DD15DCC188821CB0EDB3AB368B`; the candidate raw SHA-256 is `59A63E933BF13A4FC39EC583227B2E9724B5E06B510A1896CB1307DBCC8F1D06`. The unchanged live contract still binds the old hash. Its production gate is therefore intentionally stale for this candidate; this is a future authority step, not an invitation to rebind or bypass it here. The inert test verifies the interface and one budget-denial path, not scientific correctness or a complete C9 execution.

Next gates, in order: independent repair ACCEPT/REJECT; separate review of the new wrapper identity and contract proposal; Owner adoption of the exact reviewed identity; then a distinct Owner decision and explicit one-shot science budget. The consumed attempt grants no retry, partial resume, or C10 authority.
