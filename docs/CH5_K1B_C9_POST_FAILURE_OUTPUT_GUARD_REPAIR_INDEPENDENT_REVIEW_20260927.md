# C9 output-guard zero-science repair: independent GPT Work review

Verdict: `REJECT__ROOT_REPLACEMENT_WINDOW_TEST_GAP_AND_OVERBROAD_CLAIM__NO_SCIENCE`.
Date: 2026-09-27 (Asia/Shanghai).

## Candidate and preserved facts

Candidate `5e40792d7ed921a58b5991e413d49cd907ad38b3`; parent `98a75859d495c35c6d26643bf45f0f6fbb14b651`; tree `c261467c5d7650d3ef74b644d93ffe3fdf31248c`; `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`. The commit changed only the allowed delegate and inert test, and added the allowed report and receipt. Tracked/index are clean; six protected untracked output roots remain, with all six manifest and the new readback raw hashes unchanged.

The pre-edit backup is independently checkable: bundle SHA-256 `07CAFD0BC6A4946C29F25C2A49F81A59DCABEA0737745CC1A01784B099025D6E`, backup-manifest SHA-256 `3CCD743A399370F4899562530D1E31A020D7C1C7C12B76518871454A811E34B0`, and 14/14 new-C9 failure files copied with matching byte count and SHA-256. The single focused inert test run recorded `7 passed, 1 skipped, 62 deselected`; the skipped case was a real directory symlink unavailable on this host, while simulated reparse passed. No preflight, `--execute`, wrapper, model or scientific entry was used in the candidate or this review.

## Blocking finding

The accepted diagnosis requested a regression for replacement of the owned output root **between checks**. The new `test_output_guard_mkdir_rejects_replaced_owned_root` replaces the root before calling `guard_output_mkdir`, so it verifies only detection at the first ownership check. The new guard also performs a final ownership check before calling original `Path.mkdir`; this distinct branch is untested. The report's statement that root replacement is blocked without qualification overstates the evidence. It must say which check-time replacement is detected and retain the post-final-check mutation window as an unresolved residual risk; the current code does not atomically bind the checked directory to the subsequent `Path.mkdir`.

The safe-missing-suffix path and checks for existing reparse attributes, `lstat` errors, and ordinary `parents=False` missing-parent behavior are supported within the focused test scope. But that does not cure the specified root-replacement evidence gap. New failure detail is implemented for the `mkdir` guard only; other output-guard paths still lack the same detail and are outside this narrow repair's authority. The original two prohibited `--execute` probes and every historical REJECT remain recorded and are not reclassified.

## Next gate

Only a separate zero-science **test/evidence correction** may proceed under a new task: exercise root replacement after the first successful ownership check but before the final check, correct the report's guarantee and provide a new receipt. Do not edit the delegate in that task. If the test fails, stop and return for a new scoped engineering decision. This REJECT does not restore either consumed C9 attempt, resolve either `CALL_LEDGER_UNRESOLVED` actual ledger, activate a contract, permit retry/partial resume/C10, or change Results eligibility `FALSE`. Any future science still needs fresh explicit Owner authorization and a new independently reviewed R/C/O/T chain.
