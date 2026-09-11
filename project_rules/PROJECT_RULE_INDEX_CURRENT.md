# Chapter 5 当前规则入口
更新：2026-09-11；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
6. `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
7. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`K1A_SYMMETRIC_BOUNDED_RERUN_ACCEPTED__PAYOFF_RETURN_REAUDIT_REQUIRED_BEFORE_K1B`。
当前 active Builder task：无，待发布 payoff-return re-audit exact task。
最新 accepted K1A symmetric rerun candidate：`ca66dd5d7364f80ed2686d4d2e77a1a6adab2ecb`。
Reviewer acceptance：`docs/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_SYMMETRIC_RERUN_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

资本网络总体科学设计冻结稿：
`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。
K1 scoring/data 当前冻结稿：
`docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`。

K1A symmetric bounded rerun已经接受：equal-share `beta_distance=0` 与 pure-geographic `beta_distance=2` 均完成25 turns，K1 accounting、same-S、C1 residual-public-assets 与 source-faithful labor gates通过。geography差异从turn2起通过network-produced `rah`进入household并传播到后续firm states。

当前不能直接进入K1B。对称rerun中 Path A/B raw `ra0>.09` 分别为 `754/775` 和 `755/775`，说明 current source-used/clipped `ra` 仍只能作为 `K1A_SOURCE_FAITHFUL_PAYOFF_BRIDGE__NOT_FINAL_ECONOMIC_RETURN_AUTHORITY`。进入任何改变 household `rah` 的下一阶段前，必须先完成payoff-return re-audit，厘清raw `ra0`、used/clipped `ra`、period/unit/numeraire、firm decomposition及clipping distortion。

K1B `beta_return=.5` 仍仅为preregistered，不授权runtime。K2不授权。corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning仍是独立KFE blocker。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复自动附Codex启动prompt。
