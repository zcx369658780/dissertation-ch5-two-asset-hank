# 第五章 CURRENT：V010 Stage A GitHub交付恢复，Windows ENGINEERING_ONLY Stage B–E 已正式签发

更新：2026-10-16（Asia/Shanghai）。
**ACTIVE_TASK=V010_RUNNER_IO_WINDOWS_ENGINEERING_STAGE_B_E_PREFLIGHT**。
**STATUS=OWNER_CONTINUE__NEW_ENGINEERING_ONLY_TASK_ISSUED__WAIT_CODEX_DELIVERY**。
**PERMISSION=WINDOWS_ENGINEERING_PYTHON_MAX_4__REAL_RUNNER_MAX_2__NO_SCIENCE**。
**NEXT_STOP=WAIT_ASTRA_V010_RUNNER_IO_WINDOWS_BE_REVIEW / STOP**。

**Stage A正式交付与审议已闭合**：原[Stage A限域独立验收](versions/0.0.10/stage_a_git_reachability_uploaded_primary_review_20261016.md)保留9份远端源码Git Blob/SHA256/字节复算9/9；新[GitHub恢复补遗](versions/0.0.10/stage_a_github_publication_recovery_followup_review_20261016.md)已真正核review ref`review/v010-stage-a-model-ref-reachability-20261016`→commit `d84cc76b19cbb81e097f502348b5073633fbda6e`、tree `5a03f952ba471352a685b327e79a33176e8bd7b6`、sole parent原Stage A发行commit `68530b3f121952b4382d08dc9ff964c7f6c7ab75`，仅2份白名单文件，远端字节SHA256分别`A1DFCAA8FAEA7A1A257D119A54F2AFBA4911FDC705B5B589B08239316F5C26F8`（6190B）、`C6593C9C1B1B0DD8FB84A52D3D93C242F01311F359A0F574E43FE9357CE66ABC`（15107B），与此前上传完全一致。`GITHUB_DELIVERY_VERIFIED`，原第一次push失败历史仍保留，SSH443本机认证/是否改global Git config仅Codex报告。Stage A只是`DOCUMENTARY_LIMITED_ACCEPT`，未成为本机Windows runtime认证。

**Owner本会话“补上GitHub验收，然后继续”已被限域为独立新ENGINEERING_ONLY预检任务**：唯一已发行[Stage B–E冻结task](versions/0.0.10/runner_io_windows_engineering_stage_b_e_preflight_task_20261016.md)，发行commit `7ec7eae170ae744b6c1b8321c434baf565e9ef7c`、tree `41da24010c732866988360bd1c01107a4e88f20c`、task blob `72f3b503ce5f468b8f80c2cb9cb16497a4b5b75f`。**已签发不重发**；只读复用Stage A既有独立model clone，先验身份与九源码bytes；禁止新模型clone/fetch、原dirty树或旧失败目录写操作。最多**4个新的工程Python进程（AST≤1、纯负例harness≤1、真实Windows runner≤2）**，各≤180秒，总任务≤3小时，新非Git工件≤32MiB，独立Git review发布元数据≤1GiB；无数学/模型源码修改。`HA/HJB/KFE/selector/root/GE/IRF/MATLAB/pytest/real C8`严格0，ONE_HA无条件拒绝；不得挪用前一次STOP工程Python0/4。

原V010计划commit`bf091da33d59293f147d52c11580327d3ac2a85d`/blob`85138d8859d53295262fe13bf5bc277bca95ed3f`、合成fixture`40915658d93403cfc21b33a6b864b332b7857749`、单点manifest`c23d331bed34e5ca478324cdc05034609ecb91b7`仍冻结。真实第五章研究方向：纠正原MATLAB两资产条件HA→多省顺序单轮→原GovInv收益边界0.9/1.1与Zt自适应→原冻结目标GDP≤1%门→原lagged-NKPC递推冲击，保留同一S、lagged raw ra0、目的地工资税一次及人均/省总量和家庭/企业劳动分账。

**旧账和锁定不变**：初始实施Codex报告pytest4/6、science driver1/4、HA1/26、selector1626、roots1642；两次单点preflight各Python1/1 HA0，首笔43,519,638B超旧32MiB 9,965,206B；前一工程preflight因stage A checkout128 FAIL_CLOSED、未耗Python0/4不结转；随后Stage A Git-only已经交付。现在完整runner I/O仍`BLOCKED`、单点corrected HA `UNTESTED`、`ENGINEERING_RUNTIME_NOT_RUN`、`HA_SCIENCE_NOT_RUN`、`model_activation=False`、`Results FALSE`、`V011 NOT_STARTED`。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、真实C8 A–D REQUEST_ONLY、原8dirty/index/staged/untracked/ignored/外Git common-dir及旧失败原证保护不变。GitHub不自动同步本机QMD/Basic Memory；V1.2工作流不变。
