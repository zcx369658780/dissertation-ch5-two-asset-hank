# Chapter 5 当前规则入口
更新：2026-09-14；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

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
9. `docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_FREEZE_CURRENT.md`
10. active exact task：`tasks/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_DIAGNOSTIC.md`

当前状态：`HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_DIAGNOSTIC_TASK_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_DIAGNOSTIC.md`。
最新 accepted Stage A candidate：`32763fac5a7c4a04dc8278a9069443f35c7c7e3c`。
Results eligibility=`FALSE`。

Accepted Stage A：diagnostic bridge `h=1`；`a=[0,100]`、`b=[-2,20]`、`I=J=20`；real-wage grid `rb=.02`、`ra={.06,.0675,.07}`、`w={13,15.5,18}`。9/9 HJB legal/converged、9/9 KFE-valid；0/9 modal `b=20`，liquid upper-bound pile-up 已在 tested grid 上清除，预注册 `bmax=50` escalation 未触发。

Illiquid levels remain precision-sensitive：`At≈84–89`、modal `a` 靠近 89.47、`amax` mass约 9%–17%，且 `J=20` 的 `da≈5.26316` 很粗。当前任务只做代表性中央状态的 grid-density sensitivity，不改 domain 或经济参数。

P1：`rb=.02,ra=.0675,w=15.5,a=[0,100],b=[-2,20]`，固定 `I=20`；复用 accepted `J=20`，新跑 `J=40,80,160`。只有 P1 描述性稳定才进入 P2：固定 `J=160`，复用 `I=20`，新跑 `I=40,80`。本任务禁止自动 full 3×3 finer-grid rerun。

Owner 已授权 ChatGPT Reviewer 对类似局部数值校准/调试直接做 bounded、预注册决策并发布 exact task；结构方程、accepted equations/guards、主要经济校准、因果解释、Results eligibility 的变更仍由 Owner 决定。

HJB/KFE science、wjt guard、ra mapping、asset bounds、rates、solver/tolerance 均冻结。Standalone contaminated-row KFE 与 unresolved corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker 继续分离。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
