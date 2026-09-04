# MP4C 2018 fresh diagnostic KFE gauge comparison after sparse-norm repair

## Terminal

`MP4C_2018_DIAGNOSTIC_KFE_GAUGE_REDESIGN_FRESH_COMPARISON_COMPLETE__MASS_NORMALIZATION_AND_ADAPTIVE_ROW_CLASSIFIED__NO_PRODUCTION_CHANGE_NO_2018_RERUN`

The strongest supported classification is:

`GAUGE_REDESIGN_CHANGES_ACCEPTED_LEGACY_SUCCESS_DENSITY_MATERIALLY__NOT_A_PURE_GAUGE_REDESIGN__NO_PRODUCTION_REPAIR_AUTHORIZED`

This is a bounded diagnostic comparison on frozen stored operators.  It is not
a production KFE repair, a 2018 annual/GE rerun, a HJB/household/stationary
execution, a 2009--2022 acceptance, or a Results claim.

## Authority, identity, and zero-science gate

- Live task authority: `cb14b839ed12c3bf27c6e66feef1171b3fb0c4a2`, the direct
  child of `6a6dec124bc113ea257835b445d40edea59acc08`.
- Start state after fetch and fast-forward: `HEAD == origin/main`,
  ahead/behind `0/0`, clean tracked worktree.
- Certified helper root:
  `D:\ProjectTemp\ch5-mp4c-2018-kfe-gauge-helper-sparse-norm-zero-science-repair-20260904-001`.
  Its audit-manifest SHA-256 was required and verified as
  `C9EB92BAB4BFFF7B61A135647F5A58D97D178883AD01BD984DFB11C8461B957D`.
  All 12 bound entries re-hashed successfully; the exact bound repaired helper
  bytes were imported without modification.
- Before touching a frozen operator, the required synthetic-only full
  post-solve diagnostic preflight persisted
  `MP4C_2018_GAUGE_COMPARISON_FULL_POSTSOLVE_DIAGNOSTIC_PREFLIGHT_PASS__ZERO_SCIENCE__FRESH_8_SOLVE_BUDGET_AUTHORIZED`.
  It exercised sparse matrix and vector infinity norms, residual and
  backward-error construction, normalization, negative mass, and JSON
  persistence.  Its sparse/dense matrix norm was exactly `10`; residual was
  `0`; mass error was `0`; and both `spsolve` and direct KFE density-entry
  guards recorded `0` calls.

The repair used the certified sparse-safe induced norm
`max_i sum_j abs(M_ij)`.  The backward-error rule, G0/G1/G2 definitions,
operator identities, cell weights, density rule/tolerance, aggregate formulas,
parameters, controller, and calendar semantics were not changed.

## Frozen operator suite and budget

| Operator | Preserved identity | State shape | Cell weight | New solves |
| --- | --- | --- | ---: | ---: |
| O1 MATLAB post-convergence | `7A2ADC...222C0F` | 5x5x2 | 0.125 | G0, G1, G2 |
| O2 Python post-convergence | `B07A23...A52035` | 5x5x2 | 0.125 | G0, G1, G2 |
| O3 captured 2018 | `A17AA9...AA1B42` | 20x20x2 | `(7/19)*(10/19)` | G1, G2 |

All O3 retrospective anchors, including the manifest
`D0472539...06C490`, A transpose, legacy contaminated matrix, RHS, and raw
legacy solve, re-hashed before execution.  The permanent limitation remains
`CAPTURE_TIME_RAW_HASH_GAP_REMAINS__RETROSPECTIVE_CURRENT_FILE_INTEGRITY_CERTIFIED`.

The fresh ledger records exactly 8 new sparse solves, 0 retries, and 0 warnings:
O1 `3/3`, O2 `3/3`, O3 `2/2`.  O3/G0 was not rerun; it remains the captured
legacy failure baseline.  There were no HJB, household, stationary controller,
GE, MATLAB, R/PLM, shock, IRF, or annual-2018 execution calls.

## Per-candidate diagnostics

Every new system returned a finite raw vector and passed the frozen
`256*eps64` backward-error certificate.  `r` is the zero-based replaced row;
all solver-warning counts are zero.

| Operator/gauge | r | nnz | residual inf / bound | mass error | negative count / weighted mass | `||A'g||inf` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| O1/G0 | 17 | 176 | 2.1684e-18 / 5.6843e-14 | 2.2204e-16 | 5 / 9.9658e-19 | 0.8611673509 |
| O1/G1 | 17 | 225 | 2.2804e-16 / 1.2691e-12 | 0 | 3 / 8.2664e-20 | 0.8611673509 |
| O1/G2 | 29 | 177 | 0 / 5.6843e-14 | 0 | 0 / 0 | 0.05676253353 |
| O2/G0 | 17 | 176 | 3.5237e-18 / 5.6843e-14 | 0 | 5 / 5.4250e-18 | 0.8611673509 |
| O2/G1 | 17 | 225 | 6.9627e-16 / 1.2691e-12 | 0 | 3 / 1.5097e-20 | 0.8611673509 |
| O2/G2 | 29 | 177 | 3.9445e-19 / 5.6843e-14 | 0 | 1 / 1.5635e-17 | 0.05676253353 |
| O3/G1 | 295 | 3901 | 1.0580e-14 / 6.8213e-06 | 2.2204e-16 | 255 / 0.09372780046 | 0.2923442517 |
| O3/G2 | 620 | 3102 | 1.3765e-17 / 6.0814e-08 | 0 | 91 / 7.4039e-17 | 1.4117166e-15 |

The frozen `gesvd` directional witness selected row 29 for both accepted
operators, and row 620 for O3.  Its O3 legacy-row component was
`2.7120552534140134e-16` after max-absolute normalization, while the selected
row component was `1`, consistent with the prior qualitative gauge evidence.
No absolute smallest singular value is claimed as an exact nullspace
certificate.

## Accepted-operator invariance

G1 is machine-level consistent with G0 on both accepted operators:

| Comparison | Max abs density diff | Weighted L1 | L2 | Direct rule |
| --- | ---: | ---: | ---: | --- |
| O1 G1 vs G0 | 8.8818e-16 | 3.8045e-16 | 1.1652e-15 | PASS |
| O2 G1 vs G0 | 8.8818e-16 | 6.5962e-16 | 1.6686e-15 | PASS |

G2 is materially different from G0 on both accepted operators:

| Comparison | Max abs density diff | Weighted L1 | L2 | Direct rule |
| --- | ---: | ---: | ---: | --- |
| O1 G2 vs G0 | 1.6241113447 | 0.7791477352 | 2.4393454216 | FAIL |
| O2 G2 vs G0 | 1.6241113447 | 0.7791477352 | 2.4393454216 | FAIL |

The preserved policy arrays were available for both O1 and O2; no HJB or
household policy was rerun.  Every G1 aggregate comparison (`C`, `L`, `A`,
`B`, and `A+B`) passes the direct machine rule.  G2 fails it materially for
every aggregate.  For O1, G2 minus G0 is respectively `+0.03238975497`,
`-0.007603979407`, `-0.4405947668`, `+0.03987917768`, and
`-0.4007155891`; O2 has the same displayed differences to roundoff.  Thus G2
is not a pure relocation of a unit-row gauge under the frozen contract.

## O3 captured-operator counterfactual

Both permitted O3 counterfactual systems are finite and backward-error
certified, but neither result permits a production conclusion.

- G1 is normalized but has a material negative component: minimum
  `-0.17056674608786826`, 255 negative entries, and weighted negative mass
  `0.09372780046006104`.  It is not economically admissible under the
  task's no-new-threshold boundary.
- G2 has only roundoff-scale negative mass, but G1 and G2 are not density
  equivalent: maximum absolute difference `0.1705667460878683`, weighted L1
  `0.18745560092012198`, L2 `0.25519000578215323`, and the direct density
  rule fails.
- No 2018 aggregate was computed:
  `2018_POLICY_ARRAYS_NOT_CAPTURED__AGGREGATE_COUNTERFACTUAL_NOT_AUTHORIZED`.

Accordingly, a finite sparse solve is not treated as an economically accepted
stationary distribution.  The evidence does not authorize a production G1 or
G2 redesign; Owner/L3 review remains required.

## Evidence and next boundary

The no-overwrite evidence root is:

`D:\ProjectTemp\ch5-mp4c-2018-diagnostic-kfe-gauge-redesign-comparison-fresh-after-sparse-norm-repair-20260904-001`

Its 42 manifest-listed files re-hashed successfully.  Audit-manifest SHA-256:
`E576DBCDCA05BDC91245A8743C389CC36A4C5FEA237191F69EBAB91629A8706E`.

No repository source, test, model, production, or diagnostic file was changed.
Only this report is authorized for publication.  The next action, if any,
requires a new Owner/L3 task; no automatic KFE repair, 2018 rerun, or Results
route follows from this comparison.
