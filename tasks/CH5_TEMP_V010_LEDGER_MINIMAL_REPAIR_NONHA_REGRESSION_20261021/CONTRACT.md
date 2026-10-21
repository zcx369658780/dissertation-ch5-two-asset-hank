# CH5 TEMP V010｜生产Ledger真实Budget最小修复与无HA隔离回归（单张长任务）

TASK_ID=CH5_TEMP_V010_LEDGER_MINIMAL_REPAIR_NONHA_REGRESSION_20261021
REVISION=ISSUED_20261021_R1
SCOPE=PRIVATE_DERIVED_REAL_BUDGET_MINIMAL_REPAIR_PLUS_ISOLATED_NONHA_REGRESSION
OWNER_APPROVAL=2026-10-21明确同意继续上一轮建议的真实ledger最小修复和无HA回归
SCIENTIFIC_SOLVER_BUDGET=0

## A. 目标与正确的完成分类
上轮已独立验收的真实旧方法隔离证据（终审docs/CH5_TEMP_REAL_LEDGER_NONHA_INTERFACE_FINAL_INDEPENDENT_REVIEW_20261021.md）显示：append后checkpoint在WinError5时可残留current.next阻断重试；finish二次失败可能遮盖首次错误；原run以E2_文本判断共享硬故障会漏掉plain PermissionError；STOP在event append之后/持久checkpoint和惰性entry之前发布时出现局部准入竞态。原constructor拒绝已存在目录符合one-shot设计，不能未经决定改成自动resume。旧方法测试结果限于受控Windows、原AST身份和惰性哨兵，不等于完整生产supervisor/reader/HA已被Astra直接运行。
本次在新scratch建立**从原始factorial_driver.py派生的受限修复候选**，尽量保持原方法最小diff，T1—T6旧用例加J1/J2有界回归。只有事件账、首错分类和准入在隔离接口通过才可称`ISOLATED_REPAIR_REGRESSION_PASS__NOT_DEPLOYED`；任何明确未消除的旧缺陷或违反账本不变量要诚实报告`CHANGES_REQUIRED_IN_CANDIDATE`、`PARTIAL_REPAIR`或`STOP_SCOPE_REQUIRED`，不为了绿色结果增大权限或隐藏首错。
**本轮不得直接修改原生产文件/旧journal/正式V010，也不部署/切换实际TEMP runner。** 修复候选是可追溯的新scratch派生源码、patch及无HA实验，原真实生产全链仍UNVERIFIED，A1–A3数值预算0。

## B. 冻结输入
首先读取治理live ref并在同一HEAD核CURRENT.md、TASK_CURRENT.md、docs/DOC_INDEX_CURRENT.md唯一ACTIVE；发行manifest在后发release commit，本合同和参数在`issue_commit`，旧review fixed parent与动态治理head不同，不混用。6份精确Git历史文档commit+blob按TASK_PARAMETERS只读。
历史私人原档 `TEMP_V010_PRICE_BRIDGE_FACTORIAL_100_PRIVATE_FINAL.zip`，字节1214713，SHA256=`f3e8984fe4d2ef4be65692c27fa7594d96b870d372a8c45d029899f7891841d8`。只能在参数列明旧scratch下4条精确相对路径stat：唯一普通非reparse文件+原字节SHA匹配后才能查ZIP中心目录（≤300成员），只解码 `factorial_driver.py`（12102B，SHA `2f956b9c1495d1026b23b219da059681b9cdd98fadb9233acf02154559ddf456`）和必要的`temp_driver.py`静态部分（16549B、SHA `c4f6aedfc9ae22afc5e2ddc59d490eee29267049de132090d36df93f0a42e001`）。无第二身份匹配者，不猜改名、不全盘glob、不读私人HA数组、旧491/158/910压缩包、不公开旧原件。
上一轮已接受的公开ZIP可按历史commit `95e283f9a7fd5bc4bee1b1d9e56eb5afc4442792`精确路径回取（Git Blob `a611622093efccbcefd4b9936cc5bafc4ea72f9b`、34287B、SHA `2076ce9ab27dec42f2c4ecd3a7c42ab6efbb73d0f9473dcdbf4d7a3b002ed4a4`）；只读参数明确的harness/AST/测试成员复用，禁止root recursive tree，不按清理后review HEAD读取旧临时文件。来源不存在或无法安全AST隔离即止于`SOURCE_UNAVAILABLE/STOP_UNSAFE_BOUNDARY`并保留静态可证部分。
BOOTSTRAP0先可信父链/保护root locator/index有限只读stat和新scratch不存在；BOOTSTRAP1独占创建；BOOTSTRAP2首次日志写前二次身份确认。新patch、修后私有原件、全测试和安全报告仅写参数的新scratch。保护目录before/after hash可测则记真实，不可测为UNKNOWN，不能记0。

## C. 最小修复合同（允许改派生候选、不动原生产）
R1 **checkpoint/original prefix**：以事件append+fsync/seq/previousHash链作为事实，把`current.json`与`current.next`标明old prefix、valid staged、invalid/ambiguous的独立状态；首次WinError5保留原现象，只有真实逐字节/链可证明是同一预期后继时才安全完成幂等reconcile，否则FAIL_CLOSED并保留私人原件。不能盲删/覆盖current.next、伪造成功checkpoint、重复追加已持久事件、从旧科学预算直接重启。
R2 **首错保全与计数**：primary异常不得被后续`finish`二次exception覆盖；error diagnostic可失败但原原因、stage和相关链仍在私有记录；active/failure/unresolved/charged/entered/completed必须真实与持久事件分账。不能将一次科学HA计费/失败算成成功返回（测试HA只惰性marker）。
R3 **结构化共享E2硬故障**：定义最小typed fault(或结构化枚举)，覆盖WinError5/PermissionError的checkpoint拒绝、无法证明的ledger divergence和STOP unsafe等真实硬门；源run的`E2_`文本判断须至少形成可审的安全候选/静态比较，禁止为了抽取原full run而执行原科学程序。未知可能破坏共享状态的故障fail-closed，非硬门E1不得无限扩大成全局停止；保留文本作为展示而非权限判定唯一依据。
R4 **STOP准入线性化**：在受控单写者/发布者遵守同一fence协议时，以可复核同步与持久化，阻止STOP被确认之后的新成功持久扣费和惰性entry；测试pre-STOP和已同步发布的竞态。若真实外部supervisor/reader未纳入协议，必须标`LOCAL_FENCE_ONLY__GLOBAL_STOP_UNVERIFIED`，不能宣称仅加thread lock就保证跨进程全局STOP。
R5 **one-shot边界不变**：旧constructor已有目录拒绝原则不放宽；若确需跨进程resume，另报E3，不擅启历史checkpoint/旧run；派生候选若扩到temp_driver、宏观方程或未列保护文件立即STOP_SCOPE。

只允许对参数列出的必要Budget方法及安全的run错误分类辅助方法做最小AST/patch；源行和变更函数需有source hash、AST digest、逐hunk理由、公开最小必要脱敏diff。完整老源码、私有journal和私有绝对路径不公开。

## D. 无HA回归与可证伪STOP
沿用T1–T6语义并增加J1/J2。必须对相同合成输入跑original旧方法和patched派生方法成对对照，记录预期缺陷在original仍复现、patched改善哪些性质；不允许把original失败当patched自动通过，也不允许跳过负例。
- T1：单写者事件链/三个新目录与原constructor重复目录拒绝非回归。
- T2：checkpoint fail后staged残留、正确前缀恢复（无重复事件）/损坏staged fail-closed。
- T3：Windows无读者与受控reader两种share模式，实际native error和close后恢复；不得宣称历史读句柄唯一根因已确定。
- T4：secondary finish失败仍暴露primary，plain WinError5 typed hard STOP能被识别；完整原run不执行，新增 helper 的安全可用性和真实生产接线仍需单独集成。
- T5：已经存在STOP及竞态发布时的持久计费/内存计费/惰性entry分账；只有参与共同fence的writer/publisher才可声明局部线性化，真实supervisor/reader UNKNOWN。
- T6：受控子进程exit与reap、charged/entered/completed/failed/unresolved，保留原one-shot不提供未经授权恢复。
- J1：JSON损坏、短写、事件prevSHA/seq错误、重复`current.next`、一半写入应全部FAIL_CLOSED，不构造伪造事件或修改历史密封原件。
- J2：合法成功checkpoint重复调用与幂等恢复不增加持久事件、不允许先读到尚未完成的旧staged并误认committed。
Windows计时小于分辨率时使用显式同步/QPC，不将时钟UNKNOWN编为0。只有已授权的无HA测试自身进程/线程可创建、回收，不调用生产HA/driver/full run或original old ledger。

## E. 有界资源和E1
总≤14400秒（4小时），verification≤1200、engineering≤9600、delivery≤2700，整体仍以总上限/最后180秒封存为硬门；工程Python≤32、focused pytest≤8、direct starts≤140、owned helpers≤14并发≤3、E1≤4批，每组最多3次；新非Git文件总量≤64MiB。原WinError5故障复现是**预期负例**，并非失败资源超限。所有调用先扣费，内核后代不可观测记UNKNOWN。科学HA/HJB/KFE/GE/IRF及science drivers总预算皆0。不安装依赖，不搜索全仓库，不越权跑real dates/provinces。
若4批E1或安全门已耗尽，保留足够原始首错/patch及安全回执后STOP，不为赶PASS复活旧额度、不无限修脚本。

## F. GitHub临时证据自动上传（Owner再次强调：强制）
**Codex必须自动将逐成员脱敏的`evidence_sanitized.zip`，连同`result.md`和`manifest.json`，上传到GitHub仓库本任务独立Review分支`review/ch5-temp-ledger-minimal-repair-nonha-20261021`上的临时目录`_review_tmp/ch5/temp-ledger-minimal-repair-nonha-20261021/`，只允许这三件文件。** 固定候选sole parent=`f34cbd06e613481bf185d839a7e319e30cfc192f`（不是新发行后的live治理HEAD）。必须远端回读commit/tree/sole parent、精确三件Git Blob、原始bytes、所有ZIP成员CRC/长度/SHA256及公开隐私。只提供本机路径/本地自检不能称已发布；默认也不要求Owner复制文件手工中转。
优先有权使用的现成Git Data API精确blob/tree/commit/new ref，若API端点/认证/政策明确拒绝立刻STOP，不改账号或切SSH绕过；仅客观无API写能力且预授权SSH可用时用限域SSH路径，不能root recursive、克隆整个仓库、强推、重写已有review。每个公开文件在发行前脱敏与逐成员隐私门。审阅原始ZIP、完整私有旧源码、真实journal和绝对Windows私有路径一律不得发布；可公开最小新patch与安全测试源码、合成fixture、必要审查原件。
新候选`review`发布后不能由Codex清理，等待Astra独立终审，PASS/CHANGES_REQUIRED先永久归档回读，再仅非强制删除三文件并读回404。只有Astra二进制校验的I/O受限时，标`REVIEW_PENDING_IO`且保留；不得误认为Codex没上传或要求重推。
其它两份历史review分支保持`REVIEW_PENDING_IO`，严禁触碰：
- 4e05976bbc8068b971ba5915133e9a6c3b73193d
- 1579e7f1d7a1975c322dd6ae9af1776e88e83e7c

## G. 最终回执与停止
终态交付：修复范围、冻结输入的原字节核验、patch的source/AST身份、8组旧/修成对原件、持续fail-closed账本验证、native WinError5/STOP数据、所有首错/E1与资源账、安全/隐私/前后保护hash、确切生产集成缺口。分别给`PATCH_PREPARED_NOT_DEPLOYED`、`ISOLATED_REPAIR_REGRESSION_PASS/DEFECT_REMAINS/PARTIAL/STOP_UNSAFE`、`GLOBAL_SUPERVISOR_UNKNOWN`、`HA_CALLS=0`，不能把通过称`PRODUCTION_READY`。
输出最终JSON完整Base64及真实bytes/SHA256、run_id、actual_terminal、new_candidate_sha/tree/parent、remote三原件哈希与zip成员、独立外部controller completion event。预定停点`WAIT_ASTRA_LEDGER_MINIMAL_REPAIR_NONHA_REVIEW`仅为计划；实际STOP优先。不得签发下一任务或自动运行A1–A3。
