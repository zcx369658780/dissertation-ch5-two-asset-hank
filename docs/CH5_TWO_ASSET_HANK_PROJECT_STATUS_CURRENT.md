# Chapter 5 两资产 HANK 当前状态
更新：2026-09-12。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_HJB_PAYOFF_SCALE_AUTHORITY_AUDIT_ACCEPTED__QUARTERLY_HJB_VS_ANNUAL_FIRM_FLOW_PROVENANCE_CLOSURE_ACTIVE`。

最新 accepted payoff-scale authority audit candidate：`367de55e60d144042b0a95ad1fd49fbc5267f85f`。
Reviewer acceptance：`docs/CH5_MP4C_K1_HJB_PAYOFF_SCALE_AUTHORITY_ZERO_SCIENCE_AUDIT_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_QUARTERLY_HJB_VS_ANNUAL_FIRM_FLOW_PROVENANCE_CLOSURE.md`。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

资本网络总体科学设计冻结稿：`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。
K1 scoring/data 冻结稿：`docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`。
Payoff-return 冻结稿：`docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`。
Payoff-scale/debug guard policy：`docs/CH5_MP4C_K1_PAYOFF_SCALE_MAPPING_AND_DIAGNOSTIC_BOUND_POLICY_FREEZE_CURRENT.md`。

## 已接受：旧 direct raw-ra0 -> HJB r_a 数值映射失去 authority
最新 zero-science authority audit 证明：corrected-2018 firm block 的 `Y` 是年度 GDP flow、`K` 是资本存量，因此 `rk=mt*alpha*Y/K` 与 profit/K 在现有数据合同下是年度 flow/stock rate；而论文第四章明确把 `delta=.025` 解释为季度折旧率。当前 firm 代码却直接计算 `ra0=rk+after_tax_profit_over_K-delta`，因此 raw `ra0` 本身已经混合了年度与季度尺度。

Chapter-5 参数表另写 `delta=.0025`，与 Chapter-4 `.025`、代码 `.025` 冲突。旧 MATLAB / dissertation 证明历史上 firm return 曾直接进入 `rah/r_a`，但这种 source fidelity 不能证明 calendar/model-time dimensional consistency。

Household HJB 是连续时间方程。`rho=.05`、`rb=.02`、`r_a/rah`、productivity generator `1/3`、wage、transfer 与 adjustment-cost 系数目前都只有 model-time 或 unresolved authority，尚无完整统一的 calendar unit。因此 direct numerical identity `HouseholdInputs.r_a = firm ra0` 当前不再授权 runtime。

## 当前 scientific route
Owner 仍保留 raw `ra0` 作为经济 payoff source object，但 numerical payoff mapping 未冻结。不得自行采用 `/4`、复利/对数转换、z-score、任意 shrinkage、normalization、smoothing 或重新把历史 `[.02,.09]` clipping 升级为 structural payoff law。

当前 exact task 为纯 zero-science source/calibration provenance closure。目标是解决 Chapter-4 / Chapter-5 / code 的 depreciation conflict，并统一 `rho/rb/r_a/Q_z/Y/K/wage/transfer/adjustment-cost` 的 calendar/model-time convention。只有完整 source-backed conversion 或明确 Owner recalibration contract 冻结后，才可设计新的 bounded runtime diagnostic。

## 数值调试 guard policy
Owner 已授权未来在 exact debugging task 中对 `ra/rah`、`wjt/wage` 等使用 hard bounds 作为临时 numerical diagnostic scaffolding，以先建立 provisional steady-state route，再按 preregistered relaxation ladder 放宽或移除。但这些 guard 不得被称为 structural economics；必须事先冻结值、保存 hit/saturation counts，且不得在看完同一运行结果后反复调界求 PASS。

## K1B / K2 / KFE
K1B `beta_return=.5` 仍仅 preregistered，不授权 runtime；其 z-scored raw `ra0` 只用于 destination attractiveness，不是 payoff。K2 不授权。

corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning 仍是独立 KFE blocker。当前任何 K1 结论均不构成 steady-state、KFE、annual/IRF/welfare 或 Results acceptance。
