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
8. 当前 active exact task 及其直接相关 acceptance/report。

当前状态：`K1_PAYOFF_CONTRACT_FROZEN_RAW_RA0__BOUNDED_RUNTIME_SAFETY_DIAGNOSTIC_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOUNDED_RUNTIME_SAFETY_DIAGNOSTIC.md`。
最新 accepted payoff-return re-audit candidate：`e6297bb19e10a77593e1c2c7876eb94f02c71533`。
Reviewer acceptance：`docs/CH5_MP4C_K1A_PAYOFF_RETURN_REAUDIT_ACCEPTANCE.md`。
Owner payoff freeze：`docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`。
Results eligibility=`FALSE`。

K1 bilateral capital network 已不仅是静态测试对象：accepted `capital_network.py` 已通过 K1A adapter/runner 接入 corrected-2018 bounded route，equal-share beta-distance=0 与 pure-geographic beta-distance=2 均真实完成25-turn路径；1550个 province-turn 的 capital conservation、home retention、quantity/rah same-`S`、C1 与 source-faithful labor gates 通过，且 geography 差异从turn2开始进入 household 并传播到后续 Y/wage/firm states。

但 K1 network 尚未被声明为无条件的全局 production/default steady-state authority。当前它通过明确的 K1A bounded adapter/runner 选择性启用；legacy allocator 继续保留为历史/source-faithful reference。因此准确状态是：网络已真实生效并产生科学传播证据，但仍在分阶段验证后再升级为最终主路径。

Payoff-return re-audit 已接受：raw `ra0` 是 source pre-clip net productive-capital return-like object；clipped `ra` 的 `[.02,.09]` 仅为 `EMPIRICAL_NUMERICAL_SAFEGUARD`，并在 accepted K1A evidence 中几乎抹平省际 payoff ordering。

Owner 已冻结最终 K1 payoff contract：household illiquid payoff 目标采用 raw `ra0`，解释为 per-model-time endogenous net productive-capital return rate；calendar annual/quarterly mapping unresolved，不做 annualization；内部 productive-capital return numeraire 可用于模型，外部 market-return mapping unresolved。目标 network payoff 为 `rah_i=sum_j S[j,i]*ra0_j`。

当前 exact task 只做短 horizon runtime safety：pure-geographic beta-distance=2 下 Control clipped-payoff 与 Raw raw-ra0-payoff 各最多5 turns，beta_return=0，fixed theta、source-faithful labor、C1、solver/grid/tolerance unchanged。最多2次 trajectory；不得进入 K1B/K2、standalone KFE、annual/IRF/Results。

K1B `beta_return=.5` 仍 preregistered，不授权 runtime；其 z-scored raw-`ra0` 仅用于 destination attractiveness，不是 household payoff。K2 不授权。corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning 继续是独立 KFE blocker。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复自动附Codex启动prompt。