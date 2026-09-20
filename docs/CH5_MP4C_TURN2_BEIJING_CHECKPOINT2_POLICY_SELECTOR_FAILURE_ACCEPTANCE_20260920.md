# Chapter 5 turn-2 Beijing checkpoint-2 policy-selector failure acceptance

Date: 2026-09-20

Reviewer verdict:

`ACCEPTED_FAIL__TURN2_BEIJING_CHECKPOINT2_F0579_NO_ADMISSIBLE_POLICY__CURRENT_SELECTOR_AUTHORITY_FAILS_CLOSED__SINGLE_CELL_BRANCH_ROOT_FORENSIC_AUTHORIZED`

## Accepted candidate

- live-main baseline: `a6fbf9d66d4d3603759e87f845e71bc4597c0e1c`
- Builder candidate: `37e563a87bf0dc1fb90224b03e0c4df9daea9d5f`
- candidate tree reported/read back by Builder: `c1f6e431edb03c37fe1cb884ae5b44040d18415d`
- ancestry independently verified: `2 ahead / 0 behind`, merge-base exactly baseline
- GitHub compare interface returned a capped file list with no CURRENT paths; Builder reports the full task diff as two task driver/test paths, one report, and run001 evidence
- ordinary non-force push and remote SHA/tree readback passed
- Builder did not merge main and did not publish a successor.

The candidate has been fast-forwarded into live `main`.

## Exact accepted first failure

Terminal:

`FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`

First failing object:

- province: 北京
- province_index: `0`
- checkpoint: `2`
- F-order flat index: `579`
- state index: `(b,a,z)=(19,8,1)`
- physical state:
  - `b=5`
  - `a=4.2105263157894735`
  - `z=1.3`
- selector outcome:
  `NO_ADMISSIBLE_POLICY`
- checkpoint-2 D2/Q: not assembled.

The durable failure-cell receipt is:

`reports/ch5_mp4c_corrected_optionb_turn2_unique_closed_class_kfe_20260920_run001/household/p00_北京/checkpoint_002/cell_0579.json`

and is accepted as the exact scientific failure witness under the current selector authority.

## Reached checkpoints

Checkpoint 0:

- B: `0.35948978452765235`
- D: N.A.
- D2/Q: PASS
- direct solve backward error:
  `2.1754586146795478e-16`.

Checkpoint 1:

- B: `0.019968227378343403`
- D: `0.5603661628256393`
- primary convergence: FAIL
- exact cycle: none
- approximate period-2/3 cycle: none
- D2/Q: PASS
- direct solve backward error:
  `1.4650295837509506e-16`.

Checkpoint 2 stopped inside the partial policy map before D2/Q construction.

## Failure-cell evidence

Persisted cell inputs:

- `p_b_backward = p_b_forward = 0.005058006084641677`
- `p_a_backward = -0.00014542975673859096`
- `p_a_forward = -0.0004814219651986697`
- effective illiquid return:
  `0.8815438210537105`
- liquid return:
  `0.02`
- net wage:
  `21.428042860932116`
- transfer income:
  `0.1`.

The inactive upper-b candidates fail the boundary/derivative/KKT gates and are not accepted.

For the active upper-b regimes:

- negative transfer is rejected before scalar-root execution because more than one illiquid derivative branch survives the current pre-root viability screen:
  `DERIVATIVE_BRANCH_NOT_UNIQUE_BEFORE_ROOT`;
- zero-kink invokes the liquid boundary root and returns:
  `ROOT_FAILURE_NO_UNIQUE_BRACKET`;
- positive transfer obtains a root but fails transfer-sign/KKT admissibility.

Therefore the accepted current-selector result is legitimately `NO_ADMISSIBLE_POLICY` under the frozen implementation.

## Scientific interpretation boundary

This acceptance does **not** yet establish that the continuous constrained household problem has no feasible control at this state.

The failure occurs at a selector enumeration/root-domain gate. In particular, the active upper-b negative regime is rejected before its surviving illiquid derivative branches are each evaluated at their own liquid-boundary root.

That pre-root uniqueness rule may be either:

1. scientifically necessary to preserve a previously adopted boundary selection law; or
2. overly restrictive and masking a uniquely admissible post-root branch.

The current evidence does not decide between these possibilities.

No selector law is changed by this acceptance.

## Scientific ledger

Accepted actual turn-2 run consumption:

- source-native initializations: 1
- labor roots attempted/returned: 800/800
- policy-map attempts: 3
  - complete: 2
  - partial failed: 1
- selector evaluations: 2,180
- scalar selector roots: 1,154
- liquid-Z roots: 422
- interior-a / joint roots: 0 / 0
- D2/Q assemblies: 2
- direct HJB updates: 2
- completed post-update evaluations: 1
- SCC / restricted GESVD / full-space GESVD: 0 / 0 / 0
- KFE candidate / full-Q stationarity: 0 / 0
- aggregates/integration/firms: 0
- scientific retries / solver substitutions: 0 / 0
- turn 3 / K1B / K2 / MATLAB / GE / Results: 0.

The partial checkpoint-2 selector consumption is reconciled from the durable failure-cell cumulative budget without scientific recomputation.

## Evidence

Run root:

`reports/ch5_mp4c_corrected_optionb_turn2_unique_closed_class_kfe_20260920_run001/`

Sealed manifest:

`50D2E87C94E762D3936C64E3AAD416F600118AEBB8DCE1588DB369938FA2351A`

with 612 entries and 9,677,554 bytes. Independent readback PASS and pre/post code freeze matched.

## Route consequence

No fresh turn-2 HJB rerun is authorized yet.

The next bounded task is a single-cell root-domain forensic using only the persisted failure-cell state/derivatives and the already accepted selector equations.

It may evaluate the upper-b active negative-transfer derivative branches independently under the same frozen multiplier/root domain and apply the existing downstream KKT/direction/boundary admissibility checks.

It must not modify the selector or perform a household HJB update.

Only after that forensic can the Reviewer decide whether the failure is:

- a genuine no-admissible-policy event;
- a pre-root branch-uniqueness false negative suitable for a narrowly scoped selector repair; or
- an unresolved selector ambiguity requiring Owner authority.

Results eligibility remains `FALSE`.
