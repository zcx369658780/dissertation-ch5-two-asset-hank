# Chapter 5 两资产 HANK 当前状态

更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`REAL_COMPOSITE_WAGE_DOMAIN_STANDALONE_3X3_AND_MACRO_SCALE_AUDIT_TASK_ACTIVE`。

最新 accepted mapping audit candidate：`3975d42fae57cc25f179225857b5defce1d7731f`。
Reviewer acceptance：`docs/CH5_MP4C_K1_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT_ACCEPTANCE.md`。
Owner/Reviewer freeze：`docs/CH5_MP4C_K1_REAL_COMPOSITE_WAGE_DOMAIN_AND_MACRO_SCALE_CONSISTENCY_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_REAL_COMPOSITE_WAGE_DOMAIN_STANDALONE_3X3_AND_MACRO_SCALE_AUDIT.md`。
Results eligibility=`FALSE`。

Accepted mapping audit：standalone `w` 与省级 household-HJB consumed `results.w` / `HouseholdInputs.wages[0]` 是同一 household-wage object；`guarded_wjt` 是上游 firm wage，必须经 source-defined aggregation 才生成 composite wage。Accepted provincial composite wage turn1 约 `13.84–18.52`、turn2 约 `12.84–17.48`，而旧 standalone map 只覆盖 `.8/1.05/1.3`，所以 62/62 provincial states 均在旧 health-map wage coverage 外。

当前 active task 将 standalone household wage 扩展到真实 composite-wage scale，但不修改 `wjt` range。Exact grid：`rb=.02`；`ra={.06,.0675,.07}`；`w={13.0,15.5,18.0}`，共 9 个 Cartesian points。保持 accepted MATLAB-faithful HJB/KFE 算法、grid、numerics、FOC、selector、boundary、transition legality 和 contaminated-row KFE 完全不变；不得 damping、solver/tolerance/grid/derivative-floor/guard 变化，不得自适应加点。

同一任务增加 read-only macro-scale consistency audit：追踪省级 GDP/output、population/per-capita GDP、`wjt`、household composite `w`、investment/capital/GDP scaling multipliers/divisors、productivity/labor normalization。必须区分统计物理单位、model-normalized scale、dimensionless/calibrated object 与无法证明单位的对象；不得把变量标签直接解释为人民币/元。

如果真实 composite-wage scan 广泛不收敛、KFE 严重病态或普遍撞人工边界，不得现场调 `wjt`/`ra`/GDP/投资乘数。应转入 joint recalibration Owner gate，并在未来改 `wjt` 范围前共同核对省级 GDP、人均 GDP、household average/composite wage 的数量级和现有 normalization。

Runtime：HJB exactly 9；KFE<=9、仅在 HJB converged 后；global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results 全部 0。Standalone contaminated-row KFE 与 unresolved corrected-2018 multi-province finite-box upper-b leakage/MATLAB-style pinning blocker继续分离。

下一 gate：Builder完成 active exact task 后，由 ChatGPT Reviewer 独立 ACCEPT/REJECT，并依据真实 wage-domain scan 与 macro-scale audit 选择 exactly one Owner gate。
