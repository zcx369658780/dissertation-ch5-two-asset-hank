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
10. active exact task：`tasks/CH5_MP4C_K1_J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_AUDIT.md`

当前状态：`J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_AUDIT_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_AUDIT.md`。
最新 accepted mechanism candidate：`ad4cdc8bbdf924c2ed06477abc10d1010038a5f7`。
Results eligibility=`FALSE`。

Accepted practical household grid：`I=20,J=160,a=[0,100],b=[-2,20],h=1`，仅用于 bounded diagnostics。Finer-J route 因 J640 policy/selector chatter 关闭；finer-I route 因 I40 operator illegality 关闭。禁止增加 maxit 或通过 damping/relaxation/line-search、修改 tolerance/floor/selector 来制造 convergence。

Accepted first-turn provincial HJB：25/31 converged，六省 legal nonconverged。Accepted exact replay mechanism panel：天津、山西、重庆、甘肃为 policy/selector chatter with value oscillation；江西为 derivative-floor amplification after earlier switching；贵州为 exact joint-selector period-2 recurrence without exact value recurrence。Panel=`SIX_FAILURES_HETEROGENEOUS_MECHANISMS`。

因此当前不得宣称一个共同 slow-convergence 原因，也不得直接采用统一 HJB fix 或共同 recalibration。所有六省虽在 iteration2 开始 switching，但后续 floor timing、oscillation、recurrence 不同。

Active task 是 zero-science-runtime trace audit：只分析 accepted/sealed 六省 iteration traces，定位 value-update argmax、selector switching、derivative-floor activity 与 recurrence 在 `(b,a,z)` 状态空间的边界/内部位置；缺乏 coordinate-level evidence 时必须显式 unresolved，不得猜测。

HJB=0，KFE=0，所有 model/science runtime=0。禁止新 `(ra,w)` experiments、grid/domain 或 mapping/calibration change。

Standalone contaminated-row KFE 与 unresolved corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker继续分离。

Owner 已授权 ChatGPT Reviewer 对 bounded numerical diagnostics 作预注册决策；结构方程、accepted equations/guards、主要经济校准、因果解释与 Results eligibility 仍由 Owner 决定。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
