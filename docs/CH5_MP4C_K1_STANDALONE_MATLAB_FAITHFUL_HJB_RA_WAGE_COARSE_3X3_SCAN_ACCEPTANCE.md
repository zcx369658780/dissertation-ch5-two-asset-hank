# CH5 MP4C K1 — standalone MATLAB-faithful HJB ra × wage coarse 3×3 scan acceptance

Date: 2026-09-13.

Reviewer verdict:

`STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_COARSE_3X3_SCAN_ACCEPTED__HJB_HEALTHY_ACROSS_GRID__ILLIQUID_ASSET_STEADY_STATE_PRIMARILY_RA_DRIVEN__INTERIOR_RA_TRANSITION_REFINEMENT_REQUIRED`

Accepted candidate: `5f55b474780d70921bfcf3ea2f863039c61814c1`.

## Acceptance basis

Independent review accepts the candidate as a bounded standalone MATLAB-faithful household HJB/KFE parameter-domain diagnostic. The candidate is a single Builder commit directly ahead of baseline `45f0e3aedeb88e0dc9ca5e35e1e79664cedf2909`; changes are confined to task-owned runner/finalizer/tests, compact evidence, report and CURRENT closeout docs.

Accepted execution facts:

- exact grid: `rb=.02`; `ra={.02,.055,.09}`; `w={.8,1.05,1.3}`;
- HJB calls `9/9`; KFE calls `9/9`; scientific retries `0`;
- global outer turns, firm, MATLAB, K1B/K2, GE, annual downstream, shock/IRF and Results all `0`;
- all 9 HJBs converged under the unchanged accepted MATLAB-faithful HJB algorithm;
- no transition-matrix legality failure; maximum observed `A2max=.007712953842301029 < homecrit=.01`;
- all scientific arrays finite with expected shapes and accepted label domains.

## Accepted domain evidence

At `ra=.02` and `.055`, all three wage points place essentially all stationary mass at the structural lower illiquid-asset bound `amin=0`. These six points remain `QUALITY_AMBIGUOUS__OWNER_REVIEW_REQUIRED`: the lower bound is an economic state constraint rather than an artificial upper truncation, and the standalone contaminated-row KFE receipts include small signed numerical mass / raw-system residual variation.

At `ra=.09`, all three wage points have modal `a=10` and approximately `18.7%–20.9%` stationary mass at `amax`, exceeding the adjacent interior bin. These three points are accepted as `BOUNDARY_CONVERGED_CANDIDATE`.

The coarse scan therefore identifies no GOOD point, but it does identify a clear qualitative transition along the `ra` axis between `.055` and `.09`. Wage changes over `.8–1.3` do not alter the lower-versus-upper illiquid-boundary classification and do not generate HJB failure in the coarse scan.

## Scientific interpretation boundary

This acceptance does not calibrate the full multi-province model and does not establish a production admissible interval. It supports the practical numerical route of mapping a standalone healthy household-input domain while keeping the validated MATLAB-faithful HJB/KFE algorithm unchanged.

The next diagnostic should refine only the `ra` transition interval while preserving the same wage coverage and fixed `rb=.02`, searching for an interior illiquid-asset distribution between lower-bound and upper-bound regimes.

## KFE / Results boundary

The accepted standalone MATLAB-faithful contaminated-row KFE is used only for isolated household parameter-domain mapping. It does not resolve or waive the corrected-2018 multi-province finite-box upper-`b` leakage / MATLAB-style pinning blocker.

Results eligibility=`FALSE`.

## Exactly one next Owner/Reviewer gate

`OWNER_REVIEW_STANDALONE_RA_TRANSITION_REFINEMENT_3X3`

Pre-registered refinement grid: `rb=.02`; `ra={.065,.0725,.08}`; `w={.8,1.05,1.3}`. No other parameter points are authorized by this acceptance.
