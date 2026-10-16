# V010 当期 first/final 封存证据：受控脱敏 GitHub 审阅交换

**唯一任务ID：V010_CURRENT_SEAL_SANITIZED_GITHUB_EVIDENCE_EXCHANGE**
**版次：V0.0.10 / V010；类别：EVIDENCE_EXCHANGE_ONLY + LIMITED_GIT_PUBLICATION**
**Owner授权：2026-10-16，在最新本地合成集成主审后同意由Codex发布当前已生成的安全脱敏证据，供Astra独立回读。**
**交付ID：V010_CURRENT_SEAL_SANITIZED_GITHUB_EVIDENCE_EXCHANGE_RESULT**
**最终停点：WAIT_ASTRA_V010_CURRENT_SEAL_GITHUB_EVIDENCE_REVIEW / STOP**
**冻结签发Commit/Blob以签发后TASK_CURRENT登记为准。本文件冻结后不可追改；禁止将旧STOP任务当成仍有余额。**

## 0. 精确前提与权限解释

- GitHub唯一仓库：zcx369658780/dissertation-ch5-two-asset-hank；权威治理分支：migration/astra-workflow-20261012，不是默认main。先从固定任务发行commit读本文件完整正文并核Git Blob，再读取DOC_INDEX_CURRENT、CURRENT、TASK_CURRENT、VERSION_REGISTER、V1.2、Owner风险/SSH/Loader决定、远端临时脱敏review交换协议。
- 紧邻上一STOP工程任务：V010_ENGINEERING_INTEGRATION_SEAL_CHAIN_SYNTHETIC_MKTREE_PREFLIGHT，发行commit 34497613d7085cfeea39682aef15f983ef5030a9、任务Blob 6aa223b4c98391e051ebe4f7b8d358f88cf678bf。最新独立主审：versions/0.0.10/engineering_integration_seal_chain_synthetic_mktree_local_only_primary_review_20261016.md，Git Blob 32272533e9f4136883f536814919bddf2cb037d9。
- 上轮Codex只在本地报告17/17合成工程集成、两条精确tree entries的synthetic mktree正例和多余空行负例exit128、当前 first/final 两份真实raw字节与同run_id/17项result hash/单向引用；**Astra没有直接取原字节，不存在远端独立工程PASS**。最新Owner转述本地DELIVERY_RECEIPT.json SHA256=859398F7F4ABF2067AAF6613213290B9F027EE48D2A7E0EEA361BC0C5FDF5197，未经网页独立哈希复算。
- 更早B/S/L 20项任务的旧首版seal**仅有快照/hash引用、缺可还原原字节且未记录旧run_id**，正式分类LEGACY_SEAL_CHAIN_UNVERIFIABLE，永不得补造、重跑20项来伪称原封存通过，也不得把本轮run_id/first seal回填历史。原旧被拒脱敏材料仍PUBLICATION_DENIED、原拒绝根因UNKNOWN；历史中间台账复制raw argv/短源码偏差仍UNRESOLVED，不删除旧证据、不上传旧原件。
- 本任务只做**安全新证据交换**，不修模型和工程程序、不跑之前17项或B/S/L20项测试、不重试旧bare/旧mktree，不触及science Results/V011。若所需原证无法在规定只读预算内定位/哈希/脱敏，立即LOCAL_ONLY FAIL_CLOSED并准确保留未完成项。

## 1. 独立scratch、精确证据与字节判定

**唯一新项目外scratch**：D:/ProjectTemp/ch5_v010_current_seal_exchange_20261016_01。创建前必须确认根及祖先无reparse/junction/symlink/UNC/ADS/别名，不属于旧scratch、旧D盘保护树、已有工作树、模型Git/common-dir或C盘SSD备份；不满足即STOP。除这处新的scratch与其中全新独占无工作树bare Git对象仓，不准写任何原项目、冻结模型、Stage A身份根、旧失败回执或其他目录。

**只读旧证据白名单**：上轮D:/ProjectTemp/ch5_v010_integration_seal_mktree_20261016_01中准确的最终DELIVERY_RECEIPT.json及其指向的原始first seal、final seal、17项case manifest/结果hash索引、所需原匿名流水线proof。按文件路径来源及hash先判定，最多8份确切原件，累计真实读取≤1MiB；禁止目录泛扫、读取大日志/模型源/原raw argv。优先取前轮最终回执的原字节并重新SHA256，应精确匹配本节固定的859398F7...值；哈希不符则RECEIPT_IDENTITY_MISMATCH/STOP。检查源first/final是否真的存在于磁盘且为两个不同raw可读实体，同run_id、同测试索引/结果hash、单向链一致。任一raw实体不存在，不得用回执文字、快照、投影文件虚构原件。

**需供独立审阅的最小证据**：本轮必须形成一个可被Astra从GitHub真正读取的、与旧raw实体明确定级的证据包：
1. 新的first_seal.json：仅来源本轮first seal的最小字段（源run_id、case result摘要hash、timestamp类别、first/final引用关系和各门状态），不能含绝对D/C路径、私人对象名、原argv/源码/原stderr、credential。
2. 新的final_seal.json：仅来源本轮final seal的安全字段、同run_id、对first raw hash的单向指针、完整17项核验/资源汇总的非敏感统计。
3. manifest.json：固定task/model/科学plan Git身份、证据类型、原first/final本机raw SHA256/size（仅本机重新计算的**声明**）、上载文件各自raw SHA256/size（可供Astra复算）、source-to-published映射、17项各组真实跑过的匿名case ID及result identity（不得伪造明细）、sealed hash/run-id链接、原OldSeal不可验证、真实runner未跑、科学仍BLOCKED、全部资源实际消费/未知及脱敏扫描安全状态。
4. result.md：简短的事实/失败/证据等级/门禁总表，明确原旧材料仍禁止发布。

**原字节 vs 脱敏派生严格分级：**
- 若前轮first/final原文件已天然符合UTF-8/LF、JSON结构和全部安全规则，且无一字节敏感内容，则新first_seal.json/final_seal.json可作为**RAW_EXACT_UNCHANGED**直接原字节上传，不改变换行、排序、字段、标点或BOM；manifest中须分别记录local_source_SHA256与remote_file_SHA256相同且source representation为RAW_EXACT。
- 若原件任何字段不能安全公开，只准在新scratch构造**SANITIZED_DERIVATIVE**投影（必须保留能安全表述的run_id、hash指针、case result身份和必要计数）；manifest同时记原始源hash及发布派生hash，并明确Astra**只能独立核派生物字节**、不能独立认证未发表raw。绝不可把派生物重新称为RAW_EXACT或原Windows完整链已Astra鉴证。
- 原raw内若包含真实key、token、SSH私钥、原始含秘密的argv或敏感路径，一律不外传。若连投影也无法保留关键可核字段/形成安全证据包，则直接LOCAL_ONLY/STOP，不为了完成GitHub发布而降低脱敏门或私自补生成缺失身份。科研不涉保密不等于凭据/私有路径豁免。

## 2. 受控脱敏与发布器前置

- 使用上一已测试的StructuredSanitizer/SafeLedger安全结构化约束，仅处理本轮拟发表的四份文件；最多一轮本地受界筛查+修正后再一轮复核（必须明确记录次数），只允许PowerShell文本/JSON静态校验与安全稿写入，不执行Python或真实科研/runner。要求JSON UTF-8 LF、有效schema/无重复键/深度/大小/嵌套/转义安全；合法JSON转义不是自动秘密，但解码后私有绝对路径、秘钥格式、raw argv、真实日志必须DENY。所有异常/扫描返回只有匿名file ID、规则ID、字段类别、命中数、阶段，不输出命中原文字节。旧SANITIZATION_DENIED来源仍UNKNOWN，不对旧候选补扫/补推。
- 远端目标分支：review/ch5-temp-v010-current-seal-evidence-20261016（**须确认此前不存在**）。远端候选树中**唯一新增路径前缀**：_review_tmp/ch5/v010-current-seal-evidence-20261016/；对应四文件的精确白名单：
  - result.md（≤24KiB）
  - manifest.json（≤96KiB）
  - first_seal.json（≤64KiB）
  - final_seal.json（≤64KiB）
  全部为经脱敏的UTF-8 LF文本，目录/文件名不得新增别的。**_review_tmp 前缀只能在独立review分支Git tree中存在，不得在任何本地科研、模型、治理worktree/index/staged中创建目录、checkout/git add，也不借.gitignore隐藏。** 本地新scratch仅平铺四个发布素材，bare仅存Git objects，不使用工作树。
- **单parent candidate**：唯一parent=本任务正式发行commit（参照发行后TASK_CURRENT），其Git tree在新candidate中只额外增加上述4个安全文件，parent历史树下任何旧路径不许删除或更动。禁止将本轮临时文件放main/治理分支，禁止改版本冻结计划或模型。
- 根据Owner SSH技术决定：Codex只能使用其现有SSH Key+严格host-key+ssh.github.com:443（不改global/system Git配置、不引入PAT/API token、不泄露agent/private key），在**项目外全新独占git --bare**对象仓中备齐固定发行commit/tree/必要blob、无alternates/--shared/--reference/worktree/checkout。为固定parent完整对象准备最多**一次完整SSH fetch**，不使用缺必要对象的浅blob:none猜测write-tree可行；若全部真实Git对象闭包无法在本轮资源内验证，停止发布，不另挪模型仓或追加网络。仅在发布白名单/脱敏/树/大小全PASS并且远端目标ref尚不存在时，准**一次普通非强制 push**至本轮全新review ref；失败立即LOCAL_ONLY_STOP，不重试、不强推、不push旧分支。
- 发布后Codex仅核一次远端新ref SHA/readback、commit唯一parent/tree SHA和四Git blob ID/原文字节SHA256（本地计算），并如实返回给Astra。Astra之后用GitHub连接器独立读取**新远端branch/commit真实四份文件**、计算/核对可取得的字节与关系，永久审查写入治理并回读后，依据Owner既有协议才清除**此轮remote临时review目录白名单文件**；旧commit历史保留。切勿声称删除临时工作分支后的历史blob已被彻底擦除。

## 3. 一次性新预算与绝对禁止事项

- 专项Nature=EVIDENCE_EXCHANGE_ONLY。新的Windows PowerShell静态来源核验、哈希/脱敏准备限**≤2批次**，**Python进程0**、VerifiedLoader/真实runner/模型import0、HA/HJB/KFE/selector/roots/GE/IRF/MATLAB/真实C8/科学校准全部0，前一B/S/L20与最新17次合成测试重跑0；无需新source assembly/E0 guard/mktree synthetic panel。不得更改旧本地seal任何一字节。
- 原证只读≤8份/1MiB，项目外新scratch所有非Git新文件（含封存/安全扫描记录/4份平铺脱敏稿/失败回执）≤8份且总物理新增≤2MiB，final应急封存先预留≥128KiB；单独新bare Git完整metadata/对象≤3GiB（它是临时工程交换对象库不是第三套模型备份），独立计量。总wall≤150分钟，Git metadata read调用≤80。网络最多本轮一个完整固定parent fetch、一次普通非强制push、一次remote ref readback；禁止模型clone、安装软件、隐式lazy fetch/反复SSH、对原Stage A clone或任何旧bare Git写入。
- 允许在独立bare中为**四份脱敏文件和审阅candidate的构造**精确进行git hash-object -w≤4、tree组装git mktree≤8、git commit-tree≤1；这些只用于已获批的本次证据发布，不重做科学/旧故障实验。若Git版本/脚本将额外空行传给mktree或构造出的tree非精确原父树+四新增文件，则立即STOP，不能以重试或删除原始目录规避。不要在本地建review目标目录物理树或项目index。
- 任何旧保护目录不可改变：D:/ProjectTemp/c5k1bturn56原8 dirty、staged/index、untracked/ignored、外Git common-dir、所有旧失败scratch与本轮上一17项证据、C盘物理独立SSD既有备份、真实C8/2017/2018/B3/V009失败数组。无额外VM或第三套备份要求，Owner认可可信工作站局部工程隔离但不等于OS-native sandbox。
- 不得激活V011、修改现行V010冻结经济法则和已接受corrected HJB/KFE，继续保留源方法手动多省、GovInv收益边界×0.9/1.1/Zt、目的地工资税一次、家庭人均/省财政总量/三劳动账、same-S/前完整轮raw ra0、phi_max=.3、lagged-NKPC与冻结GDP≤1%独立目标。新corrected HA单点rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07依然UNTESTED；FULL_RUNNER_IO_CLOSURE=BLOCKED、model_activation=False、Results FALSE、real C8 REQUEST_ONLY、A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、V011 NOT_STARTED均不变。

## 4. 交付及终点

Codex一次集中交付V010_CURRENT_SEAL_SANITIZED_GITHUB_EVIDENCE_EXCHANGE_RESULT，至少包含：
1. 发行commit/task blob、来源上轮scratch原final receipt SHA256实算及first/final存在性、相互run_id及17项结果hash和单向链本机核对；
2. 四个published文件representation（RAW_EXACT/SANITIZED_DERIVATIVE）、大小、Git blob SHA1和published SHA256、raw source SHA256（声明）、所有本地证据等级/可独立核验边界；
3. 防泄露的scan`PASS/FAIL_CLOSED`、规则ID统计、时间/文件/容量/Git子进程/fetch/push/SSH返回码的准确使用账，凡没有实际观测一律UNKNOWN；
4. 若成功发布，review ref/唯一parent candidate SHA/tree与远端HEAD回读，等待Astra独立核验，不自授科学/工程集成或GitHub内容验收PASS；
5. 若任何一项前置失败，LOCAL_ONLY/FAIL_CLOSED、未使用网络和推送额度关闭，不将旧被拒候选拿来补充发布，不恢复上一STOP任务余额。

最终分类不能超过EVIDENCE_EXCHANGE_CANDIDATE_PUBLISHED_AWAIT_ASTRA_REVIEW；如全部四件为RAW_EXACT且由Astra回读匹配，可在**后续独立主审**才分账写可验证raw来源关系；SANITIZED_DERIVATIVE只允许remote projection内容核验，不能称原私有raw已独立证明。结尾统一：WAIT_ASTRA_V010_CURRENT_SEAL_GITHUB_EVIDENCE_REVIEW / STOP。Codex不得自动开始Python工程import、真实runner、HA数值或下一版。
