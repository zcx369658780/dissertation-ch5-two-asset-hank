# TEMP31 HJB边界/离散生成元与原MATLAB对应：独立隔离纯数学审计R1

TASK_ID=CH5_TEMP31_HJB_GENERATOR_BOUNDARY_MATLAB_PROVENANCE_ISOLATED_AUDIT_R1_20261029
STATUS=ISSUED_AWAITING_OWNER_TRANSFER
OWNER_APPROVAL=2026-10-29__REVIEW_HJB_OPERATOR_BOUNDARIES_BEFORE_MORE_TUNING__PRESERVE_OWNER_THREE_STEP_PRICE_DOMAIN_WORKFLOW
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=7bb47760f13e8b8dbdb23c9b3eb635dec51fa17e
TASK_PUBLICATION_COMMIT=EXACT_40_HEX_PROVIDED_BY_GPT_AFTER_PUBLICATION
EXPECTED_GOVERNANCE_REMOTE_HEAD=TASK_PUBLICATION_COMMIT_STRICT_EQUALITY
TASK_CONTRACT_PATH=tasks/CH5_TEMP31_HJB_GENERATOR_BOUNDARY_MATLAB_PROVENANCE_ISOLATED_AUDIT_R1_20261029/CONTRACT.md
FIXED_PARENT=56447829ce0e6c3c85552c53c351b26a2452a4bd
SOURCE_COMMIT=56447829ce0e6c3c85552c53c351b26a2452a4bd
SOURCE_PARENT=a51c2e7ff6548340a1ee86857b0ee55792fa69b4
SOURCE_ROOT_TREE=7b7cb29dd5b37be92561e7f1bc688c0d29789732
CANDIDATE_BRANCH=codex/ch5-temp31-hjb-generator-boundary-matlab-audit-20261029-r1
PREVIOUS_INDEPENDENT_REVIEW_COMMIT=7bb47760f13e8b8dbdb23c9b3eb635dec51fa17e
PREVIOUS_VERDICT=PASS_BOUNDED_NUMERICAL_LADDER_EXECUTION_AND_34_OF_34_DELIVERY__NOT_CONVERGED__GENERATOR_SCIENTIFIC_RISK_BLOCKED
REAL_HJB_HA_POLICY_INITIALIZER_KFE_GE_IRF_CALLS=0
MODEL_TEST_COMMANDS_MAX=0
PURE_SYNTHETIC_OPERATOR_TEST_COMMANDS_MAX=2
OPERATOR_PURE_ASSEMBLY_FIXTURES_MAX=4
NO_PRODUCTION_CODE_MODIFICATIONS=TRUE
NO_EXISTING_SOURCE_MODIFICATIONS=TRUE
NO_PRIMARY_EXCEL_OR_PROTECTED_MATLAB_TREE_READ=TRUE
NEW_GIT_REPOSITORIES=0
NEW_WORKTREES=0
NO_PRICE_SEARCH=TRUE
NO_ECONOMIC_PARAMETER_TUNING=TRUE
NO_SOLVER_ITERATIONS=TRUE
NO_AUTO_ISSUE=TRUE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 0. Owner的新的科研方法论（未来路线；当前不执行）

Owner在2026-10-29明确回顾其多省HANK历史调试方法并批准先审计算子：
1. **先确定家户可收敛的价格区间/价格向量区域**，不能只找一次偶然的收敛点；真实价格向量应包含家户工资（要区分首轮数值有效工资guess=19和后轮目的地tau_j净综合工资）、相关两资产回报及转移等，并明确数值/经济来源、范围和固定初始化。
2. **再研究厂商/经济系统的价格更新映射是否把新价格持续送回家户可收敛区域**。需明确一轮更新的时间先后、firm wage clipping、税率/迁移净工资组合及财政/产出/劳动有效量纲。将此表述为待验证的闭环映射，不擅自把“落入区域”视为GE已收敛。
3. **从个别省份的可收敛切片渐进到31省联合收敛**；定位差异、分组扩展、查看相互溢出和停止条件，而不是简单调经济参数让各省数据看似收敛。任何经验数据、政策校准、真实HA/firm/GE/31省运行都另需Owner冻结授权。

本次仅输出后续工作研究路线与必需输入/未决科学决策列表。**不得启动价格区间搜索、任何firm callback或其他真实模型求解**。当前三个delta的8状态HJB均不收敛：A delta1000、B100、C10，各80轮，且出现负非对角和非零绝对行和。初步区分算法/生成元风险与价格域问题，优先处理前者。

## 1. 已经独立确认的固定身份与数值事实

GitHub固定科研SOURCE_COMMIT=56447829ce0e6c3c85552c53c351b26a2452a4bd；唯一parent=a51c2e7ff6548340a1ee86857b0ee55792fa69b4，tree=7b7cb29dd5b37be92561e7f1bc688c0d29789732。
冻结Python源（源Blob必须实际核验）：
- src/ch5_two_asset_hank/matlab_faithful_operator.py = 9a511e151c9bf449412dc5605dfa1a2076711277
- src/ch5_two_asset_hank/temp31_netwage_policy.py = d90eb4ba627d4c702062116c2a4ffadac0f43d86
- src/ch5_two_asset_hank/temp31_netwage_hjb.py = 56441c1c41ec94190997ce6f0ecbb2b5c2ca7b56
- src/ch5_two_asset_hank/temp31_netwage_economics.py = 30528d55b884c62f3c9785dfe59197a61f125a3c
- tests/其他依赖只在确证必要时静态核对；原R4/R5和R2候选全部保留。

来自前序已获GPT独立A/B/C审核的同一8状态最后政策算子摘要（**是固定的执行者证据，不是完整8×8矩阵**）：
- delta1000: min offdiag=-0.2891145162423588, max|G1|=0.00045691399330394233, final deltaV=0.031119609835753792
- delta100: min offdiag=-0.081, max|G1|=0.00045691399330394233, final deltaV=0.01607907986119894
- delta10: min offdiag=-0.27379287506930644, max|G1|=0.00045691399330394233, final deltaV=0.16462851608474538
- 全部80轮未收敛，隐式线性代数误差约1e-15；不得从此推断结构模型本身永远不收敛或某个边界必然承担全部责任。

**原始MATLAB来源身份（本次GPT已直接从Owner上传的原版ZIP独立读取，不代表Codex本地安全库存在这些文件）**：
ZIP: 多省份HANK_matlab原版程序.zip，SHA-256 ceb94ccf34d2d218722b81e5111a8f4c530571a9f886bd4afe0610a00321f755。
内部 HANK_2ASSETS_HJB.m：raw12227 bytes，SHA-256 049136b769560040bc678f828f5d3ec5338ddcaa2090d6bed4e40732f56c3eae。
内部 multi_prov_HANK_12sts.m：raw5531 bytes，SHA-256 3c44449cfd4047b5c9e17e540afea2f50b4251150f8f74ab8cceed26e15dec97。
内部 HANK_mp_1turn.m：raw3254 bytes，SHA-256 d3d03f37286ed66202673ea63d49babce8d5309bac9c13793c8e60585c21fecf。
只允许Codex从**其既有安全隔离库中已经可直接核验的源对象**读取原MATLAB；若原MATLAB原字节并不存在，不能访问P3或原保护目录、不能联网/SSH额外拉取原件、不能声称Codex独立读取了ZIP。可使用下述GPT已独立从原版ZIP提取的逐行证据作BOUND_EXCERPT_REFERENCE，并明确MATLAB_RAW_LOCAL_VERIFICATION=NOT_AVAILABLE；如需完全逐字节MATLAB比对，应另向Owner要求授权提供安全副本。本任务不允许从被保护树补充源文件。

原版可核对的关键行及语义：
- HANK_2ASSETS_HJB.m 155-157: X=-Ic_B.*sc_B/db - Idh_B.*sdh_B/db；Y=Ic_B.*sc_B/db + Idh_B.*sdh_B/db - Ic_F.*sc_F/db - Idh_F.*sdh_F/db；Z=Ic_F.*sc_F/db + Idh_F.*sdh_F/db。
- 同文件 185-189: BBi使用spdiags对角及offset +-1, BB2max=max(sum(BB,2))。
- 同文件 190-198: dhB、dhF, MhB=min(dhB,0), MhF=max(dhF,0)+Rah.*aaah; 上界显式改写 MhB(:,J,:)=dhB(:,J,:)+Rah(:,J,:).*ahmax, MhF(:,J,:)=0, chih=-MhB/dah, yyh=(MhB-MhF)/dah, zetah=MhF/dah。
- 同文件 226-233: AAH采用spdiags offsets +-I，A=BB+AAH+Bswitch, A2max=max(abs(sum(A,2)))。
- 同文件 234-239: if A2max > num.homecrit 则报告Improper Transition Matrix并break。multi_prov_HANK_12sts.m 18: num.homecrit=10^(-2)；19: num.Delta=1000；14: num.maxit=100。
- 同文件 240-244: B=(1/Delta+rho)*I-A, rhs=u+V/Delta, B\rhs。以上只供固定边界/行和机制溯源，不可凭截取的若干行宣称所有MATLAB原文件已经字节级与Python同构。
- HANK_mp_1turn.m 15家户先求、46厂商更新、50计算综合工资；仅支撑未来价格映射流程的粗时序，不能将首轮旧来源税楔重新引入已修正Python家户代码。

**重要判断边界**：观察到max|G1|≈4.56914e-4确实非零，但比原MATLAB的homecrit=1e-2小；若严格按这个原版阈值，不能断言这次算子会触发原版行和STOP。原版检查了行和，不等于完整检查了所有非对角率非负；数学生成元审查应将source-faithful与经济数值admissible分列，不能混淆。

## 2. 必须逐项完成的静态源码与纯数学问题

A. MATLAB–Python有限原始证据映射：把原MATLAB X/Y/Z, BB, MhB/MhF, chih/yyh/zetah, AAH, Bswitch, max|row sum|/homecrit与Python新HJB选policy后的四个传递rates、operator.assemble_source_axis/assemble_source_operator逐一对照，记录原MATLAB关键行号、Python路径与真实行号、符号/offset/Fortran序列、边界选择。特别查py源 operator.py 39-43：边界越界的非对角项会被省略，但对角元仍无条件减去rb+rf。判断何时导致行和非零、符号如何变化；不得未经证据断言源代码肯定与MATLAB不同或肯定完全忠实。
B. rates上游成因：查新policy.py上界分支行230-232，将 mh_b=shadow_transfer_b+effective_return*a_max 转成a_backward_rate=-mh_b/da（行261），是否可能变成负rate；查看其他方向系数、适用边界flags及原MATLAB同义行。区分负rate自身、存储为offdiag是否对应合法网格邻居，以及对角修正。不能只通过scalar“负数存在”就声称三组真实G的负offdiag都已精确定位。
C. 矩阵元素诊断：限定 shape=(2,2,2)，Fortran列主线性索引 row=i+j*I+nz*I*J；计算/解释BB、AAH、Bswitch与G各部分，独立检查 row sums、offdiag sign、越界边及Bswitch作用。可基于**2条以内纯合成算子组装验证命令**与**总计最多4个8-cell fixtures**（例如合法rate的守恒反例测试、边界越界rate、上界负rate）直接调用固定原字节的**纯operator构造函数**；不允许调用真实policy、HJB driver、初始化/root、KFE/GE、31省数据、调整经济参数或迭代。
D. 对纯合成fixture逐row输出非零位置、bb/aah/bswitch单独贡献、row sum、offdiag、边界截断的因果标志及独立手算/解析关系。测试应能在故意注入负rate、边界出流时检测到异常，不以“生成元全部非负”作为假设。MATLAB只以引用摘录比较，缺原字节须降级科学源比对结论。
E. 前序三组末轮只有scalar summary/每轮标量轨迹，**没有归档完整原末轮8×8 G及每cell全部真实rates**，故若无原始G不可进行实际末轮逐元素真值归因。需要时明示LAST_ITERATION_EXACT_RATE_ATTRIBUTION=BLOCKED_NOT_ARCHIVED；不能悄悄重跑真实HJB为本任务补数据，也不能把合成fixture当成实际历史G。
F. 结论分四层：ORIGINAL_MATLAB_EXCERPT_SEMANTICS、PYTHON_SOURCE_FAITHFULNESS_BOUND、CTMC_GENERATOR_ADMISSIBILITY_MATH、CAUSAL_ATTRIBUTION_EVIDENCE. 若存在源忠实但生成元非法，需指出两者可以并存，以及未来修正须先由Owner裁决保真与科学正确性路径；不自动改历史程序或接受“修生成元”政策。

## 3. 本轮严格执行与预算

**运行HA/HJB/initializer/root/policy/KFE/GE/IRF/外层稳态/firm的次数均为0。** 最多两条独立Python命令，仅无HA纯数学合成operator，所有fixtures固定8-cell无经验数据，禁止pip/conda联网安装。不得重新运行前序240轮或追加第4个delta。允许静态AST/阅读GitHub冻结源、纯数组公式/人工计算不消耗模型call预算；任何检测脚本内调用实际HJB求解都属越界，必须STOP。

每条允许的合成命令需设置30秒硬超时、单进程/BLAS环境线程数1、1GiB进程提交内存限制（如安全监督不可用，STOP并报告）；不允许自动重复。测试脚本要带有源Git Blob验证、fixture实际输入，记录每次命令、原始stdout/stderr hash、公开脱敏内容、预先声明/响应与STOP。若operator模块本地缺失且合同未授权再次同步，则STOP纯测试部分，不从P3补文件。上轮R2/scientific source、34份先前证据所有字节保持。

仅写白名单：
- validators/multi_province/temp31_generator_boundary_source_audit_isolated.py（可新增，只做static和pure operator synthetic，不import HJB）
- tasks/CH5_TEMP31_HJB_GENERATOR_BOUNDARY_MATLAB_PROVENANCE_ISOLATED_AUDIT_R1_20261029/（CONTRACT只在治理branch；candidate中可加result.md、matlab_python_boundary_mapping.md、generator_component_matrix.md、synthetic_operator_evidence.md、three_stage_price_domain_future_work.md、gap_register.md、source_identity.json、privacy_report.md、manifest.json、DELIVERY_FINAL_RECEIPT.json和真实evidence/）
不得修改 src/ch5_two_asset_hank 下任何现有文件，不能新增生产调用或改变数值算子；不得新增新的Git仓库、worktree、分支以外的目录/路径，禁止修改已有冻结任务证据、清理、重置或提交任何私人LOCAL_ONLY原始数据。

## 4. 交付与正式停止门

复用以前批准的安全独立Git repo，先无follow/只读确认P3 BLOCKED、原shallow.lock库不可触碰、reparse/WASM及refs/工作区安全。GitHub治理branch发布后，Codex须实际查询远端治理HEAD=GPT给的TASK_PUBLICATION_COMMIT，且parent=7bb47760f13e8b8dbdb23c9b3eb635dec51fa17e、diff只新增本合同。科研候选源commit=56447829ce0e6c3c85552c53c351b26a2452a4bd、root tree=7b7cb29dd5b37be92561e7f1bc688c0d29789732、branch必须严格固定，不以治理branch作为代码parent。仅从SOURCE_COMMIT新建一个独立候选分支 codex/ch5-temp31-hjb-generator-boundary-matlab-audit-20261029-r1，且不得覆盖既有工作目录或其他候选。

真实对照源码、数学fixture及未来价格调试路线必须给出清晰可复核报告。原MATLAB原件若在隔离库不可获得，引用本任务冻结摘录及Owner上传ZIP SHA256作**GPT_EXCERPT_PROVENANCE_ONLY**；不得声称Codex独立原件核验。必须提交完整代码diff、输入fixture、手算/运算逐行矩阵分解、所触发的生成元风险、可与不可归因证据和未来需Owner裁决事项。

候选通过已授权普通SSH分阶段payload→seal交付，精确远端readback commit/parent/root tree/路径/Blob/bytes/SHA-256；seal commit只新增DELIVERY_FINAL_RECEIPT.json，不把本地外置回执/STOP日记也推送。SSH失败只用有界远端只读检查消歧，不自动重复push、不切换账号/Key/协议。Codex交付后STOP，等待GPT独立A提交/源→B具体数学与源码→C分层科学裁决；无自动Issue/PR/merge/cleanup/next。

P3_PROTECTION_BASELINE=BLOCKED
FORMAL_SOURCE_FREEZE=FALSE
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE
FULL_RUNNER_IO_CLOSURE=BLOCKED
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE
