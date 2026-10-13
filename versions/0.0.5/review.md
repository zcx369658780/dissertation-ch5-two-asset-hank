# V0.0.5 Astra 版前技术方案审议：等待 Owner 提供独立可信根

日期：2026-10-13（Asia/Shanghai）

**裁决：`REVIEWED__ACCEPT_EXECUTION_PROPOSAL__OWNER_SUPPLIED_ANCHOR_REQUIRED__NO_IMPLEMENTATION_AUTHORIZED`**。

本文件审议 Codex `V0.0.5_TRUSTED_ROOT_EXECUTION_PROPOSAL_DRAFT`，**不冻结原 DRAFT 计划、不授权环境探测或创建、不批准任何真实受保护资产读取、不恢复 V0.0.4 实验或科学预算**。

## 1. 独立审议及证据分层

- 固定原草案：[V0.0.5 plan](plan.md)，发布提交 `6792e7d7df57be9f5430d09583894131cd802795`，blob `af76fe8bac68fd60f5e4bcb32e558d9b646f33d9`，继续为 DRAFT。
- Astra 已通过 GitHub 核对 [V0.0.4 正式 G0 阻塞验收](../0.0.4/acceptance.md)、[复盘](../0.0.4/retrospective.md) 和 V1.2 规则。上版 `CLOSED__BLOCKED__G0_FIXTURE_ISOLATION_UNPROVEN__NO_EXPERIMENT__WITH_OBSERVATIONS`，无代码候选、无实验；旧 D3-fixture/D4-fixture 实施许可随版本关闭。
- Astra 另核 Microsoft 官方文档 `Naming a Volume`、`NtCreateFile`、hard links/junction 及 VHD attach：volume GUID 比盘符/卷标适合定位，但不证明卷的 Owner 所有权/专用可弃用属性，且一个卷可能有多个 GUID；`NtCreateFile.RootDirectory` 允许相对名称，但先要有可信根句柄。Windows API 机制为 `OS_DOCUMENTED`，实际资源、token、ACL、祖先/卷/VM 配置仍 `UNKNOWN`。
- Codex 本地 Git 只读状态、未写入/未探测等为 `CODEX_REPORTED_WITH_LOCAL_REPORT`，Astra 没有读取 Windows 私有状态/原回执，不将其称作独立证明。

## 2. A/B/C 路线最终版前取舍

| 路线 | 判定 | 关键先决 |
|---|---|---|
| **A：已存在且 Owner/可信平台提供证据的专用可弃用卷** | **首选，`OWNER_SUPPLIED_ANCHOR_REQUIRED`** | 独立供应/身份、专用与无研究资产声明、后续受限验证权限，不能仅给字符串盘符或卷标 |
| **B：可信供应的独立卷/隔离 Windows 环境** | **备选，`OWNER_ENVIRONMENT_PROVISIONING_REQUIRED`** | 新的供应方、宿主后端/VM分享与重定向/权限生命周期审议，不能默认安装、创建、挂载、格式化或连接研究盘 |
| **C：已有可信句柄下的单组件相对创建** | **`DEPENDENT_ON_A_OR_B`** | 仅能从已验证根约束子对象创建，不能自行证明初始根可信 |

**两条互不替代的证明**：①可信外部根身份和实际根对象绑定；②可变实验祖先及攻击对象与不可弃用真实资产隔离。后续首次创建/FILE_ID_INFO 只证明执行结果与对象身份，不替代外部可信供应记录。已存在卷、volume GUID、VHD、VM、独立驱动器均不能以名称或运行成功推导 A16 全部保护已完成。方案 C 不能独立补齐 G0。

官方参照：
- https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-volume
- https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntcreatefile
- https://learn.microsoft.com/en-us/windows/win32/fileio/hard-links-and-junctions
- https://learn.microsoft.com/en-us/windows/win32/api/virtdisk/nf-virtdisk-attachvirtualdisk

## 3. Owner 当前唯一关键资源选择

**首先仅请 Owner 说明：是否已有一块确实专用、完全可弃用、独立供应且能提供身份/配置证明的卷或隔离环境？** 有则选择 A，并由 Owner 私下提供必要定位和证据（不在公共 GitHub 披露卷 GUID、SID/机器路径或私有安全配置）；无则讨论 B 的可信供应与所需环境授权。**选择 A/B 只决定研究路线，绝非授权探测、开启 VM、创建目录或加载真实数据。**

后续仍须独立明确：执行 principal、官方身份锚与读取入口、具体允许的根身份/ACL/句柄查询次数、最多一次人工子树/哨兵创建、授信范围、隔离不成立时 STOP，以及 LOCAL_ONLY/公开脱敏/保存期限。拟议 bootstrap-only 预算（Codex建议 1次16KiB供应记录、1次根打开、<=16个固定查询、一次目录/一次人工文件创建及同句柄回读等）**目前仅 REQUEST_ONLY**，未冻结或支用。

## 4. 正式终态与科学防升级

**`WAIT_OWNER_TRUSTED_ROOT_RESOURCE_CHOICE__NO_PROBE__V0.0.5_NOT_FROZEN`**。

不得要求 Codex 自行扫盘找根、探测卷/祖先、安装 VM/VHD、格式化分区、调 ACL、提权、创建 fixture/运行原12场景或读取 run004 北京三文件。代码候选 `NEXT_BASELINE_ADOPTION=UNDECIDED`，V0.0.3 accepted `cf74384f151427f0b7071ac0461cede6ad6cdf11` 仅推荐，原模型 worktree/main/index/dirty 不改。

Owner D1历史初始北京三文件拟核验对象及 D2完整威胁模型持续采纳；D3-real/D4-real 未授权。A16 `UNRESOLVED/FAIL_CLOSED`、window `UNACCEPTED`、C9 `PAUSED`、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE及旧科学预算不变。V0.0.6 NOT_STARTED。
