# 第五章现行路线图：原MATLAB修错、有界迭代的Python重写与论文交付

> **2026-10-16 最新进度覆盖层（优先于下方“V010实施等待Codex交付”的历史时态）**：原MATLAB修错→Python重写是唯一主线，V010冻结科学计划仍有效；已形成冻结模型代码candidate，但真实Windows import/runner I/O、单点corrected HA/HJB/KFE、外层共同稳态与GDP≤1%验证没有完成。此前B8/S8/L4合成20/20及本轮新集成17/17是Codex本地报告，不等于科学通过；旧首版seal没有原字节且缺run_id，永久UNVERIFIABLE，新first/final有本地回执但待远端独立审查。**M1部分完成，M2未获V010稳态结果，M3仍需合格基点，M4尚无Results，V011 NOT_STARTED**。详细等级与后续门见[2026-10-16 V010路线图进度](CH5_V010_ROADMAP_PROGRESS_AND_NEXT_GATES_20261016.md)。Owner已明确授权下一张**仅脱敏证据交换**任务，冻结发行Commit`49ff1c3053fa1aa6a0646f55abcffb077e2b62b2`、任务Blob`1dc5f07a88261c41de434a9c4075b0d179ee871a`，严禁借此启动Python/runner/HA/真实数据或V011；动态ACTIVE以CURRENT/TASK_CURRENT为准。


更新：2026-10-15，依据[Owner主线纠偏](CH5_OWNER_SCOPE_REALIGNMENT_20261015.md)。
**当前阶段：V010原方法的Python集中实施合同已冻结（commit `bf091da33d59293f147d52c11580327d3ac2a85d`）；唯一实施任务已单独签发，仅放开隔离代码与受界synthetic，不放开真实31省及Results。**

## 唯一主线

修正原MATLAB具体错误，继承省级HA黑箱接口、有界多省顺序迭代、GovInv/Zt自适应校准和原递推冲击框架，在Python完成可复核的第五章模型及论文。不是另建人工HANK制度，再要求原论文等待新制度的稳态或动态闭合。

HANK_2ASSETS_HJB条件家庭稳态 → HANK_mp_1turn跨省劳动/资本/企业/工资/货币财政 → HANK_mp_1eq边界、阻尼、GovInv/Zt和全省共同收敛 → 原政策冲击递推。源模型的具体bug可以修正，总体方法不默认被替换。

## 里程碑与当前进展

| 阶段 | 实质目标 | 证据/下一动作 |
|---|---|---|
| 纠偏同步门 | 让执行端明确恢复主线、停旧Newton任务 | 已[限定接受](../versions/0.0.10/scope_sync_acceptance.md)，不再重复同步 |
| M1 原框架修错与接线 | 选定原MATLAB参考和合适Python baseline；复用已接受HA数值修复，修字段/轴/单位/税/资本实际错误；保留单轮与外层 | [V010 SOURCE_ONLY集中方案](../versions/0.0.10/mainline_alignment_task.md)已有限接受；[正式V010计划](../versions/0.0.10/plan.md)与[集中实施](../versions/0.0.10/implementation_task.md)已下达，等待Codex交付 |
| M2 有界多省稳态与校准 | 明确允许价格域与GovInv/Zt更新规则，核HA有效性、外层共同固定点、触边、数据校准 | 数值复现、修正版、经济解释分账；不以新增联合债券财政根当唯一合法算法 |
| M3 原论文省际冲击 | 从已接受基点重现原TFP/国有资本/税率AR(1)及跨省传导，修注入/时序/参数更新/图表错误 | 检查零冲击、小冲击与回归特征，明确原预期/分布递推假设；完整前瞻路径不是自动前置 |
| M4 第五章与投稿 | 修订公式、方法、稳态/联动/冲击图、稳健性和可重现材料 | 由真实证据支撑主张，不提前宣称Results |

每版优先一个完整可验收科学问题。不承诺固定若干版本内投稿，不为普通目录/文档再切微版本，不重复全库理论审查。

## 必须集中处理的兼容性

原GovInv收益边界调节与后来C1=max(Ktarget-Kprivate,0)不是同一个更新映射；原价格有界与raw/used/lagged回报、Lt前后状态/人口单位、税及AtTax/Tt也有具体需核之处。恢复主线不一键回滚旧接受，不将新人工科学制度强加回原代码。该SOURCE_ONLY任务已完成，Owner已决定采用原GovInv 0.9/1.1、目的地工资税一次，实施合同已固定。

合法校准期调整Zt/GovInv不是事后篡改验收标准。要核清校准阶段、稳定基点验证和冲击阶段允许更新哪些字段，避免调节动作吸收冲击；此时只查真实代码，不擅自改规则。

IMPLEMENTATION_CODE_PARENT=`a1db8c114dec0ab69d69a5576e153a7f868cba0e`，只是已冻结工程起点，尚未科学接受GE。原始参考、已修复目标和人工实验分开；旧C8 Option1是限定诊断，不是全项目永久定义。V008/V009人工Newton/固定Bg/内生T/竞争模型及前瞻动态研究均为AUXILIARY_RESEARCH_NOT_MAINLINE，保留但不作为M1—M4前置。

## 权限与历史

同V010的SOURCE_ONLY方案已有限接受，Owner科学裁决完成；2026-10-15正式冻结与独立实施许可已签发，受限于synthetic及白名单，不能外推真实GE。原MATLAB/Python历史数值与错误分开，不能为了对齐bug数值拒绝修正版。

旧2026-10-14路线全文保留在db2c2e289419ecab7921667e210bd510ff3c447b，纠偏同步阶段在916e2b47d3489f6eacd814b55cc568d92be4c9fb同路径。本次不改任何已冻结版本/历史接受，也不要求覆盖原16文档镜像。

真实C8/C9与旧预算、A16/window/CALL_LEDGER/Results、原worktree与B3保护不变；不借路线恢复重开真实数据或调用。V1.2工作流保持。
