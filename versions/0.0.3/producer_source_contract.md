# V0.0.3 Corrected Producer 联合来源合同

资格上限：`DOCUMENTARY_SOURCE_CONTRACT`。本文为 SOURCE / DESIGN 合同，不是
真实资产认证、文件读取许可、数值重跑或生产准入。所有产物 locator 均来自
公开源码/历史接受；本版没有核查其当前存在性、字节或访问保护。

冻结计划：`768a3181fcbc9d367ccce08b1d69458353a48229`，blob
`1bf80332586a4e3beeeb355d90b5ec049c7e503c`；独立授权
`2ec13ea41e7bb86eacb19f4601d243a1298bd4bd`。
本版候选单父基线为 `8f5457947492eef552f4261f8630c6c886af9fa5`，tree
`af2a6a3d85f7525d480ad7da1916eaa25bf349b1`；不是历史 run004 的 execution HEAD。
历史 producer 的精确执行版本与资产绑定仍须从获准原证独立确认。

## G1：来源与证据对象

下列 path/行号均指向本次实际读取的固定基线。GitHub 源码身份可独立重读；
`SOURCE_ONLY` 仅证明代码事实。`HISTORICAL_ACCEPTED` 仅描述原接受的范围。
`UNKNOWN` 表示未证实，`REQUIRES_OWNER_AUTHORIZATION` 表示尚无保护读取许可。
V0.0.2 的 `SYNTHETIC_ENGINEERING` 模拟身份/seal 不提供本版真实信任锚。

### 可重读的固定来源

| ID | 路径（基线相对路径） | Git blob |
|---|---|---|
| S1 | src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py | a473f86eef22ad893673dba2a80ec8029de8afd1 |
| S2 | src/ch5_two_asset_hank/corrected_diagnostic/optionb_initial_turn_integration.py | 114202ca4b23b8e29e6220295bd98860ea391d67 |
| S3 | src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py | 042189063fa5d24480ed4193e133425599b32c8b |
| S4 | src/ch5_two_asset_hank/corrected_diagnostic/run004_canonical_integration_replay.py | 94505fbddcf50cae3052290ac984d0793ccfa1be |
| S5 | validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py | 37936a422d4ea34d925a2ca67461cd9fc5f40b9e |
| S6 | validators/multi_province/beijing_unique_closed_class_kfe_candidate/run.py | 57cd518f9edee6c594c4fab6571448a2d6068436 |
| S7 | scripts/ch5_mp4c_2018_corrected_household_aggregate_binding.py | 9a49b5841871d8276dc90d73fa6df60fb4d26e8c |
| S8 | exports/matlab_faithful_two_asset_ha.py | e144c645d3f4dc842c2faa6b93b2ba0e24275dcf |

固定源码链接格式：
`https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/8f5457947492eef552f4261f8630c6c886af9fa5/<path>#L<line>`。
例如 [corrected terminal KFE](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/8f5457947492eef552f4261f8630c6c886af9fa5/src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py#L956)。

### 分开保存的历史原件

以下文档全部以相同基线固定引用，均未在本版修改：

| ID | docs/ 下的原件 | Git blob | 范围 |
|---|---|---|---|
| H1 | CH5_MP4C_2018_CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATE_AND_ADAPTER_BINDING_ACCEPTANCE_20260920.md | a8b5bf7f4089fe2f003b54f8fabe18d0bd84b032 | 固定 checkpoint-11 聚合与 opt-in adapter fixture，非31省认证 |
| H2 | CH5_MP4C_CORRECTED_OPTIONB_BEIJING_UNIQUE_CLOSED_CLASS_KFE_METHOD_CANDIDATE_DIAGNOSTIC_ACCEPTANCE_20260920.md | 0e13f3b25d18ad107be1d5700e02f3f00955e57c | 北京 checkpoint-12 方法候选诊断，原接受时尚待 Owner 方法采纳 |
| H3 | CH5_MP4C_UNIQUE_CLOSED_CLASS_SUPPORT_KFE_OWNER_ADOPTION_20260920.md | 1351e6537ce9397bda1c6efd02839e5565dc8c32 | Owner 随后采纳 unique-closed-class terminal KFE 方法 |
| H4 | CH5_MP4C_CORRECTED_INITIAL_TURN_FULL_CLOSURE_ACCEPTANCE_20260920.md | 8aac7ebd6af43c31723283e258515c80aebcd1dc | run004 历史31/31 HJB、采纳的 KFE、aggregate，及 integration-only replay |
| H5 | CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_OWNER_ADOPTION_20260921.md | 524b2cd6ecef879c457a92c50b96b21ca2694481 | 后续 HJB relaxation 与同 checkpoint B AND D 法则 |
| H6 | CH5_MP4C_K1A_RAW_RA0_PAYOFF_OWNER_ADOPTION_20260920.md | 2437d7576afd2c807e462d2c93ec34856a28cf3f | raw-ra0、一模型期、同 S、lagged timing、收益与 taper 分离 |

H1 的 V11/P11/u11/Q11/mass 及其接受不能并入 H2 的北京 Q12/p_full。
H2 的数值支持与 H3 的方法采纳是不同门。H4 的历史31省成功可以引用，
不能解释为今天所有省份文件、权限或后续 turns 已认证；其 replay 未重跑家户。
H5 是后来的方法扩展，不能倒写进9月20日 producer 的实际运行版本。
本版不会重写这些历史合同中的旧“下一步”或借其恢复已耗执行预算。

### 实际 corrected 调用与字段矩阵

| 源字段/阶段 | 实际源码事实 | 必须补齐的联合证据 |
|---|---|---|
| 初始 producer | S2 `_solve_province`:591；source_initial_arrays:616；_map_checkpoint:653 | 该运行的 producer/code hashes、进入状态、参数、grid、run/province/turn，不以当前代码代替历史 execution HEAD |
| 后续 producer | S3 `_solve_province`:638；S5 run_household_turn:454–480 调用 S3 的 province solver | 并行任务驱动的 stage/路径与历史授权要分别绑定；不得调用本版禁止的 runner |
| C/l/utility | S1 `_policy_arrays`:409–422，把选定政策填入 `(20,20,2)` F 数组 | 数值字段完整摘要、选定政策对象、cell/F-index与同值 Q 关系 |
| policy identity | S1 `_selected_identity`:397–405；_policy_diagnostics:431–439 | identity 主要是分支/约束/marker，不是 C/l 全数值摘要；还需数值 artifact/字段封存 |
| checkpoint identity | S1 checkpoint_identity:318–323 | V + policy marker identity + CSR Q 的组合，不独立包含省份、进入状态、收益、grid 或代码身份 |
| HJB terminal | S1 primary_converged:326–331；S2:693–702 | 同 checkpoint 有限 B<=1e-8 AND D<=1e-7；相关 V_old/V_next、fresh policy/Q 与原求解回执 |
| Q | S2 _map_checkpoint 产生同值 policy/Q；S1 _sparse_identity 与 checkpoint_identity | 原 Q artifact bytes、CSR data/indices/indptr/shape、轴序、D2 gate、省份与checkpoint联合关联 |
| KFE 调用 | S2:733–742、S3:780–789 → accounting wrapper → S1 _terminal_kfe:956 | passed-in Q 与封存 Q 必须是同一原件；terminal-only、唯一闭类与准确科学计数 |
| KFE方法 | S1:966 onward exact-positive SCC；Q_CC restricted solve、零暂态嵌入、一次原 Q 验证；H3方法权威 | 原拓扑/support、两 rank views、一次 GESVD/方向/归一化、原验证及无 fallback 证据 |
| p/g | S1:1233–1252 写 stationary_mass_arrays 与字段摘要；g=p/OMEGA | 与原 Q/省份/checkpoint一致，closed/transient 索引、非负及归一化、p/g/omega联合封存 |
| grid / omega | 20×20×2 `(b,a,z)`，b最快，F-order，omega=70/361 | 完整坐标/参数身份而非形状或名字；无 dz、端点加权或再次密度归一化 |
| uniform rah | S2:747/759；S3:794/806 来自进入state | 历史 bootstrap vs 后续 raw-payoff 角色，进入状态和上一已完成return来源 |
| effective_r_a | S2:746–749；S3:793–797，冻结 taper | 同一 rah、grid和参数；不是另一个自由输入或年化收益 |
| aggregate | S2:752–760；S3:799–807 调用 corrected adapter | 同政策/mass/returns，Ct、z加权Lt、At/Bt/AtTax 原式，不改变科学量纲 |
| frozen/batch | V0.0.1/V0.0.2 只接受合成消费路径；S4:228–240 重构历史batch | 不把标量或 converged flag 当完整科学证据，不声称本版执行过消费 |

S2/S3 import 的 faithful grid/params 容器不是 faithful solver 的调用证据。
S8:652–669 的 contaminated-row KFE 及再归一化不是已采纳 corrected KFE；
S8:698–705 的 solve_household_steady_state 禁止用于替代本路线。
S7 固定 checkpoint-11 binding 只作为 SOURCE_ONLY locator/映射，不运行。

## G2：联合身份 schema（DESIGN_ONLY）

未来受信任记录必须分别保存以下域，不以一个 `REAL_AUTHENTICATED` 位概括：

1. Authority：合同/接受固定commit、原范围、适用method版本、签发/独立回读依据。
2. Producer：历史execution HEAD、数值源码blobs、run/task、环境、实际方法与原调用账。
3. Context：province index/name/order、outer stage、checkpoint、进入state与参数/初始化来源。
4. Policy/value：V、V_old、C/l/utility数值身份、policy marker身份、grid/F-index、B/D原回执。
5. Operator：原CSR Q artifact与内容身份、D2证据；policy/value/checkpoint的对应边。
6. Terminal mass：method、Q引用、support/rank/SVD原回执、p/g与omega、原验证、artifact成员身份。
7. Returns：uniform rah、used effective_r_a、冻结taper；后续raw-ra0来自同路径上一完成turn，
   quantity/payoff使用同一S及其方向，规定reduction与时序；bootstrap必须单列历史初始化资格。
8. Consumption：aggregate/frozen/batch的输入关系、科学/经济/生产资格分别表达。
9. Access：Owner精确文件/字段/次数/字节许可、保护条件、有效期、保密与输出限制。

### 验证顺序与拒绝

| 顺序 | 必要输入/检查 | 拒绝或缺口 |
|---|---|---|
| 0 权限与保护 | 本版之外的Owner明确选择、准确文件清单、Objective A16/window与路径条件 | 未授权、旧闭预算、保护风险：不打开文件；REQUIRES_OWNER_AUTHORIZATION |
| 1 可信权威锚 | 独立可核历史接受/采纳原件及其适用producer/method版本 | 自报seal、孤立hash、目录名或模拟metadata：不足；不能选错方法 |
| 2 manifest原件 | 在精确新许可内匹配可信锚，限定成员与实际bytes | hash不符/缺原件/越大小：停止；不得全量跟随4353成员 |
| 3 联合成员 | run/province/stage/checkpoint、state/params/grid/code、V/C/l/Q引用 | 跨省/跨turn/跨checkpoint、marker代替数值、完整state缺失：UNKNOWN/BLOCKED |
| 4 same-Q mass | 采纳方法、support、rank/原KFE回执及p/g与同Q引用 | faithful pinning、旧full-space方法静默替代、wrong p/g/omega、第二归一化：拒绝 |
| 5 收益与消费 | rah/effective角色、taper、raw-ra0/S/lagged或历史bootstrap资格 | 同turn反馈、跨路径收益、错误S、收益口径/时期转换：拒绝 |
| 6 资格与生命周期 | 授权内快照、不别名、原件不可变、每次消费明确来源/允许作用 | byte完整性不能升级科学/经济/生产资格；未定义经济映射阻止对应用途 |

哈希证明内容匹配，不证明真实生成过程、科学有效或访问合法。历史人工接受提供
其原范围的证据锚，不是整个目录的永久授权。真实 source-loader、独立认证器、
新签名或数值验证都不是本版实现。后续获准回读也不能自动调用 SCC/SVD/Q.T@p。

## 尚未认证及科学停点

当前资产存在性/bytes、run004北京terminal checkpoint、子文件hash、历史producer
与当前代码差异、C/l数值联合身份、完整进入state及收益来源均 UNKNOWN。
劳动力量纲、人口分母、外部年份/价格/日历、真实callback、31省当前可用性、
稳态/GE/Results/生产均未通过。人口/人均保留、户均封存、不N=P/3。
C9 PAUSED、CALL_LEDGER_UNRESOLVED、Objective A16 UNRESOLVED/FAIL_CLOSED、window
UNACCEPTED、model_activation=False、Results FALSE和旧CLOSED预算保持。
下一门及Owner选择见 [读取申请](owner_read_request.md) 和 [执行/阶段记录](execution.md)。
