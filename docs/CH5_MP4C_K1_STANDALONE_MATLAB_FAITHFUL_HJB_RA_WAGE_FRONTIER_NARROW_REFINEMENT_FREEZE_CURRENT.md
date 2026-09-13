# CH5 MP4C K1 — standalone MATLAB-faithful HJB ra×wage frontier narrow refinement freeze

Date: 2026-09-13.
Status: `OWNER_APPROVED_NARROW_RA_REFINEMENT_AROUND_WAGE_DEPENDENT_FRONTIER`.

## 1. Owner decision

Continue bounded standalone household parameter-domain mapping under the unchanged accepted MATLAB-faithful HJB/KFE algorithm. Do not redesign HJB/KFE and do not run the full multi-province model.

The accepted previous refinement established a wage-dependent illiquid-asset frontier: `ra=.065,w={1.05,1.3}` were the only interior candidates; `ra=.065,w=.8` was transitional; `ra=.0725,w=.8` already piled at `amax`; `ra=.0725,w={1.05,1.3}` remained mixed; `ra=.08` piled at `amax` for all wages. No wage-robust interior `ra` band was established.

## 2. Exact next grid

Fix `rb=.02` and run exactly the Cartesian product:

- `ra ∈ {.06,.0675,.07}`;
- household wage proxy `w ∈ {.8,1.05,1.3}`.

Exactly nine standalone points. No adaptive or additional point may be added after observing results.

## 3. Frozen science and numerics

Use the exact accepted standalone configuration from the previous scans:

- `I=20`, `b∈[-2,5]`;
- `J=20`, `a∈[0,10]`;
- `Nz=2`, `z=[.8,1.3]`, original productivity transition matrix;
- `rb=.02`, borrowing-rate gap `.07`;
- all other accepted/original household parameters and MATLAB-faithful initialization unchanged;
- original HJB equations, upwind construction, `BB+AAH+Bswitch`, derivative floor, transfer FOC, selector, boundary laws, pseudo-time/direct solve, `max(abs(V_new-V_old))` convergence rule, tolerance, 100-iteration ceiling and `homecrit=.01` unchanged;
- accepted MATLAB-faithful contaminated-row stationary KFE unchanged.

No damping/relaxation, no solver/grid/tolerance/ceiling/derivative-floor/FOC/selector/boundary/KFE change, no global price guard.

## 4. Required classification

For every point first classify HJB as one of:

- `HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX`;
- `HJB_NOT_CONVERGED`;
- `HJB_CONVERGED`.

Only after HJB convergence, run KFE and classify the illiquid distribution descriptively as one of:

- `LOWER_A_BOUNDARY_DOMINATED`;
- `INTERIOR_A_DISTRIBUTION_CANDIDATE`;
- `UPPER_A_BOUNDARY_PILEUP`;
- `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED`.

Do not fit a numerical cutoff after seeing results. Preserve raw marginals and endpoint/interior masses.

## 5. Primary scientific question

Determine whether the narrower region contains a wage-robust nondegenerate interior `ra` band. In particular, test whether any of `.06`, `.0675`, `.07` is interior across all three wages, and map how the lower/interior/upper frontier shifts with wage.

For every converged point record at least `Ct,Lt,At,Bt`, full `a`/`b` marginals, masses at `amin,amax,bmin,bmax`, interior-a mass, modal `a/b`, top three `a` bins, `amax/adjacent` ratio where defined, KFE mass normalization/residual/signed-mass receipts, HJB iterations/final statistic/A2max.

## 6. Decision boundary after this task

If a tested `ra` is interior at all three wages, Reviewer may consider a provisional wage-robust `ra` health-band freeze or one final local-bound refinement.

If no tested `ra` is interior across all three wages, do not continue blind one-dimensional refinement automatically. The next Owner gate must consider a two-dimensional wage-conditional `(ra,w)` health region / provincial return-mapping constraint rather than pretending a universal scalar `ra` interval has been established.

## 7. Runtime boundary

HJB calls exactly 9 unless shared preflight corruption blocks execution. KFE calls at most 9 and only after HJB convergence. Scientific retries after a point starts: 0. One pre-HJB engineering retry allowed only for path/import/serialization/output-shape defects with unchanged scientific inputs.

Global multi-province outer turns, firm, MATLAB, K1B/K2, GE, downstream annual, shock, IRF and Results: all 0.

Standalone KFE evidence does not resolve the separate corrected-2018 multi-province finite-box upper-`b` leakage / MATLAB-style pinning blocker.

Results eligibility=`FALSE`.
