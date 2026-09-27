# C9 output mutation A2：安全边界规格候选（零科学）

状态：`PROPOSED__DECISION_EVIDENCE_ONLY__NO_BOUNDARY_ADOPTION`。签发 parent `489efcc597c6873a1a0ec21fa48e335bea9235ca`，冻结 `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。Owner 选择的是 **A2 规格编写**，不是隔离边界、缩窄威胁、实现或实验的采纳。本报告仅依据下列本地材料，不作主机能力、权限或 API 实测。

## 依据与事实级别

| 来源 | 已确立的范围；不能推导的范围 |
| --- | --- |
| `docs/CH5_K1B_C9_OUTPUT_MUTATION_SAFETY_OBJECTIVE_A_OWNER_ADOPTION_20260927.md` | Owner 保留并发/恶意路径替换防护，最终检查到变更的窗口不可当作安全；未采纳较窄威胁模型。 |
| `docs/CH5_K1B_C9_OUTPUT_MUTATION_A2_SPECIFICATION_ONLY_OWNER_SELECTION_20260927.md` | Owner 只选零科学安全边界规格；尚未采纳隔离方案、排除攻击者、实现或实验。 |
| `docs/CH5_K1B_C9_OUTPUT_MUTATION_A_POST_CONTRACT_GAP_OWNER_DECISION_PACKET_20260927.md` | 恶意进程可在任意时刻替换根、父目录及 symlink/reparse/junction；其 principal、权限、祖先控制与同 token/特权写者是否在范围内均未确定。该包本身非执行权威。 |
| `docs/CH5_K1B_C9_OUTPUT_MUTATION_ATOMICITY_ZERO_SCIENCE_DESIGN_20260927.md` 及其独立审查 | 根声明、逐层 `mkdir`、独占 JSON/NPZ 创建、指定叶 `unlink` 各有最终检查后按路径变更的窗口。独立 `ACCEPT__ZERO_SCIENCE_DESIGN_EVIDENCE_ONLY__SAFETY_DECISION_PENDING` 只接受设计证据。 |
| `docs/CH5_K1B_C9_OUTPUT_MUTATION_A_NATIVE_API_CONTRACT_INDEPENDENT_REVIEW_20260927.md` 及 `docs/CH5_K1B_C9_OUTPUT_MUTATION_A1_USERMODE_NTCREATEFILE_QUOTE_REPAIR1_INDEPENDENT_REVIEW_20260927.md` | 官方合同缺口证据和 A1 引文 Repair1 的 ACCEPT 均限其范围；四项完整合同继续 `UNRESOLVED__FAIL_CLOSED`，不证明 A2 的 OS 排除边界。原 A1 候选的 REJECT 仍有效。 |

## 待定威胁与路径清单

下表的“待定”是**必须先取得的规格输入**，不是本报告填入的假设。现有资料没有未来独占输出根的精确路径，故以 `P0 → … → Pn → R → L` 表示：`P0…Pn` 是从可变命名空间入口到输出根父目录的**每一级**祖先，`R` 为待声明的独占输出根，`L` 为被创建或删除的指定叶。逐层 `mkdir` 还会把每个尚不存在的 `Pj` 变成下一步的父目录。必须对每一级单独判定，不能只检查 `R` 或最终叶。

| 项目 | 已确立 | 待定且不得默认 |
| --- | --- | --- |
| 攻击者身份与能力 | 目标 A 包含任意时刻的恶意路径替换。 | 每个潜在写者的 security principal、token、权限及其能否与执行者同 token；特权写者是否在范围内；是否可改变所有权/DACL、重命名或删除各级 `Pj`、`R` 和叶。不能假定 ACL 会约束所有在范围内的写者。 |
| 每级路径控制 | 最后检查不与后续路径变更原子绑定。 | `P0…Pn`、`R` 与叶的精确位置、创建者/所有者、DACL 及继承、谁可替换父项、谁可在根声明后重命名/删除根；父项被替换时对新对象的权限与身份。未来输出根尚未由本任务创建。 |
| 链接与卷 | 威胁描述包含 symlink、Windows reparse/junction。 | 每级祖先和最终组件的重解析策略及拒绝/跟随结果；junction 指向别处或跨卷时的边界、同卷/跨卷重命名与身份规则。无材料证明当前 ACL、账户或容器已覆盖这些路径。 |
| 独立运行身份的最小访问 | A2 要求保留冻结模型输入读取和授权输出写入。 | 新 principal 如何只读地取得全部冻结输入且不改写它们；如何仅在指定新输出根及必要父级取得创建、写入、删除权限；如何排除对受保护旧报告根和其他路径的写入，及这些授权能否被在范围内的写者更改。 |

## 四项变更的判定门

| 操作 | A2 若要声称 `PRESERVES_A` 必须给出的证明 | 当前结论 |
| --- | --- | --- |
| 初始 root claim | 在可信父级下独占声明 `R`，并证明所有可变祖先、父目录、最终根在检查到创建期间不可能被在范围内的攻击者换走；记录身份后仍保持同一安全边界。 | `UNRESOLVED`：父级权属/攻击者权限/并发替换未知。 |
| 每级 recursive `mkdir` | 对每个 `Pj` 的创建或已存在分支分别证明父身份和目标路径不被在范围内写者替换；处理 symlink/junction、部分创建与失败后权限边界。 | `UNRESOLVED`：逐层控制与重解析/失败状态未知。 |
| 独占 JSON/NPZ 创建 | 不仅叶名独占，还须证明已检查的父目录在路径式 `open("x")`/`open("xb")` 时仍属于授权根；写入、关闭或失败的部分叶不得外逸。 | `UNRESOLVED`：父级安全与并发 rename/delete、清理权限未知。 |
| 指定叶 `unlink` | 证明删除动作指向已授权父级下**指定叶**，且并发替换、重解析、权限/共享、失败与关闭不会转向另一对象。 | `UNRESOLVED`：安全寻址与删除权限合同未知。 |

下列候选只是待评估的**边界类别**；现有本地证据不能对任一类别、任一操作给出 `PRESERVES_A`。表中四列依次为 root claim、每级 `mkdir`、独占 JSON/NPZ、指定叶 `unlink`。

| 候选边界 | root claim | `mkdir` | JSON/NPZ | `unlink` | 缺失的核心证据 |
| --- | --- | --- | --- | --- | --- |
| ACL/DACL 排除写入者 | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` | 攻击者 token/特权、所有祖先及根的所有权和有效权限、能否改 DACL/重命名/删除。 |
| 独立账户或独立 principal | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` | 独立身份的输入只读/输出限写权限、每级路径上的其他写者能力和跨身份重解析。 |
| sandbox 隔离 | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` | 隔离对外部及同 token/特权写者、每级路径、链接和跨卷的实际约束。 |
| AppContainer 边界 | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` | 与上一行同类的精确权限与路径证明，以及冻结输入/授权输出的必要访问。 |

**缩窄判定规则：**如果任何候选方案只在**假定**本来能替换 `Pj`、`R` 或叶的写者不参与、或从威胁范围中移除该能力后成立，而没有证明 OS 边界在该写者仍在范围内时实际阻断变更，则其对应操作属于拟议的 `NARROWS_A`，**不能**标成 `PRESERVES_A`。所需 Owner 决定须逐项指明拟排除的 principal/token/权限（特别是同 token 与特权写者）、受影响的路径层级和操作、保留的并发攻击能力及残余外逸/误删风险，并明确是否接受该威胁模型缩窄。没有这份单独决定，Objective A 原范围继续有效。相反，若攻击者仍在原范围内，且精确权限、路径、重解析、跨卷和并发证据证明 OS 边界确实使四项变更不外逸，才可**提出** `PRESERVES_A` 供独立审查；本候选没有这样的证据。

本规格不采纳 ACL/账户/sandbox/AppContainer 作为等价 containment，不给出实施或可执行实验步骤。下一门是 GPT Work 对本零科学候选独立 ACCEPT/REJECT；即便 ACCEPT，也只是决策证据。任何后续缩窄须另经 Owner 风险决定；边界实现或隔离验证须另有独立有界任务。两次 C9 已消耗，实际调用账本均为 `CALL_LEDGER_UNRESOLVED`；C10、重试、部分续跑与 Results 关闭，Results eligibility `FALSE`。历史两次被禁止的 `--execute` 探测及全部 REJECT/有限 ACCEPT 范围不变。本轮无主机/API/`ctypes` 探测、ACL/账户/临时目录实验、测试、preflight、`--execute`、wrapper、模型或科学调用，且无新输出根。
