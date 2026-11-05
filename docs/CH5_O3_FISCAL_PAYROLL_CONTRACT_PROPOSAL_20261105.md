# O3财政工资税金额合同：Owner决策稿

DATE=2026-11-05
STATUS=OWNER_ADOPTED_PAYROLL_SUBCONTRACT__SEE_IMPLEMENTATION_RECORD

后续更新：Owner回答“采用该工资总额税基（建议）”，仅采纳目的地比例工资税金额与所用gross工资版本。独立子账及14项限定工程检查见[实施记录](CH5_O3_PAYROLL_TAX_IMPLEMENTATION_20261105.md)。下文推导与“当时尚未采纳”文字按原提案时点保留，其余单位/财政建议没有自动获准。
GOVERNANCE_PARENT=b21d611fe6f8e40a6f4b66ee5a7549bdf75a1095
MODEL_DOCUMENT_HEAD_AT_RECHECK=017a631ce3db0cd117115c0a5370b8cf042b0324
MODEL_CODE_CANDIDATE=23d8ac8fe622d604f89dece6585769a969d16d9a
NEW_SCIENTIFIC_RUN_GRANT=NONE

## 建议与待Owner决定的范围

建议将工资税明确为**目的地省对企业税前劳动报酬总额征收的比例税**。企业劳动沿已选A1，政府工资税收入候选为：

```text
Payroll[j,k] = firm_wjt_out[j,k] * L_A1_supply[j,k]
WageTax[j,k] = tau_enter[j,k] * Payroll[j,k]
L_A1_supply[j,k] = sum_i q[j,i,k] * p[i] * H[i]
```

k表示外层算法迭代，不是经济年份/期间。firm_wjt_out是当前企业块实际输出的gross工资，经过原有上下限处理；不是裁切前边际工资wt0，不是进入轮旧工资，也不是来源地家户的net综合工资w。税率取本轮目的地tau，同一个企业输出工资随后供净综合工资生成使用；新综合工资进入下一外层迭代的家户接口。

这是科学口径建议，**尚未获Owner采纳**。本轮“可以，请继续”用于完成具体决策稿，不解释为已经选择上述公式或批准数值运行。采纳该工资税合同也不同时采纳Tt/AtTax换算、R/P制度、数据单位、财政平衡目标或完整O3生产资格。

## 为什么建议工资总额税基

| 候选 | 在现有比例税率解释下的量纲 | 判断 |
| --- | --- | --- |
| tau * L | 税率无量纲，乘劳动仍为劳动量 | 不能直接与公司税、投资收益等金额流相加；若解释为每单位劳动的定额税，则必须另定义有金额/劳动单位的税参数，不能把当前比例tau默认为该参数 |
| tau * wjt * L | 税率 × 金额/劳动 × 劳动 = 金额流 | 在wjt与L使用同一生产劳动单位、同一模型期间和货币单位的前提下，与比例工资税含义一致，建议采用 |
| tau * household_net_w * L | 来源地综合net工资不是企业工作地gross工资 | 不作为企业工资总额税基 |

本轮只作条件性量纲推导，不声称已证明真实工时/效率、年度统计工资或模型货币单位桥。即便某个试点wjt数值恰为1，也不能据此宣布tau*L与tau*wjt*L一般等价。不给税基选择虚设接受阈值。

## 与当前源码的精确关系

源码锚定上述模型HEAD。只读外层接口和现有财政计算，不进入HA内部研究。

| 文件及行号 | 可核事实 | 本建议的处理 |
| --- | --- | --- |
| src/ch5_two_asset_hank/multi_province/firm.py:102 | wt0是裁切前企业工资；126—133行输出裁切后wjt，并调整Corptax | 候选税基取输出wjt；保留原裁切与Corptax，不重复记补贴或补偿，不把Corptax改名成纯公司所得税 |
| src/ch5_two_asset_hank/multi_province/firm.py:135 | 现式Govinc=Corptax+L*tau+AtTax+GovInv*ra-Tt | 尚未改代码。后续若采纳，只在新外层财政账分列工资税候选；完整Govinc需先过其它金额项单位门 |
| src/ch5_two_asset_hank/multi_province/one_turn.py:204 | 旧劳动映射使用进入轮企业工资 | 记录entering工资与firm_out工资为不同迭代角色；不修改既定劳动核，不在未收敛迭代声称家户收入和企业工资账已相等 |
| src/ch5_two_asset_hank/multi_province/one_turn.py:231 | 新净综合工资使用当前firm.wjt | 工资税候选与这个gross工资来源一致；不在HA再扣同一税 |
| src/ch5_two_asset_hank/multi_province/one_turn.py:222 | household.at_tax直接赋给firm_source.AtTax | 传值可证，省级金额尺度未由此证明；不自动把其乘H或E |
| validators/multi_province/mp4b_python_empirical.py:115 | state.Tt来自transfer_income；348—354行将Tt作为家户外部输入，另构造at_tax | 家户输入角色可证，省级总额换算未证；不读原始私有数据、不重算密度或修改HA聚合 |
| src/ch5_two_asset_hank/multi_province/fiscal_diagnostics.py:22 | 全国诊断为sum(Govinc-Bt*rb*N) | 现式仅诊断，不是财政闭合；保留家庭H尺度，不改成E，不自行设余额为零 |
| src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py:199 | 已有tau*wjt*L条件诊断，SCIENTIFIC_PENDING | 不执行、不把函数存在视为采纳或证明 |

工资上限/下限处理及Corptax内补偿项已经属于既有企业算法。本决策稿只建议选择其输出工资作税基，不授权改限值、税补算法或价格更新规则。

## 省级财政总账的单位门

后续新外层账建议分列：

```text
Govinc_proposed = ExistingCorptax
                 + WageTax_proposed
                 + AssetRevenue_total
                 + GovInv * ra
                 - Transfer_total
GovSurplus_diagnostic = sum_j Govinc_proposed[j] - sum_i Bt[i] * rb[i] * H[i]
```

这只是金额项清单，**不是已接受的新财政公式或预算平衡条件**。AssetRevenue_total与Transfer_total必须附原输出量的分母、人口尺度、模型期间与货币单位。若已证为每单位H金额，省级金额应乘H一次；若已是省级总额则不再乘。当前缺少完整桥接证据，因此既不自动乘H，也不假设旧直接相加已经正确；企业劳动E不替代家庭财政尺度H。

A1的L已包含pH，工资税账不得再乘H、p、E或z。Sigma仍不自动作政府税；居民地工资归属/共享与本次工作地征税决定分开。企业gross工资总额也不自动等于家户net综合指数乘HA劳动，完整收入/激励兼容仍保留E3。

## 采纳后的最小实施边界

若Owner选择上述比例工资税合同，可在独立外层模块分列旧工资税项与拟议工资税项，携带目的地、省序、迭代、gross工资来源和已聚合劳动尺度；保留旧firm.py/one_turn.py作为历史源链，不在HA内补扣税。不以替换工资税一项宣称Govinc、E3或完整外层闭合通过。

工程检查只验证新账的字段/拒绝规则和已授权的纯接口行为；任何实际工资、劳动、企业、HA或外层科学算术执行均按具体运行许可，原TEMP31/Moll额度不重开。Tt/AtTax单位未证时，完整省级财政账保持不可用，不通过默认值、自动缩放或“沿旧式”标为就绪。

## 证据与本轮验证

历史G04及A1来源见[既有决定恢复](CH5_O3_LABOR_WAGE_TAX_DECISIONS_RECOVERED_20261105.md)中的固定提交/Blob，不重做旧13报告/116摘录审计。图谱只作函数发现；工资/时序/字段结论以当前源码定点核对为准，未执行任何所列函数。

本轮新增产出为决策稿及当前入口更新，源代码未改；TESTS=NOT_RUN_DOCUMENT_ONLY，MODEL_IMPORTS=0，SCIENTIFIC_CALLS=0，NEW_RUN_GRANTS=0，SUBAGENTS=0。TEMP31 7/7、Moll 3/3关闭；其它旧有限范围与保护保持。严格reference/thresholds仍null；科学接受、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。

OWNER_DECISION=ADOPTED_WORKSITE_GROSS_PAYROLL_BASE_AND_CURRENT_FIRM_OUTPUT_WAGE
NEXT=Tt/AtTax省级单位及收入兼容缺口继续保留；完整O3未组合，不运行模型。
