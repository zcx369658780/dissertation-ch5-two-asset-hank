# TEMP-V010 · 两类家庭价格传递的2×2受控比较（100轮硬上限）

**TASK_ID：TEMP_V010_PRICE_BRIDGE_FACTORIAL_100_ROUND_LONG_TASK**
**DELIVERY_ID：TEMP_V010_PRICE_BRIDGE_FACTORIAL_100_LONG_RESULT**
**Owner 2026-10-18明确批准：**“我同意下一轮在独立 TEMP 版本中研究这两种价格桥的对照，而正式 V010 继续保持冻结。其实100轮已经足够了，至少是否收敛已经可以判断出来了。请继续下达任务单。”
**性质：一张完整TEMP版本科研对照长任务；本临时经济价格输入试验获Owner E3研究授权，不构成正式V010经济法则采纳；绝不改HA黑箱。**
**发行时固定Commit与本任务Git Blob由签发后治理Owner Memo精确登记；今后不改本任务发行原字节。**
**最终STOP：WAIT_ASTRA_TEMP_V010_PRICE_BRIDGE_FACTORIAL_100_REVIEW / STOP**。

## 一、科学问题和不能混用的基准

当前经过独立审计的TEMP匿名双省100轮：终态\`OWNER_100_ROUND_LIMIT_NONCONVERGED\`，SYN_A/SYN_B均100/100轮企业资本回报率\`ra_used=ramax=.09\`，其\`ra0_raw\`最低约0.3733/0.4155；家庭收敛0/2，最终max KN gap0.107521825623095，max Y跨轮gap0.0127193109669088。曾有完整HA返回200次、另有一次Owner中断HA计费，总201；原家庭模块原字节不变。100轮是**本实验判断的确定观察窗口和上限，不是证明无穷期永远不收敛**。既往TEMP预算关闭，不延用。

此次只检验两个**进入下一轮家庭HA的价格传递选择**对两省反馈和触界程度的影响，不修改企业利润、GDP目标、资本数量、政府、移民劳动、税账或HA算法。两因子构成4组：

| ARM | 资本回报给来源家庭\`rah_i\` | 净工资给来源家庭\`w_eff_i\` | 是否新科学运行 |
|---|---|---|---|
| \`A0_RAW_RA0_RAW_WT0\` | \`Σ_j S[j,i] ra0_raw[j]\` | \`mainline_effective_wages(wt0)\` | **否**；复用已经验收的历史100轮 |
| \`A1_USED_RA_RAW_WT0\` | \`Σ_j S[j,i] ra_used[j]\` | \`mainline_effective_wages(wt0)\` | 是，最多100轮 |
| \`A2_RAW_RA_USED_WJT\` | \`Σ_j S[j,i] ra0_raw[j]\` | \`mainline_effective_wages(wjt_used)\` | 是，最多100轮 |
| \`A3_USED_RA_USED_WJT\` | \`Σ_j S[j,i] ra_used[j]\` | \`mainline_effective_wages(wjt_used)\` | 是，最多100轮 |

所有\`S\`列总和为1，\`j\`是目的地、\`i\`是来源地。注意\`ra_used\`是已冻结企业模块\`firm.ra\`（而非手工再\`clip\`其他变量），\`wjt_used\`是\`firm.wjt\`，\`ra0_raw\`和\`wt0\`仍分别为\`firm.ra0\`、\`firm.wt0\`。不得用A1/A3的used回报重新训练/构造\`S\`评分；份额律始终采用**前一完整轮raw ra0**的zscore(ddof=0)、distance、theta、beta2/.5和同轮同\`S\`量/收益绑定；份额随各ARM内生状态而变，不强迫不同实验臂以后份额相等。

**只新跑A1/A2/A3三条路径**。A0以前一轮Owner已经上传的原始100轮证据为固定只读对照，不重新付费跑同一baseline，不把以前的Owner中断+续算两science driver变写成一个不中断科学过程。

## 二、源身份及过去实证资格（先验不可变）

本新实验Git分支必须由旧隔离TEMP任务发行Commit \`503b418f790d61049f3df9016a783dcecc793237\` / tree \`4ed1a949074056a0b81e17d5bf6047bc4af607f0\` 派生，仅新增长任务合同，不修改任一源文件。该原TEMP由历史已验收的2009年31省MATLAB/Python共184轮校准基线 \`216283cf4f1303afa60f1915e143a0b7303a9ffb\` / tree \`b7a28f7afe7e8de23fb5afdfb377d36c9d025b50\` 派生；正式独立接受2009年稳态的Commit \`84c26d2e61fb397e0e54621869a95c5b136963eb\`只适用于其原正确日历2009运行。

**历史faithful HA不得修改一个字节**：
- \`exports/matlab_faithful_two_asset_ha.py\` Git Blob \`9e7dc9556a2b76811e78f89999abecc045886106\`、SHA256 \`B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3\`；
- 原source-postloop adapter \`validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py\` Blob \`0033baee136c0328e80ffb8b794a88d4405c976c\`，SHA256 \`8A6308870606A02886E9A8E4B32E942A7D433237405E6B9E86EE4175FB2DFF06\`；
- 原2009来源只作静态对照，不再次运行任何真实2009/2017/2018/C8或31省。
- V010物理冻结数学源码Commit \`94de4501dec051b969bee9d852eba2d4591f30ef\` / tree \`205eab47c4e4f9c6292c2ead9947d94d1a7579a5\`，原经济单位、国资、same-S与劳动税合同都不改；
- 唯一匿名双省fixture Git Blob \`40915658d93403cfc21b33a6b864b332b7857749\`、SHA256 \`BC002D71430D5472F8C5C62543F07A845F2D6BF564CB5BB92E6DD8142AC50252\`；
- 上轮TEMP运行包 \`TEMP_V010_MATLAB_HA_BLACKBOX_100PLUS_EVIDENCE.zip\` **6,352,227B**、SHA256 \`4CD602CC3589F404E176937B96D21E265EB036374BCA95D708E5DC246A394156\`，包含源证 \`experiment_bridge.py\` SHA256 \`73D21D91DCDF421E5F65EEE7EEF862978A5EC720E5AD754C3533EC934B05FA28\`、\`temp_driver.py\` SHA256 \`C4F6AEDFC9AE22AFC5E2DDC59D490EEE29267049DE132090D36DF93F0A42E001\`、\`temp_loader.py\` SHA256 \`7F11ED574F7FB6EB57B42223CDB03334C81FD0943C4FC3385E46D715BDC20B53\`、全100轮\`run/trajectory.jsonl\` SHA256 \`99E849304674BAC1608176EA3903AAF60EC9B3BF6E4A7A39243E497FA2CF7303\`，旧TEMP顾问审议 \`docs/CH5_TEMP_V010_BLACKBOX_100_ROUNDS_INDEPENDENT_REVIEW_20261018.md\`，价格来源审议 \`docs/CH5_TEMP_V010_RA_BOUNDARY_SOURCE_ONLY_FORENSIC_20261018.md\`；
- **只读取此已知ZIP和指定成员**，不要枚举更早已STOP科研scratch的其它无名路径。固定\`A0\`的100轮原件和真实HA摘要作为对照，不能用100轮报告重新模拟基准科学结果。
- 必须验证源码精确来源、Git Blob SHA、所有原始字节、模块导入边界和前轮HA黑箱计算入口。任何认证失败E2停止，不能假定同名脚本即已认证。

原HA每次20×20×2/F-order b最快/Delta=1000/最多100次内部HJB更新/source\`D<1e-7\`的converged标志/原MATLAB-faithful KFE contaminated-row/postloop全部保持。Bellman B、KFE负数尾数、KKT等保留观察值但不得变成此次另加的数学PASS门；源码抛错、数组非有限/非法shape以及前置预算门属于真实不可伪造的硬停止。结果要区分原HJB收敛标志、实际返回的KFE、真正外层source收敛条件。

## 三、实验桥的准确允许变化，禁止“看似变价却没有影响HA”

**唯一可改之处是独立TEMP实验脚本对\`entering household prices\`的两个字段赋值**；冻结原V010\`src/\`、原HA\`exports/\`、2009 adapter、原TEMP旧源码、政策/测试/fixture均只读。

上一TEMP\`experiment_bridge.py\`是宏观一轮参考。固定V010 \`multi_province/one_turn.py:346–363\` 的 \`prepare_mainline_household_states\` 会在**每轮第2轮起、调用HA之前**重新用\`ra0_raw_previous\`以及raw score构建portfolio\`S\`，并覆盖输入\`rah\`；这正是本实验最危险的「bridge改了，进入HA前又被覆盖」陷阱。必须新建**TEMP-only\`prepare_prices_for_arm\`包装器**：
- 第一轮，全部ARM **精确使用原fixture的initial_household_rah、initial w_eff、rb、Tt、rb_gap等**，不预先替换报价；同一初始fixture保证可比性。第1轮匿名两省的原HA进入输入哈希必须与A0已归档第1轮原值及黑箱身份一致。
- 从第2轮起，对该ARM实际第t-1轮完成后封存的\`ra0_raw_previous\`，只使用raw滞后信号计算固定\`S_t\`；无论ARM回报类型如何，**\(S_t\)的评分输入始终为raw，theta/distance及外资本份额律不变**。
- A0/A2：\(\mathrm{rah}_{i,t}=\sum_j S_{ji,t}\,\mathrm{ra0\_raw}_{j,t-1}\)；A1/A3：\(\mathrm{rah}_{i,t}=\sum_j S_{ji,t}\,\mathrm{ra\_used}_{j,t-1}\)，其中后一\`ra_used\`从真实已完成企业态\`state['ra']\`读取，不得从原raw重clip或改写原\`ra0_raw_previous\`。
- 显示/上一轮状态中的\`rah\`也应有相应ARM标记，并在**真正进入HA的当前S绑定之后**才保存权威\`effectiveRahUsedByHA\`，同时记录post-turn上一同轮S预测与next-turn实际S可能不同的来源。**进入HA前必须用哈希及独立公式oracle验证ARM的rah值，不能只查one-turn输出字段。**
- 原capital quantity的\`S_t\`要用**同一raw-score形成的S_t**，\`sum_j S_{ji}=1\`、私人资金配置守恒；\`capital_network.py\`的原zscore/score和asset数量不改、不用新used-return-score。若旧\`prepare\`函数重算raw\`rah\`，新TEMP包装器须在其返回后明确覆盖为ARM口径；捕获实际进入HA的字段。禁止抄写/替代两资产HJB。
- 当轮企业得出真实\`firm.wt0\`与\`firm.wjt\`之后，A0/A1仅把raw\`wt0\`用于\`mainline_effective_wages\`，A2/A3仅把used\`wjt\`用于该函数；将结果作为**下一轮家庭净工资\`w_eff\`**，HA内使用\`wages=w_eff,tau_HA=0\`，不能二次扣目的地税。不得错误地让当前轮HA使用尚未算出的当前企业工资。
- **不可改变的其他传导**：当前宏观桥用于双边劳动重构的\`wjt_gross\`继续沿旧raw\`wt0\`字段；企业生产工资方程、资本收益\`ra0/ra\`及边界裁切、\`Corptax\`边界补偿、\`tau*wt0*Lt_firm\`财政税基、GovInv×0.9/1.1，Zt/KN平滑、tKN 0.6/0.4、份额beta、人口/家庭/企业劳动、same-turn与lagged firms及政策输入严格保留。**这是纯家庭输入价格干预，不是恢复整套原MATLAB企业财政市场闭合；任何结果只能称TEMP cross-bridge sensitivity。**
- 修改不得泄漏到\`src/\`或\`exports/\`；不得改真实数据、经济偏好、KFE实现、VO原初值/根求解或资产网格，不能“为实验跑通”改firm价格边界或求解收敛阈值。

## 四、先无需科学求解的完整验证，再运行A1/A2/A3

**工程Gate P0（HA/HJB/KFE=0）**：
1. V1.3 BOOTSTRAP0/1/2首次写前身份＋仅新scratch保护；从Git固定identity装配旧黑箱及V010模块、原100轮实验桥脚本参考；记录固定Commit/Blob/来源、完整原字节、环境版本。旧完整100轮轨迹静态验证100×2记录与baseline终态；若原件只在其他受保护scratch且不可合法读取，依Owner已上传的那个固定ZIP在本地受控位置取得，不扫描原旧路径。
2. Pure stub F1：相同冻结第1轮各ARM输入完全一致；先给相同\`PreFrozenHouseholdOutputBatch\`（取已封存第1轮真实数据作常量）计算相同宏观一轮：除各ARM选定\`next price/rah\`外，\`Ct/At/Bt\`、\`firm ra0/ra\`、\`firm wt0/wjt\`、\`S\`、\`private K\`、\`Lt_mat\`、\`GovInv/Zt\`、财政式均精确相同。不得在stub里重跑HA。
3. Pure stub F2：\`1+1\`下一轮准备，检查A1/A3 的pre-HA \`rah\`取\`state['ra'] @ S\`，A0/A2取\`ra0_raw_previous @ S\`；A2/A3下一轮\`w_eff\`取\`firm.wjt\`，A0/A1取\`firm.wt0\`；验证不会被旧\`prepare_mainline_household_states\`静默重置。先看**两条价格的实际pre-Ha字节/float64值**，并留反例当一字段不同能被测试检出。
4. 直接以真实第100轮已归档价格作**不运行HA**的双因子代数对照oracle：第100轮raw \`rah~0.389/.419\` 对used \`rah=.09/.09\`，raw\`w_eff~6.948/7.029\` vs used\`~2.038/2.019\`，验证所有四ARM选价逻辑按冻结公式，且orig VAT/GovInc/price wedges不被测试非法改动。此处只是同一旧状态下静态反事实，不充作新解。
5. 编译/允许的focused单元回归＋人工反例：负净工资幂基、未找到原文件、两来源不对应、源Hash不同、S列不守恒、跨ARM price混用、误把\`ra_used\`当raw score、双重工资税、原blackbox变动，应有明确FAIL。所有P0失败可以在明确TEMP白名单/余额内修复E1并保留首错；数学/身份/原保护/E3错误STOP。

**科学Gate P1**：三ARM使用**同一个**冻结双省初始fixture、相同HA源码/环境，分别从第1轮开始（不是从原A0第100轮热启动），独立science run ID；第1轮pre-HA两个匿名省输入原字节/浮点身份同A0固定第1轮相等；第2轮起干预。三ARM各由一个独立science driver在最多100轮或源式提前收敛时停止，运行过程不逐轮等Astra/Owner确认。每ARM最多200次HA（包含其可能失败），全任务≤600；HA首次计费须在实际调用任何V0/HJB/KFE前持久记录。
- Source stop仍为\`all(hjb.converged)\`、\`max KN/tKN gap<1e-9\`、\`max Y/Y_previous gap<1e-9\`及所有\`ra_used\`严格非界内；\`wjt\`是否边界只记录，不新增强制边界条件。原源码异常/非有限/质量不可用不能靠补值延续。
- 100轮未收敛即\`NOT_CONVERGED_WITHIN_100\`并停止该ARM，不续算到500、不从第100轮续算、不复用未消耗预算换参重跑。若原条件更早合格，即\`SOURCE_CONVERGED_BY_ROUND_N\`自然早停，不强行跑足100。
- ARM早期异常/预算缺失，封存首次失败、该ARM立即STOP、不隐性重跑；若异常只与该ARM经济方程/状态价格相关，且完整源码身份和预算仍可信，可继续其它**先冻结**ARM的一次执行（不替失败ARM重试）；任何共享身份、原黑箱、保护根、账本可信性受损则整个任务FAIL_CLOSED。新试验科学预算不可拿历史A0旧余额替补。
- 每轮每省保存\`preHArah,preHAwEff,previousRa0Raw,previousRaUsed,scoreRaw, S, capital, firm ra0/ra, wt0/wjt, wageTaxSource\`、\`household converged/HJB updates/HJB D/B diagnostic/KFE returned/mass min/max\`、\`GovInv,Zt,Y,K,L_firm,At,Bt,Ct,tax,public K,source flags\`及合格条件、原值和边界余量。第1/10/25/50/75/100轮及最终轮自动摘要，所有轮静态轨迹完整记录。**Bellman只是diagnostic，不参与新实验拒绝门**；不能将原HJB未收敛标志偷偷改True。
- 终态比较以全部100轮 \`max ra0-ramax\`/持续边界频率、\`ra_used\`、\`wjt\`、KN/Y gap 25轮滚动方向、HJB合格轮/两省共同合格轮、GovInv/Zt调节次数、私人资本守恒、工资税/财政恒等、变化在第2轮开始的首个事实为核心。单ARM 100轮未收敛不等于不存在任何将来稳态。
- 构成2×2因子差异及交互项时**只有4ARM在同轮可比且有值**才计算；A0历史是前47轮被Owner中断后续算至100轮，报告这项与新三ARM独立单进程的执行差异，不将因子差异宣称因果统计显著性检验或论文估计。

## 五、独立预算、源码安全和执行边界

- 这是一张**新Owner批准TEMP方法对照**，不是旧TEMP的1000 HA余额或正式V010 M1/F25额度解封。总science drivers最多3个（各ARM 1个，不能重试失败ARM）；每ARM至多100轮×2匿名省＝200次HA，**三ARM全局最多600个真实HA**，各HA最多原黑箱100次HJB迭代（不可额外放大），每返回HA的原KFE最多一次，不在后台启动单独GA/GE。原HJB数值容差及消费/资产算法不改。
- 工程non-solver Python子进程（含测试/打包和辅助脚本）≤24，其中focused pytest启动≤8；科学driver分别有独立计数，失败/预启动也计入相应数量；不借工程预算运行黑箱。总墙钟从首次实际写/测试起≤24小时，累计不因脚本退出或E1修复而重置。新非Git artifacts总量≤512 MiB，科学进程RSS采样软目标≤2GiB，异常内存/磁盘/日志/壁钟停止并真实计费；无法监测记录UNKNOWN，不能伪造0。
- 私人历史A0证据ZIP6,352,227B及其中固定成员只读读取累计≤128MiB；新挂载old/reference源码需认证来源，首次身份不足FAIL_CLOSED。不要求第三备份或虚拟机。可信Windows隔离残余风险保留\`FULL_RUNNER_IO_CLOSURE=BLOCKED\`，不是独立OS_NATIVE_SANDBOX_PASS。
- 新源码/脚本/证据允许写在全新已认证的\`D:\ProjectTemp\ch5_temp_pricebridge_2x2_100_20261018_01\` scratch，并只允许作为TEMP衍生在本实验命名空间建立新文件。原8dirty/index/external common-dir、原M1/F25/TEMP100 scratch与第一原始实验、C盘物理独立SSD备份、历史MATLAB、全部旧Git工作树、real C8/2017/2018/B3/V009及数据资产不得写入、checkout、reset、stash、clean、merge、worktree attach或共享Git对象。先V1.3 BOOTSTRAP0只读父/目标路径身份 → 创建新scratch并在首写前二次认证 → 再准备源码和日志，首次违约不可后补。不得联网pip下载/改全局Git配置/多生成器写journal。
- 只能修复新TEMP实验桥/纯实验测试/证据包装E1，不能修改上述被冻结的\`exports/\`、\`validators/\`、\`src/\`或经济数学参数、V010 prior blackbox、网络分配、真实数据以及SCIENCE_DECISIONS。需要触及新第三个经济通道或修HA则E3 STOP，请Owner另裁决。所有新代码hash和pre/post成对原字节接线证明入私有包。

## 六、GitHub脱敏MD + ZIP优先交付，验收后清理（Owner 2026-10-18规则）

本任务正式适用\`docs/CH5_OWNER_REVIEW_MD_ZIP_TEMP_EXCHANGE_POLICY_20261018.md\`；**审核原件私下保存与remote sanitized衍生必须分账**。
- 目标review ref固定唯一：\`review/ch5-temp-pricebridge-factorial100-20261018\`，必须首次读回不存在。
- 只允许**远端独立review分支当前Git Tree**的 \`_review_tmp/ch5/temp-v010-pricebridge-2x2-100-20261018/\` 下三件：\`result.md\`（≤128KiB）、\`manifest.json\`（≤256KiB）、\`evidence_sanitized.zip\`（压缩≤32MiB、解压≤256MiB、成员≤3000、严格递归检查内嵌档案、前后比对哈希）。其他路径及文件0，原工作树/index绝无\`_review_tmp\`目录。
- 固定唯一review父Commit为**本新任务正式发行Commit**，子树只能新增三件；本任务在新独立bare Git对象仓完整对象前提下，用既有SSH Key、\`ssh.github.com:443\`，最多1次SSH预检、最多1次为必需父对象的已授权fetch、1次普通nonforce push；不修改main/治理/冻结实验模型branch，不用PAT、global/system git config、force和额外重试。首次SSH失败则 \`LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED\`，**不影响已经合法完成的科学结果，也不允许科学重跑**。
- ZIP扫描必须逐成员，包含nested ZIP/tar及二进制meta中的私人Windows绝对路径、用户名、私人IP/邮箱、token/ssh/argv/env、受保护真实数据、symlink/绝对解压路径/../巨额解压/重复成员；不确定成员禁止发布。脱敏\`evidence_sanitized.zip\`以synthetic全轮CSV/JSON与相应hash回执、图形、少量静态衍生脚本为主，必要完整binary只限明确合成V/density，不需将全部600组RAW原件上云。原RAW完整证据留在本地/Owner许可两SSD，manifest清楚分\`RAW_EXACT\`与\`SANITIZED_DERIVATIVE\`原始SHA256/长度及失去内容的证据等级。禁止GitHub清理后宣称Git历史不可读。
- Astra后续先取精确review commit+tree+三blob，独立复核原字节包括二进制ZIP（若连接器不能取得真实字节则由Owner上传私有原证补充、不得假称PASS）；先在治理分支永久归档数学、预算与结果并远端回读，再只删除上述独立review当前分支的三个白名单临时文件/核对清理Commit，不能清理历史模型源码或Git对象。旧Git历史仍保留。
- 把原本真RAW和完整scientific ledger封存为一个本地私人ZIP；如remote不成立，Owner可上传PRIVATE ZIP/MD供独立审核。**不要将SSH失败变成新代码bug工作循环。**

## 七、集中交付与终态

只交一次\`TEMP_V010_PRICE_BRIDGE_FACTORIAL_100_LONG_RESULT\`；提供冻结source identity、基准A0原件SHA，三新ARM每轮输入身份/新TEMP桥SHA、100轮轨迹（或合法早停时真实已运行轮数）、原收敛门是否满足、原始与used价格距离、家庭HJB源式收敛次数、长期ra触界频率、GovInv/Zt控制行为、比较表及交互项，真实3个science driver/HA≤600计数、硬故障与首错、source unchanged、private ZIP/远端sanitized ZIP验证级别/清理权限说明。三ARM完成或合法STOP后立即WAIT_ASTRA，不允许把报告自称正式V010科研验收，不自动发下张模型任务。

**正式治理\`migration/astra-workflow-20261012\`的\`CURRENT/TASK_CURRENT=ACTIVE_TASK_NONE\`、V010冻结Plan Blob \`85138d8859d53295262fe13bf5bc277bca95ed3f\`、旧CP2/F25的原Owner联合切换规则、\`model_activation=False\`、\`REAL_GE=False\`、\`Results FALSE\`、\`V011 NOT_STARTED\`均原样不动。实验成功仅是 TEMP_SYNTHETIC_OPTION_COMPARISON 而不是论文结果。**