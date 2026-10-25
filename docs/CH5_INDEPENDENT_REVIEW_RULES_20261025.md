# CH5 独立审阅规则 V3（GitHub 固定提交优先）
STATUS=OWNER_APPROVED_CURRENT
AUTHORITY=docs/CH5_GITHUB_WORKFLOW_AUTHORITY_CURRENT_20261025.md
ZIP_DEFAULT=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

A阶段：固定候选分支、commit、parent、root tree、治理起点与任务单；核对远端路径、Blob、大小、manifest；可取得原始字节时用成熟标准库核SHA-256。区分Git Blob与SHA-256，不扫描无关历史树，不把跨commit差异直接判为缺陷。
B阶段：以候选diff和关键调用路径为入口，直接阅读GitHub固定commit中的实际源码和证据。复杂项目不能只交摘要、哈希或ZIP；必须有足够上下文独立推导。独立核对关键公式、单位、税基、劳动、时序、边界与测试错误检测能力。科学审阅与交付审阅分开。
C阶段：分别记录artifact_integrity、source_identity、numeric_review、implementation_review、scientific_review、privacy_review、actual_terminal、delivery、cleanup、not_completed。PASS须完成全部硬门；PASS_BOUNDED写明边界；有充分缺陷证据时CHANGES_REQUIRED早停。工具故障为REVIEW_TOOL_ERROR，原件缺失为REVIEW_PENDING_IO。
中断后从固定任务和检查点恢复；不从头重跑、不扩展到无关文件、不推断未返回结果。无自动合并、清理或下一任务。科学权限仍以Owner单独批准为准。