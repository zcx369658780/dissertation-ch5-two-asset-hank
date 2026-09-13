# Chapter 5 当前规则入口
更新：2026-09-13；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT_20260913_HJB_MECHANISM.md`
5. accepted bilateral-capital / scoring-data / payoff / annual-HJB / price-guard authority docs
6. `docs/CH5_MP4C_K1_TRANSFER_CONTROL_RAW_CANDIDATE_CENSUS_INSTRUMENTED_BOUNDED_DIAGNOSTIC_ACCEPTANCE.md`
7. `docs/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_ADMISSIBILITY_FREEZE_CURRENT.md`
8. `docs/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC_ACCEPTANCE.md`
9. `docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_REVIEW_FREEZE_CURRENT.md`
10. candidate report：`docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC_REPORT.md`
11. candidate直接相关的当前HJB实现、accepted evidence producer与compact evidence。

当前状态：`HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_CANDIDATE_PUBLISHED__INDEPENDENT_REVIEW_REQUIRED`。
当前 active Builder task：NONE。
最新 accepted D1 candidate：`c7d29f5bc0751751f1547072eac79eff916a8240`。
Results eligibility=`FALSE`。

D1 exact contract保持不变：symmetric `[-1e5,+1e5]`，inclusive `abs(d_raw)<=1e5`；语义=`C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION`；raw FOC receipt保留；禁止 clipping/manufactured endpoint；existing zero 与其他 admissible branches继续按 accepted selector law。

Accepted D1 runtime：turn1 exact equal；turn2 common-state gate PASS；turns2-5 rejection=`15,330/39,440,000`，winner changes=`3,459`，其中 zero fallback=`2,156`、other nonzero=`1,303`。D1显著压低 far-tail transfer/cost/mu/drift extrema，但 HJB convergence control=`6/124`、D1=`5/124`，不支持 longer D1 或自动进入 wider D stage。

Owner/Reviewer已冻结 `HJB_CONVERGENCE_MECHANISM_REVIEW_FIRST`。优先级：HJB iteration/fixed-point mechanism → derivative/value safeguard evidence → return interface → wage interface → boundary/selector only if evidence redirects there。

Candidate事实：accepted G2 control、D1 OFF 的 turn1/turn2 exact-input覆盖62/62；observation-only parity=PASS；2 parity + 62 replay = 64 HJB；scientific retry=0；KFE/outer advancement/MATLAB/firm/GE/IRF/Results=0；62/62 outputs/operators exact。分类为policy chattering + non-monotone value-update oscillation + later derivative-floor amplification，不支持pure two-cycle、monotone-slow或仅延长iteration ceiling。

诊断只观察，不调 solver、tolerance、100-iteration ceiling、pseudo-time/update law、derivative floor、return/wage guards、economic parameters、grid、boundary/KKT 或 K1/C1/labor science。

Return/wage safeguards仍 binding；长期目标仍为 `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。KFE=`DIAGNOSTIC_ONLY`，KKT residual unavailable。

Builder已停止scientific work，不合并main，不发布successor task。唯一当前gate是ChatGPT Reviewer独立ACCEPT/REJECT；只有验收后Reviewer/Owner才能决定下一Owner gate。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
