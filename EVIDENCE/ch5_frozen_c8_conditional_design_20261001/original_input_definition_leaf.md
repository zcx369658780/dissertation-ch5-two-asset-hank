# Record18 original input definition leaf

**静态定义事实；SOURCE_OUTPUT_SCOPE_NONCOMPLIANT，待 Work 独立审查。** 仅读已 pin 的 optionb_turn2_household_integration.py；未实例化任何输入。

| integration.params 字段 | 定义行 | 来源表达式类别 |
|---|---|---|
| ga、phi_l、alphal、epsilon | 869 | CONSTANT_LITERAL_NOT_EXTRACTED |
| theta、delta | 870 | CONSTANT_LITERAL_NOT_EXTRACTED |

868 行以 MappingProxyType 包装字典；istar/rho_pi（870）、totalpit/epsilon_pi（871）同为常量类别。六个目标字段不是 state／payload selector，不复制或使用其值。873 行静态转发 OneTurnInputs(PROVINCE_ORDER, states, params, phi, wedges, batch)。states/batch 直接来自函数参数；integration.params 是本地另建字典。household EconomicParams 保持独立，未核其定义或数值等价；范围外 1489 行不作为新依据。

_one_turn_inputs（857–873）中的本地 phi 是使用 productivity 两个广播视图的数组表达式；本地 wedges 是对载入 distance 的算术变换表达式。这里只登记表达式类别，不复述公式／标量，不调用 constructor 或组装矩阵。构造器按上述位置转发 phi/wedges；导入类型的字段定义未跟读。destination_origin 仅保留为既有字段方向标签，完整 shape/axes/dtype/units 绑定不因此建立。

DISTANCE_RELATIVE（93–95）声明为 docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv；866 行定义 load_accepted_distance_score 调用，目标未读取或 hashcheck。原 migration wedge 与 share distance 仍是不同用途的对象：wedge 表达式使用载入 score，不等于 raw score；既有 share consumer 对 distance 的使用保留。未推断数值关系或对象等价。前瞻年度 coefficient replacement 仅属既有设计；本轮未替换 phi，原 migration wedge 与 share distance 均未改变。

仍缺原 C8 实际 source-stage／sealed 输入绑定、显式 units/calendar、完整矩阵与 archive/canonical/import metadata、保护闭合。需要 Work 精确 locator／hash／字段 authority；不追引用、不建立实际重载、不提出运行或科学后继。

读取偏差：helper1 额外展示 1489 的 constructor 名称；helper2 额外触及 96–97、950–951、955、991，并有一次 raw 筛选输出意外包含被禁止的模型标量表达式。均保留并排除相关内容为新增合同依据；不宣称范围合规 PASS。已停止新源码读取，没有纠正补读、公式计算或禁止值向本文传播。

所有新运行预算／调用 0；源码／测试／Git／既有证据未改。固定 C8 baseline 保留，C9 暂停，Objective A 保留／窗口未接受／16 类未解；旧 consumed budgets 与 CALL_LEDGER_UNRESOLVED 不变，model/Results=False。停在 Work review。

