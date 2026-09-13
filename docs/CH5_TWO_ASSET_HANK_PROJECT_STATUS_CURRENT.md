# Chapter 5 两资产 HANK 当前状态

更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_ACCEPTED__OWNER_REVIEW_TWO_DIMENSIONAL_HEALTH_REGION_REQUIRED`。

Accepted candidate：`d1401fc5154a6fb77989b0de343da20329bf724a`。
Reviewer acceptance：`docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_SCAN_ACCEPTANCE.md`。
当前 active Builder task：NONE。Results eligibility=`FALSE`。

Accepted terminal classification：`ALL_HJB_LEGAL_CONVERGED__NO_WAGE_ROBUST_INTERIOR_RA__TWO_DIMENSIONAL_HEALTH_REGION_REQUIRED`。

Exact grid：`rb=.02`；`ra={.06,.0675,.07}`；`w={.8,1.05,1.3}`。HJB `9/9`、KFE `9/9`、scientific/engineering retries `0/0`。全部 HJB legal/converged；lower `2`、interior `2`、ambiguous `4`、upper-bound `1`。Interior candidates 仅为 `(.06,1.3)` 和 `(.0675,1.3)`；没有任何 tested `ra` 对三个 wage 都 interior，也没有 connected wage-robust scalar `ra` health band。

重要边界：`.06,w=.8` contaminated-row KFE 出现显著 signed pathology（`amin mass>1`、`amax/interior-a mass<0`、`At<0`、density minimum 约 `-.01259`）。该点的 lower label 仅描述 raw modal/dominance，不是 admissibility claim；不得裁剪后升级为健康稳态。

科学解释：当前 standalone evidence 支持健康区域是 wage-dependent 的二维 `(ra,w)` 区域，而不是 universal scalar `ra` 区间。不得继续自动一维 `ra` refinement，也不得修改 HJB/KFE 算法来扩大可行域。

Standalone contaminated-row KFE 仅用于 household parameter-domain mapping；corrected-2018 multi-province finite-box upper-b leakage 与 MATLAB-style pinning blocker 仍独立未解决。

唯一下一 Owner gate：`OWNER_REVIEW_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING`。下一步应先基于已接受 standalone evidence 构造 provisional 二维 household-health map，再审查 provincial return/wage mapping 如何把各省放入或推离该区域；尚未发布 successor runtime task。
