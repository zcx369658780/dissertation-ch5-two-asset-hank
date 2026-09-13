# Chapter 5 当前规则入口
更新：2026-09-13；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. accepted bilateral-capital / scoring-data / payoff / annual-HJB / price-guard authority docs
6. `docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_SCAN_ACCEPTANCE.md`
7. `docs/CH5_MP4C_K1_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT_ACCEPTANCE.md`
8. `docs/CH5_MP4C_K1_REAL_COMPOSITE_WAGE_DOMAIN_AND_MACRO_SCALE_CONSISTENCY_FREEZE_CURRENT.md`
9. active exact task：`tasks/CH5_MP4C_K1_REAL_COMPOSITE_WAGE_DOMAIN_STANDALONE_3X3_AND_MACRO_SCALE_AUDIT.md`

当前状态：`REAL_COMPOSITE_WAGE_DOMAIN_STANDALONE_3X3_AND_MACRO_SCALE_AUDIT_TASK_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_REAL_COMPOSITE_WAGE_DOMAIN_STANDALONE_3X3_AND_MACRO_SCALE_AUDIT.md`。
最新 accepted mapping audit candidate：`3975d42fae57cc25f179225857b5defce1d7731f`。
Results eligibility=`FALSE`。

Accepted wage identity：standalone `w` 与 provincial household HJB consumed `results.w` / `HouseholdInputs.wages[0]` 语义/API identity 对齐；上游 `wjt` 必须经 source-defined aggregation。旧 standalone wage `.8/1.05/1.3` 与真实 provincial composite wage 约 `12.84–18.52` 完全错位，因此旧 health map不能给省级状态赋健康标签。

Active exact scan：`rb=.02`；`ra={.06,.0675,.07}`；household composite `w={13.0,15.5,18.0}`。只允许 9 个 Cartesian points；不改 `wjt` range，不改 HJB/KFE，不允许 outcome-adaptive tuning。

Active task 同时进行 macro-scale audit：核对省级 GDP/output、population/per-capita GDP、household average/composite wage、`wjt`、GDP/investment/capital scaling multiplier/divisor、productivity/labor normalization。任何未来 `wjt` range 调整前必须先核对 GDP、人均 GDP、household wage 的数量级和单位/normalization chain。

若真实 wage-domain scan 广泛失败或尺度审计 unresolved，不得继续单变量调参；转入 joint recalibration Owner gate，联合审查 `wjt→w`、return mapping→`ra/rah` 与 macro output/investment scaling。

Scientific runtime 限定：HJB=9；KFE<=9；global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results=0。Standalone contaminated-row KFE 与 corrected-2018 multi-province KFE blocker 分离。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
