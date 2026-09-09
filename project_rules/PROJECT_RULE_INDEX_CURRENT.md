# Chapter 5 当前规则入口
更新：2026-09-09；治理修订仍为 `CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。读取AGENTS、此索引、当前状态和active exact task；旧R5/R1A及过期CURRENT只作历史。

当前状态：`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`。
路线：`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`。
交接：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_TEMPORAL_CONTRACT_AND_ZT_LEGACY_AUDIT.md`。
状态标记：`TEMPORAL_CONTRACT_AND_ZT_LEGACY_AUDIT_ACTIVE__PLM_PRESERVED`。

Builder默认`gpt-5.6-sol / medium`；host未暴露时不虚报实际模型，不改provider/global配置。

最新接受数据审计`f850937ccb7b11b835ce5e45b9819ee25412ad03`证明2018标签混用2009水平量、vintage19 alpha和2020水平锚定Zt。Owner随后澄清原意：用2000–2009样本估计2009稳态技术对象，后续年度沿用截至该年的估计；PLM是既有比较中效果最好的方法，当前保留PLM；固定2020行Zt疑似遗留代码。

当前task只做零模型调用的时间合同/legacy审计：验证`steady_year=2008+ii`、同年水平量是否应为`ii+9`行、PLM vintage是否已与年度一致、Zt固定2020行是否无依据，并给出最小patch plan。不得执行patch或模型，不切换估计方法。

不继续扩大bmax，不调整alpha/GovInv，不重跑年度/多省份/GE/Results。生产网格仍I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。Results eligibility=FALSE。
