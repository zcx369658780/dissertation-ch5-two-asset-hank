# Chapter 5 当前规则入口
更新：2026-09-10；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`ORIGIN_PRESERVING_BILATERAL_LABOR_NORMALIZATION_ACCEPTED__FULL_MATRIX_TRACEABILITY_AND_ORIGIN_MASS_CONSERVATION_ENFORCED__GOVINV_REMAINS_NEXT_PRIMARY_STEADY_STATE_BLOCKER`。
当前 active Builder task：无。
最新接受候选：`a76ea81eda4093ce762bf6660b5fbdff0a7ec700`。
Reviewer acceptance：`docs/CH5_MP4C_ORIGIN_PRESERVING_BILATERAL_LABOR_NORMALIZATION_IMPLEMENTATION_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

最新劳动实现已接受。legacy/source-faithful `reconstruct_migration_labor` 与 `run_source_faithful_one_turn` 保持不变；新的 normalized successor route 显式保留 `destination x origin` 31×31 双边矩阵。每个来源省先由 `household_labor_per_capita * population` 形成 origin aggregate labor mass；现有 `Lt_seperate`-style attractiveness kernel 生成 `q[j,i]` 后按 origin 列归一化，形成 `s[j,i]`，再用 `M[j,i]=s[j,i]*L_origin_i` 构造双边流量。每个 origin 列守恒到来源省劳动总量，全国 destination labor 与全国 origin labor 守恒，同时保留逐省净流入/流出和完整来源去向溯源。

该接受不等于 labor calibration 或 wage aggregation 已完成。当前 CES-like `composite_household_wages` 未修改；完整 `M[:,i]` 与 `s[:,i]` 仅为以后单独 wage-provenance 任务提供可审计的来源-目的地信息。normalized one-turn route 尚未连接 steady-state/annual runtime，任何科学整合仍需新 exact task。

资本侧仍是下一主要稳态 blocker。accepted 25-turn corrected-2018 evidence显示 turn20-25 `firm_K_total/Ktarget` median约`2.36`，其中 private K median约`0.0029`，GovInv median约`2.358`；overshoot明确由GovInv主导。因此下一科学优先级应回到 GovInv initialization/private-capital reconciliation，而不是把现有不收敛主要归因于劳动。

GovInv redesign specification继续有效：`GovInv0=Ktarget`仅保留为 historical/source-faithful numerical start；residual候选 `GovInv0=max(Ktarget-Kt_supply_initial,0)` 在会计与量纲上成立，但 `Kt_supply_initial` 的观察时点和 At-grid→MU bridge 仍需单独识别。GovInv initialization 与 controller redesign必须拆分，不能从 convergence 或 boundary-hit 表现反推初始化或 controller 参数。

corrected-2018 runtime input-binding repair继续作为唯一活动数据契约：actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、`MU=10万元`、`NU=100 persons`、same-year Zt0；legacy/canonical fallback已隔离。KFE/HJB独立blockers继续存在。

当前没有 active Builder task。下一步需要 Owner/Reviewer 对 initial private-K observation / At→MU bridge 与 GovInv residual initialization 的具体合同作科学冻结后，方可发布下一 implementation 或 bounded diagnostic exact task。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新科学执行必须先发布exact GitHub task；发布task时同一回复自动附Codex启动prompt。
