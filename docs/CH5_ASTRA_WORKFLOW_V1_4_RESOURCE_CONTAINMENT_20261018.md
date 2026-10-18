# 第五章 V1.4：资源门禁真实性、同步闭环与一次性DOC_ONLY同步

**批准依据：** Owner于2026-10-18明确要求分析并优化当前工作流、让Codex同步一次；本文件只收敛执行器与文档同步流程，不授权科学运行。
**适用范围：** 后续新冻结任务及本次一次性文档同步。既有失败任务不追认、不重开。
**前序政策：** V1.3仍保留为历史规则；本V1.4仅补充和覆盖资源计数/真实OS约束、当前状态同步与本地Source同步的相关条款。
**科学权限：** HA黑箱原则不变。当前不授权HA/HJB/KFE/selector/root solver，正式V010不改，V011未启动，Results FALSE。

## 1. 2026-10-18资源门禁失败的正式定性

任务 `TEMP_V010_RESOURCE_GATE_REPAIR_20261018`（run_id `977d18ebe6e14a91bb049924cae715e4`）最终为：

`FAIL_CLOSED_UNRESERVED_REAL_DESCENDANT / STOP`

确认的证据等级：
- 旧账本差异已在本次原件内对齐：prepublication ENGINEERING 37 = kernel-only 35 + 2 tool-observed intake processes；统一口径35→35，保守口径37→37。92份历史原件SHA未变；历史OS独立复算仍UNKNOWN/NOT_PERFORMED。
- V2合成测试报告28/28通过，但边界项使用synthetic ledger/callback，不能证明Windows内核会在真实创建前阻止进程。
- 真实Windows dummy第二个nested bundle预留2个进程，Job终态累计3个，触发E2并STOP。两个退出后代身份/PID未取得原始证明，保持UNKNOWN；实际Python总数也保持UNKNOWN。
- 真实测试计划6项：1通过、1失败、4未运行。真实失败后没有继续修复或测试。
- 科学调用0、Git fetch/push 0、正式模型写入0。完整Windows Runner I/O仍BLOCKED。

这是一项资源门禁工程失败，不是HA黑箱失败，不是科学结果，也不授权继续科学。

## 2. 核心技术修正：预留账本不等于OS执行约束

必须在所有任务和报告中区分以下概念：
1. **Reservation ledger**：应用程序自己的预留/配额记录。
2. **Native creation control**：操作系统在进程创建前实际执行的拒绝机制。
3. **Job accounting**：Windows Job的TotalProcesses/ActiveProcesses等观测值。
4. **Post-hoc detector**：进程创建后或轮询时才发现累计数超出预期。
5. **Synthetic callback**：人工测试账本，不是真实OS控制证据。

禁止将第1项或第4/5项描述为第2项。

Windows Job的ActiveProcessLimit限制的是同时活动进程数，不是整个Job生命周期累计创建数。轮询TotalProcesses只能发现累计数不符，不能撤销已经发生的越界。因此：
- 任何声称“在创建前硬拒绝”的累计进程预算，必须有实际约束创建入口的控制路径及其原始OS证据。
- 不允许任意dummy在受控Job内创建不经gate授权的后代，再把事后检测称作预防。
- 后续资源门禁回归优先使用单一直接子进程、单进程Job（ActiveProcessLimit=1）、创建时CREATE_SUSPENDED、分配Job并核验后再Resume；测试程序不得派生子进程。
- 若必须测试后代行为，必须明确标记为OS负例/containment test，使用独立Job并证明OS在第二个同时活动进程创建前拒绝。不得把该测试用于证明任意深度、任意时序后代的累计创建总数可以由轮询硬限制。
- 如果未来业务必须支持子进程树，必须先设计可控的统一launcher/worker协议或真正限制进程创建能力的隔离机制，并独立验收；不得仅提高预留数或轮询频率。

## 3. 账本语义和STOP规则

所有实现分别维护并输出：
- 累计process reservations；
- 每次创建前的reservation ID/lease；
- 每个lease的实际直接创建与完成状态；
- Windows Job TotalProcesses与ActiveProcesses；
- Python启动预留/确认/活动数；
- worker-thread预留/活动数；
- 工具观察进程（非kernel证据）；
- 启动失败、被拒绝、已退出后代、身份UNKNOWN。

同一进程不得重复计费；已创建累计数不可因reap而减少，活动数可在确认退出后减少。口径迁移必须是显式审计事件，不得静默把累计数调低。

单次lease须绑定一个具体gate、task/run、域、配额及允许的创建操作，单次消费。通用Created(n)账本增量不能替代对单个lease实际消费量的校验。发现OS计数与预留不一致、进程身份未知、append/checkpoint失信或STOP传播异常时，立即E2 STOP；停止后不得继续测试或调用backend。不得为了修复失败而在同一停止链中反复重启controller。

## 4. 测试证据分层

每份测试报告须分别列出：
- Synthetic：分母、结果与callback实现；只证明逻辑用例。
- Real Windows：实际创建方式、job limits、原始kernel counters、PID/parent/exit identity、reservation与实际创建的逐项映射。
- Unknown/Not Run：明确原因；不得折算为通过。
- 首错和修复前版本原字节必须保留；后续修复使用新attempt，不能覆盖首次失败。
- 对无法读取/上传的本机原件只标CODEX_REPORTED/UNKNOWN；不得宣称Astra独立复算。

最终回执必须可从上传的原始文件独立验证长度和SHA。ZIP manifest必须准确声明其登记范围（例如529个登记成员与530个实际成员必须有明确的额外成员说明）；所有成员校验通过不自动证明未登记成员合规。最终回执若不在上传材料中，明确列为未复核，不要求从摘要重建原件。

## 5. Codex/GitHub/GPT Project Sources三平面同步

必须区分三个独立同步面：
A. GitHub治理源（CURRENT/TASK_CURRENT/工作流政策/任务合同）；
B. 本地Codex项目目录、AGENTS/任务入口/镜像文档；
C. ChatGPT Project Sources离线文件。

更新A不代表B已同步；更新B不代表C已更新；GPT Project Sources必须由Owner手动上传正式Source更新包。任何同步都必须报告各文件的来源commit/blob或本地SHA、目标路径和回读SHA。没有回执不能宣称同步完成。

每次工作流变更最多发起一张DOC_ONLY同步任务，执行一次集中批量同步：
1. 只读恢复GitHub当前治理HEAD、CURRENT/TASK_CURRENT、动态目录、工作流正文及本次失败报告。
2. 对照本地Codex规则入口，明确新增/更新/未更新/冲突，不猜测不存在的文件。
3. 仅在独立文档镜像及合同白名单内同步；先通过V1.3 BOOTSTRAP 0/1/2，保护原worktree/index/common-dir/旧scratch/备份。
4. 不运行测试、不调用模型、不启动Python/C# runner、不fetch/push、不清理review目录。
5. 一次交付差异表、每个目标文件SHA256、前后读回证据、冲突及UNKNOWN；发现保护路径不明立即STOP。
6. Owner手动上传同一包至GPT Project Sources后，后续GPT会话才能以新Source为导航；不宣称平台Memory自动更新。

## 6. 本次DOC_ONLY同步的验收边界

唯一任务：
`CH5_V14_ONE_TIME_CODEX_DOC_SYNC_20261018`

范围：只读核对当前治理源；同步本地项目文档镜像中的工作流入口/索引/当前状态；记录真实差异。不得执行TEMP修复、不得重跑28项或真实dummy测试、不得启动科学实验。

若本地源目录/文件白名单或写前身份不能确认，改为只读报告并STOP，不创建scratch或文件。工程/科学/交付预算均不得从旧任务继承。

最终状态要求：
- `TEMP_V010_RESOURCE_GATE_REPAIR_20261018=FAIL_CLOSED_UNRESERVED_REAL_DESCENDANT`
- `ACTIVE_RESEARCH_TASK=NONE`
- `ACTIVE_SCIENCE_TASK=NONE`
- `model_activation=False`
- `REAL_GE=False`
- `Results=FALSE`
- `V011=NOT_STARTED`
- `FULL_RUNNER_IO_CLOSURE=BLOCKED`
- `NEXT=WAIT_OWNER_NEW_TASK_AFTER_DOC_SYNC`

V1.4本身不授权任何新工程修复或科学任务。
