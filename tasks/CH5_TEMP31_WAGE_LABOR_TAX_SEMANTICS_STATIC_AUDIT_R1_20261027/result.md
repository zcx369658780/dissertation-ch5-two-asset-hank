# TEMP31 工资、劳动与税收静态语义审计

固定任务：a4476b1873b0950cf4fbd3d10122de41cd981dec；治理父提交：79b0502feae4c400be3a1cdbd7aad3aa67c55004。
候选分支：codex/ch5-temp31-wage-labor-tax-semantics-20261027-r1；实际日期：2026-10-27（Asia/Shanghai）。

本轮完成有界只读语义审阅。所列PROVEN只表示精确原字节、表达式、索引或静态调用可证；不表示原模型已运行、数值有效、补丁已部署或科学接受。原始MATLAB与论文TeX归档哈希均匹配已记录身份；历史Python从ba985固定Git对象读取，当前实现按工作树实际字节分别记录。c5原档和c3候选没有混作同一版本。

## 实质发现

1. **目的地税/来源地税静态差异可证。** M_W:8、C_W:57–63在综合工资中用目的地tau；M_L:7、C_L:107–125在旧劳动拆分中用来源tau。P3_L:113–131和P3_O:168–176局部改用目的地税。但当前C_RUN:235–240及C_BASE:945–953仍保留来源字段。R3未由此成为全生产闭包。历史统一税率不能证明异质税率索引正确，本轮没有测试任何税率案例。

2. **同税重复楔子的静态路径可见，运行结果未检查。** C_W已经构造含目的地税/迁移楔子的综合w；C_SS:162将其放入下一轮state.w；C_EMP:345–350和C_A:204–211仍向HA传tau，C_HA:159–164再乘该楔子。若该w依合同为净综合工资且消费者tau非零，则是重复楔子风险。初始common scalar w的净身份仍UNKNOWN。P2_A:204–218与P2_EMP:171–184/346–351局部使用tau=0并改初始化；通用HA非零tau仍可服务gross wage调用者。FOC/预算共用同一税后报酬，以及财政/家户双边记账，本身不等于重复扣税。

当前corrected直接链也已核对：C_BASE:285–305 → C_CONT:704–732 → C_SEL:388–414；C_BASE:663–665调用的初始化C_INIT:153–176同样保留(1-tau)*w*z。该路径不由历史包装器替代。C_CONT:43–44的N=800只是网格状态数，和人口N_i分开。

3. **财政表达式、综合工资幂次和偏好方向存在版本差异。** c5:161/M_F:95/C_F:135有L*tau项，c3:50及P2_F:135有工资因子。表达式差异PROVEN，若tau是比例工资税则单位疑点SUSPECTED，未自行选税种或修复。c5:161的j求和中公司税项仍写i下标，另记混合下标疑点，不自行改写。原c5:52和当前/历史wage.py的alphal负幂，与R1 c3候选/P2_W:72的正幂不同。M_O:7–10和C_EMP:339–340保留plus符号，R2 EMP:341为minus。候选局部修订不等于原c5或正式V010已变更。

4. **工资、劳动、人口分别是不同对象。** 企业wjt来自给定目的地L的边际产出并裁切，不是直接观测的年平均工资，也没有在该函数中另解员工需求；家户w是来源省综合指数。个体l、分布加权∫z*l dg、来源人口N、目的地Lt_supply不能互换。旧迁移拆分Ct表达式没有显式z分布积分，不能自动等于论文c5:119的有效劳动定义。当前另有单独命名的列归一化劳动路线，但默认采纳未证明，也不等于真实人员OD。

5. **三份新工资候选没有任何直接匹配单元。** 数据到模型矩阵覆盖3来源×9个实际目标（27个单元）。A为非私营倾向均值31省原始候选，B为私营均值30省非异常候选/西藏30隔离，C为工资总额31省非异常候选。文件内来源声明不替代NBS指标ID、导出及vintage；均不等于模型净工资、边际有效劳动价格或已验证税基。所有原异常年份保持隔离，未推断30含义、未填补、未生成净工资/工资率、未用总额除均值推就业。

6. **历史scalar与实际2018省级观测分开。** 2009输入的composite_wage、wjt、wage_tax各是一个float，加载器将同一scalar放入31个state；不是31个实测工资。原件36263字节，SHA256=507d1259a8a515e4224f40d434bd89645c02472650b51f5ada3181ba4bcdad48。2009 binding和fixed_zt_calendar_year=2020分别记录，不宣称共同vintage。所读src/validators无新候选目录和回执标签的文字引用；这只说明限定读域没有找到该导入桥，不证明所有动态/域外路径不存在。

## 可审阅证据

symbol_semantics_matrix.md给出符号、公式、维度、单位边界、税位及生产者/消费者。
wage_labor_tax_lineage.json记录25条带来源行号的静态有向边与单独的BLOCKED数据/生产接线边。
statistics_to_model_bridge_matrix.md对每个实际目标列三行来源资格。
source_excerpts.json保留必要的原方程和调用上下文，逐项原始文件哈希及原行号可核，不以摘要/哈希代替原文。
owner_decision_brief.md只给至多三项来源支持的非约束性方向，保留既有工作地税合同，不新增桥公式或选择经济学定义。

仅脱敏证据发布GitHub，完整TeX、MATLAB归档、Excel、工资值表、本地旁置回执及个人绝对路径不上传。科研工作树HEAD/index/refs/dirty/untracked、原件、V010/V011及所有历史STOP/PENDING保留。保护终核及最终远端commit/tree/manifest自哈希在外置回执，避免自引用。

artifact_integrity=BOUNDED_SOURCE_IDENTITIES_AND_EXCERPTS_RECORDED__REMOTE_VERIFICATION_IN_DELIVERY_RECEIPTS
source_identity=ORIGINAL_ARCHIVES_AND_HISTORICAL_GIT_IDENTIFIED__CURRENT_AND_ISOLATED_PATCHES_SEPARATED
numeric_review=NOT_RUN
implementation_review=STATIC_TRACE_ONLY
scientific_review=STATIC_SEMANTICS_ONLY__NO_FORMAL_ACCEPTANCE
privacy_review=BOUNDED_PUBLIC_SAFE_SOURCE_EXCERPTS_ONLY
actual_terminal=STATIC_AUDIT_COMPLETE_WITH_GAPS__FINAL_REMOTE_READBACK_AND_STOP_RECORDED_EXTERNALLY
delivery=SEE_DELIVERY_FINAL_RECEIPT_AND_EXTERNAL_FINAL_REMOTE_READBACK
cleanup=NOT_AUTHORIZED_NOT_PERFORMED
not_completed=PRODUCTION_COMMON_SNAPSHOT_CALLBACK;MODEL_LABOR_UNIT_PERIOD_BRIDGE;NBS_SOURCE_DEFINITIONS_AND_VINTAGE;ID_ARRAY_JOIN;SCIENTIFIC_ACCEPTANCE

科研执行、数值模型、测试、预检、项目import执行、HA/HJB/KFE/GE/IRF、科研源码/数据改写、外部数据下载全部0。FORMAL_SOURCE_FREEZE=FALSE；V010=UNCHANGED；V011=NOT_STARTED；Results=FALSE；model_activation=False；REAL_GE=False；FULL_RUNNER_IO_CLOSURE=BLOCKED。远端回读后立即STOP，不启动下一任务。
