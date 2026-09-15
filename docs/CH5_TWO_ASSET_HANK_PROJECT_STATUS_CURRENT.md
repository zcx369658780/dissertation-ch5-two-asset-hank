# Chapter 5 两资产 HANK 当前状态

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`LOCAL_BASIN_REEXECUTION_ACCEPTED__NEXT_REVIEWER_ROUTE_PENDING`。

最新 accepted Builder candidate：`c994cee14b5958e47078bd7281acffcbe56797e5`。
最新 Reviewer acceptance：`docs/CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION_ACCEPTANCE.md`。
当前 active Builder task：无。任何新 science runtime 前，Reviewer 必须 fresh-fetch GitHub authority，并发布新的 freeze / exact task。

Results eligibility=`FALSE`。

## 当前 numerical authority

Accepted practical household grid：`I=20,J=160,Nz=2,a=[0,100],b=[-2,20],h=1`。仅具有 `PRACTICAL_BOUNDED_DIAGNOSTIC_GRID` authority，不代表 continuum convergence 或 production-final precision。

Finer-J route 已因 accepted J640 `POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION` 关闭。Finer-I route 已因 I40/J160 在 maxit100 内 nonconverged 且 iteration94 首次 operator-illegal 关闭。禁止通过增加 maxit、damping/relaxation/line-search、tolerance/floor/selector 变化制造 convergence。

## First-turn provincial HJB authority

Exact accepted 31-province first-turn household input vector authority PASS。I20/J160 first-turn HJB：25/31 converged；天津、山西、江西、重庆、贵州、甘肃为 legal nonconverged；illegal operator=0，hard error=0；KFE=0。

六个失败的 accepted temporal mechanism heterogeneous：天津、山西、重庆、甘肃为 policy/selector chatter with value oscillation；江西为 derivative-floor amplification after earlier switching；贵州为 exact joint-selector period-2 recurrence without exact value recurrence。

Value-update argmax spatial audit 与 coordinate-resolved selector/floor matched-control diagnostic 进一步表明 spatial footprint heterogeneous；successful controls 也存在 substantial upper-b selector/floor activity。因此 failure-specific common upper-b pathology、统一 boundary repair、统一 grid expansion 或统一 HJB fix 均不被支持。

## Input/outcome envelope authority

31省 failures/successes 在 consumed `ra` 与 household composite `w` 上高度重叠：ranges、2D bounding boxes、convex hulls overlap；不存在 single-ra 或 single-w separating threshold；fixed k=3 standardized graph interleaved。Return guard 31/31=`NOT_APPLIED_BOOTSTRAP`，corrected upstream wjt guard 31/31=`UPPER`，无横截面判别变异。Simple safe-price envelope / universal guard route CLOSED。

## Latest accepted local-basin authority

四个 preregistered pair 均已证明除 consumed `ra` / household composite `w` 外全部 household scientific inputs exact equal。A2max receipt repair 后，同一12个 sealed synthetic probes controlled reexecution；12/12 scientific source-generator A2max maxima 均低于 `.01`，first scientific illegal iteration 全为 null，且 terminal class / iteration count / final max|dV| 与 blocked run bit-exact。

Formal pair topology：

- 山西→河北：`F→C→C→C→C`；`ALL_INTERIOR_PROBES_CONVERGE`
- 重庆→河北：`F→C→C→C→C`；`ALL_INTERIOR_PROBES_CONVERGE`
- 江西→安徽：`F→F→C→C→C`；`SINGLE_TRANSITION_FAILURE_TO_SUCCESS`
- 贵州→四川：`F→C→F→C→C`；`NONMONOTONE_OR_INTERLEAVED_LOCAL_BASIN`

Panel authority：`LOCAL_BASIN_TOPOLOGY_HETEROGENEOUS_OR_INTERLEAVED`。

这只确认 numerical HJB local-basin topology 对 `(ra,w)` 变化可呈 pair-specific、甚至非单调/交错响应；不等于经济多重均衡、省级均衡多重性、mapping 错误、calibration 错误或经济反事实。当前不得据此授权 clipping、recalibration、guard/mapping change、boundary/grid change 或 HJB algorithm change。

## Separate unresolved blocker

Corrected-2018 multi-province finite-box upper-`b` leakage / MATLAB-style pinning KFE blocker仍独立存在且未解决。Standalone contaminated-row KFE 不替代 corrected multi-province KFE authority。

## Next action

本会话已收口，当前没有 active Builder task。下一会话首先 fresh-fetch GitHub live main，并读取 `AGENTS.md`、rule index、current status、current handoff、latest acceptance 与 immutable handoff snapshot。

不得默认继续 synthetic interpolation、adaptive bisection 或 recalibration。Reviewer 应重新选择下一条高信息量路线：

1. 仅当能直接回答 integration decision 时，设计最小 local-basin mechanism robustness/attribution diagnostic；或
2. 停止继续 basin mapping，返回 corrected multi-province integration 的下一 unresolved gate，尤其是独立的 KFE finite-box/pinning blocker。

在 Reviewer 正式发布 successor freeze/task 前，science runtime=0。
