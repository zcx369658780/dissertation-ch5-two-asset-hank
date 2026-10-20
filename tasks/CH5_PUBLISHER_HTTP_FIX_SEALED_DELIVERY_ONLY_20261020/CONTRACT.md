# CH5 封存 HTTP 修复成果一次性交付任务

TASK_ID=CH5_PUBLISHER_HTTP_FIX_SEALED_DELIVERY_ONLY_20261020
REVISION=ISSUED_20261020_R1
SCOPE=SEALED_LOCAL_ARTIFACT_VERIFY_AND_OWN_GITHUB_DELIVERY_ONLY
OWNER_AUTHORIZATION=2026-10-20 Owner明确同意新的DELIVERY_ONLY任务
STATE=ISSUED_NOT_STARTED

## 1. 来源、历史与权威
Owner最终科学决策；GPT独立Reviewer/Orchestrator；Codex执行冻结任务。本任务不复活任何已经消耗完毕的旧任务预算。正式执行授权仅以本任务发行后的同一live治理快照CURRENT/TASK_CURRENT为准。固定任务签发/发行身份见ISSUE_MANIFEST；不要要求live HEAD永久等于固定issue或父提交。
前任务CH5_PUBLISHER_PRECISE_HTTP_READBACK_FIX_20261020，run_id=b6a028b65b98471d9480517ab18be22b，Codex报告4/4冻结源正确、精确HTTP回读及中断诊断已完成、新10/10有限合成测试通过、fresh fake-bare通过、14成员安全ZIP已封存；实际终态DELIVERY_BLOCKED_HTTP_403_RATE_LIMIT。GitHub 403发生于首个ref读：返回278字节错误体后停止，SSH/fetch/push=0，candidate未建。Astra上轮由于没有远端三文件原字节，仅REVIEW_PENDING_IO，**不是实现PASS**。Owner现在授权对封存成果进行一次新交付。本任务并非追认上一轮成功。
项目Sources已由Owner确认上传；此前DOC_ONLY本地同步已由Owner接受并免GitHub补交；均不作为本任务待办。现行五步验收及强制交付/清理规则继续适用。

## 2. 唯一交付对象与不可变来源
本任务只可读取TASK_PARAMETERS指定旧scratch中的**三份精确安全成品**：result.md、manifest.json、evidence_sanitized.zip；不递归遍历旧scratch，不读取raw_private、源文件、旧失败目录、旧491/158成员ZIP、Git密钥或旧文档镜像内容。旧scratch只读。
由于封存文件的确切package位置未由Astra实测，参数列出有限的候选相对位置。对每一个名字只stat这些候选路径，选择唯一长度/SHA256完全符合上轮封存回执所声明值的文件；若缺失、重复匹配或身份不符，STOP SOURCE_ARTIFACT_MISSING_OR_MISMATCH，不猜路径、不搜索全目录、不重新打包旧材料。
三份先以Python标准库完整验证字节长度和hashlib.sha256；原manifest须能解析、安全约束合理，核对ZIP的每一个成员名称、size、CRC、SHA256及清单、同名/大小写碰撞、解压限额、符号链接/嵌套压缩及隐私安全边界。不能以旧自检报告代替本次逐成员校验。封存的原ZIP全部字节不许修改、重新压缩或生成替代工程证据；无法核验则停止而不是修源码。
本次只允许在新scratch中生成小型new result.md和manifest.json两份**交付封套元数据**，明确标注来源为前一run的未获Astra审阅成果及10/10仅为Codex历史报告。new manifest需携带14成员的本轮实际机器核验结果、原包sha和来源、约定的三件新交付清单；不得自引用其最终哈希。直接复用经校验未变的evidence_sanitized.zip作为第三件；不得往ZIP加入额外字节。原始source result/manifest身份在新的封套元数据中记录，历史回执不追改。

## 3. 保护与执行
新scratch的创建及任何写入前做BOOTSTRAP 0/1/2：可信父链、无junction/symlink/reparse重定向、原路径和新scratch无重叠、确认scratch原不存在，独占创建；正式worktree只做参数允许的Git locator/index元数据读取及hash前后对照。旧scratch与本项目其他保护根不修改、不清理、不递归检索；不能访问现有private log内容。所有临时文件、Git bare store、包装元数据均位于新scratch。公开包逐项隐私检查，不因为“先前14成员PASS”跳过；公开材料不得泄露绝对私有路径、密钥、token或私有响应。
SCIENCE/ENGINEERING_CODE/TEST_REPLAY预算全为0；不修改任何Python实现、不修bug、不重跑旧10组、新fake-bare、旧12组、分类器、adapter、HA、TEMP、GE、IRF或模型；不安装包，不调整网络代理、git global config、SSH host checking或凭据。只有标准库Hash/ZIP验证和正常Git/SSH交付允许。
预算严格以TASK_PARAMETERS为准，普通封套格式错误可在新DELIVERY E1额度内有界修复并记录首错。来源失配、内容不安全、平台拒绝、实际保护路径冲突、资源失控为硬STOP，不能换账户/协议/授权通道绕过。

## 4. HTTP 预检与仅一次可授权远端尝试
先在允许的现有GitHub HTTP读取通道对**本任务review ref**做一次精确只读preflight（不存在返回404是预期，不代表失败）。若仍为HTTP 403 RATE_LIMIT，必须私有留存有界完整/部分响应并报告DELIVERY_BLOCKED_HTTP_403_RATE_LIMIT，**不再发起SSH、fetch、push**，不重试，避免无谓消耗限流配额。
若GET成功并确定新ref不存在，才使用既有标准SSH key到ssh.github.com:443（正常主机验证）；必要固定parent仅获取对应必要Git对象，不clone整仓库，不修改正式worktree/index。先在本地新bare组装严格固定parent + 仅三条新temp文件的唯一候选tree/commit，核对候选与fixed parent、白名单和原字节身份。普通non-force仅一次push至新review branch；不force，不写main/治理ref、不使用新账户或认证方式。
若HTTP返回429或其它rate-limit/policy denial一样STOP。ref已存在且对象与预期无关则STOP REF_CONFLICT，不覆盖；如果前检查分支恰为本任务**同一不可变候选**，可只读核验，不重复push。push返回含糊失败必须有界只读核对同一ref、候选commit/目录/三原件，禁止盲推。没有实际远端候选就报告NOT_APPLICABLE_NO_CANDIDATE，别改称“清理成功”。
远端实际读回要校验三个原字节长度/sha、ZIP每成员CRC/sha、安全清单、唯一parent、仅三白名单新增路径，不调用root recursive=1。成功下载已验证字节不重复获取。
全程不能把GitHub HTTP连接器当前可用当作Codex本地免限流证明，也不能把403归罪于实现。任何取证工具本身失败记录REVIEW_TOOL_ERROR或IO阻塞，不作为候选缺陷。

## 5. 分层验收与最终交付
Codex必须输出实际结果、新run_id、新candidate/tree/sole parent（未创建就UNKNOWN_NOT_CREATED）、新result/manifest/ZIP字节身份、14/14成员批量核验、隐私、受保护源与index前后哈希、GET/SSH/fetch/push的真实计数、首错和已知问题，且返回自己的最终JSON回执完整Base64、字节长度、SHA256、独立控制器退出事件。生产外部退出0仅代表封存完成，不等于publish成功。
Astra收到远端候选后单独按五步验收：对象固定→全部必要字节/ZIP成员机器完整性核验→针对HTTP源码与测试证据独立语义审阅/隐私审阅→PASS|CHANGES_REQUIRED|REVIEW_PENDING_IO→PASS/CHANGES_REQUIRED永久归档回读后**精确非强制清理**新review分支三件，PENDING保留。当前仅新任务受理，不能提前claim工程PASS。
预计停点WAIT_ASTRA_SEALED_HTTP_FIX_DELIVERY_REVIEW。真实终态仍以回执为准。

## 6. 科学状态
V010/v0.0.10；V011=NOT_STARTED；model_activation=False；REAL_GE=False；Results=FALSE；FULL_RUNNER_IO_CLOSURE=BLOCKED。SCIENCE_BUDGET=0。
