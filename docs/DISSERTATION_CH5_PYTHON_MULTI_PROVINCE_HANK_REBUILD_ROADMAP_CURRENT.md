# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-07。唯一活动代码库：zcx369658780/dissertation-ch5-two-asset-hank。

## 目标与来源
完成可审计的两资产household与多省份重构，继而在独立科学规格下建立真正动态响应。旧one-asset R5只读历史，不保留其科学runtime作为活动依赖。
MATLAB-faithful reference继续冻结；忠实性、数值有效性、收敛及论文资格分别判断。有依据的修复须有独立版本及科学authority，不能悄然替换reference。独立修复target目前仅为已审阅提案，待Owner采纳。

## 阶段与依赖
| 阶段 | 状态/目标 | 真正退出条件 |
| --- | --- | --- |
| household特定基准 | 历史HJB/算子/KFE/聚合限定证据 | 仅对已验证fixture及版本成立 |
| MP0–MP3 | 来源/方向/适配及ordered one-turn已有接受记录 | At/Bt、Lt/Lt_supply、省份次序及来源不变量 |
| MP4 | call-725边界/算子修复规格已接受，待Owner采纳target | 明确版本下完整收敛、适用算子诊断、来源与比较证据 |
| MP5 | 冲击law与响应定义 | 来源、变量、频率、创新及归一化明确 |
| MP6 | 真正动态两资产规格 | 时间依赖HJB/KFE、初末条件、价格/财政/空间时序明确 |
| MP7–MP8 | 动态household与多省份集成 | 冻结规格下小规模相关数值验证 |
| MP9 | 受控响应与稳健性 | 已接受基线、冲击、路径、截断和误差证据 |
| MP10 | 正式Results | 具体输出/解释/来源/稳健性最终审阅 |

这些是科学依赖，不是逐工程步骤审批门禁。实现、相关测试、有界执行及报告可在一个任务内完成。独立规格推导可先行，但未决科学选择不能默认为实施授权。

## 最新诊断和路线裁决
首轮53/53通过；raw-vb 40/40为保存阶段差异。多轮MATLAB143收敛、Python500未收敛；四状态M24/P24/M143_FINAL38/38，P32首差V1及统计量。
冻结线性2ff3eb2已接受归因：精确共同M/RHS下四组跨语言解仍FAIL；原语言重放精确；输入敏感性和固定输入solver路径差异共存，向量分解复现旧差异。ROW_POW2未普遍改善后向误差，P32极端对角已丢失sigma。不再以换solver/调容差/重复轨迹追求1e-13 PASS。
最新15f51be9733b5043e738d3e522b97554e95902b9完成并获接受：14/14保存快照预算/捕获漂移一致，但各有上界向外漂移。闭合非负守恒算子在坐标上界不能产生正漂移，因此仅修矩阵不能同时保留所有原控制和预算。异常包含channel、边界遗漏和表示误差，不能一概称为边界缺陷。
联合角点KKT、漂移一致生成算子及API/验证方案作为提案接受；没有新模型/求解。该任务完成，不重跑。

## 当前科学决策；无active Builder successor
状态：BOUNDARY_SPEC_ACCEPTED__OWNER_TARGET_ADOPTION_PENDING。
Owner待一次性确认的推荐方案B：D1独立诊断target的人工上界采用明确数值状态约束，后续截断敏感性必需；D2按同一consumed总预算漂移上风离散，承认有限网格人工扩散变化；D3保留现有max(a,a_bar)成本及参数，从同一成本推target FOC，不引入V_b floor或transfer cap。
经济下界、reference保护、固定输入和同对象128-eps规则已确定；不重复申请。D3是对新target的成本/FOC一致性采纳，不篡改reference或历史fixture。
本轮没有后继执行任务。Owner采纳后先发一份整合有界实现/相关检查/选定单元验证task；Builder报告建议的先零调用工程实现再十点验证，不必拆成两个审批门禁。具体选择算法、导数绑定、有限root预算和新正确性检查须在观察新结果前写入task，不能直接沿用提案数字为运行授权。
验收与决策表见docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_ACCEPTANCE.md。

## 不变量与未解除风险
- 生产资本At*N，不是At+Bt；household Lt与firm Lt_supply区分，省份排序/矩阵方向及共同旧状态保留。
- source-faithful外层update map不悄改root solver；保护MATLAB/输入身份与已消费预算。
- branch派生视图与局部公式重建不是独立runtime捕获；14快照不是全状态/网格稳健性证明。
- frozen-reference parity与修复target正确性为两条不同验证线。旧FAIL行保留；不要求修复target匹配已知无效边界，也不将其包装为原source parity通过。
- KKT条件不等于已选定的全局离散policy；未来还需可行性、互补、方向和Hamiltonian选择检查。reference-derived内点控制不自动拥有target最优性。
- 边界修复不保证解决P32内点极大transfer/cost、sigma丢失、Python500步不收敛。算子/收敛/KFE均仍未由此接受。
- MATLAB命名IRF的顺序比较静态不等于真正动态系统。

## 年度能力与后续顺序
旧runtime-cache口径Python2009–2023的15/15年、465省年曾正式接受，不代表全年度跨语言parity。修正Owner-A口径2009–2022共14年中13年返回PASS、2018失败，完整覆盖未接受；不同初始化不混用。
后续：Owner采纳target科学定义→exact task内整合实现与有界验证→算子有效性/非线性收敛→恢复2018及修正年度覆盖→冻结冲击和真正动态规格→动态household/多省份集成→稳健性/Results。各项不能预先保证。
真实科学选择在此暂停；普通工程修复不另起门禁，未变化的证据复用。进度用能力与阻塞项表述，不给论文编造精确百分比。Results eligibility=FALSE。
