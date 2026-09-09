# CH5 MP4C corrected-2018 five-turn KFE leakage attribution

Date: 2026-09-09. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Using only the already-saved five-turn corrected-2018 operator/density/drift artifacts, perform a zero-science-call forensic attribution of the turn 4–5 KFE/distribution blocker.

Determine whether the observed source-free stationarity failure is explained by the same finite-box upper-b leakage plus contaminated-row/pinning algebra previously established in the accepted call725 `rah=.07` KFE mass-balance attribution, and quantify the mechanism across provinces and turns.

This task is post-processing only. It does not authorize any new HJB/KFE/firm/controller/trajectory/model solve.

## 2. Required authorities

Read:

- `docs/CH5_MP4C_2018_CORRECTED_INPUT_FIVE_TURN_PREFIX_ACCEPTANCE.md`;
- `docs/CH5_MP4C_CALL725_RAH_0P07_KFE_MASS_BALANCE_ATTRIBUTION_ACCEPTANCE.md`;
- the accepted five-turn report package under `reports/mp4c_2018_corrected_five_turn_20260909/`;
- current governance/status docs.

Accepted five-turn candidate: `9864129dd2e97bae97238ab9cc588aea48682d29`.

## 3. Scientific-call budget

All zero:

- scientific processes 0;
- trajectory/turn/province updates 0;
- household/HJB/KFE 0;
- root/Brent/direct/iterative/eigen solves 0;
- firm/wage/migration/capital allocation/controller 0;
- MATLAB/GE/annual/IRF/Results 0.

Allowed only:

- read saved artifacts;
- array/matrix reconstruction from saved artifacts;
- pure algebra/post-processing;
- hashes/serialization/tests.

If required saved artifacts are missing, return a bounded evidence-gap verdict rather than rerunning science.

## 4. Core forensic checks

For each available province and turn, with primary emphasis on turns 4–5:

1. Identify the exact saved post-loop KFE operator used for the returned density.
2. Confirm transpose/orientation, flattening order, normalization weights, row-replacement/pin index and RHS convention.
3. Reconstruct source-free residual `r = A.T @ g` (or the exact accepted equivalent using the saved operator convention).
4. Separate pin-row residual from off-pin residuals.
5. Compute outward-leak vector from saved drift/operator and classify faces: lower-b, upper-b, lower-a, upper-a.
6. Compute density-weighted escape flow by face.
7. Check the signed mass-balance identity linking weighted sum of source-free residual to outward escape, up to floating-point reconstruction error.
8. If row replacement is present, compute the implicit balancing source intensity implied by the dropped row and compare it with total escape.
9. Verify that machine-scale negative density mass cannot explain the material source-free residual.
10. Quantify upper-b face probability mass and its relation to escape.

Do not interpret the row replacement as an economic entry/exit mechanism unless source code explicitly implements one. If the algebra is equivalent to an implicit source, state that it is an algebraic consequence of finite-box closure/pinning, not an adopted household entry process.

## 5. Cross-province / cross-turn attribution

Produce national summaries for turns 4 and 5:

- number of provinces with material source-free residual;
- number of provinces where pin row accounts for approximately all L1 residual mass;
- number of provinces with positive upper-b escape;
- total positive leak-cell count by face;
- max/median density-weighted escape;
- max/median upper-b face mass;
- residual-to-escape signed identity error distribution;
- implicit source vs escape discrepancy distribution;
- top provinces by escape intensity and by upper-b face mass.

Also inspect turn 3 if saved artifacts permit, to determine whether the sharp asset collapse coincides with the same leakage/source mechanism already present at that turn.

## 6. Comparison to accepted call725 mechanism

Explicitly compare the corrected-2018 turn 4–5 mechanism to the accepted call725 `rah=.07` attribution on these dimensions:

- post-loop operator versus HJB-loop operator;
- upper-b outward drift/leakage;
- row replacement / dropped source-free equation;
- pin-row concentration of stationarity residual;
- density-weighted escape;
- implicit source equivalence;
- sign/magnitude of negative density entries;
- whether the same source-code boundary construction is implicated.

Allowed classifications:

- `SAME_FINITE_BOX_UPPER_B_LEAKAGE_AND_PINNING_MECHANISM_CONFIRMED`;
- `PARTIAL_MECHANISM_MATCH__ADDITIONAL_RESIDUAL_SOURCE_PRESENT`;
- `DISTINCT_KFE_FAILURE_MECHANISM`;
- `INSUFFICIENT_SAVED_ARTIFACTS_FOR_ATTRIBUTION`.

## 7. Source-code attribution

Using current frozen source code and saved source identities only, identify the exact code path that creates any retained-diagonal / omitted-outside-grid upper-b leakage, and the exact KFE row-replacement/pinning path.

Do not modify source code.

Do not propose D1–D3 as adopted fixes. If mentioned, clearly label as previously deferred redesign proposals.

## 8. Asset interpretation boundary

For Anhui turn 3–5 and any high-leak provinces, compare A/B/A+B changes with density validity diagnostics.

Do not claim the asset collapse is caused by leakage unless the saved evidence supports a direct attribution. Allowed conclusions include:

- temporally coincident with invalid density;
- consistent with invalid-density contamination;
- not causally separable from saved evidence.

Do not promote C/L/A/B as accepted economic moments while source-free stationarity fails.

## 9. Evidence root

Use fresh root:

`D:\ProjectTemp\ch5-2018-five-turn-kfe-leakage-attribution-20260909-001`

Use a fresh suffix if occupied. Never overwrite predecessor evidence.

Required repository-safe outputs:

- `docs/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION_REPORT.md`;
- machine-readable per-province/per-turn mass-balance ledger;
- cross-province summary;
- pin-row attribution summary;
- boundary leakage summary;
- call725 mechanism comparison;
- source-code attribution receipt;
- call ledger showing all scientific/model calls = 0;
- tests/static checks;
- manifest/readback;
- terminal result.

Do not commit private raw/canonical/proprietary files.

## 10. Allowed primary verdicts

- `FIVE_TURN_KFE_ATTRIBUTION_PASS__SAME_UPPER_B_LEAKAGE_AND_PINNING_MECHANISM_CONFIRMED`;
- `FIVE_TURN_KFE_ATTRIBUTION_PARTIAL__ADDITIONAL_RESIDUAL_SOURCE_PRESENT`;
- `FIVE_TURN_KFE_ATTRIBUTION_DISTINCT_MECHANISM`;
- `FIVE_TURN_KFE_ATTRIBUTION_BLOCKED__INSUFFICIENT_SAVED_ARTIFACTS`.

## 11. Authority after completion

Even on PASS:

- no turn 6+;
- no new KFE solve;
- no steady state;
- no GE/annual/IRF/Results;
- no production boundary/grid/source/pinning repair;
- Results eligibility remains FALSE.

Commit and non-force push a dedicated branch. Do not merge main and do not start a successor scientific task.
