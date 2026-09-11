# Chapter 5 两资产 HANK 当前状态
更新：2026-09-11。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_SCORING_DATA_PARTIAL_FREEZE_ACCEPTED__K1A_ZERO_SCIENCE_DISTANCE_MAPPING_ACTIVE`。
最新 K1 implementation 接受候选：`742ae11dbb057c7d33650ed4bc8d4db59b90d435`。
Reviewer acceptance：`docs/CH5_MP4C_K1_BILATERAL_CAPITAL_NETWORK_REPAIR_AND_ENDOGENOUS_FOREIGN_SHARE_IMPLEMENTATION_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1A_2018_DISTANCE_SCORE_MAPPING_AND_STATIC_PORTFOLIO_DIAGNOSTIC.md`。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

资本网络科学设计冻结稿：
`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。
K1 scoring/data 冻结稿：
`docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`。
后续有关K1/K2的经济解释、矩阵方向、时序、分阶段顺序和Owner待决参数，应优先以这两份冻结稿为准，不再依赖聊天回忆。

## 当前 Owner-approved scoring/data freeze
已冻结：
- 顺序：K1A repaired equal-share → K1A pure-geographic → K1B lagged-return → K2；
- K1A第一距离概念：纯地理距离；
- distance normalization：全国共同尺度 `D[j,i]/D_max`，不做逐行/逐列归一化；
- zero-science `beta_distance` diagnostic grid：`[0,.5,1,2,4]`，仅用于静态形状/集中度，不是最终参数；
- K1B attractiveness：completed-iteration raw unclipped `ra0` 的跨省 z-score，只允许进入下一 outer iteration；
- zero-science `beta_return` diagnostic grid：`[0,.25,.5,1,2]`，仅用于代数解释，不是最终参数；
- attractiveness 与 household payoff return 严格分离；
- 第一版 K1A/K1B 不启用 portfolio smoothing/partial adjustment；
- 第一次 K1 scientific integration 继续 source-faithful labor。

仍待 Owner freeze：最终 `beta_distance`、最终 `beta_return`、household payoff-return concept，以及未来 economic-distance/market-size 扩展、任何 smoothing 重新引入、K2 endogenous-theta functional form。

## 已接受的资本侧重构主线
### C1 GovInv residual public assets
Owner已冻结GovInv经济含义：GovInv代表不可直接观测的政府/公共生产性资产，而非任意numerical balancing stock。已接受C1定义：
`GovInv=max(Ktarget-Kprivate,0)`。
历史clipped-return C0 controller会在K已高于target时继续`GovInv*=1.1`，是此前2–3倍capital overshoot的主要机制。C1 contemporaneous 25-turn bounded diagnostic完成775/775 province-turn accounting assertions，turn20-25 total-K/Ktarget=`1/1/1`，GovInv-driven overshoot消失。

### price/numeraire/raw-ra forensic
在旧private-capital allocation仍使用legacy逻辑的C1路径上，turn25 raw `ra0` 30/31高于历史`.09`上界。zero-science decomposition显示主要来源是`rk=mt*alpha*Y/K`；profit/K几乎不贡献，delta固定`.025`只向下调整。return bounds `[.02,.09]`当前仅分类为`EMPIRICAL_NUMERICAL_SAFEGUARD`；wage bounds `[.8,1.3]`为`SOURCE_VALUE_WITH_UNRESOLVED_ECONOMIC_UNIT`。当前证据不足以直接扩大/删除return clips。

## K1 bilateral private-capital network：最新接受
Owner重新确认原经济意图：每省household illiquid wealth同时持有本省和外省企业资产，本省权重更高，household `rah`应由实际资本组合的省级回报加权得到。Owner曾真实尝试三资产多省HANK，但单HA求解约由两资产20秒上升到三资产5分钟；若真正把30个外省资产显式纳入household state，会导致不可接受的维度与稳态成本。K1/K2因此采用“household两资产 + post-household bilateral portfolio layer”，而不是31资产HJB。

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

## 已冻结的理论方向：nested Scheme B
最终理论结构不是简单的单层均匀外投改进，而是嵌套结构：
- household继续只有两资产`(b,a)`；
- `a_i`解释为省`i` household持有的provincial portfolio fund；
- 第一层未来决定home vs foreign margin；
- 第二层决定foreign destinations之间的bilateral shares。

K1当前只实现第二层，并暂时固定`theta_i`。foreign destination engine允许：
`score[j,i] = -beta_distance*distance_score[j,i] + beta_return*lagged_return_score[j]`，仅对`j!=i`做softmax。

Owner明确赞成lagged timing：allocation iteration n+1只能使用completed iteration n的return-attractiveness signal，避免same-turn `firm -> ra -> shares -> K -> firm`反馈导致震荡。这个顺序是steady-state numerical fixed-point timing，不是现实时间瞬时调整。

## 分阶段 scientific route
### K1A
固定`theta_i`。先完成当前 zero-science mapping task，然后依次验证 repaired equal-share 与 pure-geographic space-only 资本网络。真实科学 integration 前仍须由Owner从静态证据冻结最终 `beta_distance` 与 payoff-return contract。

### K1B
仍固定`theta_i`，加入completed-iteration raw `ra0` z-score的lagged-return endogenous foreign destination shares。最终 `beta_return` 必须在trajectory前冻结，且不得same-turn更新。

### K2
K1科学验证后，才讨论让`theta_i`自身内生化，最终使外投比例成为`1-S[i,i]`的模型结果。

## 与C1、labor、KFE的联合边界
K1会改变`Kprivate`，因此此前C1 25-turn旧private-K量级不能直接外推。未来必须重新联合验证`K1 private capital + C1 residual GovInv`。若`Kprivate>=Ktarget`，GovInv必须floor到0并保留private-only overshoot。

origin-preserving bilateral labor normalization已接受，但第一次K1 scientific integration不同时启用，避免资本与劳动同时改变导致无法归因。

KFE必须区分：clean/source-free generator-KFE合同已有稳定验证版本；当前corrected-2018 empirical finite-box upper-b leakage/pinning仍为独立 scientific blocker，未因K1修复解决。

## corrected-2018数据合同
当前活动数据契约继续使用actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM capital、`delta_pim=.096`、`alpha=.7380939146868483`、MU=`10万元`、NU=`100 persons`、same-year Zt0。asset bridge `beta_a=1`仍为`SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`，不能从convergence反推。

## 当前科学边界
当前 active Builder task 仅为 zero-science 2018 distance/source mapping + static portfolio diagnostics。其 MATLAB/Python HJB/KFE/firm/outer-loop/steady-state/trajectory/GE/annual/IRF/Results scientific/model call budget 全部为 `0`。

不得直接开始trajectory。当前task完成并验收后，由Owner/Reviewer根据静态矩阵证据冻结最终 `beta_distance`；在K1B前还须冻结最终 `beta_return`；任何改变 household `rah` 的runtime integration前必须另外冻结 payoff-return concept。
