# CH5动态总目录 · V1.9路径分类器合成修复任务

## 当前唯一任务

- [CURRENT.md](../CURRENT.md)：当前许可与状态。
- [TASK_CURRENT.md](../TASK_CURRENT.md)：当前唯一任务。
- [V1.9 URI/文件路径/JSON转义分类器规则](CH5_ASTRA_WORKFLOW_V1_9_REVIEW_PATH_CLASSIFIER_20261018.md)。
- [V1.9合成-only固定任务](../tasks/CH5_REVIEW_PATH_CLASSIFIER_V19_SYNTHETIC_ONLY_20261018.md)。
- [V1.8来源身份溯源](CH5_ASTRA_WORKFLOW_V1_8_SOURCE_IDENTITY_PROVENANCE_20261018.md)；[V1.7交付闭环](CH5_ASTRA_WORKFLOW_V1_7_DELIVERY_CLOSURE_20261018.md)。

Delivery V2 run_id=447f9775e1b5482f9e3add9344742017已STOP，17/491成员审查、474未审，完整ZIP安全性UNKNOWN。新任务只处理合成分类器，不访问旧ZIP、不发布网络、不运行runner或科学模型。旧Delivery V2保持关闭。

正式V010不变；V011 NOT_STARTED；model_activation=False；REAL_GE=False；Results FALSE；FULL_RUNNER_IO_CLOSURE BLOCKED。

---

# CH5动态总目录 · V1.8来源身份溯源与Delivery V2

## 当前唯一任务

- [CURRENT.md](../CURRENT.md)：当前许可与状态。
- [TASK_CURRENT.md](../TASK_CURRENT.md)：当前唯一任务。
- [V1.8来源证据身份与预期值溯源](CH5_ASTRA_WORKFLOW_V1_8_SOURCE_IDENTITY_PROVENANCE_20261018.md)。
- [V1.7交付闭环规则](CH5_ASTRA_WORKFLOW_V1_7_DELIVERY_CLOSURE_20261018.md)。
- [Delivery Recovery V2固定合同](../tasks/TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_V2_20261018.md)。

上一交付任务在SOURCE_FINAL_RECEIPT_IDENTITY停止，因为本地校验器添加了65字符、未在合同中冻结的手抄预期SHA。不得将其定性为源文件修改。V1.8要求预期值有明确来源；新V2合同已冻结ZIP、manifest、FINAL_RECEIPT三个来源身份及预算。新任务只审查/交付已有证据，禁止测试、runner或科学重跑。

科学调用0；正式V010不变；V011 NOT_STARTED；Results FALSE；FULL_RUNNER_IO_CLOSURE BLOCKED。

---

# CH5动态总目录 · V1.7交付闭环与V3证据补交

## 当前唯一任务

- [CURRENT.md](../CURRENT.md)：当前许可与状态。
- [TASK_CURRENT.md](../TASK_CURRENT.md)：当前唯一任务登记。
- [V1.7交付闭环规则](CH5_ASTRA_WORKFLOW_V1_7_DELIVERY_CLOSURE_20261018.md)：分离SCIENCE/ENGINEERING/DELIVERY预算；明确远端临时审阅、fake-bare预检、原字节核验、先归档后清理。
- [V3既有证据补交任务](../tasks/TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_20261018.md)：只交付run_id=33f2b49ddc274e868956f6480d5f3a3a的既有证据，不重跑测试、runner或模型。
- [来源V3工程合同](../experiments/TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_20261018/ENGINEERING_CONTRACT.md)：其禁止网络发布的限制保持不变；新的delivery-only任务不追溯修改它。

当前来源工程结果为PASS_BOUNDED_ADAPTER_INTEGRATION_LOCAL，Astra独立验收仍PENDING。delivery任务尚未开始，不能声称远端材料已发布。正式V010不变；V011 NOT_STARTED；model_activation=False；REAL_GE=False；Results FALSE；FULL_RUNNER_IO_CLOSURE BLOCKED。

---

# CH5动态总目录 · V1.6保护路径边界与Adapter V3

## 当前唯一任务

- [CURRENT.md](../CURRENT.md)：当前许可状态。
- [TASK_CURRENT.md](../TASK_CURRENT.md)：当前唯一任务。
- [V1.6保护路径边界与PATH_ALIAS分类](CH5_ASTRA_WORKFLOW_V1_6_PROTECTED_PATH_BOUNDARIES_20261018.md)。
- [V1.5不可变任务身份与启动校验](CH5_ASTRA_WORKFLOW_V1_5_IMMUTABLE_TASK_IDENTITY_20261018.md)。
- [V1.4资源门禁真实性与三平面同步](CH5_ASTRA_WORKFLOW_V1_4_RESOURCE_CONTAINMENT_20261018.md)。
- [Adapter Integration V3固定合同](../experiments/TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_20261018/ENGINEERING_CONTRACT.md)。

**最新失败：** Adapter V2在BOOTSTRAP 0因递归枚举中的node_modules依赖文件触发PATH_ALIAS而停止；最终路径未解析，相关性UNKNOWN。V1.6现要求保护根边界核验与目标路径解析分离，不再因无关依赖条目自动拒绝整个任务；无法证明无关则仍STOP。

当前仅允许Adapter V3工程集成；科学调用0；正式V010不变；V011 NOT_STARTED；Results FALSE；FULL_RUNNER_IO_CLOSURE BLOCKED。

---

# CH5动态总目录 · V1.5不可变任务身份与Adapter V2

## 当前唯一任务

- [CURRENT.md](../CURRENT.md)：当前许可状态。
- [TASK_CURRENT.md](../TASK_CURRENT.md)：当前唯一任务。
- [V1.5不可变任务身份与启动校验](CH5_ASTRA_WORKFLOW_V1_5_IMMUTABLE_TASK_IDENTITY_20261018.md)。
- [V1.4资源门禁真实性与三平面同步](CH5_ASTRA_WORKFLOW_V1_4_RESOURCE_CONTAINMENT_20261018.md)。
- [Adapter Integration V2固定合同](../experiments/TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V2_20261018/ENGINEERING_CONTRACT.md)。

**当前状态：** 前一Adapter任务因本地组装校验文本替换了历史V3身份而在BOOTSTRAP 0停止；该任务未实施、未创建工件，现已SUPERSEDED_NOT_STARTED。新V2合同不含自身发行身份，身份元数据仅放在CURRENT/TASK_CURRENT。必须原样读取固定合同，不得重写正文进行校验。

科学调用0；正式V010不变；V011 NOT_STARTED；Results FALSE；FULL_RUNNER_IO_CLOSURE BLOCKED。当前任务仅限ResourceGate窄adapter集成；不得恢复旧TEMP科学运行。

---

# CH5动态总目录 · V1.4资源门禁与Codex同步

## 当前唯一任务：一次性DOC_ONLY同步

- [CURRENT.md](../CURRENT.md)：当前许可状态。
- [TASK_CURRENT.md](../TASK_CURRENT.md)：当前唯一任务。
- [V1.4资源门禁真实性与同步闭环](CH5_ASTRA_WORKFLOW_V1_4_RESOURCE_CONTAINMENT_20261018.md)。
- [V1.4一次性Codex文档同步合同](../versions/0.0.10/ch5_v14_one_time_codex_doc_sync_task_20261018.md)。

**当前状态：** 上一资源修复任务 `TEMP_V010_RESOURCE_GATE_REPAIR_20261018` 已 `FAIL_CLOSED_UNRESERVED_REAL_DESCENDANT / STOP`。28/28 synthetic通过不等于真实Windows Job门禁通过；预留2、Job累计3触发E2。科学调用0、Git fetch/push 0。旧账本按同口径已对齐kernel-only ENGINEERING 35→35、保守37→37；两个退出后代身份与实际Python总数仍UNKNOWN。

**本次只允许一次DOC_ONLY本地Codex文档同步。** 不测试、不启动runner、不运行科学模型、不改正式模型、不执行Git fetch/push、不清理旧审阅目录。Owner必须手动上传Project Source更新包；GitHub发布不代表Codex本地或ChatGPT Sources已同步。

**正式科学状态：** V010不变；V011 NOT_STARTED；model_activation=False；REAL_GE=False；Results FALSE；FULL_RUNNER_IO_CLOSURE=BLOCKED。

---


## 最新权威：TEMP失败封存，不重跑科学；仅工程门禁修复

最新任务：[TEMP_V010_RESOURCE_GATE_REPAIR_20261018 固定合同](../experiments/TEMP_V010_RESOURCE_GATE_REPAIR_20261018/ENGINEERING_CONTRACT.md)。发行提交：2ba4a716ebde395a7f659729513e725e0d8d1f07；任务Blob：e817ce5737ba8c2a189122e4d0bb08cd4f85ef7c。

[CURRENT.md](../CURRENT.md) 与 [TASK_CURRENT.md](../TASK_CURRENT.md) 顶部为当前许可状态。当前唯一任务为 ENGINEERING_ONLY / NO_SCIENCE / NO_HA；Python/focused启动预算调整为48、并发Python进程8、跨进程活动线程64，工程总后代仍≤192。所有上限须在创建前强制执行，线程和进程分别计数。

前一实验结果 [TEMP_V010_HA_BLACKBOX_SIMPLE_PRICE_TUNING_100_RESULT](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/fb1456fa1be9b547d81e93bdf52912089df664db/_review_tmp/ch5/temp-blackbox-price-tuning-100-20261018/result.md) 已因至少29个Python进程超过原24子上限而 FAIL_CLOSED。原science driver已停止，A1不续跑、A2/A3不启动，旧预算不结转。manifest/最终回执 ENGINEERING计数差异待原证核对；无原证时保持UNKNOWN。

**本次新任务不授权HA/HJB/KFE/selector/root solver、正式V010修改、Git fetch/push或清理旧review候选。** 正式V010不变；V011 NOT_STARTED；model_activation=False；REAL_GE=False；Results FALSE；FULL_RUNNER_IO_CLOSURE=BLOCKED。

---

## 2026-10-18本会话新Owner决定：TEMP黑箱价格调参已签发、尚未执行

Owner在完成旧会话恢复后明确“可以，让我们继续TEMP的方向（HA黑箱+约束条件简单化 的调参）”。[新授权与精确身份](CH5_OWNER_TEMP_BLACKBOX_SIMPLE_PRICE_TUNING_100_AUTHORITY_20261018.md)；[新冻结长任务](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/6d07cdf1a565376927bd64997780ad77669d9390/experiments/TEMP_V010_HA_BLACKBOX_SIMPLE_PRICE_TUNING_100_20261018/EXPERIMENT_CONTRACT.md)。

**唯一ACTIVE_TASK=TEMP_V010_HA_BLACKBOX_SIMPLE_PRICE_TUNING_100_20261018；SCOPE=TEMP_SYNTHETIC_ONLY；STATUS=ISSUED_NOT_STARTED。** 发行Commit 6d07cdf1a565376927bd64997780ad77669d9390 / Tree 628677d32b773d7fd8cb9a4e9f906979d17067b5 / Blob 04af299d04f1e37243d8af806fb4a4e10eed0feb。先工程P0（账本/STOP/完整进程计数/fake-bare ZIP/价格stub），通过后同任务内自动A1→A2→A3串行、各≤100轮/200HA，总≤600；A0复用旧原件。HA黑箱不改，Bellman等只观察但源式收敛不伪造；只两条raw/used家庭价桥，不另扩参数网格。正式V010无活动任务/方法修改，Results FALSE、V011 NOT_STARTED。

工程、科学、交付独立新预算；旧STOP、旧0/2/2与12HA、旧至少26/24报告级异常及已完成清理均保留。以下旧ACTIVE/NEXT/NONE是当时历史，不能覆盖本次新任务，也不能恢复旧额度。当前许可只看CURRENT/TASK_CURRENT顶部与固定新合同。

## 前序记录（保留历史）

# CH5 动态总目录 · V010 CP2_F25独立机制取证终结，Owner科学决定待定

## 当前权威（2026-10-18交接，下面旧ACTIVE/NEXT均视作历史，不自动授权）
- [本会话全部Owner决定、TEMP黑箱、2×2科学E2、GitHub ZIP实际交付与26/24工程失败、远端清理和下一会话边界](CH5_SESSION_HANDOFF_20261018_AFTER_TEMP_HA_PRICE_BRIDGE_AND_GITHUB_ZIP_CLOSEOUT.md)。
- 当前实际：**RESEARCH ACTIVE_TASK=NONE；DELIVERY ACTIVE_TASK=NONE；ALL_BUDGETS_CLOSED；OWNER_NEW_TASK=NEXT_CONVERSATION_ONLY**。正式V010冻结，Results FALSE，V011 NOT_STARTED。上一纯交付任务已结束、临时审阅3/3清理成功。
- 本目录下文保留各历史任务发行/STOP及旧“当前”措辞作可溯源记录。**以CURRENT.md、TASK_CURRENT.md及上述本会话handoff的2026-10-18状态为准，不能从后文旧NEXT推导执行权。**

**2026-10-18 GitHub MD＋ZIP远端实证核验完成：** [独立交付审议](CH5_GITHUB_ZIP_PUBLISHER_DELIVERY_RESOURCE_EXCEPTION_INDEPENDENT_REVIEW_20261018.md)确认remote review HEAD `7623a4eb4680f0b4039f03dd245307ec791cea15`、唯一任务父 `2d9a3a5a3100fa82f24f125ce3264bb68c01c333`，远端仅三文件，完整ZIP196296B/29成员、SHA256与旧私有原证相符。Codex自报Git内部子进程**至少26/24，交付工程仍FAIL_CLOSED_RESOURCE_EXCEPTION**，不能因上传成功认定工程PASS。科学与交付活动任务均NONE、正式V010/Results不变；按既定授权永久审议回读后清理remote临时分支当前三文件，保留Git历史。


**2026-10-18最高优先交付状态：** [自动GitHub MD＋ZIP V2](CH5_GITHUB_AUTO_ZIP_REVIEW_DELIVERY_V2_20261018.md)已经签发；[TEMP2×2科学E2失败独立终审](CH5_TEMP_PRICE_BRIDGE_FACTORIAL_E2_LEDGER_TERMINAL_REVIEW_20261018.md)确认A1/A2/A3完成0/2/2、HA计费12，正式V010不变；**当前独立DELIVERY-only工程任务** [GitHub ZIP发布器修复及旧证据自动补交](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/2d9a3a5a3100fa82f24f125ce3264bb68c01c333/tasks/CH5_GITHUB_ZIP_PUBLISHER_REPAIR_DELIVERY_RECOVERY_20261018.md) 发行Commit 2d9a3a5a3100fa82f24f125ce3264bb68c01c333、Blob c0f020b6b11a6289d65aa0cbde734d415633037c。本任务只对既有脱敏result.md/manifest.json/evidence_sanitized.zip修Git argv与远端发布，science HA/HJB/KFE严格0，不复活旧预算。Owner以后不应每轮手动上传ZIP；正式研究 ACTIVE_TASK=NONE、Results FALSE、V011 NOT_STARTED。


**2026-10-18 Owner新临时数值实验已签发（正式V010仍ACTIVE_TASK=NONE）：** [2×2价格桥实验Owner科学授权](CH5_OWNER_TEMP_PRICE_BRIDGE_FACTORIAL_100_AUTHORITY_20261018.md)；[独立TEMP100轮冻结任务](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/2c855f616efbca05c29d4069a44e3c6651070b44/experiments/TEMP_V010_PRICE_BRIDGE_FACTORIAL_100_20261018/EXPERIMENT_CONTRACT.md)。A0旧raw/raw100轮不重跑，新A1 used/raw、A2 raw/used、A3 used/used各最多100轮，新science最多600 HA，严禁改原HA黑箱；进入HA前必须防止旧prepare重绑raw价；本任务与旧科学预算完全分开，正式V010数学合同不改、Results FALSE。

**2026-10-18 TEMP 100轮原始收益与价格桥机制源证：** [ra0长期越界/家户收益与工资输入同MATLAB的来源差异](CH5_TEMP_V010_RA_BOUNDARY_SOURCE_ONLY_FORENSIC_20261018.md)。两省100/100轮raw ra0>0.09（最低0.3733/0.4155），各26次GovInv×1.1；本轮家户rah沿raw ra0 same-S，w_eff沿wt0而非有界ra/wjt，现价桥与MATLAB源不等价。**这不是已证明的HA故障或替代实验收敛，也没有批准更改V010原模型；正式ACTIVE_TASK仍NONE、旧预算CLOSED。**

**2026-10-18新Owner交换规则与实验结果（不改变正式ACTIVE_TASK=NONE）：** [TEMP-V010 100轮独立证据终审](CH5_TEMP_V010_BLACKBOX_100_ROUNDS_INDEPENDENT_REVIEW_20261018.md)；[GitHub临时审阅支持脱敏MD＋ZIP](CH5_OWNER_REVIEW_MD_ZIP_TEMP_EXCHANGE_POLICY_20261018.md)。100轮两省未达原稳态门，HA200完整返回/201计费，ra触界100/100轮，原HA黑箱不变；正式V010/Results未接受。


**Owner 2026-10-17新方向（正式科学合同暂不改）：** [HA黑箱与100+轮隔离实验决定](CH5_OWNER_HA_BLACKBOX_TEMP_V010_EXPERIMENT_DECISION_20261017.md)；独立实验任务 [TEMP-V010 MATLAB-faithful HA黑箱](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/503b418f790d61049f3df9016a783dcecc793237/experiments/TEMP_V010_MATLAB_FAITHFUL_HA_BLACKBOX_100PLUS_20261017/EXPERIMENT_CONTRACT.md)。**正式ACTIVE_TASK仍NONE；独立TEMP实验按其实验分支授权，不解封旧V010科学预算。**

**RESEARCH_VERSION=V010/v0.0.10；ACTIVE_TASK=NONE；V011 NOT_STARTED。**
**LAST_TASK=V010_CP2F25_SELECTOR_MECHANISM_AND_CONDITIONAL_REPAIR_LONG_TASK；TERMINAL=V010_CP2F25__NO_MATH_PRESERVING_REPAIR_PROVEN__INDEPENDENT_LIMITED_ACCEPT__STOP；BUDGET_CLOSED。**
**NEXT=WAIT_OWNER_V010_JOINT_TRIGGER_SCIENTIFIC_DECISION / STOP**。

| 文件 | 当前authority |
|---|---|
| [CURRENT](../CURRENT.md)、[TASK_CURRENT](../TASK_CURRENT.md) | 唯一当前许可状态；不允许再执行selector/HJB/HA |
| [本轮F25独立科学终审](../versions/0.0.10/v010_cp2f25_selector_no_math_preserving_repair_independent_terminal_review_20261017.md) | 521/521私人ZIP、Owner采纳双侧合法Z规则、12候选独立复算、原selector一致/无patch、终态资源 |
| [本轮冻结CP2_F25长任务](../versions/0.0.10/v010_cp2f25_selector_mechanism_conditional_repair_long_task_20261017.md) | 历史发行commit 98b3154e84db62d4d319836db0a39e3278017c33 / Blob dfc29c2df0187875aee8d81b0ad6a23662e76a02；现已STOP |
| [上轮M1 B1科学FAIL_CLOSED主审](../versions/0.0.10/v010_m1_long_synthetic_b1_cp2_f25_independent_terminal_review_20261017.md) | 真实失败原件/旧预算已关闭 |
| [V010冻结plan](../versions/0.0.10/plan.md) | 经济与数值最高合同不变 |
| [版本登记](CH5_VERSION_REGISTER_CURRENT.md) | V010继续研究，但目前无数值求解许可，V011未启动 |
| [科学决定](../SCIENTIFIC_DECISIONS.md) | 2026-09-16/19原Z和联合严格触发Owner已采纳；无新E3规则修改 |
| [V1.3工作流](CH5_ASTRA_WORKFLOW_V1_3_20261017.md) | E1自主工程、E2/E3真实硬门、单长任务 |
| [知识入口](knowledge/CH5_WEB_KNOWLEDGE_CURRENT.md) | 最新终态优先于历史ACTIVE记录 |

本轮私有原证没有作为remote temp候选上传。Codex原SSH首次失败128，fetch/push0，Astra GitHub查询临时branch 404，无白名单临时文件可清。旧任务余量不可结转，不能直接改数学合同或启动新版HA。
