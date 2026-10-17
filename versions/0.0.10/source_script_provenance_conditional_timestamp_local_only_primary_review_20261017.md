# V010 来源身份恢复及条件式SOURCE_TIMESTAMP修正：独立限域主审

**主审日期：**2026-10-17（Asia/Shanghai）。  
**唯一冻结任务：** `V010_SOURCE_SCRIPT_PROVENANCE_RECOVERY_AND_CONDITIONAL_TIMESTAMP_FIX`。  
**正式任务发行Commit：** `fafffe0582a213ceec25312f97f47ade6f1aa508`。  
**固定任务Git Blob：** `22aea7c18716c36ffb1f3154d35d751d9f524bf1`。  
**交付ID：** `V010_SOURCE_SCRIPT_PROVENANCE_RECOVERY_CONDITIONAL_TIMESTAMP_FIX_RESULT`。  
**正式主审分类：** `SOURCE_PROVENANCE_PRESENT_DAY_CORROBORATED_CODEX_REPORTED__HISTORICAL_EXECUTED_BYTES_UNVERIFIED__CURRENT_PS_7_6_6_TYPED_COERCION_CODEX_REPORTED__SYNTHETIC_24_OF_25_EXPECTED_MATCH_1_SPEC_UNRESOLVED__DOCUMENTARY_LIMITED_ACCEPT__NO_GITHUB_OR_SCIENCE`。  
**原任务终态：** `DELIVERED__STOPPED`；`ACTIVE_TASK=NONE`；全部旧/新未用运行额度封闭。  
**下一停点：** `WAIT_OWNER_FRESH_V010_TIMESTAMP_SPEC_BOUNDARY_AND_EVIDENCE_EXCHANGE_AUTHORITY / STOP`；本次正式验收不给新Python/真实runner/HA或远端Git发布权限。

## 1. 独立取得的GitHub身份事实

Astra通过已连接GitHub工具，按发行Commit完整读取`versions/0.0.10/source_script_provenance_recovery_conditional_timestamp_fix_task_20261017.md`，Git Blob确切为`22aea7c18716c36ffb1f3154d35d751d9f524bf1`。本次主审前`migration/astra-workflow-20261012` live HEAD `61ac59380e91ea2b57382a0fb8d52681f77615bf`；对上一状态比较`identical`（ahead0/behind0）；CURRENT/TASK_CURRENT当时仍标本次任务ACTIVE。GitHub搜索本任务相关review分支及旧`v010-current-seal-evidence`分支均无返回；本任务本来`GIT=0/SSH=0/GITHUB_PUBLISH=0`，无需新review候选清理。

**独立核验界限：** Astra只核对了任务及远端治理信息，**没有**读取本机三旧scratch元数据、当次PowerShell 7.6.6运行环境、被认证脚本全文件实际字节、原JSON原token、25项单例回执、新first/final原字节、时间/读账。因此以下所有本地哈希、路径调用匹配、时间语义、17/25测试身份和消费数属于`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`；不写`ASTRA_WINDOWS_RUNTIME_INDEPENDENT_PASS`或`REMOTE_RAW_SOURCE_VERIFIED`。

本轮最终receipt SHA256由Owner转述：`B37FA71992497C299D2E218029D08AD1F863A83A6F6C60C852342C82EB0430B0`。未收到本机receipt原字节，**尚未独立重算**。

## 2. 分门科学与工程裁决

### Gate R——恢复了现时的来源索引，但不是历史原字节身份认证

Codex报告从既有执行调用证据与匹配的旧失败receipt定位了守门脚本的精确身份、**当前**全文件SHA256和SOURCE_TIMESTAMP字段/schema锚点，并明确提示历史源代码hash未记录。依本任务允许的额外R1/R2/R3三根非递归metadata盘点，新一次`authorized_locator+current_whole_file_hash+field_schema_anchor`的本地取证比空`sourceIndex`有实质改进。

**分类：** `SOURCE_IDENTITY_CURRENT_LOCAL_CORROBORATED=CODEX_REPORTED`、`HISTORICAL_SOURCE_HASH_NOT_RECORDED=TRUE`、`HISTORICAL_EXECUTED_BYTES_UNVERIFIED=TRUE`。当下SHA256不能追溯证明历史执行瞬间文件字节与现时完全相同，也不能被导出成上轮缺失的sourceIndex当时已经存在。网页未取得对应文件，故本Gate仅**有限接受本机来源定位及hash报告**，不给历史执行同字节PASS。

### Gate T——本次解析转换机制已报告复现；历史环境未认证

Codex给出**本轮**实际字段原JSON token为String，PowerShell 7.6.6解析后的.NET类型为`System.DateTime`（Utc）；旧脚本要求解析后仍为string，因此当前执行类型守门拒绝。其原字符串符合旧schema的`Z`后缀和日期合同（仅Codex本地核证），说明当前有依据认为这是**合法原JSON token与解析后对象类型混用引起的误拒**。

分账：
- `RAW_TOKEN_KIND=String (CODEX_REPORTED)`；
- `CURRENT_PARSER_RUNTIME=PowerShell 7.6.6 (CODEX_REPORTED)`；
- `CURRENT_PARSED_TYPE=System.DateTime / Utc (CODEX_REPORTED)`；
- `CURRENT_TYPE_ASSUMPTION_DEFECT=LOCALLY_CORROBORATED`；
- `HISTORICAL_RUNTIME_VERSION=UNKNOWN`；
- `HISTORICAL_EXECUTED_BYTES_IDENTITY=UNVERIFIED`，故历史某次失败的**精确环境/字节因果重放**仍无完全证据。

这既不能宣称原时间戳无效，也不能宣称PS7.6.6的转换行为必然代表所有旧PS版本。不得更改源first/final或旧失败回执去消除历史缺失。

### Gate F——24项符合预期、1项仍无权威精度规范

Codex报告25项**新**合成用例，24项预期匹配，1项关于此前合同**没有规定的高精度时间形态**被正确标`SPEC_UNRESOLVED`，**没有计入PASS**。一次原字段修正版只读检查按本机报告通过，原文件SHA256不变；这些仅是新scratch修复版本的结果，不表示历史守门脚本被修改，也不意味未来所有序列化器形态获得验证。

`SYNTHETIC_OBSERVED_PASS=24`、`SYNTHETIC_TOTAL=25`、`SYNTHETIC_SPEC_UNRESOLVED=1`。**分类：`PARTIAL_SYNTHETIC_ACCEPT_WITH_SPEC_BOUNDARY`，非25/25完全合格。** 不允许擅自放宽日期精度、补出高精度accepted规则或把未定义形态算失败事实；该项须在未来Owner认可的旧schema证据下解决，必要时由Owner明示新的技术格式上界。没有复核到逐项原运行文件，不能将24/25变成网页亲自执行的结果。

`REAL_ORIGINAL_TIMESTAMP_FIELD_LOCAL_RECHECK=CODEX_REPORTED_PASS`；`ORIGINAL_SOURCE_RAW_HASH_REPORTED_UNCHANGED`，不表示整个旧发布安全验证或GitHub raw bytes已经完成。

## 3. 执行账与两代封存

Codex本次自报如下：

| 资源 | 本任务本地实际与上限 | 审议 |
| --- | --- | --- |
| PowerShell受界批次 | **2/2** | 新预算全部消耗 |
| 旧root metadata inventory | **3根各1次，4/4/9个条目** | 均在每根≤12上限；metadata盘点不能替代文件实际内容的授权 |
| 旧source文件 | **6个distinct、共14次读取、累计95,510B** | 小于≤12份/2MiB；件数与读次数分别记账 |
| 新scratch新增 | **7份文件，总47,844B** | 低于8份/1MiB；写前预留128KiB过程、wall时长与其它逐项元数据未独立核 |
| 修复后合成测试 | 25项，24按预期、1`SPEC_UNRESOLVED` | 不允许计25/25 PASS |
| 实际原字段只读复核 | 1次、获准（Codex报告） | 原raw hash据报未变 |
| Git/SSH/fetch/push/Python/VerifiedLoader/真实runner/模型科学 | 全部0 | 无远端candidate、无模型科学资格 |

本轮真实first/final失败或交付receipt据Codex均保留，同`run_id`、单向哈希链接，但两份文件及其可复算字节尚未传送给Astra。新回执只能证明**本轮**的封存方法，不允许修复B/S/L旧20项任务永缺raw first/旧run_id的`LEGACY_SEAL_CHAIN_UNVERIFIABLE`。

源工程17/17合成和新seal仍是本机reported，未获GitHub远端独立raw审查；最早原sanitize拒绝的命中文件/字段/规则/次数仍UNKNOWN，被拒旧候选`PUBLICATION_DENIED`；历史中间ledger复制raw argv/源码的过程偏差仍`UNRESOLVED`。

本轮**全部未用额度及以前所有已STOP预算闭合、不结转**；本审议没有新授权使用另一个版本PowerShell、重跑旧25例、GitHub发布或HA科研。

## 4. 永续科学合同与工程下一门

冻结V010计划：commit `bf091da33d59293f147d52c11580327d3ac2a85d`/Blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；模型候选commit `94de4501dec051b969bee9d852eba2d4591f30ef`/tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`均不更改。原MATLAB纠错主线：corrected两资产HA/HJB/KFE→跨省顺序单轮→GovInv原收益边界乘0.9/1.1与自适应Zt→冻结GDP每省目标误差≤1%独立回读→原lagged-NKPC递推；目的地工资税只扣一次、same-S/前完整轮lagged raw ra0、家庭人均/省财政总量与三劳动账、phi_max=.3、20×20×2网格/数值阈值全冻结。Owner corrected单点`rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07`仍UNTESTED。

Owner已有独立C盘SSD备份+GitHub备份、可信工作站和SSH Key/443风险决定有效，不强制VM或第三备份。原受保护`D:\ProjectTemp\c5k1bturn56`八dirty/index/staged/untracked/ignored、外Git common-dir、C备份、全部旧失败raw与真实C8/2017/2018/B3、V009数组保持不可触写；远端`_review_tmp/ch5/<task-id>/`只能在Owner另批独立GitHub review tree中出现，不落本地项目worktree/index。

继续`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`model_activation=False`、`Results FALSE`、`V011 NOT_STARTED`、`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`real C8 A–D REQUEST_ONLY`。

**合理后继（建议，不自动签发）**：优先做一轮`CURRENT_SEAL_SANITIZED_EVIDENCE_PUBLICATION_WITH_TYPED_GUARD`的新单独授权，**只针对原raw已报告合法、未定高精度形态明确DENY或保持UNKNOWN、不放宽任何脱敏约束**；提交当前first/final或安全衍生投影、24通过/1待定及对应source现时/历史证据等级供Astra独立GitHub核验，再进一步独立提出可信Windows import/runner门和HA科学许可。下一任务具体sole parent/ref/四文件白名单/SSH443限额必须另冻并Owner新批；更早被拒候选永远不因新合成修复而自动解封。若需要高精度格式纳入支持范围，先取得旧schema权威或Owner新明确采纳，不改写历史格式。
