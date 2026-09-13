# Chapter 5 两资产 HANK 当前状态
更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_TRANSFER_RAW_CANDIDATE_CENSUS_CANDIDATE_COMPLETE__INDEPENDENT_L3_REVIEW_REQUIRED__NUMERIC_LADDER_UNRESOLVED`。

最新 accepted transfer-control design candidate：`bdc2ecd48ca3408cf10138ee58d02383185ffd50`。
Reviewer acceptance：`docs/CH5_MP4C_K1_TRANSFER_CONTROL_ADMISSIBILITY_SAFEGUARD_ZERO_SCIENCE_DESIGN_ACCEPTANCE.md`。
Owner transfer-control safeguard freeze：`docs/CH5_MP4C_K1_TRANSFER_CONTROL_TEMPORARY_ADMISSIBILITY_SAFEGUARD_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_TRANSFER_CONTROL_RAW_CANDIDATE_CENSUS_INSTRUMENTED_BOUNDED_DIAGNOSTIC.md` 已在candidate branch完成，尚未被独立Reviewer接受。
Results eligibility=`FALSE`。

## Candidate closure（待独立Reviewer验收）

Candidate在完全冻结science下完成G1/G2各5 turns：310 HJB、310 KFE、27,196 HJB iterations。Observation-only census持久化87,027,200个raw branch-cell candidates，全部finite；21,756,800个iteration-cell selected controls全部可由记录的raw contributors exact重建。108,784个raw arrays的min/median/p95/p99/max/hash与旧accepted summaries逐项exact match。

Exact pooled `abs(d)`为p50 `2.7556`、p99 `2,888.04`、p99.9 `58,175.12`、p99.99 `1,015,033.53`，极值约`-2.785e9`至`+1.715e12`。尾部在preregistered `1e2–1e8` grid上连续存在；唯一巨大相邻比只隔离top two positive outliers，不形成branch/path/turn2-robust cutoff。因此numeric ladder仍需Owner/Reviewer决定，未实现任何safeguard。

报告：`docs/CH5_MP4C_K1_TRANSFER_CONTROL_RAW_CANDIDATE_CENSUS_INSTRUMENTED_BOUNDED_DIAGNOSTIC_REPORT.md`。

唯一next gate：`INDEPENDENT_GPT_L3_ACCEPT_OR_REJECT_RAW_CANDIDATE_CENSUS_CANDIDATE`。

## 已接受：temporary transfer-control safeguard design
Zero-science design 已确认 raw transfer candidates 存在巨大但 finite 的 explosive tail。现有 instrumented summaries 代表 `87,027,200` 个 branch-cell candidate evaluations，所有 persisted nonfinite counts 为0，但 raw witnesses 约从 `-2.785e9` 到 `+1.715e12`。最终 selected `d` 的248,000个cell可精确读取，`abs(d)` median约`1.38`、p99约`1.62e3`、p99.9约`3.72e4`、max约`4.27e7`。

现有 accepted traces 没有保存完整 cell-level raw branch arrays，因此无法诚实获得 pooled raw quantiles、exact raw threshold-hit shares、branch-cell sign frequencies或唯一可辩护的 numeric ladder。`1e3/1e4/1e5/1e6`只接受为 static sensitivity grid，不是 frozen stages。

Safeguard semantics 中，当前 evidence 最支持 `C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION`：保留raw FOC receipt，越界raw branch不参与selector竞争，同时保留accepted zero-transfer option；不推荐candidate clipping，因为会制造不满足原FOC的endpoint surrogate。该语义目前仍是 Reviewer preferred design，不等于Owner numeric/implementation freeze。

## Reviewer 对 next gate 的修正
由于完整raw arrays从未持久化，进一步纯zero-science分析不能从hash/summary中恢复cell-level raw distribution。下一门必须是**observation-only raw-candidate census bounded runtime**，重复完全相同的accepted annual G1/G2 5-turn science，只增加raw-candidate census持久化；不得实现任何transfer safeguard。

任务必须持久化每次HJB iteration、每个raw transfer branch、每个grid cell的raw `d`，并生成exact branch-wise pooled quantiles、sign frequencies、threshold hit shares、turn/path/return/wage/interior-boundary partitions。完整census放sealed external evidence，Git仅保存compact summaries/manifests。

## Frozen science
`chi0=.1`、`chi1=2 years`、annual calibration、transfer FOC、derivative floor、G1/G2 return guards、`wjt [.8,1.3]`、selector/boundary/KKT law、grid、tolerance、solver、K1/C1、source-faithful labor全部保持不变。当前没有任何active `d` bound/rejection/clipping。

Price-bound hit monitoring继续强制；长期目标仍为`ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`，最终科学结果也不得依赖binding temporary transfer-control safeguard。

不得 longer G2、G3/G4、wage relaxation、K1B/K2。KFE仍为`DIAGNOSTIC_ONLY`，finite-box upper-b leakage与MATLAB-style pinning独立未解决。Standalone KKT residual=`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。

Results eligibility=`FALSE`。
