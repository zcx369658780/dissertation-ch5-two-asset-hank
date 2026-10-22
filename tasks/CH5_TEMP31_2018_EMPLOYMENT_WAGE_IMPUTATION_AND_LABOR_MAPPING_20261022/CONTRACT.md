# CH5 TEMP31｜2018工资—就业统计面板证据复用、有限插值与家庭—企业劳动整体映射（一次长任务）
TASK_ID=CH5_TEMP31_2018_EMPLOYMENT_WAGE_IMPUTATION_AND_LABOR_MAPPING_20261022
REVISION=ISSUED_20261022_R1
OWNER_APPROVAL=2026-10-22__OFFICIAL_CONTINUED_DATA_RESEARCH__CONDITIONAL_INTERPOLATION__FOCUS_SYSTEM_WIDE_MAPPING
GOVERNANCE_BASELINE=4500347a525c39a8d7c5c2a483fac19bebaa18a3
REVIEW_BRANCH=review/ch5-temp31-wage-employment-mapping-20181022
REVIEW_FIXED_PARENT=4500347a525c39a8d7c5c2a483fac19bebaa18a3
REVIEW_TEMP_PATH=_review_tmp/ch5/temp31-wage-employment-mapping-20181022/
TYPE=SOURCE_ONLY_DATA_IMPUTATION_AND_NONHA_SYMBOLIC_STRUCTURAL_MODEL_BRIDGE
HA_HJB_KFE_ROOTS_SCIENCE_DRIVER_OUTER_GE_IRF=ALL_ZERO
V010=FROZEN
Results=FALSE
V011=NOT_STARTED

## 1. 经济学问题优先于机械凑满31行
Owner决定允许继续官方工资/就业资料检索与有依据的缺失值插值，注意力转向将工资、就业、居民/家庭人口和省际迁移接入多省异质家庭—企业模型。源工资是2018年城镇私营/非私营单位税前平均工资，不是全社会全部劳动者平均工资；就业应区分居住地、工作地、单位统计范围、年末人数与年度平均人数。国家统计局2025年答复：分省全社会就业人数和城镇非私营单位就业人数范围/数据来源不同，2020年后才开始按年统一测算发布分省就业人数；不得将2020年以后口径直接当2018同质值。
本任务不仅搜集数据，更要形成一个有经济学含义、可以在后续Owner批准后接入TEMP31的SOURCE_ONLY变量合同、数学桥接、31省结构oracle和待定参数清单。禁止自动确定HU、asset_bridge、工资/ra上界、劳动效率、就业时长或非就业者效用制度；不运行正式或TEMP的HA、HJB/KFE、外层、IRF、GE。无HA单元/代数oracle准许。

## 2. 历史证据和唯一只读来源
已独立审查的最近STOP review固定Git历史commit e9eb6a0d131bc8046af61d95892b2aa45e5740d8，tree89915a69c4653ac0540826cf4d29eb33a554c03c，独立ZIP original blob87b3173fc12f4ec3bec34dbde785f27ad627e37f，size220081，SHA256 14746e539ce792189dc85d207ec148e97bad27f8101a4c598c475d49a05008fc，26/26成员真实CRC/length/SHA PASS；前轮正反单位向量258/258限域独立复算PASS，但31省工资就业完整面板NOT_PASS。GitHub review当前树临时三文件已清理，必须只读固定**历史commit/blob**或上轮已知本地ZIP原件，核原字节后在新scratch提取；不得恢复旧Review或重抓固定官方原件。
前轮数据主对象：wage_employment_2018_31_verified.csv、source_value_normalization_ledger.csv（219条含2018新数）、official_source_provenance_2018.csv、verified_coverage_2018.md、unit_validator_tests.json、source_reuse_and_new_fetch_ledger.json、new_official_sources.jsonl、official_discovery_receipts.jsonl及关键unit_validator.py。保留前轮全部异常和原source层级，不把CODEX部分流水线标称完整受理。独立审查结果：20来源原字节单位/声明范围局部匹配，11 extract-only，27 time/geo不明，2非primary，159 missing；工资私营12、非私营16、总就业14、城镇8是未最终验收观察；完整可用省级面板0。前次真正计费58/120但构建器只数50的批量漏计8已独立证实，旧预算关闭不准继承。
宏观31省人口、GDP及PIM本地工作簿如需要，只可只读已知准确路径 D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx、完整SHA AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67，只取同年2018必要字段；严禁读其它保护档、旧MATLAB2018混年缓存和私人原始工作簿外传。源人口单位MU=10万元、NU=100人，GDP亿元×1000、PIM K万元÷10、POP万人×100；企业工资万元与YUAN/employee/year必须跟有效劳动效率和时间单位桥后才能解释。s_H=64.8906755511 GDP人均只是先前未采纳候选，不能自动固定。

## 3. 首先复用数据和修复请求计数与单位门
唯一独立新scratch D:\ProjectTemp\ch5_temp31_wage_employment_mapping_20261022_01，父D:\ProjectTemp身份、新路径不存在、符号链接/reparse逃逸及受保护Git index/worktree先行验证；首次写前二次检查。新scratch可保存补充脚本和SOURCE_ONLY结果，原sourceZIP、正式V010、科学算法、旧journal全部只读。若固定原件不可合法取得，停止于STOP_SOURCE_EVIDENCE_UNAVAILABLE，不从摘要假造旧来源。
重构SOURCE_ONLY source request计数：每个search query/open/官方HTTP请求有规范唯一event记录和request_kind/batch_index/query_index、请求时点、尝试状态、source_id；批检索包含4条query必须计4而非0，47个web receipt=45个单条+2×4批量→53、再加5个原站→58。计数由规范events表导出，控制器实际值与builder的计数不得静默设常数相等；任何出入STOP并交首错。记录每次错误与E1，无自动重跑旧整条耗费任务。旧吉林2793233人/10000=279.3233万人正例和2793232人负例、年份/统计范围/表题/省份轴继续锁定，不能仅做substring source match；原价值的scope/time争议不被单位换算抹平。

## 4. 缺失处理三层严格隔离
数据层O（OBSERVED）：2018同省同指标，官方年鉴/统计局来源原表能定位值/单位/年份/发布vintage/统计总体/时点/来源地区，标OBS_SOURCE_VERIFIED；政府转载或连接器摘录须降低SOURCE_CLASS并标精确获取限制；不能把source可信但时间地理未证的值当O。
数据层I（INTERPOLATED）：Owner明确本轮许可、仅用于TEMP参数校准的条件估计，不得覆写O。只有同省同一统计指标的**2017及2019**两侧官方值且定义/覆盖范围/年份/vintage/地理/时间指标可证明一致时，2018正值工资/就业规模可冻结log-linear时间插值 exp((log v17+log v19)/2)，并以算术插值(v17+v19)/2作为灵敏度比较；零/负/口径中断禁止log。若2017/2019两侧有一侧缺失或不连续、不一致则I不可生成；未来年份用于回顾2018并非前瞻预测，不叫2018官方数据。分母为年末 vs 年均不可互插，私营 vs 非私营不可混插，resident vs employed /urban vs total不可混插。全国、地区或同年其他省均值不可打作I。
数据层S（SCENARIO_ONLY）：对于无时间双端且缺失的指标，可以用事先固定、明示模型假设的地区工资比例/同组比例作为**独立的敏感性情景**演算，必须单列S、带公式和理由、never accepted as official or final calibration, 不合并到O/I主表；若本任务无法从可靠官方数据确定比例，不计算，只记NEEDS_OWNER_E3。任何插值前统计原值与完整两端缺口、方法、2017/2019 SHA/URL、delta和estimated_range。须输出observed/imputed/scenario分层每省每列面板、完整缺失及源身份证据，never 31/31 observed from imputation；后续是否采用插值到模型基点由Owner单独E3。
主要搜2017/2019同口径年鉴以支援2018个别缺口，官方年鉴/地区统计部门2019版和国家数据优先，搜索无法取官方来源留MISSING_OFFICIAL_SOURCE。对超过2018±1年的回溯资料仅SOURCE_REFERENCE，不变成已验证插值端点。原部分值上海140270/140400、西藏/陕西错位、浙江88883轴、辽宁67324口径、新疆2018年年鉴后年回溯、甘肃转载、天津就业居住工作地未知等必须列风险表。

## 5. 整体经济映射比统计补齐更重要
强制建立变量合同：家庭财富/消费总量人口 H_i^resident (2018常住人口；是否包括儿童/非就业者是一项待定代表主体问题)；劳动供给基数 E_i^resident_origin 为来源居民就业者；生产需求就业口径 E_j^workplace_destination（如数据可证），城镇私营/非私营工资覆盖年度平均人数 E_{j,c}^{unit,avg}；有效劳动 L_j^firm 为(NU×效率劳动)目的地而非简单E_j；就业率p_i=E_i/H_i只在居民地与同年度人口都对齐时才具解释资格。不得由省级就业未知定义强制等号。
源一条按2018工资统计报告单位工资是税前平均每单位就业者年劳动报酬，非单位有效劳动工资，也不是税后家庭工资。应给符号桥：w_{j,c}^{stat,yuan/person/year} ↔ w_j^{firm, MU/(NU_eff*year)}×平均劳动小时h_{j,c}×有效劳动质量e_{j,c}×[相同货币单位精确换算]，单位效率因子未知则E3；企业工资税按工作地目的地且一次扣税；家户HJB面对收入工资与就业概率/劳动分布的连接要独立标出，不能把平均工资机械当效率工资。
需要提供至少两种结构可行方案：A优先/建议：保留家户人口与资产的resident总量，另引入就业参与率和效率劳动映射使firm供给基数为就业者，允许将非就业者/儿童收入转移处理留待Owner；B研究敏感性：家户仅代表就业者与其自有人均资产，必须重标居民财富/消费/转移、未就业家庭与福利，不可当做纯单位替换。明示V010 source labor equation Lt_mat[j,i]按来源Ct/N与工资/迁移原公式，任何把N_i直接替换就业E_i都会改变源经济方程，属于Owner E3，不自动实施。两种方案均仅代数、无HA。还要给迁移来源—目的地矩阵的总量可行性、(目的地工作人口与各来源总人口)是否可比较、双重N乘数/转移二次扣税/重算alpha/Zt/产出劳动时间维度负例。
以目前原始价格界wjt[0.8,1.3]、ra[0.02,0.09]为历史定义标签，不直接按统计工资去强迫clip内，不能调整HU、HA a/b/efficiency or unemployment制度。最终比较三个分账：居民人口、就业人口和单位工资覆盖人口如何改变原模型宏观生产K/L与家庭财政/福利统计口径；哪些属于纯物理单位纠正、哪些是实际经济方程变动需要Owner授权。
必须提供明确建议的首个可执行TEMP31模型接口草图、人口/有效劳动字段名、来源—目的地维度、工资货币/时间单位、可检验守恒恒等式、全部E3待定清单及分省可得性热区，不运行生产模型。至少两个非对称31省合成样例验证人口、就业、迁移、工资统计覆盖及家庭与企业资金桥符号守恒，针对小样本可独立计算的oracle给公式与数值，但不要运行HA或GE。真实数据不够时保留参数符号与NA，仍须完成非HA总体映射架构和交付。

## 6. 输出和证据门
必须写至少：`wage_employment_2018_observed_31.csv`、`wage_employment_2018_interpolated_31.csv`、`official_source_and_endpoint_ledger.csv`、`employment_population_scope_bridge.md`、`household_firm_labor_mapping_contract.md`、`mapping_31_synthetic_oracles.json`、`imputation_method_and_sensitivity.md`、`source_request_canonical_events.jsonl`、`source_request_reconciliation.json`、`unresolved_economic_E3.md`、`first_error_budget_and_stop.json`；后两层不确定的原始值未验不得放进Observed。所有真实省份标输入身份、来源年份、是否观察/估算/情景、URL、原字节SHA及查询时间或无法取原因，不得空缺代0。
允许限定的`PASS_SOURCE_ONLY_MAPPING_DESIGN_WITH_PENDING_DATA`（结构代数清楚，未凑齐数据），不批准`COMPLETE_31_PROVINCE_PANEL`或`HA_CALIBRATED`除非未来全体真正获得经采纳数据和Owner确认。新的URL/网页原始证据只保留合规有限公开内容，不能把不相关长文章/私人表/付费年鉴全部上传GitHub；来源有版权或隐私约束时以精确引用/sha/页码和合法短摘录为准。

## 7. 执行预算、公开交付与停止
新墙钟<=14400秒，阶段source/recovery<=1800，统计检索及端点核对<=6000，整体映射实现/测试<=3000，交付<=3000，final reserve<=600；来源新query/open/官方HTTP调用<=160，工程Python启动<=24，direct process启动<=100，E1<=3个独立修复批（只非科学脚本、事件计数、文本抽取/编码等，保留首错和真正重测试回执；真官方数据矛盾不能靠E1掩盖）；scratch新增<=256MiB，独立source读取范围按上面固定白名单，Review总三个文件<=6MiB，ZIP展开<=16MiB/<=40成员，Git Data写入<=8，成功publish<=1。旧source 58/120、E1 3/3及旧科研调用不能结转，也不用新次数重计旧request。
唯一scratch D:\ProjectTemp\ch5_temp31_employment_wage_mapping_20261022_01，D:\ProjectTemp可信父根先验，路径原不存在/no reparse/old protected Git/index/其他项目脏树，首次写前二次身份门；不得为了满足合同扩大扫描受保护数据根。Codex在新scratch执行SOURCE_ONLY，不能修改正式V010源码、原MATLAB、上轮工作区与Git治理分支；本次GitHub只在独立review白名单三文件交付。
REVIEW_BRANCH=review/ch5-temp31-wage-employment-mapping-20181022
FIXED_PARENT=4500347a525c39a8d7c5c2a483fac19bebaa18a3
TEMP_PATH=_review_tmp/ch5/temp31-wage-employment-mapping-20181022/
Codex必须自动普通nonforce提交且只提交result.md、manifest.json、evidence_sanitized.zip；新候选唯一父B，不要使用治理Release为Review父；manifest包含公开members bytes sha256 CRC、实际子任务结果、来源/导出标签、隐私及唯一工件身份。ZIP未变的历史来源引用历史commit，不重复打包历史大原文；新官方原文如有版权只记录合法来源节选/位置，不能以哈希代替本轮新结构测试的必要原件。完成后从固定Git commit远端原字节readback三Blob/所有ZIP成员CRC长度SHA与隐私检查；平台工具拒绝/账号安全限制立即STOP不更换认证绕过。Astra独立科学顾问终审后先归档正式治理并回读，再精准清理本轮三个review临时文件；以前B-only/AB/HTTP三PENDING及旧review不动。
最终外置DELIVERY_FINAL_RECEIPT原始JSON byte length/SHA256/Base64及控制器退出之后独立完成事件，四阶段预算实耗，完整source event ledger和STOP/first errors；结束后状态WAIT_ASTRA_AND_OWNER_POPULATION_WAGE_MAPPING_DECISION，无自动新参数/HA任务。
