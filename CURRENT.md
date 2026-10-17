# 第五章 CURRENT · M1长任务回执上传独立SHA已确认，九份工程原件待进一步验证

2026-10-17（Asia/Shanghai），V1.3重要工程候选文档证据增级。
**WORKFLOW=V1.3__LONG_TASK_DELIVERED__UPLOADED_RECEIPT_HASH_VERIFIED**。
**VERSION=V010/V0.0.10；V011 NOT_STARTED**。
**ACTIVE_TASK=NONE**。
**LAST_TASK=V010_M1_V13_CONSOLIDATED_ENGINEERING_EXIT__DELIVERED__STOPPED**。
**LATEST_VERDICT=UPLOADED_RECEIPT_SHA256_VERIFIED__DOCUMENTARY_LIMITED_ACCEPT__M1_LOCAL_ENGINEERING_CANDIDATE_ONLY**。
**ADDENDUM=[本次独立上传字节核验补充审议](versions/0.0.10/m1_v13_consolidated_uploaded_delivery_receipt_independent_sha_addendum_20261017.md)**。
**PRIMARY_REVIEW=[先前限域主审](versions/0.0.10/m1_v13_consolidated_engineering_local_only_candidate_review_20261017.md)**。
**NEXT_GATE=WAIT_OWNER_EXISTING_NINE_M1_ARTIFACTS_SINGLE_ARCHIVE_FOR_INDEPENDENT_REVIEW / STOP**。
**NEW_EXECUTION_PERMISSION=NONE__ENGINEERING_PYTHON0__RUNNER0__GITHUB_PUSH0__HA/HJB/KFE/GE/IRF/REAL_C8_0**。
**FULL_RUNNER_IO_CLOSURE=BLOCKED；model_activation=False；Results FALSE；V011 NOT_STARTED**。

Astra此次**实际读取Owner上传的2个文件**并对原始字节复算：`DELIVERY_RECEIPT.json` 5,875B SHA256 `E100A61CA00DBD510FF8C7E9417EB2C2663E66C73AEBEDD81B6581A85BF36F50`，精确等于先前Codex报告；`DELIVERY_SUMMARY.md`1,984B SHA256`351BF6C2FDF378142A1FCC4DFCFD81390A204C834E512F8ADD74680B88F20EA0`。27键JSON合法、Python15控制器+8 dummy=23/24、raw源码协议流2,212,964B<16MiB、非Git回执前5,030,611B<128MiB、旧11件701,946B等统计字段内部一致，**但不是Windows执行日志独立复算**。回执内索引9份其他既有原件合计204,154B，仅载明SHA/字节，实际原件未上传，first-final/run_id、九模块/runner/Job/PIPE和源/诊断分流无法独立全验。

回执同时明确early Git prelaunch snapshots未留存、N13原streams_complete字段错误已另作派生更正、原任务文本换行投影不是RAW、总wall从first receipt才计时、早期PowerShell PID及overflow probe为UNKNOWN。此前原生canonical仍BLOCKED；仅scoped adapter-only获得CODEX_REPORTED_PASS。GitHub远端review ref先前实查不存在、SSH一次预检exit128；旧预算全部STOP。**不重跑M1，也不发GitHub输送微任务**：如Owner愿意，一次附9份原字节文件的单个安全ZIP，再做真正逐原件审阅。

冻结V010模型tree205eab47c4e4f9c6292c2ead9947d94d1a7579a5/科学plan Blob85138d8859d53295262fe13bf5bc277bca95ed3f不变；HA单点UNTESTED，Results FALSE与V011 NOT_STARTED，原8dirty/index/外common-dir、C盘SSD备份、所有旧失败/真实C8与A16/window/C9/CALL_LEDGER持续保护。
