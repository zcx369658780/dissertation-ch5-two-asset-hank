# Chapter 5 两资产 HANK 当前状态
更新：2026-09-11。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1A_STATIC_MAPPING_ACCEPTED__BETA_DISTANCE_2_FROZEN__BETA_RETURN_POINT5_PREREGISTERED__BOUNDED_K1A_INTEGRATION_ACTIVE`。

最新 accepted K1A zero-science candidate：`2ad7c74876d91326c127d8c7ef1c400991320968`。
Reviewer acceptance：`docs/CH5_MP4C_K1A_2018_DISTANCE_SCORE_MAPPING_AND_STATIC_PORTFOLIO_DIAGNOSTIC_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_BOUNDED_INTEGRATION.md`。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

资本网络总体科学设计冻结稿：
`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。
K1 scoring/data 冻结稿：
`docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`。

## K1A zero-science mapping：已接受
保护的省会地理距离 workbook SHA-256：`26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566`；读取范围 `geom!B2:AF32`；31/31 label-backed mapping 完整；961/961 finite；missing=0；negative=0；`max|D-D.T|=0`；`D_max=3639.514265`，最大距离为黑龙江–西藏；normalized off-diagonal range `[0.030224736871583606,1]`。

2018 theta authority SHA-256：`5DAD517983CBC436A5FB3E5AD85F1257D957D844994180D15929044A049C7212`；31/31 active order；源公式复算最大残差0；theta range `[0,0.3]`。

Static `beta_distance=[0,.5,1,2,4]` diagnostics 完成。mean normalized entropy 从 beta0 的 `1.000000` 降至 beta4 的 `0.943791`；31/31 origins entropy 随 beta weakly decreases；equal-share 与全部 capital/share conservation residuals 均在 `1e-12` 内。scientific/model/runtime calls=0。

## Owner 最新参数冻结
Owner 已批准：

- K1A pure-geographic benchmark：`beta_distance=2.0`；
- 第一条 bounded comparison：repaired equal-share `beta_distance=0` vs pure-geographic `beta_distance=2`；
- 两条 K1A path 均 `beta_return=0`；
- K1B future benchmark preregistered：`beta_return=0.5`，但当前不授权 K1B runtime；
- K1B attractiveness 继续使用 completed-iteration raw unclipped `ra0` cross-sectional z-score，只能进入下一 outer iteration；
- K1A household payoff 暂时保持 current source-used/clipped `ra`，分类为 `K1A_SOURCE_FAITHFUL_PAYOFF_BRIDGE__NOT_FINAL_ECONOMIC_RETURN_AUTHORITY`；
- smoothing / partial adjustment = OFF；
- 第一次 K1 integration 继续 source-faithful labor；
- K2 继续不授权。

Payoff bridge 的目的只是保持 attribution：本轮改变 private-capital quantity/network，而不同时改变 household return-level law。它不代表 `[.02,.09]` 已获得经济识别。

## 当前 active bounded K1A integration
Exact task：`tasks/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_BOUNDED_INTEGRATION.md`。

任务授权将 accepted K1 successor 接入 corrected-2018 bounded route，并执行恰好两个 preregistered trajectories：

1. equal-share beta distance 0；
2. pure-geographic beta distance 2。

每条最多25 outer turns；非资本设定、初始数据、theta、payoff bridge、labor、C1公式必须一致。

本轮重点验收：

- K1 origin/national private-capital conservation；
- home retained capital；
- quantity/rah same-matrix accounting；
- C1 `GovInv=max(Ktarget-Kprivate,0)` 联合闭合；
- `Kprivate>=Ktarget` 时 GovInv=0 且 private-only overshoot 被如实保留；
- raw `ra0 = rk + profit/K - delta` decomposition；
- `.02/.09` clipping pressure/counts 在 K1 后的变化；
- equal-share vs geography 对 Kprivate、GovInv、K/Ktarget、raw/used returns、rah 和现有 convergence statistics 的差异；
- source-faithful labor 确实保持；
- corrected-2018 empirical KFE caveat 继续保留。

## 仍未解决的科学对象

K1A 完成后仍需根据新 private-K / raw-ra evidence 决定最终 household payoff-return concept。不得因为 trajectory convergence 事后修改 beta、return bounds、solver、tolerance、grid、C1 formula 或 smoothing。

K1B 只有在 K1A bounded evidence 被 Reviewer 接受后才可启动；`beta_return=.5` 虽已预注册但尚未授权运行。K2 functional form、economic distance/market size 扩展、normalized labor stack、empirical KFE production closure 均属于后续阶段。

## 当前边界

本任务不是 steady-state acceptance、annual/GE、shock/IRF、welfare 或 Results。Results eligibility 继续为 `FALSE`。
