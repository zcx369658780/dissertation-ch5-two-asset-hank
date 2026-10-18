# TEMP-V010：HA黑箱、简化观察门与家庭价格调参——单张集中长任务

TASK_ID = TEMP_V010_HA_BLACKBOX_SIMPLE_PRICE_TUNING_100_20261018
DELIVERY_ID = TEMP_V010_HA_BLACKBOX_SIMPLE_PRICE_TUNING_100_RESULT
STATUS_AT_ISSUE = ISSUED_NOT_STARTED__P0_ENGINEERING_THEN_CONDITIONAL_TEMP_SCIENCE

## 0. 本次Owner授权与任务范围

Owner于2026-10-18本会话明确：“可以，让我们继续TEMP的方向（HA黑箱+约束条件简单化 的调参）”。

据此，顾问将本轮执行范围冻结为：先在同一任务内解决已知账本与交付可靠性缺口，P0合格后自动顺序执行三个已定义的家庭价格配置，每组最多100轮；最终一次自动交付。不在P0与科学阶段之间增加人工微任务审批。以下参数选择、工程额度和执行顺序是本次顾问冻结的具体实施范围，不冒称Owner逐项给出了这些数字。

本轮“调参”限于两个二元外部价格传递开关；不扩展为未限定的参数优化。约束简单化是允许原HA正常返回但尚未收敛时继续外层观察，不加入Bellman/KKT等新家庭否决门，同时减少并发运行和重复封存环节。旧TEMP已经把Bellman作为观察项，不能宣称本轮才首次取消它、或取消它已解决不收敛。

这是新TASK、新run_id、新scratch、新预算。旧100轮、旧2×2的0/2/2轮与12次HA、旧发布器至少26/24次资源异常均原样保留、全部CLOSED_NO_CARRY_FORWARD。不得续跑旧A2/A3、重新上传已清理的旧三件或把新结果回填旧回执。

正式V010/v0.0.10继续冻结；V011 NOT_STARTED，model_activation=False、REAL_GE=False、Results FALSE。允许的TEMP科学调用仅匿名双省；无真实2009/2017/2018/C8/31省、IRF或正式模型修改权限。HA内部一个字节和运行语义都不可改，不能回到CP2_F25 selector修补。

## 1. 固定来源与当前任务身份

Repo：zcx369658780/dissertation-ch5-two-asset-hank。
发行分支：experiment/ch5-temp-blackbox-simple-price-100-20261018。
本合同由旧实验发行Commit 2c855f616efbca05c29d4069a44e3c6651070b44、Tree f1958ef815f6610905daea0810a920e8a4bbab6b 派生，只新增本文件；旧合同仅作科学设计来源，旧运行权不继承。
本合同发行Commit/Tree/Blob由签发后治理CURRENT/TASK_CURRENT及Owner Memo登记，执行必须三者一致，不依赖浮动实验分支替代固定身份。
签发前治理HEAD：03f61eda86546bd6f1204c03a2923aac9081a2c1；完整交接为docs/CH5_SESSION_HANDOFF_20261018_AFTER_TEMP_HA_PRICE_BRIDGE_AND_GITHUB_ZIP_CLOSEOUT.md。

| 对象 | 固定身份 |
|---|---|
| 历史HA代码Commit/Tree | 216283cf4f1303afa60f1915e143a0b7303a9ffb / b7a28f7afe7e8de23fb5afdfb377d36c9d025b50 |
| HA路径 | exports/matlab_faithful_two_asset_ha.py |
| HA Blob / SHA256 | 9e7dc9556a2b76811e78f89999abecc045886106 / B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3 |
| 原postloop adapter | validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py |
| adapter Blob / SHA256 | 0033baee136c0328e80ffb8b794a88d4405c976c / 8A6308870606A02886E9A8E4B32E942A7D433237405E6B9E86EE4175FB2DFF06 |
| V010外层只读代码Commit/Tree | 94de4501dec051b969bee9d852eba2d4591f30ef / 205eab47c4e4f9c6292c2ead9947d94d1a7579a5 |
| fixture在上述代码Commit的有效路径 | tests/fixtures/v010_mainline_synthetic_v1.json |
| fixture Blob / SHA256 | 40915658d93403cfc21b33a6b864b332b7857749 / BC002D71430D5472F8C5C62543F07A845F2D6BF564CB5BB92E6DD8142AC50252 |
| steady_state.py Blob | 5fa6c73884067391bd2b998d4b050443c97c38e8 |
| 旧价格桥科学设计合同Blob | 4e81556bff068b9bedc6c7c608faf24ee1e439fe |
| A0已接受私人证据ZIP | TEMP_V010_MATLAB_HA_BLACKBOX_100PLUS_EVIDENCE.zip；6,352,227B；SHA256 4CD602CC3589F404E176937B96D21E265EB036374BCA95D708E5DC246A394156 |
| A0轨迹成员 | run/trajectory.jsonl；SHA256 99E849304674BAC1608176EA3903AAF60EC9B3BF6E4A7A39243E497FA2CF7303 |
| 旧TEMP桥仅作只读参考 | experiment_bridge.py；SHA256 73D21D91DCDF421E5F65EEE7EEF862978A5EC720E5AD754C3533EC934B05FA28 |

HA的20×20×2网格、F-order b最快、Delta=1000、每HA最多100次内部HJB更新、原D<1e-7收敛标记、初始化、FOC、政策、KFE与postloop保持原实现。历史2009年184轮/5704HA/31省终态一致性仅是已接受来源锚点，不在本任务重跑，也不推广到其他年份。

仅从已知包、既有交付回执指向的位置或合法固定Git对象读取上述来源。允许在新scratch解包所需成员并核字节；不扫描未知旧科学目录、全部磁盘或其他项目。旧2×2与发布器已知scratch仅允许定向只读取得明确命名的失败记录/脚本参考，不能以原脚本同名即可信而直接执行。原件缺失/身份不符须报告，不重造A0。

## 2. 唯一科学设计：三个新配置，A0只读复用

| ARM | 家庭资本收益rah | 家庭净工资w_eff的企业信号 | 本次运行 |
|---|---|---|---|
| A0 | 前轮raw ra0，经同S加权 | 前轮raw wt0 | 无；复用旧100轮 |
| A1 | 前轮used ra，经同S加权 | 前轮raw wt0 | 新起点，最多100轮 |
| A2 | 前轮raw ra0，经同S加权 | 前轮clipped wjt | 新起点，最多100轮 |
| A3 | 前轮used ra，经同S加权 | 前轮clipped wjt | 新起点，最多100轮 |

顺序固定A1→A2→A3，单一产生HA调用的science driver，任何时刻最多一个HA在执行。每臂独立state、arm_id和轨迹，但全任务共用一份不可重置的科学账。每臂均从同一个fixture第1轮开始，不用前臂终态或旧失败第2轮热启动。省级state之外的tKN_previous、Y_previous及任何外围热状态也逐臂重置为A0第1轮初值；原tKN初值为每省3.0，须与A0初始回执核对。全局只共享不可重置的资源账，不共享演化中的经济状态。

第1轮各臂使用A0的原initial_household_rah、原净工资构造、rb、Tt、rb_gap、网格及参数。第1轮实际HA输入值/数组布局应与已归档A0第1轮一致；不额外运行HA来证明一致。第2轮起才实施价格干预：

1. 每臂S_t始终由自身前一完整轮raw ra0、原theta/distance/beta/foreign-only份额律计算，zscore ddof=0。不得用used回报作为评分信号。
2. A0/A2：rah[i,t]=sum_j S_t[j,i]*ra0_raw[j,t-1]；A1/A3：rah[i,t]=sum_j S_t[j,i]*ra_used[j,t-1]。used值直接取冻结企业输出firm.ra，不自行再次clip或移动边界。
3. 资本数量与收益在每臂内绑定同一个S_t，列和为1；干预后不同臂的S不必相同。
4. 旧prepare_mainline_household_states会重算并覆盖raw rah。新TEMP包装器必须在其返回后按ARM重新设置真实pre-HA rah，并在实际调用边界核验公式与字段身份；只看post-turn输出不能算接线验证。
5. 由前轮firm.wt0或firm.wjt通过原mainline_effective_wages计算下一轮w_eff，禁止使用尚未得到的当轮企业工资。wages=w_eff、tau_HA=0等原单次扣目的地税的接口保持，不能二次扣税。
6. 其他通道原样：用于劳动重构的旧wjt_gross/raw wt0口径、财政工资税基、Corptax边界补偿、same-S数量、人口与人均→总量、GovInv×0.9/1.1、Zt调整及max KN gap<0.1触发、tKN=0.6*KN+0.4*tKN_previous、价格上下界和其他经济方程保持。

本轮不改GovInv初值/增益、Zt控制、0.6/0.4松弛率、偏好、价格边界、网格、HA容差，不增加第四个新配置、warm start搜索或优化器。A3仅是家庭两条输入价桥使用受界价，不称完整恢复原MATLAB外层经济。

## 3. 简化后的观察与停止规则

原HA正常返回真实、有限、合法shape的输出时，即使原hjb.converged=False，也允许继续该臂外层；忠实保留False。Bellman B、KKT、可记录的KFE负尾数/质量误差、工资触界和GDP目标gap均为观察项，不增加新的HA拒绝门，不为取得诊断额外调用solver或selector；无法获得的观察量标UNKNOWN。

以下源式条件全部成立，才能标SOURCE_CONVERGED_BY_ROUND_N并自然早停：
- 两省原HA converged均True；
- max_i abs(KN_i/tKN_previous_i-1)<1e-9；
- max_i abs(Y_i/Y_previous_i-1)<1e-9；
- 两省ra_used均严格处于原上下界之间。

工资边界只观察；GDP目标≤1%和正式V010严格Bellman/KFE资格均不因本TEMP而得到认证。不满足源式联合条件但数据合法，继续至第100轮并标NOT_CONVERGED_WITHIN_100。不得把曲线平缓、used价格被clip成常数或放宽阈值叫作源式收敛。原2009条件、V010正式方法和本TEMP来源的差别要报告。

真实源码异常、非法定义域、NaN/Inf、非法shape或缺失真实HA输出，立即停止该臂并留首错，不填零、不替用前轮结果、不裁剪新概率尾数。若仅是该臂状态相关失败，且共享身份、输入桥与全局计费仍可信，允许继续余下已冻结臂；不重试失败臂。任何共享身份/黑箱/预算/账本/保护根失信，或已使用错误桥输入，则全任务科学FAIL_CLOSED，不能换臂继续。

## 4. P0集中预检：通过后本任务内自动进入科学

P0不允许任何HA/HJB/KFE/selector/root求解。可以导入认证后的纯算术接口、读旧输出作常量，不能以smoke名义调用家庭黑箱。

### P0-A：一次身份和接线验证

按V1.3 BOOTSTRAP0只读可信父/新目标与保护根→创建新scratch→首文件写入前二次身份→执行器的顺序。复用已认证入口，不在preflight前先写启动脚本。正式V010、历史HA/adapter与fixture首尾全文件hash一致；两版本同名Python包不得影子导入。

用已归档第1轮家庭输出作纯常量进行1+1轮stub：第1轮非处理通道同值，第2轮实际pre-HA两字段满足ARM公式；错误覆盖rah、used作score、重复工资税和跨ARM串状态的反例能被检出。以A0第100轮价格进行无HA代数核查，只验证公式，不把静态替代价格当新轨迹。普通新包装器/字段/测试接线E1在本任务工程预算内集中修复。

### P0-B：单写账本与Windows观察兼容

每种账本仅一个写者；scientific events仅由单science driver提交。每次HA及既有KFE进入计费点在实际进入前append唯一seq/调用id/累计数/前事件hash，flush并fsync，完成同目录检查点与读回核对后才准调用。正常返回另记完成；失败/未进入/中断分别记，不用“返回数”替代计费数。科学计数不得跨臂、跨阶段或E1重置。

为每次已完成checkpoint发布唯一seq的不可变快照，先写临时文件、flush/fsync/close、再发布最终名；临时名包含run_id、seq和唯一后缀，不反复独占创建固定current.next，历史残留只保留不用。外部PowerShell/状态监视仅短句柄读取已经完成的不可变快照，不读取或持有writer更新的current.json或临时件。current可保留为writer-only原子替换兼容件，不能把未经核验的显示快照作为调度权威。禁止多写者或每轮新起PowerShell读current。

checkpoint/append/计费读回任一步真实失败：立即设置进程内全局STOP锁，禁止下一HA及下一ARM，保留原append/current/残留.next与首错；不重试原失败科学事务、不回滚收费、不补写假匹配。异常证据写到此前认证的新终态目录，不通过再次替换失败current来记录其自身失败。若硬盘/路径也不可写，用已受控终端报告，不扩大写域。单driver使“某臂失效但兄弟臂仍继续”不再是正常执行路径。

须在实际Windows、本次同文件系统上用人工事件而非HA完成以下小型证据组：
- 至少200次append/checkpoint，另有真实短句柄读取进程观察不可变快照；seq/hash/累计数一致，无半文件消费。
- 临时测试文件由无FILE_SHARE_DELETE的读句柄持有时替换的行为，及修正监视方案；这是机制测试，不据此追认旧WinError5根因。
- 人工注入append后checkpoint失败、残留.next、损坏/缺少seq、STOP请求：dummy调用器的后继调用和后继ARM均为0；所有注入仅在专用测试账本，不能混入真实科学账。
- 全局预算用极小人工上限验证先收费、拒绝下一次与错误收尾；不运行真实HA。

不要求新增通用数据库/VM/第三套备份，也不将此作用域测试升级为FULL_RUNNER_IO_CLOSURE或OS原生安全沙箱PASS。

### P0-C：一次发布器预演与真实进程计费

在独占bare Git库和本地fake-bare远端中，以一个含二进制成员的小ZIP完成：独立argv token→hash-object/tree/commit→普通push→直接读回ZIP字节/hash→清理测试树。用旧“--git-dir与-c合为一个参数”的反例验证拒绝。仅fake远端可在预演中清理；真实新review三件须留给Astra验收后清理。

所有本机新启动的PowerShell/Python/git/ssh及Git内部后代均纳入累计进程账；线程、预先存在的用户宿主和GitHub服务器端进程不混计。CLI尝试另记：失败启动也收费，成功发布最多一次。不得只数调用包装器或靠结束时PID列表推定短寿命子进程不存在。

优先复用已知Windows Job执行封装，通过内核TotalProcesses等包含已退出进程的累计计数核对；进程在执行前纳入监视，禁breakaway。若实现其他机制，须以短寿命多层子进程正反例证明同等完整性。不单靠轮询或Job通知消息数量。记录每次命令前后累计数、可观测子树和UNKNOWN，避免父/子重复计数。

ENGINEERING、SCIENCE、DELIVERY按操作所属预算域分别记账，不按发生时间简单划分：P0中的fake-bare/发布器测试及全部Git/SSH/source fetch、打包脱敏、发布回读均消耗DELIVERY预算；身份/账本/桥stub、观察/计数/终态辅助进程（即使在科学运行期间启动）消耗ENGINEERING预算；只有真实HA driver消耗SCIENCE预算。一个进程及其后代只能归一个域；三个互斥域的实际进程数之和应等于全局数，常驻controller不因进入新阶段重复计费。预算域可切换但累计数不重置，嵌套Job不重复/漏计。启动Git命令前至少保留32个真实后代进程槽和该域收尾额度；不足则不启动。若实际越界仍如实FAIL_CLOSED，不以预留或上传成功豁免。实际创建失败的CLI/bootstrap尝试另扣对应尝试额度并保留原错误，不冒称内核已有真实PID。第一次真实网络发布前，计数机制必须已通过包含Git短寿命后代的预演。

P0全部真实通过即在本冻结任务内自动进入P1；不等Owner再批准一次“开始100轮”。P0失败若为新白名单内E1，可在额度内修复；E2/E3或额度耗尽则合法封存交付，科学保持0。

## 5. P1科学预算与集中运行

SCIENCE_BUDGET独立：
- 唯一实际产生HA调用的driver最多1个，固定A1→A2→A3串行；每臂独立最多100轮、200次计费HA，全任务最多600次计费HA。
- 首次HA收费前的纯启动/import/argv E1允许至多3次bootstrap启动尝试（包括最终成功那次）；未产生HA收费的失败进程计ENGINEERING，唯一实际进入HA的driver计SCIENCE且不重复计。若已有任何HA收费，即不能将该driver回称工程启动失败，也不能再起第二个science driver。
- 每HA原内部HJB更新最多100、原postloop KFE按原入口至多1次，既有初始化/内部操作据原实现观察记录；不新增smoke、重算诊断、selector探针或失败重跑。首次HA前冻结所有新数值桥/driver内容和hash，科学开始后不得热改桥或模型。
- HA未收敛但正常返回时按第3节继续；只有真实错误、共同硬门、源式收敛、100轮上限、Owner STOP或资源到界才停止。
- 各臂未用额度关闭，不移给其他臂，不续到500轮；Owner中断后科学预算关闭，不自动resume。
- 三臂总科学墙钟最多18小时；总任务从首次写/测试起最多24小时，主动ENGINEERING准备/修复累计最多3小时，DELIVERY累计最多3小时（包含科学前发布器预演/source fetch与科学后封存发布）。对已启动science的被动监视不把同一18小时再次扣成工程准备墙钟，但其新辅助进程照扣ENGINEERING。时间不因脚本失败重置，不跨领域挪借。18小时是新资源上限，不保证串行三臂均完成100轮；到界即真实部分交付，不为补齐对照延时或追加探测。

ENGINEERING_BUDGET（不含真实HA和已归DELIVERY域的操作）：本机新进程含全部后代≤192，集中修复/验证批次≤8，纯Python/focused pytest启动合计≤24（包含在192内），bootstrap≤3也包含在内；不得为报告对原模型跑全库测试。science driver实际开始HA前的成功启动在首次收费时最终归SCIENCE且不在工程池重复计；未进入HA的失败bootstrap归ENGINEERING并保留创建/退出事实。

DELIVERY_BUDGET独立：本机新进程含全部后代≤192、封存/脱敏/发布E1恢复批次≤6；SSH认证预检≤2次，Git fetch CLI≤3次，普通non-force push CLI≤2次，最多1次真实成功发布。需要的固定source/父对象获取也计在该网络池，不另开“预检免费fetch”。所有新进程全任务累计硬上限385=192+1+192；每阶段与全局均须满足，不互借。phase ledger要明确计费归属，常驻controller启动只记一次。

新的私人日志/科学证据/脚本增量合计≤512MiB；所有独立Git对象库合计≤2GiB；旧A0包及必要成员累计读取≤128MiB。预算本身的监测和收尾亦在上限内，预留空间，不先越界再删除证据掩盖。RSS采样软目标2GiB，无法采样明示UNKNOWN；真实内存/存储失控则停止。预算与路径完整性无法成立时不启动科学。

## 6. 写入白名单和科学STOP后的交付

本机仅新增于经BOOTSTRAP认证的D:\ProjectTemp\ch5_temp_blackbox_price_tuning_20261018_01；若目标已存在，只读确认并在同一已认证父下使用预授权的_02或_03未存在新目标，不删除/重建旧目标。新scratch可设reference只读拷贝、temp_runtime、focused_tests、science、receipts、private、delivery、bare等子目录；实现所需新外围文件均可在这些范围内集中创建和修复，不为新文件名逐项索取微许可。readonly reference中的源内容禁止改写后执行。

原D盘8dirty/index/external common-dir、历史各scratch、C盘独立SSD备份、原MATLAB与全部正式/历史HA源码、真实科研数据和其他项目禁止写入、checkout/reset/stash/clean/merge或共享worktree/index。不得安装新的网络依赖、改global/system Git、索取新PAT/SSH Key、扩大原机权限或强推。

科学STOP立即关闭SCIENCE_BUDGET。若路径、原件和交付域仍可信，已预授权的独立DELIVERY_BUDGET继续完成已有证据的只读汇总、脱敏、封存与发布；科学账失效不能伪修，但可作为真实失败材料交付。影响全部安全写入/来源/外传的E2/E3则只做仍合法的收尾，报告具体未完成项，不借交付预算再调用HA。

E1范围：新TEMP外围脚本的普通语法、argv、字段/manifest、图表、打包和非求解focused测试；保留first失败，在明确预算内自主修复。HA内部、任何新增经济通道/阈值、已使用错误科学输入、真实数据或既有保护根越权不是E1。已有科学原件不可用重算替代。

## 7. P2一次报告与自动GitHub三件交付

每轮每省保存：真实pre-HA rah/w_eff与来源轮次、raw/used前价、S及raw评分、资金数量、firm ra0/ra/wt0/wjt、Ct/At/Bt/Lt_HA/Lt_firm/K/Y、GovInv/Zt、原converged/D/更新数及可获B、KFE真实输出和质量/尾数观察、KN/Y/目标gap、税基和原财政诊断、source收敛各项布尔值。完整终端V/density二进制和HA输入身份保存在私人原件，文件与账本以调用id绑定，不仅留汇总hash。

自动摘要轮次1/10/25/50/75/100及每臂最终轮；集中比较共同实际观测轮的资本/工资raw-used差距、边界频率、KN/Y轨迹、原HA收敛频率、GovInv/Zt触发次数及25轮窗口变化。只做已有轨迹的代数分析，不新增solver调用。

仅四臂在同轮都有可信值时计算资本因素、工资因素与交互项；自然早停后不补齐或前值填充成100轮。某臂缺失则完整对照NOT_ESTABLISHED，仍交付真实有据部分。A0曾两进程中断续算，新臂单driver独立起点的执行差别要披露；不称随机实验显著性、真实经济校准或无限期不收敛证明。

唯一新review分支：review/ch5-temp-blackbox-price-tuning-100-20261018。
唯一远端目录：_review_tmp/ch5/temp-blackbox-price-tuning-100-20261018/。
唯一真实发布白名单：
- result.md，≤128KiB；
- manifest.json，≤256KiB；
- evidence_sanitized.zip，压缩≤32MiB、解压≤256MiB、成员≤3000。

review Commit唯一parent必须为本新任务正式发行Commit，diff只新增三件，不能复用旧2c855…或旧补交父。manifest中taskCommit/taskBlob、reviewRef、parentCommit必须是本次身份，不复制旧manifest的陈旧元数据；manifest自身hash置于外部回执防自引用，发布后产生的commit/tree放外部readback而不要求自引用ZIP。

全RAW封存为一个本地私人ZIP。递归逐成员检查ZIP/内嵌压缩包，去除私人路径、凭据、身份、argv/env和未许可真实数据；RAW_EXACT与SANITIZED_DERIVATIVE各记hash与长度，不以脱敏件代称未获原字节的本机事实。默认公开全部合成轨迹、实际账本及输入/输出可审摘要、first/final原文件的脱敏派生、计数和必要合成二进制；不可读字段明示删减，不只交结果摘要。

在新独占bare对象库用现有SSH Key和ssh.github.com:443发布，先确认唯一review ref不存在、父对象/三件/预算/脱敏成立，普通nonforce；不得在任何本地受保护worktree/index落地_review_tmp。发布器自检在科学前完成，真实发布在最终封存后进行。

成功后回读远端ref/tree/三Blob及ZIP原字节SHA256，保留真实资源异常回执（如有）而非只写“0调用”。科学原件与prepublication计数可进入三件，随后真实push/readback的最终计数不可能提前写进同一次发布的ZIP；必须在manifest明确这一时序边界，禁止把prepublication数冒充最终总数。

发布/回读结束后写一个≤8KiB的DELIVERY_FINAL_RECEIPT.json原文件，列任务身份、实际review commit/tree/三Blob、每域及全局内核累计计数、尝试数、真实异常、未取得的事实和最终STOP；在最终交付消息同时给SHA256、字节数及该原文件的完整Base64。这是一次有界文本回执，不触发第二次Git成功发布，不重包科学ZIP。细粒度过程原件仍存本地；Astra若收到这些Base64字节可独立验其文件身份，Windows执行事实仍按其来源分级；未收到则仅CODEX_REPORTED，不能假称已独立枚举OS进程。

Astra独立读取GitHub实际二进制并验收，先永久归档、再仅清该review分支当前三文件；Codex不提前清真实候选。Git历史不会因此消失。

普通E1上传错误在本次交付额度内自修；真正无法安全发布则交一次LOCAL_ONLY理由与已封存位置，手动上传仅不可恢复兜底，不重新要求科学重跑。不要再传上一次已验收清理的196296B ZIP。

## 8. 终态与证据等级

最终只交一次DELIVERY_ID报告，分别登记：
- ENGINEERING_PRECHECK：实际Windows/纯stub/fake-bare/计数验证结果与首错；
- ARM_A1/A2/A3：SOURCE_CONVERGED_BY_ROUND_N、NOT_CONVERGED_WITHIN_100、ARM_STOPPED_SOURCE_OR_OUTPUT_FAILURE、ARM_STOPPED_RESOURCE_OR_TIME、ARM_STOPPED_OWNER、ARM_STOPPED_SHARED_INTEGRITY或NOT_RUN；分别列真实完整轮数、计费/进入/完整返回/失败/中断/未进入HA数和尾部partial轮。资源/Owner/共享STOP后尚未开始的臂记NOT_RUN，绝不写成已完成100轮；
- SCIENCE_INTEGRITY：可信完整/真实部分/共享硬门FAIL_CLOSED；
- TRANSPORT：远端字节实际核验或LOCAL_ONLY；
- RESOURCE：实际计费、上限、余量关闭、是否异常；
- FORMAL_V010：UNCHANGED，REAL_GE=False、Results FALSE、V011 NOT_STARTED。

一次工程PASS不能代称数值收敛；一次正常100轮非收敛不是工程失败。传输成功不抵消资源超限，kernel计数证据与Codex本机主张/未提供原字节分别标明。无论哪一臂满足源式条件，都仅为TEMP_SYNTHETIC_PRICE_BRIDGE_SENSITIVITY，正式方法采纳由Owner另行决定。

最终STOP = WAIT_ASTRA_TEMP_BLACKBOX_PRICE_TUNING_100_REVIEW。不得自动签发下一调参网格、续算旧额度或启动V011。

## 9. 工程参考（说明机制，不追认旧故障根因）

- Microsoft CreateFileW：FILE_SHARE_DELETE及打开句柄的共享模式含义。https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew
- Python os：buffered file先flush再fsync；replace成功时的替换语义不保证调用无权限/文件系统故障。https://docs.python.org/3/library/os.html
- Microsoft JOBOBJECT_BASIC_ACCOUNTING_INFORMATION与Job Objects：TotalProcesses包含已退出进程；普通消息通知不替代可靠累计计数。https://learn.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-jobobject_basic_accounting_information ; https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects
