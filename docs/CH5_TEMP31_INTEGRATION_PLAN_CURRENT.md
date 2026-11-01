# TEMP31 当前生产接线方案 · 2026-11-01

STATUS=INITIALIZER_SYNTHETIC_PASS__PRODUCTION_BINDING_STATIC_SPEC_READY__IMPLEMENTATION_NOT_DONE
OWNER_SOURCE_ADOPTION=56447829ce0e6c3c85552c53c351b26a2452a4bd__DEVELOPMENT_SOURCE_ANCHOR
SOURCE_ROOT_TREE=7b7cb29dd5b37be92561e7f1bc688c0d29789732
LOCAL_SOURCE_MATERIALIZATION_COMMIT=91941302f966f12d5f206691f74c800cadf3e797__LOCAL_ONLY_NOT_PUSHED
SCIENTIFIC_SOURCE_FREEZE=FALSE

本方案承接Owner对上一轮TEMP31选择建议的同意，落实来源采纳、独立源码工作区和接线设计。不重写V010冻结计划、不恢复旧预算，也不把选定来源等同于接受其中每个历史数值写法。唯一当前进度仍由CH5_LOCAL_FIRST_STATUS_CURRENT.md维护，Owner决定见OWNER_LOCAL_FIRST_CODEX_20261101.md。

当前增量：独立初始化已实施并通过11项静态检查；此前两次单次授权导入停止保留。Owner新批准10个worker有限累计调试后，用3/10通过固定8格初始化数值工程检查，HA及求解0。下列按阶段保留的SPEC_ONLY/未授权/未执行描述为历史过程；以文末增量和唯一短状态为准。

当前生产接线细化规格：[CH5_TEMP31_PRODUCTION_BINDING_SPEC_20261101.md](CH5_TEMP31_PRODUCTION_BINDING_SPEC_20261101.md)。已定点核实20文件身份/20项AST观察，给出工资证据、逐来源地输入、新初始化、HA公开组合、严格资格、批次单位与外层时序的接口及缺口；仍未实现或激活生产入口。

## 已完成的工程基础

选定提交的src、exports、validators、tests及pyproject.toml共565路径、5,817,417源字节已全部物化。每件核对原始Git Blob、字节数和SHA-256；新Git中的四个目录子树和pyproject Blob与原提交逐项一致。新工作区使用独立.git、无alternates，源码物化提交为新根提交，不能冒充原56447829整棵仓库checkout或原历史祖先链。独立Git对象fsck --full --strict通过。

| 范围 | 原提交与新工作区共同身份 |
|---|---|
| src | 8ac1458f0586f1fad58e7bcb85d8acf1a3ef0600 |
| exports | f0614665143257e024cc7857afc3bbaf08e730c0 |
| validators | 3e7f0a8262c398aa8a65914ea376acbc294ebf41 |
| tests | a3281412de682d7c8e127f3bdc0da0d716f386bc |
| pyproject.toml | 5c778f7ccbbabfaf1046d4696cf843dc0adbb34c |

仅复制上述固定公开代码范围；随原目录保留的历史验证脚本不执行。未复制完整仓库历史、原始数据、数组、旧任务日志、源码缓存或MATLAB原件；不是G2全资产归档/恢复认证。原dirty工作树、原TEMP31 snapshot和原对象库保留。代码已齐不证明运行环境、输入或科学解有效。

## 接线对象与验证顺序

| 工作 | 具体实现方向 | 通过依据及当前状态 |
|---|---|---|
| 来源入口分离 | 新TEMP31入口显式绑定选定src；保留历史export及其入口身份关系，避免通过旧mp4b bootstrap混装新export | 先静态列全模块/Blob与实际入口；不以改旧ORACLE_SHA或覆盖export完成认证。PLAN_ONLY |
| 工资生产与家户消费 | 工作目的地tau[j]与sigma[j,i]只进入净工资生产一次；带context/省份轴/期次的净工资记录进入Temp31NetWageInputs；初始化、HJB边界、policy/FOC和预算消费同一记录 | 非对称目的地税、两轴置换、不同省序、伪造已扣税值和重复扣税注入必须可拒；只在获准工程实现范围验证纯结构/代数，不调用求解器。PLAN_ONLY |
| 初始化合同对齐 | 在接线前逐式核TEMP31历史初始化与既有V010冻结合同；不得原样激活已知不一致的helper，也不得暗改科学公式 | 见下方明确阻塞。NOT_CLOSED |
| 多省单轮适配 | 在新独立入口装配家户batch、目的地劳动、资本/回报、企业、工资和财政；先用显式stub观察绑定与账本 | 保留人均/省总量和目的地/来源地轴；不因函数名相似替换经济机制；新科学源码实现与调用须匹配已有合同和具体授权。NOT_STARTED |
| 外层与运行环境 | 明确同源模块加载、版本、runner I/O、状态交接、失败即停和调用预算；独立记录工程import与真实HA | pyproject只有依赖下限，尚无锁定且通过的环境。不安装、不import、不运行旧runner来试探。NOT_STARTED |
| 科学验证 | 获得对应新预算后，从固定输入单点HA开始，严格HJB/KFE及终端聚合；前门通过再考虑多省稳态 | 初猜、价格域、网格、容差、次数/时间/内存和真实数据采用均须对应Owner决定；当前科学调用0，旧耗额不复活。NOT_AUTHORIZED_BY_THIS_PLAN |

## 接线前必须处理的现存初始化不一致

选定源码src/ch5_two_asset_hank/multi_province/temp31_ha_taxfree_bootstrap.py第211行仍为temp=effective*effective+rb*b+Tt；第214行c=wage*l+rb*b+Tt未包含同一资产收益项。这是历史source-derived helper的实际写法，本轮只读识别，未执行、修改或宣称其数值后果已验证。

既有V010冻结计划versions/0.0.10/plan.md（冻结commit bf091da33d59293f147d52c11580327d3ac2a85d，Blob85138d8859d53295262fe13bf5bc277bca95ed3f）第2节明确R=r_b(b)*b+r_a(a)*a+Tt、c0=w_eff*z*l0+R，且不得用旧Rah.*raah错误替代a*r_a(a)。Bootstrap19历史隔离任务保留原初始化写法，来源真实性不授予其生产公式的新资格。

因此本方案不把历史helper接入生产。下一步先形成与已采纳V010合同的精确crosswalk：确认适用主线、初猜与效用式、根域/容差及工资记录；若现行TEMP31专门合同与该冻结要求实质冲突或需要新的科学选择，向Owner提交这一个具体决定。原冻结合同与历史helper均保留，不以一般工程权改写任一方，也不在新运行中恢复已修正错误。

## 其他科学与保护边界

源候选同时包含source-like与origin-normalized劳动函数，生产选择须保持已采纳机制，不由工程归一化便利决定。资本same-S/raw/lagged时序、人口/有效劳动/财政总量、首轮19数值初猜的资格、真实canonical/年份/31省轴、严格生成元/KFE门及16项未决义务均不由本方案接受。

本轮不改科学源码/参数/输入，不启动MATLAB、HJB/KFE/HA/GE/IRF或校准，不通过import触发计算。R12 STOP、R13未授权、六路径WASM STOP、OWNER_BASELINE_REBIND=NOT_AUTHORIZED保持。源码锚点采纳不等于保护状态重绑定。

## 分支清理位置

当前只具备选定代码范围的独立可核验副本。九月源/结果、各历史实验/STOP与私有资产的完整恢复仍未认证；本方案不授权删除分支。后续先逐分支列独有提交、已登记工作树/dirty和证据覆盖，确认保留引用及相应归档/保护门，再形成具体候选清单供Owner决定。

## 2026-11-01 公式来源核查补充（不改冻结合同）

详见CH5_TEMP31_INITIALIZATION_FORMULA_PROVENANCE_20261101.md。已追溯平方项至原MATLAB初始化及九月Python，并由Bootstrap19变换清单确认TEMP31为限域修税而保留该项；资产乘收益率亦可直接在原论文和原MATLAB真实资产漂移中找到。

需要限定本方案前文“初始化不一致”的处理含义：确认平方项缺乏作为收入的来源，不等于V010的V0规则自动成为双账户可行静止政策。非流动资产收益与可消费现金不同；下一步必须明确初猜的资产积累/提款/调整成本和可行性假设。若需改变现有冻结V0合同，提交Owner决定；本轮只补经济解释，不按任何候选公式运行、改源或追改冻结文件。

## 2026-11-01 Owner采纳资产乘收益率：初始化实施规格增量

OWNER_DECISION=USE_A_TIMES_EFFECTIVE_R_A__RATE_SQUARED_REMAINS_HISTORICAL
IMPLEMENTATION_STATUS=SPECIFIED_NOT_IMPLEMENTED__NO_MODEL_CALLS

Owner已明确选择收益率×资产；资本收益项不再是未决定的二选一。既定有效收益率r_a(a)与资产网格a的乘积I_a(a)=a*r_a(a)用于后续初始化设计，保持原收益率来源/折减式与参数，不将利率平方作生产收入。

| 验证对象 | 必须满足的规格 | 当前证据等级 |
|---|---|---|
| 资本收益角色 | 资产数量取对应grid.a[j]，收益率为该资产点的有效r_a(a)，乘积只构造一次 | Owner方向已采纳；代码未实现 |
| 资源一致性 | 劳动根使用的消费资源与计算c0/V0使用的消费资源由同一来源构造；V010的R=r_b(b)*b+a*r_a(a)+T、c0=w_eff*z*l0+R为既有冻结候选规则 | SPEC_ONLY；不追改冻结合同 |
| 零量与符号 | a=0或r_a=0时I_a=0；不取绝对值、平方、floor或clip以改变资本收益符号 | 待纯公式oracle核对，NOT_RUN |
| 资产数量关系 | 固定收益率时资本收益随资产线性缩放；沿现有r_a(a)资产网格变化时不错误要求整体线性 | 待纯公式oracle核对，NOT_RUN |
| 净工资与预算分账 | 净工资仅在生产端扣目的地税一次；资本收益不冒充工资税修正，不以此删去正式两账户的d与chi | SPEC_ONLY；无生产接线或运行 |

完整消费资源/提款/积累/调整成本及可行域解释仍须单列。Owner选定资本收益项并不自动证明V010初猜是两个账户均静止的可行策略；也不授权变更正式经济机制、调用旧helper或重用既有耗尽预算。当前只记录决定与规格，不改源、不执行根求解/模型/测试、不删除历史分支。

## 2026-11-01 实施增量：独立初始化已编码，运行验证未开始

实现与11项静态/符号合同检查见CH5_TEMP31_ASSET_RETURN_INITIALIZER_IMPLEMENTATION_20261101.md。新增源candidate为本地1cdebe761dc4406a83093884ae15f0377d891b8f，旧565路径及历史平方helper保持。

当前可审阅的新入口以a*r_a(a)构造资本收益，并让劳动根、c0与初始效用共用R；通过显式必填resource_convention区分V010数值初猜与真实现金流政策，不接生产路径。11项检查只读AST/符号表达式，实际初始化/root/模型调用0；不能将静态通过升级成数值PASS。下一门是新输入身份、数值初猜语义、受界import/initializer/root验证范围与预算；旧V010执行预算不复用，不自动运行、改正式预算或发布源码candidate。

## 下一次实际初始化验证的具体提案（未授权、未执行）

供Owner单独决定：在固定candidate上，一次新Python子进程、墙钟最多30秒、一次数组初始化、最多8个劳动根、每根maxiter=100；失败即停、重试0。HJB/KFE/HA/GE/IRF/policy/MATLAB调用全部0。运行前须核来源和隔离import，不把此提案当作现有运行许可。

仅用明确标记的合成8格：b=[-0.1,0.1]，a=[0,1]，z=[0.8,1.2]，grid.switch_matrix为2×2零矩阵（初始化不使用）；rah=.09、rb=.02、rb_gap=.07、Tt=.1、rho=.05、gamma_c=2、phi=5、劳动权重1。为完整构造既有参数类型，另记录chi_0=.1、chi_1=2、a_bar=1e-6、mu_z=0、sigma_z=0；这些字段不在本次初始化资源式中消费，不是对调整成本的新经济采纳。工资沿已有numerical_bootstrap19语义：初始20与参考税.05构成19，合成省序A/B、origin0、税向量[.05,.05]、迁移楔为零矩阵，并明确V010_TOTAL_WEALTH_NUMERICAL_INITIAL_GUESS标签；不是实证工资或真实省份。

该提案只检验新初始化函数的同源资源、正消费、FOC残差诊断、有限V0/资产斜率与F-order身份，严格记录实际调用；不改输入或网格救通过。它不是原冻结20×20×2运行，也不修改原V010 fixture或采纳新经济参数。其输入/资源语义、工程import与8次求根预算必须由Owner另行授权；当前均NOT_RUN。

## 2026-11-01 单次探针后的路线位置

Owner已授权前述单次8格验证。唯一worker运行2.438秒后在依赖导入阶段停止：验证器把socket.gethostname本机元数据查询误归入socket.*禁止事件。初始化/root/Brent和HJB/KFE/HA/GE/IRF/policy/MATLAB调用均0；未生成V0，数值性质未测得。详见实现说明文末及Owner记录；原执行证据保留，不修后重试，本次1/1尝试已消耗。

路线仍在“独立初始化静态通过、数值验证尚未到达”处，未进入生产接线或严格驻定。下一具体方案只修正验证器对本机名事件的误拦截，维持固定源/固定合成输入和原30秒、单进程、一次初始化、8根/maxiter100、零重试限制；它是未实施的新提案，新worker需Owner另行授权。后续生产接线、31省/GE/动态/IRF/福利与Results门均未放行。原保护门、历史科学预算与分支清理限制保持。

## 2026-11-01 第二次单次授权后的路线位置

Owner明确批准上述同限额新探针，另表示稍后提供可纳入项目规则/长期记忆的通用数值调试细则。已按批准仅排除本机名事件；新worker在1.532秒后因stdlib Windows版本查询拟调用本地ver命令、触发仍保持的子进程禁止门而停止。该本地命令未创建，初始化/root和全部模型求解累计0；没有在本次授权内自动修改防护再试。

当前仍为11项静态通过、数值验证未到达；不能越过初始化门接生产或宣称严格驻定/Results。后续工程需明确Windows元数据查询的验证器接口；通用授权细则尚未收到，本轮不把“下方给你”外推为无限次或新增科学预算。两次独立授权/原始证据分开保留，科学源码、合成输入与所有保护门保持。

## 2026-11-01 固定合成初始化通过；HA黑箱及价格来源约束落地

Owner已批准专门有限调试规则，见CH5_TEMP31_BOUNDED_INITIALIZER_DEBUG_AUTHORIZATION_20261101.md及AGENTS。新预算用3/10，前两次只修验证器导入误拦截；第三次2.375秒通过固定8格工程数值检查。累计初始化1、劳动根/两层Brent各8、HA/HJB/KFE/GE/IRF/policy/MATLAB均0；成功即停，余7不自动消耗或恢复。源码、合成输入、原根域/容差和HA grid参数保持，具体诊断与输出身份见实现说明文末。

HA网格作为不可变黑箱，不能为收敛改变节点、上下界、轴/切换矩阵；本次独立8格fixture不替换生产HA网格。价格必须参考经认证历史测试：R1–R3已测分量包络rah[.045,.09]、rb[.01,.03]、净wt[15.5,22]，本次(.09,.02,净19)直接对应R1 P0。所有这些是离散诊断点，严格驻定认证点仍0，不能把分量包络任意组合成认证连续可行域或采纳企业毛工资。

路线推进到“独立初始化静态+固定合成数值工程检查通过”；下一步是生产绑定的静态规格与来源/网格/价格身份接口。生产接线未实施，真实双账户政策可行性、严格驻定、31省/GE/动态/IRF/福利和Results均未获得本次通过资格。旧预算、保护门、历史证据和清理限制保持。

## 2026-11-01 生产静态接线规格完成

已完成当前年度入口链的限定核查，详见上述生产接线规格。静态确认旧年度入口仍使用历史bootstrap/平方初始化/含tau输入，旧单轮劳动仍为来源地税；净工资生产者本身已扣目的地税，不能继续向家户端重复扣。现有后轮工资证据明确为合成公式见证，真实生产凭据及消费者校验桥尚未实现。新HA包装/严格资格也尚未实现：原adapter无HJB收敛条件即调用KFE，原KFE结果的raw_residual_inf不是原驻定方程证书，旧外层HJB-only标志不能替代严格资格。

本轮只绑定原HA网格构造式与来源，未生成/更改任何生产节点；家庭rah/净wt历史包络和企业ra/wjt及其边界已在规格中区分，不自动重设企业clamp。最小拟议劳动路线保持现有source-like机制并修目的地税索引；归一化替代路线未采纳，若改机制仍需Owner决定。输入人口/年频/货币单位、真实canonical和实际生产依赖闭合均未因静态检查获得认证。

下一可实施工程分片是隔离惰性接口与显式stub-only检查，不导入模型、不改变经济公式/HA网格或消耗7个剩余合成worker来运行800格HA。其后真实HA、严格驻定和生产运行须各自对应来源、科学决定和预算。本轮科学import/initializer/root/HA/HJB/KFE/GE/IRF/policy/MATLAB均0，源码未改，保护门/旧证据/Results FALSE保持。
