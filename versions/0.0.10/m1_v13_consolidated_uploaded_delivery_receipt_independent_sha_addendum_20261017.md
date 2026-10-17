# V010 M1 一体化长任务：用户上传原始交付回执的独立SHA核验补充审议

**2026-10-17｜V1.3 E2重要里程碑后续取证｜只读证据增级，不是新执行任务。**  
**原限域主审：**[M1 consolidated local-only candidate](m1_v13_consolidated_engineering_local_only_candidate_review_20261017.md)。原审议裁决仍保留，其此前`RECEIPT_RAW_NOT_AVAILABLE`状态由本次真实文件上传作局部修正。  
**冻结任务：**发行Commit `6f4df14b62fb7f5406b3df97707848aab21edf71`、Blob `762ad617365a82bc1fee2b0cc986b3e816edc883`。  
**正式增级分类：**`UPLOADED_RECEIPT_RAW_SHA256_INDEPENDENT_MATCH__SUMMARY_SHA256_INDEPENDENT_VERIFIED__DOCUMENTARY_SELF_CONSISTENCY_ACCEPT__REFERENCED_ENGINEERING_ARTIFACTS_NOT_PRESENT__NO_M1_FULL_RUNTIME_PASS`。  
**ACTIVE_TASK=NONE**，本次无Python/runner/GitHub review publication、科学运行或新额度。

## 1. 确实由Astra独立验证的字节

Owner这次直接上传了**实际文件**`DELIVERY_RECEIPT.json`和`DELIVERY_SUMMARY.md`到当前ChatGPT项目会话。Astra在隔离分析容器中对其原始字节读取、SHA256重算，而不是将本地Windows路径或先前报来的sha当文件证据。

| 文件 | 上传原始字节 | 容器独立SHA256 |
|---|---:|---|
| DELIVERY_RECEIPT.json | 5,875B | `E100A61CA00DBD510FF8C7E9417EB2C2663E66C73AEBEDD81B6581A85BF36F50` |
| DELIVERY_SUMMARY.md | 1,984B | `351BF6C2FDF378142A1FCC4DFCFD81390A204C834E512F8ADD74680B88F20EA0` |

**关键提升：**回执SHA256与之前Codex转述的`E100A61CA00DBD510FF8C7E9417EB2C2663E66C73AEBEDD81B6581A85BF36F50`完全一致，JSON按原件解析成功（27个顶级键），本次能独立验证**被上传的最终回执本身**的确切字节身份、它的声明内容与本次上传的摘要文字一致。**但这不等于验证回执内部列出的其他文件或Windows进程日志原字节。** 上传时间/Windows真实执行时间也不能由容器文件mtime证明。

固定模型`94de4501dec051b969bee9d852eba2d4591f30ef`、tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`、task issuer/blob在回执中与GitHub冻结值文本一致。`run_id=98dd956bb1d54154a1d449b244f83a50`是回执确实载明的当次标识，但未取得First/Final bytes证明同一run_id单向链接。

## 2. 回执与摘要内部交叉验证

- 工程Python `pythonControllers=15` + `dummyPythonChildren=8` = **23/24**，算术一致；科学调用在回执中标`0`，仅属本机声明。
- 固定Git raw source protocol流`2,212,964B` ≤ `16,777,216B`（16MiB），文字摘要一致；此为**回执的统计字段和上限比较**，不是独立流式限流原证。
- 新非Git工件回执生成前`5,030,611B`，加本次实获回执`5,875B`约`5,036,486B`，均远小于`134,217,728B`（128MiB），但未核Windows全scratch累计写入与terminal reserve的启动时序。
- 旧根11 distinct files、18成功读取、701,946B，符合摘要和本任务24件/8MiB总界的**回执声明**。
- 控制器peak RSS `85,770,240B`，其他Git/dummy RSS显式`UNKNOWN`；`elapsedFromFirstReceiptSeconds=892.7274707`，但`intakeWallBeforeFirstReceipt=NOT_PRECISELY_CAPTURED_TOOL_TRANSCRIPT_AVAILABLE`，**不能把892.727s当全部墙钟独立证明**。
- `runnerGit=20`、`sourceGit=14`、`publicationGit=1`是回执记账；主张的runner`FIVE_REAL_GIT_CHILDREN_PASS`和九模块`NATURAL_9_OF_9_EXPLICIT_ALLOWLIST_CONFIRMED_ADDITIONAL_0`仍需逐child/模块原始证据，不能凭标签认定真实Windows执行全过程已验证。
- `CANONICAL_ADAPTER=SCOPED_ADAPTER_ONLY_PASS`和`CANONICAL_NATIVE=BLOCKED_GIT_NO_CAPABILITY_NO_SPAWN`明确分账；不可将adapter-only导入提升为原生PASS或科学HA许可。
- `PUBLICATION_ONE_SSH_REF_PRECHECK_FAILED`、exit128、fetch/push/readback0；根因`COULD_NOT_READ_REMOTE_REPOSITORY_ACCESS_OR_EXISTENCE_UNRESOLVED`，不能自行推断账户/SSH键究竟是哪项失败。
- 文件索引中9份文件均给出64位hex SHA256、独立文件名和标称字节，合计**204,154B**；但这次只上传两份**不同的**文件，不能重算索引内任何一份的SHA或文件内容。

## 3. 必须如实保留的已披露差异

1. `E1_ATOMIC_LEDGER_PATCH_MISSED_LITERAL`事件报告范围`SEQUENTIAL_GIT_EXTRACTION_ONLY`、`concurrentWriters=0`、`recordRestoration=NONE_ALL_SEVEN_CHILD_RECORDS_ALREADY_PRESENT`，但是`prelaunchSnapshots=NOT_RETAINED`。总体`ENGINEERING_LEDGER=SINGLE_WRITER_ATOMIC_REPAIRED_INITIAL_SNAPSHOT_RETAINED`只能作为后续实际工程机制的本机报告级，**不能追溯证明最早Git children启动前原始快照完整留存**。
2. 早期`frozen_task.md`是与`frozen_task_RAW.md`不同的换行投影`DERIVATIVE_NOT_RAW`；早期投影Git Blob mismatch标明，虽然raw任务Blob与冻结身份对应。不得把换行转换后的副本当原始冻结文件。
3. 原`process_result_19/final.json`误记`n13.streams_complete=true`，实际有继承PIPE reader存活时应为FALSE；Codex保留原件并报告派生表达式已修。当前N13为约2秒的本机正向报告，**不能据派生布尔字段声称原日志已被修改或完全独立验证**。
4. `sealPreflightFailure`记载`REGISTERED_PID_ABSENT`、原因`UNKNOWN_OR_TRANSIENT_PID_REUSE`，后续按process creation time检查且无进程被杀，但早期PowerShell host wrapper PID仍`UNKNOWN`。未知保留。
5. `oldDummyOverflowProbeBytes=UNKNOWN_ORIGINAL_RAW_RETAINED`和`earlyGitPrelaunchSnapshots`缺失仍是不完整证据，**不能把后来成功的总量与摘要解释成历史每次流量/启动事件均被完整重放**。

## 4. 索引中9份仍未收到的工程原件

| 已存在的原件名称 | 回执载明字节 | 回执载明SHA256（非独立复算） |
|---|---:|---|
| FIRST_RECEIPT.json | 1097 | `4F1511731A3A01C4F69136F5B9F7C81E0F492F21202107D8EDF9108131B87F32` |
| ENGINEERING_FINAL_RAW.json | 6879 | `80F224002E4A5B41ABF3D7E14CB522F3E948329658DE1AB40E17A485B99D24CF` |
| manifest.json | 1290 | `C2A6D9C1C6E96445B5DBA0BB0D9729A482F3D8684F6F2287DED18D460F4550BB` |
| result.md | 3238 | `72A2236FAAA7A2DF33D85FAF042CBDE52C17704D8714AAB4E50D5A63ACB054BB` |
| engineering_evidence.json | 43997 | `4128FAF7755876A2AD7B2C44FCE5E4646DE681E939E9A35B8845D62BA112AB3A` |
| runner_candidate.txt | 64668 | `5FA1DC0272BEC4DAF7CD35B73141C8CCEBCF91249843FABF83DB60763F2E6391` |
| PUBLICATION_RECEIPT.json | 1178 | `644F376B591CD2011447D42771EE3BAA0861712B7FE8400C906491E7066D1E32` |
| TERMINAL_ARTIFACT_INDEX.json | 61929 | `505B58F273B3D5351692D50CF2D22463D42BC21FDC60155B74A9B441F34BBD73` |
| LEDGER.json | 19878 | `901179BF0C41941EF69C175AC18842D711A28E2AF96CBCEB6AB619C2E905E8BF` |

一次性补齐建议：Owner只需将**已存在的**上述9份文件原字节打成单个ZIP上传（在本地先检查无token、SSH key等秘密；若需安全派生，必须另列`SANITIZED_DERIVATIVE`，不得伪装raw）。这一动作**无需重新运行Python/runner、无需再发一张GitHub发布微任务或覆盖原失败**。Astra得到真实9原件后可批量计算其哈希，核first/final/run_id、adapter/模块/五Git child、N13和原子ledger边界，并依法保留任何仍UNKNOWN项目。

## 5. 科学与保护停点

**维持：**`ACTIVE_TASK=NONE`、`M1_FUNCTIONAL_CANDIDATE_CODEX_REPORTED`、`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`model_activation=False`、`Results FALSE`、`V011 NOT_STARTED`。冻结科学计划Blob`85138d8859d53295262fe13bf5bc277bca95ed3f`不变；corrected HA单点未获新运行许可。先前旧seal不可追证、原stdout超限失败、保护根/C SSD备份/真实C8与A16/window/C9/CALL_LEDGER硬边界持续。

**终态：`UPLOADED_RECEIPT_IDENTITY_INDEPENDENTLY_VERIFIED__REFERENCED_NINE_ARTIFACTS_PENDING__NO_NEW_SCIENCE_AUTHORITY`。**
