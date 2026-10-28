# TEMP31工作地tau_j单次征税：生产调用链静态闭合与最小集成设计（单张冻结任务）

TASK_ID=CH5_TEMP31_WORKPLACE_TAUJ_PRODUCTION_CALLPATH_STATIC_GATE_R1_20261028
STATUS=OWNER_AUTHORIZED_ISSUED_AWAITING_LOCAL_CODEX
OWNER_DIRECTION=2026-10-28_CONTINUE_TEMP31_MODEL__DEFER_D_DRIVE_CLEANUP
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=b6ff1620ae4740a729bacc78b79b3e9c85f850ae
TASK_PUBLICATION_COMMIT=THIS_CONTRACT_CREATION_COMMIT__VERIFY_ON_REMOTE_READBACK
CANDIDATE_BRANCH=codex/ch5-temp31-worksite-tauj-production-callpath-static-20261028-r1
FIXED_PARENT=b6ff1620ae4740a729bacc78b79b3e9c85f850ae
SOURCE_COMMIT=b6ff1620ae4740a729bacc78b79b3e9c85f850ae
SOURCE_TREE=GITHUB_CONNECTOR_DID_NOT_EXPOSE_ROOT_TREE_SHA__MANDATORY_EXACT_GIT_PREFLIGHT_BEFORE_WORK
TASK_PATH=tasks/CH5_TEMP31_WORKPLACE_TAUJ_PRODUCTION_CALLPATH_STATIC_GATE_R1_20261028/
DELIVERY_MODE=GITHUB_CANDIDATE_BRANCH_SSH
AUTO_ISSUE=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 唯一目的及验收问题
只用固定GitHub源码，梳理TEMP31“目的地/工作地tau_j、同一份劳动收入税仅应用一次”的实际生产数据流和最小可实施接口修正方案，提供Owner可裁决的公式/方向/税基与合成测试合同。不执行修正、不做任何科研计算。本任务不是R2/R3已有隔离验收的重复，不寻找D盘Excel，也不延伸P3/WASM检查。

要回答：现有生产链哪些节点仍用origin tau、哪些用destination tau、家户实际接受gross还是net综合工资、财政工资税收入是否含工资税基及方向、双重扣税在何种条件下成立？为每个结论给出真实代码语句位置和“已证事实/条件风险/需Owner裁决”标记。提出最小修改位置与可失败的2省非对称测试设计，供后续单独授权实现。

## A. 冻结源身份与硬前置
所有远端文件必须从SOURCE_COMMIT精确读取，禁止隐式采用更新HEAD、默认分支或工作树不明版本。连接器已独立固定以下Git Blob（**Git Blob不是原字节SHA-256**）：

1. src/ch5_two_asset_hank/multi_province/wage.py — 48001b2e4ca64d81dda6174255f6ccf130e07004
2. src/ch5_two_asset_hank/multi_province/migration_labor.py — e6fd216aeda40b9b477c0f0e16332e6366b66900
3. src/ch5_two_asset_hank/multi_province/one_turn.py — 621c8e2dfaf5f55eda39c9b9bffb22cd52ee451f
4. src/ch5_two_asset_hank/multi_province/firm.py — 1f7d37247e2d712fc0477a9f562dce81d1b367ce
5. src/ch5_two_asset_hank/multi_province/fiscal_diagnostics.py — c24bbda9ea88c1581eeed6d734062b30d13def2f
6. src/ch5_two_asset_hank/multi_province/stationary_runtime.py — 8717cfa759948bd1ad3c8cd788f8f4736f250598
7. src/ch5_two_asset_hank/multi_province/steady_state.py — 5c5b56e6a2eb82fab4e80eb7b8e5bbbf97f08c22
8. validators/multi_province/mp4c_python_annual_empirical.py — d2e74cb8b491489053dcde525cd4d83cb4bd0b3a
9. validators/multi_province/mp4c_python_annual_production.py — 7473e04418744d745000afb21d84588273cc5bca
10. validators/multi_province/mp4c_run_full_annual_batch.py — 599202c39a358b78c4115dcb1e5886021f388389

只读治理合同：docs/CH5_GITHUB_WORKFLOW_AUTHORITY_CURRENT_20261025.md（Blob f98324985f5ebe2a42ec979a61604543a96bb52a）、docs/CH5_INDEPENDENT_REVIEW_RULES_20261025.md（Blob 89017c798dbee6b5f9b31ccb88b5b9008a064cbf）、docs/CH5_SESSION_HANDOFF_CURRENT.md（Blob 507a386c322453a570f8bd79ae1492b3ff6f35cc）、本CONTRACT。其他历史任务只可引用既有审阅定论；需要打开未列明文件时STOP并登记缺口，不得搜索整仓或扩大源码路径。

MANDATORY PREFLIGHT: 从已授权**治理隔离环境中的固定Git对象**获取SOURCE_COMMIT的唯一parent及root tree SHA，回读10份Source Blob，使用标准库分别计算能取得原始字节的UTF-8/原字节bytes与SHA-256并写入source_identity.json；记录任务发布commit、parent、tree。任何来源/对象不可取、Git Blob不符、源tree不可认证、权限/平台拒绝，均STOP，标SOURCE_IDENTITY_PENDING，不继续实质审阅。不以猜测填tree，不将Git Blob误称SHA256。治理父提交与候选固定父可相同，任务发布提交不等于候选固定父。

## B. 静态审阅范围
B1 定向复核对照：
- wage.py 中目的地tau[destination]、sigma[destination,origin]及复合工资的定义和单位；
- migration_labor.py 的 tax_by_origin[origin] 和 destination-row/origin-column，含另一个normalized路径是否不同；
- one_turn.py、stationary_runtime.py、steady_state.py 到生产入口的**实际调用**，区分source-faithful和隔离候选；
- mp4c_python_annual_empirical.py 中 tau、w、wjt和N状态来源；production.py中的HA HouseholdInputs(tau,w)入参及结果回流；
- firm.py 的 Govinc=Corptax+Lt*tau+AtTax+GovInv*ra-Tt 与财政诊断所用量，明确其税基是否与工作地工资收入一致，勿未经经济学批准直接替换公式。
B2 单独给出“工资值是否已经税后”与“HA是否再次扣tau”的条件性证据矩阵：若固定源码不能证明HA最深层预算式或canonical实物，就标UNKNOWN/BLOCKED，不能把重复征税写成已经观察到的运行事实。
B3 产出Owner决策卡：tau归属工作地、迁移成本sigma归宿、gross/net边界、税基中的w_j z_i l_{ji}及N_i是否出现一次、每省和全国财政收入、Lt_mat轴方向。每项标既定Owner目标/代码事实/未决经济合同；不可自行确定税收归属、劳动人数和工资数据采用。
B4 最小实现设计：精确拟修改文件/函数/字段及不修改范围、源接口兼容策略和回滚路径；提供**仅设计不执行**的2省非对称反例与税率置换、sigma=0、tau=0、同一收入仅扣一次、矩阵行列和全国税收核算等测试断言。不得把拟议断言视为测试PASS。

## C. 本次预算/安全
SOURCE_CONTENT_READS_MAX=10 (listed pinned files only)
GOVERNANCE_DOC_READS_MAX=4
GIT_METADATA_PREFLIGHT_MAX=1_BOUNDED_ROUND
SCIENCE_BUDGET=0
TEST_BUDGET=0
PREFLIGHT_BUDGET=0 (no model preflight; only Git identity metadata)
MODEL_CALLS=0
HA_HJB_KFE_GE_IRF=0
STEADY_STATE_IRF_CALIBRATION=0
FORMAL_SOURCE_WRITES=0
SYNTHETIC_EXECUTION=0
D_DRIVE_DISCOVERY=0
WASM_REPARSE_FOLLOW=0
CLEANUP_DELETE_MOVE_COPY=0
WAGE_OR_NBS_ADOPTION=FALSE
HA_ORACLE_SHA_CHANGE=FALSE

科研工作树P3继续BLOCKED，旧status c443420c...及恢复观察734f1176...不允许重新绑定。严格禁止访问被保护的本地科研工作树、D盘版本目录、WASM或reparse目标；仅使用已授权GitHub固定对象与可证明独立的治理隔离目录。若工具/执行环境要求进入被阻塞工作树或出现任何保护异常则STOP，不以改凭据、路径或其他传输协议绕过安全门。无科研/模型源码提交、运行、安装依赖、更新git index、修改科学机制；候选分支只能新增本任务证据文件。

## D. 交付、三阶段审阅与终态
仅在独立候选分支任务目录新增：
- result.md（COMPLETED/BLOCKED/NOT_COMPLETED/NEXT_ACTION及明确STOP）
- source_identity.json（commit/parent/tree及10文件Git Blob/bytes/SHA-256，原始字节若不可取得须标缺口）
- callpath_evidence.md（实际短源码片段、准确行号、入口→调用链、事实/风险/UNKNOWN）
- tax_contract_decision_cards.md（不擅裁决经济口径）
- minimal_integration_and_test_plan.md（无执行的修正设计与反例断言）
- gap_register.md、privacy_report.md
- manifest.json（每项payload路径、bytes、SHA-256、Git Blob、provenance、purpose）
- DELIVERY_FINAL_RECEIPT.json（最终commit、parent、tree、diff范围、远端精确readback、预算/STOP）

SHA256用成熟标准库计算，Git Blob单独取得；manifest自身单检，避免自包含循环。来源完整性可审核不等于科学真实性。不得上传任何本地私人绝对路径、密钥、工资原始个人数据或WASM信息；只出必要公开源码摘录。仅普通已授权SSH发布独立候选，remote readback后STOP，**不自动Issue/PR、合并、清理、下张任务**。若SSH有权限/安全拒绝直接STOP。

GPT下一轮按A（固定提交parent/tree、Blob、bytes、SHA256和来源）→B（真实源码、经济学/实现风险）→C（artifact_integrity、source_identity、numeric_review、implementation_review、scientific_review、privacy_review、actual_terminal、delivery、cleanup、not_completed）独立审阅。无源原件或生产证据时最多PASS_BOUNDED，不发布Results、不激活模型。
ACTIVE_TASK=ISSUED_AWAITING_OWNER_TRANSFER
P3_OWNER_APPROVED=TRUE
PROTECTION_BASELINE=BLOCKED
FORMAL_SOURCE_FREEZE=FALSE
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE
FULL_RUNNER_IO_CLOSURE=BLOCKED
AUTO_NEXT=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
