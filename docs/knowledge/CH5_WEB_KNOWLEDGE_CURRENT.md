# 第五章网页知识入口与恢复摘要

## 2026-10-15 新科研决策：保留人均GDP驱动的劳动偏好矩阵方案B

Owner明确优先保留原博士论文第79页的`max_phi=0.3`有界相对劳动厌恶机制，而非人工方案A全φ=1。V009本次只在原冻结`plan.md`之外补数值参数：[CES φ方案B](../../versions/0.0.9/ces_phi_supplement.md)。1省`phi=((1,),)`、2省目的行来源列`phi=((1,1.1),(0.9,1))`，来源是人工固定pGDP参考比`1:2`，不是2018真实数据，不在宏观求根内反复重算。旧MATLAB计算公式差值方向与论文反向，不照搬。V009已提交原blocked工程候选`18256cd70b827e133e52d7609746c8afadb63ac1`，科学HJB/KFE/宏观0次；pytest已用4/8，续跑不重置。旧科研/安全保护和V1.2工作流持续有效。

## 2026-10-15 Owner长期规则与最新科研路线（覆盖本文旧迁移时态，不覆盖科学原证）

Owner明确委托：在Codex交付并完成Astra独立验收、版本归档之后，若没有新的工作流修改/重大科学或数据授权选择，则**直接顺序立下一科研长版本**；不要每版再次询问“是否继续”。任何**工作流变更**需`STOP_AND_NOTIFY_OWNER__WORKFLOW_CHANGE_REQUIRED`，先告知Owner；经同意后让Codex在安全隔离位置同步权威文档和本地研究知识并回读，不能覆盖原8个dirty文件或未核的QMD/BasicMemory。持续有效的准确Owner授权见 [版本推进长期指令](../CH5_OWNER_CONTINUOUS_VERSION_DIRECTIVE_20261015.md)；[现行V1.2工作流](../CH5_ASTRA_WORKFLOW_CURRENT.md)新增限域Owner例外，而不是自动获取受保护数据/科学调用权限。

2026-10-15 V0.0.8已受限接受：新的corrected CES劳动—综合工资对偶/全国单次工资税/统一财政人工账，在1/2/31个**人工省份**给定两资产和家庭分布下取得条件稳态；四条单省外生AR(1)逐期静态响应数值可复算但绝非正式HANK IRF，Gate D`IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE`，Results FALSE。已接受新代码候选`d41d229b681e09b913c21deff7a057085b9bc419`、tree`88833acf90613380afa30ab8d6ee7e0297e98664`。Owner本轮已授权顺序启动V0.0.9，重点是**完整合成两资产HANK家庭最优化/HJB、前向KFE/资产/财政与动态IRF真实科学方程闭合**，先Codex SOURCE_ONLY集中方案，实际数值新许可为0；以[CURRENT](../../CURRENT.md)为当轮状态权威。原C8 A–D真实文件仅REQUEST_ONLY，A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED/CALL_LEDGER_UNRESOLVED及旧封闭预算不变。

2026-10-12迁移安全正文；复用本轮前已完成知识归档，不重新总结全部sessions。原本地导航、CH5_RECOVERED_KNOWLEDGE和CH5_ARCHIVE_20261012保留在唯一代码树docs/knowledge；含私有日志定位/本机细节，标LOCAL_ONLY，未作为完整外发正文。本页给网页端可用内容和覆盖边界。

## 决定及来源
2026-09-29原Owner讨论先尝试户均，随后10:02:45 UTC明确：“现在我们封存户均这个思路，把稿件改回人均（不然前期的程序参数校准部分又要重来了）。”10:13:53 UTC补充人均劳动与人均资产/收入对应，家庭不是严格三个人。原会话01a0ec2a-e8de-71d1-aa90-e7990e45276c，本地原user行538、626在已完成归档中核出，原日志LOCAL_ONLY。人口/人均方向保持、户均封存，不N=P/3，不再重问人或户。
[劳动历史安全正文](published/CH5_LABOR_UNIT_HISTORY_AND_EVIDENCE_20261010_145723Z.md)区分人口对象与百人尺度。NU_100_PERSONS/MU_10WAN_YUAN是历史源码/外会话报告，不是本次运行核验；劳动人数/工时/效率单位、完整N缩放、真实人均分母、时点与firm可比性仍未知。firm Lt称“模型生产端劳动投入”，不能提前认效率劳动。

## 当前已报告接受与未闭链
[进度快照](published/CH5_WORK_PROGRESS_FLOW_MANUAL_HANDOFF_20261011_140603Z.md)及[验收账](published/CH5_WORK_ACCEPTANCE_LEDGER_MANUAL_HANDOFF_20261011_140603Z.md)保留10月11日证据账。迁移只核其已存在内容，不新读源码/跑测试，不追认旧失败。
HA局部sum(z*l*g*db*da)；corrected adapter局部归约及optional frozen投影；batch schema；外部callback/batch消费与firm局部接线已在交接中报告接受，SOURCE_ONLY/CACHED/DOCUMENT_ONLY范围分开。部分劳动候选本身仍写WORK_REVIEW_PENDING，其接受仅Work交接报告，本轮未核原接受工具回执。
实际solver输出→外部数组来源、聚合及frozen实际调用、frozen标量→batch构造、callback真实装配、量纲/人口分母/时点及科学运行仍未闭。局部接受不能拼成完整actualroute/runtime/science接受。
最新ACCEPT/CLOSED仅scripts/tools直接Python文件metadata门：13文件、名称候选binding脚本15010bytes。末binding门原turn completed308677/600000ms未超时，完整交付缺失及contextCompaction后final失配，DELIVERY_INCOMPLETE / NOT_ACCEPTED / CLOSED；prepared不等于disk，不补交不补跑。
fiveFalse、ResultsFALSE、C9PAUSED、windowUNACCEPTED、CALL_LEDGER_UNRESOLVED、C8/RCOTUNKNOWN、A16allUNRESOLVED__FAIL_CLOSED、normalinitNOT_READY-NOT_RUN、science/economics/algorithm/convergence/guardsNOT_CHECKED及production未接受保持。

## 归档、恢复测试与缺口
已有归档实际验证四类问题：人口/户均决定、Python检测与要求、完整劳动桥、末binding门拒绝原因；QMD关键词检索并回读对应正文，Basic Memory显式本地项目检索/笔记读回。它证明有限检索可找回，不证明科学正确或全历史覆盖。
Owner在本次迁移指令补充：已完成无交接新会话恢复测试。记为OWNER_REPORTED_COMPLETED，具体测试时间、会话ID和逐字回答未提供，不补造，不升为本轮独立验收。此前归档只称尚未完成独立新会话验证的截点陈述保留，以此补充更新。
归档未覆盖archived_sessions、其他历史Work独立日志、未落地网页会话；recall无已有数据库，未建全局索引。原user来源由已定位日志核出，不称recall成功搜索全部历史。
Basic Memory本地项目与QMD named index均ch5-two-asset-hank-knowledge，QMD collection ch5-knowledge，显式路由；共享默认项目曾变化，原因未独立归因。网页不能调用这些本地工具。
历史检测Python3.11.9；pyproject要求>=3.11、numpy>=2.0、scipy>=1.14；包安装版本与科学运行解释器未核。本轮没有重新检测/运行，不能把配置要求当环境通过。

## Sources正文与历史
五份旧Markdown在[project-sources](project-sources/DISSERTATION_KNOWLEDGE_BASE_CURRENT.md)以历史快照复用：知识库资格、研究改写结构、旧治理、历史证据索引及旧替换清单。旧状态、旧Work角色和任务授权被当前[新工作流](../CH5_ASTRA_WORKFLOW_CURRENT.md)替代，科学定义/证据限制保留。
论文PDF和MATLAB ZIP仍在项目Sources，可能含唯一全文；本轮不上传二进制、不据存在认全文已核。旧24项本地备份仅历史清单声称存在，本轮未打开或核存，LOCAL_ONLY；需要未覆盖原材料由Owner人工提供脱敏片段/提交快照。
隔离第五章、DeepLearning-HANK、EliteSync/v10，其他项目决定不代入。敏感数据、凭据、私有日志、环境本地细节留本地；GitHub正文不是全部本地成果自动同步。
