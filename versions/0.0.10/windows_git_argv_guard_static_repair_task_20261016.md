# V010 Windows Git argv 守门器：仅静态取证与安全修复方案

**任务ID**：`V010_WINDOWS_GIT_ARGV_PREFLIGHT_STATIC_FORENSIC_AND_GUARD_REPAIR`。
**唯一授权类别**：`NON_SCIENTIFIC_SOURCE_ONLY_WITH_ISOLATED_DRAFT_OUTPUT`。Astra依据Owner既定V010路线与工作流V1.2发放当前**低风险静态诊断**；**绝不授权任何新Python进程、HA/HJB/KFE、selector/root、pytest、MATLAB、宏观/IRF或真实数据访问**。本任务结束后仅提交修复证据供Astra验收，不得自签发新的科学调用。

## 1. 固定authority与已知两次失败

- 仓库`zcx369658780/dissertation-ch5-two-asset-hank`，治理branch`migration/astra-workflow-20261012`。
- 原V010工程候选commit `94de4501dec051b969bee9d852eba2d4591f30ef`、tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，模型与corrected数学源码不能修改。
- 单点输入仍为manifest `versions/0.0.10/corrected_ha_price_probe_v1.json` Git blob `c23d331bed34e5ca478324cdc05034609ecb91b7`，freeze `81181490495f827aa0e15e6a6efb186e8addee67`；`rah=.0675,w_eff=15.5,rb=.02`的数字和税/网格完全不变。
- 第一次单点预检task `21c736d4163a12978486c3b8256f4db8b9bd6c76`：系统GBK误读UTF-8、进程1/1耗尽、HA0、产物43519638B超32MiB 9965206B，历史不追改；
- 第二次恢复freeze `9aca1018c77d19e9489f2baf59c02bc654923999`/blob `95843d1ec838f52b056a8ca768d3f4cc55022b6f`，执行task `042195e633dec2eec532ab1b56da9822e912afe3`/blob `000a7089183178e9014e9721f45c1f947e2290b1`：Codex报告Windows子进程 argv 守门误拒**首次只读Git核验**，新进程1/1，HA0，artifact117446B，不曾新超额；原17份证据无改（CODEX_REPORTED_WITH_LOCAL_RECEIPTS）。
- [最新Astra限域验收](corrected_ha_recovery_argv_preflight_review_20261016.md)。不得把`process`消耗与`HA`实际调用混同。

## 2. 精确local SOURCE_ONLY 输入和审阅边界

优先只读：
`D:\ProjectTemp\ch5_v010_corrected_ha_price_probe_recovery_20261016_01\V010_CORRECTED_HA_ONE_SHOT_RECOVERY_RESULT.md`；
该目录中本轮私有runner、子进程guard定义/调用、被拒绝Git核验的**既有**错误摘要/进程回执；必要时只读其源绑定清单/最小manifest；首次GBK失败目录仅限核查已出具的旧失败记录/哈希（不需要重新读17份raw，不允许扫描大文件）。可读取已存在固定candidate下**精确Python runner入口/模块导入**以核对预检前真实可调用依赖，禁止遍历reports/.git对象与其它项目。

总只读文件≤12件、正文读取≤4MiB、用时≤60分钟。私有路径/环境信息若敏感只写脱敏命令结构与SHA，绝不公开记录Windows用户名、凭据或原始异常bytes；任何对象大到无法限界，STOP。

**只允许在新的独立scratch根** `D:\ProjectTemp\ch5_v010_windows_git_argv_guard_static_20261016_01` 写**最多3份**纯文本/静态源方案（总≤1MiB，UTF-8/LF，排他新建）；不得触碰两次原runner目录原字节或历史model工作树，不安装软件/改OS配置/写Git，不能为静态任务使用历史science预算。新scratch中若附`.py`只能作为**未执行源草案**、绝不可import、py_compile或启动它。可以用PowerShell既有文本工具作读取与字符串比对，但**不得运行`python`, `py`, `pytest`, MATLAB或任意科学模块**。Git如需读取身份只准精确非改写命令，不得fetch/checkout/reset/stash/add/hash-object -w/clean/commit/merge/push或在原dirty树中操作。

## 3. 必须找出的实际失败点和最小静态修复

A. 在原runner中准确定位Windows`subprocess.run/check_output/Popen`的**拦截器**和首次只读Git核验的**调用站点**（文件哈希、行号、callee、cwd、`shell`取值、原本允许的Git子命令）。从已有回执**只读**抽取被拒的真实argv结构及拒绝理由，明确它是字符串、列表还是元组、可执行名`git/git.exe/绝对路径`、是否含`-C`、Windows路径或PowerShell转义；取不到就标`NOT_IN_EXISTING_RECEIPT`，不可臆造一个路径或根因。

B. 给出**一份**最窄可验证的guard修复草案，只允许明确的read-only Git identity动作：例如`git [-C <exact_safe_candidate_root>] rev-parse HEAD`、`rev-parse HEAD^{tree}`、必要时只读`hash-object`（**不带 -w**）；依真实需求确定，不为方便放行任意Git/Python命令。固定目标root必须是原受控candidate独立clone，且校验Git SHA/tree，绝不指向历史dirty仓；`shell=False`、严格argv token数组、识别已证Windows`git.exe`合法可执行名及可接受参数顺序，所有其它子进程默认拒绝。不允许仅把guard全局关闭或添加任意通配符、shell=True、`cmd /c`、`powershell -Command`广泛豁免；`git status`、fetch、checkout、reset、add、commit、push、clean等不在许可中。

C. 在不执行Python的前提下，以真实被拒argv和至少6类显式反例制作**静态allow/deny用例表**：相同只读git实参的Windows合法表示应allow；带不受保护cwd、写Git、未知exe、shell=True、参数插入、路径绕过/ `hash-object -w`应deny。这里仅为**静态评审**，不是runtime PASS；如无法仅凭静态源码证明，明确需要未来独立工程preflight过程，不能将source scan冒充通过。

D. 检视runner内是否仍有无显式UTF-8的文本读取、异常byte展开、写前quota遗漏；只报告真正证据定位和可能受影响的I/O边界，**不得修改科学方程或selector**。对现存runner缺陷作同任务内集中修复提议，而不是再次大范围规划、修改冻结合同或随机换参数。

E. 交付一份可直接验收的`V010_WINDOWS_ARGV_GUARD_STATIC_REPAIR_RESULT`，列真实被拒argv摘要及类别、执行器bug的证据强度、唯一repair草案哈希/行段、静态allow/deny矩阵、旧两次process/HA/输出分别记账、操作命令/读写对象、所有未知与保护状态。对是否可安全发放下轮短工程preflight检验写`STATIC_READY`或`BLOCKED`，但不自授`RUNTIME_PASS`。

## 4. 终止和后续门

若无法定位既有argv/runner、文件保护风险、读取配额达到、合同需改变或必须运行Python才能验证，立即`STOP_AND_REPORT`；不另做调参或科学执行。

任务终点：`WAIT_ASTRA_V010_WINDOWS_ARGV_STATIC_REVIEW / STOP`。第三次Python科学任务只可由Owner在单独审核后**前瞻性重新授权**，最好分离一个仅工程preflight Python与一个真正HA科学进程；此前两次1/1进程永久消耗，不得重名恢复。

原A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、real C8 A–D REQUEST_ONLY，V011 NOT_STARTED，原D盘8dirty/index/external common-dir及所有私有证据保护不变。
