# Chapter 5 当前规则入口
更新：2026-09-11；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`C1_PRICE_NUMERAIRE_RAW_RA_FORENSIC_ACCEPTED__OWNER_FREEZES_NESTED_BILATERAL_CAPITAL_NETWORK_DIRECTION__K1_ZERO_SCIENCE_IMPLEMENTATION_AUTHORIZED`。
当前 active Builder task：`tasks/CH5_MP4C_K1_BILATERAL_CAPITAL_NETWORK_REPAIR_AND_ENDOGENOUS_FOREIGN_SHARE_IMPLEMENTATION.md`。
最新接受候选：`8c0606ebc67e8f51a0a27ff06505ce67bd69ba7d`。
Reviewer acceptance：`docs/CH5_MP4C_C1_PRICE_NUMERAIRE_RAW_RA_FORENSIC_AND_NORMALIZATION_SPEC_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

最新 price/numeraire/raw-ra forensic 已接受：C1 25-turn 下 turn25 raw `ra0` 30/31 高于历史 `.09` safeguard，主来源是 `rk=mt*alpha*Y/K`；return bounds `[.02,.09]` 仍只属 `EMPIRICAL_NUMERICAL_SAFEGUARD`，wage bounds `[.8,1.3]` 仍为 `SOURCE_VALUE_WITH_UNRESOLVED_ECONOMIC_UNIT`。不得据此直接扩大/删除 return clips。KFE仍是独立 scientific blocker。

Owner 随后重新审视 protected MATLAB `HANK_mp_1turn.m` 的 private-capital network，并确认原经济意图为：每省 household illiquid wealth 同时持有本省和外省企业资产，本省权重更高，外省持仓形成 household illiquid return 的组合收益。现 legacy source 可能存在两项结构性遗漏：第一，`Kt_supply` 只统计跨省流入而没有把 `(1-inter_prv_ratio_i)*At_i*N_i` 的本省保留资本加入 destination private K；第二，`rah` 外省收益中再次乘 destination `inter_prv_ratio_j`，与后来“theta 仅表示 origin 对外投资比例、外省平均分配”的简化意图不一致，且 portfolio weights一般不和为1。

Owner 已冻结下一结构方向为 nested Scheme B，而不是增加31个 household asset states：household block 继续保持两资产 `(b,a)`；每个 origin household sector 的 aggregate illiquid wealth `A_i*N_i` 经一个 31x31 destination-by-origin portfolio matrix 分配到全国企业。资本流量与 household `rah` 必须使用同一矩阵，从而保证 origin-column 与全国 private-capital conservation。

当前 K1 gate 先保留现有 `inter_prv_ratio_i = theta_i` 作为 origin 总对外投资比例，只内生化 foreign destination shares；home share 固定为 `1-theta_i`。foreign conditional share engine 允许使用 caller-provided dimensionless distance/friction score 与 old-turn/lagged return-attractiveness score，但本 task 不选择 `beta_distance`、`beta_return` 或其他科学系数，也不运行 trajectory。关键 timing 冻结为 lagged-return update：禁止 same-turn `firm -> return -> share -> K -> firm` circular feedback。未来 K2 才讨论是否把 home-vs-foreign margin `theta_i` 本身内生化。

当前 active task 只做 zero-science implementation + deterministic accounting validation：恢复本省 private capital、实现完整 bilateral capital matrix、统一 quantity/return weights、实现可接受 distance+lagged-return score 的 foreign-share softmax engine，并保留 legacy `allocate_productive_capital` byte-identical。不得连接 active steady-state runtime，不得激活 normalized labor，不得修改 C1 GovInv、price bounds、HJB/KFE 或 beta_a。

C1 residual public-asset authority继续有效：GovInv 是不可直接观测的政府/公共生产性资产 residual，`GovInv=max(Ktarget-Kprivate,0)`；此前 C1 bounded path 已消除 GovInv-driven capital overshoot。新的 private-capital network 若未来改变 Kprivate，必须在后续单独 scientific task 中与 C1 residual public assets 一起重新验证，不能从当前 zero-science implementation 直接外推。

corrected-2018 runtime input-binding repair继续作为唯一活动数据契约：actual 2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、`MU=10万元`、`NU=100 persons`、same-year Zt0；legacy/canonical fallback已隔离。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新科学执行必须先发布exact GitHub task；发布task时同一回复自动附Codex启动prompt。
