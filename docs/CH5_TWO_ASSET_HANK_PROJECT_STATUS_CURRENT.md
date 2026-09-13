# Chapter 5 两资产 HANK 当前状态

更新：2026-09-14。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT_TASK_ACTIVE`。

最新 accepted real-wage/macro-scale candidate：`41993260d87387235a2e58cc9a93a8aa06b98515`。
Reviewer acceptance：`docs/CH5_MP4C_K1_REAL_COMPOSITE_WAGE_DOMAIN_STANDALONE_3X3_AND_MACRO_SCALE_AUDIT_ACCEPTANCE.md`。
Owner/Reviewer freeze：`docs/CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT.md`。
Results eligibility=`FALSE`。

Accepted real-wage scan：`rb=.02`、`ra={.06,.0675,.07}`、household composite `w={13,15.5,18}`。HJB 9/9 legal/converged；KFE 9/9；illiquid `a` distribution 9/9 interior。重要 caveat：liquid `b` marginal 9/9 的 mode 都在 `bmax=5`，且上界质量为实质值，不能把这些点升级为 fully healthy/admissible steady states。

Macro scale audit 仍为 `DIMENSIONAL_RELATION_UNRESOLVED`。GDP/capital、population、wjt、household composite wage 的 source scaling/aggregation 已部分证明，但 household wage 与 macro MU/NU、现实 monetary unit、model period 的统一桥接尚未证明；不得直接修改 `wjt` guard。

Owner 新冻结方向：当前 `amax=10`、`bmax=5` 均偏小。优先审查 asset-domain bounds，而不是先提高 `I/J`。Owner 提议把 monetary/asset quantities 统一到 `k`（千元）单位，并以 `amax=100` 作为第一 illiquid-asset upper-domain target；这仍是待 source-consistent dimensional audit 的设计假设，不是已授权 implementation。`amax` 是 individual household state-grid upper bound，`At` 是分布导出的平均/聚合对象，二者不得混同。

已核对原 MATLAB source：`param.GDP_multiplier=1000`、`param.POP_multiplier=100`；GDP/capital import 乘 GDP multiplier，population import 乘 POP multiplier，导出时再按相应 multiplier 除回。该事实不能简化成“所有变量都除以1000”，后续 task 必须逐变量追踪。

当前 task 为 zero-science-runtime 设计审计：不运行 HJB/KFE/global model，不修改参数/guards/grids。目标是证明或否定 coherent `1 monetary model unit = 1k currency units` normalization，逐方程识别需要数值转换的 dimensionful parameters，设计 `amax=100` 与新的 `bmax`，并评估 I=J=20 下新的 `da/db` 精度后果。

唯一下一 gate：Builder 完成 `CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT` 后，由 ChatGPT Reviewer 独立 ACCEPT/REJECT，再决定是否发布 bounded normalization/domain implementation task。
