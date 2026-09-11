# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-11。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前阶段
当前已从“复刻原MATLAB mixed-year流程”推进到“修正资本侧经济结构并建立可审计 successor route”。Results=`FALSE`。

已完成并接受的关键节点：
1. MATLAB/Python two-asset HA parity P1–P4；
2. corrected-2018 runtime binding与raw-NBS Track-A数据合同；
3. HJB nonconvergence finite continuation contract；
4. C1 residual public-asset GovInv定义与25-turn bounded validation；
5. origin-preserving bilateral labor normalization zero-science successor；
6. price/numeraire/raw-ra forensic；
7. K1 bilateral private-capital network zero-science implementation。

## C1 GovInv authority
GovInv解释为不可直接观测的政府/公共生产性资产 residual：
`GovInv=max(Ktarget-Kprivate,0)`。
历史C0 clipped-return `0.9/1.1` controller已证明会重新制造GovInv overshoot。C1 bounded path中775/775 capital accounting assertions通过，turn20-25 total-K/Ktarget固定为1，资本数量/GovInv level divergence不再是同一优先级的直接blocker。

## K1 bilateral capital network：当前新冻结点
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

## K1下一路线
在任何科学trajectory前先冻结：
1. distance/friction数据对象与dimensionless normalization；
2. lagged-return attractiveness signal及normalization；
3. `beta_distance`与`beta_return`的预注册值/识别协议；
4. portfolio payoff return概念；
5. 是否需要partial adjustment/smoothing；
6. 第一轮保持`theta_i`固定，K2再内生化home-vs-foreign margin。

推荐分阶段：
- K1A：先用固定`theta_i` + repaired equal/space-only foreign shares验证capital/rah accounting；
- K1B：再加入lagged-return tilt；
- K2：最后才让`theta_i`本身内生化。

由于单次多省稳态成本可能超过2小时，所有参数和score mapping应先做zero-science/static proof与预注册，避免边跑边调。

## price/return与capital network的关系
此前C1旧capital allocation下turn25 30/31 raw `ra0`高于`.09`，主来源是`rk=mt*alpha*Y/K`；`.02/.09`仍只是historical numerical safeguard。K1修复会显著改变private capital分布与firm Y/K，所以不要在K1 integration前直接扩大return bounds。K1科学运行后必须重新分解raw-return pressure。

## labor route
origin-preserving bilateral labor normalization successor已接受，但尚未与K1同时进入scientific path。为了归因，第一次K1 bounded integration建议继续冻结source-faithful labor；资本网络验证后再单独测试normalized labor stack。

## KFE路线
clean/source-free KFE方法学合同已稳定：HJB/KFE共享同一backward generator `Q`，forward=`Q.T`，row sums/off-diagonal/closed recurrent class/mass-first stationary solve均有gate。

但当前corrected-2018 empirical finite-box upper-b leakage + MATLAB-style pinning仍是独立blocker，不能因K1修复而宣称KFE已解决。未来production acceptance仍需单独boundary/source-free KFE closure decision。

## 数据合同
corrected-2018继续使用actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM capital、`delta_pim=.096`、`alpha=.7380939146868483`、MU=`10万元`、NU=`100 persons`、same-year Zt0。`beta_a=1`仍是`SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`。

## 当前路线节点
当前没有active Builder task。下一步不是立即跑模型，而是Owner/Reviewer在新会话冻结K1 economic scoring/data contract。冻结后再发布exact task。

后续大路线：
K1 parameter/data freeze → zero-science mapping/fixture → 单条bounded K1 integration trajectory → re-evaluate private K/C1 GovInv/raw-ra → K1 lagged-return endogenous shares → K2 endogenous home-vs-foreign margin → normalized labor stack → KFE production closure → bounded steady state → annual/GE/IRF/Results gates。
