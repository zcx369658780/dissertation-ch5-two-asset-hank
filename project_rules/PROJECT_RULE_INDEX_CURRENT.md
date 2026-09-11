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
7. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`K1A_PAYOFF_RETURN_REAUDIT_ACCEPTED__OWNER_PAYOFF_CONTRACT_FREEZE_PENDING`。
当前 active Builder task：NONE。
最新 accepted payoff-return re-audit candidate：`e6297bb19e10a77593e1c2c7876eb94f02c71533`。
Reviewer acceptance：`docs/CH5_MP4C_K1A_PAYOFF_RETURN_REAUDIT_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

K1A symmetric rerun 已接受：equal-share `beta_distance=0` 与 pure-geographic `beta_distance=2` 均完成25 turns，并通过 K1 capital conservation、home retention、quantity/rah same-`S`、C1 residual-public-assets 与 source-faithful labor gates。geography 差异从turn2开始经 network-produced `rah`进入 household 并传播到后续 Y、wage 与 firm states。

Payoff-return re-audit 已接受。Source audit确认 raw `ra0` 是 firm pre-clip net return-like object，used `ra` 是其 `[.02,.09]` clipped runtime object；K1A 以同一 `S` 聚合数量与 household `rah`。A/B upper clipping 分别为 `754/775` 与 `755/775`，30省25/25 upper-clipped，每轮 used return 仅1–2个 unique values；历史 bounds 继续只属于 `EMPIRICAL_NUMERICAL_SAFEGUARD`。Raw `ra0` 是 source-consistent candidate，但 calendar/model period、economic numeraire/payoff interpretation 与 runtime safety 尚未获得 Owner freeze。

因此目前不能发布 successor Builder task，也不能进入 K1B。下一 gate 是 Owner/Reviewer payoff-return contract freeze。若 Owner 选择 raw `ra0`，之后才可发布 bounded runtime-safety diagnostic exact task；该 safety gate 通过前 K1B runtime 仍不授权。

K1B `beta_return=.5` 仍仅 preregistered，不授权 runtime；其 z-scored raw-`ra0` 只用于 destination attractiveness，不是 household payoff。K2 不授权。corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning 继续是独立 KFE blocker。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复自动附Codex启动prompt。
