# TEMP V010 资源门禁与累计账本修复任务

TASK_ID = TEMP_V010_RESOURCE_GATE_REPAIR_20261018
STATUS_AT_ISSUE = ISSUED_NOT_STARTED
SCOPE = ENGINEERING_ONLY / NO_SCIENCE / NO_HA

## 1. Owner authorization and purpose

Owner于2026-10-18明确同意继续，并允许适度放宽Python线程/工程资源约束。本任务只处理TEMP_V010_HA_BLACKBOX_SIMPLE_PRICE_TUNING_100结果中已确认的资源门禁缺陷与待核账本差异；不续跑、不恢复、不补算原TEMP科学实验。

本任务不修改正式V010科学合同、经济方程、HA/HJB/KFE、selector、参数、收敛阈值或任何正式模型源文件。不得调用HA/HJB/KFE/selector/root solver；真实科学调用预算严格为0。不得启动A1/A2/A3，不得恢复旧预算。V011仍NOT_STARTED，model_activation=False，REAL_GE=False，Results FALSE。

## 2. Fixed source and prior failure

失败候选：
- Commit: fb1456fa1be9b547d81e93bdf52912089df664db
- Tree: 21210ad94d9ec9600325fcd921c0f94c31cbcc51
- Parent/task issue: 6d07cdf1a565376927bd64997780ad77669d9390
- Review path: _review_tmp/ch5/temp-blackbox-price-tuning-100-20261018/
- Report: result.md; manifest.json; evidence_sanitized.zip

已确认的首要问题：ENGINEERING纯Python/focused pytest启动子上限为24，实际至少创建29个Python进程，P0却误释放科学阶段。总工程进程未超192不能豁免子上限。原科学driver已停止，不能恢复。

另有待核对差异：manifest打包前 ENGINEERING=37、SCIENCE=1、DELIVERY=32、GLOBAL=70；最终回执 ENGINEERING=35、SCIENCE=1、DELIVERY=48、GLOBAL=84。DELIVERY/GLOBAL后续增加可以由打包、push、readback等解释；ENGINEERING 37→35在同一累计口径下不单调。不得推断造假；须根据原始记录判断是否为计费归属/定义差异或记录缺陷。缺少原始证据时保持 UNKNOWN。

## 3. Budget and permitted relaxation

本任务只授权工程验证和外围执行器/账本修复，不授权科学执行或真实远端发布。只可在通过V1.3 BOOTSTRAP 0/1/2的全新独立scratch内写入；禁止触写正式模型树、既有8 dirty/index/external common-dir、旧scratch、旧失败原件和C盘独立SSD备份。

- ENGINEERING全部真实子进程及后代累计硬上限：192。
- Python/focused pytest启动次数硬上限：48（本次新任务明确放宽此前24的子上限）；计数必须在创建前强制执行，不得创建第49个再报超限。
- 同时活动的Python进程最多8个；如果使用工作线程，跨所有Python进程的活动工作线程合计最多64个。线程数不得代替进程数，进程数不得代替线程数；两类分别记录。
- 主动工程时间最多3小时；工程修复/验证批次最多8；新增非Git字节最多512 MiB；独立Git对象库合计最多2 GiB。RSS不可观测则明示UNKNOWN，不伪造。
- 本任务不运行Git fetch/push，不创建远端review分支，不清理任何远端或本地旧审阅材料；不得把预算借给DELIVERY或SCIENCE。
- 资源门禁必须保留明确硬停止。放宽额度只改变上限，不放宽计数完整性、写前身份、STOP传播和证据保存。

任何资源累计来源或域归属无法重建时，不启动额外测试，报告UNKNOWN并停止。任务预算关闭后不结转。

## 4. Work packages

### WP1 — Read-only evidence reconciliation

只读检查固定候选中的result.md、manifest.json、final receipt原文（如用户/本地Codex能提供准确原字节）、相关kernel_processes记录和PREPUBLICATION_COUNTS。建立每域/全局计数时间线，区分：
- 内核可证明的累计数；
- 工具观察的接收/前期进程；
- 域内归属及迁移；
- 打包前计数与最终计数；
- 原始证据缺失导致的UNKNOWN。

不从Base64摘要或二手文字重建未提供的本机原证；不把新任务观察追认成旧执行事实。

### WP2 — Hard gate repair

在独立scratch内修复/实现资源调度门禁：
1. 所有子进程启动必须先保留并原子消费相应域及全局配额；
2. Python/focused启动第49次前必须拒绝，不允许先创建后计数；
3. 同时活动Python进程和线程分别设限；
4. 子进程、短寿命后代、启动失败与被拒绝的创建尝试分开记账；同一真实进程不得跨域重复计数；
5. P0工程通过不得自动释放科学，除非资源账本、写前身份与所有硬门均真实PASS，且当前任务明确含科学授权。本任务没有科学授权，因此永远不得释放solver；
6. STOP在append/checkpoint/计数任一步异常后必须在下一潜在调用前生效；
7. 保留首次失败原字节和单向链接，不覆盖、不回写历史失败证据。

### WP3 — Synthetic adversarial tests only

只允许无HA的人工/dummy测试。至少验证：
- 第48次Python启动可按预算处理，第49次在创建前被拒；
- 并发Python进程第9个被拒；
- 跨进程工作线程第65个被拒；
- 工程总后代第193个被拒；
- 域累计计数不能倒退；若账本口径发生变化，必须记录显式、可审计的归属事件，不可静默减计数；
- 启动失败、创建被拒、短寿命后代、工具观察进程不会混淆；
- append/checkpoint失败、损坏/缺seq、STOP后dummy调用次数均为0；
- 每个测试均不导入或调用HA/HJB/KFE/selector/root solver。

若当前Windows内核/Job原证无法独立复核，只能报告CODEX_REPORTED或UNKNOWN，不宣称Astra已认证OS事实。

### WP4 — One compact delivery

只交付一次集中结果：task/run身份、sourceIndex（不明则UNKNOWN）、输入文件固定SHA、首次失败、修复范围、各测试分母/通过/失败/UNKNOWN、逐域资源实际消耗、原证与脱敏派生关系、未解决差异、最终STOP。保留本任务原始证据和脱敏交付分开。由于本任务明确不授权网络发布，不得push；提供可核验的本地交付位置和SHA，若原件路径不可由Astra读取必须如实注明。

## 5. Acceptance

PASS仅表示本任务的无科学资源门禁工程修复在本地合成测试范围内通过；不代表上一轮P0工程PASS、不追认先前超限、不认证Windows原生完整Runner I/O、不恢复TEMP科学实验。

失败/UNKNOWN：FAIL_CLOSED / STOP。不得自动签发或启动下一轮HA实验。

Final status must preserve:
- prior TEMP result = FAIL_CLOSED_SHARED_RESOURCE_PRECONDITION;
- original review candidate and bytes retained;
- current task scientific calls = 0;
- formal V010 unchanged;
- model_activation=False; REAL_GE=False; Results FALSE; V011 NOT_STARTED;
- FULL_RUNNER_IO_CLOSURE remains BLOCKED unless independently proven otherwise.
