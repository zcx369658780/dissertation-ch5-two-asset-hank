# 第五章长期知识与恢复入口

更新：2026-10-15，Owner确认[主线纠偏](../CH5_OWNER_SCOPE_REALIGNMENT_20261015.md)。
**最高项目定位：修正原MATLAB错误并Python重写第五章，不是从零另建HANK，不能替换Owner半年多形成的总体求解方法。**

## 2026-10-16 新会话V010 runner IO静态验收（当前优先）

GitHub review候选 `c207e866cf70d9d5ae6fb245f43cabfdeac1d32b` / tree `b4ba5b7939653a0cdb8524fa82743d9634d79083` 已交付。 [新会话独立审议](../../versions/0.0.10/runner_guard_io_offline_github_primary_review_20261016.md) 仅有限接受静态设计，46机读主例及23变体均NOT_RUN；真实Windows I/O、旧audit argv、单点corrected HA均未运行。`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`model_activation=False`、`Results FALSE`、`V011 NOT_STARTED`。旧任务不重发、冻结科学不改、全部旧超额/预算保留。下一停点 `WAIT_OWNER_V010_ENGINEERING_ONLY_PREFLIGHT_DECISION / STOP`，未来工程与科学进程分别申请权限。以下“未收到Codex交付”文字为2026-10-16交接写入时点，不是当前实时结论。

## 2026-10-16 会话交接时恢复入口（现由上方新会话审议更新）

[本轮完整GitHub交接](../CH5_CONVERSATION_HANDOFF_20261016_V010_RUNNER_IO_OFFLINE_PENDING.md)。唯一ACTIVE `V010_RUNNER_GUARD_IO_OFFLINE_INTEGRATION_AND_SANITIZED_GITHUB_HANDOFF`，固定任务commit `50fece7d51bbcbb7e4384b0a5a8833b81dcbf76b`、blob `0070437d83eccaaf4a1c38838e9ce2b1a2fb5634`；离线静态runner/IO整合中、未收到Codex交付。只能安全去敏的新GitHub独立review分支，`Python/pytest/HA/HJB/KFE/GE/IRF=0新许可`。

V010代码candidate `94de4501dec051b969bee9d852eba2d4591f30ef`已工程限域接受，首synthetic HA checkpoint2 F-order25有`NO_ADMISSIBLE_POLICY`失败，单点`(.0675,15.5,.02)`的corrected HA仍`UNTESTED`。两个后续probe均预检退出，各Python进程1/1、HA0；首次GBK日志`43,519,638B`超32MiB `9,965,206B`，第二Windows argv守门故障artifact117,446B在96MiB内。Owner上传MD/py已独立静态审查，`identity_outputs`输出绑定、磁盘source、PIPE、I/O配额/audit仍`BLOCKED`；真实argv未捕获、24静态预期不是运行PASS。第三个Python/HA须Owner未来独立授权，最好先engineer-only Windows preflight再科学HA。原安全门和冻结计划始终不变。V011 NOT_STARTED、Results FALSE、model_activation=False。



## 必须跨会话保持

省级HANK_2ASSETS_HJB是非线性条件稳态HA黑箱：给定合适价格、资产域和省级参数，求居民消费/储蓄/劳动和分布统计。多省外层按HANK_mp_1turn/HANK_mp_1eq顺序更新劳动/资本/企业/工资/货币财政，采用原有边界与GovInv/Zt自适应校准寻找整体稳态，再从基点产生原递推地区冲击。

黑箱不豁免HJB/KFE验证，原MATLAB和论文可能含bug；应修具体错误并保留架构，不以“更标准HANK”为由改为Newton/fsolve、固定Bg/Bt=Bgov、内生T、竞争性人工经济或全新前瞻动态模型。原source-faithful复现与经济正确性分别审查。V008/V009人工实验与失败为非活跃辅助，保留、不删除、不自动当主线父基线；旧V010 Newton/a=0取证已停用。

人口/人均、不N=P/3、max_phi=.3及来源减目的的人均GDP偏好方向保持。原人工pgdp1:2与两省矩阵不是现实31省校准。Owner已于2026-10-15决定新主线GovInv使用原收益边界乘0.9/1.1，C1历史效力保留但不参与新求解；工资税由工作目的地征收、家庭只扣一次，来源家庭AtTax/Tt经N桥接财政总量。raw/used和same-S/lagged严格分账，家庭Lt与firm目的地Lt不可覆盖混用。

## 2026-10-15 历史恢复阶段（已过期，不再作为当前任务）

Owner要求的一次16文档同步已由Astra[限定验收](../../versions/0.0.10/scope_sync_acceptance.md)。GitHub固定源916e2b47d3489f6eacd814b55cc568d92be4c9fb已独立核；本地raw MATCH、Scope ACK、保护与4.8分钟/212234B等为Codex回执等级，不是网页执行。dirty/index未字节hash、其它会话未核；QMD/BasicMemory均NOT_UPDATED。

V010 [SOURCE_ONLY方案](../../versions/0.0.10/mainline_alignment_task.md)已有限接受；[正式冻结计划](../../versions/0.0.10/plan.md)固定commit `bf091da33d59293f147d52c11580327d3ac2a85d`、plan blob `85138d8859d53295262fe13bf5bc277bca95ed3f`。唯一ACTIVE为[集中实施](../../versions/0.0.10/implementation_task.md)，仅在不共享common-dir的独立clone中修改15条白名单，有限两省人工HJB/KFE、稳态和3期短响应；真实31省/C8/Results仍禁，不能自动V011。

旧16文档本地镜像和收据原样保留；新任务按正式冻结commit/fixture blob读取，不覆盖原模型AGENTS/CURRENT/dirty或镜像。网页不能自动写本地知识库，历史QMD collection ch5-knowledge及Basic Memory项目ch5-two-asset-hank-knowledge只作定位线索，本轮不写。

## 历史与保护

纠偏前知识全文固定于db2c2e289419ecab7921667e210bd510ff3c447b同路径，纠偏同步快照在916e2b47d3489f6eacd814b55cc568d92be4c9fb。各版科学冻结和接受/失败原件不改。

原D盘8 dirty、index、untracked/ignored、外部.git及B3不覆盖清理；A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE及真实C8 A–D REQUEST_ONLY/旧预算保持。项目原PDF/ZIP仅辅助来源，不跨入DeepLearning-HANK、EliteSync或其它仓库。V1.2及Owner连续推进委托不变。


## 旧会话边界归档：2026-10-15（已被2026-10-16交接替代）

Owner已要求先在GitHub保存本次Owner决策、V010 task和科学范围，并把**同V010最新已发表的SOURCE_ONLY结果验收**留到新会话。 [交接快照](../CH5_CONVERSATION_HANDOFF_20261015_V010_MAINLINE_PENDING_REVIEW.md)。其固定发行commit `0320916bd2447d1846099cc90e52bd92c920ebb1`、task blob `d4aacdafe5f4d0248745f8754088afd83fc1c6d2`未改，直到Codex交付前不能宣称结果已审。首要保护是“修错原MATLAB、保留HA黑箱/有界多省GovInv-Zt/原递推IRF”；不继续人工Newton支线，不替Owner决定GovInv/C1，不凭同步或代码提交开放现实GE、IRF、Results。所有个人QMD/Basic Memory仍NOT_UPDATED，本次只在仓库文档中保存。
