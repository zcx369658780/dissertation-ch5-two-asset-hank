# 第五章 CURRENT：V010 SOURCE_TIMESTAMP类型门集中修正任务 ACTIVE

更新：2026-10-17（Asia/Shanghai）。本文件顶部状态优先于历史会话ACTIVE与STOP快照。

**VERSION=V010/V0.0.10；V011 NOT_STARTED**。
**ACTIVE_TASK=V010_SOURCE_TIMESTAMP_TYPED_GUARD_CORRECTION_AND_SYNTHETIC_REGRESSION**。
**FIXED_ISSUE_COMMIT=6dfe8a1c98a839f0a94cdd0e938bb6b60f99d520；FIXED_TASK_BLOB=68143e917df883e38fa4615ce0a7c7a86c797330**。
**TASK=[唯一新冻结工程任务](versions/0.0.10/source_timestamp_typed_guard_correction_and_synthetic_regression_task_20261017.md)**。
**SCOPE=ENGINEERING_ONLY_LOCAL_TIMESTAMP_DIAGNOSIS_AND_CORRECTION**。
**NEW_BUDGET=PS_TYPED_TEST_BATCH_MAX2__OLD_SOURCE_READ_MAX12_FILES_2MIB__ONE_RAW_FIELD_DIAGNOSTIC__ONE_CORRECTED_FIELD_RECHECK__SYNTHETIC_CASES_AT_LEAST12__NEW_SCRATCH_MAX6_FLAT_FILES_1MIB__WALL_MAX120MIN**。
**NO_AUTHORITY=OLD_PUBLISH_RETRY0__SANITIZER0__BARE0__GIT_COMMAND0__SSH_FETCH_PUSH0__PYTHON0__MODEL_IMPORT0__VERIFIED_LOADER0__RUNNER0__HA/HJB/KFE/GE/IRF/REAL_C8_0**。
**LATEST_REVIEW=SOURCE_TIMESTAMP_GUARD_FAIL_CLOSED_LOCAL_ONLY__GITHUB_TARGET_REF_404_VERIFIED__PARSED_TYPE_UNKNOWN**。
**NEXT_GATE=WAIT_ASTRA_V010_SOURCE_TIMESTAMP_TYPED_CORRECTION_REVIEW / STOP**。
**FULL_RUNNER_IO_CLOSURE=BLOCKED；model_activation=False；Results FALSE；V011 NOT_STARTED**。

Owner在上一[独立主审](versions/0.0.10/current_seal_exchange_source_timestamp_fail_closed_local_only_primary_review_20261017.md) Git Blob 87d35c2270c1b8a42e19d3210f22fa0abe914bdc后批准一张新集中工程任务，不续前次SOURCE_TIMESTAMP旧任务余额。上一正式证据交换 `V010_CURRENT_SEAL_SANITIZED_GITHUB_EVIDENCE_EXCHANGE` 已 `DELIVERED__STOPPED`，发行Commit 49ff1c3053fa1aa6a0646f55abcffb077e2b62b2 / Blob 1dc5f07a88261c41de434a9c4075b0d179ee871a。上一Codex报告：脚本要求JSON解析后timestamp仍为string且拒绝，**解析后实际type、parser版本、原raw JSON token种类均未记录**；不可推断原timestamp无效或解析器必然自动DateTime转换。上一PS静态批次1/2、只读5份43,468B、scan/bare/SSH/fetch/push/模型/science0，全部旧额度STOP不结转；失败receipt Owner报告 SHA256 F93DA4C6BEE0E62F68A04620B8BF372AD60275C20DEA7782EF2C56E4BFADA6FC，网页未获取本机字节/重算。

**新任务集中交付**：在全新受保护scratch D:/ProjectTemp/ch5_v010_source_timestamp_typed_20261017_01 中，从上一失败scratch及其明确指向的17项集成封存证据精确只读，真实记录原JSON token种类、parse后的匿名.NET类型、parser名称版本及失败表达式，再只在新scratch基于原schema修正时间戳语义守门，并用至少12项合成正反例和最多一次原字段只读复核验证。严禁为了过关取消string或时间语义验证；raw/offset/fractional precision不得因culture、本机时区或解析器转换而丢失。不更改原first/final及失败receipt，不生成新GitHub candidate，所有新PS ≤2批，其余大门完全关闭。

原17/17合成集成与新first/final同run-id/hash仍为Codex本机回执，未到GitHub远端独立原件验收；更旧B/S/L20项旧first无可还原raw/旧run_id缺失 `LEGACY_SEAL_CHAIN=UNVERIFIABLE` 不补造；`ORIGINAL_SANITIZATION_DENIAL_CAUSE=UNKNOWN`且原被拒材料 `PUBLICATION_DENIED`；`HISTORICAL_LEDGER_DEVIATION=UNRESOLVED`。本轮不改变这些前提。

冻结V010科学plan Commit bf091da33d59293f147d52c11580327d3ac2a85d / Blob 85138d8859d53295262fe13bf5bc277bca95ed3f、模型Commit 94de4501dec051b969bee9d852eba2d4591f30ef / Tree 205eab47c4e4f9c6292c2ead9947d94d1a7579a5未改。原MATLAB corrected两资产HA→多省份顺序→GovInv收益边界×0.9/1.1和Zt→GDP冻结后各省误差≤1%独立验→原lagged-NKPC递推；目的地税一次、same-S/前完整轮raw ra0、家庭人均/省财政总量与三劳动账、phi_max=.3、20×20×2固定网格/阈值照旧。Owner corrected HA单点(rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07)仍UNTESTED，真实31省/GE/IRF/Results无新科学资格。

Owner双备份（C盘独立SSD既有备份+GitHub）、既有SSH Key/443与可信工作站工程风险选择不变（本任务Git/SSH0）；原D:/ProjectTemp/c5k1bturn56八dirty/index/staged/untracked/ignored/外Git common-dir、旧所有失败scratch及回执、C备份与真实C8/2017/2018/B3受保护。远端_review_tmp不得在本地科研/模型/治理worktree/index存在。**A16 FAIL_CLOSED；window UNACCEPTED；C9 PAUSED；CALL_LEDGER UNRESOLVED；real C8 A–D REQUEST_ONLY；V011 NOT_STARTED**。GitHub治理不等于本地QMD/Basic Memory自动同步。
