# C9 post-failure output-guard diagnosis: independent GPT Work review

Verdict: `ACCEPT__ZERO_SCIENCE_DIAGNOSIS_ONLY__NO_REPAIR_OR_EXECUTION_AUTHORITY`.
Date: 2026-09-27 (Asia/Shanghai).

## Candidate identity and scope

- Candidate `eebf9ead0a1f2be9642479f12058070ae866bf33`; parent `b278da2b6324d3ddae2364fb87826a71cdc9462b`; tree `b1cc12a5303581d9eeabde7f80b1f37dca384821`; `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`.
- Exactly two added paths: `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_OUTPUT_GUARD_ZERO_SCIENCE_DIAGNOSIS_20260927.md` (blob `c888d179c96e432af6e15fdde67fb158bb117fdf`, raw SHA-256 `03B357AB09283FE672FD45901C4A651D94ABAF5646FB44FAB6611A9EDBA99579`) and `EVIDENCE/ch5_k1b_c9_post_failure_output_guard_zero_science_diagnosis_20260927/diagnosis_receipt.json` (blob `16b5450a3e58dba4492740b0ca23de9cf89c3faa`, raw SHA-256 `0841E74CE292A7334057EFDF4FBE3892D7C91F8EA0CAB9EC1B6A3B81935C0DAD`). No runner, test, source, authority or protected-output path changed in the candidate.
- At review, tracked/index were clean and the six expected protected untracked `reports/` roots were present. The original five manifest SHA-256 values and the new partial-manifest/readback SHA-256 values match the diagnosis receipt. The new failed-attempt root is local untracked evidence, not content sealed into this Git commit; this review independently checked its named top-level receipts by raw hash.

## Findings

The frozen source requests `province_root.mkdir(parents=True)` for province 0. The delegate's `guarded_mkdir` checks the complete path before calling the original `mkdir`; `path_components_safe` rejects a missing intermediate component and the caller maps that result to `BLOCKED__OUTPUT_COMPONENT_REPARSE_POINT`. This is a sufficient static explanation for the observed original terminal without a real reparse point. The persisted failure receipts lack the rejected path, failing component and `lstat` detail, so this review does **not** establish the unique runtime cause or the absence/presence of an actual reparse point.

The report correctly separates one confirmed `turn9_household_calls` attempt, zero persisted detailed counters, reserved exposure, and `CALL_LEDGER_UNRESOLVED` actual calls. The 11-entry partial readback `PASS` is not a completed outer turn, integration, or safe pause. The earlier two prohibited `--execute` probes and all historical REJECT verdicts remain unchanged. No tests, preflight, runner, model or scientific entry were used for this review.

## Boundary and next gate

The old `C9_TIMED_RISK_RUN001` and new `C9_POST_FAILURE_NEW_ATTEMPT_001` attempts are consumed; neither budget is restored. This ACCEPT is diagnostic evidence only. A separate zero-science engineering task may repair the output guard and exercise inert regressions, subject to a verified local backup before source changes and fresh independent review of its candidate. It cannot activate a contract, authorize `--execute`, retry or partial resume, start C10, or make a Results claim. Both actual call ledgers remain `CALL_LEDGER_UNRESOLVED`; Results eligibility is `FALSE`. Any future scientific attempt needs a fresh explicit Owner decision and a new reviewed R/C/O/T chain.
