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
11. `docs/CH5_MP4C_K1_G1_VS_G2_HA_HJB_INSTRUMENTED_BOUNDED_DIAGNOSTIC_ACCEPTANCE.md`
12. 若存在 active exact task，再读取任务及直接相关 report/evidence。

当前状态：`K1_G1_VS_G2_INSTRUMENTED_HA_HJB_DIAGNOSTIC_ACCEPTED__OWNER_HA_NUMERICAL_CONTRACT_DECISION_REQUIRED`。
当前 active Builder task：NONE。
最新 accepted instrumented candidate：`5d28382f5914d161817642bab9f3c6d73b41c935`。
Results eligibility=`FALSE`。

Accepted instrumented diagnostic 已定位 turn2 common-entering-state mechanism：iteration1 derivatives/floors/candidates/selectors仍一致，最先差异来自不同 frozen return guard 产生的 effective illiquid-return contribution 与 `mu_a` / a-drift assembly；operator与value update随即分叉。Iteration2 后 value derivatives 与 transfer candidates开始全面分叉，derivative-floor differences更晚出现。

湖北 turn2 interior checkpoint 显示 huge transfer/cost 的 raw pre-selector `d_bb` candidate 在最终 selection 前已爆炸，因此 selector不是最初放大器；现行 value-derivative driven transfer FOC 与 quadratic adjustment-cost candidate-admissibility contract 是下一 Owner scientific decision 的核心对象。

不得由 Builder自行改 `chi0/chi1`、derivative floor、return/wage guards、boundary law、grid、tolerance或solver。不得 longer G2、G3/G4、wage relaxation、K1B/K2。Price-bound hit monitoring继续强制；理想稳态目标仍为 `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。

KFE finite-box upper-b leakage/MATLAB-style pinning仍为独立 blocker，KFE=`DIAGNOSTIC_ONLY`；standalone KKT residual=`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复必须附Codex启动prompt。
