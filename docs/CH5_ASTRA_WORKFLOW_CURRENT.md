> **2026-10-23 Owner离线工作流优先覆盖**：当前默认改为冻结MD→本地Codex→脱敏外层ZIP→Owner手动上传→GPT独立验收；GitHub自动Issue/Review上传/清理已停用。正式规则见 [CH5_OFFLINE_WORKFLOW_AUTHORITY_CURRENT_20261023.md](CH5_OFFLINE_WORKFLOW_AUTHORITY_CURRENT_20261023.md)。本文件余下旧GitHub自动交付条款仅供历史研究任务或Owner明确批准的未来在线任务，不能反向覆盖新规则；科学预算和隐私要求继续有效。
# 第五章当前工作流入口 · 验收流程优化（2026-10-19）

Owner已批准本次改进。本页整合现行验收流程，不新增通用工作流版本，不追溯改写冻结合同。执行授权以同一live治理快照的CURRENT.md、TASK_CURRENT.md和当前固定合同为准；离线记忆与旧ACTIVE/NEXT不是授权。

## 固定五步验收
1. 固定对象：一次读取治理/ref，固定任务、候选commit、parent、精确临时目录及白名单。只读本轮需要的合同与历史证据；不递归扫描全仓库目录树。
2. 一次性字节核验：按固定commit取得三份指定文件，将原始字节缓存到已授权审阅环境，以repository/commit/path/blob为缓存键。用标准库hashlib、zipfile、json等批量校验长度、SHA256、CRC、成员路径、重复/大小写碰撞、清单及所有成员哈希。完整响应已校验后不重复下载；部分响应保留INCOMPLETE，不拼造完整文件。工具不支持取得原字节时标REVIEW_PENDING_IO，不改用不受支持的调用或绕过平台控制。
3. 针对性审阅：机器核验全部成员完整性，模型重点阅读本轮变化、关键路径、真实使用接口、测试覆盖及异常。不得把抽样语义阅读说成逐件完整审阅。首次组件审查实现；已接受且哈希不变的组件引用原结论并检查接口影响，不从零重审。每项公开载荷仍须过隐私门，合成标签不是免检证明。
4. 裁决：PASS需要完成本轮全部必需检查；CHANGES_REQUIRED需要可定位的候选缺陷，可提前终止与退修结论无关的检查，并列明NOT_COMPLETED；仅取证失败为REVIEW_PENDING_IO，不算候选实现失败。验收脚本/工具自身错误另记REVIEW_TOOL_ERROR，不转嫁给Codex，不补造结果。
5. 集中归档与清理：批量写入终审记录和当前导航，回读后再核review HEAD，普通非强制提交只删除白名单临时文件并回读。PENDING时保留证据；无候选记NOT_APPLICABLE_NO_CANDIDATE；清理成功不等于实现PASS或完整交付PASS。

## 获取、工具与充分性边界
验收三文件不得使用仓库根tree的recursive=1。用精确目录/文件或逐层非递归子树，并检查额外文件和parent。每一必要对象一次成功获取；只读中断最多一次同对象、同固定commit的恢复尝试，之后及时说明阻塞并标PENDING。可从明确缺陷作出退修结论时无需为凑齐全包继续下载。不得以清理、改分支或重推修复纯读取故障。

不在验收现场重新实现Base64、SHA、DEFLATE或ZIP解析器；不把Base64反复手工搬进不同运行环境。通过已授权、实际支持的原字节通道使用成熟库；无可用通道就如实停在取证边界。标准库校验代码可固定复用，但不能以候选自身的报告代替独立核验。

普通工程验收5—10分钟为软目标，不是成功保证或新FAIL配额。记录fetch_seconds、integrity_seconds、semantic_seconds、archive_cleanup_seconds及失败恢复原因；无法计时记UNKNOWN。达到目标仍未结束时说明已完成、阻塞对象、剩余证据，再作有界继续或暂停，不无限静默扩展。复杂科学审查另按风险确定范围，不能省略科学和隐私硬门。

## 发单与交付
使用[当前任务模板](CH5_REVIEW_TASK_TEMPLATE_CURRENT.md)。固定范围、来源与路径、有限保护根、唯一scratch、E1恢复、科学/工程/交付分账、验收清单和充分退修条件。模板占位符必须在签发前填实。普通E1在同一新任务内有界修复；真实E2/E3和平台拒绝仍停止，旧关闭预算不恢复。

[强制交付与清理](CH5_MANDATORY_REVIEW_DELIVERY_AND_CLEANUP_20261019.md)继续生效：Codex自动上传result.md、manifest.json、evidence_sanitized.zip；Astra终审归档回读后删除。result必须解释变化、结果、证据位置和已知问题；必要源码、fixtures、逐项原件不可用哈希索引代替。同一原件只放一次，重复快照不默认成为重点阅读项。

## 科学与三平面边界
V1.3—V1.9各限域历史政策保留，资源预留不是OS认证、原始诊断与公开脱敏分离、不可变身份和路径保护仍有效。仅按具体问题读取，不要求每轮重读全历史。

HA保持黑箱；TEMP Bellman观察原则不自动改变正式V010合同。科学预算0，V011未启动，Results FALSE，FULL_RUNNER_IO_CLOSURE BLOCKED。

项目长期决定见[项目记忆](CH5_PROJECT_MEMORY_CURRENT.md)。GitHub、本地Codex入口、Project Sources分别记录同步状态；没有实际回执不得宣称三者已同步。平台自动长期记忆不在本文件写入能力之内。


## 2026-10-21：精确对象交付与科研优先的执行优化（Owner已同意）

这是对已采纳五步流程的**实现方式**简化，不产生新的通用工作流版本，也不追溯改写历史冻结合同：

- 默认把已授权的 GitHub Git Data API 精确 blob/tree/commit/new ref 作为三文件交付途径（必须满足现有权限与平台规则）；只有发行前已经确定API写能力不可用且**未发生平台拒绝**时，才可选择合同内原本批准的有限 Git/SSH 路径。401/403/429或策略拒绝必须停，不因快捷而绕过。
- 不为几十KB审阅材料拉取根历史树、不使用root recursive=1，不把数百MB bare Git 对象作为默认成本。每轮发行前对所有合同/参数/manifest做机器预检：任务ID、路径、parent、预算、SHA256正则64位、bytes上限、必要原件通道和隐私门；未知真实SHA必须标null等待实际字节，不写猜测的前缀。
- 交付工具在当前任务的E1额度内自修确定性格式错误；先检查错误是否可在同任务有限处理，不为普通工具/格式问题循环新发工程任务。隔离科学与交付预算，独立历史结果复用不变更其证据等级；先判是否已有可定位缺陷，否则不进行不必要下载或全历史审阅。
- 独立Reviewer仅在可用受授权原字节通道中使用成熟标准库做ZIP所有成员的CRC、长度、SHA256及清单、隐私；如果只得到URL/Blob ID/ZIP的Base64声明而无法在可验证运行环境取得完整字节，必须为REVIEW_PENDING_IO而非PASS，也不能提前清理review临时三文件。
- 科学主线比工具扩建优先；现有已能真实创建精确对象交付候选，默认不再签发新的publisher重构专项。未发生新安全阻断时，不把科研复工前置于再次扩建通用交付器。
- 2026-10-21实际有一份review候选已远端发布且parent/diff已验证，但审阅方尚未完成ZIP所有成员独立字节验证，处于PENDING；可并行进行**不调用HA/GE/IRF的科研方案研究**，不得把PENDING伪装成终审/清理完成或赋予未核证据科学资格。


## 2026-10-21 · Owner重申自动GitHub临时ZIP交付与审阅取证分账（明确执行口径）

- **Codex执行交付是硬要求**：每张已授权可公开证据的长任务都必须在合同/参数/启动Prompt中明写固定 `REVIEW_BRANCH`、`FIXED_PARENT`、`TEMP_PATH`，并由Codex自动上传该**GitHub独立review分支临时目录**的三份原件 `result.md`、`manifest.json`、`evidence_sanitized.zip`。候选commit/tree/三文件Git Blob、大小/哈希和远端完整字节回读必须提供；只打印本地路径不算发布完成。违反安全/权限/限额时如实STOP，不能绕过门禁。旧独立review树不许因新单被清理。
- **交付与独立验证是不同状态**：Codex已完成GitHub自动上传、远端commit与原字节自检，不等于Astra在其独立运行环境完成ZIP全部成员SHA/CRC语义/隐私检查；反过来，Astra无法从连接器Base64把ZIP送进标准库，只能记`REVIEW_PENDING_IO`，**不能误写成Codex没有上传**、要求Codex重复推送或扩建发布器。
- Astra优先按固定commit/path直接从GitHub原字节受支持通道验收；工具不能提供可运行标准库的完整原字节时，保留既有remote候选并暂停清理。仅作为**经Owner自愿选择的例外兜底**，可由Owner把同一候选ZIP原件上传到会话，必须先核其Git原生blob身份后再复算。不能把Owner手动中转改成常态工作流，不能要求为纯取证障碍重跑Codex或重签任务。
- 终审PASS或CHANGES_REQUIRED归档回读后仅用普通non-force精确删除当前review分支当前树三文件、逐文件404及diff回读；Git历史不会被删除，因此脱敏门仍是发行前硬门。PENDING时不删。


## 2026-10-22 TEMP参数探索的Owner逐轮人工决策门
仅在Owner明确批准的冻结合同中，Codex可自动运行单ARM的前10外层迭代并按**先验阈值**安全地延至最多20轮；完成本轮任务后`ACTIVE_TASK=NONE`，Astra必须先独立审查逐省价格触界/企业—家庭投入表，与Owner**讨论并获得下一组参数的独立明示批准**才能签下一任务。严禁自动扩宽N序列、调整Zt/GovInv初值/HA内部、放宽边界，或把价位接近clip错称成正式稳态。完整研究协议见[半自动路线](CH5_TEMP_SEMIAUTO_N_DIAGNOSTIC_ROADMAP_20261022.md)。原GitHub三文件自动交付、限域机验和清理规则不变，平台写入拦截不能靠更换认证等绕过。


## 2026-10-25 · 中断恢复与有界分段验收补充（Owner批准）

本文件的五步验收和离线优先覆盖继续有效；新增执行要求：一次验收最多按A交付/来源、B针对性实现/科学风险、C分层裁决三个阶段组织。每阶段先形成短检查点，标明COMPLETED/BLOCKED/NOT_COMPLETED/NEXT_ACTION；检查点不等于最终PASS。会话/回复/工具输出中断时，恢复固定任务合同与最近检查点，复用已核验证据，不从头重跑、不扩大范围、不推断未返回的工具结果。每次只读取当前任务必要的critical_evidence；不因接口或查询问题改查无关commit/tree，不把跨commit Blob差异误报为候选缺陷。已足够支持退修时早停；纯取证/工具故障分别记REVIEW_PENDING_IO/REVIEW_TOOL_ERROR。详见CH5_INDEPENDENT_REVIEW_RULES_20261025.md的2026-10-25补充。
