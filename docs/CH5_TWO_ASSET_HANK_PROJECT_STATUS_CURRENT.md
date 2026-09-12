# Chapter 5 两资产 HANK 当前状态
更新：2026-09-12。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_TIME_BASE_PROVENANCE_CLOSURE_ACCEPTED__OWNER_COMPLETE_RECALIBRATION_CONTRACT_REQUIRED`。

最新 accepted provenance-closure candidate：`c94352740f4390bbf2fbaecae93c486395afe83f`。
Reviewer acceptance：`docs/CH5_MP4C_K1_QUARTERLY_HJB_VS_ANNUAL_FIRM_FLOW_PROVENANCE_CLOSURE_ACCEPTANCE.md`。
当前 active Builder task：NONE。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

## 已接受：common calendar base 不能由现有 source 唯一识别
Accepted classification：`COMMON_CALENDAR_BASE_NOT_SOURCE_IDENTIFIABLE__GENUINE_DEPRECIATION_CALIBRATION_CONFLICT__OWNER_RECALIBRATION_CONTRACT_REQUIRED`。

Corrected-2018 `Y/K` 与 profit/K 具有 annual firm flow/stock scale；Chapter 4 明确描述 `delta=.025` 为 quarterly depreciation；Chapter 5 参数表写 `.0025`；active Python/protected MATLAB 使用 `.025`；annualized prose 约为 `.10`；PIM `.096` 属于 capital-stock construction。现有 source 不足以由 Builder静默选择其中任何一个作为最终 firm/HJB depreciation。

同时，continuous-time HJB 的 `rho=.05`、`rb=.02`、`r_a/rah`、`Q_z=1/3`、wage/`wjt`、transfer、consumption、adjustment-cost flow 与 `chi1` 仍缺少一套共同 calendar/model-time authority。未发现完整 source-backed annual firm flow -> HJB flow bridge，因此 `/4`、`*4`、compounding 与 log conversion 均不授权。

## 数值系统重建状态
旧多省份 MATLAB/source-faithful 系统继续保留为 provenance/reference，但其 capital allocation、household return aggregation、historical clipping、time-scale wiring 与 empirical KFE 等关键合同已有 accepted evidence 证明存在结构缺陷、信息损失或维度冲突，不能作为最终 scientific authority。

新系统已完成 K1 bilateral capital network 的 accounting/home-retention/same-S quantity-payoff/bounded dynamic transmission；但完整 time-base recalibration、长期 HJB stability、empirical KFE、K1B/K2、steady state 与 Results 尚未完成。

## Owner debugging-bound policy
未来正确顺序冻结为：保留 raw firm objects -> 应用 Owner-frozen conversion -> 在 HJB interface 对 converted objects 施加 preregistered temporary guards。任何 guard 必须分别保存 raw/converted/guarded value 和 saturation counts；依赖 guard 的 steady state 只能称 provisional，并按 preregistered relaxation ladder 放宽/去除。历史 `[.02,.09]` 与 `[.8,1.3]` 不能在 conversion 前复用，也不能自动升级为 structural calibration。

## 当前 Owner scientific gate
下一步不是 Builder task，而是 Owner 冻结完整 common time-base / recalibration contract。必须共同决定：
- HJB/model-time base；
- `delta/rho/rb/Q_z`；
- annual firm-flow conversion law；
- wage/asset numeraire；
- transfer/consumption/adjustment-cost flow；
- `chi1` 的时间尺度；
- temporary diagnostic guards 的适用层级。

只有该 contract 冻结后，Reviewer 才能发布 bounded runtime diagnostic。当前不得进入25-turn Raw、K1B、K2或Results。

## K1B / K2 / KFE
K1B `beta_return=.5` 仍仅 preregistered，不授权 runtime；其 z-scored raw `ra0` 只用于 destination attractiveness，不是 payoff。K2不授权。

corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning 仍是独立 KFE blocker。KFE=`DIAGNOSTIC_ONLY`。当前任何 K1 结论均不构成 steady-state、annual/IRF/welfare 或 Results acceptance。
