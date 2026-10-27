# TEMP31 较新版 HA 身份守卫、真实入口与 canonical 输入 · 采纳前置证据任务

TASK_ID=CH5_TEMP31_NEWER_HA_DISPATCH_CANONICAL_CONTRACT_PREPACKAGE_R1_20261027
STATUS=OWNER_AUTHORIZED__ISSUED_WAITING_LOCAL_CODEX
TASK_TYPE=READ_ONLY_SOURCE_AND_CONTRACT_DECISION_PREPACKAGE
DATE=2026-10-27
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=32d6b827aabea861ea44ffe427abbd63dbe681be
FIXED_PARENT=32d6b827aabea861ea44ffe427abbd63dbe681be
FIXED_PARENT_ROLE=ISOLATED_CANDIDATE_BASE_NOT_TASK_PUBLICATION_COMMIT
CANDIDATE_BRANCH=codex/ch5-temp31-newer-ha-dispatch-canonical-contract-20261027-r1
TASK_PATH=tasks/CH5_TEMP31_NEWER_HA_DISPATCH_CANONICAL_CONTRACT_PREPACKAGE_R1_20261027.md
EVIDENCE_DIR=tasks/CH5_TEMP31_NEWER_HA_DISPATCH_CANONICAL_CONTRACT_PREPACKAGE_R1_20261027/
DELIVERY_MODE=MANUAL_GITHUB_TASK__OWNER_TO_LOCAL_CODEX__ISOLATED_SSH_CANDIDATE__GPT_FIXED_COMMIT_REVIEW__OWNER_DECISION
FORMAL_SOURCE_BASE=b69ae535a1518c68822733603f1e506620327375
FORMAL_SOURCE_BASE_TREE=8dbd81c0938f603511c7de1c763ed29b6d2d4b83
PREVIOUS_REVIEW_COMMIT=32d6b827aabea861ea44ffe427abbd63dbe681be
PREVIOUS_CANDIDATE_COMMIT=19e03fdd2da0532e3ef8158ff7a032fe87724565
PREVIOUS_VERDICT=PASS_BOUNDED_HISTORICAL_PIN_AND_STATIC_CALLSITE_PROVENANCE__PRODUCTION_ADOPTION_BLOCKED
OWNER_CHOICE=RETAIN_NEWER_HA_AS_PREFERRED_REVIEW_CANDIDATE_ONLY__NO_FILE_REPLACEMENT_OR_FORMAL_ADOPTION
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 1. 唯一目标

Owner已经批准**保留较新版 HA 为优先待审候选**而不是回退历史原件，并授权沿既有TEMP31方向继续，但**尚未**采纳生产入口、真实 canonical 原件、任何 pin 修订方法或完整科研生产闭包。

本任务做一次**采纳前置的源码/配置/现存输入证据核实与备选合同文档包**，使 Owner 能在下一次审阅时决定：
1. 较新版HA候选的精确源码字节/版本身份及其与旧pin原件的科学风险差异，是否需要隔离版本化身份守卫方案（仅文档建议，不改守卫）。
2. 哪个MP4C/TEMP31启动入口+representation/year+config/runner能够由真实现存调用/已存运行清单/Owner批准材料支持；如何区分production命名、历史annual runner和实际已采纳TEMP31。
3. 已存在的canonical原件/生成记录/31省轴与source hashes、工资/税初始字段，以及Old tuple (D1=B) 的证据到底有哪些。**不得把有生成函数当作已实际运行，也不能把普通JSON SHA当D1 tuple witness。**

输出以“具体源身份/可否独立验证/仍需Owner授予的准确选择”为中心，避免重复上一轮原有旧pin检索和116段全域税收审计；STOP之后不自动执行任何采纳方案。

## 2. 冻结历史与本轮的授权边界

### 2.1 已验证历史（直接引用，不重新全域审计）
- 上轮GPT独立报告：`docs/CH5_TEMP31_ORACLE_PIN_PRODUCTION_DISPATCH_PROVENANCE_R1_20261027_INDEPENDENT_REVIEW.md`@32d6b827aabea861ea44ffe427abbd63dbe681be；上轮候选`19e03fdd2da0532e3ef8158ff7a032fe87724565`。
- 老的固定 `ORACLE_SHA=b92f6efc59d9398f89f8fb6ee67bf6c5f947282d76895051bec194967ec9c3e3`，由GPT独立复算，与 `ba98537fd5ae004f0aa37d319865da1f1739e503:exports/matlab_faithful_two_asset_ha.py` 完全匹配：28641B，Blob `9e7dc9556a2b76811e78f89999abecc045886106`。
- 较新版冻结 `b69ae535a1518c68822733603f1e506620327375` 和 `2aa2f67f4e5eaa1117d174b7866c3eb7b7b109b0` 里的 `exports/matlab_faithful_two_asset_ha.py` 内容相同：31143B，SHA256 `a7539eb6ba076176b81f832c1800d38d8d170dad8f3619d3b0f3893c5a163fff`，Blob `e144c645d3f4dc842c2faa6b93b2ba0e24275dcf`；历史→新版本有新的transfer candidate/helper/shadow分支表达式，不是仅仅换行。
- Executor报告当前Windows该文件31859B、SHA256 `f6007c1166c951b4a0c98b0fbf551921a2664d2e3943e7d77f847634261524f8`、CRLF 716行，与冻结较新版LF行payload相同；此本地原始字节**不是GPT直接重读**，不得升级为远端整文件独立验收。
- `validators/multi_province/mp4b_python_empirical.py` 固定历史pin校验在line30–36、顶层line64发生；此MP4B入口标题为validation-only。新版文件源/行号和旧pin不匹配不等于运行失败或源损坏，直到获得实际执行证据。
- 静态调用：`validators/multi_province/mp4c_run_full_annual_batch.py` 的batch→`mp4c_python_annual_production.py` worker；worker通过MP4B validation anchor并创建solve_batch；`mp4c_python_annual_empirical.py` 的 prepare_canonical 调用 `load_primary_annual_input`，另有runtime_cache/Owner-A两种静态物化分支。仍无 Owner TEMP31 生产采纳和真实规范输入闭包。
- User明确同意“保留较新版HA作为待审候选，不直接恢复历史文件”；这是 review-preference 而非授权实施新守卫、修改生产或定稿哪一个旧年输入representation。工作地/目的地税 `tau_j` 且同一税只扣一次的Owner设计不变，R2/R3隔离不合并。
- D1=B旧期统一tuple digest、D2显式31省batch adapter、D3=B先隔离no-HA spy仍为目标而非已验证生产实现。
- 2018三份国家统计局声称来源Excel：候选/未采纳（`MODEL_ADOPTED=FALSE`），不得上传真实工资行/插补/转换；历史2009统一scalar不代表31省实际工资数据；`fixed_zt_calendar_year=2020`独立于2009绑定。
- Owner说过“长会话导致验收失败可能解释问题”，没有带时间关联日志支持该pin版差原因；本轮不搜索会话私有JSONL、不做虚假的因果归责。

## 3. Gate A：现存真实证据与版本字节合同

A1. 核实真正本地 AGENTS 和实验保护状态：branch/HEAD、index/refs/dirty/untracked、原科学树及11件历史保护资产前后指纹。**不得**切换/checkout、reset、stash、格式化、修正换行、替换任何保护原件或下载重建源。
A2. 在已知两条源码文件上分别检查当前字节 SHA-256、Git-style Blob、文件大小、CRLF/LF、`git ls-files -s` 对应已跟踪对象，且分清本地原字节与冻结GitHub Blob身份。只读取得当前入口和新版 HA 关键 helper/shadow 变化，编写三种合同：historical-old/checked-in-newer/current-worktree-CRLF；**比较身份和功能差异，不选择科学正确版本，不改ORACLE_SHA**。
A3. 仅核对历史`ba98537...`/已冻结`b69ae535...`/已知`2aa2f67...`真实已引用的文件原件和上一轮53摘录；如要追索来源，只做指向已知config/run-manifest的明确路径，不全历史Git扫描、不寻找首次pin引入任务。
A4. 现存正式运行记录/配置如果有任务明确的相对路径和读取权限，可**只读**取schema/参数字段/路径及安全hash/原件id。报告是否有真实 Owner批准时间/版本/入口/representation/year及明示的TEMP31工作地税采纳。运行清单自带`production`标签不等于 Owner采纳。
A5. 明确旧pin对应老版本，而“current newer”若在本地因CRLF改变原字节SHA，即使冻结新版Git Blob相同语义也不能被**原字节pin守卫**自动接受；Owner后续可选择“保留当前版本、建立经核准的版本化身份守卫”作为研究方向，但不在此任务补写guard、豁免pin或执行入口。

## 4. Gate B：TEMP31采纳入口与真实canonical输入闭包的有界追踪

B1. 仅从这些具体入口向前/向后最多两跳核对：`validators/multi_province/mp4c_run_full_annual_batch.py`、`mp4c_python_annual_production.py`、`mp4c_python_annual_empirical.py`、`mp4c_matlab_runtime_cache.py`、`mp4c_owner_a_2009_2022.py`、`mp4b_python_empirical.py`；及`src/ch5_two_asset_hank/multi_province/annual.py`、`stationary_runtime.py`、`one_turn.py`和`exports/matlab_faithful_two_asset_ha.py`。若源文件实际import/精确配置引用到另一个具体相对路径，允许单层跟随并计入预算；禁止repo-wide搜索和私有路径探索。
B2. 对每个发现的**明确运行路线候选**记录：命令/配置/调用者→worker→anchor→HA版本守卫→callback→controller，representation/analysis calendar year、版本SHA和真实校验失败前置条件；区分（1）代码声明，（2）可读现存运行清单，（3）Owner明示批准和（4）执行结果四个证据级别。没有Owner实际批准就写UNKNOWN，不以`production`命名代替。
B3. Canonical选项严格区分：（a）`empirical.prepare_canonical`→`load_primary_annual_input`，（b）`runtime_cache.load_runtime_year`→`add_runtime_support`，（c）`owner_a.build_input`。分别说明来源真实文件及原始SHA/年份/31标签是否由**本次实际只读见证**核实，是否确实有运行清单指向，以及初始w/wjt/tau源标量，字段`representation`是否跨选项同义。无实际原件=BLOCKED，不构造或写入任何新canonical JSON。
B4. 工作地`tau_j`的单次应用、gross/net、`w`/wjt/财政Lt与 household labor/有效z劳动/人口N、`sigma`/phi、D1完整旧期tuple digest和D2生产batch adapter/D3先spy，逐项映射为 `PROVEN_STATIC` / `RUNTIME_UNVERIFIED` / `NEEDS_OWNER`；以前R2/R3局部代码不可假装整合生产。税前/税后缺乏证据时不可产出新的转换公式。
B5. 输出A/B/C三种来源政策的**比较矩阵**：
  - A: 历史Oracle+旧pin（已匹配，但可能失去新版helper，非建议默认回退）；
  - B: 保留新版候选，未来另行审核明确的版本化原字节/目标构建身份守卫合同（Owner当前倾向；这不是今天授权的实施）；
  - C: 暂保留blocked并仅完成Owner真实入口/输入原件认证后再审guard/接线。
每个只给必要的来源身份证据、科学/回滚/生产风险和下一次可执行的最小任务；明确是否需要Owner**额外**批准。不产生patch、测试/代码、自动替换文件或实验结果。
B6. 若目前已有确切静态链但没有Owner实际启动凭据/命令/真实canonical现存原件，则早停来源调查，提交**精准待Owner提供的最少证据**，不要凭假设生成替代输入或改造模型。

## 5. 源预算、隐私和科研硬门

MAX_DISTINCT_EXACT_SOURCE_FILES=14
MAX_SOURCE_CONTENT_READS=20
MAX_TARGETED_LOCATOR_QUERIES=6
MAX_CALL_CHAIN_DEPTH=2
MAX_SAMPLED_FROZEN_SOURCE_REFS=3
MAX_EXISTING_MANIFEST_OR_INPUT_METADATA_FILES=3
MAX_RAW_INPUT_HASH_ONLY_CHECKS=2_CONDITIONAL_ON_EXACT_KNOWN_LOCAL_PATH_AND_ALLOWED_READ
TEST_BUDGET=0
NO_HA_SPY=0
PREFLIGHT_BUDGET=0
MODEL_CALLS=0
HA_HJB_KFE_GE_IRF=0
NUMERIC_MODEL_BUDGET=0
SCIENCE_EXECUTION_BUDGET=0
PROJECT_IMPORT_EXECUTION=0
PRODUCTION_SCRIPT_EXECUTION=0
REAL_CANONICAL_GENERATION=0
DATA_TRANSFORMATIONS=0
FORMAL_SOURCE_WRITES=0
DATA_WRITES=0
EXTERNAL_DOWNLOADS=0
TOOL_RETRY_BUDGET=1_TRANSIENT_READ_ONLY_TOOL_ERROR_ONLY__NO_AUTHORIZATION_BYPASS
LOCAL_WRITE_ALLOWLIST=ONE_TASK_OWNED_SCRATCH_OUTSIDE_SCIENCE_WORKTREE_FOR_SANITIZED_REPORTS
GITHUB_WRITE_ALLOWLIST=tasks/CH5_TEMP31_NEWER_HA_DISPATCH_CANONICAL_CONTRACT_PREPACKAGE_R1_20261027/__ON_ISOLATED_CANDIDATE_BRANCH_ONLY
PROTECTED=ALL_OTHER_WORKTREE_INDEX_REFS_DIRTY_UNTRACKED_HISTORICAL_EVIDENCE_PRIVATE_WAGE_EXCEL_FORMAL_TEX_SCIENCE_SRC_V010_V011_RESULTS

源身份证据只读。既有输入原件若包含敏感原始统计数据，只允许在精确已知文件上做`size/SHA256`及必要安全元数据，不发布原字节、原工资行、私人绝对路径，不扩展隐私目录。禁止跑`--prepare-canonical`、batch、worker、`_bootstrap_repository_imports`，甚至`import`项目模块：它们可能触发身份/科学副作用。禁止任何HJB/KFE/HA/GE/IRF、稳态、外推、福利、校准、重运行。文件无、权限拒绝、重要经济学概念不一致或超预算即STOP，不能更换凭据/账号/SSH协议或绕过制度。

## 6. 必交GitHub证据：只在本任务隔离候选目录

- `result.md`：Owner目标事实、真实发现、按门状态、实际STOP和没有完成的事项。
- `newer_ha_version_identity_and_guard_options.md`：历史/冻结新版/本地CRLF合同矩阵、原字节vs Git Blob、真实代码差异、A/B/C不实施比较。
- `entrypoint_dispatch_adoption_evidence.md`：每个候选启动命令、精确import/dispatch/callback、来源是代码/运行记录/Owner认证哪一层，不可伪造已批准。
- `canonical_existing_input_binding_matrix.md`：三种canonical入口、现存真实原件可追溯性、31省轴/年份/模型期、数据/工资税单位、旧期tuple证据矩阵。
- `owner_decision_brief.md`：用户已明确“新版优先待审”，剩余需要Owner决定的**最小**版本守卫/入口/输入选项，不得将候选升格为已采纳。
- `source_inventory.json`、`source_excerpts.json`：新的必要精确原件相对路径/ref/Blob/SHA/大小/原行码及短摘录，能公开时须足以GPT独立核内容，脱敏记录变换；不要重复旧53摘录全文。
- `gap_register.json`：逐项区分本任务新增缺口与之前G01–G11，历史STOP与R2/R3判决不改写。
- `audit_checkpoint.json`、`privacy_report.json`、`INDEPENDENT_COMPLETION_EVENT.json`（无独立事件即UNKNOWN）。
- `manifest.json`：每个payload path/UTF8原始字节/标准SHA256/Git Blob/provenance/purpose及隐私身份，封存自引用分开。
- `DELIVERY_FINAL_RECEIPT.json`：先一次payload推送后远端读全，再封存最终commit/parent/tree/branch、最终远端readback/预算/STOP；最终seal自引用外部处理，不伪称所有自指哈希都已写入自身。不得以摘要/哈希替代必要源码片段。

发布受界证据到独立候选分支，普通权限SSH推送后从固定commit远端回读路径、Blob、大小和必要SHA256。所有源保护状态仍应保持不变。若SSH最终回读中断，保留事实和本地脱敏中断凭证即可STOP，GPT可独立GitHub复读；不绕过工具权限，不重做科学调查。

## 7. 三阶段验收、STOP和护栏

A=IDENTITY_AND_SOURCE_INTEGRITY，B=REAL_ENTRY_CANONICAL_AND_GUARD_DECISION_EVIDENCE，C=LAYERED_VERDICT；特别区分交付PASS与科研内容BLOCKED。必须包含`artifact_integrity`、`source_identity`、`numeric_review`、`implementation_review`、`scientific_review`、`privacy_review`、`actual_terminal`、`delivery`、`cleanup`、`not_completed`。
准许结果只会是受界来源与决策预包，不论候选来源身份如何均**不能**从本轮升级到正式TEMP31生产运行、D1/D2/D3、科学模型、Results或论文方程版本采纳。

ACTIVE_TASK_STOP_AFTER_DELIVERY=TRUE
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
