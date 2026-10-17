# V010 M1 V1.3 冻结源码真实导入与 runner I/O 工程预检：限域主审

**2026-10-17 · 正式工程验收 · V1.3 E2重要里程碑一次集中裁决**
**任务ID：** `V010_M1_V13_VERIFIED_IMPORT_RUNNER_INTEGRATED_PREFLIGHT`
**冻结任务：** [固定原文](../versions/0.0.10/m1_v13_verified_import_runner_integrated_task_20261017.md)；发行Commit `1f379141cc8c7cf84a4c798f31f8b21dd3eedc7e`；任务Blob `f914da78fdce9b6c41fc29f68743c70f8ae83ffc`。
**Codex结果：** `V010_M1_V13_VERIFIED_IMPORT_RUNNER_INTEGRATED_RESULT`
**裁决：** `PARTIAL_ENGINEERING_DIAGNOSTIC__LOCAL_ONLY__E0_FROZEN_70_SOURCE_CODEX_REPORTED__E1_LOADER_REPAIR_LOCAL__E2_TWO_RUNNER_GIT_CHILD_PARTIAL__CANONICAL_IMPORT_BLOCKED__N13_NOT_EVALUATED__E3_NO_REMOTE_CANDIDATE`。
**状态：** `DELIVERED__STOPPED`；`ACTIVE_TASK=NONE`；本轮余量关闭、不结转。
**下一门建议（未新签发）：** `WAIT_OWNER_FRESH_V010_IMPORT_IO_READ_NETWORK_AUDIT_AND_N13_ENGINEERING_AUTHORITY / STOP`。

## 1. 独立GitHub核验范围

Astra从治理分支 `migration/astra-workflow-20261012` 核得审议前HEAD `50ecd02746624737df5e14a05dcc73258ccfe606`，与先前治理HEAD对比 `identical`（ahead0/behind0），读取本任务**固定发行Commit**中原文，Blob与 `f914da78fdce9b6c41fc29f68743c70f8ae83ffc`一致。目标独立review分支 `review/ch5-temp-v010-m1-import-runner-20261017` 搜索无匹配，且对精确ref下的`result.md`和`manifest.json`取文件均返回GitHub 404 `No commit found for the ref`。**远端审阅候选commit/tree/四份白名单文件均无，不能独立核验本轮Windows跑出来的raw bytes或合成证据。** 本轮不需要对远端temp文件做清理。

以下E0/E1/E2、PID、脚本哈希、first/final、进程及资源账皆是Owner转述的`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`：Astra不能访问Owner本地Windows `D:` 原件，不曾在网页执行冻结模型、Python、runner或HA。未见完整报告/机读case源，不能将摘要级证据写成`ASTRA_WINDOWS_RUNTIME_VERIFIED`。

## 2. E0/E1/E2/E3按对象的裁决

| Gate | Codex本地报告 | 限域裁决 |
|---|---|---|
| E0 只读prewrite与源码装配 | 在首次写入前确认路径、新根创建及二次复核；70个冻结Git源码、三个真实非空init按原字节恢复并前后hash匹配 | `E0_LOCAL_SOURCE_ASSEMBLY_CORROBORATED_CODEX_REPORTED`，未独立读取70文件或证明Windows同用户OS级排他 |
| E1 工程修复 | 路径检查语法、detached HEAD查询、双根Loader与成功`exec_module`后才`EXECUTED`的实现修复；原失败保留 | `E1_PARTIAL_ENGINEERING_REPAIR_LOCAL_ONLY`；因真实导入失败，不能认证VerifiedLoader已成功加载全部模块 |
| E2 两次真实runner | 每次5个真实Git child，Audit、双PIPE、Job、正常回收据报具有正向证据 | `RUNNER_PROCESS_GIT_IO_PARTIAL_CODEX_REPORTED`，并非完整runner I/O closure |
| E2 两次import | 分别被`IO_READ_CLOSURE`和`NETWORK_DISABLED`阻断；canonical与九模块认证未完成 | `CANONICAL_IMPORT_AUTHENTICATED=FALSE`；`NINE_MODULE_AUTHENTICATION=NOT_DONE` |
| E2 负例 | 合成适配器先异常，N13没有运行 | `N13=NOT_EVALUATED` |
| E3 GitHub | 唯一一次远端ref预检据报失败；fetch/push均0 | `E3_LOCAL_ONLY_FAIL_CLOSED`；远端ref不存在由GitHub独立确认 |

`IO_READ_CLOSURE`是需定位的读取来源/范围拒绝，**首次拒绝的确切目标未给出**，不能猜是哪一模块或一个保护目录。`NETWORK_DISABLED`是guard结果，不是独立证明真的建立网络连接：**事件子类型未记录，NETWORK_ATTEMPT_OCCURRED=UNKNOWN**；不得为取得import PASS直接关闭network deny、审计或源身份门。中止前实际加载模块清单UNKNOWN；旧首次runner变体只有SHA、没有可取的变体源码原始字节，不能追溯证明那份执行物精确源内容。

## 3. 真实执行次数和来源封存

| 项目 | Codex报告 |
|---|---|
| 工程Python子进程 | `4/6`；其中静态/合成`2/2`，两次真实runner与canonical尝试`2`；子分类按摘要，不臆补其他独立canonical进程 |
| Runner Git child | `2×5`；Stage A独立只读Git `24` 次 |
| PowerShell | `29`批；本任务采用V1.3普通工程范围内总预算，不套用旧任务“两批PS”上限 |
| 非Git本轮工件 | `126`件、`1,720,053B`，在32MiB上限内 |
| 新bare库 | `127B`；E3候选缺失 |
| 写前核验至封存墙钟 | `985.318s`；权威读取时长未单独登记，整体耗时结论仅本地账级 |
| 进程回收 | `18`个已知PID据报无残留；不代表枚举了所有潜在进程 |
| 旧17/20/25用例重跑 / HA/HJB/KFE/GE/IRF/real C8 | `0`（Codex报告） |

资源据报在显式上限内，但未取得每个进程真实wall/RSS、stdout字节/Job句柄等完整原始账，不能凭摘要认定全部硬门已独立PASS。本任务四个剩余额度? **仅记录总工程Python4/6，本轮退出STOP即剩余2次不得结转，也不能于本任务外自行启动。**

### 三份不同原始/派生seal必须分账

- 本轮真实`First`原件，本地报告SHA256：`9078F43AE786F65897072425D141578560721EDF5D4C5F3CF4086A9298DA86D3`。
- **原始Final**包含用时计算错误，须原样保留，SHA256：`E5AFD6318DEDCEDF53BFA1248BFE543786EDDF01C60A153F3686B224F46667F3`。不得以新Final覆盖它或删除其错误事实。
- **只修正用时的关联Final**是后继修订实体，SHA256：`1DF8CFFD1828F6636853E202D3568AE8296C540A0FF7B147ED6D73CE1A740AA8`；它可以用于明确归因后的统计，但**不是最初Final原始字节**，关联关系与变化字段仍需原始差异证据。
- 本轮终态`DELIVERY_RECEIPT.json`由Owner提供SHA256：`4BE31B06959200677C6D42F86EAF0FD43E8244F5750780A1B7CC23FB1E5BC636`，Astra未获得本机字节，不曾独立复算。

本轮“单向链/原件保存”亦只是Codex本地回执级，不提升先前B/S/L20首版`LEGACY_SEAL_CHAIN_UNVERIFIABLE`、时间戳旧脚本实际执行字节`UNVERIFIED`或早前SANITIZER`PUBLICATION_DENIED`及历史ledger偏差`UNRESOLVED`。

## 4. 科学边界与合理后继

V010数学冻结计划Commit `bf091da33d59293f147d52c11580327d3ac2a85d` / Blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；原模型候选Commit `94de4501dec051b969bee9d852eba2d4591f30ef` / Tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`均没有新确认更改。原MATLAB corrected两资产HA/HJB/KFE→多省手动有界顺序→GovInv收益率边界×0.9/1.1及Zt→冻结GDP各省误差≤1%独立回读→原lagged-NKPC；目的地税一次、same-S/上一完整轮raw ra0、家庭人均/省财政总量与三劳动账、phi_max=.3、20×20×2原网格/阈值均照旧。Owner corrected HA单点`rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07`仍`UNTESTED`。

`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`model_activation=False`、`Results FALSE`、`V011 NOT_STARTED`，以及 `A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`real C8 A–D REQUEST_ONLY`均保留。既有原D盘8dirty/index/staged/untracked/ignored/外Git common-dir、独立C盘SSD备份、旧失败scratch、真实C8/2017/2018/B3/V009错误资产的“本轮未触写”只属Codex报告，未做全局Windows原字节重扫，不得伪称Astra独立认证全盘不变。

合理后继（**仅建议，无新许可**）：把`IO_READ_CLOSURE`首次拒绝对象、`NETWORK_DISABLED`审计子类型、canonical/九模块实际加载顺序与缺原字节的runner变体身份，集中到**一张V1.3定向import-only工程闭环修复任务**；原始源码有可证hash时优先再用原可信冻结70文件，禁止复用不可认证runner源码。根据gate补全受界E1修复和真实Windows import/runner smoke，预算独立冻结。N13可条件式同任务核验。新的GitHub脱敏发布为可选后段，不应再次阻塞真实工程修复；没有Owner新授权不得重试旧ref、接管旧剩余2个Python进程或运行科学HA。

**终态：`PARTIAL_ENGINEERING_DIAGNOSTIC__LOCAL_ONLY__CANONICAL_IMPORT_NOT_AUTHENTICATED__TASK_STOP`。**
