# Chapter 5 两资产 HANK 当前状态
更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`K1_TRANSFER_RAW_CANDIDATE_CENSUS_ACCEPTED__OWNER_D1_1E5_FROZEN__D1_BOUNDED_RUNTIME_DIAGNOSTIC_ACTIVE`。

最新 accepted raw-census candidate：`e6c71240e945c988958a16c67886b056376a2da4`。
Owner D1 freeze：`docs/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_ADMISSIBILITY_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC.md`。
Results eligibility=`FALSE`。

Owner 已冻结 D1：symmetric `[-1e5,+1e5]`，`abs(d_raw)<=1e5` admissible；超界 raw branch 按 `C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION` 排除，raw FOC receipt 保留，禁止 clipping。D1 仅为 temporary numerical continuation safeguard。

当前任务比较 fresh G2 control 与 G2+D1 treatment。Turn1 两路径完全相同且 D1 OFF；turn2 起仅 treatment 激活 D1，因此 turn2 是 common-entering-state immediate-response 窗口；turns3-5 仅作 path-history propagation。两路径均保持 G2 `r_a in [-.10,.35]` 和 `wjt in [.8,1.3]`。

`chi0=.1`、`chi1=2 years`、derivative floor、transfer FOC、annual calibration、price guards、HJB/KFE equations、boundary/KKT、grid/tolerance/solver、K1/C1、source-faithful labor全部冻结。D2/D3/OFF、G3/G4、wage relaxation、K1B/K2、Results均未授权。KFE=`DIAGNOSTIC_ONLY`。
