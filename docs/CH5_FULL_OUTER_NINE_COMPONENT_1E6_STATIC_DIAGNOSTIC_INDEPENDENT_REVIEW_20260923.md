# Independent Work review: nine-component 1e-6 static diagnostic

Date: 2026-09-23 (Asia/Shanghai)

Verdict: `ACCEPT__CH5_FULL_OUTER_NINE_COMPONENT_1E6_STATIC_DIAGNOSTIC__ZERO_SCIENCE__NO_CONVERGENCE_CLAIM`

## Candidate and identity

- Owner agreed to `10^-6 = 1e-6` as a nine-component **diagnostic precision**. `10^-12` class precision is a future aspiration. Neither is an adopted fixed-point stopping law.
- Work dispatch `34a277b5c82ab4b9339df82ae21d10faa2928ff5` from `072a0655ae4f9720b89bd5e747f94c62b0e1dda2`; Builder candidate `2d5d9a235803882b65571aab57233018d4c1fc0b` has the dispatch as parent.
- Candidate changes only `docs/CH5_FULL_OUTER_NINE_COMPONENT_1E6_STATIC_DIAGNOSTIC_20260923.md` and `EVIDENCE/ch5_full_outer_nine_component_1e6_static_diagnostic_20260923/diagnostic_receipt.json`. Document SHA-256 `B2949440543214421CFDBD305D1896698D236FA655452E136D990B6277D1DEE8`; receipt SHA-256 `7F431D581284F9327AE0CF393F9990B6AF522888029DA511B027B594600B016F`.
- All 31 receipt input paths and SHA-256 values independently read back with zero mismatch, including the three exact protected MATLAB files. The worktree is clean, `git show --check` passes, and production `src` tree remains `00682b2e1a7ba23665f6e16f6acf48ad35874883`.

## Independent findings

- C4, C5 and C6 represent completed turns 4, 5 and 6 with their respective prepared next-turn bundles. The 31-province order and destination-by-origin share orientation are preserved. Turn7 household has not run.
- Work independently recalculated all nine metrics for C4→C5 and C5→C6 directly from the sealed JSON/NPZ: all 18 full-precision values exactly equal the receipt values. The formula distinctions (relative Yt/Lt/wjt/w; Kt_prev relative to frozen Kt0; absolute rk/raw ra0/rah/S) and strict `<1e-6` comparisons are implemented as dispatched.
- Each transition has 1/9 components below the diagnostic level: only `Kt_prev`. All other eight components exceed it. The receipt's `NOT_ALL_NINE_BELOW_DIAGNOSTIC_LEVEL` label is a historical observation, not a scientific failure, contraction finding, or fixed-point verdict.
- The report correctly distinguishes MATLAB's `reg_threshold=1e-9` on K/L target and Yt ratio, plus 31 household and no clipped-ra-boundary conditions, from the current nine-component observation. All three sealed checkpoints have 31/31 clipped `ra` upper hits, so the original MATLAB outer predicate cannot be called passed. The separate inner HJB `crit=1e-7` was not reused.
- Literal ledger values are zero for household, HJB, KFE, integration, firm, K1B network, GE, turn7 and other scientific/model calls or retries. Results eligibility remains `FALSE`.

## Next gate

This ACCEPT covers the static readout and provenance only. It does not adopt a stopping rule, consecutive-pass count, 1e-12 final target, scientific call ceilings, failure protocol, GE or Results claim. Any same-frozen-state repeat or turn7 household requires a new bounded scientific task and Owner/Work scientific authority.
