# Chapter 5 当前规则入口
更新：2026-09-09；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。读取AGENTS、此索引和当前状态；存在active exact task时再读task。旧R5/R1A及过期CURRENT只作历史。

当前状态：`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`。
路线：`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`。
交接：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`。
当前 active Builder task：无。
状态标记：`PIM_CAPITAL_CHAIN_ACCEPTED__2018_CAP_BINARY64_REPRODUCED__GDP_ONLY_DATA_BLOCKER_REMAINS`。

Builder默认`gpt-5.6-sol / medium`；host未暴露时不虚报实际模型，不改provider/global配置。

最新接受候选`0bfff9ff9f388e39812c6592f72d5eedd633ae18`。2018安徽PIM资本链在冻结公式`K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`下逐年binary64精确复现`K2000..K2018`；`K2018=1357314108.2013683`，V2 transformed CAP=`1357314108201.3684`，`I2018`不参与K2018。资本存量是model-derived calibration object，不是官方资本存量；2011统计定义断点继续作为限制保留。

2018安徽人口已闭合为修订后`6076`万人。当前2018数据层只剩GDP身份未闭合：provisional `34010.91`亿元 vs 初步官方`30006.82`亿元，缺第四次全国经济普查后修订的精确2018现价GDP和revision provenance。

在GDP身份关闭前，不启动2018 household/HJB/KFE/firm/GE/annual科学运行，不调GovInv/alpha，不扩大bmax，不切换PLM。Results eligibility=FALSE。
