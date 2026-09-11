# Chapter 5 两资产重构路线与科学边界
更新：2026-09-11；轻量治理保持有效。

## 唯一活动路线
唯一活动模型仓库是`zcx369658780/dissertation-ch5-two-asset-hank`。旧one-asset R5只读历史，不保留其科学runtime为当前依赖；`deep-learning-hank`是另一个项目。

当前是MATLAB-faithful两资产、多省份重构，但已经进入“source-faithful reference 与 economically redesigned successor 并存”的阶段。忠实复现不等于legacy经济公式正确；忠实实现、经济合理性、数值有效性和论文Results必须分开判断，不能静默把reference替换为redesign。

当前资本网络科学设计冻结稿：
`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。

## K1/K2 资本网络路线
Owner已确认legacy private-capital network存在两项结构性遗漏：本省retained capital漏计，以及`rah`外省收益中destination `theta_j`残留二次权重。legacy `capital_allocation.py`必须继续保留用于parity，但不得自动成为新的经济authority。

新的经济successor采用两资产household + post-household bilateral provincial portfolio layer，不增加31个household asset states。K1固定`theta_i=inter_prv_ratio_i`作为origin总外投比例，恢复home share `1-theta_i`，foreign destinations由完整`destination x origin`矩阵分配；capital quantities与household `rah`必须使用同一portfolio matrix并满足origin/national conservation。K2未来才讨论让`theta_i`内生化。

Owner过去真实尝试三资产多省HANK但计算成本显著上升，因此本路线的硬约束之一是：不得为了“理论完整”重新引入不可计算的31资产HJB，除非Owner重新裁决。

capital-share update必须使用lagged/completed-iteration return attractiveness，禁止same-turn `firm -> return -> share -> K -> firm`反馈。该时序是steady-state numerical fixed-point rule。

后续重大顺序：K1A repaired equal/space-only → K1B lagged-return endogenous foreign shares → K2 endogenous home-vs-foreign margin。第一次K1 scientific integration继续冻结source-faithful labor，避免capital与labor同时变化。

## 参数与科学运行边界
在任何新的2-hour+多省稳态/trajectory前，必须先冻结：
- distance/friction data mapping与dimensionless normalization；
- lagged-return score来源/period/normalization；
- `beta_distance`、`beta_return`；
- payoff return concept；
- smoothing/partial adjustment是否存在；
- K1A/K1B顺序和K2进入条件。

不得根据trajectory表现事后选择这些对象，也不得从convergence反推科学参数。

## C1 GovInv 联合边界
GovInv已冻结为不可直接观测政府/公共生产性资产 residual：`GovInv=max(Ktarget-Kprivate,0)`。该定义不是return controller。此前C1 bounded path有效，但使用legacy Kprivate；K1改变private-capital accounting后必须重新联合验证C1，不得直接沿用旧量级。

## price/return 边界
历史return bounds `[.02,.09]`目前只属`EMPIRICAL_NUMERICAL_SAFEGUARD`；wage bounds `[.8,1.3]`绝对经济单位仍未闭合。旧C1路径raw-ra upper pressure主要来自`mt*alpha*Y/K`。K1改变Kprivate/Y/K后必须重新分解，不得现在直接放宽/删除bounds。

## KFE边界
clean/source-free KFE方法学已有稳定合同：共享backward generator `Q`、forward=`Q.T`、row-sum/off-diagonal/closed-class/mass-first stationary checks。当前corrected-2018 empirical finite-box upper-b leakage + MATLAB-style pinning仍是独立scientific blocker。K1不直接修改KFE数学实现，只会通过下一iteration prices/rah间接改变其input generator。

## 比较阶段与标准
历史call-725液体导数、HJB/KFE parity等已完成gate继续保留为历史authority，不从旧task重新执行。类别/mask、shape/order精确一致；同输入同阶段连续值按冻结tolerance比较；不得观察结果后调阈值。稀疏支持不得用epsilon pruning隐藏差异。

## 后续科学与Results
单个bounded diagnostic通过不代表稳态、GE、年度、动态、福利或Results通过。新阶段按明确范围、前提和预算执行；昂贵science必须优先做zero-science static proof与参数预注册。

冲击law、动态时序、初末条件、校准和政策解释等实质选择由Owner决定。MATLAB命名IRF的顺序比较静态不当作已验证动态HANK。

正式Results、福利和政策claim必须绑定已接受输出及独立Results gate；诊断表和静态counterfactual不得误标论文结果。
