# V010 来源脚本身份恢复与条件式 SOURCE_TIMESTAMP 修复：单轮集中任务

**唯一任务ID：V010_SOURCE_SCRIPT_PROVENANCE_RECOVERY_AND_CONDITIONAL_TIMESTAMP_FIX**
**版本：V010 / V0.0.10；性质：BOUNDED_SOURCE_PROVENANCE_RECOVERY + CONDITIONAL_ENGINEERING_ONLY_TIMESTAMP_FIX**
**Owner明确新授权：2026-10-17，同意有界来源身份恢复＋条件式时间戳修复。不得理解成前次失败任务重试、脱敏发布权限或科学运行许可。**
**结果ID：V010_SOURCE_SCRIPT_PROVENANCE_RECOVERY_CONDITIONAL_TIMESTAMP_FIX_RESULT**
**STOP：WAIT_ASTRA_V010_SOURCE_PROVENANCE_CONDITIONAL_TIMESTAMP_REVIEW / STOP**
**首次发行Commit及Git Blob由后续TASK_CURRENT登记；本正文首次发行后冻结不得修改。**

## 0. 固定权威、证据分类与前次缺口

1. 只以仓库 zcx369658780/dissertation-ch5-two-asset-hank 的 governance 分支 migration/astra-workflow-20261012 为当前管理权威，不以main替代。执行前从**本任务发行固定commit**读取全文并验证Git Blob，动态只读核 docs/DOC_INDEX_CURRENT.md、CURRENT.md、TASK_CURRENT.md、docs/CH5_VERSION_REGISTER_CURRENT.md、V1.2、Owner备份/SSH/Loader决定和remote-only临时审阅协议。
2. 上一已STOP任务 V010_SOURCE_TIMESTAMP_TYPED_GUARD_CORRECTION_AND_SYNTHETIC_REGRESSION，发行commit 6dfe8a1c98a839f0a94cdd0e938bb6b60f99d520，任务Blob 68143e917df883e38fa4615ce0a7c7a86c797330；最新正式主审 versions/0.0.10/source_timestamp_typed_guard_source_index_missing_fail_closed_local_only_primary_review_20261017.md，Blob 5b4a63f453fc472cc90869ca9e029c7657757caf，独立确认冻结任务Git身份，Codex自报旧manifest的sourceIndex为空，所以按“无索引STOP”。此事**不能证明脚本丢失或原timestamp有错**。最近失败receipt SHA256据Owner为1E9A02F1C9AF59FAB80BED91E39353EB4CCBD87884D46C229D3E9C44610846BC，Astra没有本机原字节核验。
3. 上上轮SOURCE_TIMESTAMP失败，解析后是否为string的判断不成立，但实际JSON原token、解析后的.NET类型、parser/PS版本、源脚本身份都尚UNKNOWN；原旧sanitizer被拒材料仍PUBLICATION_DENIED/原因UNKNOWN，历史旧中间ledger曾复制raw argv/源码的偏差UNRESOLVED。更早B/S/L20旧first封存无可还原raw和run_id，永久LEGACY_SEAL_CHAIN_UNVERIFIABLE，不补造。17/17集成、新first/final仍只是CODEX_REPORTED_WITH_LOCAL_RECEIPTS。
4. V010冻结科学plan commit bf091da33d59293f147d52c11580327d3ac2a85d / Blob 85138d8859d53295262fe13bf5bc277bca95ed3f，冻结模型commit 94de4501dec051b969bee9d852eba2d4591f30ef / tree 205eab47c4e4f9c6292c2ead9947d94d1a7579a5不改、不导入；Owner给定corrected HA单点未运行。任务不得以证据交换缺口开展新宏观建模、迁移或科学实验。

## 1. Gate R：新授权的**精确受限文件身份恢复**，不要循环依赖空sourceIndex

唯一新项目外可写scratch：D:\ProjectTemp\ch5_v010_source_provenance_conditional_20261017_01。创建前核不存在、路径祖先和最终目标不为reparse/junction/symlink/UNC/ADS/被保护目录别名，必要判断无法证明即FAIL_CLOSED。所有历史scratch、原模型/治理worktree/index、外Git common-dir与C SSD备份**仅按本节允许只读，不改一个字节**。

新Owner允许一次**与旧空sourceIndex不同的明确受界来源寻找方式**，且只限以下三处以前已有任务的**根目录的直接子项元数据（depth=0）**：
- R1：D:\ProjectTemp\ch5_v010_current_seal_exchange_20261016_01（先前实际触发SOURCE_TIMESTAMP的交换任务）。
- R2：D:\ProjectTemp\ch5_v010_source_timestamp_typed_20261017_01（刚STOP的追索任务）。
- R3：D:\ProjectTemp\ch5_v010_integration_seal_mktree_20261016_01（前序有17项集成和first/final的任务）。

对R1–R3每个根**最多一次非递归metadata inventory**，每根最多12个直接普通文件候选；只允许收集匿名文件ID、扩展名/长度/是否reparse及是否存在，不能打印绝对用户路径或原文件内容，不可递归/对其他路径搜索、遍历model repo/C8/整个D盘。某根超过12个直接子项、文件名/类型异常、出现无法校验的外链，一律停止该根扫描并标UNKNOWN，不扩展预算。metadata listing**不是**对其中所有文件的内容读取授权。

允许内容只读的条件：首先读取这三处已有任务中**精确已知名称**的本轮允许文件（如 DELIVERY_RECEIPT.json、FINAL_STOP.md、result.md、manifest.json、FIRST_RECEIPT.json、FINAL_RECEIPT.json；任一实际不存在就记UNKNOWN，不造文件），再选择**唯一明确在既有调用/manifest/源任务回执中被指明与SOURCE_TIMESTAMP失败实际相关的PowerShell脚本候选**（*.ps1）或已完整封存的原命令脚本文本对象；严格禁止仅凭文件名像guard、恰好出现SOURCE_TIMESTAMP字串就认定其为当次已运行源码。一个候选若无可认证执行出处，不能仅凭新计算SHA就冒充历史原脚本。

精确内容预算：最多**12个不同旧文件**，每个多次读取均计入实际字节，总实际读取≤2MiB；每个文件先核大小、类型/无reparse/文件访问范围，读取前后计算**全文件SHA256**并确认内容未漂移。历史raw源码/argv/日志只能在受控内存中静态审视必要条件，不得复制源码整文件或错误原文到新scratch、console或GitHub。

来源恢复必须产生三项**可核证**身份：
(1) AUTHORIZED_SOURCE_LOCATOR：精确受界根＋相对文件名、可对应到原任务当次调用或原回执的证据锚点，不是单纯“猜到一个同名文件”；
(2) WHOLE_FILE_SHA256：当下真实全文件hash/字节长度，若过去没有同时记录源码hash，必须如实写 HISTORICAL_SOURCE_HASH_NOT_RECORDED，不称历史原字节已证明；
(3) FIELD_SCHEMA_ANCHOR：真正SOURCE_TIMESTAMP guard语义/源JSON字段与schema的确切只读锚点，来自已找到且经过身份验证的源码/旧schema，不靠猜键名。

如果**找不到当次实际执行的脚本或其完整原文**，或找不到原调用与该script的可靠绑定，或schema/字段锚点欠缺，必须报告 SOURCE_PROVENANCE_UNRECOVERABLE 或 SOURCE_EXECUTION_BINDING_UNVERIFIED，并**停止Gate T/F**；可以交付Gate R得到的有界元数据，但不得临时重建一份“看起来相同”的旧脚本冒充真实来源。若源程序原本只以内联命令临时执行且无原字节留存，明确 IMMUTABLE_SCRIPT_BYTES_MISSING；禁止把GitHub冻结任务自然语言说明视为旧源script全字节认证。

## 2. Gate T（只在R三元身份可证明时）：实际parser与时间token类型

从唯一已认证源脚本+schema检其PowerShell/解析器及准确版本、实际原JSON字段引用和字符串类型断言；按上述内容只读预算，最少一次（最多一次）非模型纯静态字段读取/类型探针，保留**JSON lexical token种类**、实际解析后的安全.NET类型名称、是否有offset/精度的非值性质、解析器版本/文化及时区影响的可核事实。不能记录raw timestamp值、原argv、包含真实私有路径的异常，不能先验认定PowerShell ConvertFrom-Json会转换DateTime。若从现有环境无法保留token及原时区精度，标RAW_TOKEN_UNVERIFIABLE/STOP。分类 SCRIPT_TYPE_ASSUMPTION_DEFECT_CORROBORATED、SOURCE_SCHEMA_MISMATCH_CORROBORATED、PARSER_COERCION_UNKNOWN，而不是为结论挑原始字段。

## 3. Gate F（只在R和T合格、旧schema得到明确证据时）：一次性修复与回归

在**新scratch**编写可审的独立timestamp guard副本或静态代码差异草案，**不得修改历史失败脚本、原receipt、manifest、first/final或V010模型源**。语义门必须在原JSON lexical token满足冻结旧schema的日期格式/offset/日期有效性/精度条件时才允许解析器的string或有证明的DateTime/DateTimeOffset路径，不能简单删除string检查、无条件ToString/culture coercion、允许非字符串token或放松旧sanitizer。输入非法和歧义必须DENY，异常FAIL_CLOSED。

集中运行**至少12个纯合成、完全不敏感的timestamp JSON case**，逐例记录匿名case ID、预期、实际、Exit/异常类型与证据级别：UTC Z/显式正负offset/允许的小数秒、跨解析器类型变化的合法输入；无时区、错误日历/闰日、offset越界、非日期文本、number/bool/null/missing、array/object/duplicate key/嵌套过深及解析异常的负例。测试预期必须以认证旧schema为准：若旧schema没有某一格式的权威规定，记SPEC_UNRESOLVED，不把想当然的规则当PASS。正例不能丢offset或小数秒原语义。最多**一次**只读实际原字段修正版比较，结果标CODEX_REPORTED_LOCAL_ONLY，即使PASS也不能恢复旧证据交换的发布权限。

新guard/合成PASS只说明此新副本的有限修复，不证明前一任务当时执行的代码字节或原模型系统已经整体修复；若R只能证明现时source hash而没有历史hash，必须另列 HISTORICAL_EXECUTED_BYTES_UNVERIFIED，不升格旧会话证据。任一严格否定例unexpected ACCEPT=>FAIL_CLOSED，不补跑、改旧时间戳或修改冻结schema救PASS。

## 4. 新资源上限、交付与绝对STOP

- 单轮wall≤**150分钟**；仅新scratch平铺**最多8个UTF-8 LF非Git文件**（修复guard副本、合成fixture、匿名case结果、来源索引/manifest、result、first与final真实receipt等）新增总≤**1MiB**，必须写前预留≥**128KiB**最终/异常封存空间。除新scratch之外所有old directories完全只读。前述旧内容read≤12 distinct files、总实际字节≤2MiB；直接子项metadata非递归inventory仅R1–R3每根最多1次、每根最多12个。每次不可无界打印/stdout或创建新意外日志，预算耗尽STOP。
- PowerShell受界来源诊断/合成测试**最多2批**，每批启动前计费，无借子进程名义重置；当source身份未证明，T/F均0。一次旧真实字段只读类型诊断及一次修后复核仅在上述两批和总读取资源内，不以过往未用批次抵账。编写证明材料的静态文本生成不是新的科学任务。
- **Git/SSH/clone/fetch/push/mktree/commit/ref/review branch0**；**Python/py/pytest/VerifiedLoader/model import/真实runner/HA/HJB/KFE/selector/scalar roots/GE/IRF/MATLAB/real C8全部0**；不得重做前次17/17、20/20或 E0 阶段，不扫旧被拒sanitization候选，不启动V011、不触原论文Results。原8dirty/index/staged/untracked/ignored、外Git common-dir、C盘现有独立SSD备份和全部历史失败证据禁止触写。既有SSHKey/443为将来Owner授权保留，本轮不连接。
- 必须出具result.md+manifest.json+真实first/final receipt，列真实metadata enumeration次数、文件数/读取实际总bytes、源脚本三元身份证据、是否有历史hash、Gate R/T/F逐项PASS/FAIL_CLOSED/UNKNOWN/NOT_RUN，PowerShell批次数/退出、至少12例只计真实运行的case、异常/资源ledger及全部未运行对象。所有原件SHA注明CODEX_REPORTED_WITH_LOCAL_RECEIPTS；不得声称Astra已独立复算本机字节。新first/final从首次写入各自保留原始字节、同一个新run_id及单向链接，不得补造更旧first/run_id。
- 最终交付ID固定 V010_SOURCE_SCRIPT_PROVENANCE_RECOVERY_CONDITIONAL_TIMESTAMP_FIX_RESULT，回复≤4KiB严格脱敏短摘要、最终本机receipt SHA256和实际Gate状态，完成或失败统一 WAIT_ASTRA_V010_SOURCE_PROVENANCE_CONDITIONAL_TIMESTAMP_REVIEW / STOP。本轮全部余量一律关闭、不结转，**不自行延伸发布任务或科学权限**。

## 5. 永久科学和Owner边界

当前使命仅为修正原MATLAB具体bug、沿其两资产HA/HJB/KFE→省际顺序单轮→原GovInv收益率边界乘0.9/1.1及Zt→冻结GDP各省误差≤1%独立校准→lagged-NKPC原递推；目的地工资税一次、家庭人均/省财政总量/三劳动账、same-S/前完整轮raw ra0、phi_max=.3、原20×20×2网格/阈值保持不变。不引入Newton、Bt=Bgov、内生T、额外财政闭合或新IRF制度。纠错后首个corrected HA单点仍未运行。Owner双备份（物理独立C盘SSD既有备份+GitHub）、可信工作站工程隔离而不是原生OS sandbox；D:\ProjectTemp\c5k1bturn56 的8 dirty、index及external common-dir、原C备份与真实C8/2017/2018/B3、所有旧失败原证完全保护。

**持续标记：A16 FAIL_CLOSED；window UNACCEPTED；C9 PAUSED；CALL_LEDGER UNRESOLVED；real C8 A–D REQUEST_ONLY；FULL_RUNNER_IO_CLOSURE=BLOCKED；model_activation=False；Results FALSE；V011 NOT_STARTED。**
