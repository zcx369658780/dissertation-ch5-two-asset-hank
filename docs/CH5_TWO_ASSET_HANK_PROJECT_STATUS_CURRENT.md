# Chapter 5 两资产 HANK 当前状态

更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_COARSE_3X3_SCAN_CANDIDATE_PUBLISHED__INDEPENDENT_REVIEW_REQUIRED`。

Baseline：`45f0e3aedeb88e0dc9ca5e35e1e79664cedf2909`。

Builder branch：`codex/ch5-mp4c-k1-hjb-ra-wage-3x3-20260913`。

报告：`docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_COARSE_3X3_SCAN_REPORT.md`。

Compact evidence：`docs/evidence/ch5_mp4c_k1_standalone_hjb_ra_wage_coarse_3x3/`。

External evidence：`D:\ProjectTemp\ch5-mp4c-k1-hjb-ra-wage-3x3-evidence-20260913-001`；sealed-manifest SHA-256=`061CB52D5C5C1F2268DDFFA0A526FEF2454274C169805CE2EADBA5F7ACD746D0`。

Terminal classification：`ALL_HJB_CONVERGED__LOW_AND_MID_RA_LOWER_BOUND_AMBIGUOUS__HIGH_RA_UPPER_A_BOUNDARY_PILEUP`。

Exact 3×3 scan used `rb=.02`, `ra={.02,.055,.09}`, `w={.8,1.05,1.3}`. HJB=`9/9`, KFE=`9/9`, scientific retry=`0`; all prohibited/global runtimes=`0`. All HJBs converged and passed `A2max<=homecrit=.01`. Preliminary KFE labels are six `QUALITY_AMBIGUOUS__OWNER_REVIEW_REQUIRED` at `ra=.02/.055` and three `BOUNDARY_CONVERGED_CANDIDATE` at `ra=.09`; GOOD count is zero and no connected GOOD coarse region exists.

At low/mid `ra`, the accepted contaminated-row KFE places essentially all mass at structural `amin=0`, with mixed signed numerical-mass/raw-residual receipts; at `ra=.09`, `amax=10` is modal with mass shares `.1871–.2094`, exceeding the adjacent bin. No post-result cutoff was introduced.

Standalone KFE remains distinct from the unresolved corrected-2018 multi-province finite-box upper-b leakage/MATLAB-style pinning blocker. Results eligibility=`FALSE`。

当前 active Builder task：NONE。未发布 successor task。

唯一当前 gate：ChatGPT Reviewer 对 candidate commit、报告、compact evidence、external sealed manifest 和完整 call ledger 独立 ACCEPT/REJECT。仅作为后续 Owner/Reviewer 决策建议：若接受，可审议一个未执行的 `ra={.065,.0725,.08} × w={.8,1.05,1.3}` refinement gate；本 candidate 不授权执行。
