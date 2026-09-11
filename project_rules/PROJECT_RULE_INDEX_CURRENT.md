# Chapter 5 当前规则入口
更新：2026-09-11；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`K1_BILATERAL_CAPITAL_NETWORK_ACCEPTED__HOME_CAPITAL_RESTORED__PORTFOLIO_AND_CAPITAL_CONSERVATION_ENFORCED__LAGGED_ENDOGENOUS_FOREIGN_SHARE_ENGINE_READY_FOR_PARAMETER_FREEZE`。
当前 active Builder task：无。
最新接受候选：`742ae11dbb057c7d33650ed4bc8d4db59b90d435`。
Reviewer acceptance：`docs/CH5_MP4C_K1_BILATERAL_CAPITAL_NETWORK_REPAIR_AND_ENDOGENOUS_FOREIGN_SHARE_IMPLEMENTATION_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

最新 K1 zero-science implementation 已接受。新模块`src/ch5_two_asset_hank/multi_province/capital_network.py`采用完整`destination x origin`资本组合矩阵`S`，恢复`(1-theta_i)*A_i*N_i`本省retained private capital；同一`S`同时用于private-capital quantities与household `rah`，从而保证origin-column portfolio weights、origin wealth、national private capital conservation。legacy `capital_allocation.py`保持byte-identical用于source-faithful parity。

K1当前只内生化foreign destination shares，不内生化`theta_i=inter_prv_ratio_i`。foreign conditional shares由显式caller-provided distance/friction score与lagged/completed-iteration return-attractiveness score经stable foreign-only softmax产生；`beta_distance`、`beta_return`均无默认值，未选择科学系数。allocation iteration n+1只允许使用completed iteration n的lagged return score，禁止same-turn `firm -> return -> share -> capital -> firm`循环。

接受的K1 equal-foreign-share special case（`beta_distance=beta_return=0`）复现Owner原意：固定origin总对外投资比例，外省均匀分配，但修复两项legacy结构遗漏：本省retained capital不再丢失，`rah`外省收益不再二次乘destination `theta_j`。非对称fixture全国private K从legacy 130修复到200并与origin wealth 200守恒；legacy `rah` implied weight sums `[.93,.75,.48]`修复为`[1,1,1]`。

K1尚未连接one-turn/C1/steady-state/trajectory。下一scientific gate前必须由Owner/Reviewer冻结：distance/friction数据映射与归一化、lagged-return score来源与归一化、`beta_distance`、`beta_return`、是否需要portfolio smoothing/partial adjustment、portfolio payoff使用`ra0`/clipped `ra`/normalized return/expected return，以及何时才进入K2 endogenize `theta_i`。

C1 residual public-asset authority继续有效：GovInv解释为不可直接观测的政府/公共生产性资产 residual，`GovInv=max(Ktarget-Kprivate,0)`；此前C1 25-turn bounded path已消除GovInv-driven capital overshoot。但新K1会改变`Kprivate`，因此未来集成必须重新验证C1 residual public assets，不能直接沿用旧private-K量级结论。

price/numeraire/raw-ra forensic继续有效：C1旧路径下turn25 30/31 raw `ra0`高于历史`.09` safeguard，主来源是`rk=mt*alpha*Y/K`；return bounds `[.02,.09]`仍只属`EMPIRICAL_NUMERICAL_SAFEGUARD`，wage bounds `[.8,1.3]`仍为`SOURCE_VALUE_WITH_UNRESOLVED_ECONOMIC_UNIT`。K1修复可能显著改变private-K与Y/K，因此在K1 scientific integration前后需重新评估return pressure，不应现在直接改bounds。

KFE治理必须继续区分：clean/source-free generator-KFE合同已有稳定验证；但当前corrected-2018 empirical finite-box upper-b leakage/pinning仍是独立 scientific blocker，不因资本网络修复自动解决。

corrected-2018 runtime input-binding repair继续作为活动数据契约：actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、`MU=10万元`、`NU=100 persons`、same-year Zt0；legacy/canonical fallback已隔离。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新科学执行必须先发布exact GitHub task；发布task时同一回复自动附Codex启动prompt。
