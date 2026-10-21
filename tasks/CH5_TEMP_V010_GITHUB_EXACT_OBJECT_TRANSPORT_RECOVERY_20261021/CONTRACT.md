# 第五章 TEMP V010：GitHub精确对象读取能力恢复｜B-only 长任务

TASK_ID=CH5_TEMP_V010_GITHUB_EXACT_OBJECT_TRANSPORT_RECOVERY_20261021
REVISION=ISSUED_20261021_R1
OWNER_APPROVAL=2026-10-21，Owner明确请求继续签发新任务
AUTHORIZATION=B_ONLY__CONNECTOR_EXACT_OBJECT_TRANSPORT_RECOVERY
BASELINE=543146f61e9bcf345ca1700bdc8149d4bc470ba7
SOURCE_COMMIT=5090d84c1cb4ae03b12a230b984bb312de92afeb
REVIEW_BRANCH=review/ch5-temp-v010-github-exact-object-transport-recovery-20261021
FIXED_PARENT=543146f61e9bcf345ca1700bdc8149d4bc470ba7
TEMP_PATH=_review_tmp/ch5/temp-v010-github-exact-object-transport-recovery-20261021/

## 1. 目的与已接受历史
这是新授权、新预算；旧任务 `CH5_TEMP_V010_CONTROLLER_LOCATOR_TWO_BLOCKER_RECOVERY_20261021` 已真实停止 `STOP_EXACT_GITHUB_BLOB_TRANSPORT_UNAVAILABLE`，总体NOT_PASS。A Windows身份采集为Codex六组合成测试限域报告，原生symlink未观察，Astra没有重新运行；**保留A原等级，本轮A测试调用预算0**。B首个精确Blob因连接器Transport send error无provider HTTP状态及原字节，其余三件未请求。
上一会话六文件治理归档已在live HEAD `543146f61e9bcf345ca1700bdc8149d4bc470ba7` 核验完成；**禁止重新补写旧归档**，仅本轮产生新结果后才进行新终审归档。GPT本次能够读取治理GitHub文件，不等于Codex自身连接器B已恢复。
唯一目标：在Codex获授权的当前连接器环境中，证明已知单Git Blob或固定路径单文件的完整原字节获取、身份与边界；明确区分transport、provider拒绝、原字节缺失以及真正的成功。没有必要也没有许可重写GitHub平台连接器、迁移账号或扩大到生产控制器搜索。

## 2. 四件固定来源（不可替换）
来源commit固定：`5090d84c1cb4ae03b12a230b984bb312de92afeb`。只读四件：
1. `tasks/CH5_TEMP_V010_CONTROLLER_SOURCE_PROVENANCE_LOCATOR_GATE_20261021/CONTRACT.md` — expected Git Blob `89c953cb0ed4f8e5f82eea0486a1a7b845910bd3`
2. `tasks/CH5_TEMP_V010_CONTROLLER_SOURCE_PROVENANCE_LOCATOR_GATE_20261021/TASK_PARAMETERS.json` — expected Git Blob `dec4b2af86710fb4529f537643d3b70d7ccf7c0b`
3. `tasks/CH5_TEMP_V010_CONTROLLER_SOURCE_PROVENANCE_LOCATOR_GATE_20261021/ISSUE_MANIFEST.json` — expected Git Blob `92ddcee91f89ee014c6e33c7bdb64d6734b8e97d`
4. `docs/CH5_TEMP_V010_CONTROLLER_SOURCE_PROVENANCE_RESOURCE_STOP_INDEPENDENT_REVIEW_20261021.md` — expected Git Blob `626544b0ca0795de2c68898db418091b18814f93`
严禁查询 `GET /contents/tasks`、`list_directory(tasks)`、GitHub根recursive tree、宽目录页、clone、泛搜索，不能把旧400项截成64。不得追加任何第五件来源。B的成功只证明这些对象可安全读取，不等于旧控制器P2-P5已执行或supervisor/reader已找到。

## 3. Bootstrap与保护
从ISSUE_MANIFEST固定issue commit及合同/参数Git Blob；先读取同一live治理 `CURRENT.md`、`TASK_CURRENT.md`、`docs/DOC_INDEX_CURRENT.md`，确认唯一ACTIVE。旧离线/缓存不是执行权限。可信父目录 `D:\ProjectTemp`，新scratch唯一 `D:\ProjectTemp\ch5_temp_v010_github_exact_object_transport_recovery_20261021_01`；仅先核可信父身份及scratch不存在、拒绝reparse/unsafe，然后创建并只写自有scratch。不能以新Windows原生inode测试替代此安全最小引导；不枚举旧目录、不读取旧历史scratch/archive/journal、不触碰正式Git index。
原始尝试意图、序号、SHA/path/ref、错误和响应先持久写入自有journal，flush+os.fsync并readback后判定；写失败STOP，不推算缺失日志。必要Python仅用于标准库hashlib、json、zipfile及本任务证据。

## 4. 有界B流程及分类
B0：只检查现有获授权连接器的精确单Blob/精确路径原生接口签名、请求种类及长度界。不得试探其它账号、token、SSH、代理、web回退、手写不支持调用或目录接口。
B1：首选固定Blob `89c953cb0ed4f8e5f82eea0486a1a7b845910bd3` 的单对象读取一次。记录真实transport异常与provider HTTP状态（未返回则明确UNKNOWN），不得把发送失败说成GitHub 401/403/429或文件不存在。仅发生不带provider拒绝的transient send/timeout时，允许**同账号、同连接器、同方法、同对象**最多一次有界恢复读取；401/403/429/策略或权限拒绝硬STOP，不重试、不换认证或协议。
B2：若精确Blob取得完整原字节，继续其余三枚Blob各一次；若Blob仍transport阻断且从未出现provider拒绝，只能在同账号**同一连接器**已明确支持单文件边界的前提下，用固定commit+完整path做一次同一首文件的对照，再最多读取其余三件固定path。此分支成功必须单独标为 `EXACT_PATH_ONLY__BLOB_ENDPOINT_UNRESOLVED`，不得冒称Blob端点已恢复。两条路线均不得扩大对象数；单个响应若目录/列表/未知或大于边界立即STOP。
B3：对实际解码完整字节验证length、SHA256以及原生Git Blob `sha1(b"blob "+ascii(length)+b"\\0"+raw_bytes)`；须等于各自冻结40位Git Blob。只返回URL、文本摘要、Blob字符串或不可转成完整原字节的Base64声明，归类RAW_BYTES_UNVERIFIED而非PASS。文件路径模式还核精确固定commit/path与provider文件blob身份。
B4：分别给出 `BLOB_EXACT_4_OF_4_VERIFIED`、`PATH_ONLY_4_OF_4_VERIFIED__BLOB_UNRESOLVED`、`PARTIAL_VERIFIED`、`CONNECTOR_TRANSPORT_BLOCKED`、`PROVIDER_POLICY_STOP` 或 `IDENTITY_OR_RAW_BYTE_STOP`，依实际证据分类。路径可用不等于原Blob端点恢复，任一成功不等于生产GLOBAL_STOP有效。未取得原字节不能靠合成mock刷成功。
冻结源请求≤9次（首Blob≤2、其余Blob≤3、同连接器精确路径≤4），成功解码内容合计≤45000字节，单文件先验不安全时STOP而不接收无界响应；源路径与Blob不得计算推导替换。

## 5. 原件、交付、验收及清理
自有脱敏证据至少包含 `capability_preflight.json`、`exact_attempt_journal.jsonl`、`response_identity_checks.json`、`failure_classification.json`、`safe_exact_read_recipe.md`、`first_error_and_budget.json`、`privacy_and_protected_roots.md`。可审阅真正读取的响应身份/必要有限源码或脱敏原字节，不能只提供hash汇总；不得传凭据、原私人archive和敏感本机路径。没有实际响应写NOT_OBSERVED。
**Codex必须把本任务逐成员脱敏后的`evidence_sanitized.zip`连同`result.md`、`manifest.json`，自动上传至GitHub仓库的`REVIEW_BRANCH/TEMP_PATH`指定的独立Review分支临时目录，仅三文件白名单。** 新candidate唯一parent=`543146f61e9bcf345ca1700bdc8149d4bc470ba7`，仅新增`_review_tmp/ch5/temp-v010-github-exact-object-transport-recovery-20261021/result.md`、`_review_tmp/ch5/temp-v010-github-exact-object-transport-recovery-20261021/manifest.json`、`_review_tmp/ch5/temp-v010-github-exact-object-transport-recovery-20261021/evidence_sanitized.zip`。普通非强制、精确Git Data API；已有同名ref或路径不符合预期则STOP。真实远端commit/tree/sole parent、三件Git Blob、原字节SHA256、ZIP逐成员CRC/长度/SHA256与隐私必须回读，单报本地路径不算交付。Connector无法交付时记录真实终态/本地原始首错，不准造候选PASS。Owner人工搬运不是默认流程。
两旧PENDING review分支 `review/ch5-temp-price-ledger-precondition-20261021` SHA `4e05976bbc8068b971ba5915133e9a6c3b73193d` 与 `review/ch5-http-object-evidence-20261020` SHA `1579e7f1d7a1975c322dd6ae9af1776e88e83e7c` 均只读保留，不能修改/删。Astra独立取得ZIP原字节、终审归档远端回读后才能non-force精确删除本轮三件；PENDING保持；无候选清理N/A。

## 6. 资源、禁止和最终JSON
本轮wall≤3600秒（验证600、受界工程与观察1440、交付1380、封存预留180）；Python starts≤8、direct≤32、E1≤1批、Git源请求≤9、解码≤45000B、新scratch非Git证据≤8MiB、Git对象storage≤256MiB，公开发布成功次数≤1、Git Data API写调用≤8。不得继承任何旧任务预算。严格遵守任务JSON更多限制。
科学HA/HJB/KFE/GE/IRF、正式runner/GE、TEMP A0-A3均调用0；**Windows A重跑0**；生产driver/旧journal/派生patch修改部署0、来源P2-P5扫描0、旧review清理0。生产supervisor/reader/GLOBAL_STOP继续UNVERIFIED，`model_activation=False`、`REAL_GE=False`、`Results=FALSE`、`V011=NOT_STARTED`、`FULL_RUNNER_IO_CLOSURE=BLOCKED`。
Codex最终给run_id、actual_terminal、逐请求响应类型/字节/错误与provider状态、各对象身份复算、A未运行/HA调用0、保护根前后状态及不可观测OS descendants UNKNOWN、资源分类与首错、交付与Astra原字节验收未完成的界限；最终原始JSON Base64+真实长度及SHA256经支持渠道输出，明确控制器退出后完成事件。预定`WAIT_ASTRA_EXACT_OBJECT_CONNECTOR_REVIEW`只是计划停点，不替代实际终态。到此停，不自动续P2-P5或发布下一任务。
