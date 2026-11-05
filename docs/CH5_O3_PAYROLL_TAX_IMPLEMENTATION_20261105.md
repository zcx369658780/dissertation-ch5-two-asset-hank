# O3工作地工资税：Owner采纳与独立外层子账实现

DATE=2026-11-05
STATUS=OWNER_PAYROLL_CONTRACT_ADOPTED__BOUNDED_LEDGER_ENGINEERING_COMPLETE
GOVERNANCE_PARENT=6fc223e6b4dc365d983e63910ac4c655f694dc2f
MODEL_PARENT=cc5655af9fb15dffa16708932b42b5213cd84964
MODEL_CODE_CANDIDATE=caa5a83c6b480f616286ffb7eabbae6abdb1f9e8
MODEL_CODE_CANDIDATE_TREE=f616a26b1d66ae4879c3c0896d4a8ba164eaaee0
MODEL_BRANCH_AND_CODE=LOCAL_ONLY_NOT_PUSHED
NEW_SCIENTIFIC_RUN_GRANT=NONE

## Owner已采纳的精确范围

Owner对以下问题回答“采用该工资总额税基（建议）”：

> 是否采纳O3工资税口径：目的地税率 × 当轮企业输出的税前工资（沿用原有上下限处理）× 已聚合A1劳动？不再额外乘人口或就业率，HA不再扣同一工资税。此次只决定工资税金额合同，转移支付Tt、资产税AtTax的省级单位转换仍另行核实。

因此工资税金额口径及工资版本已采纳，不再列为Owner待选：

```text
GrossPayroll[j,k] = firm_wjt_out[j,k] * L_A1_supply[j,k]
WageTax[j,k] = tau_enter[j,k] * GrossPayroll[j,k]
L_A1_supply[j,k] = sum_i q[j,i,k] * p[i] * H[i]
```

k为外层迭代，不是经济年份。gross工资取该迭代企业输出、沿用原上下限处理，与后续净综合工资生成使用的企业工资相同；不取旧进入工资、裁切前wt0或家户net综合工资。A1劳动已经含pH，不重复乘H/p/E/z。企业原裁切及Corptax补偿不变，sigma不自动入政府账，净工资进入HA不重复扣同一税。

本次只采纳工资税合同。它不构成Tt/AtTax省级金额桥、R/P居民收入制度、真实来源/数据资格、E3、完整Govinc、均衡接受或新模型运行授权。

## 独立工程实现

仅在模型树新增两个文件，保留全部已有源代码：

- src/ch5_two_asset_hank/multi_province/outer_payroll_tax.py
- tests/test_outer_payroll_tax.py

account_worksite_payroll_tax复用已有标准库BindingContext，输入为按目的地排列的完整预给定行。每行带同一上下文、目的地、税率、企业gross工资及已聚合A1劳动声明。它核对省序、迭代、快照/源包/网格身份的一致性和数据语义；计算税前工资总额、已采纳工资税金额，并单列历史L*tau作对照，**不将旧项加到新税上**。

输出为只读PayrollTaxLedger，保留目的地逐项和全国合计。producer_execution_verified、full_fiscal_ready、scientific_acceptance及model_activation固定为FALSE；没有Govinc字段，不接Tt/AtTax，也没有求解器callback、生产者调用或自动派发入口。语义标签和上下文匹配仅证明所给数据声明一致，不验证数据确由当前企业调用产生，不证明物理单位或实际裁切过程。

scalar域拒绝布尔、字符串、非有限数、负工资/负劳动、区间[0,1]外比例税及乘积/总计溢出；这些是账项接口域，不是新的模型接受阈值。零税/全税/零工资或劳动在独立账中有定义，不因此认证上游工资/劳动生产者可行。

## 限定检查与工程复核

使用python -B，且测试设置sys.dont_write_bytecode=True；仅加载新模块和既有标准库绑定契约，绕过会导入HA的包初始化。固定玩具输入不加载真实数据、保存的科学数组或实际模型参数，不调用现有工资/劳动/企业/初始化/HA等科学函数。

14项限定检查通过，涵盖：

- 两目的地已知金额及旧项分列；劳动同比放大一次；零税/全税/零工资或劳动。
- 所给gross工资原值使用；错省序、重复/缺失批次和错误输入类型拒绝。
- 陈旧迭代、错快照/源包/网格/省序/上下文拒绝；旧工资、net工资、裁切前工资及未聚合劳动声明拒绝。
- 非法标量/税率、逐项及合计溢出拒绝；结果只读、完整财政状态保持FALSE。
- 31个虚拟目的地标签路由与声明边界，及只加载标准库/绑定契约的限制。31是工程标签，不是31省模型运行。

ENGINEERING_CHECKS=14_PASS
EXISTING_SOURCE_EDITS=0
NEW_CODE_PATHS=2
SCIENTIFIC_PRODUCER_IMPORTS=0
SCIENTIFIC_KERNEL_CALLS=0
MODEL_RUNS=0
HA_ALGORITHM_AND_GRID_EDITS=0
NEW_SCIENTIFIC_RUN_GRANTS=0
SUBAGENTS=0
REVIEW=MAIN_AGENT_SELF_REVIEW__NOT_INDEPENDENT_SCIENTIFIC_REVIEW

检查包括AST、精确变更路径、文档一致性及Git差异；不重跑已完成O1/O2或历史51,159项合成检查。测试通过只接受独立工资税账的工程范围，不冒充真实生产/完整外层闭合。完整原始检查日志、现场与同步回执LOCAL_ONLY保存，旧6份缓存按字节/SHA256保持。

## 尚未完成与下一目标

O3完整组合仍未实施。劳动A1的实际p来源/人口就业效率桥、居民收入与劳动激励兼容仍按原记录保留；未接旧one_turn、firm或任何runner，未修改其历史Govinc。

工资税子项已完成采纳与独立工程；G04其余Tt/AtTax金额单位和人口尺度并未关闭。下一目标是定点复用既有来源，核清这两个量在家户与省级财政之间的单位合同，再进行受其影响的外层财政组合；若证据只支持UNKNOWN则如实保留，不自动乘H、不改成E，也不自行设财政余额为零。

所有实际HA/企业/劳动/工资或外层科学执行仍需对应前瞻有限许可。TEMP31 7/7、Moll 3/3及工资/补录额度保持关闭；初始化旧余量仅原8格范围。严格reference/thresholds仍null；科学接受、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。R12 STOP、R13未授权、WASM六路径STOP、保护重绑定未授权及16项义务保持。原件、历史dirty树、索引、缓存和LOCAL_ONLY证据保留；只同步脱敏治理文档，不推模型代码，不合并main。

前置决策稿：[工资税金额合同](CH5_O3_FISCAL_PAYROLL_CONTRACT_PROPOSAL_20261105.md)，其“未收到决定”为当时状态，已由本次Owner回答覆盖；历史原文保留。A1等既有决定见[恢复记录](CH5_O3_LABOR_WAGE_TAX_DECISIONS_RECOVERED_20261105.md)。当前任务入口：[路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)、[任务清单](../tasks/todo.md)。
