# V010 SOURCE_TIMESTAMP：解析类型取证、语义守门修复与合成正反例集中任务

**唯一任务ID：** `V010_SOURCE_TIMESTAMP_TYPED_GUARD_CORRECTION_AND_SYNTHETIC_REGRESSION`  
**版本：** V0.0.10 / V010。**性质：ENGINEERING_ONLY_LOCAL_TIMESTAMP_DIAGNOSIS_AND_CORRECTION**。  
**Owner新授权：** 2026-10-17，在上一证据交换 `FAIL_CLOSED / LOCAL_ONLY` 正式主审归档后，明确同意**同一张任务**完成根因定位、只在新隔离区修正类型/时间语义守门以及纯合成正反测试。**不是**对上一停止任务的重试、GitHub候选发布授权，亦不是模型Python/runner/HA科学许可。  
**交付：** `V010_SOURCE_TIMESTAMP_TYPED_GUARD_CORRECTION_AND_SYNTHETIC_REGRESSION_RESULT`。  
**终点：** `WAIT_ASTRA_V010_SOURCE_TIMESTAMP_TYPED_CORRECTION_REVIEW / STOP`。  
**冻结身份：** 本任务原文第一次发行的commit与Git Blob由后续动态 `TASK_CURRENT.md` 精确登记；本文发行后不得追改，Codex必须从固定commit直接读取。

## 0. 权威、上一轮证据与不变裁决

- 仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。治理分支：`migration/astra-workflow-20261012`，**不是main**。先读取本任务固定发行commit下全文及Blob，再只读核 `docs/DOC_INDEX_CURRENT.md`、`CURRENT.md`、`TASK_CURRENT.md`、V1.2及Owner备份/SSH/Loader、临时审阅协议和版本登记。任何动态分支漂移或Task冻结不匹配：STOP。
- 上一STOP证据交换任务 `V010_CURRENT_SEAL_SANITIZED_GITHUB_EVIDENCE_EXCHANGE`：发行Commit `49ff1c3053fa1aa6a0646f55abcffb077e2b62b2`、任务Blob `1dc5f07a88261c41de434a9c4075b0d179ee871a`。正式主审 `versions/0.0.10/current_seal_exchange_source_timestamp_fail_closed_local_only_primary_review_20261017.md`，Blob `87d35c2270c1b8a42e19d3210f22fa0abe914bdc`，分类 `SOURCE_TIMESTAMP_PARSED_TYPE_GUARD_REJECTED__ACTUAL_TYPE_UNKNOWN__NO_GITHUB_CANDIDATE`。据Codex上一回执：JSON解析后timestamp被要求仍为string，门失败，**并未记录真实类型、解析器名称/版本及原JSON token种类**。这不证明原始时间戳无效，更不证明具体是PowerShell自动转换造成。
- 上一失败receipt Owner提供SHA256 `F93DA4C6BEE0E62F68A04620B8BF372AD60275C20DEA7782EF2C56E4BFADA6FC`；网页Astra尚未取本机raw复算。原交换只用静态PowerShell批次1/2、旧文件5份43,468B，scan0、bare0、SSH0、fetch/push0，任务已STOP，余额一律关闭不得借用。
- 上一轮本地工程集成17/17与**当前**first/final同run_id、测试hash链仅`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`；更早B/S/L20项的**旧**first seal缺可还原raw、旧run_id缺失，永久`LEGACY_SEAL_CHAIN_UNVERIFIABLE`，不得再补造。原旧候选扫描拒绝原因UNKNOWN且材料`PUBLICATION_DENIED`，历史台账曾包含raw argv/短源码的偏差`UNRESOLVED`。不得将任何一项误写为PASS。
- V010冻结科学plan commit `bf091da33d59293f147d52c11580327d3ac2a85d`、Blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；模型候选commit `94de4501dec051b969bee9d852eba2d4591f30ef`、tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，不可改写或import。Owner corrected HA单点 `rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07` 未运行；V011未启动。

## 1. 独立scratch与受界原证只读

**唯一新增可写根：** `D:\ProjectTemp\ch5_v010_source_timestamp_typed_20261017_01`。创建前先证明不存在、不是reparse/junction/symlink/UNC/ADS/替代数据流别名或受保护根的子代；新root和其中新flat文件才准写，严禁触写旧scratch、原科研worktree/index/common-dir、C盘备份和真实数据。

仅允许从以下两个固定旧scratch中**精确只读最多12份普通小文件，总计原字节≤2MiB**，且必须从前一正式receipt/manifest的确切引用确定文件身份，不准泛目录遍历或递归搜索：
1. 前次证据交换失败scratch `D:\ProjectTemp\ch5_v010_current_seal_exchange_20261016_01` 的准确最终FAIL/receipt、当次PowerShell SOURCE_TIMESTAMP门脚本、静态日志中经匿名化的必要字段类别/前后证据（如果确实存在）。
2. 它所精确指向的前一次17/17集成封存scratch `D:\ProjectTemp\ch5_v010_integration_seal_mktree_20261016_01` 的最少first/final JSON真实原件、对应schema或manifest。无明确索引或出现敏感/private/redirected路径，STOP并记UNKNOWN，不自己猜文件名/另找目录。

每个旧文件读前核物理大小、普通路径/无reparse、字节预算与全文件SHA256；读后核相同hash，原字节**绝不改/移动/再封存**。旧原JSON timestamp的值只允许在**进程内存**中进行一次**非执行型字段诊断**，不得打印/写入原始值、完整JSON、原argv、源码行、私有绝对路径或错误原文。日志/新报告仅允许匿名file ID、字段/schema ID、JSON原始token种类、value长度/是否有显式时区、解析后安全.NET/Powershell类型**名称**、解析器名字/版本、命令分支/规则ID/原字节SHA256；如果类型名称也无法安全取得，写`UNKNOWN`。

## 2. Gate T：实际类型与语义根因取证，不先决定结论

必须来自**上一失败脚本和原真实JSON**，以真实源码锚点取证：
- 原脚本是哪种JSON解析器、PowerShell版本、参数/配置、引用哪个确切字段、在哪一步判断`[string]`或字符串，以及判断是对原始JSON lexical token还是转换后的对象。把`SOURCE_TIMESTAMP`解释为原工程守门器标签，不凭标签猜JSON键名。
- 不修改原raw的前提下，用经认证且受控的**同类解析调用**最多1次读取被阻断的**同一字段**，记录`RAW_JSON_TOKEN_KIND`（如string/number/null/object/array/missing）、`PARSED_VALUE_TYPE_NAME`（安全完整类型名，如System.DateTime、System.String、其他或UNKNOWN）、时间戳是否可依据原合约做合法时间语义校验、是否是PowerShell/解析器自动类型转换。不得因某解析器可能隐式转换就提前写`DATE_CONVERSION_ROOT_CAUSE_CONFIRMED`。
- 保留原字符串格式、时区偏移与小数精度的相关**匿名语义属性**；不能通过直接`ToString()`或本机文化区/当前时区转换然后声称与原timestamp等价。必须有可靠的原始JSON token读取手段（例如环境实际提供的JSON词法/token API；可用内置.NET库但版本需取证）；如果工具只能得到已经转换的日期对象而不可恢复原始token/偏移，则记`RAW_TOKEN_UNVERIFIABLE / FAIL_CLOSED`，不得松门通过。
- 对合法性根据**读取到的冻结旧schema与原守门源码**定标准；不擅自把“任何可解析DateTime”全部接受，不擅自新增科研语义/结果时间戳。区分`SCRIPT_TYPE_ASSUMPTION_DEFECT_CONFIRMED`、`ORIGINAL_JSON_SCHEMA_VIOLATION_CONFIRMED`、`PARSER_BEHAVIOR_UNRESOLVED`与`NOT_EVALUATED`，每项必须有来源和证据等级。

## 3. Gate F：一次集中修复（仅新scratch副本）与合成回归

不触原旧脚本，在新scratch基于来源可信的门片段实现**独立可用的修正版timestamp校验函数**。不可只取消`[string]`门、无条件转换、降低脱敏拦截或`try/catch`吞错。最小修复应在**原始JSON token为string**且满足原冻结时间格式/日期/时区要求时，接受解析器可能返回的受支持类型；如是DateTime/DateTimeOffset，必须从可信**raw lexical token**和不损失offset/precision的语义判定交叉核对。解析器自动转换是需要证据验证的候选机制，不是已确认结论。

**合成回归至少12项，需逐例case ID、expected、observed、runner退出码及安全归因**，只造非敏感的模拟JSON/时间值：
- 合约允许的UTC`Z`、显式正/负时区偏移、合约允许的小数秒；即使解析为对象也不能丢原时间表示的意义。
- 原类型假设可能导致误拒的安全模拟输入；不允许利用强制字符串转换救PASS。
- 合约不允许的无时区日期、日期不存在/闰日、非法offset、非日期字符串、空值与missing字段；数值/布尔、array/object、重复键、过度嵌套等负例至少覆盖。**如果冻结旧schema事实上允许某一形态，则按原schema作为oracle，不能凭任务例子制造新合约；如原schema未规定，标`SPEC_UNRESOLVED`，不擅自将测试标PASS。**
- 同一值在旧/新解析方式下的原raw token与转换后的类型差异、JSON roundtrip是否改offset/精度；不可通过覆盖原source或采集真实字段原文来建fixture。
- 无效/模糊日期必须`DENY`，意外异常必须`FAIL_CLOSED`；不得把所有case“未执行”或只断言退出0计成12/12。

**一次针对上一实际原timestamp字段的修正版只读校验**允许在Gate T取得合法类型与原格式证据且未触坏任何硬门后进行，仍只检查本地时序schema，不调用脱敏发布器、不把源文件改写或上传。如果原raw合法，可报`SOURCE_TIMESTAMP_REAL_INPUT_LOCAL_RECHECK=CODEX_REPORTED_PASS`；如果原raw非法则`CONFIRMED_SCHEMA_MISMATCH`；实际字段/规则不明则`UNKNOWN`。合成PASS不能替代这一真实字段检查，更不能自动解锁GitHub发布。

## 4. 独立新资源、输出、停止点

- **新PowerShell受界测试/诊断批次最多2个**（可在批次内完成静态检查与合成fixture验证，失败/异常仍消耗，不借子脚本/别名/另起PowerShell重置）；每批有显式计时、进程/日志/文件bytes上限。Gate T的旧原timestamp非执行型诊断最多1次、Gate F的修正后同字段只读复核最多1次，只可在上述已计费批次里完成。
- 总wall≤**120分钟**；旧scratch累计精确只读≤12文件/2MiB；新scratch**最多6份平铺非Git UTF-8/LF文件，总物理新增≤1MiB**，其中先预留失败和最终回执≥128KiB；无大日志、旧source拷贝、未授权私有材料。建议固定新文件 `timestamp_guard.ps1`、`synthetic_cases.json`、`result.md`、`manifest.json`、`FIRST_RECEIPT.json`、`FINAL_RECEIPT.json`；先验证使用字段均已完全匿名/安全，不将源文件原字节嵌入这些物。
- **Git commands 0（含git init/bare/mktree/hash-object/fetch/push/commit/ref）**；**SSH、GitHub review发布、远端临时目录创建0**；**Python/py/pytest/Jupyter、模型源码load/import、VerifiedLoader、真实runner、HA/HJB/KFE/selector/roots/GE/IRF/MATLAB/真实C8全部0**。不重跑旧17/17或20/20，不另做E0、更不续用上一STOP静态1/2、fetch/push 0/1等未用余额。未来证据交换若要发布必须另有Owner新的固定任务、独立review分支/sole parent/白名单/SSH443预算。
- 交付必须区分`SOURCE_PARSER_AND_VERSION`、`RAW_TOKEN_KIND`、`PARSED_ACTUAL_TYPE`、`STATIC_CAUSE`、`SYNTHETIC_CASE_PASS_COUNT`、`REAL_FIELD_RECHECK`、`ORIGINAL_RAW_MODIFIED=FALSE`、`SANITIZER_NOT_RUN`、`GITHUB_PUBLICATION_NOT_AUTHORIZED`、`SCIENCE_NOT_RUN`、逐项真实资源与文件SHA和所有UNKNOWN。旧失败receipt保存，不清理、stash、reset、重写以消除历史缺口。本轮新first/final必须从创建开始保持raw实体、同run-id与单向hash链接；不能借本轮新seal修复上一旧封存链。
- 新任务完成后只返回**≤4KiB严格脱敏摘要**，本地raw哈希注明`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，待Astra独立限域审查；任何关键负例异常、真实raw token不可验证、原脚本未取得、旧原件SHA不一致或资源超限，立即`FAIL_CLOSED / LOCAL_ONLY`并停在`WAIT_ASTRA_V010_SOURCE_TIMESTAMP_TYPED_CORRECTION_REVIEW / STOP`，不自动重试、变更冻结任务或重启Git发布。

## 5. 永久科学/Owner保护

修正原MATLAB具体错误、继承两资产HA/HJB/KFE、跨省手动有界顺序、GovInv收益边界×0.9/×1.1及Zt、GDP冻结各省误差≤1%独立目标、原lagged-NKPC递推；目的地工资税只扣一次、家户人均/省财政总量与三劳动账、same-S/前完整轮raw ra0、phi_max=.3、20×20×2原网格、已采纳数值阈值不可改。不得引入Newton、Bt=Bgov、固定公共资本残差律、内生T或伪Results。

原受保护`D:\ProjectTemp\c5k1bturn56`及8 dirty/index/staged/untracked/ignored/外Git common-dir，所有旧失败scratch、C盘独立SSD既有备份、真实C8/2017/2018/B3、V009失败数组均不触写、不清理、不checkout、不复制原argv/raw日志。Owner C盘+GitHub现有备份、已有SSH Key/443及可信工作站风险决定保持（本任务没有网络Git许可），不强制VM或第三备份；远端`_review_tmp/ch5/<task-id>/`只准在另授权的独立GitHub review tree，绝不进入本地科研/治理/model worktree/index。

**持续：`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`real C8 A–D REQUEST_ONLY`、`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`model_activation=False`、`Results FALSE`、`V011 NOT_STARTED`。**
