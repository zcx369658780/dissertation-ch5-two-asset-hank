# 初始化公式来源与经济含义核查 · 2026-11-01

SCOPE=FIXED_SOURCE_AND_CONTRACT_TEXT_PLUS_EXPLICIT_ECONOMIC_DERIVATION
MODEL_IMPORTS_RUNS=0
SCIENTIFIC_SOURCE_OR_FROZEN_CONTRACT_EDITS=0
INDEPENDENT_SCIENTIFIC_ACCEPTANCE=NOT_ESTABLISHED

## 结论与前述表述的限定

1. a*r_a(a)作为非流动性资产收益，有论文预算约束和原MATLAB真实状态方程的直接依据，并非V010凭空新增的经济机制。
2. V010把它加入R并设c0=w_eff*z*l0+R，是2026-10-15冻结时明确写入的V0数值初猜方案；资产收益的经济合法性不自动证明这份初猜对应双账户可行静止策略。
3. TEMP31的effective*effective直接继承历史Python初始化，原MATLAB对应Rah.*raah。两变量均为收益率；未找到将收益率平方作为收入的经济推导。高度符合变量误用，但最初作者意图、最早修改提交/开发日期UNKNOWN，不把可能笔误说成已证明的作者意图。
4. 前述“V010资产收益项优于旧平方项”应限定为变量角色/预算量纲及既有合同判断；不能据此机械替换并宣布完整初始化经济自洽。当前不改源、不改冻结合同、不跑模型。

## 一、V010公式的文档来源

正式冻结提交bf091da33d59293f147d52c11580327d3ac2a85d，versions/0.0.10/plan.md，Blob85138d8859d53295262fe13bf5bc277bca95ed3f第40行明定：

- r_a(a)=rah*(1-0.1*(a/a_max)^9)。
- R=r_b(b)*b+r_a(a)*a+Tt。
- c0=w_eff*z*l0+R，V0=flow_utility(c0,l0)/rho。
- 用同一c0资源定义求静态劳动FOC的正根；V0只是初猜、不构成新效用律，并禁止以旧Rah.*raah代替a*r_a(a)。

固定提交diff证实该段在本次正式冻结中作为明确V0规则加入。此前prefreeze_scientific_review_20261015.md要求冻结前明确synthetic全输入与V0身份，但该文件没有给出上述完整V0现金流推导。因此可证明它是冻结的数值合同，不能声称已找到更早、独立的双账户可行性证明或论文对这份具体初猜的直接推导。

## 二、平方项的可核来源链

| 位置 | 实际写法与证据 |
|---|---|
| Owner提供的原MATLAB HANK_2ASSETS_HJB.m | 第81行raah按rah及资产网格计算有效收益率；第85行Rah(i,j,nz)=raah(j)；第90行tempMat=Rah.*raah+Rb.*bbb+Tt。两个因子都是同一网格点的收益率，依其数组轴扩展等于r_a(a)^2 |
| 同一原MATLAB的劳动根 | tempMat经params(7)传入lab_solve2.m，其劳动残差把w_net*z*l+tempMat作为消费资源；该平方项被当作非劳动资源，不是方差/风险项的独立公式 |
| 九月首次复现Python | 90ee5b29f3be070d9f8f28c9614e1b59fe798462中validators/multi_province/corrected_2018_single_turn/run.py第158行已有effective*effective；因此不是TEMP31工资税修正时新创造的项 |
| TEMP31直接Python母本 | validators/multi_province/mp4b_python_empirical.py，Blobb1710ae3c5d8d7baf96e85c932d777fa5f3b908c，第171–184行_source_initial_arrays保留该式 |
| TEMP31迁移证据 | 10ee7973713c547faa581388aa97fbfd898809de的Bootstrap19 source_transformation_manifest.json明确initialization_original_blob=b1710ae...，声明非税初始化body保留effective*effective和l**6/6；bootstrap19_source_and_semantics.md亦明说只换工资系数，不静默修这些项 |
| 当前选定源码 | 56447829ce0e6c3c85552c53c351b26a2452a4bd的temp31_ha_taxfree_bootstrap.py，Blobb82eadea383a4d7546a11d4f19686440f8d71870，第211行继续保留平方项 |

原MATLAB HJB当前原字节12227 bytes，SHA-256=049136b769560040bc678f828f5d3ec5338ddcaa2090d6bed4e40732f56c3eae，与既有原件身份一致。本轮只读文本/哈希，没有运行MATLAB。文件目录中的年份不是经本轮认证的源代码最初创作日期。

## 三、变量定义决定的经济含义

原MATLAB中ah(j)/aaah是非流动性资产存量a；rah是基准收益率；raah与Rah是按资产网格调整后的收益率r_a(a)。原HJB第264行真实资产漂移使用mh=dh+Rah.*aaah，与论文c5.tex第39–42行的dot(a)=r_a*a+d相符；当前Python temp31_netwage_economics.py第140行同样为mu_a=r_a_effective*a+transfer。

因而a*r_a(a)表示该资产带来的财富增长流量（本模型期口径，不能未经单位合同称为年收入）。按现有变量角色，r_a(a)^2既缺资产数量，又会把负收益率变成非负数；在当前Python a=0、rah>0时也给出正数。源式没有将该项换算为收入的系数或经济推导。即使模型数值无量纲化，也不能凭数字可加抹去其变量角色与预算来源缺口。

Rah与raah名称接近，而资产网格变量为aaah，因此Rah.*aaah是一个有源预算支持的候选写法；“原作者本来想写哪个变量”仍只是推断，不作为已证明的历史事实。

## 四、为何不能把资产收益直接当成可消费现金

论文给出两个账户，代码另含转移支付T。令u=w_eff*z，则其结构为：

    dot(b) = r_b*b + u*l + T - d - chi(d,a) - c
    dot(a) = r_a(a)*a + d

相加得到总财富预算：

    dot(a+b) = r_b*b + r_a(a)*a + u*l + T - chi(d,a) - c

这里r_a(a)*a首先进入非流动性账户。它是经济收益，不代表同额资金已无成本进入流动性账户。

- 若初猜取d=0且dot(b)=0，则c=u*l+r_b*b+T，同时dot(a)=r_a(a)*a；这是允许非流动资产积累的初猜。
- 若要求两账户都不积累，且提款可行，则d=-r_a(a)*a，进而c=u*l+r_b*b+T+r_a(a)*a-chi(-r_a(a)*a,a)。忽略调整成本或提款可行性不能称为完整静止政策。
- V010的c0=u*l+R在形式上接近忽略调整成本的总财富资源规则；可作为数值初猜启发式，但不等于两账户均静止。合同没有明示选择上述哪种资产流动假设，本审计不替合同作者补造其意图。

V010劳动根对应标准CRRA劳动FOC：在alphac=1时，alphal*l^phi=(w_eff*z)*c^(-gamma)。代入哪份c资源定义，会得到哪份劳动初猜；FOC形式正确与资源假设正确是两件事。V0=flow_utility/rho也是初值近似，不是包含资产漂移和生产率状态转换的完整HJB解。

## 五、另一处可见的不一致与结论边界

MATLAB第90行把平方项送进劳动根，第111行c0却不含该平方项；当前TEMP31第211行与第214行存在同样差异。因此“求劳动时使用的消费资源”和“算初始效用时的消费”并非同一静态假设。本轮未计算其数值影响。

这些写法发生在初值生成。任意有限数值初猜不必就是已最优的经济政策；因此不能从此直接宣布全部历史HJB/KFE结果无效，亦不能保证只影响速度。在同一模型具有合适唯一性与严格收敛等条件时，最终解才应摆脱初猜影响；本项目尚不能据旧converged标志或一轮返回就认为这些条件均已证明。

## 六、建议与剩余决定

正式两资产状态方程中的a*r_a(a)有明确经济依据；不建议把收益率平方作为生产经济收入。历史平方初始化保持原件用于复现，不作新的经济采纳。下一接线方案必须独立说明V0的资源/资产流动假设、调整成本、可行域及与最终HJB的关系；若需改变现有冻结V010初猜合同，仍由Owner决定并保留原冻结文件。源锚点选择不自动完成该决定。

本审计属于有界来源与经济解释核查，不是数值实验、独立科学评议、Owner科学接受或正式Results。图谱对精确初始化符号未返回匹配，故按固定路径/Blob/原件短段落核查，未扩展索引或扫描其他项目。
