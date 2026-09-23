# 完整外层 carrier 的单位、尺度与精度证据（零科学调用）

Task `CH5_FULL_OUTER_STATE_UNIT_SCALE_PRECISION_EVIDENCE_20260923`。起始/提交前 HEAD：`1e12ac1bff3a770ab7ba8df12201bf276a9c188f`；父提交 `4d80d992e0d5f537a400f586cb526b584342adc0`；冻结 `src` 树 `00682b2e1a7ba23665f6e16f6acf48ad35874883`。这是对已通过 Work 设计质量审查的八向量/一矩阵候选 carrier 的补证，**不是 Owner 对 carrier、尺度、范数或容差的采纳**。科学/model 调用为零，turn7 household 未运行，Results eligibility 为 `FALSE`。

## 来源和静态取值口径

- 设计对象及 C_n 对齐：`docs/CH5_FULL_OUTER_STATE_MAP_ZERO_SCIENCE_DESIGN_20260923.md`；独立审查 `docs/CH5_FULL_OUTER_STATE_MAP_ZERO_SCIENCE_DESIGN_INDEPENDENT_REVIEW_20260923.md`。当前有界路线的候选写者与计划字段见 `validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py:227-400,428-481`（下称 R）。
- 单位原点：`src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py:21-30,80-102,115-153,177-192,252-269`（下称 U）。源码字面单位 `MU_10WAN_YUAN` = **10 万元**，`NU_100_PERSONS` = **100 人**；原始 GDP/资本的亿元值乘 1000，人口的万人值乘 100。源码把初始化 `Yt0,Kt0,N` 绑定在这些单位，并以 `N` 充当初始 `Lt` 代理。动态劳动量/工资的精确经济单位没有同级声明。
- 家庭与劳动/企业方程：`src/ch5_two_asset_hank/multi_province/corrected_household_adapter.py:153-205`（家庭聚合），`src/ch5_two_asset_hank/multi_province/migration_labor.py:36-73,98-130`（下称 L），`src/ch5_two_asset_hank/multi_province/firm.py:44-139`（下称 F），`src/ch5_two_asset_hank/multi_province/wage.py:11-75`（下称 W）。冻结份额及 payoff 见 `src/ch5_two_asset_hank/multi_province/capital_network.py:133-164,275-342`、`validators/multi_province/k1b_turn3_lagged_raw_ra0_activation_safety_gate/run.py:114-141` 与 `SCIENTIFIC_DECISIONS.md` 的 K1/K1B 行。
- 封存检查点 C4、C5、C6 分别由 turn5、turn6、turn7 **进入候选 JSON/NPZ** 代表；C6 的 turn7 束只来自已完成 turn6 的 raw `ra0`，不代表 C7。路径、SHA-256 与全部数值范围/ULP 在 `EVIDENCE/ch5_full_outer_state_unit_scale_precision_20260923/evidence_receipt.json`（下称 receipt）。R:88–125、322–380、428–451 定义候选/计划的绑定。turn3–turn6 轨迹 `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/turn3_through_turn6_trajectory_diagnostic.json` 是描述性证据，不提供容差或噪声下界。

以下表中的 C6 水平是封存 `turn7_k1b_input_candidate.json` 的 31 省向量或配套 NPZ `portfolio_shares_destination_origin` 的**静态** `min / median / max`；表格显示值适度缩写，receipt 保留从封存 float64 解析的完整值。`ULP` 是 C6 中位数附近相邻 float64 的间距，**不是模型误差界**。`PROPOSED_NOT_ADOPTED` 的固定尺度只说明经济解释可能成立，不能从这些水平选择阈值。

| carrier；轴/顺序 | 定义、单位证据 | C6 水平；精确零/近零 | 固定尺度候选与解释；精度与缺口 |
|---|---|---|---|
| `Yt`，31 省 | F:86、136–139 的企业产出；U:139–147、179–182 的 `Yt0` 为 MU。动态 Yt 为 MU 是沿同一生产方程/校准的**量纲推断**，非独立输出单位声明。 | `5.5687e6 / 4.4891e7 / 1.4876e8`；零 0。 | `Yt0_i` 是冻结的 2018 各省产出 MU，可作为“相对基年产出”的**提案**；C6 中位 ULP `7.450580596923828e-09` MU。动态单位继承和可接受经济精度仍待 Owner。 |
| `Lt`（旧企业劳动），31 省 | L:104–125 从人口 `N`（NU）和工资/消费/楔子重建目的地供给；R:289–295 传给企业，F:56–63、136–139 写回 `Lt`。若劳动因子无量纲，可推得 NU；该前提与精确单位**`UNRESOLVED`**。它不同于家庭 `Lt=sum(z*l*p)`（家庭聚合源码:174–176）。 | `4.6924e6 / 5.0922e6 / 5.2403e6`；零 0。C6 `Lt/N` 为 `4.04 / 13.21 / 132.55`，不宜把 `N` 自动认作可比尺度。 | `N_i`（冻结人口 NU）仅是**有条件提案**；须先澄清源劳动量纲/归一化。中位 ULP `9.313225746154785e-10` 个序列化单位；经济尺度与噪声均未定。 |
| `wjt`（企业目的地工资），31 省 | F:101–133 从 `mt,alpha,Zt,Kt/Lt` 算 `wt0`，再经 `wjtmin/wjtmax` 边界给出。若 Yt=MU 且 Lt=NU，工资可推为 MU/NU；源码未独立声明，**`UNRESOLVED`**。它不是复合家庭工资 `w`。 | `0.8 / 1.3 / 1.3`；零 0；3 省精确下界、25 省精确上界、3 省内部。 | 冻结初始 `wjt0` 或工资经济单位可供**提案**，但尚无足够单位/精度证据支持固定尺度。中位 ULP `2.220446049250313e-16`；裁剪可造成平坦变化，不能据此宣称外层稳定。 |
| `rk`，31 省 | F:80、103 的 `mt*alpha*Yt/Kt`，作为下回合 prior `rk`；同 MU 的产出/资本比给出无量纲每模型期回报的**方程推断**，日历年率 `UNRESOLVED`。 | `0.278897 / 0.516388 / 1.114404`；零 0。 | 以 1 个十进制回报单位衡量绝对百分点变化是**提案**，不依赖本次经验中位数；中位 ULP `1.1102230246251565e-16`。经济目标精度与外层误差界缺失。 |
| `Kt_prev`，31 省 | R:368 写本回合 `firm.Kt`，F:61 的 `Kt=Kt_supply+GovInv`，U:143、180 的资本/目标为 MU；由同量纲会计关系支持 MU。 | `6.3257e6 / 6.7307e7 / 2.1002e8`；零 0；C6 有 30/31 个 `Kt_prev==Kt0` 位值相等，其余差 `1.4901161193847656e-08` MU。 | `Kt0_i`（冻结基年/目标资本 MU）可作为“相对目标资本”的**提案**；中位 ULP `1.4901161193847656e-08` MU。C1 使 Kt 接近目标不证明其他状态收敛。 |
| `w`（来源家庭复合工资），31 省 | W:55–75 把目的地 `wjt` 与税/楔子/phi 非线性组合，R:302–305、367 写给下一家庭。若上述因子与 `alphal` 无量纲，量纲可能承继 `wjt`；并无显式经济单位声明，**`UNRESOLVED`**。 | `12.8771 / 16.9125 / 17.8304`；零 0。 | 冻结初始 `w0` 是可讨论的**提案**，但其单位及与企业工资的可比性尚未封闭。中位 ULP `3.552713678800501e-15`。 |
| `raw_ra0`（候选 `state.ra0`/行顶层 `raw_ra0_turn6`），31 省 | F:103–110 的未裁剪企业净生产资本回报；`SCIENTIFIC_DECISIONS.md` 明确**一模型期原始水平**，无年化、平滑或 z-score。R:312–350 用完成回合 raw 值准备下一束。 | `0.253897 / 0.491388 / 1.089404`；零 0。 | 1 个十进制回报单位是**提案**的绝对 rate scale，不能拿样本变化量当容差；中位 ULP `5.551115123125783e-17`。经济精度目标/外层误差仍缺。 |
| `rah`（进入下一家庭的 payoff），31 省 | `rah_o=sum_d S[d,o]*raw_ra0_d`，同一 S 且与完成 raw 相差一拍；这是**一模型期组合回报**，不等同于 raw 或外国吸引力 z-score（资本网络源码:289–312；R:322–350）。 | `0.311292 / 0.496876 / 1.017749`；零 0。 | 可用与 raw 相同的 rate 单位作**提案**，仍必须单独检查该分量；中位 ULP `5.551115123125783e-17`。份额加权/序列化误差上界未建立。 |
| `S[destination,origin]`，31×31 | 冻结 `theta=inter_prv_ratio` 决定每来源外国总份额，外国条件 softmax 与本地 `1-theta` 组成列和 1；**无量纲份额**，只把 z-score 用于外国吸引力（资本网络源码:133–164、289–312；R:322–350）。 | `0 / 0.001723313 / 1`；30 个精确零来自 `theta=0` 的一个来源列，正值最小 `1.6061615262412464e-05`。 | 1 个份额单位是**提案**的自然固定尺度，零项可用绝对差；中位 ULP `2.168404344971009e-19`。数值容差、结构零的保持门与映射误差界仍需独立决定。 |

**仅 C4–C6 的事实**：八向量均未见精确零，但这不能预测将来状态；C6 的零份额有固定 `theta=0` 来源。`wjt` 的截断边界与 `Kt_prev≈Kt0` 使局部分量变化可能很小或为零，不能把这些分量单独用作停止证明。所有候选固定尺度均 `PROPOSED_NOT_ADOPTED`；`Yt0,Kt0,N,w0,wjt0` 的身份、单位和使用方式必须在未来判据中明确冻结。

## 已有数值门究竟约束什么

| 证据 | 具体事实与来源 | 能约束/不能约束 |
|---|---|---|
| 内层 HJB/直接解 | `src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py:43-48,326-331` 规定同一检查点 `B<=1e-8,D<=1e-7`、直接线性解 normwise backward error `<=1e-12`。封存 `turn5_reached_province_hjb_kfe_status.json`、`turn6_reached_province_hjb_kfe_status.json` 的各 31 行全部 `HJB_KFE_PASS`：turn5 最大 B/D `3.5289673960825496e-11 / 3.5288722166626485e-08`；turn6 `3.529293524096033e-11 / 3.529515701927721e-08`。两份 `turn*/household_batch_receipt.json` 的最大 backward error 分别 `4.027911808120014e-16`、`3.509596573922357e-16`。 | 约束**每省内层求解**和线性代数残差；不界定九分量外层 F 的绝对/相对求值误差，更不能移作外层容差。 |
| 终端 KFE 与集成恒等 | 上述逐省 KFE `stationarity.residual_inf` 最大分别 `4.553649124439119e-16`、`3.8077180297690916e-16`；唯一闭类/受限 GESVD 门见 `SCIENTIFIC_DECISIONS.md` 及封存逐省 KFE 检查。R:246–287 的 S 列和、私人资本守恒、C1 残差规则通过；turn5/6 `turn*_frozen_k1b_capital_receipt.json` 的全国私人资本残差为 `0`、`2.9802322387695312e-08` MU，后者是在约 `140310000` MU 总量上的浮点算术残差。 | 约束 KFE stationarity 与会计/身份合法性；单次残差不估计同状态重复求值散布，也不界定动态工资/收益误差。 |
| 表示、序列化与 readback | R:67–68 调用 `nonlinear_continuation.py:218-222` 的 `json.dumps(...allow_nan=False,sort_keys=True)` 并写 UTF-8；计划 NPZ 使用 float64（R:312–350）。静态只读解析三束 C4/C5/C6：`raw_ra0_turn{n}` 的 31 个 JSON 数对相应 NPZ 数、`state.rah` 对 NPZ 的 `rah_turn{n+1}_by_origin`，各束按 float64 位模式均为 **0/31 不匹配**；`S` NPZ dtype 全为 float64。turn7 束 manifest/readback 完整，sealed 总 manifest `51F636...2E9127` 的独立 readback 为 9470 条、0 坏路径。 | 证明这些**已存工件**的位值/文件身份一致；float64 ULP、JSON 轮转、哈希和 readback 不能证明上游科学求值的精度或跨机器重现。 |
| 重复求值与噪声 | C4/C5/C6 是**不同**相邻状态；封存报告的缩小变化和 62 次 source-native 初始化分别服务不同省/回合。当前引用的封存证据没有同一冻结 x、同一源与输入身份下的独立重复外层 F 评价。 | 外层映射噪声下界、重复运行一致性与包含 HJB/KFE/企业/工资/份额链的误差传播均为 **`UNAVAILABLE`**。相邻状态差、B/D 门、资本残差或 ULP 不能替代。 |

## Owner 决策矩阵（候选，全部 `PROPOSED_NOT_ADOPTED`）

| 分量 | 已支持的单位/尺度解释 | 无法据此给出阈值的缺口；如需补证的最小后续工作 |
|---|---|---|
| `Yt` | 基线 `Yt0_i` 为正 MU；相对基年产出是条件尺度。 | 动态 MU 继承的源声明、经济目标精度和 F 误差界不足；先做零科学单位/基线绑定审查，如要经验噪声才另授权同状态重复评价。 |
| `Lt` | 冻结 `N_i` 为 NU，但劳动是否同 NU 不明；`Lt/N` 的封存范围显示不能默认归一。 | 先由 Owner/源契约确认家庭劳动、迁移劳动、企业劳动与人口换算；必要的数值误差补证另立有界调用。 |
| `wjt` | 初始 `wjt0` 来源存在，动态边界/截断可核对。 | 工资单位、基线量纲和裁剪平坦区的判据含义未定；先零科学追溯初始工资标度，重复评价仅在需噪声证据时另授权。 |
| `rk` | 由 Yt/Kt 可推每模型期比率；rate 单位可用绝对差。 | 年历解释、可接受回报精度与传播误差缺；Owner 定义目标后，如有必要另授权同状态评价。 |
| `Kt_prev` | `Kt0_i` 为正 MU，C1 目标可作条件尺度。 | 近恒定资本有结构原因；先明确该分量是否仍是独立停止门及所需 MU 精度，必要时另作误差评估。 |
| `w` | 初始 `w0` 来源存在，复合工资公式可追。 | 源未声明其与 `wjt` 的经济单位/标度关系；先零科学单位审查，再决定是否需重复评价。 |
| `raw_ra0` | 已采纳一模型期原始回报；绝对 rate 点可提议。 | 经济回报精度目标、从企业输入到 raw 的误差界缺；不能据现有 ULP 或缩小比值设阈值。 |
| `rah` | 与 raw 同模型期回报单位，但经 S 加权且滞后一拍。 | 份额/收益传播误差及经济精度目标缺；先固定映射身份，必要时另授权同状态评价。 |
| `S` | 无量纲列份额，1 是自然单位；结构零需保留。 | 允许的份额偏差、结构零门和整个 map 误差界缺；现有列和检查仅是合法性门。 |

最小**经验重复性**方案（仅建议）：在未来获授权的专用任务中，以一个**已封存且完全同一的进入状态、份额计划、冻结文件和源码身份**为基准，作一次独立完整外层评价，与原已封存评价组成至少一对；按九分量和中间数逐位/逐差记录，并在任何合法性失败处停止。这仍需要独立列明 31 省 household/HJB/KFE、一次集成及每类调用的上限；本任务没有这些调用预算，不提议具体容差。若同态复现的身份、随机性或平台条件不能固定，噪声估计仍 `UNAVAILABLE`。

## 设计冲突与终点

未见本次静态来源与已采纳 K1B/HJB/KFE 法则的直接矛盾；但有三项应送 Work/Owner 决定：① 已接受设计中“MU（万单位元）”的中文释义不够精确，源码字面为 **10 万元**，这里仅更正本报告的释义，不改已接受文件；② `Lt/N` 的封存量级及劳动量纲未闭合，`N` 不能自动成为有效固定尺度；③ `wjt` 裁剪和 C1 下近恒定 `Kt_prev` 的数值平坦不意味着完整 carrier 稳定。纯数值 F 的文件无关等价性仍依前一设计记 `UNRESOLVED`。

**外层各分量尺度、零附近绝对门、经济精度目标、数值误差界与具体容差全部 `UNRESOLVED`；外层噪声下界 `UNAVAILABLE`。** 本报告不从封存变化或内层阈值推断容差，不触发 turn7，也不支持固定点、GE、稳态或 Results 声称。下一步是 Work 对这份证据候选独立 ACCEPT/REJECT，实质规则仍待 Owner。
