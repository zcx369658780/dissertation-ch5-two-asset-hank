# Chapter 5 当前规则入口
更新：2026-09-09；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。读取AGENTS、此索引、当前状态和active exact task；旧R5/R1A及过期CURRENT只作历史。

当前状态：`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`。
路线：`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`。
交接：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_CORRECTED_INPUT_SINGLE_TURN_VALIDATION.md`。
状态标记：`REVISED_2018_GDP_AND_CANONICAL_WORKBOOK_ACCEPTED__2018_DATA_LAYER_CLOSED__SINGLE_TURN_VALIDATION_ACTIVE`。

Builder默认`gpt-5.6-sol / medium`；host未暴露时不虚报实际模型，不改provider/global配置。

2018数据层已关闭：安徽修订后GDP官方公布`34010.9`亿元（保护workbook `34010.91`仅在官方0.1亿元精度下匹配）；人口修订值`6076`万人；PIM `K2018=1357314108.2013683`逐年binary64闭合；rolling-10y PLM vintage19和same-year Zt已冻结。canonical workbook `CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx` SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`，私有本体不提交GitHub。

当前task授权一次且仅一次corrected-2018 source-faithful ordered one-turn。必须hash校验canonical workbook；完整31省source order，但只执行1 turn，不进入steady-state/GE/annual/IRF。旧mixed-year只用保存证据比较，不重跑。任何科学失败立即保存并停止，不调GovInv/alpha、grid、rates、solver/tolerance或boundary law。Results eligibility=FALSE。