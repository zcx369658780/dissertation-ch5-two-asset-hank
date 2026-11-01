<!-- LOCAL_FIRST_CLASSIFICATION_20261101 -->
> **适用范围：SCIENTIFIC_CONSTRAINT；普通工程网页终验角色属于 SUPERSEDED_WORKFLOW**
>
> 当前执行入口：[AGENTS](../AGENTS.md) → [唯一短状态](CH5_LOCAL_FIRST_STATUS_CURRENT.md) → [唯一工作流](CH5_ASTRA_WORKFLOW_CURRENT.md)。Owner 决策见 [2026-11-01 决策记录](OWNER_LOCAL_FIRST_CODEX_20261101.md)。
>
> 本文件不整体失效：来源身份、实际原件、数值证据、公式/单位/税基/劳动/时序/边界审查、隐私、STOP、缺口分层和不得推断未返回结果的要求继续保留。
> 不再据此要求普通工程必须等 GPT/Astra 或强制 A/B/C 网页验收。Local Codex 工程验收不等于独立科学评议；仍有效科学合同要求的独立科学门与 Owner 最终科学接受不能由自验代替。
> 下方原文保留；历史 STATUS/AUTHORITY 和 A/B/C 叙述须按上述范围理解，不能成为新的普通工程门禁或科学执行许可。

---

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