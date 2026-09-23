# K1B 完整外层状态映射：零科学设计候选

Task `CH5_FULL_OUTER_STATE_MAP_ZERO_SCIENCE_DESIGN_20260923`；派发 HEAD `ca00a602ffbcb65da1e4a5cfc2038f5b16c9f686`，父提交 `724b53c0507de34ebd9a2c3eabc8d5f6a8885aad`，生产 `src` 树 `00682b2e1a7ba23665f6e16f6acf48ad35874883`。本文所有检查点、范数和规则均为 **`PROPOSED_NOT_ADOPTED`**；没有科学调用、外层收敛律、turn7 执行权或 Results 许可。Owner 已选择“完整外层状态”作为设计范围，含义仅限当前实际执行的 K1B 有界回合，不含 GE。

## 引用定位及证据边界

下表的短名均指此工作树中的精确路径。静态引用只证明当前有界路线的读写行为；封存 turn3–turn6 仅证明已执行的描述性轨迹。

| 短名 | 路径及关键行/证据 |
|---|---|
| R | `validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py`：88–125、215–224、227–400、428–481、630–676 |
| H | `src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py`：285–330、638–680、780–813、857–873 |
| I | `validators/multi_province/corrected_2018_single_turn/run.py`：153–177（source-native 初始化） |
| L | `src/ch5_two_asset_hank/multi_province/migration_labor.py`：36–73、76–130 |
| F | `src/ch5_two_asset_hank/multi_province/firm.py`：20–40、44–141 |
| W | `src/ch5_two_asset_hank/multi_province/wage.py`：11–75 |
| M | `src/ch5_two_asset_hank/multi_province/monetary.py`：10–25；`src/ch5_two_asset_hank/multi_province/fiscal_diagnostics.py`：11–43 |
| P | `src/ch5_two_asset_hank/multi_province/province_contracts.py`：10–30；`src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py`：21–30、177–213 |
| S | `src/ch5_two_asset_hank/multi_province/capital_network.py`：16–21、133–164、275–342；`validators/multi_province/k1b_turn3_lagged_raw_ra0_activation_safety_gate/run.py`：114–141 |
| E | `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/turn3_through_turn6_trajectory_diagnostic.json`、`turn7_entering_bundle_manifest.json`、`turn7_entering_bundle_readback.json`、`turn7_k1b_input_candidate.json`、`turn7_k1b_frozen_share_payoff_plan.npz`（同一证据根）；`docs/CH5_K1B_CONVERGENCE_DESIGN_EVIDENCE_DOSSIER_20260923.md` 及其独立审查 |

`P` 固定 31 省顺序。向量均沿此顺序；矩阵的行是目的地、列是来源。资本/产出的源声明单位是 MU（万单位元），人口源声明单位 NU（百人）；对 `Ct`、`w`、`wjt`、`Lt`、`Lt_supply`、`At`、`Bt`、`AtTax` 等是否同量纲及可用尺度，当前证据不足，均留 `UNRESOLVED`。`raw ra0` 是一个模型期的原始净生产资本回报，不裁剪、年化或标准化；`S` 是无量纲列归一份额。数值字段大小写敏感：`It` 是企业投资、`it` 是货币名义利率、`PIt` 是企业利润、`pit` 是通胀输入，四者不能合并（R:307–319、363–371；F:75、104–110、136–139；M）。

## 实际完整回合顺序

1. 读取 31 行 `rows[*].state`，并从配套计划读取 `portfolio_shares_destination_origin`、`rah_turn{n}_by_origin`、`raw_ra0_turn{n-1}`；核对行序、哈希、列和及 state `rah`（R:88–125、428–451）。文件只是绑定输入。turn7 manifest 标为 `COMPLETED_TURN6_RAW_RA0_ONLY` 且 `sealed_before_household=true`；readback `PASS`、科学调用 0。没有 turn7 household。
2. 用进入状态的 `rah, rb, rb_gap, tau, w, Tt`，固定 20×20×2 F-order 网格和 source-native 初始化，按每省 HJB/KFE 门得到 `Ct, Lt, At, Bt, AtTax`；31/31 后才形成家庭批次（I:153–177；H:285–330、638–680、780–813；R:215–224、454–479）。上一回合价值/政策/分布不作为 warm start。
3. 旧企业 `Yt/Lt` 与冻结距离构成 `phi[d,o]` 和 wedge；本回合 `Ct`、旧 `wjt`、冻结 `N,tau` 经来源忠实劳动重建给出 `Lt_supply`（H:857–873；L:36–73、98–130；R:232–244）。此处旧 `Lt` 是进入记录的**企业** `Lt`，不是本回合家庭 `Lt`。
4. 固定进入矩阵 `S_n[d,o]`，用本回合家庭 `At_o` 与冻结人口 `N_o` 得出来源财富、双边流和目的地私人资本 `Kt_supply`；不以本回合企业回报重算 `S_n`。C1 随后用冻结目标 `Kt0` 与当前私人资本构造 `GovInv=max(Kt0-Kt_supply,0)`（R:246–287；`SCIENTIFIC_DECISIONS.md` 的 C1/K1B 行）。
5. 每省企业以当前 `Kt_supply,Lt_supply,GovInv,AtTax`，进入记录的 `alpha,Zt,pit,Kt_prev,Zt_1,pit_1,rk,corptau,tau,Tt,ramin,ramax,wjtmin,wjtmax` 和本回合家庭 `Lt` 求值。关键顺序是 `source.update(..., Lt_prev=household.household_lt)` **覆盖进入记录的 `Lt_prev`**；不能把进入记录的 `Lt_prev` 误当该次企业求解的有效输入（R:289–299；F:56–139）。得到企业 `Kt,Lt,Yt,wjt,rk,ra0,ra,It,PIt` 等。
6. 新企业工资经 `phi,wedge,tau` 产生下一家庭 `w`；冻结 Taylor 参数给出 `it,rb`；本回合 `Bt` 与企业 `Govinc` 仅进入财政诊断（R:302–320；W:11–75；M）。完成回合 n 的原始 `ra0_n` 再以总体 z-score（`ddof=0`）构造下一回合外国吸引力、`S_{n+1}[d,o]` 与 `rah_{n+1,o}=sum_d S_{n+1}[d,o] raw_ra0_{n,d}`；原始水平仅用于 payoff（R:322–359；S）。
7. 候选 `state` 先复制旧记录，再更新本回合家庭/劳动/资本、`rah_{n+1},w,it,rb`、滞后字段，最后以企业结果覆盖同名字段，封存下一回合 JSON/NPZ/manifest。`Yt_1` 存旧 `Yt`，`Kt_prev` 存本回合企业 `Kt`，`Lt_prev` 存本回合企业 `Lt`，`Zt_1`/`pit_1` 存旧 `Zt`/`pit`；`firm` 的 `Kt,Lt,Yt,ra0` 覆盖前述旧值（R:361–422）。`Yt_1` 和记录中的 `Lt_prev` 在当前下一回合经济计算中没有独立读取；这仅是当前有界路线的静态发现。

## 输入逐字段映射与分类

所有行的维度均为 31 省向量，除显式 31×31 矩阵或标量。表中“冻结”表示该有界路线从进入记录沿用/从冻结文件读取，不宣称一般模型中恒定；精确经济单位未获源支持时记 `UNRESOLVED`。写者列描述检查点 `C_n` 的产生方式，消费者指 **turn n+1** 的实际读取；完整的 51 个候选记录 key 分类也列于 JSON receipt。

| 精确 key（单位） | 分类；C_n 写者/来源 | 下一回合消费者与检查点 |
|---|---|---|
| `state.w`, `state.rah`（工资单位 `UNRESOLVED`；回报/期） | 跨回合动态；W 给 `w_n`，完成 `ra0_n` 经下一计划给 `rah_{n+1}`（R:322–370） | 家庭初始化、HJB 与聚合（I:160–171；H:291–297、794–806） |
| `state.Yt`, `state.Lt`（MU；劳动单位 `UNRESOLVED`） | 跨回合动态；本回合企业 `FirmResult.Yt,Lt` 最后覆盖 `state`（R:371；F:136–139） | H:862–867 的旧 `Yt/Lt` 生产率构造 `phi`；`Lt` 此时为旧**企业**劳动 |
| `state.wjt`（`UNRESOLVED`） | 跨回合动态；本回合企业工资结果（F:126–139；R:371） | L:109–115 的旧目的地企业工资 |
| `state.rk`, `state.Kt_prev`（每期回报；MU） | 跨回合动态；本回合企业 `rk,Kt`，其中 `Kt_prev := firm.Kt`（R:368、371） | F:76、80、90–105 的上期资本/收益输入 |
| `state.ra0` 与行顶层 `raw_ra0_turn{n}`（回报/期） | 跨回合动态的完成回合 payoff；本回合企业 `ra0`（R:312–319、371–380；F:110） | 下一计划的 z-score、外国份额与 payoff（R:322–350）；`state.ra0` 本身不直接进下回合家庭 |
| NPZ `portfolio_shares_destination_origin`、`rah_turn{n+1}_by_origin`（无量纲 31×31；回报/期 31） | 上项及冻结 `theta,distance` 的可重建下一输入；准备后封存，分别记 `S_{n+1},rah_{n+1}`（R:322–350） | 读取计划并绑定 state `rah`；`S_{n+1}` 用于本次资本分配（R:428–451、246–253） |
| `state.rb`, `state.it`（利率/期） | 货币参数可重建；`rb,it := taylor_assignment(frozen params)`（R:306–308、367；M） | `rb` 被家庭读取；`it` 在当前路线无下回合经济消费者 |
| `state.rb_gap`, `state.tau`, `state.Tt`（利差/期、税率、转移单位 `UNRESOLVED`） | 冻结进入记录，来源 P:184–192；R:363 复制 | `rb_gap,tau,Tt` 进家庭；`tau` 进劳动、工资和企业；`Tt` 进企业（I:162–171；H:291–297；L:109–115；W:42–61；F:82–84） |
| `state.N`, `state.inter_prv_ratio`, `state.Kt0`（NU、无量纲、MU） | 冻结进入记录，来源 P:179–183；R:363 复制 | N 进劳动、私人财富、财政；比率作来源固定外国份额；Kt0 进 C1（R:235–278、310、330–332） |
| `state.alpha`, `state.Zt`, `state.pit`, `state.corptau`（弹性、生产率、通胀率、税率；生产率精确单位 `UNRESOLVED`） | 冻结进入记录，来源 P:179–192；R:363 复制 | 企业 F:65–110 |
| `state.Zt_1`, `state.pit_1`（分别同 `Zt,pit`） | 记录中的滞后字段；R:369 在 C_n 写旧 `Zt,pit`，当前路线通常仍等于冻结水平 | 企业 F:78–99；必须保留实际字段而非默认为一般经济恒等 |
| `state.ramin`, `state.ramax`, `state.wjtmin`, `state.wjtmax`（回报/期；工资单位 `UNRESOLVED`） | 冻结企业边界，来源 P:191–192；R:363 复制 | 企业 F:112–132；`raw ra0` 仍取裁剪前值 |
| `state.name`（省标签） | 冻结 31 省顺序，P:10–30 | 候选读取和 OneTurnInputs 顺序校验（R:88–99；`one_turn.py`:107–117） |
| `state.AtTax`（`UNRESOLVED`） | 本回合家庭终端输出，R:215–224、364 | 下回合旧值先复制，但企业前被**下回合**家庭 `AtTax` 覆写（R:292–295；F:82）；非独立跨回合状态 |
| 本回合家庭 `Ct,Lt,At,Bt`（单位 `UNRESOLVED`） | Household terminal output，H:780–813；R:215–224 | 同回合劳动/企业 `Lt_prev`/资本/财政（R:235–253、292–311）；旧 `state.Ct,At,Bt` 不被下回合相应模块读取 |
| `state.Lt_prev`（劳动单位 `UNRESOLVED`） | C_n 写本回合企业 `Lt`（R:369）；数值可与 `state.Lt` 重合 | 下回合企业前被新家庭 `Lt` 覆写（R:292–295）；非独立跨回合输入 |
| `state.GovInv`, `state.Kt_supply`, `state.Lt_supply`（MU；劳动单位 `UNRESOLVED`） | 本回合可重建/报告量，R:246–287、365–370 | 下一回合旧值复制，但资本、劳动、C1 都重新计算；企业消费新值（R:235–295） |
| 距离 `normalized_distance_destination_origin.csv`、`phi[d,o]`、wedge（31×31） | 距离为冻结外部文件；`phi` 由旧 `Yt/Lt` 与固定公式重建，wedge=`0.5*distance`（H:862–873） | 劳动与工资（R:238–239、303–305）；下回合候选文件自身不包含距离矩阵 |
| 固定网格/参数 `ga,phi_l,alphal,epsilon,theta,delta,istar,rho_pi,totalpit,epsilon_pi` 及家庭参数 | 冻结代码常数和任务绑定，H:298–330、868–873；R:462–465 | 家庭、劳动、企业、工资、货币；不是回合变化量，代码/输入身份必须另行冻结 |

企业其他结果 `Kt,ra,wt0,KNratio,Thetat,It,PIt,Corptax,Govinc,mt` 的实际下回合经济消费者按 R/H/F/L/W/M 的当前路径为无；其中 `Kt` 是 `Kt_prev` 的来源，`ra0` 是下一 payoff 来源，`Yt,Lt,wjt,rk` 已列动态。`state.Yt_1`、`state.GovSurplus`、`state.convergent`、`state.ra`、`state.It`、`state.PIt`、`state.it` 不能因存在于序列化记录就自动升格为闭合状态。`GovSurplus` 是诊断量；`It`/`PIt` 与 `it`/`pit` 保持大小写区分。

## 同阶段检查点与候选映射

**`PROPOSED_NOT_ADOPTED`** 定义 `C_n`：turn n 的 31/31 家庭 HJB/KFE 合法门、恰好一次劳动/冻结份额资本/C1/企业/工资/货币/财政集成全部完成；`raw ra0_n` 已写出；`S_{n+1}`、`rah_{n+1}` 和下一候选 JSON/NPZ 已由 raw 值封存并静态 readback。仅有下一束而未运行 household（如现有 turn7）仍可作为 **C6 的准备端**，绝不是 C7。`C_n` 与 `C_{n+1}` 只比较各自同阶段字段，不把完成 n 的 `raw ra0` 与进入 n 的 `rah` 错配（R:630–676；E 的 turn7 manifest/readback）。

候选数值 carrier `x_n`（**`PROPOSED_NOT_ADOPTED`**）包含八个 31 省向量 `Yt_n,Lt_n,wjt_n,rk_n,Kt_prev_n,w_n,raw_ra0_n,rah_{n+1}`，以及一个 31×31 的 `S_{n+1}`。这是保守的充分状态表示：`raw_ra0_n` 与 `S_{n+1},rah_{n+1}` 冗余，必须核对同源映射；`Kt_prev_n=Kt_n` 也有可验证恒等，但保留实际消费字段。冻结 `theta_frozen` 应身份绑定：31 省顺序、距离文件、`N,Kt0,inter_prv_ratio,alpha,Zt,pit,corptau,tau,Tt,rb_gap,ramin,ramax,wjtmin,wjtmax`、`Zt_1,pit_1` 的当前固定路径、家庭网格/参数、企业/货币参数和源版本。`rb` 在当前路线可由 Taylor 常数重建，进入 `rb` 必须与重建值一致。`name` 是轴身份。`Lt_prev` 的实际消费已被当前家庭 `Lt` 覆写，不进最小闭合 carrier。

只有在封存输入身份有效、所有源函数确定、无隐藏 warm start/缓存且每次从同一类 `C_n` 开始时，才可把有界经济数值步骤写成候选 `x_{n+1}=F(x_n;theta_frozen)`。目前运行器还依赖进入 JSON/NPZ 的文件身份与哈希、固定距离 CSV、任务绑定文件和生产源码哈希；这些是**执行闭合/复现条件**，不是可忽略的纯内存映射细节（H:315–324；R:102–125、428–451、459–469）。若未来诊断需要不依赖文件身份的纯数值映射，具体状态重建器、序列化与 bitwise 等价证明仍 `UNRESOLVED`。这不是当前封存路径的矛盾，只是拟议 F 的实现门。

价值函数、政策和 KFE 分布在此 source-native、每回合重解的路径中是确定性**内层输出及合法性检查**，不是跨回合 warm-start 状态（H:638–680、780–813）。若 Owner 要将其范数纳入外层停止判据，需另外定义同网格、同序、概率质量的比较与接受含义；现有轨迹 JSON 没有相邻完整数组范数，应标 `UNAVAILABLE`，不能视为稳定。

## 分量诊断候选与 Owner 决策

以下全部为 **`PROPOSED_NOT_ADOPTED`**。对 carrier 八个向量和一个矩阵，候选逐分量记录 `max_abs_delta`：向量取 31 省 `max_i |x_{n+1,i}-x_{n,i}|`，份额矩阵取 31×31 `max_{d,o}|S_{n+2}[d,o]-S_{n+1}[d,o]|`；另记录 L2/Frobenius 以审计，不能拿后者替代未选定判据。`S` 无量纲且自然幅度不超过 1；其他分量的源单位/跨分量尺度不足以支持共同绝对阈值。候选归一式为 `max_abs_delta_j / scale_j`，其中正 `scale_j` 必须经 Owner 逐分量指定或采纳有经济意义的冻结基准；零/近零基准使用独立的、同量纲绝对容差，而不是除零、机器 epsilon 自动阈值或任意 `1`。`scale_j`、绝对/相对容差全部 `UNRESOLVED`，本文不给数值。动态合法性恒等（S 列和、raw→z-score→S/rah、C1、资本守恒、31/31 household）独立于距离阈值继续检查。候选总规则是 **每个必需动态分量同时达标且全部合法性门通过**，不允许一个大分量被均值抵消。

| 必需动态分量（C_n→C_{n+1} 同阶段） | 候选主范数；辅助审计 | 正尺度、零处理与数值容差 |
|---|---|---|
| `Yt_n` | 31 省最大绝对差；L2 | MU；经济尺度 `UNRESOLVED`，零附近用同 MU 绝对门，阈值 `UNRESOLVED` |
| `Lt_n` | 31 省最大绝对差；L2 | 劳动单位/尺度 `UNRESOLVED`，零附近绝对门 `UNRESOLVED` |
| `wjt_n` | 31 省最大绝对差；L2 | 工资单位/尺度 `UNRESOLVED`，零附近绝对门 `UNRESOLVED` |
| `rk_n` | 31 省最大绝对差；L2 | 模型期回报尺度 `UNRESOLVED`，零附近同回报单位绝对门 `UNRESOLVED` |
| `Kt_prev_n` | 31 省最大绝对差；L2 | MU；经济尺度 `UNRESOLVED`，零附近同 MU 绝对门 `UNRESOLVED` |
| `w_n` | 31 省最大绝对差；L2 | 复合工资单位/尺度 `UNRESOLVED`，零附近绝对门 `UNRESOLVED` |
| `raw_ra0_n` | 31 省最大绝对差；L2 | 模型期原始回报尺度 `UNRESOLVED`，零附近绝对门 `UNRESOLVED` |
| `rah_{n+1}` | 31 省最大绝对差；L2 | 同模型期 payoff，但不同对象；尺度与零附近门 `UNRESOLVED` |
| `S_{n+1}[d,o]` | 31×31 最大绝对差；Frobenius | 无量纲、自然上界 1；零份额直接用绝对差，阈值仍 `UNRESOLVED` |

| Owner 待决项 | 候选建议（均 `PROPOSED_NOT_ADOPTED`）及当前缺口 |
|---|---|
| 对象 | 用上述完整 carrier 及冻结身份约束，保留冗余核验；是否将内层分布/额外报告聚合纳入停止规则仍由 Owner 决定。 |
| 范数/尺度与零处理 | 每分量 max 范数、辅助 L2/Frobenius，逐分量固定经济尺度和零附近同量纲绝对门；所有尺度/容差数值 `UNRESOLVED`。 |
| 容差 | 没有可据三次缩小变化推出的外层数值；HJB 内层 B/D 容差不可转用。任何具体阈值须 Owner 根据单位、目标精度和噪声证据另定。 |
| 检查点与残差 | `C_n` 对 `C_{n+1}`，两边均需完整合法 turn 及下一束准备；对这个**未加速、未阻尼、同一冻结 θ** 的候选映射，实际一步变化 `x_{n+1}-x_n` 才等于在 `x_n` 评价的映射残差 `F(x_n)-x_n`。若重构方式、冻结输入、随机性或加速改变，该等式不可直接沿用；近零一步变化不证明数学收缩。 |
| 停止规则 | 候选为合法性优先、全部必需分量同时达标的预声明规则；连续检查次数、精度与分类语言 `UNRESOLVED`，判据达到也只可称“本有界映射的预定数值判据满足”。 |
| 最大 turn/调用预算 | 可供 Owner 考虑分批最多两完整 turn、每类模型调用明示上限及失败计数；具体最大 turns/各调用上限 `UNRESOLVED`。此建议不授权任何一次 turn7 调用。 |
| 首个失败 | 合法性失败立即停止并封存首错；合法但未达阈值继续仅在将来授权预算内；预算耗尽记 `VALID_NOT_MET_OR_UNRESOLVED_AT_BUDGET`；全部门满足记 `CRITERION_MET_FOR_BOUNDED_MAP_ONLY`。是否采用这些标签、是否禁止重试需 Owner 决定；当前零调用任务没有重试权。 |

被冻结的 `Zt,pit,N,Kt0,theta`、Taylor 参数和源代码参数无需“收敛”比较；固定工资 **并不存在**：进入 `wjt` 与 `w` 是跨回合更新量（R:302–308、363–371；W）。一个未来获授权的诊断最多能在指定冻结路线、指定状态、指定范数/容差及有限预算内报告数值判据是否满足；不能凭此证明全局收缩、数学固定点、通用稳态、完整 GE 均衡、校准有效或 Results 可用。现有 turn3–turn6 的范数比值仅为描述，`fixed_point_tolerance=null`（E；已接受卷宗及其独立审查）。
