# Chapter 5 两资产 HANK 当前状态
更新：2026-09-07。唯一活动仓库：zcx369658780/dissertation-ch5-two-asset-hank。
最新已接受诊断提交：`b2d7a814039a585b696d8cc5079b8b9865017501`。这是证据锚点，不表示未来 live main 恒定。

## 当前结论与真正阻塞项
当前处于 MP4C 2018 安徽 call-725 的数值定位。
策略/算子任务已在 L3 仓库提交与发布报告范围接受：`COMMON_STATE_IMPLEMENTATION_OR_NUMERICAL_DIFFERENCE_LOCALIZED`。
M24、P24、M143_FINAL 各38/38；P32为36/38，首次超界为V1，随后停止统计量。P32 V1最大绝对差8.881784197001252e-14，296个坐标超界；不能因绝对值小而改判通过。
P32的M/RHS是容差内一致而非逐位一致；尚不能分离求解器算术与输入微差敏感性，不能认定公式缺陷或已证明病态。

第24步离散差异位于(5,19,0)，两条不同状态轨迹的导数比值跨过0.9阈值；各自共同状态复查均通过。算子极大值已追踪至两端未截断的transfer导数分母及平方调整成本。候选/阈值为保存输入的公式重建，不是独立runtime捕获。
两端存储算子均存在负非对角率和边界泄漏；M143_FINAL两端仍各有18个负非对角元、15个泄漏位置。这是尚未解决的legacy算子有效性问题，不能靠忠实重构、停止标志或小线性后向误差解除。
M143_FINAL单步距离分别2.6173063716328215e-11、2.6199042935104444e-11，输入态非线性缺陷范数均1.3374745755356798e-11；这不证明Python独立轨迹会到达该点。
独立轨迹仍是MATLAB143步收敛、Python500步不收敛，Python最后100步统计量约0.00862并持续切换；不宣称极限环。完整多轮parity、修正2018年度及Results均未因此接受。

## 验收证据与预算口径
验收：`docs/CH5_MP4C_CALL725_POLICY_OPERATOR_STABILITY_ACCEPTANCE.md`。
报告：`docs/CH5_MP4C_CALL725_POLICY_OPERATOR_STABILITY_REPORT.md`。
摘要：`reports/call725_policy_operator_stability_20260907/`。
候选相对原main a55019d4a6fe7b36eb783223e8b20dbc73fa59fb为直接子提交，20个新增文件均在允许范围，生产文件无变动。
本次Builder每端4次调用/更新/求解，重试0，下游0。Reviewer读取相关GitHub代码和摘要，未访问Windows原MAT/NPZ、未独立运行8项测试、未重新执行模型。8项通过及外部manifest核验按Builder发布证据记录，不升级为独立测试证明。Reviewer本轮新增科学调用0。

## 当前唯一执行任务
`tasks/CH5_MP4C_CALL725_FROZEN_LINEAR_SYSTEM_ATTRIBUTION.md`。
对已保存P32的两套M/RHS做两求解器交叉求解及固定二进制幂行缩放对照，分析残差、输入敏感性与浮点表示；不重算policy/HJB。
正常每端4次直接求解，共8次；每端至多1次符合条件的外部工程失败重试，硬上限及条件以task为准。HJB、长轨迹、KFE、GE、年度和动态调用0。发布不代表执行，生产实现不变。
策略/算子任务已完成，不从旧交接重新启动。即使线性比较全部通过，独立轨迹及算子有效性阻塞仍须另行解决。

## 已接受历史范围
- 原raw-vb的40/40差异已解释为保存阶段差异，早期证据锚点e98bfad214b0c85005fac2ce23b1e4585a20e634。主比较为边界覆盖后导数，不能据此修生产导数。
- 完整首轮：25e5db97a0239d956d572359db5835cec945962f，53/53通过，V1最大差3.9968028886505635e-15；当时Reviewer独立15项比较器测试通过，原Windows数组未直接重读。
- 多轮诊断：dedd0f8e5fa894b83c8b20e522d66893e7b6b377，第2步consumption首次超界、第3步更新V1超界、第4步输入V超界、第24步离散分叉；共同MATLAB第2步前状态38/38。每端2次调用，MATLAB144/Python501次更新求解，重试0；当时Reviewer独立4项可移植测试通过，另2项依赖Windows未重跑。
- household特定fixture以及MP0–MP3历史限定范围接受保留，不升级为所有经验输入有效。
每个历史任务预算均已消费，不因新规则/会话重置；前置曾有未持久化MATLAB调用，仍属于原任务记录。本节不是全项目累计调用统计。

## 年度来源口径
旧Owner指定protected runtime-cache口径：Python2009–2023共15/15年、465省年曾正式接受；corrected-2009跨语言接受只对其历史配置成立，不代表所有年份parity。
修正Owner-A资本/输入口径：2009–2022共14年，2009–2017及2019–2022共13年返回PASS，2018失败，完整修正覆盖未接受。2018曾捕获KFE contaminated-row singular/nonfinite异常。
不同初始化的历史实验曾两端500步内收敛，不能覆盖当前精确共同初始化的Python500步未收敛。此次诊断不重审或撤销不同配置的历史结果。
年度来源：
- docs/CH5_TWO_ASSET_HANK_MP4C_L3_FORMAL_2009_2023_ANNUAL_STATIONARY_COVERAGE_ACCEPTANCE_REPORT.md
- docs/CH5_TWO_ASSET_HANK_MP4C_OWNER_A_2009_2022_CORRECTED_8WORKER_ANNUAL_STATIONARY_REPORT.md
- docs/CH5_TWO_ASSET_HANK_MP4C_2018_OBSERVABILITY_REPAIR_SINGLE_RETRY_AND_2009_2022_COMPOSITE_ACCEPTANCE_REPORT.md
- docs/CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_MATLAB_SAME_ACTIVE_INPUT_HJB100_HJB500_AND_LEGACY_KFE_FRESH_EXECUTION_AFTER_PATH_RECERTIFICATION_REPORT.md

## 科学身份与工作目录
- protected HANK_2ASSETS_HJB.m SHA256：049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE。
- exports/matlab_faithful_two_asset_ha.py Git blob：9e7dc9556a2b76811e78f89999abecc045886106。
- authoritative initialization MAT SHA256：1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81。
- scalar binding SHA256：A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6。
本地文档同步d2f3e6e7cc21fffe8807f577ec2262bb77afdc07已接受，不重开。
工作目录D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001；原主checkout及其70个未跟踪文件保留，不能声称原目录已同步。
已存轨迹根D:\ProjectTemp\ch5-call725-multi-iteration-trajectory-20260907-001；四状态证据根D:\ProjectTemp\ch5-call725-policy-operator-stability-20260907-001。Reviewer未直接访问这些Windows目录。
Owner最终科学authority；Reviewer获持续任务发布及验收后纳入main授权。普通对话不自动启动本地Builder。正式Results eligibility仍为FALSE。
