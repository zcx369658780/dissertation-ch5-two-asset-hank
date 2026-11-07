# O3上一轮企业劳动：Owner决定与外部输入准备

DATE=2026-11-06
STATUS=OWNER_ADOPTED_PREVIOUS_DESTINATION_FIRM_LABOR__INPUT_PREPARATION12_PASS
SOURCE_AUTHORITY=OWNER_AGREED_RECOMMENDATION_AND_CONTINUATION
SUBAGENTS=0
SCIENTIFIC_CALLS_HA_GRID_GENERATIONS_NUMERICAL_IMPORTS_NEW_RUN_GRANTS=ALL0
REAL_ENTERPRISE_DISPATCH=NOT_IMPLEMENTED_BY_THIS_SLICE
SYNC=PENDING_SYNC__PREVIOUS_SSH_FAILURE_NOT_RETRIED

## Owner已明确的口径

Owner同意：企业公式中的Lt_prev取上一轮同一工作省、同一规模口径的企业有效劳动总量。它不取当轮来源省HA家户劳动，也不取尚未形成的本轮企业劳动。此项不再待Owner选择。

本决定沿用有效劳动已含能力z、A1企业E=pH、家庭H、目的地单次征税和家庭劳动收入直接归属等既有选择。HA算法、效用、网格、数值控制及企业经济公式不改；不补上一轮值或默认首轮劳动。

## 定点核对发现及历史保留

旧one_turn入口把当轮household_lt传入企业Lt_prev；已关闭的七入口观察也确实采用这一传值。原企业公式会用Lt_prev与当前目的地劳动之差影响企业价格及工资，因此新口径不能靠字段改名或重贴标签继承旧企业输出。

旧源码入口、观察runner/fixture/合同、原调用记录、旧B1/B2等证据原样保留。旧返回只证明当时的实际调用，不能冒充本次Owner口径下重新计算的企业/工资结果；旧1/1仍关闭，零重试。原合成输入采纳及保存原值不因本次决定重算或改写。

## 最小工程实现

仅在现有src/ch5_two_asset_hank/multi_province/outer_one_turn.py增加PreparedFirmLaborInputs和prepare_firm_labor_inputs两个定义：

- 读取既有A1账与同一进入快照；重建核对A1内容，拒绝被改动的当前劳动矩阵或目的地合计。
- 复用原O2字段/快照/省序/轮次核对，不装载O2数值工厂或调用科学生产者。
- 每个工作省的Lt_prev只从进入快照中的同名字段取得。缺失或非数值就拒绝，不回退到household_lt、当前企业劳动或默认值。
- 原AtTax按已有家户返回逐项复制，其他省级输入保持；不重复乘H、p、E或z。
- 当前A1目的地有效劳动与上一轮值分列，输出省级映射及其嵌套内容只读；执行/科学/消费/Results/激活标记全部FALSE。

这是供未来原企业调用使用的外部输入准备，不执行evaluate_firm，不安装实际dispatch，也不改变旧拼装函数的行为。结构上的同快照、同轴及H单位绑定，不等于已经证明前序真实企业来源、完整劳动物理单位或全部H/E收入映射。

原进入快照若缺少可信的上一轮企业值，未来准备须拒绝并保留缺口，不能为通过检查修改已采纳保存包。

## 本轮检查及证据边界

新增tests/test_outer_previous_firm_labor_inputs.py仅使用新的两省离线数据夹具和标准库隔离命名空间。先记录缺少新准备接口的预期失败，再由新实现通过12项检查（单次完整检查约0.031秒）：

上一轮值读取、拒绝家户替代、缺值拒绝、非数值拒绝、上下文/快照/来源不符拒绝、A1内容篡改拒绝、H单位不符拒绝、AtTax原样及其他字段保留、深度只读、资格不放行、零输入不伪造正劳动、无数值/科学生产模块或外部动作。

静态对比确认原模块全部既存导入、函数、类与赋值的AST未改变，仅新增上述两个定义。旧缓存6文件、已消费决定、关闭观察fixture/runner原字节保持。未重跑原23项拼装、原6项B1、环境V2或任何既有成功科学观察。主代理工程自审不称外部独立科学审查。

原关闭合同的源码pin保持当时值；当前外层模块有新增代码，不把旧合同复用于当前候选，也不重封来源或续用额度。代码和新检查仅本地，治理树只保存本报告及当前入口。

## 当前未完成事项

实际企业调用尚未使用新准备结果，新的企业/工资返回并未取得。Ct先汇总后倒推与g下家庭收入等价、真实p及就业/工时/货币/时期单位桥、外层校准/均衡与经济停止口径仍未完成；这些问题不由本项12检查自动关闭。

既有实际网格身份/外部保护与完整准入准备方向保持，actual_grid_sha256及严格reference/thresholds仍null；全部消费/科学接受/正式冻结/Results/激活/REAL_GE资格FALSE，NEW_RUN_BUDGET=0。R12/R13/WASM保护STOP及16项义务不变。

本轮只完成该外部输入准备片。后续实际源调用和HA/网格/外层运行仍需各自适用的具体范围与有限授权，不能把本次继续解释为科学运行许可。

关联：[劳动与收入澄清](CH5_O3_EFFECTIVE_LABOR_OWNER_CLARIFICATION_20261106.md)；[当前状态](CH5_LOCAL_FIRST_STATUS_CURRENT.md)；[主路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)。
