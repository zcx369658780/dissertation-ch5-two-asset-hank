# V0.0.2 · Astra 版本复盘

日期：2026-10-13（Asia/Shanghai）　终态：`CLOSED__ACCEPT__SOURCE_CONTRACT_AND_SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`

证据入口：[冻结计划](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/4b11c46823e7cdabc12de8b8036cc5efc2380c52/versions/0.0.2/plan.md)、[独立授权](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/3ed139aee7563a7033fa02fb933c3b49f24bd6b1/versions/0.0.2/authorization.md)、[最终验收](acceptance.md)、[Codex 执行报告](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/8f5457947492eef552f4261f8630c6c886af9fa5/versions/0.0.2/execution.md)、[来源 crosswalk](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/8f5457947492eef552f4261f8630c6c886af9fa5/versions/0.0.2/source_crosswalk.md)。

## 1. 目标与达到的工程级别

目标是从 V0.0.1 的合成下游链向上游来源边界推进：逐字段 SOURCE crosswalk + 独立 typed 模拟引用/manifest + 明示 SYNTHETIC-only 的 fail-closed 入口 + 真实 corrected aggregate/frozen/V0.0.1 batch 合成复用。代码候选只新增冻结允许的五文件，无旧源修改；GitHub 独立核候选单父 commit/tree 和五文件。Codex 报告最终准确候选树 `62 passed, exit0`，由静态测试源码设计和本地回执共同支持受限工程接受。真实来源及科学有效性仍未认证，不以合成测试补造。

## 2. V1.1 新流程实际表现

- 一轮 Codex 完整只读方案，Astra 审议采纳 V0.0.1 固定候选为本版代码起点；既有工作树 HEAD/index 不切换。正式计划 freeze SHA 固定后再另行授权，Codex 不宣布自我最终 ACCEPT。
- Codex 自主实现及失败/修复，报告 focused pytest `6/12`，真实模型/数据/受保护 consumer 均0；墙钟含前置保守额度 `2810.44/10800秒`，新建存储约26.9MB，远低于各冻结分层限额。实际与采样属执行端回执；网页没有读取本地所有原日志。
- V1.1 的**分层存储与候选证据规则**发挥作用：Git operational objects、candidate_views、receipts、public reports 分账，避免重演 V0.0.1 将临时 index 全算入10MiB证据根而停工；没有另向 Owner 申请本版资源豁免。长期仍须坚持权限和目录隔离，不把 GitHub 上传误当模型生产认证。
- 相比 V0.0.1，source crosswalk 和最小脱敏摘要更加完整。但预封存摘要缺最终运行和最终 tree，仍依赖交付回执作终端证据；网页缺完整原始进程输出，故只能 `CODEX_REPORTED_WITH_LOCAL_RECEIPTS`。

## 3. 实际偏差与归因

| 现象 | 分类 | 处理与下一版教训 |
|---|---|---|
| run01 新模块不存在，收集错误 exit2 | 预期 test-first RED | 保留，不宣称所有测试一次通过，且计入进程 |
| run01/run02 未取得 RSS peak | 观测缺口 | 后续使用 Windows 原生取样；历史峰值保持 UNKNOWN，不回填 |
| Git pre-publication whitespace check 因新报告 CRLF 失败 | 编码/文本治理缺口 | 保留旧字节与失败；仅新报告转 LF 后复核，不改科学逻辑 |
| GBK console 无法展示 Unicode minus | 本机显示编码问题 | 读取已保存 UTF-8 回执诊断，不用显示错误推断模型错 |
| 报告 helper 曾用系统默认 GBK 读 UTF-8，发生部分文件更新 | 跨脚本编码/原子性不足 | 显式 UTF-8；下次将报告生成/写入/校验做先成功后继续的受控事务 |
| PowerShell wrapper 在前一步失败后误发第5次 pytest | 编排/门禁缺口 | 中间树 PASS 不能当最终验证；该次计入6进程，第6次对最终精确 tree 再验证。未来命令间必须检查退出码/前置条件，停止依赖后续 |
| 公开摘要写入在最终 commit 前 | 证据时间序列限制 | 保留预封存状态，最终唯一身份由 enclosing Git commit + 单独 final delivery receipt 绑定；下一版可设计可独立验证的短签出回执，但不制造自引用 SHA |

偏差没有导致冻结科学法则、参数/网格、真实权限、既有 dirty 文件被候选改变。候选验收也没有回滚或擦去失败。

## 4. 对未来研发的建议（不是新授权）

优先解决真实 corrected producer 路线的固定选择、政策/质量/Q/checkpoint/省份/阶段联合 provenance 与 Owner 所需实际数据读取保护许可；只读 crosswalk 已表明 faithful KFE 与 corrected KFE 并非可互换。下一步若要真实数据来源认证，不应再仅扩写自报 digest 验证。

未来常规工程可考虑统一 Python/PowerShell UTF-8、原子写新报告和子命令退出码 gating、final-tree 测试签出及轻量 receipt digest；这些建议纳入下一版版前调查即可，不追改已冻结 V0.0.2，也不自动开新版本。独立网页复测不足的证据级别如实保留。

## 5. 封存

版本 `0.0.2` 最终 `CLOSED/ACCEPT_WITH_OBSERVATIONS`（限 `SOURCE_CONTRACT_AND_SYNTHETIC_ENGINEERING`），候选分支维持独立，无 main merge、无生产/真实数据门许可，Codex 该版停止。V0.0.3 `NOT_STARTED`。

`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、A16 `FAIL_CLOSED`、`model_activation=False`、`Results FALSE`、旧 CLOSED 资源/科学保护保持；人口/人均不变，不 `N=P/3`。此文仅复盘已关闭的 V0.0.2，不签发后继。
