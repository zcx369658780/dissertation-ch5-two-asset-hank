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
10. `docs/CH5_MP4C_K1_PRICE_GUARD_CONTINUATION_AND_BOUNDARY_HIT_MONITORING_FREEZE_CURRENT.md`
11. `docs/CH5_MP4C_K1_G1_VS_G2_HA_HJB_MECHANISM_ZERO_SCIENCE_DIAGNOSTIC_ACCEPTANCE.md`
12. 当前 active exact task 及直接相关 report/evidence。

当前状态：`K1_G1_VS_G2_MECHANISM_ZERO_SCIENCE_ACCEPTED__INSTRUMENTED_HA_HJB_DIAGNOSTIC_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_G1_VS_G2_HA_HJB_INSTRUMENTED_BOUNDED_DIAGNOSTIC.md`。
最新 accepted G1-vs-G2 runtime candidate：`ab6b19022d920a8929a2ee66cc5511be6f602557`。
最新 accepted zero-science mechanism candidate：`f7c52f061b9eb3666d26985602ad6527774b5bb2`。
Results eligibility=`FALSE`。

Accepted G1/G2 continuation 已确认：G2降低return saturation并恢复部分省际payoff variation，但HJB convergence从G1 `18/124`降至G2 `6/124`，且多项control/cost/drift极值扩大；因此longer G2、G3/G4均未授权。wjt `[.8,1.3]`保持固定，price-bound hit monitoring继续强制执行。

Accepted zero-science mechanism forensic进一步确认：G2 stress在newly-unsaturated与still-saturated return regimes之间呈mixed分布；top stress cells主要位于interior，outward face hits总量反而下降，故不是boundary-only failure。G1自身已有大extrema，且部分G1 worst cells在G2下改善。现有persisted evidence缺少value/directional derivatives、pre-selector candidates、per-iteration HJB trace与standalone KKT residual，因此不能识别return、wage、selector与path-history的先后机制。

当前exact task只增加observation-only instrumentation，重复相同annual G1/G2 5-turn scientific design。turn2为common-entering-state immediate-response窗口；turns3-5必须标记为path-history propagation。必须持久化HJB iteration trace、existing directional/value derivatives、derivative-floor activations、pre-selector candidate controls/drifts/costs/selector criteria以及selected policy，并保持所有科学输出与instrumentation-off路径一致。

任何参数、guard、annual calibration、equation、grid、tolerance、solver、boundary/KKT、capital network、C1或labor science均不得修改。Builder不得自行调`chi0/chi1`、derivative floor、return/wage guards。K1B/K2继续不授权。KFE finite-box upper-b leakage/MATLAB-style pinning仍为独立blocker，KFE=`DIAGNOSTIC_ONLY`。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复自动附Codex启动prompt。
