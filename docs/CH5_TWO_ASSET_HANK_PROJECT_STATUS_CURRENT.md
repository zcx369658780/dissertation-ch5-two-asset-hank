# Chapter 5 两资产 HANK 当前状态
更新：2026-09-11。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_BILATERAL_CAPITAL_NETWORK_ACCEPTED__HOME_CAPITAL_RESTORED__PORTFOLIO_AND_CAPITAL_CONSERVATION_ENFORCED__LAGGED_ENDOGENOUS_FOREIGN_SHARE_ENGINE_READY_FOR_PARAMETER_FREEZE`。
最新接受候选：`742ae11dbb057c7d33650ed4bc8d4db59b90d435`。
Reviewer acceptance：`docs/CH5_MP4C_K1_BILATERAL_CAPITAL_NETWORK_REPAIR_AND_ENDOGENOUS_FOREIGN_SHARE_IMPLEMENTATION_ACCEPTANCE.md`。
当前 active Builder task：无。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

## 已接受的资本侧重构主线
### C1 GovInv residual public assets
Owner已冻结GovInv经济含义：GovInv代表不可直接观测的政府/公共生产性资产，而非任意numerical balancing stock。已接受C1定义：
`GovInv=max(Ktarget-Kprivate,0)`。
历史clipped-return C0 controller会在K已高于target时继续`GovInv*=1.1`，是此前2–3倍capital overshoot的主要机制。C1 contemporaneous 25-turn bounded diagnostic完成775/775 province-turn accounting assertions，turn20-25 total-K/Ktarget=`1/1/1`，GovInv-driven overshoot消失。

### price/numeraire/raw-ra forensic
在旧private-capital allocation仍使用legacy逻辑的C1路径上，turn25 raw `ra0` 30/31高于历史`.09`上界。zero-science decomposition显示主要来源是`rk=mt*alpha*Y/K`；profit/K几乎不贡献，delta固定`.025`只向下调整。return bounds `[.02,.09]`当前仅分类为`EMPIRICAL_NUMERICAL_SAFEGUARD`；wage bounds `[.8,1.3]`为`SOURCE_VALUE_WITH_UNRESOLVED_ECONOMIC_UNIT`。当前证据不足以直接扩大/删除return clips。

## K1 bilateral private-capital network：最新接受
Owner重新确认原经济意图：每省household illiquid wealth同时持有本省和外省企业资产，本省权重更高，household `rah`应由实际资本组合的省级回报加权得到。

legacy `HANK_mp_1turn.m`/Python source-faithful `capital_allocation.py`被确认存在两项结构性遗漏：
1. destination private K只统计跨省流入，没有加入`(1-inter_prv_ratio_i)*At_i*N_i`本省retained private capital；
2. `rah`外省收益再次乘destination `inter_prv_ratio_j`，与后来“theta只表示origin对外投资比例”的简化意图不一致，portfolio weights通常不和为1。

K1 successor已在`src/ch5_two_asset_hank/multi_province/capital_network.py`实现，但尚未接线：
- orientation：`destination x origin`；
- origin wealth：`W_i=A_i*N_i`；
- 当前固定`theta_i=inter_prv_ratio_i`；
- home share：`S[i,i]=1-theta_i`；
- foreign share：`S[j,i]=theta_i*P[j,i]`；
- `P[:,i]`在foreign destinations上通过stable softmax归一化；
- bilateral flow：`M_K[j,i]=S[j,i]*W_i`；
- destination private K：row sums；
- household `rah_i=sum_j S[j,i]*portfolio_return_j`；
- quantity与return严格使用同一个`S`；
- origin-column与national private capital conservation强制检查；
- same-turn return feedback禁止，只允许completed-iteration/lagged return score。

accepted asymmetric fixture：origin wealth `[20,60,120]`，national `200`；legacy destination K `[63,50,17]`，repaired `[79,80,41]`；差额`[16,30,24]`等于遗漏home retained capital；legacy `rah`权重和`[.93,.75,.48]`，repaired=`[1,1,1]`。final focused tests `29/29`通过，scientific/model/runtime calls=`0`。legacy `capital_allocation.py` byte-identical。

## K1下一Owner gate
K1 engineering/accounting contract已闭合，但scientific coefficients尚未识别。任何bounded trajectory前必须冻结：
- distance/friction data mapping及dimensionless normalization；
- lagged-return attractiveness score来源、period与normalization；
- `beta_distance`；
- `beta_return`；
- portfolio smoothing/partial-adjustment是否启用；
- portfolio payoff使用raw `ra0`、clipped `ra`、normalized return或expected return；
- 是否先保持`theta_i`固定完成K1 scientific validation，再进入K2 endogenize home/foreign margin。

当前倾向的理论结构是nested Scheme B：household继续两资产`(b,a)`，不增加31个asset states；K1先固定`theta_i`只内生化foreign destination shares，K2未来才讨论让`theta_i`本身内生。

## KFE状态
必须区分两件事：
- clean/source-free generator-KFE合同已有稳定验证版本，核心为同一backward generator `Q`、forward=`Q.T`、row-sum/off-diagonal/closed-class/mass-first stationary checks；
- 当前corrected-2018 empirical finite-box upper-b leakage/pinning仍为独立 scientific blocker，未因K1修复解决。

## corrected-2018数据合同
当前活动数据契约继续使用actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM capital、`delta_pim=.096`、`alpha=.7380939146868483`、MU=`10万元`、NU=`100 persons`、same-year Zt0。asset bridge `beta_a=1`仍为`SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`，不能从convergence反推。

## 当前科学边界
当前没有active Builder task。不得自动运行新的HJB/KFE/firm/outer-loop/trajectory/steady-state/GE/annual/IRF/Results。

下一步应先在新会话中冻结K1 scoring/data contract，再发布单独的zero-science mapping task或bounded integration task。考虑单次多省稳态计算成本可能超过2小时，应尽量先完成静态识别和预注册参数，再只运行一次有信息量的bounded trajectory。
