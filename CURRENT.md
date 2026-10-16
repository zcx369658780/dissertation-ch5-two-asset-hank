# 第五章 CURRENT：V010 BARE_COMMON_DIR与脱敏拒绝单点取证任务已签发

更新：2026-10-16（Asia/Shanghai）。
**VERSION=V010/V0.0.10；ACTIVE_TASK=V010_BARE_COMMON_DIR_AND_SANITIZATION_SOURCE_ONLY_FORENSIC**。
**ACTIVE_TASK_FIXED_COMMIT=5b66d6e3c0b3ad6e292009e13bbe9c19472dde1e；TASK_BLOB=085412aaee3df3067540c4336ff37eb4b07f9383**。
**TASK=[SOURCE_ONLY取证冻结任务](versions/0.0.10/bare_common_dir_sanitization_source_only_forensic_task_20261016.md)**。
**TASK_SCOPE=READ_ONLY_FORENSIC_AND_SOURCE_ONLY_DRAFT**。
**TASK_BUDGET=MAX90MIN__READ_MAX8_FILES_2MIB__READONLY_GIT_IDENTITY_PROBES_MAX4__NEW_SCRATCH_MAX4_FILES_512KIB**。
**NEW_PYTHON=0；MODEL_IMPORT=0；REAL_RUNNER=0；MKTREE=0；GIT_FETCH/PUSH/COMMIT=0；HA/HJB/KFE/GE/IRF/REAL_C8=0**。
**LAST_DELIVERY=V010_E0_LAUNCHER_UINT32_TEMP_MKTREE_CORRECTION_RESULT__FAIL_CLOSED__LOCAL_ONLY**。
**LATEST_INDEPENDENT_REVIEW=GITHUB_NO_E0_REVIEW_REF_VERIFIED__LOCAL_E0_PROOF_UNVERIFIED**。
**NEXT_GATE=WAIT_ASTRA_V010_BARE_SANITIZATION_SOURCE_ONLY_REVIEW / STOP**。
**FULL_RUNNER_IO_CLOSURE=BLOCKED；HA_SCIENCE_NOT_RUN；model_activation=False；Results FALSE；V011 NOT_STARTED**。

Owner本次明确同意对前次两个阻断项开展一次新的、小范围只读取证，不授权纠错方案的实际执行。目标一为`BARE_COMMON_DIR`身份门的expected/observed、调用参数/路径归一化与真实共享风险；目标二为脱敏封存拒绝的规则ID/匿名字段类别/最小可安全交付构想。先用上轮既有本机回执做静态核查，缺关键输出且旧独占bare身份路径安全可证时，才允许最多4次read-only Git `rev-parse`身份探针。**禁止mktree、重新封存、Git发布、Python/模型或旧任务重试。** 本次因原发布和脱敏链未通过，Codex只给最小脱敏摘要及LOCAL_ONLY文件，GitHub临时review发布不授权。

原E0主审[永久归档](versions/0.0.10/e0_launcher_mktree_fail_closed_local_only_primary_review_20261016.md) Blob`3f675de31449ce946a2ecb3b51ed6c9a55850197`；上一冻结任务commit`e474c0d25a7351b7510f6a9ba914cd8733dceffc`/blob`a3683c751acf08d49d700422a63f264b61130e78`已STOP。Codex上次报告UInt32修复24例匹配、PowerShell E0一次局部PASS但bare身份和脱敏DENIED，mktree/fetch/push/Python/runner/HA0；D盘回执SHA256 `AC06ECCFAA023AC4593017CC18C4AD4FAC644BC52C00FA2F71B5FD82C54C4816`此前仅Owner转述、未独立重算。旧预算包含该E0任务的剩余E0 1/2、mktree 0/2及前一个工程Python 0/6、runner 0/2，全部关闭**不结转**。

冻结科学plan commit`bf091da33d59293f147d52c11580327d3ac2a85d`/blob`85138d8859d53295262fe13bf5bc277bca95ed3f`及模型代码commit`94de4501dec051b969bee9d852eba2d4591f30ef`/tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`保持不变。corrected单点HA（rah=.0675、w_eff=15.5、rb=.02、Tt=.1、rb_gap=.07）未真正运行；原双省F-order25`NO_ADMISSIBLE_POLICY`，外层GE/正式IRF/Results未合格。原GovInv收益边界×0.9/1.1、Zt、GDP冻结目标≤1%、目的地工资税一次、same-S及lagged raw ra0、phi_max=.3、人口/劳动分账、lagged-NKPC主线不改；V008/V009人工Newton仅历史研究。

保护原`D:\ProjectTemp\c5k1bturn56`的8 dirty、index/staged/untracked/ignored、外Git common-dir、全部历史失败目录、C盘现有独立SSD备份、真实C8/2017/2018/B3。Owner双备份+C/D独立SSD、Codex SSH Key/443与可信工作站VerifiedLoader风险决定不变；远端review tmp不得进入本地项目worktree/index。**A16 FAIL_CLOSED；window UNACCEPTED；C9 PAUSED；CALL_LEDGER UNRESOLVED；real C8 A–D REQUEST_ONLY；Results FALSE；V011 NOT_STARTED**。GitHub发布文档不等于QMD/Basic Memory自动同步。
