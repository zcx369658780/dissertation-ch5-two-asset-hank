# V010 当前 timestamp 证据交换：首次写入早于路径身份核验的独立限域主审

**审议日期：**2026-10-17（Asia/Shanghai）。  
**固定任务：** `V010_CURRENT_TIMESTAMP_SANITIZED_EVIDENCE_EXCHANGE`。  
**冻结发行Commit：** `74b1a21f9012c60fe3ad3f3a620e0e33f214083b`。  
**冻结任务Git Blob：** `f1567a2d8b96eacadbaa951dcf955adbfc589f98`。  
**Owner转述交付ID：** `V010_CURRENT_TIMESTAMP_SANITIZED_EVIDENCE_EXCHANGE_RESULT`。  
**正式裁决：** `FAIL_CLOSED__LOCAL_ONLY__PREWRITE_PATH_IDENTITY_SEQUENCE_VIOLATION_REPORTED__NO_EXECUTION__NO_REMOTE_CANDIDATE__NO_ENGINEERING_OR_SCIENCE_PASS`。  
**任务终态：** `DELIVERED__STOPPED`，`ACTIVE_TASK=NONE`。  
**下一门：** `WAIT_OWNER_FRESH_V010_PREWRITE_IDENTITY_GUARD_AND_EVIDENCE_EXCHANGE_AUTHORITY / STOP`；不自动恢复旧任务、不授权新Git发布、Python、runner或HA。

## 一、Astra独立核验的GitHub事实

Astra使用已连接GitHub工具直接读取仓库 `zcx369658780/dissertation-ch5-two-asset-hank`、治理分支 `migration/astra-workflow-20261012`。审议前HEAD为 `d3ddab6d790d30747cebac21d48e407644ced192`，对上一完成状态比较 `identical`（ahead0/behind0）。完整读取固定发行Commit中的`versions/0.0.10/current_timestamp_sanitized_evidence_exchange_task_20261017.md`，任务Blob实查 `f1567a2d8b96eacadbaa951dcf955adbfc589f98`，与CURRENT/TASK_CURRENT一致。

冻结任务第1节写明：**在新scratch创建和任何写入之前**核实新根及其父路径的真实身份，不是重解析/UNC/device/ADS或与受保护根发生别名/重叠；只有前置门PASS才允许在独占scratch编写五份脱敏候选与构建新的Git-only review对象。失败必须STOP，不可后补检查宣称第一次写入前已遵守。

目标独立review分支 `review/ch5-temp-v010-timestamp-proof-20261017` 经GitHub `search_branches`未返回匹配；又对该ref下预定 `manifest.json` 与 `result.md` 进行精确 `fetch_file`，二者均返回GitHub 404 `No commit found for the ref`。**截至此刻，独立核查确无目标review ref或五份远端候选文件可验；没有本轮remote-only临时审阅内容可清理。** 这不代表Astra实际审计了本地Windows scratch或被写出的两个文件。

## 二、执行顺序违规及封闭程度

据Owner完整转述Codex交付：本轮先**写入准备脚本**，而没有先完成冻结约定的**写入前路径身份检查**。Codex已主动披露顺序偏差并停止，没有执行该脚本，也没有读取旧来源或运行安全扫描、Git及科研进程。

精确分类：
- `PREWRITE_PATH_IDENTITY_CHECK=NOT_DONE_BEFORE_FIRST_WRITE`，`PROCESS_ORDER_COMPLIANCE=FAIL`。该违规因第一次写入已经发生，不能由事后补检追溯消除。
- `WRITTEN_SCRATCH_ROOT_IDENTITY=UNVERIFIED_AT_WRITE_TIME`。并无证据证明发生了受保护目录破坏，但也**不能**称写入动作已被原路径防护独立认证。
- `PREPARATION_SCRIPT_WRITTEN=YES (CODEX_REPORTED)`；`PREPARATION_SCRIPT_EXECUTED=NO (CODEX_REPORTED)`。未执行只约束后续脚本行为，不会使首次写入顺序变合规。
- `OLD_EVIDENCE_READ=0`、`25_CASES_RERUN=0`、`SANITIZER_SCAN=0`、`GIT/SSH/FETCH/PUSH=0`、`PYTHON/VERIFIED_LOADER/REAL_RUNNER/HA/HJB/KFE/GE/IRF/REAL_C8=0` 均为Codex报告，Astra没有本地操作审计和原件可独立交叉核验。
- `GITHUB_CANDIDATE_COMMIT/TREE/FIVE_BLOBS=N/A`，远端目标ref不存在则由GitHub独立核证；本轮不能宣称 `SAFE_PUBLICATION=PASS`、`BASIC_ENGINEERING_GATE=PASS` 或任何科学结论。

**明确裁决：** `FAIL_CLOSED/LOCAL_ONLY`作为遵循故障停点的交付状态被接受；但整体过程**不符合**写前门禁，严格保留为 `PROCESS_ORDER_VIOLATION`，不是工程合格证明，也不是单纯未运行的无害PASS。

## 三、资源、封存原件与本地证据等级

Codex报告**终态封存批次1次**，但未对PowerShell其他批次的计量提供清晰单独分类，不据此擅自写成`PS_STATIC_BATCH_1_OF_2`；新增非Git文件**2份，总25,733B**。尚未报告总墙钟、首次写入前的物理路径检查、两个文件的各自SHA或本机实际写入目标目录身份。新scratch文件位置必须保持原样取证，不能为通过结果而删改、移走或补做写前记录。

本轮最终回执 SHA256 由Owner转述为：

`EFC643EE08F7BE5E217DB748B11C7EA6C4E431C36B6FC00388EB0EE084A994B8`

Owner提供的是**Windows本地文件路径与SHA256文字声明**，没有通过连接器向Astra提供实际回执原始字节。故本项只可标记 `CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，**不得**标 `ASTRA_INDEPENDENTLY_REHASHED`；不能从该SHA值反推出file contents、真实本地路径身份或已完成全套资源门。

冻结任务允许的网络/Git、PowerShell和发布资源一经STOP全部封闭，不能将“未用”额度顺延到后继任务；历史所有STOP额度与超额记录亦不得清零。

## 四、旧有效证据继续分账，科学主线保持冻结

紧邻上一正式主审 `versions/0.0.10/source_script_provenance_conditional_timestamp_local_only_primary_review_20261017.md`、Git Blob `d6a53e96e359ac2c3d437ed9025cd5f58b129492` 的限域裁决不变：Codex此前报告当前PS 7.6.6 对合法JSON String/Z时间戳解析成`System.DateTime/Utc`，25个**此前执行的**合成案例24项符合预期、1项高精度形态 `SPEC_UNRESOLVED`，未获网页原件独立检验；本次25案**没有重跑**，不可因为本次STOP将其改记25项失败或完全PASS。前轮已找出脚本当下来源及当前hash，但**历史实际执行脚本原字节未记录**，依旧 `HISTORICAL_EXECUTED_BYTES_UNVERIFIED`。

更早B/S/L 20项旧first缺raw字节与run_id，永远`LEGACY_SEAL_CHAIN_UNVERIFIABLE`；此前17项合成工程和新seal仍为本机Codex报告级，最初被拒的脱敏候选 `PUBLICATION_DENIED`、根因UNKNOWN，历史ledger原argv/源码中间复制偏差 `UNRESOLVED`。

冻结V010科学计划 Commit `bf091da33d59293f147d52c11580327d3ac2a85d`/Git Blob `85138d8859d53295262fe13bf5bc277bca95ed3f`，模型 Commit `94de4501dec051b969bee9d852eba2d4591f30ef`/tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`不更改。原MATLAB修错、corrected两资产HA→多省顺序→GovInv收益边界0.9/1.1与Zt→冻结GDP各省≤1%独立目标→lagged-NKPC，目的地税一次、same-S/前完整轮raw ra0、家庭人均/省财政总量/三劳动账、phi_max=.3、20×20×2网格阈值不变；Owner corrected HA单点仍 `UNTESTED`。

`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`model_activation=False`、`Results FALSE`、`V011 NOT_STARTED`，以及 `A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`real C8 A–D REQUEST_ONLY`继续。Owner既有C盘物理独立SSD备份＋GitHub备份、现有SSHKey/443选择不变，但本次SSH未调用。原D盘8dirty/index/staged/untracked/ignored/外Git common-dir、所有旧失败scratch、C盘备份和真实C8/2017/2018/B3及V009失败数组不得越权触写。临时review路径只可能出现在另获授权的远端独立Git tree，本次未产生；不在本地任何工作树/index创建。

## 五、后继建议（没有自动授权）

建议Owner若继续，仅以**一次紧凑、受限的新证据交换工程任务**恢复合法实施，要求把`PREWRITE_PATH_IDENTITY`设计为第一次写操作之前的独立只读硬门：先只读校验目标不存在、父路径/句柄/重解析/别名与保护根分离并固定身份回执，再按严格scope新建目录/文件，接着重新检查根一致性；任何无法保证写前时序和目标身份的情况直接STOP。**不能在此已写入scratch上补“创建前验证”的证明，也不能删除已有失败文件后冒称新鲜root**。如果Owner同意新任务，应使用新的唯一scratch、ref、sole parent、五文件白名单与独立预算；前置合法之后才允许制作脱敏证据与GitHub发布。真实Python/runner/HA科研仍须后续另行授权。

**总终态：** `V010_TIMESTAMP_EVIDENCE_EXCHANGE_PREWRITE_IDENTITY_ORDER_VIOLATION__FAIL_CLOSED_LOCAL_ONLY__REMOTE_REF_ABSENT__TASK_STOP`。
