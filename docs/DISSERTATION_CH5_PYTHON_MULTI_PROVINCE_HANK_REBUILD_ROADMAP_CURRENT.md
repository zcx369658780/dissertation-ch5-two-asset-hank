# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-11。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

资本网络科学设计冻结稿：
`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。

## 当前阶段
当前已从“复刻原MATLAB mixed-year流程”推进到“修正资本侧经济结构并建立可审计 successor route”。Results=`FALSE`。

已完成并接受的关键节点：
1. MATLAB/Python two-asset HA parity P1–P4；
2. corrected-2018 runtime binding与raw-NBS Track-A数据合同；
3. HJB nonconvergence finite continuation contract；
4. C1 residual public-asset GovInv定义与25-turn bounded validation；
5. origin-preserving bilateral labor normalization zero-science successor；
6. price/numeraire/raw-ra forensic；
7. K1 bilateral private-capital network zero-science implementation；
8. K1/K2 scientific design freeze：两资产省籍基金 + nested bilateral portfolio route + lagged-return timing。

## C1 GovInv authority
GovInv解释为不可直接观测的政府/公共生产性资产 residual：
`GovInv=max(Ktarget-Kprivate,0)`。
历史C0 clipped-return `0.9/1.1` controller已证明会重新制造GovInv overshoot。C1 bounded path中775/775 capital accounting assertions通过，turn20-25 total-K/Ktarget固定为1，资本数量/GovInv level divergence不再是同一优先级的直接blocker。

但该C1 scientific path使用legacy private-capital allocation。K1会改变`Kprivate`，因此后续必须重新联合验证`K1 private capital + C1 residual GovInv`，不得沿用旧private-K量级结论。

## 为什么采用两资产省籍基金而不是31资产HANK
Owner曾真实尝试三资产多省HANK，但单个HA模块由两资产约20秒上升到三资产约5分钟。若把30个外省目的地都显式写成household assets，会造成31资产HJB与严重维度爆炸。只保留一个foreign asset又无法保存真正的30目的地双边网络。

因此当前路线把高维portfolio state choice拆成post-household intermediary layer：

`household aggregate illiquid wealth -> bilateral provincial portfolio fund -> province firms`。

household HJB继续只有`(b,a)`；portfolio layer负责31省配置。这样既保留两资产HA的可计算性，又能逐步实现资本全国内生化。

## K1 bilateral capital network：当前冻结点
最新接受候选：`742ae11dbb057c7d33650ed4bc8d4db59b90d435`。
Reviewer acceptance：`docs/CH5_MP4C_K1_BILATERAL_CAPITAL_NETWORK_REPAIR_AND_ENDOGENOUS_FOREIGN_SHARE_IMPLEMENTATION_ACCEPTANCE.md`。

Owner确认原资本市场设计意图：每省household aggregate illiquid wealth同时持有本省与外省企业资产，本省权重更高；household `rah`应由实际组合权重与destination returns得到。旧source的两个结构性bug已在successor中修复：
- 本省retained capital `(1-theta_i)*A_i*N_i`不再丢失；
- `rah`不再把destination `theta_j`重复作为权重。

K1保持household HJB为两资产，不增加31个asset states。定义完整`destination x origin`矩阵：
- `W_i=A_i*N_i`；
- 当前固定`theta_i=inter_prv_ratio_i`；
- `S[i,i]=1-theta_i`；
- `S[j,i]=theta_i*P[j,i]`，`j!=i`；
- `M_K[j,i]=S[j,i]*W_i`；
- `Kprivate_j=sum_i M_K[j,i]`；
- `rah_i=sum_j S[j,i]*portfolio_return_j`。

`P[j,i]`由foreign-only stable softmax生成，输入为caller-provided distance/friction score与lagged/completed-iteration return score。same-turn `firm -> return -> share -> capital -> firm`反馈被禁止。`beta_distance`、`beta_return`无默认值，未识别。

## 理论方向：nested Scheme B
最终不是单层`S_ji proportional to return`，而是嵌套结构：

第一层：home vs foreign；
第二层：conditional on foreign，决定destination shares。

K1只做第二层，固定`theta_i`。K2未来才内生化home-vs-foreign margin，使`theta_i`最终成为`1-S[i,i]`的模型结果。

这个结构吸收multi-country portfolio allocation、financial gravity和dynamic spatial GE的核心思想：return、home bias、distance/information/transaction frictions共同决定bilateral holdings；存在friction时各省长期return可以不同，不要求无摩擦完全均等化。

但本项目不直接照搬高维portfolio perturbation或31资产HJB；portfolio/intermediary layer必须保持计算成本远低于household block。

## lagged-return numerical timing
Owner明确赞成lagged update，原因是过去same-turn price feedback真实造成过震荡不收敛。冻结：

`allocation iteration n+1 uses return score from completed iteration n`。

推荐outer fixed-point顺序：
1. household使用上一完整iteration价格/组合收益；
2. household得到`A_i`；
3. capital network使用当前`W_i=A_iN_i`和上一完整iteration return score分配private capital；
4. firm计算新的`ra0/ra/wjt`；
5. 新return只影响下一iteration portfolio attractiveness。

这是steady-state numerical timing，不是calendar-time即时调整假设。

## K1后续分阶段路线
由于单次多省稳态成本可能超过2小时，所有science必须一次只增加一个反馈机制。

### K1A：repaired baseline / space-only
- 固定`theta_i`；
- repaired equal foreign shares或预注册的pure-distance shares；
- 不加入return feedback；
- source-faithful labor继续冻结；
- 重新验证K1 private K + C1 GovInv + raw-ra。

### K1B：lagged-return endogenous foreign destinations
- 仍固定`theta_i`；
- foreign shares加入lagged return attractiveness；
- 不允许same-turn反馈；
- 独立比较对K、rah、ra0、C1 residual和convergence path的增量影响。

### K2：endogenous home-vs-foreign margin
- 仅在K1A/K1B通过后进入；
- 让`theta_i`自身成为模型内生对象；
- 可考虑嵌套home/foreign choice或frictional inclusive-value机制；
- 具体效用/摩擦/系数尚未冻结。

## distance/friction 数据路线
下一Owner gate必须先冻结dimensionless score mapping。

优先候选：

### D0：pure geographic distance
第一版最简单、最易解释，适合K1A。

### D1：geographic + economic distance
例如：
`distance_econ_ij = abs(log(pgdp_i)-log(pgdp_j))`。

pgdp difference应解释为friction/similarity，不应同时承担destination market-size attractiveness。目的省GDP/market size如未来加入，应作为独立变量。

更复杂的trade linkage、industry similarity、financial-center variables未来再加入，第一轮不宜同时堆叠。

## return attractiveness 与 payoff return
必须继续区分两类对象：
- `lagged_return_score_by_destination`：决定capital destination attractiveness；
- `portfolio_return_by_destination`：用于`rah`收益聚合。

clipped`ra`不能自动作为score，因为`.02/.09`已被识别为historical numerical safeguard，且旧C1 path中30/31 raw`ra0`高于`.09`；直接使用clipped return会把省际差异压平。

科学冻结前至少比较：
- lagged raw `ra0`；
- relative raw return；
- cross-sectional standardized return；
- smoothed / expected return。

不得观察trajectory后再选normalization。

## price/return与capital network的关系
此前C1旧capital allocation下turn25 30/31 raw `ra0`高于`.09`，主来源是`rk=mt*alpha*Y/K`；`.02/.09`仍只是historical numerical safeguard。K1修复会显著改变private capital分布与firm Y/K，所以不要在K1 integration前直接扩大return bounds。K1科学运行后必须重新分解raw-return pressure。

## labor route
origin-preserving bilateral labor normalization successor已接受，但尚未与K1同时进入scientific path。为了归因，第一次K1 bounded integration继续冻结source-faithful labor；资本网络验证后再单独测试normalized labor stack。

最终理论目标可形成双内生空间通道：
- origin labor stock × destination labor shares；
- origin private wealth × destination capital portfolio shares。

两者都保留完整destination-by-origin flow matrix，但经济signal与frictions不同。

## KFE路线
clean/source-free KFE方法学合同已稳定：HJB/KFE共享同一backward generator `Q`，forward=`Q.T`，row sums/off-diagonal/closed recurrent class/mass-first stationary solve均有gate。

但当前corrected-2018 empirical finite-box upper-b leakage + MATLAB-style pinning仍是独立blocker，不能因K1修复而宣称KFE已解决。未来production acceptance仍需单独boundary/source-free KFE closure decision。

K1本身位于household solve之后，不直接修改单省KFE算法；但通过下一iteration的`rah`与firm prices间接改变HJB policy和KFE generator。

## 数据合同
corrected-2018继续使用actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM capital、`delta_pim=.096`、`alpha=.7380939146868483`、MU=`10万元`、NU=`100 persons`、same-year Zt0。`beta_a=1`仍是`SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`。

## 当前路线节点
当前没有active Builder task。下一步不是立即跑模型，而是Owner/Reviewer在新会话冻结K1 economic scoring/data contract。冻结后再发布exact task。

建议大路线：
K1 scoring/data freeze → zero-science 2018 distance/score mapping receipt → K1A static matrix receipt → 单条bounded K1A integration trajectory → re-evaluate private K/C1 GovInv/raw-ra → K1B lagged-return endogenous shares → K2 endogenous home-vs-foreign margin → normalized labor stack → KFE production closure → bounded steady state → annual/GE/IRF/Results gates。
