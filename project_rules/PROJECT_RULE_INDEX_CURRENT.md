# Chapter 5 当前规则入口
更新：2026-09-09；治理修订仍为 `CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。读取AGENTS、此索引、当前状态和active exact task；旧R5/R1A及过期CURRENT只作历史。

当前状态：`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`。
路线：`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`。
交接：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_OFFICIAL_DATA_IDENTITY_CLOSURE.md`。
状态标记：`OFFICIAL_2018_DATA_IDENTITY_CLOSURE_ACTIVE__NO_SCIENCE_RUN`。

Builder默认`gpt-5.6-sol / medium`；host未暴露时不虚报实际模型，不改provider/global配置。

最新接受候选`6746565506eb953ea599536d3f745764d225ffef`已经实现V2 rolling-10y/same-year-Zt annual pre-model合同。当前任务只关闭2018数据身份：安徽2018 GDP、常住人口、固定资产投资及由冻结递推得到的模型资本存量。官方来源优先国家统计局与安徽省统计局/安徽统计年鉴；必须区分官方观测值与模型派生资本存量。

若官方数据与当前provisional workbook一致，形成可审计identity receipt；若不一致，仅生成versioned candidate correction package，不覆盖原Excel/MAT/cache/生产代码。投资序列口径不可比或官方数据缺失时停止并生成Owner人工下载清单，不自行插补。

本任务所有MATLAB、household/HJB/KFE、root/direct/eigen、firm/one-turn/controller、annual/GE/IRF/Results科学调用均为0。不调整GovInv/alpha，不扩大bmax，不切换PLM。Results eligibility=FALSE。
