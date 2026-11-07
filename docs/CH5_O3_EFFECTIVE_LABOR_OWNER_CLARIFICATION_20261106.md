# O3劳动口径：Owner澄清有效劳动与效用劳动指数

DATE=2026-11-06
STATUS=OWNER_CLARIFIED_LABOR_SEMANTICS__DOCUMENTATION_ONLY
SOURCE_AUTHORITY=OWNER_CURRENT_DISCUSSION_AND_CONTINUATION
SUBAGENTS=0
SOURCE_FORMULA_PARAMETER_GRID_CONTROLS_CHANGES=0
MODEL_IMPORTS_SCIENTIFIC_CALLS_GRID_GENERATIONS_REAL_WORKERS_NEW_RUN_GRANTS=ALL0
TESTS=NOT_RUN__DOCUMENTATION_ONLY

## 后续Owner补充：劳动收入直接归对应家庭

最新消费输入决定：Owner核对MATLAB使用标量Ct后，要求Python保存原始C矩阵并用于同一Frisch算法；[新矩阵路径](CH5_O3_RAW_CONSUMPTION_MATRIX_ALLOCATION_20261106.md)已实现逐格C配原g/权重积分、无额外z、A1不变。以下较早的Ct聚合讨论按历史阶段理解，不再据其要求新分支使用标量Ct；实际收入对应与科学接受仍未完成。

Owner在同日后续讨论中明确：跨省工作的劳动收入直接归于对应家庭；在稳态分布g下，家庭工资收入z_t Lt w_t与其在各工作省取得的劳动收入加总等同。按本次问题的既定税后工资口径记录，不新增收入共享、统一收入池或再次分配步骤。

本记录将该关系记为Owner明确的模型收入等价关系：Y_lab_HA(g) = sum_j Y_lab_worksite_j(g)。两端必须指向同一来源居民家庭、同一稳态分布g、同一期次、同一税/迁移楔子和效率单位口径；沿原g的积分/权重约定，不改变HA、网格或归一化。Owner本次表述不自动加强为每个资产/能力网格点都已逐项核验的等式。

家庭收入归属/是否共享这一劳动收入子问题已回答，不再作为待Owner选择事项。直接归家庭的工资收入与原Tt/AtTax财政项分别保留；本次不推导其他未明确的R/P制度。

需要区分：上述收入等价是Owner明确的模型关系，当前外部省级Ct倒推及A1规模处理是否在实际源码和同一轮次中实现该关系，仍未完成核对。尤其不能把来源省平均消费的非线性变换自动当作异质家庭逐户变换的积分，也不能忽略H与E=pH的既定尺度区别。本次不宣称实现已经相等，不设置新阈值或经济接受条件。后续[收入对应账静态记录](CH5_O3_LABOR_INCOME_ACCOUNT_MAP_20261106.md)已列出同价/同原始量前提下的必要关系；下一步先讨论既有聚合推导或近似含义，不改已定分配或自行补系数。

## 本次明确的定义

Owner回顾并确认既有选择：保留当前Frisch劳动分配及相对劳动厌恶系数，不为强制线性加总相等而归一化或调整偏好。效用中的原Lt按等效劳动指数理解，具体外部劳动总量由各地劳动在同单位下直接相加得到。

Owner进一步明确：外部分配的双边劳动已包含能力z_t，按有效劳动解释；个体劳动收入中的z_t乘原个体劳动，与外部工资乘有效劳动是不同层级的表达。外部已经按有效劳动计量的数量不得再额外乘一次z_t。本次没有改变HA个体劳动政策、原z加权操作、原返回字段或其数值定义。

符号在本记录统一为“工作地j为行、居民来源地i为列”；Owner使用Lij时沿用其具体上下文，不因下标书写交换来源/目的地。

| 对象 | 本次明确的口径 | 用途与限定 |
| --- | --- | --- |
| 外部双边L[j,i] | 来源i向工作地j提供、已含能力的有效劳动；保留既定A1规模处理 | 企业生产及对应工资金额；不重复乘z |
| 来源有效劳动总量sum_j L[j,i] | 同一来源居民向各工作地提供的有效劳动之和 | 非就业人数、非原始工时；不强制等于效用Lt |
| 工作地企业劳动sum_i L[j,i] | 同一目的地从各来源获得的有效劳动之和 | 原企业劳动接口；不重复乘人口、p或z |
| 效用中的原Lt | 当前选定Frisch结构下的等效劳动指数 | 保留原效用和求解；一般不等于外部算术劳动总量 |

同一矩阵、同一期次、同一有效劳动单位下，来源端与工作地端的双重求和相等是加总恒等式。它不要求效用劳动指数等于算术总量，也不建立就业人头或工时守恒的认证。

## 原式核对与证据边界

定点核对原Lt_seperate.m及当前Python工作地税对应式：外部分配保留来源Ct的消费幂、目的地企业工资、劳动厌恶系数和税/迁移楔子，未另传显式z。当前对应入口为src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py中的_temp31_attractiveness与reconstruct_temp31_worksite_labor。

“公式没有显式z”只证明该分配步骤未另乘z；它本身不能证明能力已在数学聚合中完整吸收。有效劳动解释的科学依据是Owner本次明确的模型口径，不能把语义采纳写成新的数值验证或聚合等价性证明。

原MATLAB注释仍使用“平均个人时长”。该注释保留为原件历史措辞；当前项目解释以本记录为准，本轮不修改原MATLAB或Python科学源码。旧原式的来源地税写法也不作为新接线依据，继续执行已经采纳的目的地税与单次征税。

## 已定合同保持及仍待核对事项

- A1企业劳动尺度E_i=p_i H_i保持；当前适配在原H尺度来源列上乘p一次，不以有效劳动解释额外乘H/E/z。家庭资产、消费和财政保持H尺度。
- 目的地工资税、当轮gross工资与既定劳动账、财政Tt/AtTax各乘同源H一次保持；不把迁移楔子新增为政府税收。
- 各工资/劳动账仍须按原合同绑定同一轮次、来源和尺度；有效劳动解释不替代保存输入/同record身份及消费许可。
- 仍需核对省级Ct倒推劳动与HA异质家庭劳动收入聚合的兼容性。不能仅凭等效工资名称、缺少显式z或当前定义，宣称家庭预算/激励已经一致；本轮不新增经济方程、收入池、残差接受目标或HA内部诊断。
- 真实p来源、就业/工时/能力到有效劳动的数据桥、模型期和货币单位仍未完整采纳；本次只收束“外部L是工时还是有效劳动”的模型语义问题，不整体关闭原G06/G09等缺口。
- 家庭劳动收入直接归属及g下收入等价已由后续Owner补充明确；不再将该子问题标为未决。Owner又采纳Lt_prev取上一轮同一工作省、同一规模的企业有效劳动，输入准备12项检查通过，见[专门记录](CH5_O3_PREVIOUS_FIRM_LABOR_INPUT_BINDING_20261106.md)；实际企业调度尚未接入。外层校准/均衡更新和经济停止口径仍未决，不将本次回答外推为其他未明确R/P制度的采纳。

## 本轮交付与下一讨论

本轮仅保存Owner语义澄清并更新当前入口，两处现有工作树的同名治理文档保持一致。旧交接、历史PENDING/ISSUED、失败证据和保护基线保留，不反向改写为新授权。

下一劳动事项可围绕已明确的家庭直接收入归属和g下收入等价，定点整理现有外部Ct重构、A1尺度及工资轮次如何对应；不重问已明确的收入归属，不把模型关系视作实现已验证，不改HA、不运行模型。实际网格身份/外部保护与有限准入准备仍是已知工程方向，本次记录不自动启动它。

ACTUAL_GRID_SHA256=null
STRICT_REFERENCE_THRESHOLDS=null
SCIENTIFIC_ACCEPTANCE_FORMAL_SOURCE_FREEZE_CONSUMER_READY_FORMAL_HA_ACCEPTED_RESULTS_MODEL_ACTIVATION_REAL_GE=ALL_FALSE
GRID_GENERATION_SCIENTIFIC_RUN_CONSUMER_PERMISSION=NOT_AUTHORIZED
NEW_RUN_BUDGET=0

旧全部关闭额度、STOP与16项义务保持。GitHub仅限脱敏治理文档；模型代码、测试、机器决定及原载荷继续仅本地。文档同步是否完成以本次实际Git回读为准。

关联：[当前状态](CH5_LOCAL_FIRST_STATUS_CURRENT.md)；[主路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)；[既有A1接口记录](CH5_O3_A1_SCALE_INTERFACE_IMPLEMENTATION_20261105.md)。
