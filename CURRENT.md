# 第五章 CURRENT · V010 工程证据到合成科学的长任务（科学阶段待释放）

**2026-10-17最新会话交接（Owner要求GitHub永久保存）：** [V010 Stage A生效、Stage B冻结以及Owner决策的完整交接](docs/CH5_CONVERSATION_HANDOFF_20261017_V010_VERSION_LONG_TASK_STAGE_A.md)。本轮交接不新增任务、不替换冻结Task Commit/Blob，不开放科学求解；后续仅按原任务接续。


2026-10-17（Asia/Shanghai）Owner明确请求继续下达版本任务，V1.3单张版本长任务生效；不启动V011。
**WORKFLOW=V1.3__VERSION_LONG_TASK__NO_MICROTASK_SPLIT**。
**RESEARCH_VERSION=V010/V0.0.10；V011 NOT_STARTED**。
**ACTIVE_TASK=V010_M1_EVIDENCE_AND_CONDITIONAL_SYNTHETIC_MAINLINE_LONG_TASK**。
**FIXED_ISSUE_COMMIT=54454066859692a0f481cfa44de8df8dc298ce03；FIXED_TASK_BLOB=5d87753b4a3ac972f37f1ac59722b464efd11bd9**。
**TASK=[固定单任务全文](versions/0.0.10/v010_m1_evidence_conditional_synthetic_mainline_long_task_20261017.md)**。
**STAGE_A=ACTIVE__RAW_M1_NINE_EVIDENCE_AND_NON_SOLVER_PREP_AUTHORIZED**。
**STAGE_B=SYNTHETIC_SCIENCE_FROZEN_CONDITIONAL_NOT_RELEASED**。
**SCIENCE_RELEASE=ONLY_AFTER_ASTRA_INDEPENDENT_M1_EVIDENCE_REVIEW_AND_SIGNED_SYNTHETIC_PRECONDITION_PASS**。
**STOP=WAIT_ASTRA_V010_M1_M2_SYNTHETIC_MAINLINE_REVIEW / STOP**。
**FULL_RUNNER_IO_CLOSURE=BLOCKED；model_activation=False；Results FALSE；V011 NOT_STARTED**。

**FIXED_V010_PLAN_COMMIT=bf091da33d59293f147d52c11580327d3ac2a85d；PLAN_BLOB=85138d8859d53295262fe13bf5bc277bca95ed3f**。
**FIXED_MODEL_COMMIT=94de4501dec051b969bee9d852eba2d4591f30ef；MODEL_TREE=205eab47c4e4f9c6292c2ead9947d94d1a7579a5**。
**FIXED_SYNTHETIC_FIXTURE_BLOB=40915658d93403cfc21b33a6b864b332b7857749**。
**STAGE_A_LIMIT=ENGINEERING_ONLY__PYTHON16__WALL4H__ARTIFACTS64MIB**。
**STAGE_B_BUDGET_NOT_RELEASED=MAX_HA26__PYTEST6__SCIENCE_DRIVER4__SCIENCE_WALL8H__ONLY_FROZEN_TWO_PROVINCE_SYNTHETIC**。
**CURRENT_SCIENTIFIC_RUNTIME_PERMISSION=0__HA/HJB/KFE/selector/root/GE/IRF/REAL_C8_0**。

Owner已上传并经Astra独立SHA验证上一M1长任务`DELIVERY_RECEIPT.json`（5,875B、SHA256`E100A61CA00DBD510FF8C7E9417EB2C2663E66C73AEBEDD81B6581A85BF36F50`）及`DELIVERY_SUMMARY.md`；但九份原始工程证据尚未到ChatGPT独立审查。[最新增级审议](versions/0.0.10/m1_v13_consolidated_uploaded_delivery_receipt_independent_sha_addendum_20261017.md)确认这不是M1完整Windows runner原证独立PASS。`SCOPED_ADAPTER_ONLY` canonical与九模块及runner仍仅本机报告，原生导入受GIT能力门阻断；early Git prelaunch snapshots缺失、N13原streams_complete字段错误与派生修正/历史seal缺失不能回填。

**本轮Stage A** Codex一次性从旧可信回执已列的九个原件取`size/SHA256`逐个复算，将原始文件字节打包为单个供Owner上传ChatGPT的ZIP；若原raw含敏感信息，只能另标SANITIZED_DERIVATIVE不能冒充原证。并在同一总工程预算内独立准备V010 fixture/stub/公式非求解测试，冻结15路径以内的源码diff与科学前置审计。普通工程bug自主修复、不再拆证据转运微任务。达到A4独立审议释放才可在**同一TASK_ID**内继续Stage B，未经Astra签出明确科学前提PASS，HA/selector/root=0，不凭本地工程哈希自授科学权限。

**Stage B（冻结、尚无执行权）**原V010唯一双省synthetic fixture，依plan先两个同输入HA，再最多5轮×2有界outer、冻结Zt/GovInv后2 HA readback、最后短3期×2零路径/TFP递推合计≤26 HA，原HJB/KFE双门、财政/税一次/same-S/lagged raw ra0/GDP各省≤1%和资源原阈值不改；任何失败STOP，`Results FALSE`与现实GE FALSE不变。Owner给定价格HA额外候选未被这份fixture许可，仍UNTESTED。

原C盘独立SSD备份、D盘8dirty/index/staged/untracked/ignored与外Git common-dir、所有旧失败scratch、真实C8/2017/2018/B3/V009原证严格保护。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、real C8 A–D REQUEST_ONLY持续。旧全部STOP资源不结转。本轮旧证ZIP可人工上传一次，不强迫SSH443重试，避免GitHub失败妨碍科学准备。
