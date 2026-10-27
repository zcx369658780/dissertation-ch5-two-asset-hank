# 第五章 GPT 顾问 · 2026-10-27 会话正式交接（GitHub 治理权威）

STATUS=SESSION_HANDOFF_DOCUMENTED__NO_NEW_TASK_ISSUED
DATE=2026-10-27
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
HANDOFF_SOURCE_GOVERNANCE_COMMIT=7a42502946117862df021a9ec0a3909b1d77a8b1
LAST_ISSUED_TASK=CH5_TEMP31_WAGE_LABOR_TAX_SEMANTICS_STATIC_AUDIT_R1_20261027
LAST_ISSUED_TASK_COMMIT=a4476b1873b0950cf4fbd3d10122de41cd981dec
LAST_TASK_CANDIDATE_COMMIT=9bdc9e83127d32e6e29a0a5895800fd97d92cd3a
LAST_TASK_VERDICT=PASS_BOUNDED_STATIC_SOURCE_SEMANTICS__SCIENTIFIC_ACCEPTANCE_BLOCKED
ACTIVE_TASK=NONE
NEXT=OWNER_SCIENTIFIC_DECISION__DO_NOT_RERUN_LAST_TASK
AUTO_NEXT=FALSE

## 0. 最高优先级：真实 GitHub 状态高于旧会话最后一条消息

本会话上一次用户可见交付仅说“静态口径审计任务已签发/等待 Codex”，但在本次交接前直接回读 GitHub 治理分支，发现该任务已经有候选提交、独立有界验收与治理状态更新。

真实最新状态：
- 已签发的任务单：`tasks/CH5_TEMP31_WAGE_LABOR_TAX_SEMANTICS_STATIC_AUDIT_R1_20261027.md`，源提交 `a4476b1873b0950cf4fbd3d10122de41cd981dec`。
- Codex 候选：`9bdc9e83127d32e6e29a0a5895800fd97d92cd3a`，对应任务证据目录 `tasks/CH5_TEMP31_WAGE_LABOR_TAX_SEMANTICS_STATIC_AUDIT_R1_20261027/`。
- GPT 独立验收历史提交：`4699787ea100310ce09d20833fe25aa321bae200`（临时验收文件已从审阅分支当前树移除，Git 历史仍可按 SHA 读取）。
- 治理验收状态提交：`7a42502946117862df021a9ec0a3909b1d77a8b1`，最新 CURRENT/TASK_CURRENT 均记录 `ACTIVE_TASK=NONE`。
- 裁决：`PASS_BOUNDED_STATIC_SOURCE_SEMANTICS__SCIENTIFIC_ACCEPTANCE_BLOCKED`。含义是静态资料审阅的有界完成，绝非正式模型/经济学/数值通过。
- 下个会话不应重发或重跑此任务，除非 Owner 另有新指令。首先阅读固定源证据与待 Owner 决策说明。

## 1. Owner 已明确批准的项目工作流（正式且长期有效）

1. 人工 GitHub 流程：GPT 发布冻结任务单至治理分支；Owner 将任务交本地 Codex；Codex按白名单只在隔离候选分支工作，可用 Owner 已授权的普通权限 SSH key 推送；GPT/Astra 读取固定 commit 的实际源码和证据独立验收；最后 Owner 做经济学、实施、预算或继续/停止决定。
2. GitHub 插件曾连接失败，SSH 曾成功；Codex 推送不依赖插件，但禁止绕过任何权限/认证拒绝、使用未授权账号/凭据或提升权限。
3. 复杂程序项目禁止把离线 ZIP 当常规必需验收载体；以可直接读取的固定 GitHub commit、源码差异、精确原件路径/Blob/来源及必要脱敏短摘录为主。
4. **Owner 最新追加**：所有验收文件必须先上传 GitHub；允许临时审阅目录，GPT 直接回读验证后可仅清理该临时审阅目录当前树文件，Git 历史保留。原科研证据、正式裁决、历史 STOP/PENDING、原始数据和候选交付不得自动删除。
5. 不自动 Issue/PR、不自动合并、不自动清理科研证据、不自动下一任务。每项任务必须唯一冻结源 SHA、写入白名单、预算、STOP 与证据硬门；回读 commit/parent/tree/Blob/字节数/SHA-256。
6. Project Sources、GitHub 治理、Codex 本地工作树为独立平面。Project Sources 已在上一阶段由 Owner 手工替换为治理规则 V3；本轮 GitHub handoff 不代表本地工作区/Project Sources 自动同步。
7. Owner 保留经济学概念、公式修改、真实数据采纳、科研运行预算、正式来源冻结与合并/下一任务的最终决定权。
权威规则：`docs/CH5_GITHUB_WORKFLOW_AUTHORITY_CURRENT_20261025.md`、`docs/CH5_INDEPENDENT_REVIEW_RULES_20261025.md`、`docs/CH5_ASTRA_WORKFLOW_CURRENT.md`。

## 2. Owner 已作出的科学设计决策（不等于生产实现已通过）

- TEMP31 独立于正式 V010/历史主线；工资税按工作地/目的地省份归属；目的地异质税 `tau_j` 在劳动拆分使用目的地索引；同一工资税不得重复扣减，含目的地税的综合净工资送往家户时不能在 HA 消费侧再次扣同一税。
- D1=B：旧期间一致的 batch tuple digest 目标合同；D2：未来显式 31 省 batch adapter；D3=B：真实 HA 前先做 no-HA synthetic spy；三者是批准的设计/验证方向，不代表已获执行预算或实现通过。
- 2026年9月初首次复现MATLAB的历史Python基线是候选修订起点（候选固定提交 `ba98537fd5ae004f0aa37d319865da1f1739e503`）。历史 corrected-2009 的 184 次迭代/5704 家户调用/31省收敛，不证明现今 TEMP31、所有输入接口或正式科学接受。
- 统计工资率不等于HANK净工资或有效劳动工资，不能因Excel字段或省份数匹配就直接使用。

## 3. 2026-10-27 工资数据发现、复制与采纳边界

Owner 多次在国家统计局数据库手动导出工资相关原件并上传；原件由本地 Codex 原字节保存，仅脱敏哈希/回执入 GitHub，未导入模型。
三份本地源候选：
A. 城镇单位就业人员平均工资（元）：`data/external_sources/nbs_provincial_urban_unit_wage_20261027/分省年度数据_城镇单位就业人员平均工资(元).xlsx`；12652 B，SHA-256 `8bb799fc41da5728a52c4958b2da0641ccbc81470a8d6e377625d79b5816b176`。2018年31省非异常值候选；`NONPRIVATE_LIKELY__DEFINITION_PENDING`。
B. 城镇私营单位就业人员平均工资（元）：`data/external_sources/nbs_wage_supplement_20261027/分省年度数据_城镇私营单位就业人员平均工(元).xlsx`；12411 B，SHA-256 `5c790a478a244ca12b4c3c2c682465683c64e2b36bbf1d6f5e430bd79b23f21a`。2018年30省非异常值候选，西藏的字面 `30` 隔离待核。
C. 城镇单位就业人员工资总额（亿元）：`data/external_sources/nbs_wage_supplement_20261027/分省年度数据_城镇单位就业人员工资总额(亿元).xlsx`；13310 B，SHA-256 `f27313c73dc08e8217aeeefe147ce62d7bc0d7c463ecc651c54c7682682c9dc7`。2018年31省非异常值候选，工资总额与平均工资不是同一对象。
各Excel里若干年份大量重复字面 `30`，已按来源回执隔离但其确切编码含义尚未证明；原件不可改零、删除或插值。原始指标 ID、真实导出 URL、导出时间、修订vintage与统一统计口径未完成核证。SOURCE_ROLE=OWNER_DOWNLOADED_NBS_CLAIMED；MODEL_ADOPTED=FALSE。
背景：此前严格2018 O层仅私营3省、非私营4省；后来找到完整性较高的上述原始候选，不得追溯将以前旧O层认定全数通过。
历史2009输入 `calendar_2009_primary_premodel_input.json` 36263 B，SHA-256 `507d1259a8a515e4224f40d434bd89645c02472650b51f5ada3181ba4bcdad48`，三个工资/税变量是共用标量，不是实测31省工资向量。
原始附件没有被上传到GitHub；新会话若要亲自重验本地Excel副本须取得受权可读字节，不能仅凭Codex哈希回执声称独立打开用户Windows磁盘。

## 4. 最新静态语义审阅发现及尚未解决的问题（下个会话的关键议题）

最近静态审阅结果文件：
- `tasks/CH5_TEMP31_WAGE_LABOR_TAX_SEMANTICS_STATIC_AUDIT_R1_20261027/result.md`
- `source_excerpts.json` / `source_inventory.json`（原路径、原公式/源码精确范围与哈希）
- `symbol_semantics_matrix.md`
- `wage_labor_tax_lineage.json`（25条静态有向边）
- `statistics_to_model_bridge_matrix.md`（3份工作簿×9个模型目标=27项；0项已证明直接匹配）
- `owner_decision_brief.md`
- `gap_register.json` 和 `audit_checkpoint.json`。

由上述固定提交报告支持的静态结论：
1. 原论文 c5/MATLAB/当前 Python 之间存在税率原籍/目的地索引差异，证据在综合工资、迁移劳动拆分及初始化/生产调用链。R3局部修改目标地税索引，但现有报告未证明其形成全生产闭包。
2. 已含目的地税楔子的综合工资再次与非零 `tau` 传入 HA 消费者时存在**条件性重复税楔子风险**；未运行模型、不能称作运行时已发生的重复扣税。部分隔离候选将 `tau=0`，但不代表正式修复。
3. 企业 `wjt` 涉及边际产出和目的地劳动，家户 `w` 为跨目的地综合报酬；个体劳动 `l`、分布加权有效劳动、人口 `N` 和目的地 `Lt_supply` 不可混用。
4. 企业综合工资指数中 `alphal` 幂次、`phi` 符号方向、财政工资税基是否缺工资因子、企业税项混合 i/j 下标均存在历史版本/单位或表达式差异，尚待 Owner 科学裁决。不得由执行者自行修公式。
5. 统计工资年均金额、工资总额、模型边际有效劳动工资、综合税后工资在27个对照单元里**没有一项直接科学匹配被证明**。
6. 部分最新 Python 原始字节来自执行者 dirty/untracked 工作树，与同名远端 Blob 不同；静态报告本身有来源引用，但 GPT 尚不能独立读取所有本地未提交原字节，不能把其 PRODUCTION_CALLER 标注升级为正式生产身份验证。
7. 正式生产 `wjt/tau/sigma/phi` 数组/ID映射、callback、同一31省数据快照和模型劳动单位桥仍BLOCKED。

## 5. 最新真实状态及禁止事项

截至本次交接，GitHub治理状态 `ACTIVE_TASK=NONE`，上一任务有界验收后 STOP；`NEXT=OWNER_SCIENTIFIC_DECISION`。没有新的 Codex 科研任务单被批准或签发。
固定保护条件：
`FORMAL_SOURCE_FREEZE=FALSE`
`V010=UNCHANGED`
`V011=NOT_STARTED`
`Results=FALSE`
`model_activation=FALSE`
`REAL_GE=FALSE`
`FULL_RUNNER_IO_CLOSURE=BLOCKED`
`HA_HJB_KFE_GE_IRF=0`（最后静态审阅任务预算）
`AUTO_NEXT=FALSE`
`AUTO_MERGE=FALSE`
`AUTO_CLEANUP=FALSE`

禁止下个会话见到最后任务单就自动让Codex重跑、生成补丁、改公式、插值、运行HA/HJB/KFE/GE/IRF或宣布Results。先复核GitHub固定证据，向Owner提出下一项最小证据或科研选择，等明确授权才发新任务。

## 6. 新会话初始化顺序

1. 连接GitHub仓库 `zcx369658780/dissertation-ch5-two-asset-hank`，**先回读** `migration/astra-workflow-20261012` 的实时 HEAD；确认没有比本handoff更晚的治理提交。
2. 首先阅读本handoff，然后读取 `CURRENT.md` 的最后一段、`TASK_CURRENT.md` 的最后一段、治理V3、`docs/CH5_PROJECT_MEMORY_CURRENT.md` 最新补充；同文件前部历史ACTIVE字段只能当历史。
3. 固定读取候选 `9bdc9e83127d32e6e29a0a5895800fd97d92cd3a` 的 `result.md`、`owner_decision_brief.md`、`gap_register.json`、关键源码摘录/lineage及独立审阅历史 commit，不用重复打包离线ZIP。
4. 给Owner一份简短“已完成/待决策/建议下一步”报告，至少区分事实、静态疑点和未验证闭包；**不要新建任务或执行科研工作**，除非Owner指示。

END_OF_SESSION_HANDOFF__GITHUB_DOCUMENTED__STOP
