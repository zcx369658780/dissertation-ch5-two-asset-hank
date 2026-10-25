# TEMP31 当前进度与关键证据发布：普通权限 SSH 恢复

本次 Owner 授权使用普通权限 PowerShell 和指定 SSH 密钥恢复原任务证据发布。固定治理起点 04a5572d1978202f2a66be06f27748cf0585d989，独立候选分支 codex/ch5-temp31-evidence-publication-20261025-r1。GitHub 连接器调用为零，不使用 UAC，不改全局 Git/SSH 配置，不读取/复制/哈希私钥。之前管理员 SSH 已成功，但本地 git write-tree 超时；不能将该超时归因于 UAC 或密钥。之前的连接器和普通权限 SSH 失败均作为历史记录保留。

复用已准备证据：原静态审计 ZIP 100834 字节、SHA-256 00ecaf1cf987956d48379e440015dd39963c84779bc5ba9f94ca2ee2e38431fa；30 字段账本、98 条源码片段、税基矩阵、vintage 表、Owner 简报和 15 份冻结源码文本。未重跑审计、历史测试或模型。仅修正发布工具的目录构建方法：显式构建允许目录及祖先树，继承其余树对象，不使用全局索引或重新校验全部父树 Blob。

真实 canonical 净工资来源、31 省 ID/order join、单位/期间/vintage 及生产 callback 仍 UNKNOWN/BLOCKED。独立审计报告原件仍缺失，治理转述不等于本轮原件验证。D1=B、D2、D3=B 是目标合同/设计，科学门不升级。原历史 STOP 文档与管理员准备快照为历史证据；当前状态以本页和当前回执为准。

artifact_integrity=PASS_PACKAGING_ONLY
source_identity=EXACT_ARCHIVE_CONTEXT_REUSED__REAL_CANONICAL_BLOCKED
numeric_review=NOT_RUN
implementation_review=PACKAGING_AND_PROVENANCE_ONLY
scientific_review=NOT_RUN
privacy_review=PASS_FINITE_PATTERNS
actual_terminal=PREPARED__REMOTE_READBACK_PENDING
delivery=NOT_YET_CERTIFIED
cleanup=NOT_AUTHORIZED_NOT_PERFORMED
not_completed=Independent audit report original; canonical/units/vintage/31-ID/callback closure; independent acceptance; global connector disable

证据提交先远端回读全部原字节，再形成回执封存提交。公开封存回执指向已回读证据提交；封存提交自身 Commit/Parent/Root 及最后回读结果见外置回执和交付消息，避免自引用。交付不等于 GPT/Astra 独立接受。没有独立完成事件，标 UNKNOWN。

SCIENCE/TEST/PREFLIGHT/MODEL/HA/HJB/KFE/GE/IRF/FORMAL_SOURCE_WRITES=0。V010=UNCHANGED，V011=NOT_STARTED，Results=FALSE，FORMAL_SOURCE_FREEZE=FALSE，model_activation=False，REAL_GE=False，FULL_RUNNER_IO_CLOSURE=BLOCKED。治理及默认分支不写入；不发 Issue/PR、不合并、不清理、不自动下一任务。完成最终回读后 STOP。
