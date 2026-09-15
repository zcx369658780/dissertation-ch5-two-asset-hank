# Chapter 5 两资产 HANK 当前状态

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION_TASK_ACTIVE`。

最新 accepted precision candidate：`de4994c22303e30be9cd4c22c0a5c7f7a00db88a`。
Reviewer acceptance：`docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION_ACCEPTANCE.md`。
Finer-precision freeze：`docs/CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION.md`。
Results eligibility=`FALSE`。

Diagnostic-only household monetary bridge 继续冻结为 `h=1`；代表状态固定为 `rb=.02, ra=.0675, w=15.5, a=[0,100], b=[-2,20], I=20`。这不是最终现实货币单位证明。`wjt` guard、`ra` mapping、HJB/KFE equations、rates、solver/tolerance、asset bounds 均冻结。

Grid-generic receipt repair 已接受：修复仅限 task-owned runner/finalizer/tests，不改变 accepted HJB/KFE numerical science；KFE numeric return 后先持久化 raw density/scientific arrays/grid supports，再执行 receipt validation。Focused tests=`17 passed`。

Accepted P1 precision evidence：复用 J20，fresh 运行 `J={40,80,160}`。HJB 3/3 legal/converged，KFE 3/3 numeric-returned/persisted/valid，scientific retries=0。`At` 序列约为 `87.75417 -> 87.55005 -> 88.60704 -> 89.29783`；modal `a` 约为 `89.47368 -> 89.74359 -> 92.40506 -> 94.33962`；a-marginal CDF distance 约为 `0.01261 -> 0.01760 -> 0.01462`。J80→J160 仍有 `ΔAt≈+0.69079`、`ΔBt≈+0.78798`，因此 `ILLIQUID_GRID_PRECISION_NOT_STABILIZED` 已接受，P2 未运行。

旧 `a=[0,10]` 到扩展 `a=[0,100]` 的巨大 At 跳跃现可判断主要是 domain response，因为 finer-J 后 At 仍处于 high-80s；但扩展域内最终 illiquid level/shape 尚无 precision authority。固定 I20 时 `bmax=20` 在已测试 J ladder 上保持 nonmodal，J160 bmax mass约 `0.0009774`，但尚无 I-grid precision authority。

当前 finer-precision task：复用 accepted `I=20,J=160`，不重跑；fresh 运行 exactly `J={320,640,1280}`，I 固定20，其余 science 全部不变。禁止 J>1280、liquid-I ladder、multi-state/finer 3×3、asset-domain change、recalibration、global/GE/Results runtime。

若 J640→J1280 描述性明显收敛且完整 marginal sequence 显示 stabilization，可进入 bounded liquid-I / cross-state confirmation；若到 J1280 仍明显 material，则停止继续加密，转入 domain/scale review，而不是无限增加 J。

Standalone contaminated-row KFE 仍不解决 corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker。
