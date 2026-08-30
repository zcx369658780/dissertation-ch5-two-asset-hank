# Chapter 5 MATLAB-faithful end-to-end stationary distribution and household aggregate parity report

## Terminal verdict

`MATLAB_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_AND_HOUSEHOLD_AGGREGATE_PARITY_BLOCKED`

The authorized scientific objects were produced within budget, but the single final comparator call failed while serializing its JSON result:

`TypeError: Object of type bool is not JSON serializable`

The value was a NumPy boolean scalar. The comparator did not persist `comparison.json`. Under the live task's no-repair/no-rerun rule, the comparator was not modified or invoked again. Therefore neither PASS nor MATERIAL MISMATCH is asserted, and the two requested acceptance freezes are not issued.

Successor artifact root: `D:\ProjectTemp\ch5-end-to-end-stationary-aggregate-20260830-001`.

## Live authority and boundaries

- Execution start, `HEAD`, and fresh-fetched `origin/main`: `00e256272f3efc4d12e6c05ed6e9fa5d56ee1c2b`.
- Worktree was clean before execution.
- Primary authority retained: `MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`.
- Accepted HJB/KFE authorities were reused; no MATLAB or Python HJB and no MATLAB KFE was rerun.
- No general-equilibrium steady-state loop, `r*`/`w*` solution, D1-D3, asset-tail, transition, IRF, dynamics, calibration extension, or Results execution occurred.

## Mandatory MATLAB source audit

Designated source:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m`

Verified SHA-256:

`049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`

The exact post-KFE block is unambiguous:

- density: contaminated-row `g_stacked`, normalized by `g_stacked'*ones(M,1)*db*dah`, then reshaped to `g(:,:,1:2)` in MATLAB/Fortran `(b,a,z)` order;
- `C^ss`: `Ct = sum(C.*g*dah*db,'all')`, published as `results.Ct`;
- `L^ss`: `Lt = sum(zzz.*l.*g*dah*db,'all')`, published as `results.Lt`;
- `A^ss`: `Aht = sum(aaah.*g*dah*db,'all')`, published as `results.At`;
- `B^ss`: `Bt = sum(bbb.*g*dah*db,'all')`, published as `results.Bt`;
- weight: exactly `dah*db = 0.5*0.25 = 0.125`;
- no `dz`, productivity probability, trapezoid, or endpoint weight appears;
- `C` and `l` are the post-convergence policy arrays; `aaah` and `bbb` are the illiquid and liquid grid arrays;
- `Lt` is productivity-weighted effective household labor `zzz.*l`, not raw hours and not a separately defined production/equilibrium labor object;
- total assets are not a separate source field in this block; the requested value is the identity `A^ss+B^ss`.

Source diagnostics also include `Bt_pos`, `Bt_neg`, `Bdotres`, `Income`, `St`, `AhTax`, `Ut`, `Borrow`, `Borrowint`, `CHI_H`, and `UC`; none was substituted for the requested four aggregates.

## Frozen inputs and arithmetic contract

- MATLAB HJB artifact: `7351351B5D0F7012F03CB6A8CB79A6E31D8FC65FF5D7C26B4A241047F1B5DE94`.
- Python HJB artifact: `A33EEA2F7A1698624EC4F773FFE42C2BF88B255F9C231960E8C182ECA2C870AB`.
- MATLAB accepted KFE artifact: `A53B304C134A909D99F1911983F8CB273AC295AEFF1A7DBBC9CFE621401F44E8`.
- Python same-operator KFE artifact: `DF97F38C48CB46B5BC871DCB036B0AD3336DB17BC897A4921B8DEEA148AA98A7`.
- Common MATLAB operator artifact: `7A2ADC63CE7A4BB5184036E4CFC07EC082185C90C5B818C572ED05756D222C0F`.
- Faithful KFE source: `27DA91779788E76C9F92697247FFF520D460CB9CCAFAC2DE39CDCFF7440A3E88`.
- Lossless Python `A_P` serialization: `B07A2311FEA22D01ED4A26F59D8C79EEA5E82DFEC7AADBBD52C8D2BCE8A52035`.

Before scientific execution, the 50-state finite-sum bound was frozen with `gamma_n=n*eps64/(1-n*eps64)`. Aggregate reduction used the two-product plus 49-addition bound; decomposition closure used `8*gamma_50` times the declared magnitude scale; density bridge closure used `8*eps64` elementwise. The existing same-input rule `128*eps64*max(1,abs(x),abs(y))` was retained.

## Persisted scientific outputs before comparator failure

Python own-operator KFE ran exactly once and persisted SHA-256:

`FBFE4DF7BFD8FDFA848268F440E4CC6ADCF669EDF9C91067D87FCF3E4F324BE8`

Its persisted certificate records:

- contaminated-system residual infinity norm: `3.5236570605778894e-18`;
- backward-error bound: `5.684341886080802e-14`;
- normalized density integral: `1.0`;
- normalization bound: `2.842170943040401e-14`;
- density minimum/maximum: `-3.4394387830411846e-17` / `2.4697052857465276`;
- negative count: `5` (roundoff-scale values).

The MATLAB aggregate evaluator ran once and persisted `DB42C6338AB079D46DF95F2BA12BAE3326B624D3FBD5E430273966D88073F2F9`. The Python aggregate evaluator ran once and persisted `212C424BEE00C5EBF9FA994FF3077F9F4786B9AA78DEDD1BBD2C36301431D6FA`.

The comparator persisted the density bridge NPZ before JSON serialization failed: `7CE32408C6E91062F88F389160BC0EFC8561F4BEB93B8EB5CB2FFD437C0C8939`. Read-only extraction gives:

- same-operator solver leg max abs: `4.440892098500626e-16`;
- own-operator leg max abs: `2.724487302430134e-13`;
- total end-to-end max abs: `2.723377079405509e-13`;
- bridge residual max abs: `3.851859888774472e-34`;
- frozen bridge-bound max: `1.7763568394002505e-15`.

These persisted diagnostics are evidence, not a substitute for the failed qualified comparator verdict.

## Household aggregate values

The following values are direct read-back of the two successfully persisted aggregate evaluator outputs. Because the sole comparator failed, every classification is `NOT_QUALIFIED_COMPARATOR_PERSISTENCE_BLOCKED`.

| Stationary household quantity | MATLAB | Python | Abs. diff | Rel. diff | Classification |
|---|---:|---:|---:|---:|---|
| `C^ss` | 1.1296890749137012 | 1.1296890749136979 | 3.3306690738754696e-15 | 2.9483059966123022e-15 | `NOT_QUALIFIED_COMPARATOR_PERSISTENCE_BLOCKED` |
| `L^ss` | 0.7341069339182125 | 0.7341069339182127 | 2.220446049250313e-16 | 3.024690200648199e-16 | `NOT_QUALIFIED_COMPARATOR_PERSISTENCE_BLOCKED` |
| `A^ss` | 0.4405947668272667 | 0.44059476682729026 | 2.353672812205332e-14 | 5.3420353336333504e-14 | `NOT_QUALIFIED_COMPARATOR_PERSISTENCE_BLOCKED` |
| `B^ss` | 0.4601208223181074 | 0.4601208223181049 | 2.4980018054066022e-15 | 5.4290127380490355e-15 | `NOT_QUALIFIED_COMPARATOR_PERSISTENCE_BLOCKED` |
| `A^ss + B^ss` | 0.9007155891453742 | 0.9007155891453952 | 2.098321516541546e-14 | 2.3296160761827683e-14 | `NOT_QUALIFIED_COMPARATOR_PERSISTENCE_BLOCKED` |

The required decomposition was computed in memory by the consumed comparator but was not durably serialized. It cannot be reconstructed by a replacement comparator under this task.

| Quantity | Policy contribution | Density contribution | Decomposition residual |
|---|---:|---:|---:|
| `C^ss` | not persisted | not persisted | not persisted |
| `L^ss` | not persisted | not persisted | not persisted |
| `A^ss` | source/common-grid contribution fixed at `0`, but qualified row not persisted | not persisted | not persisted |
| `B^ss` | source/common-grid contribution fixed at `0`, but qualified row not persisted | not persisted | not persisted |

These are frozen-price stationary household aggregates only. They are not a general-equilibrium steady-state acceptance.

## Call ledger and closeout

| Scientific call | Consumed |
|---|---:|
| MATLAB HJB | 0 |
| Python HJB | 0 |
| MATLAB KFE | 0 |
| Python own-operator KFE | 1 |
| MATLAB aggregate evaluator | 1 |
| Python aggregate evaluator | 1 |
| comparator | 1 (JSON persistence failure) |

No source or test module was changed. This is report-only publication. Because the terminal is BLOCKED, no next scientific gate is recommended or authorized.
