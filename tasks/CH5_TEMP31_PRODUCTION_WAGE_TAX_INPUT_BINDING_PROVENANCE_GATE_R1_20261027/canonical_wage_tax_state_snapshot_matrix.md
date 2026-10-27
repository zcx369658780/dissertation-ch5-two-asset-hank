# Canonical与旧期state来源/消费矩阵

下列字段路径仅是读取源码中的producer/consumer表达式。实际TEMP31 canonical原件、生成调用和已部署consumer尚未绑定；不构造真实tuple digest，不生成数据或桥公式。

| 字段 | 已知producer/初始化与更新 | 维度/索引/时点 | 经济单位与税位 | 消费者/接口 | 未闭合来源 |
| --- | --- | --- | --- | --- | --- |
| w | ANNUAL:178提供composite_wage scalar；ENTRY:114复制到每个state；STATE_UPDATE:162后续来自household_composite_wage | 来源省每state一个；初始共同scalar vs 后续综合指数 | 初始gross/net UNKNOWN；后续含楔子是继承静态事实 | ENTRY:179、348–349；HA_ADAPTER:207–208；HA_CONSUMER:159–164 | 初始值、初始生成调用、live真实净身份、同快照tuple均未证 |
| wjt | ANNUAL:177提供scalar；ENTRY:114初始共用；ONE_TURN:231–238用新firm.wjt传综合工资 | 目的地企业价格；旧wjt用于劳动拆分，新wjt用于下一综合w | 模型生产劳动价格；元/人/年与价格基年/模型期UNKNOWN | ONE_TURN:204/233；企业形成的详细式继承上轮，未重新展开 | 真实31省价格序列来源和同轮时间定义未证；不能把历史scalar称实测 |
| tau | ANNUAL:181的wage_tax scalar → ENTRY:116每state；CORRECTED_ENTRY:295仍读state.tau | 家户标量或省有序vector；ONE_TURN:205调用仍tax_by_origin | 已有工作地tau_j是Owner设计合同；没有法定税基/实际数据身份认证 | ENTRY:348、HA_ADAPTER:207、CORRECTED_ENTRY:295；通用HA使用非零tau | R2局部tau=0与R3目的地索引仅继承先验孤立证据；生产采纳未证 |
| sigma/sigmau | ANNUAL:478的distance/max(distance)*max_sigmau；canonical_payload matrices；ENTRY:372传入控制器 | destination×origin双边矩阵 | 比例摩擦楔子；经济收受方及计价UNKNOWN | ONE_TURN:207/235传递；继承旧wage/migration摘录 | 真实原件/矩阵source ID、与其他字段同快照未证 |
| phi | ENTRY:339–340及CORRECTED_ENTRY:862–865由进入state.Yt/state.Lt构建 | destination×origin；不是税率、工资或工时 | Y/L量纲、人口/有效劳动切换、旧/新期一致性UNKNOWN | ONE_TURN:206/234；RUNTIME:42–55持有传入phi | 局部可见matrix传递，不等于初始化、HA和更新共享D1 batch tuple digest |
| N | ANNUAL:456人口表×pop_multiplier；ENTRY:109从v.pop[i]取 | 来源省population_by_origin，ONE_TURN:203按来源列供给 | 人口尺度不是就业、工时或已验证户数；禁止N=P/3 | ONE_TURN:203、214；原劳动分布到企业的桥继承未决 | 行政省ID、人口/vintage、就业与有效劳动完整桥未证 |
| Ct | 初始ENTRY:117读initial_ct scalar；solve_batch聚合后ENTRY:361–363形成batch.ct | 来源家户省聚合；进入一轮时来自哪一批需实际身份 | 模型消费量、单位与频率UNKNOWN | ONE_TURN:202 -> migration reconstruction | 真实canonical/HA batch当前未绑定；真实HA不可运行 |
| Lt / household_lt | 初始ENTRY:110用pop；household聚合HA_CONSUMER:694为sum(z*l*g*weight) | 来源分布劳动与企业目的地Lt_supply分开 | 个体劳动、z加权聚合、人口和物理工时不能互换 | ONE_TURN:223用household_lt作Lt_prev；227用目的地row sum送firm | 不同Lt字段初始化/更新定义及同轮桥未闭合 |
| Tt | ANNUAL:179 transfer_income scalar → ENTRY:115；CORRECTED_ENTRY:297 | 每state家户transfer字段，财政合计范围另需证据 | 家庭/省级总额口径、时间期及价格单位UNKNOWN | ENTRY:350 / POSTLOOP transfer_income -> HA预算 | 不是工资税或可凭变量名合并的税后工资；实际来源、聚合单位未证 |
| province IDs / ordered batch | ANNUAL:447检查PROVINCE_ORDER、262输出labels；RUNTIME:40检查state.name顺序 | labels/shape checks vs行政ID/明确31省adapter不同 | 字符串序列不是生产数组来源身份证明 | RUNTIME:52将entering传callback，53–55传进入一轮 | 真实31省ID字典、跨field ordered source hashes、D1共同旧期tuple witness、D2生产dispatcher均缺 |


ANNUAL.load_primary_annual_input接受sources、binding、scalars参数；它可以生成GDP/资本/人口及其他模型字段的canonical载荷。源码中的canonical_sha256只定义字节序列哈希接口，不能替代真实生产生成调用，也不能自动当作D1包含同轮w/wjt/tau/sigma/phi/N/Ct/Lt的共同batch tuple证据。旧2009 JSON及三份2018工资候选均不替代缺失的真实TEMP31输入来源。
