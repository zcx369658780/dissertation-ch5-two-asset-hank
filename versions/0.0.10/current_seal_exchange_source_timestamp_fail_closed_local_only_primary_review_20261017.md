# V010 当前seal脱敏GitHub证据交换：SOURCE_TIMESTAMP提前STOP的独立限域主审

**主审日期：2026-10-17（Asia/Shanghai）**  
**交付报告ID：** `V010_CURRENT_SEAL_SANITIZED_GITHUB_EVIDENCE_EXCHANGE_RESULT`  
**原冻结任务：** `V010_CURRENT_SEAL_SANITIZED_GITHUB_EVIDENCE_EXCHANGE`  
**任务发行Commit：** `49ff1c3053fa1aa6a0646f55abcffb077e2b62b2`  
**任务Git Blob：** `1dc5f07a88261c41de434a9c4075b0d179ee871a`  
**交付终态与正式审议：** `FAIL_CLOSED__LOCAL_ONLY__SOURCE_TIMESTAMP_PARSED_TYPE_GUARD_REJECTED__NO_REMOTE_CANDIDATE__LOCAL_RAW_EVIDENCE_UNVERIFIED`。  
**任务状态：** `DELIVERED__STOPPED`、`ACTIVE_TASK=NONE`，无新运行许可。  
**下一权限停点：** `WAIT_OWNER_FRESH_V010_SOURCE_TIMESTAMP_TYPED_DIAGNOSTIC_AUTHORITY / STOP`。任何后继源码修正、静态类型实验或发布重试必须单独冻结新预算，原本次1/2剩额随STOP关闭。

## 1. GitHub实际独立核验

Astra通过已连接GitHub工具核实仓库 `zcx369658780/dissertation-ch5-two-asset-hank`，治理分支 `migration/astra-workflow-20261012`。在审议前，该分支HEAD为 `9b9bcc3aa284a4674fd59b697813c45680be7122`，与上一轮治理终态比较为`identical`（ahead0、behind0），动态CURRENT/TASK_CURRENT仍标上一任务ACTIVE；本正式主审将其变更为STOP/NONE。

按正式任务发行commit读取全文，Git Blob实查与 `1dc5f07a88261c41de434a9c4075b0d179ee871a`一致。任务明确要求先证明本轮已有first/final与17项合成工程证据来源、通过严格脱敏，才可能在独立bare中以现有SSH Key/443一次受界fetch和一次non-force push发布至唯一review分支，不批准Python/runner/HA、旧候选重扫与额外重试。

目标远端审阅分支：
`review/ch5-temp-v010-current-seal-evidence-20261016`；
唯一远端tree路径：
`_review_tmp/ch5/v010-current-seal-evidence-20261016/`。

GitHub `search_branches`查询该分支后无匹配，且通过`fetch_file`尝试读取该ref下`result.md`和`manifest.json`均得404：`No commit found for the ref`。**独立可证：截至本次核查目标ref不存在，Astra没有可取的candidate commit/tree/四文件，亦没有本轮remote-only暂存物需要清理。** 远端不存在不能独立证明本机scratch内全部文件状态，后者保持Codex回执等级。

## 2. SOURCE_TIMESTAMP主审：失败存在，不推断时间戳无效

Owner转述Codex交付：前置准备在`SOURCE_TIMESTAMP`门停止；旧脚本要求JSON**解析后的**时间戳仍为字符串，这项判定为FALSE，**实际解析结果类型未记录**，脚本没有更改或重试。正式分账如下：

- `SOURCE_TIMESTAMP_GUARD=FAIL_CLOSED__CODEX_REPORTED`。
- `PARSED_TIMESTAMP_ACTUAL_TYPE=UNRECORDED/UNKNOWN`。
- `RAW_JSON_TIMESTAMP_VALIDITY=UNKNOWN`，不能认定原始时间戳不存在、错误、无效或不符合ISO格式。
- `PARSER_NAME_VERSION_AND_COERCION_BEHAVIOR=UNKNOWN`，不能将未读取的PowerShell/JSON脚本假定为某一解析器、某一类型自动转换行为，更不能声称已证实真正根因。
- `SANITIZER_SCAN=NOT_RUN`；`PUBLISHED_SAFETY=NOT_PROVEN`；`RAW_EXACT_OR_DERIVATIVE=NOT_DETERMINED`。
- `BARE_GIT_CREATE/SSH/FETCH/PUSH=0`，`CANDIDATE_COMMIT/TREE/FOUR_BLOBS=N/A`。

**合规结论：**在来源前置失败后不修正、不重试、不试图跳过守门、不上传候选，符合本次冻结FAIL_CLOSED/LOCAL_ONLY规则。一次本地类型检查的失败仅属于**证据交换脚本/序列化契约待取证**，不是前轮合成测试失效、JSON原件无效、科学模型错误或GitHub发布认证故障的证明。

## 3. 前轮本地正向证据分级不升格

Codex称本次准备阶段已经核前一轮终版receipt SHA256，核first/final哈希引用、相同run_id和17项结果关联，尚未进入安全扫描；本次**原本地文件未交给Astra**，故这些仍是`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，不能写`ASTRA_INDEPENDENTLY_VERIFIED_SEAL_RAW_BYTES`。本次`SOURCE_TIMESTAMP`早停也不能反向推翻前轮17/17合成集成，或把旧seal与新seal混为一个run。

上一轮新集成固定主审：
`versions/0.0.10/engineering_integration_seal_chain_synthetic_mktree_local_only_primary_review_20261016.md`，Git Blob `32272533e9f4136883f536814919bddf2cb037d9`。前前轮B/S/L20/20的**旧first seal没有可还原原始字节、旧run_id未记录**，`LEGACY_SEAL_CHAIN=UNVERIFIABLE`永久保留、不追溯补造。本轮准备失败后，本次尚无GitHub远端可独立验的新seal。原旧脱敏候选`PUBLICATION_DENIED`，首次命中详细原因`UNKNOWN`；历史曾复制原argv与短源码的中间台账偏差`UNRESOLVED`，两者均未关闭。

## 4. 预算与留存

Codex本轮报告：

- PowerShell静态准备批次：`1/2`；本轮STOP以后剩余`1`关闭、不结转。
- 上轮已封存文件读取：**5份，43,468 B**，小于冻结的8份/1MiB，但原始路径/逐项hash没有通过远端提交，仍属本地摘要。
- 脱敏扫描、bare创建、SSH、Git fetch、push：**0**。实际PowerShell解析类型和原始错误上下文未记录，不能自行补写。
- 上次17项合成/之前20项合成重跑、Python/model import/VerifiedLoader、真实runner、HA/HJB/KFE、selector、root、GE、IRF、MATLAB、真实C8、科学计算：全部**0**（Codex摘要级）。
- 本次产生的新物理文件数量/总字节、wall、逐次PowerShell出入码等：本轮摘要**未列出/UNKNOWN**，不可臆填通过。
- 原失败回执已据Codex保留原字节，其SHA256由Owner转述：
  `F93DA4C6BEE0E62F68A04620B8BF372AD60275C20DEA7782EF2C56E4BFADA6FC`；
  **未提供文件原字节给Astra，未独立复算/认证该SHA256**。

上一轮及更早一切STOP预算、Windows/GBK异常产物与科学账保持，不借工程发布任务恢复旧权限。

## 5. 科学合同及后续建议

冻结V010科学计划Commit `bf091da33d59293f147d52c11580327d3ac2a85d` / Blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；模型Commit `94de4501dec051b969bee9d852eba2d4591f30ef` / Tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`未改。主线纠正原MATLAB两资产HA/HJB/KFE→多省有界顺序→GovInv收益率边界×0.9/1.1/Zt→GDP目标冻结后各省≤1%独立验证→lagged-NKPC原递推；目的地税一次、same-S和上一完整轮raw ra0、家庭人均/省总量/三劳动账、phi_max=.3、20×20×2及原数值资格仍冻结。Owner新corrected HA单点 `rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07` 仍UNTESTED，`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`model_activation=False`、`Results FALSE`、`V011 NOT_STARTED`。

Owner已有C盘物理独立SSD备份＋GitHub备份，不要求第三备份/VM；既有SSH Key/443只允许未来特定新授权使用，本轮没有网络操作。原受保护`D:\ProjectTemp\c5k1bturn56`之8 dirty tracked、staged/index、untracked/ignored、外Git common-dir、所有失败本机scratch、C备份、真实C8/2017/2018/B3与V009错误数组不可触写；远端`_review_tmp`仅可位于另批独立review tree，不能进入本地研究/治理worktree/index。原`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`real C8 A–D REQUEST_ONLY`继续生效。

**下一步仅建议，尚未签发：** Owner若新授权，应先对**实际SOURCE_TIMESTAMP guard源码、解析器版本、parse前原始JSON token种类、parse后安全type名称、规范化时区/日期类型判断**进行受界最小静态取证；区分合法时间戳被解析器转型与真实原件schema错误。仅在新独占scratch、合成fixture中验证严格但正确的类型/时间语义门，所有原first/final与失败回执只读、不改/不重试既停发布任务；诊断通过后如仍需GitHub审阅，须再另发专用新发布预算。避免绕过安全要求或无证据把`SOURCE_TIMESTAMP`标PASS。

**终态：`V010_CURRENT_SEAL_EXCHANGE_FAIL_CLOSED_LOCAL_ONLY_SOURCE_TIMESTAMP_TYPE_UNOBSERVED__GITHUB_CANDIDATE_NONE__NO_NEW_PYTHON_OR_SCIENCE`。**
