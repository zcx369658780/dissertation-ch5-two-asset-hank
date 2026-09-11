# Chapter 5 当前规则入口
更新：2026-09-11；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`C1_GOVINV_RESIDUAL_LEVEL_REPLACEMENT_ACCEPTED__PURE_PUBLIC_ASSET_RESIDUAL_IMPLEMENTED__STATIC_G1_REPLAY_FULLY_CLOSES_HISTORICAL_GOVINV_OVERSHOOT__BOUNDED_RUNTIME_INTEGRATION_AUTHORIZED`。
当前 active Builder task：`tasks/CH5_MP4C_C1_RESIDUAL_PUBLIC_ASSET_25TURN_CONTEMPORANEOUS_INTEGRATION_DIAGNOSTIC.md`。
最新接受候选：`77c17f224c466720b4c7e67250513817f584d1f8`。
Reviewer acceptance：`docs/CH5_MP4C_C1_GOVINV_RESIDUAL_LEVEL_REPLACEMENT_IMPLEMENTATION_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

C1 pure public-asset residual implementation 已接受。独立API `residual_government_asset_level(s)` 实现 `GovInv=max(Ktarget-Kprivate_current,0)`，没有 gain、ra target、damping、hysteresis，也未连接 active steady-state runtime。private K 低于 target 时 accounting firm K 精确等于 target；private K 达到/超过 target 时 GovInv floor 为0并显式保留 private overshoot。历史 C0 clipped-return controller 继续保持 byte-identical/source-faithful authority。

对 accepted G1 25-turn ledger 的 zero-science static replay 显示 775/775 rows private K 都低于 Ktarget，因此 C1 静态 replacement 全部精确闭合到 target。turn20-25 historical total-K/target median=`2.353363495591088`，static C1 median=`1.0`；pooled late historical positive overshoot `19,963,597,940.767487 MU` 在 static accounting 中全部由 residual replacement 消除，remaining private-only overshoot=`0 MU`。这些是静态 accounting counterfactual，不是动态稳定性证据。

Owner 已冻结 GovInv 的经济解释：GovInv 为不可直接观测的政府/公共生产性资产，用于填补经验 total productive capital 与 household/private productive capital 之间的缺口。C1 因而是 level definition，而不是 calibrated controller gain。

当前 active task 将 C1 接入一个显式 successor numerical steady-state one-turn route，并只运行一条最多25-turn bounded diagnostic。关键 timing 被定义为：每个 outer numerical iteration 在 household outputs 和 At-only private-capital allocation 后，使用 contemporaneous `Kprivate` 计算 C1 GovInv，再进入同一 turn firm evaluation。因此这是 steady-state 数值迭代中的 contemporaneous stock identity，不应解释成真实时间内政府资产瞬时调整。

为了单独识别资本块，本次 scientific trajectory 继续使用 source-faithful migration/labor route，已接受的 origin-preserving normalized labor successor 不激活；wage、firm、Zt、tKNratio、HJB/KFE、bounds、grid、solver均冻结。C1 successor route 中只禁用历史 GovInv `0.9/1.1` return-bound action，历史 C0 本身不得修改。

此前 accepted G1+C0 scientific FAIL 继续有效：G1 initialization 能31/31对齐初始 Ktarget，但 historical C0 随后重建 GovInv overshoot。HJB/KFE blockers继续独立存在，beta_a仍为 `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`。

corrected-2018 runtime input-binding repair继续作为唯一活动数据契约：actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、`MU=10万元`、`NU=100 persons`、same-year Zt0；legacy/canonical fallback已隔离。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新科学执行必须先发布exact GitHub task；发布task时同一回复自动附Codex启动prompt。
