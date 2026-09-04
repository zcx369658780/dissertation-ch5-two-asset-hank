# CH5_TWO_ASSET_HANK_MP4C_2018_DIAGNOSTIC_KFE_GAUGE_REDESIGN_COMPARISON_FRESH_EXECUTION_AFTER_SPARSE_NORM_REPAIR

Date: 2026-09-04

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / diagnostic numerical-comparison executor

Owner: final scientific authority

## 1. Authority basis

Immediate predecessor execution:

`6a6dec124bc113ea257835b445d40edea59acc08`

with terminal:

`MP4C_2018_KFE_GAUGE_HELPER_SPARSE_NORM_ZERO_SCIENCE_REPAIRED_AND_CERTIFIED__NO_PARAMETER_CHANGE__READY_FOR_FRESH_GAUGE_COMPARISON_EXECUTION_TASK`

The predecessor certifies that the prior gauge-comparison blocker was a helper-layer sparse-matrix norm API defect, not a model-parameter problem. The sparse induced infinity norm path is now zero-science certified. No economic, model, grid, HJB, KFE, tolerance, controller, calendar, G0/G1/G2, operator, cell-weight, solve-order, or solve-budget parameter changed.

Owner's previously approved scientific route remains controlling:

> diagnostic-only KFE gauge redesign comparison comparing mass-normalization gauge versus adaptive-row diagnostic oracle; no production change and no 2018 GE rerun.

This task authorizes a **fresh bounded execution** of that same comparison after the instrumentation repair.

## 2. Live continuity

At start:

1. `git fetch origin`;
2. require this exact task live on `origin/main` as direct child of `6a6dec124bc113ea257835b445d40edea59acc08`;
3. require `HEAD == origin/main`, ahead/behind `0/0`, tracked worktree clean;
4. read `AGENTS.md`, all CURRENT project rules, the original gauge-comparison task/report, the sparse-norm repair task/report, nullspace cross-check report, accepted KFE parity authority, and accepted end-to-end aggregate authority.

No execution from a dirty tracked worktree.

## 3. Certified helper identity and mandatory preflight

Certified helper-repair evidence root:

`D:\ProjectTemp\ch5-mp4c-2018-kfe-gauge-helper-sparse-norm-zero-science-repair-20260904-001`

Require its audit manifest SHA-256:

`C9EB92BAB4BFFF7B61A135647F5A58D97D178883AD01BD984DFB11C8461B957D`.

Use the exact repaired helper bytes bound by that manifest. Do not re-edit the helper before execution.

Before any scientific sparse solve, perform a zero-science execution preflight using synthetic sparse matrices and synthetic vectors only. Exercise the complete post-solve diagnostic path that will be applied after a real solve, including:

- sparse-safe matrix infinity norm;
- vector infinity norm;
- backward-error scale construction;
- residual diagnostics;
- normalization diagnostics;
- negative-entry/negative-mass diagnostics;
- result serialization / persistence.

No `spsolve` or frozen scientific operator may be used in this preflight. If the synthetic full diagnostic path fails, STOP before consuming the fresh solve budget.

Required preflight marker:

`MP4C_2018_GAUGE_COMPARISON_FULL_POSTSOLVE_DIAGNOSTIC_PREFLIGHT_PASS__ZERO_SCIENCE__FRESH_8_SOLVE_BUDGET_AUTHORIZED`

## 4. Scientific contract — inherit without change

The scientific definitions from:

`tasks/CH5_TWO_ASSET_HANK_MP4C_2018_DIAGNOSTIC_KFE_GAUGE_REDESIGN_COMPARISON.md`

remain controlling except that this task grants a new execution budget after the certified helper repair.

Freeze before solving:

- accepted backward-error formula:
  `residual_inf <= 256*eps64*max(1, ||M||_inf*||x||_inf, ||rhs||_inf)`;
- accepted density normalization rule;
- accepted density comparison tolerance;
- accepted aggregate formulas/tolerance;
- G0/G1/G2 definitions;
- O1/O2/O3 identities and cell weights.

No parameter tuning is authorized.

## 5. Frozen operator suite

Use exactly the same three frozen operators as the original comparison task.

### O1 — accepted MATLAB post-convergence operator

Common-operator identity:

`7A2ADC63CE7A4BB5184036E4CFC07EC082185C90C5B818C572ED05756D222C0F`

Expected shape/order/spacing:

- `(b,a,z)=(5,5,2)`;
- Fortran/MATLAB ordering;
- `db=0.25`, `da=0.5`, cell weight `0.125`.

### O2 — accepted Python own post-convergence operator

Use the exact preserved accepted Python post-convergence operator from the accepted HJB artifact root. Do not rerun HJB. Record and verify its stored identity before solving.

### O3 — captured 2018 failing operator

Preserved root:

`D:\ProjectTemp\ch5-mp4c-2018-final-production-path-faithful-durable-execution-20260903-001`

Require retrospective manifest SHA-256:

`D0472539EA553CFCFF7D34046EA71C8C68DD78C7FF7D44F58F7A3AD50D06C490`

Require raw anchors:

- A: `A17AA9CF512D4D3FDD79235D0D1897CFB20486D2EF5FAA68850910C849AA1B42`;
- A transpose: `7C1ADEDEE5B26BB30B5A8CC1C9D3D0E83DFF18FAE7860C39986E9E6C2D8FDA66`;
- legacy contaminated matrix: `B04F5A4B99135272FCFF61BEAE220A2C25F5455E478F7994C1394CD6EC869EF4`;
- RHS: `C8ADAA98B7B1B7484CAF2A1C4E44D7FD0106D62BCC8FB10084D11CD877CDABFB`;
- raw solve: `F4D51DC00DBAB73F63322A73692EBEA13CAEC2D0A1204A514CBE39329DF8B8E2`.

O3 cell weight remains the frozen 20x20x2 production `db*da` contract, with no `dz` or endpoint weight.

Permanent caveat:

`CAPTURE_TIME_RAW_HASH_GAP_REMAINS__RETROSPECTIVE_CURRENT_FILE_INTEGRITY_CERTIFIED`.

## 6. Gauge definitions

For every operator, let `T=A.transpose()` and `n=T.shape[0]`.

### G0 — legacy/source-faithful baseline

`r_legacy = floor(0.37*n)-1`.

Replace row `r_legacy` by unit row, set `rhs[r_legacy]=0.007`, solve once, and if finite normalize by `sum(raw)*cell_weight`.

Run G0 once for O1 and once for O2 only.

For O3 do **not** rerun G0; reuse the already captured legacy failure evidence.

### G1 — mass-normalization gauge

Keep row index `r_legacy`, replace that row with `cell_weight*ones(n)^T`, set `rhs[r_legacy]=1.0`, solve once. The solution is directly the normalized candidate; do not post-normalize except as a diagnostic check.

### G2 — adaptive-row diagnostic oracle

Use `scipy.linalg.svd(T_dense, full_matrices=False, lapack_driver='gesvd')` only to obtain a directional near-null witness. Do not treat the absolute smallest singular value as exact.

Normalize by `max(abs(v))=1` and choose the smallest index achieving `max(abs(v))`. Replace that row with a unit row, set RHS there to `0.007`, solve once, then apply the same post-solve mass normalization as G0 if finite.

G2 remains a diagnostic oracle only, not a production SVD fallback proposal.

## 7. Fresh solve budget

The predecessor task consumed one O1/G0 invocation but produced no qualified result because instrumentation failed. This new task grants a **fresh, independent, bounded comparison budget** after zero-science repair.

Maximum new sparse solves in this task:

- O1: G0 once + G1 once + G2 once = 3;
- O2: G0 once + G1 once + G2 once = 3;
- O3: G1 once + G2 once = 2.

Total maximum = **8 new sparse solves**.

No automatic retries. Each predeclared pair may be invoked at most once in this task.

If a solve warns or returns nonfinite output, persist the raw result and diagnostics and proceed only to the next predeclared pair. Do not retune, regularize, perturb, change gauges, or rerun a consumed pair.

If instrumentation fails after a real solve, fail closed and do not rerun that pair.

## 8. Required diagnostics

For every finite candidate report:

- system shape / nnz;
- gauge type / selected row;
- warning status;
- finite status;
- mass and mass error;
- min/max density;
- negative-entry count;
- most-negative value;
- weighted negative mass;
- `||A'g||_inf` and `||A'g||_2`;
- backward-error bound and actual residual;
- backward-error PASS/FAIL.

Finiteness alone is not acceptance.

## 9. O1/O2 pure-gauge invariance

Use G0 as the legacy-success baseline for O1/O2. Compare G1 and G2 to G0 using the already accepted density tolerance.

Report at least max absolute difference, weighted L1, L2, mass difference, residual difference, and negative-mass diagnostics.

Scientific gate:

> On operators where legacy G0 succeeds, gauge redesign must preserve the normalized stationary density within accepted numerical tolerance to count as a pure gauge redesign.

Material deviation means semantic redesign and blocks production use.

## 10. O1/O2 aggregate invariance

Using preserved accepted policy arrays only, compute source-authorized `C^ss`, `L^ss`, `A^ss`, `B^ss`, and `A^ss+B^ss` for successful densities. Do not rerun HJB or household policies.

Compare G1/G2 against G0 using the accepted aggregate tolerance. If O2 policy arrays are unavailable, state:

`AGGREGATE_COMPARISON_UNAVAILABLE_FOR_O2__NO_REGENERATION`.

## 11. O3 / 2018 captured-operator diagnostic

Run exactly once each:

- O3/G1;
- O3/G2.

Do not rerun O3/G0.

For each candidate evaluate full numerical and economic-admissibility diagnostics. If both are finite and backward-error certified, compare G1 versus G2 density differences and negative-mass diagnostics.

Do not compute 2018 aggregates unless exact failing-call policy arrays already exist in the preserved evidence root and are cryptographically bound. Otherwise state:

`2018_POLICY_ARRAYS_NOT_CAPTURED__AGGREGATE_COUNTERFACTUAL_NOT_AUTHORIZED`.

Do not rerun HJB to obtain them.

## 12. Interpretation and classification

Answer explicitly:

1. Does G1 preserve accepted O1/O2 normalized densities?
2. Does G2 preserve them?
3. Does O3/G1 yield a finite, normalized, backward-error-certified and economically admissible density?
4. Does O3/G2?
5. If both work, do the normalized O3 densities agree?
6. Does the evidence support G1 as a production candidate, or does Owner review remain unresolved?

Choose the strongest supported classification from the original comparison ladder, including:

- `MASS_NORMALIZATION_GAUGE_PRESERVES_ACCEPTED_DENSITIES_AND_CLOSES_CAPTURED_2018_OPERATOR__ADAPTIVE_ROW_AGREES__PRODUCTION_RULE_OWNER_REVIEW_REQUIRED`;
- `MASS_NORMALIZATION_GAUGE_PRESERVES_ACCEPTED_DENSITIES_AND_CLOSES_CAPTURED_2018_OPERATOR__ADAPTIVE_ROW_DIAGNOSTIC_DIFFERS_OR_IS_UNNECESSARY`;
- `ADAPTIVE_ROW_ONLY_CLOSES_CAPTURED_2018_OPERATOR__MASS_NORMALIZATION_GAUGE_NOT_CERTIFIED__PRODUCTION_REDESIGN_REMAINS_UNRESOLVED`;
- `BOTH_GAUGES_CLOSE_LINEAR_SYSTEM_BUT_2018_DENSITY_IS_NOT_ECONOMICALLY_ADMISSIBLE__NO_PRODUCTION_REPAIR_AUTHORIZED`;
- `GAUGE_REDESIGN_CHANGES_ACCEPTED_LEGACY_SUCCESS_DENSITY_MATERIALLY__NOT_A_PURE_GAUGE_REDESIGN__NO_PRODUCTION_REPAIR_AUTHORIZED`;
- `DIAGNOSTIC_KFE_GAUGE_REDESIGN_COMPARISON_INCONCLUSIVE__NO_PRODUCTION_REPAIR_AUTHORIZED`.

## 13. Hard no-production boundary

Even if G1 clearly dominates G2:

- do not modify production KFE;
- do not modify faithful KFE source;
- do not rerun 2018 GE;
- do not run shock/IRF;
- do not declare 2009-2022 annual acceptance;
- do not create a Results claim.

Return evidence to ChatGPT L3 / Owner for the next scientific decision.

## 14. Evidence root and report

Use fresh no-overwrite root:

`D:\ProjectTemp\ch5-mp4c-2018-diagnostic-kfe-gauge-redesign-comparison-fresh-after-sparse-norm-repair-20260904-001`

Persist at minimum:

- `authority_and_source_identity.json`;
- `certified_helper_identity.json`;
- `zero_science_full_diagnostic_preflight.json`;
- `accepted_kfe_contract.json`;
- `operator_suite_identity.json`;
- `gauge_definitions.json`;
- `solve_budget_ledger.json`;
- `o1_gauge_results.json`;
- `o2_gauge_results.json`;
- `o3_2018_gauge_results.json`;
- `accepted_operator_density_comparison.csv`;
- aggregate comparison artifact if available;
- O3 G1-vs-G2 comparison if both finite;
- negative-mass/backward-error summary;
- `classification.json`;
- stdout/stderr;
- `audit_manifest.json`.

Required report:

`docs/CH5_TWO_ASSET_HANK_MP4C_2018_DIAGNOSTIC_KFE_GAUGE_REDESIGN_COMPARISON_FRESH_AFTER_SPARSE_NORM_REPAIR_REPORT.md`

If execution completes consistently, only one report-only commit + push is authorized.

Suggested commit message:

`Rerun MP4C 2018 diagnostic KFE gauge comparison after helper repair`

After push: fresh-fetch and require `HEAD == origin/main`, ahead/behind `0/0`, tracked worktree clean.

PASS terminal:

`MP4C_2018_DIAGNOSTIC_KFE_GAUGE_REDESIGN_FRESH_COMPARISON_COMPLETE__MASS_NORMALIZATION_AND_ADAPTIVE_ROW_CLASSIFIED__NO_PRODUCTION_CHANGE_NO_2018_RERUN`

Blocked terminal:

`MP4C_2018_DIAGNOSTIC_KFE_GAUGE_REDESIGN_FRESH_COMPARISON_BLOCKED__NO_PRODUCTION_CHANGE_NO_2018_RERUN`.
