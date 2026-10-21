# CH5 TEMP V010｜真实Ledger安全接线与跨进程STOP门（长任务）
TASK_ID=CH5_TEMP_V010_LEDGER_SAFE_INTEGRATION_CROSS_PROCESS_GATE_20261021
REVISION=ISSUED_20261021_R1
SCOPE=CONDITIONAL_ORIGINAL_RUN_STATIC_WIRING_PLUS_DISPOSABLE_CROSS_PROCESS_NOHA_GATE
OWNER=2026-10-21明确同意继续真实ledger安全集成及supervisor/reader验证
SCIENTIFIC_HA_HJB_KFE_GE_IRF_BUDGET=0

## 1. 核心问题与前提
上一轮派生Budget最小修复的已接受结论仅为`PASS__BOUNDED_ISOLATED_REPAIR_REGRESSION_EVIDENCE`，candidate尚未部署；完整生产run的`E2_`文本判别、真实外部supervisor/reader与跨进程STOP协议仍未验证。不能拿已通过的单进程LOCAL_FENCE当GLOBAL_STOP，通过新进程fixture也不能称实际生产控制器已验。新任务只在完全隔离scratch里分析原run静态接线，构造无HA真正独立进程的STOP协议测试；绝不执行生产driver/run/temp_driver/HA，不写旧journal，不改V010，不能启动A0–A3。原生产实际部署需Owner后续另批。

## 2. 输入和保护
启动时从live治理同一快照读取CURRENT/TASK_CURRENT/INDEX，唯一ACTIVE与本ID匹配；ISSUE_MANIFEST在后发发行commit、冻结合同/参数在issue_commit，review parent是另一个固定baseline，不混淆。
真实历史archive：1214713 B，SHA256 `f3e8984fe4d2ef4be65692c27fa7594d96b870d372a8c45d029899f7891841d8`，只允许在PARAMETERS的四个精确位置中找一个不为symlink/reparse的普通文件，完整bytes/hash匹配才读取ZIP中心目录≤300成员及2份固定原源码（factorial_driver.py 12102B SHA256 2f956b9c1495d1026b23b219da059681b9cdd98fadb9233acf02154559ddf456，temp_driver.py 16549B SHA256 c4f6aedfc9ae22afc5e2ddc59d490eee29267049de132090d36df93f0a42e001）。私有修复候选13136B SHA256`51005056766f99b9f6c4bf4fe0fb8d42d6547ace8eebba9ab5bba30465ff8a3c`，仅从参数唯一旧scratch精确路径读取；若已不在，允许以已认证的原源码和固定GitHub public ZIP中的build_candidate.py，在新scratch内重建并必须SHA逐字节一致，否则SOURCE_UNAVAILABLE。
上一轮public ZIP只读历史commit `6cbac91ccaab323a938e94a7bc0720238c91dd36`指定精确路径、Git Blob 3dd5e6c28ed55f02ec332f0c2fc8c743c9877e56，47700B SHA256`76ed04b3864b694bc2475666c970862d9514559775a8db31b40b0c39d28a074f`，仅提取PARAMETERS固定hash的5个成员+最多4额外必要成员，不取root recursive tree、不取清理后的review HEAD。所有写入只在不存在后独占新建`D:\ProjectTemp\ch5_temp_v010_ledger_safe_integration_crossprocess_20261021_01`，其它目录仅有限stat/hash。BOOTSTRAP0/1/2、保护git locator/index只读前后证据。无Package install、无认证修改、无全盘递归寻找。

## 3. 精确控制器来源门
在已验原archive的central directory中仅以PARAMETERS列出的8个basename做精确成员名识别（不是任意关键字全文搜索），匹配多个同名路径则SOURCE_AMBIGUOUS/STOP；最多额外读取4件、每件≤64KiB、总source≤128KiB，且必须先静态安全分析import/副作用。STOP文件JSON只能证明历史控制文书，不等于真实supervisor/reader源码。如果实际controller/reader源码不在这个冻结范围，标`REAL_SUPERVISOR_READER_SOURCE_UNAVAILABLE`；不编造真实产线验证，也不得越界搜其它目录/ZIP。仍完成原run静态诊断与新scratch跨进程fixture。

## 4. 真run静态接线＋安全独立适配器
在原factorial_driver.py AST内定位run的Budget调用、异常捕获、`E2_`文本识别、共享STOP发布及其时序，给静态行号、源哈希和无法验证的动态边界。仅在隔离scratch创建不含科学入口的新`typed-run-catch adapter`，以已认证派生修复的typed classify和primary error handoff替代字符串真假，并演练plain WinError5、受损checkpoint/previousHash及普通E1；绝不import/exec原run、原temp_driver或完整生产模块，也不能宣称真实生产catch已接线。原控制来源不够时结果`RUN_WIRING_SOURCE_GAP`。

## 5. 真正跨进程（但任务自有）STOP围栏
必须使用两个以上**Windows独立进程**，而非仅thread：进程一使用已认证派生Budget的安全AST方法/新scratch日志，进程二任务自有STOP publisher，必要时进程三任务自有reader。新adapter须说明旧RepairProtocol()的admission.fence通过xb排他创建，第二进程不能再调用constructor并假装可attach；发布者只可在验证同一scratch围栏文件的owner/identity后，以自己的handle执行msvcrt.locking byte-range lock。所有共同参与者持同一锁：writer guard→持久事件/commit→惰性回调返回，发布者在锁内写入并fsync任务自有STOP文档，发布`STOP_ACK`后新成功charge/惰性entry均为0。严格区分STOP尝试、持久发布、ACK和读者观察时间；故障、非预期持读或损坏STOP应fail-closed。所有helper只回收本任务owned进程，任何HA real entry/call/import都是硬STOP。即使样机X2/X3通过，也只能标`COOPERATING_CROSS_PROCESS_FIXTURE_PASS`，真实外部supervisor/reader仍UNVERIFIED，除非已有来源被准确核实且仅静态确认其兼容性。

## 6. X1-X6及预算
X1: 原run控制流/原Budget与派生candidate SHA/AST锁定；
X2: 不少于两独立自有进程的共享STOP锁、ACK与两组惯性空哨兵时序；
X3: 第三自有reader看到STOP并在ACK后不再成功扣费、进入；
X4: typed E2错误及首错处理、合法/非法checkpoint；
X5: WinError5、残留current.next、损坏STOP、重复发布、受控中断与资源回收；
X6: 与已接受T1-T6/J1/J2源身份接口回归，并形成按真实控制器来源划分的READY/NOT_READY判定。
总墙钟≤14400s，工程Python≤32、direct进程≤120、pytest≤7、helper≤16且并发≤3，E1≤4批；verification/delivery另账。所有预算详见TASK_PARAMETERS，不得继承旧预算。真实BUG/负例不是失败原因，不以修改原生产或扩大权限换取绿色。必须保留首错，kernel descendants无法确认写UNKNOWN。科学HA/HJB/KFE/GE/IRF/driver全部0。

## 7. Codex自动GitHub临时三文件（强制）
Codex必须自动把脱敏`result.md`、`manifest.json`、`evidence_sanitized.zip`三原件上传至GitHub仓库**独立review分支** `review/ch5-temp-ledger-safe-integration-gate-20261021`的临时目录 `_review_tmp/ch5/temp-ledger-safe-integration-gate-20261021/`。候选固定唯一parent=`48d39c23b912ad4704e5ea10781ab993081c44a1`，仅允许三件新增。自动上传后的远端commit/tree/parent、3 Git Blob/实际原字节SHA及ZIP全部成员CRC/size/SHA和隐私逐项readback要进入最终receipt；本地路径不构成交付。优先现有Git Data API；401/403/429等权限/平台拒绝必须STOP，不可换账号/协议绕过、根recursive tree、全仓clone、force push。Codex不得清理临时文件，Astra终审先归档回读再non-force精确删除；PENDING保留；Owner人工中转不是默认流程。旧两个PENDING refs`4e05976bbc8068b971ba5915133e9a6c3b73193d`与`1579e7f1d7a1975c322dd6ae9af1776e88e83e7c`完全不碰。

## 8. 交付与冻结停点
证据至少含冻结三层来源身份、原run E2 static map、外部controller目录源鉴定、真实多进程任务owned安全harness源码、每个X1–X6的逐案结果/首错/STOP_ACK/真实读者fsync的顺序、任务only路径保护及资源/隐私；不公开私有原始源全文/日志/Windows绝对路径/个人凭据。最后原始JSON receipt输出完整Base64、真实bytes/SHA256、run_id、candidate commit/tree/唯一parent和独立controller completion event。真实控制器未找到时照实SOURCE_MISSING，整体可以交部分科研有价值成果，但**绝不能标PRODUCTION_READY或GLOBAL_STOP_PASS**。计划停点`WAIT_ASTRA_TEMP_LEDGER_SAFE_INTEGRATION_GATE_REVIEW`，真实实际终态优先。不启动A1–A3或任何后继任务。
