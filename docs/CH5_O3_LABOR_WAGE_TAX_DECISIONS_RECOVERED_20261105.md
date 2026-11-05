# O3企业劳动、工资与税收：既有决定恢复及接线约束

DATE=2026-11-05
STATUS=EXISTING_DECISIONS_RECOVERED__O3_PLAN_CORRECTED__NO_SOURCE_CHANGE

后续Owner决定：工资税gross payroll金额子合同已采纳并完成独立子账工程，见[实施记录](CH5_O3_PAYROLL_TAX_IMPLEMENTATION_20261105.md)。本篇下文G04未采纳及代码未改为恢复历史时点的事实；Tt/AtTax省级单位、收入兼容等其余缺口保持。
MODEL_DOCUMENT_HEAD_AT_RECHECK=ffe7a3b11b951e972ab61bf2096025359d896007
MODEL_CODE_CANDIDATE=23d8ac8fe622d604f89dece6585769a969d16d9a
MODEL_CODE_TREE=2adeb8af7e5cff5f0ea9cbbc6ab0eba50e56f392
GOVERNANCE_PARENT=581429a3abcd2dc95eb6d8f622107b8bf1fde071
NEW_SCIENTIFIC_RUN_GRANT=NONE

## 恢复结论

Owner提醒：“可以请继续，企业劳动和工资税基之前已将进行过一轮整理了，你可以找找”。

已找回2026-10-23 A1决定与2026-10-27工资—劳动—税收静态语义审计。此前O3计划把“原量式还是归一化”重新并列为待选，遗漏了已有A1决定，本记录纠正该安排。只恢复有证据的科学决定，不恢复历史离线派单、GPT日常工程签收或旧预算。

| 事项 | 已有决定与边界 | O3处理 |
| --- | --- | --- |
| 企业劳动映射 | Owner已选A1，未选A2。保留消费驱动核，以就业规模E_i=p_i H_i替代企业劳动侧的H_i | 沿A1准备接线；不再询问A1/A2，不接归一化函数 |
| 家庭聚合尺度 | 家庭资产、消费、财政继续按H_i聚合 | 企业E与家庭H分别传递，不全局改N；不将At/Bt/Ct或财政人口尺度一起乘p |
| 工资税方向 | 按实际工作地/目的地归属，劳动拆分用tau_j | 目的地为行、来源地为列；不沿旧调用的tax_by_origin接线 |
| 净工资税位 | 已含目的地税/迁移楔子的综合净工资进入HA，同一工资税只扣一次 | 保留既有净工资接口及原HA；不改通用gross-wage消费者的税语义 |
| 迁移楔子sigma | 不得自动作政府税 | 不新增sigma税收入 |
| 财政金额税基 | G04保留量纲疑点，payroll税基及转移/人口单位尚未科学采纳 | 不将条件诊断tau*wjt*L替换正式Govinc |
| R+P居民归属/共享 | 仅曾获准作为优先研究方向，具体制度未正式采纳 | 不自动建立居民收入池、共享工资或修改劳动激励 |

## A1的精确含义

原消费驱动劳动核保持：

```text
q[j,i] = C[i]^(-gamma_c/phi_l)
         * (w[j]*(1-tau[j]-sigma[j,i])/phi[j,i])^(1/phi_l)
L_S0[j,i] = q[j,i] * H[i]
E[i] = p[i] * H[i]
L_A1[j,i] = q[j,i] * E[i] = p[i] * L_S0[j,i]
L_supply[j] = sum_i L_A1[j,i]
```

A1不是就业人头守恒迁移矩阵；不要求来源列和等于E，也不能用HA返回的有效劳动重新归一化这些列。A2列归一化会消去原Ct来源公共因子，Owner已未选。恢复A1决定不等于已证明其真实家庭预算、工时/效率、工资统计或31省均衡闭合。

## 对当前源码的接线对照

以下行号按上述模型HEAD定点核对，只读源码；代码未推送，不构造远端源码链接。

| 位置 | 当前事实 | 下一接线约束 |
| --- | --- | --- |
| src/ch5_two_asset_hank/multi_province/one_turn.py:203 | 旧劳动调用传population_by_origin=N，205行传tax_by_origin | 保留历史one_turn；新组合显式区分H、p、E并使用目的地税 |
| src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py:106 | 源量式工作地税函数按传入尺度乘来源列 | 可作为A1外层复用候选：仅企业劳动尺度传E，参数名population不得误导为全局人口重定义；正式接线尚未实施 |
| src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py:115 | 另有按家户劳动归一化函数 | A2未选，不接当前路线 |
| src/ch5_two_asset_hank/multi_province/one_turn.py:214 | 资本配置用家庭人口N | 保留H尺度，不随企业劳动改成E |
| src/ch5_two_asset_hank/multi_province/firm.py:135 | Govinc的工资税项为lt*tau | 在G04采纳前保持原式，且不得称为已接受的财政闭合 |
| src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py:199 | tau*wjt*Lt是条件诊断，SCIENTIFIC_PENDING | 不据函数存在自动取得财政采纳资格 |

接线计划为：O2完整预给定家户批次及同轮省序/快照 → 保留Ct与已有phi → A1企业劳动E和目的地tau → 既有资本配置H → 企业/净工资/下一轮状态。企业gross工资wjt、家户net综合工资w、HA的z加权有效劳动和目的地生产劳动各自保留语义，不用同名或相同shape替代单位证据。p的来源/定义和实际数据采用须有依据，不默认p=1、不从工资总额除均值构造就业。

这是外层组合方案，不授权改HA、改劳动核、改财政公式或启动数值验证。新组合不得把旧企业Govinc返回当成G04已解决，也不得凭A1合成代数通过自动建立居民收入/劳动激励兼容性。

## 真正保留的缺口

2026-10-27审计G04为SUSPECTED_DIMENSIONAL_INCONSISTENCY：c5.tex写Ls*tau，原MATLAB/当前firm.py写L*tau，而c3.tex及隔离R2写w*L*tau。该审计明确保留“Independent semantic adoption of the payroll base and transfer/population units; no fiscal repair performed”。工作地归属已定，不代表金额税基、工资vintage、转移/人口单位已定。

因此下一科学讨论应聚焦：若tau是工资从价税率，政府工资税项是否按同一工作地gross payroll计量，以及采用哪一轮工资与劳动单位；不得把这一推论写成Owner决定。先固定该金额账和单位，再实施受其影响的财政组合。

G06人口/就业/工时/效率桥、G09模型期与货币单位桥仍未闭合；统计工资均值不是模型wjt或家户w，旧s_H=64.8906755511未正式采用。R/P收入归属与共享也未正式采纳。它们与财政G04分别记录，不借本次历史恢复自动关闭，不重开已决定的A1/A2选择。

## 可追溯来源

1. [A1会话交接第3节](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/581429a3abcd2dc95eb6d8f622107b8bf1fde071/docs/CH5_SESSION_HANDOFF_20261023_A1_RP_OFFLINE_PENDING_INDEPENDENT_REVIEW.md)：Blob 8f533918633e274427dcfef0e3e6bea385436298；含A1、E=pH、家庭H、A2未选及R+P保留。
2. [语义审计Owner说明](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/9bdc9e83127d32e6e29a0a5895800fd97d92cd3a/tasks/CH5_TEMP31_WAGE_LABOR_TAX_SEMANTICS_STATIC_AUDIT_R1_20261027/owner_decision_brief.md)：Blob d9bbd440bf581b4ba503a3ee1378057db96995c4；既有目的地税/单次扣税决定不重开。
3. [语义审计缺口表](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/9bdc9e83127d32e6e29a0a5895800fd97d92cd3a/tasks/CH5_TEMP31_WAGE_LABOR_TAX_SEMANTICS_STATIC_AUDIT_R1_20261027/gap_register.json)：Blob bd3d50f47dcf808a7f1b3a3642cabe2490f75f7f；G04、G06、G09。
4. [语义矩阵](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/9bdc9e83127d32e6e29a0a5895800fd97d92cd3a/tasks/CH5_TEMP31_WAGE_LABOR_TAX_SEMANTICS_STATIC_AUDIT_R1_20261027/symbol_semantics_matrix.md)：Blob c01a5d90126c4df30a118e45b932e8f7a37344e7；区分工资、劳动及人口语义。
5. 项目记忆CH5_PROJECT_MEMORY_CURRENT.md的2026-10-23 A1段、工作地税段和2026-10-27静态语义审计段相互印证。本轮不重做13报告/116摘录盘点或51,159项历史合成检查。历史PASS_BOUNDED不升级为生产或科学接受。

## 本轮范围及后继边界

本轮仅恢复既有决定、定点核源码并修正文档。TESTS=NOT_RUN；MODEL_IMPORTS=0；SCIENTIFIC_CALLS=0；SOURCE_EDITS=0；NEW_RUN_GRANTS=0；SUBAGENTS=0。这不重复宣称O1/O2检查已在本轮执行。

下一目标：沿A1准备外层接线，先解决受G04影响的财政金额合同及必要单位，后续按具体授权实施组合；不重新研究HA，不重新选择A1/A2。真实生产资格、数据采用、完整E3与均衡口径各按原门保留。

TEMP31 7/7、Moll 3/3关闭，零重试；初始化旧余量仅原8格范围，工资/补录关闭。严格reference/thresholds仍null；科学接受、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。R12 STOP、R13未授权、WASM六路径STOP、保护重绑定未授权及16项义务保持。原件、历史dirty树、缓存及LOCAL_ONLY载荷保留；模型分支和代码仅本地。只同步脱敏治理文档至既定SSH治理分支，不合并main。

路线入口：[主路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)、[外层方案](CH5_OUTER_PRODUCTION_CHAIN_GAPS_AND_MINIMAL_CLOSURE_PLAN_20261105.md)、[任务清单](../tasks/todo.md)。
