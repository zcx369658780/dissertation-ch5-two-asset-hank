# CH5 MP4C K1A 2018 distance-score mapping and static portfolio diagnostic report

## Outcome

Verdict: **PASS** — the protected workbook maps one-to-one onto the active 31-province axis; `geom!B2:AF32` is complete and symmetric; the frozen national `D/D_max` score, accepted 2018 theta vector, equal-share limit, pure-geographic grid, and all conservation identities reproduce without any scientific/model/runtime call.

This is a zero-science static allocation receipt, not estimated bilateral holdings, a selected coefficient, a steady state, or Results evidence. Results eligibility remains `FALSE`.

## Authority and execution identity

- Task: `CH5_MP4C_K1A_2018_DISTANCE_SCORE_MAPPING_AND_STATIC_PORTFOLIO_DIAGNOSTIC`.
- Fresh live-main baseline: `0090f6d60ba7eeede09a88f2bd5c21887b45bb7b`.
- Worktree: `D:\ProjectTemp\ch5-k1a-distance-mapping-20260911-001`.
- Branch: `codex/ch5-k1a-distance-mapping-20260911`.
- Stage order preserved: `K1A equal-share -> K1A pure-geographic -> K1B lagged-return -> K2`.
- Runtime integration performed: none.

## Protected distance source

- Path: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\中国各省省会地理距离矩阵.xlsx`.
- SHA-256: `26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566`; bytes: `39895`.
- Workbook sheets observed: `geom, igeom, iigeom`; source used: `geom` only.
- Labels: `A2:A32` and `B1:AF1`; numeric range: `B2:AF32`.
- Orientation after label-backed mapping: destination rows x origin columns.
- Units: `UNRESOLVED`; the workbook contains no explicit unit metadata. Values are reported in source units only.
- Integrity: shape 31x31; finite 961/961; missing 0; negative 0; diagonal all exact zero.
- Symmetry residual `max|D-D.T|=0.0`.
- Off-diagonal minimum `110.003361` at `[['北京', '天津']]`.
- `D_max=3639.514265` at `[['黑龙江', '西藏']]`.
- No symmetrization, imputation, or workbook modification occurred.

## Exact source-label mapping

| pos | source | active | rule |
|---|---|---|---|
| 1 | 北京市 | 北京 | DROP_TERMINAL_ADMIN_SUFFIX |
| 2 | 天津市 | 天津 | DROP_TERMINAL_ADMIN_SUFFIX |
| 3 | 河北省 | 河北 | DROP_TERMINAL_ADMIN_SUFFIX |
| 4 | 山西省 | 山西 | DROP_TERMINAL_ADMIN_SUFFIX |
| 5 | 内蒙古 | 内蒙古 | EXACT_SHORT_LABEL |
| 6 | 辽宁省 | 辽宁 | DROP_TERMINAL_ADMIN_SUFFIX |
| 7 | 吉林省 | 吉林 | DROP_TERMINAL_ADMIN_SUFFIX |
| 8 | 黑龙江 | 黑龙江 | EXACT_SHORT_LABEL |
| 9 | 上海市 | 上海 | DROP_TERMINAL_ADMIN_SUFFIX |
| 10 | 江苏省 | 江苏 | DROP_TERMINAL_ADMIN_SUFFIX |
| 11 | 浙江省 | 浙江 | DROP_TERMINAL_ADMIN_SUFFIX |
| 12 | 安徽省 | 安徽 | DROP_TERMINAL_ADMIN_SUFFIX |
| 13 | 福建省 | 福建 | DROP_TERMINAL_ADMIN_SUFFIX |
| 14 | 江西省 | 江西 | DROP_TERMINAL_ADMIN_SUFFIX |
| 15 | 山东省 | 山东 | DROP_TERMINAL_ADMIN_SUFFIX |
| 16 | 河南省 | 河南 | DROP_TERMINAL_ADMIN_SUFFIX |
| 17 | 湖北省 | 湖北 | DROP_TERMINAL_ADMIN_SUFFIX |
| 18 | 湖南省 | 湖南 | DROP_TERMINAL_ADMIN_SUFFIX |
| 19 | 广东省 | 广东 | DROP_TERMINAL_ADMIN_SUFFIX |
| 20 | 广西 | 广西 | EXACT_SHORT_LABEL |
| 21 | 海南省 | 海南 | DROP_TERMINAL_ADMIN_SUFFIX |
| 22 | 重庆市 | 重庆 | DROP_TERMINAL_ADMIN_SUFFIX |
| 23 | 四川省 | 四川 | DROP_TERMINAL_ADMIN_SUFFIX |
| 24 | 贵州省 | 贵州 | DROP_TERMINAL_ADMIN_SUFFIX |
| 25 | 云南省 | 云南 | DROP_TERMINAL_ADMIN_SUFFIX |
| 26 | 西藏 | 西藏 | EXACT_SHORT_LABEL |
| 27 | 陕西省 | 陕西 | DROP_TERMINAL_ADMIN_SUFFIX |
| 28 | 甘肃省 | 甘肃 | DROP_TERMINAL_ADMIN_SUFFIX |
| 29 | 青海省 | 青海 | DROP_TERMINAL_ADMIN_SUFFIX |
| 30 | 宁夏 | 宁夏 | EXACT_SHORT_LABEL |
| 31 | 新疆 | 新疆 | EXACT_SHORT_LABEL |

All 31 labels map uniquely. Workbook short forms `内蒙古`, `广西`, `宁夏`, `新疆`, and `西藏` map exactly to the active short labels; the explicit autonomous-region aliases remain accepted by the script but were not needed by this workbook. Province and municipality terminal `省/市` suffixes are removed transparently.

## Frozen normalized distance matrix

`D_score=D/D_max` uses the single national off-diagonal maximum, never a row/column maximum. The mapped score is 31x31; diagonal is exact zero; off-diagonal range is `[0.030224736871583606, 1.0]`; maximum is 1; symmetry residual is `0.0`. Full raw and normalized long-form receipts are manifest-bound.

## Theta provenance

- Accepted receipt: `D:\ProjectTemp\ch5-k1a-distance-mapping-20260911-001\reports\mp4c_unit_normalized_initialization_probe_20260910\province_initialization_receipt.csv`.
- SHA-256: `5DAD517983CBC436A5FB3E5AD85F1257D957D844994180D15929044A049C7212`; exact 31/31 active order.
- Source formula: `0.3*(K0/N0-min(K0/N0))/(max(K0/N0)-min(K0/N0))` at `validators/multi_province/corrected_2018_single_turn/run.py:246-247`.
- Active fail-closed binding: `src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py:228-289`.
- Formula reproduction max absolute residual: `0.0`; theta range `[0.0, 0.3]`.

Theta is therefore source-authoritative for this static receipt. It is not estimated or changed here.

## Pure-geographic beta-distance diagnostics

These diagnostics use `beta_return=0`, an explicit all-zero completed-iteration score fixture, and the pre-registered distance grid only. No value is selected as a benchmark.

| beta_d | H mean | H/log30 mean | max P mean | exp(H) mean | median top distance |
|---|---|---|---|---|---|
| 0 | 3.4012 | 1 | 0.0333333 | 30 | 1126.58 |
| 0.5 | 3.39748 | 0.998908 | 0.0384378 | 29.8888 | 281.716 |
| 1 | 3.38678 | 0.99576 | 0.0440465 | 29.5707 | 281.716 |
| 2 | 3.34692 | 0.984043 | 0.0568025 | 28.4187 | 281.716 |
| 4 | 3.21002 | 0.943791 | 0.0883009 | 24.8228 | 281.716 |

Entropy mean/min/max, normalized entropy mean/min/max, largest-share mean/min/max, and effective-destination mean/min/max are all retained in `beta_distance_summary.csv`. Entropy weakly decreases with beta for every one of 31 origins: `True`; exceptions: `[]`.

Top-destination tie-breaking is deterministic by active destination index. At beta 0 all 30 eligible destinations tie; positive betas select the nearest destination because this is a pure-distance score.

| beta_d | origin | top destination | share | distance | ties |
|---|---|---|---|---|---|
| 0 | 北京 | 天津 | 0.0333333 | 110.003 | 30 |
| 0 | 上海 | 北京 | 0.0333333 | 1074.36 | 30 |
| 0 | 河南 | 北京 | 0.0333333 | 622.606 | 30 |
| 0 | 广西 | 北京 | 0.0333333 | 2047.84 | 30 |
| 0 | 四川 | 北京 | 0.0333333 | 1518.5 | 30 |
| 0 | 新疆 | 北京 | 0.0333333 | 2405.87 | 30 |
| 0.5 | 北京 | 天津 | 0.0387199 | 110.003 | 1 |
| 0.5 | 上海 | 浙江 | 0.0388633 | 165.834 | 1 |
| 0.5 | 河南 | 山西 | 0.0363738 | 358.921 | 1 |
| 0.5 | 广西 | 海南 | 0.0389289 | 376.282 | 1 |
| 0.5 | 四川 | 重庆 | 0.0382125 | 259.819 | 1 |
| 0.5 | 新疆 | 青海 | 0.0405898 | 1109.74 | 1 |
| 1 | 北京 | 天津 | 0.0446361 | 110.003 | 1 |
| 1 | 上海 | 浙江 | 0.0449222 | 165.834 | 1 |
| 1 | 河南 | 山西 | 0.0394941 | 358.921 | 1 |
| 1 | 广西 | 海南 | 0.0450346 | 376.282 | 1 |
| 1 | 四川 | 重庆 | 0.0435732 | 259.819 | 1 |
| 1 | 新疆 | 青海 | 0.0490933 | 1109.74 | 1 |
| 2 | 北京 | 天津 | 0.0580365 | 110.003 | 1 |
| 2 | 上海 | 浙江 | 0.0586291 | 165.834 | 1 |
| 2 | 河南 | 山西 | 0.0459312 | 358.921 | 1 |
| 2 | 广西 | 海南 | 0.0586933 | 376.282 | 1 |
| 2 | 四川 | 重庆 | 0.0558123 | 259.819 | 1 |
| 2 | 新疆 | 青海 | 0.0702982 | 1109.74 | 1 |
| 4 | 北京 | 天津 | 0.0906358 | 110.003 | 1 |
| 4 | 上海 | 浙江 | 0.09211 | 165.834 | 1 |
| 4 | 河南 | 山西 | 0.0593376 | 358.921 | 1 |
| 4 | 广西 | 海南 | 0.0908614 | 376.282 | 1 |
| 4 | 四川 | 重庆 | 0.0867395 | 259.819 | 1 |
| 4 | 新疆 | 青海 | 0.131557 | 1109.74 | 1 |

Representative origins were fixed before inspecting shares by active indices `[0,8,15,19,22,30]`, spanning north/east/central/south/southwest/far-west. Their top-3 table at beta 0/1/4 is:

| beta_d | origin | rank | destination | share | distance |
|---|---|---|---|---|---|
| 0 | 北京 | 1 | 天津 | 0.0333333 | 110.003 |
| 0 | 北京 | 2 | 河北 | 0.0333333 | 224.419 |
| 0 | 北京 | 3 | 山西 | 0.0333333 | 406.036 |
| 0 | 上海 | 1 | 北京 | 0.0333333 | 1074.36 |
| 0 | 上海 | 2 | 天津 | 0.0333333 | 966.501 |
| 0 | 上海 | 3 | 河北 | 0.0333333 | 940.694 |
| 0 | 河南 | 1 | 北京 | 0.0333333 | 622.606 |
| 0 | 河南 | 2 | 天津 | 0.0333333 | 578.908 |
| 0 | 河南 | 3 | 河北 | 0.0333333 | 398.552 |
| 0 | 广西 | 1 | 北京 | 0.0333333 | 2047.84 |
| 0 | 广西 | 2 | 天津 | 0.0333333 | 1998.75 |
| 0 | 广西 | 3 | 河北 | 0.0333333 | 1823.75 |
| 0 | 四川 | 1 | 北京 | 0.0333333 | 1518.5 |
| 0 | 四川 | 2 | 天津 | 0.0333333 | 1520.64 |
| 0 | 四川 | 3 | 河北 | 0.0333333 | 1328.41 |
| 0 | 新疆 | 1 | 北京 | 0.0333333 | 2405.87 |
| 0 | 新疆 | 2 | 天津 | 0.0333333 | 2499.39 |
| 0 | 新疆 | 3 | 河北 | 0.0333333 | 2409.25 |
| 1 | 北京 | 1 | 天津 | 0.0446361 | 110.003 |
| 1 | 北京 | 2 | 河北 | 0.0432547 | 224.419 |
| 1 | 北京 | 3 | 山东 | 0.0416277 | 363.954 |
| 1 | 上海 | 1 | 浙江 | 0.0449222 | 165.834 |
| 1 | 上海 | 2 | 江苏 | 0.0445955 | 192.398 |
| 1 | 上海 | 3 | 安徽 | 0.0419921 | 411.324 |
| 1 | 河南 | 1 | 山西 | 0.0394941 | 358.921 |
| 1 | 河南 | 2 | 山东 | 0.0393793 | 369.52 |
| 1 | 河南 | 3 | 河北 | 0.0390664 | 398.552 |
| 1 | 广西 | 1 | 海南 | 0.0450346 | 376.282 |
| 1 | 广西 | 2 | 贵州 | 0.0441734 | 446.557 |
| 1 | 广西 | 3 | 广东 | 0.0434776 | 504.34 |
| 1 | 四川 | 1 | 重庆 | 0.0435732 | 259.819 |
| 1 | 四川 | 2 | 贵州 | 0.0405211 | 524.116 |
| 1 | 四川 | 3 | 甘肃 | 0.0397118 | 597.547 |
| 1 | 新疆 | 1 | 青海 | 0.0490933 | 1109.74 |
| 1 | 新疆 | 2 | 西藏 | 0.0441876 | 1492.91 |
| 1 | 新疆 | 3 | 甘肃 | 0.0427594 | 1612.49 |
| 4 | 北京 | 1 | 天津 | 0.0906358 | 110.003 |
| 4 | 北京 | 2 | 河北 | 0.079926 | 224.419 |
| 4 | 北京 | 3 | 山东 | 0.0685625 | 363.954 |
| 4 | 上海 | 1 | 浙江 | 0.09211 | 165.834 |
| 4 | 上海 | 2 | 江苏 | 0.0894597 | 192.398 |
| 4 | 上海 | 3 | 安徽 | 0.0703286 | 411.324 |
| 4 | 河南 | 1 | 山西 | 0.0593376 | 358.921 |
| 4 | 河南 | 2 | 山东 | 0.0586504 | 369.52 |
| 4 | 河南 | 3 | 河北 | 0.0568085 | 398.552 |
| 4 | 广西 | 1 | 海南 | 0.0908614 | 376.282 |
| 4 | 广西 | 2 | 贵州 | 0.0841079 | 446.557 |
| 4 | 广西 | 3 | 广东 | 0.0789326 | 504.34 |
| 4 | 四川 | 1 | 重庆 | 0.0867395 | 259.819 |
| 4 | 四川 | 2 | 贵州 | 0.0648731 | 524.116 |
| 4 | 四川 | 3 | 甘肃 | 0.0598433 | 597.547 |
| 4 | 新疆 | 1 | 青海 | 0.131557 | 1109.74 |
| 4 | 新疆 | 2 | 西藏 | 0.0863427 | 1492.91 |
| 4 | 新疆 | 3 | 甘肃 | 0.0757096 | 1612.49 |

## Equal-share and conservation checks

Unit origin wealth `W_i=1` is a mathematical fixture only, not a claim about 2018 capital quantities. The accepted pure `capital_network.py` utility produced the full matrices.

| check | max residual | PASS |
|---|---|---|
| foreign_column_sum_residual | 4.44089e-16 | True |
| full_share_column_sum_residual | 1.33227e-15 | True |
| home_share_residual | 0 | True |
| origin_wealth_residual | 1.33227e-15 | True |
| national_capital_residual | 7.10543e-15 | True |
| equal_share_residual_beta_0 | 0 | True |
| no_destination_theta_double_weighting_residual | 0 | True |

The beta-zero foreign conditional share is exactly `1/(31-1)` within tolerance. Full off-diagonal shares equal `theta_i*P[j,i]`; no destination `theta_j` weighting appears.

## K1B lagged-return coefficient interpretation

Future K1B uses `z_ra0=(ra0-mean)/sd` across destinations from completed iteration n raw, unclipped `ra0`, and may use it only for allocation iteration n+1. Same-turn feedback is prohibited. The z-score is an attractiveness signal and must never be passed as household payoff `rah`. No `ra0` was generated or loaded in this task.

| beta_r | Delta z | exp(beta_r*Delta z) |
|---|---|---|
| 0 | 1 | 1 |
| 0 | 2 | 1 |
| 0.25 | 1 | 1.28403 |
| 0.25 | 2 | 1.64872 |
| 0.5 | 1 | 1.64872 |
| 0.5 | 2 | 2.71828 |
| 1 | 1 | 2.71828 |
| 1 | 2 | 7.38906 |
| 2 | 1 | 7.38906 |
| 2 | 2 | 54.5982 |

These are algebraic odds factors only, not identification or a coefficient choice.

## Call ledger and boundaries

| call class | count |
|---|---:|
| MATLAB / HJB / KFE / household / firm / migration / outer loop / trajectory / steady state | 0 |
| GE / annual / shock / IRF / Results | 0 |
| protected workbook reads | 1 per script reproduction |
| accepted pure capital-network algebra evaluations | 5 |

No production scientific/runtime source changed. The protected workbook was read only. `capital_network.py` was not modified.

## Verification and evidence closure

- Reproduction script: `scripts/ch5_mp4c_k1a_distance_mapping.py`.
- Evidence manifest: `docs/evidence/ch5_mp4c_k1a_distance_mapping/manifest.json` with 11 hashed entries (script, report, and nine non-manifest receipts); every path, byte count, and SHA-256 is read back after generation.
- A second complete reproduction produced the identical manifest SHA-256.
- Accepted capital-network focused suite: `29/29` passed (`tests/test_mp4c_k1_bilateral_capital_network.py`).
- Tracked changes remain limited to this task's script, report, and evidence directory.

## Remaining Owner decisions before runtime integration

- Select the final scientific `beta_distance` after reviewing this static receipt.
- Before K1B, select final `beta_return`.
- Freeze the household payoff-return concept; standardized attractiveness scores are not payoff returns.
- Any economic-distance/market-size extension, smoothing, or K2 endogenous-theta form remains a separate future decision.

After those decisions, a new exact task is still required for any K1 runtime integration. The first integration must retain source-faithful labor and separately revalidate C1 residual public assets and the independent KFE blocker.
