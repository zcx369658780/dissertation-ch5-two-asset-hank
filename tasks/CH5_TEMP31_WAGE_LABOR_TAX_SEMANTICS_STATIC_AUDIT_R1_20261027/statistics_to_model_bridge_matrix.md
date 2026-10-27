# 三份统计原始候选与实际模型量的口径对应

仅做资格匹配，不写转换公式、不计算工资率、净工资、就业人数或私人/非私人合成权重。每个实际目标均给三行；同一模型名按其来源/调用税位区分。DIRECTLY_MATCHES_WITH_EVIDENCE本轮没有任何单元满足，不能因31个名字或工资标签相似而直接采纳。

共同缺口：正式NBS指标ID、原始导出链接与时间、修订vintage、确切统计总体/税前税后/名义实际及模型期、行政省ID和生产数组join。模型劳动目标另缺匹配就业、工时、有效劳动及z分布证据；需要哪一项取决于Owner最终选择的目标，而非本轮制造桥。

## Q1 企业wt0/wjt：由给定目的地L算边际产出并裁切；model currency/model productive labor；未扣tau

模型证据：C_F:99–109; C_F:126–135。

| 文件 | 观察口径与覆盖 | 兼容性 | 原因 |
| --- | --- | --- | --- |
| A | 城镇单位就业人员平均工资；标题元；2018=31省原始候选；NONPRIVATE_LIKELY__DEFINITION_PENDING | REQUIRES_OWNER_DECISION_OR_TRANSFORMATION | 统计年平均报酬不是已证明的模型边际/有效劳动工资；非私营倾向定义仍待核 |
| B | 城镇私营单位就业人员平均工资；标题元；2018=30省非异常候选，西藏30隔离 | REQUIRES_OWNER_DECISION_OR_TRANSFORMATION | 私营范围不同且西藏缺口；不能直接替换省级企业生产工资 |
| C | 城镇单位就业人员工资总额；标题亿元；2018=31省非异常原始候选 | INCOMPATIBLE_BY_DEFINITION | 亿元工资总额是总额，wjt是单位劳动价格；不能直接当价格 |

## Q2 来源家户综合w_i：目的地求和的非线性指数，含tau/sigma

模型证据：C_W:52–76; P2_W:52–76。

| 文件 | 观察口径与覆盖 | 兼容性 | 原因 |
| --- | --- | --- | --- |
| A | 城镇单位就业人员平均工资；标题元；2018=31省原始候选；NONPRIVATE_LIKELY__DEFINITION_PENDING | REQUIRES_OWNER_DECISION_OR_TRANSFORMATION | 31省工作地统计均值不是来源省综合指数，缺OD/phi/sigma/tax与单位桥 |
| B | 城镇私营单位就业人员平均工资；标题元；2018=30省非异常候选，西藏30隔离 | REQUIRES_OWNER_DECISION_OR_TRANSFORMATION | 30省私营统计均值不能直接等同来源家户净综合指数 |
| C | 城镇单位就业人员工资总额；标题亿元；2018=31省非异常原始候选 | INCOMPATIBLE_BY_DEFINITION | 工作地总额不能直接等同来源家户综合工资系数 |

## Q3 通用HA的HouseholdInputs.wages与tau位置：gross调用和R2 net调用合同不同

模型证据：C_EMP:345–350; P2_EMP:346–351; C_HA:159–164。

| 文件 | 观察口径与覆盖 | 兼容性 | 原因 |
| --- | --- | --- | --- |
| A | 城镇单位就业人员平均工资；标题元；2018=31省原始候选；NONPRIVATE_LIKELY__DEFINITION_PENDING | UNKNOWN | 原Excel税前税后字段、完整统计总体和模型期未证，不能选gross/net调用语义 |
| B | 城镇私营单位就业人员平均工资；标题元；2018=30省非异常候选，西藏30隔离 | UNKNOWN | 私营标签不证明净工资，税基/期/劳动单位仍缺 |
| C | 城镇单位就业人员工资总额；标题亿元；2018=31省非异常原始候选 | INCOMPATIBLE_BY_DEFINITION | 总额不能直接放入singleton工资率输入 |

## Q4 个体l/ell及物理工时：HA FOC内生选择，带z及劳动厌恶

模型证据：T3:355–365; C_HA:131–136。

| 文件 | 观察口径与覆盖 | 兼容性 | 原因 |
| --- | --- | --- | --- |
| A | 城镇单位就业人员平均工资；标题元；2018=31省原始候选；NONPRIVATE_LIKELY__DEFINITION_PENDING | INCOMPATIBLE_BY_DEFINITION | 工资报酬观察不是个体劳动/工时 |
| B | 城镇私营单位就业人员平均工资；标题元；2018=30省非异常候选，西藏30隔离 | INCOMPATIBLE_BY_DEFINITION | 工资报酬观察不是个体劳动/工时 |
| C | 城镇单位就业人员工资总额；标题亿元；2018=31省非异常原始候选 | INCOMPATIBLE_BY_DEFINITION | 工资总额不是个体劳动/工时 |

## Q5 来源家户Lt/l_ss=分布加权z*l：每来源省有效劳动

模型证据：C_HA:686–696。

| 文件 | 观察口径与覆盖 | 兼容性 | 原因 |
| --- | --- | --- | --- |
| A | 城镇单位就业人员平均工资；标题元；2018=31省原始候选；NONPRIVATE_LIKELY__DEFINITION_PENDING | INCOMPATIBLE_BY_DEFINITION | 年均工资不提供分布加权劳动或z权重 |
| B | 城镇私营单位就业人员平均工资；标题元；2018=30省非异常候选，西藏30隔离 | INCOMPATIBLE_BY_DEFINITION | 私营年均工资不提供全居民劳动分布 |
| C | 城镇单位就业人员工资总额；标题亿元；2018=31省非异常原始候选 | INCOMPATIBLE_BY_DEFINITION | 亿元报酬总额不等于∫z*l dg |

## Q6 目的地Lt_supply与双边Lt_mat：旧拆分或独立列归一化路径

模型证据：C_L:101–131; C_L:311–355。

| 文件 | 观察口径与覆盖 | 兼容性 | 原因 |
| --- | --- | --- | --- |
| A | 城镇单位就业人员平均工资；标题元；2018=31省原始候选；NONPRIVATE_LIKELY__DEFINITION_PENDING | INCOMPATIBLE_BY_DEFINITION | 工资均值不是双边劳动流或行和 |
| B | 城镇私营单位就业人员平均工资；标题元；2018=30省非异常候选，西藏30隔离 | INCOMPATIBLE_BY_DEFINITION | 私营工资均值不提供OD、工时或效率劳动量 |
| C | 城镇单位就业人员工资总额；标题亿元；2018=31省非异常原始候选 | INCOMPATIBLE_BY_DEFINITION | 工资总额不提供已匹配的劳动量分母；不得除均值造就业 |

## Q7 N_i来源人口/规模与n省轴长度

模型证据：M_EQ:29–30; C_EMP:108–116。

| 文件 | 观察口径与覆盖 | 兼容性 | 原因 |
| --- | --- | --- | --- |
| A | 城镇单位就业人员平均工资；标题元；2018=31省原始候选；NONPRIVATE_LIKELY__DEFINITION_PENDING | INCOMPATIBLE_BY_DEFINITION | 工资不是人口或行政ID |
| B | 城镇私营单位就业人员平均工资；标题元；2018=30省非异常候选，西藏30隔离 | INCOMPATIBLE_BY_DEFINITION | 工资不是人口或行政ID |
| C | 城镇单位就业人员工资总额；标题亿元；2018=31省非异常原始候选 | INCOMPATIBLE_BY_DEFINITION | 总额不是人口或员工数量；不能据其他表比例推导 |

## Q8 工资收入/财政工资税基：HA wage*z*l与R2企业lt*wjt，分别不同聚合

模型证据：C_HA:159–164; P2_F:135。

| 文件 | 观察口径与覆盖 | 兼容性 | 原因 |
| --- | --- | --- | --- |
| A | 城镇单位就业人员平均工资；标题元；2018=31省原始候选；NONPRIVATE_LIKELY__DEFINITION_PENDING | INCOMPATIBLE_BY_DEFINITION | 均值不是家户收入或目的地工资总额；缺匹配就业/有效劳动总体 |
| B | 城镇私营单位就业人员平均工资；标题元；2018=30省非异常候选，西藏30隔离 | INCOMPATIBLE_BY_DEFINITION | 私营均值不是省级总额，也不是全体家户净收入 |
| C | 城镇单位就业人员工资总额；标题亿元；2018=31省非异常原始候选 | REQUIRES_OWNER_DECISION_OR_TRANSFORMATION | 工资总额可作候选总额参考，但统计总体、单位亿元、模型期、税基/税前税后、跨省人员与有效劳动仍未匹配；不据此转换 |

## Q9 tau、sigma、phi、效率z与劳动/就业权重：参数及分布而非报酬指标

模型证据：T5:35–45; C_BASE:857–873; C_HA:131–136。

| 文件 | 观察口径与覆盖 | 兼容性 | 原因 |
| --- | --- | --- | --- |
| A | 城镇单位就业人员平均工资；标题元；2018=31省原始候选；NONPRIVATE_LIKELY__DEFINITION_PENDING | INCOMPATIBLE_BY_DEFINITION | 观察工资不直接等于税率/偏好/效率/权重 |
| B | 城镇私营单位就业人员平均工资；标题元；2018=30省非异常候选，西藏30隔离 | INCOMPATIBLE_BY_DEFINITION | 观察工资不直接等于税率/偏好/效率/权重 |
| C | 城镇单位就业人员工资总额；标题亿元；2018=31省非异常原始候选 | INCOMPATIBLE_BY_DEFINITION | 亿元工资总额不直接等于税率/偏好/效率/权重 |

## 原始候选身份和异常年份

| 文件 | 字节 | SHA-256 | 来源资格 |
| --- | --- | --- | --- |
| A | 12652 | 8bb799fc41da5728a52c4958b2da0641ccbc81470a8d6e377625d79b5816b176 | OWNER_DOWNLOADED_NBS_CLAIMED / MODEL_ADOPTED=FALSE |
| B | 12411 | 5c790a478a244ca12b4c3c2c682465683c64e2b36bbf1d6f5e430bd79b23f21a | OWNER_DOWNLOADED_NBS_CLAIMED / MODEL_ADOPTED=FALSE |
| C | 13310 | f27313c73dc08e8217aeeefe147ce62d7bc0d7c463ecc651c54c7682682c9dc7 | OWNER_DOWNLOADED_NBS_CLAIMED / MODEL_ADOPTED=FALSE |

A的2025及2001—2005全省30隔离；B的2025及2001—2008全省30、西藏2009—2019的30隔离；C的2025、2001—2003、2005全省30及2004年25省30隔离。30的语义不推断。C的1995—2008劳动报酬总额历史说明保留。原件及来源旁置回执哈希保护，无原工资值表上传。2006—2024等其他年份没有因本轮对照获得年度认证。

2009原始输入三个工资/税字段为各一个float，由load_entry_state重复放入31个state；不是2018年31个观测。该JSON的binding=2009与fixed_zt_calendar_year=2020是不同元数据，不构成共同vintage或新工资来源认证。

当前corrected目标Q3的直接表达式还见C_BASE:285–305 → C_CONT:704–732 → C_SEL:388–414；初始化见C_INIT:153–176。其标量税位仍不允许从NBS文件名决定应填gross还是net。C_CONT:43–44的N是网格状态数，不是Q7人口。
