# TEMP31 预执行校验与非科学进程保护实施 · 2026-11-02

STATUS=PASS_E1_METADATA_PREFLIGHT_AND_E2_WINDOWS_TOY_PROBES__NOT_A_SCIENTIFIC_RUNNER
AUTHORIZATION_PARENT=e0aaa2f3b034a9af6e68b112cff63069aece30ba
OWNER_CONTINUATION=可以请继续
E1_CODE_CANDIDATE=2383af15b97fcf7efdc52a5e4248b8f383c40c55
E2_CODE_CANDIDATE=edb8104c8a186b989ee26b39ac909d82268cf988
E2_CODE_PARENT=2383af15b97fcf7efdc52a5e4248b8f383c40c55
E2_CODE_TREE=9a6e01aa6c4328251b2cbaf6586c759cce97da56
CODE_PUBLICATION=LOCAL_ONLY_NOT_PUSHED

本轮实施前次精确静态方案中的E1/E2。只新增两个标准库工程模块、两份行为测试及一个固定非科学worker夹具，不改任何原科学模块、工资消费者或HA网格，不导入NumPy/SciPy/模型，不启动初始化/HA/HJB/KFE/GE/IRF/policy/校准/MATLAB。以下实际进程全部是非科学工程夹具，不计入或恢复科学预算。

## E1：有身份的计划元数据与入口前计数

inspect_preexecution_plan只核传入计划原字节及独立PlanPin。它先匹配大小/SHA，再拒绝重复JSON键/非有限常量、科学scope/布尔门升级、错origin/期次/网格声明/预算、真假整数、错/重复/越界模块路径及缺字段，输出11个声明模块pins、固定fixture元数据摘要和计数限额。工厂不读模块文件、不解码真实科学载荷、没有启动进程或执行callback的入口；source_bytes_verified、runtime_ready、scientific_run_authorized、consumer_ready及接受旗标均FALSE。

现场只读固定父提交的31241字节计划副本，SHA-256=aea2f06db3bb05bfc3b7ea6ee29e3a46ae2e5cd9f96448ee4e843ee90d2152fc；与父提交字节固定后执行该元数据检查，结果PLAN_METADATA_ONLY，11模块声明对齐。原科学文件未在此接口中重读，不把pins格式完整当来源/输入采纳或实际装配验证。

AttemptCounter在调用主体前累计attempted，限额内才累计admitted；超额或未声明入口后进入STOPPED，同对象无reset/restore，成功/失败完成后也不可再进入。线程竞争最多准入限额次数。它明确标记为内存工程计数器，不冒称持久科学账本或对任意同解释器恶意代码的隔离；未来真实科学观察器仍须另绑持久账本、函数身份和许可。

## E2：只允许固定非科学worker的Windows保护

run_toy_probe没有任意命令、脚本或callback参数，只接受明确的非科学模式；拒绝HA/科学模式、120秒/2GiB的科学规模参数。工程夹具范围为0.1–5秒、64–256MiB提交内存；实际正向/故障案例使用96MiB和默认3秒，超时案例0.5秒。它不能直接启动上一轮提出的HA程序，也未验证科学环境或120秒/2GiB运行。

每个新意图目录独占创建、CLAIM独占写入并flush/fsync，之后才核固定worker与E1模块字节pins并保存原字节快照。相同意图目录无论成功或失败均拒绝重用；原claim/result/失败记录不覆盖。源及输出祖先的符号链接/重解析点拒绝，不变更保护基线；证据写在独立LOCAL_ONLY工程根，不写科学源码树。

Windows路径创建挂起且隐藏窗口的固定Python进程，先配置Job Object的提交内存限额、active_process_limit=1、关闭job即终止所辖进程，并回读限额；将进程绑定job、落盘PRE_RESUME_JOB_LIMITS后才ResumeThread。没有无约束后备启动，也不允许breakaway。父进程按含启动阶段的墙钟截止等待，超时终止自己创建的job并核等待退出；设置/绑定/恢复状态异常、失去返回或终止未确认均保留STOP/UNKNOWN，不自动重试。

夹具以-I/-S/-B启动，不加载site；子进程中的科学包导入门会在NumPy等模块加载前拒绝。载入的只是固定非科学脚本与E1工程模块完整字节，未采用或调用11个真实科学模块。只有自己的临时job/进程句柄被关闭，未处理任何其他进程或全局配置。

本机实际验证：

| 案例 | 观察结果 |
|---|---|
| 正常返回 | 挂起进程绑定并回读job后启动，固定toy主体一次，返回证据匹配；科学就绪仍FALSE |
| 超时 | 0.5秒截止终止固定toy，退出124，原claim和started保留，无return；终止确认 |
| 内存 | 96MiB进程提交内存上限下，实际256MiB分配触发MemoryError，退出23并保留拒绝证据；不是RSS或科学负载基准 |
| 子进程数 | active_process_limit=1实际拒绝toy再建子进程，退出25并保留证据 |
| 计数超额 | attempted=2、admitted=1、STOPPED，第二主体标记不存在，退出21 |
| 科学导入拒绝 | 一次刻意的numpy导入尝试被拒绝，实际已载入科学模块列表为空，退出22；不能说子进程“拒绝尝试0” |
| 崩溃 | 退出17，started/claim保留且无return，不宣称执行成功 |
| 设置或pin故障 | 无worker创建，旧意图继续封闭，不改pin或重用意图救通过 |

Win32机制依据：[Job内存字段](https://learn.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-jobobject_extended_limit_information)、[进程绑定与限额](https://learn.microsoft.com/en-us/windows/win32/api/jobapi2/nf-jobapi2-assignprocesstojobobject)、[挂起及隐藏窗口创建标志](https://learn.microsoft.com/en-us/windows/win32/procthread/process-creation-flags)。这是受限工程夹具的本机验证，不是对不可信任意代码的完整安全隔离或未来HA兼容认证。

## 检查与版本身份

26项不同的行为检查已覆盖并通过（E1共14项、E2共12项）：扩展检查首次25通过，另1项夹具在调用API前因拼接非法function参数自身报错；只修该测试的标签构造，单独复核该失败项通过。未为取得“整套绿色”重跑已成功的进程案例；完整原日志与失败过程均保留，无遗留失败/错误/跳过。E1计划检查、计数器、E2 API缺失先分别由失败用例复现，再增量实现。工程自审调整了异常ResumeThread状态的UNKNOWN归类、句柄关闭失败状态、悬空重解析祖先识别和子进程实际模块清单，随后扩展行为检查通过。

累计非科学工程账本有11个独立intent、9个toy进程（含初版正向验证1个及扩展案例8个；另2个设置/pin拒绝未建进程）；这不是9次科学worker，也不是把原一次性观测重命名。每个意图的独立代码pins、结果与记录均保留，无重置或隐式续跑。主测试进程科学模块导入/原科学函数调用均0；子进程科学模块实际导入/科学函数调用均0，一次刻意拒绝导入已单列。

| 路径 | 字节 | Git Blob | SHA-256 |
|---|---:|---|---|
| src/ch5_two_asset_hank/multi_province/temp31_execution_preflight.py | 8797 | 4b15afbf16368bf671fa9df6e138177ffbb792bc | a83905dcc8ceb1d5228f679f7be63a084efdf9269215827085c0cc60491baf75 |
| tests/test_temp31_execution_preflight.py | 6787 | 65fed6cbfc0b61a30cbd0f7757fae590c68d47f9 | 5a4a7bf7a43c89041c75a9399637f077b0d313d360188c2d2562116e18eed421 |
| src/ch5_two_asset_hank/multi_province/temp31_toy_supervisor.py | 11473 | 7d084063c73a3f62fd73310443892384de5c8d62 | 61a60f431eaa5bb6cf539419788299c6cdb1fbf388e916a21d5d55833443c099 |
| tests/test_temp31_toy_supervisor.py | 6460 | 10d666a3d53592505dd8bd62492a30c349585e12 | 0b2dbf9b11982da5756fa9bd775ab31c1b9e822e36eed743c55c9538cf442bca |
| tests/fixtures/temp31_toy_worker.py | 2946 | e7e5c0631351478c88ef45be4f76f31dfb7226e3 | 625023f1cbc6ea90ecbbe582d4c8925963ed4c9956fd4d85bf2d14fa88811abb |

原578条选定代码路径和最初565条基线逐项保持；新增5条后583条选定代码路径。源码candidate只在本地，公开同步本说明与治理进度，不上传脚本、数组、CSR、原始输入或完整日志。验收为Local Codex工程自审，不是独立科学评议。

## 剩余门与下一工程片

E1/E2已完成，但科学HA运行器仍不存在：尚需在默认禁用且未获许可即退出的独立驱动中，绑定固定11模块完整加载、确切函数/C调用观察器、持久单次科学意图账本、原网格/输入/算子身份及最终环境pins。可先用非科学装配夹具验证这些机制，保持真实科学模块导入/执行0；不能把现有toy接口改模式或放大限额直接启动HA。

上述具体运行器和最终pins可审阅后，再由Owner决定首来源地800格/最多800根、HJB/KFE等新的具体科学许可。真实生产输入兼容A/B仍未选择，共用工资消费者未改；严格判据reference/thresholds仍null，不从诊断或HJB返回自动接受。旧初始化3/10余7、旧工资/补录各1/1关闭，科学源码/公式/参数/输入/网格/容差、dirty树/HEAD/index、R12/R13/WASM、未授权保护重绑定及16义务保持。FORMAL_SOURCE_FREEZE、Results、model_activation、REAL_GE与全部生产/科学接受门均FALSE，无分支删除/main合并/原件清理或全局配置修改。
