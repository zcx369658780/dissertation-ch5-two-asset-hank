# CH5 V1.9 分类器：既有完整证据自动 GitHub 补交

TASK_ID=CH5_CLASSIFIER_V19_EXISTING_EVIDENCE_GITHUB_DELIVERY_20261019
SCOPE=DELIVERY_ONLY / NO_CLASSIFIER_EXECUTION / NO_TEST_RERUN / NO_OLD_ARCHIVE / ZERO_SCIENCE
STATUS_AT_ISSUE=ISSUED_NOT_STARTED
日期：2026-10-19。Owner已在四份附件有限验收后明确授权继续补交现成材料。

## 1. 目的与不变边界

只补齐运行 06ed068da2d948649f463889051ea157 的现成源码、合成语料、逐样本结果及保护/资源/错误记录，不重跑91样本，不重新编译或调用分类器，不执行ResourceGate/adapter/旧runner，不读取以前491成员的ZIP，不运行HA/HJB/KFE/selector/root/GE/IRF或模型。原V1.9执行合同及4/4批次额度保持关闭。Astra已接受四份附件字节与元数据一致性；实现审查仍为PENDING_REQUIRED_ARTIFACTS，不因本次交付而提前提升。

继承 docs/CH5_MANDATORY_REVIEW_DELIVERY_AND_CLEANUP_20261019.md。本任务明确允许且要求独立DELIVERY联网；历史执行期NO_NETWORK不适用于本任务的发布阶段。打包、哈希、文本解析、脱敏以及发布器自检用的PowerShell/.NET或Python辅助程序可在DELIVERY预算内运行；它们不是分类器测试或科学runner。禁止导入、编译或执行待验源码以及归档内代码。

## 2. 固定身份与精确写入范围

本合同与同目录 SOURCE_EXPECTATIONS.json 为不可变任务输入，由包外发行清单登记issue commit、Blob、原字节SHA256及长度；不得改写正文、替换历史哈希或制造校验版文本。结构化来源清单的四个锚点由Astra对Owner附件实际计算，其他33个载荷的预期值来自锚定后的原manifest，不手工二次录入。连接器文本与RAW_GIT_OBJECT_VERIFIED分级如实报告。历史未知项不是本任务新设的强制失败条件。

私有启动Prompt提供且仅提供两个绝对路径：SOURCE_ROOT与DELIVERY_ROOT。它们的精确末级目录名在 SOURCE_EXPECTATIONS.json 冻结；此处明确授权对SOURCE_ROOT中的35份白名单原件只读，以及在DELIVERY_ROOT不存在并通过身份检查后独占新建。不得把真实主机绝对路径复制到公开交付件。

BOOTSTRAP 0：只读验证任务授权、四份锚点、有限保护根及两条实际路径父链；SOURCE_ROOT只准读取原manifest登记的33份文件及manifest、FINAL_RECEIPT，共35份。源路径不得逃出该根，不扫描无关node_modules、旧ZIP或备份内容。完整保护根信息取既有可核原证/定位信息；目标重定向或必需身份不明则停止，不另找目录。
BOOTSTRAP 1：0通过后在私有Prompt指定路径创建独占DELIVERY_ROOT，重新核目录身份。
BOOTSTRAP 2：仅在该根写入平铺审阅件、delivery_audit、工具脚本和非共享bare对象库；不得覆盖SOURCE_ROOT、旧失败目录、项目worktree/index/common-dir或备份。不在本地创建_review_tmp目录；远端路径仅以Git tree条目构造。允许复用已安装git/ssh/PowerShell等工具，不改变global/system配置，不要求新凭据。

## 3. 必交证据：内容而不只是索引

来源清单绑定source task、source run、四份已独立核验锚点、原manifest的33条载荷及五项关键内容。必须核对并打包全部35份原件的安全可审阅副本到ZIP的 source/ 前缀，保留相对路径。包括：
- 最终分类器源码与测试源码、fixtures/synthetic_cases.json、attempt_02/RESULTS.json、docs/CLASSIFIER_BOUNDARY.md；
- 两次COMPILE_INDEX、TEST_SUMMARY、SOURCE_TEST_SHA_INDEX、PRETEST_SOURCE_REVIEW；
- FIRST、FINAL_PROTECTION、resource/000至003、保留的错误与旧候选；
- 原执行报告、原manifest、原FINAL_RECEIPT及其已登记治理快照。

source/manifest.json是原始来源索引，不是新ZIP的顶层manifest。不得用哈希表代替源码、gold标签和逐样本输出；不得删减失败样本、重新生成gold或为了补证重跑。读取不到必需载荷或与冻结预期不符时保留具体缺项/差异，禁止宣称完整补交。

若旧控制器的外部工具完成原件可从既有工具记录只读取得，另附 delivery_audit/source_controller_exit.json，标明工具事件来源及证据等级；没有原件则同一路径记录EVIDENCE_UNAVAILABLE/UNKNOWN，不生成虚构退出证明，也不重跑进程。其他35份现成证据仍可完成交付，终审不得将该未知项升级为已证实。

ZIP还须包含本次只读来源逐项对账、脱敏映射和发布器自检记录。源文件原字节不改；首尾复核35份源文件哈希。保留“原件”和“公开副本”不同身份。

## 4. 安全审查与可恢复工程错误

对35份源文件及所有新增公开载荷逐项按格式只读检查；清点包括JSON键和值、日志、源码字面量、Base64或嵌入文本，必要时有界解码以审阅内容，绝不执行。文件名或LOCAL_TASK_ARTIFACT_SYNTHETIC_OR_GOVERNANCE_ONLY标签不能代替内容检查。禁止上传真实凭据、主机私有路径/身份/网络环境、真实非授权研究数据、Git内部文件、编译二进制或未经审阅内嵌归档。

必须区分URI、JSON序列化表示、解码后的字符串、实际主机路径和可证明的合成样例。https://不是盘符；带转义的JSON字符串仍需检查解码语义；识别为URI不自动代表安全，仍查userinfo/query等。只在可追溯合成语料及上下文证明下保留必要的假路径/假凭据用例，不能泛化为“源码/fixture全部安全”。不把一个正则命中当作已证实泄露。

私有运行路径等非语义元数据可在副本中稳定脱敏；逐文件记录original bytes/SHA256、published bytes/SHA256、RAW_EXACT或SANITIZED_DERIVATIVE、具体规则和改变范围。不得修改算法、gold、实际分类、断言计数和错误结论。任何核心语义因敏感内容无法安全保持时，记录REVIEW_MATERIAL_BLOCKED，不悄悄缺省或改写。

不运行尚待验收的分类器充当自身公开安全的唯一认证器。不在本任务修复分类器；仅允许修复打包/格式解析/脱敏/发布辅助逻辑。发现普通语法、argv、上下文误判或无依据额外预期值，保留首错，在6次E1修复额度内对原始只读输入重新核验；不是每个误报都重发任务。真实冻结原件不匹配、保护区写入风险、凭据无法隔离或资源/认证硬门失败则STOP。单项内容未决可在安全只读条件下继续清点其余有限载荷以一次报告全部问题，但所有未决必须解决后才发布。

## 5. GitHub强制交付，发布前自检

REVIEW_BRANCH=review/ch5-classifier-v19-evidence-20261019
FIXED_PARENT=69652a0791e813ffaa0dd629feafcf9b5bd4db79
TEMP_PATH=_review_tmp/ch5/classifier-v19-evidence-20261019/
REMOTE_ALLOWLIST=result.md,manifest.json,evidence_sanitized.zip

固定parent是本任务之前的已归档治理提交，不是源合成任务commit，也不是本任务issue commit；三者不得互换。候选唯一parent必须等于上述值，相对它仅新增三件。只允许新独立review分支；若已经存在，不覆盖、不force，记录冲突。

Codex必须自动打包并发布，正常终点不是本地路径或要求Owner手动上传。沿用既有SSH Key及ssh.github.com:443，在新scratch的独占bare库构造对象，无checkout、无共享objects/alternates，不触及原项目index。父tree必要对象须完整，不用缺promisor对象的partial基线假装可发布。此处明确授权所需有限fetch，不是旧任务恢复。

先用小型人工ZIP在本地fake-bare中验证同一发布器的argv、三件tree/单parent、普通推送、实际ZIP字节回读与白名单删除；失败按E1修复额度处理。它属于DELIVERY_SELFTEST，不重跑分类器测试。完整35件新包再做CRC、成员安全、逐成员SHA、重复/大小写碰撞、绝对/UNC/ADS/..路径、链接和解压总量核验。不要将真实旧归档混入自检。

顶层result.md描述补交范围与旧结论等级；顶层manifest.json登记result与ZIP身份及ZIP所有成员的原件/副本身份。不要求manifest包含自身最终哈希，不要求候选commit/tree预先出现在会影响该commit的文件中。source/manifest保持来源身份。新ZIP不内嵌它自己的顶层manifest或自身哈希。

安全自检通过后执行一次成功的普通non-force发布，并回读ref、commit、tree、唯一parent和三件真实字节。MD/JSON也按原字节计算，ZIP必须实际得到字节而不是只读SHA标识。候选发布成功但回读暂失败时只读重试，不再推送第二候选。

## 6. 本次独立预算及阶段权限

SCIENCE_BUDGET=0；CLASSIFIER_COMPILE_OR_TEST_RERUN=0；OLD_ARCHIVE_READ=0；MODEL_RUNNER=0。
DELIVERY：最长180分钟（从本任务首个计时动作，启动只读阶段计入）；修复/重试批次最多6；所有真实进程及后代累计最多256，包含controller/Git/SSH/短寿命后代；Python辅助启动最多48，同时活动Python最多4；不建立额外worker线程池，运行时线程如实观察，不将运行时线程冒充任务worker。工具观察启动数与内核计数分账且不重复累加；无法追溯的旧OS身份保持UNKNOWN。新非Git字节<=128MiB；独占Git对象<=2GiB。预算执行前检查并预留；意外后代或可信计数失信停止相关执行，不声称single-child gate能容纳任意Git后代。

发布器fake-bare完整自检最多3轮，纳入上述预算；SSH预检<=2；真实git fetch<=3；真实push CLI尝试<=2，最多1次成功发布；治理导航、ref查询及远端字节回读GET合计<=64（失败也计数，明确不等于全程无网络）。认证/权限硬失败、已超预算不得继续；argv等尚未联网的确定性E1可以在余额内修复。不得使用旧任务剩余额度。

公开文件上限：result<=128KiB，manifest<=1MiB，ZIP<=8MiB，ZIP总解压<=32MiB，成员<=200。若发现嵌套归档，最多2层、合计同一大小/成员限额，全部审查；不可解析则不发布。当前来源本是小型文本证据，不能为扩大范围压缩绕过上限。

## 7. 最终回执通道与单向身份关系

源FINAL_RECEIPT是已存在原件，必须随source/进入ZIP，不再单独遗留本机。它的controllerExit=PENDING_EXTERNAL_TOOL_COMPLETION不得被新报告追溯改写。

新DELIVERY_FINAL_RECEIPT.json在成功push及全部字节回读后生成；含候选身份、三件字节长度/SHA256/Git Blob、原件映射、实际预算、首错、UNKNOWN、封存时controller状态及单调计数截止点。它不回写已发布三件，避免自引用和第二次成功发布。由同一交付进程输出该原文件的完整Base64、长度、SHA256至工具最终输出，Codex原样带回最终答复；这就是预先授权的包外回执通道，不要求Owner另行手动上传文件。之后只允许关闭句柄、退出和回收，不再启动子进程或测试。

控制器退出证明用紧随其后的外部工具完成原始回执单列，由Codex带回；不能把尚未发生的退出写进自身回执。若工具不提供可转交原始事件，标明UNKNOWN，不伪造全链独立认证。Astra永久归档回执或其安全派生件及身份。传输成功、实现验收、OS认证分别报告。

## 8. Astra验收后强制归档与删除

CLEANUP_OWNER=ASTRA；Codex在WAIT_ASTRA停下，禁止提前删除。
Astra读取指定候选三件真实字节，检查完整源文件/派生关系与测试证据，给出限定终审。先在治理分支永久归档结论、必要身份与未决项并回读，然后必须删除本review分支当前tree中的三件白名单文件；核实review HEAD未被改变，普通非force清理commit，回读三路径缺失并归档清理回执。清理最多2次有界写尝试，冲突不得覆盖第三方修改；失败记TEMP_CLEANUP_PENDING，不能报CLOSED。没有候选则NOT_APPLICABLE_NO_CANDIDATE；验收仍PENDING时不先清理。

完整关闭需DELIVERY_VERIFIED + REVIEW_ARCHIVED_AND_READBACK + TEMP_CLEANUP_VERIFIED。Git删除不抹除历史，所以敏感信息必须发布前处理。不得清理其他旧任务、main、冻结合同或模型。

FINAL_STOP=WAIT_ASTRA_CLASSIFIER_V19_FULL_EVIDENCE_REVIEW
正式V010不变；model_activation=False；REAL_GE=False；Results=FALSE；V011=NOT_STARTED；FULL_RUNNER_IO_CLOSURE=BLOCKED。分类器补交完成不自动授权旧ZIP扫描、发布旧包或任何后继科学任务。
