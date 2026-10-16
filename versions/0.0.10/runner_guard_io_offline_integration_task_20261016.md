# V010 runner守门器与I/O全闭环：单轮离线工程集成 + GitHub脱敏候选

**任务ID**：`V010_RUNNER_GUARD_IO_OFFLINE_INTEGRATION_AND_SANITIZED_GITHUB_HANDOFF`。
**权限**：Astra以Owner既定V010工程改进方向发布此**非科学、不可运行**的限域工程任务。此前两次Python科学进程各1/1已经消耗且HA均0。本任务**新增Python进程=0、HA/HJB/KFE/selector/root/pytest/MATLAB/IRF/真实数据读取=0**，**不开放任何工程runtime Python**。Codex只能查看既有小型原证与编辑**新隔离草案**，提交静态去敏报告供Astra独立复审。

## 0. 固定输入与已独立审核的依据

- Github仓库`zcx369658780/dissertation-ch5-two-asset-hank`；治理分支`migration/astra-workflow-20261012`仅为review/task权威。
- 原代码工程候选SHA `94de4501dec051b969bee9d852eba2d4591f30ef` / tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，原V010科学冻结plan blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；单点输入原manifest blob `c23d331bed34e5ca478324cdc05034609ecb91b7`、`rah=.0675,w_eff=15.5,rb=.02`。都不可改。
- 前次SOURCE_ONLY任务固定commit `de244919a556a04929ecd73c3406881bae3c3e79` / blob `3d3a0520d001b7fe71d112fe33627fdf486db4d0`，其本地报告与`windows_git_guard_draft.py`**现在已由Owner上传给Astra**。Astra确认报告原始文件SHA256 `27CD9B23FC7032E523E0D397D2E7FAF05BD99B500E4CB8E6487AA98B20EC1151`、草案SHA256 `A021AFD81CE1342290A8C8387C0B49383CAE20C66B00F46336F220DB546B1C5C`，草案静态AST parse PASS，**没有任何Windows runtime**。
- 必读[上传原文件独立静态验收](windows_git_guard_uploaded_primary_review_20261016.md)。其P0-A到P0-E列出身份输出联结、磁盘源码字节、bounded child pipes/timeout/reap、完整audit/I-O全闭环、runner旧错误初始化/预留/配额等。必须**一次集中集成**, 不再重复Source-only广泛调查，也不能仅重写一份任务复述旧失败。
- 当前旧`recovery_runner.py`准确本地路径与前次静态摘要见上次报告；此轮必须只读该旧runner及24例配套JSON，核对每个具体缺口。**旧实际audit argv没有被记录**，不要伪称重建为实测。

## 1. 仅离线静态草案实施：不可启动Python

只允许读取：
- 先前独立runner源码及已存在静态草案/report/24例JSON，最多12件非敏小文件，正文累计≤5MiB，墙钟≤3小时；
- 候选已冻结的必要单点HA import入口和已有固定GitHub任务/验收docs；不得遍历原数据树、reports目录、MAT文件、旧C8/B3或.git对象。
- PowerShell本机文本编辑、文件hash、静态字符串/JSON核对可用；**禁止任何`python`/`py`/`pytest`/`py_compile`/`import`/Jupyter/MATLAB/科学模型调用**；不运行新的runner或任何子进程工程模拟，不安装包/更改Windows/PATH/config。

在新隔离scratch
`D:\ProjectTemp\ch5_v010_runner_guard_io_offline_20261016_01`
创建不超过5份 UTF-8/LF 文件、累计≤2MiB，原文件排他保留且不覆写：
1. **完整新的runner离线候选**（`.py`仅文本草案，从未执行）：替换旧subprocess守门分支而不叠加旧sys.audit hook；Git请求/审计精确exe/cwd/env/shell=False、一次性event capability、window token vs exact list2cmdline、最小只读命令白名单；记录事件类型/哈希而不泄露整个私有命令字符串。
2. 真实Git child身份完成前`verified=False`；绑定4条身份read-only命令的**有界stdout/stderr、timeout、exit code、capability使用记录**，源`ls-tree`仅在4条身份已通过后可运行；`identity_outputs`不再可单独靠调用者传入预置预期值就解锁状态。
3. **真正导入源码字节绑定**：除`ls-tree HEAD`外，还必须对9份磁盘`Path.read_bytes`计算Git Blob SHA，核路径与`__file__`、在同一固定候选树，不得依据动态HEAD/pycache/未跟踪副本；只读、不写.git/index/原受保护tree。
4. **I/O全闭环**：全部输入明确UTF-8、未知异常不`str(exc)`携bytes；stdout/stderr流量在入内存前限制，每个child有timeout/reap；受界JSON writer在UTF-8编码完之后先校文件/路径/累计字节，再排他原子写，异常也做保底；final回执预留容量不得小于真正最坏写入限；bootstrap和watchdog即使日志失败也要STOP；拒绝reparse/dotdot/不可信写入闭包，不能把Python audit称OS沙箱。
5. **24例静态矩阵扩充**：真实A01–A08/D01–D16逐条提供完整**脱敏输入结构、ALLOW/DENY预期与guard分支映射**，再至少追加针对`identity_outputs`伪造值、dirty磁盘源码、child输出超限、stderr膨胀、日志事务失败与旧hook叠加的DENY/STOP静态表。全部为静态设计，不是PASS。**不能重跑旧24例或标记runtime通过**。
6. 针对固定候选模型HA入口重新审输入/输出**只读代码位置**，证明新runner真正只调用`solve_conditioned_household`至多一次且0 macro/IRF；这里只是源码结构承诺，**不执行**。
7. 显式区分`ENGINEERING_STATIC_DRAFT_READY`、`ENGINEERING_RUNTIME_NOT_RUN`、`HA_SCIENCE_NOT_RUN`；若I/O任一关键保护尚不可设计成闭包，必须报`STILL_BLOCKED`，不为结果改宽权限。

## 2. task特许：脱敏产物GitHub提交，解决人工文件转交

**这是本任务专属、范围明确的GitHub文档交付许可，不修改长期V1.2、也不是追认上个任务禁止push为“忘记”。** 仅发布可公开的、经本地查隐私/秘密/绝对路径审计的资料到独立review分支（不发治理/main/原代码候选分支）：
`review/v010-runner-io-offline-20261016`，从本任务签发commit单一父构建，**普通non-force push至该新branch一次、回读验证commit/tree/blob**，遇已有同名分支STOP而不force替换。
唯一允许的3个Git文件：
- `versions/0.0.10/review_runner_io_offline_result_20261016.md`：不超过30KiB的脱敏实施/静态审阅摘要、所有未验证、真实调用0、旧预算与来源hash；
- `versions/0.0.10/review_runner_io_offline_static_draft_20261016.txt`：**不可执行**的脱敏示意源文本（本地绝对路径/私人环境标记替换为中性符号，承诺无 secrets、hostnames、raw logs、Windows账号路径）；
- `versions/0.0.10/review_runner_io_offline_static_cases_20261016.json`：静态用例完整明细，仅预期、无成功运行冒充；
不得推`D:\...`私有原始runner、超额日志、未经脱敏argv、用户目录、真实C8/B3、模型Python tracked更改或测试产物。若不能安全脱敏，**不push**并交`LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED`；不得为了满足GitHub交付硬推私人证据。GitHub候选只作Astra独立审阅，不自授任何工程或科学PASS。远端branch只存安全静态材料；如需Git工作区，限新独立非共享common-dir clone，≤2GiB，不触原8dirty旧树；新artifact+证据≤2MiB不含独立clone，计字节如实。

## 3. 旧损失与新的停止资格

永久分账：V010原实施science driver1/4、HA1/26、pytest4/6、selector1626/root1642；第一次单点probe Python1/1 HA0、artifact43519638B，超旧32MiB 9965206B；第二恢复Python1/1 HA0、artifact117446B。此前静态SOURCE_ONLY Python/HA0/0、产物33576B。**本任务科学/工程Python运行/pytest预算一律0**；不得用旧剩余额度执行。

最终报告`V010_RUNNER_GUARD_IO_OFFLINE_INTEGRATION_RESULT`，状态`WAIT_ASTRA_V010_RUNNER_IO_STATIC_INTEGRATION_REVIEW / STOP`。即使静态草案完善，工程Windows preflight进程仍需要Owner另行批准；HA科学只能在工程预检独立验收后再次单独授权。V011 NOT_STARTED、model_activation=False、Results FALSE、真实C8 A–D REQUEST_ONLY、A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED及原8dirty/index/common-dir/untracked/ignored保护不变。
