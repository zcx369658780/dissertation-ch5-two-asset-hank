# Chapter 5 当前规则入口
更新：2026-09-11；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`ORIGIN_PRESERVING_BILATERAL_LABOR_NORMALIZATION_ACCEPTED__GOVINV_INITIALIZATION_PRIVATE_K_RECONCILIATION_AUTHORIZED`。
当前 active Builder task：`tasks/CH5_MP4C_INITIAL_PRIVATE_K_OBSERVATION_AND_RESIDUAL_GOVINV_PROBE.md`。
最新接受候选：`a76ea81eda4093ce762bf6660b5fbdff0a7ec700`。
Reviewer acceptance：`docs/CH5_MP4C_ORIGIN_PRESERVING_BILATERAL_LABOR_NORMALIZATION_IMPLEMENTATION_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

最新劳动实现已接受。legacy/source-faithful `reconstruct_migration_labor` 与 `run_source_faithful_one_turn` 保持不变；新的 normalized successor route 显式保留 `destination x origin` 31×31 双边矩阵。每个来源省由 `household_labor_per_capita * population` 形成 origin aggregate labor mass，`Lt_seperate`-style attractiveness kernel 按 origin 列归一化后构成双边 flow matrix，确保 origin-column 与全国劳动守恒，同时保留省际流向溯源。该 normalized route 尚未连接 steady-state/annual runtime。

资本侧仍是下一主要稳态 blocker。accepted 25-turn corrected-2018 evidence显示 turn20-25 `firm_K_total/Ktarget` median约`2.36`，其中 private K median约`0.0029`，GovInv median约`2.358`；overshoot明确由 GovInv 主导。Owner进一步说明历史 `HANK_mp_1eq.m` 通过 clipped return 触发 GovInv 的 ±10% 乘法更新，是在无法直接识别复杂网络各省投资额时使用的经验逼近；该方法在其他状态不稳定时可能导致 Kt 发散，因此同意试验 residual initialization 思路。

当前 active task 只做一次清晰标记的 initial household observation：在 accepted corrected-2018 fixed initial states/prices 下，各省最多一次 HJB/KFE/aggregate，随后全批量一次 At-only productive-capital allocation，得到 `Kt_supply_initial`。然后只做会计比较：历史 G0 `GovInv0=Ktarget` 与候选 G1 `GovInv0=max(Ktarget-Kt_supply_initial,0)`。本任务不得调用 firm、migration、wage、GovInv controller、outer turn 或 steady state，也不得把 G1 接入 active runtime。

At-grid→MU bridge仍未生产识别。本 task 仅保留 source-faithful `beta_a=1` 为 `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`，并必须报告符号尺度关系 `Kt_supply(beta)=beta*Kt_supply(beta=1)` 及逐省 `beta_a_star=Ktarget/Kt_supply(beta=1)`，不得从 convergence/target matching 反推 beta。HJB/KFE diagnostic blockers继续保留并单独报告。

corrected-2018 runtime input-binding repair继续作为唯一活动数据契约：actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、`MU=10万元`、`NU=100 persons`、same-year Zt0；legacy/canonical fallback已隔离。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新科学执行必须先发布exact GitHub task；发布task时同一回复自动附Codex启动prompt。
