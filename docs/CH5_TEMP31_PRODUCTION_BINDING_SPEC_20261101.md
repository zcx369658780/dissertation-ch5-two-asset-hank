# TEMP31 生产入口：静态接线规格与缺口 · 2026-11-01

STATUS=STATIC_SPECIFICATION_READY__PRODUCTION_IMPLEMENTATION_AND_ACTIVATION_NOT_DONE
AUTHORITY=OWNER_CONTINUATION_OF_STATIC_PRODUCTION_BINDING_AND_GRID_PRICE_IDENTITY_REVIEW
GOVERNANCE_CHECK_PARENT=af72ab735e510f239fb69a612001ea80c5b96f4d
SOURCE_WORKSPACE_HEAD_AT_CHECK=db56cfb8b30e14f0f63a2bd30ce40af8e90f596d
SCIENTIFIC_SOURCE_ANCHOR=56447829ce0e6c3c85552c53c351b26a2452a4bd
LOCAL_INITIALIZER_CANDIDATE=1cdebe761dc4406a83093884ae15f0377d891b8f__NOT_PUSHED
METHOD=EXACT_FILE_GIT_IDENTITIES_AND_STDLIB_AST__NO_PROJECT_IMPORTS

本轮把生产接线方案细化到实际入口、输入输出和拒绝条件，没有实现或运行新生产程序。当前源码工作区未建代码图谱，未使用其他历史仓库图谱推断当前代码；限定读取20个相关源码/入口文件，现场字节与当前HEAD的Git Blob、大小、SHA-256一致，20项静态观察确认。它不是全仓库动态依赖闭合或生产验收。

## 已核实的现有调用链

| 环节 | 实际位置 | 静态事实 |
|---|---|---|
| 年度入口 | validators/multi_province/mp4c_python_annual_production.py:145、167–187 | solve_batch仍调用anchor._source_initial_arrays、含tau的anchor.HouseholdInputs及历史HA adapter；未调用新增资产乘收益率初始化或净工资消费者 |
| 导入来源门 | validators/multi_province/mp4b_python_empirical.py:19、30–64 | import时即执行旧bootstrap；ORACLE_SHA仍固定九月export身份。当前export为另一有语义版本；本轮只确认静态冲突，未执行bootstrap，也未改pin |
| 外层单轮 | src/ch5_two_asset_hank/multi_province/stationary_runtime.py:35；one_turn.py:194–238 | 固定调用旧source-like composer，其劳动输入仍为tax_by_origin；目的地税修正模块独立存在，没有接入此链 |
| 净工资生产 | src/ch5_two_asset_hank/multi_province/wage.py:11 | 已按目的地tau[j]/sigma[j,i]计算来源地家庭净复合工资；不能再让家户消费端扣税 |
| 工资来源凭据 | temp31_ha_wage_debug.py:56、161；temp31_ha_taxfree_bootstrap.py:44、106 | 现有later wage凭据要求SyntheticNetWageCalculation，其scope明确SYNTHETIC_FORMULA_RECOMPUTATION_ONLY；不具备真实生产调用凭据桥 |
| 初始化与净工资HJB | temp31_asset_return_initializer.py:67；temp31_netwage_hjb.py:65 | 新初始化已有固定合成检查通过，净工资HJB公开接口已存在，但尚无新生产HA组合包装层；本轮不进入黑箱求解 |
| 旧HA组合 | validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py:15–41 | HJB返回后无收敛条件便调用KFE；旧行为保留作历史，不能直接成为新正式生产资格门 |
| 驻定资格 | matlab_faithful_kfe.py:10；multi_province/steady_state.py:172–194 | KFE公开结果提供raw_residual_inf，未提供原方程严格驻定证书；旧外层按batch.converged计家庭通过数，未独立认证原KFE驻定 |
| 汇总与资本 | exports/matlab_faithful_two_asset_ha.py:686；capital_allocation.py:31、70 | 汇总函数仅消费网格/消费/劳动/密度，劳动为z加权统计量；资本接口只接At、人口、跨省比例与旧firm-ra，不接Bt |

旧bootstrap保留的SHA-256=B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3；当前export Blob=e144c645d3f4dc842c2faa6b93b2ba0e24275dcf、SHA-256=a7539eb6ba076176b81f832c1800d38d8d170dad8f3619d3b0f3893c5a163fff。不能改常量或换回旧export来掩盖代际混装。新入口应独立绑定同源组件，旧年度入口/adapter/静态MP1字段映射原样保留。

## 拟议接线及其输入输出

```mermaid
flowchart LR
    S[获准输入与同源身份] --> W[带期次和来源的净工资凭据]
    W --> I[逐来源地净工资输入与新初始化]
    I --> H[保持原网格的HA公开接口]
    H --> Q[原始诊断与严格资格分开]
    Q --> B[完整省份批次和单位台账]
    B --> O[单轮企业 资本 工资 财政]
    O --> N[下一轮工资凭据]
```

以上为拟议接口，图中新增凭据/组合/资格桥尚未实现或激活。具体规范如下：

1. **入口身份与完整批次。** 独立入口先绑定源Blob、输入版本/年份、省份顺序、上下文和进入本轮的只读快照。所有来源地家户使用同一快照；任一必要来源地失败时，不向企业块提交半个批次。真实canonical、缓存、年份及31省输入资格仍待各自授权核验，本轮不读取数据内容。
2. **工资凭据桥。** 保留composite_household_wages既有公式。在实际生产者调用处，记录生成期次、进入消费期次、省序、上下文、实际企业工资/目的地税/phi/sigma/偏好输入身份及原净工资输出身份。生成于t的工资进入t+1；不能为了套凭据而用t+1的新矩阵重算、改变既有时序。首轮19只在已有数值初猜合同适用时标记为numerical_bootstrap19，不能标成实证工资。后轮需新增明确的真实生产凭据接口；禁止把SyntheticNetWageCalculation改标签、替换历史SOURCE_COMMIT或仅凭state.w数值就当来源通过。现有Temp31EffectiveWageRecord的校验分支也需有对应、经审查的生产桥，不能假装当前已兼容。
3. **逐来源地消费者与V0。** 依据同一省序/origin_index把净工资记录交给明确的净工资类型；家庭接口没有tau/migration_costs再扣减入口。state.rah/rb与消费者r_a/r_b一致；原Tt/rb_gap保持。新初始化必须显式声明V010_TOTAL_WEALTH_NUMERICAL_INITIAL_GUESS，在首次HJB前封存该来源地输入及F-order V0/labor身份。数值初猜资格不替代两账户提款/成本/政策可行性。
4. **HA组合包装层。** 候选组件是同源的src净工资HJB、指定原KFE和固定export中仅消费数组的aggregate_stationary_household。该汇总函数不接HouseholdInputs或tau，可作为显式固定依赖，而不能经旧mp4b bootstrap偷渡旧solver/default。新组合层须显式绑定组件和身份；KFE只接同次HJB返回的post_convergence_operator.full及同一(b,a,z)网格。不能重装算子、更换密度、裁剪负质量或修改黑箱来救通过。此处是接口候选，不是已获准的HA调用。
5. **严格资格独立。** 保留原hjb.converged与原KFE raw_residual_inf，不改名或覆盖成另一种含义。正式资格需由黑箱外的独立记录描述HJB收敛、原后置算子驻定、密度/质量及相应已获准门槛；污染行线性方程残差不能冒充原方程驻定。当前KFE返回类型没有该证书，新外层不能直接复用旧HJB-only通过计数作为严格HA通过。若需真实资格诊断/求解，要使用对应科学预算；本轮未执行，也未新增接受阈值。
6. **统计量、单位和批次。** 保留汇总输出c_ss、z加权l_ss、a_ss、b_ss及原AtTax重构角色。家户统计量、来源地人口、目的地劳动与省总量必须在接口台账分别标明；不能在家户批次预乘N后又在资本/劳动/财政边界重复乘N。资本继续At-only，Bt不进入生产资本接口。真实人口/年频/货币量纲资格仍不能由源码身份或字段名证明。原PreFrozenHouseholdOutputBatch的原始converged语义保留；未来正式资格作为独立证据，未通过时不得送入正式生产。
7. **外层税率、机制与时序。** 当前旧入口为source-like不归一化劳动机制；最小拟议修正是保持这一机制并用目的地税修正路径，尚未实施/采纳为生产。reconstruct_temp31_normalized_worksite_labor还引入按来源地劳动总量归一化，输入及经济含义不同，不得为接口方便静默选择；若改机制须Owner决定。保留目的地行/来源地列、资本旧firm-ra时序、企业/货币/财政既有规则；企业更新后的工资输出及其证据送下一进入期。
8. **终端状态。** 严格家户资格、外层停止条件、来源/输入/网格/输出身份和运行预算均须对应。旧SUCCESS标记或宏观误差变小不能替代严格HA资格，更不能由8格初始化通过直接获得Results/REAL_GE资格。

## HA网格和价格变量的明确边界

HA所有grid参数继续视为不可变黑箱。当前旧年度入口第162行与既有R1–R3参考构造一致：(b,a,z)=(20,20,2)，b范围[-2,5]、a范围[0,10]、z=[.8,1.3]、切换率1/3。本轮只比较构造式及来源，没有生成生产HA节点数组或测量运行时网格哈希；不把这一静态匹配说成运行认证。未来外层只能在获准时记录原对象/数值/dtype/轴/内存表示身份，并前后比较；不能改变节点、重采样、改flags或重建另一网格来使检查通过。既有8格合成fixture不替换生产网格；余下7个8格worker预算不授权一次800根初始化或HA。

原年度入口的MatlabFaithfulHJBGrid与净工资HJB注解中的Temp31NetWageHJBGrid是不同类型，公开字段均为b/a/z/switch_matrix。字段匹配只支持后续结构接口设计，不证明运行时可互换；惰性接口应保持原网格对象并显式描述所需公开属性，不能为满足类型名重建或转换网格。真实组合相容性仍未测试。

价格必须区分实际变量角色：

| 实际变量 | 本链角色 | 不能直接替代的量 |
|---|---|---|
| state.rah → Temp31NetWageInputs.r_a | 家庭非流动资产基准收益率；历史价格测试rah轴 | 企业state.ra、rk及其上下限 |
| state.rb → Temp31NetWageInputs.r_b | 家庭流动资产利率；借款侧原rb_gap规则保持 | 另一个未获准的金融价格或自动新范围 |
| state.w、历史测试net wt | 每来源地家庭净复合工资 | 目的地企业毛工资wjt或wt0 |
| FirmResult.wjt、state.ra | 企业工资和回报输出，经既有企业规则和界限处理 | 历史家庭净工资/rah包络 |

既有已测点包络rah[.045,.09]、rb[.01,.03]、净wt[15.5,22]的来源见已批准调试规则；它不是连续可行域，也不是这些企业变量的新clamp边界。当前固定(.09,.02,净19)保持R1 P0身份，本轮不改ramin/ramax/wjtmin/wjtmax，也不另扣税。

## 可实施分片与仍未完成的门

先做隔离的惰性接口骨架：生产工资证据、逐来源地输入包、完整批次与严格资格记录，实际HA依赖只能由显式stub注入且默认禁用。然后用不导入模型的工程检查拒绝错省序/错期次/错源/重复扣税/错单位/网格更改/不完整批次及HJB-only资格；这类工程接线结果仍不能替代真实数值验证。该骨架和检查尚未实施。

之后才可能在对应授权内绑定不变公开组件，并另行安排冻结网格单点HA及严格驻定；生产来源桥、劳动机制/时序的适用科学合同、真实输入、数值初猜可行性及各自预算须明确。31省稳态、GE、动态、IRF、福利和论文Results排在这些门之后。

本轮交付包括20项静态观察、20文件身份及机器可读拟议接线契约；逐项证据与审计脚本仅LOCAL_ONLY，不上传模型源码或原始科学数组。科学import/initializer/root/HA/HJB/KFE/GE/IRF/policy/MATLAB调用0，初始化调试预算仍3/10、余7；旧证据、dirty工作树/index、V010、WASM/R12 STOP、R13未授权、保护重绑定未授权、16项义务与Results FALSE保持。无分支删除或main合并。

ENGINEERING_VERDICT=PASS_BOUNDED_STATIC_CALL_CHAIN_AND_REVIEWABLE_INTERFACE_SPECIFICATION
PRODUCTION_BINDING=NOT_IMPLEMENTED_NOT_ACTIVATED
SCIENTIFIC_ACCEPTANCE_AND_STRICT_STATIONARITY=NOT_ESTABLISHED
