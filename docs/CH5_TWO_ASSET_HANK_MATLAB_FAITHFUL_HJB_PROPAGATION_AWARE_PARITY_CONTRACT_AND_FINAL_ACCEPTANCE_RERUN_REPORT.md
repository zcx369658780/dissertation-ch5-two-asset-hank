# MATLAB-faithful HJB propagation-aware parity contract and final acceptance rerun report

## Terminal classification and acceptance

`MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_AND_FINAL_ACCEPTANCE_RERUN_PASS`

The final pre-authorized acceptance pair and propagation-aware comparator passed. Freeze:

- `MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HJB_OPERATOR_PARITY_ACCEPTED`
- `MATLAB_FAITHFUL_HJB_MATHEMATICAL_SPARSE_SUPPORT_IGNORES_EXACT_STORED_ZEROS`
- `MATLAB_FAITHFUL_HJB_PARITY_SEPARATES_FIXED_POINT_SOLVER_PROPAGATION_FROM_SAME_INPUT_FORMULA_PARITY`

Acceptance is limited to the faithful household HJB/operator layer. It does not accept KFE, stationary distribution, steady-state aggregates, or dynamics.

## Live authority and source identity

- Live start/final pre-publication `origin/main`: `d51049f1f843860c43a7b86c8b82c63abbff4db7`.
- Accepted predecessor diagnosis: `FAITHFUL_HJB_MISMATCH_DIAGNOSIS_REPRESENTATION_AND_FLOATING_PROPAGATION_ONLY`.
- Designated MATLAB hashes matched: HJB `049136B7...EAE`, FOC `772B7B7B...3D`, cost `3504A74B...3C`, labor solver `74FD6AE8...20`.
- Preserved patch: `7EEE8E46B70FAC23C68725B548B6E7FDC957F4ED6B26DD7A50CCD73EA9E62677`.

The rejected faithful candidate was restored only from that patch and reproduced the required bytes:

| Path | SHA-256 |
|---|---|
| `matlab_faithful_policy.py` | `D8A595B93689ED7A9457738620479E3158C734F6878A063FA6B12B0CCFD5F8C2` |
| `matlab_faithful_operator.py` | `0C9F6C1AE3E6428E49086DE900BE55D5038A10144EC061EDDFB9E7249A4A1AAC` |
| `matlab_faithful_hjb.py` | `924831362C904A253D8AD6011FE9BB4C099C6DF4268D0C2AA30AB9139569F1DE` |

Static compilation passed. Corrected/reference `policies.py`, `hjb.py`, `generator.py`, KFE, and steady-state modules were untouched.

## Frozen contract, fixture, and engineering preflight

Artifact root: `D:\ProjectTemp\ch5-hjb-propagation-aware-final-20260830-001`.

- Final comparator: `E049D0B48901799A07D551978BF3C767CD326AB33034CC2C21CD2E2F815EE231`.
- Comparator preflight: `6F1F12F28570B1DD846B047CD028CE150F1BDB4E32F6364421339357C33ADAA2`.
- Freeze manifest: `EBF67BE53238B864BA5AEA459C164C13E9BB3F48AA79C45E4D103BED6C7E21BE`.
- Evaluator/runner: `F6D33348...99FE` / `CE3C320D...2AC`.
- Manifest/order/initialization/tolerances: `784ADA48...F6C7A`, `52EB9943...2926D`, `C6662095...52A9F`, `915B3539...EF72D`.
- Fixture remained 50 states (`5 b x 5 a x 2 z`), `Delta=1000`, `crit=1e-7`, `maxit=100`.

Exactly one no-science preflight returned `PROPAGATION_AWARE_COMPARATOR_CONTRACT_PREFLIGHT_PASS`. It proved:

- all 21 old raw pattern differences were exact stored-zero representation only;
- exact-zero-only canonicalization exposed no nonzero support mismatch;
- same-input continuous and sparse coefficient replay passed the unchanged `128*eps64*max(...)` rule;
- synthetic material formula, nonzero support, and categorical mismatches failed;
- unsupported serializer objects remained fail-closed.

No threshold, `isclose`, epsilon pruning, or nonzero-value removal was used.

## Final scientific execution

| Object | Calls/budget | Result | SHA-256 |
|---|---:|---|---|
| MATLAB HJB | `1/1` | converged, 12 iterations, `9.076792650830612e-10` | `7351351B5D0F7012F03CB6A8CB79A6E31D8FC65FF5D7C26B4A241047F1B5DE94` |
| Python faithful HJB | `1/1` | converged, 12 iterations, `9.07700581365134e-10` | `A33EEA2F7A1698624EC4F773FFE42C2BF88B255F9C231960E8C182ECA2C870AB` |
| Final comparator | `1/1` | PASS | `F7C1A55341C403535081C97195C082CB6B10702BE8A59982E3A7F37EFE5A717C` |

Final ledger SHA-256: `2913F1F321D89A01C17ED7388B7CC4CACFF2FE597EAFA8AA860DC7485CABE163`.

There were no repairs or reruns after any scientific output.

## Complete parity summary

Direct gates all passed:

- grid `a/b/z`, ordering, initialization, convergence boolean, and iteration count exact;
- liquid and transfer labels exact;
- derivative-floor activation exact;
- `V` maximum absolute difference `2.0961010704922955e-13 <= 1e-7`;
- same-input formula replay passed the unchanged machine bound everywhere;
- same-input sparse coefficient replay passed everywhere;
- Bswitch exact;
- mathematical sparse support exact for every iteration and post-convergence operator.

The 21 raw storage differences remained diagnostic: iteration BB `1`, iteration AAH `10`, post AAH `10`; every one was exact `0.0/-0.0` representation. Raw NNZ remained reported as `96/97`, `110/120`, and `80/90` respectively.

Residual raw policy differences were classified only `SOLVER_PROPAGATED_DIAGNOSTIC_DIFFERENCE`:

- labor `6.661338147750939e-14`;
- transfer and `mu_a` `7.16093850883226e-14`;
- `mu_b` `1.1934897514720433e-13`;
- utility `1.0746958878371515e-13`.

Operator raw maxima were likewise solver-propagated diagnostics: BB `4.769518113789672e-13`, AAH `1.432187701766452e-13`, full A `5.098144129078719e-13`, post BB/full A `4.773959005888173e-13`, and post AAH `1.432187701766452e-13`.

Complete material mismatch list: empty. Complete unresolved scientific residual list: empty. Complete source/environment failure list: empty.

## Repository closeout and next gate

Accepted published paths are exactly the three restored faithful source modules and this report. No comparator artifact is published as production source. No KFE, stationary distribution, steady state, D1-D3, tail, transition, IRF, dynamics, calibration, or Results execution occurred.

The only recommended next gate is: **MATLAB-faithful stationary KFE contaminated-row implementation and same post-convergence operator density parity.** This report does not itself authorize that execution.
