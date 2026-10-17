# 第五章 CURRENT · V010 M1 / V1.3 平台版本子进程来源与可信导入工程门

更新：2026-10-17（Asia/Shanghai）；本文件顶端时态优先于历史主审和旧ACTIVE快照。
**WORKFLOW=V1.3__OWNER_APPROVED__LOCAL_CODEX_DOC_SYNC_LIMITED_ACCEPTED**。
**RESEARCH_VERSION=V010/V0.0.10；V011 NOT_STARTED**。
**ACTIVE_TASK=V010_M1_V13_PLATFORM_SYSCMD_VER_PROVENANCE_AND_CANONICAL_RUNNER_GATE**。
**FIXED_ISSUE_COMMIT=7e9ade7c36a1b606c8d8125b0fd21e9b067d4f9c；FIXED_TASK_BLOB=67928a92b742054d7303771974cb8cb42943cd65**。
**TASK=[唯一冻结本轮工程任务](versions/0.0.10/m1_v13_platform_syscmd_ver_provenance_canonical_runner_task_20261017.md)**。
**STOP=WAIT_ASTRA_V010_M1_PLATFORM_CANONICAL_RUNNER_REVIEW / STOP**。
**FULL_RUNNER_IO_CLOSURE=BLOCKED；model_activation=False；Results FALSE**。

**CLASS=ENGINEERING_ONLY__SYSCMD_VER_PROVENANCE__CANONICAL_NINE_MODULE__RUNNER_IO**。
**SCIENTIFIC_PLAN_BLOB=85138d8859d53295262fe13bf5bc277bca95ed3f**。
**FROZEN_MODEL_COMMIT=94de4501dec051b969bee9d852eba2d4591f30ef；FROZEN_MODEL_TREE=205eab47c4e4f9c6292c2ead9947d94d1a7579a5**。
**NEW_BUDGET=ENGINEERING_PYTHON_MAX8__WALL150MIN__PER_PROCESS180S__NON_GIT_ARTIFACTS32MIB__OLD_READ12_FILES_2MIB**。
**NEW_SCIENTIFIC_HA/HJB/KFE/SELECTOR/ROOT/GE/IRF/REAL_C8=0**。
**NON_GIT_POPEN_PERMISSION=0__NO_ARBITRARY_SPAWN__ORIGINAL_GIT_FIVE_CHILD_CAPABILITIES_PRESERVED**。
**OPTIONAL_REVIEW_REF=review/ch5-temp-v010-m1-platform-syscmd-20261017**。

Owner在上一[正式限域主审](versions/0.0.10/m1_v13_io_network_n13_partial_local_only_review_20261017.md)后明确批准新的集中工程修复。此前的真实工程进展：70份模型原raw/三init核证、IO缺失缓存探测窄修、socket.gethostname安全分类，N13活进程4.039秒超时/回收本地报告通过；canonical仍被Python `platform._syscmd_ver` 的未授权 `subprocess.Popen` 于创建前触发`GIT_NO_CAPABILITY`阻断，九监测模块与真实runner未运行。原执行Popen的具体callsite/参数真实字节没有认证；**不能盲猜命令、开放任意spawn或对系统stdlib注入伪平台版本值**。N13已有本地证据，不要求每轮重复，除非新runner改动Job/timeout/reader机制。

此次唯一授权：V1.3先只读路径Preflight、创建全新独立scratch并再次核验后首写→以固定Git模型Commit的70原始字节/独立Stage A只读源身份复核→精确取证当前Python stdlib`platform._syscmd_ver`真实Popen来源/意图与参数类型→仅当原值可验证等价、无spawn风险时尝试**新scratch中有来源、有原字节hash的工程版本元数据兼容适配器**→真实canonical import-only并区分`NATIVE_UNMODIFIED`与`SCOPED_METADATA_ADAPTER_ONLY`，九模块/runner工程测试仅在先决安全通过后执行。不能为PASS关闭Popen/网络/IO身份的DENY。GitHub证据交付可选，只对本轮安全脱敏材料一次审阅尝试，失败本地结果保持原证据级，不授独立远端或科学PASS。全部限额详见首次发行冻结任务全文。

旧B/S/L首版raw/run_id缺失`LEGACY_SEAL_CHAIN_UNVERIFIABLE`，时间戳上轮24/25+1 `SPEC_UNRESOLVED`与历史执行代码字节UNKNOWN、最早sanitize拒绝材料`PUBLICATION_DENIED`、旧ledger偏差不受本任务改写。上一任务Python6/8剩余2次及Git网络额度STOP不可结转；新本轮是**独立新预算**。

V010原MATLAB corrected两资产HA/HJB/KFE→多省手动有界顺序→GovInv收益边界×0.9/1.1和Zt→冻结GDP每省误差≤1%→原lagged-NKPC递推、目的地税一次、same-S/前完整轮raw ra0、家庭人均/省财政总量及三劳动账、phi_max=.3、20×20×2原网格与阈值照旧。Owner corrected HA单点仍UNTESTED。原D盘8dirty/index/staged/untracked/ignored/外Git common-dir、C盘物理独立SSD原备份、全部旧失败原件、真实C8/2017/2018/B3/V009资产保护不变。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、real C8 A–D REQUEST_ONLY持续。
