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
当前 active Builder task：`tasks/CH5_MP4C_2018_RAW_NBS_DATA_REBUILD_CAPITAL_AND_PRODUCTIVITY_REESTIMATION.md`。
该任务由Owner明确要求：直接从国家统计局原始XLS重建同年2018数据、重新估计各省资本存量与生产率，并将可复现的派生结果保存到GitHub；不得运行HANK/HJB/KFE/firm/outer-loop模型。
最新接受候选：`1321b7a227e6b1e341623222eeecd11748189727`。
Reviewer acceptance：`docs/CH5_MP4C_2018_MATLAB_INPUT_DATA_AND_INITIAL_STATE_COMPARISON_AUDIT_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

原MATLAB“2018”对象已确认混合使用2009 GDP/CAP/POP levels、2020 level-derived Zt与PLM vintage19 alpha；alpha 31/31与canonical精确一致，但GDP和资本31/31均存在material level difference。GovInv初始化自Kt0，因此继承资本年份/尺度问题。安徽差异尤其明显：GDP约-68.06%，资本约-83.19%，而POP约+0.91%、Zt约-7.49%、alpha精确一致。

当前新任务使用Owner提供的原始国家统计局文件：`地区生产总值 亿元.xls`、`固定资本形成总额 亿元.xls`、`固定资产折旧 亿元.xls`、`年末常住人口 万人.xls`。要求先重建clean province-year panel，再以当前accepted PIM contract作为primary Track A估计资本；同时利用实际折旧数据构建单独的Track B accounting diagnostic，不自动升级为production authority；随后按rolling 10-year、2018 vintage=2009–2018的既有PLM方程族重新估计alpha，并用同年2018 Y/K/L计算province Zt。

此前five-turn KFE attribution仍是有效历史证据，但Owner当前明确要求先修正数据与校准对象，不自动进入boundary/KFE production redesign，也不运行任何模型查看是否收敛。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新的科学执行必须先发布exact task。以后每次发布exact task，同一回复自动附Codex启动prompt。