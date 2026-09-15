# CH5 MP4C K1 J160 bounded cross-state confirmation

## Terminal classification

`J160_BOUNDED_CROSS_STATE_CONFIRMATION_PASS__PRACTICAL_DIAGNOSTIC_GRID_SUPPORTED`

This is a zero-science-runtime finalizer repair and closeout. It supports J160 only for later bounded diagnostics. It does not establish continuum convergence, production-final precision, GE validity, or Results eligibility.

## Source and execution boundary

- Actual fresh-fetched baseline: `1c2d2b0bc0167b1821315164356e461a0f3c05fa`.
- Preserved raw science root: `D:\ProjectTemp\ch5-mp4c-k1-j160-cross-state-evidence-20260915-001`.
- Raw evidence integrity: PASS; 20 exact files, 1,331,049 bytes. No raw seal/manifest existed, which is recorded rather than treated as an automatic failure.
- All four NPZ archives reproduce the receipt hashes for `value`, `consumption`, `labor`, `transfer`, `mu_a`, `mu_b`, and `density`; array shapes are `(20,160,2)`, values are finite, and grids are exact.
- Preserved science ledger: HJB started/completed `4/4`; KFE started/completed `4/4`; scientific retries `0`; center and J20 reuse calls `0/0`; every forbidden runtime category `0`.
- This repair task's science ledger is all zero: HJB, KFE, every grid rerun, scientific retries, outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results.

## Finalizer repair

The prior finalizer rejected unequal supports. The task-owned replacement preserves the accepted same-support cumulative-node-mass and piecewise-linear interpolation semantics. For unequal supports it evaluates both raw signed CDFs over the union interval, extends each CDF by zero below its own support and by its raw total marginal mass above its own support, then divides the absolute-CDF integral by union width.

No signed mass is clipped, renormalized, smoothed, or rebinned. Every J20→J160 marginal metric is named `DOMAIN_PLUS_GRID_CDF_DISTANCE`, because both domain and discretization change.

Focused regression coverage includes same-support exact equivalence, the two required unequal-support fixtures, both exterior extensions, preservation of signed/non-unit mass, invalid and zero-width fail-closed behavior, and an AST check that the finalizer imports no solver or run module.

Final engineering verification: focused plus relevant accepted regressions `32 passed`; `py_compile` PASS; `git diff --check` PASS; compact sealed manifest PASS with 10 entries totaling 248,767 bytes.

## Five J160 states

| State `(ra,w)` | Source | HJB iter / final | Ct | Lt | At | Bt | modal a | modal b | amax mass | bmax mass |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `(.06,13)` | fresh | 14 / `4.44643e-9` | 12.3214 | 0.643307 | 85.6697 | 4.82888 | 90.5660 | 2.63158 | 0 | `1.62252e-5` |
| `(.06,18)` | fresh | 68 / `8.04693e-8` | 13.4628 | 0.627062 | 81.1883 | 5.97040 | 75.4717 | 1.47368 | 0 | 0.0162997 |
| `(.0675,15.5)` | accepted reuse | 16 / `2.26131e-10` | 14.2588 | 0.628060 | 89.2978 | 5.81025 | 94.3396 | 2.63158 | 0 | 0.000977401 |
| `(.07,13)` | fresh | 11 / `2.19058e-10` | 13.0223 | 0.629211 | 90.7323 | 5.78054 | 94.3396 | 2.63158 | 0 | 0.000155482 |
| `(.07,18)` | fresh | 17 / `3.17469e-8` | 15.7496 | 0.620789 | 89.6487 | 6.15232 | 95.5975 | 2.63158 | 0 | 0.00282348 |

All four fresh HJBs are legal and converged. All four KFE receipts completed with total mass equal to one within floating-point tolerance; residual infinity norms range from about `1.77e-17` to `1.38e-13`. Density minima range from about `-1.06e-18` to `-2.83e-18`, inside the accepted numerical rounding band, and the raw signed entries remain unchanged.

## J20 to J160 comparison

| State `(ra,w)` | iter J20→J160 | At J20→J160 | Bt J20→J160 | modal a J20→J160 | modal b J20→J160 | a `DOMAIN_PLUS_GRID_CDF_DISTANCE` | b `DOMAIN_PLUS_GRID_CDF_DISTANCE` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `(.06,13)` | 13→14 | 7.14335→85.6697 | 1.60951→4.82888 | 7.36842→90.5660 | 5→2.63158 | 0.784750 | 0.128339 |
| `(.06,18)` | 21→68 | 7.27038→81.1883 | 4.69721→5.97040 | 7.36842→75.4717 | 5→1.47368 | 0.738666 | 0.162583 |
| `(.0675,15.5)` | 24→16 | 7.30523→89.2978 | 4.68278→5.81025 | 7.36842→94.3396 | 5→2.63158 | 0.819413 | 0.112200 |
| `(.07,13)` | 24→11 | 7.33469→90.7323 | 4.66291→5.78054 | 7.36842→94.3396 | 5→2.63158 | 0.833463 | 0.0948707 |
| `(.07,18)` | 23→17 | 7.29108→89.6487 | 4.69951→6.15232 | 7.36842→95.5975 | 5→2.63158 | 0.823063 | 0.129788 |

The large a changes and both CDF-distance columns combine domain expansion with grid change; they are not grid-only precision evidence. Full `Ct`, `Lt`, endpoint-mass deltas, and exact-precision values are preserved in `j20_j160_comparison.json`.

## Scientific closeout

- A domain: `amax=100` is nonbinding at every fresh corner. All fresh modal-a locations are interior and every fresh amax mass is zero. The distributions are scientifically interpretable for bounded diagnostic use.
- B domain: `bmax=20` is nonbinding in the bounded-diagnostic sense at every fresh corner. The largest fresh bmax mass is 0.0162997 at `(.06,18)`; it remains below its adjacent interior mass and is not a modal boundary pileup.
- Cross-state coherence: aggregates and distributions remain finite and nonpathological. Changes are state-dependent, including the slower 68-iteration `(.06,18)` solve, but all states satisfy the frozen HJB and KFE gates.
- Practical diagnostic grid supported: `TRUE`.
- KFE caveat: this remains the accepted standalone contaminated-row KFE construction; tiny signed numerical entries were preserved, and corrected-2018 finite-box/pinning authority remains separate.
- Results eligibility: `FALSE`.

Exactly one next gate: `REVIEWER_J160_CROSS_STATE_ROUTE_DECISION`.
