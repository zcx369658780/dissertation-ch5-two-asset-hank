# CH5 自动GitHub MD＋二进制ZIP交付实测审议：文件真实上传，资源超限FAIL_CLOSED

**2026-10-18／验收边界：`DELIVERY_ARTIFACTS_REMOTE_BYTE_IDENTITY_ACCEPTED__ENGINEERING_FAIL_CLOSED_RESOURCE_EXCEPTION`。**
**绝不以三文件远端上传成功宣称整张工程任务PASS，也不恢复任何已STOP科学调用。**

## 1. 唯一受界交付与真实Git身份

- 已冻结纯证据交付任务：`CH5_GITHUB_ZIP_PUBLISHER_REPAIR_DELIVERY_RECOVERY_20261018`；发行Commit `2d9a3a5a3100fa82f24f125ce3264bb68c01c333`、任务Blob `c0f020b6b11a6289d65aa0cbde734d415633037c`。原TEMP价格桥科学试验早已E2共享ledger STOP，A1/A2/A3完成0/2/2轮、HA12（9完整、1失败、2中断），不能得出经济因子比较结果。
- Astra通过已连接GitHub读取远端review分支 `review/ch5-temp-pricebridge-factorial100-deliveryrecovery-20261018`，实际HEAD `7623a4eb4680f0b4039f03dd245307ec791cea15`、Tree `1f63524a65701a8f37d05b9766f849ce243e5dd5`，**唯一父提交精确为上方交付任务发行Commit**；以该父作比较 `ahead=1 / behind=0`，**仅新增3条远端白名单路径**。无额外源/模型/治理树变更：
  - `_review_tmp/ch5/temp-v010-pricebridge-2x2-100-delivery-20261018/result.md`：Git Blob `ef6b53af5527f6ca47dc06119c6103788a7df8af`；UTF-8原字节4542B，独立SHA256 `70b047d4fd3c14182bfe00ea183c55f1917343cc777562108345c470e387500b`。
  - 同目录 `manifest.json`：Git Blob `689be23b05a000bbaacd7c7e462efc977e73e3e6`；13864B，SHA256 `24a193f6557fe2ec7ff12872d5097274e6ef0e609d47e5b3b3d05ed38aec0e9b`。
  - 同目录 `evidence_sanitized.zip`：Git Blob `ea59ed80e78e7ca8b5642dfa35af326a7f40bd50`；196296B；**Astra从GitHub本身取base64字节并自主SHA256复算** `9f3f2cda8360577de83bfe02d01b6f57814bee4e03b1c883f3a6a79698dc08e2`，与Owner先前实际上传私人ZIP中该成员的SHA256与独立Git blob身份完全一致。ZIP中央目录共29项；对私人包中同一原字节的ZIP运行完整CRC PASS，内部其余28项与签发前manifest的SHA256及长度28/28相符，另1项是防自引用的包内manifest。
- GitHub远端发布路径**实际上存在且内容正确，不需要Codex再fetch/push/重复上传**。虽然本机`container.download`在DNS层失败，本审计通过GitHub connector读取完整base64原字节并在独立V8代码中计算了远端ZIP SHA256；故二进制审阅不是只靠文件名或GitHub URL猜测。
- 原封脱敏`manifest.json`内的`reviewRef`和`parentCommit`仍为**旧价格桥科学任务**的生成时描述（`review/ch5-temp-pricebridge-factorial100-20261018`、`2c855f616efbca05c29d4069a44e3c6651070b44`）；这不是本次补交review实际Git身份。后者必须以上方已直接回读的远端 ref/HEAD/唯一parent为准。为保持脱敏原字节身份，不静默重写旧manifest，也不宣称其发布元数据已更新。

## 2. 工程资源异常：有限接受，绝不假PASS

- Codex自报纯交付任务存在漏计Git内部子进程，实际**至少26/24次子进程启动**，已执行STOP，分类 `FAIL_CLOSED_RESOURCE_EXCEPTION`。这属于明确超过冻结工程调用次数；并不能通过文件上传成功或远端Blob匹配豁免。**本次未收到用户Windows上`DELIVERY_RECEIPT_WITH_RESOURCE_EXCEPTION.json`的原字节**，故26/24以上仅标`CODEX_REPORTED_RESOURCE_EXCEPTION__UNINDEPENDENTLY_ENUMERATED`，不宣称Astra完成主机进程清单复算。
- Codex称交付期间科学调用0，且旧模型/私人RAW未变；这些由远端模型差异不存在和其报告支持，但Windows实际工作站的负操作事实仍是`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，不可提升为native sandbox或source overwrite的独立OS认证。
- 窄的**交付文件字节身份PASS**与完整任务的**工程资源FAIL_CLOSED**必须分别登记：`TRANSPORT_CONTENT_VERIFIED=TRUE`；`ENGINEERING_TASK_ACCEPTED=FALSE`；`RESOURCE_LIMIT=24`，`REPORTED_AT_LEAST=26`，未用额度永久关闭。不要求Codex再运行发布器来“补PASS”。

## 3. 工作流结论与科学状态

- 证明Codex已经有能力自动把**脱敏MD＋manifest＋ZIP三文件**发布到远端GitHub临时审阅目录，并有可独立读取的二进制原字节。这满足Owner最关心的**不需每轮人工上传ZIP**的交付可用性目标；不能将一次超预算工程运行称为全流程可靠性验收通过。
- 未来新交付任务，应在冻结前明确“子进程”的统一语义：外层PowerShell/Python启动、每个`git`命令及其实际派生进程都必须有**全局持久计数**，预留发布验证与安全清理额度，并在启用实际远程传输前完成no-network fake-bare/ZIP preflight。不能靠日终追补未计内部`git`，更不能为试验PASS扩大既有资源上限。
- 原TEMP2×2 E2共享账本故障与不完整科学结果不受此二进制传输影响；正式`V010 ACTIVE_TASK=NONE`、`Results FALSE`、`V011 NOT_STARTED`、历史HA黑箱/旧预算与保护资产均不改。本轮不签任何新科学/工程执行任务。
- 此主审与治理STOP状态**先行永久发布并远端回读**，之后仅对上述`review`分支当前Tree的3条白名单执行普通非强制清理Commit，清理结果独立记入后续cleanup receipt。Git commit历史保留，不能声称文件被永久抹去。
