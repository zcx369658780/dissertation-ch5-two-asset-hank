# Chapter 5 当前规则入口
更新：2026-09-10；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`GOVINV_LABOR_REDESIGN_SPEC_ACCEPTED__OWNER_FROZE_ORIGIN_PRESERVING_BILATERAL_LABOR_NORMALIZATION__IMPLEMENTATION_ONLY_AUTHORIZED`。
当前 active Builder task：`tasks/CH5_MP4C_ORIGIN_PRESERVING_BILATERAL_LABOR_NORMALIZATION_IMPLEMENTATION.md`。
最新接受候选：`afb1cffeba207368b78c8ac4b93958285312eb53`。
Reviewer acceptance：`docs/CH5_MP4C_GOVINV_INITIALIZATION_AND_LABOR_NORMALIZATION_REDESIGN_SPEC_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

最新zero-science redesign specification已接受。资本侧：`GovInv0=Ktarget`仅保留为historical/source-faithful数值起点，不再解释为已识别公共资本；residual候选`GovInv0=max(Ktarget-Kt_supply_initial,0)`在会计/量纲上成立，但`Kt_supply_initial`的观察时点与At-grid→MU bridge尚未识别。GovInv initialization与controller redesign必须拆分，不从收敛表现反推初始化或controller参数。

Owner随后冻结劳动修正方向：必须保留完整`destination x origin`双边劳动矩阵，不能压缩成全国destination shares。每个origin省先由household block给出per-household/efficiency labor，再乘该省人口一次形成`L_origin_i`；现有`Lt_seperate` destination-attractiveness kernel生成`q[j,i]`后，必须按origin列归一化`s[j,i]=q[j,i]/sum_j q[j,i]`；双边流量`M[j,i]=s[j,i]*L_origin_i`。因此每个origin列必须守恒到该省household aggregate labor，destination firm labor为行和，全国destination labor总量必须等于全国origin household labor总量。省级origin labor与destination firm labor可以不同，差额由完整province-to-province matrix精确溯源。

当前active task仅实现这一origin-preserving bilateral normalization contract及零科学测试。现有literal/source-faithful `reconstruct_migration_labor`和`run_source_faithful_one_turn`必须保留不变用于MATLAB parity；normalized successor必须采用显式不同API/route。当前不修改`wage_caculate`/composite wage，不修改GovInv、capital allocation、asset bridge、HJB/KFE、price bounds、controller、damping或其他经济参数，也不运行任何scientific trajectory。完整矩阵和normalized shares必须保留，以便后续单独任务验证origin-specific household wage attribution。

Owner同时强调当前稳态主要问题预计仍更直接来自GovInv而非劳动。accepted 25-turn evidence显示turn20-25 `firm_K_total/Ktarget` median约`2.36`，private K median约`0.0029`，GovInv median约`2.358`；因此劳动归一化implementation完成并验收后，下一科学优先级仍应回到GovInv initialization，而不是把不收敛主要归因于labor。

corrected-2018 runtime input-binding repair继续作为唯一活动数据契约：actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、`MU=10万元`、`NU=100 persons`、same-year Zt0；legacy/canonical fallback已隔离。KFE/HJB独立blockers继续存在。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新科学执行必须先发布exact GitHub task；发布task时同一回复自动附Codex启动prompt。
