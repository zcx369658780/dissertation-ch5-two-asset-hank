# Chapter 5 两资产 HANK 当前状态

更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT_ACCEPTED__OWNER_REVIEW_TWO_DIMENSIONAL_HEALTH_REGION_UNRESOLVED`。

Accepted candidate：`3975d42fae57cc25f179225857b5defce1d7731f`。
Reviewer acceptance：`docs/CH5_MP4C_K1_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT_ACCEPTANCE.md`。
当前 active Builder task：NONE。Results eligibility=`FALSE`。

Accepted wage semantic gate：`WAGE_VARIABLE_IDENTITY_PROVEN_DIRECTLY_COMPARABLE`。Standalone scan `w` 与 multi-province household HJB consumed `results.w` / `HouseholdInputs.wages[0]` 是同一 household-wage object/API role；`guarded_wjt` 是上游 firm wage，必须通过 source-defined wage aggregation 转换为 household composite wage。不得把 `wjt` 直接作为 standalone coordinate，也不得人为缩放或 normalization tuning。

Accepted observed standalone health map 共 27 点：interior=4、ambiguous=7、lower=7、upper=8、KFE pathological=1。该 map 仅支持 exact observed coordinates；不得 interpolation/fitted boundary 后宣布 admissible。

关键新结论：省级 household consumed composite wage 与 standalone scan 的数值覆盖完全不重叠。Standalone observed wage 仅为 `.8/1.05/1.3`；accepted provincial turn1 composite wage 约 `13.8375–18.5197`，turn2 约 `12.8426–17.4810`。因此 accepted 62 个 provincial states 全部为 `UNOBSERVED_OR_INTERPOLATION_NOT_AUTHORIZED`，不能从当前 standalone map 继承 interior/lower/upper/ambiguous 健康标签。

20/20 turn1-converged→turn2-failed 省份均表现为 consumed `ra` 上升、composite wage 下降，但由于两端都在 standalone wage coverage 之外，这只能是描述性共变，不能证明跨越 health frontier 或构成失败原因。Return guard / wage guard 也不能唯一分离成功与失败。

重要 caveat：`(.06,.8)` standalone contaminated-row KFE 的 severe signed pathology 继续保留并视为 non-admissible；不得 clipping。Standalone contaminated-row KFE 仍不解决 corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker。

当前不得继续自动一维 `ra` refinement，也不得直接进入 provincial return-mapping redesign。唯一下一 Owner gate：`OWNER_REVIEW_TWO_DIMENSIONAL_HEALTH_REGION_UNRESOLVED`。Owner/Reviewer 应先决定如何把 standalone `(ra,w)` health-map coverage 扩展到真实 provincial household composite-wage domain，再讨论 return mapping 改造。
