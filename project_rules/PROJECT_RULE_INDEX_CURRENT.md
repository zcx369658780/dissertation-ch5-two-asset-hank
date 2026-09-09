# Chapter 5 当前规则入口
更新：2026-09-09；治理修订仍为 `CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。读取AGENTS、此索引、当前状态和active exact task；旧R5/R1A及过期CURRENT只作历史。

当前状态：`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`。
路线：`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`。
交接：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_TEMPORAL_CONTRACT_MINIMAL_IMPLEMENTATION.md`。
状态标记：`TEMPORAL_CONTRACT_MINIMAL_IMPLEMENTATION_ACTIVE__ROLLING_10Y_PLM_FROZEN`。

Builder默认`gpt-5.6-sol / medium`；host未暴露时不虚报实际模型，不改provider/global配置。

已冻结Owner科学合同：`steady_year=2008+ii`；同年水平量一基row=`ii+9`；PLM estimator保持；PLM使用最近10年rolling window `steady_year-9:steady_year`；2009=2000–2009、2018=2009–2018、2023=2014–2023。固定2020 Zt仅为`LIKELY_LEGACY_FIXED_YEAR_ANCHOR`，本次实现按Owner批准方向改为同年level row，公式不变。

当前task只实现Python annual/pre-model时间合同、same-year Zt与版本化metadata/stale-cache拒绝，并只读生成2009/2018 pre-model输入摘要。科学模型调用全部0；原MATLAB/Excel/MAT/PLM workbook只读，MATLAB仅输出patch spec，不实际修改。

不继续扩大bmax、不调整GovInv/alpha速度、不切换PLM估计器、不运行household/HJB/KFE/firm/one-turn/annual/GE/IRF/Results。生产网格仍I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。前序2018官方数据核验请求继续开放，Results eligibility=FALSE。
