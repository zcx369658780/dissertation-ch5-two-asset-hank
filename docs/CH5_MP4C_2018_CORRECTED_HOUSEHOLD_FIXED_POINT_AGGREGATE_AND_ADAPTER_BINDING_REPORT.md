# CH5 MP4C 2018 corrected household fixed-point aggregate and adapter binding

Date: 2026-09-20

Task:

`CH5_MP4C_2018_CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATE_AND_ADAPTER_BINDING_20260920`

## Terminal verdict

`PASS__CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATES_BOUND__OPT_IN_ADAPTER_FIXTURE_READY`

Results eligibility remains `FALSE`.

This task performed deterministic post-processing of the already accepted checkpoint-11 policy and stationary mass. It did not run or update HJB, KFE, policy selection, roots, Q/D2, firms, prices, allocation, an outer loop, MATLAB, GE, annual, shock, IRF, welfare, or Results.

## Repository and authority binding

- Fresh-read `origin/main`: `ee81460b69652038e8807b12c7d3016b4f274d97`.
- Task branch: `codex/ch5-mp4c-2018-corrected-household-fixed-point-aggregate-and-adapter-binding-20260920`.
- Implementation freeze commit used for the one aggregate evaluation: `7ce7182b`.
- Checkpoint policy evidence manifest: `5E67E595B32024213EC5E6517389A7DCA6462A24FB735B06EB2F85D6E1621E41`; 819 entries; 13,089,592 bytes; readback bad count 0.
- Terminal mass evidence manifest: `B7C06E3C369B6A5400DE76252DD70A539EFF1F2E4072C04639A1E93E512F5C1D`; 12 entries; 41,890 bytes; readback bad count 0.

Exact checkpoint binding passed:

| Object | SHA-256 |
|---|---|
| V11 | `A097A3DDA767B979224638A51CEDC53EA635687CCDEFBE190FED0B899606921F` |
| P11 | `89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3` |
| u11 | `2E9A077FFA809F2DECEE385FD9E7F50C03E16750C2A074F990C0F3CBCC212648` |
| Q11 | `33367258F3EADB1482D4A5CB30A64A8574830C993B0E5280C451499CBD6913AD` |
| checkpoint identity | `8093BE714CA83531816B20DFEB2BAB3DCB7AF9B971AD255C3596C1CA2A9E2A3B` |

All 800 sealed cell receipts were loaded in zero-based F order and reproduced the accepted P11 identity. No policy map or selector was called.

Exact stationary mass binding passed:

| Object | SHA-256 |
|---|---|
| stationary mass artifact | `1DD70201EAC5EED0AE768362D99A76736276BFB4D5E6AF0D8DBDB4E9D6FE7D16` |
| p | `E215FAE862DA81AD6DEB603859709EA0CF73B8F6F1897567DF942B186CD65ED7` |
| g | `D02592257722313B81C7A1DB40B799ADED8E8BDB5100A65C469E0997DA22E1CE` |

The bound grid shape is `(20,20,2)` with axis order `(b,a,z)`, F-order flattening, and `b` fastest. `omega=70/361=0.19390581717451524`. The maximum elementwise `|p-omega*g|` is `3.469446951953614e-18`, below the prospective maximum bound `1.7807977314990681e-13`. No second density normalization was applied.

## Source formula mapping

The designated source is:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m`

Its SHA-256 is `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`.

The exact stationary source reductions are:

| Output | Source expression | Source line |
|---|---|---:|
| Ct | `sum(C.*g*dah*db,'all')` | 354 |
| Lt | `sum(zzz.*l.*g*dah*db,'all')` | 347 |
| At (`Aht`) | `sum(aaah.*g*dah*db,'all')` | 351 |
| Bt | `sum(bbb.*g*dah*db,'all')` | 348 |
| total assets | `At + Bt` | contract reduction |
| AtTax (`AhTax`) | `Aht*rah - sum(aaah.*raah.*g*dah*db,'all')` | 365 |

The AtTax operands are closed as follows:

- `rah=results.rah=0.09` is the uniform source illiquid return.
- Source line 81 defines `raah=rah*(1-0.1*(ahmax./ah).^(-9))`.
- The accepted checkpoint receipts bind the same used tapered return as `effective_r_a=0.09*(1-0.1*(a/10)^9)` at every cell.
- `aaah` is the illiquid asset state, and `g*dah*db` is stationary probability mass.

AtTax is therefore an aggregate illiquid-return flow gap: the return flow at uniform `rah` minus the flow at the state-dependent tapered return used by the accepted household object. Its units are relative household asset-flow units per model period. The source contains no absolute currency conversion. This mapping does not choose or modify the unresolved K1A payoff-return law.

No `dz`, productivity probability, trapezoid weight, or endpoint weight appears in these reductions.

## One deterministic aggregate evaluation

Exactly one accepted checkpoint-11 aggregate evaluation was performed.

| Output | Probability-mass form | Density form | Absolute difference | Prospective bound | Status |
|---|---:|---:|---:|---:|---|
| Ct | 11.72504598498222 | 11.725045984982218 | 1.7763568394002505e-15 | 2.0905970123813382e-12 | PASS |
| Lt | 0.6881256647265093 | 0.6881256647265092 | 1.1102230246251565e-16 | 1.7830181775483192e-13 | PASS |
| At | 9.210552290174773 | 9.210552290174773 | 0 | 1.642258215864095e-12 | PASS |
| Bt | 1.6622560718337767 | 1.6622560718337767 | 0 | 4.626283168451263e-13 | PASS |
| total assets | 10.87280836200855 | 10.87280836200855 | 0 | 2.104886532709221e-12 | PASS |
| AtTax | 0.05117497248083413 | 0.05117497248083419 | 6.245004513516506e-17 | 2.868386527320986e-13 | PASS |

The mass forms use `sum_F(field*p)`. The density forms use `omega*sum_F(field*g)`. Effective household labor is `z*l` in both forms.

## Opt-in adapter and fixture

The new module is:

`src/ch5_two_asset_hank/multi_province/corrected_household_adapter.py`

It accepts all arrays, axes, `omega`, uniform `source_r_a`, and cellwise `effective_r_a` explicitly. It exposes the existing `FrozenHouseholdOutputs` contract only through an explicit `frozen_output(...)` call after the deterministic reductions. It has no solver entry point and contains no hidden calibration default.

The accepted fixture contains the aggregate values above, `converged=true`, and checkpoint-11 Bellman residual `5.456747553811425e-11` as the convergence statistic.

The following existing default-route files have the same Git blob at the implementation freeze as on live `origin/main`:

- `household_adapter.py`: `d4f62c869e781f078053fb3507e51b22151e3f10`
- `one_turn.py`: `621c8e2dfaf5f55eda39c9b9bffb22cd52ee451f`
- `stationary_runtime.py`: `8717cfa759948bd1ad3c8cd788f8f4736f250598`

The default/source-faithful production route was not changed.

## Verification

- Focused tests: 33 passed in 1.07 seconds.
- `py_compile`: PASS.
- `git diff --check`: PASS.
- Exact accepted artifact/provenance test: PASS.
- F-order shape/orientation tests: PASS.
- p versus `g*omega` tests: PASS.
- mass-form versus density-form tests: PASS.
- AtTax source contract test: PASS.
- incomplete/mismatched input fail-closed tests: PASS.
- no solver/default-route test: PASS.

## Scientific call ledger

| Call class | Count |
|---|---:|
| accepted checkpoint-11 aggregate post-processing evaluations | 1 |
| HJB solves/updates | 0 |
| KFE/nullspace/SVD/eigen solves | 0 |
| policy maps/selectors/roots | 0 |
| Q/D2 assemblies | 0 |
| firm calls | 0 |
| wage/return calls | 0 |
| capital/labor allocation calls | 0 |
| outer-loop/steady-state/trajectory calls | 0 |
| MATLAB scientific calls | 0 |
| GE/annual/shock/IRF/welfare/Results calls | 0 |
| scientific retries | 0 |

## Evidence seal

Evidence root:

`reports/ch5_mp4c_2018_corrected_household_fixed_point_aggregate_and_adapter_binding_20260920_run001`

- Sealed manifest SHA-256: `0FF6C22FC4C7A8D67119EA477A9BF1E125413F9AE0882B5B064BF1124A7EE3A6`
- Entries: 11
- Bytes: 13,955
- Readback bad count: 0

No CURRENT file was modified. No merge or successor publication was performed.
