# Chapter 5 当前规则入口
更新：2026-09-13；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT_20260913_D1.md`
5. accepted bilateral-capital / scoring-data / payoff / annual-HJB / price-guard authority docs
6. `docs/CH5_MP4C_K1_TRANSFER_CONTROL_RAW_CANDIDATE_CENSUS_INSTRUMENTED_BOUNDED_DIAGNOSTIC_ACCEPTANCE.md`
7. `docs/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_ADMISSIBILITY_FREEZE_CURRENT.md`
8. `docs/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC_ACCEPTANCE.md`
9. 若存在 active exact task，再读取 task 及直接相关 report/evidence。

当前状态：`D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC_ACCEPTED__FAR_TAIL_STRESS_REDUCED__HJB_CONVERGENCE_NOT_IMPROVED__OWNER_HA_NUMERICAL_CONTRACT_REASSESSMENT_REQUIRED`。
当前 active Builder task：NONE。
最新 accepted D1 candidate：`c7d29f5bc0751751f1547072eac79eff916a8240`。
Results eligibility=`FALSE`。

D1 exact contract：symmetric `[-1e5,+1e5]`，inclusive `abs(d_raw)<=1e5`；语义=`C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION`；raw FOC receipt保留；禁止 clipping/manufactured endpoint；existing zero 与其他 admissible branches继续按 accepted selector law。

Accepted D1 runtime：turn1 exact equal；turn2 common-state gate PASS；turns2-5 rejection=`15,330/39,440,000`，winner changes=`3,459`，其中 zero fallback=`2,156`、other nonzero=`1,303`。D1显著压低 far-tail transfer/cost/mu/drift extrema，但 HJB convergence control=`6/124`、D1=`5/124`，不支持 longer D1 或自动进入 wider D stage。

Return/wage safeguards仍 binding；长期目标仍为 `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。KFE=`DIAGNOSTIC_ONLY`，KKT residual unavailable。不得自动改 `chi0/chi1`、derivative floor、return/wage guards、grid/tolerance/solver、boundary/KKT、K1/C1/labor science。

唯一 next gate：`OWNER_HA_NUMERICAL_CONTRACT_REASSESSMENT_REQUIRED`。新会话先讨论 remaining HJB convergence blocker 的隔离顺序；在 Owner/Reviewer 达成 substantive route 前不得发布 successor runtime task。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。正式发布 exact task 时同一 ChatGPT 回复必须附完整 Codex startup prompt。
