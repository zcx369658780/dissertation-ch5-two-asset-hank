# V010 工程集成 / first-final封存链 / 纯合成 mktree：独立GitHub限域主审

**审议时间：**2026-10-16（Asia/Shanghai）  
**原任务：** `V010_ENGINEERING_INTEGRATION_SEAL_CHAIN_SYNTHETIC_MKTREE_PREFLIGHT`  
**冻结任务发行Commit：** `34497613d7085cfeea39682aef15f983ef5030a9`  
**冻结任务Blob：** `6aa223b4c98391e051ebe4f7b8d358f88cf678bf`  
**Codex结果ID：** `V010_ENGINEERING_INTEGRATION_SEAL_CHAIN_SYNTHETIC_MKTREE_RESULT`  
**正式主审裁决：** `PARTIAL__LEGACY_SEAL_CHAIN_UNVERIFIABLE__CURRENT_SYNTHETIC_INTEGRATION_17_OF_17_CODEX_REPORTED__CURRENT_SEAL_CHAIN_LOCAL_RAW_PROVENANCE_REPORTED__MKTREE_SYNTHETIC_POSITIVE_NEGATIVE_REPORTED__NO_INDEPENDENT_WINDOWS_VERIFICATION`  
**上一任务状态：** `DELIVERED__STOPPED`；`ACTIVE_TASK=NONE`。  
**停止点：** `WAIT_OWNER_FRESH_V010_SANITIZED_EVIDENCE_EXCHANGE_AND_REAL_ENGINEERING_GATE_AUTHORITY / STOP`，无下一任务及运行许可自动派发。

## 一、GitHub独立核验的范围

Astra使用GitHub连接器核实仓库 `zcx369658780/dissertation-ch5-two-asset-hank` 治理分支 `migration/astra-workflow-20261012`。审议前HEAD `b862f0206bc507ccfd6f748715ca756cfb7e2414` 与上一归档基线比较 `identical/ahead0/behind0`。按照固定发行Commit读取 `versions/0.0.10/engineering_integration_seal_chain_synthetic_mktree_task_20261016.md`，Blob精确匹配 `6aa223b4c98391e051ebe4f7b8d358f88cf678bf`，明确许可的是纯本地PowerShell合成工程集成、前轮seal核验和新的独占bare合成mktree，不允许GitHub发布、模型Python、真实runner或科学HA。GitHub用`seal`查分支未见对应新临时review；本任务本来不授权发布，未发现远端候选符合报告，不把有限分支查询等同全库/本地不存在证明。

**Astra未能直接读取**本轮 `D:\ProjectTemp\ch5_v010_integration_seal_mktree_20261016_01` 内真实first/final封存字节、PowerShell脚本、17项逐案expected/actual、Git子进程stdout/stderr、旧scratch首版封存或Windows任务资源账。所有“本机hash匹配”“17/17”“正反mktree”“本轮新封存链”均按 `CODEX_REPORTED_WITH_LOCAL_RECEIPTS` 级别审议；GitHub上的固定任务身份是真实独立核验，**不等于**Astra独立Windows工程验收PASS。

本轮最终回执SHA256由Owner转述为 `859398F7F4ABF2067AAF6613213290B9F027EE48D2A7E0EEA361BC0C5FDF5197`，没有原字节上传，本主审**没有独立重算**。

## 二、分门实质裁决

### Gate S：前轮封存链不可验证，不能追溯补证

Codex报告前轮最终receipt的实际原字节SHA256与既有Owner哈希 `70622F5AF09089983639F81973837D7EF7D5E0CAA6B33E85D0C74B5B7EA74D23` 一致，属于 `CODEX_REPORTED_LOCAL_HASH_MATCH`，非Astra直接读取结果。但前轮**首版seal只有结构化快照/引用哈希，没有可独立还原验证的原始字节实体**；旧`run_id`亦从未记录。因此旧链的 `FIRST_SEAL_RAW_EXISTS=NO`（按Codex当地取证报告）、`FIRST_FINAL_SAME_RUN_ID=UNVERIFIABLE`、`CASE_MANIFEST_UNCHANGED_ACROSS_LEGACY_SEAL=UNVERIFIABLE`、`LEGACY_SEAL_CHAIN_PROVEN=NO`。

`LEGACY_SEAL_CHAIN=UNVERIFIABLE` 是真实历史证据缺口，**不得**通过重跑上轮20测试、补写run_id、借本轮新first receipt冒充前轮原字节、删除原null快照来追溯填平。前一轮20/20依然是带封存链限制的`CODEX_REPORTED_SYNTHETIC_EXPECTED_MATCH`，不能升级历史认证。旧证据真实原件须继续只读保存。此门不满足历史完整闭环标准，但不阻止按冻结任务处理**独立**的新合成门，且总体不得标FULL_PASS。

### Gate I：17/17本轮集成，仅限合成、本地回执

Codex报告`INTEGRATION_17_OF_17_EXPECTED_MATCH`：在新独立bare对修正身份门、结构化脱敏和匿名台账联动测试，没有报告任何实际用例不匹配；Git identities与模拟正负例均按既定合成边界运行，`BARE_NONSHARED_GUARD_INTEGRATION=CODEX_REPORTED_SYNTHETIC`、`SANITIZER_LEDGER_PIPELINE_INTEGRATION=CODEX_REPORTED_SYNTHETIC`。由于没提供17项逐例原件及实际修复脚本哈希供Astra复查，不能断言具体每组实际条数、文件来自上一修复sha或曾遭改写，更不能把合成身份测试等同原真实发布裸仓已经被认证、同用户恶意替换能被OS级沙箱阻断。

**mktree：** Codex报告本轮serializer在写入前主动拒绝额外空白行，合成正例使用两个安全文字blob生成恰好两条tree entry；向Git直接提交额外空行的负例得到真实退出码`128`。该本地回执支持 `MKTREE_SERIALIZER_SYNTHETIC_POSITIVE_TWO_ENTRIES__NEGATIVE_EXIT_128_CODEX_REPORTED`；不能把Git负例退出码128当成未来所有Git版本语义或远端GitHub发布成功，也没有在原旧发布器上执行真实push。

`ORIGINAL_REJECTED_SANITIZATION_CANDIDATE=DENIED`、`ORIGINAL_SANITIZATION_DENIAL_CAUSE=UNKNOWN`继续保持；新合成脱敏器的通过不能自动解除旧发布材料限制。

### Gate N：**本轮**first/final真实封存链据报完整，不修前轮

Codex明确报告本轮实际保留了first与final两份可独立读取的原始字节，二者`run_id`相同、17个合成结果hash稳定且使用单向哈希链接，`CURRENT_SEAL_CHAIN_LOCAL_RAW_PROVENANCE=CODEX_REPORTED_CORROBORATED`。本次证据形式优于上轮仅有first结构化快照的做法，属于合理的工程进展。此处“可独立读取”是**Codex在本机据报核证的性质**，不是Astra已获取两份文件独立校验；Astra仍需对应脱敏原件才能写 `GITHUB_REMOTE_EVIDENCE_INDEPENDENTLY_VERIFIED`。

本轮真实first/final即使经未来确认完整，也**不允许**修补上轮缺失的raw首版或未记run_id。历史 `LEGACY_SEAL_CHAIN_UNVERIFIABLE` 和本轮 `CURRENT_SEAL_CHAIN_LOCAL_PROVENANCE_REPORTED` 是两个独立事实并存，不能跨run回填。

## 三、预算与留存评级

Codex摘要自报（非AstraWindows直验）：

| 项目 | 本轮实际 / 冻结最大 | 分类 |
| --- | --- | --- |
| PowerShell集成测试 | 1/2 | 第二轮未用额度随STOP关闭 |
| 新独立bare init | 1/1 | 仅本轮合成仓 |
| Git read-only身份child | 4/6 | 其余2不可结转 |
| hash-object -w | 2/2 | 只安全合成对象 |
| mktree | 2/2 | 正负各一次 |
| ls-tree | 1/1 | 仅合成tree |
| 前轮精确文件读取 | 43,787B | 上限1MiB；**文件数未给出** |
| 新非Git平铺文件 | 8份 / 68,551B | 已达8文件上限，写前128KiB预留过程仍未亲核 |
| bare整体目录 | 16条目 / 保守1,049,165B | Codex报告全目录metadata保守计量；未独立量算，低于32MiB上限 |
| Git其它metadata read、wall、逐次超时/资源日志 | UNKNOWN | 不能推定全部流程硬门已独立PASS |
| Python / VerifiedLoader / 真实runner / HJB KFE GE IRF C8 | 0（Codex报告） | 完全未运行 |
| GitHub fetch/push/commit/ref发布 | 0（Codex报告） | 本任务明确禁止 |

前轮及全部旧任务的Git/PowerShell/Python/科学未使用余额早已STOP；本轮所有未使用部分亦从此次`DELIVERED__STOPPED`起关闭，**不能转给下一任务**。历史GBK日志超限、Windows argv、Stage A/旧root/首次封存null等依原样存档，不能擦除。

## 四、固定科学合同与保护

V010科学plan commit`bf091da33d59293f147d52c11580327d3ac2a85d`/Blob`85138d8859d53295262fe13bf5bc277bca95ed3f`，模型候选commit`94de4501dec051b969bee9d852eba2d4591f30ef`/tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`不改。主线依原MATLAB修具体错误：corrected两资产HA/HJB/KFE→多省顺序单轮→GovInv收益率边界×0.9/1.1及Zt→冻结GDP误差≤1%独立验证→原lagged-NKPC递推。目的地工资税仅一次、家庭人均/省财政总量、三劳动账、same-S与前完整轮lagged raw ra0、phi_max=.3、20×20×2网格/阈值继续冻结。旧双省synthetic F-order25`NO_ADMISSIBLE_POLICY`与Owner新单点 `rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07` `UNTESTED`，没有真实runner或任何GE/正式IRF/论文Results。

Owner现有C盘独立SSD备份+GitHub备份、现有SSH Key/443、可信工作站工程风险选择不变；不强制VM/第三备份，也不能宣传OS_NATIVE_SECURITY_SANDBOX_VERIFIED。原受保护 `D:\ProjectTemp\c5k1bturn56` 8 dirty/index/staged/untracked/ignored、外Git common-dir、全部旧失败原证、C盘备份、真实C8/2017/2018/B3及V009失败数组保持不可触写。远端 `_review_tmp/ch5/<task-id>/` 只允许经另行授权在独立GitHub review branch tree出现，不进入任何本地科研/模型/治理worktree/index；本轮没有可清的新增远端临时证据。

**永久状态：** `LEGACY_SEAL_CHAIN_UNVERIFIABLE`、`CURRENT_SEAL_CHAIN_LOCAL_PROVENANCE_CODEX_REPORTED`、`ORIGINAL_SANITIZATION_DENIAL_CAUSE=UNKNOWN`、`HISTORICAL_LEDGER_DEVIATION=UNRESOLVED`、`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`real C8 A–D REQUEST_ONLY`、`model_activation=False`、`Results FALSE`、`V011 NOT_STARTED`。

## 五、结论与建议（不自动发行下一任务）

**总裁决**：`PARTIAL__LEGACY_SEAL_UNVERIFIABLE__CURRENT_LOCAL_SYNTHETIC_17_17_AND_SEAL_CHAIN_REPORTED__NO_FULL_PASS`。重点工程进展为：前一代不可验证的旧封存原件已被如实隔离为永久历史限制；本代新17项集成、tree序列化正反测试和raw first/final哈希链接获得Codex本地依据，但尚无远端Astra独立原始字节证明。

**合理的下一有限门**（仅建议）是Owner另行授权**可验证的新证据交换及其独立回读**：优先最小、经过新版sanitizer核准的**本轮**匿名schema字段、合成测试索引与first/final两份精确哈希/结构化不可反推标识，不需要推旧候选或修补原来不存在的旧seal。届时按Owner协议为新的临时review ref单独冻结任务parent/file白名单、大小、SSH443预算与失败STOP，远端实际Git核验后归档再删除本轮独立review tree的临时文件。**Python真实工程导入、完整runner、HA科学调用及GitHub发布均需要明确分别授权；本轮没有这些权利。**
