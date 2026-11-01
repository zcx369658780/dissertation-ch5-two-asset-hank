# TEMP31 初始化受界调试：Owner授权与固定边界 · 2026-11-01

STATUS=OWNER_APPROVED__FINITE_CUMULATIVE_BUDGET__NOT_A_GENERAL_MODEL_RUN_LICENSE
GOVERNANCE_AUTHORIZATION_PARENT=46aaa5c9c8b531ac18f8ea8219dcaa0645f3ce60
OWNER_EXACT_STATEMENT=可以我同意，这里附带之前的结论：1、HA模块的grid参数不允许更改，视为黑箱。2、ra rb wt等价格变量的范围，参考你之前进行过的稳态测试选择。

本决定承接对话中的明确10进程调试提案。与之前两次分别获准、已消耗的单次尝试分开登记；新预算只有一份，跨会话累计，不因重新启动、文档提交或改验证器而恢复。

## 当前许可和计数

- 仅当前独立TEMP31资产乘收益率初始化函数及其验证器；源candidate=1cdebe761dc4406a83093884ae15f0377d891b8f，initializer Blob=9a4b5f1a54c5b5f1a88317f8edfa2b52fd253955，不改科学源码。
- 新验证worker累计最多10个，每个墙钟最多30秒，包含导入/初始化/求根和其限定本地元数据辅助命令。每worker初始化最多1次、劳动根最多8次、Brent每根maxiter100；总初始化最多10次、根最多80次。到达目标后停止，不为用完预算重复运行。
- 验证器误拦截、导入路径、日志/计数/输出格式等工程问题可由Codex在剩余预算内修复重试，逐次保留旧版本、claim、结果和实际计数。stdlib-only准备/记录进程不是科学worker，不能借此导入/执行科学代码规避计数。
- 本机信息读取及依赖库限定的Windows版本查询允许；本轮执行器只例外允许标准库platform._syscmd_ver来源的系统cmd.exe /c ver，一次/worker。网络和任意其他子进程仍被阻断，不改Desktop/CUA/全局配置，不安装或升级依赖。
- 真实求根失败、非法消费、非有限值、非正资产差分、来源不符、保护/权限故障或预算耗尽，停止相应数值工作并报告；不得将这些失败改标成普通工程错误后自动重试。不得改经济公式/参数/网格/输入/根区间/容差/科学标准救通过。
- HA/HJB/KFE/GE/IRF/policy/MATLAB/校准/真实数据运行均0。既有STOP、旧耗额、Results FALSE、保护基线与Owner科学接受权限不变。

## HA网格和本轮合成fixture

HA grid所有参数视为不可变黑箱，不改变节点数、上下界、节点值、轴顺序或切换矩阵。已认证R1–R3参考网格为(b,a,z)=(20,20,2)，b=[-2,5]、a=[0,10]、z=[0.8,1.3]，切换率1/3；这些是历史来源定位，不是新运行或重绑许可。生产HA参数仍按其对应冻结来源保持。

本轮沿用Owner同时同意的既有独立8格合成初始化fixture，SHA-256=cfc69df57a1f224a42dd92d33bb3bd38a786893456d71c7c32b293c45a8d7f23：b=[-.1,.1]、a=[0,1]、z=[.8,1.2]、零切换矩阵；rah=.09、rb=.02、rb_gap=.07、Tt=.1；净工资19沿numerical_bootstrap19语义。它不调用HA，不覆盖、缩减或替换生产HA网格，也不以此通过HA数值验收。V010_TOTAL_WEALTH_NUMERICAL_INITIAL_GUESS标签保持；不声明无成本提款/两账户均静止的政策可行性。

## 既有价格测试来源

| 固定来源 | 已测试价格点的分量包络 | 资格 |
|---|---|---|
| R1 c46a6e5e7220009450cceaf5d59e6e4db7c34f11；tasks/CH5_TEMP31_MATLAB800_THREE_PRICE_INTERIOR_HA_PILOT_R1_20261029/point_grid.json、result.md | rah .05–.09；rb .01–.03；净wt15.5–22；P0精确为(.09,.02,19) | 七点均执行；P0原HJB返回收敛，但KFE未认证，严格稳态候选0 |
| R2 ffb156712e56bd2fe24924ba40295858ad67e18f；tasks/CH5_TEMP31_MATLAB800_THREE_PRICE_LOCAL_DOMAIN_MAP_R2_20261030/point_grid.json、result.md | rah .045–.07；rb .015–.025；净wt17–21 | 十二点均执行；严格驻定认证点0 |
| R3 e194e44be4287cc447fdc3d83adb0dbd01bcb9d0；tasks/CH5_TEMP31_MATLAB800_PRICE_NEIGHBORHOOD_DISTRIBUTION_SWITCH_R3_20261030/point_grid.json、result.md | rah .05–.07；rb .0175–.025；净wt17–19.9 | 十二点均执行；严格驻定认证点0 |

合计已测点分量包络为rah [.045,.09]、rb [.01,.03]、净wt[15.5,22]，只是离散已测点集的描述，不是已认证连续三维可行域，不能据此随意组合或采纳实证价格。本轮固定(.09,.02,19)与R1 P0同点，故不需要改变合成价格。这里wt为家户净有效工资，不能直接替代企业毛工资或另扣一次税；其他价格/变量必须有各自来源，不能外推本表。

## 本轮工程判据

来源/调用计数一致；有限数组；消费为正；劳动根/c0/V0采用同一资源；两个资产轴V0差分为正；小端float64、F-order、只读及输入/输出身份封存。保留现有Brent xtol=rtol=1e-12和maxiter100；劳动根/FOC残差完整报告，本授权未新增FOC科学接受阈值。通过只表示固定合成初始化的受界工程数值检查，不表示稳态、生产接线、独立科学接受或Results。

实际预算与结论见唯一短状态和本地只追加执行账本；原始脚本、数组、完整日志均LOCAL_ONLY，公开只同步脱敏聚合结论。
