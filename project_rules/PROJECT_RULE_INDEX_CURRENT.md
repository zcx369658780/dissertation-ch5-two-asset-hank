# Chapter 5 当前规则入口
更新：2026-09-12；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
6. `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
7. `docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`
8. `docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOOTSTRAP_TIMING_FREEZE_CURRENT.md`
9. `docs/CH5_MP4C_K1_PAYOFF_SCALE_MAPPING_AND_DIAGNOSTIC_BOUND_POLICY_FREEZE_CURRENT.md`
10. `docs/CH5_MP4C_K1_HJB_PAYOFF_SCALE_AUTHORITY_ZERO_SCIENCE_AUDIT_ACCEPTANCE.md`
11. 当前 active exact task 及直接相关 report/evidence。

当前状态：`K1_HJB_PAYOFF_SCALE_AUTHORITY_AUDIT_ACCEPTED__QUARTERLY_HJB_VS_ANNUAL_FIRM_FLOW_PROVENANCE_CLOSURE_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_QUARTERLY_HJB_VS_ANNUAL_FIRM_FLOW_PROVENANCE_CLOSURE.md`。
最新 accepted payoff-scale authority audit candidate：`367de55e60d144042b0a95ad1fd49fbc5267f85f`。
Results eligibility=`FALSE`。

Accepted payoff-scale audit 已确认：corrected-2018 `Y/K` 与 profit/K 在当前数据合同下是 annual flow/stock rate；dissertation Chapter 4 明确将 `delta=.025` 定义为 quarterly depreciation，而 Chapter 5 参数表写 `.0025`、active code仍使用 `.025`。因此 current raw `ra0` 已混合冲突日历尺度，direct numerical identity `HJB r_a = current raw ra0` 不授权 runtime。

Household HJB 是 continuous-time；`rho=.05`、`rb=.02`、`r_a/rah`、`Q_z=1/3`、wage、transfer 与 adjustment-cost flows 尚未获得统一 calendar/model-time authority。旧 MATLAB direct wiring 仅为 provenance，不构成 dimensional authority。

Owner 仍保留 raw `ra0` 为经济 payoff source object。不得由 Builder 自行选择 `/4`、compounding/log conversion、normalization、shrinkage、smoothing 或新 structural cap。历史 `[.02,.09]` 与 `[.8,1.3]` 继续属于 safeguard/未闭合对象，而不是自动有效 structural calibration。

当前 zero-science task 要解决 Chapter-4/Chapter-5/code depreciation conflict，并建立 `rho/rb/r_a/Q_z/Y/K/wage/transfer/adjustment-cost` 的统一 provenance tree 与候选 calendar convention。若 source 无法唯一决定，必须停止在 precise Owner calibration decision，不得为了下一次 runtime 发明 conversion。

Owner debugging-bound policy 继续有效：未来 exact debugging task 可预先登记 `ra/rah`、`wjt/wage` 等 hard guards 作为 temporary numerical diagnostic scaffolding，并记录 hit/saturation counts、使用 preregistered relaxation ladder；当前 task 不激活任何新 bound。

K1B `beta_return=.5` 仍仅 preregistered，不授权 runtime；K2不授权。corrected-2018 finite-box upper-b leakage/MATLAB-style pinning 继续是独立 KFE blocker，KFE=`DIAGNOSTIC_ONLY`。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复自动附Codex启动prompt。
