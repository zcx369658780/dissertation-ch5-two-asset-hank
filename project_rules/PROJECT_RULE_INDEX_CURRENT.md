# Chapter 5 当前规则入口
更新：2026-09-12；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
6. `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
7. `docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`
8. `docs/CH5_MP4C_K1_PAYOFF_SCALE_MAPPING_AND_DIAGNOSTIC_BOUND_POLICY_FREEZE_CURRENT.md`
9. `docs/CH5_MP4C_K1_ANNUAL_HJB_COMPLETE_RECALIBRATION_CONTRACT_FREEZE_CURRENT.md`
10. `docs/CH5_MP4C_K1_PRICE_GUARD_CONTINUATION_AND_BOUNDARY_HIT_MONITORING_FREEZE_CURRENT.md`
11. `docs/CH5_MP4C_K1_ANNUAL_HJB_G1_VS_G2_PRICE_GUARD_CONTINUATION_DIAGNOSTIC_ACCEPTANCE.md`
12. 当前 active exact task 及直接相关 report/evidence。

当前状态：`K1_ANNUAL_HJB_G1_VS_G2_CONTINUATION_ACCEPTED__G2_RESTORES_PARTIAL_RETURN_HETEROGENEITY_BUT_DEGRADES_HJB__FOCUSED_HA_HJB_MECHANISM_DIAGNOSTIC_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_G1_VS_G2_HA_HJB_MECHANISM_ZERO_SCIENCE_DIAGNOSTIC.md`。
最新 accepted continuation candidate：`ab6b19022d920a8929a2ee66cc5511be6f602557`。
Results eligibility=`FALSE`。

Annual G1 vs G2 bounded continuation 已接受：G1 treatment return upper-hit=`124/124`；G2=`84/124`，并恢复`40/124` unsaturated observations和部分HJB-consumed return heterogeneity。但 G2 HJB convergence 从 G1 `18/124`降到`6/124`，且若干transfer/adjustment-cost/drift extrema显著放大。因此不得 longer G2，也不得进入G3/G4。

Legacy wage safeguard `[.8,1.3]` 继续固定且高度绑定：G1 wage hits=`112/124`，G2=`109/124`。每个后续 runtime task仍必须记录return/wage upper/lower/unsaturated province names、counts和shares；长期目标仍是`ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。

当前 zero-science mechanism task 只读取已保存 G1/G2 evidence 与 accepted HJB source，定位 convergence loss/control-drift amplification 到province/turn/grid cell、return saturation regime、wage-hit regime、policy branch、value-derivative/transfer-FOC chain及boundary/interior状态。新增trajectory/HJB/KFE/firm/household等科学调用预算全部为0。

在该机制诊断完成前，不得改`chi0/chi1`、derivative floor、boundary/KKT law、solver/grid/tolerance、annual calibration或wage guard；不得 longer G2、G3/G4、K1B/K2。KFE finite-box upper-b leakage/MATLAB-style pinning仍为独立blocker，KFE=`DIAGNOSTIC_ONLY`。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复自动附Codex启动prompt。
