# 完整外层状态停止与复算：Owner 决策材料（零科学调用）

任务 `CH5_OUTER_STOP_REPEATABILITY_OWNER_DECISION_PACKET_20260925`；派发 HEAD `f80f89028e210b3de7a4f2e818f34104741f6f85`，是 Work 验收提交 `8cb5d35224a6a336be81e15a8a727343e5ecc58d` 的后代。`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。本材料只整理已封存证据，**不采纳新停止律，也不授权 turn7 household**；本任务科学/模型调用和重试均为零，Results eligibility 为 `FALSE`。

## 已确立的证据边界

Work 已分别验收 [停止、失败与预算提案](CH5_OUTER_STOP_FAILURE_BUDGET_CONTRACT_PROPOSAL_20260923.md)的材料质量，以及[一次性复算](CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_EXECUTION_INDEPENDENT_REVIEW_20260925.md)的单对执行证据。唯一一次 `K1B_C5_C6P_20260925_ONCE` 从封存 C5 输入完成 31 个省的 household/KFE 和一次 integration；终态为 `PASS__TURN6_SAME_FROZEN_INPUT_REPEAT__ONE_PAIR_ONLY`，账本已核清，无首败、拒绝调用或重试。C6-prime 对封存 C6 的九个外层分量及 70 项中间比较全部为 `EXACT_BITWISE_MATCH`，逐项 bitwise mismatch 和诊断差异为零。生成的进入 turn7 材料只属于这次复算的输出证据；turn7 household 为零。

这确立了**所记录输入、源码、环境下的一对完整外层映射的经验性逐位一致**。它不能给出跨输入、跨环境或所有未来调用的一般数值误差上界，也不证明相邻的 C4→C5 或 C5→C6 变化已收缩、收敛、达到不动点或稳态。内层 HJB/KFE 的通过也不替代外层停止检验。Owner 同意的 `1e-6` 目前仍只是九分量的观察精度；`10^-12` 级精度仍为远期愿望。原提案中 C4、C5、C6 的 clipped `ra` 上界命中均为 31/31；复算逐位一致不会自动解决它与原 MATLAB 零命中谓词的关系。

### 身份和消耗账本的紧凑锚点

| 对象 | SHA-256 / 已验收事实 |
|---|---|
| 生产 `src` 树 | `00682b2e1a7ba23665f6e16f6acf48ad35874883` |
| 已验收复算 runner | `E362B921D4984669C3257A671684F55809702531522D253C26D80886786880B2` |
| 封存 C5 JSON / NPZ | `87BEB944AD35C16BAF62D35FE8DDAD3BDEBC9000DCB6CC9F7D6949A039F4B1BC` / `95880D37D5BBB10B95FF776E32B8B786447B20C1770117044C7735D91292ED34` |
| 封存 C6 JSON / NPZ | `D84E9D74C7E965A3B492F2F0F9A63D3320D436DD4A6D78E1E655F014C05FC059` / `37A1258F8EC87116F03084D8178C77424FDD5F3859A1BC73D9704940A3B9381E` |
| 复算 [preflight](../reports/ch5_turn6_same_frozen_input_repeat_20260923_run001/preflight.json) | `85DFE5F6210DA8373880AFE51213C20C24967008FB028E31B490785E5022A55E`；Python 3.11.9、NumPy 2.4.6、SciPy 1.17.1、Windows-10-10.0.26200-SP0；完整 BLAS/线程环境见该收据 |
| 复算 [比较收据](../reports/ch5_turn6_same_frozen_input_repeat_20260923_run001/comparison_receipt.json) | `4E41A251E050A0D25F73246E36800B872B29F526D519189C1D69B425A8D89C9B`；九分量与 70 中间项逐位一致 |
| 复算 [终态与完整源/尝试账本](../reports/ch5_turn6_same_frozen_input_repeat_20260923_run001/terminal_receipt.json) | `8F008B2CEF18A305EB3A1F4C11DF484CAB249513ACB7475728CF1B1248E6B03F`；37 类 guard 尝试计数与源账本相等 |
| 原位 [产物清单](../reports/ch5_turn6_same_frozen_input_repeat_20260923_run001/execution_artifact_manifest.json) | `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`；5,141 个清单内产物、63,888,760 字节，另有清单自身；逐文件回读无差异 |

一次性预算**已经消耗**。终态尝试账本的关键值是：源初始化 31、labor roots attempted/returned 各 24,800、policy maps 409、selector evaluations 327,200、selector root invocations 141,123、direct HJB updates 与 relaxation helper 各 378、alpha candidates 382、terminal KFE attempts 31、restricted GESVD 31、firm evaluations 31、full integrations 1、frozen K1B allocations/feedback alias 各 1；turn7 household、K2、GE、科学重试和 solver substitution 均为 0。其余类别与精确源/guard 数值以终态收据为准，不把已消耗量误作未来上限。输出根已按上述清单备份，仍原位未跟踪；本材料不写入它。

## 待 Owner 明确选择的科学合同

以下均为**选项而非已采纳规则**。在任何新 household 调用前，Work 需将 Owner 选择写成独立、可审查的任务边界。

| 决策项 | 待选择的明确方案 | 选择后最多支持的主张 | 仍不支持的主张 |
|---|---|---|---|
| 载体与公式 | A：采纳同一阶段的八个 31 省向量 `Yt,Lt,wjt,rk,Kt_prev,w,raw_ra0,rah` 及目的地×来源 `S`。`Yt,Lt,wjt,w` 用 `max abs(new/old-1)`；`Kt_prev` 用 `max abs(new-old)/Kt0`（冻结正 `Kt0`）；`rk,raw_ra0,rah,S` 用最大绝对差，并固定合法分母、维度、有限性和时点。B：修改任一载体/公式，先做新的零科学设计与静态读数。 | A 可形成冻结 K1B 有界映射的九分量可复核比较；B 只确定新设计路线。 | 任一方案都不直接证明完整经济模型的不动点或 GE。 |
| `1e-6` 的地位 | A：在两个完整合法、相邻的同口径 checkpoint 上，要求**每个**分量严格 `<1e-6`，并明示它是有界映射的数值判据。B：继续只作观察精度，暂不设停止判据。 | A 可报告预先定义的有界映射判据是否满足；B 可报告观察值。 | 单点复算没有一般误差上界；A 也不能据此证明数学收敛或物理精度。 |
| R3 证据后的通过次数 | R3 的一对同输入逐位一致已获验收，预算已耗尽。若采纳停止判据，选 R1：一个合法相邻通过；或 R2：两个连续合法相邻通过（C6→C7、C7→C8），在 turn9 household 前停。 | R1 是一次相邻状态命中；R2 另提供连续两次的经验持续性。 | 二者均不给一般重复性误差上界、压缩映射或不动点证明；不能把 R3 一对样本升级为此类保证。 |
| clipped `ra` 上界 | A：对新九分量判据视为不合格；B：逐 checkpoint 报告但不作为该新判据的否决项。无论选择哪项，原 MATLAB 零命中谓词单独保留。 | 只界定新有界 K1B 判据对既有 31/31 命中的处理方式。 | B 不等于原 MATLAB 零命中通过；A 也不自动决定新经济机制的有效性。 |
| 最大新 turns 与调用上限 | 选零、一或最多两个**完整**新 turn，并逐项明确每 turn、逐省和合计的 attempted-call 上限。原提案的 31 省、50 次 direct HJB updates/省、51 maps/省、一次 integration/turn 及两 turn 算术表只是模板。必须另行给 `scalar_selector_root_invocations`、独立 terminal KFE attempts、`k1b_feedback_calls` 的数字与别名口径；一次性复算采用的 20,000,000 roots/省、1 KFE/省、反馈为一次冻结 allocation 的别名可作决策参考，**不自动继承**。 | 可形成一次独立任务的可执行资源上界，账本含失败尝试。 | 已观察的 141,123 roots、31 KFE、1 feedback 不能作为未来上限，也不授权 C7/C8。 |
| 首败、无重试与不确定性 | A：采纳合法性先行、首个原始内层 terminal 与位置/账本保留、缺账本标 `CALL_LEDGER_UNRESOLVED`、无重试；区分合法但水平未达、预算后未达、未完成 checkpoint 和真实失败。B：如需不同协议，先修订设计再申请执行。明确一般外层误差上界仍为 `UNAVAILABLE`。 | A 支持可审计的有界执行和有限证据分类。 | 协议本身不产生数值误差界，也不能把合法未达标说成发散或失败。 |

## 条件建议和下一门

现在可以作出的零科学决定，是**是否**把原提案的载体、严格水平、通过次数、边界命中处理和失败/预算合同采纳为“冻结 K1B 有界映射”的预设诊断判据。单输入的一对精确复算消除了该输入下“是否观察到一致”的未知，但一般外层误差界仍为 `UNAVAILABLE`。若 Owner 愿意在此限制下采纳有界诊断判据，建议 R2 而非 R1，以观察连续两次合法更新的持续性；这仍不是收敛定理。若 Owner 要求先有一般误差界，则保持 `1e-6` 为诊断精度，不启动下一 household。

任何 turn7 household 之前，Owner 必须明确上表全部科学选择，特别是 clipped-`ra` 与三项尚未继承的调用上限；随后 Work 需独立审查并派发新的有界执行任务，绑定封存 C6/进入 turn7 输入、精确 SHA-256、逐省/逐类预算、首败停机、输出与独立复核门。本材料既不作该决定，也不签发该任务。Results eligibility 仍为 `FALSE`。
