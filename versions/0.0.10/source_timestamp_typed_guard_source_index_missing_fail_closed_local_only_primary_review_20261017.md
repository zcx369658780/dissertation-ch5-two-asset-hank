# V010 SOURCE_TIMESTAMP：sourceIndex 缺失导致前置拒绝的独立限域主审

**日期：**2026-10-17（Asia/Shanghai）。
**正式任务ID：** `V010_SOURCE_TIMESTAMP_TYPED_GUARD_CORRECTION_AND_SYNTHETIC_REGRESSION`。
**固定发行Commit：** `6dfe8a1c98a839f0a94cdd0e938bb6b60f99d520`。
**固定任务Git Blob：** `68143e917df883e38fa4615ce0a7c7a86c797330`。
**Codex结果ID：** `V010_SOURCE_TIMESTAMP_TYPED_GUARD_CORRECTION_AND_SYNTHETIC_REGRESSION_RESULT`。
**总裁决：** `FAIL_CLOSED__LOCAL_ONLY__SOURCE_INDEX_MISSING__NO_SCRIPT_OR_FIELD_IDENTITY__NO_TIMESTAMP_DIAGNOSTIC_OR_FIX`。
**终态：** `DELIVERED__STOPPED`，`ACTIVE_TASK=NONE`。
**下一授权门：** `WAIT_OWNER_FRESH_V010_SOURCE_SCRIPT_IDENTITY_RECOVERY_AUTHORITY / STOP`。本审议**不**自行创建后续冻结执行任务，不得继承任何旧资源。

## 1. Astra独立GitHub核验范围

独立连接GitHub仓库`zcx369658780/dissertation-ch5-two-asset-hank`的治理分支`migration/astra-workflow-20261012`。本轮主审前实时HEAD为`d53de3ae507a204d87b3b30c82ef08b3438dd7bf`，和上一同步HEAD比较`status=identical`（ahead0/behind0）。固定发行Commit下读完整冻结任务，实核Blob`68143e917df883e38fa4615ce0a7c7a86c797330`，与CURRENT和TASK_CURRENT登记一致。

冻结任务第1节要求：旧scratch文件的访问必须依据上一正式receipt/manifest的**确切来源索引**，最多只读12个普通小文件、累计≤2MiB；如无明确索引即STOP，不准猜测文件名、寻找附近路径或泛目录遍历。该条不是任意工程判断，而是本轮已冻结的来源保护要求。

GitHub查询没有发现相应新任务的review分支；对更早的指定`review/ch5-temp-v010-current-seal-evidence-20261016` ref查询`result.md`及`manifest.json`均得到GitHub 404 `No commit found for the ref`，因此此前证据交换亦未产生可独立核验的四份远端文件。本轮固定任务本来明文`GIT_COMMANDS=0 / GITHUB_PUBLICATION=0`；远端不存在与Codex报告相符，但不是本机数据/文件系统的独立认证。**没有新的Codex候选Commit/Tree/远端原件可供本轮复核或清理。**

## 2. SOURCE_INDEX 的实际停止事件及证据等级

Owner转述的Codex交付为`LOCAL_ONLY / FAIL_CLOSED`：前次证据交换失败回执原文件的SHA256据Codex在本机重算匹配其既有值`F93DA4C6BEE0E62F68A04620B8BF372AD60275C20DEA7782EF2C56E4BFADA6FC`，但回执对应的manifest中`sourceIndex`为空，**没有提供上一失败SOURCE_TIMESTAMP守门脚本的确切授权路径、文件整体hash与字段/schema索引**。Codex按冻结第1节在该先决条件处停止，没有推测路径、扩大目录读取或从随机脚本反推身份。

正式证据分账：

- `SOURCE_INDEX_EMPTY=CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，Astra**未收到manifest本机原字节**，故不能标`GITHUB_RAW_VERIFIED`。
- `GUARD_SCRIPT_AUTHORIZED_PATH=UNAVAILABLE`；`GUARD_SCRIPT_WHOLE_FILE_SHA256=UNAVAILABLE`；`RAW_FIELD_SCHEMA_INDEX=UNAVAILABLE`。
- `SOURCE_IDENTITY_PRECONDITION=FAIL_CLOSED`；由此`ACTUAL_PARSER_VERSION / RAW_JSON_TOKEN_KIND / PARSED_TIMESTAMP_ACTUAL_TYPE=UNKNOWN / NOT_DIAGNOSED`。
- `TIMESTAMP_GUARD_FIXED=NOT_RUN`；`SYNTHETIC_12_CASES=NOT_RUN`；`REAL_TIMESTAMP_FIELD_RECHECK=NOT_RUN`。
- 旧的`SOURCE_TIMESTAMP`是否确实因解析器将合法字符串转换成.NET时间对象而误拒，仍`UNDETERMINED`；**不能**从sourceIndex缺失推断原timestamp无效或脚本实体丢失。只能证明当次manifest在任务约束下不足以认证来源。

这次局部`FAIL_CLOSED`是符合冻结合同的停止，不把尚未执行的合成测试称为失败、也不将未读到的脚本猜为某个PowerShell路径。禁止借本轮新的匿名seal覆盖旧回执源链的空缺。

## 3. 新旧封存与资源的分账

Codex自报：本轮PowerShell受界批次**1/2**；**2份**已授权旧文件共**4次读取，累计6,800B**（“文件数”与“读取操作数”不得混为一谈）；新独立scratch**四份新增文件、累计9,463B**。Git命令、bare、SSH、fetch、push、Python/model import/VerifiedLoader、真实runner、HA/HJB/KFE/GE/IRF/真实C8及其他科学调用全部**0**。

本轮`FIRST_RECEIPT`和`FINAL_RECEIPT`据Codex以真实原字节封存，报告共享同一run_id及单向哈希链；其真实性属于`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，Astra未得到本机文件字节直接复算。Owner转述本轮最终回执SHA256：

`1E9A02F1C9AF59FAB80BED91E39353EB4CCBD87884D46C229D3E9C44610846BC`

**不是Astra独立计算结果**。墙钟具体时长、单文件hash和匿名case清单（本轮测试尚未运行）不在Codex简报中，不能虚构。所有本轮未用额度（包括第二批PS及未执行的真实字段核查）、全部更早已STOP工程/科学预算随STOP关闭、不结转。

前轮17/17合成工程集成与其first/final关系仍是Codex本机报告级；更早20项B/S/L合成的旧first seal缺可还原raw与旧run_id，正式`LEGACY_SEAL_CHAIN_UNVERIFIABLE`，永不得补造。本轮新的failure-first/final只能证明**本轮失败留证能力的报告**，不能替代守门源码索引，也不能修复前轮证据链。原旧脱敏拒绝原因`UNKNOWN`且被拒材料依旧`PUBLICATION_DENIED`；原中间ledger曾包含短源码/原argv的历史偏差`UNRESOLVED`。

## 4. 永久科学保护及下一许可建议

原V010科学冻结计划Commit`bf091da33d59293f147d52c11580327d3ac2a85d`、Blob`85138d8859d53295262fe13bf5bc277bca95ed3f`，模型Commit`94de4501dec051b969bee9d852eba2d4591f30ef`、Tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，没有任何新科学验收或修改。原MATLAB两资产corrected HA/HJB/KFE→多省顺序→GovInv收益边界×0.9/1.1与Zt→冻结GDP误差≤1%独立验证→lagged-NKPC原递推不变；目的地工资税一次、same-S和前完整轮raw-ra0、家庭人均/省财政总量与三劳动账、phi_max=.3、20×20×2原网格阈值冻结。

Owner新corrected HA单点`rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07`仍`UNTESTED`。`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`model_activation=False`、`Results FALSE`、`V011 NOT_STARTED`、`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`real C8 A–D REQUEST_ONLY`均保持。Owner现有C盘独立SSD备份+GitHub备份、可信工作站和既有SSH Key/443政策不变，但本轮Git/SSH=0。原受保护D盘`c5k1bturn56`八dirty/index/staged/untracked/ignored、外部Git common-dir、旧失败scratch和原raw证据、C盘备份与真实C8/2017/2018/B3不触写。远端`_review_tmp`不得进入本地项目工作树/index。

**建议而非已授权新任务：** 下一步先解决“合法的、可审计的SOURCE脚本身份从何取得”，而非继续针对未知脚本做类型实验。Owner可另授一次**精确来源索引恢复+原timestamp类型修正的条件任务**：以固定上位任务或已知原receipt、文件整体hash索引和显式只读白名单为权限依据，在新的独立scratch只读核实脚本身份；只有三元身份`authorized_path + whole_file_SHA256 + source_field/schema anchor`被可靠恢复，才进入解析器/类型诊断和合成12例；若恢复失败则STOP。禁止从空sourceIndex无界枚举旧目录、推测脚本、凭借历史SHA随意选择附近文件；不得把该建议当作本轮剩余额度或发布许可。

**正式终态：**`V010_SOURCE_TIMESTAMP_TYPED_GUARD_SOURCE_INDEX_MISSING__FAIL_CLOSED_LOCAL_ONLY__NO_SYNTHETIC_OR_SCIENCE__STOP`。
