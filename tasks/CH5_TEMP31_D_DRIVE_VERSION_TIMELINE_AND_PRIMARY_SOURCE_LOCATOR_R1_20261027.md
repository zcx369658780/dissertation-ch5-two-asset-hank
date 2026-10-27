# TEMP31 C方案 · D盘模型多版本时间线与三份primary宏观原件位置溯源（有界只读）

TASK_ID=CH5_TEMP31_D_DRIVE_VERSION_TIMELINE_AND_PRIMARY_SOURCE_LOCATOR_R1_20261027
STATUS=OWNER_AUTHORIZED__ISSUED_WAITING_LOCAL_CODEX
DATE=2026-10-27
TASK_TYPE=BOUNDED_LOCAL_D_ROOT_MODEL_VERSION_DIRECTORY_TIMESTAMP_AND_SOURCE_IDENTITY_DISCOVERY
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=1aa1026daceb6b0966470f28fcaa7516cde4a908
CANDIDATE_FIXED_PARENT=1aa1026daceb6b0966470f28fcaa7516cde4a908
CANDIDATE_BRANCH=codex/ch5-temp31-d-drive-version-timeline-source-locator-20261027-r1
TASK_PATH=tasks/CH5_TEMP31_D_DRIVE_VERSION_TIMELINE_AND_PRIMARY_SOURCE_LOCATOR_R1_20261027.md
EVIDENCE_DIR=tasks/CH5_TEMP31_D_DRIVE_VERSION_TIMELINE_AND_PRIMARY_SOURCE_LOCATOR_R1_20261027/
TASK_PUBLICATION_COMMIT=READ_FROM_IMMUTABLE_GITHUB_TASK_URL_AFTER_ISSUANCE
FIXED_SOURCE_COMMIT=b69ae535a1518c68822733603f1e506620327375
FIXED_SOURCE_TREE=8dbd81c0938f603511c7de1c763ed29b6d2d4b83
PREVIOUS_CANDIDATE=ec5b2ccef4da2440af3eb74e3d51b4ce47b33e6c
PREVIOUS_ACCEPTANCE_COMMIT=1aa1026daceb6b0966470f28fcaa7516cde4a908
PRIOR_VERDICT=PASS_BOUNDED_C_SOURCE_LOCATION_NEGATIVE_COVERAGE_AND_STOP__REAL_SOURCE_LAUNCH_CANONICAL_BLOCKED
OWNER_NEW_AUTHORIZATION=D_DRIVE_ROOT_IMMEDIATE_MODEL_VERSION_DIRECTORY_METADATA__BOUNDED_FOLLOWUP
OWNER_ROUTE=C_LOCATE_REAL_INPUTS_AND_LAUNCH_WITNESS_FIRST
NEWER_HA=PREFERRED_REVIEW_CANDIDATE_ONLY_NOT_FORMALLY_ADOPTED
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 1. 唯一目标与新增授权的精确边界

Owner明确指出：**Codex会在D盘根目录建立多个文件夹保存模型不同版本/不同阶段进度**；现在允许检查这些项目关联目录的版本时间戳和少量已知数据源名称。此前在当前科学工作区的项目相对`data_local/`内4次检查不存在的裁决仍然成立，不代表其他D盘模型版本文件夹也没有原件。

本次只读完成：
1. 精确检查 Windows `D:/` **根目录一级目录的名称/创建时间/最后修改时间**，选出明确与本博士论文第五章、HANK、多省、多资产、MATLAB/Python模型、Codex历史模型工作区相关的**至多15个**候选模型版本目录；用相关目录中非常有限的固定文件名/README或AGENTS、版本标签/安全Git身份辅助排序。对无关个人、应用、财务、生活文件夹只做“不属于模型候选”的即时分类，不展开、不发布名称。
2. 在已选候选目录内，检查具体已知路径及直接目录元信息：`data_local/matlab_primary_source_snapshot/`与3个basename、`validators/multi_province/`入口、`exports/matlab_faithful_two_asset_ha.py`、`CURRENT.md`、`TASK_CURRENT.md`、`AGENTS.md`、已经明确命名的`run_manifest.json`/`batch_manifest.json`/`calendar_<year>_...json`。只允许限定层级，无任意递归或全盘filename搜索。
3. 为相关候选编制可审计的时间线：创建时间(Windows CreationTimeUtc)、最后写入时间(LastWriteTimeUtc)、如果候选确实独立Git工作树则只读 HEAD commit hash/commit author/committer时间、关键文件时间与必要SHA256，标注本地时区与UTC；不得只因目录较新就宣布科学版本更新/真实生产采纳。
4. 尝试精确定位以下3份旧primary原始文件及项目版本来源：`中国各省省会地理距离矩阵.xlsx`、`2000年后各省数据_填充NA.xlsx`、`R语言估计结果_plm估计.xlsx`。只有原件在受授权目录中的确切路径可读时，才计算size/SHA256并与`validators/multi_province/mp4c_python_annual_empirical.py:34–38`中expected hashes逐项比较；不得打开Excel工作簿内容或扫描所有文件。
5. 若同一模型目录有确切已知的run/canonical记录，择最多3件做只读有限schema/年份/representation/sourcehash/code SHA字段核验；明确历史运行见证≠Owner当前TEMP31采纳。找不到就是UNKNOWN/BLOCKED，不重做运行或生成任何JSON。
6. 给Owner一张“版本时间线+原件可能在哪个已认证候选”表。绝不自动选“最新”、不拼接旧版本原件到新工程、不修改pin或更换运行来源。当前TEMP31入口、原件共同vintage、31省ID及D1/B D2 D3/B仍以科研来源为最终门槛。

## 2. Gate A：工作区保护与D盘根目录受界元数据

A0. Codex先从GitHub任务固定发文commit读取完整规则、AGENTS、Owner授权和旧独立验收。采集当前科研工作树 branch/HEAD、index/refs、dirty/untracked、11件既有保护资产before fingerprint；任务末再次测after。**禁止** checkout/reset/stash/rename/move/copy原件、变更任何source或创建模型目录。工作空间身份不符合则STOP并报告，不要修复它。
A1. 仅允许一次 `D:/` 根**直接子目录**目录元数据列举。总量最多120个立即子目录；如果超过120或权限不足，则STOP并报告超界，不截取一部分假称“全盘已检”。根目录文件、未授权盘符、用户profile、隐藏/系统目录、链接/ junction/reparse-point均不可进入。禁止`Get-ChildItem D:/ -Recurse`、全盘`rg`、`where /r`、`dir /s`、glob循环深遍历、文件内容索引或目录/磁盘读写扫描。
A2. 只将文件夹名/来源线索明确关联第五章/HANK/多省/MATLAB/Python/模型版本/科研项目或既知`D:/ProjectTemp`中CH5前缀任务目录的候选纳入核查。最多15个模型或相关证据候选文件夹；命名含糊不能凭个人资料好奇心进入，应`NOT_CLASSIFIED`并STOP待Owner提供名称。无关目录绝不展开或抄进GitHub。
A3. 每个候选只可读取文件夹本身的CreationTimeUtc、LastWriteTimeUtc、Attributes和限定的直接子文件/子目录名称与时间；总子目录元数据列举最多30次，目录层级相对候选版本根最多2（仅当明确发现 `data_local`、`matlab_primary_source_snapshot`、`validators`、`multi_province`、`exports`、`docs`、`run`、`results`等已识别项目结构才允许向下精确path check）。对`D:/ProjectTemp`仅允许直接列举带`ch5`任务前缀的子目录时间及其确切已知receipt的文件元数据，不读其它文件。
A4. 防范 NTFS junction/symlink/reparse point逸出D盘授权范围；命中就记录`REPARSE_POINT_NOT_FOLLOWED`、不展开。不能使用另一账号、提升权限、改变ACL或协议绕过。无关原件的路径一律不进入。
A5. 文件/文件夹时间必须同时记录UTC和Asia/Shanghai(+08:00)显示或明确时区转换。CreationTime可能是复制/解压生成时间、LastWriteTime可能由解压保留、Git commit时间是历史提交标记；时间戳**不是来源真实性/科研正确版本的证明**。对每个“最新”建议必须列出各证据的冲突/可信度，而不能凭mtime推出Owner批准。
A6. Git元数据只在确实是已授权模型目录且发现有效`.git`时做最多6组`rev-parse HEAD`、`git log -1 --format=...`、Git工作区当前分支的**只读**检查；不checkout、不fetch/pull、不遍历Git历史、不更改refs/index。独立历史工作树与当前保护的科研工作树不混用。
A7. 保密：GitHub只公开候选别名`D_MODEL_01`、`D_MODEL_02`等（或`D_CH5_RECEIPT_01`）及相对于该候选根的必要安全文件名、UTC/本地时间和哈希。绝不发布Windows用户目录、私有绝对D盘路径、无关D根目录名称、用户名、邮箱、凭据。Codex本地任务scratch可另存仅Owner可见的`OWNER_LOCAL_PATH_LOOKUP.json`，准确映射别名→本地全路径；**此文件绝对不上传GitHub**，只在最终摘要给Owner准确的本地保存位置，GPT不会假称可以访问。
A8. 若找不到任何模型候选目录或超过预算，停止有界调查，给出受界发现覆盖/Owner需指定的模型版本目录名称；不在其它盘自动搜索。

## 3. Gate B：三个primary原件与运行证据的限定核查

B1. 对候选模型根，只做下面的精确路径存在性检查，不对候选根任意递归`-Filter *.xlsx -Recurse`：
  - 版本根下`data_local/matlab_primary_source_snapshot/`的3个已知basename；
  - 如果已存在`data_local`、`data`、`inputs`或字面上直接指向primary/matlab原件的**至多2个已识别直接子目录**，在各自直下检查这3个basename；
  - 如候选根内已识别的配置/源码只读字符串明确引用了额外的具体相对位置，准许最多2个额外精确路径；
  - 其他目录或用户私人绝对路径均不获许可。不能凭同名猜证据身份。
B2. 全任务最多36次“精确文件exists/元数据”核验（包括三个basename在各候选的检查）、最多9份确实存在的source/workbook候选进行size+SHA256，最多6份关键版本源码做raw hash，最多3份有确切来源目录的run/canonical manifest进行受界header/schema/hash与安全字段读取。遇大文件时只做流式哈希，既不按需导入项目模块，也不解包Excel/缓存。
B3. 对不同候选目录里的同名文件必须逐件记录原始SHA/size/mtime/创建时间/来源别名。可归组为`EXACT_RAW_SHA_MATCH_EXPECTED`、`HASH_MISMATCH`、`FOUND_NOT_HASHED_BUDGET`、`NOT_FOUND_AT_TESTED_RELATIVE_PATH`；源码预期SHA单独标`EXPECTED_CODE_CONSTANT`，不是现场原件测量。
B4. 路由证据必须四层分离：`STATIC_CODE_CALL`、`HISTORIC_EXISTING_RUN_MANIFEST`、`OWNER_APPROVED_ACTIVE_TEMP31_ENTRY`、`RUNTIME_EXECUTED_IN_THIS_TASK=FALSE`。比较现存run_manifest中的year/representation/code SHA与候选Git身份，不能将历史MP4C annual worker或清单名字提升为当前TEMP31正式入口。源SHA匹配也不证明31省ID映射/同一旧期tuple/vintage/税前净工资身份。
B5. 时间线说明：按目录CreationTime、文件LastWriteTime和Git commit time分别排序且分别标依据；指出哪些可能复制/解压所得，哪些时间逆序。提出最多3个优先请求Owner核实的候选，并附“需要Owner选择什么”说明。**不自动择最新文件替代当前原件、复制工作簿或合并任何运行输出。**
B6. 科研静态阻塞沿用：新版HA为Owner优先待审非正式采纳；旧`ORACLE_SHA`与新版原件不匹配，不能改pin/换文件/规范化换行；`fixed_zt_calendar_year` vs `zt_source_calendar_year`属于静态合同问题，历史Zt固定2020不能自动改steady-year；primary`常住人口` vs Owner-A`就业人数`未决，N与劳动单位/财政tax base未决；工作地目的地`tau_j`同税只扣一次为Owner目标但R2/R3局部隔离未入正式生产。三份NBS 2018工资候选`MODEL_ADOPTED=FALSE`，不得当作primary宏观原件。
B7. 若没有准确数据与run manifest，只交时间线、受界没找到清单和Owner最小路径清单，然后STOP；不得再提出“在未授权盘下搜索”的自动下一步，也不得因剩余预算再猜路径。

## 4. 白名单预算

MAX_D_ROOT_IMMEDIATE_DIRECTORY_METADATA=120
MAX_D_MODEL_CANDIDATE_ROOTS=15
MAX_CHILD_DIR_METADATA_LISTINGS=30
MAX_EXACT_FILE_EXISTENCE_OR_METADATA_CHECKS=36
MAX_SOURCE_WORKBOOK_RAW_SHA256_CHECKS=9
MAX_MODEL_CODE_RAW_SHA256_CHECKS=6
MAX_GIT_METADATA_ROOTS=6
MAX_EXISTING_RUN_CANONICAL_MANIFEST_READS=3
MAX_ADDITIONAL_REFERENCED_RELATIVE_PATHS=2
MAX_INSPECTION_DEPTH_AFTER_CANDIDATE_ROOT=2
TOOL_FAILURE_RETRY=1_FOR_TRANSIENT_METADATA_ERROR_ONLY
SCIENCE_EXECUTION_BUDGET=0
NUMERIC_MODEL_BUDGET=0
MODEL_CALLS=0
TEST_BUDGET=0
NO_HA_TESTS=0
PREFLIGHT_BUDGET=0
PROJECT_IMPORT_EXECUTION=0
PRODUCTION_SCRIPT_EXECUTION=0
CANONICAL_GENERATION_EXECUTION=0
RAW_EXCEL_CONTENT_OR_SHEET_READS=0
DATA_TRANSFORMATIONS=0
ORIGINAL_FILE_COPIES_MOVES_EDITS=0
SOURCE_WRITES=0
MODEL_RESULTS=FALSE
EXTERNAL_DOWNLOADS=0
UNRELATED_DIR_EXPANSION=0
ROOT_WIDE_RECURSIVE_SEARCH=0
LOCAL_WRITE_ALLOWLIST=ONE_TASK_OWNED_DISPOSABLE_SCRATCH_FOR_SANITIZED_REPORTS_AND_PRIVATE_OWNER_PATH_MAP
GITHUB_WRITE_ALLOWLIST=tasks/CH5_TEMP31_D_DRIVE_VERSION_TIMELINE_AND_PRIMARY_SOURCE_LOCATOR_R1_20261027/__ISOLATED_CANDIDATE_ONLY
PROTECTED=SCIENCE_WORKTREE_INDEX_REFS_DIRTY_UNTRACKED;SOURCE_DATA_TEX;V010_V011;R2_R3;HISTORICAL_STOP_PENDING;NBS_WORKBOOKS
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

不读取`D:/`无关目录内容，不触碰私人/系统目录，不用无人授权的大范围索引，不能换权限/凭据/协议绕过拒绝。已知文件 hash/mtime 等只读元数据可在Owner新范围内执行；不要启动科学脚本/测试或宏观数据转换。

## 5. 交付：证据先GitHub，再STOP

Codex按Owner已授权的普通SSH，在从`1aa1026daceb6b0966470f28fcaa7516cde4a908`建立的**独立**候选分支`codex/ch5-temp31-d-drive-version-timeline-source-locator-20261027-r1`只创建目录`tasks/CH5_TEMP31_D_DRIVE_VERSION_TIMELINE_AND_PRIMARY_SOURCE_LOCATOR_R1_20261027/`。冻结任务发文commit由GPT公布，它不同于候选固定parent，必须使用真实GitHub链接读取全文，不能为了让它一致而改parent。

仅允许上传以下安全文件（有缺口也必须写UNKNOWN/BLOCKED）：
- `result.md`：受界根目录覆盖、各时间依据、发现3份primary/运行清单与否、实际预算、STOP；
- `d_root_model_version_timeline.md`：模型候选别名与时间、Git commit来源、关键文件mtime和可信度，禁止泄露无关文件夹；
- `d_root_model_version_ledger.json`：元数据查询、depth、时间UTC+本地、alias、候选规则、原件是否找到、budget；
- `primary_macro_source_candidates.json`：三份primary原件的分候选size/SHA/source expected哈希匹配、文件mtime、可信度，没有就NOT_MEASURED；
- `launch_and_canonical_witness_candidates.md`：已有运行清单的准确信息 vs static candidates vs Owner未批准；
- `owner_decision_brief.md`：最多3个优先候选别名与理由、实际原件路径信息**仅指向本地私有lookup，不放D绝对路径**，需要Owner确认的版本/年份/统计口径；
- `source_inventory.json`及`source_excerpts.json`：必要原路径来源类、短摘录和原始SHA/Blob、敏感路径的可审查脱敏映射，不在GitHub公布完整私人文件内容；
- `audit_checkpoint.json`、`gap_register.json`、`privacy_report.json`、`INDEPENDENT_COMPLETION_EVENT.json`(如无独立见证=UNKNOWN)；
- `manifest.json`：每个payload path/UTF-8字节/SHA256/Git Blob；最终seal自身引用按既有外置规则处理；
- `DELIVERY_FINAL_RECEIPT.json`：候选分支、payload/seal SHA/parent/tree、远端逐文件身份回读、真实预算与STOP。
本地**仅Owner可读、不上传GitHub**：`OWNER_LOCAL_PATH_LOOKUP.json`别名→实际D盘绝对目录和具体原件路径，含必要本地时间与哈希。只在任务私有scratch保存，禁止写入科学工作树/受保护D盘版本目录。公开报告不得含用户名/私人根、无关目录、账号凭据。

完整GitHub报告上传独立候选并固定commit后，须远端回读路径/Blob/bytes/sha256、candidate parent/root tree；如SSH回读中断记录失败且STOP，不反复提升权限/改凭据；GPT审阅时独立固定commit再核。接受A/B/C独立审阅与Owner最终选择，无自动合并/清理/后续任务。

## 6. 硬门与终态

artifact_integrity=TO_BE_VERIFIED
source_identity=METADATA_OR_RAW_BYTES_AS_AVAILABLE__NOT_SCIENTIFIC_ADOPTION
numeric_review=NOT_RUN
implementation_review=READ_ONLY_VERSION_TIMELINE_AND_PATH_DISCOVERY_ONLY
scientific_review=NO_FORMAL_ACCEPTANCE
privacy_review=BOUNDED_MODEL_DIRECTORY_ALIASES_ONLY
actual_terminal=STOP_AFTER_GITHUB_FIXED_READBACK
delivery=AUTHORIZED_SSH_ISOLATED_CANDIDATE
cleanup=NOT_AUTHORIZED_NOT_PERFORMED
not_completed=ACTUAL_TEMP31_OWNER_ADOPTION;31_PROVINCE_REAL_CANONICAL_JOIN;D1_D2_D3;NEWER_HA_FORMAL_SOURCE_REVIEW;NUMERIC_MODEL
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
