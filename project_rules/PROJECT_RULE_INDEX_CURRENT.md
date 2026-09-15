# Chapter 5 当前规则入口
更新：2026-09-15；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. accepted bilateral-capital / scoring-data / payoff / annual-HJB / price-guard authority docs
6. `docs/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION_ACCEPTANCE.md`
7. `docs/CH5_MP4C_K1_J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY_ACCEPTANCE.md`
8. `docs/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_ACCEPTANCE.md`
9. `docs/CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_ACCEPTANCE.md`
10. `docs/CH5_MP4C_K1_J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_AUDIT_ACCEPTANCE.md`
11. `docs/CH5_MP4C_K1_J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC_FREEZE_CURRENT.md`
12. active exact task：`tasks/CH5_MP4C_K1_J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC.md`

当前状态：`J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC.md`。
最新 accepted spatial-audit candidate：`1e76a9222eb2ba6dff485b49f0c2c9ffa30af379`。
Results eligibility=`FALSE`。

Accepted practical household grid：`I=20,J=160,a=[0,100],b=[-2,20],h=1`，仅用于 bounded diagnostics。Finer-J route 因 J640 chatter 关闭；finer-I route 因 I40 operator illegality 关闭。禁止通过增加 maxit、damping/relaxation/line-search、修改 tolerance/floor/selector 来制造 convergence。

Accepted first-turn provincial HJB：25/31 converged，六省 legal nonconverged。Accepted exact replay mechanism panel heterogeneous：天津、山西、重庆、甘肃 chatter；江西 floor amplification after earlier switching；贵州 joint-selector period-2 recurrence without exact value recurrence。

Accepted zero-runtime spatial audit further establishes value-update argmax heterogeneity：江西、甘肃 liquid-upper-bound concentrated；天津、山西、重庆、贵州 mixed。四个 chatter provinces 也没有共同 value-argmax spatial signature。

该 spatial audit 明确没有 coordinate-level selector changed-cell 或 derivative-floor locations，因此不得把 value argmax 当成完整 instability footprint，也不得直接授权 boundary/grid/HJB/mapping/calibration change。

Active task 采用预注册 matched panel 做 coordinate-resolved observational HJB replay：失败代表 天津、江西、贵州、甘肃；成功 controls 湖南、上海、福建；expected HJB exactly7，KFE=0，scientific retries=0。目标是比较 selector-switch 与 derivative-floor spatial footprint 是否 failure-specific。禁止 synthetic points、upstream recalculation、KFE/outer/GE/Results runtime。

Standalone contaminated-row KFE 与 unresolved corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker继续分离。

Owner 已授权 ChatGPT Reviewer 对 bounded numerical diagnostics 作预注册决策；结构方程、accepted equations/guards、主要经济校准、因果解释与 Results eligibility 仍由 Owner 决定。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
