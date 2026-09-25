# Owner decision packet — K1B after valid R2 level miss

Decision state: the independently accepted C6→C7 and C7→C8 turns were complete, legal and each used its own one-shot budget. Their nine-component strict `<1e-6` comparisons passed only 2/9 and 5/9 components. The adopted two-turn maximum is consumed; terminal `VALID__LEVEL_NOT_MET_AT_BUDGET`. The post-R2 zero-science design at `413505022af4b0bb5bc846e65570c6a108dd7c65` has been independently ACCEPTED for evidence quality in `docs/CH5_K1B_POST_R2_NONATTAINMENT_ZERO_SCIENCE_DESIGN_INDEPENDENT_REVIEW_20260925.md`. Results eligibility is `FALSE`; no further scientific/model call is authorized.

## What the observations say

At C7→C8, `Lt=1.4616551486934526e-6`, `rk=5.358519392650862e-6`, `raw_ra0=5.358519392650862e-6`, and `rah=4.685714629193427e-6` still exceed the strict level. The four observed adjacent differences shrink for most components, but this finite trajectory establishes neither a contraction nor an error bound or a number of further turns to PASS. The one exact C5→C6-prime same-input repeat establishes only input-specific reproducibility. All three C6/C7/C8 checkpoints had 31/31 clipped `ra` upper hits; the new criterion treats them as report-only, while the original MATLAB zero-hit predicate remains unmet. No fixed point, steady state, GE or dissertation Results claim follows.

## Decision now

| Route | Owner decision | Next authorized kind of work | What remains closed |
|---|---|---|---|
| A. End K1B scientific calls at this boundary | Accept bounded level nonattainment as the final K1B diagnostic for now. | Preserve evidence and prepare limitation/interpretation material under a separate zero-science task. | Turn9, new stopping law, GE, Results. |
| B. Retain frozen economics and investigate a future rolling criterion | Authorize **design only** of a new prospective rolling two-pass window and finite budget/runner contract. A one-launch multi-turn Python runner may be evaluated to reduce Work/Codex token handoffs. | Zero-science specification and independent review first; Owner later approves exact maximum turns, per-province/per-turn/combined calls, compute/time ceiling and execution if justified. | All model calls until that later approval; current C6→C7/C7→C8 R2 result cannot be relabeled. |
| C. Revisit the scientific object | Authorize a separate high-risk design of clipped-`ra` boundary meaning, economic admissibility, or a replacement stopping criterion. | Source-backed zero-science economic/mathematical design, then explicit Owner adoption and separate implementation/review if warranted. | Automatic tuning, retrospective PASS, model calls, GE, Results. |

**GPT Work recommendation:** choose **B for a zero-science specification stage** if the goal is to test the same frozen K1B map further while reducing token overhead. The specification should encode per-turn atomic seal/readback, full attempted-call ledger, first-failure and early-success stop, and no automatic tuning. A 10- or 20-turn one-launch process is only an illustrative engineering shape; neither number is a scientifically justified or authorized budget. One launch can reduce coordination tokens, but compute and scientific calls still accrue every turn, and a defect may only be independently reviewed after more work has been spent. The current data do not justify a specific next call count or relaxing `1e-6`; both remain Owner decisions after a concrete reviewed proposal. Routes A and C remain available independently of how evidence is preserved.

Please select **A**, **B design only**, or **C design only**, or specify a different scientific question. A selection of B or C authorizes only the next bounded zero-science task. It does not restart a consumed budget or authorize turn9.
