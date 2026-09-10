# Chapter 5 当前规则入口
更新：2026-09-11；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`INITIAL_PRIVATE_K_RESIDUAL_GOVINV_PROBE_ACCEPTED__G1_ACCOUNTING_VALIDATED_UNDER_DIAGNOSTIC_BETA1__SUCCESSOR_RUNTIME_INTEGRATION_AUTHORIZED`。
当前 active Builder task：`tasks/CH5_MP4C_G1_RESIDUAL_GOVINV_INITIALIZATION_INTEGRATION_AND_25TURN_ISOLATED_DIAGNOSTIC.md`。
最新接受候选：`8df20bef54618487664ae16ea4dfe5639750cc3b`。
Reviewer acceptance：`docs/CH5_MP4C_INITIAL_PRIVATE_K_OBSERVATION_AND_RESIDUAL_GOVINV_PROBE_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

最新 initial private-K probe 已接受。accepted corrected-2018 fixed initial states/prices 下，31/31 省完成唯一一次 household observation 与一次 At-only productive-capital allocation。HJB 20/31 converged、11/31 为 `HJB_NONCONVERGED_DIAGNOSTIC_ONLY`；31/31 KFE 均为 `DIAGNOSTIC_ONLY`。在仍未生产识别、仅作 `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY` 的 `beta_a=1` 下，private-K/Track-A-target min/median/mean/max=`0.0009496604680542149/0.003209990990658578/0.005053897862873359/0.03486516202709419`。

历史 G0 `GovInv0=Ktarget` 的机械 overshoot 等于正的 initial private K；全国 overshoot=`6,633,077.122860028 MU`。候选 G1 `GovInv0=max(Ktarget-Kt_supply_initial,0)` 在 beta=1 下 31/31 private K 都低于 target，因此 31/31 accounting total-K/target 精确等于1且没有 residual-zero clipping。该结论只建立初始化会计可行性，不识别公共资本、不识别 beta_a，也不解决 HJB/KFE。

逐省 `beta_a_star=Ktarget/Kprivate(beta=1)` min/median/mean/max=`28.681926079187193/311.5273540985344/380.5993931756444/1053.007926136935`，只作为 bridge sensitivity geometry，不得当作估计的 beta_a。安徽 accepted probe：private K=`218901.27196706057 MU`，Ktarget=`70182433.35888097 MU`，G0 ratio=`1.003119032234857`，G1 residual GovInv=`69963532.08691391 MU`，G1 total-K ratio=`1`。

当前 active task 将 G1 接入一个显式 diagnostic successor initialization route，并在 Phase-A zero-science tests 通过后只运行一条最多25-turn trajectory。为了隔离 G1 初始化效应，本 task 的科学 trajectory 继续使用与已接受 G0 25-turn 基线相同的 source-faithful labor route；已接受的 origin-preserving normalized labor implementation 本轮不同时启用。历史 GovInv controller 也完全冻结不变，以区分“初始化修正”与“controller 后续行为”。

当前 task 重点比较 G0 与 G1：G1 是否消除 turn-1 `Ktarget+private K` 重复叠加；25 turns 内 unchanged controller 是否保持、侵蚀或逆转该改善；turn20-25 的 total/private/GovInv K ratios、ra/rah、KN/Y/GDP gaps 与 HJB/KFE blockers 如何变化。不得调参、不得第二 trajectory、不得修改 controller、labor normalization、HJB/KFE、bounds、grid 或 beta_a。

最新劳动实现继续作为已接受但本轮隔离的 successor capability：完整 `destination x origin` 双边矩阵、origin-column 与全国劳动守恒均已实现；source-faithful migration route仍保持不变。corrected-2018 runtime input-binding repair继续作为唯一活动数据契约：actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、`MU=10万元`、`NU=100 persons`、same-year Zt0；legacy/canonical fallback已隔离。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新科学执行必须先发布exact GitHub task；发布task时同一回复自动附Codex启动prompt。
