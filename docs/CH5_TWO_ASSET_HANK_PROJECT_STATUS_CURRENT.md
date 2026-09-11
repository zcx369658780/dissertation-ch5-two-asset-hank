# Chapter 5 两资产 HANK 当前状态
更新：2026-09-11。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1A_BOUNDED_INTEGRATION_PARTIAL_ACCEPTED__VALIDATOR_REPAIRED__SYMMETRIC_AB_RERUN_ACTIVE`。

最新 accepted bounded-integration candidate：`f57fec4d66bb82d48dc02bed775761ec194e0084`。
Reviewer acceptance：`docs/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_BOUNDED_INTEGRATION_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_SYMMETRIC_RERUN.md`。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

资本网络总体科学设计冻结稿：`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。
K1 scoring/data 冻结稿：`docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`。

## 已冻结 K1A/K1B 参数
- K1A equal-share：`beta_distance=0`, `beta_return=0`；
- K1A geography benchmark：`beta_distance=2`, `beta_return=0`；
- K1B future benchmark preregistered：`beta_return=.5`，当前不运行；
- theta 固定为 `inter_prv_ratio_i`；
- source-faithful labor；
- smoothing/partial adjustment OFF；
- K1A payoff bridge = current source-used/clipped `ra`，仅分类为 `K1A_SOURCE_FAITHFUL_PAYOFF_BRIDGE__NOT_FINAL_ECONOMIC_RETURN_AUTHORITY`；
- C1 `GovInv=max(Ktarget-Kprivate,0)` 不变。

## 前一 bounded integration：partial evidence 已接受
Pre-run 50/50 focused tests 通过。Path A 在完成 turn 1 后，于 turn-2 entry 被 task-wrapper 中遗留的 legacy `rah` validator assertion 阻断；由于 scientific state 已推进，未重跑。该 validator 后续仅做 zero-science provenance repair：改为验证 prior completed K1A allocation 使用同一 `S` 的 `rah`，没有改变经济方程、参数、容差、solver 或 state evolution。

Path B 在 repaired validator 下完成 25 turns。806 个已完成 province-turn 中，quantity/`rah` same-`S`、home retention、origin/national private-capital conservation 与 no destination-theta double weighting 全部通过。C1 始终保持 `GovInv=max(Ktarget-Kprivate,0)`；观察样本中 `Kprivate>=Ktarget` 为0，private-only overshoot为0。

Path B turn25 仍未满足冻结 outer convergence predicate：`max_nk_gap=1.8619512598405663e-09 > 1e-9`。不得调 tolerance 或 solver。

raw-return pressure 仍很强：Path B pooled raw `ra0` 775 条中 755 条高于 `.09`，upper clipping 755 次。旧 `.02/.09` 继续仅是 empirical numerical safeguard，不获得最终经济 authority。

## 当前 active symmetric rerun
新 task 只为消除 predecessor wrapper defect 造成的非对称证据：从 identical accepted initialization，在已修正 provenance validator 下重新执行两条预注册路径，每条最多25 turns。

不得改变：beta、theta、payoff bridge、labor、smoothing、C1、return/wage bounds、HJB/KFE/firm science、grids、tolerances、iteration limits、solver semantics。

本轮要获得完整 common-prefix A/B evidence，重点比较 Kprivate、GovInv、total K、raw/used returns、rah、output、wage 与 outer convergence。若某路径科学性停止，则只报告真实共同前缀，不得重调科学对象。

## KFE 与 Results 边界
所有当前 empirical KFE 仍为 diagnostic-only；corrected-2018 finite-box upper-b leakage + MATLAB-style pinning 是独立 blocker。K1A bounded run 不构成 KFE closure、steady-state acceptance、annual/IRF/welfare 或 Results。

Results eligibility=`FALSE`。
