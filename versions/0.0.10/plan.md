# V0.0.10 修订DRAFT：回归原MATLAB有界多省份迭代的修错与Python重写

日期：2026-10-15（Asia/Shanghai）。
**状态：V010_RESCOPED_DRAFT__WAIT_CODEX_DOCUMENT_SYNC__RESEARCH_HOLD。**
**本次唯一允许任务：owner_scope_document_sync.md规定的一次文档同步。以下科研内容是待后续集中落实的范围，不是现在的SOURCE_ONLY、源码读取、测试或运行许可。**

## 1. 替代旧版前任务

Owner确认原项目目的并要求先同步再继续。原V010 DRAFT在commit db2c2e289419ecab7921667e210bd510ff3c447b，blob eae74d9db34b319544ec32cd1c7b71325db6e650，任务名V0.0.10_M2_V009_PRIVATE_CAPITAL_ZERO_SUPPORT_AND_NEWTON_TRIAL_FAIL_CLOSED_FORENSIC。它尚未成为正式科学冻结合同；本次明确将其后续执行指示置为SUPERSEDED_BY_OWNER_SCOPE_REALIGNMENT，不继续Newton/Jacobian/a=0取证、不再读取为其指定的V009私有失败数组。

已经发生的工作如有，保留事实、调用账和文件，不反称NOT_RUN；执行状态由Codex在同步回执中报告。没有新版本号或额外微版本，仍在V010中恢复主线。

## 2. 同步后的版本目标（待Astra另发实际任务）

围绕原HA黑箱—单轮映射—有界外层校准这条链，完成一次集中、具体的Python修错与接续方案，优先推进已有源代码而不是新人工模型：

A. 精确确定原MATLAB参考、已接受的source-faithful Python及后来数值修复的真实关系。不得默认以reconciled_hank人工Newton候选为父基线，也不自动切换原脏工作树。主线代码baseline目前UNSELECTED。

B. 对齐HA输入输出合同：资产上下界、rb/rah/w/tau/Tt/本省参数 → Ct/At/Bt/Lt、政策与稳态分布及已有统计。复用已接受HJB/KFE数学修复；只针对可核缺陷修复，不另造家庭宏观闭合。

C. 对齐原单轮和外层更新：HA → 迁移劳动 → 私人资本及收益 → 企业 → 综合工资/货币财政 → 下一轮；明确GovInv/Zt调节、边界、阻尼、退出条件和数据校准身份。合法校准更新与事后篡改标准严格区分。

D. 仅列阻碍该闭环的最小修错集：phi差值/轴与人均口径、劳动变量生命周期、资本份额与收益、税和财政单位等。每项写“源码证据、错误性质、最小修复、会否改变Owner已采纳法则、同输入验证办法”。不因发现财政歧义就预设全国债券供给根、内生T或竞争性新企业。

E. 为之后的原方法稳态及递推冲击建立可核验路径；不把前瞻动态重构作为本版主目标或先决条件。

本版应争取一个完整科研长任务，不变成逐文件微审批。具体允许路径、试验输入和数值预算必须在同步回执接受后，基于真实源状态集中冻结；本文不预造数据、校准、可用代码SHA或求解权限。

## 3. 必须集中处理而不能擅自决定的兼容性问题

- 原GovInv根据收益边界调节，后来C1为GovInv=max(Ktarget-Kprivate,0)。两者不是同一迭代映射。本轮恢复原方法优先级，但不取消C1历史接受；实际新主线更新法待对照原件后集中确认。
- 原价格有界与后来raw-ra0/lagged回报修复，须区分raw、used、触边标志、条件HA输入和外层退出，不自动clip或回滚。
- 已采纳人口/人均、不N=P/3及max_phi=0.3的富裕目的地偏好方向保留；人工两省pGDP比1:2不是现实31省校准。
- 原借贷域、税/转移含义与合成试验的b>=0、Bt=Bgov、内生T不同；不把后者带回原模型。
- 旧论文和MATLAB都可能含错。数值复现与经济正确性分账，必要的会计检查继续存在，但不得以重建另一套总均衡为默认修复方式。

## 4. 本轮权限与退出

当前科研许可全部为0：不读模型源码/旧科研数组以继续取证，不import研究包、不运行HJB/KFE/selector/宏观迭代/Newton/IRF/pytest/MATLAB，不改变参数或网格，不建立代码候选、不push或合并main。

只执行[文档同步](owner_scope_document_sync.md)：读取本次固定治理快照，保存到独立新文档目录，核每文件身份，明确旧任务停用和主线范围，提交同步回执后STOP。

同步完成并经Astra核验之前，不能以Owner连续立版委托或此计划中的“同步后目标”自动开始科研。同步接受后Astra再发布同V010的具体任务；必要的科学方向冲突仍由Owner决定。V011 NOT_STARTED。

A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE以及真实C8 A–D REQUEST_ONLY和旧已耗预算维持原状。原8 dirty/外部common-dir/untracked/ignored/B3不覆盖、不清理；原V008/V009辅助成果不删除。
