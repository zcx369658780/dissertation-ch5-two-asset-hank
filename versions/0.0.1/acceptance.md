# V0.0.1 独立最终验收（Astra）

- 日期：2026-10-13（Asia/Shanghai）
- 版本：`0.0.1`
- **最终分类：`CLOSED__ACCEPT__SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`**
- 原冻结计划：[固定提交 6c9a13bdf6a54913d8f16b5ec23fdda2a68f28e8](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/6c9a13bdf6a54913d8f16b5ec23fdda2a68f28e8/versions/0.0.1/plan.md)；原计划 Git blob `065cfaf699db99f36d0fb05f037986ba22479298`，不修改、不追改。
- 实施授权：[固定提交 837b99dff12f1b263fd7f4b80c43e19cf4efaa48](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/837b99dff12f1b263fd7f4b80c43e19cf4efaa48/versions/0.0.1/authorization.md)。
- 代码基线：`a1db8c114dec0ab69d69a5576e153a7f868cba0e`。
- 正式候选：[3260ec393dd4d53d6aab6c34d7c0442f09aa79f4](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/3260ec393dd4d53d6aab6c34d7c0442f09aa79f4)；tree `39e7a91ca473ba770bd65518607c3f78f4b9fe24`。
- Codex 执行报告：[execution.md（固定候选）](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/3260ec393dd4d53d6aab6c34d7c0442f09aa79f4/versions/0.0.1/execution.md)。
- 当前结果仅适用于显式 opt-in 的小省份 **SYNTHETIC_ENGINEERING**；不授予任何 `RUNTIME_REAL`、`SCIENCE`、`RESULTS`、生产或安全沙箱的资格。

## 一、审查的直接证据

Astra 通过已授权 GitHub 连接完成如下**独立静态与仓库元数据核验**：

1. GitHub Git commit REST 正文报告此候选 tree 为 `39e7a91ca473ba770bd65518607c3f78f4b9fe24`，父提交严格是批准代码基线。
2. GitHub 比较基线→候选：`ahead 1 / behind 0`；且仅新增 `src/ch5_two_asset_hank/multi_province/synthetic_household_bridge.py`（178行）、`tests/test_v001_synthetic_household_bridge.py`（357行）、`versions/0.0.1/execution.md`（174行），无旧科学文件修改。
3. 候选分支 `codex/ch5-v0.0.1-synthetic-household-bridge` HEAD 与候选完全一致。
4. 独立打开上述新增源码、测试和执行报告；source blob `41c0283bacef8a658be64f1cb69467f6d4a07197`、test blob `e7aeba558463567971fbbc9451b724a32157915b` 与执行报告所述相符。
5. 检查原 `corrected_household_adapter.py`、`one_turn.py`、`firm.py`、`migration_labor.py` 的获批基线相关函数：现有 API、双劳动入参以及新增回调和装配路径的源码可相互对照。
6. 冻结计划及独立授权以固定 SHA 实际读取；本次验收没有修改计划或科学合同。

**证据边界**：Astra 没有直接读取 Windows 的私有原始 stdout/stderr/JUnit、完整 local candidate_view manifest、进程采样 JSON、原 index 或旧 dirty/untracked 文件，也未在相同环境独立执行 pytest。执行报告与 Owner 交付称最终对准确 candidate tree 测试 `42/42 passed`、累计 `4/8` 次；测试源码静态可数 42 个参数展开实例。故“实际本地进程通过、预算峰值及保全”作为 **CODEX_REPORTED_WITH_LOCAL_RECEIPTS**，与本轮 independently verified Git/code facts 分账。测试中 `real_solver_calls=0` 等记录是受界哨兵声明，不是对整台机器的普遍隔离证明。

## 二、按冻结计划逐项裁决

| 冻结目标 | 结论 | 依据及严格上限 |
|---|---|---|
| G1：原源码→聚合→frozen→batch→callback→one-turn→firm 的身份/断点矩阵 | **PASS（受界源码）** | execution.md 对实际调用点、历史 SOURCE_ONLY 与本版合成执行分列；不等于真实 runner 全部接线 |
| G2：独立 opt-in 工程装配 | **PASS** | 仅新增模块，`SyntheticHouseholdRecord`、`build_synthetic_household_batch`、`make_synthetic_household_callback`、`run_synthetic_bridge_once`；未修改原生产/API |
| G3：单一合成调用链、两劳动路径与可观测原 firm | **PASS（合成工程）** | 同一参数化集成测试分别覆盖2/3合成省份；真实 aggregate/frozen/batch、一次 callback、一轮 one-turn；firm wrapper 委托原 `evaluate_firm`，不造 FirmResult |
| C1：合成来源/阶段/省份顺序/一次 callback | **PASS** | 正/负向参数化测试；仅 `SYNTH_*` + `SYNTHETIC/NOT_REAL_SOURCE`，有明确边界 |
| C2：独立算术 oracle、不可变快照 | **PASS** | Python 独立三重循环及迁移目的地×来源矩阵 oracle；原数组改动/只读诊断检查 |
| C3：家户 `Lt→Lt_prev` 与迁移 `lt_supply→firm当前Lt` | **PASS** | 捕获真实 firm 参数，两路不强制相等；单变 labor / Ct 检验。`pit=0` 时 mt 对 Lt_prev 不敏感，另用非零 pit 合成 oracle 检验；不把静态入参传递夸大为无条件经济响应 |
| C4：关键拒绝与 guards 保留 | **PASS（已列测试范围）** | 真实/缺失来源标签、轴序、乱序、非法 mass、p/g、stage、迁移负 base 和 firm 违法参数；有限同形转置依独立 oracle，不虚称 production guard 必检 |
| C5：精确候选树隔离视图 | **PASS（已发表证明 + 本地回执）** | 代码有 loaded-module `__file__` 必属 candidate_view 的检查；执行报告说明实际从 Git tree 导出并于封存后复测；原始导出清单未由网页直接打开 |
| C6/G4：结果/失败/恢复/资源及未闭矩阵 | **PASS WITH OBSERVATIONS** | 公开报告保留失败原文、测试修复和回执索引；最终完整原始工具流/样本仅本地，未由网页单独复验 |
| D：时长/进程/资源/科学预算 | **OWNER-REMEDIED WITH OBSERVATION** | 执行方报约21分钟、4/8 pytest、<=120秒/进程、峰值低于2GiB、最终 evidence 约1.87MiB；初始临时 index 导致 cap 超限真实记录存在，详见下一节 |
| E：保护与集中候选 | **PASS（Git 差异） / REPORTED（本地保全）** | 远端只添加3文件，一次发布；本地 HEAD/index、8 dirty、untracked/ignored 保全仅以执行端回执为依据 |

## 三、例外、偏差与授权解释

**真实问题**：初始临时 Git index（14,927,094B）放入 EVIDENCE，导致根目录约 15,908,461B，突破原冻结 `10MiB` 证据上限；主管前置拒绝、无 pytest 启动，当时应当并确已 STOP。此事实不能被事后抹除或改写为“首次通过”。

**恢复依据**：后续执行报告载有 Owner 对轻度修正的批准原话；此次交付也表明用户认可记录的授权依据。Codex 据此将**操作性临时 Git index** 移出 EVIDENCE 至独立 Git 管理路径，保留原失败和前后摘要、未重置4小时和8进程额度，不改科学模型/旧结果/冻结验收标准。Astra 将此认定为 **明确披露的 Owner 限定运维例外**，不是推定 Codex 有权无限修改资源预算。Owner 原始私有对话/回执未在此轮网页工具中独立读取。

**测试修正**：原 run02 40pass/1fail；由于 synthetic `pit=0`，`mt` 式中 `Lt_prev` 敏感性为零，原断言不成立。Codex 修正的是**测试期望**，独立新增 `pit!=0` 测试，保留公式原样。run03 及 post-seal 最终回执据执行方报告通过。属于原目标内普通工程修复，不是科学 law 变更。

**UTC 账务**：执行方报告对时间记录有勘误；本轮不从 GitHub 提取的非原始 UTC 字符串推算另一套进程耗时上界，仍以原 local receipts 的已报告值为准，不伪造起止时刻。

## 四、边界及最终冻结状态

- 仅确认**显式合成、小省份、非科学的工程装配路径**。不把这个独立入口连接到生产 `stationary_runtime` 或历史 K1B runner；真实 solver 来源/31省输入身份/frozen→生产 batch/callback 装配仍 `UNKNOWN/UNACCEPTED`。
- 经济意义仍未知：劳动人数与工时及效率关系、完整人口分母和单位缩放、实际年份/价格/时点、数据源等级和来源认证；不得认为 `Lt_prev` 等于当前 `lt_supply`。
- 原 K1B、C1、KFE/HJB、重要 guards 和 payoff/timing/资本科学合同不动；`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `UNRESOLVED/FAIL_CLOSED`、`Results FALSE`、`model_activation=False`、生产未接受与已耗预算不变。
- 人口/人均决策保留，户均封存，不恢复 `N=P/3`。
- 不自动创建、启动或授权 V0.0.2；后续任何真实数据/科学授权须另经版前协商、冻结与 Owner 必要决定。
- 此版本 `CLOSED/ACCEPT_WITH_OBSERVATIONS`，Codex 任务结束；GitHub 代码候选维持独立分支，**未合并 main**。

## 五、可复核入口

正式代码候选：https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/3260ec393dd4d53d6aab6c34d7c0442f09aa79f4

完整公开执行摘要：https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/3260ec393dd4d53d6aab6c34d7c0442f09aa79f4/versions/0.0.1/execution.md

冻结计划：https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/6c9a13bdf6a54913d8f16b5ec23fdda2a68f28e8/versions/0.0.1/plan.md

**裁决完毕：`ACCEPT__CH5_V0.0.1__SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`。**
