# CH5 MP4C K1 — standalone MATLAB-faithful HJB `ra × wage` narrow frontier 3×3 acceptance

Date: 2026-09-13.

Reviewer verdict:

`STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_ACCEPTED__NO_UNIVERSAL_RA_HEALTH_BAND__TWO_DIMENSIONAL_RA_WAGE_REGION_REQUIRED`

Accepted candidate: `d1401fc5154a6fb77989b0de343da20329bf724a`.

## Acceptance basis

The candidate is accepted as a bounded standalone MATLAB-faithful HJB/KFE parameter-domain diagnostic under the frozen household algorithm.

Independent review verified that the candidate is exactly one commit ahead of baseline `d0323df5a85617f3c856b93c88c98a08deb697be`; changed paths are confined to the task-owned report, CURRENT closeout docs, compact evidence, tests, and standalone frontier runner/finalizer package. No accepted HJB/KFE scientific source or protected MATLAB source was modified.

Accepted execution facts:

- exact grid: `rb=.02`, `ra={.06,.0675,.07}`, `w={.8,1.05,1.3}`;
- nine fresh MATLAB-style initializations; only `inputs.r_a` and `inputs.wages[0]` vary;
- HJB `9/9`, all legal and converged;
- KFE `9/9`, one after each converged HJB;
- all HJB calls used 9 iterations; maximum `A2max=5.32907e-15`; no first illegal iteration;
- scientific retries `0`; engineering retries `0`;
- global multi-province outer turns, firm, MATLAB, K1B/K2, GE, downstream annual, shock, IRF, Results all `0`.

## Accepted distribution evidence

Supported terminal classification:

`ALL_HJB_LEGAL_CONVERGED__NO_WAGE_ROBUST_INTERIOR_RA__TWO_DIMENSIONAL_HEALTH_REGION_REQUIRED`

Accepted point labels:

- `ra=.06,w=.8`: `LOWER_A_BOUNDARY_DOMINATED`, with severe signed contaminated-row KFE pathology; descriptive label only, not admissibility;
- `ra=.06,w=1.05`: `LOWER_A_BOUNDARY_DOMINATED`;
- `ra=.06,w=1.3`: `INTERIOR_A_DISTRIBUTION_CANDIDATE`;
- `ra=.0675,w=.8/1.05`: `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED`;
- `ra=.0675,w=1.3`: `INTERIOR_A_DISTRIBUTION_CANDIDATE`;
- `ra=.07,w=.8`: `UPPER_A_BOUNDARY_PILEUP`;
- `ra=.07,w=1.05/1.3`: `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED`.

No tested scalar `ra` is interior for all three wages. Therefore no wage-robust connected scalar `ra` health band is established.

## Important KFE boundary

The point `(ra,w)=(.06,.8)` has raw signed KFE pathology: `amin` mass above one, negative `amax` and interior-a mass, negative `At`, and density minimum about `-0.01259`. These values were correctly preserved rather than clipped. This point must not be treated as an admissible lower-bound steady state; its label only records the raw modal/dominance pattern.

This observation strengthens, rather than weakens, the conclusion that a scalar `ra` interval is not an adequate universal health rule.

## Interpretation

The accepted evidence shows a materially wage-dependent frontier. Higher wage shifts the household block away from the low-`ra` lower-bound regime and delays or changes the transition toward the artificial upper-`a` boundary. A single scalar `ra` band valid across `w=.8–1.3` is not supported by the tested domain.

The two interior candidates are descriptive only and have aggregate ranges:

- `Ct=[1.6271748553562086,1.6579145830154138]`;
- `Lt=[.8653040707113617,.891817638945374]`;
- `At=[8.735398940966421,8.935854550440705]`;
- `Bt=[.5804628039224781,.807045544098199]`.

These ranges confer no GE, production, or Results authority.

## Scientific boundary

This acceptance does not authorize further automatic one-dimensional `ra` refinement. It does not authorize HJB/KFE algorithm changes, damping, solver/tolerance/grid/derivative-floor changes, price guards, or full-model calibration changes.

Standalone contaminated-row KFE remains distinct from the unresolved corrected-2018 multi-province finite-box upper-`b` leakage and MATLAB-style pinning blocker.

Results eligibility=`FALSE`.

## Exactly one next Owner gate

`OWNER_REVIEW_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING`

The next review should use the accumulated standalone evidence to define a provisional two-dimensional `(ra,w)` household-health map and then inspect how the provincial return/wage mapping places each province relative to that map. No successor runtime task is authorized by this acceptance alone.
