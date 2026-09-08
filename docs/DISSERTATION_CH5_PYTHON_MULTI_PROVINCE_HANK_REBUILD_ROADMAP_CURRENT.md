# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-09。唯一代码库zcx369658780/dissertation-ch5-two-asset-hank。

## 目标、角色与来源
可审计MATLAB→Python两资产household/多省份重构，再在独立规格下构建真正动态。旧R5只读历史；deep-learning-hank是另一项目。忠实性、停止条件、数值有效性和论文资格分别判断。
Owner保留原算法、a_bar及生产设置，批准的.07仅为独立诊断副本。D1–D3只作已审提案，未采纳/未实施。Reviewer整体规划；Builder默认gpt-5.6-sol / medium，task可指定有理由的模型例外，不更改global/provider；模型切换不重置预算。

## 科学阶段
| 阶段 | 当前能力/目标 | 退出条件 |
| --- | --- | --- |
| household特定基准 | 历史限定HJB/算子/KFE/聚合证据 | 仅对指定fixture/版本有效 |
| MP0–MP3 | 来源/方向/适配/ordered one-turn已有接受 | At/Bt、劳动、次序/来源不变量 |
| MP4 | .07单户敏感性已接受；稳态分布残差阻塞 | 版本明确的收敛、算子、原稳态方程及来源证据 |
| MP5 | 冲击law与响应定义 | 来源、变量、频率、创新/归一化 |
| MP6 | 真正动态两资产规格 | 时变HJB/KFE、初末条件/经济时序 |
| MP7–MP8 | 动态household与多省集成 | 冻结规格的小规模验证 |
| MP9 | 受控响应/稳健性 | 已接受基线、路径与截断/误差 |
| MP10 | 正式Results | 具体输出/解释/来源/稳健性终审 |

阶段是科学依赖，不是每个工程动作的审批门。完整实现、相关检查、有界执行和报告可在一个task完成。

## 已有结论发生了什么变化
e3176e9352b4f7e155c91891a4cabdd517e9e232：只把保存安徽call725的rah改为float('0.07')并使用原生初始化，HJB从.09的100步false变为26步converged，statistic8.867440115523095e-11；原KFE/聚合返回。.09基线只读，无新.09调用。该局部受控结果支持收益率及其初始化链敏感性，不是普适安全阈值或生产改动依据。
有限归一密度仍不是原系统稳态：未修改转置残差3.4540415243199343、尺度比.14988946066377937；post-loop有29个upper-b外向格点，末次HJB算子21负非对角元。不能把小contaminated残差/质量1写成MODEL_PASS。C/L/A/B仅为诊断积分。
9d76747f原参数前缀已接受725入口*11字段零差、原call725异常复现；安徽raw收益率约.219而实际家户收到.09。原反馈已执行，turn23贵州使门开且安徽增加国资/下调Zt，raw虽下降仍在clip上方；全国当轮24省ra在上界。价格传递滞后和资本/劳动对象不变。
8ef4a2a6旧价格审计保留当时PARTIAL_EVIDENCE；旧403/465年度表不重算。新的内部观测不倒填历史数组身份或捕获时哈希。

## 当前活动完整任务
状态RAH_0P07_SENSITIVITY_ACCEPTED__ZERO_SOLVE_KFE_MASS_BALANCE_ACTIVE。
任务tasks/CH5_MP4C_CALL725_RAH_0P07_KFE_MASS_BALANCE_ATTRIBUTION.md。
新增初始化/root/HJB/KFE/任何solve或评价器/多省模型/MATLAB调用全部0。只使用已有.07有限density、raw、Q/T/污染矩阵和保存drift，核对对象身份、被丢弃方程的局部残差及密度加权质量流；检验是否存在pin行隐含源与upper-b流失的平衡。该解释尚非已接受结果，不提前断言。
这不是重新做边界规格或.07诊断，而是此前.09没有有限density时无法完成的概率质量账本。不要为了求得通过而移动pin、补对角、裁剪速率或密度，也不加扫描利率/扩展网格/年度执行。不运行矩阵特征值/新固定点或额外求解。
报告须给出具体残差所在格点和带权流量、符号与舍入量级说明，区分HJB迭代算子和post-loop算子，并指出最小后续科学决定。已有修复提案引用即可，不能当作自动授权。发布不启动本地计算。

## 不变量、仍开放问题与后续
At*N而非At+Bt；household Lt与目的省Lt_supply/actual firm Lt_prev不互换，不补本地资本项、不归一化投资权重、不改外层更新为root。raw/clip/家户价格与firm前后/适应时点分开。保持原公式、a_bar、source文件与历史失败。
首轮53/53和raw-vb阶段解释保留；完全共同MAT初值MATLAB143/Python500未收敛与当前原生初始化.09/.07分开。M14318负元/15泄漏、14/14上界可行性冲突、P32巨大transfer/cost及sigma丢失均未被价格变化解决。固定线性2ff3eb2和ROW_POW2结论不抹去，不调容差/反复换solver求PASS。
旧runtime-cache Python15/15年历史接受并非全年度parity；修正Owner-A13/14年PASS，2018完整覆盖仍阻塞。后续顺序：现有分布质量/残差归因→有证据的必要科学选择/明确任务→数值有效性及修正2018→年度覆盖→真正动态规格/集成→稳健性/Results。不再把重复观测和文档门禁当作默认下一步。
MATLAB顺序比较静态不等于真正IRF；不编造论文完成百分比，不在原稳态残差失败时将诊断聚合带入政策结论。Results eligibility=FALSE。
