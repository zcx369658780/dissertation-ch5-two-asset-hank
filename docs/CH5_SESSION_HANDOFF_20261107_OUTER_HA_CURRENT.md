# CH5会话交接：休眠worker入口/输入反序列化/外部保护接线

日期：2026-11-07。本轮完成休眠入口、给定请求输入反序列化和外部保护接线及保存：16新+63回归共79通过；NumPy仅用合成输入/布局/Cg容器，实际原包读取/解释、真实OS/HA/实际网格/科学worker/新额度均0，子代理0。历史各轮测试数不跨轮累加。

## 恢复与当前路线

先核实际两树Git根、分支、HEAD、remote及staged/dirty/untracked。读AGENTS、当前短状态、当前工作流、[Owner自主推进决定](CH5_OWNER_ENGINEERING_AUTONOMY_20261107.md)和本卡；历史只按具体问题读相关报告。外层Zotero旧R40不是CH5授权。普通工程连续完成工作包，不为内部切片再请示；科学预算、保护和接受边界不变。

模型分支codex/ch5-temp31-local-first-source-20261101；本轮启动HEAD 900ca037f718e975ce1ac187beb05a7cebc05217。治理分支governance/ch5-codex-local-first-20261101；启动HEAD 1939509a242a6b4f451d2a57b806947ef57473e4；启动远端治理HEAD ed7a92b199d3b793348d19a0d687b846b82cb85d。现场分支/根/remote及7未跟踪项吻合，main未变。最新代码候选56ce2934cb8bba11445844aae383fc966e7f24e9。最终保存提交和逐文件Blob/字节/SHA256回读见本地交付回执；API与本地链可不同，不强推求同。

路线保持Python多省份外层闭环→31省数据/校准→基准经济→政策实验/第五章写作。TEMP31内部诊断退休，56447829是选定开发基础。HA整体HJB+KFE及原汇总黑箱、算法/网格/controls冻结，正式post→原KFE→原归一化和同inputs、净工资、a*r_a不变。

## Owner已定决定

- 保留Frisch分配及相对劳动厌恶系数；效用Lt是等效劳动指数，不强迫其等于外部算术和。外部双边劳动按含能力z的有效劳动解释，不额外乘z。
- 跨省劳动收入直接归对应家庭，稳态g下家庭工资收入与其各工作省收入加总等同。该模型关系不等于当前源码数值关系已验证。
- Owner核对MATLAB原用加总Ct倒推后，改采原始C逐格路径。原始C/g/原权重分离保存，各格代入原Frisch后按原g/权重积分，再沿A1 pH；不把g放进C负幂、不额外z、不回退Ct、不重归一化。Owner原话：“按上述逐格积分口径实现，不额外新增 z 因子”。机器记录owner_pointwise_adoption.json。
- Lt_prev取上一轮同工作省、同规模企业有效劳动；不取本轮家户劳动或补默认。输入准备已实现，实际企业调度尚未接入。
- A1 E=pH/家庭H、目的地工资税单次、财政Tt/AtTax各乘同源H一次、a*r_a保持。
- 保存A第2轮原值已采纳，仅A/0，生成1进入2；保留A/B上下文。owner_input_adoption.json和新Owner决定优先于旧proposal PENDING/FALSE。不重算/舍入/裁切/补扣税，不重标19，不运行B或冒称完整O2。候选包SHA256为8ed0fb98445ed02debfee0a971e0c728dbd583f6cc323ccfba22406b8191b225；原值和私有载荷只留本地。
- 无需Owner决策或改变路线图时，自主连续推进普通工程；本次已将该决定落实到AGENTS、短状态和工作流，按完整工程结果交付，减少重复清单/逐片文档/重复检查。

## 已完成工程索引

| 工程片 | 代码候选 | 当片检查数 | 报告 |
| --- | --- | --- | --- |
| 原始C/g与逐格劳动 | `4c4c198` | 27新+44回归 | [CH5_O3_RAW_CONSUMPTION_MATRIX_ALLOCATION_20261106.md](CH5_O3_RAW_CONSUMPTION_MATRIX_ALLOCATION_20261106.md) |
| 外部对象/布局守卫 | `7f09b87` | 28+13 | [CH5_B3_EXTERNAL_STATE_GUARDS_20261106.md](CH5_B3_EXTERNAL_STATE_GUARDS_20261106.md) |
| 同record输出胶囊 | `ea6e67c` | 21+9 | [CH5_B3_SAME_RECORD_ORIGIN_OUTPUT_20261106.md](CH5_B3_SAME_RECORD_ORIGIN_OUTPUT_20261106.md) |
| 计数回放 | `90dcd5d` | 31 | [CH5_B3_COUNTER_REPLAY_PRIMITIVE_20261106.md](CH5_B3_COUNTER_REPLAY_PRIMITIVE_20261106.md) |
| 来源到模块绑定 | `e7b5358` | 28 | [CH5_B3_SOURCE_MODULE_BINDING_20261107.md](CH5_B3_SOURCE_MODULE_BINDING_20261107.md) |
| 显式包/延迟导入 | `cb52a5e` | 29+28 | [CH5_B3_SOURCE_BUNDLE_BINDING_20261107.md](CH5_B3_SOURCE_BUNDLE_BINDING_20261107.md) |
| 导入counter关联 | `3f0fe24` | 23+31+29 | [CH5_B3_IMPORT_COUNTER_LINK_20261107.md](CH5_B3_IMPORT_COUNTER_LINK_20261107.md) |
| 进程采样器 | `a009bc9` | 21+23 | [CH5_B3_PROCESS_TELEMETRY_PREPARATION_20261107.md](CH5_B3_PROCESS_TELEMETRY_PREPARATION_20261107.md) |
| Job/counter绑定 | `c313924` | 23+21 | [CH5_B3_SUPERVISED_PROCESS_BINDING_20261107.md](CH5_B3_SUPERVISED_PROCESS_BINDING_20261107.md) |
| 生命周期驱动 | `84d3b53` | 24+23 | [CH5_B3_WORKER_LIFECYCLE_PREPARATION_20261107.md](CH5_B3_WORKER_LIFECYCLE_PREPARATION_20261107.md) |
| Win32后端代码 | `22cd354` | 16+24 | [CH5_B3_NATIVE_WORKER_BACKEND_PREPARATION_20261107.md](CH5_B3_NATIVE_WORKER_BACKEND_PREPARATION_20261107.md) |
| worker字节封存/内联loader/持久占位 | `7949e69` | 16+16 | [CH5_B3_WORKER_BYTE_CAPSULE_PREPARATION_20261107.md](CH5_B3_WORKER_BYTE_CAPSULE_PREPARATION_20261107.md) |
| 原六阶段与同counter接线 | `de139a0` | 15+31 | [CH5_B3_WORKER_PHASE_COUNTER_BINDING_20261107.md](CH5_B3_WORKER_PHASE_COUNTER_BINDING_20261107.md) |
| 同record根回报/Cg/准入集成准备 | `84778bf` | 17+80 | [CH5_B3_WORKER_ROOT_OUTPUT_INTEGRATION_20261107.md](CH5_B3_WORKER_ROOT_OUTPUT_INTEGRATION_20261107.md) |
| 封存worker/装载/占位/root离线组合 | `c71f580` | 17+85 | [CH5_B3_SEALED_WORKER_PACKAGE_INTEGRATION_20261107.md](CH5_B3_SEALED_WORKER_PACKAGE_INTEGRATION_20261107.md) |
| 启动工件静态合同/全部计数覆盖计划 | `6668449` | 18+45 | [CH5_B3_STARTUP_ARTIFACT_CONTRACT_AND_COUNT_COVERAGE_20261107.md](CH5_B3_STARTUP_ARTIFACT_CONTRACT_AND_COUNT_COVERAGE_20261107.md) |
| 休眠入口/输入反序列化/外部守卫接线 | `56ce293` | 16+63 | [CH5_B3_DORMANT_WORKER_ENTRY_REHYDRATION_20261107.md](CH5_B3_DORMANT_WORKER_ENTRY_REHYDRATION_20261107.md) |

各片包含重复回归，不能相加为唯一总测试数。另有[劳动口径](CH5_O3_EFFECTIVE_LABOR_OWNER_CLARIFICATION_20261106.md)、[收入对应账](CH5_O3_LABOR_INCOME_ACCOUNT_MAP_20261106.md)、[Lt_prev准备](CH5_O3_PREVIOUS_FIRM_LABOR_INPUT_BINDING_20261106.md)、[原始C来源静态绑定](CH5_O3_RAW_C_SOURCE_BINDING_20261106.md)、[计数/资源静态计划](CH5_B3_CALL_RESOURCE_STATIC_PLAN_20261106.md)。

此前封存包/装载/占位/root/Cg组合与启动静态合同保持。本轮新增输入传输codec和休眠入口：给定A/0请求往返保留价格位模式、工资/权重原字节，复用原工厂重建worker内同request/inputs/record，接入源码及布局守卫。独立main在import前拒绝，公开执行在解码/I/O/后端构造前拒绝。

最新49源码/90内部边（4延迟，保守装载图无环），新增当前来源/startup合同/两新模块接口/接线计划四份JSON。16新+启动18/守卫28/root17共79通过；来源注释保留在完整清单，consumer按原三字段确定性投影，旧校验未放宽。adapter与守卫角色错配先失败修复，删除身份判断的变异被捕获且源码原字节恢复。原47来源、上片4机器记录、两份adoption和7未跟踪文件共60件启动基线保持。工程自审不冒充独立科学审查；前轮5752调用/165循环只属于当时47文件静态范围，不是当前运行预算。

外部序列旧回归首次13/14，唯一失败为旧24文件快照误当当前树；两处历史接口差异不是本轮改动。已修正工程测试的版本定位：固定旧快照原摘要、明确已知两处差异，当前相关范围按固定c71f580的46来源严格核对，新模块另由47来源绑定覆盖；旧pins和历史reference工件未改、未重新盘点/重绑，修复后14/14，不跳过测试。

占位接口仅测试注入：OFFLINE请求、实际Owner/grid/15预算null，所有真实权限FALSE。替身共享存储按claim_id防重复，换包/目录不复用同一记录；失败不回滚。未证明跨存储/进程、重启持久性、并发原子性或真实全局信任，不是Owner许可账本。完整求解器/native及所有重复源读取/复制/摘要/序列化字节计数仍缺。

本轮本进程用封存合成工资证据、合成packet和小型布局/Cg夹具；NumPy只用于容器/原字节往返，科学函数/HA实例化/外部动作禁入检查有效。原实际候选packet未读取或解释；源码候选存在不代表科学入口/启动声明已采纳，给定字节身份不证明实际冻结grid/参数资格。旧V2和替身证据不迁移为真实运行资格。

## 缺口、下一完整工程包与Owner事项

本轮休眠入口/给定请求输入反序列化/保护接线已完整交付。后续可将休眠源码及传输摘要与已有capsule/固定启动声明做同record静态封装，并准备原候选packet到请求的明确适配；不读取未开放私有载荷、不生成实际grid、不调用真实OS/科学后端。原实际packet仍不透明，当前实际传输/科学入口/capsule/启动声明资格、grid/参数、可信账本、完整计数和实际OS/source/module/root/Cg证明仍缺，actual_worker_program/capsule及实际预算仍null。

Owner仍需决定真实p/单位/劳动激励、RP/外层经济停止和严格科学接受标准，及未来具体网格/科学运行的有限范围/预算。不要重问已定口径，不补默认值；科学事项不阻塞独立普通工程。

原20×20×2定义锁定，实际grid hash/artifact、strict reference/thresholds和15实际预算仍null；合成grid_metadata_identity不能替代实际身份。后端实现声明TRUE只代表代码存在；真实OS/worker资格、live_counts_enforced及全部科学资格FALSE，公开门继续拒绝。持久占位NOT_RUN_AUTHORITY，不是Owner许可/全局可信消费账本，禁止换目录续额度。1worker/120秒/2GiB与800根/100步等只是不完整未批准骨架。

scientific_acceptance、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。网格生成/HA/消费许可/新运行预算均未授予。

## 保护和发布

模型tracked/staged原干净，原7个untracked为6缓存+已消费execution_decision.json，原字节保持。模型源码、测试、计划、机器决定不推送；治理分支仅脱敏文档。main保持b7e595ceb1cd7ffb5adfbf54e2de4e65f01090a5，不合并治理线。历史PENDING_SYNC/旧SSH失败保留当时状态，本次API同步不重用旧失败额度。

TEMP31 7/7、Moll3/3、七入口1/1、工资/补录、旧无模型四项、V2环境1/1全部关闭，零自动重试；初始化3/10已用，余7仅原8格，不跨借。旧ISSUED/owner_approved文字不产生新授权。R12 STOP、R13未授权、WASM六路径STOP、保护重绑未授权及16义务不变。

历史dirty树HEAD/index/porcelain基线保持，本轮不重审重绑。不得reset/stash/clean、强推、main合并、删分支、移动缓存证据、公开LOCAL_ONLY载荷/完整私有路径或修改Desktop/CUA/全局配置。原始20261106交接卡作为历史保留，新恢复以本卡和最新Owner决定为准。
