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
9. 读取最新相关 acceptance/report；若存在 active task 再读取 exact task。

当前状态：`K1_RAW_RA0_HJB_DRIFT_FORENSIC_ACCEPTED__OWNER_PAYOFF_MAPPING_SCALE_DECISION_REQUIRED`。
当前 active Builder task：NONE。
最新 accepted raw-payoff safety candidate：`678860073d3d5b653b8863b71f494f569960ced7`。
最新 accepted forensic candidate：`cd5abea31cfbfcdb4170970df7e0504b394571d5`。
Reviewer acceptance：`docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_HJB_DRIFT_ZERO_SCIENCE_FORENSIC_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

K1 capital network 已在 corrected-2018 bounded runtime 中真实启用并获得 accepted dynamic evidence；它不是仅离线测试。Owner 已冻结 raw `ra0` 为 intended final K1 household illiquid payoff source object，并冻结 common turn-1 clipped bootstrap。

Raw five-turn safety evidence 已接受 narrow executability，但 treatment HJB convergence 为 Control `49/124`、Raw `12/124`，Raw turn5 `0/31` converged，且出现大幅 finite transfer/cost/drift sensitivity。因此该路径尚不能作为稳定 quantitative solution，也不得进入25-turn Raw或K1B。

Zero-science forensic 已接受：stress 并非 boundary-only；大多数 extreme cells 位于 interior。Raw payoff scale 通过 accepted HJB value derivatives 与 transfer FOC / quadratic adjustment-cost law被放大，同时 upper-a outward regime 扩张。Control 自身也存在显著 baseline extremes，upper-b outward behavior 更强，因此不得把所有异常归因于 Raw。Lower-b exact-sign counts 低于 accepted tolerance，属于 floating-point sign noise；standalone KKT residual仍不可得。

下一步是 Owner scientific decision on payoff mapping / scale interpretation。当前不得由 Builder自行选择 annualization、normalization、cap、clipping、transform、boundary-law、transfer-cost、solver、grid或tolerance変更。K1B `beta_return=.5` 仍仅 preregistered，不授权 runtime；K2不授权；corrected-2018 KFE仍为`DIAGNOSTIC_ONLY`。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复自动附Codex启动prompt。
