# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-08。唯一代码库：zcx369658780/dissertation-ch5-two-asset-hank。

## 目标与边界
完成可审计的MATLAB→Python两资产household及多省份重构，再在独立规格下构建真正动态。旧one-asset R5只读历史，deep-learning-hank为其他项目。忠实性、数值有效性、收敛和论文资格分别判断。
Owner保留原算法、a_bar及生产设置；D1–D3修复target仅已审提案，未采纳、未实施、暂缓。此次Owner仅批准独立单户rah=.07诊断输入，不是生产参数改动。其他诊断发现不自动授权替换reference。

## 阶段依赖
| 阶段 | 当前能力/目标 | 退出条件 |
| --- | --- | --- |
| household特定基准 | 历史限定HJB/算子/KFE/聚合证据 | 仅对已验证fixture与版本 |
| MP0–MP3 | 来源/方向/适配及ordered one-turn历史接受 | At/Bt、劳动对象、次序/来源不变量 |
| MP4 | 原参数2018前缀复现已接受；已批准单户rah=.07原生初始化敏感性 | 明确版本下完整收敛、算子、来源与比较证据 |
| MP5 | 冲击law与响应定义 | 来源、变量、频率、创新/归一化 |
| MP6 | 真正动态两资产规格 | 时变HJB/KFE、初末条件及经济时序 |
| MP7–MP8 | 动态household/多省份集成 | 冻结规格小规模验证 |
| MP9 | 受控响应与稳健性 | 基线、路径、截断和误差证据 |
| MP10 | 正式Results | 输出/解释/来源/稳健性最终审阅 |

阶段是科学依赖，不是逐工程步骤审批。一个完整任务可同时包含实现、相关检查、有界运行和报告；未知科学选择仍不能默认为授权。

## 最新结果与诊断更新
9d76747f48858a3e9289de8f284fffbc49aaedce已接受为OBSERVABLE_PREFIX_CAPTURE_COMPLETE / MATCHED_PREFIX_AND_FAILURE_REPRODUCED，验收见docs/CH5_MP4C_2018_ORIGINAL_PARAMETER_OBSERVABLE_PREFIX_REPLAY_ACCEPTANCE.md。
725入口11标量全匹配且误差0；24全国完整共同入口、713firm返回、23controller记录。安徽call725原HJB100步false后KFE non-finite复现；缺有效KFE返回不影响此前观测完成，不等于模型通过。
安徽turn22/23 raw ra0分别约.219795/.219069，turn23 wt0约2.57727，实际clip为.09/1.3。原资本租金.244069减折旧.025解释该时点ra0，PIt截零，非正利润分红放大。turn23贵州决定全国gap约.041249，适应门开，安徽Zt下降/GovInv增加10%。反馈确已执行，raw虽从早期约.53423下降，仍在clip上方，因而存储ra持续.09。
全国第23轮仍24省ra触上界，工资19上界/5下界；必须同时关注多省份校准路径与单户数值失败，不能提前认定某一项是唯一原因。原价格传递滞后、对象/单位、私人资本与国资按实际源定义保留。
前置价格审计8ef4a2a6仍保留PARTIAL_EVIDENCE；旧文件缺口没有被倒填，本次是独立观测。旧年度403/465终点分组及工资触界结论不重复计算。旧捕获时哈希/完整环境不确定性不凭标量匹配消除。

## 当前已批准的最小受控实验
状态：OWNER_APPROVED_CALL725_RAH_0P07_NATIVE_INIT_SENSITIVITY_ACTIVE。
活动任务：tasks/CH5_MP4C_CALL725_RAH_0P07_NATIVE_INIT_SENSITIVITY.md。
Owner明确批准独立单户rah .09→float('0.07')，其他输入/网格/a_bar/算法/solver/HJB100步规则不变。采用该诊断价格下的原生初始化，复用保存.09失败基线，新增.09调用0。这检验包含初始化响应在内的源求解链敏感性，非固定V0/l0的纯算子效应。
任务整合实现、相关合成检查、一次初始化/最多800劳动根、一次HJB/最多100次更新求解，以及自然到达时一次原KFE与聚合。科学开始后不重启，不扩充利率点，不改生产ramax，不启动MATLAB/firm/GE/年度；具体预算、工程启动重试及时间以task为准。发布未自动启动本地Builder，尚未收到报告。
旧prefix和年度表审计完成，不重跑。此前等待Owner的未来安排被本次明确批准取代；历史报告无需改写。D1–D3不是必须先采纳才能继续的路线。
HJB原停止条件、KFE返回/异常、分布和生成算子诊断分别报告；KFE返回不等于HJB收敛，跨价格输出不适用同输入parity判定。即使改善也不自动升级为生产ramax变更、年度覆盖、唯一致因或.07普适安全定理；保留后续科学决策。

## 不变量与未解除风险
按源At*N而非At+Bt；household Lt、目的地Lt_supply及实际firm Lt_prev不互换；不悄加本地资本、不归一化portfolio权重，不改外层update map为root solver。raw/clip/household价格与调整前后状态分开；初始化与求解期不能混用。
首轮53/53与raw-vb阶段解释保留；完全共同MAT初值下MATLAB143/Python500未收敛与原生初值实验分开。M143终点18负非对角元/15泄漏、14/14快照上界可行性、P32巨大transfer/cost和sigma丢失均开放。固定线性2ff3eb2与ROW_POW2结论不被价格诊断覆盖；不调容差或反复换solver追求PASS。
旧runtime-cache Python15/15年历史接受不等于全年度parity；Owner-A13/14年PASS、2018阻塞完整修正覆盖。后续科学顺序是本次受控原因检验/必要明确修复→数值有效性和2018→年度覆盖→真正动态规格与集成→稳健性/Results。
MATLAB顺序比较静态不等于真正IRF，不编造论文完成百分比。Results eligibility=FALSE。
