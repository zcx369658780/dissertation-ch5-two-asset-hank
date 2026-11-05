# O3外层省级财政金额账：预给定子账组合工程

DATE=2026-11-05
STATUS=BOUNDED_SUPPLIED_FISCAL_COMPOSITION_ENGINEERING_COMPLETE__REAL_PRODUCTION_NOT_RUN
GOVERNANCE_PARENT=a37bc64fd86492b15ff5d4db715ca04864b73748
MODEL_PARENT=7f1cfff3258327f1539da550a571dbe66fe2bd54
MODEL_CODE_CANDIDATE=a3e357edecdc0cbc29f52ee12818337e507624fe
MODEL_CODE_CANDIDATE_TREE=310e25641fce2fdac5f6e4a6f0c4fc94fb5c77ba
MODEL_BRANCH_AND_CODE=LOCAL_ONLY_NOT_PUSHED
NEW_SCIENTIFIC_RUN_GRANT=NONE

## 已完成的组合

本轮按Owner“请继续”完成已采纳子账的普通工程组合，不提出新经济制度或运行许可：

```text
Govinc[i] = ExistingCorptax[i]
            + AdoptedWorksiteWageTax[i]
            + ProvincialAssetGapRevenue[i]
            + EnteringGovInv[i] * CurrentFirmOutputRa[i]
            - ProvincialTransferTotal[i]
```

工资税沿已定目的地tau×当轮企业gross工资×已聚合A1劳动；家户资产收益差额和转移支付沿已定财政边界各乘同源H一次。这里消费的是已形成的省级金额，不再乘H/p/E/z，不加入旧L*tau或旧Govinc，不重复扣家户税。Corptax保留原工资/收益裁切补偿，GovInv*ra保留原企业项的进入投资和当轮输出收益率角色；不重新计算利润税或再加补偿。

只新增模型树两个文件：

- src/ch5_two_asset_hank/multi_province/outer_fiscal_ledger.py
- tests/test_outer_fiscal_ledger.py

所有既有模块保持；没有改旧firm.py、one_turn.py、财政诊断、HA、初始化或runner。原firm.py:135只用来核对其它金额项及其顺序；其旧工资税/家庭金额尺度没有借此重新采纳。

## 输入、单位与一致性

compose_provincial_fiscal_ledger接收共同BindingContext、HouseholdFiscalUnits、工资税账、家户财政账及完整企业财政输入行。工资税按工作地、家户财政量按居民来源地分别已有明确角色；两份账用同一个省份轴逐省连接，不重分配居民工资收入或引入R/P制度。

组合前重建两份**工程子账**的标准结果，与给定行/合计逐项一致才接受，拒绝被改动的金额、旧scope、错误省序、缺项、错误迭代/快照/源包/网格、非法类型或伪造资格。该复核只使用已存在的标准库工程子账函数，不调用原工资/企业/劳动/HA等科学生产者。

原工资税账没有货币/期间ID，因此本接口要求调用者显式给出payroll_money_unit_id和payroll_period_unit_id，与家户财政单位一致；企业行也需同一单位合同。没有默认单位、换算系数或按相同shape直接拼接。标签相等不验证实际物理单位或生产来源。

企业输入还显式携带当轮gross工资，必须与同省工资税账的gross工资精确一致；要求Corptax声明包含原裁切补偿、GovInv与ra使用原时序。实际调用见证/真实输出身份仍未建立，声明一致不升级为执行验证。没有新数值容差或科学接受阈值。

## 输出与财政诊断边界

输出只读ProvincialFiscalLedger，逐省分列Corptax、工资税、资产收益差额收入、政府投资收益、转移总额及Govinc，并给出total_Govinc。金额符号原样保留；逐项或全国合计溢出则拒绝，失败不交付部分账。原始子账不被修改。

Govinc是扣全国政府债息诊断**之前**的原角色金额，不是GovSurplus，也不设余额为零。本模块不接Bt/rb或运行旧national_fiscal_diagnostics，不改政府债务、央行或GovInv自适应规则。producer_execution_verified、physical_units_verified、full_fiscal_ready、scientific_acceptance、model_activation始终FALSE。

## 验证与工程复核

最终18项限定检查通过，覆盖两省带符号已知金额、分项及合计；旧工资税和H不重复加入；原Corptax及供给ra各使用一次；工资税的显式单位、家户/企业单位、所有上下文/省序/批次拒绝；子账金额/合计篡改及布尔冒充零金额拒绝；资格/scope伪造拒绝；当轮企业gross工资不一致拒绝；非法标量及乘积/全国合计溢出拒绝；结果只读、无GovSurplus/接受升级；31个虚拟省份标签连接和导入限制。31为工程标签，不是科学运行。

测试通过独立命名空间加载标准库绑定、两份既有工程子账和新组合模块，使用python -B及sys.dont_write_bytecode=True，避开HA包初始化；没有真实数据、保存的科学数组或实际模型参数。旧14项工资税、13项家户聚合、O1/O2及历史审计未重复运行；其函数仅在新测试中以固定玩具量构造/复核子账。

ENGINEERING_CHECKS=18_PASS_FINAL
NEW_CODE_PATHS=2
EXISTING_SOURCE_EDITS=0
SCIENTIFIC_PRODUCER_IMPORTS=0
SCIENTIFIC_KERNEL_CALLS=0
MODEL_RUNS=0
HA_ALGORITHM_AND_GRID_EDITS=0
NEW_SCIENTIFIC_RUN_GRANTS=0
SUBAGENTS=0
REVIEW=MAIN_AGENT_SELF_REVIEW__NOT_INDEPENDENT_SCIENTIFIC_REVIEW

主代理完成实现、自审、AST/变更路径/缓存保护核对，不能冒称外部独立科学审查。早期检查与最终18项日志分别保留，未覆盖证据；6份旧缓存字节/SHA256保持。原始日志、现场、提交及同步回执LOCAL_ONLY保存。

## 下一目标与未完成项

外层财政金额组合的工程片已完成；完整O3一轮仍未接通。下一目标为核对A1的H/p/E既有输入来源和单位、保持企业E与家庭H分离，并准备劳动→资本→企业→工资/财政的独立外层组合。不得重新选择A1/A2或已采纳税基/H聚合，也不得以默认p=1、工资总额除均值造就业或复制HA算法推进。

真实人口/货币/期间与来源资格、收入/劳动激励兼容、完整生产链、均衡口径/控制器及实际数值运行均未完成。本次不把可计算Govinc标为完整财政、Results或GE接受，不新增科学门槛。

TEMP31 7/7、Moll 3/3、工资/补录仍关闭，初始化旧余量仅原8格；严格reference/thresholds仍null，科学接受、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。原保护义务、历史dirty树、原件/索引/缓存/LOCAL_ONLY及失败证据保持；只同步脱敏治理文档，不推模型分支/代码，不合并main。

前置：[工资税账](CH5_O3_PAYROLL_TAX_IMPLEMENTATION_20261105.md)、[家户财政H聚合账](CH5_O3_HOUSEHOLD_FISCAL_IMPLEMENTATION_20261105.md)；当前入口：[路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)、[任务清单](../tasks/todo.md)。
