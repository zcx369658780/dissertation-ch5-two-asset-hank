# V0.0.4 Astra 独立实施许可：完全隔离的 synthetic fixture

日期：2026-10-13（Asia/Shanghai）

**`ASTRA_APPROVED_EXECUTION__CH5_V0.0.4__ISOLATED_SYNTHETIC_FIXTURE_ONLY`**

Owner 已明确批准本版本实验级 **D3-fixture/D4-fixture**：在完整原 D2 A16/window 威胁边界下，对全部人工合成、可弃用且与真实项目隔离的 Windows 句柄保护场景进行有限可行性试验。真实 run004 北京三文件只属于此前 D1 拟核验对象，**D3-real/D4-real 尚未批准**；本许可不得读取或探测任何真实模型/受保护资产，也不授权旧 A16/C9 输出变更 runner 的继续执行。

## 固定合同、起点、分支

- 正式不可追改冻结计划：[V0.0.4 plan](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/1b825948e69fcdfd30c1826be023d6963d2e9b25/versions/0.0.4/plan.md)，freeze SHA `1b825948e69fcdfd30c1826be023d6963d2e9b25`，plan blob `d5b6bbfd6b3b7146d2b9ab4a458ab75d666e1a91`。只有此文件与本独立许可共同确定执行边界；以前 DRAFT、review/feasibility 和历史任务不是额外权限。
- **`NEXT_BASELINE_ADOPTION=ADOPTED_FROM_EXACT_SHA` 仅本版单父候选：** `cf74384f151427f0b7071ac0461cede6ad6cdf11`、tree `372c693ca3dccea716ae8caef382f513e5a2316e`。
- 候选分支固定：`codex/ch5-v0.0.4-isolated-handle-fixture`；从固定 baseline 独立 Git index 构造，禁止 main/治理分支 merge，原工作树 `D:\ProjectTemp\c5k1bturn56` 的 branch/HEAD/index/八个 dirty 与 untracked/ignored 必须完整保护。
- 只准在代码候选**新增三个文件**：`tools/ch5_v004_isolated_handle_fixture.py`、`tests/test_ch5_v004_isolated_handle_fixture.py`、`versions/0.0.4/execution.md`。已有路径冲突立即 STOP，不编辑冻结 plan/授权/真实科学源码/旧 V0.0.3 代码或全局配置。需要新增 native .c/.exe 文件、SDK、账户配置、其它 public/secret 文件时不得自动扩文件清单；可报告设计受阻。

## 必须先满足的 G0

在任何 fixture 危险操作/首次创建前，Codex 检查**现有合法工具和平台能力**及一个实际可建立的**专用完全可弃用**实验根。其所有被攻击、被重命名/删除、更改 reparse/ACL 的目录（包括测试的祖先）必须位于同一可弃用 subtree 内，与真实模型、其他个人项目及它们的不可弃用父目录隔离。**不得把 `D:\ProjectTemp` 或公共盘符/模型所在目录作为攻击对象；不得通过对真实受保护路径 stat/ACL/exists/probe 来证明隔离。**

若无法确认符合以上边界、已有 WinAPI 访问和正确测试身份，直接 `STOP__FIXTURE_ISOLATION_UNPROVEN` 或 `BLOCKED__CAPABILITY_MISSING__NO_EXPERIMENT`，不要先创建目录后补许可；不能调整 D2、提权、管理员运行、安装编译器/驱动、启用系统功能、创建新用户或改全局 ACL。现有第二种非管理员攻击身份若不可用，则覆盖标 NOT_VERIFIED，不能以权限不足当防护 PASS。所有 API 引数必须限制为本版已确认的 fixture 白名单对象及进程。

## 已授权受限实施

- 可在上述三个文件内自主实现最小 `ctypes`/现有系统 WinAPI 的受限封装、受限 supervisor、人工 fixture、同步屏障和故障注入。此许可不开放任意路径读写 CLI；入口必须 fail-closed 的 `--fixture-only`，不能接收真实文件根为工作目标。
- 实验12个固定类别、每类最多1次启动/3次指定攻击动作/5个同步屏障、每场景60秒、合计实验墙钟不超过30分钟，零自动重试；最多4个同时存活实验子进程（含 supervisor），严格限制仅结束**自己启动**的 fixture 进程。每次尝试在 API 调用前入账；预算和场景不能因换目录/命名重置。
- 只在人工数据上测试可信根/相对打开、`OBJ_DONT_REPARSE`、共享标志/既存句柄、父 `DELETE_CHILD`、祖先 replace、POSIX rename/delete、reparse、映射/硬链接、进程句柄/关闭等能力。分别评价 `OBJECT_READ_CORRECTNESS` 和 `PATH_AND_ASSET_IMMUTABILITY`；攻击者无权限执行某个攻击时 `NOT_VERIFIED`，不是“被保护 PASS”。
- `AUTHORITY → ISOLATION → ENVIRONMENT → ANCHOR → HANDLE_CHAIN → WINDOW_ESTABLISHED → FIXTURE_READ → FINALIZE → CLOSE` 每步读取真实 native return/NTSTATUS、句柄和前置结果。任一前置步骤失败，后继被**程序逻辑**阻断（后继 open/read =0）；不得因 Python/PowerShell 的脚本错误继续调用。所有实际测试控制必须可安全停止。
- 冻结存储/资源：**fixture <=4MiB；LOCAL_ONLY原回执 <=4MiB；工具/构建/临时 index/objects/candidate_view 共同 <=24MiB；GitHub三文档/代码总公开 payload <=128KiB；合计新建 <=32.125MiB**。所有科学、HJB/KFE、31省、C8/C9/C10、real source、原北京三文件的 stat/ACL/reparse/exists/open/read/hash 等严格0；测试人工 fixture 的窗口不计为真实数据证据。工作集目标128MiB，未测量如实 UNKNOWN，不伪造。
- D4-fixture：**原始日志、SID/token/ACL、完整机器路径、含个人细节的环境回执仅 LOCAL_ONLY**，保留至 Astra 验收，**不自动删**；公开报告只展示脱敏场景、API状态分类/计数、环境版本的非敏感信息、欠缺能力及候选结果。验收后具体保留/删除待 Owner 决定，本许可不承诺彻底擦除内存字节。不上传新 fixture 原始 bytes 或真实资产。
- 普通范围内修复/重验可自主完成，但冻结的场景、次数、时间、存储资源不得追加/重开，所有失败与修复保留。违反硬门立即 STOP/REPORT，不做窗口缩小或平台限制旁路。

## 候选发布及最终停点

按 V1.2 新文档 UTF-8/LF、实际 return code fail-fast、精确独立候选树验证；`execution.md` 必须 `PRE_FINAL`，最终候选 commit/tree、测试与收据哈希放到单独 LOCAL_ONLY 交付回执。若运行 BLOCKED 或部分覆盖，真实上报，**不得捏造 12/12 保护 PASS**。

如全部合规，允许一次普通 non-force push 到 `codex/ch5-v0.0.4-isolated-handle-fixture` 并远端 GitHub commit/tree/parent/三路径回读。提交后停于 `WAIT_ASTRA_FINAL_ACCEPTANCE / STOP`。Codex 不自行判定 `A16 PASS`、`RUNTIME_REAL`、`SCIENCE`、`Results`，Astra 收齐证据后再决定有限工程接受或 BLOCKED。

本许可不签发新的 V0.0.5、不授权北京原元数据读取、不打开旧 Objective A mutation runner 的执行。
