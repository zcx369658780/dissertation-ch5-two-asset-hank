# Chapter 5 当前规则入口
更新：2026-09-09；治理修订仍为 `CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。读取AGENTS、此索引和当前状态；存在active exact task时再读task。旧R5/R1A及过期CURRENT只作历史。

当前状态：`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`。
路线：`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`。
交接：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`。
当前 active Builder task：无。
状态标记：`TEMPORAL_CONTRACT_IMPLEMENTATION_ACCEPTED__V2_ROLLING10Y_SAMEYEAR_ZT_STATIC_PASS__OFFICIAL_2018_DATA_STILL_BLOCKS_SCIENCE`。

Builder默认`gpt-5.6-sol / medium`；host未暴露时不虚报实际模型，不改provider/global配置。

最新接受候选`6746565506eb953ea599536d3f745764d225ffef`。Python annual/pre-model层已实现`CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`：`steady_year=2008+ii`；同年level row=`ii+9`；PLM保持rolling 10-year；Zt改为same-year row；V2 metadata/source-hash合同fail closed，旧无版本cache不得覆盖当前hash-bound PLM workbook。

2009和2018仅做静态pre-model构造，科学调用全部0。2018安徽provisional corrected输入为GDP 34010910.0、POP 607600.0、CAP 1357314108201.3684、alpha .772866243094144、same-year IND_Zt .0006934646534806338；这些仍未完成国家统计局/省年鉴官方身份闭合。

在2018官方数据身份关闭前：不启动新的household/HJB/KFE/firm/GE/annual科学运行，不调整GovInv/alpha速度，不继续扩大bmax，不把provisional workbook值升级为官方事实。生产网格仍I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。Results eligibility=FALSE。
