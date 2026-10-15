# TASK_CURRENT：V010首次HA失败单元已有回执SOURCE_ONLY精准提取

日期：2026-10-15（Asia/Shanghai）。
**ACTIVE_TASK=V010_FIRST_HA_FAILED_CELL_EXISTING_RECEIPT_EXTRACTION_SOURCE_ONLY**。
**ALLOWED=EXISTING_SYNTHETIC_JSON_READ_AND_DEIDENTIFIED_SUMMARY_ONLY**。
**NEW_HJB_KFE_SELECTOR_ROOT_PYTEST_MACRO_IRF_BUDGET=0；NO_CODE_CHANGES，NO_SCIENTIFIC_REEXECUTION**。

任务全文：[versions/0.0.10/first_failed_cell_evidence_task_20261015.md](versions/0.0.10/first_failed_cell_evidence_task_20261015.md)。
确切前置：V010工程候选 `94de4501dec051b969bee9d852eba2d4591f30ef`，独立审议 `versions/0.0.10/implementation_review_20261015.md` blob `df7b4b38b3cc77b6cb0c7dac7b733d45f34274b6`。Owner已允许本轮仅从首次科学run现存`first_failed_cell.json`/`attempt_summary.json`和关联输入身份中提取原因；无权再次求解。

原冻结plan仍固定 `bf091da33d59293f147d52c11580327d3ac2a85d`、blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；不修改。原科学消费4/6 pytest，1/4 driver，1/26 HA，1626 selector cells和1642 roots仅继承记账，不构成新调用许可。原8 dirty树、真实C8/B3及旧研究不触。

交付 `V010_FIRST_HA_FAILED_CELL_SOURCE_ONLY_EVIDENCE`，最终 `WAIT_ASTRA_V010_FIRST_HA_FAILURE_REASON_REVIEW / STOP`；V011 NOT_STARTED、Results FALSE。
