# Chapter 5 当前规则入口
更新：2026-09-09；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。读取AGENTS、此索引、当前状态和active exact task；旧R5/R1A及过期CURRENT只作历史。

当前状态：`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`。
路线：`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`。
交接：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_PIM_CAPITAL_CHAIN_CLOSURE.md`。
状态标记：`PIM_CAPITAL_CHAIN_CLOSURE_ACTIVE__EXISTING_PIM_METHOD_FROZEN__GDP_STILL_OPEN`。

Builder默认`gpt-5.6-sol / medium`；host未暴露时不虚报实际模型，不改provider/global配置。

V2 rolling-10y/same-year-Zt合同继续冻结。2018安徽人口已由2023《中国人口和就业统计年鉴》修订历史值`6076`万人闭合。

Owner最新科学裁决：资本存量继续使用现有永续盘存法（PIM），不再把缺少官方资本存量视为blocker。冻结公式`K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`，折旧率和初始化均不改；K2018使用I2000..I2017。当前省级投资链作为模型校准来源使用，但必须保留2011统计定义断点及CNKI整理来源限制，不得升级为官方连续同口径序列。

当前task只做静态PIM复现、provenance/receipt版本化和必要二次交叉核验；所有科学模型调用0。若精确复现现有K2018，则关闭资本/PIM data-method blocker。GDP仍未闭合：provisional 34010.91亿元 vs 初步官方30006.82亿元，缺第四次经济普查后修订精确值。

不运行2018 household/HJB/KFE/firm/GE/annual，不调GovInv/alpha，不扩大bmax，不切换PLM。Results eligibility=FALSE。
