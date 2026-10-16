# V010 B/S/L 三项集中 ENGINEERING_ONLY 合成工程交付：独立GitHub限域主审

**审议日期：2026-10-16（Asia/Shanghai）**  
**任务ID：** `V010_BARE_IDENTITY_SANITIZER_LEDGER_ENGINEERING_ONLY_CORRECTION`  
**正式任务发行Commit：** `2a252ec2627d9a1f48dcab0c1bab16cc6cf9d9fe`  
**冻结任务Blob：** `6c31d861a9e15f1b5956dfdfa7132a074bdb2e5e`  
**本轮结果ID：** `V010_BARE_IDENTITY_SANITIZER_LEDGER_ENGINEERING_CORRECTION_RESULT`  
**交付介质：** `LOCAL_ONLY`，没有授权或生成GitHub Codex candidate。  
**独立主审分类：** `ENGINEERING_SYNTHETIC_BSL_20_OF_20_CODEX_REPORTED__DOCUMENTARY_LIMITED_ACCEPT__FIRST_SEAL_SUMMARY_NULL_RESERVATION__LOCAL_RAW_BYTES_UNVERIFIED__NO_REAL_RUNNER_OR_PUBLICATION_PASS`  
**任务停点：** `DELIVERED__STOPPED`；`ACTIVE_TASK=NONE`；`WAIT_OWNER_FRESH_V010_ENGINEERING_INTEGRATION_AND_EVIDENCE_PUBLICATION_AUTHORITY / STOP`。本主审不自动发行后续工程、Python、HA或GitHub发布许可。

## 一、GitHub实际独立核验的依据

- 唯一仓库`zcx369658780/dissertation-ch5-two-asset-hank`，权威治理分支`migration/astra-workflow-20261012`。本主审前live HEAD为`f6bed4a0b31ec0f3e942cf5175efee4d04a6bedb`，与前轮最后归档HEAD比较`status=identical, ahead=0, behind=0`。GitHub连接器完整读取**固定发行Commit**下正式冻结任务`versions/0.0.10/bare_identity_sanitizer_ledger_engineering_correction_task_20261016.md`，Git Blob精确为`6c31d861a9e15f1b5956dfdfa7132a074bdb2e5e`；新任务正式允许PowerShell合成批次≤2、新scratch独立`git init --bare`≤1、此新bare的只读Git身份children≤4，除此之外没有新Git mktree/fetch/push、Python模型或真实runner/HA许可。
- GitHub `search_branches`使用`bare`检索未发现新候选分支；本任务**明确禁止**Codex创建GitHub候选或review发布，故无对应新远端候选可供源码/回执核验。该查询可描述本轮远端可见范围，**不代表证明所有可能命名的分支均绝对不存在**，亦不能证明本机状态。
- 本轮依据Owner转述Codex最终脱敏摘要，而**没有**得到本机修复PowerShell源码、20个case逐条expected/actual、真实运行stdout/stderr、first seal原始回执、corrected summary原始回执、manifest及Windows文件字节。网页主审没有直接运行Windows tests/哈希程序，所有本地工程成功、资源计数、存储与异常处理细节都归类为`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`。不能写成`ASTRA_INDEPENDENTLY_EXECUTED_ENGINEERING_PASS`。

## 二、三组工程测试分项审查

### B：bare Git身份与路径比较（报告8/8）

Codex表示修正Git正斜线与Windows反斜线在字面比较中的误拒，并以8个合成用例实际验证目录句柄身份、Git alternates、真实junction、路径混淆和错误上下文的拒绝，`B01–B08=8/8 EXPECTED_MATCH`。依正式任务，保持身份根与新bare common-dir彼此独立、可信句柄/目录检查及非共享对象约束，不能简单用文本replace删掉guard。**验收：`BARE_NORMALIZED_COMPARATOR_SYNTHETIC=CODEX_REPORTED_8_OF_8`；`BARE_NONSHARED_GUARD_SYNTHETIC=CODEX_REPORTED`。** 这支持从上一轮静态缺陷归因进入真实合成验证；但**没有**核实完整原任务bare对象库、旧错误Git发布链、所有parent/tree/blob可达性、环境污染防护或同用户恶意TOCTOU，不能称`BARE_GIT_PUBLISHING_IDENTITY_PASS`或`OS_NATIVE_SECURITY_SANDBOX_VERIFIED`。

### S：脱敏结构化诊断（报告8/8）

Codex表示`S01–S08=8/8 EXPECTED_MATCH`：允许无秘密的合法JSON转义；模拟凭据/私有字段被拒；诊断只记录匿名类别、规则和计数。**验收：`SANITIZER_STRUCTURED_DIAGNOSTICS_SYNTHETIC=CODEX_REPORTED_8_OF_8`**。原旧发布材料的脱敏拒绝现场**没有命中具体文件、字段、规则及次数**，故`ORIGINAL_SANITIZATION_DENIAL_CAUSE=UNKNOWN`、`ORIGINAL_REJECTED_MATERIAL_PUBLICATION=DENIED`，不能由新合成8/8反推旧候选的安全性或实际未泄露；本轮不批准原件重扫、外传或GitHub发布。

### L：新中间台账匿名写入（报告4/4）

Codex表示`L01–L04=4/4 EXPECTED_MATCH`，从首次写入即使用匿名typed schema，长异常、配额不足及真实写入拒绝均有测试证据。**验收：`LEDGER_NEW_PIPELINE_SYNTHETIC=CODEX_REPORTED_4_OF_4`**。此前旧取证任务曾在中间台账复制短源码行及原argv，历史偏差不因本轮新合成测试成功而消失；原旧回执/历史原件必须保留、不覆写、不清理、不得推送。分类保持`HISTORICAL_INTERMEDIATE_LEDGER_DEVIATION=UNRESOLVED`；最多认可新实现针对将来写入风险的限域合成证据。

**综合：** 20/20 是`CODEX_REPORTED_SYNTHETIC_EXPECTED_MATCH`，未核验到原脚本、合成用例实现或机器原回执；非完整runner、原bare、脱敏真材料/真实C8/科学数值的结果。

## 三、封存汇总空值与证据链保留

Codex明确报告：**首次封存汇总曾产生空值**；首版回执保留，后来**只修正资源汇总，未重跑测试**。这是应保留的披露，不应把第一次seal省略，不能通过覆盖或删除历史来制造“首次就完整PASS”的错觉。

- `FIRST_SEAL_SUMMARY_NULL=CODEX_REPORTED`；
- `FIRST_RECEIPT_RETAINED=CODEX_REPORTED`；
- `RESOURCE_SUMMARY_CORRECTED_WITHOUT_TEST_RERUN=CODEX_REPORTED`；
- `END_TO_END_SEAL_CHAIN_BYTE_AUTHENTICATED=NO/UNKNOWN`；
- `RUN_ID_CASE_MANIFEST_FIRST_FINAL_CROSS_CHECK=NOT_INDEPENDENTLY_VERIFIED`。

限域主审对**工程合成测试的报告**予以文档级有限接受，但对**封存回执完整性**不颁发PASS：首版空值、何字段为null、原因、首次与更正的文件SHA/时间、补正后是否只改变汇总、是否仍指向同一次测试Run和20项原始证据，均未从本机原始文件查验。将来如要提高到工程集成PASS，应在新独立、明确资源授权下原样保留first receipt并仅审阅经去敏的first/final索引、关联哈希和run-id；不应为“修报告”擅自重跑或修改本轮冻结账。

## 四、实际预算、回执与未知项

Codex最终摘要报告（均非Astra本机亲验）：
- **PowerShell合成测试批次：1/2**；首批消耗不可重置，任务STOP后剩余`1`关闭，不结转。
- **全新合成bare初始化：1/1**；在任务内耗尽，后续不复用。
- **新bare只读Git身份子进程：4/4**，全部消耗。
- **精确旧文件只读：2份/16,826B**，低于任务最多10份、2MiB界。
- **新非Git文件：6份/58,657B**，数量到6/6上限、字节在2MiB内；若曾有临时/失败中间文件、写前128KiB预留账等，未获独立明细，**不得单凭最终6文件推断所有过程账均PASS**。
- **合成bare文件：130B（Codex回报）**；这不是被独立核实的bare仓库**全部物理元数据**大小。该数究竟仅文件内容、对象库、少数文件，是否含目录及隐藏/模板文件均`UNKNOWN`，不得宣称32MiB物理硬界完整认证。
- **Wall时间、原6件具体文件名/每件hash、前后seal关联身份、实际Windows进程输出、隔离守门原始证据：UNKNOWN**。
- **本轮最终`DELIVERY_RECEIPT.json` SHA256（Owner转述）：** `70622F5AF09089983639F81973837D7EF7D5E0CAA6B33E85D0C74B5B7EA74D23`，没有本机原字节可供本轮重新计算或确认。SHA256值本身不等于其文件在GitHub可取得或已经通过Astra认证。
- **未运行：**`E0_RETEST=0`、`MKTREE=0`、`GIT_FETCH/PUSH/PUBLICATION=0`、`PYTHON/MODEL_IMPORT/VERIFIED_LOADER/REAL_RUNNER=0`、`HA/HJB/KFE/SELECTOR/ROOT/GE/IRF/REAL_C8=0`，均据Codex结果陈述。不得把未运行的项目标为数值失败或科学PASS。
- 按任务`STOP`关闭所有未消耗预算，包括PowerShell第二批；以前所有旧工程/科研曾关闭额度、超GBK存储上限、Windows argv、先前4/4 source-only身份探针及旧失败原证保持原样。

## 五、保留科学边界与下一决策

**综合独立审议：** `DOCUMENTARY_LIMITED_ACCEPT__CODEX_REPORTED_B8_S8_L4_SYNTHETIC__SEAL_SUMMARY_NULL_RESERVATION`。这是有明确正反例结果的工程局部进展，不是纯Source-only猜测；但不足以宣称原可信工作站真实loader/runner、bare Git GitHub candidate、匿名脱敏完整发布安全或经济学成果通过。

冻结V010科学plan commit`bf091da33d59293f147d52c11580327d3ac2a85d`/blob`85138d8859d53295262fe13bf5bc277bca95ed3f`和模型commit`94de4501dec051b969bee9d852eba2d4591f30ef`/tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`**没有修改**。原MATLAB修正路线：corrected两资产HA/HJB/KFE→多省顺序单轮→原GovInv收益率边界0.9/1.1及Zt→冻结GDP独立≤1%验证→原lagged-NKPC递推，目的地工资税一次、家庭人均/省财政总量、三劳动账、same-S、前完整轮raw ra0、phi_max=.3、20×20×2原格点/阈值全部不变。双省synthetic F-order25`NO_ADMISSIBLE_POLICY`旧结果与新corrected HA单点`rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07`完全`UNTESTED`继续记录，不存在GE/正式IRF/论文Results资格。

Owner现有独立C盘SSD备份+GitHub备份、SSH key/443、`TRUSTED_WORKSTATION_ENGINEERING_CONTAINMENT`而不宣称native OS sandbox，禁触原受保护`D:\ProjectTemp\c5k1bturn56`的8 dirty/index/staged/untracked/ignored、外Git common-dir、所有旧回执、C盘备份、真实C8/2017/2018/B3与V009数组。临时`_review_tmp/ch5/<task-id>/`只能出现于Owner另行批准的独立GitHub review commit tree，不能在本地原项目工作树/index/staged落地；本任务没有新的远端temp候选可清。

**保持：**`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`ORIGINAL_SANITIZATION_DENIAL_CAUSE=UNKNOWN`、`HISTORICAL_LEDGER_DEVIATION=UNRESOLVED`、`SEAL_EVIDENCE_INTEGRITY=UNVERIFIED`、`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`model_activation=False`、`Results FALSE`、`real C8 A–D REQUEST_ONLY`、`V011 NOT_STARTED`。

**后续建议，非自动授权：** Owner如同意，可在一张独立有限`ENGINEERING_INTEGRATION`任务中，针对**新工程脚本与合成产物**做真实身份集成验证及first/final封存链关联审查，并考虑用更易安全复查的最小脱敏结果从GitHub独立review branch向Astra交付；该任务需新明确E0/mktree/Python子进程/SSH Git发布次数、保护边界和候选白名单，亦不能因本次20/20就自动启动模型HA科学预算。