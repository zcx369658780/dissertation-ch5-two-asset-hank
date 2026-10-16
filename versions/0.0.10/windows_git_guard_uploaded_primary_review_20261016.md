# V010 Windows Git argv guard：Owner上传原始报告与静态代码的Astra独立审查

日期：2026-10-16（Asia/Shanghai）。
**审议分类**：`INDEPENDENT_STATIC_SOURCE_REVIEW_COMPLETE__GUARD_DESIGN_CONDITIONALLY_SUPPORTED__FULL_RUNNER_IO_BLOCKED__NO_RUNTIME_AUTHORITY`。
**结论**：支持继续完成独立runner的工程离线集成；**不**认定本草案可以执行、24个案例已经PASS、现有恢复runner已安全或HA点已经验证。

## 1. 本轮独立读取的对象和证据层级

Owner已在ChatGPT当前会话上传两份实际源文件，Astra直接读取原始UTF-8字节，独立计算：
- `V010_WINDOWS_ARGV_GUARD_STATIC_REPAIR_RESULT.md`：9,998字节，92行，SHA-256 `27CD9B23FC7032E523E0D397D2E7FAF05BD99B500E4CB8E6487AA98B20EC1151`。
- `windows_git_guard_draft.py`：7,540字节，157行，SHA-256 `A021AFD81CE1342290A8C8387C0B49383CAE20C66B00F46336F220DB546B1C5C`。
- 两份源文件均可严格UTF-8解码、LF换行；Python draft由Astra用`ast.parse`做**纯语法解析PASS**，未import、未实例化、未注册audit hook、未调用Popen、未执行任何模型或Windows进程；源顶层为docstring/import/常量/函数/类，不含自动执行入口。
- 24例在上传的MD中只有分组预期：A01–A08共8类ALLOW，D01–D16共16类DENY；配套逐项JSON**本轮没有上传**。因此可验证“报告列有24个预期类别”，不能独立认定24项实际用例已被机器校验或静态结果全PASS。
- 报告中的旧`recovery_runner.py`第91–96、215–218、257、369等行，以及旧receipt SHA，仍属`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`：该旧runner与逐项JSON未作为此次附件，Astra**没有**独立读取旧runner或历史Windows事件。
- GitHub仓库此前独立确认冻结任务 `de244919a556a04929ecd73c3406881bae3c3e79` / task blob `3d3a0520d001b7fe71d112fe33627fdf486db4d0`；原V010模型候选 `94de4501dec051b969bee9d852eba2d4591f30ef`、tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，新价格manifest blob `c23d331bed34e5ca478324cdc05034609ecb91b7`，旧冻结计划blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；均不因静态审核变化。

## 2. 上传Python草案中已独立核实的正确方向

- `windows_git_guard_draft.py:25–34`严格限定4项只读身份Git tail和身份核准后的唯一`ls-tree`；没有`status/fetch/checkout/reset/clean/add/commit/push/hash-object -w`等命令。
- `:43–59`对请求path做Windows绝对/字面身份核对，检查dot/dotdot、UNC、device、ADS及祖先reparse标志；尚不是充分的OS沙箱或原子文件操作保证。
- `:88–106`固定Git可执行、工作目录、环境、`shell=False`及tokenized argv，预计算`subprocess.list2cmdline`；`:108–125`针对`subprocess.Popen`审计事件只接受与已准许的tuple/list或Windows精确渲染字符串，拒绝其余命令形态，使用线程本地一次性spawn capability。没有解析任意命令行字符串、没有全局关闭audit。
- `:136–150`仅定义`spawn_identity`，没有挂载hook或执行，草案顶部明确UNEXECUTED。这些静态方向可作为**下一轮离线集成参考**，不代表Windows实测兼容。

## 3. 独立发现/确认的未闭环阻断项（先修再讨论工程进程）

**P0-A：Git输出身份链未封闭。** `:76–86`的`identity_outputs(head,tree,parents,common_dir)`接收调用方传入的标量，一旦相等就设置`identity_verified=True`；当前草案**没有**把这些值绑定到实际`spawn_identity`的有界stdout、exit code和精确命令回执，也没有身份状态机约束执行次序。未来必须在同一受界Git命令结果验证后才能设置verified；失败/异常后默认不可进入source phase。

**P0-B：Git提交树不等于本机导入源码。** `ls-tree -r HEAD -- src/...`仅证明**commit tree blob IDs**；即使HEAD/tree正确，独立clone工作区中尚可能有修改/未跟踪的实际Python源。必须结合逐文件`Path.read_bytes()` Git blob SHA/原始SHA和实际Python`__file__`、绝对路径、无reparse别名验证，把所导入九份源码的磁盘字节绑定到固定候选；禁止只用`ls-tree`冒充完整来源认证。

**P0-C：子进程I/O仍无运行保护。** `:136–148`直接返回`Popen(stdout=PIPE,stderr=PIPE)` child，无bounded pipe drain、timeout/kill/reap、单命令stdout/stderr原始大小/哈希和故障保底回执；草案的docstring/`:151–156`也主动说明该闭环未实施。在新的runner中必须预先限制读取缓冲、清理超时child，在写文件前守字节硬限；不允许无界`communicate()`。

**P0-D：audit完整覆盖未集成。** `:108–110`对非Popen事件直接return，须由**未来新runner中正确集成**其他文件/I/O audit限制，不能因此绕过；`sys.addaudithook`一旦登记不能从同一进程删除旧guard，报告要求在全新进程**替换旧hook而非叠加**是合理的安全硬门。必须记录新runner中hook安装位置、覆盖路径以及fail-close行为。

**P0-E：完整runner的I/O仍为BLOCKED。** 上传MD第66–78行据其旧runner源码报告列出：RuntimeError潜在`str(exc)`原始bytes展开、stderr无界、`Path.absolute`/is_relative_to词法路径不足、防reparse/写入闭包不完整、最后回执4MiB上限与2MiB预留不匹配、`pending`记账不回滚、初始化错误逃逸总try、watchdog依赖日志写入等。这些具体行号尚未获Astra直接读取旧runner，应在后续工程集成按原件核验和封闭，不能凭本次静态报告宣布I/O PASS。

**P1-A：Windows真实审计argv仍未知。** 旧回执没有保存实际audit层argv，报告只由旧源码重构请求方数组`['git','--no-optional-locks','-C',SAFE_CANDIDATE_ROOT,'rev-parse','HEAD']`；草案固定git.exe SHA仅代表Codex当时检查的包装可执行文件，**不证明旧child身份或底层实际执行链**。未来只有在单独批准的ENGINEERING-ONLY Windows运行中记录安全脱敏的真实event type、形态、exit code和hash才可升级证据。
**P1-B：24项逐例证据缺失。** MD的A/D矩阵是期望类别，不是可独立执行的测试断言；需在后续不含科学调用的工程回合提供逐例输入/预期与静态实现闭包，独立审核之后才可放工程运行。
**P1-C：父路径及环境虽做静态检查，仍非OS沙箱。** 对源路径根、Git内部程序执行链与路径替换的运行时风险须有明确可信机器假设和fail-close；不要宣称防御所有同机恶意进程。

## 4. 任务交付/GitHub规范与下一权威

本次Codex不是“忘记push”：前一个V010 SOURCE_ONLY任务**明文禁止Git更新或push**，所以将静态草案留本地是遵约。Astra现将**去敏审议、源SHA与门禁结论**同步治理分支；不将原私有runner、raw log或带绝对本机路径的可运行草案直接推入可能公开的GitHub。
建议下一任务仅以**单次task限域**允许把经过确认的**脱敏工程报告、24条机读静态spec、只读文本patch**发布到独立review分支；不改V1.2长期工作流、不更新科学源码、不推main/治理accepted，也不复用旧process配额。发布物必须经过secret/path/rawbytes检查，失败则停留LOCAL_ONLY并报告，绝不以备份冒充独立验收。

当前科研判断：`rah=.0675,w_eff=15.5,rb=.02`仍`UNTESTED`，历史两次science进程各1/1均止于preflight且HA=0；首次日志43519638B超原32MiB 9965206B、第二117446B在96MiB内，均保留；原V010首HA checkpoint2 F25另有历史失败证据。**不授权新的Python、pytest、HJB/KFE或HA调用。**

最新后续工程任务：[runner_guard_io_offline_integration_task_20261016.md](runner_guard_io_offline_integration_task_20261016.md)，仅在隔离工作区进行不运行的工程草案集成及去敏GitHub候选交付。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、真实C8 A–D REQUEST_ONLY、8dirty/index/common-dir保护及V011 NOT_STARTED全部保持。
