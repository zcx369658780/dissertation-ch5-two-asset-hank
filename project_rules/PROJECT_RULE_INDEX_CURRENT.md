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
9. `docs/CH5_MP4C_K1_QUARTERLY_HJB_VS_ANNUAL_FIRM_FLOW_PROVENANCE_CLOSURE_ACCEPTANCE.md`
10. `docs/CH5_MP4C_K1_ANNUAL_HJB_COMPLETE_RECALIBRATION_CONTRACT_FREEZE_CURRENT.md`
11. `docs/CH5_MP4C_K1_ANNUAL_HJB_RECALIBRATED_G1_GUARD_BOUNDED_RUNTIME_DIAGNOSTIC_ACCEPTANCE.md`
12. 若存在 active task，再读取 exact task及直接相关 report/evidence。

当前状态：`K1_ANNUAL_HJB_G1_SHORT_HORIZON_DIAGNOSTIC_ACCEPTED__RETURN_GUARD_FULLY_SATURATED__WAGE_GUARD_HIGHLY_SATURATED__OWNER_NUMERAIRE_AND_GUARD_CALIBRATION_DECISION_REQUIRED`。
当前 active Builder task：NONE。
最新 accepted annual-G1 candidate：`a7eccde5e0ca694f95d3b3c082bfa82e0ce8cbb1`。
Results eligibility=`FALSE`。

Owner annual continuous-time recalibration 已真实运行并通过 short-horizon accounting/provenance/hard-stop gates。Annual unguarded U treatment HJB convergence=`11/124`；G1=`18/124`。Annual recalibration 使 turn1 raw `ra0` 相对 `.025` evidence 每省约下降 `.075`，但未解决 household HJB 稳定性。

G1 return guard `[-.05,.20]` 在 treatment 中 `124/124` 全部 upper-saturated，导致进入HJB的 `r_a` 全部为 `.20`，guard 前仍存在的省际 payoff ranking 被完全压平。Existing wage guard `[.8,1.3]` 在G1中 `112/124`（90.3%）饱和。G1只接受为 temporary numerical scaffolding，不授权 longer G1；也不得自动进入 G2。

下一 gate 属于 Owner scientific decision：必须决定 annual household asset numeraire / firm-to-household wage scaling / wage guard policy 与下一 return-guard stage 是否联合重标定。确认前不得发布 successor task、不得 longer G1/G2、不得进入 K1B/K2。

K1 bilateral capital network 继续为 accepted bounded-runtime authority；KFE finite-box upper-b leakage/MATLAB-style pinning仍是独立 blocker，KFE=`DIAGNOSTIC_ONLY`。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复自动附Codex启动prompt。
