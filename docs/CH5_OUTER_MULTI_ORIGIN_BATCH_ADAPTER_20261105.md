# 第五章O2：多来源家户批次适配工程

DATE=2026-11-05
OWNER_EXACT_STATEMENT=可以请继续
ACTIVE_RESEARCH_MAINLINE=PYTHON_MULTI_PROVINCE_HANK_OUTER_CLOSURE
STATUS=ENGINEERING_PRECOMPUTED_BATCH_ADAPTER_COMPLETE__REAL_HA_AND_SCIENTIFIC_CONSUMPTION_NOT_RUN
MODEL_CODE_CANDIDATE=23d8ac8fe622d604f89dece6585769a969d16d9a
MODEL_CODE_TREE=2adeb8af7e5cff5f0ea9cbbc6ab0eba50e56f392
CODE_PUBLICATION=LOCAL_ONLY_NOT_PUSHED

## 交付及边界

新增outer_ha_batch_adapter.py和对应行为测试，仅接收明确提供的进入轮快照、工资记录和逐来源预计算回复，无求解器callback、科学函数dispatch或文件读写分支。没有更改既有源码、HA算法/网格、O1来源校验、原worker、监督器、观察器或账本。

本轮复用BindingContext绑定快照/省序/进入期次/源码集合和固定网格标签，复用O1的Temp31NetWageInputs承接原值净工资和价格，最终复用PreFrozenHouseholdOutputBatch承接Ct、家户Lt、At、Bt、AtTax及原收敛标记；没有创建一套替代HA或重复stub授权框架。

## 输入、组装和拒绝行为

| 接口/环节 | 已实现的工程行为 | 没有由此建立的事实 |
| --- | --- | --- |
| prepare_household_batch | 对调用方提供的UTF-8 JSON进入轮快照核对原字节SHA256、省序和必需字段；将各来源rah/rb/Tt/rb_gap及既有工资记录绑定到原输入容器 | 不加载真实数据，不构造HA网格，不生成或校准新价格 |
| 工资和期次 | 首轮仅沿原19数值初猜分支；后轮接受O1结构记录并校验上下文、省序、进入期次及源码集合标签，拒绝旧合成后轮改标签进入 | 工资生成t的快照与进入t+1的快照是两个身份，分别绑定，不要求两者哈希相同；没有证明生产者在现场运行 |
| 同次输入 | 每个预给定回复必须引用该批次对应request，初始化/HJB的输入声明必须是同一个既有输入对象；重新构造的等值对象也拒绝 | 这是回复声明的对象身份校验，不是实际初始化或HJB消费过该对象的执行证明 |
| assemble_household_batch | 同一批次必须包含完整、唯一且按既定省序排列的回复；同时检查原converged=True、返回网格标签和原未乘人口单位标签 | 不设置任何新HJB/KFE精度阈值，网格标签相等也不是实际网格内容未变的科学认证 |
| 原值输出 | Ct/Lt/At/Bt/AtTax只作有限实数输入校验和复制，保留负Bt；由已有批次类型执行其既有数值域约束 | 不计算AtTax，不重乘人口/生产率，不再扣税或迁移楔子，不裁剪或重新归一化HA输出 |
| 失败处理 | 缺来源、重复/错序、跨批次、输入替换、错误单位/网格、非有限或非收敛回复均拒绝；所有回复校验完成后才构造完整输出 | 不持久化部分批次，无自动补来源、重试、调用HA或修正失败输出 |

PreparedHouseholdBatch和AssembledHouseholdBatch始终标注PRECOMPUTED_BATCH_ROUTING_ONLY_NOT_HA_EXECUTION_OR_ACCEPTANCE，consumer_ready、real_execution_enabled、formal_ha_accepted均FALSE。批次中的converged仅搬运预给定的原标记，不升级为HA接受或Results。O1的科学消费门仍以PRODUCER_INVOCATION_NOT_VERIFIED拒绝未见证来源。

## 限定检查与审查

最终35项限定检查通过：20项O2新增检查，加15项与本次复用相关的O1回归；失败、错误、跳过0。2/3/31来源均为工程标签和预给定数据，不是实际省份运行、HA样本或新数值实验。没有重跑旧S01—S03、Moll、资产盘点或全科学测试套件。

检查覆盖：初猜与后轮原值、工资生成/进入快照区分、完整性/省序、同一输入对象、快照/价格/来源/期次、单位/网格标签、末来源失败后无部分批次、负Bt和NumPy实数返回保留、只读输出、无callback及原科学消费门保持关闭。

TDD的首次缺模块setup错误、首次监视器误将数据类定义识别为科学调用，以及审查中“标签对象触发自定义相等比较”的真实失败均保留。监视器只修正函数/类定义的分类，标签问题只修正新适配器的类型检查；没有改模型数值代码。最终运行剖面记录原工资、HA及外层经济核函数进入0。

定点变异将新适配器的原收敛标记检查放宽，允许末来源失败的测试真实失败；随后恢复新文件原字节。主代理完成工程自审，不冒称外部独立科学审查。

工程检查均禁写bytecode：前轮6个既存未跟踪缓存逐件字节数/SHA256保持，新增缓存0，不清理、移动或暂存缓存。既有5个复用源码的字节身份保持；Git变更范围仅两份新代码/测试及本轮治理文档。

## 本地代码身份

| 路径 | Git Blob | 提交对象字节数 | SHA256 |
| --- | --- | ---: | --- |
| `src/ch5_two_asset_hank/multi_province/outer_ha_batch_adapter.py` | `b6ea1952fa80ea3d9ab370220bbf46d64d752698` | 10537 | `c1539c1da075d980fc8699833cf3cf34dfab9ca10ae5f014f3b631ccc674e741` |
| `tests/test_outer_ha_batch_adapter.py` | `3f9f51d92f11246ad0916433ef8614334c2f47c8` | 13241 | `1bb43ed19668133326f349204ef1441aa0891e759dd07f1d159511e9061e59e0` |

代码及测试仅本地模型分支，公共治理分支仅同步本报告及入口文档。原科学模块及旧证据/pins不被更新成新代码的历史证明。

## 下一步：O3外层劳动/财政合同先讨论

O2工程适配完成，真实多来源HA批次、真实工资现场见证和实际生产消费仍NOT_RUN，旧有限预算不重开。下一目标是先明确O3的外部经济口径，再接工作地税的一轮组合：

1. 企业劳动L采用工作地税修正后的原量式重构，还是采用HA已返回家户劳动并按来源地总量归一化分配。两种候选均已存在，当前不按代码存在自动选择，也不改HA黑箱。
2. 企业工资税收入采用现行Lt×tau，还是在明确工资和劳动单位后采用tau×wjt×Lt。后者目前仅为条件诊断，不能静默写入Govinc。

上述问题的现状和精确源码路径见[外层接线方案](CH5_OUTER_PRODUCTION_CHAIN_GAPS_AND_MINIMAL_CLOSURE_PLAN_20261105.md)。均衡/校准目标及原Zt/GovInv自适应的选择仍在后续O4确定；本轮不替Owner作经济制度决定。

ENGINEERING_CHECKS=35_PASS__20_NEW_AND15_RELEVANT_REGRESSION
EXISTING_SOURCE_EDITS=0
NUMERICAL_HA_ALGORITHM_EDITS=0
GRID_EDITS=0
ACTUAL_WAGE_HA_OUTER_KERNEL_CALLS=0
NEW_SCIENTIFIC_GRANTS=0
SUBAGENTS=0

TEMP31原7/7、Moll3/3、工资/补录关闭及原初始化余额范围不变。严格reference/thresholds仍null；科学接受、consumer_ready、formal_ha_accepted、FORMAL_SOURCE_FREEZE、Results、model_activation及REAL_GE保持FALSE。R12/R13/WASM、保护重绑定、16项义务及历史dirty树/原件/证据保护保持。

[主路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)、[O1记录](CH5_OUTER_PRODUCTION_WAGE_INTERFACE_ADAPTATION_20261105.md)、[任务清单](../tasks/todo.md)相互衔接。本轮文档交付后不自动实现O3或启动科学运行。
