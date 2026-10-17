# V010：当前 SOURCE_TIMESTAMP 条件修复的脱敏 GitHub 证据交换

**唯一任务ID：** V010_CURRENT_TIMESTAMP_SANITIZED_EVIDENCE_EXCHANGE
**版本/性质：** V0.0.10 / V010；EVIDENCE_EXCHANGE_ONLY + ONE_BOUNDED_GITHUB_REVIEW_PUBLICATION
**Owner授权：** 2026-10-17，同意只将上一轮新产生的 SOURCE_TIMESTAMP 来源/类型/25项合成与 first/final 封存的安全材料交到 GitHub 独立review分支，由Astra独立核查。本次不作高精度格式新采纳、不补造历史执行字节、不恢复旧任务。
**交付ID：** V010_CURRENT_TIMESTAMP_SANITIZED_EVIDENCE_EXCHANGE_RESULT
**结束：** WAIT_ASTRA_V010_CURRENT_TIMESTAMP_EVIDENCE_REVIEW / STOP
**发行身份：** 第一次冻结提交Commit与本文件Git Blob，以签发后 TASK_CURRENT.md 记录为准；不得追改正文。

## 0. 必读权威与不变证据等级

- 唯一仓库 zcx369658780/dissertation-ch5-two-asset-hank，治理分支 migration/astra-workflow-20261012（不是main）。Codex先从本任务**固定发行Commit**读取全文并验证Blob，随后只读CURRENT、TASK_CURRENT、DOC_INDEX、版本登记、V1.2、Owner风险/备份/SSH/Loader决定及 docs/CH5_TEMP_SANITIZED_REVIEW_EXCHANGE_20261016.md。若身份矛盾/分支漂移，FAIL_CLOSED。
- 最近冻结任务 V010_SOURCE_SCRIPT_PROVENANCE_RECOVERY_AND_CONDITIONAL_TIMESTAMP_FIX：Commit fafffe0582a213ceec25312f97f47ade6f1aa508、Blob 22aea7c18716c36ffb1f3154d35d751d9f524bf1；已STOP。正式主审 versions/0.0.10/source_script_provenance_conditional_timestamp_local_only_primary_review_20261017.md，Blob d6a53e96e359ac2c3d437ed9025cd5f58b129492。其结论仅限 CODEX_REPORTED_WITH_LOCAL_RECEIPTS：Gate R取得现时来源/整文件SHA256/schema锚点，**历史源码hash未记录，HISTORICAL_EXECUTED_BYTES_UNVERIFIED**；Gate T报告现时PowerShell7.6.6把合法JSON String/Z时间戳解析为System.DateTime/Utc而与旧“解析后仍string”断言冲突，历史PS版本UNKNOWN；Gate F25个新合成中24符合预期，**第25个高精度形态 SPEC_UNRESOLVED，不算PASS**；原字段只读复核据报通过但原件未获网页独立复算。
- 上轮最终本机receipt SHA256由Owner转述 B37FA71992497C299D2E218029D08AD1F863A83A6F6C60C852342C82EB0430B0，Astra未获取原字节重算。前几轮17/17集成/其seal仍本机报告级，更旧B/S/L20旧first raw与run_id缺失永久 LEGACY_SEAL_CHAIN_UNVERIFIABLE。旧sanitizer曾拒绝的候选始终 PUBLICATION_DENIED、命中根因UNKNOWN；历史ledger复制raw argv/源码过程偏差UNRESOLVED。新任务不清理、不重写、不重跑任何旧证据。

## 1. 新scratch、精确来源与提交表示

**唯一新可写根：** D:\ProjectTemp\ch5_v010_timestamp_evidence_exchange_20261017_01。创建前核路径及父目录真实身份、无reparse/junction/UNC/device/ADS/别名与受保护目录重叠，失败STOP。原科研模型/治理worktree、原8dirty/index/common-dir、C盘备份、所有历史失败scratch均不触写。

**唯一允许精确只读的上轮来源根：** D:\ProjectTemp\ch5_v010_source_provenance_conditional_20261017_01。优先用上次 FINAL_RECEIPT / manifest 已认证的**实际文件定位**确定上轮真实 FIRST/FINAL_RECEIPT、当前来源身份锚点、测试结果/25项case evidence、安全修复设计文档。若缺索引，至多在此**单一根执行一次depth=0元数据盘点（最多8个直接子项）**，但仅凭相似名称不得替代实际绑定；内容只读最多**8份不同普通小文件，包含重复读取总字节≤1MiB**。先核类型、大小、不重解析及前后原字节SHA256；缺源、失败或来源索引不可信便LOCAL_ONLY STOP，不能跨到更老scratch、全盘搜索或重新生成旧原始seal。

**新的远端证据必须按字节来源分级：**
- RAW_EXACT_UNCHANGED：上一真实first/final文件原始字节完全安全（UTF-8/LF/schema/所有脱敏规则均PASS）方允许原封不动发表，不重排JSON键、换行或改变timestamp；remote SHA256 应等于当前本机raw hash。
- SANITIZED_DERIVATIVE：若raw中有绝对私有路径、原argv、原源码片段、时间值/其他不宜公开内容，则仅用本轮新scratch构造最小安全投影，声明 raw_source_SHA256、published_SHA256、映射和哪些字段脱敏/不可再验证；Astra独立只能核已发布派生文件，**不得将投影叫做真实raw已远端认证**。源本机raw SHA只能作为Codex计算的声明，不能从派生物推断旧原字节。
- 无法安全产生满足相同run_id、first/final单向链接、24个实际PASS和1个SPEC_UNRESOLVED的可审查投影时，停止，不能把25个案例全部标成PASS或伪造case hash/run_id。
- 不在本轮“接受”“拒绝”原合同未规定的高精度表示。相关case明确保留 SPEC_UNRESOLVED，排除出合格接受集；不重新执行该case，不用新的format floor或宽松日期parse求PASS。历史脚本哈希/PS版本仍UNKNOWN。

## 2. 唯一远端review分支、五份白名单和精确parent

**新review ref：** review/ch5-temp-v010-timestamp-proof-20261017
**远端Git tree唯一新增前缀：** _review_tmp/ch5/v010-timestamp-proof-20261017/
**仅以下5份 UTF-8/LF 严格脱敏、非可执行文档可新增：**
1. result.md ≤24KiB：本轮LIMITED/local证据、三Gate分账、实际资源与STOP；
2. manifest.json ≤96KiB：冻结task/model身份、旧Task/Review、来源现时与历史证据级别、source raw/current SHA声明、每份发布文件hash/字节数/来源映射、run_id/hash-chain ID、远端/本地可验边界与发布账；
3. first_seal.json ≤48KiB：本轮first真实原字节（如安全），否则最小DERIVATIVE；禁止伪造历史first；
4. final_seal.json ≤48KiB：对应final真实原字节（如安全），否则最小DERIVATIVE；
5. cases.json ≤96KiB：**25项新合成的已存在匿名case_id、expected/observed/result_hash以及24 expected-match / 1 SPEC_UNRESOLVED，不重跑、不补造**；注明旧run与本轮run身份不同。

manifest应含其他4个发布文件的SHA256与字节数；**不能自含自己的SHA256造成自引用**，manifest自身SHA256/Git Blob在最终脱敏交付摘要和GitHub readback中单独报告。result.md不得反向引用manifest自身hash以形成互相循环。所有原raw SHA256与已发布文件hash须区分，不能混作“GitHub核实了本地原始值”。源程序源码或diff的实际原文字节、真实timestamp值、完整argv、absolute private path、token/SSH key、raw日志、模型数据及原拒绝候选禁止上传。

**唯一候选Commit的sole parent必须等于本任务第一次发行Commit**（不是推送时live治理HEAD、main或旧failed ref）。候选tree须是固定parent的原tree加上述5个白名单路径，其他任何原路径都不能改、删、stage、checkout。新review ref必须在发布前确认不存在，不覆盖已有同名ref。用户本地包括scratch在内**不得物理创建** _review_tmp/ch5/... 目录，remote-only路径只作为Git commit tree项；五份素材本地只能平铺，不能进入任何科研、模型、治理worktree或Git index。

## 3. 发布前检查、SSH Git对象闭包与一次性严格预算

1. 使用已做过合成测试的结构化Sanitizer/SafeLedger原则对**拟公开的5份**新素材检查：合法转义允许但解码后真实私有路径、raw argv、credentials、原日志须DENY；对嵌套、重复键、异常时间类型、UTF-8/LF、大小与case身份逐项核验。只能输出匿名rule_id/file_id/field_class/count，不得显示命中原文。静态筛查≤2轮（首轮失败则只允许在本轮scope内修安全投影后做一次复核；语义身份缺失/无法安全修则STOP）。不使用旧被拒候选当样例或重新扫旧敏感材料。
2. Codex仅使用已有SSH Key和 ssh.github.com:443，严格verified host key；禁止PAT/API token、私钥外发或更改global/system Git config。先在**全新scratch独占非共享的git --bare对象库**准备发行Commit的完整parent/tree/必需blob；不shared/alternates/worktree/checkout、不依赖 --depth=1 --filter=blob:none 不完整对象。真实Git common-dir/对象闭包、目录非共享、Git argv/stdio/timeout按既有工程守门，任何FAIL_CLOSED不得为了发布绕过。
3. 为确保远端ref不存在，最多**1次SSH ls-remote精确ref预检**；为获取唯一固定parent完整对象最多**1次有界SSH fetch**，候选Git-only对象构造最多git hash-object -w 5次、git mktree 10次、git commit-tree 1次、额外read-only Git元数据children总≤40。全部先做固定parent和白名单tree比对，mktree serializer额外空行/非法mode/path必须主动DENY。只有**5份全套安全PASS、证据等级正确、唯一parent/tree对象可达且预算余量可证**才允许**1次普通non-force push**到唯一新review ref，失败LOCAL_ONLY_STOP、不二次push、不force；推送后允许最多**1次远端ref readback**。禁止其它GitHub branch或旧candidate变更。
4. 总wall≤**150分钟**，本轮新scratch新增最多**9份非Git平铺文件、总计≤2MiB**（包含5个平铺发布文档、检测/计数记录、first/final新封存及结论），须预留≥128KiB用于失败和终态回执；新独立bare全目录含objects/config/refs/隐藏meta≤**3GiB**独立计量。上轮已有数据精确只读≤8 distinct files/总读取≤1MiB；单根depth0 metadata listing≤1次/最多8直接子项；PowerShell文本准备/脱敏/封存最多**2个受界批次**，启动前计费。Git网络4种操作的预算如上，任一失败不延长时间、不借新任务名续额。
5. **所有模型与科研进程0**：Python/py/pytest/Jupyter/VerifiedLoader/model import/真实runner/HA/HJB/KFE/selector/roots/GE/IRF/MATLAB/real C8/原17项、原20项与新25项重跑均0；不修改V010代码、冻结科学计划、原raw timestamp、源guard、原first/final或旧失败日志。Owner现有两物理SSD上的C盘既有备份＋GitHub和受信任Windows工作站技术风险边界保留，不强制第三份备份或新VM。

## 4. 交付、独立验收与STOP

Codex交付V010_CURRENT_TIMESTAMP_SANITIZED_EVIDENCE_EXCHANGE_RESULT：固定issueCommit/taskBlob、候选commit/tree/sole parent与远端ref（若发行）、5个remote Git blob ID/发布SHA256/size/representation、原raw SHA声明与本地哈希链关联、25项分类24 expected/1 SPEC_UNRESOLVED与未运行项、结构化sanitizer scan PASS或规则匿名失败、目录/读取/进程/全部网络计账与所有UNKNOWN、FAIL及保护状态。结果等级最高 `SANITIZED_GITHUB_CANDIDATE_PUBLISHED_AWAIT_ASTRA_REVIEW`，不得自授Astra独立remote审议PASS。任何前置失败一律 `LOCAL_ONLY_FAIL_CLOSED`，不准追加fetch/push/换ref。

Astra收到候选后，按候选固定SHA/ref实际读取5文件，核单父、tree仅白名单、Git Blob、SHA256与case、first/final及源raw/派生分级；只有独立回读到的远端字节能升级证据等级。先在治理分支永久归档主审和当前状态并读回，再按Owner已许可协议**只删除新review分支当前tree中5个临时文件**并回读，不能清理原本地scratch、旧失败证据或重写Git历史；如连接器不能安全执行删除，标TEMP_CLEANUP_PENDING并保留，不force。Git删临时文件不等于旧commit的字节从历史被清除，因此严格前置脱敏。

科学不变：V010 plan commit bf091da33d59293f147d52c11580327d3ac2a85d / Blob 85138d8859d53295262fe13bf5bc277bca95ed3f；模型commit 94de4501dec051b969bee9d852eba2d4591f30ef / Tree 205eab47c4e4f9c6292c2ead9947d94d1a7579a5。原MATLAB修错与corrected两资产HA/HJB/KFE、多省手动顺序、GovInv原收益界×0.9/1.1与Zt、GDP冻结后各省误差≤1%、目的地税一次、same-S与lagged raw ra0、家庭/省财政单位/三劳动账、phi_max=.3、lagged-NKPC不改。Owner corrected HA单点仍UNTESTED；A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、real C8 A–D REQUEST_ONLY、FULL_RUNNER_IO_CLOSURE BLOCKED、model_activation=False、Results FALSE、V011 NOT_STARTED。原D:\ProjectTemp\c5k1bturn56八dirty/index/staged/untracked/ignored/外Git common-dir、旧失败raw、C SSD备份、真实C8/2017/2018/B3/V009数组一律不可触写。统一 STOP = WAIT_ASTRA_V010_CURRENT_TIMESTAMP_EVIDENCE_REVIEW / STOP；无后继科学授权。
