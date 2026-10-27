# TEMP31 C方案 · 现存距离矩阵与生产启动/Canonical来源认证前置门（有界只读）

TASK_ID=CH5_TEMP31_C_SOURCE_LOCATION_LAUNCH_PROVENANCE_GATE_R1_20261027
STATUS=ISSUED_WAITING_LOCAL_CODEX__OWNER_AUTHORIZED_C
DATE=2026-10-27
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=40b48a85e8ed66265dde29a9cda98c51778811d8
CANDIDATE_FIXED_PARENT=40b48a85e8ed66265dde29a9cda98c51778811d8
CANDIDATE_BRANCH=codex/ch5-temp31-c-source-location-launch-provenance-20261027-r1
TASK_PATH=tasks/CH5_TEMP31_C_SOURCE_LOCATION_LAUNCH_PROVENANCE_GATE_R1_20261027.md
EVIDENCE_DIR=tasks/CH5_TEMP31_C_SOURCE_LOCATION_LAUNCH_PROVENANCE_GATE_R1_20261027/
TASK_PUBLICATION_COMMIT=RESOLVE_FROM_FIXED_GITHUB_TASK_URL_AFTER_ISSUANCE
FIXED_SCIENCE_GIT_REF=b69ae535a1518c68822733603f1e506620327375
FIXED_SCIENCE_GIT_TREE=8dbd81c0938f603511c7de1c763ed29b6d2d4b83
PREVIOUS_TASK_CANDIDATE=bdc2091de80dd6a82013534fd39013ffb5acbb07
PREVIOUS_INDEPENDENT_REVIEW=40b48a85e8ed66265dde29a9cda98c51778811d8
PREVIOUS_VERDICT=PASS_BOUNDED_DECISION_PREPACKAGE__SOURCE_PATH_AND_PRODUCTION_CANONICAL_GATES_BLOCKED
OWNER_DECISION=C_SOURCE_AND_AUTHENTIC_LAUNCH_EVIDENCE_FIRST__NEWER_HA_PREFERRED_REVIEW_CANDIDATE_ONLY
DELIVERY=GPT_FROZEN_GITHUB_TASK__OWNER_TO_LOCAL_CODEX__AUTHORIZED_SSH_ISOLATED_BRANCH__GPT_FIXED_COMMIT_REVIEW__OWNER_DECISION
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 1. 唯一验收问题和Owner C方案选择

Owner于2026-10-27明确同意采用C方案并继续执行：**先认证现存数据源的位置/原字节身份与TEMP31启动/生成的证据，随后才另议B方案新版HA原字节守卫。**
本任务一次完成“有界来源定位和准确证据缺口”：
1) 前轮Codex在项目固定默认相对路径 `data_local/matlab_primary_source_snapshot/中国各省省会地理距离矩阵.xlsx` 报MISSING_AT_EXACT_PATH。新授权只允许在指定项目内元数据位置、精确3个原始宏观文件名和文件自身允许读到的直接路径中定位，记录原件size/SHA256与代码expected SHA的证据关系；不搬迁、复制、改名、重建或打开表格单元格。
2) 识别当前拟采用的MP4C/TEMP31生产入口的**来源身份层级**：静态runner/worker/anchor，是否确实存在同版run/batch清单、Owner批准命令、representation、year与code SHA；如果无真实授权或运行记录则明确UNKNOWN/BLOCKED。识别实际使用的canonical输入路径/bytes/hash及producer记录，不凭算法、变量名、历史输出推断已运行。
3) 整理Zt旧`fixed_zt_calendar_year=2020`与新版`zt_source_calendar_year`字段、`empirical.py:105`对旧属性的静态引用，以及常住人口vs就业人数两个来源表名作为**后续Owner合同决策清单**，不选Zt年、人口N定义，不修源码。

成功只允许是 **PROVEN_BOUNDED_FILE_IDENTITY / PROVEN_STATIC_REFERENCE / VERIFIED_EXISTING_MANIFEST** 级别；不能因为发现Excel或缓存哈希匹配而升级真实生产、D1/D2/D3或科学接受。
不重复上轮13件证据、38段摘录与A/B/C比较，只引用固定commit，补C路线新增证据。若位置找不到也要给出有限范围排除表和Owner最少应提供的准确路径。

## 2. 冻结知识、科研选择保留

- 当前治理权威 = 本任务发文commit继承40b48a85e8ed66265dde29a9cda98c51778811d8；上轮正式独立报告=`docs/CH5_TEMP31_NEWER_HA_DISPATCH_CANONICAL_CONTRACT_PREPACKAGE_R1_20261027_INDEPENDENT_REVIEW.md`。
- 受保护原始科研Git来源commit=`b69ae535a1518c68822733603f1e506620327375`，tree=`8dbd81c0938f603511c7de1c763ed29b6d2d4b83`。历史旧pin `b92f6efc59d9398f89f8fb6ee67bf6c5f947282d76895051bec194967ec9c3e3`有旧版本对应；较新版Git HA原件31143B，sha=`a7539eb6ba076176b81f832c1800d38d8d170dad8f3619d3b0f3893c5a163fff`、Blob=`e144c645d3f4dc842c2faa6b93b2ba0e24275dcf`，执行者本地CRLF另有真实原字节SHA。Owner仅批准新版**优先待审**，未批准修改pin、换行或采纳版本。
- 明确静态路径：`validators/multi_province/mp4c_python_annual_production.py:155`→`mp4c_python_annual_empirical.py:74-82`→`data_local/matlab_primary_source_snapshot/中国各省省会地理距离矩阵.xlsx`。其他两条原件精确名字=`2000年后各省数据_填充NA.xlsx`、`R语言估计结果_plm估计.xlsx`，都仅是模型旧primary来源而非新增三份NBS工资原件。
- 已知静态调度器`validators/multi_province/mp4c_run_full_annual_batch.py`调用annual worker；可能有primary annual、runtime_cache或Owner-A三种不同表述/物化路线。持久化合同 `validators/multi_province/matlab_persistence_contract.json` 只包含legacy/cache/checkpoint定义，不是Owner当前TEMP31实际launch。
- `annual.py`新`CanonicalAnnualInput`定义`zt_source_calendar_year`、无`fixed_zt_calendar_year`；同源当前`mp4c_python_annual_empirical.py:105`却读旧属性，属于静态接口差异，**未运行因而未观测AttributeError**。历史Zt固定2020≠新路由按steady year，别自行统一。 `annual.py:441`读常住人口，`mp4c_owner_a_2009_2022.py:35`定义就业人数；任何模型N/实际就业或有效工时意义留Owner。
- 工作地/目的地`tau_j`及同一工资税单次征收为已决目标；R2/R3局部修订仍隔离、正式合并/生产接线未闭合。D1=B旧期同快照tuple，D2显式31省生产adapter，D3=B先no-HA synthetic spy均目标合同但当前无真实证明。
- 三份2018 NBS-claimed工资Excel未正式采纳，不能拿它们替代上述3份primary原件，不能猜测原表缺失值30、生成工资/就业桥或改变vintage。历史2009共用scalar w,wjt,tau不是实测31省工资。
- 仅有Windows本地执行者可看见其本地科研目录；GPT通过GitHub不能直接看到用户Windows原始目录。报告每项身份必须区分LOCAL_EXACT_BYTES、HISTORIC_GIT、SOURCE_METADATA_ONLY、OWNER_APPROVAL、RUNTIME_WITNESS、UNKNOWN；不得以源名/哈希常量冒充完整原件或已运行。

## 3. Gate A：保护状态及项目内**有界精确文件名定位**

A0. Codex从GitHub固定发文commit读取本任务全文和当前AGENTS/工作流/Owner委托。先记录真正科学工作区分支HEAD、index、refs、dirty/untracked与11件保护资产身份，完成前后对比；即使不等于旧快照也不能checkout/reset/stash、清理或更改原件来匹配。GitHub候选写入使用独立scratch/隔离分支，不接触真实科研工作树。
A1. 先对冻结代码中出现的3个basenames做精确存在性核验，只依据下列**有限相对范围**（先有直接证据再加一层）：
  - 项目根 `data_local/matlab_primary_source_snapshot/` 的3个确定basename；
  - 项目根 `data_local/` 的**直接条目**和已存在且名字明确指向primary/matlab输入的**至多2个直接子目录**，仅列名称/是否目录/文件大小，不递归遍历子树；
  - 现有 `validators/multi_province/` 中的 `mp4c_python_annual_empirical.py`、`mp4c_python_annual_production.py`、`mp4c_run_full_annual_batch.py` 和 `matlab_persistence_contract.json` 的已知输入相对路径引用；
  - 如上述源或已批准的现存清单给出**另一条具体的项目内相对路径**，才允许最多2条精确额外路径检查；路径必须在repo root下、不得符号链接逃逸、不得通向私人绝对根。其它根（如Downloads、D:/ProjectTemp、用户profile、云端）**未授权**。
A2. 这次**明确放宽前轮“首个默认路径不存在就STOP”的范围到A1白名单**，但禁止无限递归find/rg全仓/glob整盘/搜索管理员或其他磁盘。最多8次精确路径检查/定向目录元数据请求，最多3个原始文件候选做大小、SHA256及Git-style Blob（如适用）而不读内容。对每个候选标证据：ABSENT_AT_TESTED_PATH / FOUND_NOT_AUTHENTICATED / EXACT_BYTES_MATCH_EXPECTED_HASH / HASH_MISMATCH / NO_READ_PERMISSION。
A3. 只要遇到越界路径、权限拒绝、同名但来源版本含混、SHA/size不匹配，不把文件复制/改名/换行/覆盖/伪造回执，不尝试其它账号/协议、停止涉及该原件的认证；可在预算内完成**互不依赖的**静态入口和合同核查，不做隐含修复。路径仍不可得时生成Owner应提供的最小准确相对路径+源hash请求。
A4. 不打开任意Excel单元格或宏观sheet，不上传原始xlsx、数据行、保护Cache或私人root。expected SHA只是代码常量；真正sha必须来自当前原件读取或清晰标`NOT_MEASURED`。精确文件哈希也只能证明字节身份，不证明31省ID、年份、经济统计口径或model adopted。
A5. 关于 Zt/人口字段仅复核已冻结源码短摘录及真实版本身份，不改`fixed_zt_calendar_year`、`zt_source_calendar_year`、人口表名、统计单位、经济学公式。

## 4. Gate B：生产入口与canonical历史实存见证

B1. 只读`validators/multi_province/mp4c_run_full_annual_batch.py`、`mp4c_python_annual_production.py`、`mp4c_python_annual_empirical.py`、`mp4c_matlab_runtime_cache.py`、`mp4c_owner_a_2009_2022.py`及`src/ch5_two_asset_hank/multi_province/annual.py`已知必要行；程序**不import、不调用**。对每条候选写明caller/worker/anchor/representation/year/读取原件来源/expected原SHA和相应run/canonical文件位置表达式。
B2. 只允许验证已知/精确引用的运行清单名字：`batch_manifest.json`、`run_manifest.json`、`calendar_<year>_primary_premodel_input.json` 或 `calendar_<year>_matlab_runtime_cache_input.json`；只有在源码、已知任务元信息或Owner已有批准资料中**出现确切项目内相对所在目录/年份**时，才可做最多2件运行/生成metadata原件的只读验证。不可泛搜全部子目录或猜年份。若任何报告揭示真正工资/税/人口敏感数值，公开包只发布筛选安全metadata、相对路径/原hash/文件类型/允许的来源字段，原件不上传。
B3. 区分证据层：STATIC_CALLSITE、FILE_EXISTS_BYTES_VERIFIED、EXISTING_RUN_MANIFEST_OBSERVED、OWNER_APPROVED_ENTRY_AND_REPRESENTATION、RUNTIME_EXECUTED_THIS_SCOPE(永远FALSE)。现存持久化合同或源码“production”称谓不可提升到真实TEMP31采纳；即便存在过去annual运行清单，也不等于Owner今天授权为TEMP31。缺Owner明确入口/representation/year，写`OWNER_ADOPTION_PENDING`并给出可选的已有代码入口证据，不擅自替用户选。
B4. 三种canonical来源严格分开：primary source annual / protected runtime cache / Owner-A。只读产出入值的元信息、年份轴、31省名字和是否有真实hash；**绝不重生成canonical JSON或执行缓存**，绝不借NBS工资表填空。共同D1 tuple、D2正式31省adapter、D3先spy和正式税收工资接线保持BLOCKED，不能用历史旧期标量和候选spy伪造闭包。
B5. 对Zt年份字段静态接口/人口vs就业名称，形成`source-defined`对照与Owner选择清单。不要把科学定义选择归咎于工作流故障，不修`annual.py`与`empirical.py`，不运行可能触发AttributeError的代码。若真实输入缺失，不把“不知道”改成模型失败。
B6. 若存在并匹配精确输入原件，输出`SOURCE_FOUND_NOT_MODEL_ADOPTED`即可STOP并请求正式路线选择；若不存在，输出受限查找覆盖和Owner最少提供的3个字段（准确project-relative path或可授权目录、bytes/SHA256、来源时间/版本），不继续横向扩大查找。

## 5. 预算与读写白名单（授权时有效）

MAX_SOURCE_CODE_CONTENT_READS=10
MAX_LOCATOR_OR_DIR_METADATA_QUERIES=8
MAX_RAW_MACRO_SOURCE_HASH_CHECKS=3
MAX_EXISTING_RUN_OR_CANONICAL_METADATA_READS=2
MAX_METADATA_DIRECTORY_DEPTH=1_AFTER_REPO_LOCAL_ANCHOR
MAX_CONFIG_REFERENCE_FOLLOW_DEPTH=1
TEST_BUDGET=0
NO_HA_CHECKS=0
PREFLIGHT_BUDGET=0
SCIENCE_EXECUTION_BUDGET=0
NUMERIC_MODEL_BUDGET=0
MODEL_CALLS=0
HA_HJB_KFE_GE_IRF=0
PROJECT_IMPORT_EXECUTION=0
PRODUCTION_RUNNER_EXECUTION=0
CANONICAL_GENERATION_EXECUTION=0
EXCEL_SHEET_READING=0
DATA_TRANSFORMATIONS=0
FORMAL_SOURCE_WRITES=0
DATA_WRITES=0
EXTERNAL_DOWNLOADS=0
TOOL_RETRY_BUDGET=1_FOR_TRANSIENT_READ_ONLY_FAILURE_ONLY
LOCAL_WRITE_ALLOWLIST=TASK_OWNED_DISPOSABLE_SCRATCH_OUTSIDE_SCIENCE_WORKTREE_FOR_REPORTS_ONLY
GITHUB_WRITE_ALLOWLIST=tasks/CH5_TEMP31_C_SOURCE_LOCATION_LAUNCH_PROVENANCE_GATE_R1_20261027/__ON_ISOLATED_CANDIDATE_BRANCH_ONLY
PROTECTED=ALL_ORIGINAL_SCIENCE_WORKTREE_DATA_TEX_NBS_RAW_WORKBOOKS_OLD_TASK_EVIDENCE_V010_V011_RESULTS
NO_GIT_RESET_CHECKOUT_STASH_FORCE_PUSH=TRUE

不可绕过身份/权限/SSH限制；必须记录失败真实终态。允许将所需独立原始短源码片段、header、文件大小及hash发表为脱敏review evidence，但不能公开个人本地绝对路径/密钥或上传原始宏观工作簿。无任务之外临时清理、无Issue/PR/merge/auto-next。

## 6. Codex发布的证据硬门

仅可在独立候选目录 `tasks/CH5_TEMP31_C_SOURCE_LOCATION_LAUNCH_PROVENANCE_GATE_R1_20261027/` 写入：
- `result.md`：C是否在新限定范围内成功找到真实源？Source/production/Canonical各门状态、STOP、Owner最小缺口；
- `bounded_source_location_ledger.json`：每个精确路径的source/filename/provenance/exists/type/bytes/SHA/expected与真实测量区别、查询顺序、保护标记；绝不放私有绝对目录或源数据；
- `distance_and_primary_original_identity_matrix.md`：三份primary原件身份账本及源/原件关系，缺失也要有证据；
- `existing_launch_and_canonical_witness_matrix.md`：static代码入口vs现存真实清单vsOwner批准身份/年度/representation，三条canonical路线分开；
- `zt_population_contract_open_questions.md`：两个科学/接口差异的来源行号、条件风险、Owner未选择；
- `owner_decision_brief.md`：准确要补的本地相对源路径或批准目录、source hash、当前TEMP31实际拟采用的入口/representation/year，以及若仍缺源需要用户提供哪几项；
- `source_inventory.json`、`source_excerpts.json`：短而充分的真实源码上下文、原路径+源身份/字节/行号；历史已验收部分可固定引用而不重复粘贴。
- `gap_register.json`、`audit_checkpoint.json`、`privacy_report.json`、`INDEPENDENT_COMPLETION_EVENT.json`（无独立见证写UNKNOWN）。
- `manifest.json`：完整交付payload路径、UTF-8 bytes/SHA256与Git Blob分别核验及脱敏变换。
- `DELIVERY_FINAL_RECEIPT.json`：候选commit/parent/tree、任务发文commit、payload及最终seal远端回读/预算/STOP；seal自引用按固定惯例放外部回执，不自称文件写入后还能同时携带自己hash。

Codex根据冻结候选parent `40b48a85e8ed66265dde29a9cda98c51778811d8` 建立独立候选分支，**发文commit另由GPT后续发布，必须读取其固定GitHub全文**；不能擅自把candidate parent改成发文commit。采用已授权普通SSH推送候选，再按固定commit重读Git Blob、大小和SHA256。任何远端最终回读中断保留事实、立刻STOP；GPT后续独立读GitHub，不为传输原因重跑科学来源。
所有验收件应先在GitHub可读，GPT再分A身份、B来源/科研语义、C分层裁决。不得自动合并、清理或下一任务。

## 7. 科研保护及终态

artifact_integrity=TO_BE_INDEPENDENTLY_REVIEWED
source_identity=TO_BE_VERIFIED_WITH_BOUNDED_SCOPE
numeric_review=NOT_RUN
implementation_review=READ_ONLY_PROVENANCE_ONLY
scientific_review=NO_FORMAL_ACCEPTANCE
privacy_review=BOUNDED_METADATA_AND_SAFE_EXCERPTS_ONLY
actual_terminal=STOP_AFTER_EVIDENCE_DELIVERY
delivery=GITHUB_ISOLATED_SSH_CANDIDATE
cleanup=NOT_AUTHORIZED_NOT_PERFORMED
not_completed=REAL_31_PROVINCE_INPUT_JOIN;D1_D2_D3;TRUE_PRODUCTION_ACTIVATION;SCIENTIFIC_ADOPTION
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
