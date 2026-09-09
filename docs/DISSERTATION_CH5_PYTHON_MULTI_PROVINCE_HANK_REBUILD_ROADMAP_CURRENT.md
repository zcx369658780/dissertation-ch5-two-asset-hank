# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-09。唯一活动代码库：zcx369658780/dissertation-ch5-two-asset-hank。

## 目标与阶段
目标仍是完成可审计MATLAB→Python两资产household/多省份重构，再以独立规格建立真正动态。Owner最终科学authority；Reviewer规划/验收；Builder默认gpt-5.6-sol / medium。忠实性、HJB停止、生成算子、source-free KFE稳态、GE与Results分开判断。

MP4当前已完成：原参数call725失败复现、rah=.07单户敏感性、KFE source/escape质量归因、以及一次单户b域扩展。MP4退出条件仍未满足，因为原source-free stationarity与Qh符号问题未解决。

## 当前最重要的截断结论
旧生产家户网格：I20、b[-2,5]；J20、a[0,10]；Nz2、z[.8,1.3]。
Owner批准的唯一扩箱诊断保持原db，精确保留旧20节点并扩至I39、bmax=12，只运行2018安徽call725、rah=.07单户，其余算法/参数保持。

扩箱结果：HJB17步收敛，但Qh仍11负非对角元；post-loop Q仍17个upper-b外向单元。原`Tg=0`仍FAIL，`||Tg||inf=.5206986084614471`。返回诊断密度约46.72%位于旧b=5以上，新b=12顶面仍约6.84%，density-weighted escape约.10097。

由此支持：旧bmax=5对该单户状态构成物质性截断；但bmax=12仍没有达到可接受截断，也没有建立网格收敛。生产网格继续冻结，不能因诊断改善直接替换。

KFE pin公式随状态数变化，扩箱使pin从295变576，所以新旧KFE density/aggregate存在伴随pin变化。它不妨碍观察新顶面压力和旧b=5以上尾部，但阻止把聚合变化称为固定pin纯bmax因果效应。

## 当前科学停止点
状态：`B_DOMAIN_EXPANSION_ACCEPTED__TRUNCATION_MATERIAL__B12_STILL_INSUFFICIENT__NEXT_GRID_OR_BOUNDARY_DECISION_PENDING`。active Builder task：无。

Reviewer不建议以数值pin补源作为经济机制，也不建议自动扫bmax直到PASS。下一步需Owner在以下方向中明确选择：
1. 再冻结一个单一、更大、仍为安徽call725单户的截断稳健性点，以观察top-face mass/escape/Tg是否继续系统下降；或
2. 停止扩箱，转入有限箱边界法则的科学定义和实现选择。

若选1，下一task必须预先固定b端点、节点构造、预算和停止标准，并保持“不直接跑多省份”。若选2，必须明确有限箱的经济/数值含义；不能默认为批准已有D1–D3、a_bar/FOC修改或经济source。

## 后续顺序
明确截断/边界合同 → household数值有效性 → 修正2018单年与必要的有限省份验证 → 修正年度覆盖 → MP5冲击law → MP6真正动态规格 → 动态household/多省集成 → 稳健性/Results。
旧runtime-cache 15/15年与Owner-A 13/14年证据继续分开；当前不恢复年度运行。MATLAB顺序比较静态不等于真正IRF。Results eligibility=FALSE。

## 不变量
生产资本At*N、不用At+Bt；household Lt与firm Lt_supply不混；不补本地资本、不归一化portfolio权重、不改外层update map为root solver；保护MATLAB源、原算法、a_bar及生产参数。所有历史parity/失败证据按原范围保留。
