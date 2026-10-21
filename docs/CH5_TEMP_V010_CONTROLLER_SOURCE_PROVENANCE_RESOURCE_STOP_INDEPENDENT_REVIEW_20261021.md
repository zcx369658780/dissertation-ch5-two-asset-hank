# CH5 TEMP V010 真实控制器来源调查资源硬门停止 — GPT/Astra 独立检查

TASK_ID=CH5_TEMP_V010_CONTROLLER_SOURCE_PROVENANCE_LOCATOR_GATE_20261021
RUN_ID=bb28bb74ec6f46c78287d82937eb1209
DATE=2026-10-21
ACTUAL_TERMINAL=STOP_RESOURCE_GITHUB_DIRECTORY_METADATA_LIMIT_EXCEEDED
ACTUAL_PHASE=P4_GITHUB_FIXED_PREFIX_METADATA_HARD_STOP
ASTRA_REVIEW=STOP_CONFIRMED__RESOURCE_HARD_GATE__RESEARCH_INCOMPLETE
TASK_ACCEPTANCE=NOT_PASS__SOURCE_PROVENANCE_UNRESOLVED
REVIEW_CANDIDATE=NONE
CLEANUP=NOT_APPLICABLE_NO_CANDIDATE
SCIENTIFIC_BUDGET=0

## 1. 原始回执与冻结合同
- Owner提供的本轮粘贴文本附件，经Python标准库`base64.b64decode(validate=True)`、`hashlib.sha256`和`json.loads`独立处理；最终JSON 8226字节，SHA256 `57aaf435c73fa59f587d12150f8f013488cea8f68f49a9ec1354f7359fe82322`；TASK_ID/run_id/actual_terminal/actual_phase与Owner文本一致。独立核验为**回执身份**，不等于Astra独立访问Codex Windows私人scratch或GitHub provider出错时的底层响应。
- 远端治理HEAD `77b18b8c4de8bf1fe4c7ddbf19b6d44150ad16bc`，源issue `b2cc3050157283b0b52cff11dc35a73e922f341c`，release `77b18b8c4de8bf1fe4c7ddbf19b6d44150ad16bc`。精确读取冻结`TASK_PARAMETERS.json` Git Blob `dec4b2af86710fb4529f537643d3b70d7ccf7c0b`，`CONTRACT.md` Git Blob `89c953cb0ed4f8e5f82eea0486a1a7b845910bd3`；确证Github单prefix返回条数上限64，允许prefix包含`tasks`。旧14份Git原件验证是Codex自报，本轮独立确认最必要合同/参数。
- GitHub直接查询本轮`review/ch5-temp-controller-source-provenance-gate-20261021` ref返回404，没有可供Astra验收的候选commit/tree/三文件；Codex自报API mutation=0、成功发布=0。故`NOT_APPLICABLE_NO_CANDIDATE`，不是遗忘了清理，不能捏造候选 SHA 或手动创建替代候选。
- 两份已存在的历史待审ref准确未变：`review/ch5-temp-price-ledger-precondition-20261021`→`4e05976bbc8068b971ba5915133e9a6c3b73193d`，`review/ch5-http-object-evidence-20261020`→`1579e7f1d7a1975c322dd6ae9af1776e88e83e7c`。未触碰。

## 2. 冻结资源硬门与合法停止
- Codex回执记录GitHub前缀精确非递归请求五处：`src/ch5_two_asset_hank`返回20项、`src/ch5_two_asset_hank/multi_province`返回20项、`scripts`返回5项、`tools`返回2项，均≤64；`tasks`一次响应**400项**，超每目录64条硬上限，响应内容655695字符。400与原始工具响应身份属于Codex本地保存的私有控制器记录，本轮Astra**没有重新请求超限目录**，所以不写成Astra独立测得400。
- 有限合同仅允许≤64，而本轮选择的目录端点允许返回400。触发后Codex报告即刻停止一切后续候选内容读取/网络调用、未把400截断冒充合规、没有发布或切换方式；**停止动作符合资源安全要求**。但是调用本身没有预先保证接口分页/响应项上限，是后续Planner/执行源头需要消除的前置缺陷；不因此把未完成源调查宣布PASS。
- 该资源超限是`STOP_RESOURCE_...`的终态，不是正常E1；不补发这次旧预算，不建议无批准地重试`tasks`目录或进行 root recursive tree。另行新合同应剔除宽泛`tasks`目录请求，优先精确任务文件/已知子路径、查询前验证可服务端限项；否则STOP，不做响应事后切分伪装合规。

## 3. P2 本地取证不完整
- 本轮只报告三处冻结历史TEMP安全根通过boundary身份；调用`DirEntry.stat().st_ino`与`Path.stat().st_ino`的Windows接口值不一致，首错AssertionError（P2 chunk 1105d1，E1批次1）；受控新scratch对照观察4项`DirEntry` inode=0、`Path` inode非零而size/mtime相等，支持API元数据差异解释，却**不能证明**历史文件字节没改或根因唯一。
- 原本应写的directory_open_count、filename_metadata_count及候选相对路径和比较值，实际`UNKNOWN_NOT_FLUSHED_BEFORE_ASSERTION`。一次候选内容读取尝试的具体身份UNKNOWN、已认证本地候选数0；未重新扫描旧根。这是独立于Github硬门的**证据落盘次序缺陷**，下一次需先记录原始元数据/首错/扫描游标再断言，不以松开身份安全门解决。
- 终态收据也有E1批次2：finalizer引用了错误的scratch相对metadata observation路径，后仅更正新scratch finalizer输入，没有重启旧扫描或网络。原始进程首错stdout/stderr未全量独立留存，不能把未知写0。

## 4. 当前可接受事实与不能接受的结论
- Codex原始回执：认证1,214,713B私人archive原始SHA256 `f3e8984fe4d2ef4be65692c27fa7594d96b870d372a8c45d029899f7891841d8`、278条ZIP目录、四件既定授权小成员合计29752B；这些是Codex本地自报，Astra没有重新读私人1.2MB归档字节。由四件原件构成的两个STOP JSON有元数据证据等级C，但**角色含义尚未解析**。
- 本轮STOP_PRODUCER、STOP_WRITER、STOP_READER、RUN_MAIN_CATCH、BUDGET_ADMISSION_CALLER、SUPERVISOR_DISPATCHER、WORKER_OBSERVER均为`UNKNOWN_NOT_COMPLETED`。A/B来源等级未建立、D有限负结论也未建立、E资源硬停/记录缺口；不能以“没找到”写真实控制器不存在。此前已接受的X2/X3共同协议fixture限域PASS不受本轮停止影响，却不能替代真实生产来源。
- Codex报告旧formal Git locator/index前后长度和SHA不变；私人archive stat未变；旧journal写入0、科学HA/HJB/KFE/GE/IRF/model_runner/driver调用0，kernel descendant UNKNOWN；未对整个formal worktree做内容hash且Astra未在用户Windows重做这些OS核验。
- 资源账：verification Python2/Shell5/Git4/direct11/GET15，provenance Python4/Shell4/direct8/E1批次2，delivery所有写0；总direct19、GET20，墙钟445.263秒。不存在成功发布或远端待删除证据。

## 5. 复工建议（不是授权）
仅Owner后续独立同意时，另签一次**两处定向修正的来源溯源续单**：首先在源查询前使用确切子路径/服务端限制而非宽泛tasks枚举，确保最大响应≤64；其次修复Windows文件身份采集，先持久化每一步原始比较值和游标、再判定，不松开保护门。旧私人archive的已接受身份可按固定SHA复用历史接受结论，但本轮执行中未完成的P2/P4来源结果不得伪造重用。直到获得真实supervisor/reader执行源与调用证明，生产global STOP、真实run接线、HA科学启动均冻结。

artifact_integrity=FINAL_RECEIPT_RAW_BYTES_INDEPENDENT_PASS__PRIVATE_SOURCE_REPORTED_ONLY
source_investigation=INCOMPLETE
resource_gate=STOP_ACCEPTED__CALL_RESPONSE_EXCEEDED_DECLARED_CAP
delivery=NOT_STARTED__NO_GITHUB_CANDIDATE
privacy=NOT_PUBLIC_PACKAGE__PRIVATE_RAW_OUT_OF_SCOPE
cleanup=NOT_APPLICABLE_NO_CANDIDATE
NOT_COMPLETED=P2_COVERAGE;P3_CONTROLLER_CANDIDATES;P4_TASKS_PREFIX;P5_ROLES_GRAPH;PUBLISH_3_FILES;ASTRA_ZIP_REVIEW
model_activation=False
REAL_GE=False
Results=FALSE
V011=NOT_STARTED
FULL_RUNNER_IO_CLOSURE=BLOCKED
