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
当前完整首轮 stagewise parity 尚需在统一阶段契约下完成复核；多轮传播及 2018 多省份 stationary parity 尚未由本次证据建立。
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

## 当前执行任务
`tasks/CH5_ASTRA_LOCAL_DOCUMENTATION_SYNC_2026_09_07.md`：
同步本地 repo 文档及 AGENTS，检查本仓库内生效的局部说明，发布简短同步报告。不得运行科学模型。
报告 `docs/CH5_ASTRA_LOCAL_DOCUMENTATION_SYNC_REPORT_2026_09_07.md` 若存在，应读取完成状态；不要重复执行已完成 task。

## 后续科学建议
在已冻结的 post-boundary 主比较口径下，以一个完整任务关闭首轮比较。先使用已有数组；仅确实缺失证据且新 task 有预算时才新调用。
当前没有发布该科学 successor。单纯命名决定无需 Owner 再审；真实方程或求解器选择仍需明确科学授权。

## 关键报告
- docs/CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_RAW_LIQUID_DERIVATIVE_BOUNDARY_ROOT_CAUSE_FORENSIC_REPORT.md
- docs/CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_POST_CALL_RESIDUAL_VECTORIZATION_REPAIR_AND_FIRST_ITERATION_STAGEWISE_REEXECUTION_REPORT.md
- docs/CH5_TWO_ASSET_HANK_MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_REPORT.md

旧 2026-07-22 R5 状态和 2026-08-21 R1A handoff 不再是启动指令。
