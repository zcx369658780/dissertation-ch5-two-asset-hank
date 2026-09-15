# Chapter 5 当前交接 — finer illiquid-grid precision escalation active

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION_TASK_ACTIVE`。

最新 accepted precision candidate：`de4994c22303e30be9cd4c22c0a5c7f7a00db88a`。
Reviewer acceptance：`docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION_ACCEPTANCE.md`。
Finer-precision freeze：`docs/CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION_FREEZE_CURRENT.md`。
Active task：`tasks/CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION.md`。
Results eligibility=`FALSE`。

上一 Builder candidate 已由 Reviewer 接受并 fast-forward。R0 grid-generic receipt repair 只修改 task-owned precision runner/finalizer/tests；accepted HJB/KFE solver、oracle、MATLAB source、经济方程、参数、bounds、guards、wage/return mappings 未改变。Focused tests=`17 passed`，R0 science HJB/KFE=`0/0`。

代表性中央状态继续冻结：`rb=.02,ra=.0675,w=15.5,a=[0,100],b=[-2,20],h=1,I=20`。

Accepted P1：复用 J20 reference，fresh 运行 J40/J80/J160。HJB=`3/3` legal/converged；KFE=`3/3` numeric-returned/persisted/valid；scientific retries=0。`At≈87.75417→87.55005→88.60704→89.29783`；modal `a≈89.47368→89.74359→92.40506→94.33962`；a-CDF distance≈`0.01261→0.01760→0.01462`。J80→J160 `ΔAt≈+0.69079`、`ΔBt≈+0.78798`，故 Reviewer 接受 terminal=`ILLIQUID_GRID_PRECISION_NOT_STABILIZED`。P2 没有触发。

当前 bounded escalation 复用 accepted I20/J160，不重跑该 science point。新运行 exactly：`I20/J320`、`I20/J640`、`I20/J1280`。每点 fresh initialization，HJB exactly once；只有合法收敛才 KFE exactly once。KFE numeric return 后必须先持久化 raw density、scientific arrays、grid supports 与 shape，再做 receipt processing。

本任务禁止 J>1280、I-grid ladder、multi-state/finer 3×3、asset-domain change、wjt/ra recalibration、HJB/KFE modification、global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results。

若 J640→J1280 相较前序 refinement 已描述性很小且 marginal sequence 明显稳定，可推荐 bounded liquid-I/cross-state confirmation；若仍 material，则停止继续 grid refinement，下一 gate 必须转为 domain/scale review。不得通过无限增加 J 制造稳定。

Owner 已授权 ChatGPT Reviewer 对类似局部数值调试直接做 bounded、预注册决策并发布 exact task；结构模型、accepted equations/guards、主要经济校准、因果解释与 Results eligibility 仍保留 Owner authority。

Standalone contaminated-row KFE 仍不解决 corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker。
