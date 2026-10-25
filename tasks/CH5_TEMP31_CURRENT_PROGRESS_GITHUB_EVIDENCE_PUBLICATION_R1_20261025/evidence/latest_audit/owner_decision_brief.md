# Owner 决策简报

本轮只审计文本，未导入、编译或执行被审计源码，未运行测试、预检或模型。三个原件身份匹配。字段账本的 SOURCE_CONFIRMED 只确认静态代码映射；不表示真实 canonical 数据已被接纳。

## SOURCE_CONFIRMED

- 初始 w 来自 canonical.scalars.composite_wage；wjt、tau 来自另外两个 scalar key。加载器未重建净工资，也未把 CANONICAL_SHA 与实际 canonical 字节比较。
- destination j 的 tau 用于工资聚合、迁移劳动和企业工资税项。企业工资税项是 Lt_supply[j] × 新 firm.wjt[j] × 进入轮 tau[j]，仅一个显式税率因子。
- phi[j,i] 由进入轮 Y/L 的对比构造；回调刷新 phi 后家户仍读取 state.w。初始化和 solve 都读取同一命名 state.w。
- 通用 HA 保留非零 tau 功能。多省净综合工资路径局部传 tau=0；初始 seed 已经净税尚无原件证明。
- 家户 l_ss 是 z 加权分布聚合；企业接收双边劳动矩阵的目的地行和，不能直接视为同一劳动量。
- C 的全列引用与摘要属于 SYNTHETIC_ONLY 目标合同。其源码明确阻止真实 canonical 准入。

## SOURCE_CONTRADICTION

未取得足以比较数值/来源相互矛盾的真实 canonical 原件，也没有证据表明 C 的严格生成-vintage 规则已成为生产合同，因此不把“缺证”写成已证实的违约。已确认的时序差异见冲突表 V2/V3：它们与“所有输入都由同一轮生成”的无条件描述不兼容，但允许滞后还是同步尚需 Owner 明定。本轮没有擅自补设这条生产规则。

## OWNER_DECISION_REQUIRED

### 1. 初始净工资来源

方案 A：保留历史 seed，须取得原始 canonical、生产函数和净税/单位/时点证明。优点是保持原有初始化；缺点是不能仅以旧标量作真实税后工资证据。

方案 B：在另行授权的隔离任务中，从同一指定快照重建初始 w。优点是生成链更容易核验；缺点是改变初始化合同，可能影响原有 fixture/数值路径，当前不获授权。

建议先补齐原件、数据字典和 seed 生成链，再决定是否保留或重建；本轮不选择经济制度。区分证据：canonical 字节与 hash、实际生成函数、四类输入和逐字段 vintage。

### 2. phi 与工资 vintage

方案 A：要求 w、wjt、tau、sigma、phi 同一生成快照。优点是来源合同直观；缺点是可能改变历史带入 w 的时序，需要独立审查。

方案 B：明确允许滞后 phi/w，但每项记录 generation_vintage 与 consumption_snapshot。优点是可表述当前的带入路径；缺点是不能再把 OLD_TURN 标签当作共同生成证明，经济含义需要裁定。

建议先明确“共同消费快照”与“共同生成 vintage”的区别，再由 Owner 选择。区分证据：原始时序合同、w 的实际生成记录、phi 的指标定义，尤其初始 pop 与后续 firm Lt 的分母桥接。

### 3. 正式单位权威

方案 A：以原始数据字典和模型方程单位表为权威，附每列缩放/物价基期/模型期间。优点是可逐字段追溯；缺点是需补齐原始材料。

方案 B：若原定义确实缺失，由 Owner 单独冻结明确的模型归一化及输入转换表。优点是未来规则可明确；缺点是这是新的合同决策，不能冒充已恢复的历史事实。

建议先取 A；缺失则保持 UNKNOWN，再单独决定 B。工资、Ct、a/b、Tt、GovInv、Y、N、l/z、rb/rah/rk、rho、switch rate 与模型时间必须一起协调，不能凭变量名或数值量级确认。

### 4. 目的地税率与税基

方案 A：保留源码先用旧工资拆劳动、再用新企业工资计税的顺序，显式声明这种价格/数量时序。优点是忠实当前顺序；缺点是不能声称家户与企业同价同税基已闭合。

方案 B：在另行授权下讨论统一 payroll 价格/数量基准。优点是比较基准更清楚；缺点是可能更改经济/数值合同，当前不实施。

建议先取得目的地税率文件、ID join、劳动/HU/效率和货币期间定义，再讨论时序。区分证据：逐目的地 gross payroll、tau 口径、家庭聚合到双边劳动的会计桥；本轮不运行此比较。

### 5. 是否允许真实 HA

方案 A：来源、单位和 vintage 闭合前，只保留静态/合成 spy 工作。优点是不会把假数据身份带入真实求解；限制是没有科研进度或收敛结论。

方案 B：补证并经独立验收后，另发首次真实调用合同，明确输入身份、次数、失败策略和停止条件。优点是可审计；前提未满足。

建议当前维持 A。本次任何审计 PASS 都不授权真实 HA 或后续任务；B 需要新的明确授权。

## BLOCKED_NOT_EVIDENCED

原始 canonical 字节与唯一上游生产函数、真实省份 ID/名称/顺序及矩阵/税率 join、原始单位与期间字典、初始净工资生成链、phi/w 生成 vintage、家户与目的地劳动/工资税基的单位与时序桥接、真实 callback 输入闭包及真实 31 省 snapshot/tuple digest 均未闭合。没有用任何合成 fixture 填补这些项目，也没有把输入包中的历史测试结果作为本轮执行结果。

保持 FORMAL_SOURCE_FREEZE=FALSE，V010=UNCHANGED，V011=NOT_STARTED，Results=FALSE，model_activation=False，REAL_GE=False，FULL_RUNNER_IO_CLOSURE=BLOCKED。交付后 STOP。
