# Chapter 5 当前规则入口
更新：2026-09-10；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`CORRECTED_2018_25TURN_KL_RECONCILIATION_REJECTED__PREMATURE_HJB_NONCONVERGENCE_STOP_NOT_SOURCE_BACKED__PROPAGATION_REPAIR_AND_BOUNDED_RERUN_AUTHORIZED`。
当前 active Builder task：`tasks/CH5_MP4C_CORRECTED_2018_HJB_NONCONVERGENCE_PROPAGATION_AND_25TURN_KL_RERUN_REPAIR.md`。
最新接受候选：`a7bd3b1a705ff42e2933b22a8c6563ec47248ce4`。
最新Reviewer rejection：`docs/CH5_MP4C_CORRECTED_2018_25_TURN_KL_TARGET_RECONCILIATION_DIAGNOSTIC_REJECTION.md`。
Results eligibility=`FALSE`。

最新实现修复仍为已接受 authority：corrected-2018 active runtime单一路径绑定actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、`MU=10万元`、`NU=100 persons`及same-year `Zt0`；legacy/canonical fallback已隔离，31/31 pre-science assertions和旧尺度注入fail-closed继续有效。

候选`a0e117ade98f8197bb76cd2471f7932d545afbcc`未被接受。其corrected runtime绑定本身通过，但25-turn harness在安徽turn1 HJB达到100次、`converged=false`后立即`raise`，导致0个完整outer turns。accepted MATLAB multi-province source contract只把31个household convergence flags作为最终steady-state predicate的一部分，没有证明单个household nonconvergence必须立即中止当前turn。因此该early stop属于Python harness额外严格规则，不能作为source-faithful K/L reconciliation的终止依据。

当前active task先修复这一传播逻辑：有限且结构可用的HJB返回即使`converged=false`，也要标记为`HJB_NONCONVERGED_DIAGNOSTIC_ONLY`并继续source-style KFE/aggregate/downstream turn；false convergence flag必须保留并阻止最终source steady-state acceptance。只有真正无法继续的nonfinite/unusable return、KFE hard failure、shape/order failure或不可恢复异常才允许提前终止。

修复通过zero-science tests后，只允许一条新的correctly-bound 25-turn K/L trajectory；冻结数据、GovInv0=Ktarget、Lt_seperate、beta_a、price bounds、HJB/KFE equations/tolerances/grids、damping/hysteresis等，不得调参。重点仍是turn20-25的firm total/private/GovInv K相对Track-A target与destination firm labor相对population proxy的reconciliation，并新增逐轮HJB nonconverged-but-continued省份轨迹。

此前firm-price forensic仍有效：wage bound主要受未闭合numeraire影响；firm return主要受`Y/K`经济比率相对历史数值safeguard影响。household绝对货币归一化、asset bridge识别、GovInv初始化科学规则、Lt迁移/生产劳动映射、KFE/HJB独立blockers均尚未解决。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新科学执行必须先发布exact GitHub task；发布task时同一回复自动附Codex启动prompt。