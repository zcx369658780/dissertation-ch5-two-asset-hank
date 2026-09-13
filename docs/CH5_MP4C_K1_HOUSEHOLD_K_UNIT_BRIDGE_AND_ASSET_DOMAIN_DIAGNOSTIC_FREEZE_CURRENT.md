# CH5 MP4C K1 — household k-unit diagnostic bridge and asset-domain freeze

Date: 2026-09-14.

## Authority and purpose

Owner has approved the next bounded diagnostic and delegated routine small-range numerical calibration/debug decisions to ChatGPT Reviewer for acceleration. This delegation does **not** authorize structural model redesign, HJB/KFE equation changes, arbitrary outcome-fitting, or Results claims.

This freeze authorizes a diagnostic-only household monetary convention and bounded asset-domain expansion. It does not claim that the household-to-real-currency bridge has been empirically proved.

Results eligibility=`FALSE`.

## Temporary household monetary convention

For this diagnostic only, accept the convention:

`h=1`

meaning existing household monetary numerics `w,C,Tt,a,b,At,Bt` are provisionally interpreted as `k` currency units per household/person as appropriate, with flows additionally carrying the model-period interpretation.

This is a **diagnostic normalization convention**, not a final dissertation monetary-unit claim. Therefore:

- no numerical rescaling of household `w,C,Tt,a,b,At,Bt` occurs;
- `alphac`, `a_bar`, derivative floor and drift tolerance remain numerically unchanged under `h=1`;
- `ra`, `rb`, borrowing gap, `rho`, depreciation, taxes and other rates remain unchanged;
- no `wjt` guard change is authorized;
- no macro aggregate rebasing is required for this standalone household-domain diagnostic.

## Frozen asset domain — Stage A

Use:

- `amin=0`;
- `amax=100`;
- `bmin=-2`;
- `bmax=20`;
- `I=20`;
- `J=20`.

Thus:

- `da=100/19≈5.2631578947368425`;
- `db=22/19≈1.1578947368421053`.

`amax=100` is an individual household illiquid-asset state-grid upper bound, not an `At` target or cap.

`bmax=20` is selected by Owner/Reviewer as the first bounded liquid-domain candidate because it materially expands the accepted `bmax=5` domain without jumping immediately to the coarser `bmax=50` candidate.

## Exact standalone science grid

Use the accepted real composite-wage domain:

- `rb=.02`;
- `ra={.06,.0675,.07}`;
- household composite `w={13,15.5,18}`.

Stage A is exactly 9 Cartesian points. Every point uses fresh MATLAB-style initialization; no warm starts.

All accepted HJB/KFE equations, FOC, selectors, derivative floor, boundary law, direct solve, pseudo-time rule, HJB tolerance, 100-iteration ceiling, MATLAB-equivalent transition legality and contaminated-row KFE remain frozen.

## Pre-registered Stage B escalation

Owner has delegated bounded small-range numerical calibration/debug decisions. Accordingly, one and only one domain escalation is pre-authorized here.

After completing all Stage A points, run Stage B with `bmax=50` **only if** Stage A shows that the liquid domain remains inadequate by this ex-ante rule:

- at least one Stage A converged/KFE-valid point has the `b` marginal mode at exact `bmax=20`.

Stage B keeps everything else identical:

- `amin=0`, `amax=100`, `bmin=-2`, `bmax=50`;
- `I=J=20`;
- same exact `rb × ra × w` grid;
- fresh initialization for all 9 Stage B points;
- `db=52/19≈2.736842105263158`.

No third expansion beyond `bmax=50` is authorized. If Stage B still has any exact-`bmax` modal point, stop and return domain/precision unresolved.

Stage B is a domain diagnostic, not production authority. Its coarser `db` must be explicitly caveated.

## Required classifications

HJB classification per point:

- `HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX`;
- `HJB_NOT_CONVERGED`;
- `HJB_CONVERGED`.

Asset-domain classification per converged/KFE point must report both assets separately.

Illiquid `a`:

- lower-bound dominated;
- interior candidate;
- upper-bound pile-up;
- ambiguous/pathological.

Liquid `b`:

- `B_INTERIOR_DISTRIBUTION_CANDIDATE` if the modal bin is strictly interior and neither endpoint is the modal bin;
- `B_LOWER_BOUNDARY_DOMINATED` if `bmin` is modal;
- `B_UPPER_BOUNDARY_PILEUP` if `bmax` is modal;
- `B_TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED` otherwise;
- `KFE_NUMERICALLY_PATHOLOGICAL` if signed mass/residual is materially non-probabilistic.

Do not fit a post-result threshold to force health labels. Always publish raw marginals and endpoint masses.

## Required receipts

For every point report at least:

- HJB iterations, final `max|ΔV|`, max `A2max`, first illegal iteration;
- `Ct,Lt,At,Bt`, `Bt_pos/Bt_neg` if available;
- full 20-bin `a` and `b` marginals;
- `amin/amax/bmin/bmax` masses;
- modal `a` and `b`;
- top three bins for both assets;
- KFE total mass, residual, density minimum and negative-entry count;
- whether `a` and `b` domains are individually adequate.

## Comparison authority

Compare Stage A directly to the accepted prior real-wage scan at `a=[0,10]`, `b=[-2,5]` using the same `rb × ra × w` points. Compare Stage B only if activated.

The primary questions are:

1. Does expanding `a` to 100 preserve HJB legality/convergence and interior `a` distributions?
2. Does `bmax=20` move the liquid distribution off the artificial upper boundary?
3. If Stage B is activated, does `bmax=50` do so?
4. How do `Ct,Lt,At,Bt` change relative to the accepted narrow-domain baseline?
5. Does any domain expansion introduce new KFE signed pathology or transition-matrix illegality?

## Precision boundary

`I=J=20` is frozen for this task. Domain adequacy and discretization precision are deliberately separated.

Even if Stage A or B clears the asset boundaries, production use is not authorized. A later precision-sensitivity gate is mandatory before production/Results authority.

## Hard stops

Stop on:

- any HJB/KFE algorithm change;
- any change to `wjt` guard or provincial return mapping;
- any rate/tolerance/solver/derivative-floor change;
- any household monetary rescaling with `h!=1`;
- any point outside the exact registered `rb × ra × w` grid;
- any domain expansion beyond the pre-authorized `bmax=50` Stage B;
- any global multi-province, firm, MATLAB, K1B/K2, GE, downstream, shock, IRF or Results runtime.

## Delegated numerical authority

For future closely related small-range diagnostic/calibration tasks, ChatGPT Reviewer may choose and publish bounded parameter/domain probes without waiting for a separate Owner reply, provided all of the following hold:

- the decision is numerical/local rather than a structural economic redesign;
- the choice is pre-registered before execution;
- no accepted equation, causal interpretation, monetary bridge, guard semantics or Results eligibility is changed;
- the range is bounded and justified by accepted evidence;
- outcome-adaptive tuning is prohibited unless the staged escalation rule itself was frozen ex ante;
- all such decisions remain subject to subsequent independent acceptance review.

Structural changes remain Owner authority.
