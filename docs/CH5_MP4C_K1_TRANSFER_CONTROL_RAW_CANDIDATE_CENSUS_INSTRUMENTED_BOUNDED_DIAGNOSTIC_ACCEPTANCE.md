# CH5 MP4C K1 transfer-control raw-candidate census acceptance

Date: 2026-09-13.

Reviewer verdict:

`RAW_TRANSFER_CANDIDATE_CENSUS_ACCEPTED__EXPLOSIVE_FINITE_HEAVY_TAIL_CONFIRMED__NO_ROBUST_DATA_IDENTIFIED_CUTOFF__OWNER_NUMERIC_TRANSFER_SAFEGUARD_FREEZE_REQUIRED`

Accepted candidate: `e6c71240e945c988958a16c67886b056376a2da4`.

## Accepted findings

The observation-only rerun preserved frozen annual G1/G2 science and stayed within the authorized runtime budget. No transfer safeguard was implemented.

The exact census contains 87,027,200 raw branch-cell transfer candidates. Old instrumented summaries reconcile exactly. The pooled raw distribution is strongly heavy-tailed, with abs(d) median about 2.76, p99 about 2.89e3, p99.9 about 5.82e4, p99.99 about 1.02e6, and extrema spanning roughly -2.79e9 to +1.71e12.

Exact diagnostic exceedance shares are accepted: abs(d)>1e3 = 2.145776%, >1e4 = 0.398441%, >1e5 = 0.064336%, >1e6 = 0.010142%. These are sensitivity diagnostics, not frozen safeguard stages.

The only exceptionally large adjacent top-tail gap isolates the two largest positive observations and is not robust across branch/path/turn-2 partitions. The evidence therefore does not identify a unique operational cutoff.

The preferred future semantic design remains `C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION`. Candidate clipping remains nonpreferred. No numeric d interval is frozen by this acceptance.

## Boundary

`chi0=.1`, `chi1=2 years`, derivative floor, transfer FOC, selector/boundary laws, return/wage guards, annual calibration, grid, tolerance, solver, K1/C1 and labor science remain unchanged.

No longer G2, G3/G4, wage relaxation, K1B/K2, steady-state acceptance or Results is authorized. KFE remains `DIAGNOSTIC_ONLY`; standalone KKT residual remains unavailable in accepted evidence.

## Next gate

`OWNER_NUMERIC_TRANSFER_SAFEGUARD_FREEZE`

The Owner must choose the first temporary transfer-control admissibility interval/ladder and whether it is symmetric or asymmetric. The census supplies bounded options but does not uniquely select one.

Results eligibility remains `FALSE`.
