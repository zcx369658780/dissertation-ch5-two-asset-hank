# V0.0.1 版本复盘（Astra）

日期：2026-10-13（Asia/Shanghai）
状态：`CLOSED__ACCEPT__SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`。

正式依据：

- [冻结计划（不可变 SHA）](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/6c9a13bdf6a54913d8f16b5ec23fdda2a68f28e8/versions/0.0.1/plan.md)
- [独立实施许可](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/837b99dff12f1b263fd7f4b80c43e19cf4efaa48/versions/0.0.1/authorization.md)
- [Codex candidate execution](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/3260ec393dd4d53d6aab6c34d7c0442f09aa79f4/versions/0.0.1/execution.md)
- [Astra final acceptance](acceptance.md)

## 1. 版本目标与真实结果

预定：完成合成 household 输入→原 aggregate→frozen→batch→显式 callback→原 source-faithful one-turn→firm 入参的可核验小规模工程路径，并留足科学资格和真实数据保护界线。

结果：候选仅新增获批模块、测试、脱敏报告3文件。GitHub 独立确认代码基线后进1提交、branch/tree正确、未触及现有科学源码。Codex 报告 candidate_view 实测42/42、4次 focused 测试进程；Astra 静态查验测试参数展开数42、调用链和数学 oracle/失效 guard，未亲自重跑 pytest。最终仅受界 `SYNTHETIC_ENGINEERING` 接受。没有证据支持真实 solver→生产 consumer、经济单位、GE/Results 接受。

## 2. 资源及真实流程观察（非自动监控）

- Codex 报告全程墙钟采样**约21分钟**；正式冻结工程上限4小时。网页未复核原始本地时钟。
- Codex 报告 focused pytest **4/8次**；单次≤120秒、最高报告进程峰值约87MB、最终本地新 EVIDENCE 约1.87MiB。私有原始流水未对网页开放，这些均为执行端回执，不是 Astra 本地进程复测。
- GitHub 仓库独立可核：候选从固定代码基线前进**1个提交**、**3个新增路径**；候选分支指向报告 SHA。一次 non-force push 由 Codex 报告，最终 Git 状态可独立读回；原本地 index/dirty 保全仅依据 Codex 回执。
- 版前协商：**一轮正式 Codex 执行方案草稿**，Astra 采纳并冻结有界科学含义与资源范围；冻结后没有实时监督/多轮微审批。
- 工程期间人为介入：**一次 Owner 报告的轻度运维修正授权**（临时 Git index 位置）；不构成再版前协商。初始超限记录保留，不算无障碍一次通过。
- 错误返修：run01 test-first 缺新模块；run02 **40pass/1fail**，原因是 synthetic `pit=0` 消除了 mt 中 Lt_prev 变动影响；调整不正确的测试期待并新添非零 pit oracle；run03 42pass，run04 为最终 sealed candidate tree 复测（上述次数由执行端报告）。没有模型方程、输入经济单位或旧 guard 变更。
- 当前可识别的真实持续阻塞：本机项目控制上下文与模型 CWD 曾不同但已显式设绝对根；生产链来源/受保护实际模型数据/经济时点仍不满足高等级门限。本版没有解决这些问题，也没有隐性下一版授权。

## 3. 偏差分类与原因

| 分类 | 本版情况 | 如何处理 |
|---|---|---|
| **执行偏差** | 初次临时 Git index 约14.93MB误放到 10MiB 的新 EVIDENCE 根，根总约15.91MB，触发前置STOP | 原失败不可删除或转成 PASS；获 Owner 有限修正授权后，将操作性 index 移往受控 Git admin 位置，保留旧收据并沿用原资源账 |
| **测试假设偏差** | 误将 Lt_prev 传递等同于任何状态下 mt 必变化，忽略 pit=0 | 修正测试而非科学公式；增加合成非零 pit oracle，保留原失败 |
| **记录/时间偏差** | UTC 账务更正 | 保留原值与修正说明，不伪造网页侧精确耗时 |
| **方案范围遗漏** | 原计划已要求 candidate_view，但没有预先区分 Git operational index 与 EVIDENCE 配额对象 | 以后版前将 operating index、exported view、local evidence 和公开交付纳入不同的明确存储核算；这条是未来建议，不追改本版冻结约束 |
| **验证仍不足** | 私有完整运行回执、模块 readback、原 checkout 保全哈希无法由网页直接打开 | 审查凭公开源码与执行端证明接受有限合成工程；未来如需更强独立复验，设计安全的脱敏 receipts 摘要或独立可复测 runner，不因此回头放开受保护数据 |
| **验收漂移** | 无证据表明改动了 frozen targets/标准；新 Owner 运维授权只修正操作性存储 | 独立 `acceptance.md` 记录例外，固定 `plan.md` 不修改 |

## 4. 新流程试点结论

V0.0.1 证明了新协作**在本例中**可运行：Astra 先发布草案，Codex 回报真实代码可行性，Astra 固定科学/工程边界并独立授权；Codex 自主完成普通实现、测试与修复，集中发布候选；Astra 根据固定 SHA 独立复核并归档复盘。

这是一个版本的流程样本，不能据此推出未来复杂科学版本都能无阻塞自主执行。对真正科学/保护决策和已闭预算的停点仍然必须保留。

建议今后任何版前计划明确：（a）区分科学预算与普通工程预算；（b）临时 Git index 是否算证据配额；（c）测试输入变化对经济公式的条件敏感性；（d）供网页独立验收的最小脱敏原始运行回执；（e）真实 source-boundary/data-authentication 与 synthetic engineering 的分层资格。

上述为未来规划输入，**不构成 V0.0.2 立版或任务授权**。

## 5. 最终封存与下一步边界

`V0.0.1 CLOSED / ACCEPT WITH OBSERVATIONS`。保留 GitHub 单独 candidate branch，不合并 main。Codex 在收到本裁决后停止本版本实施，不追加测试、不清理本地证据。

C9暂停、CALL_LEDGER未解、Objective A16失败封闭、Results FALSE、model_activation=False、真实数据保护/科学合同均不变。人口/人均保持、不 N=P/3。

下一版的编号、目标、资源和正式授权须由 Owner 再次确认并经新版前协商；这里无自动签发。
