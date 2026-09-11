# Chapter 5 当前规则入口
更新：2026-09-11；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`C1_PRICE_NUMERAIRE_RAW_RA_FORENSIC_ACCEPTED__RAW_RA_PRESSURE_PRIMARILY_YK_MPK_GEOMETRY__RETURN_BOUNDS_NOT_ECONOMICALLY_IDENTIFIED__PRICE_NORMALIZATION_OWNER_DECISION_REQUIRED`。
当前 active Builder task：无。
最新接受候选：`8c0606ebc67e8f51a0a27ff06505ce67bd69ba7d`。
Reviewer acceptance：`docs/CH5_MP4C_C1_PRICE_NUMERAIRE_RAW_RA_FORENSIC_AND_NORMALIZATION_SPEC_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

最新 zero-science price/numeraire/raw-ra forensic 已接受。775/775 accepted C1 province-turn rows 完成静态 raw-return 分解，最大 `ra0` 重建误差=`2.220446049250313e-16`。turn25 raw `ra0` min/median/max=`0.08784757593701044/0.2140623214392065/0.40633797203054156`，30/31 省高于历史 `.09` 上界。

return pressure 的主来源已定量：dominant term 为 `rk=mt*alpha*Y/K`。turn25 即使移除 profit term，仍有30/31省 `ra0_without_profit>.09`；即使静态替换 `mt->mstar=.9`，仍有30/31省超过 `.09`。profit 在28/31省被 floor 到0，折旧固定贡献 `-.025`，因此都不是主要上压来源。accepted corrected-2018 `Y/K` 相对历史 return safeguard 的几何关系是当前直接解释，`mt`仅小幅放大。

return bounds `[.02,.09]` 当前分类为 `EMPIRICAL_NUMERICAL_SAFEGUARD`，不是已识别的经济回报率区间。wage bounds `[.8,1.3]` 分类为 `SOURCE_VALUE_WITH_UNRESOLVED_ECONOMIC_UNIT`。当前证据不足以直接扩大或删除 return clips，也不足以选择新的 `ra` target/period convention。

firm raw wage 与 household composite wage 不能按数值水平直接比较：firm wage 有 MU/NU-per-model-period 的 implied macro unit，而 legacy wage clip 缺少绝对单位映射；household `w` 是经过31个 destination 的非线性 composite aggregator。存在 numeraire/aggregation mapping 未闭合，但本 forensic 没有证明该问题直接造成当期 `ra0`；它只可能通过后续 household labor/assets、firm Y/K 与 mt 间接影响 return path。

accepted origin-preserving normalized labor successor 继续保持 inactive；当前最低风险顺序不是叠加 labor change，而是先由 Owner 冻结一个明确、单位一致、预先注册的 price/return normalization object。Owner decision 至少需要明确：return period/concept、firm-to-household wage numeraire mapping（currency/deflator/period/labor unit/aggregator normalization），以及是否继续保留现有 return bounds 仅作为 safeguard。冻结前不得自动发布新的 scientific task。

C1 residual public-asset result继续作为当前资本 authority：turn20-25 total-K/target=1/1/1，GovInv overshoot 已从 bounded dynamic path 中消失；资本数量本身不再是同一优先级的直接 numerical blocker。HJB 从turn6起31/31 converged，但 KFE 775/775 仍为 `DIAGNOSTIC_ONLY`，继续作为独立 scientific blocker；price/numeraire工作不得吞并KFE治理。

corrected-2018 runtime input-binding repair继续作为唯一活动数据契约：actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、`MU=10万元`、`NU=100 persons`、same-year Zt0；legacy/canonical fallback已隔离。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新科学执行必须先发布exact GitHub task；发布task时同一回复自动附Codex启动prompt。
