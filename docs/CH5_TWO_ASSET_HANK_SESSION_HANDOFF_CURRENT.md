# Chapter 5 当前交接
更新：2026-09-11。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

Owner为最终scientific authority；ChatGPT为L3 independent reviewer / scientific-route authority / GitHub exact-task issuer / acceptance-gate reviewer；Codex为bounded Builder，默认`gpt-5.6-sol / medium`。GitHub live main是唯一repository-state authority；聊天不能替代task authority。

## 新会话恢复顺序
1. fresh-fetch live `origin/main`，不要把本交接中的SHA假定为最新；
2. 读取`AGENTS.md`；
3. 读取`project_rules/PROJECT_RULE_INDEX_CURRENT.md`；
4. 读取`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`；
5. 读取本交接；
6. **必须读取**`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`；
7. 读取`docs/CH5_MP4C_K1_BILATERAL_CAPITAL_NETWORK_REPAIR_AND_ENDOGENOUS_FOREIGN_SHARE_IMPLEMENTATION_ACCEPTANCE.md`及其report；
8. 如继续科学工作，先完成Owner/Reviewer的K1 scoring/data contract冻结，再发布新的exact GitHub task。

## 当前状态
状态：`K1_BILATERAL_CAPITAL_NETWORK_ACCEPTED__HOME_CAPITAL_RESTORED__PORTFOLIO_AND_CAPITAL_CONSERVATION_ENFORCED__LAGGED_ENDOGENOUS_FOREIGN_SHARE_ENGINE_READY_FOR_PARAMETER_FREEZE`。
当前 active Builder task：无。
最新接受候选：`742ae11dbb057c7d33650ed4bc8d4db59b90d435`。
Reviewer acceptance：`docs/CH5_MP4C_K1_BILATERAL_CAPITAL_NETWORK_REPAIR_AND_ENDOGENOUS_FOREIGN_SHARE_IMPLEMENTATION_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

资本网络科学设计唯一冻结稿：
`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。
后续不要依赖聊天摘要猜测Owner原意；K1/K2理论结构、历史动机、分阶段顺序、lagged timing、distance/return score候选及待Owner冻结项均已固化在该文件。

## 本会话最重要的新科学发现：legacy private-capital network 有结构性遗漏
Owner确认原经济意图：每省household aggregate illiquid wealth既持有本省企业资产，也持有外省企业资产；本省权重更高；household `rah`应为实际省际portfolio的收益加权。

protected MATLAB / source-faithful Python旧逻辑实际上：
- `Kt_supply_i`只计算其他省cross-province inflows，漏掉`(1-theta_i)*At_i*N_i`本省retained private capital；
- `rah_i`外省部分再次乘destination `theta_j`，这是早期“destination investment weight”设计残留，与后来`theta`仅表示origin对外投资比例的简化意图不一致；因此portfolio weights一般不和为1。

这可以解释此前private-K/Ktarget异常偏小以及household return被机械压低的部分现象。旧source继续保留用于parity，但不再代表新的economic successor design。

## 为什么继续两资产而不是31资产HANK
Owner并非没有尝试过多资产内生资本流动：曾做过三资产多省HANK，但单个HA求解由两资产约20秒上升到三资产约5分钟；31省稳态会变得不可接受。若只增加一个foreign asset，它无法记录30个目的地的真正双边网络；若每个目的地都成为household asset state，则形成31资产HJB并产生维度爆炸。

因此当前路线是计算上可行的中介式设计：household仍决定总illiquid wealth，post-household provincial portfolio layer决定31省配置。它不是放弃资本内生化，而是把高维household portfolio state choice压缩为一个低成本的bilateral portfolio/intermediary block。

## Owner冻结的资本网络理论方向：nested Scheme B
不再尝试31-asset HJB。household继续两资产`(b,a)`；每个origin household sector的aggregate illiquid wealth在post-household portfolio layer分配到31省企业。

最终愿景是双层：
1. home-vs-foreign margin；
2. foreign destinations内部的bilateral allocation。

但K1第一阶段只内生化foreign destination shares，暂时保留`theta_i=inter_prv_ratio_i`作为origin总对外投资比例。K2未来才讨论让`theta_i`本身内生化。

## K1 accepted contract
新模块：`src/ch5_two_asset_hank/multi_province/capital_network.py`。

orientation：rows=destination，columns=origin。

对origin i：
- `W_i=A_i*N_i`；
- `S[i,i]=1-theta_i`；
- `S[j,i]=theta_i*P[j,i]` for `j!=i`；
- `sum_j S[j,i]=1`；
- `M_K[j,i]=S[j,i]*W_i`；
- `Kprivate_j=sum_i M_K[j,i]`；
- `rah_i=sum_j S[j,i]*portfolio_return_by_destination[j]`。

quantity allocation与household return必须使用同一个`S`。

foreign conditional share engine：
`score[j,i] = -beta_distance*distance_score[j,i] + beta_return*lagged_return_score[j]`，仅foreign destinations参与stable softmax。

`beta_distance`、`beta_return`都是显式必填参数，没有默认值；当前没有科学识别/选择。

return signal与payoff return分离：
- `lagged_return_score_by_destination`只决定foreign attractiveness；
- `portfolio_return_by_destination`只决定household `rah`。

## lagged timing必须保留
Owner明确支持lagged update以避免same-turn nonlinear feedback导致震荡，且这与旧MATLAB“先household、再firm、最后更新ra/wjt进入下一轮”的数值经验一致。

冻结合同：allocation iteration n+1只能使用completed iteration n的return-attractiveness signal。禁止same-turn `firm -> return -> portfolio shares -> K -> firm`闭环。

这属于steady-state numerical iteration timing，不是现实calendar-time政府/家庭瞬时调整解释。

## K1 accepted evidence
候选：`742ae11dbb057c7d33650ed4bc8d4db59b90d435`。

final focused tests：`29/29` PASS；compile、diff/show checks PASS；manifest `15/15` readback；scientific/model/runtime calls=`0`。

非对称fixture：
- origin wealth `[20,60,120]`，全国200；
- legacy destination private K `[63,50,17]`；
- repaired `[79,80,41]`；
- repaired-minus-legacy `[16,30,24]`，精确等于遗漏的home retained capital；
- legacy implied `rah` weight sums `[.93,.75,.48]`；
- repaired `[1,1,1]`；
- national conservation residual 0。

`beta_distance=beta_return=0`时，foreign shares精确退化为`1/(N-1)`，即Owner原来想要的“固定theta + 外省均匀投资”版本，但现在资本与return权重都正确守恒。

legacy `src/ch5_two_asset_hank/multi_province/capital_allocation.py`保持byte-identical，SHA256=`BB3F283BD782399A5C1C9AEE06DC50BBA61A0599BF062669DE0B1EBBB01AEE40`。

## 未来资本网络科学分阶段路线
考虑单次多省稳态可能超过2小时，冻结一次只增加一个内生反馈：

### K1A — repaired baseline / space-only
固定`theta_i`。第一科学版本优先只验证修复后的资本守恒和空间配置，可采用equal foreign shares或预先冻结的纯distance share；不加入return feedback也不同时启用normalized labor。

### K1B — lagged-return endogenous foreign shares
仍固定`theta_i`，在foreign share中加入completed-iteration lagged return attractiveness。不得same-turn更新。

### K2 — endogenous home-vs-foreign margin
K1验证后，才讨论让`theta_i`本身内生化，使外投比例最终成为`1-S[i,i]`的模型结果。可采用嵌套home/foreign choice，但尚未冻结具体效用/摩擦形式。

## distance/friction与return-attractiveness候选
第一版distance contract尚未冻结。当前值得比较：
- pure geographical distance；
- geographical + economic distance，例如`abs(log pgdp_i-log pgdp_j)`。

如果使用pgdp差异，应把它解释为friction/similarity；目的省market size/attractiveness应作为独立变量，不能与economic distance混成同一概念。

return score也尚未冻结。至少应比较：
- lagged raw `ra0`；
- relative raw return；
- standardized cross-sectional return；
- smoothed/expected return。

不得默认用clipped `.02-.09` return，因为该区间已分类为`EMPIRICAL_NUMERICAL_SAFEGUARD`且会抹掉省际raw-return差异。

## 文献/理论启发边界
当前路线吸收multi-country portfolio allocation、financial gravity、dynamic spatial GE的结构思想：收益、home bias、distance/information/transaction frictions共同决定bilateral holdings；摩擦存在时不同地区长期return不必完全相等。

但当前实现**不直接复制**高维portfolio perturbation或31资产HJB。核心是：
`household aggregate illiquid wealth -> bilateral portfolio/intermediary layer -> province firms`。

最终可形成平行双内生空间通道：bilateral labor network + bilateral capital network。

## C1 GovInv：继续有效但必须在K1后重验
Owner冻结GovInv为不可直接观测政府/公共生产性资产 residual：
`GovInv=max(Ktarget-Kprivate,0)`。

此前C1 contemporaneous 25-turn bounded path消除了GovInv-driven 2–3x capital overshoot。但该路径使用legacy private-capital allocation。K1会显著改变`Kprivate`，因此未来必须把K1 private capital与C1 residual public assets联合重新验证，不能直接沿用旧private-K量级。

若K1下某省`Kprivate>=Ktarget`，GovInv必须floor到0并保留private-only overshoot，不允许负GovInv抵消私人资本超额。

## price/return forensic：结论继续有效但需要K1后复核
旧C1路径turn25 raw `ra0` 30/31高于`.09`，主要由`rk=mt*alpha*Y/K`驱动；profit/K几乎为零，delta=.025只向下。`.02/.09`是`EMPIRICAL_NUMERICAL_SAFEGUARD`，不是经济识别区间；wage `[.8,1.3]`绝对单位未闭合。

但K1修复会改变private K spatial allocation、firm K构成及Y/K，因此当前不要直接扩大return bounds。K1 scientific integration后应重新做raw-ra decomposition。

## labor route
origin-preserving bilateral labor normalization successor已接受：完整destination x origin劳动矩阵、origin-column和全国劳动守恒。第一次K1 scientific integration建议仍冻结source-faithful labor，以隔离capital-network effect；K1通过后再单独叠加normalized labor。

## KFE状态：必须区分clean方法与empirical blocker
clean/source-free KFE稳定方法学已验证：
- HJB与KFE共享同一backward generator `Q`；
- forward=`Q.T`；
- row sums=0；
- off-diagonal非负；
- unique closed recurrent class gate；
- stationary probability mass `p`先解，再由cell weights得到density；
- normalization不能修复boundary leakage。

但当前corrected-2018 empirical finite-box upper-b leakage + MATLAB-style pinning仍是独立scientific blocker。资本网络修复不会自动解决KFE。

## corrected-2018数据合同
活动合同：actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM capital、`delta_pim=.096`、`alpha=.7380939146868483`、MU=`10万元`、NU=`100 persons`、same-year Zt0。

asset bridge `beta_a=1`仍为`SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`，不得通过convergence/target matching反推。

## 下一Owner/Reviewer决策：不要直接跑模型
单次多省稳态可能超过2小时。下一会话先冻结K1 scoring/data contract，再授权科学运行。

至少要讨论并冻结：
1. `distance_score`第一版使用什么：纯geographical distance，还是加入pgdp/经济距离；
2. distance如何dimensionless normalize；
3. `lagged_return_score`使用raw `ra0`、相对return、标准化return、expected/smoothed return中的哪一种；
4. return score的period/normalization；
5. `beta_distance`、`beta_return`如何预注册或数据识别；
6. 是否先跑`beta_return=0`的space-only K1A，再加入lagged-return tilt K1B；
7. 是否需要portfolio partial adjustment/smoothing；
8. payoff return用什么对象；
9. 什么时候才进入K2 endogenize `theta_i`。

当前Reviewer倾向的最低风险顺序：
K1A repaired equal/space-only allocation → K1B lagged-return endogenous foreign shares → K2 endogenous home-vs-foreign margin。

在任何science前，应优先做zero-science 2018 distance/score mapping receipt与static portfolio matrix diagnostics，避免边跑边调。

## Workflow规则
- GitHub main唯一repository authority；
- Owner是最终scientific authority；
- ChatGPT可在standing authorization下fresh-fetch、验收、non-force纳入main、更新状态与发布bounded exact task；
- substantive scientific choice必须交Owner；
- exact task发布时同一回复附完整Codex startup prompt；
- no force push/reset/clean/stash；
- 不调参数/solver/tolerance求PASS；
- Results eligibility维持FALSE，直到独立Results gate。
