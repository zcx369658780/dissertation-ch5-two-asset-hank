# CH5 — 现有发布器精确 HTTP 回读最小修复（2026-10-20）
TASK_ID=CH5_PUBLISHER_PRECISE_HTTP_READBACK_FIX_20261020
REVISION=ISSUED_20261020_R1
SCOPE=BOUNDED_EXISTING_PUBLISHER_HTTP_READBACK_FIX_AND_OWN_DELIVERY

## 权威与既往任务关闭
Owner已在2026-10-20明确要求下达下一任务。本次是新任务、新预算，不续跑任何CLOSED任务。
之前的CH5_REVIEW_WORKFLOW_ONE_TIME_DOC_SYNC_20261019：Codex报告本地9/9同步（4更新5新增）、AGENTS导航修改、保护身份不变；真实GitHub push断开，远端查询404。Owner随后明确接受本地完成，并豁免此文档同步的GitHub补交。它不是完整远端交付PASS，也不需重启/重推，不要再显示Project Sources待上传（Owner已确认上传；非独立文件哈希验证）。
原发布器任务CH5_PUBLISHER_DIAGNOSTICS_AND_DELIVERY_REPAIR_20261019终审CHANGES_REQUIRED_REMOTE_READBACK_IMPLEMENTATION，候选42ac4f1c76ece94e5ada633f66daa7efddc1512d已历史归档、其review三文件已清理。原12组PASS为历史测试记录，未全量独立审核旧158成员ZIP。不得重开原预算。
源裁决：docs/CH5_PUBLISHER_DIAGNOSTICS_REMOTE_READBACK_REVIEW_20261019.md。最新流程：docs/CH5_ASTRA_WORKFLOW_CURRENT.md、docs/CH5_MANDATORY_REVIEW_DELIVERY_AND_CLEANUP_20261019.md。当前入口仅docs/DOC_INDEX_CURRENT.md。正式冻结合同以本任务参数及ISSUE_MANIFEST为准。

## 目标：只修一个子系统
最小修复已存在的src/ch5_evidence_publisher.py中GitHub REST远端readback及_http响应留存：
A. 移除通过仓库根/git/trees/{sha}?recursive=1为三文件回读定位的路径；按固定commit逐层非递归tree/固定子目录精确定位。固定候选唯一parent和commit/tree；限定三条白名单、检查目录额外文件、路径类型/名称碰撞、Git tree truncated及缺失情形。对于三文件实际获取原始字节，用成熟标准库验证Git对象身份/内容长度/sha256（和manifest一致），ZIP逐成员的CRC、解压后长度、SHA256、路径与清单一致性。已完整校验的相同commit/path/blob原件只取一次、缓存复用；任何部分响应不可标完整。严禁根recursive=1，无需仓库全量tree。
B. _http增加请求操作阶段、规范化相对path（不含token/认证）、响应状态、Content-Length声明/实际计数、已接收长度、有界原始partial bytes私有留存，明确INCOMPLETE/UNKNOWN。http.client.IncompleteRead及连接中断时保留首错，公开报告只含安全阶段、字节计数、脱敏错误；不将secret-like内容写公开包。真实HTTP异常原理不得猜测为已定位网络根因。
C. 补充小型确定性合成测试：深度固定非递归tree正常路径、三文件+多余文件拒绝、tree truncated、IncompleteRead有部分body、ref不存在/冲突、文件字节或清单hash错误、完整字节缓存命中、不可盲目重复push；复用成熟hashlib/zipfile/json/base64及已有安全装配。至少7个独立可定位断言簇，记录首错与E1修复。
D. 对原publisher其它日志、fake-bare、安全门、公开脱敏、流程入口保持原行为；仅在接口受影响时做最少兼容修改。运行新针对性测试和一次更新后fake-bare精确三文件往返/白名单删除，不重跑旧12组全历史、不跑分类器/adapter/HA/真实模型。不得开发全新发布器、通用命令执行器或新认证渠道。

## 源文件和强制停机
输入仅为TASK_PARAMETERS锁定的上轮本地既有publisher源码、tests、helper、lock四个准确路径和此前终审两份正文；旧本地目录READ_ONLY，禁止递归扫描、复制整个目录、读取raw_private/旧ZIP/其它历史私有证据。
对已获独立审阅的源码与测试分别先计算字节SHA256，与参数中受界身份一致才能复制进独占新scratch。不存在/哈希不一致时STOP=SOURCE_MISMATCH，不擅自从158成员ZIP恢复。lock用于理解约束，不隐式覆盖本任务新发布配置。
BOOTSTRAP0有限根及父链、reparse/link、旧代码树/index真实定位与元数据哈希；BOOTSTRAP1确认new_scratch原不存在后独占创建，BOOTSTRAP2初始化本任务日志。源根和正式工作树只读，任何保护重定向/权限拒绝立即停止相应动作。不得读取或修改SSH Key、系统代理、安全设置、Git全局配置及无关进程；只能对自己启动的子进程进行有界结束/回收。OS内核无法观察则记UNKNOWN，不能推断0。
严格区分ENGINEERING、DELIVERY预算，不延续旧额度。普通E1语法/fixture/测试不一致在本任务3批内改好，保留首错，修复后只重测受影响接口。E2/E3实际来源失配、隐私暴露、保护路径异常或平台/认证拒绝则STOP且安全封存。

## 交付与验收
必须由Codex自己准备并尝试一次独立安全GitHub交付：review/ch5-publisher-precise-http-fix-20261020，唯一parent固定为参数中的fixed_parent，temp_path固定为_review_tmp/ch5/publisher-precise-http-fix-20261020/。远端只新增result.md、manifest.json、evidence_sanitized.zip三件；普通non-force push，禁止main/治理分支或其它远端写入，不将_scratch写入保护worktree。使用已有SSH/443与正常主机验证；发布后如push不明确，只做精确read-only reconciliation；不盲目重推。授权只允许本次现有交付通道，不允许被拒绝后换账号、换协议绕过。
evidence ZIP必须含最终源码（实际可审）、修改diff、对应测试/fixtures、每簇断言结果、fake-bare三文件字节/清理证明、保护哈希、资源统计、首错与恢复、安全公开HTTP诊断实例，不含凭据/raw_private/本机绝对私有路径。manifest逐成员记录相对路径、bytes、sha256、来源、关键证据；ZIP全成员路径安全、无重复/碰撞/嵌套压缩包/敏感内容，使用标准库完成CRC+SHA。公开前逐项隐私核验，不把hash索引当源码。
真实远端候选若存在，验收按新五步：fixed object→一次字节完整性全查→聚焦实现/接口/异常审阅→PASS|CHANGES_REQUIRED|REVIEW_PENDING_IO→归档回读/精确清理；本次远端三份全部原字节不能取得时不得宣称PASS。Astra终审PASS/CHANGES_REQUIRED后先归档回读，再确认review HEAD，用普通非强制删除三白名单并回读。PENDING保留证据；无候选NOT_APPLICABLE_NO_CANDIDATE。
Codex返回最终原始JSON回执的完整Base64、bytes、SHA256、run_id、候选commit/tree/parent、真实终态、实际阶段、资源统计及独立外部退出事件；不能以controller退出0冒充上传成功。按失败类型标记DELIVERY_BLOCKED/REVIEW_PENDING_IO，未传凭据也不能要求Owner手工搬运为默认。
执行停点：WAIT_ASTRA_PUBLISHER_PRECISE_HTTP_FIX_REVIEW；仅预期值，真实结果以回执为准。

## 科学冻结
SCIENCE=0；MODEL=0；旧491成员ZIP读取=0；91样本分类器=0；adapter=0；旧发布器158成员归档读取=0；HTTP修复以外源码=0；正式模型worktree写入=0；软件安装=0。
正式V010/v0.0.10；HA是MATLAB-faithful黑箱。model_activation=False；REAL_GE=False；Results=FALSE；V011=NOT_STARTED；FULL_RUNNER_IO_CLOSURE=BLOCKED。
