# Chapter 5 两资产 HANK 当前状态

更新：2026-09-14。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`MACRO_K_UNIT_REBASE_COHERENT__HOUSEHOLD_MONETARY_BRIDGE_UNPROVEN__BMAX_OWNER_SELECTION_REQUIRED`。

最新 accepted real-wage/macro-scale candidate：`41993260d87387235a2e58cc9a93a8aa06b98515`。
Reviewer acceptance：`docs/CH5_MP4C_K1_REAL_COMPOSITE_WAGE_DOMAIN_STANDALONE_3X3_AND_MACRO_SCALE_AUDIT_ACCEPTANCE.md`。
Owner/Reviewer freeze：`docs/CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_FREEZE_CURRENT.md`。
最新完成 Builder task：`tasks/CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT.md`；active Builder task=`NONE`，未发布 successor task。
Results eligibility=`FALSE`。

Accepted real-wage scan：`rb=.02`、`ra={.06,.0675,.07}`、household composite `w={13,15.5,18}`。HJB 9/9 legal/converged；KFE 9/9；illiquid `a` distribution 9/9 interior。重要 caveat：liquid `b` marginal 9/9 的 mode 都在 `bmax=5`，且上界质量为实质值，不能把这些点升级为 fully healthy/admissible steady states。

Macro scale audit 仍为 `DIMENSIONAL_RELATION_UNRESOLVED`。GDP/capital、population、wjt、household composite wage 的 source scaling/aggregation 已部分证明，但 household wage 与 macro MU/NU、现实 monetary unit、model period 的统一桥接尚未证明；不得直接修改 `wjt` guard。

Owner 新冻结方向：当前 `amax=10`、`bmax=5` 均偏小。优先审查 asset-domain bounds，而不是先提高 `I/J`。Owner 提议把 monetary/asset quantities 统一到 `k`（千元）单位，并以 `amax=100` 作为第一 illiquid-asset upper-domain target；这仍是待 source-consistent dimensional audit 的设计假设，不是已授权 implementation。`amax` 是 individual household state-grid upper bound，`At` 是分布导出的平均/聚合对象，二者不得混同。

已核对原 MATLAB source：`param.GDP_multiplier=1000`、`param.POP_multiplier=100`；GDP/capital import 乘 GDP multiplier，population import 乘 POP multiplier，导出时再按相应 multiplier 除回。该事实不能简化成“所有变量都除以1000”，后续 task 必须逐变量追踪。

Zero-science-runtime 设计审计已完成。Macro chain 可 coherent rebase 到 `1 monetary model unit=1k currency`：aggregate money 与 person quantities 数值均乘 100，因而 `Y/N`、`K/N`、`Z`、raw firm wage 与 rates 数值不变。household `w/C/Tt/a/b/At/Bt` 到同一现实 monetary/period 单位的 bridge 仍未证明，结论为 `MONETARY_UNIT_BRIDGE_UNPROVEN`。

Owner-proposed `amax=100` 仅在 household k/person bridge 被接受后 dimensionally coherent；它是 individual state-grid bound，不是 `At` cap。`bmax` 不可 outcome-fit，bounded candidates 为 `{20,50}`，需 Owner 选择。I=J=20 时 `da=100/19≈5.26316`，对应 `db=22/19≈1.15789` 或 `52/19≈2.73684`；仅适合 first domain diagnostic，production 前必须独立 precision-sensitivity gate。

报告：`docs/CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT_REPORT.md`。Compact evidence：`docs/evidence/ch5_mp4c_k1_k_unit_normalization_asset_domain_design/`。Scientific/model runtime、parameter/grid changes 与 Results 全部为 0。

唯一下一 Owner gate：`OWNER_REVIEW_HOUSEHOLD_K_UNIT_BRIDGE_AND_BMAX_SELECTION`。在此之前先由 ChatGPT Reviewer 对 Builder candidate 独立 ACCEPT/REJECT；不得 merge main 或发布 successor task。
