# CH5_TWO_ASSET_HANK_MP4C_2018_DIAGNOSTIC_KFE_GAUGE_REDESIGN_COMPARISON

Date: 2026-09-04

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / diagnostic numerical-comparison executor

Owner: final scientific authority

## 1. Owner decision and authority basis

Immediate predecessor execution:

`20f39fbcda4b92b45d7b61ec0e323aa49c5b3d94`

with accepted classification:

`NULLSPACE_FORENSIC_QUALITATIVE_GAUGE_RESULT_CONFIRMED__BOTTOM_SINGULAR_VALUE_DRIVER_DEPENDENT`

The Owner has explicitly approved the next route:

> Enter a **diagnostic-only KFE gauge redesign comparison** comparing a mass-normalization gauge with an adaptive-row fallback. Do not modify production and do not rerun 2018.

Accepted predecessor facts:

- the absolute bottom singular value of the captured 2018 matrix is LAPACK-driver/mode dependent and is **not** an exact nullspace certificate;
- the dominant numerical near-null direction is nevertheless cross-driver stable;
- source-faithful fixed row 295 has negligible component in that direction and remains an ineffective gauge under the frozen numerical-rank convention;
- row 620 removes the dominant numerical near-null direction in rank-only diagnostics;
- prior Anhui HJB nonconvergence is recurrent and associated with the KFE failure, but is not established as a sufficient cause;
- source-faithful boundary row nonconservation is not automatically a Python implementation defect;
- the permanent evidence caveat remains:
  `CAPTURE_TIME_RAW_HASH_GAP_REMAINS__RETROSPECTIVE_CURRENT_FILE_INTEGRITY_CERTIFIED`.

This task is a bounded **diagnostic solver-semantics comparison**. It is not production implementation authority and it does not authorize a new 2018 GE execution.

## 2. Live continuity

At start:

1. `git fetch origin`;
2. require this exact task live on `origin/main` as direct child of `20f39fbcda4b92b45d7b61ec0e323aa49c5b3d94`;
3. require `HEAD == origin/main`, ahead/behind `0/0`, tracked worktree clean;
4. read:
   - `AGENTS.md`;
   - `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
   - all CURRENT rules;
   - final 2018 durable execution report;
   - retrospective evidence-integrity certification report;
   - captured-operator forensic report;
   - nullspace numerical-consistency cross-check report;
   - accepted MATLAB-faithful KFE parity reports/tasks needed to recover the accepted KFE tolerance and aggregate formulas;
   - faithful KFE source and accepted end-to-end stationary household aggregate authority.

No execution from a dirty worktree.

## 3. Hard boundary

Task type:

`DIAGNOSTIC_ONLY_KFE_GAUGE_REDESIGN_COMPARISON__NO_PRODUCTION_CHANGE__NO_2018_RERUN`

Forbidden:

- any new 2018 annual steady-state / GE outer-loop execution;
- any new HJB solve;
- household-model solve;
- stationary controller execution;
- MATLAB execution;
- R/PLM execution;
- production/model/diagnostic/test source modification;
- changing the production contaminated-row rule;
- changing HJB/KFE equations, grid, parameters, tolerances, controller, calendar/input semantics;
- pseudoinverse, regularization, fallback density, matrix perturbation beyond the two predeclared diagnostic gauges below;
- shock/IRF/Results work.

Allowed scientific computation is strictly limited to **linear algebra / KFE-style solves on already frozen stored operators** under the predeclared gauge candidates below.

Any helper code must live only in a fresh external evidence root. No helper may be committed to the repository.

## 4. Frozen operator suite

Use exactly three operator objects unless one accepted object is unavailable; if unavailable, STOP rather than substitute an unreviewed object.

### O1 — accepted MATLAB post-convergence operator

From the accepted HJB/KFE parity artifacts:

`D:\ProjectTemp\ch5-hjb-propagation-aware-final-20260830-001`

and/or the accepted same-operator KFE root:

`D:\ProjectTemp\ch5-kfe-same-operator-20260830-001`

Use the exact accepted MATLAB operator `A_M` whose common-operator identity was previously frozen as:

`7A2ADC63CE7A4BB5184036E4CFC07EC082185C90C5B818C572ED05756D222C0F`

Expected accepted shape/order/spacing:

- `(b,a,z)=(5,5,2)`;
- Fortran/MATLAB ordering;
- `db=0.25`;
- `da=0.5`;
- cell weight `0.125`.

### O2 — accepted Python own post-convergence operator

Use the exact accepted Python post-convergence operator `A_P` from the same accepted HJB artifact root.

Do not rerun HJB to regenerate it.

Record its stored artifact identity before any solve.

### O3 — captured 2018 failing operator

Preserved root:

`D:\ProjectTemp\ch5-mp4c-2018-final-production-path-faithful-durable-execution-20260903-001`

Require retrospective manifest SHA-256:

`D0472539EA553CFCFF7D34046EA71C8C68DD78C7FF7D44F58F7A3AD50D06C490`

Require current raw hashes:

- A: `A17AA9CF512D4D3FDD79235D0D1897CFB20486D2EF5FAA68850910C849AA1B42`;
- A transpose: `7C1ADEDEE5B26BB30B5A8CC1C9D3D0E83DFF18FAE7860C39986E9E6C2D8FDA66`;
- captured legacy contaminated matrix: `B04F5A4B99135272FCFF61BEAE220A2C25F5455E478F7994C1394CD6EC869EF4`;
- RHS: `C8ADAA98B7B1B7484CAF2A1C4E44D7FD0106D62BCC8FB10084D11CD877CDABFB`;
- raw solve: `F4D51DC00DBAB73F63322A73692EBEA13CAEC2D0A1204A514CBE39329DF8B8E2`.

For O3 use the frozen production cell weight implied by the captured 20x20x2 grid (`db*da` only, no dz), verified from the production input/grid receipts and faithful aggregation contract before solving.

Do not regenerate any 2018 policy/HJB object.

## 5. Recover existing accepted numerical certificates before solving

Before any new KFE-style solve, read the accepted MATLAB-faithful KFE parity gate and freeze in the evidence record:

- contaminated-system backward-error formula and numerical multiplier;
- accepted density normalization convention;
- accepted nonnegativity / density comparison tolerances if explicitly frozen;
- accepted aggregate formulas and weights for `C`, `L`, `A`, `B` and total assets.

Do not invent a new parity threshold where an accepted one already exists.

If accepted tolerance or aggregate formula is ambiguous, STOP before new solves.

## 6. Three gauge systems

For every operator define `T = A.transpose()` and `n = T.shape[0]`.

### G0 — legacy/source-faithful fixed-row baseline

Legacy row:

`r_legacy = floor(0.37*n) - 1`.

Legacy system:

- replace row `r_legacy` of `T` by unit row `e_r^T`;
- RHS all zero except `rhs[r_legacy] = 0.007`;
- solve with the same sparse direct solver family used by the faithful Python KFE path;
- if finite, normalize by the frozen source-faithful mass convention:
  `g = raw / (sum(raw)*cell_weight)`.

For O1/O2 this is a diagnostic repeat on frozen operators and is bounded to one solve per operator.

For O3 **do not rerun G0**: reuse the already captured warning/nonfinite raw solve and published evidence as the legacy-failure baseline.

### G1 — mass-normalization gauge candidate

Keep the same row index `r_legacy`, but replace that row with the global source-faithful mass equation:

`cell_weight * ones(n)^T`.

RHS:

- all zero;
- `rhs[r_legacy] = 1.0`.

The resulting solution is directly the normalized density candidate `g_mass`.

Do not perform a second post-hoc normalization except as a diagnostic check; report the mass error `abs(sum(g_mass)*cell_weight - 1)`.

Do not introduce `dz`, productivity probability weights, trapezoid weights, or endpoint weights unless the already accepted MATLAB aggregate/KFE source contract explicitly requires them. The accepted source contract controls.

### G2 — adaptive-row fallback candidate (diagnostic oracle only)

This candidate is **not** a production algorithm proposal in this task.

For each operator compute one deterministic near-null witness from the stored `T` using:

`scipy.linalg.svd(T_dense, full_matrices=False, lapack_driver='gesvd')`.

Use the last right-singular vector only as a **directional witness**, consistent with the predecessor cross-driver conclusion; do not interpret its absolute smallest singular value as exact.

Normalize by `max(abs(v))=1` and choose:

`r_adapt = smallest index achieving max(abs(v))`.

Adaptive unit-row system:

- replace row `r_adapt` of `T` with `e_r_adapt^T`;
- RHS all zero except `rhs[r_adapt] = 0.007`;
- solve once;
- if finite, normalize using the same source-faithful post-solve mass normalization as G0.

Record `r_adapt`, `abs(v[r_legacy])`, `abs(v[r_adapt])`, and whether `r_adapt` belongs to a closed SCC when that information is already available or cheaply derivable from the stored operator.

This G2 construction is an **oracle diagnostic comparator** only. Do not recommend production SVD fallback merely because G2 succeeds.

## 7. Strict solve budget

Maximum new sparse solves:

- O1: G0 once, G1 once, G2 once = 3;
- O2: G0 once, G1 once, G2 once = 3;
- O3: G1 once, G2 once = 2;

Total maximum new sparse solves = **8**.

No automatic retries.

If a solve warns or returns nonfinite output, persist it and continue only to the next predeclared gauge/operator pair. Do not retune, perturb, regularize, change row beyond the predeclared candidate, or rerun the failed pair.

## 8. Required numerical diagnostics for every successful candidate

For every finite density candidate report:

- system matrix shape / nnz;
- selected gauge row and gauge type;
- solver warning status;
- finite raw/solution status;
- source-faithful total mass;
- mass error;
- `min(g)`, `max(g)`;
- negative-entry count;
- most-negative value;
- weighted negative mass:
  `sum(abs(g[g<0]))*cell_weight`;
- stationary residual `||A' g||_inf` and `||A' g||_2`;
- accepted backward-error certificate using the pre-frozen accepted formula;
- whether the candidate passes that certificate.

Do not treat finiteness alone as scientific acceptance.

## 9. Legacy-success equivalence gate on O1/O2

For O1 and O2, G0 is the legacy baseline.

Compare G1 and G2 to G0 using the accepted KFE parity/density tolerances recovered in section 5.

Report at minimum:

- max absolute density difference;
- weighted L1 density difference;
- L2 density difference;
- mass difference;
- stationary residual difference;
- negative-mass diagnostics.

The purpose is to test the claim:

> When legacy fixed-row KFE succeeds, changing only the gauge equation should leave the **normalized stationary density** invariant up to accepted numerical tolerance.

If either candidate materially changes the normalized density on O1/O2, classify it as a semantic redesign rather than a pure gauge redesign.

## 10. Household aggregate invariance on accepted operators

Using only already preserved accepted policy arrays associated with O1/O2, and only after re-reading the accepted aggregate-source contract, compute for each successful density:

- `C^ss`;
- `L^ss`;
- `A^ss`;
- `B^ss`;
- `A^ss+B^ss`.

Do not rerun HJB or household policies.

Compare G1/G2 aggregates against G0 and against already accepted aggregate artifacts where available.

Use the accepted aggregate comparison tolerance; do not invent a looser one.

If the required O2 policy arrays or exact source mapping are unavailable, report `AGGREGATE_COMPARISON_UNAVAILABLE_FOR_O2__NO_REGENERATION` and continue the density-only comparison. Do not regenerate anything.

## 11. 2018 captured-operator counterfactual diagnostic

For O3, G0 is the already captured legacy failure baseline.

Run exactly once each:

- G1 mass-normalization gauge;
- G2 adaptive-row oracle gauge.

For each candidate report the full diagnostics from section 8.

If both are finite and backward-error certified, compare G1 vs G2:

- max absolute density difference;
- weighted L1 difference;
- L2 difference;
- mass difference;
- negative-mass diagnostics;
- stationary residuals.

Do **not** compute 2018 `C/L/A/B` unless the exact captured failing-call policy arrays are already present in the preserved evidence root and cryptographically bound. If absent, explicitly state:

`2018_POLICY_ARRAYS_NOT_CAPTURED__AGGREGATE_COUNTERFACTUAL_NOT_AUTHORIZED`

Do not rerun HJB to obtain them.

## 12. Required scientific interpretation

The report must distinguish these questions:

1. Does G1 behave as a **pure normalization-gauge redesign** on accepted legacy-success operators?
2. Does G2 behave as a **pure unit-row gauge relocation** on accepted legacy-success operators?
3. On the captured 2018 operator, does G1 produce a finite, normalized, backward-error-certified and economically admissible density?
4. On the captured 2018 operator, does G2 produce the same?
5. If both work, are their normalized densities numerically consistent with one another?
6. Is there any evidence that a production redesign should prefer G1 over G2, or does Owner review remain necessary?

Do not collapse "linear system solved" into "economically valid stationary distribution".

Material negative mass, failed backward-error certificate, materially different G1/G2 densities, or large accepted-operator deviations must remain blockers.

## 13. Preferred classification ladder

Choose the strongest supported classification, with explicit sub-findings if needed:

- `MASS_NORMALIZATION_GAUGE_PRESERVES_ACCEPTED_DENSITIES_AND_CLOSES_CAPTURED_2018_OPERATOR__ADAPTIVE_ROW_AGREES__PRODUCTION_RULE_OWNER_REVIEW_REQUIRED`;
- `MASS_NORMALIZATION_GAUGE_PRESERVES_ACCEPTED_DENSITIES_AND_CLOSES_CAPTURED_2018_OPERATOR__ADAPTIVE_ROW_DIAGNOSTIC_DIFFERS_OR_IS_UNNECESSARY`;
- `ADAPTIVE_ROW_ONLY_CLOSES_CAPTURED_2018_OPERATOR__MASS_NORMALIZATION_GAUGE_NOT_CERTIFIED__PRODUCTION_REDESIGN_REMAINS_UNRESOLVED`;
- `BOTH_GAUGES_CLOSE_LINEAR_SYSTEM_BUT_2018_DENSITY_IS_NOT_ECONOMICALLY_ADMISSIBLE__NO_PRODUCTION_REPAIR_AUTHORIZED`;
- `GAUGE_REDESIGN_CHANGES_ACCEPTED_LEGACY_SUCCESS_DENSITY_MATERIALLY__NOT_A_PURE_GAUGE_REDESIGN__NO_PRODUCTION_REPAIR_AUTHORIZED`;
- `DIAGNOSTIC_KFE_GAUGE_REDESIGN_COMPARISON_INCONCLUSIVE__NO_PRODUCTION_REPAIR_AUTHORIZED`.

## 14. Evidence root

Preferred fresh no-overwrite root:

`D:\ProjectTemp\ch5-mp4c-2018-diagnostic-kfe-gauge-redesign-comparison-20260904-001`

Persist at minimum:

- `authority_and_source_identity.json`;
- `accepted_kfe_contract.json`;
- `operator_suite_identity.json`;
- `gauge_definitions.json`;
- `solve_budget_ledger.json`;
- `o1_gauge_results.json`;
- `o2_gauge_results.json`;
- `o3_2018_gauge_results.json`;
- `accepted_operator_density_comparison.csv`;
- `accepted_operator_aggregate_comparison.csv` if available;
- `o3_mass_vs_adaptive_density_comparison.json` if both finite;
- `negative_mass_and_backward_error_summary.csv`;
- `classification.json`;
- analysis stdout/stderr;
- `audit_manifest.json` for this new diagnostic root only.

## 15. Repository report and publication

Required report:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_DIAGNOSTIC_KFE_GAUGE_REDESIGN_COMPARISON_REPORT.md`

The report must include:

- Owner-authorized diagnostic scope;
- exact operator identities;
- exact G0/G1/G2 definitions;
- exact solve counts and zero retries;
- accepted-operator density/aggregate invariance results;
- 2018 G1/G2 diagnostics;
- negative-mass and backward-error results;
- strongest classification;
- explicit statement that production KFE remains unchanged;
- explicit statement that 2018 was not rerun;
- permanent capture-time-hash caveat.

If analysis completes consistently, authorize only one **report-only** commit + push.

Suggested commit message:

`Compare MP4C 2018 diagnostic KFE gauges`

After push:

- `git fetch origin`;
- require `HEAD == origin/main`;
- ahead/behind `0/0`;
- tracked worktree clean.

PASS terminal:

`MP4C_2018_DIAGNOSTIC_KFE_GAUGE_REDESIGN_COMPARISON_COMPLETE__MASS_NORMALIZATION_AND_ADAPTIVE_ROW_CLASSIFIED__NO_PRODUCTION_CHANGE_NO_2018_RERUN`

Blocked terminal:

`MP4C_2018_DIAGNOSTIC_KFE_GAUGE_REDESIGN_COMPARISON_BLOCKED__NO_PRODUCTION_CHANGE_NO_2018_RERUN`

## 16. No automatic production implementation

Even if G1 is clearly preferred, this task does **not** authorize production modification or another 2018 execution.

Return to ChatGPT L3 / Owner for the next scientific decision.
