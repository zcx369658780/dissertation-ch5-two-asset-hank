# Chapter 5 两资产 HANK 当前状态
更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_CANDIDATE_PUBLISHED__INDEPENDENT_REVIEW_REQUIRED`。

最新 accepted D1 candidate：`c7d29f5bc0751751f1547072eac79eff916a8240`。
Reviewer acceptance：`docs/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC_ACCEPTANCE.md`。
Owner D1 freeze：`docs/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_ADMISSIBILITY_FREEZE_CURRENT.md`。
Owner/Reviewer HJB route freeze：`docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_REVIEW_FREEZE_CURRENT.md`。
当前 active Builder task：NONE。候选报告：`docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC_REPORT.md`。
Results eligibility=`FALSE`。

D1 exact contract继续有效：symmetric `[-1e5,+1e5]`，inclusive `abs(d_raw)<=1e5`；超界 raw branch 在 raw FOC receipt 保存后按 `C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION` 排除；禁止 clipping / manufactured endpoint；existing zero-transfer option 与其他 admissible branches继续按 accepted selector law。

Accepted D1 runtime继续作为路线判断依据：turn1 exact equal；turn2 common-entering-state gate PASS；turns2-5 rejected `15,330/39,440,000` active raw branches (`0.0388692%`)，形成 `3,459` iteration-cell winner changes，其中 `2,156` fallback 到 existing zero，`1,303` switch 到其他 admissible nonzero。D1显著压低 selected transfer / adjustment cost / `mu_a` / `mu_b` far-tail extrema，但 HJB convergence未改善：turns2-5 control `6/124`、D1 `5/124`；all-turn `26/155` vs `25/155`；turn2 same-state仍 `2/31` vs `2/31`。

因此 transfer explosive tail继续分类为重要 numerical-stress amplifier，但不是当前 HJB convergence failure 的充分或主导解释。

Owner/Reviewer已冻结 `HJB_CONVERGENCE_MECHANISM_REVIEW_FIRST`，优先级：`D HJB iteration/fixed-point mechanism -> C derivative/value-safeguard evidence -> A return interface -> B wage interface -> E boundary/selector only if evidence redirects there`。

Active task只允许 observation-only HJB instrumentation 与 accepted G2 control、D1 OFF 的 turn1/turn2 exact-input isolated replay。目标覆盖31省×2 turns=62个 proven-exact calls；另有2个 instrumentation ON/OFF parity calls，总 HJB budget最多64。KFE、outer trajectory advancement、MATLAB、K1B/K2、GE/IRF/Results均为0。不得近似重建缺失输入；identity不成立的 province-turn 必须跳过并如实报告。

候选已完成62/62 exact-input replay，另有2个parity HJB，合计64；scientific retries=0；KFE/outer advancement/MATLAB/firm runtime=0。62/62 scientific outputs 与 final operators 均和accepted artifacts exact-equal，重现turn1 `20/31`、turn2 `2/31`。

候选分类：`POLICY_CHATTERING_WITH_VALUE_UPDATE_OSCILLATION_AND_LATER_DERIVATIVE_FLOOR_AMPLIFICATION__NOT_PURE_TWO_CYCLE__NOT_MONOTONE_SLOW`。40/40 failed calls 的policy switching早于首次derivative-floor hit，38/40的value-stat non-decrease也更早；floor更像后续amplifier。初始linear-solve absolute residual在全部62 calls均为约`4.39e-14`至`9.25e-14`，operator已知signed off-diagonal/boundary row-sum特征在成功和失败calls都出现。该结论是基于预注册连续指标的post-hoc descriptive classification，不是因果gate。

Return/wage safeguards仍 binding，长期目标仍为 `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。same-S、capital conservation、C1 accounting、source-faithful labor、no same-turn feedback、raw-`ra0` provenance继续闭合。KFE=`DIAGNOSTIC_ONLY`；standalone KKT residual=`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。

当前不授权 longer D1、D2/D3/OFF、G3/G4、wage relaxation、`chi0/chi1`调整、derivative-floor/grid/tolerance/solver/pseudo-time/update-law/boundary-law变化、K1B/K2、steady-state acceptance、GE/IRF/Results。

唯一当前 gate：ChatGPT Reviewer 对候选、compact/external evidence和call ledger做独立 ACCEPT/REJECT。候选仅建议验收后由Owner考虑 `OWNER_HJB_ITERATION_FIXED_POINT_MECHANISM_INTERVENTION_DESIGN_FREEZE`；这不是已授权successor task。
