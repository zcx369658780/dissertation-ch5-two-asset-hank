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
8. 若存在 active task，再读取该 exact task及直接相关 acceptance/report。

当前状态：`K1_RAW_RA0_PAYOFF_SAFETY_BLOCKED_PRE_RUN_ACCEPTED__OWNER_BOOTSTRAP_DECISION_PENDING`。
当前 active Builder task：NONE。
最新 raw-payoff safety candidate：`2c29a38b153ee56e58c833297b7dad2da639d6e7`。
Reviewer acceptance：`docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOUNDED_RUNTIME_SAFETY_DIAGNOSTIC_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

K1 capital network 已在 corrected-2018 bounded K1A route 中真实启用并获得 accepted dynamic evidence：equal-share `beta_distance=0` 与 pure-geographic `beta_distance=2` 都完成25 turns，capital quantity 与 household `rah` 使用同一 destination-by-origin `S`，且 geography 差异从 turn 2 开始传入 household/Y/wage/firm states。它不是仅离线测试；但 legacy allocator 仍保留为 reference，K1 尚未升级为无条件 production/default steady-state route。

Owner 已冻结 raw `ra0` 为最终 K1 household illiquid payoff source object；历史 `[.02,.09]` clipped `ra` 只保留为 `EMPIRICAL_NUMERICAL_SAFEGUARD`/diagnostic bridge。raw payoff 解释为 per-model-time endogenous net productive-capital return，不做 calendar annualization，不宣称外部 market-return mapping。

最新 raw-payoff bounded safety task 在 pre-run gate 正确停止：accepted initialization 中 `ra0=0/31`，而 `ra/rah/rk=31/31`；completed turn 会把 raw `ra0` 持久化到下一 state。Builder 未自行增加 bootstrap 规则，新增 trajectory/HJB/KFE 等科学调用全部为0。

下一步不是 Builder task，而是 Owner initialization/timing freeze。Reviewer 推荐：Control 与 Raw 共用 accepted entering clipped/source-used `ra` 完成 turn 1；从同一个 completed turn-1 firm state 获得 provenance-safe raw `ra0` 后，Raw 从 turn 2 开始使用 `S'ra0`，Control 继续使用 `S'ra`。Owner确认前不得发布 successor task。

K1B `beta_return=.5` 仍仅 preregistered，不授权 runtime；其 z-scored raw `ra0` 只用于 destination attractiveness。K2不授权。corrected-2018 finite-box upper-b leakage/MATLAB-style pinning 继续是独立 KFE blocker。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复自动附Codex启动prompt。
