# Independent Work review: third turn6 repeat-runner repair

Date: 2026-09-24 (Asia/Shanghai)

Verdict: `REJECT__TURN6_SAME_FROZEN_INPUT_REPEAT_RUNNER_REPAIR3__OUTPUT_WRITE_OWNERSHIP_GAP__ZERO_SCIENCE`

## Candidate and verified repairs

Reviewed local candidate `6418ec014fd67766016f097fa2b547753a54a24f`, parent `20b1e0f95a3573425701859610bdaf871e5bb0a8`. Its four changed paths match the task allowlist; worktree clean; `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`; planned output absent; diff check passes. Focused zero-science tests pass 22/22, default preflight passes, and no model or scientific call ran.

The changed labor matrix digest is now explicitly `UNAVAILABLE` rather than exact; `int64` differences across the `2**53` boundary use exact Python integers. The sealed 70-item old-versus-old comparison strictly serializes. Integration entry guards and category reconciliation remain intact. The output-root claim handles a foreign creator that wins before this execution's claim.

## Blocking finding

`run.py:81-83` writes ordinary JSON receipts with `parent.mkdir(..., exist_ok=True)` and `write_text()`, which can recreate a removed output root and overwrite an existing same-name file. `claim_output_root()` records directory identity at lines 98-101, but ordinary writes at preflight, scientific-ledger, comparison and terminal receipt paths do not verify that identity. If the claimed root is replaced before one of those writes, the runner can write into a root it no longer owns. This defeats the task's no-overwrite and exclusive-evidence rule. The current race test covers only another process winning **before** the claim.

Use an output-root-bound write primitive for all future run receipts: verify the claimed root identity, do not recreate it from a child write, create each receipt exclusively, and fail closed if the root or target file changed. Cover an inert claim-then-replace case for preflight and terminal receipt writes. Preserve the existing first-failure and consumed-ledger behavior when the root remains owned. A path-based check may not eliminate every concurrent operating-system race; report any residual limit honestly rather than claiming a perfect atomic guarantee.

## Next gate

Issue only a four-path, zero-science repair. No one-shot repeat execution task or scientific budget is yet authorized. Work must independently ACCEPT/REJECT the next Builder candidate. Results eligibility remains `FALSE`.
