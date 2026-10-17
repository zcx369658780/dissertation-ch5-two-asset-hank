# 第五章 CURRENT：V010 有界守门脚本来源恢复＋条件式时间戳修复任务已签发

更新：2026-10-17（Asia/Shanghai）。此处最新执行门优先于下方历史ACTIVE/STOP状态。
**VERSION=V010/V0.0.10；V011 NOT_STARTED**。
**ACTIVE_TASK=V010_SOURCE_SCRIPT_PROVENANCE_RECOVERY_AND_CONDITIONAL_TIMESTAMP_FIX**。
**FIXED_ISSUE_COMMIT=fafffe0582a213ceec25312f97f47ade6f1aa508；FIXED_TASK_BLOB=22aea7c18716c36ffb1f3154d35d751d9f524bf1**。
**TASK=[唯一冻结新工程任务](versions/0.0.10/source_script_provenance_recovery_conditional_timestamp_fix_task_20261017.md)**。
**SCOPE=BOUNDED_SOURCE_PROVENANCE_RECOVERY__CONDITIONAL_LOCAL_TIMESTAMP_FIX**。
**NEW_BUDGET=ROOT_METADATA_ONLY_3x1_DEPTH0_MAX12_EACH__OLD_FILES_MAX12_TOTAL_READ_2MIB__PS_BATCH_MAX2__SYNTHETIC_CASES_MIN12_IF_PROVEN__SCRATCH_MAX8_FLAT_FILES_1MIB__WALL_MAX150MIN**。
**NO_AUTHORITY=GIT/SSH/FETCH/PUSH/COMMIT0__OLD_EXCHANGE_RETRY0__PYTHON0__MODEL_IMPORT0__VERIFIED_LOADER0__RUNNER0__SCIENTIFIC_HA/HJB/KFE/GE/IRF/REAL_C8_0**。
**LATEST_REVIEW=SOURCE_INDEX_MISSING_FAIL_CLOSED_LOCAL_ONLY__NO_SCRIPT_IDENTITY**。
**NEXT_GATE=WAIT_ASTRA_V010_SOURCE_PROVENANCE_CONDITIONAL_TIMESTAMP_REVIEW / STOP**。
**FULL_RUNNER_IO_CLOSURE=BLOCKED；model_activation=False；Results FALSE；V011 NOT_STARTED**。

Owner在上一正式[限域主审](versions/0.0.10/source_timestamp_typed_guard_source_index_missing_fail_closed_local_only_primary_review_20261017.md)（Blob 5b4a63f453fc472cc90869ca9e029c7657757caf）后明确批准一张**新、独立额度**的有界来源恢复与条件式修复任务。上一任务 V010_SOURCE_TIMESTAMP_TYPED_GUARD_CORRECTION_AND_SYNTHETIC_REGRESSION 已DELIVERED/STOPPED：Codex报告上一失败receipt的manifest sourceIndex为空，没有原脚本已执行的确切路径、整体hash和timestamp字段/schema锚点，因此依旧任务来源门STOP；没有执行timestamp类型诊断、修复、12例、GitHub发布或科学调用。这**不证明原脚本实体丢失、原timestamp非法或解析器一定自动DateTime转换**。上一Owner本机receipt SHA256 1E9A02F1C9AF59FAB80BED91E39353EB4CCBD87884D46C229D3E9C44610846BC并未被Astra实际获取字节重新计算，上一PS 1/2、旧2文件4次读共6,800B、新4文件9,463B，全部旧余量STOP不可结转。

本新任务**另外授权**在三个冻结历史scratch根只做各一次depth=0元数据盘点、每根最多12个直接子项；只读内容仍须由历史task/receipt/实际调用证据限定，最多12个不同文件、累计实际读取≤2MiB，不以“看到同名PS脚本”认定已被当时执行。必须独立证明“精确授权位置及实际调用绑定＋整文件SHA256＋原JSON字段/schema锚点”三元身份，缺失即STOP。三元身份完整才允许在新项目外scratch诊断raw lexical token、解析后.NET type和parser版本，再修仅新副本时间戳守门/≥12项安全合成用例及一次原字段只读复核。新PS总≤2批、wall≤150分钟、新平铺≤8文件/1MiB且写前预留128KiB。旧json、脚本、回执永不改写；如果无法证明历史同字节执行，只能记历史执行raw bytes UNKNOWN。

旧B/S/L20首版raw/run_id缺失仍LEGACY_SEAL_CHAIN_UNVERIFIABLE；新17项合成/first-final seal仅Codex本机证据，未远端验；旧SANITIZATION_DENIED原因UNKNOWN/候选禁止发布；旧ledger raw argv/源码复制偏差UNRESOLVED。新的GitHub发布、科学运行与V011均不授权。

V010科学计划固定commit bf091da33d59293f147d52c11580327d3ac2a85d/Blob85138d8859d53295262fe13bf5bc277bca95ed3f及模型代码commit94de4501dec051b969bee9d852eba2d4591f30ef/tree205eab47c4e4f9c6292c2ead9947d94d1a7579a5不变。原MATLAB corrected HA/HJB/KFE→多省有界顺序→GovInv收益率边界×0.9/1.1及Zt→冻结GDP≤1%独立验证→lagged-NKPC原递推，目的地工资税一次、same-S/前完整轮raw ra0、家庭人均/省财政总量/三劳动账、phi_max=.3和20×20×2原网格阈值保护。Owner单点 rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07 UNTESTED；M1真实Windows runner未闭环，M2稳态未验证，M3正式冲击/GE/IRF未过，M4 Results FALSE。

原受保护D:/ProjectTemp/c5k1bturn56八dirty/index/staged/untracked/ignored/外Git common-dir、所有旧失败证据、C盘独立SSD备份、real C8/2017/2018/B3/V009数组不可改；Owner现有C盘SSD+GitHub备份、SSHKey/443和可信工作站风险决定不变（本任务SSH0）。远端_review_tmp不得进入本地任何model/研究/治理worktree或index。**A16 FAIL_CLOSED；window UNACCEPTED；C9 PAUSED；CALL_LEDGER UNRESOLVED；real C8 A–D REQUEST_ONLY；V011 NOT_STARTED**。GitHub治理存档不代表QMD/Basic Memory自动更新。
