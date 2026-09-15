# Chapter 5 当前规则入口
更新：2026-09-15；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. accepted bilateral-capital / scoring-data / payoff / annual-HJB / price-guard authority docs
6. `docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION_ACCEPTANCE.md`
7. `docs/CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION_ACCEPTANCE.md`
8. `docs/CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC_ACCEPTANCE.md`
9. `docs/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION_FREEZE_CURRENT.md`
10. active exact task：`tasks/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION.md`

当前状态：`J160_BOUNDED_CROSS_STATE_CONFIRMATION_TASK_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION.md`。
最新 accepted mechanism candidate：`b1c4897c72e3c11c1774ec59145865ae3f5fa6ca`。
Results eligibility=`FALSE`。

Accepted J640 mechanism：`POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`。Selector switching 早于 value-stat non-decrease，后者又早于 derivative-floor activation；无 exact period-2/3 cycle。Finer-J escalation 在 accepted MATLAB-faithful HJB 下关闭，不得增加 maxit、damping/relaxation/line search 或继续 J1280/J2560 制造 convergence。

Practical-grid strategy：J160 暂作为 bounded cross-state diagnostic working grid；J320 仅为代表状态 high-resolution sensitivity check。不得宣称 J160 continuum-converged 或 production-final。

当前 exact task 只允许 fixed `I=20,J=160,a=[0,100],b=[-2,20],rb=.02,h=1` 的四个 fresh corner states：`(.06,13)`, `(.06,18)`, `(.07,13)`, `(.07,18)`；中心 `(.0675,15.5)` 复用 accepted evidence。每点 HJB exactly once，legal/converged 时 KFE exactly once，scientific retries=0。accepted J20 same-state evidence仅作比较，不重跑。

禁止 J320/J640/J1280 新 runtime、I-grid ladder、domain change、recalibration、global model 或 Results。

Owner 已授权 ChatGPT Reviewer 对类似局部数值调试直接做 bounded、预注册决策并发布 exact task；结构方程、accepted equations/guards、主要经济校准、因果解释、Results eligibility 的变更仍由 Owner 决定。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
