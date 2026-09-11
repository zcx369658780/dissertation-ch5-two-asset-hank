# Chapter 5 当前规则入口
更新：2026-09-11；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
6. `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
7. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`K1A_STATIC_MAPPING_ACCEPTED__BETA_DISTANCE_2_FROZEN__BETA_RETURN_POINT5_PREREGISTERED__BOUNDED_K1A_INTEGRATION_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_BOUNDED_INTEGRATION.md`。
最新 accepted K1A zero-science candidate：`2ad7c74876d91326c127d8c7ef1c400991320968`。
Reviewer acceptance：`docs/CH5_MP4C_K1A_2018_DISTANCE_SCORE_MAPPING_AND_STATIC_PORTFOLIO_DIAGNOSTIC_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

资本网络总体科学设计冻结稿：
`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。
K1 scoring/data 当前冻结稿：
`docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`。

Owner 已根据 zero-science static diagnostics 冻结第一条 K1A runtime 比较：repaired equal-share `beta_distance=0` 对 pure-geographic `beta_distance=2`，两者均 `beta_return=0`。K1B `beta_return=.5` 已预注册但尚未授权运行。第一版 K1A household payoff 继续使用 current source-used/clipped `ra`，仅作为 `K1A_SOURCE_FAITHFUL_PAYOFF_BRIDGE__NOT_FINAL_ECONOMIC_RETURN_AUTHORITY`，用于保持资本网络变化的归因；这不认可历史 `[.02,.09]` 为最终经济回报区间。

K1A/K1B 继续固定 `theta_i=inter_prv_ratio_i`。foreign destination shares 采用 accepted `destination x origin` 资本矩阵；quantity 与 `rah` 使用同一 `S`。same-turn return feedback 禁止；K1B 未来只能使用 completed-iteration raw unclipped `ra0` z-score进入下一 outer iteration。第一版 smoothing/partial adjustment 关闭，第一次 K1 integration 继续 source-faithful labor。

当前 exact task 授权的科学执行仅为两条 corrected-2018 bounded K1A diagnostic trajectories：equal-share beta 0 与 geography beta 2；每条最多25 outer turns。任务必须重验 K1 private-capital conservation、C1 `GovInv=max(Ktarget-Kprivate,0)`、private-only overshoot、raw-ra decomposition/clipping pressure，并保持 source-faithful labor。K1B/K2、standalone KFE、steady-state acceptance、annual/GE/IRF/Results 均不在本任务范围。

C1 residual public-asset authority继续有效。KFE治理继续区分 clean/source-free generator-KFE 方法学与 corrected-2018 empirical finite-box upper-b leakage/pinning blocker。任何 bounded K1A PASS 均不能被写成 KFE 或 Results 已通过。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复自动附Codex启动prompt。
