# V0.0.5 备份受界预检及执行方案征集（DRAFT，未冻结）

2026-10-14（Asia/Shanghai）

**`DRAFT__SOURCE_SCOPE_UNRESOLVED__NO_BACKUP_COPY_AUTHORIZED`**

Owner 已要求先备份后直接接续 V0.0.5 主目标，目标备份目录为 `C:\CH5_Research_Backup`（此前 Codex 报告已空建，Astra 有限接受）。本草案只准**元数据/公开 Git 物件范围的只读备份计划评估**，**不授权真实复制、递归扫描、删除、重建目录、源数据读回或自动执行实验**。

## 1. 最小 Codex 回报对象

- 来源层 S1：从 GitHub 可核 fixed commit/tree 的**已公开 Git tracked 对象**列出最有价值的备份组（governance/current scientific contracts/accepted source code），清楚注明 fixed-commit 只代表版本化字节，不能说等于原 dirty 工作区。
- 来源层 S2：原模型 `D:\ProjectTemp\c5k1bturn56` 的 tracked dirty（历史8项、含2份源码），仅使用已授权的 Git metadata 原有范围估计数量/粗类别，**不读取 dirty 文件内容、stat/hash 原受保护文件**，不逐一输出私人敏感文件名。
- 来源层 S3：历史 untracked5947/ignored4553，sealed run004 及真实科学/LOCAL_ONLY 等严格默认排除，直到 Owner对精确对象、次数/体积/密级 D3/D4 另批准。不能调用递归源扫描或 `robocopy` 作为“预检”。
- 目的 `C:\CH5_Research_Backup`：只允许参考前次空目录回报，不为本次预检再次探测目的目录或创建新的备份层级。建议**非覆盖的新快照容器**，列唯一命名、必要目标 reparse/冲突保护和物理 C 空间预算；若没有明确的容量和写入许可，只提出后继请求。
- 定义明确的 Copy/Verification/manifest 两阶段合同：先不可变源身份（Git blob或下一门获准读的文件）→ 目标唯一命名/非覆盖 → 单次复制 → 同目的有限 hash/size/readback → 有缺项则不称为全备份；所有敏感回执 LOCAL_ONLY；GitHub仅脱敏计数与范围。
- 每一层写出物理安全限制、精确计划读取对象/次数/总体字节、保存期限/读取者、候选命令与错误处理；不对既有 HEAD/index/dirty/untracked/ignored 动任何写入。
- 主目标衔接：Owner 希望“项目内新目录”作为可弃用 fixture，说明它**为何不能**替代完整敌对 D2 的独立可弃用根；提出最小替代（已供应隔离卷/VM、或完全不做 hostile attack 的普通测试层），**不自动改变 D2**。需要明确用户所称“当前项目目录”是模型树还是别处，但不因此扫描任意其它项目。

## 2. 冻结前权限

仅审阅本仓库已公开 GitHub science/source 合同和不会触及原受保护路径的有界 Git metadata；不读取/探测 `D:\ProjectTemp\c5k1bturn56\reports\...run004` 和其它历史真实资产，不对备份目录再次做 FS 检查，不创造 copy/压缩/manifest，不写代码、报告文件、commit/push，也不运行 fixture、模型。操作性容量和 Windows 主机信息不足 `UNKNOWN`，不能假称已证明文件可备份、储存足够或目的路径安全。

## 3. 交付

一次性反馈 `V0.0.5_BACKUP_SOURCE_SCOPE_AND_FIXTURE_LOCATION_PROPOSAL`，明确**首批推荐允许来源集合**（固定 Git commit tree vs live dirty vs保护源分账）、哪一层足以实现 Owner 预期、必要 Owner 单项决定、目标空间/容量预算、备份/核验停点及不影响项目 tree 的安全部署。报告结束 `WAIT_ASTRA_BACKUP_SCOPE_REVIEW / STOP`。

本 DRAFT 不是 V0.0.5 主计划冻结，不创造任何真实数据读取权或恢复旧 V0.0.4 12场景、A16/C9/Results；V0.0.6 NOT_STARTED。
