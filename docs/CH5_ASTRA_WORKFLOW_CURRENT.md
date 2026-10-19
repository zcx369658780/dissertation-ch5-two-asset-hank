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
