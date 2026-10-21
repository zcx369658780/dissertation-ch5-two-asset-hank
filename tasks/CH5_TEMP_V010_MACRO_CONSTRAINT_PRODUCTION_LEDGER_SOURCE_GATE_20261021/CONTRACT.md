# CH5 TEMP V010 — 宏观约束可证伪诊断与真实生产账本源码限域审核

TASK_ID=CH5_TEMP_V010_MACRO_CONSTRAINT_PRODUCTION_LEDGER_SOURCE_GATE_20261021
REVISION=ISSUED_20261021_R1
SCOPE=SOURCE_ONLY_MACRO_PRICE_CONSTRAINTS_AND_REAL_LEDGER_STATIC_INTERFACE
AUTHORITY=Owner 2026-10-21明确同意继续科学研究，沿上次约定优先在不运行HA条件下诊断宏观收益约束与真实账本接口
SCIENCE_SOLVER_BUDGET=0

## 0. 为什么进入这张任务
- 已接受TEMP 100轮最终未收敛，两省raw ra0约0.3846/0.4272，超过0.09受界值；100轮ra和wage均触界100/100。家庭实际同S收益rah约0.389/0.419和工资wt0形成的w_eff约6.948/7.029，与受界后的企业价格明显有差。不能因此定单一bug或静态改价就会收敛。
- 上次A+B合成前置成果run f619d7ce43a94088ab9b20ac0be1c45c，真实review候选4e05976bbc8068b971ba5915133e9a6c3b73193d存在，但Astra因ZIP原字节独立获取受限仅REVIEW_PENDING_IO；不能把其中六组模拟测试当成已独立认可的生产ledger验证。旧HTTP候选1579e7f1d7a1975c322dd6ae9af1776e88e83e7c同样REVIEW_PENDING_IO。两份都不得修改、触碰或清理。
- 独立历史E2报告已确认A1在checkpoint os.replace遇WinError5，append事件11条而checkpoint当前为seq9；A2/A3各25条。全停信号传播曾晚于故障，科学A1/A2/A3还没有可比较四臂结果。WinError5是否因Windows reader delete-sharing，仍非确定原因。
- 本任务目标是取得**真实生产ledger源码接口的静态证据与宏观约束的可证伪科学假设**。仅在已经批准的受限私有证据ZIP可精确验证身份时阅读选定源码及极少数事件元数据；绝不运行生产ledger或HA，不做原日志写入。

## 1. 授权、来源与BOOTSTRAP
先从live治理branch同提交读CURRENT、TASK_CURRENT和docs/DOC_INDEX_CURRENT，确认此TASK_ID唯一ACTIVE。根据后发ISSUE_MANIFEST的issue_commit/Blob读取本合同/参数，历史fixed review parent不得冒充live HEAD。所有来源身份在TASK_PARAMETERS枚举，只有：6份科研审阅/恢复文档、模型历史commit下4份源码（只读静态）、前次已独立验证的1,214,713B私人科学E2证据归档（仅本合同显式特例）。
本地私有来源访问必须按参数：可信父根D:\ProjectTemp中的原TEMP私有scratch根只对四个精确候选路径stat。没有一个唯一匹配且SHA256等于F3E8984FE4D2EF4BE65692C27FA7594D96B870D372A8C45D029899F7891841D8则停止这部分SOURCE_MISSING_OR_AMBIGUOUS；不扫全机、不猜改名、不把别的同名备份当已验原件。若存在一件，允许用标准库一次校验这个本机原归档本体长度/SHA，读取其ZIP中央目录**仅作为成员名元数据**（成员数≤300），最多选择12条名称相关且文本安全的ledger/journal/checkpoint/stop/driver/controller/current/events成员，解压后总量≤262144B、单件≤65536B。禁止读ZIP内嵌归档、HA数组、其它不相关文件、旧491/158/910件ZIP。输出公开材料不得复刻私有events或整段源码。
BOOTSTRAP0仅可信父链、旧源根只读及新scratch不存在验证；BOOTSTRAP1独占创建参数唯一新scratch，BOOTSTRAP2安全日志首写前复核；正式工作树仅3条Git locator/index只读命令及前后hash。全部脚本/摘要/安全日志在新scratch，任何外部写入STOP E2。源已消失不等于假造其存在；有历史报告仍可完成不依赖私有原件的宏观诊断和差异表。
不用安装包、不修改Git凭据/SSH/代理、真实数据或任何HA/MATLAB源；不得导入/执行旧归档中的Python源码。仅可标准库解析AST和原始短文本。保留所有资源与首错，OS子孙观测不到写UNKNOWN非0。两阶段时间/进程及文件预算均在参数冻结，旧CLOSED预算绝不结转。

## 2. 科研阶段M：宏观价格约束的静态可证伪机制图
严格从已接受2026-10-18来源分析与冻结静态源码导出：raw capital return ra0 -> clip ra_used，Kprivate+GovInv与Y、rk、利润补偿，lagged raw score+同S资本配置与家庭rah，firm wt0/wjt、wage_caculate对应目的地税/迁移楔后w_eff，GovInv和Zt的非同步触发条件。
重点完成：①由firm方程推导K与raw-ra上界的当轮**静态必要尺度读数**，核历史审查Kreq约7708/9867与当轮2278/2668之比约3.38/3.70；②GovInv仅在合成双省max KN gap<0.1才间歇更新的证据与raw ra0每轮大于上界的一致性，不能当做求解稳定性定理；③为什么家庭使用raw与企业使用clip差异可能对收益、财富与劳动供给反馈形成影响，但未被真实四臂实验验证；④pre-HA prepare hook若没有授权真实源必须标UNKNOWN/NEEDS_OWNER_SOURCE，而不是主张确证覆盖；⑤逐个机制给出下一同初值、同S/滞后、固定税楔的低成本可证伪观察量/停止门。
最终输出macro_constraint_feasibility.md、price_bridge_falsifiable_hypotheses.json、science_evidence_tiers.json；各结论明确REVIEW_ACCEPTED_STATIC_FACT、STATIC_FORMULA_ORACLE、PRIVATE_SOURCE_CONFIRMED、HYPOTHESIS、NOT_OBSERVED等级。
不得运行HA/KFE/GE/IRF、修改ra上界/工资截断/GovInv或Zt方程、偷偷用重标尺救收敛、生成虚构轨迹或宣称调整价格会取得稳态。

## 3. 科研阶段L：真实生产ledger只读源与接口门
沿用已接受E2终审事实，针对上述准确归档在范围内确实存在的选定有限文本源码，追踪单写者journaling、seq/prevSHA链、current.next/open与os.replace、checkpoint异常后的partial state、持句柄读者、共享STOP广播、各ARM下一HA调用前扣账和全停顺序。
只读静态AST+精确短文本必要片段定位函数/调用；**禁止import/exec/archive脚本、禁止触碰真实账本的current.json、events原件执行、禁止任何真实HA调用**。可在独占scratch做非HA的纯公式/静态一致性小脚本，但不得把上次六组合成测试重演当作“真实生产ledger已验证”。
需给一份production_ledger_call_graph.md（函数/相对路径/输入输出/状态转移与缺失项）、ledger_source_boundary_matrix.json（每项有内容Sha/原件层级/是否经过原始生产代码接口确认）、production_gap_report.md（WinError5原因证据、checkpoint错位根因尚未证明、STOP传播机制与需补源）、proposed_nonHA_interface_tests.md（未来另需Owner批准的真实来源单写者sandbox接口测试具体方法）。
若旧私有归档不足以支持真实接口验证，保持PARTIAL_SOURCE_ONLY，不因资料缺失重启一整套工程，阶段M仍可交付完整可证实内容。禁止因合成测试成功就改变历史WinError5的归因或启动A1–A3。

## 4. 预留后续TEMP经济学对照设计（仅DESIGN）
仅形成下一次Owner E3科学预算决策表：A0只读旧100轮基准；A1/A2/A3遵循此前冻结的两因素价格桥定义，三个实验独立从相同第1轮初值开始，前轮raw ra0作资本S score、同S数量与收益/时序及GovInv×0.9/1.1、Zt、工资税/财政口径全部保留。必须核真实进入HA的rah/w_eff（特别prepare_mainline_household_states覆盖），每臂最多100轮且先gate实验完整性。此任务不实际运行、也不提供任何新HA预算。
参数变更、效用/网格/FOC/KFE/黑箱HA改动均是E3，不可凭本任务自行授权。

## 5. 安全交付与停点
资源预算总7200s，所有数字见TASK_PARAMETERS。普通 E1 语法或纯静态分析错误在剩余两批内有界修复并保留首错；来源损坏、路径保护、真实隐私、任何未授权科学调用、系统/认证平台拒绝须停止。
由Codex使用已授权精确Git Data API提交本任务新review分支下唯一固定parent的result.md、manifest.json、evidence_sanitized.zip三件；仅公开新生成、已逐成员脱敏的摘要/静态结论和可复核代码引用，不公开原始私有归档、原事件流、凭据、Windows全路径或原完整生产源码。不能获取真实原件时如实写SOURCE_NOT_AVAILABLE；科学SOURCE_ONLY有意义部分正常交付。上传成功后按固定commit精确readback，报告hash/ZIP成员、真实parent/diff、资源与待办。
Astra按五步独立机器完整性/聚焦科学语义/隐私终审，PASS或CHANGES_REQUIRED先永久归档readback再准确非强制清理本任务三件；PENDING保留。本任务不得接触前两份候选。若再次遇到仅验收工具原字节IO阻断，保留PENDING并让科学分析不依赖未验结果。
最终完整原始JSON receipt Base64+length+SHA256、run_id、实际终态/阶段、SOURCE_ONLY结论/证据等级、原归档读取的实际文件计数、HA等全部0、git commit/tree/parent与退出事件。停点WAIT_ASTRA_TEMP_MACRO_LEDGER_SOURCE_GATE_REVIEW。
