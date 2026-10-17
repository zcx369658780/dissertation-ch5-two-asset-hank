# V010 M1 · Platform syscmd 来源与导入工程：Git 源码管道超限、局部诊断限域主审

**日期：**2026-10-17（Asia/Shanghai）  
**工作流：**V1.3（工程E2重要里程碑一次集中验收）  
**任务ID：**`V010_M1_V13_PLATFORM_SYSCMD_VER_PROVENANCE_AND_CANONICAL_RUNNER_GATE`  
**冻结发行Commit：**`7e9ade7c36a1b606c8d8125b0fd21e9b067d4f9c`；**任务Git Blob：**`67928a92b742054d7303771974cb8cb42943cd65`  
**任务原件：**[固定实施门](m1_v13_platform_syscmd_ver_provenance_canonical_runner_task_20261017.md)  
**Codex交付ID：**`V010_M1_V13_PLATFORM_SYSCMD_CANONICAL_RUNNER_RESULT`  
**正式裁决：**`FAIL_CLOSED__LOCAL_ONLY__GIT_SOURCE_PIPE_STDOUT_CAP_OVERRUN_REPORTED__LATE_OVERRUN_DETECTION__PROCESS_LEDGER_CONCURRENCY_CONFLICT_REPORTED__PLATFORM_SYSCMD_SOURCE_PROVENANCE_PARTIAL__CANONICAL_IMPORT_BLOCKED__NO_REMOTE_CANDIDATE`  
**终态：**`DELIVERED__STOPPED`、`ACTIVE_TASK=NONE`。全部本轮剩余工程与发布预算结束不结转。  
**建议后继（并未新签发）：**`WAIT_OWNER_FRESH_V010_M1_CONSOLIDATED_ENGINEERING_EXIT_GATE_AUTHORITY / STOP`。

## 1. Astra 实际独立验到的 GitHub 事实

通过已连接GitHub工具，独立读取发行Commit `7e9ade7c36a1b606c8d8125b0fd21e9b067d4f9c` 对应的固定任务文件，Git Blob`67928a92b742054d7303771974cb8cb42943cd65`匹配；本次审议前治理HEAD=`e4df86056037438c7a87f017193bee1abda427bc`，与上一已知HEAD对比`identical`，ahead0/behind0。目标远端分支`review/ch5-temp-v010-m1-platform-syscmd-20261017`查询无匹配；精确读取其`_review_tmp/ch5/v010-m1-platform-syscmd-20261017/result.md`返回GitHub`404 No commit found for the ref`。本轮没有可供独立复算的远端candidate commit/tree/four blobs，也没有需按远端协议清理的临时审阅文件。

Astra**没有**读取Owner Windows `D:`本地的first/final/delivery原始字节、Python/audit/stdout/stderr逐进程文件、资源计费原件或保护根文件系统。下列所有E0、真实调用链、进程/流量、Python回执、source保存与旧文件不变等均归`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，不可升格为`ASTRA_WINDOWS_RUNTIME_INDEPENDENT_PASS`。对独立GitHub冻结任务/远端ref状态的核验不能替代本机原证复算。

## 2. E0—E3分项裁决

| 门 | Codex明确报告的本轮事实 | 限域评价 |
|---|---|---|
| E0身份与冻结源码 | 写前preflight已完成，70份固定模型Python源码终态身份匹配 | `E0_SOURCE_INTEGRITY_CODEX_REPORTED`；网页无原字节复算 |
| 平台信息Popen源 | NumPy→`platform.machine`→`uname`→`win32_ver`→`_syscmd_ver`→`Popen`；请求类别`LITERAL_VER`、`shell=True` | `SYSCMD_CALLCHAIN_PROVENANCE_LOCALLY_CORROBORATED`；精准来源比上轮更清晰，但不证明该shell命令可放行 |
| 子进程安全守门 | `GIT_NO_CAPABILITY`在创建前拒绝未授权`Popen`，未新增非Git子进程权限 | `NON_GIT_SPAWN_DENIED_CODEX_REPORTED`；不得为导入通过取消能力检查 |
| 无子进程适配 | 完整语义等价性`UNRESOLVED`，适配器未安装 | `ADAPTER_NOT_INSTALLED`，不能自封`ADAPTER_ONLY_PASS` |
| Canonical/九模块/runner | 原生canonical失败；适配模式、显式九模块及真实runner均`NOT_RUN` | `M1_IMPORT_ENGINEERING_CLOSURE=BLOCKED` |
| 合成探针 | Python标准库版本规范化为前三段，但合成expected错误要求四段；失败已保留，没有重跑 | `SYNTHETIC_ORACLE_DEFECT_REPORTED__REGRESSION_NOT_RERUN`；未提供可独立确认的测试原文，不以旧失败证明标准库bug或本轮PASS |
| N13 | Job、timeout、reader机制据报未修改，按冻结任务不重复N13 | 沿用先前`N13_TIMEOUT_REAP_CODEX_REPORTED`局部证据，本轮`NOT_RERUN` |
| E3安全审阅 | Codex报告远端预检/fetch/push/readback全部0；未创建candidate | `LOCAL_ONLY__NOT_ATTEMPTED`；目标ref缺失GitHub独立确认 |

**新信息价值：**已报告的链路将上轮笼统`platform._syscmd_ver`触发`Popen`细化成NumPy发起、具体标准库转入`LITERAL_VER`+`shell=True`，且实际spawn被拒绝。这支持未来选择准确工程边界，不会把`platform.machine`等同任意科学模型执行，也不能凭名字就断定请求完全安全。旧`socket.gethostname`分类及`Lib/__future__.py`缺失缓存探测局部结论保留，无本轮改动证据，不重复授新PASS。

## 3. 硬额度超限与台账源缺陷——与正常工程进展分别记录

Codex交付报告在收尾时发现：**Git源码管道输出`1,106,482B`**，冻结任务第4节限制每进程stdout+stderr合计**`262,144B`**，**报告超额`844,338B`**。Codex亦报告本轮未及时在执行过程中截流/拦截，识别时已启动**3个Python进程**。这构成`OUTPUT_CAP_BREACH_REPORTED`与`LATE_FAIL_CLOSED`；不可事后把原任务上限扩大、赦免超限、伪造实时截流，整体工程门不能授PASS。

**同时需要区分任务合同的设计缺陷可能性**：上次冻结70份源码合计约1.1MB，本轮Git源码管道1.106MB与该量级接近。若审计原文证实这是合法的**Git raw source数据流**而非诊断日志，旧任务将原字节来源数据与普通进程stdout/stderr统一按256KiB截断，可能存在数据用途混淆。这只是`POTENTIAL_SOURCE_DATA_VS_LOG_CAP_DESIGN_MISMATCH`而非本机流向事实已经独立认证；下版应由Codex核真实callsite/pipe及计量位置，然后将**受身份认证、总字节和单文件hash控制的源码流**与**日志流**分别设定预算、真实限流和预读上界。不允许自动将所有输出排除审计，不能用“合理原始数据”追溯免除本轮超额。

此外Codex报告**台账并发覆盖**与其后**启动前文件冲突**，均已保留；静态进程计数按真实工具回执和执行脚本SHA256追认，但未重跑。判为`PROCESS_LEDGER_CONCURRENT_OVERWRITE_REPORTED__AUDIT_CHAIN_INTEGRITY_PARTIAL`：不凭恢复摘要等同完整原始事件顺序，也不能认定已违规增加隐形进程。下一大任务的通用执行器应做单写者/原子ledger事件序号与提交前后读回，失败记录与原first/final独立保存，不再为单个ledger字段签发微任务。

## 4. 本轮资源与封存

| 项目 | Codex报数 | 解释 |
|---|---|---|
| 工程Python | `3/8`：static/probe2，canonical1，九模块/runner0 | 计数在总额内，但stdout硬超额独立导致FAIL_CLOSED；未用5次不结转 |
| Stage A只读Git | `7` | ≤100，源Git管道超额另计 |
| PowerShell | `20`批 | V1.3任务没有“旧2批”通用上限，不单独构成违约 |
| 旧文件只读 | `12`件，总计`1,984,899B` | ≤12件、≤2MiB（2,097,152B），非常接近上限；不同次读取细账仅本地报告 |
| 用时 | `442.730s` | 总wall≤150分钟，本机逐进程wall未知 |
| 新非Git文件 | `144`件、`2,870,502B` | 总量≤32MiB；未独立审查2MiB封存预留时序 |
| 全新审阅发布 | GitHub预检/fetch/push/readback`0` | 没有使用网络预算 |
| 进程/科学 | Codex称已登记PID全部结束，科学调用`0` | 非全OS扫描或网页独立模型审查 |

**封存三件分账（仅Owner/Codex提供SHA文本；未经原件独立SHA重算）：**
- `FIRST` `94C6C517BF7C98A18FF3806F2B2BD0949473E63290FD7D5B5336C66908025451`。
- `ENGINEERING_FINAL` **发现超限前就存在的原字节，不得覆盖**：`4BDBDBAD1F329C8AC8829C5CEAAE869FD0DBA97A1FEE80DEDF51376E55D0B5B5`。
- `DELIVERY` **披露超限与台账异常之后的最终交付身份**：`D643C68E4537E88C551C1A316289236AF965F14C0BE6F3400784FE0C625BDC44`。

`ENGINEERING_FINAL` 不能因发现硬超额就被静默改写成“全程合规的Final”；`DELIVERY`对违规事实的后续说明也**不**意味着first→final→delivery原始哈希链由Astra实际复算。历史更旧B/S/L20`LEGACY_SEAL_CHAIN_UNVERIFIABLE`、旧runner变体实际源码raw缺失、历史PS执行源码hash未认证、上轮timestamp合成24/25+1`SPEC_UNRESOLVED`、旧sanitizer`PUBLICATION_DENIED`和历史ledger偏差均原状保存。

## 5. 科学/保护状态与后续长任务结构建议

V010科学计划Commit `bf091da33d59293f147d52c11580327d3ac2a85d` / Blob`85138d8859d53295262fe13bf5bc277bca95ed3f`；模型Commit `94de4501dec051b969bee9d852eba2d4591f30ef` / Tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`不改。原MATLAB corrected两资产HA/HJB/KFE→多省手动有界顺序→GovInv收益界×0.9/1.1与Zt→冻结GDP每省≤1%独立回读→原lagged-NKPC；目的地工资税一次、same-S/上轮完整raw ra0、家庭人均/省财政总量与三劳动账、phi_max=.3、20×20×2网格及原数值阈值持续冻结。Owner corrected HA给定价格单点仍`UNTESTED`、`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`model_activation=False`、`Results FALSE`、`V011 NOT_STARTED`。

原D盘`D:\ProjectTemp\c5k1bturn56`八dirty tracked/index/staged/untracked/ignored、外Git common-dir、C盘物理独立SSD原备份、旧失败scratch及真实C8/2017/2018/B3/V009原件不可触写。Codex报告未写原保护树，但**没有全局字节复查**，网页也未直接审计。原`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`real C8 A–D REQUEST_ONLY`继续。

**回应Owner明确提醒：不能继续按单个报错拆微任务。** 本轮截至此处只有可信工程诊断而无canonical import PASS。建议下一授权以**一次完整M1工程交付的大任务**覆盖：可信source/stdlib与stdout raw数据流分账、台账原子记账、合法Windows元数据读取策略与原生/适配模式准确区分、真实canonical/九监测模块、完整Job/runner与必要负例、集中证据交付。普通工程错由Codex在预设总体预算内自主修复，不为每次异常另立GitHub任务。科学HA/真实数据/经济方程与不可逆风险仍需Owner单独授权；是否在以后同一大版本从M1进入经批准的科学单点，应在新冻结任务中事先写明而不是中途越权扩权。

**本轮STOP：不得使用剩余5次Python或剩余Git操作；下一任务需要Owner明确授权且重新冻结整体范围，不自动签发。**
