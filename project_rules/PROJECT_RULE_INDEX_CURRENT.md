# Chapter 5 当前规则入口
更新：2026-09-11；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`GOVINV_CONTROLLER_REDESIGN_SPEC_ACCEPTED__C0_FAILURE_MECHANISM_QUANTIFIED__OWNER_IDENTIFIES_GOVINV_AS_GOVERNMENT_ASSET_RESIDUAL__C1_LEVEL_REPLACEMENT_IMPLEMENTATION_AUTHORIZED`。
当前 active Builder task：`tasks/CH5_MP4C_C1_GOVINV_RESIDUAL_LEVEL_REPLACEMENT_IMPLEMENTATION.md`。
最新接受候选：`ac71e396cd64ecd1e7d6b6497981042800d8411e`。
Reviewer acceptance：`docs/CH5_MP4C_GOVINV_CONTROLLER_REDESIGN_FORENSIC_AND_SPEC_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

最新 controller forensic/spec 已接受。历史 C0 clipped-return controller 在 accepted G1 775 条 province-turn ledger 上静态 replay 为 0 mismatch；258/775（33.290323%）在 contemporaneous K-level gap 意义上方向恶化，全部为 total K 已高于 Ktarget 时仍触发 `GovInv *= 1.1`。C0 明确是 return-bound controller，不含 Ktarget、total-K residual 或 private-K residual。

Owner 进一步冻结 GovInv 的经济含义：GovInv 代表政府/公共生产性资产。原因是经验估计得到的总生产资本 Kt 与 household/private illiquid asset At 之间存在显著缺口，而省级政府生产性资产额度难以直接获得，因此历史 MATLAB 将 GovInv 作为内生变量，通过 return-bound heuristic 经验调整。GovInv 不能再解释为任意 numerical balancing stock，而应解释为“不可直接观测的政府/公共生产性资产 residual”。

因此下一最低风险控制对象被冻结为 C1 direct level replacement，而不是选择一个需要调参的 gain：
`GovInv_next = max(Ktarget - Kprivate_current, 0)`。
它在代数上等价于 generic C1 的 `lambda_K=1` one-step replacement，但本项目不把 1 解释为估计/校准 gain；它是 Owner 经济解释下的直接 residual public-asset definition。若 private K 已高于 Ktarget，则 GovInv floor 到0并显式保留 private overshoot，不允许隐藏。

当前 active task 只实现这一 C1 residual-government-asset pure function/API，并对 accepted G1 ledger 做 zero-science static replay。不得运行 HJB/KFE/firm/migration/wage/controller runtime/trajectory/steady state；不得改历史 C0；不得引入 lambda_K、ra_target、damping、hysteresis 或 staged controller。通过后才可由新的 exact task 授权一条 bounded scientific trajectory。

此前 G1 isolated diagnostic 继续作为 accepted scientific FAIL evidence：G1 initialization 31/31 对齐 initial Ktarget，但 unchanged C0 25 turns 后重新把 median total-K/target 推至约2.353，late overshoot 几乎全部来自 GovInv。HJB/KFE blockers仍独立存在，beta_a仍为 `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`。

已接受 origin-preserving normalized labor successor 继续保留但本资本侧任务不激活。corrected-2018 runtime input-binding repair继续作为唯一活动数据契约：actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、`MU=10万元`、`NU=100 persons`、same-year Zt0；legacy/canonical fallback已隔离。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新科学执行必须先发布exact GitHub task；发布task时同一回复自动附Codex启动prompt。
