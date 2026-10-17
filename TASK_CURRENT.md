# TASK_CURRENT · V1.3 Codex一次本地文档同步

**ACTIVE_TASK=CH5_V13_ONE_TIME_CODEX_LOCAL_DOCUMENT_SYNC**。
**FIXED_ISSUE_COMMIT=77b4e7119b23008b8b708b6b39cc6b75077e2b4b**。
**FIXED_TASK_BLOB=daf6807397ac19a580a45a73c14e27665580bb04**。
**TASK_FILE=[正式冻结DOC_ONLY同步任务](versions/0.0.10/workflow_v13_one_time_codex_local_docs_sync_task_20261017.md)**。
**V13_POLICY=[Owner批准工程快速通道](docs/CH5_ASTRA_WORKFLOW_V1_3_20261017.md)**。
**AUTHORITY=DOC_ONLY__LOCAL_SAFE_DOCUMENT_MIRROR__NO_MODEL_WORKTREE_WRITE**。
**STOP=WAIT_ASTRA_CH5_V13_LOCAL_DOC_SYNC_REVIEW / STOP**。

新Owner授权仅一次本地Codex文档镜像同步：从上述固定发行Commit读取任务/规则并验证任务Blob，在已独立认证的安全文档镜像或唯一新隔离目录中更新**V1.3工作流、CURRENT、TASK_CURRENT、总目录、项目Source记忆覆盖层**，输出准确SHA256与保护证明。必须**先只读路径身份检查→新目录建立→再核身份→首次写文件**，不能为准备preflight先在不可信scratch写脚本/日志。若无可信目录或父目录身份，终端返回STOP，不建目录、不修改受保护资产。

**NEW_PROCESS_BUDGET=POWERSHELL_STATIC_MAX2__WALL_MAX45MIN__SOURCE_DOCS_MAX8_300KIB__OUTPUT_DOCS_MAX8_400KIB**。
**NO_AUTHORITY=GITHUB_WRITE/PUSH0__PYTHON0__VERIFIED_LOADER0__RUNNER0__HA/HJB/KFE/GE/IRF/REAL_C8_0**。
**NO_SYNC_CLAIM_UNTIL_CODEX_RECEIPT**。

旧`V010_CURRENT_TIMESTAMP_SANITIZED_EVIDENCE_EXCHANGE`已STOP、候选无ref、原V010模型/科学权限不变。此前工程24/25+1项SPEC_UNRESOLVED及历史原first/旧脚本hash缺失不能通过新流程追认。Codex不能把本同步扩成旧GitHub timestamp候选发布或主线HA模型实验。