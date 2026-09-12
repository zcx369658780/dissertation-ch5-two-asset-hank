# Chapter 5 两资产 HANK 当前状态
更新：2026-09-12。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_ANNUAL_HJB_COMPLETE_RECALIBRATION_FROZEN__G1_GUARDED_BOUNDED_RUNTIME_DIAGNOSTIC_ACTIVE`。

最新 accepted provenance-closure candidate：`c94352740f4390bbf2fbaecae93c486395afe83f`。
Reviewer acceptance：`docs/CH5_MP4C_K1_QUARTERLY_HJB_VS_ANNUAL_FIRM_FLOW_PROVENANCE_CLOSURE_ACCEPTANCE.md`。
Owner annual recalibration freeze：`docs/CH5_MP4C_K1_ANNUAL_HJB_COMPLETE_RECALIBRATION_CONTRACT_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_ANNUAL_HJB_RECALIBRATED_G1_GUARD_BOUNDED_RUNTIME_DIAGNOSTIC.md`。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

## Owner annual continuous-time recalibration contract：已冻结
由于现有 source 无法唯一识别 common calendar base，Owner 现作为新的 scientific calibration choice 冻结：

- `MODEL_TIME_BASE=ANNUAL_CONTINUOUS_TIME`；
- `rho=.05/year`；
- `rb=.02/year`；
- borrowing gap `.07/year`；
- firm/HJB depreciation `delta=.10/year`；
- `Q_z` off-diagonal intensity `1/3 per year`；
- corrected-2018 annual `Y/K` 与 after-tax profit/K 保持 annual flow/stock rate，不做 `/4`；
- `ra0_annual = rk + after_tax_profit_over_K - .10`；
- `rah=S'ra0_annual`，quantity/payoff继续使用同一`S`；
- `chi0=.1`，`chi1=2 years` 作为 provisional annual adjustment-cost calibration；
- wage/consumption/transfer/adjustment-cost 统一解释为 annual household-model-unit flow；
- household asset numeraire 暂不改变；
- outer turn 继续只是 numerical fixed-point iteration。

`.10` 是新的 Owner-frozen annual calibration，不声称是 `.025` 的精确复利换算。PIM `.096` 继续只用于资本存量构造。

## Diagnostic guard policy：第一阶段 G1 已 preregister
未来 guard 必须在 raw/converted objects 保存之后，仅在 HJB interface 施加。第一阶段 G1 冻结：

- HJB illiquid return input `r_a`：`[-.05,.20]`；
- 现有 firm `wjt [.8,1.3]` 继续仅作为 temporary diagnostic guard，并记录 hit counts。

Return-guard relaxation ladder：
`G1 [-.05,.20] -> G2 [-.10,.35] -> G3 [-.20,.60] -> G4 OFF`。

只有 G1 当前获 runtime authority；任何后续 stage 必须先验收前一阶段并重新授权。依赖 guard 的 steady state 只能称 `PROVISIONAL_STEADY_STATE`。

## 当前 bounded runtime gate
当前任务从 byte-identical accepted initialization 比较两条最多5-turn路径：

- U：annual recalibration，turn1 common bootstrap，turns2-5 使用 same-path prior annual raw `ra0@S`，不加新 `r_a` guard；
- G1：同样 annual recalibration，turn1 common bootstrap，turns2-5 在 HJB interface 将 annual converted `rah` guard 到 `[-.05,.20]`。

两路径均使用 `beta_distance=2`、`beta_return=0`、fixed theta、source-faithful labor、smoothing OFF、C1 unchanged、K1B/K2 OFF。必须分别保存 raw annual `ra0`、converted annual `rah`、HJB-consumed guarded/unbounded `r_a` 与 saturation counts。

该任务只测试 short-horizon annual recalibration 与 diagnostic guard 的数值作用，不构成25-turn、steady state或Results gate。

## 数值系统重建状态
旧多省份 MATLAB/source-faithful 系统继续保留为 provenance/reference，但其 capital allocation、household return aggregation、historical clipping、time-scale wiring 与 empirical KFE 等关键合同已有 accepted evidence 证明存在结构缺陷、信息损失或维度冲突，不能作为最终 scientific authority。

新系统已完成 K1 bilateral capital network 的 accounting/home-retention/same-S quantity-payoff/bounded dynamic transmission；现在正式进入 annual recalibration + diagnostic-guard 数值重建阶段。长期 HJB stability、empirical KFE、K1B/K2、steady state 与 Results 仍未完成。

## K1B / K2 / KFE
K1B `beta_return=.5` 仍仅 preregistered，不授权 runtime；其 z-scored raw `ra0` 只用于 destination attractiveness，不是 payoff。K2不授权。

corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning 仍是独立 KFE blocker。KFE=`DIAGNOSTIC_ONLY`。当前任何 K1 结论均不构成 steady-state、annual/IRF/welfare 或 Results acceptance。
