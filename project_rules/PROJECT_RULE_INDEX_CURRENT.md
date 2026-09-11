# Chapter 5 当前规则入口
更新：2026-09-12；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
6. `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
7. `docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`
8. `docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOOTSTRAP_TIMING_FREEZE_CURRENT.md`
9. 当前 active exact task 及直接相关 acceptance/report。

当前状态：`K1_RAW_RA0_PAYOFF_BOOTSTRAP_TIMING_FROZEN__COMMON_TURN1_SAFETY_DIAGNOSTIC_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOUNDED_RUNTIME_SAFETY_DIAGNOSTIC_WITH_COMMON_TURN1_BOOTSTRAP.md`。
最新 blocked-pre-run candidate：`2c29a38b153ee56e58c833297b7dad2da639d6e7`；其 blocker evidence 已接受。
Results eligibility=`FALSE`。

K1 capital network 已在 corrected-2018 bounded K1A route 中真实启用并获得 accepted dynamic evidence：equal-share `beta_distance=0` 与 pure-geographic `beta_distance=2` 均完成25 turns，capital quantity 与 household `rah` 使用同一 destination-by-origin `S`，geography 差异从 turn2 开始进入 household/Y/wage/firm states。它不是仅离线测试；legacy allocator 仍保留为 reference，K1 尚未升级为无条件 production/default steady-state route。

Owner 已冻结 raw `ra0` 为最终 K1 household illiquid payoff source object；历史 `[.02,.09]` clipped `ra` 只保留为 `EMPIRICAL_NUMERICAL_SAFEGUARD`/diagnostic bridge。raw payoff 解释为 per-model-time endogenous net productive-capital return，不做 calendar annualization，不宣称外部 market-return mapping。

Accepted initialization 不含 prior-completed raw `ra0`。Owner 已冻结 common turn-1 bootstrap：Control 与 Raw 都用 accepted entering clipped/source-used `ra` 完成 turn1；turn1 完成后各自获得 provenance-safe raw `ra0`。从 turn2 起，Control 继续用本路径 prior-completed used `ra`，Raw 用本路径 prior-completed raw `ra0`；不允许 cross-path borrowing 或 same-turn feedback。

当前任务每条最多5 completed turns：turn1单独作为共同bootstrap，raw-payoff treatment horizon为turns2-5。仅测试 short-horizon runtime safety，不授权25-turn、steady-state、K1B/K2或Results。

K1B `beta_return=.5` 仍仅 preregistered，不授权 runtime；其 z-scored raw `ra0` 只用于 destination attractiveness，不是 payoff。K2不授权。corrected-2018 finite-box upper-b leakage/MATLAB-style pinning 继续是独立 KFE blocker。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复自动附Codex启动prompt。
