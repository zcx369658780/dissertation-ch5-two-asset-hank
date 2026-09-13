# Chapter 5 两资产 HANK 当前状态

更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_CANDIDATE_PUBLISHED__INDEPENDENT_REVIEW_REQUIRED`。

Baseline：`d0323df5a85617f3c856b93c88c98a08deb697be`。Branch：`codex/ch5-mp4c-k1-hjb-ra-wage-frontier-narrow-3x3-20260913`。Worktree：`D:\ProjectTemp\ch5-mp4c-k1-hjb-ra-wage-frontier-narrow-3x3-20260913-001`。

Exact Builder task 已完成，active Builder task=`NONE`；未发布 successor task。Results eligibility=`FALSE`。

报告：`docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_SCAN_REPORT.md`。

Terminal classification：`ALL_HJB_LEGAL_CONVERGED__NO_WAGE_ROBUST_INTERIOR_RA__TWO_DIMENSIONAL_HEALTH_REGION_REQUIRED`。

Exact grid：`rb=.02`；`ra={.06,.0675,.07}`；`w={.8,1.05,1.3}`。HJB `9/9`、KFE `9/9`、scientific/engineering retries `0/0`。全部 HJB legal/converged；lower `2`、interior `2`、ambiguous `4`、upper-bound `1`。Interior candidates 仅为 `(.06,1.3)` 和 `(.0675,1.3)`；没有任何 tested `ra` 对三个 wage 都 interior，也没有 connected wage-robust interior `ra` band。

输入不变性：九点分别 fresh initialization；仅 `inputs.r_a` 与 `inputs.wages[0]` 变化，unexpected varying fields=`[]`，all non-scanned fields identical=`true`。global outer turn/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results 均为 `0`。

重要限制：`.06,w=.8` contaminated-row KFE 有显著 signed pathology（density minimum `-.01259`、negative count `340`、`At<0`）；未裁剪。其 lower label 仅为 raw modal/dominance 描述，不是 admissibility claim。

Compact evidence：`docs/evidence/ch5_mp4c_k1_standalone_hjb_ra_wage_frontier_narrow_3x3/`，sealed-manifest SHA-256=`AEDC537B4A1E67D3E750876319B59DFBC306C6DD0665723CF979400C250AFD58`。External evidence：`D:\ProjectTemp\ch5-mp4c-k1-hjb-ra-wage-frontier-narrow-3x3-evidence-20260913-001`，sealed-manifest SHA-256=`614D8D458DF481BD4FFCFE7688969DF7A243CC83BA6D1ED8BFDC70746E231AEF`。

KFE caveat：standalone contaminated-row KFE 不解决 corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker。

唯一当前 gate：ChatGPT Reviewer 独立 ACCEPT/REJECT。唯一建议但未授权/未执行/未发布的后续 gate：`OWNER_REVIEW_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING`。不得继续自动一维 `ra` refinement；不要 merge main。
