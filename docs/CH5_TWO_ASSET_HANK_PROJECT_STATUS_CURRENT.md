# Chapter 5 两资产 HANK 当前状态
更新：2026-09-12。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_ANNUAL_HJB_G1_SHORT_HORIZON_DIAGNOSTIC_ACCEPTED__RETURN_GUARD_FULLY_SATURATED__WAGE_GUARD_HIGHLY_SATURATED__OWNER_NUMERAIRE_AND_GUARD_CALIBRATION_DECISION_REQUIRED`。

最新 accepted annual-G1 candidate：`a7eccde5e0ca694f95d3b3c082bfa82e0ce8cbb1`。
Reviewer acceptance：`docs/CH5_MP4C_K1_ANNUAL_HJB_RECALIBRATED_G1_GUARD_BOUNDED_RUNTIME_DIAGNOSTIC_ACCEPTANCE.md`。
Owner annual recalibration freeze：`docs/CH5_MP4C_K1_ANNUAL_HJB_COMPLETE_RECALIBRATION_CONTRACT_FREEZE_CURRENT.md`。
当前 active Builder task：NONE。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

## Annual recalibration：bounded route 已接受
Owner-frozen annual continuous-time contract 已在两条5-turn路径中真实执行：`rho=.05/year`、`rb=.02/year`、borrowing gap `.07/year`、`delta=.10/year`、`Q_z=1/3/year`、annual `Y/K` 与 profit/K 不做 `/4`、`ra0_annual=rk+after_tax_profit_over_K-.10`、`chi0=.1`、`chi1=2 years`。U/G1 turn1 完全一致，same-S、lagged provenance、K1/C1 accounting、source-faithful labor、NaN/Inf hard-stop 均通过。

`.10` 相对旧 `.025` route 在 turn1 使每省 raw `ra0` 精确下降约 `.075`。Annual unguarded U 仍可执行，但 treatment HJB convergence 只有 `11/124`，说明仅修正 depreciation/time-base 并未建立稳定 household numerical solution。

## G1 diagnostic guard：接受为脚手架，但不能延长
G1 HJB return guard 为 `[-.05,.20]`。Treatment turns2-5 中 upper `.20` 命中 `124/124`、lower `0/124`、unsaturated `0/124`。因此 guard 前每轮仍保留31个不同的 converted `rah`，但进入 HJB 后全部变成 `.20`，省际 payoff ranking 被完全压平。

G1 HJB convergence 为 `18/124`，较 U 的 `11/124` 有小幅改善；turns3-5 worst statistic 显著降低，但 transfer、adjustment-cost、`mu_a/mu_b` 与 drift extrema 在 turns2-4 反而更大，只有 turn5 较低。故 G1 不是统一稳定化处理。

Existing wage guard `[.8,1.3]` 同样高度绑定：G1 treatment `112/124`（90.3%）省轮命中上下界。return 与 wage 两个 household interface 同时高度 guard-dependent，说明当前 numerical interface 过度压缩。

Reviewer route decision：不发布更长 G1。更长 G1 主要会研究常数 `r_a=.20` 的 household block，而不是 intended provincial payoff heterogeneity。也不自动进入 G2；在放宽 return guard 前必须先由 Owner 决定 annual household wage/asset numeraire 与下一阶段 guard calibration 是否需要共同调整。

## 数值系统重建状态
K1 bilateral capital network 的 accounting/home-retention/same-S quantity-payoff/bounded transmission 已 accepted；annual time-base 也已进入实际 runtime。当前主要 blocker 已转向 household interface calibration：payoff guard 完全饱和、wage guard 高度饱和、HJB convergence 仍低。旧 MATLAB/source-faithful 数值系统继续仅保留 provenance/reference。

## 当前 Owner scientific gate
下一步必须由 Owner 决定：
- 是否保留当前 annual household asset numeraire；
- firm-to-household wage scaling/normalization 是否需要重标定；
- 下一阶段是否允许 G2 `r_a in [-.10,.35]`；
- wage guard 是否与 G2 同时重新 preregister；
- 或先修改 household flow/numeraire calibration 再保留 G1。

确认前不发布 successor Builder task，不运行 longer G1/G2，不进入 K1B/K2。

## K1B / K2 / KFE
K1B `beta_return=.5` 仍仅 preregistered，不授权 runtime；K2不授权。corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning 仍是独立 KFE blocker；KFE=`DIAGNOSTIC_ONLY`。当前任何 K1 结论均不构成 steady-state、annual/IRF/welfare 或 Results acceptance。
