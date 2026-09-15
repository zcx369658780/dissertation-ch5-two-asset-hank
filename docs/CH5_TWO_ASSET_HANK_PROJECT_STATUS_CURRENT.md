# Chapter 5 两资产 HANK 当前状态

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J160_BOUNDED_CROSS_STATE_CONFIRMATION_TASK_ACTIVE`。

最新 accepted mechanism candidate：`b1c4897c72e3c11c1774ec59145865ae3f5fa6ca`。
Reviewer acceptance：`docs/CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC_ACCEPTANCE.md`。
Current freeze：`docs/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION.md`。
Results eligibility=`FALSE`。

J640 mechanism diagnostic 已接受：identical frozen input 下 nonconvergence 精确复现，terminal statistic=`0.0012277767122459426`。首个 selector switching 在 iteration 2，首个 value-stat non-decrease 在 iteration 8，首个 derivative-floor hit 在 iteration 10；61 次下降、38 次 non-decrease，95 个 iteration 仍有 selector switching，无 exact period-2/3 cycle。Accepted class=`POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`。

因此 finer-J escalation route 在当前 MATLAB-faithful HJB algorithm 下关闭：不得增加 maxit、damping/relaxation/line search、修改 tolerance/floor/selector，且不再运行 J1280/J2560 以制造 convergence。Continuum-grid convergence 不是当前 source-faithful household block 的 correctness gate。

当前 practical-grid strategy：`J160` 作为 provisional working illiquid-grid density；`J320` 保留为代表状态的一次 valid high-resolution sensitivity check。该策略不声称 J160 continuum-converged 或 production-final。代表状态 J160→J320 的 `Delta At≈-0.1280`、a-CDF distance≈`0.00213`，明显小于此前 coarse refinements，而 J640 进入 chatter。

当前任务固定 `rb=.02, a=[0,100], b=[-2,20], I=20, J=160, h=1`，复用中心 `(ra=.0675,w=15.5)` accepted evidence，只 fresh 运行四个角点：`(.06,13)`, `(.06,18)`, `(.07,13)`, `(.07,18)`。每点 HJB exactly once；legal/converged 时 KFE exactly once；scientific retries=0。accepted J20 same-state evidence 仅用于 comparison，不重跑。

禁止：J320/J640/J1280 新运行、修改 I/J/domain/maxit、damping、调整 HJB/KFE science、wjt/ra recalibration、global/GE/Results runtime。

Standalone contaminated-row KFE 仍不解决 corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker。
