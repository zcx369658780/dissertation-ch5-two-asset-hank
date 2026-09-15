# CH5 MP4C K1 — J160 local-basin A2max receipt repair and reexecution acceptance

更新：2026-09-15。

Reviewer verdict：

`LOCAL_BASIN_A2MAX_REEXECUTION_ACCEPTED__HETEROGENEOUS_OR_INTERLEAVED_NUMERICAL_BASIN_TOPOLOGY_CONFIRMED__NO_CALIBRATION_OR_HJB_CHANGE_AUTHORIZED`

Accepted candidate：`c994cee14b5958e47078bd7281acffcbe56797e5`。
Accepted baseline：`a3978f7827aa00e880822c47a2c24157ef092e76`。
Candidate 与 baseline 的关系：exactly one commit ahead，behind 0。

## Acceptance basis

本轮 task-owned receipt repair 已把 scientific A2max 严格限定为真实 HJB scientific iterations 内 source-generator `A` 的 row-sum legality metric；post-convergence implicit system matrix 被独立记录并明确排除出 scientific legality。Protected HJB/KFE、FOC、selector、derivative floor、solver、initialization、grid/domain、tolerance、Delta、maxit 均未修改。

12 个预注册 synthetic probes 全部完成 controlled reexecution；每个 probe 的 scientific A2max sequence 长度与 scientific iteration count 一致，12/12 maximum scientific A2max 均低于冻结 gate `0.01`，first scientific illegal iteration 全部为 null。Blocked run 的 terminal class、iteration count 与 final max|dV| 对本次重跑逐点 bit-exact 复现。

## Accepted probe outcomes

- 山西→河北：t=.25/.50/.75 = C34 / C39 / C37。
- 重庆→河北：t=.25/.50/.75 = C46 / C57 / C30。
- 江西→安徽：t=.25/.50/.75 = F100 / C77 / C71；t=.25 机制仍为 `DERIVATIVE_FLOOR_AMPLIFICATION_AFTER_EARLIER_SWITCHING`。
- 贵州→四川：t=.25/.50/.75 = C80 / F100 / C56；t=.50 机制仍为 `POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`。

12 点 scientific maximum A2max 均约 `0.00247`–`0.00268`，远低于 `0.01` legality gate，因此本轮不再存在 A2max receipt blocker。

## Accepted formal topology

- 山西→河北：`F→C→C→C→C`；`ALL_INTERIOR_PROBES_CONVERGE`。
- 重庆→河北：`F→C→C→C→C`；`ALL_INTERIOR_PROBES_CONVERGE`。
- 江西→安徽：`F→F→C→C→C`；`SINGLE_TRANSITION_FAILURE_TO_SUCCESS`。
- 贵州→四川：`F→C→F→C→C`；`NONMONOTONE_OR_INTERLEAVED_LOCAL_BASIN`。

Panel class：

`LOCAL_BASIN_TOPOLOGY_HETEROGENEOUS_OR_INTERLEAVED`

这建立的是 numerical HJB local-basin evidence，而不是经济多重均衡、省级均衡多重性、校准错误、mapping 错误或经济反事实。

## Scientific interpretation

本轮正式确认：在保持 pair 内除 consumed `ra` 与 household composite `w` 外全部 household scientific inputs exact equal 的条件下，局部 HJB 收敛结果可以对 `(ra,w)` 变化呈 pair-specific、甚至非单调/交错响应。特别是贵州→四川的 accepted sequence `F→C→F→C→C` 排除了一个简单单调 local safe-direction 解释。

这一证据与此前 accepted 结论一致：

1. 31 省 failures/successes 在 consumed `(ra,w)` 上高度重叠；
2. 不存在统一 single-ra / single-w separating threshold；
3. guard states 无横截面判别变异；
4. failure temporal mechanisms heterogeneous；
5. value-argmax spatial patterns heterogeneous；
6. coordinate-resolved selector/floor matched controls 不支持 failure-specific common upper-b pathology。

因此当前没有科学依据授权统一 clipping、safe-price envelope、统一 recalibration、guard change、mapping change、boundary/grid repair 或 HJB algorithm change。

## Numerical authority boundary

Accepted practical household grid 仍为：

`I=20, J=160, Nz=2, a=[0,100], b=[-2,20], h=1`

仅具有 `PRACTICAL_BOUNDED_DIAGNOSTIC_GRID` authority；不代表 continuum convergence 或 production-final precision。

Finer-J route 仍因 accepted J640 policy/selector chatter 关闭；finer-I route 仍因 accepted I40 operator illegality 关闭。不得通过增加 maxit、damping/relaxation/line-search 或 tolerance/floor/selector 变化制造 convergence。

## Runtime ledger accepted

- HJB started/completed/hard-error = `12/12/0`
- endpoint HJB = `0`
- KFE = `0`
- scientific retries = `0`
- engineering retry = `1/1`，且只发生在 first HJB 前的 manifest newline receipt plumbing
- outer/firm/wage/return/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results = `0`

## Unresolved blockers

Corrected-2018 multi-province finite-box upper-`b` leakage / MATLAB-style pinning KFE blocker仍独立存在，未被本轮重新打开或解决。

Results eligibility=`FALSE`。

## Next Reviewer route

本会话在本 acceptance 后收口并交接。下一会话不应默认继续 synthetic interpolation、adaptive bisection 或 recalibration。应先从 GitHub live main 读取 current status / handoff / rule index，并基于本 acceptance 决定下一条高信息量路线。

推荐优先讨论的 Reviewer-level 路线是：在不修改 accepted household science 的前提下，判断是否需要对 `local-basin topology` 做最小机制归因/robustness 设计，或直接返回 corrected multi-province integration 的下一 unresolved gate；任何新 scientific task 都必须先由 Reviewer 在 GitHub 发布 exact task。
