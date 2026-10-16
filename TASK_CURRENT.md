# TASK_CURRENT：V010 E0 Launcher UInt32 + 独占bare Git mktree工程修复

更新：2026-10-16（Asia/Shanghai）。
**ACTIVE_TASK=V010_E0_LAUNCHER_UINT32_AND_TEMP_MKTREE_CORRECTION**。
**FIXED_ISSUE_COMMIT=e474c0d25a7351b7510f6a9ba914cd8733dceffc**。
**FIXED_TASK_BLOB=a3683c751acf08d49d700422a63f264b61130e78**。
**TASK_FILE=[正式唯一冻结任务](versions/0.0.10/e0_launcher_uint32_temp_mktree_correction_task_20261016.md)**。
**SCOPE=ENGINEERING_ONLY_E0_AND_GIT_PUBLICATION_ONLY**。
**RUNTIME_AUTHORITY=POWERSHELL_E0_MAX2__NEW_BARE_SYNTHETIC_MKTREE_MAX2__PYTHON0__RUNNER0__HA0**。
**STOP=WAIT_ASTRA_V010_E0_LAUNCHER_MKTREE_CORRECTION_REVIEW / STOP**。

这是Owner在2026-10-16新会话要求正式交接后立即下达的**新任务**，不是重发旧 `01129efd5220683d415bd1486f23f6ecd068cb53` 已STOP任务。新任务只修复Launcher UInt32的参数类型/边界与Git mktree输入空行；检查独立source_assembly_root E0保护门、最多2次PowerShell E0试验及新独占bare合成tree最多2次工程验证，严禁调用Python/pytest/AST模型导入、VerifiedLoader/真实runner或科学求解。旧工程0/6 Python、0/2 runner额度全部随前任务STOP关闭，**不结转**；本任务没有新Python额度。

唯一新独占scratch `D:\ProjectTemp\ch5_v010_e0_launcher_mktree_20261016_01`；非Git新增物理工件≤16MiB（终态预留≥1MiB）、新独占bare Git对象≤1.5GiB、wall≤2.5h，冻结Git只读命令≤100，模型clone/fetch/checkout=0。只允许严格合规的新review `review/ch5-temp-v010-e0-launcher-mktree-20261016` 分支，远端tree路径 `_review_tmp/ch5/v010-e0-launcher-mktree-20261016/` 下三件脱敏文件：`result.md`、`manifest.json`、`correction_draft.txt`；本地项目worktree/index不得出现该临时目录。候选commit唯一parent为本任务发行commit `e474c0d25a7351b7510f6a9ba914cd8733dceffc`，新bare准备完整发行基线、严格SSH key/443、最多一次nonforce push且需远端SHA/tree/blob回读；失败LOCAL_ONLY/STOP不重试。**不得补推上个失败review分支**。

上一[独立E0主审](versions/0.0.10/trusted_loader_e0_fail_closed_local_only_primary_review_20261016.md) Blob `d9d5a3ea38fcff89633ce09fdf0d97d9e9e61293`，上一[交接](docs/CH5_CONVERSATION_HANDOFF_20261016_TRUSTED_LOADER_E0_LOCAL_ONLY_STOP.md) Blob `7865222ca9966720b9cc335a4e41facfc9a7fc8e`。旧E0报告70文件本机装配但UInt32失败；mktree exit128/candidate0/push0；工程Python0/6、runner0/2；本地结果尚未独立取字节。旧科学合同、原单点HA UNTESTED、A16 FAIL_CLOSED/window UNACCEPTED/C9 PAUSED/CALL_LEDGER UNRESOLVED/Results FALSE/model_activation=False/real C8 REQUEST_ONLY、原8dirty/index/common-dir、V011 NOT_STARTED不变。

**交付ID=V010_E0_LAUNCHER_UINT32_TEMP_MKTREE_CORRECTION_RESULT；等待Codex结果后由Astra独立审议。** 任何以后ENGINEERING Python或独立HA科学进程都需要Owner新授权。
