# V0.0.4 Astra Windows A16/window 技术可行性独立审议

日期：2026-10-13（Asia/Shanghai）

**裁决：`ACCEPT_FEASIBILITY_DESIGN__POTENTIALLY_FEASIBLE__NOT_PROVEN`。**

**现行保护状态：`OWNER_D1_D2_ADOPTED__D3_D4_PENDING__PROTECTION_BLOCKED__NO_READ__V0.0.4_NOT_FROZEN`。** 本审议仅接受 Codex 已提交的 `V0.0.4_A16_WINDOW_PROTECTION_FEASIBILITY_DESIGN` 为**值得独立 fixture 验证的技术候选**，不构成 A16 PASS、Windows 实测、旧 C9 输出 mutation runner 的安全认证、受保护真实文件的任何访问许可，也不授权创建/运行 fixture 实验。只有 Owner 另行批准具体 D3/D4 的 fixture 限定后，Astra 才可能冻结相应有界实验计划，再独立授权 Codex。

## 1. 审议权威和证据等级

- [现行 Owner D1/D2 确认](owner_d1_d2_adoption.md)：固定提交 `ddcca3f18ec31f6a7c25f1273ee632f1fec45f90`；D1=历史 run004 初始北京三元数据**拟核验对象已选**，D2=完整 A16/window 威胁域**不得缩小**。D3/D4仍待决，不得以本研究签发实际许可。
- [V0.0.4 原始 DRAFT](plan.md)、[此前 Astra 审议](review.md)、V0.0.3 固定[来源合同](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/cf74384f151427f0b7071ac0461cede6ad6cdf11/versions/0.0.3/producer_source_contract.md)与[读取申请](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/cf74384f151427f0b7071ac0461cede6ad6cdf11/versions/0.0.3/owner_read_request.md)持续作为范围约束。
- 原 [Objective A Owner 采纳](../../docs/CH5_K1B_C9_OUTPUT_MUTATION_SAFETY_OBJECTIVE_A_OWNER_ADOPTION_20260927.md) 明确以**敌对路径替换下的输出 mutation 安全**为完整目标，旧 final-check-to-mutation 窗口不被接受；[A 原平台缺口决策包](../../docs/CH5_K1B_C9_OUTPUT_MUTATION_A_POST_CONTRACT_GAP_OWNER_DECISION_PACKET_20260927.md)指出 root claim、recursive mkdir、JSON/NPZ creation、unlink 四种操作都 `UNRESOLVED__FAIL_CLOSED`。因此下述**只读元数据窗口**即使未来 fixture PASS，也**不关闭**旧 C9/A16 的完整输出变更 Objective A，不使其旧任务恢复。
- Astra 独立检查微软官方公开说明：`NtCreateFile` 的 `RootDirectory`、访问与 share 相容性、`FILE_OPEN`；`OBJECT_ATTRIBUTES.OBJ_DONT_REPARSE`；扩展 POSIX 删除、进程 `PROCESS_DUP_HANDLE` 与 `DuplicateHandle(DUPLICATE_CLOSE_SOURCE)`。这是 **DOCUMENTED_API_MECHANISM** 证据，不是实际 Windows/NTFS/ACL/SID/并发可达性证明；Codex 本轮无实验、无本地目标接触均仅为 Codex 报告。
- Microsoft 官方参考：
  - https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntcreatefile
  - https://learn.microsoft.com/en-us/windows/win32/api/ntdef/ns-ntdef-_object_attributes
  - https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_disposition_information_ex
  - https://learn.microsoft.com/en-us/windows/win32/procthread/process-security-and-access-rights
  - https://learn.microsoft.com/en-us/windows/win32/api/handleapi/nf-handleapi-duplicatehandle

## 2. 方案级技术裁决

| 设计 | 裁决 | 不能越过的界限 |
|---|---|---|
| path resolve/stat/open + SHA | `INSUFFICIENT` | 存在 TOCTOU、祖先替换和独立的访问合法性问题 |
| 可信根 + `NtCreateFile(RootDirectory)` 逐组件相对打开 + `OBJ_DONT_REPARSE` + 有限共享限制 + 全寿命句柄链 | **`POTENTIALLY_FEASIBLE / NOT_PROVEN`** | 可信根初始获得、目标 FS/OS 参数语义、父目录 `DELETE_CHILD`、非合作并发、POSIX rename/delete、映射/硬链接、ACL/token/protected process 全需独立证明 |
| mutex、字节锁、oplock 独立使用 | `INSUFFICIENT` | 不能单独保护整个目录命名空间和非合作进程 |
| ACL、独立 principal、sandbox/AppContainer | `NOT_PROVEN` | 不能假定通过换身份、改全局 ACL 或削弱 D2 威胁即可宣告等效保护 |

**两项不等价的必要性质**：
1. **对象读取正确性**：读取器没有被引向其它文件/越界对象，读取的是已获准且经身份绑定的对象；
2. **原路径/资产不变性**：在完整保护窗口内，原文件与父/祖先路径、可变元数据和文件内容均没有在已定威胁下被替换/破坏。

持有句柄仍可读取旧对象**不能**推导原命名空间不变；扩展 POSIX 删除允许旧句柄仍有访问能力。全链句柄也不是整个子树的自动锁。必须同时满足 D2 的所有相关性质，否则 `PROTECTION_BLOCKED/NO_READ`。模拟 fixture 通过有限并发样例最多给出 **环境绑定、场景覆盖有限的保护证据**，不是通用 A16 PASS。

## 3. Fixture 实验是下一潜在门，不是现行授权

Astra 倾向在 Owner **单独批准**且能证明隔离范围安全之后，规划一版**零真实资产、零科学调用的可弃用原生 Windows 句柄保护 fixture 试验**，而不是直接打开 run004 文件。

前置隔离要求：fixture 根应在一块完全明确的**可弃用命名空间**内；任何攻击性 rename/delete/reparse、权限设置或祖先替换，只能触碰**经 Owner 确认可弃用的 fixture 组件及其可弃用祖先**。不能因 fixture 设在 `D:\ProjectTemp` 下就把公共祖先 `D:\ProjectTemp`、磁盘卷根或含真实模型 `D:\ProjectTemp\c5k1bturn56` 的目录设为攻击目标。若无法使所有可能被变更的祖先与真实模型/私人资产隔离，则 `STOP`，不创建实验；最好是有确定独占边界的独立可弃用卷/隔离环境，但**不得擅装虚拟化组件、调整全局安全配置或移动现有资产**。构造受限文件名与句柄链、同步屏障及故障注入检查，不能触碰真实受保护数据。

Codex 建议的最多12种已列场景、30分钟、每场景60秒、至多4进程、fixture4MiB、LOCAL_ONLY回执4MiB、构建/工具24MiB、公开报告128KiB，**目前全部仅是参考提议而不是冻结额度**。必须进一步区分实际攻击尝试数/屏障、API调用和新建临时对象，而不是将无界攻击循环隐入“场景数”。第二 principal、SDK、符号链接/重解析创建权等若未现有许可与能力，不准创建账号、提权、修改开发者模式或扩大访问；`NOT_VERIFIED` 不得写 PASS。安全攻击实验必须单独获得 D3-fixture 权限；不得默认复用旧 C9 已耗预算。

**执行保护要求：** 单个 supervisor、准确原生返回状态与句柄、操作前扣账、失败严格阻断下游、异常不签发 `PASS`、最终树精确来源和 LOCAL_ONLY 原证。需区分保护窗口的建立、实际读旧 fixture 内容、窗口关闭后的行为。任何测试只允许人为合成并明确可删除资产，不允许真实 run004 `stat/exists/open/read/hash/ACL/祖先探测`。

## 4. Owner 尚须批准的实验级 D3/D4（不等于真实读取 D3/D4）

**D3-fixture 建议选项**：仅允许未来一次**隔离的人工可弃用 fixture** 的方案冻结与试验；固定工具版本和权限边界，**禁止一切真实第五章资产访问、修改模型根/公共祖先、提权、创建 OS 帐号、调整全局 ACL、安装 SDK/驱动、切 main/旧分支**。如现有 host 无合格编译器或其它必要能力则先 BLOCKED 复议。最多12个有限场景等限额在正式冻结时精确列全，Owner 当次批准实验条件后仍需 Astra 发布固定冻结/独立授权。**D3-real（真实三个北京文件）继续不授权**。

**D4-fixture 建议选项**：所有人工 fixture 的字节只在隔离目录和受控进程中产生/使用，原生安全日志/SID/token/ACL/完整机器路径与进程回执仅 `LOCAL_ONLY`，公开只可放脱敏场景、API返回码/计数、实验版本与 `PASS/FAIL/UNKNOWN`；明确由谁可读原日志、保留多久、何时/如何销毁，且不得以试验结束就宣称所有内存原始字节已被物理擦除。**D4-real（真实资产原字节生命周期）继续待 Owner 决定**。

若 Owner 暂不批准 fixture 技术实验，则继续 `PROTECTION_BLOCKED/NO_READ`，不重复源合同文档，也不自动启动 V0.0.5。

## 5. V0.0.4 当前停点

**`FEASIBILITY_DESIGN_REVIEWED__FIXTURE_GATE_REQUIRES_OWNER_D3_D4__PROTECTION_BLOCKED__NO_READ__NOT_FROZEN`**。

Owner D1/D2 已采纳且不重复决策。需 Owner 明确选择是否进入仅 synthetic fixture 的实验级 D3/D4；尚无正式冻结 V0.0.4 实施计划，也无 `ASTRA_APPROVED_EXECUTION`，无真实资产 stat/open/read/hash/ACL/probe 或任何实验执行许可。`NEXT_BASELINE_ADOPTION=UNDECIDED`，V0.0.3 candidate `cf74384f151427f0b7071ac0461cede6ad6cdf11` 仅建议候选根，不改 main/原 worktree。

原 `C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `UNRESOLVED/FAIL_CLOSED`、window `UNACCEPTED`、`model_activation=False`、`Results FALSE`、旧 CLOSED 科学/数据预算全部保持。人口/人均、不 `N=P/3` 和劳动/年份/价格/日历/真实 producer 联合认证缺口不变。V0.0.5 `NOT_STARTED`。
