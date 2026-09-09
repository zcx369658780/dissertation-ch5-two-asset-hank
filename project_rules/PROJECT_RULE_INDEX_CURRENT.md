# Chapter 5 当前规则入口
更新：2026-09-09；治理修订仍为 `CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。读取 AGENTS、此索引、当前状态和 active exact task；旧R5/R1A及过期CURRENT只作历史。

当前状态：`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`。
路线：`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`。
交接：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_RAW_DATA_AND_INTERPOLATION_AUDIT.md`。
状态标记：`2018_RAW_DATA_AND_INTERPOLATION_AUDIT_ACTIVE__BMAX_ROUTE_DEFERRED`。

Builder默认 `gpt-5.6-sol / medium`；实际host未暴露时不虚报已验证模型，不改provider/global配置。

最新接受的b域扩展事实继续有效，但Owner已明确停止继续搜索更大`bmax`：其历史经验是实际收敛稳态中的`Bt`基本在0附近，且低收益流动资产不应通过不断增大上界来解释异常路径；生产网格仍冻结为I20,b[-2,5]，J20,a[0,10]，保持`amax>bmax`的设计。

新任务优先审计原始数据、缺失值填充/插值链、年份/省份/单位映射和2018安徽最终消费数据。原始Excel/MAT/Matlab源只读；新HJB/KFE/firm/GE/年度/MATLAB调用全部0。若发现物质性数据问题，先报告并等待Owner决定官方修正；若未发现，下一科学方向是外层收敛/适应算法（如高收益状态下GovInv调整速度），不是继续扩箱。

Results eligibility=FALSE。
