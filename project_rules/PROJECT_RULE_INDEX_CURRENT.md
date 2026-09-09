# Chapter 5 当前规则入口
更新：2026-09-09；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。读取AGENTS、此索引和当前状态；存在active exact task时再读task。旧R5/R1A及过期CURRENT只作历史。

当前状态：`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`。
路线：`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`。
交接：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`。
当前 active Builder task：无。
状态标记：`PURCHASED_DATASET_AUDIT_ACCEPTED__2018_POPULATION_IDENTITY_CLOSED__GDP_AND_INVESTMENT_REMAIN_OPEN`。

Builder默认`gpt-5.6-sol / medium`；host未暴露时不虚报实际模型，不改provider/global配置。

最新接受候选`4db5c0691535e92d34a86c67ee96c2b8978c1de2`。付费数据审计接受：2023《中国人口和就业统计年鉴》表1-1支持安徽2018常住人口`6076`万人，并明确2011–2019依据2020人口普查修订，因此人口身份已闭合；权威是官方年鉴而非付费包。

GDP仍未闭合：provisional workbook `34010.91`亿元与2018初步官方`30006.82`亿元之间缺少第四次经济普查后修订2018精确表值。`sj479`安徽2000–2017城市投资覆盖完整但省级加总合同/口径/残余覆盖未证明，2017还含增速推算，因此不得直接求和或用于CAP。TFP包仅作未来验证候选，PLM不替换。

在GDP和投资/资本方法关闭前，不启动2018 household/HJB/KFE/firm/GE/annual，不调GovInv/alpha，不扩大bmax，不切换PLM。Results eligibility=FALSE。
