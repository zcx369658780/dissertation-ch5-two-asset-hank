# Initial independent engineering review

Date: 2026-09-30. Work verdict: ENGINEERING_REJECT_PENDING_BOUNDED_REPAIR.
Independent reviewer: wedge_engineering_review, GPT-6.1 Sol / high; read-only.

Reviewed helper SHA-256: D09C8E28307407D3AD31292E1E10C25224177DED067ECCE9380C0C3AFF78E83C.
Reviewed test SHA-256: A185A201A3185FA9FE02049F275B89D0C1FBC1B51442485AB650D0857E108F81.
Initial evidence: one direct synthetic invocation, 12 tests, exit 0. No review test or science was executed.

Required findings:
1. Provenance enum fields input_kind, population_basis and price_basis must be built-in str before equality/allowlist checks. A mutable custom equality object otherwise passes and survives in the frozen output binding, violating the immutable snapshot contract. Reject such objects and str subclasses in synthetic tests.
2. Distinct near-equal per-capita GDP values may round a non-diagonal coefficient to 1. Example raw GDP 1.0 and 1.0000000000000002, population both 1.0, amplitude 0.3. Explicitly reject loss of the required richer-destination direction; do not clip or use nextafter. Add a synthetic regression fixture.

Work concurs with both findings and dispatched a repair to the same designated Builder under the existing concrete-fix test budget. This does not change the formula, authorize integration, renew science budgets or establish scientific acceptance. C9 remains paused; historical ledgers CALL_LEDGER_UNRESOLVED; Results eligibility FALSE.
