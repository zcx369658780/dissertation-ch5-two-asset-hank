# Chapter 5 两资产 HANK 当前状态

更新：2026-09-14。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC_TASK_ACTIVE`。

最新 accepted design-audit candidate：`6b89d8e47f075906d463f58f3e984bf8665710f6`。
Reviewer acceptance：`docs/CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT_ACCEPTANCE.md`。
Owner/Reviewer diagnostic freeze：`docs/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_BRIDGE_AND_ASSET_DOMAIN_DIAGNOSTIC_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC.md`。
Results eligibility=`FALSE`。

Owner 已批准 diagnostic-only household k-unit bridge：本轮临时接受 `h=1`，即现有 household `w/C/Tt/a/b/At/Bt` 数值作为 k-unit diagnostic numerics，不做额外数值 rescale；这不是最终现实货币单位证明。`wjt` guard、`ra` mapping、HJB/KFE 算法、rates 和 tolerance 均冻结。

Stage A 固定：`amin=0`、`amax=100`、`bmin=-2`、`bmax=20`、`I=J=20`；exact standalone science grid 为 `rb=.02`、`ra={.06,.0675,.07}`、household composite `w={13,15.5,18}`，共 9 点，fresh initialization，无 warm start。

预注册 Stage B：只有当 Stage A 至少一个 converged/KFE-valid point 的 liquid-asset modal `b` 精确等于 `bmax=20` 时，才运行第二个 9 点 grid，将唯一变化设为 `bmax=50`。不得进一步扩大 `bmax`。Stage B 若仍存在 exact-`bmax` mode，则停止并判定 domain/precision unresolved。

本轮目标是分离 asset-domain adequacy 与 discretization precision。`I=J=20` 只用于 first bounded domain diagnostic；即便边界问题消失，production 前仍必须独立 precision-sensitivity gate。

Owner 已授权 ChatGPT Reviewer 对后续类似的小范围、本地数值校准/调试做 bounded 决策并直接发布 exact task，以加快进度；前提是决定预注册、范围有限、不改变 accepted equations/guards/causal interpretation/Results eligibility，结构性经济模型变更仍保留 Owner authority。

重要 caveat：accepted standalone contaminated-row KFE 仍不解决 corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker。
