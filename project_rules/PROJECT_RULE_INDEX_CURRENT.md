# Chapter 5 当前规则入口
更新：2026-09-11；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`C1_RESIDUAL_PUBLIC_ASSET_25TURN_ACCEPTED__CAPITAL_TARGET_HELD__GOVINV_OVERSHOOT_REMOVED__PRICE_NUMERAIRE_RAW_RA_UPPER_PRESSURE_IS_NEXT_DIRECT_NUMERICAL_BLOCKER`。
当前 active Builder task：`tasks/CH5_MP4C_C1_PRICE_NUMERAIRE_RAW_RA_FORENSIC_AND_NORMALIZATION_SPEC.md`。
最新接受候选：`b3183d1aa404922ee179359dc6fa43b411978090`。
Reviewer acceptance：`docs/CH5_MP4C_C1_RESIDUAL_PUBLIC_ASSET_25TURN_CONTEMPORANEOUS_INTEGRATION_DIAGNOSTIC_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

C1 contemporaneous residual-public-asset bounded diagnostic 已接受。独立 successor route 在每个 numerical outer turn 中先由 household outputs 和 At-only capital allocation 得到 current private productive K，再计算 `GovInv=max(Ktarget-Kprivate,0)`，随后进入同 turn firm evaluation；历史 source-faithful one-turn、C0 controller、firm、capital allocation 均保持不变。该 timing 是稳态数值迭代中的 capital-stock decomposition，不解释为真实时间中的政府资产瞬时变化。

25/25 turns、775/775 province updates 完成；C1 accounting assertion 775/775 通过，最大 accounting residual=`1.4901161193847656e-08 MU`。private K 在全部775 rows均低于 Ktarget，residual floor从未绑定。turn20-25 pooled firm total-K/target min/median/max=`1/1/1`，此前 G0/G1+C0 的2–3倍 GovInv-driven capital overshoot 在真实 bounded dynamic path 中消失。因此当前资本数量/GovInv level divergence 不再是同一优先级的直接数值 blocker。

但 firm raw return 压力显著暴露：turn25 raw-ra lower/interior/upper=`0/1/30`，而 accepted G0 与 G1+C0 均为`0/21/10`。C1 pooled `rah`仍靠近历史上界区域，没有变得明显更 interior。KN/Y/GDP 数值路径大幅改善：turn25 max KN gap=`2.0177068904558837e-09`，max Y/Yprev gap=`1.3322676295501878e-15`，max GDP-level gap=`0.007556323724974279`；Zt 只在turn4/6/7调整，turn20-25为0，因此晚期异常不能优先归因于活跃 Zt 调整。

HJB nonconvergence仅集中于早期；turn6起31/31 HJB converged。KFE 775/775 仍为`DIAGNOSTIC_ONLY`，继续作为独立 scientific blocker。beta_a仍为`SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`。已接受 origin-preserving normalized labor successor 本门仍未激活，因此本次资本侧改善不能归因于 labor normalization。

当前 active task 为 zero-science price/numeraire/raw-ra forensic。必须用 accepted C1 saved ledgers 与 source equations 静态分解 `ra0 = rk-delta + profit*(1-corptau)/K`、`rk=mt*alpha/(K/Y)`，恢复 `.02/.09` return bounds 与 `[.8,1.3]` wage bounds 的 provenance，并梳理 firm raw wage、clipped wage、household composite wage、Y/K 与 MU/NU 的 dimensional chain。不得运行新的 HJB/KFE/firm/wage/controller/trajectory，也不得直接修改 bounds、alpha、delta、Zt、Ktarget、beta_a 或 labor normalization。

corrected-2018 runtime input-binding repair继续作为唯一活动数据契约：actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、`MU=10万元`、`NU=100 persons`、same-year Zt0；legacy/canonical fallback已隔离。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新科学执行必须先发布exact GitHub task；发布task时同一回复自动附Codex启动prompt。
