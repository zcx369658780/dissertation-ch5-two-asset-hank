# V0.0.4 版前计划草案：run004 北京历史元数据的受控读取可行性与 Owner 保护决策

**日期：** 2026-10-13（Asia/Shanghai）

**状态：`DRAFT__WAIT_CODEX_EXECUTION_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED`**

Owner 已明确同意启动 V0.0.4 **版本规划**。本草案不是冻结计划、受保护资产读取许可、代码任务或科学执行许可。Codex 本轮只可做有界**只读源码/公开科学合同/Git 元数据**评估并提交 `V0.0.4_EXECUTION_PROPOSAL_DRAFT`。Astra 审议后，如涉及实际受保护数据读取，必须先取得 Owner 对具体科学对象与安全/访问范围的**另一次明确取舍**，然后才可能冻结该范围并单独发布许可。不得从本草案或用户“启动版本”推断 Owner 同意读取文件。

## 1. 先验依据与本版科学问题

- V0.0.1：`CLOSED__ACCEPT__SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`，受限合成下游数据消费链，代码 `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4`。
- V0.0.2：`CLOSED__ACCEPT__SOURCE_CONTRACT_AND_SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`，synthetic-only 内存准入，代码 `8f5457947492eef552f4261f8630c6c886af9fa5`；模拟 digest/seal 不是历史真实来源认证。
- V0.0.3：`CLOSED__ACCEPT__DOCUMENTARY_SOURCE_CONTRACT_ONLY__WITH_OBSERVATIONS`，候选 `cf74384f151427f0b7071ac0461cede6ad6cdf11`，tree `372c693ca3dccea716ae8caef382f513e5a2316e`。它是一个**单父文档候选**，其 [corrected producer 来源合同](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/cf74384f151427f0b7071ac0461cede6ad6cdf11/versions/0.0.3/producer_source_contract.md) 和 [Owner 未来读取请求](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/cf74384f151427f0b7071ac0461cede6ad6cdf11/versions/0.0.3/owner_read_request.md) 均已有限接受，但三文件 `REQUEST_ONLY` 不等于已获读取批准。
- 原 corrected 科学合同、历史 31/31 run004 接受、KFE unique-closed-class Owner 方法采纳及 C9/A16/source ledger 等旧门禁仍以 `SCIENTIFIC_DECISIONS.md`、原接受全文与 `CURRENT.md` 最新前缀约束。checkpoint-11 聚合 fixture、北京 checkpoint-12 方法论诊断与 run004 31省初始成功**是不同固定证据对象**；历史成功不能证明当前本地受保护产物仍存在或已认证。
- GitHub 动态文档分支 `migration/astra-workflow-20261012`；本版代码/文档候选来源基线 **`NEXT_BASELINE_ADOPTION=UNDECIDED`**，倾向由 Codex 核查是否继续使用 V0.0.3 `cf74384f…` 固定树，因为它包含前版来源合同；未自动 merge main、移动原代码工作树或采纳来源身份。
- V1.2 工作流已经规定**依赖命令失败必须停止下游、UTF-8/LF、PRE_FINAL/最终树分离和资源 UNKNOWN**；V0.0.3 再次发生过前置失败仍续写，这是**执行落实问题**，不修改工作流版本。Codex 版前方案须具体说明最小 fail-fast 实施手段，不能再只重复规范性口号。

**本版建议目标**：在未来可能进行的第一次小规模真实历史元数据核验前，明确可信源、具体对象、Owner 的保护决定和可操作的停止门；在满足合法权限时才考虑让单个历史 run004 北京元数据子集获得**有界内容/成员身份一致性证明**，绝不因此直接认证真实经济单位、HJB/KFE 数值或生产模型。

## 2. 候选研究 G1–G4（均待 Codex 可行性审议）

**G1 · 信任锚与必要保护门的独立取证设计**（目前 SOURCE_ONLY）。重新核对 V0.0.3 合同所引用的**公开 GitHub 源码/固定历史接受原件**，说明历史 run004 科学成功的确切对象、原 producer 版本、信任锚及 manifest SHA `CF70E7D6A62A35F461D1A75B28F8F502B2CBDD2D94ED5D9DDFA099D821CC5EC6` 的形成与受信任条件。重点辨明 Objective A16 / window / source ledger 的旧禁止或未闭门到底怎样约束**未来三文件只读元数据门**；绝不把“文档已设计”偷换为“保护条件已满足”。存在先决冲突或证据不全就标 `OWNER_DECISION_REQUIRED/BLOCKED`，不能自动采用最宽松解释。不得读取被保护的原 manifest/收据来替代目前的公开证据。

**G2 · Owner 明确选择与受保护读取许可的最小决定**（`REQUEST_ONLY`）。Codex 评估是否继续建议固定 run004 初始**北京**还是有更可追溯的代表性方案（不得自行改选真实来源）；严格保留 V0.0.3 的三个源码推导 locator：
`R=D:\ProjectTemp\c5k1bturn56\reports\ch5_mp4c_corrected_optionb_initial_turn_unique_closed_class_kfe_20260920_run004`
① `R\sealed_manifest.json`，未来候选读取1次、上限2MiB；② `R\household\p00_北京\province_terminal_receipt.json`，未来候选1次、64KiB；③ `R\household\p00_北京\native_initialization_receipt.json`，未来候选1次、64KiB。仅为**拟议值**：3文件尝试/2.125MiB/重试0；不能把旧 manifest 包含4353项、历史成员总字节61,650,777误当成本次获准完整读取。三个目标的现时路径、存在性、大小、子文件 hash、可信祖先保护条件均 `UNKNOWN`。Owner 必须另外决定选哪个历史对象、是否允许这三个精确文件、采用什么访问工具/权限/身份、数据生命周期和保密输出、A16/window 处理是否允许继续；不同意时不进入读取。

**G3 · 如果 Owner 后续批准的微型历史元数据 readback 设计**（`NOT_IMPLEMENTED/NOT_AUTHORIZED`）。提出预读保护检查、规范路径/重解析与祖先条件、普通文件/大小门、可信 SHA/manifest 对照、最多一次内存快照解析、精确被授权成员读取和去敏日志的顺序；**逐项区分 stat/metadata probe、打开/读取、哈希、JSON 解析、科学运行的权限/次数账**，防止偷偷用 stat、目录遍历或旧 `_verify_run004_manifest` 扫描整个4353成员。任何实际资产读取都应在 Owner 具体允许后，由 Astra 另行冻结在可执行版本内并单独授权；A16/window 或保护先决不能关闭则 `BLOCKED/NO_READ`。若获得一次未来真实元数据一致性验证，仅支持单个历史元数据成员层 `HISTORICAL_METADATA_MEMBER_CONSISTENCY`（建议标签，待独立采纳），仍不具备完整 policy/Q/KFE/p/g 联合认证。

**G4 · 单个可停止闭环与工程可执行性**。提出最小入口/脚本/文档形态（若有必要才编码）、封存候选的准确基线与允许路径、测试/实际读权限分账、预算和 UTC/fail-fast 账、信息脱敏、严格真实保护停点及最终 Astra 独立验收标准。避免另做一轮纯文字复制；如 V0.0.3 的文本已足够而科学许可不齐，重点交付**阻塞证据和供 Owner 一次决策的明确选项**。若 Owner 不允许读取，或实际许可门不闭合，本版可按事先冻结的 `DESIGN/STOP` 分支结束，不应为了宣称真实进展伪造 readback。任何后续 policy/Q/p/g 数值数组、31省、HJB/KFE、经济量纲、C9/GE/Results 都是后续独立门。

## 3. 预拟验收标准（未冻结，不是执行许可）

A. 精确报告历史 run004 北京 proposed 三文件的证据来源、科学版本和与 V0.0.3 原合同的一致性；把 source-only/path/hash、历史接受、当前可读/已验证三种资格严格分离。
B. 形成 Owner 可明确“选择/拒绝/要求补充”的**精简决策包**，并说明 A16/window/账本保护中哪条是必须先解除/澄清的硬前置。未作决定则保持 `OWNER_DECISION_REQUIRED`，不得用用户启动版本代替批准。
C. 读取行为的最小化安全方案具有明文 fail-closed 条件，禁止 symlink/reparse 越界、目录扫描、遍历整个 manifest 或不受控 JSON/NPZ 批量接线；后继审查的信任锚与客观通过条件可核，明确每次统计哪个操作是读取预算。
D. 版本候选及证据若获得工程授权，必须保持已有科学与生产文件不变；GitHub 代码/文档固定 SHA 与 Codex local 原回执分账。**无独立 Owner 保护读取授权时，实际真实受保护资产读取、stat/原成员散列、科学调用和生产均为0**；不能造一个假的`PASS_REAL_AUTHENTICATED`。
E. 冻结后才可设实际可执行的受保护读取/普通工程预算、项目专属临时目录和候选路径；不为做成版本连续性机械沿用前两版的合成测试次数、模型 RAM 或证明旧数据可用的空跑。不同最终状态可包括 `DESIGN_ONLY`、`OWNER_DECISION_REQUIRED`、`PROTECTION_BLOCKED` 或在真正许可且独立核实后才考虑有界历史元数据一致性，不自动提升为 `SCIENCE/RESULTS`。

## 4. 当前禁止事项与下一代码基线

- **本草案阶段 0 次真实受保护文件 stat/open/read/hash、0 次 pytest、模型 HJB/KFE、C8/C9/C10、31省 consumer、GE、Results、生产/部署及旧任务重试。** 不运行旧验证器，不读取元数据来“检测是否存在”，不新建脚本或工程候选。可以有界只读已有公开 GitHub 证据/本地非受保护源码和实际 Git 元数据。
- 目前原 worktree 据最近 Codex 回执为 `D:\ProjectTemp\c5k1bturn56`，原 HEAD `a1db8c114dec0ab69d69a5576e153a7f868cba0e`、staged0、dirty8、既存 untracked5915、ignored4553；网页未重新直接核对。保护原 index/dirty、两份 dirty 源码、旧真实数据与 local EVIDENCE；不得 `reset/stash/rebase/clean/force-push`，也不能修其他项目 Git/本地配置。
- `C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `UNRESOLVED/FAIL_CLOSED`、`window UNACCEPTED`、`model_activation=False`、`Results FALSE`、全部旧 CLOSED 预算仍有效。人口/人均决策保持、户均封存、不 `N=P/3`；劳动量纲、人口分母、外部价格/年份/日历和生产有效性 `UNKNOWN`。
- 文档发布分支 `migration/astra-workflow-20261012`、历史代码/文档候选 `cf74384f151427f0b7071ac0461cede6ad6cdf11`、原本地 HEAD、`main` 是不同对象。Codex 必须在版前推荐明确代码基线/是否沿用 accepted V0.0.3 及必要新增路径、资源等级；**`NEXT_BASELINE_ADOPTION=UNDECIDED`**，不可在此阶段自主合并代码/改变工作树。
- V0.0.4 的实施不由此前 V0.0.3 版本授权自动延续；本版草案也不等于授予新受保护读取权限。

## 5. Codex 唯一版前任务

只读实际读取：本计划草案、V1.2 工作流、CURRENT 与版本登记前缀、V0.0.3 来源合同和读取请求固定 candidate、必要公开科学合同及所指生产者源码。不要索引整个数千文件的本地仓库，不重新验证旧原资产，也不通过网络/其他仓库读取秘密。交付一次集中 `V0.0.4_EXECUTION_PROPOSAL_DRAFT`：

1. fresh worktree/host/projectId/origin/branch/HEAD/index/dirty/untracked/ignored 与文档/代码候选身份，推荐 `NEXT_BASELINE_ADOPTION`（对候选不对原 checkout）；
2. 对现有可信历史 run004 原件和 A16/window/C9/旧 ledger 的只读条件判断，区分版本级别科学方法采用、这一次特定资产证据是否可申请和保护许可是否尚缺；
3. 是否将 run004 北京三文件作为未来**需要 Owner 选择**的单一最小对象，哪些 locator/bytes/hash/producer 版本信息已确证、哪些未知；
4. 明确 Owner 需作出的最少方向/保护决定、是否存在不可绕过的阻塞，以及未来若批准的 preflight→stat/open/read/hash/parse 操作边界和出错停止条件；
5. 未来最小实施路径与有限的版本变更清单、科学/数据/工程/存储/脱敏资源建议，强制依赖步骤实际 fail-fast，而非仅文字承诺；完整 SOURCE_ONLY / HISTORICAL_ACCEPTED / UNKNOWN / REQUEST_ONLY 分账；
6. 若当前缺 Owner 决定或硬保护条件，提出可审议的 `BLOCKED/OWNER_DECISION_REQUIRED` 方案，不制造虚假的实体读取进展。

回复后 `WAIT_ASTRA_PLAN_REVIEW / STOP`。Astra 先集中审议，需要实质 Owner 授权时单独呈交决策；在新版本固定冻结 SHA 和**独立**实施许可之前，不得进行本版实现、文档写入、科学测试/真实数据读取、提交或推送候选。

## 6. 当前状态

- V0.0.1、V0.0.2、V0.0.3：按既有各自限定证据资格 `CLOSED/ACCEPT_WITH_OBSERVATIONS`，不回改。
- V0.0.4：`DRAFT__WAIT_CODEX_EXECUTION_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED`，本次没有实际 readback/测试/科学执行权。
- V0.0.5：`NOT_STARTED`。
