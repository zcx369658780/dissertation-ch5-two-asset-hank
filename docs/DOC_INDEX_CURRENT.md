# 第五章动态总目录（2026-10-17 V010 来源身份有界恢复＋条件式时间戳修复ACTIVE）

**ACTIVE_TASK=V010_SOURCE_SCRIPT_PROVENANCE_RECOVERY_AND_CONDITIONAL_TIMESTAMP_FIX**。
**FIXED_TASK_ISSUE_COMMIT=fafffe0582a213ceec25312f97f47ade6f1aa508；FIXED_TASK_BLOB=22aea7c18716c36ffb1f3154d35d751d9f524bf1**。Owner已明确授权**新范围的精确来源身份恢复**，只允许三个既定旧scratch根各一次depth=0/≤12直接子项的元数据盘点，旧实际内容只读≤12文件/2MiB；证明已执行脚本位置/整文件hash/字段schema锚点后三阶段才可继续时间戳解析、仅新scratch修正与至少12个合成案例。**旧GitHub发布任务STOP不复用；本轮Git/SSH/Python/HA全部0。**

| 作用 | GitHub权威入口 | 当前状态 |
|---|---|---|
| **唯一ACTIVE冻结任务** | [V010来源恢复＋条件式时间戳修复](../versions/0.0.10/source_script_provenance_recovery_conditional_timestamp_fix_task_20261017.md) | 固定Commit fafffe0582a213ceec25312f97f47ade6f1aa508 / Blob 22aea7c18716c36ffb1f3154d35d751d9f524bf1，待Codex |
| CURRENT | [实时状态](../CURRENT.md) | 当前唯一授权及禁令 |
| TASK_CURRENT | [当前任务权限](../TASK_CURRENT.md) | 新scratch、三根元数据盘点/旧读取、PS2批、失败STOP |
| 上一独立限域主审 | [SOURCE_INDEX缺失导致前置STOP](../versions/0.0.10/source_timestamp_typed_guard_source_index_missing_fail_closed_local_only_primary_review_20261017.md) | Blob 5b4a63f453fc472cc90869ca9e029c7657757caf；manifest sourceIndex空仅本机回执级 |
| 已STOP旧修复任务 | [旧timestamp typed guard任务](../versions/0.0.10/source_timestamp_typed_guard_correction_and_synthetic_regression_task_20261017.md) | commit 6dfe8a1c98a839f0a94cdd0e938bb6b60f99d520 / blob 68143e917df883e38fa4615ce0a7c7a86c797330，不继续旧额度 |
| 最新路线图进度 | [V010 M1–M4及下一门](CH5_V010_ROADMAP_PROGRESS_AND_NEXT_GATES_20261016.md) | M1工程部分完成/M2-M4无新科学PASS |
| Owner备份/SSH | [风险决定](CH5_OWNER_RISK_BACKUP_SSH_LOADER_DECISION_20261016.md) | C盘独立SSD备份+GitHub，现有SSH Key/443本轮禁用 |
| 临时review协议 | [仅远端审阅](CH5_TEMP_SANITIZED_REVIEW_EXCHANGE_20261016.md) | 本轮不发行remote candidate，旧DENIED材料不上传 |
| V1.2 | [工作流](CH5_ASTRA_WORKFLOW_CURRENT.md) | Owner/冻结/独立验收 |
| 科学计划 | [SCIENTIFIC_DECISIONS](../SCIENTIFIC_DECISIONS.md) | V010数学合同不改 |
| 版本登记 | [CH5_VERSION_REGISTER_CURRENT](CH5_VERSION_REGISTER_CURRENT.md) | V010中、V011未启 |
| 长期知识 | [CH5_WEB_KNOWLEDGE_CURRENT](knowledge/CH5_WEB_KNOWLEDGE_CURRENT.md) | 最新顶层时态有效 |

上一任务本机消耗PS1/2、旧2个文件四次读6,800B、新4文件9,463B，Guard修复/12合成NOT_RUN；last receipt SHA256 1E9A02F1C9AF59FAB80BED91E39353EB4CCBD87884D46C229D3E9C44610846BC为Owner转述，Astra未直接复算；已STOP余额不能结转。新任务若只能找到类似文件但无法证明原调用与来源绑定，必须FAIL_CLOSED，不能补造源码。更旧first缺真实raw/run_id永久LEGACY_SEAL_UNVERIFIABLE；新17合成seal仅本地回执，原Sanitizer DENIED/UNKNOWN、历史ledger偏差UNRESOLVED。V010冻结plan Blob 85138d8859d53295262fe13bf5bc277bca95ed3f / 模型Tree 205eab47c4e4f9c6292c2ead9947d94d1a7579a5不改；Owner HA单点UNTESTED，FULL_RUNNER_IO_CLOSURE BLOCKED，Results FALSE，V011 NOT_STARTED，原A16/window/C9/CALL_LEDGER、real C8 REQUEST_ONLY、原8dirty/index/外common-dir/C SSD备份保持。GitHub同步不证明本地QMD/Basic Memory同步。
