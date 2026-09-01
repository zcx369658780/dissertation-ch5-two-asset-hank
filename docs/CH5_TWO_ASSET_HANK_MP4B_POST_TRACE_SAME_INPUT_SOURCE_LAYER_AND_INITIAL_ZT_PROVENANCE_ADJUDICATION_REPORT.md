# MP4B post-trace same-input source-layer and initial-Zt provenance adjudication

## Terminal verdict

`MP4B_POST_TRACE_SAME_INPUT_SOURCE_LAYER_AND_INITIAL_ZT_PROVENANCE_ADJUDICATION_PASS`

Strongest supported classification:

`MP4B_TURN1_ZT_SOURCE_BINDING_REPRESENTATION_DIVERGENCE_LOCALIZED`

The accepted markers remain preserved, without weakening the MATLAB-to-MATLAB baseline result:

- `MP4B_L3_DELEGATED_INSTRUMENTED_MATLAB_BASELINE_ADMISSIBLE`
- `MP4B_UPSTREAM_NUMERICAL_TRAJECTORY_DIVERGENCE_LOCALIZED__FAULT_NOT_YET_ATTRIBUTED`

No same-input source-contract violation is established for either implementation.

## Live continuity and scope

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Live task authority / execution-start `HEAD` / `origin/main`:
  `b3a41cebb69e2f82d7b479231dc6fecadbea1fe3`.
- Required direct parent: `b7be2233576a2342385db8ef0ba8a9c3359f1245`; verified.
- Execution-start branch: `codex/ch5-adjustment-boundary-redesign`.
- Fresh fetch, clean worktree, `HEAD == origin/main`, and ahead/behind `0/0`: PASS.

This was read-only, zero-model-execution work over durable artifacts. It did not
run MATLAB, `checkcode`, Python stationary/HJB/KFE/household/MP2/MP3, a
comparator, replay, another year/batch, shocks/AR1, transition/dynamics/IRF,
R5, or Results.

## Immutable identity verification

All required durable inputs matched their frozen SHA-256 values:

| Evidence | SHA-256 |
| --- | --- |
| instrumented MATLAB trace | `6C4AEC5992A59C1C8D7859DEF082E5711864789CAE009FD1E5CC2B78B3F6A520` |
| instrumented MATLAB final state | `D2F4B225AC362A6805AAD1CD065AFA87DA32551833E5FC867BA3A37C9FD0B8F0` |
| MATLAB baseline-admissibility result | `68C9F396C57D385E72E6A46D94A53F4196F7E9BFBC84A6EAF66AB1FF64A0866B` |
| chronology alignment V5 | `A64172CC32EC7295297CED6DFE27B52CE51B5EAD64AD82453C60EBE0152965C3` |
| Python run manifest | `030A4241D4FB7A8CFA5370811FC4502028A61E46521F9329D7768B45278F6774` |
| Python terminal summary | `CE943372D0F313A33E1D326747683F47CC3065B502A8B2646B492FF3B64A8F01` |
| canonical corrected-2009 input | `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48` |

The frozen repository source, source-postloop adapter, validation driver,
source-semantics map, final-state field map, comparator helper, and all seven
protected MATLAB source identities were re-hashed successfully. The documented
`C:\MatlabProgram` Junction still targets `D:\MatlabProgram`.

## Objective A — turn-1 Tianjin initial Zt

The protected source chain is exact:

1. `load_GDPdata.m:135-137` evaluates and persists
   `GDP(2020) * CAP(2020)^(-alpha) * POP(2020)^(alpha-1)` to `IND_Zt`.
2. `mpHANK_equilibrium_2000.m:25` binds
   `data_MAT.IND_Zt{st_ind}(1,i) * param.Ztratio` to initial `Zt`.
3. `multi_prov_HANK_12sts.m:82` fixes `param.Ztratio = 1`.
4. `mp4b_python_empirical.py:109-111` directly assigns the canonical persisted
   `initialized_zt[i]` to both `Zt` and `Zt_1`; it does not recompute this value.

For Tianjin (one-based province 2), the immutable cache binds the next binary64
value while the canonical JSON equals a standard-library reproduction of the
protected source expression:

| Boundary | Decimal | binary64 hex |
| --- | ---: | --- |
| raw/cached GDP(2020) | 14083700.0 | `0x1.adcce80000000p+23` |
| raw/cached CAP(2020) | 753172150637.6503 | `0x1.5eb91df2db4cfp+39` |
| raw/cached POP(2020) | 138700.0 | `0x1.0ee6000000000p+17` |
| cached alpha | 0.539451671764441 | `0x1.143302700068fp-1` |
| source-order scalar reproduction / canonical Python | 0.023633692874437028 | `0x1.8336e47eaebd6p-6` |
| copied MATLAB cache `IND_Zt` / MATLAB trace entry | 0.02363369287443703 | `0x1.8336e47eaebd7p-6` |

The difference is exactly one ULP,
`3.469446951953614e-18`. Because multiplication by the exact binary64 `1`
preserves the cached value, the difference already exists before the first turn
at the cache/canonical binding boundary. It is neither a same-input arithmetic
violation nor, by itself, a scientific defect.

## Objective B — turn-8 reset-category divergence

The protected controller condition is `maxNKgap < 0.1 && steady_state == 1`,
then strict `Yt/Yt0 - 1 > 0.01 || Yt/Yt0 - 1 < -0.01` (`HANK_mp_1eq.m:47-55`).
The Python static source implements the same strict criterion. The full decimal
and binary64 matrices are in the external artifacts; decisive predicate facts
are below.

| Coordinate | MATLAB discrepancy | Python discrepancy | MATLAB action | Python action | Same predicate inputs? | Verdict |
| --- | ---: | ---: | --- | --- | --- | --- |
| turn 8, Shanghai (9) | -0.00990424052123362 (`-0x1.448aca90b17c0p-7`) | computed from distinct persisted `Yt`,`Yt0`: -0.01446374266232775 (`-0x1.d9f2aadb31d00p-7`) | no Zt reset | Zt reset | no | upstream-input-driven |
| turn 8, Qinghai (29) | -0.010830717205571272 (`-0x1.62e6a41856f00p-7`) | computed from distinct persisted `Yt`,`Yt0`: -0.007589404703638669 (`-0x1.f16114ff8c700p-8`) | Zt reset | no Zt reset | no | upstream-input-driven |

Both locations are adaptation-eligible. At both locations, each side's recorded
strict predicate and resulting action agree with that side's own inputs.
`Zt`, `Kt`, `Lt`, `Yt`, and several upstream firm/state values are already
non-bitwise-equal. Therefore:

`MP4B_TURN8_RESET_DIVERGENCE_UPSTREAM_INPUT_DRIVEN`

Neither `MP4B_TURN8_RESET_SAME_INPUT_MATLAB_LEGACY_DEFECT_CONFIRMED` nor
`MP4B_TURN8_RESET_SAME_INPUT_PYTHON_IMPLEMENTATION_DEFECT_CONFIRMED` is
supported.

## Objective C — turn-1 to turn-8 propagation

- Earliest bitwise difference: turn 1, Tianjin entry `Zt` (the one-ULP cache
  binding divergence above).
- Earliest recorded measurable continuous difference: turn 1, Beijing household
  `Ct`: MATLAB `11.400731651946101` (`0x1.6cd2cb2f7293fp+3`) versus Python
  `11.400731651949162` (`0x1.6cd2cb2f72ffap+3`). This task has no exact
  protected household arithmetic contract sufficient to attribute that output.
- Earliest later mapped household-input difference: turn 2, Beijing wage:
  MATLAB `17.740518629558398` (`0x1.1bd92a1000835p+4`) versus Python
  `17.729107634252784` (`0x1.1baa6cc446130p+4`).
- First categorical divergence: turn 8, MATLAB-only Qinghai reset and
  Python-only Shanghai reset.

The persisted layers were inspected in source order: entry, household input and
output, migration, capital/`rah`, firm input/pre-clip/output, composite wage,
policy/fiscal, controller, and next-turn carries. A causal path from the tiny
turn-1 Tianjin `Zt` difference to either turn-8 Shanghai/Qinghai branch is not
demonstrated by these artifacts. Chronological precedence is not causation.

## Objective D — turn-154 Zhejiang

The low-return threshold is `ramin + 0.02 = 0.04`
(`0x1.47ae147ae147bp-5`) on both sides, but the inputs are not the same:

| Field | MATLAB | Python |
| --- | ---: | ---: |
| `ra` | 0.03997259518672249 (`0x1.47749ba205e63p-5`) | 0.04005859575487796 (`0x1.4828f6d61bbb7p-5`) |
| `ra - 0.04` | -0.000027404813277509543 | 0.000058595754877960315 |
| `GovInv` before | 179942687.09319925 | 179942687.09319925 |
| `Zt` before | 0.6019495765273021 | 0.5991030825999832 |
| adaptation eligible | true | true |
| low-return action | MATLAB `0.9` action | Python `NONE` |

The immediately upstream `Kt`, `Lt`, `Yt`, `KNratio`, `rah`, wage, and firm
output records also differ. The source predicate therefore receives non-identical
inputs: MATLAB is below the strict threshold and Python is above it. The
controller action remains downstream, not a root-cause attribution.

## External audit package

The final no-overwrite package is
`D:\ProjectTemp\ch5-mp4b-post-trace-same-input-source-layer-adjudication-20260901-002`.
It contains the required seven artifacts and the standard-library-only renderer:

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `turn1_tianjin_zt_provenance.json` | 3607 | `49E9F54F38201DF67D75A1B71702CB6F8875C557DB112821BE91784508A69D4D` |
| `turn8_reset_same_input_matrix.json` | 9017 | `ACB2874F87A519ECA2712BE6A124C9497A71864F7461893C8638C2CE7656A6B3` |
| `turn1_to_turn8_propagation_chain.json` | 2262 | `D0F09BADED546A6AACAA647DF26CC7A0D6314C9F3FDF12D82148EF7715ED3ED1` |
| `turn154_zhejiang_same_input_matrix.json` | 7148 | `EB7922B163F468D053BCD447D84B14B4A59337FCACCF9351998CD11E3AB8F03C` |
| `source_expression_map.md` | 801 | `5723D9C223F3D874687A35E54F323F724DF6A633BAA3FABDC607D15DE5731E25` |
| `binary64_audit.json` | 21388 | `C29AE12444EA4FF021F207F220AF3C9E112FE3788DCA3031EBECA985E6FF8A01` |
| `diagnostic_manifest.json` | 3086 | `2112948AC8A7AB3BD5B64C34634722F53DAFF29796F743E93B559CE7783EF3DC` |

The preceding read-only root `...-001` is preserved without overwriting as the
raw HDF5/cache direct-readout package; it contains no model output or source
mutation. Its cache and trace readouts are respectively
`2903EFE3EDD6AFCE5BBA62830048F8A00EBA1A9D0F59F5B028E9B371286B99AC` and
`637410063F605D4B09D0759A19559360069FE2F7C5D851623DAE0D148592CE5B`.

`python -m py_compile` passed for the external standard-library scripts.

## Boundary and closeout audit

- Zero-model ledger: every forbidden scientific/model category is `0`.
- No protected MATLAB source, canonical data, scientific Python module,
  adapter, comparator, field map, task, prior report, or project rule changed.
- No new stationary run root was created; no model module was imported.
- Changed repository path: this report only.
- `git diff --check` on the staged report: PASS.

Exactly one recommended next gate:

`L3_READ_ONLY_REVIEW_OF_THE_SOURCE_BINDING_DIVERGENCE_AND_THE_UNATTRIBUTED_EARLY_HOUSEHOLD_OUTPUT_DIFFERENCE`

This recommendation does not authorize repair, stationary rerun, shocks, IRF,
annual batch, R5, or Results work.
