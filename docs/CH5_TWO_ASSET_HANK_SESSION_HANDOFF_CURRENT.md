# Chapter 5 当前交接 — local-basin reexecution accepted / next Reviewer route pending

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`LOCAL_BASIN_REEXECUTION_ACCEPTED__NEXT_REVIEWER_ROUTE_PENDING`。

最新 accepted Builder candidate：`c994cee14b5958e47078bd7281acffcbe56797e5`。
Acceptance：`docs/CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION_ACCEPTANCE.md`。
当前 active Builder task：无。
Results eligibility=`FALSE`。

## Governance

Owner 是 final scientific authority；ChatGPT 是 L3 independent Reviewer / scientific-route authority / bounded local numerical-debug authority；Codex 是 bounded Builder / executor。GitHub live `main` 是唯一 repository-state authority。严禁混用 `zcx369658780/deep-learning-hank`。

Owner 已授权 Reviewer 对 bounded numerical diagnostics 作预注册路线决策；结构方程、accepted equations/guards、major economic calibration、causal interpretation、Results eligibility 仍由 Owner 决定。

任何 successor science 前必须：fresh-fetch live main → Reviewer route decision → GitHub freeze/exact task → Builder bounded execution。不得从聊天直接启动未发布任务。

## Frozen household science

Accepted practical household grid：`I=20,J=160,Nz=2,a=[0,100],b=[-2,20],h=1`，仅用于 bounded diagnostics，不代表 continuum convergence 或 production-final precision。

保持 accepted MATLAB-faithful household block：annual continuous time；`rho=.05`、`rb=.02`、borrowing gap `.07`、`Delta=1000`、HJB tolerance `1e-7`、maxit `100`、A2max legality gate `.01`；fresh source-style initialization；accepted FOC / selectors / boundaries / derivative-floor logic / sparse direct solve。

Finer-J route 因 accepted J640 policy/selector chatter 关闭；finer-I route 因 I40/J160 operator illegality 关闭。不得通过增加 maxit、damping/relaxation/line-search、修改 tolerance/floor/selector/solver 来制造 convergence。

## First-turn provincial evidence

Exact accepted 31-province first-turn household input vector authority PASS。I20/J160 HJB：25/31 converged；天津、山西、江西、重庆、贵州、甘肃 legal nonconverged；0 illegal operator；0 hard error；KFE=0。

Accepted six-failure temporal classes：

- 天津：`POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`
- 山西：`POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`
- 江西：`DERIVATIVE_FLOOR_AMPLIFICATION_AFTER_EARLIER_SWITCHING`
- 重庆：`POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`
- 贵州：`REPEATING_OR_LOW_PERIOD_CYCLE`，joint-selector recurrence 96→98 period2，无 exact value recurrence
- 甘肃：`POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`

Panel=`SIX_FAILURES_HETEROGENEOUS_MECHANISMS`。

## Spatial / matched-control evidence

Value-update argmax localization heterogeneous；coordinate-resolved selector/floor matched-control diagnostic 显示 failures 与 successful controls 的 upper-b selector shares 高度接近，controls 也有 substantial upper-b floor activity。江西 floor hits 主要 double-interior；天津 selector/floor 主要 double-interior；贵州 period-2 selector recurrence 可定位到 stable 3-cell near-upper-b/a-interior changed set，但无 exact value recurrence。

结论：failure-specific common upper-b pathology 不成立；不得据此统一扩大 bmax、修改 boundary/selector/floor/HJB 或统一 recalibration。

## Input/outcome envelope evidence

31省 failure/success consumed `ra` 与 household composite `w` ranges/boxes/hulls overlap；single-ra threshold、single-w threshold 均不存在；fixed k=3 graph interleaved。Return guard 31/31=`NOT_APPLIED_BOOTSTRAP`，corrected upstream wjt guard 31/31=`UPPER`；无 discriminating guard variation。Raw provincial `wjt` 不得与 household composite `w` 混同。

结论：simple safe-price envelope / universal guard route CLOSED。

## Latest accepted local-basin evidence

四对 preregistered matched pairs：

1. 山西 failure → 河北 success
2. 重庆 failure → 河北 success
3. 江西 failure → 安徽 success
4. 贵州 failure → 四川 success

每对除 consumed `ra` / household composite `w` 外全部 consumed household scientific inputs exact equal。Endpoints reuse-only；synthetic probes 为 t=.25/.50/.75 numerical HJB diagnostics，不是省级均衡、calibrated state、upstream mapping output 或经济 counterfactual。

第一次执行因 task-owned A2max receipt 把 post-convergence implicit system matrix 混入 scientific generator A2max 而 fail-closed。随后已修复 receipt 并 controlled reexecute 同一12点；scientific A2max sequence 仅包含真实 HJB iteration source-generator `A`，post-convergence matrix 独立排除。12/12 exact maximum A2max < `.01`，first scientific illegal iteration 全 null；terminal class、iteration count、final max|dV| 与 blocked run bit-exact。

Formal topology：

- 山西→河北：`F→C→C→C→C`；`ALL_INTERIOR_PROBES_CONVERGE`
- 重庆→河北：`F→C→C→C→C`；`ALL_INTERIOR_PROBES_CONVERGE`
- 江西→安徽：`F→F→C→C→C`；`SINGLE_TRANSITION_FAILURE_TO_SUCCESS`
- 贵州→四川：`F→C→F→C→C`；`NONMONOTONE_OR_INTERLEAVED_LOCAL_BASIN`

Panel=`LOCAL_BASIN_TOPOLOGY_HETEROGENEOUS_OR_INTERLEAVED`。

这只建立 numerical HJB basin topology 对 `(ra,w)` 的 pair-specific / nonmonotone sensitivity；不等于 economic multiple equilibrium、省级均衡多重性、calibration/mapping error。不得自动 clipping、recalibration、guard/mapping change、HJB/grid/boundary change。

## Separate unresolved blocker

Corrected-2018 multi-province finite-box upper-`b` leakage / MATLAB-style pinning KFE blocker仍未解决，与 standalone contaminated-row KFE 分离。

## Handoff decision boundary

当前没有 active Builder task；science runtime=0，直到 Reviewer 发布 successor task。

下一会话不得自动继续 synthetic interpolation、adaptive bisection 或 recalibration。Reviewer 应先读 live GitHub authority，然后在两类路线之间决策：

1. 仅当能够直接支持 integration decision 时，设计一个最小 local-basin mechanism robustness/attribution diagnostic；或
2. 停止继续 basin mapping，返回 corrected multi-province integration 的下一 unresolved gate，优先评估独立 KFE finite-box/pinning blocker或 roadmap 中下一 accepted integration gate。

本交接的不可变快照：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_20260915_LOCAL_BASIN_ACCEPTED.md`。
