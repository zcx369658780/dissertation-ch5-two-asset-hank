# Chapter 5 当前规则入口
更新：2026-09-09；治理修订仍为 `CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。读取AGENTS、此索引和当前状态；存在active exact task时再读task。旧R5/R1A及过期CURRENT只作历史。

当前状态：`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`。
路线：`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`。
交接：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`。
当前 active Builder task：无。
状态标记：`TEMPORAL_CONTRACT_AUDIT_ACCEPTED__ROLLING_10Y_PLM_FROZEN__LEVEL_INDEX_DEFECT_CONFIRMED__ZT_2020_ANCHOR_LIKELY_LEGACY`。

Builder默认`gpt-5.6-sol / medium`；host未暴露时不虚报实际模型，不改provider/global配置。

最新接受候选`deb2d56560ce85590b9e19d34b4d28ea6b084e27`。Reviewer验收文件明确修正候选报告中的一项科学口径：Owner最终选择PLM滚动10年窗，而非从2000开始持续扩张窗口。正式合同为`steady_year=2008+ii`；同年水平量一基row=`ii+9`；PLM样本为最近10年`steady_year-9:steady_year`；2009用2000–2009，2018用2009–2018，2023用2014–2023。PLM估计器保持。

已确认当前level-row索引缺陷；固定2020行Zt缺乏已发现经济依据，分类`LIKELY_LEGACY_FIXED_YEAR_ANCHOR`。旧cache与较新PLM workbook存在版本身份不一致，后续必须版本化metadata/cache。2022–2023六个负资本/复数log问题继续独立阻塞对应年份。

当前不继续扩大bmax、不调整GovInv/alpha速度、不重跑年度/多省份/GE/Results。生产网格仍I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。下一步是有界时间合同实现和2018数据身份闭合；尚未发布实现task。Results eligibility=FALSE。
