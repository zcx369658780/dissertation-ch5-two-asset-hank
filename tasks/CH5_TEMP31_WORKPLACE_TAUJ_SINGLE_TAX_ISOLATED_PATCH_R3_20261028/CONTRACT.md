# TEMP31 工作地 tau_j / 单次扣税：隔离代码修正与合成反例 R3（旧隔离库锁阻塞后专项重签）

TASK_ID=CH5_TEMP31_WORKPLACE_TAUJ_SINGLE_TAX_ISOLATED_PATCH_R3_20261028
STATUS=ISSUED_AWAITING_OWNER_TRANSFER
OWNER_APPROVAL=2026-10-28__TEMP31_R3_ONE_NEW_INDEPENDENT_LIGHTWEIGHT_GIT_REPO__OLD_SHALLOW_LOCK_UNTOUCHED__R2_SCIENCE_SCOPE_AND_BUDGET
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=5e4ec0ae4c310b8071b6aef68642fd0ffd862478
TASK_PUBLICATION_COMMIT=EXACT_SHA_SUPPLIED_BY_GPT_AFTER_PUBLICATION__REQUIRED_EXTERNAL_FREEZE
EXPECTED_REMOTE_HEAD=TASK_PUBLICATION_COMMIT_FROM_GPT_HANDOFF__EXACT_EQUALITY
TASK_CONTRACT_PATH=tasks/CH5_TEMP31_WORKPLACE_TAUJ_SINGLE_TAX_ISOLATED_PATCH_R3_20261028/CONTRACT.md
PREVIOUS_R2_TERMINAL=STOP__SOURCE_IDENTITY_PENDING__ISOLATED_GIT_SHALLOW_LOCK_EXISTS__NO_PATCH_NO_TEST__STOPPED
PREVIOUS_R1_TERMINAL=STOP__REMOTE_GOVERNANCE_HEAD_MISMATCH__REFREEZE_REQUIRED__NO_PATCH_NO_TEST__STOPPED
CANDIDATE_BRANCH=codex/ch5-temp31-worksite-tauj-single-tax-isolated-20261028-r3
FIXED_PARENT=5e4ec0ae4c310b8071b6aef68642fd0ffd862478
SOURCE_COMMIT=5e4ec0ae4c310b8071b6aef68642fd0ffd862478
SOURCE_ROOT_TREE=UNOBSERVED_BY_PLANNER_CONNECTOR__MUST_PROVE_WITH_GIT_OBJECT_BEFORE_MODIFICATION
NEW_INDEPENDENT_GIT_REPO_MAX=1
OLD_ISOLATED_REPO_LOCK_ACTIONS=0
NO_SHARED_GIT_OBJECT_STORE=TRUE
TASK_PATH=tasks/CH5_TEMP31_WORKPLACE_TAUJ_SINGLE_TAX_ISOLATED_PATCH_R3_20261028/
DELIVERY_MODE=INDEPENDENT_CANDIDATE_BRANCH__ORDINARY_AUTHORIZED_SSH__SMALL_SEQUENTIAL_PUSHES
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 0. 决策与本任务唯一目的

Owner已正式决定家户来源省 i、工资发放及工作省 j 时使用目的地 tau_j，**同一笔劳动所得仅扣一次税**；这是必须修复的历史遗留经济学错误，不允许保留origin tau作为TEMP31正确机制。GPT已从固定GitHub源码静态核查：
- wage.py 55-75 已使用 tau[destination]、sigma[destination,origin] 计算综合工资；
- migration_labor.py 98-131、311-345 两条劳动分配路径仍使用 tax_by_origin[origin]；
- one_turn.py 194-210、263-289 传入原籍税率；stationary_runtime.py 50-56调用历史source-faithful路径；
- mp4c_python_annual_production.py 167-187 在HA循环中同时传 state["w"] 和 state["tau"]；
- mp4b_python_empirical.py 171-183 的初始化与 matlab_faithful_hjb.py 89-94、matlab_faithful_policy.py 119-155 的HJB/策略均对输入w再应用(1-tau)；
- firm.py 135 的Govinc包含Lt*tau，其税基是否应为wjt*有效劳动尚待单位/财政合同确认。

任务目标：在**完全隔离、未接入正式模型**的代码路径上，实现目的地tau的双边劳动计算与“已是税后综合工资→HA不得再次扣税”的显式适配接口，提供可证伪的非对称两省及其他小规模合成测试；保留历史source-faithful代码、V010和HA算法原样。输出后续正式生产接线的最小差异与未决合同；不做生产整合、不宣布科学收敛。

## 1. 强制第一步：新独立Git库专项授权及固定源码同步

### 1.1 R2 STOP与R3新增权限
R2回执报告：普通SSH远端HEAD查询exit 0并匹配发布提交，但**旧隔离Git库有shallow.lock**，是否为活跃进程持有UNKNOWN。R2已STOP，代码改动0、测试0/2、未创建候选。GPT仅独立验证远端治理HEAD和无R2候选，没有取得本地停止证据原字节。R2旧预算不续用。

Owner本次授权：允许**最多创建一个**位于安全隔离目录、Git对象和refs完全独立的轻量新仓库，然后按此前获批的科研合同执行TEMP31隔离修正及最多两次无HA合成测试。**旧隔离仓库及shallow.lock原样保留**，不得删锁、改锁、改名、移动、kill未知持锁进程、写入旧库、复制旧.git、改旧库index/refs或重用其objects。无需先解锁旧库，不把锁当已确认的过期垃圾。

### 1.2 安全选址与受界同步
任何写入前，仅使用不跟随重解析的只读安全元数据，确认新目录为空、获授权、与P3受保护科研树、旧隔离库、WASM和reparse目标**物理与Git身份均独立**。安全性未知则STOP，不因Owner允许新库而豁免P3。禁止shared/reference clone、alternates、Git worktree指向旧库、复制旧库.git或跨库共用对象存储。仅新仓库内部允许Git初始化、必要源对象获取及候选修改；不触碰正式工作树或D盘历史版本。

在这一个新仓库执行**一次受界的普通SSH固定对象同步/精确增量获取**，优先所需治理commit与必要源码对象；不得无界全量clone、unshallow历史或递归扫描。任何再次出现锁、对象获取卡住、资源预算超限或安全/权限/策略拒绝须STOP，禁止无界重试、换协议/账号/密钥或开第二仓库。原R2规则中只允许在同一已批准SSH路径、无安全拒绝的瞬时工具失败最多一次技术重试的限制保留；默认不重试。

### 1.3 三身份严格相等门
R3 TASK_PUBLICATION_COMMIT必须来自**本任务发布后由GPT在Owner转交指令提供的完整40位SHA**，不得根据本合同的占位字段自行猜测。远端治理HEAD必须**严格等于R3 TASK_PUBLICATION_COMMIT**，不是SOURCE_COMMIT或GOVERNANCE_PARENT。R3发布commit必须恰有一个直接parent，严格等于 GOVERNANCE_PARENT=5e4ec0ae4c310b8071b6aef68642fd0ffd862478；其对parent的diff只能新增R3合同本路径。任何不符直接STOP，不可自行改为祖先判定或漂移跟随。

FIXED_PARENT=SOURCE_COMMIT=5e4ec0ae4c310b8071b6aef68642fd0ffd862478为R3签发前的固定源码提交，**R3合同不会存在于该父提交**，这属于正常情况。仅用SOURCE_COMMIT的固定对象认证parent/root tree、以下源路径Git Blob和能取得的原字节bytes/SHA-256，并从FIXED_PARENT创建一个隔离候选分支。Git Blob不是SHA-256，不得猜填tree；未通过任何身份或P3安全门就不得修改/测试。

### 1.4 预检证据
先形成独立新库不共享对象的非敏感证据、一次受界SSH获取日志、R3发布commit/parent/tree、固定源码commit/parent/tree、10个固定源码path/Blob/bytes/SHA256、未触碰旧库/锁及受保护树的证据和预算记录。若任何硬门缺失，STOP并报告准确缺口；不得伪称源认证通过。

固定Git Blob目录：
- src/ch5_two_asset_hank/multi_province/wage.py = 48001b2e4ca64d81dda6174255f6ccf130e07004
- src/ch5_two_asset_hank/multi_province/migration_labor.py = e6fd216aeda40b9b477c0f0e16332e6366b66900
- src/ch5_two_asset_hank/multi_province/one_turn.py = 621c8e2dfaf5f55eda39c9b9bffb22cd52ee451f
- src/ch5_two_asset_hank/multi_province/firm.py = 1f7d37247e2d712fc0477a9f562dce81d1b367ce
- src/ch5_two_asset_hank/multi_province/fiscal_diagnostics.py = c24bbda9ea88c1581eeed6d734062b30d13def2f
- src/ch5_two_asset_hank/multi_province/stationary_runtime.py = 8717cfa759948bd1ad3c8cd788f8f4736f250598
- src/ch5_two_asset_hank/multi_province/steady_state.py = 5c5b56e6a2eb82fab4e80eb7b8e5bbbf97f08c22
- validators/multi_province/mp4c_python_annual_empirical.py = d2e74cb8b491489053dcde525cd4d83cb4bd0b3a
- validators/multi_province/mp4c_python_annual_production.py = 7473e04418744d745000afb21d84588273cc5bca
- validators/multi_province/mp4c_run_full_annual_batch.py = 599202c39a358b78c4115dcb1e5886021f388389

这些Blob为前述冻结源码的Git对象身份，必须基于R3固定SOURCE_COMMIT在新独立库完成同步后逐项核验；额外可只读固定commit下 contracts.py、matlab_faithful_hjb.py、matlab_faithful_policy.py、mp4b_python_empirical.py 和 mp4b_matlab_source_postloop_household_adapter.py；不读取未知私人源。

预检报告必须分别记录：实际git工作区/branch/HEAD身份（安全匿名）、远端HEAD、父提交、root tree、源码Blob、bytes/SHA256、保护工作区未接触声明与预算；不能以完成Git同步代替科研来源/运行认证。所有前置硬门通过后，从FIXED_PARENT创建一个**新的、独立的**候选分支，严禁修改治理分支或历史科学分支。之前的SSH_FETCH_STALLED、R1的REMOTE_GOVERNANCE_HEAD_MISMATCH及R2的SHALLOW_LOCK_EXISTS均为历史STOP，不得自动恢复旧任务或绕过来源身份门。

## 2. 编码实施范围——隔离候选，不改历史忠实算法

A. **工作地税率**：在TEMP31专用、具名的新函数/适配器上实现所有bilateral destination-row/origin-column项统一使用tax_by_destination[j]，覆盖（1）source-like原始双边劳动重构和（2）origin-preserving normalized另一路径。复用现有算法步骤、phi、sigma、人口乘数和索引维度，不改劳动弹性或normalization逻辑。旧的reconstruct_migration_labor、reconstruct_origin_preserving_normalized_migration_labor及其MATLAB-faithful行为必须保留；不得悄悄替换原函数，使历史基准失去可重复性。显式命名新函数及tau向量语义，避免保留误导性的tax_by_origin变量名。若以共享helper去重，须用旧行为回归测试证明两条历史路径完全未变；否则采用独立TEMP31实现。

B. **HA净工资单次扣税适配**：新增TEMP31专属纯函数/数据合同，把已含目的地tau_j及sigma_ji的net composite wage输入转换为HA单一劳动类别的净工资语义；必须同时涵盖初始化initial_value/baseline_labor与后续HJB HouseholdInputs的**一致净工资**，不允许只在HJB局部设0而初始化仍扣tau。候选可以用隔离适配层的tau_for_HA=0与migration_costs_for_HA=0表达“已扣净工资”，前提是可直接证明没有再次扣除，且原始各省tau_j、sigma_ji仍保留用于真实工资税与迁移机制。不可直接修改shared HouseholdInputs、HJB、KFE、matlab_faithful_policy、历史anchor的原有功能。禁止在正式生产worker中接线。特别登记首轮生产state["w"]可能仅为默认初值（尚未通过真实net证明），不可声明生产首轮已闭合。

C. **财政税基**：只做隔离的条件性税基诊断与设计，不改firm.py/fiscal_diagnostics.py正式计算。对比当前Lt*tau与可选的tau_j*wjt_j*L_j，列出Lt_mat有效劳动是否已含z_i与N_i、工资单位、政府收入归属、sigma是否税收、工资被clip之后的实际税基等缺口。未知事项标BLOCKED；绝不把建议式直接写入生产。

D. **实现边界与改动白名单**：仅允许新增/最小调整：
- src/ch5_two_asset_hank/multi_province/migration_labor.py（仅隔离TEMP31具名新函数/必要不改变旧行为的内部共享）
- src/ch5_two_asset_hank/multi_province/one_turn.py（仅可增具名TEMP31隔离composition或adapter；旧run_source_faithful_one_turn、已接线函数保持字节/行为不变）
- src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py（可新建：净工资适配、条件性财政税基/合同）
- validators/multi_province/temp31_worksite_tax_isolated.py（可新建：纯静态/合成测试调用入口，不得调用生产runner）
- tests/test_temp31_worksite_tax_isolated.py（可新建：定向无HA合成测试）
- tasks/CH5_TEMP31_WORKPLACE_TAUJ_SINGLE_TAX_ISOLATED_PATCH_R3_20261028/（仅报告与证据）

其他源码/科学原件/正式模型/任何.git基础对象不得写入。若发现必须改HA/HJB/KFE、正式入口、旧ORACLE_SHA或超白名单才能实现科学正确性，停止该部分，提交最小gap，不进行“顺手修复”。

## 3. 小规模测试：不得调用HA/HJB/KFE/GE/IRF

每项合成测试采用可手算的有理数/简单浮点数据，明确期望值、错误注入前失败与修后通过的区别；可采用定向pytest，不得加载会自动执行模型的测试套件。至少：
1. 两省非对称 tau_0 != tau_1、w_0 != w_1、sigma非对称：双方跨省工作时均由 **目的地** tau_j 决定税后工资，不允许tax_by_origin结果误通过；与历史路径产出有非零差异的反例。
2. 税率交换/目的地选择与列顺序变化应满足源列、目的地行的变换等变性；测试同址、自身劳动、tau=0、sigma=0。
3. 矩阵有效性：destination行求和 = 目的地供给；normalized替代路径必须每个origin列劳动质量守恒，N_i只乘一次，拒绝shape错位和负税后幂底。
4. 已含税/迁移成本的综合工资进入隔离HA输入适配后有效工资不再乘第二次(1-tau_i)或扣第二次sigma；初始化与HJB适配必须由同一个合同产生输入，但**不得实际调用HJB函数**。
5. 可观察的“重复税收错误注入”反例，测试若错误使用非零HA tau，结果须检测失败；0税与同税率退化样本不能代替非对称强检。
6. 财政只做条件性恒等式测试或静态诊断；模型真实税基/单位不通过则标SCIENTIFIC_PENDING，不能伪称财政已闭合。
允许两省和最多三省的小型合成输入；可选31省shape-only纯数组检查，但不得真实31省稳态、HA或原件读取。禁止校准、调参、利润/福利政策模拟、网格HJB/KFE、真实科研preflight。

预算：
SCIENCE_BUDGET=0
MODEL_CALLS=0
HA_HJB_KFE_GE_IRF=0
STEADY_STATE_IRF_CALIBRATION=0
REAL_PRODUCTION=0
TEST_BUDGET=2_BOUNDED_SYNTHETIC_NO_HA_TEST_INVOCATIONS
TOOL_FAILURE_RETRY_MAX=1_ONLY_FOR_TRANSIENT_FAILURE_WITHIN_ALREADY_APPROVED_TRANSPORT_AND_SCOPE
SOURCE_FETCH_BUDGET=ONE_BOUNDED_SYNC_PREFLIGHT__NO_UNLIMITED_FETCH_RETRY
FORMAL_SOURCE_WRITES=0
D_ROOT_DISCOVERY=0
WASM_READ_OR_REPARSE_FOLLOW=0
GIT_BASELINE_REBIND=0
CLEANUP_OR_DELETE=0
V010_CHANGES=0
V011_ACTIVATION=0

## 4. 差异、来源、交付与STOP

交付候选须含最小真实patch和以下完整证据：
- result.md（COMPLETED/BLOCKED/NOT_COMPLETED/NEXT_ACTION及终态）
- source_identity.json（GitHub commit/parent/tree、源码path/Blob/bytes/SHA256、isolated sync记录及任何缺失）
- code_diff_and_callpath.md（实际前后代码短摘录、准确行号、隔离路径、旧功能未动证明、正式生产未接线证明）
- synthetic_test_evidence.md（测试名称/命令、两个受界测试预算、原始stdout/stderr、安全报告、失败检测能力）
- tax_contract_and_fiscal_gaps.md（Owner已批准tau_j及single-tax、N/z/Lt单位、财政、首轮净工资未决）
- gap_register.md, privacy_report.md
- manifest.json（全部载荷路径、UTF-8/原字节bytes、SHA256、Git Blob、provenance、purpose，manifest自身另核）
- DELIVERY_FINAL_RECEIPT.json（候选payload及seal阶段身份、实际parent/tree、远端文件/Blob/size/readback，避免自指sha循环）
- 如必要，在tasks/CH5_TEMP31_WORKPLACE_TAUJ_SINGLE_TAX_ISOLATED_PATCH_R3_20261028/evidence/内放不涉隐私的精简真实测试记录与机器可复算合成fixture，不得用摘要代替真实源码。

通过当前已授权普通SSH，**优先使用两阶段小提交分批推送**：第一阶段只推送最小代码、测试、报告及非自引用manifest；成功远端逐项回读后第二阶段补齐最终回执seal。每次push应以独立候选分支为目标，禁止一次推送全量科研档案或提交无关文件；若Git对象传输/网络停滞，保存准确错误与进程诊断，受界单次技术重试若已批准且未触发安全拒绝，仍失败即STOP。平台/权限/安全拒绝不得换SSH密钥、账号、HTTP/git对象API或路径绕过；成功推送不证明独立验收PASS。

远端自检必须报告 candidate commit/parent/root tree，逐path Git Blob、原字节bytes及SHA256，明确readback原始性、测试执行范围、未提交/未交付项；提交材料不得包含本地私有绝对路径、WASM、密钥、真实个人工资微观数据或不必要的巨型数据。任一身份/安全硬门失败，允许本地保留STOP证据但**不得冒充已发布候选**；向Owner报告准确终态。GitHub当前累计CURRENT.md/TASK_CURRENT.md未同步，不擅自写大文件或覆盖历史证据。

随后本地Codex立即STOP，GPT从固定候选commit按 A提交/来源（parent/tree/blob/bytes/SHA）→B关键实现、合成测试和数学/经济学风险→C分层裁决（artifact_integrity/source_identity/numeric_review/implementation_review/scientific_review/privacy_review/actual_terminal/delivery/cleanup/not_completed），不得根据Codex PASS自报宣布真实科学模型PASS。实际生产接线、财政税基最终裁决、原件认证、HA替换、模型激活与下一任务需Owner再授权。

## 5. 固定现状
ACTIVE_TASK=ISSUED_AWAITING_OWNER_TRANSFER
PREVIOUS_TASK=CH5_TEMP31_WORKPLACE_TAUJ_SINGLE_TAX_ISOLATED_PATCH_R2_20261028
PREVIOUS_TASK_TERMINAL=STOP__SOURCE_IDENTITY_PENDING__ISOLATED_GIT_SHALLOW_LOCK_EXISTS__NO_PATCH_NO_TEST__STOPPED
PREVIOUS_R1_TASK=CH5_TEMP31_WORKPLACE_TAUJ_SINGLE_TAX_ISOLATED_PATCH_R1_20261028
PREVIOUS_R1_TERMINAL_AT_CLOSE=STOP__REMOTE_GOVERNANCE_HEAD_MISMATCH__REFREEZE_REQUIRED__NO_PATCH_NO_TEST__STOPPED
PREVIOUS_OLDER_TASK=CH5_TEMP31_WORKPLACE_TAUJ_PRODUCTION_CALLPATH_STATIC_GATE_R1_20261028
PREVIOUS_OLDER_TERMINAL=STOP__SOURCE_IDENTITY_PENDING__SSH_FIXED_OBJECT_FETCH_STALLED__NO_CANDIDATE
P3_OWNER_FORMALLY_APPROVED=TRUE
PROTECTION_BASELINE=BLOCKED
TRUSTED_NEW_STATUS_BASELINE=NOT_APPROVED
FORMAL_SOURCE_FREEZE=FALSE
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE
FULL_RUNNER_IO_CLOSURE=BLOCKED
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE
