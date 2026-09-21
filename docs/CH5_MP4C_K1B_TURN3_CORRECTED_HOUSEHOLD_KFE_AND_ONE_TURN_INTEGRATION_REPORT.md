# CH5 MP4C K1B turn3 corrected household/KFE and one-turn integration report

Date: 2026-09-21

Task: `CH5_MP4C_K1B_TURN3_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_20260921`

## Terminal

`PASS__K1B_TURN3_31_PROVINCE_HJB_KFE_AND_ONE_INTEGRATION__TURN4_K1B_INPUT_READY__TURN4_NOT_RUN`

This bounded run completed the first real K1B-active turn3. All 31 corrected household HJB/KFE blocks passed in canonical order. The run then performed exactly one source-faithful-labor + frozen-K1B-capital + C1 + firm integration and prepared the lagged K1B turn4 input candidate. Turn4 household HJB/KFE was not run.

Results eligibility remains `FALSE`. No successor is published by this task.

## Authority and frozen inputs

- Live-main baseline: `33e2177823fbdfd717c9a53b00c455047f91d86f`.
- Turn3 input candidate blob: `b33bfdf2fa17fb110684b83757b871fff3e884c7`.
- Turn3 input candidate SHA-256: `76238863C98929E30B895FA5BE200CC1185A6ABFD0E11BC34AB3082A2705CE27`.
- Entering classification: `TURN3_K1B_INPUT_CANDIDATE_ONLY__HOUSEHOLD_NOT_RUN`.
- Entering household `rah` SHA-256: `CEEFE34C16BA0DFDE9FA0C5590DFBB89084475BD88A8496EC18FEEBA7CB674D2`.
- Frozen turn3 plan blob: `f6d917c1a2bb391d048d36ac1a49cc07516440fa`.
- Frozen turn3 plan SHA-256: `06D25DA78B2DAFD090A9E77EC544FB9CEFA42EE0F9B925EE0544169A2DD2858D`.
- Frozen turn3 `S_K1B` SHA-256: `4C3AB67F1982AEB3B707D07C53BB98C5BA54C835234DFEDE45A96B09BC5E3AB6`.
- Accepted production-source binding and pre/post code freeze: PASS.
- Production source changes: 0.

## Household HJB/KFE result

All 31 provinces used source-native initialization, fixed `Delta=1000`, the accepted corrected selector/D1-D3 laws, one `spsolve` per direct update, the adopted monotonicity-preserving relaxation, and the unique-closed-class KFE authority.

| # | Province | Terminal checkpoint | B | D |
|---:|---|---:|---:|---:|
| 0 | 北京 | 12 | 6.794251272701501e-11 | 6.750061443128175e-08 |
| 1 | 天津 | 12 | 4.168498879408844e-12 | 4.158448252411517e-09 |
| 2 | 河北 | 13 | 2.596825532386049e-12 | 2.593995462873977e-09 |
| 3 | 山西 | 12 | 4.370961925737049e-12 | 4.358382543756534e-09 |
| 4 | 内蒙古 | 13 | 5.0158904807418025e-12 | 4.934979314086263e-09 |
| 5 | 辽宁 | 12 | 1.448970110562442e-11 | 1.4019641891849233e-08 |
| 6 | 吉林 | 13 | 1.5996787228189646e-12 | 1.5914385365078942e-09 |
| 7 | 黑龙江 | 13 | 1.7246759576039494e-12 | 1.7191128520721577e-09 |
| 8 | 上海 | 11 | 4.1008127449337906e-11 | 4.097495498456283e-08 |
| 9 | 江苏 | 12 | 3.2726182874753817e-12 | 3.26455973365114e-09 |
| 10 | 浙江 | 12 | 3.684524907399123e-12 | 3.6793099678078534e-09 |
| 11 | 安徽 | 12 | 4.718253565627606e-12 | 4.71499905785322e-09 |
| 12 | 福建 | 12 | 3.950034743738229e-12 | 3.944505611030991e-09 |
| 13 | 江西 | 12 | 4.203332126806458e-12 | 4.195458203071212e-09 |
| 14 | 山东 | 13 | 2.507147267571952e-12 | 2.5037287798568286e-09 |
| 15 | 河南 | 15 | 1.9771684289793257e-13 | 1.9802826045633992e-10 |
| 16 | 湖北 | 12 | 3.2472774469383126e-12 | 3.235240741972234e-09 |
| 17 | 湖南 | 12 | 3.6282921112018585e-12 | 3.6250900059542346e-09 |
| 18 | 广东 | 12 | 3.0672409057075356e-12 | 3.0603841683074506e-09 |
| 19 | 广西 | 12 | 1.4025877681511645e-11 | 1.4024522876354695e-08 |
| 20 | 海南 | 12 | 4.012373766570931e-12 | 4.004764964093965e-09 |
| 21 | 重庆 | 12 | 5.319911178247594e-12 | 5.3160291724196895e-09 |
| 22 | 四川 | 12 | 2.941480392593121e-12 | 2.9319031646934945e-09 |
| 23 | 贵州 | 12 | 3.0455776789395372e-12 | 3.039013929395651e-09 |
| 24 | 云南 | 12 | 9.863498906526047e-13 | 9.848906135090374e-10 |
| 25 | 西藏 | 11 | 2.0828574975872982e-11 | 2.082517047696797e-08 |
| 26 | 陕西 | 12 | 3.538502824085299e-12 | 3.5367502260186257e-09 |
| 27 | 甘肃 | 12 | 2.4809876375542217e-12 | 2.4798010311855023e-09 |
| 28 | 青海 | 12 | 1.0800096927887637e-11 | 1.0796285643266401e-08 |
| 29 | 宁夏 | 12 | 1.76353376346583e-12 | 1.7598820178932328e-09 |
| 30 | 新疆 | 11 | 1.5369802652820397e-11 | 1.5256619523285053e-08 |

The maximum terminal Bellman metric was `6.794251272701501e-11 <= 1e-8`; the maximum terminal value-change metric was `6.750061443128175e-08 <= 1e-7`.

## Relaxation ledger

- Helper invocations: 377.
- Alpha candidates evaluated: 383.
- Accepted with `alpha=1`: 371.
- Accepted with `alpha=0.5`: 6.
- Other accepted alpha values: 0.
- Exhaustion/failure: none.
- Smallest accepted raw b slope across province minima: `7.672127670556508e-05` (河南).

The six one-halving updates were 河北 checkpoints 2->3 and 3->4, 山东 checkpoints 2->3 and 3->4, 广西 checkpoint 2->3, and 青海 checkpoint 2->3. Each full solve occurred once; alpha search did not trigger another solve.

## Scientific-call ledger

- Source-native initializations: 31.
- Scalar labor roots attempted/returned: 24,800 / 24,800.
- Corrected policy maps / D2-Q assemblies: 408 / 408.
- Selector evaluations: 326,400.
- Direct HJB updates: 377.
- SCC decompositions: 31.
- Restricted dense GESVD: 31.
- Normalized stationary candidates: 31.
- Full-Q stationarity checks: 31.
- Full-space 800x800 GESVD: 0.
- Corrected aggregate evaluations: 31.
- Household batch constructions: 1.
- Scientific retries / solver substitutions: 0 / 0.
- Adaptive controller, clipping, artificial diffusion, alternate continuation: 0.
- MATLAB, K2, GE/annual/shock/IRF/welfare/Results: 0.
- Wall time: `2578.8459096999723` seconds.

## Exactly one turn3 integration

- Source-faithful labor reconstructions: 1.
- Frozen turn3 K1B quantity allocations: 1.
- C1 residual-GovInv constructions: 1.
- Firm evaluations: 31.
- Composite wage / monetary / fiscal batches: 1 / 1 / 1.
- Completed-turn3 raw-ra0 vectors: 1.
- Frozen `S_K1B` SHA-256 revalidated as `4C3AB67F1982AEB3B707D07C53BB98C5BA54C835234DFEDE45A96B09BC5E3AB6`.
- Origin private wealth total: `140310000.0`.
- Destination private capital total: `140310000.0`.
- National private capital residual: `0.0`.
- Home-retained identity: exact PASS.
- No same-turn share recomputation: PASS.
- C1 `GovInv` total: `2341682906.900551`; exact residual rule and nonnegativity PASS.
- Completed-turn3 raw `ra0` SHA-256: `1C587932F4E8471209663D2262DB1BB308857EEEA1198D7868E4721CFB031E8F`.
- Raw `ra0` range: `[0.25385118409465646, 1.0844648167925854]`.
- Historical used-return vector SHA-256: `939825C2D0F908414CE574221B758D5E2889E58CB2796FB1A2719BBBFDA088FC`; all 31 entries differ from raw `ra0`, recorded only as a diagnostic.

## Deterministic turn4 K1B preparation

- Population z-score mean input: `0.5185879356888632`.
- Population standard deviation: `0.1907497808664968`.
- Z-score SHA-256: `67F06784094DAE4F6691AD79EA8107830FEF076CB1A2E28A96A34919E5122741`.
- Foreign conditional share SHA-256: `7A86442D2AF7876D726101561EFA029ACBDF81E0C3566514703399D284F5E1D3`.
- Frozen turn4 portfolio-share SHA-256: `5E8FB74E547CBF776A70E908F1ECA7F8FD80DD1A7637100BBD159B7F0803028B`.
- Turn4 household `rah` SHA-256: `7DE65A71206F52AB3D2DA98D6D01C43A8A69D8B2C423BE49A15D5D287C434BE9`.
- Classification: `TURN4_K1B_INPUT_CANDIDATE_ONLY__TURN4_HOUSEHOLD_NOT_RUN`.
- Turn4 household calls: 0.

The completed-turn3 raw `ra0` entered only the lagged population z-score and raw-payoff construction for turn4. The already frozen turn3 `S_K1B` was not changed by same-turn firm returns.

## Evidence seal

- Evidence root: `reports/ch5_mp4c_k1b_turn3_corrected_household_kfe_and_one_turn_integration_20260921_run001/`.
- Sealed manifest entries: 4,724.
- Sealed bytes: 63,722,204.
- Manifest SHA-256: `776F348F4BBF36587E2B484A10A00F96F6D01689322207A52A3770B93CDC03D9`.
- Independent readback: PASS, bad paths 0, readback scientific calls 0.

## Boundary

This PASS prepares a Reviewer-inspectable turn4 K1B input candidate. It does not authorize turn4 household HJB/KFE, K2, an outer fixed-point claim, GE, Results, CURRENT modification, main merge, or successor publication.
