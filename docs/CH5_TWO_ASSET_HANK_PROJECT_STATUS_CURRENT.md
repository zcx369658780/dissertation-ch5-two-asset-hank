# Chapter 5 两资产 HANK 当前状态
更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HJB_CONVERGENCE_MECHANISM_REVIEW_ROUTE_FROZEN__DIAGNOSTIC_ONLY__SUCCESSOR_TASK_PENDING_PUBLICATION`。

最新 accepted D1 candidate：`c7d29f5bc0751751f1547072eac79eff916a8240`。
Reviewer acceptance：`docs/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC_ACCEPTANCE.md`。
Owner D1 freeze：`docs/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_ADMISSIBILITY_FREEZE_CURRENT.md`。
Owner/Reviewer HJB route freeze：`docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_REVIEW_FREEZE_CURRENT.md`。
当前 active Builder task：NONE（successor exact task 尚未发布）。
Results eligibility=`FALSE`。

D1 exact contract继续有效：symmetric `[-1e5,+1e5]`，inclusive `abs(d_raw)<=1e5`；超界 raw branch 在 raw FOC receipt 保存后按 `C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION` 排除；禁止 clipping / manufactured endpoint；existing zero-transfer option 与其他 admissible branches继续按 accepted selector law。

Accepted D1 runtime继续作为路线判断依据：turn1 exact equal；turn2 common-entering-state gate PASS；turns2-5 rejected `15,330/39,440,000` active raw branches (`0.0388692%`)，形成 `3,459` iteration-cell winner changes，其中 `2,156` fallback 到 existing zero，`1,303` switch 到其他 admissible nonzero。D1显著压低 selected transfer / adjustment cost / `mu_a` / `mu_b` far-tail extrema，但 HJB convergence未改善：turns2-5 control `6/124`、D1 `5/124`；all-turn `26/155` vs `25/155`；turn2 same-state仍 `2/31` vs `2/31`。

因此 transfer explosive tail继续分类为重要 numerical-stress amplifier，但不是当前 HJB convergence failure 的充分或主导解释。

Owner/Reviewer已冻结下一优先路线为 `HJB_CONVERGENCE_MECHANISM_REVIEW_FIRST`，优先级：`D HJB iteration/fixed-point mechanism -> C derivative/value-safeguard evidence -> A return interface -> B wage interface -> E boundary/selector only if evidence redirects there`。目标是先解释 accepted G2 control 中 HJB 从 turn1 `20/31` converged 降至 turn2 `2/31` 的机制，而不是立即修 solver 或经济参数。

新冻结要求：优先使用 accepted G2 control、D1 OFF 的 turn1/turn2 exact inputs，比较全部省份的 converged/failed call groups；记录逐 HJB iteration convergence statistic、value update、policy switching、raw/used derivatives 与 derivative-floor hits、operator/linear-solve diagnostics、controls/drifts，以及 consumed return/wage guard state，用 event ordering 寻找最早区分事件。不得用最终相关性直接声称因果。

Return/wage safeguards仍 binding，长期目标仍为 `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。same-S、capital conservation、C1 accounting、source-faithful labor、no same-turn feedback、raw-`ra0` provenance继续闭合。KFE=`DIAGNOSTIC_ONLY`；standalone KKT residual=`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。

当前不授权 longer D1、D2/D3/OFF、G3/G4、wage relaxation、`chi0/chi1`调整、derivative-floor/grid/tolerance/solver/pseudo-time/update-law/boundary-law变化、K1B/K2、GE/IRF/Results。

下一操作：发布一个 bounded exact Builder task，用于 HJB convergence-mechanism instrumentation + turn1/turn2 exact-input replay/analysis；在该 task 发布前不进行科学调用。
