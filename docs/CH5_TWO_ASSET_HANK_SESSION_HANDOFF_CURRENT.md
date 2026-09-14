# Chapter 5 当前交接 — household asset-grid precision sensitivity active

更新：2026-09-14。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_DIAGNOSTIC_TASK_ACTIVE`。

最新 accepted Stage A candidate：`32763fac5a7c4a04dc8278a9069443f35c7c7e3c`。
Reviewer acceptance：`docs/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC_ACCEPTANCE.md`。
Precision freeze：`docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_FREEZE_CURRENT.md`。
Active task：`tasks/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_DIAGNOSTIC.md`。
Results eligibility=`FALSE`。

Accepted Stage A facts：temporary diagnostic household bridge `h=1`；`a=[0,100]`、`b=[-2,20]`、`I=J=20`；`rb=.02`、`ra={.06,.0675,.07}`、`w={13,15.5,18}`。9/9 HJB legal/converged，9/9 KFE-valid。Liquid marginal 9/9 modal `b=2.6315789473684212`，0/9 modal `b=20`，`bmax` mass至多约 `6.13e-08`；旧 `bmax=5` pile-up 已清除，Stage B `bmax=50` 未触发。

Illiquid result 尚未获得 precision authority：`At≈84.02–88.86`、modal `a` 多在 `89.47`、`amax` bin mass约 `9.3%–17.4%`，`J=20` 的 `da≈5.26316`。旧域 `At≈7.14–7.33` 到扩域 `At≈84–89` 是重大 domain/discretization response，不得解释为 calibration improvement。

当前 precision task representative state 固定为 `rb=.02,ra=.0675,w=15.5,a=[0,100],b=[-2,20],h=1`。Stage P1 复用 accepted `I=20,J=20` reference，新跑 `I=20,J={40,80,160}` 三点。比较 `J20→40→80→160` 的 `At/Bt/Ct/Lt`、modal `a`、endpoint mass 与 full-marginal distances；无 post-result fitted threshold。

只有 P1 到 `J=160` 描述性稳定且 HJB/KFE 正常，才触发 Stage P2：固定 `J=160`，复用 `I=20` reference，新跑 `I={40,80}` 两点。若 P1 不稳定，P2 必须为 0。即使 P1/P2 稳定，本任务也禁止自动运行 finer full 3×3；由 ChatGPT Reviewer 决定最小 cross-state confirmation。

Runtime budget：P1 新 HJB exactly 3、KFE<=3；P2 若触发则新 HJB exactly 2、KFE<=2；scientific retries=0；global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results=0。

Owner 已授权 ChatGPT Reviewer 对后续相似的小范围、本地数值校准/调试直接做 bounded、预注册决策并发布 exact task；结构性模型、accepted equations/guards、主要经济校准、因果解释或 Results eligibility 变更仍需 Owner authority。

Standalone contaminated-row KFE 不解决 corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker。Builder完成当前 precision task 后 STOP，交 ChatGPT Reviewer 独立验收并按证据继续 bounded numerical gate。
