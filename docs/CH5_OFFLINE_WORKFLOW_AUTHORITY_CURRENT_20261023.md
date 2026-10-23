# CH5 正式治理：离线优先工作流（Owner 2026-10-23）
STATUS=OWNER_APPROVED_OFFLINE_PRIMARY
EFFECTIVE=2026-10-23
AUTHORITY=OWNER_WORKFLOW_SUPERSESSION
GITHUB_AUTO_TASK_ISSUE=DISABLED
GITHUB_AUTO_REVIEW_UPLOAD=DISABLED
GITHUB_AUTO_REVIEW_CLEANUP=DISABLED
RESULTS=FALSE
V011=NOT_STARTED

## 生效与优先级
Owner于2026-10-23正式决定由临时离线交付升级为当前默认工作流：GPT顾问下发冻结MD任务单，Owner交本地Codex执行，Codex生成一份完整脱敏外层ZIP，Owner手动上传到GPT，GPT独立验收，Owner决定下一步。此决定覆盖旧AGENTS、CH5_ASTRA_WORKFLOW、MANDATORY_REVIEW、REVIEW_TASK_TEMPLATE中要求每次通过GitHub自动Issue、自动上传三件Review、审阅后自动清理的**日常交付机制**。旧已签合同与历史GitHub证据不追溯修改；若旧导航与本页冲突，以本页和Owner新签科学合同为准。
GitHub只读查冻结代码和历史证据允许（需任务单精确指定），里程碑备份及Code Review写入必须Owner再次明确批准，不使用GitHub作为默认任务单与验收中转。遇OpenAI平台写入安全拒绝立即停止，不更换认证、账号、路径或协议绕过。更改默认流程不代表已经证明安全阻断被修复。
## 任务执行与交付
- 任务单：唯一TASK_ID、Owner范围、冻结源码来源commit/path/blob、原字节取得渠道、唯一可信scratch、受保护边界、SCIENCE/ENGINEERING/DELIVERY分账、E1和E3、STOP、输出、隐私；未实际发行的历史Issue不自动转为活跃任务。
- Codex：默认只在本地隔离目录执行，禁止未经明确批准运行HA/HJB/KFE/roots/outer/GE/IRF、修改正式V010或写GitHub；使用经冻结允许的只读GitHub GET并不能升级为写入授权。
- 离线交付：Codex自动生成单份脱敏外层ZIP，内含result.md、manifest.json、evidence_sanitized.zip、DELIVERY_FINAL_RECEIPT.json、INDEPENDENT_COMPLETION_EVENT.json。按标准库核每件长度/SHA256/CRC、路径、重名/目录穿越和私密信息；必要源码、合成fixture、测试向量和真实首错在内层包可审，不可用仅有hash的摘要代替。最终事件不能验证时标UNKNOWN。STOP同样须尽最大可能交证据。
- Owner只需手动上传完整ZIP；GPT独立原字节及语义验收，分开artifact_integrity、numeric、source_identity、science、privacy、actual_terminal。不得把Codex的退出码、自检或ZIP完整性当作HA科学PASS。无可获取原字节标REVIEW_PENDING_IO，不伪造。
- Project Sources由Owner手动上传更新，Codex单次本地文档同步必须由Owner提交明确Prompt且有真实回执。GitHub治理、Project Sources与本地Codex三平面分别记录，不能因其中一项通过宣称全部同步。平台自动Memory也不会通过写MD自动改变。
## 截至本次批准的科研状态
ACTIVE_TASK=NONE（规则迁移，不启动科研任务）
Owner已选A1作为TEMP31研究路线：家户财富、消费与财政按居民H聚合，劳动核沿用Ct机制且企业来源规模E=pH；A2未采纳，**A1尚未实装入冻结正式V010**。离线run56ea4f3d6a304913a022c9653c48230b受界终审PASS_BOUNDED_A1_SYNTHETIC_ADAPTER_AND_ALGEBRA__HA_ADMISSION_BLOCKED；真实家庭收入预算、HU与劳动时间单位、2018省份数据均未闭合。O合格候选10格7省，实际I/S为0；s_H=64.8906755511未获Owner批准。HA/HJB/KFE/GE/IRF预算0；Results=FALSE、V011=NOT_STARTED、model_activation=False、REAL_GE=False、FULL_RUNNER_IO_CLOSURE=BLOCKED。
旧Github未发行Scheme A Issue a46eb80156e9fca7f85be166ea03adc1ea1676ab仅作为历史对象，不能当新ACTIVE。三个更早PENDING Review refs仍保护，禁止本次治理任务清理。
