# Ordered update and damping contract

## Current one-turn semantics

1. Copy the complete old-turn 31-province state.
2. Build `phi_MAT` from old Y/L.
3. Run all household blocks against their own old states; no province sees a partially updated peer household.
4. Use new household Ct and retained old clipped `wjt` in `Lt_seperate`; multiply each origin column by N once; row sums become destination `Lt_supply`.
5. Convert and multiply new household At by N, then apply the existing capital-allocation weights to form `Kt_supply`.
6. Construct `rah` from retained old clipped firm ra. This is the next household return and gives the source a one-turn price lag.
7. Call the firm with `Kt_supply+GovInv`, `Lt_supply`, current Zt and alpha. Compute raw prices, tax compensation, then clipped `ra/wjt`.
8. Construct household wage `w` from the new clipped firm wage vector.
9. Update Taylor-rule rb and fiscal diagnostics.
10. Evaluate K/N-reference gap, Y/Y_prev gap, household convergence, and bound-hit counts.
11. If nonconverged, near the source K/N gate, and in steady-state mode: reset Zt where GDP gap exceeds .01; then multiply GovInv by .9/.1 as triggered by clipped ra.
12. Update only the reference `tKNratio=.6*new+.4*old`.

## Successor state names

For each firm-side price retain `firm_raw`, `firm_clipped`, `clip_flag`, and `clip_reason`. For each household composite retain `composite_raw`, `prior_household_used`, `next_household_used`, `lambda`, and `damping_delta`. A field named only `w` or `rah` is insufficient in new serialized evidence.

The canonical after-firm candidate sequence is:

`old household-used prices → household → labor/capital allocation → firm raw prices → firm clipping/tax compensation → raw cross-province composite prices → composite damping → next-household-used prices → diagnostics/stage gate → controller proposal/use → K/N-reference damping`.

This preserves current safety and fiscal semantics, but for rah it removes the source's extra propagation lag. The minimal source-faithful baseline instead computes `rah_composite_raw` from the prior clipped ra vector before the current firm and damps that value for the next household. Both candidates aggregate only clipped ra. Their timing must be compared as separate future cells; it cannot be changed implicitly as part of damping.

`damp raw firm price → clip` is rejected because the result would no longer match the source Corptax compensation. Damping firm prices themselves is outside the Owner-approved w/rah scope.

## Damping contract

For `x ∈ {w,rah}`:

`x_next_used = (1-lambda_x) x_prior_used + lambda_x x_composite_raw`, with `0 < lambda_x <= 1`.

Pre-registered candidates are `lambda_x ∈ {1,.5,.25}`. The bounded matrix is `(1,1),(.5,.5),(.25,.25),(.5,.25),(.25,.5)`. `lambda=1` is the no-new-damping comparator. No coefficient may be added after trajectory inspection.

At a fixed point, `x_prior_used=x_composite_raw`, so convex damping leaves the fixed point unchanged. Validation must nevertheless compare final states, because clipping, stage gates, and finite termination can make realized paths non-equivalent.
