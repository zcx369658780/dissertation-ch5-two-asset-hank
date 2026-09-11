# Chapter 5 多省份双边资本网络科学设计冻结稿

更新：2026-09-11。状态：`SCIENTIFIC_DESIGN_FREEZE__K1_ACCOUNTING_ACCEPTED__SCORING_AND_K2_PENDING_OWNER_FREEZE`。

## 1. 设计动机与历史背景

Owner 原始经济意图从未是“只有跨省资本流入才构成企业私人资本”，而是：每省 household 的 illiquid wealth 同时持有本省与外省企业资产，本省持仓更多；household illiquid return `rah` 应由这组真实省际资产组合的收益加权得到。旧 MATLAB 版本为了避免 31 资产 HJB 的维度爆炸，保留两资产 HA 并设置固定对外投资比例 `inter_prv_ratio_i`，再将外投资产在其他省份间简化配置。

Owner 曾真实尝试过三资产多省 HANK，但单个 HA 模块由两资产约 20 秒上升到三资产约 5 分钟；31 省稳态因此不可接受。若继续扩展为每省一个 foreign asset，最终会形成约 31 个 illiquid destination assets 的高维 HJB。K1/K2 路线的目标正是：**不增加 household state dimension，却恢复完整双边资本网络与内生空间配置。**

旧 source-faithful `HANK_mp_1turn.m` / `capital_allocation.py` 被确认有两个结构性遗漏：
1. destination private K 只统计跨省流入，漏掉 `(1-theta_i) A_i N_i` 的本省 retained capital；
2. `rah` 外省部分再次乘 destination `theta_j`，这是早期 destination-weight 思路遗留，与后来“theta 只表示 origin 对外投资比例”的简化设定不一致，导致 portfolio weights 一般不和为 1。

## 2. 当前模型的核心抽象：省籍基金 / provincial portfolio fund

household HJB 继续只保留两资产 `(b,a)`。省 `i` household sector 的 aggregate illiquid wealth 定义为：

`W_i = A_i * N_i`。

将 `a_i` 解释为省 `i` household 持有的 illiquid provincial portfolio fund，而不是显式的 31 个目的地资产状态。基金通过一个完整的 `destination x origin` 组合矩阵 `S^K` 持有全国企业资产。

这个中介层把 household saving decision 与 cross-province portfolio allocation 分开：
- household block 决定总 illiquid wealth；
- capital-network block 决定这笔 wealth 如何分布到全国企业；
- firm returns 再通过同一 portfolio matrix 汇总为 household `rah`。

因此资本流量与收益聚合必须使用同一个矩阵，避免旧模型 quantity weight / return weight 不一致。

## 3. K1 已冻结并接受的 nested Scheme B

K1 暂时保留：

`theta_i = inter_prv_ratio_i`

作为 origin `i` 的总对外投资比例，不在本阶段内生化 home-vs-foreign margin。

定义：

- home share：`S[i,i] = 1 - theta_i`
- foreign conditional shares：`P[j,i]`, `j != i`
- foreign full share：`S[j,i] = theta_i * P[j,i]`
- `P[i,i] = 0`
- `sum_{j != i} P[j,i] = 1`
- `sum_j S[j,i] = 1`

双边 private-capital flow：

`M_K[j,i] = S[j,i] * W_i`

目的省 private productive capital：

`Kprivate_j = sum_i M_K[j,i]`

household illiquid portfolio return：

`rah_i = sum_j S[j,i] * portfolio_return_j`

由此强制：

`sum_j M_K[j,i] = W_i`

以及：

`sum_j Kprivate_j = sum_i W_i`。

K1 zero-science implementation candidate `742ae11dbb057c7d33650ed4bc8d4db59b90d435` 已接受。非对称 fixture 中 legacy destination K `[63,50,17]` 修复为 `[79,80,41]`，差额 `[16,30,24]` 精确等于遗漏的本省 retained capital；legacy `rah` implied weight sums `[.93,.75,.48]` 修复为 `[1,1,1]`。

## 4. foreign destination share 的最终方向

Owner 与 Reviewer 已同意：foreign allocation 不应永久停留在 `1/(N-1)` 均分，而应形成受空间摩擦与收益吸引力共同决定的内生权重。

当前 K1 pure engine 已预留：

`score[j,i] = - beta_distance * distance_score[j,i] + beta_return * lagged_return_score[j]`

并仅在 `j != i` 上做 stable softmax：

`P[j,i] = softmax_j(score[j,i])`。

经济解释是：
- distance/friction 抑制跨省资本配置；
- expected/lagged return attractiveness 提高目的省资本权重；
- `theta_i` 仍控制 origin 总外投规模；
- K2 才考虑让 `theta_i` 本身内生化。

## 5. 为什么不做 contemporaneous same-turn return allocation

Owner 明确确认过去曾遇到 same-turn 价格反馈导致稳态震荡不收敛。当前 steady-state numerical iteration 必须采用 lagged timing：

`allocation iteration n+1 uses completed iteration n return score`。

禁止：

`firm -> current ra -> current portfolio shares -> current K -> same-turn firm`。

推荐外层数值时序：
1. household block 使用上一完整 iteration 的 `rah` / wage；
2. household output 得到 `A_i`；
3. K1 根据上一完整 iteration 的 return-attractiveness score 与当前 `W_i=A_iN_i` 形成资本矩阵；
4. firms 使用新 `Kprivate`；
5. firms 输出新的 raw/used return；
6. 新 return 只进入下一 outer iteration 的 capital-share attractiveness。

这是 steady-state fixed-point solver 的 numerical timing，不是现实时间中政府或资本瞬时调整的结构假设。

## 6. K1 与 K2 的分阶段路线

为了避免单次多省稳态约 2 小时以上的运行被低信息量试错消耗，冻结分阶段顺序：

### K1A — accounting / repaired baseline
- 固定 `theta_i`；
- 首先验证 repaired equal-share 或 space-only allocation；
- 重点确认 capital conservation、home retained K、`rah` 权重一致；
- 不同时启用 normalized labor。

### K1B — lagged-return endogenous foreign destination shares
- 固定 `theta_i`；
- foreign `P[j,i]` 加入 lagged return attractiveness；
- 只使用 completed-iteration return signal；
- 首次 trajectory 仍保持 source-faithful labor，以隔离资本通道。

### K2 — endogenous home-vs-foreign margin
未来才讨论 `theta_i` 内生化，例如嵌套 home/foreign choice：
- 第一层决定 home vs foreign；
- 第二层决定 foreign destination shares；
- 这样旧外生 `inter_prv_ratio_i` 最终可变成模型结果 `1-S[i,i]`。

K2 不得在 K1 尚未科学验证时提前实施。

## 7. distance / financial-friction 设计方向

当前工程接口允许任意 caller-provided dimensionless `distance_score[destination,origin]`，但尚未冻结数据映射。

候选路线：

### A. pure geographic-distance baseline
优点：最少参数、最容易解释、最适合作为 K1A/K1B 第一科学版本。

### B. geographic + economic distance
候选 economic distance 可使用：

`abs(log(pgdp_i) - log(pgdp_j))`

但 pgdp difference 应解释为 friction / similarity，而目的省经济规模应作为独立 attractiveness，而不是把两者混为一项。

未来可扩展：trade linkage、industrial similarity、financial-center effect，但第一 scientific version 不应一次加入过多变量。

## 8. return attractiveness 与 payoff return 必须分离

K1 API 已强制区分：

- `lagged_return_score_by_destination`：只用于 foreign destination attractiveness；
- `portfolio_return_by_destination`：只用于 `rah` payoff aggregation。

原因：当前 raw `ra0`、clipped `ra`、normalized return、expected return 的经济 period / numeraire 尚未最终冻结。

不得默认用 clipped `.02-.09` return 做 attractiveness，因为此前 price forensic 已证明该区间只是 `EMPIRICAL_NUMERICAL_SAFEGUARD`，且 C1旧路径下 30/31 raw `ra0` 高于 `.09`。使用 clipped return 会人为抹平省际差异。

候选 return score 在科学冻结前至少比较：
- raw lagged `ra0`；
- relative raw return `ra0_j - mean(ra0)`；
- standardized cross-sectional score；
- smoothed/expected return。

不得观察 trajectory 后再选择 normalization。

## 9. 与 financial gravity / multi-country portfolio literature 的关系

本项目不直接照搬 31-asset household portfolio FOC，因为会重新引入高维 HJB。文献仅作为结构启发：
- multi-country portfolio allocation：收益、风险、portfolio frictions 共同决定资产组合；
- financial gravity：market size、distance、information/transaction frictions 解释 bilateral holdings；
- dynamic spatial GE：资本与劳动跨地区流动可分别形成双边网络，并在摩擦下保留地区收益差异。

因此当前最合适的模型层是：

`household aggregate illiquid wealth -> bilateral portfolio/intermediary layer -> province firms`。

它保留两资产 HA 的计算可行性，同时允许未来形成双内生空间传导：
- bilateral labor network；
- bilateral capital network。

## 10. 与 C1 GovInv residual public assets 的联合关系

Owner 已冻结：

`GovInv = max(Ktarget - Kprivate, 0)`

GovInv 是不可直接观测的政府/公共生产性资产 residual，不是 return controller。

旧 C1 25-turn result 使用 legacy private-capital allocation，只能证明在旧 `Kprivate` 定义下 GovInv-driven overshoot 可被消除。K1 修复会显著提高并重新分布 private K，所以未来 K1 scientific integration 时必须重新验证：

`Kprivate(K1) + GovInv(C1)`。

若某省 `Kprivate >= Ktarget`，C1 必须让 GovInv=0 并显式保留 private-only overshoot；不得用负 GovInv 强行抵消。

## 11. 与 labor route 的关系

origin-preserving bilateral labor normalization 已接受，但第一次 K1 scientific integration 暂不同时启用。原因是要保持 attribution：先验证资本网络修复本身，再单独 stack normalized labor。

最终理论目标可形成平行结构：

- `origin labor stock x destination labor-attractiveness shares`；
- `origin private wealth x destination capital-portfolio shares`。

两者都保留完整 destination-by-origin flow matrix，但摩擦和经济 signal 不同。

## 12. 与 KFE 的关系

K1 capital-network module 位于 household solve 之后，因此不改变单个省 household KFE 的数学实现；但它通过 firm return / household `rah` 改变下一 outer iteration 的 HJB policy，因此会间接改变下一轮 KFE generator。

必须继续区分：
- clean/source-free KFE 方法学合同已经稳定验证；
- corrected-2018 empirical finite-box upper-b leakage/pinning仍是独立 scientific blocker。

K1 修复不能被写成“KFE 已解决”。

## 13. 下一科学执行前必须由 Owner 冻结的对象

不得直接跑新的 2-hour+ trajectory。先冻结：
1. distance/friction score 的数据源；
2. distance score 的 dimensionless normalization；
3. lagged-return score 的来源与 normalization；
4. `beta_distance`；
5. `beta_return`；
6. portfolio payoff return concept；
7. 是否需要 portfolio smoothing / partial adjustment；
8. K1A 是否先于 K1B；
9. K1 scientific run 中 source-faithful labor 是否继续冻结（当前建议 YES）；
10. K2 endogenize `theta_i` 的进入条件。

## 14. 当前冻结结论

已经冻结/验证：
- 两资产 household state space 保持不变；
- K1 Scheme B；
- `destination x origin` matrix orientation；
- home retained capital 恢复；
- quantity / `rah` 使用同一 `S`；
- origin / national private-capital conservation；
- lagged-return timing；
- foreign conditional softmax engine；
- legacy route byte-identical保留。

尚未冻结：
- distance data mapping / normalization；
- return score / payoff return；
- `beta_distance`, `beta_return`；
- smoothing；
- K2 `theta_i` 内生化。

推测/未来工作：
- geographic + pgdp/trade/industry financial distance；
- entropy/friction interpretation；
- endogenous home-vs-foreign margin；
- normalized labor + K1 joint model；
- annual/dynamic/IRF extensions。

Results eligibility 继续为 `FALSE`。
