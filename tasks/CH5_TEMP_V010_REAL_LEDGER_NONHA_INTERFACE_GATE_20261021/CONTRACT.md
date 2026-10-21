# CH5 TEMP V010：真实生产Ledger原方法的无HA隔离接口验证（长任务）

TASK_ID=CH5_TEMP_V010_REAL_LEDGER_NONHA_INTERFACE_GATE_20261021
REVISION=ISSUED_20261021_R1
SCOPE=ORIGINAL_BUDGET_IMPLEMENTATION_NONHA_DISPOSABLE_INTERFACE_TEST
OWNER_AUTHORITY=Owner已于2026-10-21同意在SOURCE_ONLY PASS之后继续发出真实生产ledger的无HA接口测试
SCIENCE_CALLS=0

## I. 唯一问题与科学边界
此前A1原始事件头seq11而checkpoint停seq9、WinError5出现在os.replace、共享STOP迟滞；历史run方法通过错误文本是否包含E2_分类，旧Budget.checkpoint排他创建current.next+fsync+replace时缺乏局部reconcile。SOURCE_ONLY与先前另写的六组合成参考测试并非生产验证。本任务只对**历史真实Budget方法体**在新受控文件夹中的行为做最小接口验证，明确恢复/分类/STOP缺陷是否可在受控条件被触发。实验观察的PASS不解锁真实数值A1-A3；发现缺陷则记录证据与下一次修复门，不修改原生产实现。

绝对禁止：原科学driver/factorial run执行、temp_driver import、HA/HJB/KFE/GE/IRF或MATLAB blackbox import/调用、原真实journal或历史模型worktree任何写入。正式V010/v0.0.10、REAL_GE=False、Results=FALSE、V011 NOT_STARTED、FULL_RUNNER_IO_CLOSURE BLOCKED不变。

## II. 冻结真实来源与安全提取
同一live治理快照首先检查CURRENT.md/TASK_CURRENT.md/DOC_INDEX_CURRENT.md唯一ACTIVE指向此任务；再按发行清单固定issue_commit核本合同、参数和来源Git Blob。文档只读由参数input_pins界定。
历史私有证据档案`TEMP_V010_PRICE_BRIDGE_FACTORIAL_100_PRIVATE_FINAL.zip`：大小1214713 bytes、SHA256 `f3e8984fe4d2ef4be65692c27fa7594d96b870d372a8c45d029899f7891841d8`。原位置只允许stat参数指定旧scratch下四个**准确候选相对路径**，不递归搜索文件系统、多份歧义/链接绕出安全根STOP。只有唯一普通文件且原始bytes完整哈希匹配才用zipfile读取中心目录（不超过300成员），最多6份准确授权成员：`factorial_driver.py`（12102B，SHA256 `2f956b9c1495d1026b23b219da059681b9cdd98fadb9233acf02154559ddf456`）、`temp_driver.py`（16549B，SHA256 `c4f6aedfc9ae22afc5e2ddc59d490eee29267049de132090d36df93f0a42e001`）、至多四份参数allowlist的旧账本纯文本/STOP元数据。所有原始成员字节总计≤131072；不得进入ZIP嵌套私包、原100轮数组/其它旧档案、更多未知目录，不公开这些原始成员。
**生产接口准入门**：只允许先用ast.parse分析`factorial_driver.py`及`temp_driver.py`的模块导入/副作用。构建新的隔离测试 harness 可以通过Python AST提取原始Budget类和必要的纯辅助函数（只许无科学副作用）。原Budget的方法体须由ast.dump的结构身份比较验证未改，保存每个被测方法身份、源原字节SHA/行定位以及注入点；不允许把重写的模拟Budget当成真实源码测试。不得import/execute原production driver模块、temp_driver原模块及其它科学源；仅将已审查的原Budget方法体在安全的最小namespace使用stdlib、注入的安全目录/错误/时钟，所有动态依赖必须显式白名单，否则STOP_SAFE_BOUNDARY_UNAVAILABLE并只交部分静态报告。没有通过安全导入/隔离门，一次真实Budget方法都不能调用，不能用“dry-run”名称绕过。
原源码可能包含跨进程msvcrt锁行为：只作用于新scratch测试文件。Windows持读句柄实验所有Handle由任务自己建立，必须提供正确close/reap确认；不能改变系统全局共享、杀不归属进程/使用真实旧journal。
BOOTSTRAP0: 可信父链有限元数据、唯一新scratch不存在、固定旧源stat、正式git locator/index只读；BOOTSTRAP1: 独占创建新scratch；BOOTSTRAP2: 安全首写前复核。私有日志与派生/公开原件仅可写新scratch，保留首错。末轮用同只读身份方法核受保护formal worktree/locator/index前后不变。不得使用此前的旧任务余额。

## III. 聚焦T1—T6：允许观察真正的旧方法缺陷，不改原件
T1：调用经AST原样认证的Budget.__init__/guard/event/checkpoint，针对3个以上新sandbox路径核 per-arm排他单写者、raw JSON line SHA链、append/fsync到checkpoint head顺序，区分事件已追加与checkpoint已提交。禁止打开原生产文件。
T2：在Budget.checkpoint实际os.replace边界注入一次PermissionError/WinError5，先完成event append，记录首次异常、current.next残留、当前checkpoint旧前缀；审查原Budget有没有恢复/隔离/二次失败。不要替它自动“修好”，若新harness恢复逻辑仅能作为对照，必须标WRAPPER_ONLY，与ORIGINAL_BEHAVIOR分开。
T3：在Windows本任务自己创建的reader-held handle对同一sandbox checkpoint做no-reader control及可用的两组真实share flags对比，执行同一原Budget.checkpoint，不要求一定复现WinError5。分别记录原生handle权限、实际返回码、关闭/恢复的真实时序；不得推断历史PowerShell真实句柄根因。
T4：在原Budget.finish以及原run catch**仅当可在安全审阅AST抽取而无科学依赖**时分别测试“第一次checkpoint失败、后续error reporting又checkpoint失败”、保留首错与覆盖；明确`E2_`文本判断普通PermissionError的误分类（可纯公式/AST断言）。如果run代码不能安全抽取，不可启动run，结果标STATIC_ONLY_NOT_RUNTIME_VERIFIED。
T5：原Budget.guard/begin_ha在STOP文件**已经存在**时与并发竞态时，配任务独有dummy marker检验先检查STOP还是先计费/append；运行的是安全原方法和哨兵而非observer/HA。记录原始事件是否成功持久写入，区分仅内存increment与真实成功扣费。无完整supervisor/reader源码时，STOP全局线性化只能报NOT_VERIFIED；任意真实HA调用立刻STOP。
T6：原Budget日志故障/受控进程异常、checkpoint回读及只回收本任务拥有的子进程；保存第一真实native错误、已计费/进入/完成/取消四类计数，不把replay认定为成功返回HA。所有内容只针对受控sandbox副本。
严格保留原实现bug结果，不以“六项全PASS”作为结束目标。区分`REAL_ORIGINAL_METHOD_PASS`、`ORIGINAL_METHOD_DEFECT_REPRODUCED`、`WRAPPER_ONLY`、`SOURCE_STATIC_ONLY`、`UNOBSERVED`、`STOP_UNSAFE`，最终`PRODUCTION_RUNTIME_UNVERIFIED`直到实际生产管理入口、外部supervisor与reader共同得到另行授权并经过验证。即使本任务原方法测试无缺陷，也不得自动解锁TEMP A1/A2/A3。

## IV. 预算与问题处理
统一冻结在TASK_PARAMETERS；总墙钟≤10800秒（3小时）；verification≤900s、engineering≤7200s、delivery≤2400s且都服从总上限；安全预留180s。工程Python starts≤24、pytest starts≤6、直接进程starts≤96、自有helper≤12且最多3并发；E1正常脚本/fixture/脱敏恢复最多3批，另外各阶段额度独立。每个T test最多2次尝试（负例专门故障注入也计入），失败不得偷偷开T7再运行，任何硬门失败STOP并保持首错。新scratch非Git≤64MiB，Git临时存储≤1GiB；kernel descendant未实际观测记UNKNOWN。权限、源身份或文件系统保护失败、敏感信息、真实调用风险为E2立即停止。 不调旧HA、更不把D/G/E数值预算假借为验证脚本。

## V. 交付与独立验收
只交本任务新安全派生结果，公开一个确实可机器查原方法AST提取边界的脚本及受控test源、fixture、逐项真实观测结果、首错、native WinError、受保护身份、资源/隐私。**不将旧私有1.2MB原ZIP、任何原始旧事件流、旧源码全文、真实绝对路径、凭据嵌入公开ZIP。** 若原方法源码片段需证明身份，在私有受控scratch保留原字节和每方法的定位/hash；公开可包含必要少量脱敏片段/抽象调用和可审核的新harness，不泄露原完整源码。原私有输入匹配但运行/安全隔离不允许时，SOURCE_ONLY的证据可交付，明确INCOMPLETE。
由现有已授权GitHub精确Git Data API先验确认可用后，向固定review branch`review/ch5-temp-real-ledger-nonha-gate-20261021`、固定parent`d4cda508159116d27cf2a3c722a316b1c7214bab`、固定temp dir`_review_tmp/ch5/temp-real-ledger-nonha-gate-20261021/`仅新增`result.md`、`manifest.json`、`evidence_sanitized.zip`，最多一次成功发布；权限拒绝/401/403/429/平台拒绝停止且不切换渠道绕过。正常Git+SSH仅API写能力在拒绝前缺失并已预授权方可使用；禁止root recursive tree、整仓库clone、force push。对固定candidate完整远端3原字节+ZIP全成员批量自检，不代替Astra独立审计。
Astra终审严格分层：源码身份、原方法真正可调用安全边界、功能缺陷与容错、隐私、交付、cleanup；终审PASS/CHANGES_REQUIRED先归档/回读后Astra精确非强制删当前tree的三文件、远端回读。PENDING保留。旧两个PENDING候选绝对不触碰或清理。
最后提交Codex完整原始JSON Base64+bytes+SHA256、run_id、actual terminal、测试六组逐项PASS/DEFECT/UNKNOWN、真实科学调用各0、Git blob/tree/sole parent/资源/首错、独立controller completion event；预定WAIT_ASTRA_REAL_LEDGER_NONHA_INTERFACE_REVIEW仅为计划停点，不冒充实绩。不自动签发后续科学任务。
