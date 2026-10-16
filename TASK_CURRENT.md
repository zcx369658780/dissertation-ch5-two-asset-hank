# TASK_CURRENT：V010 Windows Stage B–E ENGINEERING_ONLY runner I/O预检

更新：2026-10-16（Asia/Shanghai）。
**ACTIVE_TASK=V010_RUNNER_IO_WINDOWS_ENGINEERING_STAGE_B_E_PREFLIGHT**。
**STATUS=ISSUED__WAIT_CODEX_DELIVERY**。
**AUTHORITY=OWNER_20261016_CONTINUE_ENGINEERING_ONLY__NO_HA_SCIENCE**。
**NEXT_STOP=WAIT_ASTRA_V010_RUNNER_IO_WINDOWS_BE_REVIEW / STOP**。

正式唯一[冻结任务原文](versions/0.0.10/runner_io_windows_engineering_stage_b_e_preflight_task_20261016.md)：发行commit `7ec7eae170ae744b6c1b8321c434baf565e9ef7c`，tree `41da24010c732866988360bd1c01107a4e88f20c`，task blob `72f3b503ce5f468b8f80c2cb9cb16497a4b5b75f`。**已经发布，不得因会话交接而重发或改SHA。**

前置Stage A独立限域验收和GitHub交付恢复均完成；[远端验收补遗](versions/0.0.10/stage_a_github_publication_recovery_followup_review_20261016.md)确认candidate `d84cc76b19cbb81e097f502348b5073633fbda6e` / tree `5a03f952ba471352a685b327e79a33176e8bd7b6` / sole parent `68530b3f121952b4382d08dc9ff964c7f6c7ab75`、恰2文件及原上传bytes/SHA256完全一致。原SSH第一次push失败保留历史，本机认证细节只Codex自报。

新工程权限只在**新scratch且只读复用既有独立Stage A clone**下生效：工程Python累计≤4（AST≤1、纯工程负例≤1、真实runner≤2），每个外部wall≤180秒、任务总≤3h、全部新非Git工件≤32MiB、独立review元数据Git空间≤1GiB；runner每次Git child最多5条精确只读身份/inventory，无模型clone/fetch、无重跑Stage A、无旧额度结转。预运行源磁盘身份及Git common-dir再次验证；检查真实Windows argv/audit、Job Object kill/reap、双PIPE有界、写前quota/final与emergency保护、唯一可信hook来源、九源码loader，只在ENGINEERING_ONLY中运行，ONE_HA始终拒绝。

**HA/HJB/KFE/selector/roots/GE/IRF/MATLAB/pytest/真实C8=0**；旧两次单点Python1/1、首次超额、8dirty/index/common-dir旧证据均不动。唯一新候选review分支`review/v010-runner-io-windows-engineering-b-e-20261016`，发行commit唯一parent，至多3份脱敏文件普通nonforce推送一次/远端回读，失败LOCAL_ONLY STOP。终态`WAIT_ASTRA_V010_RUNNER_IO_WINDOWS_BE_REVIEW / STOP`，Codex不得自授正式工程PASS或科学权限。原V010冻结合同、Results FALSE、A16/window/C9/CALL_LEDGER、real C8和V011 NOT_STARTED不变。
