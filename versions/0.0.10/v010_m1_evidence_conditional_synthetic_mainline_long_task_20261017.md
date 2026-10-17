# V010 — M1 原始工程证据收口 → 条件式两省 Synthetic HANK 科学验证（版本长任务）

**TASK_ID：V010_M1_EVIDENCE_AND_CONDITIONAL_SYNTHETIC_MAINLINE_LONG_TASK**  
**版本：V010 / v0.0.10；V011_NOT_STARTED。**  
**Owner新指令（2026-10-17）：**“请继续下达版本任务单”，结合Owner已采纳的V1.3“大版本/长任务/普通工程自主修复”原则。  
**性质：**一个持续的版本任务，包含只读M1取证及非求解工程准备、一次Astra独立释放检查点、条件式V010两省synthetic数值主线。**发行本任务不等于当前已获得科学运行许可**。  
**交付ID：V010_M1_EVIDENCE_SYNTHETIC_MAINLINE_LONG_RESULT**。  
**最终STOP：WAIT_ASTRA_V010_M1_M2_SYNTHETIC_MAINLINE_REVIEW / STOP**。  
**首次发行Commit/Git Blob由TASK_CURRENT登记，本文首次发行后不追改。** Codex执行前须按固定发行Commit获取正文并核Blob；不可用随时间变化的治理HEAD代替。

## 1. 本次版本目标、必须区分的证据层

研究目的：在不改变博士论文第五章已冻结的原MATLAB方法下，尽快把**M1可信Python运行工程**转化为可核算的**两省synthetic corrected HA/HJB/KFE—有界外层—冻结GDP核验—短期lagged-NKPC诊断**。实际依证据逐阶段进入；任何前置未过则保留本次已经取得的工程/分析成果并明确STOP，不假装整个宏观模型完成。

固定权威仓库`zcx369658780/dissertation-ch5-two-asset-hank`，治理`migration/astra-workflow-20261012`（不是main）。原冻结科学plan Commit`bf091da33d59293f147d52c11580327d3ac2a85d`、Blob`85138d8859d53295262fe13bf5bc277bca95ed3f`；**该plan 0–7节为数学、输入和科学计费最高约束**，本任务只能收紧、不得改方程/阈值/网格。原模型代码候选Commit`94de4501dec051b969bee9d852eba2d4591f30ef`、Tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`。唯一合成fixture`versions/0.0.10/synthetic_fixture_v1.json`，Git Blob`40915658d93403cfc21b33a6b864b332b7857749`，schema`CH5_V010_MAINLINE_SYNTHETIC_TWO_PROVINCE_V1`。Owner另提出的给定价格HA单点`rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07`**仍UNTESTED，不在本冻结fixture许可内**；不得临场代换输入取得数值PASS。

M1工程现有层级：Codex长期任务声称已完成70份Git模型原源码/3非空init、`SCOPED_ADAPTER_ONLY` canonical导入、九模块与runner五真实Git child、N13/PIPE负例；原生无适配入口仍BLOCKED。Astra已独立重算用户上传的`DELIVERY_RECEIPT.json` SHA256 `E100A61CA00DBD510FF8C7E9417EB2C2663E66C73AEBEDD81B6581A85BF36F50`（5,875B）及`DELIVERY_SUMMARY.md` SHA256 `351BF6C2FDF378142A1FCC4DFCFD81390A204C834E512F8ADD74680B88F20EA0`（1,984B），但**尚未收到其引用的九份本地原件**。原`FULL_RUNNER_IO_CLOSURE=BLOCKED`，`model_activation=False`，`Results FALSE`，`V011 NOT_STARTED`。**M1受界候选不等于完整独立工程PASS，也不自动释放任何HA预算。**

## 2. Stage A — 本版本一次性M1证据闭环与非求解科学准备（立即许可）

**本阶段新许可：**只读历史原证、允许在独立项目外scratch写本任务的证据包与非求解测试/验证脚本；工程Python/受界import-only按本阶段预算；**HA/HJB/KFE/selector/root求解调用严格0**。本阶段只负责确认已有M1工程与V010科学前提，不是重做所有工程历史。

新可写root`D:\ProjectTemp\ch5_v010_m1_science_bridge_20261017_01`，如该目标首写前已存在但尚未进行任何本次写入，仅准唯一备选`D:\ProjectTemp\ch5_v010_m1_science_bridge_20261017_02`。必须按V1.3完成可信父目录/目标**零写入只读Preflight→创建新root→首次文件写入之前二次身份复核**，旧失败root/受保护仓库不能写/改名/删除。只有新工程scratch可写，旧模型树/原失败raw/C盘SSD备份及真实C8等保持只读或禁触。

**A1：九份现成原证的确定性打包与核验。** 唯一来源是`D:\ProjectTemp\ch5_v010_m1_consolidated_20261017_01`的已报告产物。读取当前raw`DELIVERY_RECEIPT.json`并先复算上述精确SHA；由其`files[]`清单按原有明确身份取得下列**九份**真实字节，逐项校`size/SHA256/非reparse/来源`，不能猜相似文件名/向旧证据目录递归搜索、不能事后重建缺失原件：

`FIRST_RECEIPT.json`；`ENGINEERING_FINAL_RAW.json`；`manifest.json`；`result.md`；`engineering_evidence.json`；`runner_candidate.txt`；`PUBLICATION_RECEIPT.json`；`TERMINAL_ARTIFACT_INDEX.json`；`LEDGER.json`。

原receipt对九原件汇总约**204,154B**（应由实际字节重新算，不靠摘要代替）。若某项缺失/sha不符：写准确`RAW_MISSING_OR_HASH_MISMATCH`，不补造源或覆盖旧文件。仅将**通过哈希的原字节文件**打入单个便于用户上传的`CH5_V010_M1_EVIDENCE_ORIGINALS_20261017.zip`，可额外加一个独立`package_manifest.json`标记文件级SHA、来源、raw/derivative与已知UNKNOWN；ZIP压缩层字节改变不妨碍解压后的原文件内容逐件核证。若内容含真正SSH key/token/账号敏感信息不得公开，保存本机raw，仅派生脱敏副本并显著标记`SANITIZED_DERIVATIVE`（不伪称原raw完整证明）。Owner可在当前ChatGPT项目会话**上传这一份既有证据ZIP一次**，Astra独立复算和检查，无须任何SSH重试、科学重算或GitHub证据微任务。

**A2：工程事实与独立候选校验。** 对九份可用raw静态分析：`FIRST→ENGINEERING_FINAL→DELIVERY`引用、run_id/前后diff；原子ledger的单写者/并发冲突与早期Git prelaunch快照缺失分账；adapter`SCOPED_ADAPTER_ONLY`身份/来源/只读行为、九模块`EXECUTED`真实列表、五Git child×正确次数的PID/exit/Job/reader/readback、N13原错字段/派生修正与负例，逐阶段给`INDEPENDENTLY_VERIFIABLE_FROM_STATIC_BYTES`、`CODEX_REPORTED`、`UNKNOWN`。这是本机Codex自行取证，不能替Astra自己授M1 independent PASS。

**A3：V010合成科学的非求解准备。** 只读核固定fixture和冻结model tree，准备原15路径允许的工程接线/非求解focused oracles：劳动`phi[j,i]`方向、目的地工资税一次、人口单位与三劳动账、same-S及前完整轮raw ra0、GovInv收益×0.9/1.1与Zt、财政账户、原lagged-NKPC、固定20×20×2网格/HJB-KFE验收门解析。禁止在本阶段为了算测试结果触发HA/HJB/KFE、scalar roots、双省外层、真实C8；静态AST、stub与解析式focused测试若需Python必须计入工程预算。修复普通程序问题限新的独立候选视图/原plan列明的15个代码白名单路径，不改原冻结模型Commit，任何涉及新经济方程/网格/阈值的需求立即STOP。准备最终候选Git差异的精确文件名单、父Commit、Tree或LOCAL_ONLY身份供后续独立审计。

**A4：科学释放检查点（本任务内部里程碑，不新开版本任务）。** 当已经产生可上传的九原件包、已获Astra对真实raw与adapter/runner等审阅，并由Astra在治理权威以明确`M1_SCOPED_ADAPTER_ENGINEERING_PRECONDITION_FOR_V010_SYNTHETIC_SCIENCE=PASS`签出真实审议引用（或者更高独立工程PASS）时，才可在**同一个TASK_ID内**释放Stage B数值求解。未经Astra明确释放，Codex可以完成Stage A现有非求解工作，然后标记`PAUSED_FOR_ASTRA_M1_RAW_EVIDENCE_REVIEW`，**不消耗Stage B科学预算、不擅自将本机M1候选提升科学前提、不得把PAUSED伪称工程PASS**。如果原证确实缺失、来源或adapter具有危险不可消除问题，按实际门`FAIL_CLOSED/STOP`。审核等待期间不得在本任务以外另发微任务；批准后在已认证同一scratch/任务账本中恢复，任何新增模型源码差异必须如实列出并重新确认数学不变。

## 3. Stage B — 只有Astra明确释放后才启用的V010 Synthetic科学预算

**此阶段不是目前立即可运行的许可。** 本任务在Owner此次“继续下达版本任务单”的指导下预冻结未来**新独立**V010合成科学预算；实际执行必须先通过A4，且任何数学/代码超白名单变更都需Owner另行决定，不继承历史已经STOP的科学、工程Python、driver、HJB/KFE/root资源。

严格复用前述固定`plan.md`中数学接口、两省`SYN_A/SYN_B`输入、V0自造初值、全部HJB/KFE资格/数值阈值与原GovInv/Zt/lagged-NKPC方程，绝不引入Newton/fsolve、`Bt=Bgov`、财政补丁、C1替代或改变used/raw/目的地税。顺序一体化实施而不是每一阶段另签任务：

1. **B0 Final-tree focused oracles**：尽量先用Stage A准备且已审的stub/公式测试、固定fixture原字节、真实包入口、模块/适配身份作工程确认。测试PASS不等于科学PASS；候选变更后最终tree必须重新focused测试并保留不同tree身份。
2. **B1 两次完全相同输入的corrected HA绑定**：在20×20×2、F-order b-fast、Delta=1000及原corrected selector的严格HJB Bellman B、value D、Q行和/KFE单位质量、闭类source-free/At、Bt、Ct/Lt等门内运行，真实函数入口与input SHA先封存。两次成功值/分布和HJB/KFE摘要可比较，失败即只记真实失败（含`NO_ADMISSIBLE_POLICY`），**不能把更宽阈值或虚构收敛替代原采纳合同**。
3. **B2 有界两省合成steady state**：仅B1资格真PASS才至多5轮×2个HA；原phi、迁移Lt_mat、S same-turn与prev raw、firm上一轮目的地劳动、GovInv调整×0.9/1.1、Zt触发门、原tKN平滑及财税账户同时分账。失败停止科学外层，不继续冲击模拟。
4. **B3 冻结条件独立readback**：仅有真实有界outer收敛且used ra未撞界时，固定GovInv和Zt且关闭adapt，最多2个HA按原合同复算，核各省`abs(Y/Ytarget - 1)≤0.01`、全部HJB/KFE资格及共同固定点。只在本门过后可称`SYNTHETIC_TARGET_CALIBRATION_VERIFIED`，**不**等于现实31省稳态PASS。
5. **B4 原短动态递推诊断**：只有B3通过，才按冻结fixture做3期×2省零路径与1%衰减TFP短响应（合计最多12次HA）；每期外生量从冻结baseline重新赋值，保留原lagged-NKPC flag=1支路、状态carry，不用`1eq`或adaptive政策。所得只能称`SYNTHETIC_DYNAMIC_RECURSION_DIAGNOSTIC`，不等于正式现实IRF。
6. **B5 最终候选与独立结果包**：每个实际solver的原始input hash、完整成功/失败/selector/root账、模型候选tree/diff、数值摘要与不可观测值严格分开。用于论文结果的现实经济结论全部保持`FALSE`。即使某门没有通过，继续交付A阶段全部可信工程证据，不回滚、改写失败或伪造后继阶段。

原方案已冻结**总HA/HJB调用≤26**（2+10+2+12，包含失败），每HA HJB直接value update≤100、policy/Q≤101、selector cell全局≤2,100,800、每HA scalar roots≤400,000且全局≤10,400,000、KFE终端资格每HA≤1且只能在HJB双门后；严格逐项累积及原selector切换局部门。pytest focused≤6个子进程、science driver≤4个独立子进程，单次≤600秒（pytest）；总实际Stage B wall≤8小时，科学结果/产物新增≤256MiB、独立Git clone对象≤2GiB；RSS以实测为准、目标≤512MiB。所有内部Python子进程/HA/selector/root必须作为真实事件计入原子账；资源超额立即STOP。此**本任务专属新额度**不抵消历史已STOP预算，Stage B未获A4释放则这些数全部`NOT_RUN`。

## 4. 工程预算、交付模式与保护边界

Stage A非求解工程总工作wall≤4小时；所有工程Python/pytest/子Python最多16次，非Git证据工件≤64MiB，新scratch异常/终态预留≥4MiB；真实源码数据与普通日志独立实时计量，固定raw Git来源累计≤16MiB，诊断stdout/stderr每子进程≤1MiB。不要对普通PowerShell/JSON/路径/schema/manifest/adapter/ledger设置微型次数门，Codex在本任务总体预算内自主修复并重新验证。Stage A本机归档的九原证**优先手动一次ZIP上传对话**，不强求旧失败的SSH 443 remote review；若模型代码候选真改变，可在独立非共享工作树中严格只修改plan允许15路径，另备单一Git diff/patch并可选通过Owner现有SSH Key进行一次普通nonforce独立candidate branch发布，失败LOCAL_ONLY但不能因此重写原模型、重复SSH无限重试或触main/治理branch。

真正的E2/E3硬门：受保护根写入/重解析/来源SHA不可信、无法及时限制失控流或进程、真正非授权网络/子进程、额外科学预算、数学/数值阈值修改、原C8/2017/2018/B3/旧V009真实数据访问、用户隐私/SSH密钥外泄必须停止相应危险链并报告。Owner已有物理独立C盘SSD备份+GitHub，不要求新VM/第三备份；受界可信工作站不宣称OS_NATIVE_SECURITY_SANDBOX_VERIFIED。全程禁止在原`D:\ProjectTemp\c5k1bturn56`八dirty tracked、index/staged/untracked/ignored、外Git common-dir、旧失败scratch或C盘备份写入、checkout/reset/clean，不能把远端`_review_tmp`落地模型/治理worktree/index。

本任务仅运行固定合成fixture的数值科学（如且唯如A4释放后），现实中国31省GE、真实GDP/2017/2018/C8/B3、正式IRF、论文第5章结果计算、V011启动**不在此任务授权内**；`model_activation=False`、`Results FALSE`、`V011 NOT_STARTED`贯穿。更早B/S/L20首版seal`UNVERIFIABLE`、历史ledger/旧sanitizer`DENIED`及原stdout管道超额事实永久不变。

## 5. 一份版本结果、必要一次科学审议

**中间检查点只交一份**`V010_M1_STAGE_A_EVIDENCE_AND_READINESS_HANDOFF`：九原证可复算包及hash、已取得/缺失的原始证据、源/adapter/runner的具体限制、非求解测试与可重用候选tree、资源账。Owner将ZIP直接上传同一项目会话，Astra独立审核并以GitHub必要的极少量治理文件记录A4结果；**这不是新任务单或新预算**。未获得A4明确PASS时`SCIENCE=NOT_RUN`，Codex暂停在当前固定任务身份等待，不自行启动HA。

**终态只交一份**`V010_M1_EVIDENCE_SYNTHETIC_MAINLINE_LONG_RESULT`：源码及fixture固定SHA/bytes、最终15路径diff/tree、工程证据等级、所用adapter是否仅本机、准确真正科学调用/失败次数、HJB B/D/Q/KFE、same-S/税/劳动账与GovInv/Zt、目标GDP独立readback、短动态诊断及每个失败的精确阶段、输出/内存/存储/进程账与全部UNKNOWN。Owner可上传现成ZIP/脱敏结果进行独立审议；如有GitHub合法代码候选，由Astra独立核其Commit/Tree/原科学合同。不得凭`MODEL_CODE_EXISTS`、本机`SCOPED_ADAPTER_ONLY`、pytest成功或生成报告把`RESULTS`改为TRUE。

本任务执行范围明确面向版本科学主线，不再为普通schema、Windows版本查询、manifest、单个Git/SSH传输失败发布微任务。Astra最终按`SOURCE_ENGINEERING`、`SYNTHETIC_HA_HJB_KFE`、`SYNTHETIC_STEADY_STATE`、`FREEZE_GDP_TARGET`、`DYNAMIC_RECURSION`、`REAL_GE`及`RESULTS`分别做独立审议；失败保持状态不伪称PASS。后续只在Owner另批准时考虑真实数据/科学生产口径。STOP`WAIT_ASTRA_V010_M1_M2_SYNTHETIC_MAINLINE_REVIEW / STOP`。
