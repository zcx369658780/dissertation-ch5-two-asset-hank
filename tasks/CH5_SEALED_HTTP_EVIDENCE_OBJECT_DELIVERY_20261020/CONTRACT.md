# CH5 · 既有HTTP修复封存证据的轻量Git对象交付
TASK_ID=CH5_SEALED_HTTP_EVIDENCE_OBJECT_DELIVERY_20261020
REVISION=ISSUED_20261020_R1
SCOPE=SEALED_EVIDENCE_REVALIDATION_AND_BOUNDED_DELIVERY
OWNER_AUTHORITY=2026-10-20明确批准精确Git对象API及适度放宽本地存储空间；没有授权新工程源码/科学任务

## A. 固定状态与职责
先读取治理分支真实live ref，并在同一live commit核CURRENT.md、TASK_CURRENT.md与规范索引docs/DOC_INDEX_CURRENT.md，再从发行commit读取ISSUE_MANIFEST及指定issue_commit冻结合同、参数。治理提交不要求恒等于固定review parent。此任务是新的受界预算，不延续此前CLOSED的预算。
上一run=c333014661d24524b2f75cb87caf65ae，终态DELIVERY_BLOCKED_RESOURCE_STORAGE_LIMIT。Astra先前已核验9604字节原JSON回执及其中的三源声明，尚未独立获得源ZIP和HTTP源码；上一Git存储500084907 bytes超过旧268435456 bytes。精确ref、候选commit GET在上轮回读时404，不自动证明永远不存在，也不允许重推旧候选。见docs/CH5_SEALED_SOURCE_IDENTITY_RESOURCE_LIMIT_REVIEW_20261020.md。
正式V010、V011 NOT_STARTED，HA黑箱，Results FALSE，科学预算0。

## B. 封存字节与安全门
仅对参数明确的前一run新scratch根下package、sanitized、根三个有限候选相对目录逐一stat以下精确三文件：result.md、manifest.json、evidence_sanitized.zip。选择唯一、非链接、常规文件；多份不同/相同候选都必须先澄清身份而非任意挑选。不得递归扫描旧目录、全仓库或过去的私有日志。
从前轮用户所给9604字节Base64回执实际解码已取得三个合法64位SHA及长度，冻结在TASK_PARAMETERS作为**Codex报告的待核身份**，而非Astra已独立验收的原件。实际读取本地三源原字节后，用标准库hashlib/zipfile/json一次复算比对：长度、SHA256、ZIP所有14成员CRC/解压长度/成员SHA256、清单映射、唯一安全路径、大小写碰撞、symlink/嵌套压缩、bomb限制。任何SHA不符、路径歧义、原件丢失或成员违规即STOP；不猜补哈希、不改原ZIP。
对全部准备公开的源result、源manifest、ZIP逐成员以及本轮派生物做隐私检测，合成字面转义与真实UNC/Windows路径分开，真实敏感原件私有封存；如缺失人工可靠判断则STOP_PRIVACY_PENDING。不得把未经核验的历史“16项PASS”代替本轮隐私结论。
完成后在唯一新scratch生成新result.md、manifest.json交付封套（说明本轮操作、实际检查、首错、风险、资源与未完成），并且在新manifest只于隐私门通过后嵌入前一run result/manifest原字节的Base64供Astra独立复算。evidence_sanitized.zip从本轮验证的封存源逐字节拷贝，hash必须与参数一致。新manifest不得将自身哈希写为自引用；新最终回执记录三个最终输出文件的原字节长度和SHA256。最终ZIP内源码仅作为历史证据，不执行。

## C. 原子发布策略（先选方法，后变更）
优先**现有已授权的GitHub Git Data API**。在不查看凭据、不修改认证配置、不发送探测性写入的前提下，检查是否确有支持该repo的已授权WRITE工具及所需create blob/tree/commit/ref动作。若能力可用，选API_ONLY；没有能力但不是HTTP/policy拒绝时，可在无任何API写入或拒绝的情况下选择参数明列的SSH_GIT_ONLY。选择与证据必须在首次网络写入前记录。
Git对象API限定允许动作：读取目标ref和固定parent commit/tree；三原字节经必要Base64建立三个Blob；用固定parent的树为base创建仅三条新增temp白名单路径的tree；commit sole parent为固定parent；原子创建**新的**准确review ref。检查预先精确ref不存在（404正常）；存在无关ref、权限拒绝、rate limit 403/429、auth 401、受限端点缺失或平台策略拒绝就停止，不借切换方法绕过拒绝。禁止PATCH现有ref/force更新、修改治理/main及无关ref。不得用响应中的URL/blob号代替远端原字节审验。
若在第一次网络变更前已确认Git Data API写能力缺失且非拒绝，才选择预先批准的SSH_GIT_ONLY：既有SSH到ssh.github.com:443正常host verification，仅必要固定parent对象限域fetch到**新scratch**独占bare，绝不整仓库clone、不继承旧bare缓存、不读SSH密钥、不改全局Git配置。新Git存储预算2147483648 bytes（2GiB）；过1610612736 bytes记录预警并评估退出。预算虽已放宽仍是硬上限，必要时在安全边界内停止，不消耗旧额度。资源数详参数，OS内核/隐式子进程无法独立观测记UNKNOWN。
两方法均只能对参数中的固定review ref新增一次三文件候选、唯一parent；正常non-force创建，push/创建结果有歧义只能读回精确对象，不重推、不改渠道或身份。任何拒绝不改认证/账号/代理方式绕过。

## D. 回读、审核、清理与回执
交付须使Astra能通过精确commit及三个路径获取**完整原字节**，一次使用标准库批量复算全部ZIP成员以及新manifest封装的旧result/manifest原字节，核真实接口/关键代码变化和隐私。读不到原字节时REVIEW_PENDING_IO，不以Blob ID或Git commit号强行PASS；本次Codex独立自检不是Astra审查。
Astra终审PASS或CHANGES_REQUIRED后先永久归档/远端回读，再核精确review HEAD并用普通non-force删除三件temp白名单及回读。PENDING不删，无候选N/A。Codex不可自行清理；不得删除/修改已封存旧scratch及正式worktree。
BOOTSTRAP0/1/2只涉及可信父链有限元数据、独占创建全新scratch，正式Git locator/index仅读参数列明命令及哈希前后，保护根其它内容不读取。原始错误证据在新scratch私有保留，公开载荷逐项脱敏；禁止第三方软件安装/修改HTTP源码、重跑10测试/fake bare/旧491/158 ZIP/分类器/adapter/HA/GE/IRF/TEMP。
终态回执（包括实际run_id、source hashes、ZIP全成员、方法能力与选择、候选ref/sha/tree/parent、完整字节readback、保护资源实际测量、first errors、UNKNOWN与not_completed）须输出原始JSON完整Base64、bytes/SHA256，以及分开的外部控制器完成事件。预定停点WAIT_ASTRA_HTTP_OBJECT_DELIVERY_REVIEW，不代表完成。旧任务与预算绝不自动续跑。
