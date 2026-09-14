# Chapter 5 两资产 HANK 当前状态

更新：2026-09-14。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_DIAGNOSTIC_TASK_ACTIVE`。

最新 accepted Stage A candidate：`32763fac5a7c4a04dc8278a9069443f35c7c7e3c`。
Reviewer acceptance：`docs/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC_ACCEPTANCE.md`。
Precision freeze：`docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_DIAGNOSTIC.md`。
Results eligibility=`FALSE`。

Owner 已批准 diagnostic-only household monetary bridge `h=1`：现有 household `w/C/Tt/a/b/At/Bt` 数值暂按 k-unit diagnostic numerics 使用；这不是最终现实货币单位证明。`wjt` guard、`ra` mapping、HJB/KFE equations、rates、solver/tolerance 均继续冻结。

Accepted Stage A domain：`a=[0,100]`、`b=[-2,20]`、`I=J=20`；`rb=.02`、`ra={.06,.0675,.07}`、`w={13,15.5,18}`。9/9 HJB legal/converged，9/9 KFE-valid。Liquid result：9/9 modal `b=2.6315789473684212`，0/9 modal `b=20`，`bmax` mass 至多约 `6.13e-08`；旧 `bmax=5` upper-bound pile-up 已在该 tested real-wage grid 上清除，Stage B `bmax=50` 未触发。

Illiquid result 尚未数值稳定：`At≈84.02–88.86`、modal `a` 多在 `89.47`，`amax` bin mass约 `9.3%–17.4%`，而 `J=20` 时 `da≈5.26316`。旧域 `At≈7.14–7.33` 到扩域 `At≈84–89` 的巨大变化只能视为 domain/discretization response，不能解释为 calibration improvement、GE 或 production adequacy。

当前 precision task 只使用代表性中央状态 `rb=.02, ra=.0675, w=15.5, a=[0,100], b=[-2,20]`。Stage P1 固定 `I=20`，复用 accepted `J=20` reference，新跑 `J={40,80,160}` 三点；若 P1 描述性稳定，Stage P2 才固定 `J=160`、复用 `I=20` reference，新跑 `I={40,80}` 两点。不得在本任务自动跑 finer full 3×3 grid。

Owner 已授权 ChatGPT Reviewer 对后续类似的小范围、本地数值校准/调试直接做 bounded、预注册决策并发布 exact task，以加快进度；不得据此修改结构性经济模型、accepted equations/guards、主要校准目标、因果解释或 Results eligibility，这些仍保留 Owner authority。

Standalone contaminated-row KFE 仍不解决 corrected-2018 multi-province finite-box upper-`b` leakage / MATLAB-style pinning blocker。当前唯一执行 gate 是 active precision-sensitivity exact task，完成后由 ChatGPT Reviewer 独立验收并按证据直接选择下一 bounded numerical gate。
