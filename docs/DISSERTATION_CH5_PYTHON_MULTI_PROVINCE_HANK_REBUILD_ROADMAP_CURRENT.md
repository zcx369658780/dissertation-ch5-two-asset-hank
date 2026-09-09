# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-09。唯一代码库zcx369658780/dissertation-ch5-two-asset-hank。

## 目标与角色
完成可审计MATLAB→Python两资产household与多省份重构，再以独立规格建立真正动态。Owner最终科学authority；Reviewer规划/验收；Builder默认gpt-5.6-sol / medium。忠实性、停止条件、source-free稳态有效性、一般均衡和论文Results分开判断。

## 阶段
| 阶段 | 当前能力/目标 | 退出条件 |
| --- | --- | --- |
| household特定基准 | 历史限定HJB/算子/KFE/聚合 | 仅指定fixture/版本有效 |
| MP0–MP3 | 来源/方向/适配/ordered one-turn历史接受 | At/Bt、劳动、次序与来源不变量 |
| MP4 | 收益率敏感性和有限箱source/escape已定位；当前做单户b域截断诊断 | 明确配置下HJB、生成算子、原Tg=0与截断证据 |
| MP5 | 冲击law/响应定义 | 来源、频率、创新、归一化 |
| MP6 | 真正动态两资产规格 | 时变HJB/KFE、初末条件、价格/财政/空间时序 |
| MP7–MP8 | 动态household/多省集成 | 冻结规格的小规模验证 |
| MP9 | 受控响应/稳健性 | 已接受基线、路径、截断与误差 |
| MP10 | 正式Results | 输出/解释/来源/稳健性终审 |

## 已区分的三个问题
1. 安徽call725原参数rah=.09时原生HJB100不收敛/KFE非有限；单户改rah=.07并重新原生初始化后HJB26收敛且KFE返回。这是局部收益率+初始化链敏感性，不是生产ramax裁决。
2. .07返回density在旧b[-2,5]有限箱中不满足原Tg=0。density-weighted upper-b escape=.6697587443279651，被污染法替换的唯一物质性方程隐含补入同量source；只支持有限箱代数解释，不批准经济source。
3. last-HJB operator Qh仍有21负非对角元；post-loop Q的边界质量问题与Qh数值有效性问题不能互相替代。

## 当前Owner批准：只做单户b域扩展
Owner提醒原网格是反复测试留下的，改变b范围可能改变稳态变量；因此只做小规模安徽单户，不直接进入多个省份。

活动task：tasks/CH5_MP4C_CALL725_RAH_0P07_B_DOMAIN_EXPANSION_SINGLE_HOUSEHOLD.md。
生产基线保持I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。新诊断为嵌套扩箱：保留旧20个b节点字节完全一致，以相同db追加19点，I39、bmax约12；a/z/switch及rah=.07、其他参数、a_bar、原生初始化、helper/组装、solver、Delta、crit、HJB100全部不变。生产配置不修改。

只新增一次expanded-grid native initialization/HJB及自然到达的一次KFE/aggregate；旧bmax5 .07结果只读复用，其他省份/firm/GE/annual/MATLAB全部0。主要看：HJB收敛和Qh符号、new upper-b outward drift/Q*1、source-free Tg残差、b>5 tail质量与bmax top-face质量、以及KFE pin/source账本。

源污染row公式依赖state_count。新1560状态自动移动pin（预期k576），所以KFE密度/aggregate不是固定pin的纯bmax因果比较；若Q仍非守恒，分布和聚合须明确标注pin-dependent diagnostic。一次bmax扩展不能建立网格收敛，也不能授权生产bmax=12。

## 后续路线
若扩箱显著降低top-boundary质量/escape且原Tg残差随之收敛到机器规则附近，支持旧bmax=5截断是重要因素，但仍需决定是否做第二个预先定义的网格稳健性点或边界法则；不能直接跑31省。
若扩箱后仍有物质性upper-b压力/source-free残差，则简单扩大b范围不足，需要Owner再决定有限箱边界处理；不继续搜索bmax直到PASS。
无论哪种结果，D1–D3、经济source、a_bar/FOC修改均不自动批准。

随后顺序仍是：household数值有效性与截断合同→修正2018单年/必要有限省份验证→年度覆盖→真正动态规格/集成→稳健性/Results。MATLAB顺序比较静态不等于真正IRF。Results eligibility=FALSE。
