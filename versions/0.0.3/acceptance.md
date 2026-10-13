# V0.0.3 Astra 最终独立验收：Corrected Producer 来源合同

- 日期：2026-10-13（Asia/Shanghai）
- **终态：`CLOSED__ACCEPT__DOCUMENTARY_SOURCE_CONTRACT_ONLY__WITH_OBSERVATIONS`**
- **最高资格：`DOCUMENTARY_SOURCE_CONTRACT`，不是新科学、真实来源、真实数据读取或生产许可。**
- 唯一冻结依据：[plan.md（freeze commit `768a3181fcbc9d367ccce08b1d69458353a48229`）](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/768a3181fcbc9d367ccce08b1d69458353a48229/versions/0.0.3/plan.md)，原 blob `1bf80332586a4e3beeeb355d90b5ec049c7e503c`，**未追改**。
- 独立实施许可：[authorization.md（`2ec13ea41e7bb86eacb19f4601d243a1298bd4bd`）](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/2ec13ea41e7bb86eacb19f4601d243a1298bd4bd/versions/0.0.3/authorization.md)，`ASTRA_APPROVED_EXECUTION__CH5_V0.0.3__DOCUMENT_ONLY`。
- Codex 固定候选：[commit `cf74384f151427f0b7071ac0461cede6ad6cdf11`](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/cf74384f151427f0b7071ac0461cede6ad6cdf11)；tree `372c693ca3dccea716ae8caef382f513e5a2316e`；唯一父提交 `8f5457947492eef552f4261f8630c6c886af9fa5`，候选分支 `codex/ch5-v0.0.3-corrected-producer-contract`。
- 本次实际 GitHub 三份候选材料：[producer_source_contract.md](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/cf74384f151427f0b7071ac0461cede6ad6cdf11/versions/0.0.3/producer_source_contract.md)、[owner_read_request.md](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/cf74384f151427f0b7071ac0461cede6ad6cdf11/versions/0.0.3/owner_read_request.md)、[execution.md](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/cf74384f151427f0b7071ac0461cede6ad6cdf11/versions/0.0.3/execution.md)。

## 一、证据及 Git 身份独立核对

Astra 通过已授权 GitHub 连接**独立确认**：
1. commit 元数据：`cf74384f151427f0b7071ac0461cede6ad6cdf11` 单父为 `8f5457947492eef552f4261f8630c6c886af9fa5`、tree `372c693ca3dccea716ae8caef382f513e5a2316e`；基线对比 `ahead1/behind0`、代码候选分支 HEAD 和提交一致。
2. 候选严格只新增三份冻结文件：`versions/0.0.3/producer_source_contract.md`（121行，blob `27b80e7ad5d7f1bcf9f595cccb6128e8c97c9ecc`）、`owner_read_request.md`（93行，blob `9c003f5f597aa8ef5d94cc172f8a6dacaabf9edd`）和 `execution.md`（127行，blob `afe2caab913884106d2764bf71d1130e1fbbf152`）。无模型源码、tests/validators、默认执行入口、科学合同、前两版文件或 freeze plan 的候选变更。
3. 实际读取上述三份候选文档、固定原冻结计划与授权，核对文档中 **S1–S8 的8份源码 blob + H1–H6 的6份历史采纳/验收原件 blob，共14/14精确匹配** 于固定代码基线 `8f5457947492eef552f4261f8630c6c886af9fa5`。该独立校验认证的是**GitHub 公开文件身份**，不是执行端电脑的原始受保护资产真实性。
4. 抽核现有 corrected 初始 producer、后续 producer、policy/Q 同 checkpoint、terminal KFE `p/g`、run004 历史 replay 与历史 corrected 31省闭合接受原件。不同 evidence/方法/checkpoint 分层不混用。独立核验的 SOURCE_ONLY 范围不外推到真实运行。
5. 验证未来 G3 三文件是 `REQUEST_ONLY / NOT_AUTHORIZED`；建议 3 次读取、大小 `2MiB+64KiB+64KiB=2.125MiB=2,228,224B`、重试0，仅为未来 Owner 审议参考。代码与原接受支持历史 locator 的讨论依据，但原资产的当前存在/真实bytes/成员hash、保护条件均未由网页核验。
6. `execution.md` 正确自称 `PRE_FINAL/PRE_SEAL`，没有企图自引用最终 commit；闭环材料由 Codex 提供集中后封存回执，下面分别标注证据级别。

**本轮网页没有**访问 `D:\ProjectTemp\c5k1bturn56` 本地原始 LOCAL_ONLY 回执、受保护 JSON/NPZ/MAT/CSV、历史 run004 完整 manifest/成员、Windows 文件 byte 清单、Git 操作性目录，也**未执行** pytest、HJB/KFE、source-loader、31省消费者或数值求解。

## 二、按冻结 A–F 的最终裁决

| 冻结标准 | 裁决 | 证据含义 |
|---|---|---|
| A/G1 corrected 来源矩阵与各历史证据分层 | **PASS** | 14/14 指定 GitHub blob/path 回读一致，现存函数/字段可核；当前资产认证仍 UNKNOWN |
| B/G2 联合可信锚、same-Q / checkpoint / 收益与拒绝合同 | **PASS（DESIGN_ONLY）** | 对独立采纳锚、生产者版本、完整 C/l 数值摘要、原 Q/p/g、状态/省份/时点和权限分别明确；未实现 loader |
| C/G3 北京 run004 三文件最小受保护读取决策包 | **PASS（REQUEST_ONLY）** | 三个可溯历史源码的 locator、目的、每项资源、0重试、Owner 安全审批和停点均有；未读取任何一个文件 |
| D/G4 下一门责任/输入/权限/资格矩阵 | **PASS** | 下一步必须新 Owner 科学/保护取舍及精确资产门；无自动权限晋级 |
| E 候选三文件/Git 单父及原资产保护 | **PASS（远端）/REPORTED（本地）** | GitHub commit/tree/path 独立核实；本地原 HEAD/index/8 dirty/5915 untracked/4553 ignored 保全由 Codex 回执支持 |
| F 有限文档校验、资源、失败原证/证据分级 | **PASS WITH OBSERVATIONS** | 最终文档检查 `exit0` 与资源上限由 Codex LOCAL_ONLY 回执报告；V1.2 fail-fast 曾偏离 |

## 三、Codex 报告及本地回执（网页非独立复算）

- **CODEX_REPORTED_WITH_LOCAL_RECEIPTS**：准确 final tree 三文档-only 校验 `exit0`、耗时 `1.859s`、三路径/blob/UTF-8/LF、内部引用及14份来源 Git blob 已测；累计墙钟含保守前置 `1,303.69/5,400s`。
- **分层资源（Codex 报告）**：operational `14,981,305 B` / 32MiB；three-document view `27,765 B` /1MiB；LOCAL_ONLY receipt `1,106,827 B` /2MiB；public three documents `27,765 B` /128KiB；新增合计 `16,143,662 B` /35.125MiB。无 pytest / model / protected file 读取，本版本科学预算严格为0；若未有测试进程，测试峰值内存为 `NOT_APPLICABLE`。
- 后封存文档校验回执 SHA-256（用户/Codex 提供，未读取字节复算）：`5fd3f2abe2f71a9828022bde3403cd65e98aea8f56791b8551629a09dfe581eb`；原始回执集合 manifest SHA-256：`c18231495f7eb4045313b36d99b59d2db9dcea66dbb20e5db1ec531662a33523`。
- 原本地 `HEAD=a1db8c114dec0ab69d69a5576e153a7f868cba0e`、staged0、原 index 哈希、8个 dirty 文件及上版5个文件摘要维持，5915 existing untracked 与4553 ignored 路径清单维持，依据执行端报告；现有几千非追踪资产内容未做全量字节审计，不冒称安全/内容已独立确认。
- `UNKNOWN`：当前 run004 实际 manifest/北京 terminal/initialization 文件是否存在及其字节/子哈希、历史 producer 完整数值身份、same-Q 政策/质量真实接线、劳动单位、人口分母、年份价格日历、真实后续科学/生产/Results。

## 四、保留偏差（不可重写成“全程零失败”）

1. 来源阅读回执命令第一次缺 `import sys`，退出1；**两份新文档在该依赖失败后仍被续写**，违反 V1.2 的失败后不得执行依赖下游步骤。Codex 保存原错误与部分文档 bytes，随后补正命令并确认14个来源 Git blob，重新建立后续执行检查。它是**真实 fail-fast 流程偏差**；本次之所以有限接受，是因未触碰禁区/受保护资产、最终冻树/文档范围和所需核验得到支持，绝非追改冻结标准或认定原行为合规。
2. 初始来源引用 checker 未能正确继承表格中的 `docs/` 路径前缀，退出1。依赖的 Git tree/commit/push 在本次失败时停止，修正路径前缀语义并复核14个完整 blob；保留原失败。属于本版许可范围内的普通文档验证工具修复。
3. `execution.md` 是 pre-final 时态；最终 tree/commit、完整后封存检查及最后预算保全属于外部 `delivery.json` 和集中交付回执。不能以文档自身不包含未来提交 SHA 为缺陷，也不能据此声称网页独立读了原回执。
4. 科学可信度上限：历史 run004 31/31 HJB/KFE/aggregate 为原接受对象，历史 bootstrap/replay、北京 checkpoint12 方法/后来 relaxation、checkpoint11 fixture 与后续 turns 不可合并；现时资产保护认证仍 BLOCKED。

## 五、终态与后续

**`CLOSED__ACCEPT__DOCUMENTARY_SOURCE_CONTRACT_ONLY__WITH_OBSERVATIONS`**。按计划关闭 V0.0.3；已接受的是可审议的 `DOCUMENTARY_SOURCE_CONTRACT`，不是 Owner 对北京三文件读请求的批准。三个未来文件的 `3 attempts / 2.125MiB / retry0` 仍只是潜在方案参数，未来任何读取必须在**新的** Owner 独立授权、保护审查、冻结预算及特定任务门下才可进行。V0.0.4 `NOT_STARTED`，没有 ISSUED、后台监测或自动继承许可；候选不自动合并 main，也不自动成为下一代码基线。

`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `UNRESOLVED/FAIL_CLOSED`、`window UNACCEPTED`、`model_activation=False`、`Results FALSE`，全部旧科学/数据预算与人口/人均决定保持，不 `N=P/3`。无新真实来源/模型/结果接受。
