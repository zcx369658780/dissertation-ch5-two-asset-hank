# 第五章科学决定：当前适用范围与历史合同索引

> **2026-10-16 会话交接时态补充（不修改Owner历史科学裁决）**：本文2026-10-15“当前允许V010受界实施/合成科学”的表述仅指原冻结签发时的历史许可，**不能作为实时调用授权**。截至最新[2026-10-16交接](docs/CH5_CONVERSATION_HANDOFF_20261016_V010_RUNNER_IO_OFFLINE_PENDING.md)，V010唯一ACTIVE是已发布的纯离线`V010_RUNNER_GUARD_IO_OFFLINE_INTEGRATION_AND_SANITIZED_GITHUB_HANDOFF`（commit `50fece7d51bbcbb7e4384b0a5a8833b81dcbf76b`、task blob `0070437d83eccaaf4a1c38838e9ce2b1a2fb5634`），**新Python/HJB/KFE/HA/pytest/macro/IRF权限全部0**。原单点两次预检进程各1/1已耗、HA各0；任何补充数值许可须Owner再次明确批准。以下经济方程决定、GovInv边界和各原冻结科学门不变。


更新：2026-10-15，Owner已确认[项目主线纠偏](docs/CH5_OWNER_SCOPE_REALIGNMENT_20261015.md)。
**2026-10-15 Owner GovInv/目的地工资税裁决已纳入V010正式冻结实施合同。当前仅允许该版独立候选白名单修改与明确受界synthetic调用（其授权细节必须以固定plan及准确implementation_task双重身份为准）；不放开真实C8/2017/2018/B3、生产激活、Results或旧预算。**

**最新科学裁决：**[V010冻结前审议](versions/0.0.10/prefreeze_scientific_review_20261015.md)：GovInv按收益边界0.9/1.1、C1仅历史有效；目的地工资税只扣一次，AtTax/Tt按对应N桥接、GovSurplus只诊断。新增门包含家庭-企业劳动一致性、冻结后目标GDP误差≤1%以及冲击lagged-NKPC原分支。冻结合同见 [V010 plan](versions/0.0.10/plan.md)（commit `bf091da33d59293f147d52c11580327d3ac2a85d`，blob `85138d8859d53295262fe13bf5bc277bca95ed3f`），仅由 [当前实施task](versions/0.0.10/implementation_task.md)授权两省synthetic；真实数据和论文结果仍禁。

## 当前最高项目目的

修正原MATLAB的实际错误，在原HA条件黑箱＋有界多省份顺序迭代＋GovInv/Zt自适应校准＋原递推冲击响应架构上Python重写第五章。不能把新的联合价格Newton/fsolve系统、Bt=Bgov、内生财政T或竞争性人工模型作为该主线的默认替代。

原方法各层的具体实现需要验证和修复，不因原MATLAB含错就重建整个宏观闭合，也不因source-faithful parity就宣称经济正确。

## 原科学决定分账，不一键回滚

| 对象 | 当前处理 |
|---|---|
| HJB/KFE、状态顺序、质量聚合与数学修复 | 原接受的具体性质按原合同适用；HA黑箱仍须内部有效性。主线复用时只核必要输入与接口兼容，不重新发明家庭模块。 |
| 人口/人均 | 保留，不N=P/3；家庭平均量、地区总量与生产劳动不可混称。 |
| 劳动偏好phi | 保留max_phi=.3及来源减目的的人均GDP相对差方向；人工1:2参考比不是现实31省输入。 |
| 资本数量与回报 | 同一S、raw-ra0/lagged等保留原范围；本轮不运行或静默回滚。 |
| GovInv/C1 | Owner已裁决：新主线采用原ra边界GovInv乘数0.9/1.1；C1残差律保留历史验收和代码，但不参与主线或覆盖GovInv。校准触发/停止和目标验证依最新审议。 |
| Zt/GovInv校准 | 原自适应更新是主线方法；须界定触发、目标、退出及稳态/冲击阶段角色，合法校准不一概等同事后调参保PASS。 |
| Lt/Tt/AtTax/工资税等 | 工资税按工作目的地征收，净综合工资在HA只扣一次；工资税基匹配目的地工资×firm劳动；来源家庭AtTax/Tt按N桥接总量。家庭与firm劳动的完整异质性一致性仍待验证，不增加新财政债券根。 |
| 固定C8 Option1与旧R2/C9 | 限历史诊断/结果/预算，不代替全项目目标，也不因主线恢复而解锁。 |
| 原递推冲击 | 是第五章研究目标；说明时间/预期/状态和解释范围，前瞻动态重构另属扩展，不是默认前置。 |

## 辅助分支与历史索引

V008/V009人工CES/全国债券/内生T/竞争企业/人工校准/Newton实验的批准和结果只在原范围内有效，现为非活跃辅助研究。保留全部证据，不删除、不追改验收，不把人工At=0或未接受trial失败当原方法无稳态的证据。旧V010 Newton取证任务停止；主线正式实施代码父固定为 `a1db8c114dec0ab69d69a5576e153a7f868cba0e`（不等于已验收数值GE）。

纠偏前完整科学决定原blob 93f0ac784919482701417b507a1ec1b7c9ebcf9b原样保存于[历史索引](docs/history/scope_realignment_20261015/SCIENTIFIC_DECISIONS_BEFORE.md)，原相对链接在固定commit db2c2e289419ecab7921667e210bd510ff3c447b原SCIENTIFIC_DECISIONS.md读取。各版本正式冻结、Owner采纳、验收原件未修改。

直接方法证据：docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_SOURCE_AUDIT_AND_CONTRACT_FREEZE_REPORT.md和博士论文5.2.7/5.3。旧审计的MATLAB数值权威措辞只表达过去重现任务范围，不取消Owner修错要求。

A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、direct_price_verified=False、真实C8 A–D REQUEST_ONLY及旧已耗预算不变。原SOURCE_ONLY审议已完成；正式新授权仅限V010的synthetic与白名单，旧禁令在所有未列对象上保持。
