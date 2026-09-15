# Chapter 5 当前交接 — J160 liquid-grid bounded precision sensitivity active

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY_TASK_ACTIVE`。

最新 accepted cross-state candidate：`0430057603da6fb83ae4731ce4139def149c090c`。
Acceptance：`docs/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION_ACCEPTANCE.md`。
Freeze：`docs/CH5_MP4C_K1_J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY_FREEZE_CURRENT.md`。
Active task：`tasks/CH5_MP4C_K1_J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY.md`。
Results eligibility=`FALSE`。

J160 cross-state confirmation 已正式通过：四个 fresh corners HJB 4/4 legal/converged、KFE 4/4 valid/nonpathological；accepted center reuse-only。五态在 `a=[0,100],b=[-2,20],I=20,J=160` 下均可解释，fresh amax mass全部0，modal a/b均内部，最大 fresh bmax mass约0.01630。J160 因此是 practical bounded diagnostic grid，不是 continuum-converged/production-final authority。

J20→J160 comparison 的 unequal-support CDF repair 已接受。指标名固定为 `DOMAIN_PLUS_GRID_CDF_DISTANCE`，不得把 domain expansion + grid change 误写为 pure precision change。

Finer-J route 继续关闭：J640 已接受为 policy/selector chatter + value oscillation，禁止继续 J1280/J2560、提高 maxit 或引入 damping/relaxation/line search。J320 只保留为单点 high-resolution sensitivity evidence。

当前 exact task 只做代表中心状态的 liquid-I ladder：复用 `I20/J160`，fresh `I40/J160` 与 `I80/J160`。固定 `rb=.02,ra=.0675,w=15.5,a=[0,100],b=[-2,20],J=160,h=1`。每个新点 fresh initialization，HJB exactly once；legal/converged 才 KFE exactly once；scientific retries=0。

核心判断：`Bt`、modal b、full b-marginal、endpoint masses 和相关 aggregates 的 `I20→I40→I80` 是否描述性稳定。若 I40→I80仍明显 material，STOP；不得同任务追加 I160。若任一点 nonconverged/pathological，也 truthful STOP，不自动 mechanism replay。

Owner 已授权 ChatGPT Reviewer 对此类 bounded numerical diagnostics 直接作预注册决策；结构方程、主要经济校准、accepted equations/guards、因果解释和 Results eligibility 仍保留 Owner authority。
