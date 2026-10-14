# V0.0.7 原C8历史来源与经济量纲/财政公式证据

状态：PRE_SEAL；SOURCE_ONLY implementation candidate；等待Astra独立验收。
独立实施授权：ASTRA_APPROVED_EXECUTION__CH5_V007__SOURCE_ONLY_HISTORICAL_AND_ECONOMIC_UNIT_AUDIT_ONLY。
冻结：635cea1c54afecc78d6678805a263a889985a291；tree a7b77ef0c915ad28dd9f4dcd90022c4e3ac70f9d；plan blob 940ac55265f5ee9bf9b82c3e955f900fbddf32ce。
代码基线/本候选唯一parent：198b70f8b1c7b802bc2e18cb4bb0825bdb495b00；tree 0c637893d92cafdf72a194b350b3bf7016894d5c。
最终commit/tree及封存后验证位于候选外LOCAL_ONLY交付回执；本文件不预填未来身份。

## 1. 核心判断与证据界限

历史C8的生产和有限运行已有独立接受锚；今天原件是否存在、匹配及可安全读取仍未证。两项经济问题已经具体化为可证伪义务：
1. household分布劳动均值与destination firm总劳动的量纲、人口集合和迭代阶段不能由同名Lt或已有Lt_prev字段自动协调。Python当轮caller确实覆盖了传入的Lt_prev。
2. 若采用通常的人均家庭资产/消费与地区企业/财政总量解释，Lt*tau缺货币计价，AtTax和Tt缺均值至总量桥。代码的源忠实性不能替代经济闭合。
这些是条件推导和静态赋值事实，不是对未读C8数值的运行bug认证。不改任何公式或参数。

证据标签：
- INDEPENDENT_GITHUB_CODE：Astra冻结记录的独立GitHub源码核查；本次本地固定Git对象补充记CODEX_SOURCE_ONLY，不冒充网页独立执行。
- HISTORICALLY_ACCEPTED：独立接受文件记录的当时运行/回读范围。
- CURRENT_BYTE_UNKNOWN：真实原件当前字节与内容未读取。
- PROTECTED_BLOCKED：真实stat/read/hash/parse/extract许可为0，安全访问前置未解除。
- MATLAB_AUXILIARY_REPORTED_BY_FREEZE：Astra曾比对Owner上传ZIP；Codex本轮未直接取得该文本，非历史C8执行字节认证。

## 2. 最小历史crosswalk：不重做源码流水账

固定历史：runner 7b81628a8c54088117878c666995c665935a9617；dispatch 7c88960f16ce0b7dd42bbb99b882334731895749；accepted execution 63ac1ae972fe7f54dc59d2ed58764955088c57ce；后两者src tree均00682b2e1a7ba23665f6e16f6acf48ad35874883。

| 环节 | 已取得依据 | 尚未闭合及最小证据 |
|---|---|---|
| producer/execution版本 | 冻结计划§1及历史独立执行接受；前次Git对象比对确认五个核心blob与V006一致 | 整棵src不同；不能把V006全部工程追认为C8运行版本 |
| entering-C8 states/N/参数 | 执行报告固定JSON/NPZ历史摘要；C8 load_bundle的阶段/省序/字段绑定源码 | 当前JSON/NPZ字段、N、参数及真实内容须阶段B；不以初始化默认值冒充C8实值 |
| 31省terminal/checkpoint | 历史独立回读31个terminal、31组mass、一次integration | 现存叶身份/数值未知；裸aggregate正文无省名/checkpoint，须manifest+batch+writer关系 |
| 五字段 | corrected_household_adapter原质量公式及continuation._batch全部mass_form | 完整真实31省五字段须按需阶段C；不能省略Bt或以四字段middle替代原batch |
| S/raw/rah/距离 | load_bundle及同S数量/payoff、lagged合同 | 原S及raw-ra0-turn7/rah-turn8当前字节未知；距离原件另门；不能混入turn9 seal |
| annual/master/双消费者 | V006仅合成工程接受；2017 observed→2018 target合同 | 真实annual来源、release、经济单位与真实consumer均未授权；不混接run004/C8/C9/fixture |

历史接受文档：
- docs/CH5_K1B_TURN8_OUTER_R2_EXECUTION_INDEPENDENT_REVIEW_20260925.md，3–13行。
- docs/CH5_K1B_TURN8_OUTER_R2_EXECUTION_REPORT_20260925.md，9–35行。
- docs/CH5_DOT_FIXED_C8_INPUT_SAFETY_CONTRACT_20261002.md，20–33行（历史locator和字段资格）。
这些文档按基线固定ref引用。原C8 manifest SHA256：
5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301。
历史5141成员、63801638B是成员总量；manifest自身第5142文件，其本体长度UNKNOWN。C8当时39类ledger已核，不解除后续C9 CALL_LEDGER_UNRESOLVED。严格R2：C6→C7 2/9、C7→C8 5/9，未通过；不是GE或Results。

Entering-C8（完成C7后）JSON历史SHA256：
30EDAECEA59ABA03EFFD6C11530617BB7CF80FED175F58437F4DACA9E96D2F3A。
NPZ历史SHA256：
E6B5D428C1070C6F9F6D9C450F7CDB0D4C2C54F0658074C9C75E60E8FDB743DB。

## 3. MATLAB—Python可比较范围与源码索引

原MATLAB辅助文本没有直接提供给本执行会话；未搜索外部MATLAB目录、ZIP或其他项目。冻结计划§3B记录Astra已见HANK_2ASSETS_HJB.m写results.Lt、HANK_firm.m取results.Lt并使用Govinc式。本轮只把这些作为辅助来源的转述依据；MATLAB中results.Lt在firm前是否另被覆盖、调用顺序、单位注释、Tt与tau定标，均未独立取得，不能断言不存在覆盖。

本轮新增直接Git文本核查集中于家庭Tt实际控制式，不重新读全部历史源码。以下路径及行号统一固定于198b70f8b1c7b802bc2e18cb4bb0825bdb495b00：

| ID | 仓库相对路径、函数/行号 | 科学作用 |
|---|---|---|
| P1 | validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py；_batch 215–224；integrate_turn 235–311、361–371 | 五字段选择；劳动/资本/财政caller；当前覆盖和下一轮状态 |
| P2 | src/ch5_two_asset_hank/multi_province/firm.py；evaluate_firm 44–143，重点77、93、102–110、118–135 | Lt_prev/NKPC相关mt、工资、收益、clip及Govinc |
| P3 | src/ch5_two_asset_hank/multi_province/corrected_household_adapter.py；153–211 | Ct/Lt/At/Bt/AtTax质量聚合 |
| P4 | src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py；_province_inputs 285–329；_solve_province 799–831 | state.Tt/w/tau绑定、terminal writer |
| P5 | src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py；714–730 | Tt传入cell；net_wage=(1-tau)*w*z |
| P6 | src/ch5_two_asset_hank/corrected_diagnostic/selector.py；_controls 388–424 | g_b=net_wage*l+rb*b+Tt-c-d-cost；家庭Tt为直接加项 |
| P7 | src/ch5_two_asset_hank/multi_province/migration_labor.py；98–131 | 来源Ct/N/tau、旧目的工资；destination行汇总 |
| P8 | src/ch5_two_asset_hank/multi_province/wage.py；11–76 | 目的tau、新firm工资；输出origin composite wage |
| P9 | src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py；139–148、165–192、254–262 | MU/NU换算、初始代理与默认参数，不代表C8实值 |
| P10 | src/ch5_two_asset_hank/multi_province/fiscal_diagnostics.py；16–44 | sum(Govinc-Bt*rb*N)，进一步约束Govinc地区总量解释 |
| P11 | src/ch5_two_asset_hank/corrected_diagnostic/lagged_observed_gdp_wedge.py；99–151 | 年份和来源减目的q方向 |
| P12 | src/ch5_two_asset_hank/multi_province/government_assets.py；80–111 | C1残差及超额私人资本保留 |

关键Git blob：P1 37936a422d4ea34d925a2ca67461cd9fc5f40b9e；P2 1f7d37247e2d712fc0477a9f562dce81d1b367ce；P3 f79e089f06d0d74867284dc88c94c594215dc02e；P4 042189063fa5d24480ed4193e133425599b32c8b；P5 a473f86eef22ad893673dba2a80ec8029de8afd1；P6 51517dde0c829060b6e0c0d594ec60e7e6143883。P5/P6是本轮固定基线静态证据，未另行追认其历史执行字节。

## 4. 完整经济量纲矩阵

条件单位：M=10万元，U=100人，T=模型时间，H=尚未认证的个体劳动单位。z和概率质量p无量纲，sum(p)=1时聚合是分布均值，不是地区总量。下表单位是必要候选解释，不是历史实值认证。

| 变量 | 数学定义/候选单位 | 已取得依据 | 缺失条件、经济后果 | 最小验证证据 |
|---|---|---|---|---|
| a,b；At,Bt | At=sum(a*p)，Bt=sum(b*p)；M/U | P3质量公式 | 人均归一化未证；可产生100倍规模错位 | 家庭状态numeraire/人口分母定义与历史校准 |
| c；Ct | Ct=sum(c*p)；M/(U*T) | P3、P6预算漂移 | 资产与消费须共享货币桥及模型期 | c/w/Tt/a/b共同尺度和时间合同 |
| individual l；household Lt | l为政策控制；Lt=sum(z*l*p)；H | P3、P6 | 不天然等于就业、工时或效率劳动人数 | l、z、时间使用与人口覆盖说明 |
| N | 原万人P×100；U | P9 | 模型N和每省人口实际映射未读；绝不用P/3 | 已准entering-C8字段及其来源说明 |
| Y、Ktarget | GDP/资本亿元G或K×1000；Y为M/统计年，资本M | P9、已接受输入修复合同 | 年度流量不能自动等于模型一期流量 | 统计年份、资本构造和共同时间映射 |
| q与Y/N | q=10000G/P元/人；q=1000(Y/N) | P9、P11 | 仅同一统计口径下条件代数；不是工资认证 | 年度GDP/常住人口发布与单位来源 |
| wealth_i | At_i*N_i；M | P1 | 必须[At]=M/U；beta_a=1未识别桥 | 原家庭资产/人口单位共同归一化 |
| S、flows、Kprivate | flows[j,i]=S[j,i]*wealth_i；M | P1、冻结同S合同 | 列守恒保证给定数值，不修复错误单位 | 原S方向/字段身份及wealth单位证据 |
| GovInv、firm K | max(Ktarget-Kprivate,0)；M | P12、P2 | Kfirm=max(Ktarget,Kprivate)，不是强制等于target | 同单位资本输入；C1原规则保持 |
| migration L_ji、Lt_supply | N_i*C_i^(-gamma/phi_l)*(w_old_j*(1-tau_i-sigma_ji)/phi_ji)^(1/phi_l)；候选U*H | P7、P1 | 归一化与来源/目的人口集合须一致；不自动认证现实劳动 | c/w/效用系数尺度及流的经济含义 |
| firm Lt、Lt_prev | 当前destination总劳动 vs caller传household均值 | P1、P2 | 比例差要求同单位、同省角色、可解释的前后阶段 | MATLAB逐赋值/调用顺序和历史状态定义 |
| wjt、composite w | firm边际工资及跨目的聚合；M/(U*H*T) | P2、P8 | 不直接等于元/人年；新旧工资和税位置保持 | 工资numeraire、劳动计价和模型期 |
| tau、sigma | 1-tau-sigma中的比例楔子；无量纲 | P5、P7、P8 | Govinc中tau需明确是否同一税种/计价基准 | 原政策定义、征税基数和财政归属说明 |
| phi_l、gamma、phi_ji、alphal | 前二为指数；后二为效用/聚合系数 | P6–P8、P11 | 货币尺度变换会影响劳动FOC；年度无量纲phi不能单独解决尺度 | 联合效用归一化/校准合同 |
| rk、raw-ra0、rah、used ra、rb | 模型期资本收益；形式上1/T | P2、冻结raw-ra0合同 | raw家庭payoff与used公共资产ra不可混称；日历年化未授权 | 共同时间基准、clip财政处理记录 |
| Corptax | profit*corptau，加收益/工资clip调整；M/T | P2 104–135 | 非仅一个简单利润税；须和firm Y流量一致 | 企业利润、clip和财政记账口径 |
| Lt*tau | 代码直接劳动乘比例税率；U*H | P2、P5–P8 | 通常不能与M/T相加；需独立劳动货币计价或不同税定义 | 工资归一化与原财政税基证据 |
| AtTax | At*rah-sum(a*r_eff*p)；M/(U*T) | P3、P1 | 均值直接加入地区Govinc缺N桥，除非另有可信单位合同 | 原回收收益差的归属/人口转换规则 |
| Tt | 同一state字段直接进入家庭漂移及firm减项；候选M/(U*T) | P4–P6、P2 | 地区财政支出通常应为人口总量；同名变量不证明同单位 | 原transfer definition、受益人口和总量赋值 |
| Govinc、GovSurplus | 财政净流、sum(Govinc-Bt*rb*N)；候选M/T | P2、P10 | 流与均值混加会影响财政诊断；有限数值PASS不能认证 | 上述税/资产收益/转移共同财政会计 |

M/U=100000元/100人=1000元/人。因此Y=1000G、N=100P给出q=1000(Y/N)=10000G/P。若At=1被解释为每人1M，N=1代表100人，则真实总量应100M；若At单位为M/U则At*N=1M。这个100倍条件反例说明桥不能靠标签确认。

量纲与数值归一化必须分开：以固定劳动定义，FOC形如l=(c^(-gamma)*w/kappa)^(1/phi_l)。若c和w同乘h而kappa不变，则l乘h^((1-gamma)/phi_l)；保持l需kappa同时乘h^(1-gamma)。因此不能仅把家庭货币数值换单位而宣称劳动法则未变。本版不做此重标定。

既有docs/CH5_MP4C_PYTHON_RUNTIME_INPUT_BINDING_AND_UNIT_CONTRACT_REPAIR_ACCEPTANCE.md第19–38行只接受宏观输入修复，明确beta_a=1为SOURCE_FAITHFUL_DIAGNOSTIC_ONLY，未识别资产桥/工资绝对归一化。早期household k-unit的h=1是standalone诊断暂定，不是C8最终货币认证。没有取得已接受的完整桥可消除本表义务。

## 5. 疑点A：Lt_prev的单位、人口集合与时序

静态正证据：P1 292–295复制province后，将Lt_prev覆盖为当前batch.household_lt，再以migration.lt_supply作为当前firm Lt。P1 368–371又把firm Lt保存为下一轮Lt_prev，但下一次同一caller会再次覆盖。故“上一轮bundle已有firm Lt_prev”不能解释当前evaluate_firm收到的对象。household输出用entering-C8工资求得，并不因此成为上一日历期destination就业。

可比的必要条件：Lt_prev与Lt须同为目的省、同一劳动/人口单位，且前者代表所采用动态或迭代经济式要求的旧状态。即使补一个N，也未自动解决来源均值→目的流量的重分配和迭代n≠日历t。

条件反例：无迁移的单地区，个体效率劳动前后均1，N=100，真实前后总劳动均100。若caller给Lt_prev=1而Lt=100，则比例为-0.99，实际无变化应为0。
firm的该项为-(1-alpha)*(Lt_prev-Lt)/Lt，再乘pit*theta/epsilon。取纯纸面alpha=1/2、pit=0.02、theta/epsilon=10，mt会多0.099；不是C8参数/结果提取。pit=0会数值遮蔽该项，不能反证单位正确；alpha=1等退化亦须区分。错误关系可能进一步影响mt、工资、资本收益与财政，但本轮不估计实际幅度。

待验证替代解释：
- A1：household Lt本来已按相同destination人口归一化。须证明p/劳动定义的该桥，不能以sum(p)=1或人口标签替代。
- A2：当前migration Lt_supply在进入firm前另除人口/映射。已审Python caller没有此转换；MATLAB调用链未取得，不能推广断言。
- A3：results.Lt在MATLAB firm前被写回旧destination总劳动。必须取得HANK_mp_1turn.m等完整相关赋值区段、调用顺序和state字段含义；目前无直接文本。
- A4：方程是特殊迭代装置而非日历NKPC。须有独立已采纳推导和两个劳动对象的同量纲证明，仅改称迭代不能化解均值/总量错位。

当前裁定：Python覆盖是静态确证；完整经济可比条件尚未建立。MATLAB是否覆盖未独立判定；不宣称已经证实Python独有bug或原MATLAB实际运行错误。

## 6. 疑点B：Govinc逐项审计与最小反例

原式保持：Govinc=Corptax+Lt*tau+AtTax+GovInv*ra-Tt。
按照地区货币财政总流F=M/T的候选解释，必要条件为：
[Corptax]=[Lt*tau]=[AtTax]=[GovInv*ra]=[Tt]=F。

1. Corptax：企业利润和clip调整均按总资本/总劳动计价，条件上为F；不要漏掉clip的财政调整。
2. GovInv*ra：公共资产M乘模型期收益为F，使用源码used ra，不把它替换成家庭raw-ra0。
3. Lt*tau：若Lt=U*H而tau无量纲，单位仍为劳动，不是F。工资率必须提供F/(U*H)的计价桥。假设每个劳动单位按固定w0=1计价，可使数字省略w0，但须证明这是已采用的财政基准；不能因数值工资接近1就认证。若税实际为当前工资比例税，还须有税基/征收归属推导；家庭和迁移位置中的tau确为工资比例楔子，不能静默将它改称金额税。
4. AtTax：P3是同一概率分布的资产收益均值，P1无乘N传给firm。按人均解释需N倍，或证明另有已接受的地区量定义。不能直接加N作为工程修复。
5. Tt：P4→P5→P6链把state.Tt作为每个家庭cell的直接收入，P2从地区Govinc直接减同一数值。P1下一轮仅复制Tt，未见另建地区转移总量。若每个模型人口单位获得t，地区支出应N*t；若Tt是地区总额，家庭式又需要人均桥。N=1或特殊取消不能构成一般证明。初始化transfer_income=0.1仅为静态默认，不是实际C8字段认证。

纸面反例（不运行、不取真实值）：
- 工资税：总劳动100，比例税0.1，工资2个货币流/劳动单位；工资税应20，Lt*tau数值10。若工资恰1两者数字相同，仍需税基和单位证据。
- AtTax：N=100、每模型人口单位收益差0.2，则地区收益差20；直接加0.2相差人口倍数。
- Tt：N=100、每模型人口单位转移0.1，则地区支出10；直接减0.1不能同时代表同一人均预算和总财政。
- 复制地区检验：保持每人口控制和工资不变、K/L/N同倍扩张，若其他财政总量项线性扩张而AtTax=a、Tt=t仍直接作为常数，F(2N)-2F(N)=t-a。a=t可能偶然遮蔽错误，不能分别认证两条总量桥。

问题归属：
- 共享公式问题：冻结记录指出MATLAB和Python均有Govinc式；在标准总量解释下的量纲义务不能归咎于“Python语法移植”。
- Python映射问题：household AtTax/Tt原数值直接送地区firm，以及Lt_prev覆盖，有明确Python静态依据。
- 尚不能归属的问题：MATLAB是否另设劳动货币单位、是否覆盖results.Lt、是否先转换AtTax/Tt；未独立取得辅助源文本，不能证明移植有误或源方程必错。
- 数据不足问题：当前C8实际N、Tt、工资、收益差值未读；读到数值也只能判条件是否满足，不能凭有限值取代经济定义。

最小辅助文本包应由Owner直接提供准确函数及相关完整赋值区段：HANK_2ASSETS_HJB.m的Lt/AtTax/Tt，HANK_firm.m的入口/旧状态/财政式，HANK_mp_1turn.m与multi_prov_HANK_12sts.m的调用及覆盖，Lt_seperate.m、wage_caculate.m的N/工资/税，load_GDPdata.m的单位/定标。只需要有关定义和闭合赋值链，不请求私有原数据或整个外部目录；取得后仍仅辅助文本，不是历史C8字节认证。

## 7. 已定方向与Owner真正需要的科学裁决

保持2017 observed→target2018历史条件回溯；年度phi为1+0.3*(q_origin-q_destination)/(q_origin+q_destination)，与旧Y/L广播差方向不能机械互换。q的公共货币尺度在比值消去，不能认证wage/FOC尺度。固定旧工资+origin tau的migration、新工资+destination tau的composite；不以此次核查更改税位置。

raw-ra0维持每模型期净生产资本收益，无可辩护日历映射；不年化，不把统计年度GDP与一期收益直接等同。价格保持current_price_methodologically_attributed、direct_price_verified=False、price_verified=False、release UNKNOWN、baseyear None。人口/人均已采纳，不N=P/3。

需Owner集中裁决的是：
- E1：上述Lt_prev对象关系在取得完整辅助调用链后，是可证明的统一归一化，还是需要未来版本单独修订动态/迭代劳动状态关系？接受源忠实诊断不等于接受其经济闭合。
- E2：财政目标采用哪套可推导的计价/人口/税基会计？若不能提供共同单位解释，是否授权未来独立科学修订研究；本版不能以乘N/工资补丁替代。
- E3：是否提供最小辅助文本/已接受校准说明以证伪替代解释；这与真实C8数据权限分开。
- P1：是否在独立保护审议后签发下节阶段A。任何B/C/D推进另需明确许可，不因A匹配自动获得。
不重新申请既有Option1、C1、raw-ra0、人口方向或价格方法决定；也不预先要求Owner接受未经证实的bug结论。

## 8. A–D最小真实读取申请：REQUEST_ONLY，实际许可0

公开路径仅为冻结任务已有仓库相对历史locator，不表明存在性。R8=reports/ch5_k1b_turn8_outer_r2_20260925_run001/；R7=reports/ch5_k1b_turn7_outer_r2_20260925_run001/。

| 阶段 | 准确对象及单文件上限 | 能证明什么/不能证明什么 |
|---|---|---|
| A | R8/execution_artifact_manifest.json；1048576B | 当前manifest字节匹配历史独立SHA后，可绑定所列成员path/size/hash；不读成员，不认证单位 |
| B | R8/preflight.json；262144B；R8/turn8/household_batch_receipt.json；65536B；R7/turn8_k1b_input_candidate.json；2097152B；R7/turn8_k1b_frozen_share_payoff_plan.npz；65536B | 核执行预检、31省序/checkpoint、entering-C8 states/N/参数及S/raw/rah；不等于当前31省五字段全量 |
| C | R8/turn8/household/p{index:02d}_{short_name}/stationary_aggregate_receipt.json，精确31个、每个16384B | 仅确需完整真实五字段时；按manifest/batch/writer映射提取五个mass_form；不重算聚合/调用consumer |
| D | docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv；65536B | 可选固定距离源身份/所准字段；不能重算S或扩大模型 |

C的index 0..30按以下准确顺序绑定short_name：
北京、天津、河北、山西、内蒙古、辽宁、吉林、黑龙江、上海、江苏、浙江、安徽、福建、江西、山东、河南、湖北、湖南、广东、广西、海南、重庆、四川、贵州、云南、西藏、陕西、甘肃、青海、宁夏、新疆。
不得目录枚举、递归跟随manifest或追加province_terminal_receipt；如需更强内在checkpoint身份，须正式替换许可名单。

正确累计上限：A 1文件1048576B；A+B 5文件3538944B；A+B+C 36文件4046848B；A+B+C+D 37文件4112384B。前次提案中间两项少计65536B，现按冻结更正保留此错误记录；完整总额未变。这些不是当前读取预算。

每文件权限分列：existence/stat最多1次；bounded byte read最多1次；同缓冲区SHA256最多1次；parse最多1次；字段提取须另准准确成员。单文件每操作attempt<=1，retry0；失败后不换进程/副本/路径续读。hash无需第二次打开。JSON解析须限制编码/深度/重复键，NPZ须另审成员、dtype、解压后尺寸、无pickle与无磁盘解压，不调用既有真实loader；具体实现/依赖/输出边界未获准，不在本版实现。

A先连接独立接受SHA；B两个C8文件由已匹配A成员绑定，entering JSON/NPZ另有固定历史SHA；C需manifest+batch省序+writer关系。缺可信锚时，更多叶文件不能制造独立来源；停止，不碰运气。31叶不是再次证明“当时已运行31省”的必要读取；只恢复全31省五字段才需要。

manifest自身大小UNKNOWN。1MiB是候选cap，未来Owner须先批准独立元数据大小门或明确的新cap；本轮不stat。超cap不得分段读、重试或静默扩额。D仅在明确必要时签发；run004北京三文件不合并，B3副本不自动替代。副本匹配仅证明字节，不证明原件路径/生命周期；任何Owner转交路线须单独来源和权限说明。

A16/window适用边界：该单次被动读取不执行rename/delete/reparse/ACL攻击，成功读取不证明四类敌对保护PASS。它仍需要适用于实际路径祖先/身份/并发替换威胁/进程token/输入输出与LOCAL_ONLY生存期的窄操作合同；Owner与独立保护审议须明确既有A16/window中哪些义务适用于该操作、如何满足，不能由执行者宣告豁免。当前合同不足时PROTECTED_BLOCKED，真实stat/read/hash/parse/extract保持0。

完整值、成员明细和解析对象LOCAL_ONLY；公开仅脱敏身份/计数/资格/单位义务。未来生存期、清理或保留操作须在新合同中明确，本版不删除任何证据。即使37项全部匹配，也不能认证全部经济单位、真实消费者、R2/GE或Results。

## 9. 交付资格上限与停止

仅申请Astra独立审议HISTORICAL_SOURCE_CROSSWALK_DOCUMENTARY_ACCEPTED、ECONOMIC_UNIT_CRITICAL_OBLIGATIONS_ACCEPTED；当前为候选，未自接受。
REAL_C8_SOURCE_AUTHENTICATED=False；ECONOMIC_UNITS_VERIFIED=False；REAL_CONSUMER_AUTHORIZED=False；GE_CONVERGED=False；RESULTS_ACCEPTED=False。
A16 FAIL_CLOSED；window UNACCEPTED；C9 PAUSED；CALL_LEDGER_UNRESOLVED；model_activation=False；Results FALSE；旧科学/数据/consumer预算CLOSED。
交付后WAIT_ASTRA_V007_SOURCE_ONLY_ECONOMIC_EVIDENCE_ACCEPTANCE / STOP；V0.0.8 NOT_STARTED。
