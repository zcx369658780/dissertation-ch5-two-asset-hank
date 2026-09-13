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
7. `docs/CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT_ACCEPTANCE.md`
8. `docs/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_BRIDGE_AND_ASSET_DOMAIN_DIAGNOSTIC_FREEZE_CURRENT.md`
9. active exact task：`tasks/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC.md`

当前状态：`HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC_TASK_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC.md`。
最新 accepted design-audit candidate：`6b89d8e47f075906d463f58f3e984bf8665710f6`。
Results eligibility=`FALSE`。

Owner 已批准本轮 diagnostic convention：household monetary bridge 临时冻结为 `h=1`，即现有 household `w/C/Tt/a/b/At/Bt` 数值作为 k-unit diagnostic numerics 使用，不做额外 monetary rescale；这不是最终现实货币单位证明。

Stage A：`amin=0`、`amax=100`、`bmin=-2`、`bmax=20`、`I=J=20`；science grid 固定为 `rb=.02`、`ra={.06,.0675,.07}`、composite `w={13,15.5,18}`，9 个 fresh standalone points。

预注册 Stage B：仅当 Stage A 至少一个 KFE-valid point 的 modal `b` 精确等于 `bmax=20` 时，运行唯一的 bounded escalation `bmax=50`，其余全部不变；禁止进一步扩大。Stage B 若仍有 exact-`bmax` mode，则停止并进入 unresolved review。

HJB/KFE equation、FOC、selector、boundary、rates、solver、tolerance、derivative floor、`wjt` guard、`ra` mapping 均冻结。Global multi-province / firm / MATLAB / GE / Results runtime 均禁止。

Owner 已授权 ChatGPT Reviewer 对后续类似的小范围、本地数值校准/调试直接做 bounded 决策并发布 exact task，但必须预注册、范围有限且不得改变结构性经济模型、accepted equations/guards、因果解释或 Results eligibility；结构性变更仍由 Owner 决定。

即使 asset-domain boundary 清除，`I=J=20` 仍只获得 domain-diagnostic authority；production 前必须单独 precision-sensitivity gate。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
