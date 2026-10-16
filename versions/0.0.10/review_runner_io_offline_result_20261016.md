# V010_RUNNER_GUARD_IO_OFFLINE_INTEGRATION_RESULT

状态：ENGINEERING_STATIC_DRAFT_READY；ENGINEERING_RUNTIME_NOT_RUN；HA_SCIENCE_NOT_RUN。PRE_SEAL候选说明；只供Astra独立审阅，不自授工程或科学PASS。完整草案未由Codex运行、import、py_compile或AST解析。

## 固定权威与原证

任务commit `50fece7d51bbcbb7e4384b0a5a8833b81dcbf76b`，tree `c79f874a1ea60f3a880114fd5d80b0861e6ca21e`，任务blob `0070437d83eccaaf4a1c38838e9ce2b1a2fb5634`；读取时治理HEAD匹配。独立原文件审阅blob `3d6709d80ce2a8eb85cca1e1242372f6d8cdbafc`指出P0-A至P0-E，本候选一次集中回应。

前静态报告SHA256 `27CD9B23FC7032E523E0D397D2E7FAF05BD99B500E4CB8E6487AA98B20EC1151`、前草案SHA256 `A021AFD81CE1342290A8C8387C0B49383CAE20C66B00F46336F220DB546B1C5C`匹配Owner上传身份；前46例定义中的原24项来自既有逐项JSON。旧恢复runner SHA256 `4050F1E36B3FF31479960FDF5365A0DC5ADD0AD94A3BCAA31DBF24CEA7CAFF7E`仅只读，未修改。历史审计事件实际argv仍NOT_IN_EXISTING_RECEIPT，本轮没有重建成实测事件。

模型candidate `94de4501dec051b969bee9d852eba2d4591f30ef` / tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5` / parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`；原plan blob `85138d8859d53295262fe13bf5bc277bca95ed3f`、manifest blob `c23d331bed34e5ca478324cdc05034609ecb91b7`保持不变。没有新价格点，没有修改经济学/selector/HJB/KFE/网格/容差/fixture。

## 五项P0的离线集成

| 义务 | 新草案实际结构 | 静态资格 |
|---|---|---|
| P0-A 真实Git身份 | GitGate.verify内部顺序执行4条精确只读身份命令，只有bounded_child实际stdout、退出码0、审计nonce消耗与reap记录匹配时才设置私有verified；没有可注入预置输出的identity_outputs接口；verify不可重试、全局Git child最多5次 | 设计已落源，未运行 |
| P0-B 实际导入字节 | source ls-tree仅身份完成后，且使用固定commit而非动态HEAD；VerifiedLoader对实际磁盘原字节计算Git blob并将同一raw编译，禁止pycache/未跟踪模块；9必需模块复核树blob、实际__file__、专用loader与raw SHA | 设计已落源，未运行 |
| P0-C child I/O | stdout/stderr双reader每次最多读取剩余额度+1探测字节，探测超限不入buffer；身份stdout4096B、source inventory1MiB、stderr4096B；30秒timeout，Windows kill-on-close job与finally kill/wait/join；失败同样保存有界proof | 设计已落源，Windows API/回收未测 |
| P0-D 完整hook | 新进程唯一hook注册点，spawn capability绑定绝对exe、cwd、净化env与shell=False；只认token精确数组或批准数组的list2cmdline；同hook限制read/write/mkdir/rename及拒绝其他写入 | 设计已落源，不称OS sandbox |
| P0-E 初始化/终态/配额 | 初始化纳入总try；显式UTF-8；未知异常不str/repr；JSON编码后预占容量、排他临时文件+Windows不覆盖原子rename；正常写预留2MiB，final实际最多1MiB、应急最多64KiB；日志reservation只转移一次；watchdog以独立daemon尝试日志后无条件退出 | 设计已落源，故障分支未运行 |

四条身份tail是HEAD、HEAD tree、唯一parent、绝对common-dir；source inventory第五条限定固定commit的src子树。没有status、hash-object、网络或写Git权限；发布本静态候选的Git操作不属于未来runner白名单，也不由该runner执行。

源码认证现在严格比较**磁盘原字节**Git blob，不自动做CRLF归一化。若未来环境实际字节不匹配就STOP，不能为过门修改模型源或静默改换导入副本。其他项目包transitive模块也只能从该固定tree的已认证原字节加载；九份必需源映射全部写入草案NEEDED。

I/O wrapper仅替换native seal_json，不改变任何数学函数。输入以固定原manifest的完整ha_inputs构造HAInputs。one_ha中只有一处solve_conditioned_household调用；调用账先持久扣1，finally保留root/cell累计；mode默认ENGINEERING_ONLY，ONE_HA还需未来独立科学授权。当前没有执行任何模式、没有获得未来调用许可。

## 46项完整机读定义

原A01–A08与D01–D16逐项包含typed request、计划argv、审计事件、状态、child proof、source及I/O结构；均给出ALLOW/DENY期望、源代码guard anchor和后置条件。分组反例另附RFC6902 replace子用例，不靠一段文字描述替代输入。所有runtime_execution均NOT_RUN、runtime_pass均false。

新增N01–N22覆盖：调用者伪造identity_outputs、dirty磁盘源码、stdout超限、stderr膨胀、timeout/reap、非零exit、rename故障、日志事务reservation转移故障、旧hook叠加、无效UTF-8、总配额/终态上界、watchdog日志失败、不可信I/O、未跟踪模块、第六Git child、动态HEAD inventory、verified伪造赋值、来源路径/loader错配、旧输出root与导入期科学调用。

PowerShell仅核了JSON结构、46唯一ID、24+22计数、完整输入字段、source anchor存在、单一HA调用点、单一hook注册点、UTF-8/LF及脱敏规则。没有执行用例逻辑或验证Python语法/Windows行为。草案生成阶段发现PowerShell自动变量input与生成器参数冲突，静态JSON检查立即发现缺输入；在新草案封存前恢复所有46项完整输入并记录，未触任何旧原证或调用预算。

## 剩余条件与明确边界

1. 未来独立工程preflight必须先核新草案语法、真实Windows Popen审计形态、Job Object创建/分配、timeout/reap/reader退出、loader原字节导入与所有故障回执；本轮没有runtime证据。
2. 机器、Git安装、Python运行库和独占新输出root必须可信且无并发恶意替换；配置不承认这些I/O闭包假设时runner直接STOP。Python audit不是OS sandbox；Windows Job分配前的可信进程窗口及底层Git执行链没有敌对保护证明，A16未解除。
3. 若连新的输出根都不可创建，代码只能返回STOP；未来启动器必须在进程启动前保存自己的唯一进程扣账/退出见证。不能凭一个无法写入的目录保证存在磁盘回执。
4. 当前静态代码的配置路径全部为中性配置参数，没有嵌入私有环境。所有科学分支仅是未来单独授权后的源码结构；当前Python/工程runtime/HA权限始终0。工程独立验收后仍须Owner另发科学许可。
5. 本轮不自授I/O运行通过、HA条件稳态、GE、IRF或Results。若独立复审发现关键I/O闭包仍缺失，保持STILL_BLOCKED，不放宽权限救PASS。

## 账本及保护

本任务Python/py/pytest/py_compile/import/Jupyter、HA/HJB/KFE/selector/root、macro/IRF/MATLAB、真实数据读取全部0。只读既有小型runner/草案/报告/机读JSON、固定candidate单个入口和固定GitHub任务/验收文档；没有遍历reports、原dirty树、C8/B3、MAT或旧V009失败数组。只有新scratch草案和本任务指定review分支有新增写入。

历史原实施账保持driver1/4、HA1/26、pytest4/6、cells1626、roots1642；首次单点Python1/1 HA0、43,519,638B、超额9,965,206B；恢复Python1/1 HA0、117,446B；此前静态Python/HA0、33,576B。无预算重置、无第三次科学尝试。原dirty/index/common-dir/untracked/ignored不访问不覆盖。

## 脱敏发布合同（PRE_SEAL）

仅向review/v010-runner-io-offline-20261016发布本摘要、不可执行txt示意源、机读JSON三文件，单一parent为本任务发布commit；不改治理/main/原科学candidate。分支已存在则停止，普通non-force push一次，随后读回commit/tree/parent与3个blob/文件哈希。最终Git身份和本机字节/时间/读写账保留在候选外DELIVERY_RECEIPT，避免SHA自引用。

本地最多5文件、artifact<=2MiB；如需独立发布Git工作区，非共享common-dir、<=2GiB，单独核账。静态发布资料检查绝对私有路径、Windows用户目录、秘密标记及raw log；不安全则LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED。

A16 FAIL_CLOSED；window UNACCEPTED；C9 PAUSED；CALL_LEDGER UNRESOLVED；model_activation=False；Results FALSE；real C8 A-D REQUEST_ONLY；V011 NOT_STARTED。

WAIT_ASTRA_V010_RUNNER_IO_STATIC_INTEGRATION_REVIEW / STOP
草案SHA256：3FF7B5D6FBEF57CE851C327EA5C6E6CA8200C852A3C1629586F3AC584FACFF11
机读用例SHA256：5B7D1B661FFF84F5844B15AE5104307B0FDEA0A23F70B809FBAC7A29E351A1CC
