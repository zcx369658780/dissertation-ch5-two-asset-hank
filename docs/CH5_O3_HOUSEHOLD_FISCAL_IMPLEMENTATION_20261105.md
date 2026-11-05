# O3家户财政量：Owner采纳H聚合与独立换算实现

DATE=2026-11-05
STATUS=OWNER_H_AGGREGATION_ADOPTED__BOUNDED_ENGINEERING_COMPLETE
GOVERNANCE_PARENT=00f5f2492890ae4fa21696b0819ee1ac864698f7
MODEL_PARENT=6dbe3fbe410e7e30efd93bb84fd4c1cf5a318bee
MODEL_CODE_CANDIDATE=b785bcd0c225d343df986b4e6cafd462ecd40fe9
MODEL_CODE_CANDIDATE_TREE=36b55dc72a83e9b6f5d843f9812ea325463d9545
MODEL_BRANCH_AND_CODE=LOCAL_ONLY_NOT_PUSHED
NEW_SCIENTIFIC_RUN_GRANT=NONE

## Owner决定

Owner对[具体单位合同](CH5_O3_TT_ATTAX_UNIT_CONTRACT_PROPOSAL_20261105.md)回答：“采用财政边界各乘H一次（建议）”。已采纳的模型内部合同为：

```text
provincial_transfer_total[i] = H[i] * household_transfer_per_H[i]
provincial_asset_gap_revenue[i] = H[i] * asset_return_gap_per_H[i]
```

两个家户原量仍分别对应进入快照Tt和原AtTax重构，保持原值与符号；只在财政边界各乘同一来源地、同一迭代的H一次，不使用企业就业规模E=pH。家户Tt输入、HA、原AtTax重构、工资税已含pH的劳动规模和原企业裁切补偿均保持。

本次采纳的是模型内部的分母和聚合位置，不是现实人口/货币/年频单位的认证，不授予数据采纳、模型运行、完整财政或均衡接受。已采纳的工资总额税基不重开；不新增税率或将AtTax解释为新现实法定税种。

## 最小工程实现

仅新增两个模型文件，已有源文件保持：

- src/ch5_two_asset_hank/multi_province/outer_household_fiscal.py
- tests/test_outer_household_fiscal.py

aggregate_household_fiscal_flows复用标准库BindingContext，接受完整预给定来源地行。每行明确H、家户Tt和资产收益差额、原量未乘人口的声明及家庭H尺度声明。HouseholdFiscalUnits要求显式提供H分母、货币及金额流期间的单位ID；各行必须与指定单位合同一致。单位ID只检查声明一致性，不推断换算因子或验证实际单位。

函数核对来源省序、迭代、快照/源包/网格上下文及单位；输出只读HouseholdFiscalLedger，逐项保留家户原量与省级金额并分别求和。拒绝已是省级总额的输入、E就业尺度声明、重复/缺失来源地、不一致单位/上下文、非法标量/负H或乘积/合计溢出。Tt与AtTax允许保留有限正负值，未截零、取绝对值或自动扣税；H=0时不除以H。

输出producer_execution_verified、physical_units_verified、full_fiscal_ready、scientific_acceptance及model_activation始终FALSE，没有Govinc字段；不自动消费未认证生产批次，也不把用户给出的单位标签当成真实来源证书。该模块不接工资/税率/就业率/z/密度或求解器callback，不计算新的AtTax，不触碰家户输入。

## 限定检查及复核

13项固定玩具工程检查通过，覆盖：已知带符号金额和原量保持、H同比一次放大、零H/零流量、拒绝省级总额和E尺度、H分母/货币/期间单位匹配、省序及批次完整性、陈旧或错误上下文、非法数值/类型、逐项及总计溢出、结果只读和资格FALSE、31个虚拟来源地标签及导入限制。31是工程标签，不是31省科学运行。

测试以python -B启动并设置sys.dont_write_bytecode=True，通过独立测试命名空间只加载新模块和既有标准库绑定契约，避开会加载HA的包初始化；未加载真实数据或保存科学数组，未执行任何既有工资、企业、劳动、初始化、HA或外层科学函数。原工资税14项/O1/O2及历史审计不重复运行。主代理完成实现和自审，不冒称外部独立科学审查。

ENGINEERING_CHECKS=13_PASS
NEW_CODE_PATHS=2
EXISTING_SOURCE_EDITS=0
SCIENTIFIC_PRODUCER_IMPORTS=0
SCIENTIFIC_KERNEL_CALLS=0
MODEL_RUNS=0
HA_ALGORITHM_AND_GRID_EDITS=0
NEW_SCIENTIFIC_RUN_GRANTS=0
SUBAGENTS=0
REVIEW=MAIN_AGENT_SELF_REVIEW__NOT_INDEPENDENT_SCIENTIFIC_REVIEW

现场、原6份缓存的字节/SHA256保护、完整检查日志和提交/远端回读回执LOCAL_ONLY保存。只同步脱敏治理文档，模型代码仅本地，未推模型分支或合并main。

## 下一工程目标与保持的边界

工资税子账及Tt/AtTax的H聚合子账均已采纳并独立实现。下一目标为组合这两份账与既有Corptax、GovInv*ra等财政项，明确同轮省序、来源与单位，形成外层金额账；不改旧firm.py/one_turn.py，也不以计算出Govinc金额就宣布完整财政或GE通过。完整O3劳动/资本/企业/工资/控制器组合仍未实现，实际p来源、真实单位、收入/劳动激励兼容与真实来源资格分别保留。

此后普通工程无需重问已采纳的每H聚合合同。任何新的科学制度、物理换算因子、实际科学生产者/HA/外层运行或接受口径仍按Owner权限及前瞻有限授权；不为账项工程重开旧额度。

TEMP31 7/7、Moll 3/3及工资/补录关闭，初始化旧余量仅原8格。严格reference/thresholds仍null；科学接受、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。R12 STOP、R13未授权、WASM六路径STOP、保护重绑定未授权、16项义务、历史dirty树/原件/索引/缓存及LOCAL_ONLY证据保护保持。

当前入口：[路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)、[任务清单](../tasks/todo.md)。前置工资税：[已采纳实施记录](CH5_O3_PAYROLL_TAX_IMPLEMENTATION_20261105.md)。原单位决策稿的“未采纳”文字属于当时事实，由本次Owner决定覆盖，历史原文不抹去。
