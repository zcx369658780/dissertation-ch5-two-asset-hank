# 第五章科学决定：当前适用范围与历史合同索引

更新：2026-10-15，Owner已确认[项目主线纠偏](docs/CH5_OWNER_SCOPE_REALIGNMENT_20261015.md)。
**当前只准文档同步；此索引不发放科学执行、参数修改或数据访问权限。**

## 1. 当前最高项目目的

修正原MATLAB的实际错误，在原HA条件黑箱＋有界多省份顺序迭代＋GovInv/Zt自适应校准＋原递推冲击响应架构上Python重写第五章。不能把新的联合价格Newton/fsolve系统、Bt=Bgov、内生财政T或竞争性人工模型作为该主线的默认替代。

先验证和修复原方法各层的具体实现，不因原MATLAB含错就重建整个宏观闭合，也不因源忠实parity就宣称经济正确。

## 2. 原科学决定分账，不一键回滚

| 对象 | 现行处理 |
|---|---|
| HJB/KFE、状态顺序、质量聚合和数值修复 | 已接受的具体科学性质继续按原合同适用；黑箱接口不取消内部科学验证，具体主线复用须核其经济输入兼容性。 |
| 人口/人均 | 保留，不N=P/3；家庭平均量、地区总量和生产劳动口径不能混称。 |
| 劳动偏好phi | 保留Owner确认的max_phi=0.3与来源减目的的人均GDP相对差方向；原人工1:2参考比不自动成为现实31省数据。 |
| 资本份额与收益 | 同一S的数量/收益一致性、raw-ra0/lagged等保留其原接受范围；本轮不新增或回滚科学计算。 |
| GovInv/C1 | 原按收益边界调节与后来max(Ktarget-Kprivate,0)是不同映射，必须集中核对；本轮恢复原方法主线，不自动改旧C1合同，也不把其残差律强制移入未经核对的原迭代。 |
| Zt及校准 | 原自适应校准是待恢复的主线方法；允许更新的参数、触发规则、数据目标和稳态/冲击阶段的固定条件须事前明确，不能一概禁止校准动作。 |
| Lt/Tt/AtTax/税基等疑点 | 继续按来源和会计证据针对性修错；尚未证实的解释不冒充既定bug，不顺带扩充经济制度。 |
| 固定C8 Option1与历史R2/C9 | 限原历史诊断对象、结果与预算，不当作全项目永久研究定义，也不因纠偏重开。 |
| 旧原递推IRF | 是第五章重现目标；核验其时间、预期、状态和传导假设后限定解释。完整前瞻动态求解另属扩展，不是默认阻塞条件。 |

## 3. 人工支线非活跃化

V008/V009及相关人工CES/全国债券/内生T/竞争企业/固定校准/Newton实验的批准、代码、成功或失败只在原实验范围有效，现不再作为主线必经阶段。保留全部证据，禁止删除或追改验收；不得以其中At=0或试探失败否定原方法，亦不得把人工模型的参数、资产域或代码自动推广为原MATLAB Python目标。

旧V010 Newton取证任务的后续指示已被Owner纠偏覆盖，停止执行。当前重选主线代码基线尚未发生；不自动恢复旧bug或清理任何分支。

## 4. 历史完整索引和准确来源

为避免旧索引中多个“当前”状态被误作执行指令，纠偏前完整科学决定正文保持原blob 93f0ac784919482701417b507a1ec1b7c9ebcf9b，逐字节复制到[历史科学索引](docs/history/scope_realignment_20261015/SCIENTIFIC_DECISIONS_BEFORE.md)。原相对链接应在固定commit db2c2e289419ecab7921667e210bd510ff3c447b的SCIENTIFIC_DECISIONS.md读取。各个versions中的正式冻结/Owner采纳/验收原件未修改，本页只是当前适用性索引。

直接方法证据为docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_SOURCE_AUDIT_AND_CONTRACT_FREEZE_REPORT.md，以及Owner博士论文第5.2.7/5.3节。历史记忆是查找线索，不替代原文；本轮不重演历史科学运行。

A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、价格direct_price_verified=False、真实C8 A–D REQUEST_ONLY和旧已消耗预算均不变。同步后也须另发具体科研许可。
