# V0.0.10 唯一ACTIVE：MATLAB-first Python集中实施与受限synthetic验证

**任务ID**：`V010_MATLAB_FIRST_MAINLINE_IMPLEMENTATION_AND_BOUNDED_SYNTHETIC_VALIDATION`。
**授权性质**：`ASTRA_ISSUED_FROZEN_IMPLEMENTATION_AND_EXPLICIT_BOUNDED_SYNTHETIC_SCIENCE`。
**执行角色**：Owner授权同路线继续；Codex 独立工作区实现/受界测试/集中交付；Astra最终独立验收。**不需要重新让Owner解释模型，也不授权V011。**

## 0 固定冻结权威：所有身份缺一即STOP
- 仓库：`zcx369658780/dissertation-ch5-two-asset-hank`；治理分支`migration/astra-workflow-20261012`。
- 冻结计划文件：`versions/0.0.10/plan.md`，唯一冻结**commit `bf091da33d59293f147d52c11580327d3ac2a85d`、tree `668fa20883a295ee9bd831a0c542d39e366bec43`、plan blob `85138d8859d53295262fe13bf5bc277bca95ed3f`**；本任务签发后的动态治理HEAD绝不能被当作修改版冻结合同。
- 人工输入：`versions/0.0.10/synthetic_fixture_v1.json`，冻结Git blob `40915658d93403cfc21b33a6b864b332b7857749`。新candidate路径`tests/fixtures/v010_mainline_synthetic_v1.json`要做**原字节复制**，计算Git blob identity必须相同；无法安全取得此源则STOP，不自行重新造数。
- 代码父commit`a1db8c114dec0ab69d69a5576e153a7f868cba0e`，tree`4a118642da526d6bf2dfb65a1130f4d59d371374`，sole parent `cc2b94679c2c57ec01483b615305cf4ea1739c61`。代码父是修复起点，非已通过真实GE。
- 同一V010此前SOURCE_ONLY任务及验收已结束；Owner已确定GovInv原收益边界0.9/1.1、目的地税一次扣、财政量纲，详见`versions/0.0.10/prefreeze_scientific_review_20261015.md`；不重开Newton/C1选择，不启动V011。

## 1 目标：严格执行被冻结合同，不发散
依据冻结`plan.md`第1–3节的完整方程、接口和仅15条修改/新增白名单，完成：
1. 独立通用的corrected HA条件稳态入口（禁止历史锁死seed的runner接入），保留数学既有接受，返回严格HJB双门、合法Q/KFE/五字段。
2. 更正phi来源减目的pgdp、目的地工资税及只扣一次、双边labor矩阵和 household/firm/lagged状态分账；量纲和财政真实源字段不能重复乘人口。
3. K1本地保留＋foreign资本同`S`数量和raw-ra0 payoff、lagged吸引度；旧foreign-only及C1不得在新主线路径实际生效。
4. 原GovInv/Zt有界手动外层、阻尼和退出；`OUTER_ITERATION_CONVERGED`必须和冻结后`TARGET_CALIBRATION_VERIFIED`分开，GDP目标≤1%不能被假设为自动满足。
5. 仅在前置合格时，原20期目标中的**3期短synthetic**零冲击和1%TFP递推接口；保持原shock入口实际`steady_state=1`对应的lagged-NKPC分支，无外层重复校准，无前瞻路径替代。

## 2 执行许可与会计
正式许可只对冻结plan第2、4–6节的**两匿名省synthetic fixture、可核V0构造、准确允许文件及新预算**生效。允许在独立工作区编写白名单代码、6次focused pytest进程、最多4个science driver进程和最多26次省级HA/KFE尝试（2+10+2+12阶段专用，不可跨阶段洗账）。每HA至多100 value updates、101 maps、400000 scalar roots（包括V0初始化每格root）；全局最多2,100,800 policy cells及10,400,000 roots；总时限8h；每pytest进程600秒；增量科学证据≤256MiB、独立clone≤2GiB；RSS目标512MiB。**本新预算开始时间/余量/消耗必须留回执，旧耗尽预算永不恢复。**

先用人工/stub的focused oracle无科学调用证税率、phi、同S、收入/状态、GovInv高低边界；之后按合同前置允许递进调用。生成V0和省级初始输入必须在首个HJB调用之前记录数组哈希、软件版本及F-order；root、selector、失败的科学尝试全计数。若环境无solver纯组件接口，允许只在新文件里复用数学纯函数形成通用HA wrapper；不扩至corrected历史runner源或改变经济公式。后续实验若不合格，诚实STOP，不增加迭代/预算或调参救PASS。

## 3 保护和Git
原历史tree `D:\ProjectTemp\c5k1bturn56`及8项dirty、index、common-dir、untracked/ignored、同步镜像全部不可写、重置、stash、worktree add；也不得读取protected C8/2017/2018/B3及旧V009失败数组。建立独立非共享Git对象的安全clone/sparse工作区，从固定父提交开始；若缺Git对象/认证或独立clone失败就STOP，不在原tree运行改写性git。候选分支可最多一次non-force push（只有白名单代码/测试及脱敏数据，禁止main合并）；不写治理分支。GitHub commit/tree的回读独立于私有本地回执等级。

严格按V1.2前置成功才进行依赖下游、UTF-8 LF、最终candidate tree隔离 focused 验证；保留原失败真实账。敏感结果只保留LOCAL_ONLY，公开短manifest不能伪称网页直接重跑。若超许可路径、价格/方程新科学取舍、权限冲突、无法取得人工fixture字节、旧8 dirty保护风险、预算触限，立即STOP，报告实际状态，不自动派下一轮。

## 4 集中交付
一个`V010_MATLAB_FIRST_MAINLINE_IMPLEMENTATION_RESULT`，列签发任务及冻结plan identity、candidate SHA/tree/准确diff、模块加载身份、人工fixture/V0 SHA、所有tests/科学尝试和源/目标判断、结果证据等级、时间/进程/RSS/储存账、是否到达冻结验证/短响应、未验证项和保护类别。交付即：`WAIT_ASTRA_V010_IMPLEMENTATION_REVIEW / STOP`。

无论engineering通过还是科学失败，A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE；真实C8 A–D REQUEST_ONLY、V011 NOT_STARTED。
