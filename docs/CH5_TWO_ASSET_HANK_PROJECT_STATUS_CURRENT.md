# Chapter 5 两资产 HANK 当前状态

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY_TASK_ACTIVE`。

最新 accepted cross-state candidate：`0430057603da6fb83ae4731ce4139def149c090c`。
Reviewer acceptance：`docs/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION_ACCEPTANCE.md`。
Current freeze：`docs/CH5_MP4C_K1_J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY.md`。
Results eligibility=`FALSE`。

J160 bounded cross-state confirmation 已接受：四个 fresh corner HJB 4/4 legal/converged、KFE 4/4 valid，center reuse-only；五态均无 amax 上界绑定，modal a 内部；bmax=20 无 modal pileup，fresh bmax mass 最大约0.01630。`I=20,J=160` 因此支持作为 practical bounded household diagnostic grid，但不代表 continuum convergence 或 production-final precision。

J20→J160 的 marginal comparison 采用 accepted unequal-support union-CDF 规则，并明确标记为 `DOMAIN_PLUS_GRID_CDF_DISTANCE`；该距离同时包含 domain expansion 和 discretization change，不能解释为 pure precision metric。

Accepted J640 mechanism 仍为 `POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`，所以 finer-J escalation route 保持关闭：不得增加 maxit、damping/relaxation/line search，也不得继续 J1280/J2560 以制造 convergence。J320 仅保留为代表状态 high-resolution sensitivity point。

当前剩余的本地 precision gap 是 liquid dimension。代表状态固定 `rb=.02,ra=.0675,w=15.5,a=[0,100],b=[-2,20],J=160,h=1`。复用 accepted `I=20,J=160` center，不重跑；fresh exactly 运行 `I=40,J=160` 与 `I=80,J=160`。每点 fresh initialization，HJB exactly once；legal/converged 时 KFE exactly once；scientific retries=0。

本任务只判断 `Bt`、modal b、b marginal 及相关 aggregates 随 I refinement 是否描述性稳定。禁止 I160、J change、domain/parameter change、HJB/KFE modification、recalibration、global/GE/Results runtime。

Standalone contaminated-row KFE 仍不解决 corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker。
