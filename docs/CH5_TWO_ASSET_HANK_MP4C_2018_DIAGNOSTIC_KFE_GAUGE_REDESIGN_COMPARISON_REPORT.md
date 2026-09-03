# MP4C 2018 diagnostic KFE gauge redesign comparison

## Terminal

`MP4C_2018_DIAGNOSTIC_KFE_GAUGE_REDESIGN_COMPARISON_BLOCKED__NO_PRODUCTION_CHANGE_NO_2018_RERUN`

The authorized comparison stopped fail-closed during the first predeclared
O1/G0 post-solve diagnostic.  No qualified density, invariance, aggregate, G1,
G2, or 2018 counterfactual conclusion is asserted.

## Authority and boundaries

- Live authority: `8acc3ad5e4cae03b09835277902403f10f7efdf8`, direct child of
  `20f39fbcda4b92b45d7b61ec0e323aa49c5b3d94`.
- Start state after fresh fetch and fast-forward: `HEAD == origin/main ==
  8acc3ad5e4cae03b09835277902403f10f7efdf8`, ahead/behind `0/0`, clean
  tracked worktree.
- Scope was Owner-authorized diagnostic-only KFE gauge comparison on frozen
  stored operators.  Production, model, diagnostic, test, HJB, KFE, controller,
  and calendar/input sources remain unchanged.

No 2018 annual execution, GE outer loop, HJB, household solve, stationary
controller, MATLAB, R/PLM, shock, or IRF ran.  There was no retry.

## Frozen contract and identity gates

The pre-solve contract was recovered from the accepted MATLAB-faithful KFE and
end-to-end aggregate authorities:

- G0: legacy row `floor(0.37*n)-1`, unit row, RHS `0.007`, then normalize by
  `sum(raw)*db*da`.
- G1: same legacy row replaced by `cell_weight*ones(n)^T`, RHS `1.0`, with no
  post-normalization.
- G2: `scipy.linalg.svd(..., lapack_driver='gesvd')` directional witness only;
  smallest max-absolute component row, unit row, RHS `0.007`, then G0
  normalization.
- Backward-error certificate:
  `residual_inf <= 256*eps64*max(1, ||M||_inf*||x||_inf, ||rhs||_inf)`.
- Direct density/same-input rule:
  `128*eps64*max(1,abs(x),abs(y))`.
- Aggregate source formulas use only `db*da`: `sum(C*g*da*db)`,
  `sum(z*l*g*da*db)`, `sum(a*g*da*db)`, and `sum(b*g*da*db)`, with the
  accepted 50-state `gamma_n` reduction/decomposition arithmetic contract.

All required frozen source hashes passed, including O1 MATLAB post-convergence
operator `7A2ADC63CE7A4BB5184036E4CFC07EC082185C90C5B818C572ED05756D222C0F`,
O2 Python own operator `B07A2311FEA22D01ED4A26F59D8C79EEA5E82DFEC7AADBBD52C8D2BCE8A52035`,
and the O3 retrospective manifest/A/A-transpose/B/RHS/raw-solve anchors.

The intended O3 cell weight was frozen from the captured 20 by 20 by 2 grid as
`(7/19)*(10/19) = 0.19390581717451522`, with no z or endpoint weight.  The
permanent caveat remains:

`CAPTURE_TIME_RAW_HASH_GAP_REMAINS__RETROSPECTIVE_CURRENT_FILE_INTEGRITY_CERTIFIED`

## Failure and budget accounting

The helper began the first allowed sparse direct solve, O1/G0.  After that
single `spsolve` invocation returned to the helper, the helper attempted
`numpy.linalg.norm(M, numpy.inf)` on the sparse contaminated system matrix while
forming the backward-error diagnostic.  NumPy raised:

`ValueError: Improper number of dimensions to norm.`

This is a helper-layer sparse-matrix norm API failure.  The solve result was not
durably diagnosed, so its finiteness, density, residual, mass, and certificate
status are deliberately not inferred.  The strict no-retry rule means O1/G0
cannot be replaced by a repaired invocation; without that baseline, neither the
O1 pure-gauge comparison nor the complete 8-solve experiment can be qualified.

| Budget item | Count |
| --- | ---: |
| Maximum new sparse solves | 8 |
| Started | 1 (O1/G0) |
| Completed with persisted diagnostics | 0 |
| Automatic retries | 0 |
| Further predeclared pairs launched | 0 |

Accordingly, O1 G1/G2, O2 G0/G1/G2, and O3 G1/G2 were not run.  The captured
O3 legacy G0 failure remains reused evidence only; it was not rerun.

## External evidence

The no-overwrite external root is:

`D:\ProjectTemp\ch5-mp4c-2018-diagnostic-kfe-gauge-redesign-comparison-20260904-001`

It contains the completed identity gate, frozen contract, gauge definitions,
operator-suite identity, the exact helper, and a terminal failure receipt.  Its
audit manifest is SHA-256:

`EC9C4BF15E4512054A1426DF5EF8065646925B475911F53534A45B87C4FA85B5`

All files listed in that manifest re-hashed successfully.  The failure receipt
records zero production changes and zero prohibited scientific actions.

## Decision boundary

The requested scientific questions remain unanswered:

1. G1/G2 invariance on accepted operators was not measured.
2. No qualified O3 G1 or G2 density exists.
3. No negative-mass, backward-error, or aggregate comparison exists.
4. No preference between G1 and G2 is supported.

No production repair, gauge redesign, 2018 rerun, aggregate counterfactual, or
Results claim is authorized from this blocked task.  A new live Owner/L3 task
would be required to decide whether and how to recover the consumed O1/G0
diagnostic budget.
