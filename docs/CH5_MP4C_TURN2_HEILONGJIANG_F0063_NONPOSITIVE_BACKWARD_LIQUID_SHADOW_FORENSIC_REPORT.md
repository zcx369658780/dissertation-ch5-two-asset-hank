# CH5 MP4C turn-2 黑龙江 F0063 nonpositive backward liquid-shadow forensic

日期：2026-09-21

## Terminal 与 classification

Terminal：

`BLOCKED__TURN2_HEILONGJIANG_F0063_FORENSIC__OWNER_DECISION_REQUIRED_FOR_NONPOSITIVE_ONE_SIDED_LIQUID_SHADOW_EXTENSION__NO_CODE_CHANGE`

Classification：

`CURRENT_NO_ADMISSIBLE_POLICY_CORRECT_UNDER_EXISTING_AUTHORITY__COHERENT_POSITIVE_TRANSFER_ZERO_LIQUID_ROOT_EXISTS_ONLY_OUTSIDE_AUTHORIZED_TWO_POSITIVE_SHADOW_BRACKET__OWNER_DECISION_REQUIRED`

当前 selector 在既有 authority 下正确 fail closed，不是 implementation false
negative。继续 turn2 需要 Owner 决定是否采用新的 nonpositive one-sided
liquid-shadow switching law，以及该 law 的正根 bracket 如何定义。

## Exact binding

审计对象：

`reports/ch5_mp4c_lower_a_interior_z_composition_repair_turn1_parity_turn2_run004_20260921/household/p07_黑龙江/checkpoint_003/cell_0063.json`

- accepted predecessor：`4cbd4261be31c237a99cade68ccb35a13c9306b9`；
- predecessor manifest：
  `1C501CEF7740748805CF538A05ECF9D80938149CDDF31A3158091F665C45AD80`；
- cell SHA-256：
  `17C5808B073AF454172EA0478EB144CE1E6145F7657EF0C06C78C747E953F6D3`；
- province/index/checkpoint/flat：黑龙江 / 7 / 3 / 63；
- index：`(3,3,0)`；cell id：`v003_f0063_b003_a003_z000`；
- geometric faces：none；
- checkpoint-3 V SHA-256：
  `1FA95217C9EEFDAA638F0CD07F00B59B053EB4A59E5670A0CED94852922DBFE7`；
- checkpoint-2 direct update `next_value_sha256` 与该 V hash 精确一致；
- derivative field receipts、cell derivatives 和 top-manifest entry 均 PASS。

Persisted derivatives：

- `p_a^B=0.026049395991859955`；
- `p_a^F=0.024439409021974706`；
- `p_b^B=-0.0002428532863339202`；
- `p_b^F=0.014463823441006161`。

## q_b domain 与 ordinary candidates

当前 D1-D3 authority 要求 `q_b=c^{-gamma}>0`。D3 KKT 同样明确要求
`q_b>0`，并禁止 derivative floor。corrected selector 没有 clipping、absolute
value 或 epsilon replacement authority。

该 interior/interior cell 的合法 ordinary enumeration 共 8 个 persisted
candidates：

| transfer | a branch | b branch | rejection |
|---|---|---|---|
| negative | backward | backward | `q_b_DOMAIN_INVALID_NO_DERIVATIVE_FLOOR` |
| negative | backward | forward | wrong transfer sign；B direction；A direction；KKT |
| negative | forward | backward | `q_b_DOMAIN_INVALID_NO_DERIVATIVE_FLOOR` |
| negative | forward | forward | wrong transfer sign；B direction；KKT |
| zero-kink | forward | backward | `q_b_DOMAIN_INVALID_NO_DERIVATIVE_FLOOR` |
| zero-kink | forward | forward | B direction；KKT |
| positive | forward | backward | `q_b_DOMAIN_INVALID_NO_DERIVATIVE_FLOOR` |
| positive | forward | forward | B direction |

所有 backward-liquid candidates 均在 controls 前拒绝，因为
`q_b=p_b^B<0`。forward-liquid candidates 使用 `q_b=p_b^F>0`：

- negative/backward-a：`d=0.7113185172197704>0`，与 negative regime
  相反；`g_b=-2.049609690950118` 与 backward liquid direction 相反，
  `g_a=1.2020265112113617` 与 backward-a direction 相反，KKT residual
  `0.002892764688201231`；
- negative/forward-a：`d=0.6234411762227325>0`，`g_b=-1.8786576984578685`，
  KKT residual `0.002892764688201231`；
- zero-kink/forward-a：`d=0`，`g_b=-0.9467091011465394`，KKT residual
  `0.008529203236867927`；
- positive/forward-a：D3、transfer sign 和 a-forward direction 均成立，
  但 `g_b=-1.5960747263712167`，因此 forward liquid derivative direction
  不成立。

## Existing interior-Z authority

Owner-adopted generic interior-liquid Z law 的前置条件是：

1. backward 和 forward raw liquid shadows 均 finite 且 strictly positive；
2. 同一非 liquid family 的 backward drift strictly positive、forward drift
   strictly negative；
3. root bracket 是两个 positive shadows 之间的闭区间；
4. 不得 widen bracket 或 retry。

F0063 的 backward shadow finite 但为负，因此条件 1 已失败。不存在合法的
two-positive-shadow closed bracket，endpoint drift screen 和 production Z root
均不得调用。persisted receipt 的 interior-Z root count=0 与 authority 一致。

## Interior-a 与 joint switching

Interior-a switching 不能生成 candidate：

- backward-liquid 两个 ordinary a candidates 都因 `q_b<0` 在 `g_a` 产生前
  返回，没有可审计的 a-direction crossing pair；
- forward-liquid negative-regime 两个 `g_a` 分别为
  `1.2020265112113617` 和 `1.1141491702143238`，均为正，不满足
  backward-a positive / forward-a negative strict crossing；
- 强制 `g_a=0` 会给出 `d_Z=-0.49070799399159126`、negative D3 ratio
  `q_a/q_b=0.2784365409439844`，由 illiquid derivative interval 推出的
  `q_b` interval 为
  `[0.08777371295849923,0.09355595319330069]`；两个普通 liquid shadows
  均不在该区间。

对固定 `d_Z` 的独立 liquid equation 存在正根
`q_b=0.016292425733501197`，但该根不在上述 implied interval，且对应
`q_a=0.004536406664822831`，远低于现有 illiquid derivative interval。

Joint switching 也不能生成 candidate：

- prerequisite 的两个 liquid-Z candidates 均不存在；
- liquid derivative interval
  `[-0.0002428532863339202,0.014463823441006161]` 下端非正；
- 该 interval 与 mapped `q_b` interval
  `[0.08777371295849923,0.09355595319330069]` 无交集。

## Independent positive-q_b equations

独立重建没有导入或调用 production selector/root helper。统一方程为：

`g_b(q)=w(qw)^(1/5)+r_b b+T-q^(-1/2)-d(q)-C(d(q),a)`。

采用 256-step independent binary64 bisection。各相关 family 的唯一正根为：

| family | q_b root | d | legality |
|---|---:|---:|---|
| negative / backward-a | 0.018920460453074793 | 0.3764087868819042 | d 为正，transfer sign、KKT、a-backward 均失败 |
| negative / forward-a | 0.01863335288123777 | 0.32494327486772184 | d 为正，transfer sign 与 KKT 失败 |
| zero-kink / forward-a | 0.017192264126029845 | 0 | root 处 KKT residual=0.005527918483341873 |
| positive / forward-a | 0.01801822665826406 | 0.2023985483449149 | D3/KKT/direction 均自洽，但位于 authorized bracket 外 |

这些 equation 在所列 bracket 上严格递增：labor 与 consumption derivative
terms 为正；transfer family 中 `-d'(1+C_d)` 在使用的 branch 上非负且在
`d` 变化时严格为正。因此每个 sign change 对应唯一根。

前三个根不能形成合法 candidate。最后一个 positive/forward-a 根构成唯一
值得 Owner 考虑的 diagnostic continuation。

## Diagnostic-only continuation candidate

使用新的 one-sided bracket
`[p_b^F, p_a^F/1.1]=[0.014463823441006161,0.022217644565431547]`
可得到：

- `q_b=0.01801822665826406`；
- `q_a=0.024439409021974706`；
- `d=0.2023985483449149`；
- cost=`0.04618446400350643`；
- raw `g_b=-3.95516952522712e-16`；arithmetic bound=
  `1.9601536107842595e-13`；
- `g_a=0.6931065423365061`，符合 forward-a direction；
- transfer KKT residual=`0`；
- Hamiltonian=`-0.14035289592597935`。

该 root 比 positive forward shadow 高 `0.0035544032172578986`，既不位于
两个 raw liquid shadows 之间，也没有两个 positive shadow endpoints。
把它变成 candidate 必须采用新的 one-sided/nonpositive-shadow bracket
extension。因此它仅是 diagnostic evidence，不能实现或用于续跑。

## Historical/source-faithful precedent

历史 MATLAB-faithful policy 确实包含 `MATLAB_DERIVATIVE_FLOOR=1e-6` 并对
`VbB/VbF` 使用 `max(...,floor)`。当前 corrected authority 明确禁止 derivative
floor，且没有 Owner adoption 把该历史处理继承到 corrected selector。因此该
历史实现不是覆盖 F0063 sign pattern 的当前 scientific authority。

## Zero-science ledger

- persisted cell / derivative receipt / direct-solve receipt loads：1 / 1 / 1；
- independent scalar equation families：5；
- independent binary64 bisection diagnostics：5；
- production selector/root helper：0 / 0；
- HJB、D2/Q、SCC/KFE/SVD、aggregate/integration：全部 0；
- turn2 replay/rerun、turn3、MATLAB science：全部 0；
- firm/K1A/C1/wage/monetary/fiscal、GE/Results：全部 0；
- retry/tuning：0。

Focused forensic tests：3 passed；`py_compile`、`git diff --check` PASS。

## Evidence

Evidence root：

`reports/ch5_mp4c_turn2_heilongjiang_f0063_nonpositive_backward_liquid_shadow_forensic_20260921_run001/`

- manifest entries：14；
- total bytes：37,703；
- manifest SHA-256：
  `402E3A93C5E7E560B0887918E92E0AE550D29FD7560AB9B0EB2E4DD38448024E`；
- independent readback：PASS；bad paths=0；scientific calls=0。

本任务未修改 `src/ch5_two_asset_hank/**`、CURRENT 或 accepted run004
evidence；未发布 successor，未 merge main。
