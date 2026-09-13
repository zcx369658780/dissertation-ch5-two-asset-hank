# Chapter 5 当前规则入口
更新：2026-09-13；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT_20260913_HJB_MECHANISM.md`
5. accepted bilateral-capital / scoring-data / payoff / annual-HJB / price-guard authority docs
6. `docs/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC_ACCEPTANCE.md`
7. `docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_REVIEW_FREEZE_CURRENT.md`
8. `docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC_ACCEPTANCE.md`
9. accepted diagnostic report及compact evidence。

当前状态：`HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC_ACCEPTED__OWNER_FIXED_POINT_INTERVENTION_DESIGN_FREEZE_REQUIRED`。
当前 active Builder task：NONE。
最新 accepted HJB mechanism candidate：`c6d89327933edef2b942f10f462b58cfa6b52954`。
Results eligibility=`FALSE`。

Accepted mechanism diagnostic：62/62 exact-input replay；instrumentation parity PASS；64 HJB calls；0 scientific retries；0 KFE/outer trajectory/MATLAB/firm/K1B/K2/GE/IRF/Results；62/62 scientific outputs与final operators exact-equal accepted evidence；turn1 `20/31`、turn2 `2/31`。

Accepted descriptive classification：policy chattering + non-monotone value-update oscillation precede later derivative-floor amplification；not pure two-cycle；not monotone-slow。40/40 failed calls 的policy switching早于first derivative-floor hit，38/40的value-stat non-decrease也更早。该分类是temporal/associational evidence，不是因果intervention结果。

现有证据不支持仅延长100-iteration ceiling，也未支持直接修改 derivative floor、return/wage guards、solver、pseudo-time、update law、tolerance、grid、boundary/KKT 或 economic parameters。

KFE继续`DIAGNOSTIC_ONLY`；finite-box upper-b leakage / MATLAB-style pinning独立未解决。Standalone KKT residual unavailable。长期目标仍为`ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。

唯一 next gate：`OWNER_HJB_ITERATION_FIXED_POINT_MECHANISM_INTERVENTION_DESIGN_FREEZE`。在Owner/Reviewer冻结一个isolated same-input HJB-map intervention之前，不发布successor runtime task。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。