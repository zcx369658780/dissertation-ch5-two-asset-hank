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
13. `docs/CH5_MP4C_K1_TRANSFER_CONTROL_ADMISSIBILITY_SAFEGUARD_ZERO_SCIENCE_DESIGN_ACCEPTANCE.md`
14. `docs/CH5_MP4C_K1_TRANSFER_CONTROL_RAW_CANDIDATE_CENSUS_INSTRUMENTED_BOUNDED_DIAGNOSTIC_ACCEPTANCE.md`

当前状态：`K1_TRANSFER_RAW_CANDIDATE_CENSUS_ACCEPTED__OWNER_NUMERIC_TRANSFER_SAFEGUARD_FREEZE_REQUIRED`。
当前 active Builder task：NONE。
最新 accepted raw-census candidate：`e6c71240e945c988958a16c67886b056376a2da4`。
Results eligibility=`FALSE`。

Accepted raw-candidate census已经完整持久化 `87,027,200` 个 raw branch-cell candidates并通过old-summary/hash exact reconcile。Pooled raw `abs(d)` median约`2.76`，p99约`2.89e3`，p99.9约`5.82e4`，p99.99约`1.02e6`，极值约`-2.785e9`到`+1.715e12`。尾部跨多个数量级连续存在；唯一巨大adjacent top-gap只隔离两个positive outliers，不能作为branch/path/turn2-robust cutoff。

Accepted exact sensitivity evidence：`|d|>1e3`=`2.145776%`，`>1e4`=`0.398441%`，`>1e5`=`0.064336%`，`>1e6`=`0.010142%`。这些不是frozen stages。

Future safeguard semantics继续首选`C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION`；candidate clipping继续nonpreferred。当前没有active `d` bound/rejection/clipping，也没有numeric ladder implementation authority。

唯一下一gate属于Owner scientific decision：`OWNER_NUMERIC_TRANSFER_SAFEGUARD_FREEZE`。Owner需选择第一套temporary transfer-control admissibility interval/ladder以及symmetric/asymmetric形式；确认前不得发布successor runtime task。

`chi0=.1`、`chi1=2 years`、derivative floor、transfer FOC、selector/boundary law、return/wage guards、annual calibration、grid/tolerance/solver、K1/C1/labor science均保持冻结。不得 longer G2、G3/G4、wage relaxation、K1B/K2、GE/IRF/Results。

Price-bound hit monitoring继续强制；长期目标仍为`ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。KFE finite-box upper-b leakage/MATLAB-style pinning仍为独立blocker，KFE=`DIAGNOSTIC_ONLY`；standalone KKT residual=`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复必须附Codex启动prompt。
