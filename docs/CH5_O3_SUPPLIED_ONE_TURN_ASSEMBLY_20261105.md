# O3独立外层一轮：预给定阶段结果拼装

DATE=2026-11-05
STATUS=SUPPLIED_ONE_TURN_ASSEMBLY_ENGINEERING_COMPLETE__REAL_DISPATCH_NOT_IMPLEMENTED
GOVERNANCE_PARENT=f818d1f1226166cddd1456a3d40614bbd72ba105
MODEL_PARENT=ee31949e674ce14014a5d3ff71efb8a7bb9c5c27
MODEL_CODE_CANDIDATE=9a2eff9f14d5053f91c862d566c7ff437a4eb0ba
MODEL_CODE_CANDIDATE_TREE=7ed486cf790a49f5a8e82b0ae1203fd9eaa07ad3
MODEL_BRANCH_AND_CODE=LOCAL_ONLY_NOT_PUSHED
NEW_SCIENTIFIC_RUN_GRANT=NONE

## 完成的范围

新增独立接口assemble_precomputed_outer_one_turn，把现有O2批次字段、A1规模/预给定劳动结果、预给定资本/企业/工资/货币结果及已采纳财政账连接为只读候选下一轮状态。不创建第二套家户批次工厂，不调用原劳动、资本、企业、工资、货币、HA或年度runner。

本轮仅新增：
- src/ch5_two_asset_hank/multi_province/outer_one_turn.py
- tests/test_outer_one_turn.py

**这是预给定阶段结果的拼装工程，不是真实组件执行调度。** 原方程、政策、裁切、求解器、网格及旧生产链未改；资本、企业、综合工资及货币方程没有在本接口重新求解或取得数值验证。O3真实调度仍未实现，真实模型运行仍0。

## 阶段交接与候选状态

| 阶段 | 输入/输出及本接口检查 | 保持的边界 |
| --- | --- | --- |
| O2家户批次 | 读取prepared.context/entering_snapshot及household_outputs的原字段，核对scope、原收敛声明、逐来源地诊断和省序；复制Ct/Lt/At/Bt/AtTax为不放大只读元组 | 只做字段接口兼容；不导入O2工厂，不冒充原工厂已经重新验证或实际HA执行 |
| 原工作地劳动与A1 | 原劳动阶段声明Ct、进入轮wjt、目的地tau与本轮一致；复用A1按来源列乘p，企业使用该A1劳动 | 不计算消费驱动核，不归一化，不以家户Lt替代企业劳动；p=0不改成小正数，目的地企业劳动仍须正 |
| 资本 | 预给定资本阶段的At、H、进入轮企业ra及省际比例必须与家户/快照一致；接给定Kt_supply和下一轮家庭rah | 不将H换E，不将Bt送生产资本，不重算或改变资本网络；旧ra、资本rah与企业当轮输出ra分开 |
| 企业 | 每省声明的资本/劳动输入匹配前两阶段；检查输出Kt=Kt_supply+进入GovInv，Lt等于A1目的地劳动，原FirmResult字段结构完整且有限 | 不执行企业方程或修改原裁切补偿；旧Govinc只作原输出字段读取，最终不入账、不影响新Govinc |
| 下一轮净工资 | 复用O1 ProductionWageRecord，核对k生成→k+1消费、同省序/上下文/源包及进入快照；六类实际给定输入字节逐件匹配原envelope的SHA/字节数，再对照当前企业gross工资、目的地税、phi/sigma和偏好声明 | 不计算工资公式；标签/字节一致不证明生产者调用，原pending科学消费门保持关闭 |
| 货币/财政 | 货币it/rb为预给定结果且单位/期次一致；复用工资税、家户H聚合和省级财政工程函数生成Govinc；按既有Bt*rb*H角色分列债息并计算GovSurplus诊断 | 不运行Taylor函数、不设财政余额为零，不改变债务、央行或GovInv自适应，不取得财政/GE接受 |

工资生产者六类输入为既有gross_firm_wages、destination_taxes、phi_destination_origin、sigma_destination_origin、preferences及generation_snapshot。generation_snapshot绑定本进入轮快照；新企业工资另由gross_firm_wages载荷绑定，保持旧一轮代码“进入省记录+当轮企业工资”传给工资生产函数的角色。原source_bundle/输出原字节及pending资格不改写。

候选下一轮明确保留：
- N仍为家庭H；Tt保留家户输入原值；AtTax保留家户未乘H的原量。省级财政金额只在既有财政边界各乘H一次，不向下一轮家户输入塞总额。
- Lt_supply及Lt_prev对应企业A1劳动；Kt_supply和Kt_prev对应各自资本/企业结果。原家户Lt只作为原统计量保存，不给企业额外乘H或z。
- 家庭rah来自预给定资本阶段，企业ra来自本轮企业输出；w来自供k+1的原净工资载荷，rb/it来自预给定货币阶段。
- Yt_1/Zt_1/pit_1来自进入轮状态；Govinc由已采纳五项金额账覆盖原企业旧Govinc。GovSurplus仅诊断，可能非零。
- 输出状态深层只读，所有阶段均不修改输入；中途拒绝不提交部分下一轮。进入状态不能携带TRUE的接受/激活标志来污染候选状态，原convergent仅保留原返回语义。

## O2兼容性的准确限度

O2模块导入会连带加载旧外层模块。本轮采用其**已有字段接口的只读数据视图**，并通过AST核对AssembledHouseholdBatch字段、scope及FirmResult字段名；测试夹具只提供与这些字段相同的预给定数据，不是新的生产批次工厂。

因此，O2真实工厂在本轮没有执行，原请求/初始化/HA返回对象身份未由本轮重验。新接口不认证O2真实类型身份、不放行旧资格、不声称实际生产批次已有来源见证。全部结果保持real_execution_enabled、consumer_ready、formal_ha_accepted、real_data_accepted、scientific_acceptance、model_activation为FALSE；原净工资require_production_wage_consumer_ready仍返回PRODUCER_INVOCATION_NOT_VERIFIED，已在新测试确认。

同样，阶段交接字段匹配不证明原劳动核、资本分配、企业全体输入/方程或工资/货币结果已正确计算。原旧企业输入中Lt_prev等更细语义未在本轮修改或认证，不将本次接口检查当作16项科学义务的关闭依据。

## 限定检查

最终23项固定玩具检查通过：完整两省分项与候选状态；家庭H/原Tt与AtTax、资本/企业/净工资前后版本；原pending门拒绝；O2声明/诊断/省序/快照/值域；劳动Ct、旧wjt、目的地tau；资本At/H/旧ra/比例/单位；企业输入与输出供给/字段；新工资k→k+1及六类字节pin/值一致性；货币单位和非有限值；零就业下企业正值门；债息溢出和失败不修改原数据；资格标志拒绝与深层只读；31个虚拟省份拼装；原字段AST兼容和禁止科学生产者导入。

测试以python -B和sys.dont_write_bytecode=True启动，独立命名空间只加载标准库与既有工程模块；没有O2/企业/资本/工资/货币/劳动生产模块导入或调用，没有HA、真实数据/科学数组或旧runner。31是工程标签，不是模型运行。前期22项和最终23项日志分别保存，既有各专项测试未重复整套运行；工程子账仅在新测试中用于构造/复核玩具量。

ENGINEERING_CHECKS=23_PASS_FINAL
NEW_CODE_PATHS=2
EXISTING_SOURCE_EDITS=0
SCIENTIFIC_PRODUCER_IMPORTS=0
SCIENTIFIC_KERNEL_CALLS=0
MODEL_RUNS=0
O2_FACTORY_RUNTIME=NOT_RUN__STATIC_FIELD_COMPATIBILITY_ONLY
REAL_OUTER_DISPATCH=NOT_IMPLEMENTED
NEW_SCIENTIFIC_RUN_GRANTS=0
SUBAGENTS=0
REVIEW=MAIN_AGENT_SELF_REVIEW__NOT_INDEPENDENT_SCIENTIFIC_REVIEW

现场、原6份缓存字节/SHA256、日志、Git和远端回读回执LOCAL_ONLY保存；旧证据不覆盖。模型分支和代码只本地，GitHub仅脱敏治理文档。

## 下一目标

不再把增加预给定数据包装层当成真实生产闭环。下一工程目标为准备一次原外层组件真实调用的有限验证方案：固定源码/输入、各函数次数、资源时限、审计与退出条件，分清O2原工厂整合、原外层组件计算和HA调用。已有接口可以承接这些结果，但不能凭它们自动调用生产者；本轮未签发或执行该验证。

真实31省p、单位/来源资格、家户收入/劳动激励兼容、完整生产链与均衡口径仍未闭合。任何新的实际科学调用须适用明确的前瞻有限许可；不复用TEMP31 7/7、Moll 3/3、工资/补录关闭额度，初始化旧余量仅原8格。严格reference/thresholds仍null；科学接受、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。R12/R13/WASM、保护重绑定、16项义务及历史dirty树/原件/索引/缓存/LOCAL_ONLY保护保持，不合并main。

前置：[A1规模接口](CH5_O3_A1_SCALE_INTERFACE_IMPLEMENTATION_20261105.md)、[财政金额账](CH5_O3_PROVINCIAL_FISCAL_COMPOSITION_20261105.md)；当前入口：[路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)、[任务清单](../tasks/todo.md)。
