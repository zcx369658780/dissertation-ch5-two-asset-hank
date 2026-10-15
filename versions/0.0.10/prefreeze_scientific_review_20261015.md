# V0.0.10：Owner科学裁决与实施合同冻结前审议（2026-10-15）

**性质**：Astra治理/科学审议记录，非代码提交、非已冻结实施合同、非研究运行授权。  
**终态**：`READY_FOR_V010_IMPLEMENTATION_CONTRACT_FREEZE__SCIENCE_CHOICES_RESOLVED__NO_EXECUTION_AUTHORIZED`。  
**本次 Owner 已确定两项**：恢复原MATLAB收益边界 GovInv 自适应；目的地工资税一次扣除并按总量接入财政。不再就这两项重复问Owner。

## 固定来源及权限
- 治理接续源 HEAD：`af5fd206d7ffbccdfeb40262a8a0e096355f8774`，tree：`4a82337c623f2db228038826a2aa58e262fd54e2`（此处是**签发前读值**，不是往后动态 HEAD）。
- V010 SOURCE_ONLY 任务：`0320916bd2447d1846099cc90e52bd92c920ebb1`，task blob `d4aacdafe5f4d0248745f8754088afd83fc1c6d2`。Codex集中报告已获本会话Astra**有限SOURCE_ONLY接受**：不等于运行、数值稳态、GE、IRF、Results接受。
- 拟定代码父基线：`a1db8c114dec0ab69d69a5576e153a7f868cba0e`（tree `4a118642da526d6bf2dfb65a1130f4d59d371374`）；仅拟冻结，`NEXT_MAINLINE_BASELINE=UNSELECTED`直到实施合同发布和保护身份核验。
- 审议核对了原MATLAB ZIP的`HANK_mp_1eq.m`、`HANK_mp_1turn.m`、`HANK_firm.m`、`Lt_seperate.m`、`wage_caculate.m`、`mpHANK_shock_2000.m`、`HANK_2ASSETS_HJB.m`，论文5.2.7/5.3及固定Python核心源码。没有科研求解/pytest/MATLAB/真实C8/B3或原dirty改动。

## Owner O1：GovInv原有界乘数控制正式采用
校准阶段且外层尚未收敛、`max |KN/tKN-1|<0.1`才允许更新（原 `HANK_mp_1eq.m:42-61`）：
1. `ra_used_i<ramin_i+0.02` → `GovInv_next_i=0.9*GovInv_i`。
2. 否则 `ra_used_i>ramax_i-0.02` → `GovInv_next_i=1.1*GovInv_i`。
3. 其余不变；记录触边、初始值、前后值、raw/used及迭代信息，不静默clip、不补新底板或改系数。
原 `Zt_next=Ytarget K^-alpha L^(alpha-1)` 且目标误差超1%的校准角色继续保留，迭代顺序仍由旧有界手动控制器决定。GovInv 属于企业 `Kt=Kprivate+GovInv` 的国有资本；不等同经常性政府购买G。
**C1** `GovInv=max(Ktarget-Kprivate,0)` 仅保留历史已接受证据及实验代码，不在新主线中被调用或覆盖GovInv，旧验收不追改。

## Owner O2：目的地工资税仅一次
来源`i`、目的地`j`：
`q[j,i]=w_gross[j]*(1-tau[j]-sigma[j,i])`；税与迁移成本按原**加法楔**，不擅自改为乘法楔。双边劳动、来源综合工资和财政均使用目的地税率`tau[j]`，不能混入来源税`tau[i]`。
`w_eff[i]`若已经由`q[j,i]`合成，则进入HA劳动FOC/收入时不得再乘`(1-tau[i])`。允许HA内部标注`wages=w_eff,tau_HA=0`作为*无第二次扣税的显式参数化*，必须由解析及focused oracle验证；真实`tau[j]`继续存在于省级经济状态、劳动配置和工资税收入，绝非经济免税。
税基须对应工资支付/生产使用的同一目的地有效劳动：
`WageTax[j]=tau[j]*w_gross[j]*L_firm[j]`，
`L_firm[j]=sum_i Lt_mat[j,i]`（目的行、来源列）。
如果原平均`Ct_i`的`Lt_seperate`劳动重构与`N_i*Lt_HA_i`或完整异质性政策积分不一致，要单列诊断，不能无证据宣称劳动市场经济出清或擅改原数学方法。

## 财政总量恒等（不是新市场闭合）
`GovInc[j]=Corptax[j]+WageTax[j]+N[j]*AtTax[j]+GovInv[j]*ra_used[j]-N[j]*Tt[j]`。
`AtTax,Tt,Bt,Ct,At,Lt_HA`为来源家庭人均/分布聚合量；`N`是当前人口/人均桥，不能使用`N=P/3`。企业`Corptax`、`GovInv`及工资税已经是总量，不再次乘N。原`Corptax`还包含价格截断补偿，须注明税与边界账区别。
`GovSurplus=sum_j GovInc[j]-sum_i Bt[i]*rb[i]*N[i]`仅为诊断，不增加`Bt=Bgov`或内生T等方程。资产收益沿用已接受same-S、raw-ra0/lagged时序，GovInv公共资本回报单独核算。财政单位尚需工程测试证明，不能只看有限值就称财政GE通过。

## 经源证确定的最低修正
- `phi[j,i]=1+0.3*(pgdp_i-pgdp_j)/(pgdp_i+pgdp_j)`，高人均GDP目的地更低劳动厌恶；原`HANK_mp_1turn.m:10`符号反，且用`Y/Lt`冒充人均产出。依Owner及论文使用**注明年度的真实人均GDP参考**作为本年校准与冲击一致的偏好来源；受保护真实数据没有本版读取许可。V009人工1:2不可当现实31省输入。
- 分列家庭来源`Lt_HA`、双边`Lt_mat`、当前目的地`Lt_firm`、上一轮`Lt_firm_prev`和冻结基线`Lt_firm_ss`。原Python `one_turn.py:223` 将家庭Lt覆盖在NKPC上一期firm劳动是错账。
- 原`HANK_mp_1turn.m:27`在for结束后才写`results{i}.Lt_mat`，仅最后一省持有该字段；主线单轮应以整体矩阵结果避免这种错位。
- K1同S本地资本留存与`rah_i=sum_j S[j,i]ra0_j`保留，收益吸引度只用**上一完整轮次**，不用原foreign-only分配器，也不让当前回报同轮反向影响当前份额。
- HA使用已接受corrected selector、Q、严格HJB双门（B≤1e-8,D≤1e-7）、最多52次halving、唯一闭类source-free KFE、概率质量及五字段聚合，不能直接把历史seed锁定的诊断runner冒充通用新主线。
- 原控制器的退出不直接保证每省`abs(Y/Ytarget-1)≤0.01`；新主线应分账`OUTER_ITERATION_CONVERGED`与`TARGET_CALIBRATION_VERIFIED`，且后者要求冻结GovInv/Zt独立回读合格，否则科学稳态资格FAIL_CLOSED，不许冻结阶段继续调参。
- 冲击阶段严格与校准分离。原`mpHANK_shock_2000.m:46`向`HANK_mp_1turn`传`1`，实际走`HANK_firm.m:34-35`的lagged-NKPC分支（而非代码另一条ss-reference分支）；先如实复现、记录含义并对零冲击及滞后状态设oracle。冲击每期以稳态重置被指定外生量并施加shock，其他状态递推；不运行GovInv/Zt自适应，不默认改造为前瞻动态路径。

## 集中实施拟冻结条件
继续使用原HA黑箱 → 单轮 → bounded outer → 原递推冲击；不采用V008/V009人工体系、Newton、人工债券财政闭合或新增工作流。拟定父提交`a1db8c11...`；新增窄的HA主线入口及response入口，定点修复`one_turn/stationary_runtime/steady_state/firm/wage/migration_labor/fiscal_diagnostics`与4份聚焦tests、1个集中validator；不改原dirty或corrected历史runner。
可参考Codex**待批准**的8小时、6次focused pytest进程、4个science driver进程、26次HA/KFE总尝试、每HA最多100次value更新/101次policy-map、400000次scalar-root/HA、全局10400000次root、256MiB存储。**这些全部不是当前已发布的新预算**；冻结前必须准确列selector总上限、synthetic全输入与V0身份、代码白名单、temp/candidate-view/日志/fixture存储口径、停止规则与最终树验证。任何科学程序只有另行签发实施许可才可以开始。
建议一次集中Codex实施交付：受界corrected HA绑定→非对称2省stub单轮→有限双省有界外层→冻结后无校准回读→短零/非零原递推响应；真实31省、2017/2018/C8、20期正式IRF另行授权。不得以局部PASS推断整体GE/Results。

## 状态和保护
本审议结束SOURCE_ONLY选型争议及两项Owner经济选择，但**并非版本实施冻结、代码候选接受或科研预算**。原本地8 dirty、index、external common-dir、untracked/ignored、B3与V008/V009历史证据一律不触。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、真实C8 A–D REQUEST_ONLY；V011 NOT_STARTED。
