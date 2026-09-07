# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-08。唯一代码库：zcx369658780/dissertation-ch5-two-asset-hank。

## 目标与来源
完成可审计的两资产household与多省份重构，再在独立科学规格下建立真正动态响应。旧one-asset R5只读历史，deep-learning-hank为另一个项目。
MATLAB-faithful reference冻结；忠实性、数值有效性、收敛和论文资格分开判断。Owner要求保留原算法/a_bar，先查价格及原自适应机制。独立修复target仅已审提案，未采纳、未实施、暂缓。

## 阶段依赖
| 阶段 | 状态/目标 | 退出条件 |
| --- | --- | --- |
| household特定基准 | 历史限定HJB/算子/KFE/聚合证据 | 仅对已验证fixture/版本成立 |
| MP0–MP3 | 来源/方向/适配及ordered one-turn历史接受 | At/Bt、Lt/Lt_supply、次序与来源不变量 |
| MP4 | 价格保存审计已接受为PARTIAL_EVIDENCE；原参数观测前缀task活动 | 明确版本的收敛、算子/来源/比较证据 |
| MP5 | 冲击law与响应定义 | 来源、变量、频率、创新、归一化 |
| MP6 | 真正动态两资产规格 | 时变HJB/KFE、初末条件、价格/财政/空间时序 |
| MP7–MP8 | 动态household与多省份集成 | 冻结规格下小规模验证 |
| MP9 | 受控响应及稳健性 | 已接受基线、路径、截断和误差 |
| MP10 | 正式Results | 输出/解释/来源/稳健性最终审阅 |

阶段是科学依赖，不是工程逐步审批。实现、相关检查、有界执行和报告可为一个任务，但不默许未知科学选择。

## 最新价格证据及路线决定
8ef4a2a6c6df2ece2cda665890201c27dd083265已接受为PARTIAL_EVIDENCE；报告/验收见docs/CH5_MP4C_PROVINCE_PRICE_BOUNDARY_AND_ADAPTATION_AUDIT_{REPORT,ACCEPTANCE}.md。725个失败路径入口、403修正与465旧cache年度端点分组；工资触界广泛、终点ra不触界，rah>.07均0。这不是中间迭代的安全率证明。
安徽2018零外省权重使lagged ra→rah可识别，入口7–24连续18次rah=.09。原自适应确实执行：早期低产出导致Zt重置，后反复增国资；turn22贵州决定全国误差关门；turn23发生调整但全国max/决定省未知；turn24在家户/KFE失败而未完成本轮厂商/控制器。完整raw价格和实际mt/current household Lt缺失。已排除“从未调整”，未确立高rah造成失败的因果。
不再重复零调用年度表审计或靠错误Lt/不同阶段Zt补造raw。新任务tasks/CH5_MP4C_2018_ORIGINAL_PARAMETER_OBSERVABLE_PREFIX_REPLAY.md，授权一次不改参数/算法的原输入观测前缀。每轮开始先保存完整31省状态，捕获真实firm raw/cap与控制器事件，首次异常/原早收敛/超时/call725完成即停；预算以task为准。原HJBmaxit100，不延伸完整年度，不降rah、不采纳target。发布尚未执行。
新运行必须与旧入口逐项比较；路径分叉后只能解释新路径，不能充作旧运行缺失内部值。原捕获时哈希gap永久保留。缺数据是真实缺口，而非要求不断进行纯文档门禁。

## 不掩盖已有数值风险
首轮53/53与raw-vb阶段解释保留；共同初始化MATLAB143收敛、Python500未收敛仍未解决。M143终点18负非对角元/15泄漏，14/14快照有上界可行性冲突；15f51be9是诊断/提案接受，不是修复。
固定线性2ff3eb2确认同输入solver路径与输入微差敏感性并存；ROW_POW2不普遍改善，P32sigma丢失。不重复换solver/放宽容差追求1e-13 PASS。
高价格与数值异常的因果仍需区分；降低价格不能自动证明算子有效，已知算子问题也不替代上游调查。.07单因素实验、调整校准/边界/FOC或换算法仍需另行科学决定与task，当前未授权。

## 不变量及后续
按源At*N而非At+Bt，household Lt与firm Lt_supply/实际Lt_prev分开；保留省份次序、方向、共同旧状态、原投资权重和预算。严禁悄加本地留存资本项、归一化权重或改控制器为root solver。派生公式不是runtime捕获，原始文件和历史证据只读，历史预算不重置。
旧runtime-cache Python15/15年、465省年历史接受非全年度parity；Owner-A13/14年PASS，2018阻塞完整修正覆盖；不同初始化和数据口径不拼接。
近期：原参数有界观测→判断实际raw价格/mt/资本/自适应问题及必要科学选择→预定义task内验证→恢复修正2018与年度覆盖。D1–D3不是必须先采纳才能推进的路线。
长期：独立冻结真正动态规格→集成→稳健性→Results。MATLAB顺序比较静态不等于真正IRF，不编造论文完成百分比，不预先承诺收敛。Results eligibility=FALSE。
