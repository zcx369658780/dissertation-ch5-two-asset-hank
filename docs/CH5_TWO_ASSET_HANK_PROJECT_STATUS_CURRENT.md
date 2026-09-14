# Chapter 5 两资产 HANK 当前状态

更新：2026-09-14。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`ASSET_DOMAIN_STAGE_A_BOUNDARY_CLEARED__PRECISION_SENSITIVITY_REQUIRED`。

最新 accepted design-audit candidate：`6b89d8e47f075906d463f58f3e984bf8665710f6`。
Reviewer acceptance：`docs/CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT_ACCEPTANCE.md`。
Owner/Reviewer diagnostic freeze：`docs/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_BRIDGE_AND_ASSET_DOMAIN_DIAGNOSTIC_FREEZE_CURRENT.md`。
最新完成 Builder task：`tasks/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC.md`；active Builder task=`NONE`，未发布 successor task。
Results eligibility=`FALSE`。

Owner 已批准 diagnostic-only household k-unit bridge：本轮临时接受 `h=1`，即现有 household `w/C/Tt/a/b/At/Bt` 数值作为 k-unit diagnostic numerics，不做额外数值 rescale；这不是最终现实货币单位证明。`wjt` guard、`ra` mapping、HJB/KFE 算法、rates 和 tolerance 均冻结。

Stage A 已完成：`amin=0`、`amax=100`、`bmin=-2`、`bmax=20`、`I=J=20`；`rb=.02`、`ra={.06,.0675,.07}`、household composite `w={13,15.5,18}`。9/9 HJB legal/converged，9/9 KFE-valid，fresh initialization，无 warm start。

Stage A 的 liquid marginal 9/9 modal `b=2.6315789473684212`，0/9 modal `b=20`；预注册 Stage B trigger=`false`，因此 Stage B HJB/KFE 均为 0。b upper-bound pile-up 在 exact-modal diagnostic rule 下已清除，9/9 为 `B_INTERIOR_DISTRIBUTION_CANDIDATE`。

Illiquid marginal 9/9 为 `INTERIOR_A_DISTRIBUTION_CANDIDATE`，但 `At≈84.01876–88.86351`、`amax` bin mass≈`.093123–.173673`，且 `da≈5.26316`。这是强 domain/precision sensitivity，不是 production adequacy 或 calibration improvement。

报告：`docs/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC_REPORT.md`。Compact evidence：`docs/evidence/ch5_mp4c_k1_household_k_unit_asset_domain_stagewise/`。Scientific retries=0；global/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results=0。

唯一下一 gate：`OWNER_REVIEW_ASSET_DOMAIN_STAGE_A_ACCEPTANCE_AND_PRECISION_SENSITIVITY`。`I=J=20` 仍仅有 domain-diagnostic authority；production 前必须独立 precision-sensitivity gate。

Owner 已授权 ChatGPT Reviewer 对后续类似的小范围、本地数值校准/调试做 bounded 决策并直接发布 exact task，以加快进度；前提是决定预注册、范围有限、不改变 accepted equations/guards/causal interpretation/Results eligibility，结构性经济模型变更仍保留 Owner authority。

重要 caveat：accepted standalone contaminated-row KFE 仍不解决 corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker。
