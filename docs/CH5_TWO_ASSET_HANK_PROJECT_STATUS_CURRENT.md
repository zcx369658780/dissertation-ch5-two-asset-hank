# Chapter 5 两资产 HANK 当前状态
更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_3X3_TASK_ACTIVE`。

最新 accepted coarse scan candidate：`5f55b474780d70921bfcf3ea2f863039c61814c1`。
Reviewer acceptance：`docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_COARSE_3X3_SCAN_ACCEPTANCE.md`。
Owner/Reviewer refinement freeze：`docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_3X3_SCAN.md`。
Results eligibility=`FALSE`。

Accepted coarse scan facts：`rb=.02`；`ra={.02,.055,.09}`；`w={.8,1.05,1.3}`。9/9 HJB converged；0 hard error/invalid transition matrix；最大`A2max=.007712953842301029 < homecrit=.01`。`ra=.02/.055`在三个wage下均几乎全部质量位于结构性`amin=0`，保守分类为`QUALITY_AMBIGUOUS__OWNER_REVIEW_REQUIRED`；`ra=.09`在三个wage下均出现`amax=10`模态与约18.7%–20.9%的上界质量，分类为`BOUNDARY_CONVERGED_CANDIDATE`。粗网格没有GOOD点。

当前科学解释：HJB算法本身在该粗参数域内工作正常；主要转变沿`ra`方向发生，wage在本轮未形成HJB failure或改变lower/upper-a-boundary分类。下一步只在`.055`与`.09`之间沿`ra`细化，寻找`a`分布是否出现内部模态/内部质量带。

Active refinement exact grid：`rb=.02`；`ra={.065,.0725,.08}`；`w={.8,1.05,1.3}`。只允许这9个Cartesian points。保持accepted standalone MATLAB-faithful HJB/KFE算法、grid、numerics、FOC、selector、boundary、contaminated-row KFE不变；不得damping、solver/tolerance/grid/derivative-floor/price-guard变化，不跑global multi-province、firm、GE、IRF或Results。

每点先做MATLAB-style HJB classification；HJB converged后才跑standalone KFE，并输出`Ct,Lt,At,Bt`、a/b marginals、四个boundary mass、modal a/b、interior-a mass、top a bins、KFE mass/residual/finite receipts。重点判断是否出现从`amin`集中到interior distribution再到`amax`集中之间的过渡。

KFE caveat：accepted standalone MATLAB-faithful contaminated-row KFE仅用于独立household parameter-domain mapping；corrected-2018 multi-province finite-box upper-b leakage与MATLAB-style pinning blocker仍独立未解决。

下一gate：Builder完成active refinement task后，由ChatGPT Reviewer独立ACCEPT/REJECT并决定是否继续更窄ra refinement、冻结provisional ra health band，或重定向路线。
