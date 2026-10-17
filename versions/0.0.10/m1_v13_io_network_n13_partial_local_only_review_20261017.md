# V010 M1 · IO/NETWORK/canonical/N13 集中工程：独立限域主审

**审议日期：**2026-10-17（Asia/Shanghai）  
**冻结任务ID：** `V010_M1_V13_IO_READ_NETWORK_AUDIT_CANONICAL_N13_INTEGRATED_REPAIR`  
**固定发行Commit：** `72f1ef4c908b31fba339f16ccb5dba0cc7bd4fbc`  
**固定任务Blob：** `9e0160ed27a80a49cc07374f79cb75d80cfe16aa`  
**正式任务：** [只读冻结原件](../versions/0.0.10/m1_v13_io_read_network_audit_canonical_n13_integrated_task_20261017.md)  
**交付ID：** `V010_M1_V13_IO_NETWORK_CANONICAL_N13_INTEGRATED_RESULT`  
**总分类：** `PARTIAL_ENGINEERING_DIAGNOSTIC__LOCAL_ONLY__IO_PROBE_NARROW_FIX_REPORTED__SOCKET_GETHOSTNAME_CLASSIFIED__N13_TIMED_TIMEOUT_REAP_CODEX_REPORTED__CANONICAL_IMPORT_GIT_NO_CAPABILITY_BLOCKED__NINE_MODULE_AND_RUNNER_NOT_RUN`  
**任务结果：** `DELIVERED__STOPPED`；`ACTIVE_TASK=NONE`；全部本轮未用Python及Git额度关闭、不结转。  
**下一停点（建议，非新授权）：** `WAIT_OWNER_FRESH_V010_PLATFORM_SYSCMD_VER_SUBPROCESS_PROVENANCE_AND_IMPORT_ONLY_GATE_AUTHORITY / STOP`。

## 1. 独立取得的 GitHub 事实及本地证据限制

Astra通过已连接GitHub工具，从本任务发行Commit实际读取冻结正文，任务Git Blob确切匹配`9e0160ed27a80a49cc07374f79cb75d80cfe16aa`；读取治理分支`migration/astra-workflow-20261012`，审议前live HEAD=`d194ed8121aae0155fefc224e62c6ca3d85d1841`，对之前同SHA比较`identical`，ahead0/behind0。目标review ref `review/ch5-temp-v010-m1-io-network-n13-20261017` 的分支查询无匹配，对其下`result.md`和`manifest.json`精确fetch均为`404 No commit found for the ref`。因此**无GitHub远端候选Commit、Tree、五个审阅文件Blob可独立核验，也无需远端清理。**

Owner提供的Codex回执只是脱敏交付文字和三个 SHA256，没有Windows本机实际文件字节、逐进程原始审计或封存chain原件交给Astra。以下E0/E1/E2/N13、资源账、进程回收/本地保护均属于`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，**不是`ASTRA_INDEPENDENTLY_EXECUTED_OR_REHASHED_WINDOWS`**。本审议仅把局部结果限定接受为下一阶段定位依据，不授完整工程或科学PASS。

## 2. 四项工程门的分别裁决

| 门 | Codex交付的实际对象 | 证据等级与结论 |
| --- | --- | --- |
| E0 首次写前/固定源 | 新scratch写前身份PASS；从冻结模型源码得到70份原始字节；终态70/70 SHA256、GitBlob、大小与文件身份均一致 | `E0_SOURCE_INTEGRITY_CODEX_REPORTED_PASS`，网页没有取得70份Windows源原raw与本机文件系统镜像 |
| IO拒绝定位 | 首次`IO_READ_CLOSURE`为`Lib/__future__.py`的**不存在缓存探测**；修后缓存读取实际0B且不扩大可读范围 | `IO_CACHE_NEGATIVE_PROBE_NARROW_FIX_CODEX_REPORTED`；不能由此放宽真实未认证文件读取 |
| NETWORK拒绝定位 | 原审计为`socket.gethostname`；按已认证调用链窄分类；socket创建和DNS实际拒绝仍保留 | `NETWORK_EVENT_CLASSIFIED_LOCAL`，**不能说曾外联/实际连网**；网络DENY仍生效 |
| N13活超时负例 | Codex报告4.039秒超时、Windows Job终止、Python与唯一惰性dummy子进程回收、reader退出 | `N13_TIMEOUT_REAP_CODEX_REPORTED_PASS`；无原PID/exit/Job/reader全回执供网页重算 |
| canonical真实import | 两次尝试均未成功：`platform._syscmd_ver`提出未获准的`subprocess.Popen`请求，守门`GIT_NO_CAPABILITY`**创建前拒绝** | `CANONICAL_IMPORT=BLOCKED`，安全守门正确停止越界spawn；不得把失败解释为可以无条件开放Popen |
| 九模块与真正runner | Codex明确均`NOT_RUN`，没有新五Git child runner完整执行证据 | `NINE_MODULE_NOT_RUN`、`RUNNER_IMPORT_ONLY_NOT_RUN`，`FULL_RUNNER_IO_CLOSURE=BLOCKED` |
| E3 GitHub证据 | 唯一一次远端分支预检exit128、原因`UNKNOWN`，fetch/push/readback=0 | `E3_LOCAL_ONLY__PREFLIGHT_FAILURE_CAUSE_UNKNOWN`；目标ref404已由GitHub独立核 |

**特别说明：**在Windows上标准库`platform._syscmd_ver`的环境信息查询可能尝试创建额外子进程，但本地交付没有可信调用栈、实际请求命令原字节及安全能力约束的完整关联回执，不能先验认定其命令绝对安全。现有`GIT_NO_CAPABILITY`对未在明确五Git子进程白名单内的`subprocess.Popen`拒绝是合理边界；未来若新任务继续，只能先认证来源与精确调用，考虑**不增加泛用spawn权限**的明确工程方案。不能预先授予任意系统命令权限或修改冻结模型/stdlib字节。

## 3. 新预算实际消耗与封存

| 对象 | Codex报告 | 合同上限/审议 |
| --- | --- | --- |
| 工程Python子进程 | 6/8：static/dummy 2/2，probe 2/2，canonical 2/2，真实runner 0/2 | 计数在上限内；未用2次随STOP关闭，不能借给下一次 |
| native non-Python dummy | 1 | 在至多1个的本次许可内 |
| Stage A只读Git | 7 | ≤100；不代表已审完每个child stdout |
| PowerShell | 29批 | 本轮V1.3无跨任务继承的“PS 2批”上限，不据此单判超额 |
| 旧来源内容读取 | 13个不同文件、28次读取、784,720B | ≤16个不同文件、累计≤3MiB；本地读账未独立重放 |
| 总执行墙钟 | 1,199.788秒 | ≤180分钟；单进程外部wall、原RSS/日志bytes尚未取得 |
| 非Git新文件 | 168件、2,700,463B | ≤32MiB；写前末尾2MiB预留的过程不能凭最终总量独立认证 |
| 项目外bare | 127B | 本轮未建立远端提交候选 |
| Git发布 | 精确远端预检1次exit128、原因UNKNOWN；fetch0/push0/readback0 | 网络/Git余量因STOP全部封闭 |
| PID与科学调用 | Codex称已登记PID终态全部不存在，科学及旧17/20/25测试0 | 不等于网页全系统进程扫描或模型函数逐指令认证 |

**原始封存声明（仅Owner/Codex提供哈希，Astra没有对应原字节）：**
- `FIRST` SHA256：`C954CE76FC40CD3D339AED593E985DAC2F1995FC5A1B93F5331F853000120838`。
- `ENGINEERING_FINAL` SHA256：`7D1464DFA00EF50A03D7B5EBD7D13BEFC5DBFCFB6CEC75821F6BBE971F9F52F5`。
- `DELIVERY` SHA256：`D08273150803F72A35C4AFDDFF5909DE77C901065B582104E23FFE590E53AA4D`。

此前单独发来的三项哈希与此次正式交付**文本完全一致**，但“相同哈希字符串”不证明三个对象的真实文件字节或first→final→delivery单向引用已经由Astra独立验证。本次本机`DELIVERY_RECEIPT.json`据报包含五份脱敏材料身份、逐进程账、失败及UNKNOWN，未由Astra取得原字节。

过去B/S/L20缺first raw/run_id的`LEGACY_SEAL_CHAIN_UNVERIFIABLE`、上版首次runner变体无raw、旧timestamp24/25+1 `SPEC_UNRESOLVED`及历史执行脚本bytes未认证、旧Sanitizer禁止发布与历史ledger偏差均保持，不能由本轮新seal或N13替代。

## 4. V010冻结数学合同、保护及下一门

V010科学计划固定Commit `bf091da33d59293f147d52c11580327d3ac2a85d` / GitBlob `85138d8859d53295262fe13bf5bc277bca95ed3f`；模型固定Commit `94de4501dec051b969bee9d852eba2d4591f30ef` / Tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，本轮没有获准变更模型/math。科研主线仍为原MATLAB corrected两资产HA/HJB/KFE→多省顺序→GovInv收益界×0.9/1.1和Zt→冻结GDP每省误差≤1%独立校准→lagged-NKPC递推；目的地工资税一次、same-S/前完整轮raw ra0、家庭人均/省财政总量及三劳动账、phi_max=.3及20×20×2原数值阈值均冻结。

**持续：**`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`model_activation=False`、`Results FALSE`、`V011 NOT_STARTED`、`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`real C8 A–D REQUEST_ONLY`。corrected给定参数HA单点 `rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07`**UNTESTED**。真实C8/2017/2018/B3/V009数组、原8dirty/index/staged/untracked/ignored/外Git common-dir、独立C盘SSD现有备份以及旧失败原件继续保护。据Codex称本轮未触写，不表示网页直接做过全量文件哈希扫描。

**后继建议，不自动授权：**新一轮V1.3定向工程门仅围绕`platform._syscmd_ver`在import-time提出`Popen`的真实来源/能力约束，研究**保持现有子进程白名单、无泛用任意spawn**的最小合规兼容方案；一旦可认证并安全pass，才重新运行canonical / 额外九模块 / 真runner的受界工程验证。本轮N13已有本机正向报告，后继可按来源确定是否需要重复，无须为它单独拆微任务。可选远端证据传输依Owner已经接受的GitHub交换协议安全处理，SSH预检exit128原因UNKNOWN，不能猜为账号或连接修复。科学HA必须未来独立Owner新许可。

**总裁决：** `PARTIAL_ENGINEERING_PROGRESS__N13_REPORTED_PASS__CANONICAL_BLOCKED_BY_UNAUTHORIZED_SUBPROCESS__LOCAL_ONLY_STOP`。
