# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-09。唯一代码库zcx369658780/dissertation-ch5-two-asset-hank。

## 目标、角色和来源
可审计MATLAB→Python两资产household/多省份重构，再依独立规格构建真正动态。旧R5只读历史；deep-learning-hank为另一项目。忠实性、停止条件、原稳态有效性及论文资格分别判断。
Owner保留原算法、a_bar和生产设置，.07只获准用于完成的独立诊断，D1–D3未采纳/未实施。Reviewer规划/审阅；Builder默认gpt-5.6-sol / medium，task可指定合理例外，不改global/provider、不把指定标签伪称实际验证、不重置预算。

## 科学阶段
| 阶段 | 当前能力/目标 | 退出条件 |
| --- | --- | --- |
| household特定基准 | 历史限定HJB/算子/KFE/聚合 | 仅指定fixture/版本有效 |
| MP0–MP3 | 来源/方向/适配/ordered one-turn历史接受 | At/Bt、劳动、次序/来源不变量 |
| MP4 | 局部收益率敏感性及有限箱source/escape归因已接受；原稳态仍失败 | 明确版本的收敛、算子、原方程和来源证据 |
| MP5 | 冲击law与响应定义 | 来源/变量/频率/创新/归一化 |
| MP6 | 真正动态两资产规格 | 时变HJB/KFE、初末条件/经济时序 |
| MP7–MP8 | 动态household/多省集成 | 冻结规格下小规模验证 |
| MP9 | 受控响应/稳健性 | 基线、路径、截断及误差证据 |
| MP10 | 正式Results | 输出/解释/来源/稳健性终审 |

阶段是科学依赖，不是工程逐小审批。实现、相关检查、有界运行及报告可在一个task完成。

## 两个已区分的问题
第一，e3176e93独立单户rah=.07原生初始化使HJB从.09的100步false变为26步收敛，并让KFE/聚合返回。只支持包含初始化响应的局部求解链敏感性，不是应改生产ramax或.07安全定理。
第二，51ba55709dcec2ef82163f6f9f1766ba6ff90f32的零求解账本证实：该返回g并非原Q.T*g=0。物质性残差-3.4540415243199343集中在被替换row295；density加权upper-b逃逸.6697587443279651由该行隐含源平衡，完整修正后误差约1.11e-16。这个SUPPORTED是有限箱代数，不是经济source机制的批准。
29外向格中20承担正流量；返回诊断密度upper-b质量约.6758362。原组装省略越界转移却保留diagonal离开率，污染法丢弃唯一物质性不平衡方程。污染法本身并非普遍错误；不能用小污染系统残差代替原稳态检查，也不能将诊断密度当成真实家户分布。
Qh21个负非对角元仍独立存在；不得拿post-loop Q的符号合格替代。C/L/A/B仍是诊断积分，不能进入已接受GE/Results。

## 当前结束于具体科学选择
状态KFE_MASS_BALANCE_ACCEPTED__BOUNDARY_OR_TRUNCATION_DECISION_PENDING。active Builder successor：无。
已完成质量账本task、.07单户、725前缀和年度表审计，不重跑、不继承预算。新账本只用13个既有科学文件，新增模型/求解/MATLAB0；详细证据与审阅局限见当前状态/验收。
Reviewer不建议把数值pin当作经济补源。为保留原算法与a_bar，建议下一步先选择一次独立upper-b域扩展诊断，候选b[-2,5]20点→[-2,12]39点、数学间距7/19；a/z、rah=.07、其他输入、原生初始化算法、helper/组装/pin公式和HJB100不改，生产配置保持。
此建议未批准、未发布task、无新预算。源pin公式随state_count变动，因此该候选会自动k295→576；后续须预先记录该伴随变化，不能冒称固定pin的纯截断效应。实验可探查原算法在更大盒子的行为，但不保证修复，也不能用一次扩展证明网格无关性。若仍有物质性漏率/负率或不收敛，须如实报告后再决定边界实现，不能暗中补源或继续扩箱搜索PASS。
任何修改边界/矩阵/FOC或经济source都需明确科学裁决；现有D1–D3不自动捆绑批准。不为等待决定再发重复诊断或纯文档任务。

## 历史与不变量
9d76747f原参数前缀725入口*11字段零差、24完整31省旧状态/713firm/23controller/原call725失败复现。安徽raw约.219但家户收到.09；Zt/GovInv反馈已执行，raw下降仍高于clip；价格传递滞后保留。旧price审计PARTIAL_EVIDENCE及捕获时哈希gap不倒填。
At*N而非At+Bt；household Lt与目的省Lt_supply/actual firm Lt_prev不互换，不补本地资本、不归一化portfolio权重、不改外层为root solver。raw/clip/家户输入及适应前后时点分别解释。
首轮53/53、raw-vb保存阶段、多轮与固定线性/ROW_POW2、边界规格15f51be9均保留原范围。共同MAT初始化MATLAB143/Python500与原生.09/.07分开，P32极大transfer/cost/sigma丢失与旧M143边界问题未被修复，不调容差或换solver求PASS。
旧runtime-cache15/15年465省年历史限定接受非全部parity；Owner-A13/14年403成功省年，2018仍阻塞完整修正覆盖。后续：明确截断/边界诊断选择→有界任务→原数值有效性→修正2018及年度→真正动态规格/集成/稳健性→Results。顺序比较静态不等于真正IRF，不编造完成百分比。Results eligibility=FALSE。
