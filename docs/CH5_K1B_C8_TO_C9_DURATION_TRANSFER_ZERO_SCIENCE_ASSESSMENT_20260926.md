# C8 测时向 C9/C10 的迁移性与不确定性评估（零科学调用）

任务 CH5_K1B_C8_TO_C9_DURATION_TRANSFER_ZERO_SCIENCE_ASSESSMENT_20260926；签发 HEAD 8dfb3ebc09d754c157c7371dfe4fd66792050dff。独立接受的 C8 同冻结输入测时仅提供一次完整 timed-action 观察：3382.203 秒，原数值终态 VALID__LEVEL_NOT_MET_AT_BUDGET。**当前证据不能给 C9 或 C10 提供可辩护的数值 E_upper；均为 null。** C9 未运行，Results eligibility 为 FALSE。

## 封存输入静态比较

C8 样本使用 C7 已封存并读回的 entering-C8 束；候选 C9 只对应 C8 已封存并读回的 entering-C9 束。两份 manifest SHA-256 为 20861D4ADDBDF1099854EB86B00D24A097C627838B3F6EF5AFAEDABFFD647E5E、40200B60729A5B4173E24661843980851F8610A9FA2186F7E411B7FE9E5CDC65，读回均 PASS、bad_paths=[]、sealed_before_household=true。它们是**不同输入**，且 C9 束只标为候选，未发生 C9 household 调用。

输入 JSON 分别为 58130 与 58129 字节；均有 31 省，0–30 省序与名称逐项相同，每省 state 字段集合及类型结构同为 51 项。其中 27 项在全部省份逐值未变，包括 alpha、corptau、epsilon_pi、inter_prv_ratio、tau、ramin/ramax、wjtmin/wjtmax；其余 24 项至少在一省改变，ra0、rah、rk、w、Lt 等在 31 省均改变。raw-next-payoff 和 share-plan 哈希也不同。两份封存的 zscore/share/payoff 收据均记录 beta_distance=2、beta_return=0.5、ddof=0 且 checks 相同；但 zscore SHA、ordered_mean 和 population_standard_deviation 不同，进一步说明参数固定与输入值变化可同时成立。字段变化是静态输入事实，其对迭代次数和耗时的作用**未测量**。

输入 NPZ 分别为 16185 与 16169 字节。五个对应数组的 dtype、C 序和形状保持相同（三条长度 31 向量、两张 31×31 矩阵），五个成员内容 SHA-256 全部不同；完整成员/省字段比较在机器收据。结构相似、文件大小和已观察调用次数不能换算成未来运行时间。C10 没有合法封存的 entering-C10 束，无法做同类静态比较。

## 计时区间、开销与环境

已接受 timing_receipt 的单调区间从 timed-action start 9261390000000 ns 到科学封存/读回结束 12643593000000 ns，差 3382203000000 ns = 3382.203 秒；science_end 是中间点。已接受 wrapper 源码显示：future_gate 与 static_preflight 在起点**之前**；起点在 run_after_valid_gate 之前。区间包括独占输出创建、31 省及一次集成、尝试日志与计时开销、输出 I/O、科学清单封存及独立读回。测量开销**包含在总值中且未单独估计**。终点在最终 timing_receipt.json 写入和 CLI 退出之前，故此值不是 OS 进程从启动到退出的全长。

计时收据记录 Python 3.11.9、NumPy 2.4.6、SciPy 1.17.1、Windows build 26200、scipy-openblas 0.3.31.188.0。六个线程环境变量均为 null，不能证明实际线程数；machine 字段为空。没有运行时 CPU、内存、存储负载或尾部轨迹记录，候选 C9 也没有执行环境/负载收据。没有依据认为 C9 或 C10 负载条件可迁移。43,200 秒协作资源墙只拒绝到点后的下一科学入口，在途操作可越限；它不是 C9/C10 时长上界。

## 不确定性与日界门

这是 n=1 的未删失完整过程样本，不能估计重复波动、失败/删失频率、跨输入变化影响或负载尾部。Owner 尚未采纳覆盖目标、上界推导方法、跨输入外推条件和安全余量。不得把 C8 的 3382.203 秒、文件时间、任务长度、调用次数、43,200 秒资源墙或猜测倍数转换成 C9/C10 E_upper。

预启动谓词须以时区感知的 Asia/Shanghai 下一次当地 00:00 与同机时钟映射验证 now + E_upper + margin < next_local_midnight，同时核对资源合同和剩余额度。C9 的 E_upper=null、margin 未定，现行谓词无法成立；C10 还须先有完整 C9 封存/读回、自己的输入和独立上界。只有完整外层 turn 可作为跨日检查点；在途调用可越过 00:00 到安全点，手动中断或不确定账本是任务终态，不产生免费重试。C9/C10 均保持 BLOCKED__DURATION_BOUND_UNAVAILABLE。

## Owner 决策选项（均为提议）

| 路线 | 可获得的证据 | 需要的新授权或政策 |
|---|---|---|
| 保持现行门、继续静态审查 | 不产生新科学样本，C9/C10 继续阻断 | 无新科学预算；后续须明确覆盖目标、E_upper 方法和安全余量 |
| 另行预算多次 C8 同冻结输入测时 | 可研究同输入条件下的波动、失败/删失，仍不自动外推 C9/C10 | 旧测时预算已耗尽；每次须新科学预算、独占根、一次性任务和独立审查 |
| C9 专属限额计时例外 | Owner 明确承担缺少预启动上界的风险后才可能观察 C9；一次样本仍不自动建立 C10 上界 | 须显式修改现行预启动风险政策，并另批 C9 有限调用/资源合同、runner、独占根及一次性授权；不得先运行后补签 |

本任务不选择风险路线、不解开 C9 门、不派发后续科学任务。首个剩余门是 GPT Work 对本双路径候选独立 ACCEPT/REJECT；启动风险和科学预算仍由 Owner 决定。

## 来源与账本

- TASK_CURRENT.md — SHA-256 78905986758F307149B0449E45D7D4E75E6E77C9A65D3568E387D5AD96AEAAB2
- tasks/CH5_K1B_C8_TO_C9_DURATION_TRANSFER_ZERO_SCIENCE_ASSESSMENT_20260926.md — SHA-256 78905986758F307149B0449E45D7D4E75E6E77C9A65D3568E387D5AD96AEAAB2
- CURRENT.md — SHA-256 4CDDDAC5675366BC5E9DD5A2D91031494193077FDFC2808B03A5EFD09DBAB491
- SCIENTIFIC_DECISIONS.md — SHA-256 9FFF3D5EAF16E0FBCD7CB153833BEF82332CD4FA394C69F4CE6CC27A24DF0886
- REVIEW_GATE.md — SHA-256 82E8AE771BCDA75D540EFC53FB38EB3F597B8A4A92B61ADD45F7465DFED785E2
- docs/CH5_K1B_C8_TIMING_MEASUREMENT_EXECUTION_INDEPENDENT_REVIEW_20260926.md — SHA-256 89ACCCC3E5DC7B2CD99ADD505A8233BA7DB6235180EF2E31C9A1A8EBD3C4BF0E
- docs/CH5_K1B_C8_TIMING_MEASUREMENT_EXECUTION_20260926.md — SHA-256 1318DE1D6085F4C7AAFC1DB4D8F139653E50CC851748CAB99672AB13271C6A78
- docs/CH5_K1B_PROCESS_BOUND_TIMING_ACQUISITION_ZERO_SCIENCE_DESIGN_20260925.md — SHA-256 F67366FF94C207674021EA12020C3C722591E2B91497974B1192501697606535
- docs/CH5_K1B_C9_C10_COMPLETE_TURN_TIME_BUDGET_ZERO_SCIENCE_PROPOSAL_20260925.md — SHA-256 E4F89A6CBB9461656A758EDF63B6260FE491D88DC3B8878667D0BACC63ABB5DF
- validators/multi_province/k1b_turn8_same_frozen_timing_measurement/run.py — SHA-256 8DFA49C1121EF41FA750844F4F5017779C3E381CFA2E7CBE19C7834D1F0EAB4A
- tasks/CH5_K1B_TURN8_SAME_FROZEN_TIMING_MEASUREMENT_CONTRACT.json — SHA-256 64E0A111E6C8FC186DB58F188CF55159ADCD3BBF213EF1457EF5EA7AEB569CB5
- reports/ch5_k1b_turn7_outer_r2_20260925_run001/turn8_entering_bundle_manifest.json — SHA-256 20861D4ADDBDF1099854EB86B00D24A097C627838B3F6EF5AFAEDABFFD647E5E
- reports/ch5_k1b_turn7_outer_r2_20260925_run001/turn8_entering_bundle_readback.json — SHA-256 5EB75667132473C2F283666B0F3B73BB18FDF00A83C09382827E4C44958246FA
- reports/ch5_k1b_turn7_outer_r2_20260925_run001/turn8_k1b_input_candidate.json — SHA-256 30EDAECEA59ABA03EFFD6C11530617BB7CF80FED175F58437F4DACA9E96D2F3A
- reports/ch5_k1b_turn7_outer_r2_20260925_run001/turn8_k1b_frozen_share_payoff_plan.npz — SHA-256 E6B5D428C1070C6F9F6D9C450F7CDB0D4C2C54F0658074C9C75E60E8FDB743DB
- reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn9_entering_bundle_manifest.json — SHA-256 40200B60729A5B4173E24661843980851F8610A9FA2186F7E411B7FE9E5CDC65
- reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn9_entering_bundle_readback.json — SHA-256 E428D105600D091979B526ADD6BF61E0FC294050B9FAB97FE8B87A29A1012F85
- reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn9_k1b_input_candidate.json — SHA-256 FBB18A5B8B4FD94F337510DBB4E62F94188C27863EED1F79FE2E1A71B5BC39AB
- reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn9_k1b_frozen_share_payoff_plan.npz — SHA-256 E7E6AF79864F67A28386ECF8BEB3B71C6080E9A6C6E64F4CBA8125E1C19D34DD
- reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/timing_receipt.json — SHA-256 AAA86104814A4994083CD50E4B7A8C35792BBB29CD797F12E318AAB8745497F8
- reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/terminal_receipt.json — SHA-256 BEDC0BD2C6DA705B428607CC7CD008985E1E1C222E67E6DC02CB9B47DD09BDC2
- reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/science_artifact_manifest.json — SHA-256 5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D
- reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/science_artifact_readback.json — SHA-256 E7F6CC63AC53220E8FECD90DA2402312AC5EBBCD354431405BC4ADC3E73C2DFB
- reports/ch5_turn6_same_frozen_input_repeat_20260923_run001/execution_artifact_manifest.json — SHA-256 7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61
- reports/ch5_k1b_turn7_outer_r2_20260925_run001/execution_artifact_manifest.json — SHA-256 413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91
- reports/ch5_k1b_turn8_outer_r2_20260925_run001/execution_artifact_manifest.json — SHA-256 5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301

- reports/ch5_k1b_turn7_outer_r2_20260925_run001/turn8_k1b_zscore_share_payoff_receipt.json — SHA-256 1EC883780A1DA8C37D683264859F92EC3BA686B60128BF31DA673A8349B051EA
- reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn9_k1b_zscore_share_payoff_receipt.json — SHA-256 2F7BFF9FE6DFAFEBB7B0289F94B8FEE25CA9368CFE53FA42C6ECBA4E5FF3EB38

受保护 C6-prime、C7、C8 execution manifest 和 C8 测时 science manifest 的 SHA-256 分别为 7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61、413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91、5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301、5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D。任务模型调用 0、科学调用 0、重复测时 0、C9/C10 调用 0、失败尝试 0、重试 0；Results eligibility FALSE。机器收据绑定本报告 SHA-256。
