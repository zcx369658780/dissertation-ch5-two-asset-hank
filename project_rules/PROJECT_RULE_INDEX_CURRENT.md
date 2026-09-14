# Chapter 5 当前规则入口
更新：2026-09-15；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. accepted bilateral-capital / scoring-data / payoff / annual-HJB / price-guard authority docs
6. `docs/CH5_MP4C_K1_REAL_COMPOSITE_WAGE_DOMAIN_STANDALONE_3X3_AND_MACRO_SCALE_AUDIT_ACCEPTANCE.md`
7. `docs/CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT_ACCEPTANCE.md`
8. `docs/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC_ACCEPTANCE.md`
9. `docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_BLOCKED_EXECUTION_ACCEPTANCE.md`
10. `docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_FREEZE_CURRENT.md`
11. active exact task：`tasks/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION.md`

当前状态：`HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION_TASK_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION.md`。
Accepted blocked precision candidate：`e3b470f623232fcaf52ad50474178f79a2b0b9b9`。
Results eligibility=`FALSE`。

Accepted Stage A：diagnostic bridge `h=1`；`a=[0,100]`、`b=[-2,20]`、`I=J=20`；real-wage grid `rb=.02`、`ra={.06,.0675,.07}`、`w={13,15.5,18}`。Liquid upper-bound pile-up 已在 tested grid 上清除。

上一 precision execution 的 P1 HJB 3/3 legal/converged，但 KFE receipt/postprocessing 因固定 20-bin illiquid marginal 假设而失去 finer-J evidence。Reviewer 将其接受为 truthful blocked execution，不视作 grid instability、KFE scientific failure 或 recalibration evidence。

当前任务只允许 task-owned grid-generic receipt repair，并在 focused tests 通过后 fresh re-execute 同一 frozen P1 ladder；P2 仍按原 trigger。Accepted HJB/KFE science、wjt guard、ra mapping、asset bounds、rates、solver/tolerance 均冻结。禁止自动 full 3×3 finer-grid rerun。

Owner 已授权 ChatGPT Reviewer 对类似局部数值调试直接做 bounded、预注册决策并发布 exact task；结构方程、accepted equations/guards、主要经济校准、因果解释、Results eligibility 的变更仍由 Owner 决定。

Standalone contaminated-row KFE 与 unresolved corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker 继续分离。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
