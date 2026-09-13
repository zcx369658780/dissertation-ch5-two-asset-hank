# Chapter 5 两资产 HANK 当前状态

更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_TASK_ACTIVE`。

最新 accepted refinement candidate：`cdaba87bae181280e182f639d4cf8fa5a5bae773`。
Reviewer acceptance：`docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_3X3_SCAN_ACCEPTANCE.md`。
Owner/Reviewer narrow-frontier freeze：`docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_REFINEMENT_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_SCAN.md`。
Results eligibility=`FALSE`。

Accepted previous refinement facts：`rb=.02`；`ra={.065,.0725,.08}`；`w={.8,1.05,1.3}`。9/9 HJB legal and converged；最大 `A2max=7.10543e-15`。只有 `ra=.065,w={1.05,1.3}` 为 `INTERIOR_A_DISTRIBUTION_CANDIDATE`；`ra=.065,w=.8` transitional；`ra=.0725,w=.8` upper-bound，`w={1.05,1.3}` ambiguous；`ra=.08` 三个 wage 全部 upper-bound。transition materially depends on wage；尚无 wage-robust connected interior `ra` band。

当前 exact narrow grid：`rb=.02`；`ra={.06,.0675,.07}`；`w={.8,1.05,1.3}`，仅这9个 Cartesian points。每点 fresh MATLAB-style initialization；只允许 `r_a` 和 household wage 变化。HJB/KFE algorithm、grid、numerics、FOC、selector、boundary、derivative floor、contaminated-row KFE 全部冻结；不得 damping/relaxation、price guard、solver/tolerance/ceiling/grid 改动，不跑 global multi-province、firm、GE、IRF 或 Results。

任务目标：判断 narrower frontier 内是否存在至少一个对三个 wage 都为内部 `a` 分布的 `ra`，从而支持 provisional wage-robust health band；如果仍不存在，则停止盲目一维加密，下一 Owner gate 转向二维 wage-conditional `(ra,w)` health-region / provincial return-mapping review。

KFE caveat：accepted standalone MATLAB-faithful contaminated-row KFE 仅用于 household parameter-domain mapping；corrected-2018 multi-province finite-box upper-b leakage 与 MATLAB-style pinning blocker 仍独立未解决。

下一 gate：Builder 完成 active task 后，由 ChatGPT Reviewer 独立 ACCEPT/REJECT。
