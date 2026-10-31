# Codex 与 GitHub 固定提交工作流（Owner批准，2026-10-25；2026-10-31复核）

STATUS=OWNER_APPROVED_CURRENT
MODE=MANUAL_PER_TASK_NOT_AUTOMATED
DEFAULT_WORKFLOW=GPT_FROZEN_TASK_SHEET__LOCAL_CODEX__SSH_CANDIDATE_BRANCH__GPT_FIXED_COMMIT_REVIEW__OWNER_DECISION
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 1. 每项任务单独授权

GPT顾问仅在Owner授权后发布一张冻结任务单，必须列明唯一TASK_ID、治理HEAD、候选分支、固定parent、来源commit/tree/path/Blob、读写白名单、预算、STOP条件和验收字段。Owner将任务交给本地Codex执行。任务单本身不得超出Owner授权。

## 2. 本地执行与候选发布

Codex先核验本地仓库、HEAD、worktree/index状态及任务允许路径；仅在获准的独立候选分支/目录执行。完成后通过已授权普通权限SSH推送独立候选分支，并回读commit、parent、tree、路径、Git Blob、大小及必要SHA-256。完成远端回读后STOP，不自动创建Issue/PR、不合并、不清理、不签发下一任务。

遇平台、权限或安全拒绝必须STOP；不得换账号、凭据、协议、路径或其他方式绕过。GitHub插件连接器不是SSH推送前提。

## 3. GPT固定commit独立审阅

GPT/Astra直接从固定commit阅读足够的真实源码和证据上下文，独立审阅提交/来源、关键实现、数值和科学风险、隐私、实际终态及交付。摘要、哈希索引、ZIP或执行者结论不能替代必要原件。每阶段标记COMPLETED/BLOCKED/NOT_COMPLETED/NEXT_ACTION；工具故障为REVIEW_TOOL_ERROR，原字节/必要来源缺失为REVIEW_PENDING_IO。科学审阅与交付审阅分开。

## 4. 三个同步平面

GitHub仓库、Owner本地Codex工作区、ChatGPT Project Sources是三个独立同步平面。GitHub推送成功不证明本地Codex或Project Sources已同步；Project Source ZIP上传也不改变GitHub代码。每次同步必须核验具体commit/文件身份。

## 5. 科研权限与安全

本流程不授权HA/HJB/KFE/GE/IRF、稳态、校准、福利、正式源修改或正式Results。任何科学执行、参数/方程/边界/网格/求解器/容差变更均需单独、明确、有限的Owner授权。永久科学状态按当前科学规则保持；本工作流不重置预算、不解除STOP/PENDING。

## 6. 当前科研路线专项规则

自2026-10-31起，Python多省份HANK为唯一主动研究实现，MATLAB仅为历史参考；具体见`PROJECT_RULE_PYTHON_RESEARCH_MAINLINE_CURRENT_20261031.md`。本工作流管理任务和审阅，不决定科学结论。
