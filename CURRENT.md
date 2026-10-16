# 第五章 CURRENT：V010 Stage A 模型Git对象可达性修复任务已签发

更新：2026-10-16（Asia/Shanghai）。
**ACTIVE_TASK=V010_STAGE_A_FROZEN_MODEL_GIT_OBJECT_REACHABILITY_RECOVERY**。
**STATUS=OWNER_AUTHORIZED__TASK_ISSUED__WAIT_CODEX_DELIVERY__GIT_STAGE_A_ONLY**。
**PERMISSION=POWER_SHELL_AND_EXACT_SCOPED_GIT_ONLY__PYTHON_0__HA_0__NO_RUNNER**。
**TERMINAL_WHEN_DELIVERED=WAIT_ASTRA_V010_STAGE_A_GIT_OBJECT_REACHABILITY_REVIEW / STOP**。

本次Owner明确批准了上一轮独立审议建议的**新Stage A Git对象可达性单点修复**；冻结任务 [stage_a_model_git_object_reachability_recovery_task_20261016.md](versions/0.0.10/stage_a_model_git_object_reachability_recovery_task_20261016.md) 在commit `68530b3f121952b4382d08dc9ff964c7f6c7ab75`、tree `70a7662ba654dff6acbe05e3a8b0444324b8f346`、task blob `3688674363aa8a0c45a7a322c9c2098baed62fae`。**任务已发布，不得重发或从旧任务偷取余额。** 仅解决错误以治理branch single-branch clone，未取得冻结模型代码tree的Stage A准备故障；目标是1个新隔离model-branch clone，实际取得固定commit/tree/parent和9份磁盘源码Git blob，证明Git common-dir不与旧保护树共享。固定远端分支 `codex/ch5-v010-matlab-first-20261015`，HEAD `94de4501dec051b969bee9d852eba2d4591f30ef`、tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`、sole parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e` 已由Astra实际查GitHub证实，但**本轮Windows本机验证尚未发生**。

**新资源独立账**：Stage A一次全新模型clone；模型网络限一次ls-remote＋一次正确分支clone，阶段A失败后不准补fetch/重clone；加脱敏GitHub文档发布的受界对象获取须另行计账；新Git对象/checkout与可选review发布元数据合计≤2GiB，新非Git artifact≤16MiB，任务wall≤2h。所有`Python/py/Jupyter/import/py_compile/pytest/HA/HJB/KFE/selector/root/GE/IRF/real C8/MATLAB/runner`调用严格0。只许可Git/PowerShell/静态文件哈希；修复结果若通过也不批准Windows runner Stage B-E或科学HA。

**前一任务历史结论（已结束）**：`V010_RUNNER_IO_ENGINEERING_ONLY_WINDOWS_PREFLIGHT` 在A阶段clone只取治理分支，checkout失败exit128后STOP；review commit `416cff6c00d2b865c3e9dda4088242d2b80969ce`、tree `1d5bc390774d68ea619f6ad263c99d0090486b37`。Astra独立 [FAIL_CLOSED审议](versions/0.0.10/runner_io_engineering_preflight_fail_closed_primary_review_20261016.md) blob `7ba0991b76bc2d5304f78c7e7ddb5d0c8f746b96`；69例全部NOT_EVALUATED，工程Python0/4/科学HA0为Codex本地报告，**原已经STOP的4次工程许可不结转**。`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`ENGINEERING_RUNTIME_NOT_RUN`、单点corrected HA `UNTESTED`不变。

**科学与长期保护不变**：原V010冻结plan commit `bf091da33d59293f147d52c11580327d3ac2a85d`/blob`85138d8859d53295262fe13bf5bc277bca95ed3f`、synthetic fixture blob `40915658d93403cfc21b33a6b864b332b7857749`及单点manifest blob`c23d331bed34e5ca478324cdc05034609ecb91b7`不改。原MATLAB主线为修正HA→多省顺序单轮→GovInv收益边界×0.9/1.1与Zt有界迭代→独立目标GDP≤1%验证→原lagged-NKPC递推；same-S、lagged raw ra0、目的地工资税一次、家庭/财政总量与劳动分账保留。原实施预算Codex报告pytest4/6、science driver1/4、HA1/26、selector1626、roots1642；两次单点preflight各Python1/1、HA0，首次43519638B超旧32MiB 9965206B永久保留。

`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`model_activation=False`、`Results FALSE`、real C8 A-D REQUEST_ONLY、原8dirty/index/staged/外common-dir/untracked/ignored保护、`V011 NOT_STARTED`不变。旧证据只读且不可删除或覆盖。QMD/Basic Memory未因GitHub同步自动更新；V1.2工作流未改变。
