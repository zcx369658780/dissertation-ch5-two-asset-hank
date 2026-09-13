# Chapter 5 两资产 HANK 当前状态

更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_3X3_CANDIDATE_PUBLISHED__INDEPENDENT_REVIEW_REQUIRED`。

Baseline：`c58a64b65ce948f8ddc47dfe8c4fd3a3dc060921`。Branch：`codex/ch5-mp4c-k1-hjb-ra-transition-3x3-20260913`。Worktree：`D:\ProjectTemp\ch5-mp4c-k1-hjb-ra-transition-3x3-20260913-001`。

Exact Builder task 已完成，active Builder task=`NONE`；未发布 successor task。Results eligibility=`FALSE`。

报告：`docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_3X3_SCAN_REPORT.md`。

Terminal classification：`ALL_HJB_LEGAL_CONVERGED__INTERIOR_ONLY_AT_RA_0P065_HIGHER_WAGES__WAGE_DEPENDENT_TRANSITION__RA_0P08_UPPER_BOUNDARY`。

Exact grid：`rb=.02`；`ra={.065,.0725,.08}`；`w={.8,1.05,1.3}`。HJB `9/9`、KFE `9/9`、scientific/engineering retries `0/0`。9/9 HJB legal and converged；interior candidates `2`、ambiguous `3`、upper-bound pile-up `4`、lower-bound dominated `0`。只有 `ra=.065,w={1.05,1.3}` 为 interior candidates；`ra=.08` 三点均以 `amax` 为模态。transition materially depends on wage；不存在跨三个 wage 的 connected nondegenerate interior `ra` band。

输入不变性：九点分别 fresh initialization；仅 `inputs.r_a` 和 `inputs.wages[0]` 变化，unexpected varying fields=`[]`。global outer turn/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results 均为 `0`。

Compact evidence：`docs/evidence/ch5_mp4c_k1_standalone_hjb_ra_transition_refinement_3x3/`，sealed-manifest SHA-256=`D212336DF265B961CF78695B92B23CCFA298D8787FE0D8DE0D7D0419F7650322`。External evidence：`D:\ProjectTemp\ch5-mp4c-k1-hjb-ra-transition-refinement-3x3-evidence-20260913-001`，sealed-manifest SHA-256=`466A0DFB7E31082173AA7E95C0F1C5217F4FD29045F4E1F722566BD8395D1D5E`。

KFE caveat：accepted standalone MATLAB-faithful contaminated-row KFE 仅用于 household parameter-domain mapping；corrected-2018 multi-province finite-box upper-b leakage 与 MATLAB-style pinning blocker 仍未解决。

唯一当前 gate：ChatGPT Reviewer 独立 ACCEPT/REJECT。建议但未授权/未执行/未发布的唯一后续 gate 为 `OWNER_REVIEW_NARROWER_RA_REFINEMENT_AROUND_WAGE_DEPENDENT_FRONTIER`，候选 grid `rb=.02`, `ra={.06,.0675,.07}`, `w={.8,1.05,1.3}`。不要 merge main。
