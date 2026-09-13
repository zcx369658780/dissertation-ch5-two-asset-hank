# CH5 MP4C K1 — wage-conditional `(ra,w)` health-region and provincial return-mapping audit acceptance

Date: 2026-09-13.

Reviewer verdict:

`WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT_ACCEPTED__WAGE_IDENTITY_ALIGNED__PROVINCIAL_WAGE_DOMAIN_OUTSIDE_STANDALONE_COVERAGE__HEALTH_REGION_UNRESOLVED`

Accepted candidate: `3975d42fae57cc25f179225857b5defce1d7731f`.

## Acceptance basis

Independent review verified the candidate is exactly one commit ahead of baseline `44df9bb331770a930d8ff465c23d59d6fe5cb65a`, with changes confined to the audit report, CURRENT closeout docs, compact evidence, focused tests, and task-owned parser/builder code. No scientific model source, parameter, guard, HJB/KFE algorithm, or protected MATLAB source was modified.

Accepted runtime ledger: HJB=0; KFE=0; outer=0; MATLAB=0; firm=0; K1B/K2=0; GE/downstream/shock/IRF/Results=0; scientific retries=0.

## Wage semantic gate

Accepted gate result:

`WAGE_VARIABLE_IDENTITY_PROVEN_DIRECTLY_COMPARABLE`

Standalone scan `w` and the multi-province household HJB consumed `results.w` / `HouseholdInputs.wages[0]` are the same household-wage object/API role. `guarded_wjt` is a distinct upstream firm wage and is converted through the existing source-defined wage aggregation into the household composite wage. No outcome-fitted rescaling or normalization is authorized or used.

Crucially, semantic identity does not imply numerical-domain overlap.

## Health-map coverage finding

The accepted standalone health map contains 27 observed points with canonical counts: interior=4, ambiguous=7, lower=7, upper=8, KFE-pathological=1. No interpolation or fitted boundary is accepted as admissibility evidence.

All 62 accepted provincial turn1/turn2 household-input states are outside the observed standalone wage domain:

- standalone observed wage coordinates: `.8`, `1.05`, `1.3`;
- turn1 provincial composite wage range: approximately `13.8375–18.5197`;
- turn2 provincial composite wage range: approximately `12.8426–17.4810`.

Therefore all 62 provincial states are correctly classified as `UNOBSERVED_OR_INTERPOLATION_NOT_AUTHORIZED`. No provincial point may inherit an interior/ambiguous/lower/upper standalone health label from the current map.

## Association evidence

For the 20 provinces that converge in turn1 and fail in turn2, consumed `ra` rises in 20/20 and consumed composite wage falls in 20/20. This is descriptive co-movement only. Because both endpoints lie outside the standalone wage coverage, the evidence does not establish a health-frontier crossing or a causal return/wage mechanism.

Return-guard and wage-guard states do not uniquely separate convergence from failure in the accepted evidence.

## Scientific interpretation

The audit resolves the semantic question but reveals a more fundamental experimental-domain mismatch: prior standalone scans used a household-wage coordinate range numerically far below the actual multi-province household composite-wage range. Those scans remain valid isolated household experiments, but they are not sufficient to classify actual provincial states.

This acceptance does not authorize return-mapping redesign, wage rescaling, interpolation-based health boundaries, or further one-dimensional `ra` refinement.

Standalone contaminated-row KFE remains distinct from the unresolved corrected-2018 multi-province finite-box upper-`b` leakage and MATLAB-style pinning blocker. The known `(.06,.8)` KFE signed pathology remains non-admissible and uncorrected.

Results eligibility=`FALSE`.

## Exactly one next Owner gate

`OWNER_REVIEW_TWO_DIMENSIONAL_HEALTH_REGION_UNRESOLVED`

Owner/Reviewer should decide the next bounded experiment needed to extend the standalone `(ra,w)` health map into the actual provincial household-wage domain before any provincial return-mapping redesign is considered.
