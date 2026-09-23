# Nine-component outer-state static diagnostic at 1e-6

Task `CH5_FULL_OUTER_NINE_COMPONENT_1E6_STATIC_DIAGNOSTIC_20260923`. Dispatch HEAD `34a277b5c82ab4b9339df82ae21d10faa2928ff5`; parent `072a0655ae4f9720b89bd5e747f94c62b0e1dda2`; frozen `src` tree `00682b2e1a7ba23665f6e16f6acf48ad35874883`. This is a zero-science readout of sealed C4/C5/C6 only. It is not a convergence law, fixed-point verdict, or Results authorization.

## Stage and identity

C4 is completed turn4 with the sealed entering-turn5 JSON/NPZ; C5 is completed turn5 with entering-turn6; C6 is completed turn6 with entering-turn7. There is no completed turn7. All three bundles have 31 matching province indices and names in the same order. `S` is 31 x 31, row=destination and column=origin. Bundle JSON/NPZ raw return and payoff vectors match bitwise; the plan `S` hash uses float64 Fortran-order bytes. The sealed report manifest/readback and entering-bundle readback pass. Completed-turn raw `ra0_n` supplies the following turn `S_(n+1)` and `rah_(n+1)`; these are lagged inputs, not same-turn returns.

## Observed comparisons

For `Yt,Lt,wjt,w`, the diagnostic is `max_i abs(new_i/old_i - 1)`; every old denominator is finite and nonzero. For `Kt_prev`, it is `max_i abs(new_i-old_i)/Kt0_i`; `Kt0` is positive and bitwise identical across these checkpoints. For `rk,raw_ra0,rah`, it is the maximum absolute change in decimal one-model-period return units. For `S`, it is the maximum absolute share change over all destination/origin pairs. Every component uses strict `<1e-6`. The table values are rounded for display; the JSON receipt contains full float64 values, locations, raw maximum absolute changes, and old/new values.

| Transition | Yt | Lt | wjt | rk | Kt_prev | w | raw_ra0 | rah | S | Conjunction |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C4 to C5 | 0.000100744322 | 0.000384712802 | 0.000253183591 | 0.000766494273 | 1.5887487e-16 | 1.9894662e-05 | 0.000766494273 | 0.000675544301 | 3.85701398e-05 | NOT_ALL_NINE_BELOW_DIAGNOSTIC_LEVEL |
| C5 to C6 | 1.44696387e-05 | 5.52485585e-05 | 4.11913367e-05 | 0.000146881085 | 1.5887487e-16 | 3.39407954e-06 | 0.000146881085 | 0.000129031006 | 8.12234753e-06 | NOT_ALL_NINE_BELOW_DIAGNOSTIC_LEVEL |

Only `Kt_prev` is below the 1e-6 diagnostic level in each transition. All eight other components are above it. `NOT_ALL_NINE_BELOW_DIAGNOSTIC_LEVEL` is a historical comparison label only. No inference of contraction or a fixed point follows from the smaller C5-to-C6 values.

## Boundary and staging context

| Checkpoint | wjt lower hits | wjt upper hits | Kt_prev == Kt0 | clipped ra upper hits | clipped ra lower hits |
|---|---:|---:|---:|---:|---:|
| C4 | 3 | 25 | 28 | 31 | 0 |
| C5 | 3 | 25 | 29 | 31 | 0 |
| C6 | 3 | 25 | 30 | 31 | 0 |

The near-fixed `Kt_prev` and boundary-held `wjt` entries cannot replace the all-nine observation. C6 has 31/31 clipped `ra` upper-bound hits. The original MATLAB outer predicate therefore cannot be reported as passed.

## MATLAB reference and scope

Read-only SHA-256 identities of `multi_prov_HANK_12sts.m`, `HANK_mp_1eq.m`, and `HANK_2ASSETS_HJB.m` are listed in the receipt. In `multi_prov_HANK_12sts.m:15-16`, `num.crit=1e-7` is an inner HJB threshold and `num.reg_threshold=1e-9` is the outer threshold. `HANK_mp_1eq.m:28-42` checks K/L target and `abs(Yt/Yt_1-1)` against that strict outer threshold, plus 31 converged households and zero upper/lower clipped-`ra` boundary hits. The present nine-component `1e-6` comparison changes both object and diagnostic level; it does not inherit the MATLAB acceptance predicate.

## Limits and next gate

The Owner agreed to `1e-6` as diagnostic precision. `1e-12` class precision remains a future aspiration. No repeated evaluation of the full outer map at one frozen state, outer numerical error bound, adopted stopping law, or scientific call budget is available here. All model/scientific calls in this task are zero. Results eligibility remains `FALSE`. GPT Work must independently ACCEPT or REJECT this candidate before any successor.
