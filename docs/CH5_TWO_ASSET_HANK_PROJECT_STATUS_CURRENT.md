# Chapter 5 两资产 HANK 当前状态

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_DIAGNOSTIC_CANDIDATE_AWAITING_REVIEW`。

最新 accepted Stage A candidate：`32763fac5a7c4a04dc8278a9069443f35c7c7e3c`。
Reviewer acceptance：`docs/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC_ACCEPTANCE.md`。
Precision freeze：`docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_DIAGNOSTIC.md`。
Results eligibility=`FALSE`。

Owner 已批准 diagnostic-only household monetary bridge `h=1`：现有 household `w/C/Tt/a/b/At/Bt` 数值暂按 k-unit diagnostic numerics 使用；这不是最终现实货币单位证明。`wjt` guard、`ra` mapping、HJB/KFE equations、rates、solver/tolerance 均继续冻结。

Accepted Stage A domain：`a=[0,100]`、`b=[-2,20]`、`I=J=20`；`rb=.02`、`ra={.06,.0675,.07}`、`w={13,15.5,18}`。9/9 HJB legal/converged，9/9 KFE-valid。Liquid result：9/9 modal `b=2.6315789473684212`，0/9 modal `b=20`，`bmax` mass 至多约 `6.13e-08`；旧 `bmax=5` upper-bound pile-up 已在该 tested real-wage grid 上清除，Stage B `bmax=50` 未触发。

Illiquid result 尚未数值稳定：`At≈84.02–88.86`、modal `a` 多在 `89.47`，`amax` bin mass约 `9.3%–17.4%`，而 `J=20` 时 `da≈5.26316`。旧域 `At≈7.14–7.33` 到扩域 `At≈84–89` 的巨大变化只能视为 domain/discretization response，不能解释为 calibration improvement、GE 或 production adequacy。

Precision candidate terminal：`P1_KFE_EVIDENCE_UNAVAILABLE__NO_SCIENTIFIC_RETRY_AUTHORIZED`。代表状态严格固定为 `rb=.02,ra=.0675,w=15.5,a=[0,100],b=[-2,20],h=1`。P1 的 `I=20,J={40,80,160}` 三个 HJB 均合法收敛；三次 KFE 数值求解返回后，既有 wrapper 因硬编码 20-bin illiquid marginal 拒绝 finer-J receipt，故没有可恢复的 finer-grid density/aggregate/marginal evidence。Scientific retries=0，P2 HJB/KFE=0。

因此 `At/modal a/a marginal/amax mass` precision、finer-grid `Bt/b marginal` 与 `bmax=20` nonbinding 均未建立；不得把 evidence unavailable 写成 grid instability 或 recalibration evidence。当前唯一 gate 是独立 Reviewer 对 route repair / fresh exact task 的裁决；不得自行修复、重跑、merge 或发布 successor task。

Owner 已授权 ChatGPT Reviewer 对后续类似的小范围、本地数值校准/调试直接做 bounded、预注册决策并发布 exact task，以加快进度；不得据此修改结构性经济模型、accepted equations/guards、主要校准目标、因果解释或 Results eligibility，这些仍保留 Owner authority。

Standalone contaminated-row KFE 仍不解决 corrected-2018 multi-province finite-box upper-`b` leakage / MATLAB-style pinning blocker。Results eligibility=`FALSE`。
