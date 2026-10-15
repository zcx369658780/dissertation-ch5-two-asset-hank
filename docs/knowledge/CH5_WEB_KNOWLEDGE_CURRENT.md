# 第五章长期知识与恢复入口

更新：2026-10-15，Owner确认[主线纠偏](../CH5_OWNER_SCOPE_REALIGNMENT_20261015.md)。
**优先记忆：本项目当前是修正原MATLAB错误并Python重写第五章，不是从零另建HANK模型或替换用户半年多形成的求解方法。**

## 必须跨会话保留的科研定位

省级HANK_2ASSETS_HJB作为非线性条件稳态HA黑箱，在合适的价格、资产域和省级参数下产生消费/储蓄/劳动、平稳分布及已有不平等统计。多省外层按HANK_mp_1turn/HANK_mp_1eq顺序更新劳动/资本/企业/工资/货币财政，采用明确边界和GovInv/Zt自适应校准求系统稳态，再从该基点生成原递推地区冲击响应。

黑箱接口不豁免HJB/KFE内部验证；原MATLAB/论文可能含错，目标是修复具体错误并保持总体方法。源忠实parity与经济正确性分账，但不得以“更标准的HANK”为由默认替换整套迭代、债券制度或动态方法。

不默认使用Newton/fsolve宏观联合根、不强加Bt=Bgov或内生财政T，不把竞争性人工模型、人工资产域/校准或完整前瞻动态路径当作主线先决条件。V008/V009辅助人工代码、实验和失败仍保留、不删除；不自动作为主线基线。旧V010 Newton/a=0调查停用。

Owner确认人口/人均，不N=P/3；保留max_phi=0.3及来源减目的的人均GDP偏好方向。人工两省phi=((1,1.1),(.9,1))只在其已冻结人工例子适用，不能代替现实31省输入。

## 需要保留而不擅自化解的历史冲突

原GovInv收益边界调节与后来C1残差律不同；raw-ra0/used回报、Lt时序、税基、AtTax/Tt人口单位等需最小集中对照。恢复主线不等于自动撤销所有HJB/KFE、K1/C1接受或复制旧bug。旧科学冻结、失败与预算在原范围保留。不得再以人工A=0或Newton失败推翻原方法。

## 当前接续方式

先读CURRENT、TASK_CURRENT、主线纠偏决定和修订路线图。当前V010_RESCOPE_DRAFT，**仅Codex文档同步一次**；同步回执未获Astra核验前不执行科研、读失败数组或自动立下一版。Owner连续版本委托仍在，但本轮明确先同步再继续。

[同步任务](../../versions/0.0.10/owner_scope_document_sync.md)同步本页、路线图、科学索引和当前任务到隔离文档镜像，并保存本地ACK。网页不能声称QMD/Basic Memory/ChatGPT账户记忆已经更新。历史本地知识项目名ch5-two-asset-hank-knowledge、QMD collection ch5-knowledge仅作原有定位线索；本轮无写入它们的权限。

## 历史来源与保护

纠偏前本页全文固定在commit db2c2e289419ecab7921667e210bd510ff3c447b同路径，blob 695a75fd4e6b3e557d105dfb438042c0fed6e207；V005—V009历史与各受信来源均保留。本页不追改旧科学验收或本地原日志。

原论文PDF/MATLAB ZIP为Owner辅助源，不能把存在、OCR或记忆摘要冒称逐式独立核验。其他项目DeepLearning-HANK、EliteSync、Zotero独立仓库不混入本模型。原dirty/index/untracked/ignored及B3不覆盖/清理；真实C8 A–D REQUEST_ONLY，A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE和旧预算继续保持。
