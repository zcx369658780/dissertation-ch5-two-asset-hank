# Chapter 5 当前交接 — household k-unit asset-domain Stage A candidate

更新：2026-09-14。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

Baseline：`9f6d99a32e8feb00cbae0a3a4749c331975fa587`（fresh-fetched `origin/main`）。

Branch：`codex/ch5-mp4c-k1-household-k-unit-asset-domain-stagewise-20260914`。

Worktree：`D:\ProjectTemp\ch5-mp4c-k1-household-k-unit-asset-domain-stagewise-20260914-001`。

状态：`ASSET_DOMAIN_STAGE_A_BOUNDARY_CLEARED__PRECISION_SENSITIVITY_REQUIRED`。

Exact Builder task 已完成，active Builder task=`NONE`；未发布 successor task。Results eligibility=`FALSE`。

报告：`docs/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC_REPORT.md`。

Compact evidence：`docs/evidence/ch5_mp4c_k1_household_k_unit_asset_domain_stagewise/`。External sealed evidence：`D:\ProjectTemp\ch5-mp4c-k1-household-k-unit-asset-domain-stagewise-evidence-20260914-001`。

Stage A：temporary household bridge `h=1`；`a=[0,100]`、`b=[-2,20]`、`I=J=20`；exact `rb=.02 × ra={.06,.0675,.07} × w={13,15.5,18}` grid。9/9 HJB legal/converged；9/9 KFE-valid；fresh initialization，无 warm start。

Liquid result：9/9 raw modal `b=2.6315789473684212`，0/9 modal `b=20`；9/9 `B_INTERIOR_DISTRIBUTION_CANDIDATE`。Stage B trigger=`false`，Stage B initialization/HJB/KFE 全部为 0。旧域 `bmax=5` mass `.130896–.683403` 降为 roundoff 至 `6.134e-08`，exact endpoint pile-up 已清除。

Illiquid result：9/9 `INTERIOR_A_DISTRIBUTION_CANDIDATE`，mode 为 `84.210526` 或 `89.473684`，但 `At≈84.01876–88.86351`、`amax` mass≈`.093123–.173673`。在 `da≈5.26316` 下分布明显靠近上域，必须保留 domain/precision caveat；不是 production adequacy、GE 或 calibration improvement。

KFE：residual `4.909e-17–1.645e-16`；raw density min `-4.352e-18–0`，negative count `0–348`，均在 preregistered `100*epsilon` rounding band 内，未 clip。仅使用 accepted standalone contaminated-row KFE；multi-province finite-box/pinning blocker 仍独立存在。

Call ledger：Stage A HJB=`9`、KFE=`9`；Stage B HJB=`0`、KFE=`0`；scientific retries=`0`；engineering retries=`1`（首个 HJB 前）；global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results=`0`。

唯一下一 gate：`OWNER_REVIEW_ASSET_DOMAIN_STAGE_A_ACCEPTANCE_AND_PRECISION_SENSITIVITY`。

先由 ChatGPT Reviewer 独立 ACCEPT/REJECT candidate；不要 merge main，不要发布 successor task。
