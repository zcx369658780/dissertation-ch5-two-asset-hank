# CH5 MP4C K1 — standalone MATLAB-faithful HJB ra transition refinement 3×3 acceptance

Date: 2026-09-13.

Reviewer verdict:

`STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_3X3_ACCEPTED__WAGE_DEPENDENT_FRONTIER_IDENTIFIED__NO_WAGE_ROBUST_INTERIOR_BAND_YET`

Accepted candidate: `cdaba87bae181280e182f639d4cf8fa5a5bae773`.

## Acceptance basis

The candidate is accepted as a bounded standalone MATLAB-faithful HJB/KFE refinement diagnostic under the frozen household algorithm.

Independent review verified the candidate is one commit directly ahead of baseline `c58a64b65ce948f8ddc47dfe8c4fd3a3dc060921`, with changes confined to the task-owned report, CURRENT closeout docs, compact evidence, tests, and standalone refinement validator/runner code. No HJB/KFE scientific source redesign is present in the candidate diff.

Accepted execution facts:

- exact preregistered grid: `rb=.02`, `ra={.065,.0725,.08}`, `w={.8,1.05,1.3}`;
- 9 fresh initializations; only `ra` and household wage vary;
- HJB `9/9`, all legal and converged;
- KFE `9/9`, only after HJB convergence;
- scientific retries `0`; engineering retries `0`;
- global multi-province outer turns, firm, MATLAB, K1B/K2, GE, downstream annual, shock, IRF, Results all `0`;
- all HJB calls converged in 9 iterations;
- maximum `A2max=7.10543e-15`, with no legality failure.

## Accepted distribution evidence

The supported descriptive classification is:

`ALL_HJB_LEGAL_CONVERGED__INTERIOR_ONLY_AT_RA_0P065_HIGHER_WAGES__WAGE_DEPENDENT_TRANSITION__RA_0P08_UPPER_BOUNDARY`.

Accepted point labels:

- `ra=.065,w=.8`: `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED`;
- `ra=.065,w=1.05/1.3`: `INTERIOR_A_DISTRIBUTION_CANDIDATE`;
- `ra=.0725,w=.8`: `UPPER_A_BOUNDARY_PILEUP`;
- `ra=.0725,w=1.05/1.3`: `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED`;
- `ra=.08` at all three wages: `UPPER_A_BOUNDARY_PILEUP`.

No post-result numerical cutoff was used. Classification is based on exact modal location and endpoint-versus-interior bin ordering, with full raw marginals retained.

## Interpretation

The refinement establishes that the lower-to-upper illiquid-asset transition is materially wage dependent within the tested range. The only interior candidates occur at `ra=.065` for wages `1.05` and `1.3`. No single tested `ra` is interior across all three wages, so there is not yet a wage-robust connected nondegenerate `ra` health band.

The accepted interior-candidate aggregate ranges are descriptive only:

- `Ct=[1.4520245248118848,1.648582665766757]`;
- `Lt=[.873876860999354,.8788801526224764]`;
- `At=[8.89797303470002,8.959369004297567]`;
- `Bt=[.7300311913729753,.8149483194036385]`.

These do not confer production or Results authority.

## Scientific boundary

This acceptance supports continued parameter-domain mapping with the original MATLAB-faithful HJB/KFE algorithm. It does not authorize HJB damping, solver redesign, tolerance/grid/derivative-floor changes, price guards, full-model calibration changes, or global model execution.

The standalone contaminated-row KFE evidence remains distinct from the unresolved corrected-2018 multi-province finite-box upper-`b` leakage and MATLAB-style pinning blocker.

Results eligibility=`FALSE`.

## Exactly one next Owner gate

`OWNER_REVIEW_NARROWER_RA_REFINEMENT_AROUND_WAGE_DEPENDENT_FRONTIER`

The recommended candidate grid for Owner discussion is `rb=.02`, `ra={.06,.0675,.07}`, `w={.8,1.05,1.3}`. This is not yet an authorized successor runtime task. Owner/Reviewer should first decide whether this refinement is preferred over freezing a provisional wage-conditional `ra` band or redesigning the later provincial return-mapping layer.
