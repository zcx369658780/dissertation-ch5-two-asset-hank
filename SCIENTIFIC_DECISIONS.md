# 第五章科学决定：当前适用范围与历史合同索引

更新：2026-10-15，Owner已确认[项目主线纠偏](docs/CH5_OWNER_SCOPE_REALIGNMENT_20261015.md)。
**纠偏文档同步及V010 SOURCE_ONLY方案均已限定接受；Owner 2026-10-15 已作出GovInv与目的地工资税科学裁决；当前实施合同仍待正式冻结。本索引不发放代码实施、科学运行、参数修改或真实数据权限。**

**最新科学裁决：**[V010冻结前审议](versions/0.0.10/prefreeze_scientific_review_20261015.md)：GovInv按收益边界0.9/1.1、C1仅历史有效；目的地工资税只扣一次，AtTax/Tt按对应N桥接、GovSurplus只诊断。新增门包含家庭-企业劳动一致性、冻结后目标GDP误差≤1%以及冲击lagged-NKPC原分支。未经正式冻结不授权实施。

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

V008/V009人工CES/全国债券/内生T/竞争企业/人工校准/Newton实验的批准和结果只在原范围内有效，现为非活跃辅助研究。保留全部证据，不删除、不追改验收，不把人工At=0或未接受trial失败当原方法无稳态的证据。旧V010 Newton取证任务停止；主线代码baseline未选择。

纠偏前完整科学决定原blob 93f0ac784919482701417b507a1ec1b7c9ebcf9b原样保存于[历史索引](docs/history/scope_realignment_20261015/SCIENTIFIC_DECISIONS_BEFORE.md)，原相对链接在固定commit db2c2e289419ecab7921667e210bd510ff3c447b原SCIENTIFIC_DECISIONS.md读取。各版本正式冻结、Owner采纳、验收原件未修改。

直接方法证据：docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_SOURCE_AUDIT_AND_CONTRACT_FREEZE_REPORT.md和博士论文5.2.7/5.3。旧审计的MATLAB数值权威措辞只表达过去重现任务范围，不取消Owner修错要求。

A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、direct_price_verified=False、真实C8 A–D REQUEST_ONLY及旧已耗预算不变。只读源码方案完成后仍须正式冻结与独立授权才可实施。
