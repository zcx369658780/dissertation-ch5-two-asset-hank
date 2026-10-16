# TASK_CURRENT：V010 bare Git身份与脱敏拒绝单点SOURCE_ONLY取证

更新：2026-10-16（Asia/Shanghai）。
**ACTIVE_TASK=V010_BARE_COMMON_DIR_AND_SANITIZATION_SOURCE_ONLY_FORENSIC**。
**FIXED_ISSUE_COMMIT=5b66d6e3c0b3ad6e292009e13bbe9c19472dde1e；FIXED_TASK_BLOB=085412aaee3df3067540c4336ff37eb4b07f9383**。
**TASK_FILE=[本轮唯一冻结任务](versions/0.0.10/bare_common_dir_sanitization_source_only_forensic_task_20261016.md)**。
**CLASS=READ_ONLY_FORENSIC + SOURCE_ONLY_DRAFT；STOP=WAIT_ASTRA_V010_BARE_SANITIZATION_SOURCE_ONLY_REVIEW**。
**RUNTIME_AUTHORITY=READ_ONLY_GIT_IDENTITY_PROBES_MAX4_IF_REQUIRED__PYTHON0__RUNNER0__E0_RETEST0__MKTREE0__FETCH0__PUSH0__SCIENTIFIC_HA0**。

Owner在新会话明确同意继续调查上一轮`BARE_COMMON_DIR`身份失败与脱敏扫描DENIED。Codex只能在新独立scratch`D:\ProjectTemp\ch5_v010_bare_sanitize_forensic_20261016_01`中读取上一失败scratch精确最多8份小文件（累计≤2MiB），wall≤90分钟，新scratch≤4份UTF-8/LF平铺小文件总≤512KiB（回执保底预留≥64KiB），不得触写旧失败原证/模型树/受保护Git common-dir/C盘备份。优先静态证据，若旧原件缺少git输出且旧独占bare身份/位置已安全认证，才可最多4次新的只读Git身份探针，绝不运行mktree/重做E0/再次扫描或发布。结果须区分expected/observed有无原证，路径/cwd/env根因UNKNOWN与真实共享证明，脱敏规则ID/匿名字段分类与误报待核，明确未运行事项。

上一`V010_E0_LAUNCHER_UINT32_AND_TEMP_MKTREE_CORRECTION`（commit`e474c0d25a7351b7510f6a9ba914cd8733dceffc`、blob`a3683c751acf08d49d700422a63f264b61130e78`）已经FAIL_CLOSED / LOCAL_ONLY / STOP，正式[主审](versions/0.0.10/e0_launcher_mktree_fail_closed_local_only_primary_review_20261016.md) Blob`3f675de31449ce946a2ecb3b51ed6c9a55850197`。历史旧额度一律不可继承。原本机回执SHA256（Owner转述尚未独立重算）`AC06ECCFAA023AC4593017CC18C4AD4FAC644BC52C00FA2F71B5FD82C54C4816`，前次E0局部成功仅`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，原mktree从未运行。

**本次Codex GitHub发布一律不授权**：原bare与脱敏两门正是取证对象，需输出短于约4KiB的严格脱敏最终摘要供Astra独立评估；被拒原材料不上传，后续任何真正工程复测、GitHub发布、Python/HA科学进程必须再由Owner分别授权。HJB/KFE、GovInv/Zt、经济模型、原冻结plan/model候选、真实C8、Results FALSE、V011 NOT_STARTED、A16 FAIL_CLOSED/window UNACCEPTED/C9 PAUSED/CALL_LEDGER UNRESOLVED及原8dirty/index/external common-dir/C备份均不改。任务完成或受限失败后`WAIT_ASTRA_V010_BARE_SANITIZATION_SOURCE_ONLY_REVIEW / STOP`，不自行派后继。
