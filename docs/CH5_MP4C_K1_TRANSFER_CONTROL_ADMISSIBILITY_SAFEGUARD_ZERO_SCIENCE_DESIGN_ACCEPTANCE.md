# CH5 MP4C K1 transfer-control admissibility safeguard zero-science design acceptance

Date: 2026-09-13.

Reviewer verdict:

`TRANSFER_CONTROL_SAFEGUARD_ZERO_SCIENCE_DESIGN_ACCEPTED__EXPLOSIVE_FINITE_RAW_TAIL_CONFIRMED__FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION_PREFERRED__EXACT_NUMERIC_LADDER_NOT_IDENTIFIED__RAW_CANDIDATE_CENSUS_INSTRUMENTATION_REQUIRED`

Accepted candidate: `bdc2ecd48ca3408cf10138ee58d02383185ffd50`.

## Accepted findings

1. The accepted instrumented traces prove a finite explosive raw transfer-candidate tail. Across the represented 87,027,200 branch-cell evaluations all persisted nonfinite counts are zero, while raw extrema reach about `-2.785e9` to `+1.715e12`.
2. Exact final-iteration selected-control evidence contains 248,000 cells. `abs(d)` has median about `1.38`, p99 about `1.62e3`, p99.9 about `3.72e4`, and maximum about `4.27e7`, confirming a very heavy finite selected-control tail.
3. The accepted evidence does not persist full raw branch arrays. It therefore cannot support exact pooled raw percentiles, exact raw threshold-hit shares, branch-cell sign frequencies, or a uniquely defensible numerical admissibility ladder.
4. The symmetric intervals `1e3/1e4/1e5/1e6` are accepted only as static sensitivity probes, not as frozen ladder stages.
5. The semantic preference `C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION` is technically well motivated because it preserves raw FOC receipts and avoids manufacturing clipped non-FOC candidates. This acceptance records it as the preferred design for the next Owner freeze, but does not itself freeze implementation semantics or any numeric threshold.
6. Candidate clipping is not preferred because it fabricates endpoint-valued candidates that do not solve the accepted FOC outside the admissible region.

## Reviewer correction to the proposed next gate

A further purely zero-science analysis cannot recover cell-level raw arrays that were never persisted. Array hashes and per-array summaries are not invertible. Therefore the next gate must not claim that another static analysis can obtain exact raw cell distributions from the existing evidence alone.

The next gate is instead a fresh **bounded observation-only instrumentation runtime** that repeats the already accepted frozen G1/G2 short-horizon science and persists an exact raw-candidate census before any safeguard is implemented. The runtime must prove instrumentation parity and must not change `chi0/chi1`, transfer FOC, derivative floor, return/wage guards, selector, boundary law, grid, tolerance, solver, K1/C1 or labor science.

The raw-candidate census must be sufficient to compute exact branch-wise pooled quantiles, sign frequencies, threshold hit shares and turn/path partitions needed for a later Owner numerical freeze. It does not authorize any transfer-control safeguard implementation.

## Scientific boundary

No transfer-control bound is frozen or active. No longer G2, G3/G4, wage relaxation, `chi0/chi1` change, derivative-floor change, K1B/K2, steady-state acceptance or Results gate is opened.

KFE remains `DIAGNOSTIC_ONLY`; finite-box upper-`b` leakage and MATLAB-style pinning remain independent blockers. Results eligibility remains `FALSE`.
