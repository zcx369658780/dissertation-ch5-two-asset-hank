# MATLAB-faithful end-to-end aggregate comparator NumPy-bool serialization correction and closeout

## Terminal and acceptance

`MATLAB_FAITHFUL_END_TO_END_AGGREGATE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_PASS`

Freeze:

- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_PARITY_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HOUSEHOLD_AGGREGATE_PARITY_ACCEPTED`

The single replacement comparator durably persisted PASS using only predecessor scientific artifacts. No HJB, KFE, or aggregate evaluator was rerun. These remain frozen-price stationary household results, not a general-equilibrium steady-state acceptance.

Successor artifact root: `D:\ProjectTemp\ch5-end-to-end-aggregate-comparator-closeout-20260830-001`.

## Authority and continuity

- Fresh-fetched live task authority and execution start: `dc883e7aaf9033634b371225d31a5baf57fabeb2`.
- It is the direct child of predecessor report commit `ac6aee8769f948b52fe4fa9488af6d7d3ed66f8c`.
- Primary authority retained: `MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`.
- No unaccepted `matlab_faithful_stationary.py` or stationary-aggregate test path existed on live main.

Reused identities matched exactly:

- Python own-KFE: `FBFE4DF7BFD8FDFA848268F440E4CC6ADCF669EDF9C91067D87FCF3E4F324BE8`;
- MATLAB aggregate: `DB42C6338AB079D46DF95F2BA12BAE3326B624D3FBD5E430273966D88073F2F9`;
- Python aggregate: `212C424BEE00C5EBF9FA994FF3077F9F4786B9AA78DEDD1BBD2C36301431D6FA`;
- predecessor density bridge: `7CE32408C6E91062F88F389160BC0EFC8561F4BEB93B8EB5CB2FFD437C0C8939`;
- Python `A_P`: `B07A2311FEA22D01ED4A26F59D8C79EEA5E82DFEC7AADBBD52C8D2BCE8A52035`.

## Persistence-only audit and correction

Frozen classification:

`END_TO_END_AGGREGATE_COMPARATOR_NUMPY_SCALAR_JSON_SERIALIZATION_ONLY`

The predecessor raised `TypeError: Object of type bool is not JSON serializable` at `compare.py:118`, the final `json.dumps` call. Static payload tracing established:

- exact failing type: `numpy.bool_`;
- first sorted failing path: `decomposition.A.pass`;
- NumPy payload scalar types: `numpy.bool_` and `numpy.float64`;
- no ndarray/non-scalar object reached the payload;
- density bridge, table, decompositions, mismatch lists, and terminal decision had all completed before persistence;
- no formula, field, bound, mismatch rule, or PASS/MATERIAL logic required correction.

The new comparator changes only the JSON boundary: `np.generic` is converted through `.item()`; all other unsupported objects raise `TypeError`. Every changed line is classified `END_TO_END_AGGREGATE_COMPARATOR_JSON_SERIALIZATION_TYPE_NORMALIZATION_ONLY`.

- predecessor comparator: `27C9A2E945402BE1334155C249A25A5AA98C054D77FA82F9913552C94BF7F7BE`;
- corrected comparator: `D70C9521C7C28A395752832FD97DED8279C46C2B723C0808C05F3CEB16F399CA`;
- exact diff: `5B20A9F066096568DF9A63C9E2FFC19E6E28AAB5B9C34B8DB9C4C9BDA9ED77F2`;
- audit: `75639426DD2E989B56073D6053892D66AB795ED825920D962108530F093E672C`.

Exactly one no-science serializer preflight returned `END_TO_END_AGGREGATE_COMPARATOR_SERIALIZER_PREFLIGHT_PASS`: native bool/int/float were unchanged, NumPy bool/float became equal native scalars, and ndarray remained fail-closed.

## Persisted replacement comparison

Comparison SHA-256: `FB1B4A88CAEFB2EB915EBAD5E89B34219BF850E8527954E97BF146BCCEEE5421`.

Python own-KFE persisted certificate remains PASS:

- residual infinity norm: `3.5236570605778894e-18`;
- frozen backward-error bound: `5.684341886080802e-14`;
- normalization: `1.0`;
- normalization bound: `2.842170943040401e-14`.

Density bridge:

`g_P_own - g_M = (g_P_own - g_P_common) + (g_P_common - g_M)`

- same-operator solver leg max abs: `4.440892098500626e-16`;
- own-operator leg max abs: `2.724487302430134e-13`;
- total end-to-end max abs: `2.723377079405509e-13`;
- bridge residual max abs: `3.851859888774472e-34`;
- frozen bridge bound: `1.7763568394002505e-15`;
- bridge: PASS.

The exact MATLAB source formulas remain `sum(C.*g*dah*db)`, `sum(zzz.*l.*g*dah*db)`, `sum(aaah.*g*dah*db)`, and `sum(bbb.*g*dah*db)`, with weight `0.125`, Fortran `(b,a,z)` ordering, and no additional state weight.

| Stationary household quantity | MATLAB | Python | Abs. diff | Rel. diff | Classification |
|---|---:|---:|---:|---:|---|
| `C^ss` | 1.1296890749137012 | 1.1296890749136979 | 3.3306690738754696e-15 | 2.9483059966123022e-15 | `SOURCE_IDENTICAL_WITHIN_BINARY64_ARITHMETIC` |
| `L^ss` | 0.7341069339182125 | 0.7341069339182127 | 2.220446049250313e-16 | 3.024690200648199e-16 | `SOURCE_IDENTICAL_WITHIN_BINARY64_ARITHMETIC` |
| `A^ss` | 0.4405947668272667 | 0.44059476682729026 | 2.353672812205332e-14 | 5.3420353336333504e-14 | `SOURCE_IDENTICAL_WITHIN_BINARY64_ARITHMETIC` |
| `B^ss` | 0.4601208223181074 | 0.4601208223181049 | 2.4980018054066022e-15 | 5.4290127380490355e-15 | `SOURCE_IDENTICAL_WITHIN_BINARY64_ARITHMETIC` |
| `A^ss+B^ss` | 0.9007155891453742 | 0.9007155891453952 | 2.098321516541546e-14 | 2.3296160761827683e-14 | `SOURCE_IDENTICAL_WITHIN_BINARY64_ARITHMETIC` |

The predecessor `gamma_n` finite-sum bounds and `128*eps64*max(1,abs(x),abs(y))` same-input rule were unchanged. No broad aggregate tolerance was added.

| Quantity | Policy/state contribution | Density contribution | Decomposition residual | Frozen bound | Result |
|---|---:|---:|---:|---:|---|
| `C^ss` | -4.2034199964677666e-16 | -3.0375046125418977e-15 | 1.2717753831320464e-16 | 1.0033654573093586e-13 | PASS |
| `L^ss` | 8.592798661389912e-16 | -7.162474978913584e-16 | 7.90122366773986e-17 | 8.881784197001351e-14 | PASS |
| `A^ss` | 0 | 2.35127943590957e-14 | 2.393376295761751e-17 | 8.881784197001351e-14 | PASS |
| `B^ss` | 0 | -2.5233494964387694e-15 | 2.5347691032167233e-17 | 8.881784197001351e-14 | PASS |
| `A^ss+B^ss` (sum of persisted A/B decomposition) | 0 | 2.098944486265693e-14 | 4.928145398978474e-17 | each A/B component passes its frozen bound | PASS |

MATLAB and Python `A+B` identity residuals are both exactly `0`; their frozen identity bound is `2.842170943040401e-14`.

- material mismatch list: empty;
- unresolved scientific residual list: empty;
- source/environment failure list: empty.

## Execution ledger and boundary

| Call | This successor |
|---|---:|
| MATLAB HJB | 0 |
| Python HJB | 0 |
| MATLAB KFE | 0 |
| Python KFE | 0 |
| MATLAB aggregate evaluator | 0 |
| Python aggregate evaluator | 0 |
| no-science serializer preflight | 1 |
| replacement comparator | 1 |

No production or test path changed. No GE steady-state loop, `r*`, `w*`, D1-D3, asset-tail, transition, IRF, dynamics, calibration, or Results ran.

The only recommended next gate is the smallest source-backed **MATLAB-faithful general-equilibrium steady-state closure** gate at the accepted stationary household objects. This report does not itself authorize that execution or any dynamics work.
