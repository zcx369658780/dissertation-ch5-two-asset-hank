# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-08。唯一代码库：zcx369658780/dissertation-ch5-two-asset-hank。

## 目标与来源
完成可审计的两资产household与多省份重构，继而在独立科学规格下建立真正动态响应。旧one-asset R5只读历史，不保留其科学runtime为活动依赖；deep-learning-hank是另一个项目。
MATLAB-faithful reference冻结，忠实性、数值有效性、收敛和论文资格分别判断。Owner最新要求先保留原算法/a_bar，查各省价格边界与原自适应机制。此前独立修复target只是已审阅提案，未采纳、未实施、暂缓。

## 阶段与依赖
| 阶段 | 状态/目标 | 真正退出条件 |
| --- | --- | --- |
| household特定基准 | 历史HJB/算子/KFE/聚合限定证据 | 仅对已验证fixture和版本成立 |
| MP0–MP3 | 来源/方向/适配及ordered one-turn已有接受记录 | At/Bt、Lt/Lt_supply、次序与来源不变量 |
| MP4 | corrected-2018 call-725未解决；活动任务为省份价格/自适应保存证据审计 | 明确版本下完整收敛、算子诊断、来源与比较证据 |
| MP5 | 冲击law与响应定义 | 来源、变量、频率、创新及归一化 |
| MP6 | 真正动态两资产规格 | 时间依赖HJB/KFE、初末条件、价格/财政/空间时序 |
| MP7–MP8 | 动态household与多省份集成 | 冻结规格下相关小规模验证 |
| MP9 | 受控响应与稳健性 | 已接受基线、路径、截断及误差证据 |
| MP10 | 正式Results | 具体输出/解释/来源/稳健性最终审阅 |

阶段是科学依赖，不是工程小步骤审批门禁。一个任务可包含实现、相关检查、有界执行和报告，但未知科学选择不默认为授权。

## 当前任务与Owner路线调整
活动：tasks/CH5_MP4C_PROVINCE_PRICE_BOUNDARY_AND_ADAPTATION_AUDIT.md。
目标是检查原始ra0/wt0是否越界、截断ra/wjt是否触界、实际家户rah/w处在什么水平，以及Zt/GovInv为何没有把价格纠正回来或是否其实已经调整。先查corrected-2018失败路径，再分口径比较已保存的成功年度终点。
原版入口边界为ra=[.02,.09]、wjt=[.8,1.3]；原控制器只有全国maxKNratiogap<.1且steady_state时才调整，并在ra>ramax-.02时增加国资10%。需查决定全局开关的省份、价格生成时点、rah旧ra滞后及实际调整记录。
Reviewer源码复核见docs/CH5_MP4C_PRICE_BOUNDARY_SOURCE_REVIEW_20260908.md。省份数值尚待Builder读取保存证据，不能提前断言安徽的Zt或资本数据就是根因。
本任务新模型/线性或根求解/年度调用预算0。没有轨迹时标注缺口，不追加运行，也不把.07经验水平改为新安全阈值。不得调整a_bar、clip、FOC、求解器、生产参数和容差。

## 保留诊断，不让路线调整掩盖问题
首轮53/53通过，raw-vb40/40是保存阶段差异。独立多轮MATLAB143步收敛、Python500步未收敛。固定线性2ff3eb2确认同系统solver路径差异及输入微差敏感性共存，ROW_POW2不普遍改善，P32极端对角丢失sigma；不以反复换solver/调容差追求1e-13通过。
边界规格15f51be9733b5043e738d3e522b97554e95902b9已接受为证据与书面提案：14/14快照预算/捕获漂移一致但存在上界向外漂移，终点负非对角元和泄漏风险未解除。D1人工上界状态约束、D2总漂移算子、D3成本/FOC一致target均未被Owner采纳，不能实施。旧任务完成，不重跑；原接受记录及FAIL证据继续保留。
价格因素与这些数值异常是否存在因果联系需另外证明。降低收益率不能自动证明算子有效；反过来已有边界问题也不能替代对上游价格和自适应机制的调查。

## 不变量与后续
生产资本使用At*N而非At+Bt；household Lt与firm Lt_supply分开；保留省份排序、矩阵方向、共同旧状态及源表达式。source-faithful update map不悄改为root solver。新的公式重建不是独立runtime捕获。原始MATLAB和历史证据只读，预算不重置。
旧runtime-cache Python15/15年、465省年历史接受，非全年度跨语言parity；Owner-A修正口径13/14年PASS，2018阻塞完整覆盖，分组审计不拼接结果。
近期顺序：价格/触界/调整记录审计→Reviewer/Owner讨论可区分原因的最小后续→按新task执行必要受控实验或已明确修复→恢复2018与年度覆盖。此前“必须先采纳D1-D3才推进”的未来安排被此次Owner指令取代。
长期仍需独立冻结真正动态规格、集成与稳健性；MATLAB命名IRF的顺序比较静态不等于真正动态系统。Results eligibility=FALSE。无依据时不承诺收敛或给出论文完成百分比。
