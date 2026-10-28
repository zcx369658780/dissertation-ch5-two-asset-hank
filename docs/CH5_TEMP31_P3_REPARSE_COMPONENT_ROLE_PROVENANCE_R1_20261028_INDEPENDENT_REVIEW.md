# CH5 TEMP31 P3｜reparse组件词法角色与安全父侧来源｜GPT独立审阅

REVIEW_DATE=2026-10-28
TASK_ID=CH5_TEMP31_P3_REPARSE_COMPONENT_ROLE_PROVENANCE_R1_20261028
REVIEW_METHOD=INDEPENDENT_FIXED_GITHUB_COMMIT
REVIEW_VERDICT=PASS_BOUNDED_LEXICAL_ROLE_AND_NATIVE_TAG_EVIDENCE_DELIVERY__NO_PHYSICAL_PROVENANCE__P3_REMAINS_BLOCKED
REVIEW_SCOPE=DELIVERY_AND_EXECUTOR_METADATA_ONLY__NO_INDEPENDENT_WINDOWS_WITNESS
AUTO_NEXT=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE

## A. 固定权威与证据完整性（COMPLETED_BOUNDED）

- 正式任务与状态补充仅固定于**治理发文提交** `711063b7d3e914268e9ef5c27a9454fda5b318e5`，唯一Parent为`ddd60f910a4dc493ba92fb33bf9826f320ac1be8`。冻结任务Git Blob `6a9c7fa14d00254915cef0ddbd89cdf11cf586d5`；专项状态补充Git Blob `139d579856bc848d3043a610dafb16e785b63aec`。当前最高工作流Git Blob `f98324985f5ebe2a42ec979a61604543a96bb52a`，独立审阅规则Blob `89017c798dbee6b5f9b31ccb88b5b9008a064cbf`；已直接读取。候选是从该任务**共同的固定父提交**分叉，不要求执行候选包含旁支发文正文。
- 候选分支 `codex/ch5-temp31-p3-reparse-boundary-provenance-20261028-r1` 当前HEAD `5b484df4df2af80e5563e5af8b92d6dea2e6a027`；最终提交唯一Parent `c42433fad160f28578490d4f4342323a189b6f4c`，Root `5ccd9d2a56fb54bed655cc798e97ec50159b4ffd`，任务子Tree `1717d0332e7516e8677dd2278cc5f4403c279629`。前一payload `c42433fa...`的唯一Parent为固定基线`ddd60f91...`，Root `169277f5767313ea096033e8a739e177bdbf2c74`。固定基线→payload新增13件；payload→最终seal仅新增`DELIVERY_FINAL_RECEIPT.json`并更新`manifest.json`，没有模型/数据代码修改。
- GPT独立通过GitHub精确路径直接读取最终候选14/14件文件，独立重新计算manifest所列**13件**的UTF-8 bytes、SHA-256及Git Blob，**13/13匹配**；manifest本体单独检查：UTF-8 **6281 bytes**、SHA256 `438228936279afd0d1717e167799e23dbe8f11c6c48dbb44888776c002e13209`、Git Blob `2c164c3f3e72d0d0af6f932d73c269c0b53efa58`。最终receipt对payload期旧manifest记录的是**前一封存阶段**的身份，不能错称为最终manifest SHA；本次读回的13+1均正确。
- `source_excerpts.json`的10份公开excerpt_utf8内容SHA-256，GPT独立重新计算**10/10匹配**；第10段已脱敏一个私有命名token。脱敏文本的正确哈希不能反证原始私人helper的真实内容，也不能用于认定其不在GitHub的私有命名事实。
- GitHub远端树/封存身份、manifest完整性**可独立验证**；本地4个私人旧记录、OWNER_PRIVATE_ROLE_SOURCE_MAPPING、2个新lstat原件、保护raw status/Windows API执行过程仍`LOCAL_ONLY`，GPT未亲自打开或读取。不得把执行者“4/4、2/2、11件保护原证均相同”升格为独立设备见证。

## B. 实质证据边界（COMPLETED_BOUNDED_WITH_OBSERVATIONS）

### B1. 词法角色及原生reparse标签

- 固定旧候选 `623348bd9ef774288293aa02660e552a4029748a` 的4个私有组件record，报告各含其byte/SHA及alias，对照前次公开ledger确认；本轮复用ANCESTOR_00/01，只新增对非reparse父`ANCESTOR_02`及命中子`ANCESTOR_03`各1次`Path.lstat`，共2/2次，均为Codex本地报告，不是GPT在Windows上的实际lstat。
- `ANCESTOR_02`报告属性16/0x10、原生tag0；`ANCESTOR_03`属性1040/0x410即目录位0x10+reparse位0x400、原生tag `0xA0000003`=`IO_REPARSE_TAG_MOUNT_POINT`**标签类别**。这是有界公开元数据证据；该tag不能单独区别具体mount-point/junction子型、认证链接目标路径、安装来源、合法重命名或内容安全。时间字段无法认证同一真实目标始终不变。
- `ANCESTOR_03`的`LEXICAL_DEPENDENCY_DIRECTORY`标签仅来自私有真实名称在科研工作树词法父链中的命名匹配。GitHub公开的是已脱敏角色映射与辅助control-flow摘录（其中一个私有token未公开），**GPT无法独立比对原始组件名称**；只接受`EXECUTOR_REPORTED_LEXICAL_NAMING_CLUE`，不升级为`PHYSICAL_DEPENDENCY_PROVENANCE`或真实文件系统目标验证。上层`ANCESTOR_00/01`未本轮重做lstat，沿用旧固定记录的范围。

### B2. SAFE_SIDE_MANIFEST与来源缺口

- 冻结任务只允许读取**事先由精确私有映射指定**、位于`ANCESTOR_02`及更安全上层的最多2件≤16KB小型manifest。获准映射和4份记录据Codex报告**没有指定这种精确文件路径**；因此`NO_ADMISSIBLE_MANIFEST`、实际读取0/2符合冻结任务第3条的强停止分支。
- `NO_ADMISSIBLE_MANIFEST`是**本轮没有可受理的路径指定**，不是证明磁盘上不存在声明文件。不能猜package/build文件名、glob、列目录、读依赖缓存或走到reparse组件之后；留有剩余预算不构成新的源读取权限。
- 物理链接目标、来源签名/安装工具/时间、依赖刷新原因、旧状态差异发生机制、六WASM安全和内容仍`UNKNOWN/BLOCKED`；Git index查询0/2不等于“无跟踪文件”。

### B3. 权限、保护和执行窗口

- 正式任务与状态补充为Owner逐张明确的**精确只读P3授权**，上一GPT同类受界治理判读只限前次任务。此轮公开最高`CH5_GITHUB_WORKFLOW_AUTHORITY_CURRENT_20261025`允许逐张任务+Owner人工派发+固定commit独立验收；且专项状态补充明确ACTIVE_TASK。候选报告`ALLOW_EXACT_READONLY_TASK_WITH_FROZEN_STATUS_SUPPLEMENT_AND_DISCLOSED_SYNC_GAP`在**本项零科研、零写保护域任务范围**可有界接受。
- **累计治理缺口真实存在**：本次执行候选`CURRENT.md/TASK_CURRENT.md`仍承载历史`ACTIVE_TASK=NONE`等旧段，没有同步为这张P3任务。专项独立状态补充不是对累计文件的实际改写，也不全面免除后续治理核对。既有平台/权限拒绝不得绕过；不得把本次有界认可当成重新授予科学运行、清理或自动发单权限。
- Codex报告本轮科研树保护before/after原始status SHA均`734f11763de35c822f7fbf9a3ab8e2c6b8fb0ae7c8e7c49174ae3e19948e865b`、5971非空NUL记录、HEAD`a1db8c114dec0ab69d69a5576e153a7f868cba0e`、index SHA`28058a7e2d9ab773c5813205c75999e6c221533aeae0b9bb094b9a83451bf7cc`、refs 243及其SHA一致；11件受保护原证两次核验一致。这是`CODEX_REPORTED_LOCAL_EXECUTION`，不是GPT现场完整保护审计。历史旧status`c443420c...`与当前`734f1176...`继续分层，**当前观察不成为新可信保护基线**。
- 明确预算：私有lookup 1/1、四份旧组件原件4/4、live nonfollow lstat2/2、manifest 0/2、index0/2、保护快照2/2且各11项、重试0；WASM读/Hash=0、readlink/realpath/目标跟随=0、目录列举/D根搜索=0、科学/HA/HJB/KFE/GE/IRF/测试/预检=0、治理/源码数据写入及清理=0，均基于执行者及其报告，没有独立操作系统证人。
- 私有映射、真实组件名称和路径以及新元数据留本地；公开GitHub匿名alias与tag类别。GPT直接审阅公开隐私报告未发现文本中明示链接目标或WASM字节，但无法保证LOCAL_ONLY之外全本机零外泄。独立窗口见`privacy_review=PASS_BOUNDED_PUBLIC_GITHUB_ONLY`，独立本机隐私见证`UNKNOWN`。

## C. 分层裁决

artifact_integrity=PASS_BOUNDED__GITHUB_FINAL_13_OF_13_MANIFEST_ENTRIES_SHA256_BYTES_BLOB__MANIFEST_6281_BYTES_SEPARATE__10_OF_10_EXCERPT_SHA256
source_identity=PASS_BOUNDED_EXECUTOR_REPORTED_LEXICAL_COMPONENT_ROLE_AND_NATIVE_TAG_CATEGORY__PRIVATE_SOURCE_AND_TARGET_NOT_INDEPENDENTLY_OBSERVED
numeric_review=NOT_RUN
implementation_review=PASS_BOUNDED__PRIOR_PIN_REUSE_AND_TWO_NONFOLLOW_LSTAT_REPORTED__NO_ADMISSIBLE_MANIFEST__NO_SOURCE_OR_WASM_RUN
scientific_review=SCIENTIFIC_ACCEPTANCE_BLOCKED__P3_PROTECTION_BASELINE_BLOCKED
privacy_review=PASS_BOUNDED_PUBLIC_GITHUB_ONLY__OWNER_PRIVATE_MAPPING_UNREAD
actual_terminal=STOP__P3_LEXICAL_COMPONENT_ROLE_AND_NATIVE_TAG_ONLY__NO_ADMISSIBLE_MANIFEST__PROVENANCE_BLOCKED
delivery=PASS_BOUNDED__FIXED_5B484DF4_GITHUB_14_OF_14_TREE_FILES
cleanup=NOT_AUTHORIZED_NOT_PERFORMED
not_completed=SAFE_SIDE_MANIFEST;PHYSICAL_OR_INSTALLATION_PROVENANCE;LINK_TARGET_SUBTYPE_AND_DESTINATION;DEPENDENCY_REFRESH_OR_RENAME_CAUSE;SIX_WASM_CONTENT_OR_SAFETY;OLD_STATUS_ORIGIN;INDEPENDENT_WINDOWS_WITNESS;CUMULATIVE_CURRENT_TASK_CURRENT_SYNC;D_ROOT_TIMELINE;SCIENTIFIC_AND_NUMERIC_ACCEPTANCE
P3_OWNER_APPROVED=TRUE
PROTECTION_BASELINE_REBIND=FALSE
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
NEXT_ACTION=OWNER_DECISION__NO_SUCCESSOR_ISSUED

**最终：`PASS_BOUNDED_LEXICAL_ROLE_AND_NATIVE_TAG_EVIDENCE_DELIVERY__NO_PHYSICAL_PROVENANCE__P3_REMAINS_BLOCKED`。** 合规执行者信息与最终封存可接受，但本项无法确认物理来源或WASM安全，也不允许新的基线、模型测试、正式科学采纳、目录整理和后继任务。GPT本轮未读取本地私人映射、未更改main/科研工作树、未运行任何模型/WASM、未清理或自动下达任务。STOP等待Owner。
