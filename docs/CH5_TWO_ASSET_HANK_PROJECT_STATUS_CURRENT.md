# Chapter 5 两资产 HANK 当前状态
更新：2026-09-12。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_PAYOFF_CONTRACT_FROZEN_RAW_RA0__BOUNDED_RUNTIME_SAFETY_DIAGNOSTIC_ACTIVE`。

最新 accepted payoff-return re-audit candidate：`e6297bb19e10a77593e1c2c7876eb94f02c71533`。
Reviewer acceptance：`docs/CH5_MP4C_K1A_PAYOFF_RETURN_REAUDIT_ACCEPTANCE.md`。
Owner payoff freeze：`docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOUNDED_RUNTIME_SAFETY_DIAGNOSTIC.md`。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

资本网络总体科学设计冻结稿：`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。
K1 scoring/data 冻结稿：`docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`。

## K1 bilateral capital network：已实现并已在 bounded K1A route 中生效
Accepted K1 bilateral capital-network engine 已进入仓库并通过 K1A 运行适配器接入 corrected-2018 bounded route。它不是只有静态测试：equal-share `beta_distance=0` 与 pure-geographic `beta_distance=2` 两条路径均已真实运行25 turns，并通过1550个 province-turn 的 capital share/origin/national conservation、home retention、quantity/rah same-`S`、C1 与 source-faithful labor gates。geography 差异从 turn2 开始通过 network-produced `rah` 进入 household 并传播到 Y、wage 与后续 firm states。

但该 network 尚未被声明为无条件的全局 production/default steady-state authority。当前它通过明确的 K1A bounded adapter/runner 选择性启用；legacy allocator 仍保留为历史/source-faithful reference。完整 steady-state、KFE、K1B/K2 与 Results authority 尚未建立。因此准确表述是：**资本网络已经在受控科学运行中真实生效并产生内生传播，但仍处于分阶段验证/升级为最终主路径的过程中。**

## K1A symmetric bounded rerun：已接受
两条 preregistered 路径均完成25/25 turns：equal-share `beta_distance=0` 与 pure-geographic `beta_distance=2`，两者均 `beta_return=0`。fixed `theta_i=inter_prv_ratio_i`、source-faithful labor、smoothing OFF、C1 `GovInv=max(Ktarget-Kprivate,0)` 均保持。

接受证据显示：1550 province-turn 中 capital accounting 与 same-`S` payoff accounting 闭合；`Kprivate>=Ktarget`=0/0，private-only overshoot=0/0；total K/target 两路径均约为1。两路径 turn25 均未满足冻结 final predicate，且 corrected-2018 KFE 仍全部 `DIAGNOSTIC_ONLY`。

## Payoff-return re-audit：已接受
Accepted classification：`CLIPPED_RA_REMAINS_ONLY_TRANSITIONAL_BRIDGE__RAW_RA0_IS_SOURCE_CONSISTENT_CANDIDATE_REQUIRING_OWNER_PERIOD_NUMERAIRE_FREEZE`。

Source audit确认 active `ra0 = rk + after_tax_profit_over_K - delta`，source-used `ra` 是将 `ra0` 截到 `[.02,.09]` 后的 runtime object。A/B upper clipping 分别为 `754/775` 与 `755/775`；30省在25 turns中全部 upper-clipped，每轮 used return 仅1–2个 unique values；历史 bounds 继续只属于 `EMPIRICAL_NUMERICAL_SAFEGUARD`。

## Owner payoff-return contract：已冻结
Owner 于2026-09-12批准：K1 最终 household illiquid payoff source object 采用 raw pre-clip `ra0`。

冻结解释：
- `ra0` = `MODEL_TIME_RETURN_RATE__CALENDAR_PERIOD_UNRESOLVED`；
- 是 household provincial portfolio fund 对 destination productive capital 的 endogenous net return；
- 内部采用 dimensionless rate-like productive-capital return numeraire；外部 market-return mapping 仍未解析；
- 不做 annualization/de-annualization；
- `[.02,.09]` 不再是最终经济 payoff bound，只保留为历史 numerical safeguard/provenance diagnostic；
- household network payoff 目标为 `rah_i=sum_j S[j,i]*ra0_j`；
- K1B z-scored raw-`ra0` 仍仅是 attractiveness signal，不是 payoff level。

该科学冻结本身不授权直接切换完整 runtime。必须先完成 active bounded safety task。

## 当前 active safety gate
`CH5_MP4C_K1_RAW_RA0_PAYOFF_BOUNDED_RUNTIME_SAFETY_DIAGNOSTIC` 只比较 pure-geographic `beta_distance=2` 下的两个5-turn短路径：Control 使用 clipped/source-used `ra`；Raw 使用 prior-completed raw `ra0`。两条路径 fixed theta、beta_return=0、source-faithful labor、C1、solver/grid/tolerance 均相同。

目的只是检查 raw payoff 首次进入下一 household iteration 后是否出现 NaN/Inf、HJB/KKT/control/drift pathology、same-turn feedback 或 accounting 破坏。最多2次 trajectory、每条5 turns；不得进入 K1B/K2、annual/IRF/Results。

## K1B / K2 / KFE
K1B `beta_return=0.5` 仍 preregistered，不授权 runtime。K2 不授权。

corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning 仍是独立 KFE blocker。当前任何 K1 结论均不构成 steady-state、KFE、annual/IRF/welfare 或 Results acceptance。