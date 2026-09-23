# K1B 收敛诊断设计证据卷宗（零科学调用）

Task ID：`CH5_K1B_CONVERGENCE_DESIGN_EVIDENCE_DOSSIER_20260923`。起始工作树 `D:\ProjectTemp\c5k1bturn56` 干净，派发 HEAD `e23d952a68c0947778ac43ab663b11e5282e7376`；生产 `src` 树为 `00682b2e1a7ba23665f6e16f6acf48ad35874883`。本卷宗只整理封存证据，不选择收敛律。Results eligibility：`FALSE`。

## 已有证据能说明什么

独立审查接受了 turn5、turn6 各 31 省的 HJB/KFE 与各一次集成，以及 turn7 的输入准备；turn7 household 未运行。该审查把 turn3–turn6 明确限定为有界轨迹，没有接受收缩、固定点、稳态或 Results 结论。见 `docs/CH5_MP4C_K1B_TURN5_TURN6_INDEPENDENT_REVIEW_ACCEPTANCE_20260923.md` 的“Independent checks”和“Scientific route”，以及封存的 `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/turn3_through_turn6_trajectory_diagnostic.json`（下称 *轨迹 JSON*）。轨迹 JSON 的 `classification` 为 `DESCRIPTIVE_ONLY__NO_CONTRACTION_OR_CONVERGENCE_ACCEPTANCE_CONDITION`，`fixed_point_tolerance=null`，`convergence_claim=false`，`acceptance_condition=NONE__BOUNDED_TRAJECTORY_DIAGNOSTIC_ONLY`。

完整回合检查点应区分**完成 turn n 的输出**与**由该输出准备的 turn n+1 输入**。企业 `raw ra0_n` 在完成 turn n 后取得；其原始水平用作下一回合的 payoff，人口标准差 `ddof=0` 的 z-score 只用于下一回合外国吸引力。`S_{n+1}[destination,origin]` 的列和为 1，`rah_{n+1,origin}=sum_destination S_{n+1}[destination,origin] raw_ra0_{n,destination}`。同回合回报不得反馈本回合份额。见 `SCIENTIFIC_DECISIONS.md` 的 K1/K1B 行、`src/ch5_two_asset_hank/multi_province/capital_network.py:16-20,133-155,289-312`、`src/ch5_two_asset_hank/multi_province/firm.py:103-125`；turn7 的时间标识见 `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/turn7_entering_bundle_manifest.json`。turn7 束仅是输入来源，不是 household 执行许可。

## 可比较对象清单

下表的“可用”只表示已有封存检查点可追溯，不表示适合作为未来固定点判据。31 省顺序和矩阵方向必须保持；标为 `UNRESOLVED` 的单位或对象不能据此设阈值。

| 类别与对象 | 维度、量纲/归一化 | 检查点与来源 | 设计限制 |
|---|---|---|---|
| 完成回合的家庭聚合序列/可比较对象 `Ct, At, Bt, AtTax` | 各 31 省；家庭人均/源聚合量，精确经济单位 `UNRESOLVED`；聚合用概率质量，不额外归一化 | 完成回合后的家庭输出；轨迹 JSON `aggregate_state_changes`；`src/ch5_two_asset_hank/multi_province/corrected_household_adapter.py:153-205`、`province_contracts.py:80-101` | `At` 三次变化接近或等于零，单独监测它可能漏掉其他变化；被采纳的外层 state/map 定义为 `UNRESOLVED`。 |
| 家庭 `Lt` 与目的地 `Lt_supply` | 各 31 省；前者 `sum(z*l*p)`，后者是重建的企业劳动供给；共同量纲/比例 `UNRESOLVED` | `Lt_supply` 有轨迹变化，家庭 `Lt` 未列入轨迹 JSON 的相邻变化；`corrected_household_adapter.py:174-176`、`province_contracts.py:80-89`、`c1_residual_public_asset.py:61-72,90-94` | 两者不能混称或直接替换。 |
| 资本与公共资产 `Kt, Kt_supply, GovInv` | 各 31 省；资本/公共资产使用同一声明单位 MU；`Kt` 与 `Kt_supply` 定义不同 | 完成回合集成；轨迹 JSON `aggregate_state_changes`；`c1_residual_public_asset.py:73-93`、`firm.py:24-26`；`SCIENTIFIC_DECISIONS.md` 的 C1 行 | 总资本守恒残差与 `GovInv` 总量是校验/会计量，不能单凭近零变化宣告固定点。 |
| 产出与工资 `Yt, w` | 各 31 省；精确单位 `UNRESOLVED` | 完成回合状态；轨迹 JSON `aggregate_state_changes`；`firm.py:20-30`、turn5–turn6 报告的轨迹表 | 不同尺度需由 Owner 决定如何合并。 |
| 完成回合 payoff `raw ra0_n` | 31 省；一模型期净生产资本回报原始水平，无裁剪、年化或 z-score | 完成 turn n 后企业输出；轨迹 JSON `raw_ra0`；`firm.py:103-125`，turn5–turn6 报告“integration”段 | 与下一回合输入有一拍时间差。 |
| 下一回合策略 `S_{n+1}` 与 `rah_{n+1}` | `S` 为 31×31 目的地×来源、无量纲列归一；`rah` 为 31 省回报水平 | 完成 turn n 后准备；轨迹 JSON `portfolio_shares`、`rah`；`capital_network.py:289-312`；turn7 manifest | 份额变化与 payoff 变化不是同一经济对象；检查点须统一。 |
| 下一回合外国吸引力 z-score | 31 省、无量纲，原始 `ra0` 的总体标准化（`ddof=0`） | 轨迹 JSON `zscore_inputs`；turn5–turn6 报告 turn6/turn7 preparation 段 | 均值/标准差是输入生成的描述，不是独立的固定点对象。 |
| 800 格点/省的 HJB 价值、政策、KFE 分布 | 每省 20×20×2，F-order、`b` 最快；逐回合可比序列/归一化定义 `UNRESOLVED` | `SCIENTIFIC_DECISIONS.md` 的 household 行；封存逐省 terminal receipts | 轨迹 JSON 没有这些完整分布的相邻范数，不能声称已有状态收敛指标。 |

## 原有相邻变化的复述

定义沿用轨迹 JSON 的字段：对同序向量/矩阵，`maximum_absolute_change=max(abs(new-old))`，`euclidean_norm` 是向量差的 L2 范数，`frobenius_norm` 是矩阵差的 Frobenius 范数；`mean_signed_change=mean(new-old)`。`successive_change_norm_ratios` 是后一次变化范数除以前一次变化范数，属于描述性比值。以下数值直接取自轨迹 JSON 的 `transitions`；更完整的十项聚合变化、SHA 身份和比值在同一 JSON 中，机器清单也逐项保存。

| 过渡 | `raw ra0` 最大值 / L2 | `rah` 最大值 / L2 | `S` 最大值 / Frobenius | 直接 HJB 更新旧→新 | 检查点数有变化的省数 |
|---|---:|---:|---:|---:|---:|
| turn3→4 | 0.004025704005734321 / 0.005510286646555688 | 0.0035652015398268677 / 0.0051617819986116914 | 0.00017089672979736514 / 0.0002936100333500836 | 377→378 | 4 |
| turn4→5 | 0.0007664942733158764 / 0.000982914495908585 | 0.0006755443013624074 / 0.0009075749448952141 | 0.000038570139761918976 / 0.00006541207640255853 | 378→378 | 0 |
| turn5→6 | 0.00014688108470894967 / 0.00018198170434988712 | 0.0001290310060115818 / 0.00016676957901415662 | 0.000008122347528477514 / 0.000013640143450284201 | 378→378 | 0 |

相邻 L2/Frobenius 比值（turn4→5 相对 turn3→4；turn5→6 相对 turn4→5）：`raw ra0` 为 `0.17837810606876045, 0.18514500000497722`；`rah` 为 `0.17582589600632392, 0.1837529561081166`；`S` 为 `0.2227855623876619, 0.2085263792321792`。这些数没有给出收缩域、统一映射、误差界或停止规则。turn5→6 的 `Ct` 最大绝对变化为 `0.004077179613416249`，`Lt_supply` 为 `263.9059808589518`，`Kt_supply` 为 `830.6433400935493`，`GovInv` 为 `830.6433400958776`，`Yt` 为 `202.4450707733631`；混合单位直接设一个共同绝对阈值无根据。见轨迹 JSON `transitions[*].aggregate_state_changes` 及报告“Turn3-through-turn6 trajectory diagnostic”。

## Owner 决策矩阵（均未采纳）

| 待决项 | 现有证据 | 未决科学选择与未来诊断后果 |
|---|---|---|
| 比较的经济对象 | 上表的 payoff、下一回合策略/回报、状态和报告聚合量都可追溯，但时间点不同。 | Owner 需指定单一对象或有明确定义的联合对象，并规定是否要求所有分量同时满足；遗漏的分量不能由现有缩小趋势补足。 |
| 范数与尺度 | 轨迹 JSON 已给 max、L2/Frobenius、均值；量纲混合。 | Owner 需指定范数、按省/全国聚合方式、零值处理及任何尺度基准；不同选择会改变“接近”的含义。 |
| 容差 | 封存面板 `fixed_point_tolerance=null`。家庭 HJB 的 B/D 容差只针对内层求解。 | 外层容差 `UNRESOLVED`；不得借用 HJB 容差或由三次比值倒推。 |
| 检查点时间 | `raw ra0_n` 来自完成 n，`S_{n+1}`/`rah_{n+1}` 是下一回合输入。 | Owner 需规定完整回合后的对齐方式、先决的 31/31 household 与一次集成门；错位比较会改变被检验映射。 |
| 停止规则 | 现有面板接受条件为 `NONE__BOUNDED_TRAJECTORY_DIAGNOSTIC_ONLY`。 | 首次过阈、连续次数、是否同时检查残差/约束等均 `UNRESOLVED`；需先定义才可把未来路径标为达到或未达到。 |
| 最大回合/调用预算 | 已封存四个完整回合，turn7 只有输入束。 | 最大回合、每类调用上限及预算耗尽的终态 `UNRESOLVED`；新任务必须独立给定且失败调用计入预算。 |
| 失败行为 | 现有审查只接受有界执行，不接受固定点。 | 家庭门失败、非有限值、份额/资本恒等式失败、阈值未达和预算耗尽各如何分类须由 Work/Owner 明定；不能自动重试、调参或宣称稳态。 |

## 静态封存与交接门

机器清单：`EVIDENCE/ch5_k1b_convergence_design_dossier_20260923/decision_inventory.json`。本任务的 HJB/KFE、集成、企业、K1B、turn7 household、GE、Results 及所有模型/科学调用均为 `0`。本卷宗不提供任何后续科学执行权。待 Work 独立审阅，涉及实质收敛律的选取由 Owner 决定。
