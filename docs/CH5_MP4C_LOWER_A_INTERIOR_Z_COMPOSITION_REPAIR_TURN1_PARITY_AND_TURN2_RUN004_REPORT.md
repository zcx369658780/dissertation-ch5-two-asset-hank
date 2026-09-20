# CH5 MP4C lower-a / interior-Z composition repair、turn-1 parity 与 turn-2 run004 报告

日期：2026-09-21

## Terminal

`FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`

首个新科学失败发生于黑龙江（province index 7）checkpoint 3、flat 63、
`v003_f0063_b003_a003_z000`：正常 selector 返回
`NO_ADMISSIBLE_POLICY`。runner 在该对象处停止；没有 rescue、tune、retry、
solver substitution、integration 或 turn3。

## 代码修复

唯一 production source 改动为
`src/ch5_two_asset_hank/corrected_diagnostic/selector.py`。

修复仅覆盖 active lower-a + zero-kink + interior liquid b：当普通 endpoint
因 lower-a kink/multiplier intersection 为空而在 controls 前返回时，使用同一
`d=0` control 算术和既有 `_fp_bound` 获得该 endpoint 的 raw liquid drift 与
prospective arithmetic bound。只有原有 backward-positive / forward-negative
strict crossing 成立时，才调用未修改的 `_one_interior_z_root`；root candidate
仍通过既有 `_candidate(..., q_b_override=root, ...)` 重算 lower-a interval、
`q_a`、multiplier、KKT、direction、finite 与 Hamiltonian 检查。

普通 endpoint rejection object 未被改成 admissible；upper-a、active liquid
faces、positive/negative transfer、interior-a 与 joint switching 未扩展。

## Engineering gates

- focused tests：22 passed；
- `py_compile`：PASS；
- `git diff --check`：PASS；
- accepted F0005 forensic manifest：
  `039E74760D6FFAC8DD3177723B6F7EE9FFC9CFE2BD6C192EF4EB34160DAD026A`；
- accepted run003 manifest：
  `E1DBBDF7E86B8F11A4DDB646A1CBD53259E5182D6EFE6A0D2679314874B8A403`；
- accepted turn1 run004 manifest：
  `CF70E7D6A62A35F461D1A75B28F8F502B2CBDD2D94ED5D9DDFA099D821CC5EC6`；
- entering-state Git blob：`85df3f0bdcc3b0bb3e7b12f0ba35dbb9abda764d`；
- entering raw payoff SHA-256：
  `D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414`；
- cost、boundary/generator、nonlinear HJB/KFE 与 integration source：unchanged；
- pre/post execution code freeze：PASS。

## 河北 F0005 focused 与 runtime receipt

正常 selector 与 turn2 runtime map 均选中：

- active constraints：`lower_a`；
- transfer：`zero_kink`；
- branches：`a=forward, b=zero`；
- `d=-0.0`，canonical `g_a=0.0`，canonical `g_b=0.0`；
- transfer KKT residual=`0.0`；
- complementarity residual=`0.0`；
- admissible=`true`，且为 selected policy；
- no additional selector call=`true`。

独立 forensic 的高精度根为
`0.0120851325790094875041402945557588...`，binary64 authority 表示为
`0.012085132579009488`。冻结的 513-point log-screened Brent 路径实际返回
`q_b=0.012085132579009492`，相差 2 binary64 ULP，raw root residual 为
`1.7763568394002505e-15`，小于既有 arithmetic bound
`2.901541422966794e-13`。未修改 root law、screen、Brent 配置或 tolerance。

因此同一路径得到：

- kink interval：
  `[0.010876619321108543, 0.013293645836910442]`；
- `q_a=0.010876619321108543`；
- `lambda_a=0.0002848986323410619`；
- Hamiltonian=`-0.12808167052185432`。

这些值分别处于 task 所列 binary64 target 的 2 ULP 或更小范围内。证据同时
保留 task target 与冻结运行的原始 binary64 输出，没有改写为 target 字面值。

普通 endpoint 语义保持：backward endpoint 仍仅以
`B_DERIVATIVE_DIRECTION_INCONSISTENT` 拒绝；forward endpoint 仍以
`ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERSECTION_EMPTY` 在 controls 前拒绝。

## F0364 regression

focused 与正常北京 runtime receipt 均 PASS，selected policy 精确保持：

- branches：`a=zero, b=backward`；transfer=`negative`；
- `q_b=0.006091715618507631`；
- `q_a=-0.0045978913784868415`；
- `d=-7.8384208979658965`；
- `g_a=0.0`，`g_b=-4.227123020026542`；
- KKT residual=`0.0`；
- Hamiltonian=`-0.11188508398929994`。

active liquid face 与 ratio-zero 既有 fail-closed 回归均 PASS。

## Mandatory turn-1 compatibility replay

Terminal：
`PASS__TURN1_ACCEPTED_POLICY_IDENTITY_PARITY_UNDER_LOWER_A_INTERIOR_Z_COMPOSITION_REPAIR`

- maps replayed：408；
- exact matches：408；mismatches：0；
- accepted/replayed ordered digest：
  `E23F77D21521B31C62CFEFFFFA1ACF4C39D69D577A6CFBA697DAB03AE9428B6B`；
- selector evaluations：326,400；
- scalar roots：130,794；interior-Z：24,354；interior-a：392；joint：49；
- HJB direct updates、D2/Q、SCC/KFE/SVD、aggregate/integration、retry：全部 0。

## Fresh turn-2 run004

在首个失败前：

- source-native initializations：8；labor roots attempted/returned：6,400/6,400；
- selector evaluations：80,800；corrected policy maps：101；
- D2/Q assemblies：101；direct HJB updates：94；post-update checkpoints：93；
- scalar selector roots：34,735；interior-Z roots：7,477；
- converged province aggregates：7；
- SCC：7；restricted GESVD：7；normalized stationary candidates：7；
- full-Q `Q.T@p`：7；full-space GESVD：0；
- scientific retries：0；solver substitutions：0。

首个失败证据：

- province：黑龙江，index 7；
- checkpoint：3；flat：63；indices `(b,a,z)=(3,3,0)`；
- cell SHA-256：
  `17C5808B073AF454172EA0478EB144CE1E6145F7657EF0C06C78C747E953F6D3`；
- outcome：`NO_ADMISSIBLE_POLICY`；
- stage：`selector_outcome`。

因 fail-closed 停止：household batch、labor/K1A/C1 integration、firms、
wage/monetary/fiscal、canonical raw turn3 payoff、turn3 household、K1B、K2、
adaptive controller、MATLAB/GE/Results 均为 0。

## Evidence seal

Evidence root：
`reports/ch5_mp4c_lower_a_interior_z_composition_repair_turn1_parity_turn2_run004_20260921/`

- manifest entries：1,146；
- total bytes：16,835,962；
- sealed manifest SHA-256：
  `1C501CEF7740748805CF538A05ECF9D80938149CDDF31A3158091F665C45AD80`；
- independent readback：PASS，bad paths=0，scientific calls=0。

本任务未修改 CURRENT，未 merge main，未发布 successor。
