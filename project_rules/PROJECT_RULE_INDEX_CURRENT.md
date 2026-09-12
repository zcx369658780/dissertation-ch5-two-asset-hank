# Chapter 5 当前规则入口
更新：2026-09-13；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

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
12. `docs/CH5_MP4C_K1_TRANSFER_CONTROL_TEMPORARY_ADMISSIBILITY_SAFEGUARD_FREEZE_CURRENT.md`
13. 当前 active exact task 及直接相关 report/evidence。

当前状态：`K1_INSTRUMENTED_HA_HJB_MECHANISM_ACCEPTED__TEMPORARY_TRANSFER_CONTROL_SAFEGUARD_POLICY_FROZEN__ZERO_SCIENCE_NUMERIC_DESIGN_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_TRANSFER_CONTROL_ADMISSIBILITY_SAFEGUARD_ZERO_SCIENCE_DESIGN.md`。
最新 accepted instrumented candidate：`5d28382f5914d161817642bab9f3c6d73b41c935`。
Results eligibility=`FALSE`。

Accepted instrumented diagnostic 已确认：turn2 common-entering-state 下最先分叉的是不同 frozen return input 导致的 effective illiquid-return contribution 与 `mu_a` / a-drift assembly；iteration2以后 value derivatives 与 transfer candidates全面分叉。湖北 turn2 extreme cell 的 raw pre-selector transfer candidate 在最终 selection 前已爆炸，因此 selector不是 initiating mechanism。

Owner 已批准建立 temporary transfer-control admissibility safeguard，但只作为 numerical continuation scaffolding。`chi0=.1`、`chi1=2 years`、derivative floor、return/wage guards、annual calibration、transfer FOC、selector/boundary law、grid/tolerance/solver及K1/C1/labor science全部继续冻结。

Safeguard 层级冻结为：raw transfer candidate 按 accepted FOC 生成后、进入 final selector / drift / cost assembly 前执行 admissibility 判断；raw candidate必须完整保存，不得把 temporary cap 描述为结构经济约束。

当前 zero-science task 只设计 exact numeric ladder与candidate semantics，不运行模型、不激活任何`d` bound。必须比较 candidate rejection、candidate clipping、fallback-to-zero/no-transfer，并基于accepted instrumented traces分析central region、heavy tail、sign/branch asymmetry和静态hit shares。若证据不足，不得发明精确阈值。

不得 longer G2、G3/G4、wage relaxation、K1B/K2。Price-bound hit monitoring继续强制；长期目标仍为`ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`，最终科学结果也不得依赖binding temporary transfer-control safeguard。

KFE finite-box upper-b leakage/MATLAB-style pinning仍为独立 blocker，KFE=`DIAGNOSTIC_ONLY`；standalone KKT residual=`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复必须附Codex启动prompt。
