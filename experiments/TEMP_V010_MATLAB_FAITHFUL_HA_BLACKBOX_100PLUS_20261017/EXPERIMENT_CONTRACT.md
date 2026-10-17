# TEMP-V010 · 回归 MATLAB-faithful HA 黑箱的 100+ 轮稳态对照实验

**身份：独立临时实验版本，非正式 V010 修订、非 V011、非新数学方法采纳。**
**实验名：TEMP_V010_MATLAB_FAITHFUL_HA_BLACKBOX_100PLUS_20261017。**
**Owner 2026-10-17 指令要点：** 旧有 Kaplan–Moll 附录两资产 HA 改写成果应当作黑箱；不修改家庭最优策略或其 HJB/KFE 内部；Bellman 残差作诊断非硬否决；撤销 V010 synthetic 外层5轮的实验限制，100轮后看全局轨迹，考虑100轮以上乃至数百轮自然收敛。目标是先实验、再科学比较，不为此解除正式 V010 冻结合同。

## 0. 真实可信的最早已验收 31省 MATLAB–Python 稳态锚点

历史**完整31省**已获正式独立验收的最早明确锚点（不推断仓库可能更早存在未经查证的实现）：
- 2026-09-01正式主审：Commit 84c26d2e61fb397e0e54621869a95c5b136963eb，报告 docs/CH5_TWO_ASSET_HANK_MP4B_L3_FORMAL_CORRECTED2009_STATIONARY_PARITY_ACCEPTANCE_REPORT.md；结论 MP4B_CORRECTED_CALENDAR2009_MATLAB_PYTHON_STATIONARY_PARITY_FORMALLY_ACCEPTED。
- **该成功实跑的固定代码父：Commit 216283cf4f1303afa60f1915e143a0b7303a9ffb，tree b7a28f7afe7e8de23fb5afdfb377d36c9d025b50。** 它在2026-09-01修复旧 one_turn.py 的一个非HA语义错误，source one_turn blob e5d6835cdc9e6d182e1c84e11f4d51938be592e1；不得退回这个修复之前的候选并称为已接受31省parity。
- 其独立家户黑箱 **exports/matlab_faithful_two_asset_ha.py**：固定Git Blob 9e7dc9556a2b76811e78f89999abecc045886106；旧已接受2009执行器要求原字节SHA256 B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3。需在Codex本机实际复核SHA256后才可导入。
- 2009历史原驱动 validators/multi_province/mp4b_python_empirical.py blob b1710ae3c5d8d7baf96e85c932d777fa5f3b908c；source-postloop household adapter validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py blob 0033baee136c0328e80ffb8b794a88d4405c976c。该adapter用旧HJB/原post-convergence KFE/aggregate，但不把未收敛的家庭标志当成禁止进入post-loop和多省反馈的异常；记录家庭是否收敛交外层判断。
- 已接受2009 MATLAB/Python corrected empirical input是**历史验证用2009年运行overlay**，不是全部现实年份的科学正本；旧input SHA256 072E5E943FB6BFF6768CD40001B031C3AF1A6DD92FCC3A86E1B6D476E03E0137，canonical source-binding SHA256 507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48。以上历史输入仅只读参照，不在此任务重新运行或扫2009/2017/2018/C8原始数据。
- 该历史审议实测 MATLAB/Python外层均**184轮**，Python **5704次**家庭调用，最后家庭31/31收敛、ra边界0/0；31省×20状态最大归一化差异3.835889478194021e-11。**100是诊断窗口，不是新的求解最大迭代次数。**
- MATLAB用户原件 HANK_2ASSETS_HJB.m SHA256 049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE；HANK3_FOC.m 772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D；HANK3_cost.m 3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C。它们及Python端各自以原字节身份冻结。

**注意：**该Python文件是对用户历史MATLAB模型的忠实复现版，不是Kaplan–Moll原论文附录的原文件逐字节副本。此处“黑箱”是**使用本项目历史已验收 Python HJB+KFE 算法时禁止改它的代码与行为**，而非声称它从未经过任何移植。

## 1. 实验目标与两条不可混淆的参照线

**CONTROL（不产生新科学调用）：** 保存并独立对照上面2009 31省184轮正式已验收记录、早期的完整HA源码/adapter/runner身份；不默认复跑已验收2009实证稳态，节省成本。

**PRIMARY（这次真正的新实验）：** 用上面**完整冻结、不可修改的** MATLAB-faithful HA 模块替代 V010 2026-10-02模型候选中的 corrected selector 求解入口；对唯一匿名双省 synthetic fixture 做**连续的长外层稳态试验**，从同一冻点起看历史V010首省HA在CP2_F25失败是否仍发生，以及旧HA在两省反馈后能否逐步稳定。V010模型身份固定 Commit 94de4501dec051b969bee9d852eba2d4591f30ef / Tree 205eab47c4e4f9c6292c2ead9947d94d1a7579a5；唯一fixture Git Blob 40915658d93403cfc21b33a6b864b332b7857749 / SHA256 BC002D71430D5472F8C5C62543F07A845F2D6BF564CB5BB92E6DD8142AC50252。

新的主要实验是跨版本HA受控替换，并不等于MATLAB2009真实数据复现，也不能声称只有某一数值阈值导致差异。将**HA方法变更、外层停止门变化和已有V010经济传导修正**分别作为已知处理差异标注，不得归因为单一因果因素。真实31省稳态、其他年份/IRF/Results保持禁令。

## 2. 家庭模块黑箱：绝对不可碰

**以下所有原源码及参数默认配置只读不可写、不可复制改写后冒充同一模块：**
- exports/matlab_faithful_two_asset_ha.py（整个核心HJB、边界、导数、政策upwind、调整成本/FOC、原KFE、聚合全黑箱）
- validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py（原postloop调用语义只读参照；新外围桥仅可调用同样已批准的公共接口）
- 源Commit 216283cf4f1303afa60f1915e143a0b7303a9ffb 里的 src/ch5_two_asset_hank/** 、原测试/validator/exports整体；
- 冻结V010模型commit 94de4501dec051b969bee9d852eba2d4591f30ef的 src/** 、tests/** 、validators/** 、原fixture。

内层HJB网格20×20×2、F-order(b最快)、Delta=1000、单次HA max HJB iterations=100、原source收敛D<1e-7/政策原法则、KFE original contaminated-row及postloop处理**完全不变**。内层100次迭代与外层至少100轮是**两回事**。禁止把新joint Hamiltonian selector、原D1-D3/KKT、Bellman B<=1e-8门、唯一闭类source-free KFE或monotonicity halving植入此黑箱。正常记录Bellman residual数值可观察、不可据此否决家庭结果；家庭converged标志以黑箱原始值为准，外层终止时才要求全部合格。

黑箱不等于容许伪造输出：原黑箱抛错、NaN/Inf、非法结构或无法得到真实分布时必须记录失败并终止实验；不得向输出写入false positive converged、clip资产/概率/收益或替代未求出的状态。保留用户历史模型自身已存在的数值floor和边界规则，不额外引入新floor。

## 3. 外层行为与完整观测

- 采用**一个新的临时实验驱动/桥**，只位于独立scratch或实验命名空间。旧MP4B OnlineStationaryInputs和V010 one_turn/firm/government公式可作为固定源码复用。因为V010 run_mainline_stationary现有max_iterations<=5、run_mainline_one_turn会预先要求每省strict_qualified并在返回states里把convergent设置True，**不得直接拿这两个入口模拟“MATLAB允许家庭中间轮次未收敛，外层继续”**。
- 新桥必须首先以纯stub验证与原V010 2省经济一轮计算公式/状态时序**同值**；除了暂时不对未达D门的HA中间结果进行预拒绝、传递**真实原HA converged**标签之外，不得更改两省宏观经济方程、GovInv×0.9/1.1、Zt、tKN的0.6/0.4、原same-S/前一完整轮raw ra0、目的地税一次及财政人数桥。若不能保证隔离导入两套不同Commit、资产/工资接口、pre-turn工资或同值一轮，请STOP且不开主科学driver。
- 传给旧HA的w_eff必须是**冻结fixture的实际净工资**；可用旧HA的wages=w_eff,tau=0作为明确的经济等价参数化，但只在解析收入/FOC oracle证明不二次征税时允许。r_a/ra-effective taper、rb_gap、Tt、消费初猜V0、原KFE/AtTax要执行**旧黑箱原原样**；初始价格不得改为Owner另给但未测试的单点。两套相同Python包名若发生import shadow/rebind，视为身份失败而非普通测试PASS。
- 外层上限 **max_outer=500**（对应原MATLAB来源），不再沿用V010科学测试5轮上限；仅要到真实原始稳态停止规则满足便可提前结束，不强迫对已收敛状态无谓再迭代。第100轮是预先约定的**自动观察窗口，不是停机点或人工审批点**。100轮未收敛则保持同一个不中断运行，继续至真正收敛、500轮、显式硬故障或资源截止。不切分成每5轮重签/重置预算。外层正常的全部阶段保持无需Astra逐轮介入。
- 收敛与边界行为按MATLAB来源：所有省家庭converged标志为真、max abs(KN/tKN-1)<原reg_threshold、max abs(Yt/Yt_previous-1)<原reg_threshold，所有ra used未触上下边界；记录工资边界但不增加新的工资内点强制门。目标GDP相对差、Bellman残差、HJB D、KFE质量误差/各类边界频率均记录**诊断**，不作为本临时实验额外新的硬收敛条件。非有限、源码异常、非法长度等是实验证据完整性硬故障，不能冒充数值不收敛。
- 运行过程自动保存每轮全部2省的至少：Ct/At/Bt/Lt_HA/Lt_firm/Kt/Yt/ra_used/raw_ra0/GovInv/Zt/w_eff、各自hjb.converged、HJB updates/D、可计算时Bellman B（否则写UNKNOWN）、KFE状态、ra/w边界次数、KN与Y跨轮gap、GDP目标gap、GovInv和Zt修改次数、cycle/oscillation/stalling指标、资产/财政桥残差。关键自动汇总 round 1、10、25、50、75、100及以后每25轮/最终轮；**无人为逐轮STOP**。若程序在100之前因真实源码/数学错误终止，保留已完成全部真实轨迹，不伪造100轮。
- 100轮后对全局时间序列统计收敛趋势，不仅看最后一点：gap rolling窗口、方向及波动/周期、各省边界频率、参数漂移和稳定性。终态只能分为CONVERGED_BY_SOURCE_RULE / NO_CONVERGENCE_BY_500 / EARLY_ERROR_STOP / RESOURCE_STOP；即使CONVERGED，也只是TEMP_SYNTHETIC_EXPLORATORY，不等于正式V010科学接受。

## 4. 一张实验长任务的独立预算与代码权限

**Owner本次“临时版本、至少100轮”决定下的TEMP独立实验额度**（既有M1和F25所有STOP预算保持永久关闭）：
- 科学实验主driver最多**1次**，不中断地最多500个外层迭代 × 2匿名省 = **1000个历史faithful HA黑箱调用**；失败调用也算。Python/工程preflight独立子进程最多12次（纯数学/导入/stub，不含HA/HH solver）；严禁另外发起未计数的smoke HA。
- 墙钟从第一次科学或工程写入开始≤12小时；如超时如实STOP，不重启旧driver或扩大预算；非Git新增实验产物≤512MiB，运行进程RSS采样软目标≤2GiB（不可采样标UNKNOWN，失控须保护性终止），Git网络fetch最多1次仅用于固定身份认证/完整对象，SSH预检最多1次，实验候选非强制push最多1次；网络失败允许LOCAL_ONLY且不为push重启科研运行。
- 只允许**新增文件**于 experiments/TEMP_V010_MATLAB_FAITHFUL_HA_BLACKBOX_100PLUS_20261017/（源码、测试、结果模板）及经BOOTSTRAP预先认证的新独立scratch。原源树、旧接受回执、真实2009 overlay、原模型dirty树/index/外Git common-dir、原M1/F25 scratch、C盘独立SSD备份全部不写。不得改global/system Git设置、SSH secret、pip联网安装、跨项目源码。无第三备份和VM强制要求。
- 推荐新独立scratch D:\ProjectTemp\ch5_temp_matlab_ha_blackbox_100plus_20261017_01；首次写前依V1.3 BOOTSTRAP0可信父路径与protected-root identity → BOOTSTRAP1新建目标后首文件前身份readback → BOOTSTRAP2才可写first receipt/driver。失败后不得删除重建以伪造原始预检；准许严格未写时备用_02。
- 普通E1源外实验驱动、manifest/metrics/JSON、可视化脚本错误Codex在12次工程子进程/12h内自主修复，保留首错；首次写/源码哈希/预算/秘密 E2，或需改变原HA一个字节、原MATLAB经济方程、真实数据范围、正式V010 SCIENTIFIC_DECISIONS E3：STOP并报告，不靠“只是临时实验”逃过硬门。
- GitHub是实验版本的只读授权/必要备份，不是每轮人工task交接。独立实验分支仅由Owner/GPT发布当前冻结说明，Codex不能把工作推送治理/main/冻结模型分支。若按任务白名单发布结果，最多一次普通nonforce push本独立实验分支下的只读结果摘要/新实验脚本（**不**含任何原始私人输入、完整日志、密码或真实数据），路径上限同上述实验目录，文件合计≤512KiB；SSH失败LOCAL_ONLY，由Owner手动上传一个最终私有ZIP。不得建立_review_tmp本地工作树或清理历史review；本轮默认不需要GitHub临时目录中转。

## 5. 终态仅一次性交付，严禁伪造成功

必须一次交付 TEMP_V010_MATLAB_HA_BLACKBOX_100PLUS_RESULT（简洁Markdown + 机器可核JSON/回执），涵盖：
1. 固定历史代码树/HA文件/旧postloop adapter的Git Blob+独立原字节SHA；2009原184轮正式受限接受引证；冻结V010 synthetic fixture与新桥源码/入参身份。
2. 初始匹配的SYN_A/SYN_B及正确净工资/成本/资产口径oracle，1轮stubs验证；HA 100内部迭代与outer 500上限分别计数。
3. 每轮2省且最多500轮的全局轨迹（可放本地原证JSONL/压缩归档）；累计真实HA/driver进程、初始化/KFE失败与首次异常；100轮及终态趋势、边界/参数变化与波动；100轮之前失败如实分类。
4. 与冻结的上一V010 B1 CP2_F25首次FAIL_CLOSED结果**仅做同输入/机制作用域清楚的比较**；不得从两个宏观方程体系不一致的数据推断某种算法更优。
5. FIRST/FINAL独立原文件、run_id、SHA256单向关系、资源实际计数、保护根和UNKNOWN；能读取的证据等级与不能独立复验Windows事实分别记账。

终态只允许：
- TEMP_EXPERIMENT_COMPLETED__OUTER_SOURCE_CONVERGED
- TEMP_EXPERIMENT_COMPLETED__500_TURNS_NONCONVERGED
- TEMP_EXPERIMENT_BLOCKED_AT_BRIDGE_OR_INPUT
- TEMP_EXPERIMENT_STOPPED_EARLY_ON_REAL_ERROR_OR_BUDGET

**实验后STOP待Owner/Astra独立验收。** 不自动转换为V010 accepted HA方案、不恢复真实31省GE/2017/18/C8、不启动V011或论文Results，也不把Bellman低残差缺失伪装成已证明的数值正确性。

## 6. 版本边界声明

本实验本身不用现有 V010 的 D1/D2/D3、joint-Z数学合同来断言数学真伪。正式治理分支 migration/astra-workflow-20261012 的 CURRENT/TASK_CURRENT/SCIENTIFIC_DECISIONS及V010固定Plan均不被此次开临时版本的动作改写。临时对照版旨在检验：**已验收MATLAB-faithful HA黑箱与源式长轮次外层迭代，是否比当前严格V010线路更容易产生持续的省级反馈轨迹和候选稳态。** 这不是自动证明原MATLAB的全部数值细节正确。

实验源码基线Git父commit固定在216283cf4f1303afa60f1915e143a0b7303a9ffb、tree b7a28f7afe7e8de23fb5afdfb377d36c9d025b50，不使用任何V010后续正确但机制不同的HJB solver替换该黑箱。代码比较/编译/实验若在用户Windows不可安全完成，STOP并提交单次结论，不随意补权限。
