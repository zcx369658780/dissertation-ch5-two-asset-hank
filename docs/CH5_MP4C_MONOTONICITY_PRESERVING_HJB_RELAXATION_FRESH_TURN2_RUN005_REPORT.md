# CH5 MP4C monotonicity-preserving HJB relaxation fresh turn-2 run005 report

Date: 2026-09-21

## Terminal

`PASS__MONOTONICITY_PRESERVING_RELAXATION_FRESH_TURN2_RUN005__31_PROVINCE_HJB_KFE_AND_INTEGRATION_PASS__RAW_TURN3_PAYOFF_READY__TURN3_NOT_RUN`

Classification: fresh canonical turn-2 scientific runtime passed for all 31 provinces under the Owner-adopted deterministic halving invariant-domain rule. Exactly one canonical same-S integration was completed and the raw turn-3 payoff was persisted. Turn-3 household work was not run.

## Authority and frozen inputs

- GitHub live-main baseline: `8e9ad015aa01ff1c7a0ca42c6cf2150942aaeca3`.
- Accepted production implementation tree: `5dbd04ad4aaf252381283501d762d633f504ba07`.
- Entering receipt blob: `85df3f0bdcc3b0bb3e7b12f0ba35dbb9abda764d`.
- Entering receipt SHA-256: `E519E468B04D7EDC631F6A931FF367A7EDE5C3D510ED4E0979AB2FC8E13C5E11`.
- Entering raw payoff SHA-256: `D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414`.
- Canonical row count and province order: PASS, 31 rows.
- Pre- and post-execution production source freeze: PASS.
- Production source diff and CURRENT diff: empty.

The initial launcher invocation stopped before repository imports because the repository root was absent from `sys.path`. It created no evidence root and made zero scientific calls. The validator launcher path was corrected before the single fresh scientific execution; no model object was retried.

## Province HJB/KFE results

All provinces used source-native initialization with no warm start. Every row passed the existing Bellman, value-change, terminal KFE, unique-closed-class, restricted-GESVD, normalization, and full-Q checks.

| Index | Province | Terminal checkpoint | B | D | HJB/KFE |
|---:|---|---:|---:|---:|---|
| 0 | 北京 | 12 | 3.243974533440053e-11 | 3.242754242904766e-08 | PASS |
| 1 | 天津 | 12 | 3.4566238760191936e-12 | 3.4545926119733394e-09 | PASS |
| 2 | 河北 | 16 | 9.416079027602109e-14 | 8.939049500611418e-11 | PASS |
| 3 | 山西 | 12 | 3.351943722584849e-12 | 3.355180577813144e-09 | PASS |
| 4 | 内蒙古 | 15 | 1.0887124535230441e-13 | 1.0520828652715863e-10 | PASS |
| 5 | 辽宁 | 12 | 3.0777436155204896e-11 | 2.935989185104404e-08 | PASS |
| 6 | 吉林 | 12 | 2.9299340731370194e-12 | 2.9250606381481248e-09 | PASS |
| 7 | 黑龙江 | 12 | 1.5984297219162613e-11 | 1.598298737803816e-08 | PASS |
| 8 | 上海 | 12 | 2.474268012697678e-11 | 2.4740085313723625e-08 | PASS |
| 9 | 江苏 | 12 | 3.1011443413220263e-12 | 3.1012283852049904e-09 | PASS |
| 10 | 浙江 | 12 | 3.1706998138147924e-12 | 3.165942397131971e-09 | PASS |
| 11 | 安徽 | 12 | 3.653979896434123e-12 | 3.6476417442088405e-09 | PASS |
| 12 | 福建 | 12 | 3.1900593278066935e-12 | 3.176418239547729e-09 | PASS |
| 13 | 江西 | 12 | 3.415087657110405e-12 | 3.4084048916582788e-09 | PASS |
| 14 | 山东 | 13 | 2.577216218213607e-12 | 2.573313118148235e-09 | PASS |
| 15 | 河南 | 14 | 1.3042428248510873e-11 | 1.237706404033645e-08 | PASS |
| 16 | 湖北 | 12 | 3.135575132873214e-12 | 3.13699377585408e-09 | PASS |
| 17 | 湖南 | 12 | 4.283406962457548e-12 | 4.269956832558819e-09 | PASS |
| 18 | 广东 | 12 | 2.379471619740059e-12 | 2.3728039533210676e-09 | PASS |
| 19 | 广西 | 12 | 3.685468596970054e-12 | 3.681562166235608e-09 | PASS |
| 20 | 海南 | 11 | 9.982478732517563e-11 | 9.97679068248658e-08 | PASS |
| 21 | 重庆 | 12 | 3.622421806959153e-12 | 3.6182725704492213e-09 | PASS |
| 22 | 四川 | 12 | 2.6621482795974316e-12 | 2.6603177438744297e-09 | PASS |
| 23 | 贵州 | 12 | 2.64298305463484e-12 | 2.6374464834333367e-09 | PASS |
| 24 | 云南 | 12 | 5.409478420759228e-12 | 5.362142285747495e-09 | PASS |
| 25 | 西藏 | 11 | 1.725623810511223e-11 | 1.72514487140063e-08 | PASS |
| 26 | 陕西 | 12 | 4.091768590619438e-12 | 4.086648575096774e-09 | PASS |
| 27 | 甘肃 | 12 | 2.5851820684152926e-12 | 2.58784016438085e-09 | PASS |
| 28 | 青海 | 12 | 2.076902538838965e-11 | 2.0768947006644112e-08 | PASS |
| 29 | 宁夏 | 12 | 3.1754182616694493e-12 | 3.1713489612172907e-09 | PASS |
| 30 | 新疆 | 12 | 2.9006352875171615e-11 | 2.7826029480593206e-08 | PASS |

The 31 terminal checkpoints sum to 380 direct HJB updates. The maximum terminal B was `9.982478732517563e-11`; the maximum terminal D was `9.97679068248658e-08`. No scientific failure occurred.

## Relaxation ledger and 黑龙江 parity

- Helper invocations: 380.
- Alpha candidates evaluated: 386.
- Accepted with alpha=1 / zero halvings: 374.
- Accepted with alpha=0.5 / one halving: 6.
- Exhaustions or relaxation failures: 0.
- Every accepted state had 760 finite, strictly positive raw b slopes and was not bitwise stagnant.

The six one-halving updates were:

| Province | Checkpoint from | Alpha | Minimum accepted raw b slope | Accepted SHA-256 |
|---|---:|---:|---:|---|
| 黑龙江 | 2 | 0.5 | 0.005032838660371801 | `987A20DE9252104ECFAB59436433F0C73EEB8C513589B8B0FA98DB64018B66BF` |
| 黑龙江 | 3 | 0.5 | 0.005436388281590238 | `DA7059652A20E92C28910B0371C7E49550C6BEAA27F7D5D88C9A9919ED20BC2E` |
| 山东 | 2 | 0.5 | 0.0034100253500942835 | `A8300C190581B4768DCCFA645B663E46C0CAFF1A58736F51E12F3CCF1044E944` |
| 山东 | 3 | 0.5 | 0.0037902978435343966 | `0C26C9C7DDB9B173C4CCD816F05F671D6D2BFF3E2B4A41C18E12646F1CD21720` |
| 青海 | 2 | 0.5 | 0.004001210327224856 | `55403324FE9E2DF47AF409A25396D7E66E43E1115427CC2D8189FB2ECF79C619` |
| 青海 | 3 | 0.5 | 0.0044927544306768204 | `6A353F7D89B087614AD4C462496FFBFC09F51D83603C39A54F6934D816C5A480` |

黑龙江 runtime parity was captured from the normal runtime path with no extra selector or solve call:

- checkpoint0→1: alpha=1, exact full-candidate passthrough;
- checkpoint1→2: alpha=1, exact full-candidate passthrough;
- checkpoint2 full Vhat: `1FA95217C9EEFDAA638F0CD07F00B59B053EB4A59E5670A0CED94852922DBFE7`;
- checkpoint2→3: alpha=0.5;
- relaxed state: `987A20DE9252104ECFAB59436433F0C73EEB8C513589B8B0FA98DB64018B66BF`;
- minimum raw b slope: `0.005032838660371801`;
- first divergence: none;
- the subsequent fresh path converged and its terminal KFE passed.

## Scientific ledger

| Item | Count |
|---|---:|
| Source-native initializations | 31 |
| Labor roots attempted / returned | 24,800 / 24,800 |
| Corrected policy maps / D2-Q assemblies | 411 / 411 |
| Selector evaluations | 328,800 |
| Scalar selector roots | 141,561 |
| Interior-Z roots | 30,782 |
| Direct HJB updates | 380 |
| SCC decompositions | 31 |
| Restricted GESVD / full-space GESVD | 31 / 0 |
| Normalized stationary candidates / full-Q checks | 31 / 31 |
| Aggregate evaluations | 31 |
| Household batch | 1 |
| Labor / K1A / C1 | 1 / 1 / 1 |
| Firm evaluations | 31 |
| Wage / monetary / fiscal | 1 / 1 / 1 |
| Canonical raw payoff | 1 |
| Scientific retries / solver substitutions | 0 / 0 |
| Adaptive controller / MATLAB / GE / Results | 0 / 0 / 0 / 0 |
| Turn3 household / K1B / K2 | 0 / 0 / 0 |

Measured runtime was `2572.4066550999996` seconds.

## One-turn integration

- Status: PASS.
- Orientation: destination by origin.
- `beta_distance=2`, `beta_return=0`.
- Origin private wealth total: `140310000.0`.
- Destination private capital total: `140310000.0`.
- National private-capital residual: `0.0`.
- Labor destination total: `157407315.40224046`.
- C1 GovInv total: `2341682906.900551`.
- Raw turn-2 destination payoff SHA-256: `B3B50A6F0A3876904582DE05354C2DF76A71524FB53E41D4170109B8FCEB8951`.
- Canonical raw turn-3 payoff SHA-256: `5996A20CEE227389A7975703452EA6DAF1A2F817C517FFE43BEF3A53FA4292E2`.
- All seven canonical integration checks passed. The BLAS comparison remained diagnostic only; maximum absolute difference was `2.220446049250313e-16`.

The persisted payoff is a raw turn-3 input candidate only. It does not establish turn-3 household, K1B, K2, GE, Results, or successor authority.

## Evidence and readback

- Evidence root: `reports/ch5_mp4c_monotonicity_preserving_hjb_relaxation_fresh_turn2_run005_20260921/`.
- Sealed manifest SHA-256: `C93BF19DB7C909A50C2753B0EA06FD4735F48A4C41C5A4C9CA6F8817B693B72F`.
- Manifest entries / bytes: `4,752 / 64,191,647`.
- Independent readback: PASS; bad paths: 0; readback scientific calls: 0.
- Focused tests: 3 passed.

No production source or CURRENT file was changed. No successor was published.
