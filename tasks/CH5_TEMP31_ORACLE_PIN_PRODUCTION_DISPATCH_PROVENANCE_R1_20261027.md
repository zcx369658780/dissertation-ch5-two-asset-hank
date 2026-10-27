# CH5_TEMP31_ORACLE_PIN_PRODUCTION_DISPATCH_PROVENANCE_R1_20261027

TASK_ID=CH5_TEMP31_ORACLE_PIN_PRODUCTION_DISPATCH_PROVENANCE_R1_20261027
STATUS=OWNER_AUTHORIZED__ISSUED_WAITING_LOCAL_CODEX
DATE=2026-10-27
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=174260f367e91edc9985a5ed712b972dea4f1fd0
FIXED_PARENT=174260f367e91edc9985a5ed712b972dea4f1fd0
FIXED_PARENT_ROLE=ISOLATED_CANDIDATE_BASE__TASK_SHEET_PUBLISHED_IN_SUBSEQUENT_GOVERNANCE_COMMIT
CANDIDATE_BRANCH=codex/ch5-temp31-oracle-pin-production-dispatch-20261027-r1
TASK_PATH=tasks/CH5_TEMP31_ORACLE_PIN_PRODUCTION_DISPATCH_PROVENANCE_R1_20261027.md
CANDIDATE_EVIDENCE_DIR=tasks/CH5_TEMP31_ORACLE_PIN_PRODUCTION_DISPATCH_PROVENANCE_R1_20261027/
DELIVERY_MODE=GITHUB_FIXED_CANDIDATE_COMMIT__AUTHORIZED_ORDINARY_SSH
SOURCE_COMMIT=b69ae535a1518c68822733603f1e506620327375
SOURCE_TREE=8dbd81c0938f603511c7de1c763ed29b6d2d4b83
SOURCE_ENTRY_PATH=validators/multi_province/mp4b_python_empirical.py
SOURCE_ENTRY_BLOB=b1710ae3c5d8d7baf96e85c932d777fa5f3b908c
SOURCE_ORACLE_PATH=exports/matlab_faithful_two_asset_ha.py
SOURCE_ORACLE_BLOB=e144c645d3f4dc842c2faa6b93b2ba0e24275dcf
PREVIOUS_TASK_CANDIDATE=b9d0931b454334a5449ba26d8def13ebf0da7b37
PREVIOUS_TASK_REVIEW_COMMIT=174260f367e91edc9985a5ed712b972dea4f1fd0
PRIOR_VERDICT=STOP_ACCEPTED__SOURCE_GATE_BLOCKED__GITHUB_ARTIFACTS_VERIFIED__EXECUTOR_FINAL_SSH_READBACK_INTERRUPTED
ROUTE=TEMP31_WORKPLACE_WAGE_TAX_SINGLE_APPLICATION_AND_DESTINATION_INDEX
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 1. 唯一目标与要回答的问题

只读、有限来源追踪，针对上一轮已接受的SOURCE_GATE_BLOCKED，分别回答两个问题，不重复上一轮全部静态审计：
（1）validation-only入口中的固定 ORACLE_SHA 对应哪个可验证的HA导出源码版本/文件/固定Git对象或既有有界归档？它与当前本地导出原件的差别是否仅是版本身份而非来源损坏？能否定位首次出现这个pin的有证据提交/任务，不能凭相似片段猜测其形成原因。
（2）Owner打算后续采用的真实生产入口/dispatch/callback与canonical输入生成调用，是否能通过**当前可核验的源码/配置/静态引用**定位到一个可信版本和固定来源？若只找到validation-only/opt-in，保留ACTUAL_PRODUCTION=UNKNOWN及CANONICAL_BINDING=BLOCKED，并给Owner最小下一次要提供的事实。

**这是新任务的有界来源澄清，不是重试上一任务、不修hash、不实现/测试R2/R3、不做真实HA、不是正式科学接受。** 暂不修复任何版本差异；这次成果是版本候选身份证据、调用角色证据及Owner选择所需信息。

## 2. 已知事实、假设与本任务冻结输入

- 上一审阅@b9d0931b454334a5449ba26d8def13ebf0da7b37（result、source_inventory、source_excerpts、production_entrypoint_and_import_trace、gap_register及delivery）已由GPT独立读取14/14 GitHub固定候选文件；审阅报告在 174260f367e91edc9985a5ed712b972dea4f1fd0: docs/CH5_TEMP31_PRODUCTION_WAGE_TAX_INPUT_BINDING_PROVENANCE_GATE_R1_20261027_INDEPENDENT_REVIEW.md。不要重跑上轮已耗27/30读预算；本任务使用独立新预算。
- 冻结源commit b69ae535a1518c68822733603f1e506620327375 的 ENTRY源码line19固定 ORACLE_SHA=B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3；line30-36用磁盘目标字节SHA检查，不符raise，line64在HA导入前调用bootstrap。入口首行明确validation-only calendar-2009；绝非已认证生产入口。
- 上轮执行者在本地 CURRENT_LOCAL_DIRTY 源 reports中记录导出 exports/matlab_faithful_two_asset_ha.py SHA256=f6007c1166c951b4a0c98b0fbf551921a2664d2e3943e7d77f847634261524f8；GPT未能亲自读Windows私有原字节。冻结GitHub同名Blob=e144c645d3f4dc842c2faa6b93b2ba0e24275dcf，不能将Git Blob与SHA256等同或跨版本误比。
- corrected_diagnostic/optionb_turn2_household_integration.py 自称 opt-in task driver，不改默认生产路线。既有 annual.py canonical生成函数接受调用者sources/binding/scalars，但生成函数存在不代表有真实生产生成调用。旧2009输入的三个工资/税为共用scalar，不是真实31省工资向量。
- 上轮Codex封存后SSH逐件回读连接中断，而GPT随后独立GitHub回读14/14通过。**交付通道事件与源码版本pin不匹配是独立事实**。Owner猜测长会话/验收超时可能影响交付，不得在没有日志时判定导致哈希冲突，也不自动否定该假说。
- 三份2018 NBS-claimed工资Excel仍MODEL_ADOPTED=FALSE；不读取/复制实际薪资行或接入模型。R2单次扣税/R3目的地tau_j仅隔离候选；D1=B、D2、D3=B仅目标合同。FORMAL_SOURCE_FREEZE、V010、V011及Results均不得改变。

## 3. Gate A：固定来源身份与本地保护硬门

A1. 读取治理分支固定任务单及在 174260f367e91edc9985a5ed712b972dea4f1fd0 已生效的Owner微预算授权。检查当前工作区的AGENTS、真实分支/HEAD、index、refs和dirty/untracked；以哈希记录任务前后保护快照。不得checkout/reset/stash/清理源树以迎合冻结状态。若本地权限/身份不符，立即STOP写证据。
A2. 仅为已知 ENTRY 和 HA target 计算本地准确原始字节SHA256和Git-style Blob/size，明确raw bytes、换行、路径、是否untracked/dirty、工作树所在commit。不修改、格式化或规范化来源；只有完整原字节证明时才能声明本地对象SHA匹配/不匹配。
A3. 固定对照优先从以下精确已知版本的相同两条路径读取：源 b69ae535a1518c68822733603f1e506620327375；历史Python候选 ba98537fd5ae004f0aa37d319865da1f1739e503；既有TEMP31上下文 2aa2f67f4e5eaa1117d174b7866c3eb7b7b109b0；及上轮实际9bdc.../b9d...公开源清单中能证实的同名对象。若某固定commit没有该路径，记MISSING_AT_REF，不从其SHA猜字节。对确实取得的raw bytes计算SHA256和Git Blob，记录commit/tree/blob/path/byte length。
A4. 对期望哈希 B92F... 最多6次**定向**仅在已有固定任务/来源索引、精准validators/exports路径或上面固定版本记录中进行文本/元数据来源定位。只允许跟随上述精确文件中真正显示的单层调用/相邻版本身份索引；不扫描全仓历史、全磁盘、Codex会话JSONL、系统凭据、云端服务器或私人目录。不找到匹配只可写NOT_FOUND_IN_BOUNDED_SCOPE，不能断言任何历史对象都不存在。
A5. 绝不通过改ORACLE_SHA、覆盖导出文件、Git对象恢复到工作树、换行改写、绕过guard或调用bootstrap来让它“通过”；版本选择属于Owner后续决策。

## 4. Gate B：入口身份与canonical生产调用的限定溯源

B1. 严格把 validation-only、opt-in diagnostic、历史固定提交、临时R2/R3补丁、候选设计和ACTUAL_PRODUCTION分组。给出每个**实际发现**入口的调用目标、import/dispatch、身份来源、是否有部署证明，不凭函数名、CLI、类签名或PRODUCTION_CALLER标签升格为真实生产。
B2. 追踪ENTRY→HA bootstrap→postloop→OnlineStationaryInputs只是历史validation静态调用；独立检索**最多两层**已知真正引用的生产入口/runner/配置/导出原件目录，避免对整个项目进行穷尽搜索。不能证明生产身份就标UNKNOWN，STOP；不要重启历史驱动。
B3. 限定读取annual.py的canonical载荷/生成器与已知调用者之间的精确引用；是否存在真实已批准生成调用、2009 scalar source binding和有序31省行政ID/旧期tuple各自的可验证原件？找不到就列出Owner需提供的精确入口命令/配置/原件，不替换成2018工资Excel或测试伪输入。凡标为canonical的哈希，必须区分整文件指纹与D1 batch tuple digest。
B4. 报告固定sha是（a）与某精确历史原件相符，（b）仅静态定义但源未找到，（c）发现被保护的多个候选而尚无采纳权三种之一；如有版本冲突，给Owner各版本的来源级差异清单，不自行修复/选替代。
B5. 保留已决合同：工作地/目的地tau_j、工资税只扣一次；R2/R3未生产闭包。gross/net、劳动有效单位、财政税基、sigma/phi及NBS桥仍未解决的均列入gap，不从版本匹配推出经济学修正。
B6. “长会话验收失败”的原因归因单独列观察：Codex SSH断连是交付环节事实，源码pin冲突是静态来源身份事实；如没有带时间/错误的精确日志不得声明二者因果关系，也不得把失败归责模型机制。

## 5. 严格预算/白名单（本次不安排运行）

SCIENCE_EXECUTION_BUDGET=0
NUMERIC_MODEL_BUDGET=0
TEST_BUDGET=0
NO_HA_SPY=0
PREFLIGHT_BUDGET=0
PROJECT_IMPORT_EXECUTION=0
PRODUCTION_SCRIPT_EXECUTION=0
MODEL_CALLS=0
HA_HJB_KFE_GE_IRF=0
FORMAL_SOURCE_WRITES=0
REAL_DATA_WRITES=0
DATA_TRANSFORMATIONS=0
EXTERNAL_DOWNLOADS=0
MAX_EXACT_SOURCE_CONTENT_READS=18
MAX_TARGETED_LOCATOR_QUERIES=6
MAX_FROZEN_VERSION_REFS=3
MAX_DISPATCH_REFERENCE_DEPTH=2
TOOL_RETRIES=1_FOR_TRANSIENT_READ_ONLY_ERROR_MAX__NO_AUTH_BYPASS
LOCAL_WRITE_ALLOWLIST=ONE_TASK_OWNED_ISOLATED_SCRATCH_FOR_SANITIZED_REPORTS_ONLY
GITHUB_WRITE_ALLOWLIST=tasks/CH5_TEMP31_ORACLE_PIN_PRODUCTION_DISPATCH_PROVENANCE_R1_20261027/__ON_ISOLATED_CANDIDATE_BRANCH_ONLY
PROTECTED=ALL_ORIGINAL_SCIENCE_WORKTREE_DATA_TEX_R2_R3_V010_V011_RESULTS_HISTORY_STOP_PENDING_AND_OTHER_BRANCHES
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE
发现身份/权限风险、需扩大预算、无法取得必须原件或出现经济学定义决策时，只提交最小必要缺口证据并STOP。绝不打开/执行HA/HJB/KFE/GE/IRF、正式稳态、外层校准、调参、IRF或福利。

## 6. GitHub交付与证据要求

Codex只在分支 codex/ch5-temp31-oracle-pin-production-dispatch-20261027-r1 以唯一固定基点 174260f367e91edc9985a5ed712b972dea4f1fd0 生成候选，不得改动治理分支。任务单实际发文commit由Owner提供的GitHub固定URL确认，其commit**与candidate固定parent不是同一个SHA**，该差别已明确设计。已经存在身份不符分支则STOP，不force/绕过权限。
候选目录 tasks/CH5_TEMP31_ORACLE_PIN_PRODUCTION_DISPATCH_PROVENANCE_R1_20261027/ 的白名单证据文件：
- result.md — 两问题答案、原因区分、实际STOP及not_completed；
- oracle_pin_version_matrix.md — expected/current/historical精准source path、Git ref/tree/blob/SHA-256/bytes，VERSION_MATCH/UNKNOWN，是否由GPT可重核；
- bootstrap_guard_and_hash_lineage.json — pin生成/保存/消费链、精确行和版本、证据等级、source/consumer判定；
- production_entrypoint_dispatch_candidates.md — 真实/validation-only/opt-in分类及已知引用层级，正面/负面范围；
- canonical_generator_invocation_provenance.md — 来源/生成调用/2009 scalar/31省ID和统一snapshot的逐项证据或BLOCKED；
- source_inventory.json、source_excerpts.json — 原始码精确有界、公开安全短摘录、源字节原SHA，Git Blob不同算法；必要的真实内容不得只有哈希；
- gap_register.json — 上轮阻塞与本轮新来源证据分开；
- audit_checkpoint.json、privacy_report.json — protected-before/after哈希、预算、实际terminal，预判不能当实测；
- manifest.json — 路径、UTF8 bytes/SHA256/Git Blob、原件/短摘录/报告身份、脱敏说明；
- DELIVERY_FINAL_RECEIPT.json — candidate commit/parent/tree、任务发文commit、每文件远端读取/SSH真实终态；INDEPENDENT_COMPLETION_EVENT.json — 独立见证缺失则UNKNOWN。

不上传完整私有TeX、MATLAB ZIP、薪资原表、个人绝对路径、凭据；科研原件和本地dirty工作区不可修改。必须先全部证据发布GitHub，通过已授权普通权限SSH到独立候选，再按**固定最终commit**远端逐件回读路径/Blob/bytes/SHA256；封存commit的最终远端读回若断线，真实terminal如实标DELIVERY_FINAL_READBACK_INTERRUPTED，不能虚报PASS、不能绕过权限无限重试，也不必为仅交付失败重做整个科研来源调查。禁止常规全量离线ZIP。完成即STOP。

## 7. 分层验收与科研保护

GPT按当前V3三阶段独立审阅；字段artifact_integrity/source_identity/numeric_review/implementation_review/scientific_review/privacy_review/actual_terminal/delivery/cleanup/not_completed必须分层，不把GitHub交付PASS自动升格生产来源PASS。
FORMAL_SOURCE_FREEZE=FALSE
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE
FULL_RUNNER_IO_CLOSURE=BLOCKED
NEXT=OWNER_DECISION__NO_AUTO_SUCCESSOR
STOP_AFTER_REMOTE_READBACK=TRUE
