# 第五章任务模板 · 验收范围优先

TEMPLATE_ONLY / NOT_EXECUTABLE。下列字段须在实例中填实；本模板不发单，不授权任何旧任务。

## 身份与目标
TASK_ID、修订、Owner授权、唯一可验收问题、固定baseline、输入commit/path/blob及原字节来源、明确禁止项。live治理快照与baseline分开；ISSUE_MANIFEST在生成后引用合同，不要求自引用哈希。

## 边界与执行
给出规范索引docs/DOC_INDEX_CURRENT.md、唯一scratch与可信父目录、有限保护根、仅必要只读身份解析、目标文件白名单。明确谁可写哪里，不递归扫描无关依赖。
列出SCIENCE/ENGINEERING/DELIVERY各自预算与终点、可恢复E1次数/范围、真实E2/E3/平台拒绝边界。预期负例不是任务事故；失败原件不覆盖。任务未知本机事实必须实测，不在文档中宣称已认证。

## 冻结验收计划
- acceptance_criteria：逐条指向实现/测试/必要原件。
- critical_evidence：本轮关键代码、变更、接口和异常证据。
- unchanged_accepted_dependencies：已有接受记录、固定hash与本轮接口影响；未验组件不得伪装复用。
- integrity_check：三份远端文件及ZIP全成员的长度/CRC/SHA、路径/清单；使用成熟库。
- semantic_review：差异和风险聚焦；隐私每项仍有处置。
- early_changes_required：足以退修的明确缺陷及未完成项记录；不得冒充全包检查。
- acquisition_failure：REVIEW_PENDING_IO；审阅工具bug另记REVIEW_TOOL_ERROR，不计候选失败。
- time_target：普通工程5—10分钟软目标，四阶段耗时，复杂风险例外写明；非硬FAIL配额。

## 固定交付
REVIEW_BRANCH、FIXED_PARENT、TEMP_PATH、远端三件白名单、文件上限、发布次数、精确目录/文件获取方式、同对象读取恢复范围、终态原始回执通道全部填实。禁止root recursive tree；完整已校验字节缓存复用。
Codex自动上传result.md、manifest.json、evidence_sanitized.zip；必要内容不可只给hash。result说明变化/测试/风险/证据位置。清单无自引用；实际候选身份和最后计数放包外回执。

## 裁决与关闭
PASS / CHANGES_REQUIRED / REVIEW_PENDING_IO；分列完整性、实现、隐私、交付、清理与NOT_COMPLETED。先集中归档回读，再由Astra核ref、白名单删除及回读。PENDING保留材料，无候选只记N/A；清理成功不自动等于通过。
发单前检查合同、参数、CURRENT/TASK_CURRENT、Prompt、来源包是否同义且无缺项。给单一代码框启动Prompt。同步面状态分别登记，不自动启动下一任务。

## 2026-10-21 固定任务Prompt必须明写
将以下完整义务作为每张新任务合同和**单一启动Prompt**的显式句子：
“Codex必须把本任务逐成员脱敏后的`evidence_sanitized.zip`连同`result.md`、`manifest.json`，自动上传至GitHub仓库的`REVIEW_BRANCH/TEMP_PATH`所指定的**独立Review分支临时目录**，只允许三文件白名单；必须在最终回执给出候选身份及三原件远端原字节读回证据。Astra终审归档后负责准确清理。Owner人工搬运不是默认交付流程。”
若验收方原字节通道受限，归类`REVIEW_PENDING_IO`而不是Codex上传未完成；当前已知候选不重推，Owner同意才可仅上传同一已固定Git Blob原件作例外的审核入口。
