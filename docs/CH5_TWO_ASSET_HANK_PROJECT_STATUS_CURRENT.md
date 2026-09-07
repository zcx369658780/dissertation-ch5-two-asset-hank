# Chapter 5 两资产 HANK 当前状态
更新：2026-09-07。科学证据 checkpoint：
`e98bfad214b0c85005fac2ce23b1e4585a20e634`。
该 SHA 是固定证据锚点，不表示未来 live main 永远不变。

## 当前结论
工作处于 MP4C 2018 安徽 call-725 的 MATLAB–Python HJB 对比诊断。
最新 forensic 已在仓库提交范围和报告层面核验（L3），支持：
`CALL725_RAW_VB_STAGE_NAMING_OR_PERSISTENCE_SEMANTICS_GAP_CONFIRMED__NO_PRODUCTION_CHANGE`。
Reviewer 未独立读取本地 Windows MAT/NPZ；报告中的外部文件哈希和运算结果属于已发布执行证据，不能说成本会话重新运行所得。

40 个 raw forward 差异全部在上界 b=5；40 个 raw backward 差异全部在下界 b=-2。MATLAB wrapper 将边界处理后数组称为 raw，Python wrapper 的 raw 在处理前保存。内部差分、边界公式和已保存的处理后导数比较支持阶段语义解释。
现有证据不支持为此修改生产 HJB 导数。旧“首个科学源差异”的解释由最新报告收窄为表示阶段差异。

## 已接受范围与尚未接受范围
历史已有两资产 household、算子、KFE/分布/聚合的特定 fixture 证据；MP1–MP3 的多省份结构步骤已在历史路线记录接受。这些范围不自动升级为当前经验配置通过。
完整首轮 stagewise parity 已接受：candidate 25e5db97a0239d956d572359db5835cec945962f，53/53通过，V1最大绝对差3.9968028886505635e-15；Reviewer独立运行15项比较器测试全部通过。原Windows数组未由Reviewer直接重读。多轮传播及2018多省份stationary parity仍未建立。
本次不重新裁决所有历史测试。KFE/GE/annual/dynamics/IRF/Results 均没有由治理迁移获得新授权。正式 Results eligibility 仍为 FALSE。

## 科学身份
- protected MATLAB HANK_2ASSETS_HJB.m SHA-256：
  `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- Python `exports/matlab_faithful_two_asset_ha.py` Git blob：
  `9e7dc9556a2b76811e78f89999abecc045886106`
- authoritative HJB100 initialization MAT SHA-256：
  `1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81`

## 预算口径
持久化首轮 pair 的 task ledger 是 MATLAB=1、Python=1、native probe=0、retry=0；最新 forensic 新增模型调用为0。
这不是全项目累计调用数。前置任务曾有一次未持久化的 MATLAB invocation，仍然属于其原任务已消费预算，不得从历史抹去。
治理更新和本地文档同步新增科学调用预算均为0。

## 文档同步与持续授权
本地同步报告在 commit `d2f3e6e7cc21fffe8807f577ec2262bb77afdc07` 已经 Reviewer L3 接受；报告原文现纳入 main。
已同步 worktree：`D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001`。
原主 checkout 的 70 个未跟踪文件和旧 HEAD 保留；不得声称原目录也已更新。Windows 文件/调用检查依据执行报告，Reviewer 未直接访问本机。
Owner 已授权验收后自动续发无实质决策的下一任务，并采用与风险匹配的审核和有限试错。

## 当前执行任务
`tasks/CH5_MP4C_CALL725_MULTI_ITERATION_TRAJECTORY.md`。
首轮闭合已完成且新增科学调用全部0，验收见 docs/CH5_MP4C_CALL725_FIRST_ITERATION_CLOSURE_ACCEPTANCE.md。
新任务：同初始化MAT的独立MATLAB/Python迭代轨迹；100步未收敛时允许外部诊断延续至500步，并可在最早差异处进行一次共同状态单步replay。生产100步上限不改。
每端最多1次轨迹、1次条件replay、1次符合条件的外部工程失败重试；实际条件、超时及更新次数上限仅按新task。KFE/GE/annual及后继科学调用仍为0。发布不代表已执行。

## 年度路线进度补充（两种来源口径不能混算）
- 旧 Owner 指定的 protected runtime cache 口径：历史正式接受 2009–2023 Python annual stationary 15/15 年通过、465 个省年结果；保留 corrected-2009 跨语言对比的历史接受范围，并非所有年份跨语言 parity。
- 后来的 Owner-A 修正资本/输入口径：2009–2022 共14年，2009–2017与2019–2022共13年返回 PASS，2018 process failure；完整14年 composite coverage 未接受。
- 2018 retry 已捕获 KFE contaminated-row singular/nonfinite 异常。call-725 历史 HJB100/500 对比中，MATLAB/Python 都呈100步未收敛、500上限内收敛，但迭代轨迹和聚合不同。首轮 staging 解释只关闭一个伪差异，不抹去后续真正差异。
这些是已读历史报告支持的范围，不是本次重新执行或新接受的年度结果。首轮已闭合；下一步定位多轮差异，再恢复修正口径的2018及年度覆盖。

## 关键报告
- docs/CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_RAW_LIQUID_DERIVATIVE_BOUNDARY_ROOT_CAUSE_FORENSIC_REPORT.md
- docs/CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_POST_CALL_RESIDUAL_VECTORIZATION_REPAIR_AND_FIRST_ITERATION_STAGEWISE_REEXECUTION_REPORT.md
- docs/CH5_TWO_ASSET_HANK_MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_REPORT.md

旧 2026-07-22 R5 状态和 2026-08-21 R1A handoff 不再是启动指令。

年度进度来源：
- docs/CH5_TWO_ASSET_HANK_MP4C_L3_FORMAL_2009_2023_ANNUAL_STATIONARY_COVERAGE_ACCEPTANCE_REPORT.md
- docs/CH5_TWO_ASSET_HANK_MP4C_OWNER_A_2009_2022_CORRECTED_8WORKER_ANNUAL_STATIONARY_REPORT.md
- docs/CH5_TWO_ASSET_HANK_MP4C_2018_OBSERVABILITY_REPAIR_SINGLE_RETRY_AND_2009_2022_COMPOSITE_ACCEPTANCE_REPORT.md
- docs/CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_MATLAB_SAME_ACTIVE_INPUT_HJB100_HJB500_AND_LEGACY_KFE_FRESH_EXECUTION_AFTER_PATH_RECERTIFICATION_REPORT.md
