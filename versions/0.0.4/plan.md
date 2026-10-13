# V0.0.4 正式冻结版本计划：完全隔离的 Windows A16/window 合成句柄保护实验

**日期：** 2026-10-13（Asia/Shanghai）  
**版本类型：** `SYNTHETIC_FIXTURE_SECURITY_ENGINEERING_ONLY`  
**冻结时状态：** `FROZEN__AWAIT_SEPARATE_ASTRA_AUTHORIZATION`  
**实际真实资产读取许可：** `NO_READ / NO_STAT / NO_PROBE`  
**最高预期证据等级：** `ENVIRONMENT_AND_SCENARIO_BOUNDED_FIXTURE_PROTECTION_EVIDENCE`；绝非 `A16 PASS`、真实 source/窗口认证、科学/生产或 Results 资格。

## 1. 本版 Owner 权威、目标与不可追改边界

Owner 先后明确采纳：
- D1：历史 run004 初始北京三元数据只作为**未来拟核验对象**；
- D2：完整 Objective A16/window 威胁范围**不降低**，包含同用户/获 ACL 授权非管理员攻击者、父目录 `DELETE_CHILD`、祖先改名/替换、junction/reparse、POSIX delete/rename、既存映射或句柄、读句柄及 holder 进程完整生命周期；
- D3-fixture：**仅允许完全隔离的人造 fixture 的有限 Windows 句柄保护实验**，条件为已有合法工具、不得提权/安装驱动/创建账户/调整全局安全设置；完整隔离不成立则不运行；
- D4-fixture：**仅使用人工合成字节**；原始 SID/ACL/token、机器与句柄日志、故障收据 `LOCAL_ONLY`，保留到 Astra 独立验收，**不得自动销毁**；验收之后的保留/销毁处置另请 Owner 决定。公开仅允许脱敏的场景、API返回状态/类别、次数、覆盖缺口和实验版本；不得外传 SID、ACL、私有路径、原字节和机器详情。

上述 D3/D4 **仅适用于 synthetic fixture**，不代表 Owner 授权对 run004 北京文件、其父目录或真实模型的任何 `stat/exists/ACL/reparse/open/read/hash/parse`。原 [V0.0.4 版前草案](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/f5abef37cf7aa5b22c0b918782cc9a28daf60e5a/versions/0.0.4/plan.md) 与 [D1/D2 采纳](owner_d1_d2_adoption.md) 和 [Astra 技术审议](a16_window_feasibility_review.md) 分别为历史和依据；此文件取代 DRAFT，且只许在首次发布后用其**固定 Git commit 和 blob**作冻结合同，不能为谋求 PASS 或后续状态追改。

独立理论依据为 Microsoft 文档中 `NtCreateFile(RootDirectory)`、`OBJ_DONT_REPARSE`、共享模式、POSIX rename/disposition 及 `DuplicateHandle` 等受限 API 语义。尚未在真实目标 Windows 环境进行机制实验，不能由官方单一 API 描述声称全 A16 已获证实。

尤其区分：
1. 打开并保持原文件对象句柄正确，不代表其**路径命名空间不可替换**。
2. 本版仅试验**只读元数据窗口**的候选控制机制，不覆盖原 C9 Objective A root claim、recursive mkdir、JSON/NPZ creation、unlink 四个输出 mutation 操作。其原 `FAIL_CLOSED` 不变。

## 2. 固定代码基线、版本文件与保护

**`NEXT_BASELINE_ADOPTION=ADOPTED_FROM_EXACT_SHA`（只限本版独立候选树）：**
- 候选唯一父提交：V0.0.3 已接受 `cf74384f151427f0b7071ac0461cede6ad6cdf11`；
- tree：`372c693ca3dccea716ae8caef382f513e5a2316e`；
- 候选分支：`codex/ch5-v0.0.4-isolated-handle-fixture`。
- GitHub 治理文档分支：`migration/astra-workflow-20261012`；候选不得 merge 它或 `main`。

据 Codex 上次回执，本地唯一代码 worktree `D:\ProjectTemp\c5k1bturn56`，原 branch `codex/ch5-mp4c-k1b-turn5-turn6-bounded-continuation-20260922`，HEAD `a1db8c114dec0ab69d69a5576e153a7f868cba0e`，index SHA-256 `28058A7E2D9AB773C5813205C75999E6C221533AEAE0B9BB094B9A83451BF7CC`，staged0、dirty8、untracked5947、ignored4553；本轮网页不独立盘验。Codex 实施前须只读 fresh-check，确认文件冲突、保护哈希与实际 Git 根。**严禁修改/切换/清理/重置原 worktree、其 index/dirty/untracked/ignored，尤其两个 dirty 源码**，不得对 `D:\ProjectTemp`、`D:\Zotero-Analytical-Workflow`、EliteSync/DeepLearning-HANK 或其它项目作实验。

**本版代码候选严格仅新增三个路径**（已存在即 STOP 并报告，不以覆盖修复）：
1. `tools/ch5_v004_isolated_handle_fixture.py`：单一受界 fixture-only 原生 Windows API 入口/监督调度，必须带显式 `--fixture-only`，代码自身防止非 fixture 受保护路径的访问；允许 `ctypes` 调用系统已有合法 API，不准引入第三方/安装编译器/驱动；
2. `tests/test_ch5_v004_isolated_handle_fixture.py`：至多12个受限合成场景及固定同步屏障/故障注入，**不得引用任何历史 protected JSON/NPZ/MAT/CSV 或生产消费者**；
3. `versions/0.0.4/execution.md`：`PRE_FINAL` 的实施/环境/隔离/场景/预算/失败及证据级别；最终 tree/commit/后封存收据另作 `LOCAL_ONLY` 集中交付，禁止自引用。

如发现要写额外 .c/.h、可执行文件、全局配置、shell wrapper、科学/模型文件或新的公开报告路径，**不自行扩范围**；在现有三路径无法达成时可 STOP/REPORT。Astra 未来负责治理分支 `acceptance.md` / `retrospective.md`，Codex 不声明最终 ACCEPT。

## 3. 硬隔离环境前置门 G0（先于创建、调用及攻击）

1. **先只读核已有平台能力**：Windows build、目标 FS 类型、当前现有 Python/ctypes 支持、既有身份和工具能力。不得为取得能力安装组件、提升权限、创建帐号、启用开发者模式、编辑 ACL/全局安全配置。缺能力标 `NOT_VERIFIED`，不得靠跳过场景宣称全威胁模型 PASS。
2. **fixture 根必须为新建专用可弃用命名空间**，与模型树、run004、其它个人文件无交集。明确固定绝对路径、许可的本版新建路径集合及每个可变祖先。不得把 `D:\ProjectTemp`、共享磁盘根或包含真实模型/真实用户资产的共同父目录标为可变实验对象；可以在一个独立新建的可弃用 subtree 内建立更深层的目录以测试祖先 rename，但所有被攻击/修改的祖先都必须属于该 subtree。若找不到能静态证实这一隔离的已有合法位置，**在首次创建或任何改变前 `STOP__FIXTURE_ISOLATION_UNPROVEN`**。
3. 不能对现实科学/数据目录做 `stat/exists/read/ACL/reparse` 来获取证明；允许只对**拟议的专属 fixture 位置、已经批准的普通环境能力**做有界预检，且**不得触碰真实模型或共享可变祖先**。不得将聊天 cwd 或受保护模型根误识别为测试根。
4. 攻击进程只运行于一次实验监督生命周期内；所有可能危险的 rename/delete/reparse/ACL/硬链接/进程句柄操作目标**仅可由监督器白名单强制映射到人工 fixture 对象**。不得允许用户传递任意路径、通过相对路径 `..` 越界、对公共祖先作 rename，也不使用真正系统服务/驱动、真实目标 PID。需要的同用户/第二非管理员 principal 权限若缺失，则对应能力 `NOT_VERIFIED` 并在适用严格门 STOP，不得新建账号、提权或修改非 fixture ACL。
5. **程序不能运行到任何真实受保护目录/文件**，包括受保护 A16/window 相关文件的探测。只要隔离条件或路径解析信任链无法确认，直接停止；`no exception / no fallback / no retry`。

## 4. 实验 G1–G4 和场景限额（仅合成人工数据）

**G1 API/信任根链**：对人工 fixture 测试可信根目录打开、由已持有目录句柄相对打开**单一固定组件名称**、`OBJ_DONT_REPARSE` 与拒绝 reparse 行为、最小请求访问权及 share-mode，`FILE_OPEN` 不创建目标；验证真实 NTSTATUS/Win32 错误、句柄、文件身份。可信起始根无法证明时 `NOT_VERIFIED/STOP`，不将后验 hash 代替路径保护。

**G2 两性质独立 oracle**：① `OBJECT_READ_CORRECTNESS`（仅指定 fixture 内容）；② `PATH_AND_ASSET_IMMUTABILITY`（窗口内叶文件及各级被攻击祖先、命名空间与文件内容不被 D2 范围内的并发进程改变）。两项都需要明确的正/负 oracle。**不能以旧句柄仍可读、API 成功或几轮竞态攻击未奏效认定属性②**。

**G3 最多12个固定场景**（某项能力缺失→记 `NOT_VERIFIED`，不得 PASS）：
1. 完整句柄链建立及正常窗口/逆序关闭；
2. 叶文件 write/delete/rename；
3. 父目录 DELETE_CHILD / 对应 leaf name 替换；
4. fixture **内部**祖先 rename/替换（共享父/卷根绝不攻击）；
5. 初始 junction/symlink/reparse 拒绝；
6. 获取目录句柄过程的 reparse/名称替换；
7. fixture 对象的原地 reparse 设置/移除；
8. POSIX extended rename/disposition；
9. 攻击方已持有的 write/delete handles；
10. 人工 fixture 上的可写映射/硬链接别名；
11. 同用户进程对 holder 句柄/进程生命周期的影响（仅新建本版子进程，不能指向真实 PID）；
12. 前置失败、timeout、提前关闭及最终资源清理的 fail-fast。

上述**12是场景硬上限，不是成功数**；每个场景**最多一次尝试、无自动重试**，每场景硬墙钟<=60s；所有场景合计<=12次启动，**每场景最多3个明确的恶意操作、最多5个有名同步屏障**（获取前、获取中、窗口后、读取中、关闭中），实际尝试数和省略项均写清，严禁在一个场景下隐藏循环或无限随机压力测试。至多4个并发存活的受控实验进程（含监督器/holder/攻击者），超时停止本版子进程，不触碰其它用户进程。全体场景启动/测试窗口总墙钟<=30分钟，从第一次实际 fixture 实验启动起累计，**失败与前置消耗照计，不用新目录名归零**。

**G4 明确 fail-fast 状态机**：`AUTHORITY → ISOLATION → ENVIRONMENT → ANCHOR → HANDLE_CHAIN → WINDOW_ESTABLISHED → FIXTURE_READ → FINALIZE → CLOSE`。先核权限/隔离，再对每个原生调用核实际返回码/输出对象；前置失败进入不可逆终态，要求其后的打开/正文读取 **0**。场景预算和操作次数在调用前扣账，失败计入已用，绝不隐性继续运行后继链。PowerShell 外层亦检查 `$LASTEXITCODE`，不得连续脚本在错误退出后仍执行；不得将 `pytest PASS`、API日志或静态说明冒充 A16 合规证明。

**条件性受界通过**仅表示某个**明确 Windows build/FS/运行身份/API配置/实验场景**的人工 fixture oracle 成立；缺 D2 能力覆盖标 `PARTIAL/NOT_VERIFIED`，即使实验内12/12也不意味着普适保护、真实 run004 安全读取或旧 Objective A 四个 output mutation 安全。

## 5. 冻结资源与证据分账（仅本次合成 fixture）

Owner 同意的实验级资源上限：
- fixture 正文与该实验创建的人工文件总量 <= **4MiB**；本版被允许操作的根只含这些 fixture；
- `LOCAL_ONLY` 原生运行/进程/环境/错误回执合计 <= **4MiB**；实验完毕保留至 Astra 独立验收、不得自动删除，验收后处置待 Owner 决定；
- 本版**工具/脚本/构建/独立 Git 临时 index/objects/受限 candidate_view** 所有新操作性材料合计 <= **24MiB**（已含 Git 索引，不额外赠予旧 V0.0.3 的32MiB Git额度）；
- 三份 GitHub 新候选文件（脚本/测试/报告）公开 payload 合计 <= **128KiB**，不外传私有日志、SID/ACL/用户信息或人工 fixture 原始 bytes；
- 新建存储累计硬上限 <= **32.125MiB**，按上述四类分别计账，不因移动/清理路径而豁免；既有老 index/objects/ignored/untracked 不纳入新建但**不得清理**。
- 至多4并发实验进程；测试场景计数 <=12，每场景60s，窗口<=30min。Python/原生工具若无可靠峰值 RSS，可记 `UNKNOWN`；单实验进程工作集目标<=128MiB，非暗中替换成新科学进程许可；若选为硬内存门须先有可信测量。
- **真实 protected asset** stat/exists/ACL/probe/open/read/hash/parse/manifest verifier/旧 C9/C8/C10/科学 HJB/KFE/31省/GE/Results/生产部署：**0** 次。禁止继续旧科学预算或将 fixture 文件 hash 变成“真实来源已认证”。
- 新建存储/运行次数/时间任何硬限超出，立即 STOP 并报告，不得修改冻结版重置。缺 SDK/compiler/进程权限、不能建立合格 fixture 根与 ancestor isolation 均可 `BLOCKED__NO_EXPERIMENT` 收尾。

## 6. 三文件候选交付、隔离证明和 Astra 验收 A–F

冻结的候选从唯一父 `cf74384f151427f0b7071ac0461cede6ad6cdf11` 独立构造，只新增三路径；新文件应按 UTF-8/LF、显式失败停止处理。应用内 native API 需可追溯、无任意路径开放入口；当不足以证明独立保护时可提交有限报告/停点而**不造假的12/12 PASS**。

A. GitHub commit/tree/parent 与严格三文件 diff；未经许可不得修改任何科学/旧 source、V0.0.4 冻结计划、旧接受/复盘。
B. 实验隔离：完整记录固定 fixture 根与所有**获准可变祖先**、对应保护边界及运行前能力；仅公开脱敏分类，绝不公开真实文件信息。若隔离前置失败则必须**0** fixture 危险操作和0真实资产操作。
C. 测试证据：每场景是否有实际可施加的攻击能力、API/NTSTATUS、同步 barrier、attempt/exit/time、正负 oracle；不确定与能力不足不能计为 PASS；局部对象读与命名空间不可变分开报告。
D. fail-fast：前置失败/超时与未知权限都不能让后继 OPEN/READ/其它场景依赖链启动；保存全部原失败且不因新 run 名称复用预算。
E. 资源与保全：每项数目、时长与四类新建存储、独立临时 index、原 checkout/HEAD/dirty/untracked/ignored 保护及所有测试对象都来源于新 fixture；不复制真实历史资产。
F. 证据分类：`INDEPENDENTLY_VERIFIED_GITHUB_CODE` vs `CODEX_REPORTED_WITH_LOCAL_RECEIPTS` vs `UNKNOWN`；此版最高 `ENVIRONMENT_AND_SCENARIO_BOUNDED_FIXTURE_PROTECTION_EVIDENCE`，真实来源、Windows 全威胁、旧 Objective A、C9、Results 和生产均 `NOT_ACCEPTED/BLOCKED`。

封存代码候选后用实际 final tree 的独立限定视图进行文档/测试及身份核验，候选报告 `PRE_FINAL`，最终 commit/tree/后封存测试 hash 写到独立 `LOCAL_ONLY` 交付回执。允许一次普通 non-force push 并精确远端回读（如未完成则停在 BLOCKED），不合并 main/治理分支。Codex 不自行宣布 Astra ACCEPT；收到集中证据后由 Astra 独立审查并另归档 acceptance/retrospective。

## 7. 终态与保护性不升级

本冻约只在后续 Astra 发布单独 `ASTRA_APPROVED_EXECUTION__CH5_V0.0.4__ISOLATED_SYNTHETIC_FIXTURE_ONLY` 后生效实施；冻结本身不是授权。完成或阻塞后 `WAIT_ASTRA_FINAL_ACCEPTANCE/STOP`。若严格隔离与能力不足，允许 `BLOCKED__NO_EXPERIMENT`，不借此强行实施；不自动 V0.0.5。

`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `UNRESOLVED/FAIL_CLOSED`、window `UNACCEPTED`、`model_activation=False`、`Results FALSE`、原科学/数据 CLOSED 预算与人口/人均和不 `N=P/3` 都不改变。D3-real/D4-real 对 run004 北京三文件仍 **NOT_AUTHORIZED**。工作流 V1.2 生效。
