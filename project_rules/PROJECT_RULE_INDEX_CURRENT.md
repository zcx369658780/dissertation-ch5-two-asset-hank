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
9. `docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_REVIEW_FREEZE_CURRENT.md`
10. 若存在 active exact task，再读取 task 及直接相关 report/evidence。

当前状态：`HJB_CONVERGENCE_MECHANISM_REVIEW_ROUTE_FROZEN__DIAGNOSTIC_ONLY__SUCCESSOR_TASK_PENDING_PUBLICATION`。
当前 active Builder task：NONE（successor exact task 尚未发布）。
最新 accepted D1 candidate：`c7d29f5bc0751751f1547072eac79eff916a8240`。
Results eligibility=`FALSE`。

D1 exact contract保持不变：symmetric `[-1e5,+1e5]`，inclusive `abs(d_raw)<=1e5`；语义=`C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION`；raw FOC receipt保留；禁止 clipping/manufactured endpoint；existing zero 与其他 admissible branches继续按 accepted selector law。

Accepted D1 runtime：turn1 exact equal；turn2 common-state gate PASS；turns2-5 rejection=`15,330/39,440,000`，winner changes=`3,459`，其中 zero fallback=`2,156`、other nonzero=`1,303`。D1显著压低 far-tail transfer/cost/mu/drift extrema，但 HJB convergence control=`6/124`、D1=`5/124`，不支持 longer D1 或自动进入 wider D stage。

Owner/Reviewer现已冻结 `HJB_CONVERGENCE_MECHANISM_REVIEW_FIRST`。优先级：HJB iteration/fixed-point mechanism → derivative/value safeguard evidence → return interface → wage interface → boundary/selector only if evidence redirects there。第一阶段只做诊断与 exact-input replay，不调 solver、tolerance、pseudo-time、derivative floor、price guards、economic parameters、grid、boundary/KKT 或 K1/C1/labor science。

Return/wage safeguards仍 binding；长期目标仍为 `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。KFE=`DIAGNOSTIC_ONLY`，KKT residual unavailable。

下一操作是发布 bounded exact HJB convergence-mechanism Builder task；task发布前无新科学调用授权。正式发布 exact task 时同一 ChatGPT 回复必须附完整 Codex startup prompt。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
