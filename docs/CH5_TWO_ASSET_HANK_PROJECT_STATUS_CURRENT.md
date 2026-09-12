# Chapter 5 两资产 HANK 当前状态
更新：2026-09-12。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_ANNUAL_HJB_G1_ACCEPTED__RA_FIRST_CONTINUATION_FROZEN__G1_VS_G2_SHORT_HORIZON_DIAGNOSTIC_ACTIVE`。

最新 accepted annual-G1 candidate：`a7eccde5e0ca694f95d3b3c082bfa82e0ce8cbb1`。
Reviewer acceptance：`docs/CH5_MP4C_K1_ANNUAL_HJB_RECALIBRATED_G1_GUARD_BOUNDED_RUNTIME_DIAGNOSTIC_ACCEPTANCE.md`。
Owner annual recalibration freeze：`docs/CH5_MP4C_K1_ANNUAL_HJB_COMPLETE_RECALIBRATION_CONTRACT_FREEZE_CURRENT.md`。
Owner price-guard continuation freeze：`docs/CH5_MP4C_K1_PRICE_GUARD_CONTINUATION_AND_BOUNDARY_HIT_MONITORING_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_ANNUAL_HJB_G1_VS_G2_PRICE_GUARD_CONTINUATION_DIAGNOSTIC.md`。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

## Annual recalibration 与 G1：已接受为短程数值脚手架
Owner-frozen annual continuous-time contract 已进入真实 bounded runtime：`rho=.05/year`、`rb=.02/year`、borrowing gap `.07/year`、`delta=.10/year`、`Q_z=1/3/year`、annual `Y/K` 与 profit/K 不做 `/4`、`ra0_annual=rk+after_tax_profit_over_K-.10`、`chi0=.1`、`chi1=2 years`。K1 same-S、capital conservation、C1、source-faithful labor与provenance gates均闭合。

Annual unguarded U treatment HJB convergence=`11/124`；G1 return guard `[-.05,.20]` treatment convergence=`18/124`。G1 `124/124` treatment province-turn 全部 upper-saturated，进入HJB的 `r_a` 被压为 `.20`，因此G1仅作为 continuation starting point 接受，不是最终 payoff calibration，也不授权 longer G1。

## Owner 对 legacy price safeguards 的最新澄清
Owner确认：旧 MATLAB 中 `ra` 与 `wjt` 上下界主要是 nonlinear HA/HJB steady-state iteration 的 numerical safeguards，而非为了建立最终价格规模或结构性经济边界。Legacy `multi_prov_HANK_12sts.m` 定义 `wjtmin=.8`, `wjtmax=1.3`；legacy `HANK_mp_1eq.m` 同时统计 `ra` 与 `wjt` 哪些省份撞上下界。

因此新的 continuation 路线冻结为：先固定 legacy wage safeguard `[.8,1.3]`，只推进 return guard；待找到可行的 return scaffold 后，再单独设计 wage-guard relaxation ladder。不得同时放宽 return 与 wage safeguards，除非Owner另行授权。

## Mandatory price-bound monitoring
从现在起每个 runtime continuation task 必须像 legacy MATLAB 一样记录价格变量撞界情况：

- return：raw/converted/guarded `rah/r_a`、upper/lower/unsaturated province names、counts与shares；
- wage：raw/pre-guard wage（若active route可得）、guarded `wjt`、`wjt=.8/1.3` upper/lower/unsaturated province names、counts与shares。

理想最终稳态目标冻结为 `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`：最终被接受的稳态应尽量做到 `ra/rah` 与 `wjt/wage` 等价格型 numerical safeguards 均不绑定；在此之前任何依赖guard的steady state都只能称 `PROVISIONAL_STEADY_STATE`。

## 当前 active continuation gate
当前 exact task 只比较 annual G1 与 G2 两条最多5-turn路径：

- G1：`r_a in [-.05,.20]`；
- G2：`r_a in [-.10,.35]`；
- 两者均保持 `wjt in [.8,1.3]` 不变；
- annual calibration、K1 network、fixed theta、`beta_distance=2`、`beta_return=0`、source-faithful labor、C1、solver/grid/tolerance 均不变。

任务重点：G2是否显著降低return saturation、恢复HJB输入的省际差异，同时不造成HA/HJB convergence、transfer/cost/drift的不可接受恶化；并逐省逐轮记录wjt撞界。

G3/G4、longer G2、wage-bound relaxation均未授权。

## 数值系统重建状态
K1 bilateral capital network与annual time-base已进入accepted bounded runtime。当前主要重建对象是HA/HJB nonlinear solution continuation：先寻找可行return region，再处理wage safeguard，最终逐步拆除price guards。

## K1B / K2 / KFE
K1B `beta_return=.5` 仍仅preregistered，不授权runtime；K2不授权。corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning仍是独立KFE blocker；KFE=`DIAGNOSTIC_ONLY`。当前任何K1结论均不构成steady-state、annual/IRF/welfare或Results acceptance。
