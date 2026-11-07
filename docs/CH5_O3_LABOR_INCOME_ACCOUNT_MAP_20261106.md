# O3劳动收入对应账：静态映射与待讨论的聚合关系

后续Owner已明确要求Python改用原始C矩阵及g进行逐格原Frisch分配，见[当前矩阵路径](CH5_O3_RAW_CONSUMPTION_MATRIX_ALLOCATION_20261106.md)。本篇标量Ct公式及原机器计划保留为当时分析，仅适用于旧分支，不作为新分支的条件；原收入归属决定保持，实际收入等价仍未验证。

DATE=2026-11-06
STATUS=STATIC_ACCOUNT_MAP_COMPLETE__AGGREGATION_SEMANTICS_DISCUSSION_REQUIRED
UNCHANGED_ENGINEERING_CODE_CANDIDATE=03dff75e898aa0c93768aff1e7a5f00da1a61198
SOURCE_CHANGES_TESTS_NUMERICAL_EVALUATIONS_PROJECT_IMPORTS_SCIENTIFIC_CALLS_GRID_WORKERS_NEW_GRANTS=ALL0
SUBAGENTS=0
SYNC=PENDING_SYNC__NO_REMOTE_RETRY

## 已定事项保持

外部双边劳动按已含能力的有效劳动解释；保留Frisch分配及原厌恶系数，不重复乘z或做列归一化。A1企业E=pH、家庭聚合H、目的地单次征税、财政Tt/AtTax各乘同源H一次保持。跨省劳动收入直接归对应家庭；Owner明确稳态g下家庭劳动收入与各工作省收入之和等价。Lt_prev已取上一轮同一工作省、同一规模的企业有效劳动，其输入准备12项检查按上轮记录，本轮不重跑。

## 三组对应账

工作地j为行、居民来源地i为列。以下只列既有字段和表达式，实际金额全部null，未消费保存输入或调用模型。

| 账目 | 静态表达式 | 来源与轮次 | 当前边界 |
| --- | --- | --- | --- |
| HA家庭劳动收入 | 每H为W_in_i乘L_HA_i；省级H尺度为H_i乘该值 | W取该次原请求消费的进入净工资；L_HA取原公开返回l_ss | 原返回已含z；实际HA返回尚未取得，不能填旧假量或额外乘z |
| 外部来源地净收入 | 对工作地求和v_entering[j,i]乘L_A1[j,i] | v_entering取进入轮企业工资及同轮目的地税/迁移楔子；L取A1矩阵的来源列 | 须证明原工资记录使用的原始量与此处一致，且解释C聚合和p缩放后的收入关系 |
| 省级工资税账 | tau_j乘本轮企业裁切后gross工资乘目的地A1劳动合计 | 既有已采纳财政合同，本轮企业输出价格 | 保持此合同；不拿下一轮工资或gross工资替代家庭进入净工资，也不新增迁移楔子税收 |

原公开汇总的C_i是按g及原权重汇总的消费，L_HA_i是按g及原权重汇总的z乘劳动。两者沿原返回语义使用，不拆开或修改HA。现有O2原样搬运这些值，不补人口或税。

## 由现有外部公式得到的必要关系

这里只展开外部劳动和综合工资代码，不推导或修改HA。令nu为现有phi_l，gamma为现有gamma_c/ga，alpha_l为现有外部工资代码的alphal，kappa[j,i]为原phi矩阵。alpha_l不代表新选HA劳动权重，也不允许为了等式改当前HA输入。

在同一组进入轮工资、税和楔子下，定义：

\[
v_{ji}=w^{enter}_j(1-\tau_j-\sigma_{ji}),\qquad
S_i=\sum_j\kappa_{ji}(v_{ji}/\kappa_{ji})^{1+1/\nu}.
\]

现有外部分配与A1给出：

\[
L^{A1}_{ji}=p_iH_i C_i^{-\gamma/\nu}(v_{ji}/\kappa_{ji})^{1/\nu},
\qquad
Y_i^{external}=p_iH_i C_i^{-\gamma/\nu}S_i.
\]

因此，若Owner的收入关系在同一H基准下成立，且W_in_i为正，必须有：

\[
L_i^{HA}=\frac{p_i C_i^{-\gamma/\nu}S_i}{W_i^{in}}.
\]

只有进一步确认W_in_i正是由上述同一组工资、kappa、税/楔子和偏好按原综合工资式生成时，才可代入：

\[
W_i^{in}=\alpha_l^{-\nu/(1+\nu)}S_i^{\nu/(1+\nu)}
\quad\Longrightarrow\quad
L_i^{HA}=p_i\alpha_l C_i^{-\gamma/\nu}(W_i^{in})^{1/\nu}.
\]

这是对既有外部式和Owner关系的条件性代数展开，不是新闭合方程、校准条件、残差接受规则或运行许可。未代入参数/保存数据，未观察任何数值失败，也不据此认定具体点必然不等。

## 已定位的缺口

1. 进入工资原始量的身份绑定：现有O2核context、省序、进入轮和source bundle；新工资阶段核本轮企业输出及phi/sigma供下一轮使用。当前路径没有完整证明进入HA的工资所用原始工资、phi、税/楔子和偏好恰与劳动重构使用者相同。生产快照与进入快照本可不同，不能为相等而重封hash。
2. 消费非线性聚合：当前外部先取C_i=原g加权消费汇总，再作C_i的负幂。它不能一般性替代逐户作非线性变换后按g积分。是否存在原理论中的一致聚合定义/条件，需先说明；不自动把当前量认定为等效消费，也不新增HA矩或改分配式。
3. H/E映射：A1在企业劳动上乘p，而家庭H及原HA返回保持。上述必要关系显示p必须在收入对应说明中有明确位置。保留已定A1，不默认p=1、不将家户量统一乘p，也不凭该式重校厌恶系数。
4. 价格版本：同一次外层更新中的进入工资和输出工资一般不同；原家庭收入、外部分配和财政工资税要分别记账。内部给定价格的g稳态，不等于外层价格已经达到固定点；本轮不设外层经济停止口径。
5. 真实数据与单位：真实p、就业/工时/能力、H分母、货币和模型期桥仍按原缺口保留，不读取真实私有数据或补默认值。

针对“旧phi更新是否已保证上述关系”这一具体问题，定点读取两处旧年度回调：phi由相对Yt/Lt生产率更新。该代码不是已有的收入对账或g聚合等价证明。只作历史上下文定位，未执行旧runner，也不将其参数或来源重新采纳。

## 本轮产物及下一讨论

模型树新增validators/multi_province/outer_labor_income_account_map_20261106/plan.json，固定8个相关源码的实际长度/SHA、4个账目视图、条件性符号关系及5项缺口。金额、实际grid hash和严格标准均null；没有可执行消费者、残差规则或新预算。治理树只保存脱敏报告和当前入口，源码、测试、旧合同/机器决定与已采纳输入包均未修改。

下一步先讨论：保留当前Frisch分配和A1的前提下，原理论如何保证上述收入关系，尤其“省级C先汇总后倒推”与“企业侧p缩放”如何对应g下家庭收入。是已有一致聚合推导，还是原模型采用省级代表家庭近似，需要Owner明确；不以工程代码自行选择。

可独立保留进入/输出工资及其原始量身份绑定的工程缺口，但不在经济含义未清时增加收入共享、重构C、补系数、归一化或推进受影响的科学调用。严格reference/thresholds仍null，消费/科学接受/正式冻结/Results/激活/REAL_GE全部FALSE；旧关闭额度、STOP和16项义务不变。

关联：[劳动与收入决定](CH5_O3_EFFECTIVE_LABOR_OWNER_CLARIFICATION_20261106.md)；[上一轮企业劳动输入准备](CH5_O3_PREVIOUS_FIRM_LABOR_INPUT_BINDING_20261106.md)；[当前状态](CH5_LOCAL_FIRST_STATUS_CURRENT.md)；[主路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)。
