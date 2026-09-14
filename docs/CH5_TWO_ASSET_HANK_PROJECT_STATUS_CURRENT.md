# Chapter 5 两资产 HANK 当前状态

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION_TASK_ACTIVE`。

最新 accepted Stage A candidate：`32763fac5a7c4a04dc8278a9069443f35c7c7e3c`。
Accepted blocked precision candidate：`e3b470f623232fcaf52ad50474178f79a2b0b9b9`。
Blocked-execution Reviewer acceptance：`docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_BLOCKED_EXECUTION_ACCEPTANCE.md`。
Repair freeze：`docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION.md`。
Results eligibility=`FALSE`。

Owner 已批准 diagnostic-only household monetary bridge `h=1`：现有 household `w/C/Tt/a/b/At/Bt` 数值暂按 k-unit diagnostic numerics 使用；这不是最终现实货币单位证明。`wjt` guard、`ra` mapping、HJB/KFE equations、rates、solver/tolerance 均继续冻结。

Accepted Stage A domain：`a=[0,100]`、`b=[-2,20]`、`I=J=20`；`rb=.02`、`ra={.06,.0675,.07}`、`w={13,15.5,18}`。9/9 HJB legal/converged，9/9 KFE-valid。Liquid result：9/9 modal `b=2.6315789473684212`，0/9 modal `b=20`，`bmax` mass 至多约 `6.13e-08`；旧 `bmax=5` upper-bound pile-up 已在该 tested real-wage grid 上清除，Stage B `bmax=50` 未触发。

Illiquid result 尚未获得 precision authority：`At≈84.02–88.86`、modal `a` 多在 `89.47`，`amax` bin mass约 `9.3%–17.4%`，`J=20` 时 `da≈5.26316`。旧域 `At≈7.14–7.33` 到扩域 `At≈84–89` 的巨大变化仍只能视为重大 domain/discretization response。

上一 precision execution 已由 Reviewer 接受为 truthful blocked execution：P1 `I=20,J={40,80,160}` 三个 HJB 均合法收敛；三次 KFE numerical solve 返回后，receipt/postprocessing route 因固定 20-bin illiquid marginal 假设拒绝 finer-J result。Scientific retries=0，P2=0。这不是 grid instability、recalibration need 或 KFE scientific failure 的证据。

当前 exact task 仅授权 grid-generic receipt/postprocessing repair，并在 repair tests 通过后重新执行同一 frozen P1 ladder；accepted HJB/KFE numerical solver、equations、parameters、bounds、wage/return mapping、guards 均不得改变。P2 仍只在原 preregistered P1 stabilization 条件满足时运行。

Owner 已授权 ChatGPT Reviewer 对这类 bounded 本地数值调试直接预注册并发布 exact task；结构性经济模型、accepted equations/guards、主要校准目标、因果解释和 Results eligibility 仍保留 Owner authority。

Standalone contaminated-row KFE 仍不解决 corrected-2018 multi-province finite-box upper-`b` leakage / MATLAB-style pinning blocker。Results eligibility=`FALSE`。
