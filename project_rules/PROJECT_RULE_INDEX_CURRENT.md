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
11. 当前 active exact task 及直接相关 report/evidence。

当前状态：`K1_ANNUAL_HJB_COMPLETE_RECALIBRATION_FROZEN__G1_GUARDED_BOUNDED_RUNTIME_DIAGNOSTIC_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_ANNUAL_HJB_RECALIBRATED_G1_GUARD_BOUNDED_RUNTIME_DIAGNOSTIC.md`。
最新 accepted provenance candidate：`c94352740f4390bbf2fbaecae93c486395afe83f`。
Results eligibility=`FALSE`。

Owner 已完成新的 annual continuous-time recalibration freeze：`rho=.05/year`、`rb=.02/year`、borrowing gap `.07/year`、`delta=.10/year`、`Q_z=1/3 per year`；corrected annual `Y/K` 与 profit/K 不做 `/4`；raw payoff 为 `ra0_annual=rk+after_tax_profit_over_K-.10`；`rah=S'ra0_annual`；`chi0=.1`、`chi1=2 years` 暂作为 provisional annual calibration。该 contract 是新的 Owner calibration choice，不是对 legacy source 的回溯性证明。

第一阶段 diagnostic guard G1 已 preregister：HJB `r_a` 在 annual conversion 后 guard 到 `[-.05,.20]`；existing `wjt [.8,1.3]` 继续只作为 temporary diagnostic guard。必须保存 raw/converted/guarded receipts 与 saturation counts。return relaxation ladder 为 `G1 [-.05,.20] -> G2 [-.10,.35] -> G3 [-.20,.60] -> G4 OFF`，当前只授权 G1。

当前 bounded task 比较 annual unguarded U 与 annual guarded G1 两条最多5-turn路径，turn1使用共同bootstrap；turns2-5 使用各自 prior-completed annual raw `ra0@S`，仅 G1 在 HJB interface 施加 return guard。K1 capital network、same-S、fixed theta、beta_distance=2、beta_return=0、source-faithful labor、C1 与 solver/grid/tolerance 保持不变。

任何 guard-dependent steady state 只能称 provisional。不得进入25-turn Raw、K1B/K2或Results。KFE finite-box upper-b leakage/MATLAB-style pinning仍为独立 blocker，KFE=`DIAGNOSTIC_ONLY`。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复自动附Codex启动prompt。
