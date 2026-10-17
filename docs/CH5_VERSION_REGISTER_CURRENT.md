# 第五章版本登记（2026-10-17 V010来源恢复／条件修复新任务）

**VERSION=V010/V0.0.10；V011 NOT_STARTED**。
**ACTIVE_TASK=V010_SOURCE_SCRIPT_PROVENANCE_RECOVERY_AND_CONDITIONAL_TIMESTAMP_FIX**。
**FIXED_ISSUE_COMMIT=fafffe0582a213ceec25312f97f47ade6f1aa508；FIXED_TASK_BLOB=22aea7c18716c36ffb1f3154d35d751d9f524bf1**。
**TASK=[唯一冻结工程任务](../versions/0.0.10/source_script_provenance_recovery_conditional_timestamp_fix_task_20261017.md)**。
**CLASS=BOUNDED_SOURCE_PROVENANCE_RECOVERY__CONDITIONAL_LOCAL_TIMESTAMP_FIX**。
**BUDGET=3_ROOT_METADATA_DEPTH0_MAX12_EACH__OLD_READ_MAX12_FILES_2MIB__PS_BATCH_MAX2__SYNTHETIC_MIN12_IF_PROVEN__WALL_MAX150MIN__NEW_FLAT_FILES_MAX8_1MIB**。
**NO_AUTHORITY=GIT/SSH/FETCH/PUSH0__OLD_GITHUB_RETRY0__PYTHON0__VERIFIED_LOADER0__REAL_RUNNER0__HA/HJB/KFE/GE/IRF/REAL_C8_0**。
**DELIVERY=LOCAL_ONLY__GITHUB_PUBLICATION_NOT_AUTHORIZED**。
**LAST_REVIEW=SOURCE_INDEX_MISSING_LOCAL_ONLY_FAIL_CLOSED__NO_PARSER_OR_TIMESTAMP_DIAGNOSTIC**。
**NEXT_GATE=WAIT_ASTRA_V010_SOURCE_PROVENANCE_CONDITIONAL_TIMESTAMP_REVIEW / STOP**。
**FULL_RUNNER_IO_CLOSURE=BLOCKED；HA_SCIENCE_NOT_RUN；model_activation=False；Results FALSE**。

Owner本次同意**不再依赖旧空sourceIndex进行循环定位**，而依据新冻结权限允许三个精确历史scratch根各一次depth=0非递归文件元数据清单；只读内容≤12个不同文件、累计读取字节≤2MiB。仅有精确实际调用绑定/authorized locator、当下 whole-file SHA256/size 和真正字段/schema锚点才可推进后续Gate T、Gate F；仅见类似PS代码不够。脚本若只以内联运行而未保留完整字节，需报不可恢复并STOP。若原历史没有脚本hash，必须标HISTORICAL_EXECUTED_BYTES_UNVERIFIED，不能以今次算出的SHA伪证旧raw。成功恢复后只能在新scratch诊断parse前原token、parse后实际类型/解析器版本、依旧schema条件式修复及至少12合成正反例；Git发布/科学运行另需Owner新许可。

上一[独立主审](../versions/0.0.10/source_timestamp_typed_guard_source_index_missing_fail_closed_local_only_primary_review_20261017.md) Git Blob 5b4a63f453fc472cc90869ca9e029c7657757caf：此前task sourceIndex空且PS1/2、旧2文件四读6,800B，新四文件9,463B，类型/修复/测试皆NOT_RUN，所有旧STOP余量关闭；Owner上轮receipt SHA256 1E9A02F1C9AF59FAB80BED91E39353EB4CCBD87884D46C229D3E9C44610846BC非Astra本机复算。旧更早first seal缺raw与旧run_id，LEGACY_SEAL_UNVERIFIABLE；新17/17合成回执仍Local reported，旧脱敏拒绝UNKNOWN/DENIED、历史ledger偏差UNRESOLVED。

科学冻结计划Commit bf091da33d59293f147d52c11580327d3ac2a85d / Blob 85138d8859d53295262fe13bf5bc277bca95ed3f，模型Commit 94de4501dec051b969bee9d852eba2d4591f30ef / Tree 205eab47c4e4f9c6292c2ead9947d94d1a7579a5完全不变；原MATLAB corrected HA→多省顺序→GovInv收益率边界×0.9/1.1/Zt→GDP冻结后各省误差≤1%独立验收→原lagged-NKPC递推，目的地税一次、same-S/前完整轮raw ra0、phi_max=.3、家庭人均与三劳动账保护。Owner单点 rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07仍UNTESTED；M1真实runner I/O未闭，M2稳态/GDP目标未科学PASS，M3没有基点不能正式冲击，M4 Results FALSE，V011 NOT_STARTED。原8dirty/index/staged/untracked/ignored、外Git common-dir、全部旧失败证据、C SSD备份与real C8保护；A16/window/C9/CALL_LEDGER不改。
