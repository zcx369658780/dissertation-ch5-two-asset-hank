# Chapter 5 当前规则入口
更新：2026-09-14；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. accepted bilateral-capital / scoring-data / payoff / annual-HJB / price-guard authority docs
6. `docs/CH5_MP4C_K1_REAL_COMPOSITE_WAGE_DOMAIN_STANDALONE_3X3_AND_MACRO_SCALE_AUDIT_ACCEPTANCE.md`
7. `docs/CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_FREEZE_CURRENT.md`
8. active exact task：`tasks/CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT.md`

当前状态：`K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT_TASK_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT.md`。
最新 accepted real-wage/macro-scale candidate：`41993260d87387235a2e58cc9a93a8aa06b98515`。
Results eligibility=`FALSE`。

Accepted real-wage scan：`w={13,15.5,18}`、`ra={.06,.0675,.07}` 下 9/9 HJB legal/converged 且 illiquid `a` distribution interior；但 liquid `b` marginal 9/9 mode 位于 `bmax=5`，所以 asset-domain adequacy 尚未闭合。

Macro-scale relation 仍 unresolved；不得直接调整 `wjt` guard 或把不同 normalization 的 GDP/per-capita GDP/wage 当作同一 monetary unit。

Owner 方向：当前 `amax=10`、`bmax=5` 偏小；优先审查 domain bounds。提议统一 monetary/asset quantities 到 `k` 单位，并以 `amax=100` 为第一 illiquid-domain target。该提议须先通过 source-consistent dimensional/equation audit；不得直接 implementation。

Original MATLAB scaling source facts：`GDP_multiplier=1000`、`POP_multiplier=100`；GDP/capital 和 population 使用不同 multiplier，export 再分别除回。不能概括为所有变量统一 `/1000`。

Active task 为 zero-science-runtime：逐变量/逐方程定义 k-unit transformation、识别 dimensionful parameter transforms、设计 `bmax` 候选、计算 I=J=20 下新的 `da/db`，并形成 bounded implementation proposal。HJB/KFE/global model runtime 全部为0。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
