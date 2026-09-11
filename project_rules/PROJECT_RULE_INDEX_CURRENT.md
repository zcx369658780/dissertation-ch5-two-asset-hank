# Chapter 5 当前规则入口
更新：2026-09-11；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`G1_RESIDUAL_GOVINV_25TURN_FAIL_ACCEPTED__INITIAL_ALIGNMENT_VALID__UNCHANGED_RETURN_BOUND_CONTROLLER_RECREATES_GOVINV_OVERSHOOT__CONTROLLER_REDESIGN_SPEC_AUTHORIZED`。
当前 active Builder task：`tasks/CH5_MP4C_GOVINV_CONTROLLER_REDESIGN_FORENSIC_AND_SPEC.md`。
最新接受候选：`54b6736b0507bee44f433832415507c0bfb170fa`。
Reviewer acceptance：`docs/CH5_MP4C_G1_RESIDUAL_GOVINV_INITIALIZATION_INTEGRATION_AND_25TURN_ISOLATED_DIAGNOSTIC_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

最新 G1 isolated diagnostic 已接受为 scientific FAIL evidence，而不是 implementation rejection。G1 在 `beta_a=1` diagnostic bridge 下 31/31 将 initial accounting firm K 精确对齐 Track-A target，turn1 median total-K/target=`1.0`，成功消除 G0 的 `Ktarget+private K` 初始重复叠加；但 unchanged historical GovInv controller 随后重建 overshoot。25 turns controller decrease/increase/hold=`0/289/486`，与 accepted G0 totals 完全相同。

G1 turns20-25 pooled `firm_K_total/Ktarget` min/median/max=`1.3257022041568054/2.353363495591088/2.8512142917573127`；median `GovInv/Ktarget=2.3503561274071445`，median `private_K/Ktarget=0.0029186382400614363`。因此 late capital overshoot 仍由 GovInv 主导。selected turns 的 raw-ra lower/interior/upper counts 与 G0 逐轮相同，支持历史 clipped-return controller 在 G1 后仍基本执行同一方向的反馈序列。

本次 accepted FAIL 说明：residual G1 initialization 本身是有效的 accounting correction，但初始化修复不足以解决资本侧稳定性；当前主要剩余机制转为 GovInv controller objective/signal/timing。HJB/KFE blockers仍独立存在，beta_a仍为 `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`；不得把 bounded path 当 production validity。

当前 active task 为 zero-science GovInv controller forensic/spec。必须恢复历史 `maxKNratiogap` gate、Zt/GovInv/tKNratio timing、clipped-ra ±10% 反馈及其与 Ktarget gap 的关系，并比较至少：C0 historical return-bound controller、C1 capital-target residual controller、C2 return-target controller、C3 staged/hybrid controller。允许只读 accepted ledgers 和 deterministic static replay，不允许 HJB/KFE/firm/controller runtime/trajectory/steady-state/Results 调用，也不得自动选择 gain、damping、hysteresis 或 production winner。

Owner 的历史背景继续有效：旧 `HANK_mp_1eq.m` 的 GovInv ±10% 调整是无法直接观测复杂网络省级投资额时的经验逼近；其他状态不稳定时可能放大 Kt 发散。当前任务必须把 initialization 与 controller 继续分离，并明确哪些 controller objective/signal/damping 选择需要 Owner 决策。

已接受 origin-preserving normalized labor successor 继续保留但不改变当前资本侧结论。corrected-2018 runtime input-binding repair继续作为唯一活动数据契约：actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、`MU=10万元`、`NU=100 persons`、same-year Zt0；legacy/canonical fallback已隔离。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新科学执行必须先发布exact GitHub task；发布task时同一回复自动附Codex启动prompt。
