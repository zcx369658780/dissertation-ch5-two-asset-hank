# Chapter 5 两资产 HANK 当前状态
更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC_ACCEPTED__FAR_TAIL_STRESS_REDUCED__HJB_CONVERGENCE_NOT_IMPROVED__OWNER_HA_NUMERICAL_CONTRACT_REASSESSMENT_REQUIRED`。

最新 accepted D1 candidate：`c7d29f5bc0751751f1547072eac79eff916a8240`。
Reviewer acceptance：`docs/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC_ACCEPTANCE.md`。
Owner D1 freeze：`docs/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_ADMISSIBILITY_FREEZE_CURRENT.md`。
当前 active Builder task：NONE。
Results eligibility=`FALSE`。

D1 exact contract：symmetric `[-1e5,+1e5]`，inclusive `abs(d_raw)<=1e5`；超界 raw branch 在 raw FOC receipt 保存后按 `C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION` 排除；禁止 clipping / manufactured endpoint；existing zero-transfer option 与其他 admissible branches 继续按 accepted selector law。

Accepted runtime 为 fresh G2 control vs G2+D1 各5 turns。Turn1 exact equal，turn2 common-entering-state gate PASS。D1 turns2-5 rejected `15,330/39,440,000` raw branches (`0.0388692%`)，形成 `3,459` iteration-cell winner changes，其中 `2,156` fallback 到 existing zero，`1,303` switch 到其他 admissible nonzero。

D1 明显压低 far-tail stress：selected `|d|` max约 `4.27e7 -> 9.99e4`，adjustment-cost max约 `1.92e14 -> 3.79e9`，`mu_a/mu_b` extrema同数量级收缩。但 HJB convergence 没有改善：turns2-5 control `6/124`、D1 `5/124`；all-turn `26/155` vs `25/155`；turn2 same-state仍 `2/31` vs `2/31`。因此 transfer explosive tail 是重要 numerical-stress amplifier，但不是当前 convergence failure 的充分/主导解释。

Return/wage safeguards仍 binding，`ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`未达到。same-S、capital conservation、C1 accounting、source-faithful labor、no same-turn feedback、raw-`ra0` provenance继续闭合。KFE=`DIAGNOSTIC_ONLY`；standalone KKT residual=`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。

当前不授权 longer D1、D2/D3/OFF、G3/G4、wage relaxation、`chi0/chi1`调整、derivative-floor/grid/tolerance/solver/boundary-law变化、K1B/K2、GE/IRF/Results。

唯一 next gate：`OWNER_HA_NUMERICAL_CONTRACT_REASSESSMENT_REQUIRED`。下一会话先讨论 remaining HJB convergence blocker 的隔离顺序，再决定是否发布新的 exact task。

新会话交接优先读取：`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT_20260913_D1.md`。
