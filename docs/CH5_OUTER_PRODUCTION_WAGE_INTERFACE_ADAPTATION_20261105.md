# 第五章O1：外部净工资载荷的纯接口适配

DATE=2026-11-05
OWNER_EXACT_STATEMENT=允许纯接口适配，数值算法与网格冻结（建议）
DECISION_ID=CH5_OWNER_PURE_NETWAGE_INTERFACE_20261105
STATUS=ENGINEERING_STRUCTURAL_INPUT_BRIDGE_COMPLETE__SCIENTIFIC_CONSUMER_STILL_CLOSED
MODEL_CODE_CANDIDATE=479c4f4f5777c64fe16529b3421b70b86e89a90f
MODEL_CODE_TREE=5b5d8049d4b8298d3fd3288135c25e48279b6183
CODE_PUBLICATION=LOCAL_ONLY_NOT_PUSHED

## 改动及边界

Owner明确允许纯外部净工资来源/类型接口适配，HJB/KFE全部数值算法及网格继续冻结。本轮依此实施O1的结构适配：复用既有PendingWageEnvelope和WageInvocationContext，新增实际数值载荷的读取适配，不另建stub框架，也不调用工资生产者。

新模块outer_production_wage_bridge.py只用标准库与既有证据元数据接口。它读取调用方明确提供的、已封存身份的UTF-8 JSON平坦工资数组，核对输出字节/大小/SHA256、上下文、省序、生成t→进入t+1、快照角色及有限严格正值域，形成独立ProductionWageRecord。保留工资原值，不重算公式、不再扣税/楔子、不裁剪或加epsilon。该编码是新接口的显式格式，不转换或覆盖旧科学证据以求兼容。

现有政策代码会重新构建Temp31NetWageInputs。因此本轮保留同一容器，在temp31_ha_taxfree_bootstrap.py中只增加新工资记录的类型注解、显式记录校验分支和对应来源准入分支；HJB、policy、economics、初始化、KFE、汇总和网格文件均未改。旧Temp31EffectiveWageRecord、首轮19初猜、旧SOURCE_COMMIT及合成后轮语义保持。

**结构适配完成不等于真实生产放行。** 新记录沿用原pending证据的producer_invocation_verified=FALSE、consumer_ready=FALSE、model_activation=FALSE，另有scientific_acceptance=FALSE。既有输入容器可以构建并保留数值，但真正进入数值消费者时，仍调用原require_scientific_consumer_ready，当前以PRODUCER_INVOCATION_NOT_VERIFIED拒绝。没有新增可由ready布尔值开启的科学分支，没有把历史合成见证改为现场生产证明。

未来真实工资现场见证、输入/来源采纳及新的有限运行许可仍需在相应阶段建立；本次不签发这些资格。O1工程类型兼容已完成，O1真实运行兼容仍NOT_RUN。下一任务可准备O2多来源批次适配，实际HA调用继续关闭。

## 精确代码身份

| 路径 | Git Blob | 提交对象字节数 | SHA256 |
| --- | --- | ---: | --- |
| `src/ch5_two_asset_hank/multi_province/outer_production_wage_bridge.py` | `de789bb27d1c799059387929bf51a1e24453f690` | 5769 | `3038df68e147d9826649cdf16b4f0ea5cba2de5251b6054ed68e245fcbdc06ad` |
| `src/ch5_two_asset_hank/multi_province/temp31_ha_taxfree_bootstrap.py` | `822dbcef7226ed512cfc9f68d2aa3169a72b7c82` | 11950 | `2e75ef2f2473627a28162cc2a32fe7f65499d120934d3aba6ffa4c7f6bf9e0a3` |
| `tests/test_outer_production_wage_bridge.py` | `d5438e643fc6f2bd1a083fd43f77ded6d62fe49f` | 9814 | `f3705495cbf597f65d8a255a29542e56d5aeeaac15142042679c55ee773cc9bd` |

代码只在模型分支本地保存。公共GitHub治理分支只接收本说明及相关当前入口，不推上述代码或测试。

## 验证与审查

- TDD先记录缺模块导致的setup错误，tests_run=0，随后实现；未把这个失败写成测试通过。
- 最终15项限定检查通过，失败/错误/跳过0。覆盖原值保留、既有输入容器及政策重建兼容、旧首轮和旧来源校验、省序/快照/期次、字节身份、错误形状、非正/非有限/布尔/字符串载荷、资格伪造及缓存值篡改；2/3/31标签仅为工程夹具。
- 运行剖面拒绝原工资函数、初始化、HJB/KFE/policy/economics、汇总等数值函数进入，最终记录实际科学函数进入0。仅加载隔离的接口/元数据模块及现有NumPy/SciPy依赖，没有执行公共包入口、安装升级依赖或运行真实数据。
- 定点变异检查将新模块的正工资条件放宽到允许零，负例真实失败；随后恢复新模块原字节。失败记录独立保留。
- AST核对：移除声明的新增导入/记录分支及恢复类型注解后，共享原模块的完整AST与改动前精确一致；原数值定义改动0、网格改动0。原单来源worker、监督器、观察器、账本和旧pins均未改。
- 主代理完成工程自审，不冒称独立科学评议。未运行全科学测试套件、旧S01—S03、Moll参考或任何模型。

旧运行器的固定pins原样保留；不得用旧claim运行本轮新接口代码，也不修改旧清单来让新代码冒充历史来源。接口版本的来源身份已在本地新提交中独立登记，未来运行需绑定适用的新身份。

工程检查生成的6个未跟踪Python缓存留在原处，不暂存、不移动、不删除；它们不是模型结果或公开交付内容。模型树的已跟踪改动均通过明确路径提交，最终状态与回执区分这些缓存，不误报整树干净。

## 状态与下一步

ENGINEERING_INTERFACE_CHECKS=15_PASS
REAL_PRODUCER_CALLS=0
INITIALIZER_HJB_KFE_POLICY_AGGREGATE_CALLS=0
NUMERICAL_HA_ALGORITHM_EDITS=0
GRID_EDITS=0
NEW_SCIENTIFIC_GRANTS=0
SUBAGENTS=0
REAL_PRODUCTION_CONSUMER_READY=FALSE

TEMP31原7/7、Moll3/3及工资/补录旧额度保持关闭，旧初始化余量不跨用。严格reference/thresholds仍null，科学接受、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation及REAL_GE仍FALSE；R12/R13/WASM/保护重绑定和16项义务保持。只对已批准的外部来源/类型校验作窄例外，HA数值黑箱冻结不变。

[主路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)与[外层接线方案](CH5_OUTER_PRODUCTION_CHAIN_GAPS_AND_MINIMAL_CLOSURE_PLAN_20261105.md)已对齐本次Owner答复；[任务清单](../tasks/todo.md)区分O1工程完成与真实生产未运行。本轮保存后不自动进入O2或新科学调用。
