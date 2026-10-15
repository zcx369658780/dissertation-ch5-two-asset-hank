# 第五章长期知识与恢复入口

更新：2026-10-15，Owner确认[主线纠偏](../CH5_OWNER_SCOPE_REALIGNMENT_20261015.md)。
**最高项目定位：修正原MATLAB错误并Python重写第五章，不是从零另建HANK，不能替换Owner半年多形成的总体求解方法。**

## 必须跨会话保持

省级HANK_2ASSETS_HJB是非线性条件稳态HA黑箱：给定合适价格、资产域和省级参数，求居民消费/储蓄/劳动和分布统计。多省外层按HANK_mp_1turn/HANK_mp_1eq顺序更新劳动/资本/企业/工资/货币财政，采用原有边界与GovInv/Zt自适应校准寻找整体稳态，再从基点产生原递推地区冲击。

黑箱不豁免HJB/KFE验证，原MATLAB和论文可能含bug；应修具体错误并保留架构，不以“更标准HANK”为由改为Newton/fsolve、固定Bg/Bt=Bgov、内生T、竞争性人工经济或全新前瞻动态模型。原source-faithful复现与经济正确性分别审查。V008/V009人工实验与失败为非活跃辅助，保留、不删除、不自动当主线父基线；旧V010 Newton/a=0取证已停用。

人口/人均、不N=P/3、max_phi=.3及来源减目的的人均GDP偏好方向保持。原人工pgdp1:2与两省矩阵不是现实31省校准。原GovInv收益边界更新与后来C1残差律、raw/used、Lt/Tt/AtTax/税与资本接口的差异需要集中最小核查，不一键撤销旧科学修复，也不把旧C1强迫当恢复后主线唯一规则。

## 当前恢复阶段

Owner要求的一次16文档同步已由Astra[限定验收](../../versions/0.0.10/scope_sync_acceptance.md)。GitHub固定源916e2b47d3489f6eacd814b55cc568d92be4c9fb已独立核；本地raw MATCH、Scope ACK、保护与4.8分钟/212234B等为Codex回执等级，不是网页执行。dirty/index未字节hash、其它会话未核；QMD/BasicMemory均NOT_UPDATED。

接下来只执行[同V010主线源码方案任务](../../versions/0.0.10/mainline_alignment_task.md)，不是再次同步或新的版本：确认原MATLAB/source-faithful Python实际baseline、HA—单轮—外层—冲击接口与最小bug/科学冲突，交付一个可直接冻结的实施方案。当前无模型、测试、代码改动或真实数据权限。人工失败源调查不恢复。

旧16文档本地镜像和收据原样保留；新任务按本轮新固定Git身份读取，不覆盖原模型AGENTS/CURRENT/dirty或镜像。网页不能自动写本地知识库，历史QMD collection ch5-knowledge及Basic Memory项目ch5-two-asset-hank-knowledge只作定位线索，本轮不写。

## 历史与保护

纠偏前知识全文固定于db2c2e289419ecab7921667e210bd510ff3c447b同路径，纠偏同步快照在916e2b47d3489f6eacd814b55cc568d92be4c9fb。各版科学冻结和接受/失败原件不改。

原D盘8 dirty、index、untracked/ignored、外部.git及B3不覆盖清理；A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE及真实C8 A–D REQUEST_ONLY/旧预算保持。项目原PDF/ZIP仅辅助来源，不跨入DeepLearning-HANK、EliteSync或其它仓库。V1.2及Owner连续推进委托不变。


## 会话边界：2026-10-15 下一会话验收而非重复规划

Owner已要求先在GitHub保存本次Owner决策、V010 task和科学范围，并把**同V010最新已发表的SOURCE_ONLY结果验收**留到新会话。 [交接快照](../CH5_CONVERSATION_HANDOFF_20261015_V010_MAINLINE_PENDING_REVIEW.md)。其固定发行commit `0320916bd2447d1846099cc90e52bd92c920ebb1`、task blob `d4aacdafe5f4d0248745f8754088afd83fc1c6d2`未改，直到Codex交付前不能宣称结果已审。首要保护是“修错原MATLAB、保留HA黑箱/有界多省GovInv-Zt/原递推IRF”；不继续人工Newton支线，不替Owner决定GovInv/C1，不凭同步或代码提交开放现实GE、IRF、Results。所有个人QMD/Basic Memory仍NOT_UPDATED，本次只在仓库文档中保存。
