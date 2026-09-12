# Chapter 5 当前规则入口
更新：2026-09-12；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
6. `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
7. `docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`
8. `docs/CH5_MP4C_K1_PAYOFF_SCALE_MAPPING_AND_DIAGNOSTIC_BOUND_POLICY_FREEZE_CURRENT.md`
9. `docs/CH5_MP4C_K1_ANNUAL_HJB_COMPLETE_RECALIBRATION_CONTRACT_FREEZE_CURRENT.md`
10. `docs/CH5_MP4C_K1_ANNUAL_HJB_RECALIBRATED_G1_GUARD_BOUNDED_RUNTIME_DIAGNOSTIC_ACCEPTANCE.md`
11. `docs/CH5_MP4C_K1_PRICE_GUARD_CONTINUATION_AND_BOUNDARY_HIT_MONITORING_FREEZE_CURRENT.md`
12. 当前 active exact task 及直接相关 report/evidence。

当前状态：`K1_ANNUAL_HJB_G1_ACCEPTED__RA_FIRST_CONTINUATION_FROZEN__G1_VS_G2_SHORT_HORIZON_DIAGNOSTIC_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_ANNUAL_HJB_G1_VS_G2_PRICE_GUARD_CONTINUATION_DIAGNOSTIC.md`。
最新 accepted annual-G1 candidate：`a7eccde5e0ca694f95d3b3c082bfa82e0ce8cbb1`。
Results eligibility=`FALSE`。

Annual recalibration已进入accepted bounded runtime。G1 `r_a in [-.05,.20]` 在treatment中 `124/124` upper-saturated，因此G1只作为continuation起点，不授权longer G1。Owner最新澄清：legacy `ra` 与 `wjt` bounds是HA/HJB nonlinear solver safeguards；`multi_prov_HANK_12sts.m`中`wjtmin=.8`, `wjtmax=1.3`，`HANK_mp_1eq.m`会像ra一样统计wjt撞界省份。

Continuation顺序已冻结：Phase A固定`wjt [.8,1.3]`，只推进return ladder；Phase B找到可行return scaffold后再单独设计wage relaxation；Phase C逐步弱化两类guards并追求无price-guard依赖的收敛稳态。不得同时改return与wage safeguards，除非Owner另行授权。

每个runtime continuation task必须记录return和wage的upper/lower/unsaturated province names、counts、shares，并尽量保存raw/converted/guarded三层对象。长期理想目标=`ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`；任何仍依赖price guards的稳态最多是`PROVISIONAL_STEADY_STATE`。

当前exact task只比较annual G1 `[-.05,.20]` 与G2 `[-.10,.35]`，两条最多5-turn；wjt guard保持`[.8,1.3]`不变。目标是判断G2能否降低return saturation、恢复部分省际payoff variation，同时保持可接受的HJB/control/drift行为。G3/G4、longer G2、wage relaxation均未授权。

K1B/K2仍不授权。KFE finite-box upper-b leakage/MATLAB-style pinning仍为独立blocker，KFE=`DIAGNOSTIC_ONLY`。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复自动附Codex启动prompt。
