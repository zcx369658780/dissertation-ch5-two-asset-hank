# Chapter 5 当前规则入口
更新：2026-09-10；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`FIVE_TURN_KFE_ATTRIBUTION_ACCEPTED__SAME_FINITE_BOX_UPPER_B_LEAKAGE_AND_PINNING_MECHANISM_CONFIRMED__OWNER_BOUNDARY_DECISION_REQUIRED`。
当前 active Builder task：无。
最新接受候选：`ea4ac44fe3c65c506ff7fdfbdbf29d96078cc5c6`。
Results eligibility=`FALSE`。

2018数据层已闭合并继续绑定canonical workbook SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`。

Five-turn accepted blocker：turn4/5 31/31 densities均`DIAGNOSTIC_ONLY`；material问题是source-free stationarity residual与upper-b outward leakage，不是机器精度负density。

最新zero-science attribution已确认：corrected turn4/5与call725 `rah=.07`属于同一finite-box upper-b leakage + row-replacement/pinning dropped-equation implicit-source algebra。turn4/5 62/62对象residual几乎全部集中在pin row；off-pin residual仅浮点量级；signed residual-vs-escape和implicit-source-vs-escape均在约`10^-16`闭合。该implicit source是代数后果，不是已采用经济entry/exit机制。

HJB-loop negative offdiagonals仍是独立问题；post-loop KFE operator不能替代HJB-loop诊断。

当前不得继续turn6+、new KFE solve、steady state、GE/annual/IRF/Results，也不得自动实现boundary/grid/source/pinning production repair。下一步先由Owner裁决finite-box/KFE closure路线。D1–D3仍为deferred redesign proposals。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新的科学执行必须先发布exact task。以后每次发布exact task，同一回复自动附Codex启动prompt。