# Chapter 5 当前规则入口
更新：2026-09-10；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`MATLAB_2018_INPUT_DATA_AUDIT_ACCEPTED__MATERIAL_EXTERNAL_SCALE_AND_YEAR_MIXTURE_CONFIRMED__NO_CAUSAL_COLLAPSE_CLAIM`。
当前 active Builder task：无。
最新接受候选：`1321b7a227e6b1e341623222eeecd11748189727`。
Reviewer acceptance：`docs/CH5_MP4C_2018_MATLAB_INPUT_DATA_AND_INITIAL_STATE_COMPARISON_AUDIT_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

2018 corrected/canonical数据层继续绑定私有workbook SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`。

最新静态数据审计确认，原MATLAB“2018”对象混合使用2009 GDP/CAP/POP levels、2020 level-derived Zt与PLM vintage19 alpha；alpha 31/31与canonical精确一致，但GDP和资本31/31均存在material level difference。GovInv初始化自Kt0，因此继承资本年份/尺度问题。安徽差异尤其明显：GDP约-68.06%，资本约-83.19%，而POP约+0.91%、Zt约-7.49%、alpha精确一致。

该审计scientific/model calls=`0`，只支持外部数据/初始化尺度与provenance diagnosis，不证明任何单一差异导致turn3 asset collapse。原MATLAB 2018 steady-state cache缺失，因此原路线persisted At/Bt/Kt_supply、首轮firm prices及下一轮rah/wage仍不能在不进行scientific rerun的前提下恢复。

此前five-turn KFE attribution仍是有效历史证据，但Owner当前明确要求先理解外部数据/初始化尺度与outer-loop反馈，不自动进入boundary/KFE production redesign。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新的科学执行必须先发布exact task。以后每次发布exact task，同一回复自动附Codex启动prompt。