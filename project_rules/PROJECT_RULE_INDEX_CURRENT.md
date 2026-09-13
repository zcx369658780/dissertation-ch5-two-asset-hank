# Chapter 5 当前规则入口
更新：2026-09-13；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. accepted bilateral-capital / scoring-data / payoff / annual-HJB / price-guard authority docs
6. `docs/CH5_MP4C_K1_TRANSFER_CONTROL_RAW_CANDIDATE_CENSUS_INSTRUMENTED_BOUNDED_DIAGNOSTIC_ACCEPTANCE.md`
7. `docs/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_ADMISSIBILITY_FREEZE_CURRENT.md`
8. 当前 active exact task 及直接相关 report/evidence。

当前状态：`K1_TRANSFER_RAW_CANDIDATE_CENSUS_ACCEPTED__OWNER_D1_1E5_FROZEN__D1_BOUNDED_RUNTIME_DIAGNOSTIC_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC.md`。
最新 accepted raw-census candidate：`e6c71240e945c988958a16c67886b056376a2da4`。
Results eligibility=`FALSE`。

Owner D1 contract：symmetric `[-1e5,+1e5]`，inclusive `abs(d_raw)<=1e5`；语义=`C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION`。Raw FOC receipt必须保留，禁止clipping，existing zero-transfer option与其他admissible branches继续按accepted selector law工作。

当前 exact task 比较 fresh G2 control 与 G2+D1。Turn1相同且D1 OFF；turn2起仅treatment启用D1。`chi0/chi1`、derivative floor、transfer FOC、annual calibration、return/wage guards、HJB/KFE equations、boundary/KKT、grid/tolerance/solver、K1/C1/labor science均冻结。不得自动进入D2/D3/OFF、G3/G4、wage relaxation、K1B/K2或Results。KFE=`DIAGNOSTIC_ONLY`。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复必须附Codex启动prompt。
