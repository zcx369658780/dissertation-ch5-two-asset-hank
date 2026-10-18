# CH5 Owner 2026-10-18：GitHub远端临时审阅扩展为 MD + ZIP（长期默认）

**Authority：Owner 2026-10-18明确要求“类似的报告和zip文档也可以上传github临时目录（验收后清理）”。**
**状态：OWNER_APPROVED_PROSPECTIVE_DELIVERY_PROTOCOL；**优先于2026-10-16旧[脱敏临时交换协议](CH5_TEMP_SANITIZED_REVIEW_EXCHANGE_20261016.md)中“只允许MD/JSON或第三份静态文本、ZIP不许发布”的旧文件类型限制。**未改变**Owner已有GitHub SSH Key-over-443、仅remote临时目录、先验收归档再清理、Git历史留存、原项目工作树保护及真实科研数据防误公开等硬边界。V1.3普通工程自主修复与E2/E3停止门不变。

## 1. 新默认交付格式与前置冻结

从此以后**新签发**的需Astra外部独立审阅的长任务，默认允许在**唯一独立remote review分支**上的白名单`_review_tmp/ch5/<task-id>/`发布：

1. `result.md`：脱敏的集中结果/错误/资源摘要，UTF-8 LF（默认≤128KiB）。
2. `manifest.json`：候选固定commit+tree、任务Blob、run_id、文件条目SHA256/长度、原件与派生件的证据身份、累计资源、保留UNKNOWN（默认≤256KiB）。
3. `evidence_sanitized.zip`：**可选、真实需原证验收时优先**的已脱敏ZIP证据包。默认压缩体积≤32MiB（33,554,432B）、解压总长度≤256MiB、成员≤3,000；大于限制需下一新任务事前单独明确批准，不能自动压缩拆包绕开。

**不是每张任务都必须有ZIP**；已有的本地私有RAW ZIP不得擅自假称sanitized或因此在结果中被丢弃。上述名字、size均是未来默认值，不追溯授权已经STOP/LOCAL_ONLY的任务重新fetch、推送或科学求解。当次严格冻结任务如果禁止public ZIP或把上传次数设0，仍执行更严格合同；若要启用ZIP，任务发行前必须固定**精确review ref、固定父commit、唯一remote路径、白名单文件和大小、一次ordinary nonforce publish及网络/清理预算**。不能凭本协议自创推送次数。

## 2. ZIP内部核验和脱敏（上传前完成）

上传者必须**审查ZIP每一个成员及所有内嵌压缩包**，不可以只查外层ZIP文件名、外层SHA或扫描提取后少数文本。覆盖：
- 真实Windows用户目录/绝对路径与用户名、私有邮箱、IP/内网拓扑、完整命令argv/env、token/API key、PAT、SSH私钥/known_hosts/agent/credentials、Git内部元数据、个人健康/身份信息及受保护真实微观/省级数据，均不发布。即使Owner认为项目无科研秘密，GitHub仍不该成为无需同意的主机信息或凭据永久公开渠道。
- 禁止未经明确白名单的`.git/`、执行文件、二进制动态库、pickle、凭据、完整原始环境dump及不可扫描的不明格式。必要的**匿名synthetic float64数组、CSV/JSON/MD、图形、由任务明确列名的静态源码片段**可归档，但不得在审阅时执行ZIP内任何代码。
- 严格查解压路径：无绝对路径、`..`、drive/UNC/ADS、符号链接、重复case-insensitive路径、ZIP bomb或巨额压缩比；若ZIP内还有ZIP/7z/tar等，须在限定深度/体积/数量下递归扫描，**不可解析则禁止远端发布并保留LOCAL_ONLY**。
- ZIP为DERIVATIVE时保留真实本机RAW原件及其SHA256、长度、原run_id；`manifest.json`必须**分别**列RAW私人证据和SANITIZED派生证据的哈希/来源、修改规则与成员列表，不得用脱敏后哈希冒充原件SHA。可从平铺的新scratch构建审阅ZIP，**仍绝对不得在本地项目树/index创建 `_review_tmp` 目录**。
- 检查失败直接使用PRIVATE_LOCAL_ONLY + Owner在当前ChatGPT会话上传RAW原件作为补充；绝不因为“GitHub验收后会删除”跳过脱敏。尤其不要未经处理推送含历史私有nested ZIP的完整科研运行证据。

## 3. Codex发布与Astra验收／清理顺序

1. Codex仅用已有SSH Key及`ssh.github.com:443`；在原科研/模型/治理工作树之外，创建全新非共享的**bare Git对象库**，只在**remote Git候选tree**构造白名单`_review_tmp`路径，不checkout、不在原index add、不引入PAT或修改global/system配置。指定父commit的全部必要对象必须齐全；禁止浅partial promisor造成提交不完整。最多当次冻结授权的**一次**非强制push；失败STOP封存，Owner手工私下交付是fallback而非额外Git重试授权。
2. Astra从**精确remote ref/commit/blob**下载/核查MD、manifest、ZIP原字节；ZIP二进制Blob必须真实下载并独立SHA256+长度和逐件manifest复核。若连接器不能读取binary ZIP原字节，不能宣称GitHub ZIP审查通过；改由Owner私下上传RAW或其他可读传输渠道，`BINARY_UNVERIFIED`保留。二进制下载不是GitBlob SHA1的口头回执。
3. **先**把永久验收报告、来源哈希、阶段PASS/FAIL/UNKNOWN及最新许可状态写回独立治理branch并完成远端 readback；**后**只在此次remote review分支发**普通非强制清理Commit**，删白名单`result.md`、`manifest.json`、`evidence_sanitized.zip`，验证当前tree已不存在（不要从历史commit抹除），记录清理commit SHA与状态。必要时先核原review唯一parent、候选差异只有白名单、review HEAD未变化；失败记`TEMP_CLEANUP_PENDING`，不强推、不扩删除范围。
4. **Git删文件不删历史**：旧Git commit、对象以及GitHub缓存仍可能检索到原字节。因此不能在ZIP里留下真实机密、敏感元数据或路径，不能把临时GitHub仓库当作本地RAW科研存档的替代品；原RAW和中断/失败记录继续保存在Owner原本允许的本地两盘/证据体系中，保留证据级别。

## 4. 适用范围与交接

本文件为**长期新工作流默认**。每张新任务用`DELIVERY=GITHUB_TEMP_REVIEW_MD_ZIP_FIRST`、`TEMP_FILES=result.md,manifest.json[,evidence_sanitized.zip]`、`VALIDATE_ALL_ZIP_MEMBERS_AND_NESTED_ARCHIVES`、`AFTER_REVIEW=PERMANENT_ARCHIVE_REMOTE_READBACK_THEN_WHITELIST_TEMP_CLEANUP`四项表示；精确ref/parent/budget在发行时锁定。

本2026-10-18新增规则**不**修改以前冻结的V010/临时实验科研预算、数学合同、Results，不批准真实C8/31省新求解，不复活已STOP的发布次数。当前TEMP 100轮私人ZIP 6,352,227B、嵌套较早RAW ZIP及Windows绝对路径，不经完整脱敏不得原样远端提交，已由Owner本次私人上传供独立审议。此例说明ZIP传输许可≠原RAW无条件公开许可。
