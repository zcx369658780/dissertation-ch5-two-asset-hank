# CH5 MP4C K1A raw-ra0 corrected-household fixed-price three-point safety panel

Date: 2026-09-20

Task:

`CH5_MP4C_K1A_RAW_RA0_CORRECTED_HOUSEHOLD_FIXED_PRICE_THREE_POINT_SAFETY_PANEL_20260920`

## Terminal verdict

`PASS__RAW_RA0_FIXED_PRICE_THREE_POINT_CORRECTED_HOUSEHOLD_ONE_STEP_SAFETY_PANEL__LONGER_RUNTIME_NOT_YET_AUTHORIZED`

All preregistered LOW, MEDIAN and HIGH raw-payoff points completed one corrected-household policy map, one D2/Q assembly and one direct implicit update at fixed checkpoint-11 non-payoff inputs.

This PASS is a one-step fixed-price safety result. It is not an HJB convergence classification, KFE result, 31-province batch, outer trajectory, K1B result, GE result or Results authority. Results eligibility remains `FALSE`.

## Repository and implementation freeze

- Fresh live `origin/main`: `ed17a6e30f079fe7f73dcb2214b5e1a98095c75c`.
- Task branch: `codex/ch5-mp4c-k1a-raw-ra0-corrected-household-fixed-price-three-point-safety-panel-20260920`.
- Scientific implementation freeze: `824a63a1fbd9c68a94671ff7deafe24e1c796f68`.
- Focused pre-science tests: `15 passed`.
- Pre/post scientific code hashes: exact match.

The driver reuses the accepted selector, D1/D2/D3, KKT, boundary, upwind and switching implementations. No default source-faithful multi-province runtime file was changed.

## Panel source derivation

Accepted CSV:

`docs/evidence/ch5_mp4c_k1a_payoff_return_reaudit/static_no_feedback_payoff_counterfactual.csv`

SHA-256:

`5496DA47A1F06E46088D4FA80B3803654FB6C47134EE0D32F2DF79028C0FE9F9`

The CSV contains 1,550 observations: 775 `A_EQUAL_SHARE` and 775 `B_GEOGRAPHIC_BETA2`. Before any scientific call, the Path-B observations were sorted by exact decimal `static_raw_S_transpose_ra0`. The 0-based median position is 387.

| Panel point | Exact statistic | Accepted source row | Province index | Exact raw portfolio payoff |
|---|---|---|---:|---:|
| LOW | minimum | Qinghai, turn 5 | 28 | `0.11048158315647279` |
| MEDIAN | median of 775 | Hunan, turn 12 | 17 | `0.26259451366691877` |
| HIGH | maximum | Beijing, turn 4 | 0 | `1.037811238406538` |

All row identities and decimal strings match the preregistration. These are Path-B portfolio-weighted `S'ra0` household payoffs, not destination firm returns.

No clipping, annualization, rescaling, smoothing, risk adjustment or payoff z-score transformation was applied.

## Common checkpoint-11 binding

The accepted 819-entry evidence manifest was fully read back before panel science. Exact binding passed for:

| Object | SHA-256 |
|---|---|
| V11 | `A097A3DDA767B979224638A51CEDC53EA635687CCDEFBE190FED0B899606921F` |
| P11 | `89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3` |
| u11 | `2E9A077FFA809F2DECEE385FD9E7F50C03E16750C2A074F990C0F3CBCC212648` |
| Q11 | `33367258F3EADB1482D4A5CB30A64A8574830C993B0E5280C451499CBD6913AD` |
| checkpoint identity | `8093BE714CA83531816B20DFEB2BAB3DCB7AF9B971AD255C3596C1CA2A9E2A3B` |

The common seed is exact V11 with shape `(20,20,2)`, F order and `b` fastest. All non-payoff scalars equal the accepted checkpoint-11 values. The only changed scalar is `r_a`. Every point uses:

`effective_r_a(a)=r_a*(1-0.1*(a/10)^9)`.

## One-step results

| Point | B_seed | D_step | Backward error | Policy SHA-256 | Normalized identity changes |
|---|---:|---:|---:|---|---:|
| LOW | `0.0012787655754729066` | `0.019623779080780945` | `2.0486705345909371e-16` | `7F263A6B42822365E8141A7BC12E095B2F496FD53D20C082430C8D0652AF8457` | 51 |
| MEDIAN | `0.010402976627898047` | `0.13237145029256903` | `1.8258654602313007e-16` | `AF849F45C69525E626D1C5FC19E5569D0BDD5A3E34CC3FB19E8C309387C70426` | 80 |
| HIGH | `0.05667966349584988` | `0.18050857122147956` | `1.9352806692350628e-16` | `40D5B52F3BBF995F78662682136FAE807908DDBD2E10DC791DA24D33EBF235C6` | 82 |

Every solve used only `scipy.sparse.linalg.spsolve`, `Delta=1000`, and had no warning. All backward errors are below `1e-12`. `D_step` is `||vec_F(V_plus-V11)||inf`. No point received a second update.

`B_seed` and `D_step` are diagnostics only. The frozen HJB convergence law was not applied because V11 was not generated under these new raw payoff values.

## Policy and switching diagnostics

### Active constraints

| Point | none | lower_b | upper_b | upper_a | combined |
|---|---:|---:|---:|---:|---:|
| LOW | 735 | 20 | 19 | 25 | `upper_a+upper_b: 1` |
| MEDIAN | 722 | 19 | 19 | 39 | `upper_a+upper_b: 1` |
| HIGH | 722 | 19 | 19 | 39 | `lower_b+upper_a: 1` |

Transfer branches are identical at all points: negative 298, positive 323, zero-kink 179.

### Switching

| Point | Interior-a candidates / admissible / selected | Liquid-Z selected | Joint selected |
|---|---:|---:|---:|
| LOW | `28 / 14 / 14` | 0 | 0 |
| MEDIAN | `0 / 0 / 0` | 1, flat index 381 | 0 |
| HIGH | `0 / 0 / 0` | 1, flat index 798 | 0 |

LOW used one interior-a switching root. MEDIAN and HIGH used no interior-a root. No point invoked a joint-switching root.

### Maximum absolute continuous-field change from accepted P11

| Point | c | l | d | g_b | g_a | q_b | q_a | utility |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| LOW | 0.09655749927846813 | 0.0017370369233106198 | 0.18433424840825507 | 0.13264076381166856 | 0.18433424840825507 | 8.088860049669869e-05 | 0.0003384790719180245 | 0.0006636103679246025 |
| MEDIAN | 0.6637671992358971 | 0.011616863502100228 | 1.553350623002269 | 0.9050829439775209 | 1.534594355604841 | 0.0005791591619892962 | 0.0021849785286873263 | 0.004354659095152147 |
| HIGH | 1.03356651865632 | 0.031239089456974956 | 8.530301145658843 | 1.359152986970351 | 8.427300183159257 | 0.002745161636537038 | 0.019587547700713026 | 0.01730806794857921 |

No monotonicity, fitted trend or threshold is inferred from these three observations.

## D2 and Q diagnostics

All unchanged D2 structural and conservation checks passed.

| Point | Q nnz | max abs Q@1 | Prospective bound | Minimum off-diagonal | Q artifact SHA-256 |
|---|---:|---:|---:|---:|---|
| LOW | 3120 | `1.7763568394002505e-15` | `1.8696973642908742e-14` | `2.7404782515125115e-06` | `E3F2E43A722CD329D3E96A8D9784AB469F37C971899B0D585A0EE86BA0D3796B` |
| MEDIAN | 3120 | `1.4988010832439613e-15` | `2.2322584376824518e-14` | `2.7404782515125115e-06` | `CF94B223C01B973BBEA552AA33E5618196CAA5EA4E06394E8B071BE51976864F` |
| HIGH | 3120 | `4.718447854656915e-15` | `4.517060714895383e-14` | `2.7404782515125115e-06` | `B40339B116B3FE84363D2E04C76B4B208497468DF1A5F21759A543ADA50AA366` |

Minimum off-diagonals are nonnegative, diagonal construction error is exactly zero, boundary faces are feasible, and coordinate-action checks pass at every point.

## Scientific call ledger

| Call class | Count |
|---|---:|
| accepted checkpoint-11 manifest/V/P/u/Q loads | `1 / 1 / 1 / 1 / 1` |
| accepted CSV loads | 1 |
| corrected policy maps | 3 |
| selector evaluations | 2400 |
| scalar roots | 813 |
| liquid-Z roots | 44 |
| interior-a switching roots | 1 |
| joint-switching roots | 0 |
| D2/Q assemblies | 3 |
| direct HJB solves / updates | `3 / 3` |
| complete one-step panel evaluations | 3 |
| scientific retries / solver substitutions | `0 / 0` |
| KFE/SVD/eigen/nullspace/stationary mass | 0 |
| household aggregate evaluations | 0 |
| capital network | 0 |
| firm/wage/return | 0 |
| outer/steady-state/trajectory | 0 |
| MATLAB scientific calls | 0 |
| K1B feedback | 0 |
| GE/annual/shock/IRF/welfare/Results | 0 |
| clipping/rescaling/smoothing/risk adjustment/z-score transformations | 0 |

Scientific execution wall time was `19.414125500014052` seconds.

## Serialization-normalized comparison repair

The initial in-memory comparison treated new tuple-valued `active_constraints` and accepted JSON list-valued `active_constraints` as different at every cell. After science ended, both sides were reloaded from their persisted JSON receipts and the comparison was repeated without any selector, Q or solve call.

The corrected identity-change counts are `51 / 80 / 82`. Policy canonical SHA-256 values did not change. The repair consumed zero scientific calls and zero retries and is recorded in `post_execution_serialization_normalization_repair.json`.

## Evidence

Evidence root:

`reports/ch5_mp4c_k1a_raw_ra0_corrected_household_fixed_price_three_point_safety_panel_20260920_run001`

- Final sealed manifest SHA-256: `6D0A210F3979B0E0499FA8CC4C21803EB59077D655286D7119E0F85741BB5ED4`
- Entries: 2,444
- Bytes: 38,471,991
- Final independent external readback bad count: 0
- Persisted independent readback receipt: PASS

No CURRENT file was modified. No main merge or successor publication was performed.
