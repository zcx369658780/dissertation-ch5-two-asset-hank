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
9. `docs/CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_FREEZE_CURRENT.md`
10. active exact task：`tasks/CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_DIAGNOSTIC.md`

当前状态：`J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_TASK_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_DIAGNOSTIC.md`。
最新 accepted provincial candidate：`1e9c8c6416cbd732a44d739e19b40e838993e3d4`。
Results eligibility=`FALSE`。

Accepted practical household grid：`I=20,J=160,a=[0,100],b=[-2,20],h=1`，仅用于 bounded diagnostics。Finer-J route 因 J640 policy/selector chatter 关闭；finer-I route 因 I40 operator illegality 关闭。禁止通过增加 maxit、damping/relaxation/line-search、修改 tolerance/floor/selector 来制造 convergence。

Accepted first-turn provincial viability：exact accepted 31-province household input vector authority PASS；25/31 HJB converged，天津、山西、江西、重庆、贵州、甘肃 legal nonconverged；illegal operator=0，hard error=0，31/31 max A2max<0.01。KFE=0，上游 firm/wage/return mapping 未重算。

31/31 real first-turn states 均在先前 standalone J160 rectangle 之外，而其中25个成功，因此 outside-support 本身不能解释六个失败。当前不得直接 recalibrate。

Active task 仅对六个失败省份做 identical-input、fresh-initialized、instrumentation-only HJB replay，exactly one call per province；KFE=0，scientific retries=0。目标是逐省和 panel 分类 slow/near-monotone、policy/selector chatter、floor amplification、low-period cycle、heterogeneous 或 unresolved mechanism，并用 accepted successful-province receipts 做 offline nearest-neighbor comparison。

Standalone contaminated-row KFE 与 unresolved corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker继续分离。

Owner 已授权 ChatGPT Reviewer 对 bounded numerical diagnostics 作预注册决策；结构方程、accepted equations/guards、主要经济校准、因果解释与 Results eligibility 仍由 Owner 决定。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
