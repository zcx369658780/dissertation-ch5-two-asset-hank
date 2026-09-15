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
10. `docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION_ACCEPTANCE.md`
11. `docs/CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION_FREEZE_CURRENT.md`
12. active exact task：`tasks/CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION.md`

当前状态：`HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION_TASK_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION.md`。
最新 accepted precision candidate：`de4994c22303e30be9cd4c22c0a5c7f7a00db88a`。
Results eligibility=`FALSE`。

Accepted Stage A / domain authority：diagnostic bridge `h=1`；`a=[0,100]`、`b=[-2,20]`；real-wage household diagnostics only。`bmax=20` 已在 tested I20 grid 上解除旧 bmax5 exact upper-bound pile-up，但尚无 I-grid production precision authority。

Grid-generic receipt repair 已接受为 engineering-only 修复；accepted HJB/KFE numerical science、wjt guard、ra mapping、asset bounds、rates、solver/tolerance 均未改变。KFE numeric return 后须先 persist raw scientific arrays/density/support，再进入 receipt validation。

Accepted P1 representative-state precision ladder `I=20,J=20/40/80/160` 未在 J160 前稳定：At 和 modal a 继续移动，full a-marginal distance 亦无稳定趋势。Reviewer route=`FINER_PRECISION_ESCALATION`。

当前 exact task 仅运行同一代表状态的 `I=20,J={320,640,1280}`；复用 accepted J160，不得重跑。禁止 J>1280、liquid-I ladder、multi-state/finer 3x3、asset-domain change、recalibration、global model 或 Results runtime。若到 J1280 仍未稳定，必须 STOP 并转入 domain/scale review，不得无限加密。

Owner 已授权 ChatGPT Reviewer 对类似局部数值调试直接做 bounded、预注册决策并发布 exact task；结构方程、accepted equations/guards、主要经济校准、因果解释、Results eligibility 的变更仍由 Owner 决定。

Standalone contaminated-row KFE 与 unresolved corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker 继续分离。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
