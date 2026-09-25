# Owner in-principle adoption — prospective K1B rolling rule

Date: 2026-09-25 (Asia/Shanghai)

Owner response: `可以我同意，请继续`, answering GPT Work's specific question whether to **principally adopt** the proposed C8-start prospective two-consecutive-pass rule and at-most-two-new-turn short window, and authorize a separate zero-science task to find a trustworthy timing basis and hard ceiling. The accepted design is `docs/CH5_K1B_POST_R2_ROLLING_BATCH_ZERO_SCIENCE_SPEC_20260925.md`, Builder candidate `32b72f91b2edfb68bb8970bb2acc194070fa3131`; independent Work ACCEPT is `docs/CH5_K1B_POST_R2_ROLLING_BATCH_ZERO_SCIENCE_SPEC_INDEPENDENT_REVIEW_20260925.md`. This document records the Owner's **design-level scientific direction**. It authorizes no model or runner execution and does not set a complete new budget.

## Agreed prospective rule and short-window design basis

- Starting checkpoint is the previously accepted, sealed C8. The entering-turn9 bundle is input provenance only. Initialize a new rolling counter at zero. C6→C7 and C7→C8 retain their original legal `VALID__LEVEL_NOT_MET_AT_BUDGET` evidence and do not count toward the new rule.
- A new adjacent comparison exists only after a complete legal checkpoint with 31/31 accepted HJB/KFE, one full source-faithful integration, raw `ra0`, and sealed/read-back next-turn input and plan. The same nine accepted components, carrier, formulas, finite/denominator/axis identity, and strict `<1e-6` level apply. All nine passing increases the counter; a complete legal nonpass resets it to zero. Identity, inner-science, budget, accounting, seal or readback failures stop at the first original terminal and do not update the counter.
- Two consecutive **new** complete legal all-nine passes would stop at a bounded numerical-criterion candidate pending independent Work review. The short-window design basis is **at most two new complete turns, C9 and C10**. This is the smallest possible window for two new comparisons; it is not a forecast of success. An earlier candidate success, first failure, or exhausted adopted budget stops immediately. An eventual legal level miss at the new cap remains a bounded nonattainment, not divergence.
- Frozen economics and solver semantics remain as in `SCIENTIFIC_DECISIONS.md`; clipped-`ra` upper hits stay report-only for this nine-component criterion and the original MATLAB zero-hit predicate remains separate. No mathematical fixed point, steady state, GE or Results claim follows from numerical criterion success.

## Unresolved execution authority

The prior C6-to-C8 two-turn call budget is consumed and **does not transfer** to C9/C10. Copying its per-category ceilings into a new window is a reviewed proposal, not an adopted allowance. Accepted reports/receipts do not provide measured wall/compute time, so a trustworthy timing basis and explicit hard `T_owner` are still unresolved. The Owner has authorized a **zero-science timing/budget evidence task only**. Implementation of a batch runner needs a separate exact-path task and independent review. Any turn9 or turn10 household/model call requires a later explicit Owner adoption of the complete finite call/time budget and a separately bounded execution task. A 10/20-turn run is not authorized. No retry or recovery is granted.

`Results eligibility = FALSE`. K2, GE, annual dynamics, shocks, IRFs, welfare and dissertation Results remain closed.
