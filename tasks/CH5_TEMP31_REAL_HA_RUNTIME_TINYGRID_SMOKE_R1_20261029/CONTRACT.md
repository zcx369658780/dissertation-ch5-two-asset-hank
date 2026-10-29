# TEMP31 真实HA独立运行时冒烟R1：导入→初始化→单格policy→至多一次极小HJB

TASK_ID=CH5_TEMP31_REAL_HA_RUNTIME_TINYGRID_SMOKE_R1_20261029
STATUS=ISSUED_AWAITING_OWNER_TRANSFER
OWNER_AUTHORIZATION=2026-10-29__APPROVED_ENTER_NEXT_STAGE_BOUNDED_REAL_HA_RUNTIME_SMOKE
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=2604237b485699962247a44174c9d88adcfe7fa3
TASK_PUBLICATION_COMMIT=GPT_WILL_PROVIDE_EXACT_FULL_40_HEX_AFTER_PUBLICATION
EXPECTED_REMOTE_GOVERNANCE_HEAD=TASK_PUBLICATION_COMMIT__STRICT_EQUALITY
TASK_CONTRACT_PATH=tasks/CH5_TEMP31_REAL_HA_RUNTIME_TINYGRID_SMOKE_R1_20261029/CONTRACT.md
FIXED_PARENT=b4f5471aeca304f60da4bd2340e4238561c5a92d
SOURCE_COMMIT=b4f5471aeca304f60da4bd2340e4238561c5a92d
SOURCE_ROOT_TREE=45a0b90ef1575b770a45dcc27c79a2ebab59a934
CANDIDATE_BRANCH=codex/ch5-temp31-real-ha-runtime-tinygrid-smoke-20261029-r1
PREVIOUS_FINAL_REVIEW_COMMIT=2604237b485699962247a44174c9d88adcfe7fa3
PREVIOUS_FINAL_VERDICT=PASS_BOUNDED_TEMP31_R2_HJB_POLICY_CALL_BINDING__FINAL_FOUR_FILE_SEAL_25_OF_25_DELIVERED__REAL_HA_NOT_RUN
NEW_REPOSITORIES_ALLOWED=0
NEW_WORKTREES_ALLOWED=0
PRODUCTION_SOURCE_WRITES=0
ALLOWED_TEST_COMMANDS_MAX=2
ALLOWED_INITIALIZER_BATCH_CALLS_MAX=2
ALLOWED_DIRECT_POLICY_CELL_CALLS_MAX=1
ALLOWED_CORRECTED_HJB_DRIVER_CALLS_MAX=1
ALLOWED_HJB_INTERNAL_ITERATIONS_MAX=1
ALLOWED_HJB_POLICY_CELL_EVALUATIONS_MAX=8
KFE_GE_IRF_CALLS=0
OUTER_STEADY_STATE_TURNS=0
REAL_31_PROVINCE_CALLS=0
FISCAL_MODEL_CALLS=0
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 0. 权限边界与成功定义

Owner在完整R2交付独立验收后，明确同意**进入下一阶段隔离真实HA运行时验证**。此授权只允许针对已经固定的TEMP31修正源码，在原已认证安全隔离库内执行两条受控Python smoke命令：第1条真实模块导入、一次tiny-grid初始化和至多一个真实局部policy单格调用；第2条必须在第1条成功且依赖/身份完整时，至多一次tiny-grid corrected HJB driver调用，max_iterations=1。是否完成一个数值迭代、是否收敛及返回什么对象必须如实报告。KFE、GE、IRF、外层固定点、31省、校准、福利、真实生产runner和primary Excel一律0次。

本次明确跨过此前“真实HA/HJB调用=0”的门，但只在这张Owner单独批准的新合同、固定网格、固定次数和可中止独立候选中生效。**P3受保护工作树仍BLOCKED**；不得借运行授权去触碰或复制受保护科研环境、数据、正式V010或改变任何模型经济机制。不会因一次HJB小网格调用自动改变Results=FALSE或宣布科学收敛。

仅适用成功分层：
- IMPORT_RUNTIME_PASS：真实所需模块/对象在隔离源下完整导入，不能用伪造的Solver/Policy/Operator来补依赖；
- INITIALIZER_POLICY_CELL_PASS：对真实源码初始化函数及真实一个局部policy函数完成受控调用（无其他HA调用）；
- TINY_HJB_ONE_ITERATION_EXECUTED：真实调用一次corrected HJB、内层max_iterations=1，记录返回/异常与finite指标；**一轮后的converged=False可以是合理的不收敛状态，不得算作完整稳态PASS**；
- 一项失败必须输出精确FAIL/BLOCKED，不得修源重试或把无运行证据标PASS。

## 1. 身份与执行地点硬门

1. 首先只读检查已授权**同一个**R3/R4/R5/R1/R2安全独立Git仓库，确认Git object store、来源、refs、未跟踪文件不会被覆盖，拒绝跟随symlink/reparse/WASM/alternates/旧shallow.lock目录，不操作P3保护科研树、主仓库、本地历史博士目录。不得新建Git库/worktree或执行clean、reset、rebase、历史基线重绑。疑点即STOP。
2. GPT提供发布后的真实40位TASK_PUBLICATION_COMMIT；通过已许可普通SSH有界检查**远端治理HEAD必须严格等于该发布commit**，唯一parent=2604237b485699962247a44174c9d88adcfe7fa3且治理diff**只新增本合同**。不可把治理HEAD误当科研源。若发布commit对象本地缺失，可记录LOCAL_PUBLICATION_OBJECT_ABSENT并依GPT固定GitHub元数据及有界远端HEAD观察，不允许无限fetch/协议/凭据切换。远端异常、权限拒绝或新变更即STOP。
3. 科研源码固定候选 branch codex/ch5-temp31-hjb-policy-call-target-repair-20261029-r2 HEAD必须严格等于SOURCE_COMMIT=b4f5471aeca304f60da4bd2340e4238561c5a92d，唯一parent=fd81e93782c1b63bb235eeb57a6abe215228e0d8，root tree=45a0b90ef1575b770a45dcc27c79a2ebab59a934。原R2最终25件seal及GPT终审必须保留，旧测试预算不重跑。
4. 新smoke独立候选只从FIXED_PARENT=b4f5471aeca304f60da4bd2340e4238561c5a92d生成。先逐文件核对需执行源码的Git Blob、必要raw bytes/SHA-256和实际导入路径，尤其：
  - src/ch5_two_asset_hank/multi_province/temp31_ha_taxfree_bootstrap.py Blob b82eadea383a4d7546a11d4f19686440f8d71870（NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL、Temp31NetWageInputs和真实初始化root）
  - src/ch5_two_asset_hank/temp31_netwage_hjb.py Blob 56441c1c41ec94190997ce6f0ecbb2b5c2ca7b56（第105行新policy调用正确）
  - src/ch5_two_asset_hank/temp31_netwage_policy.py Blob d90eb4ba627d4c702062116c2a4ffadac0f43d86
  - src/ch5_two_asset_hank/temp31_netwage_economics.py Blob 30528d55b884c62f3c9785dfe59197a61f125a3c
  - src/ch5_two_asset_hank/contracts.py Blob c746b616bec38531a7d96da81a54e2899d8aba53
  - src/ch5_two_asset_hank/matlab_faithful_operator.py Blob 9a511e151c9bf449412dc5605dfa1a2076711277
  - src/ch5_two_asset_hank/multi_province/temp31_ha_wage_debug.py Blob 7df9c03fdd55d72beded7383866d683ca9356bc9
  - src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py Blob 90667ddc00c72b9290e91481af4835c808ecfccb
  - src/ch5_two_asset_hank/__init__.py Blob d99cf2762787ed6999e63745903116f95fe02ab9
  - src/ch5_two_asset_hank/multi_province/__init__.py Blob 58484859799b3fd3c79d33f93b5a26fa6d7c0193
5. 源码安全边界：两套项目__init__.py会导入大量非必要的旧HA/KFE/区域运行模块。可在**仅本测试进程内**使用真实固定源码的隔离模块命名空间（Python ModuleType/__path__ + importlib真实源码加载），**跳过自动执行这些包initializer**，但不能伪造任何实际数学函数、返回对象、operator、policy或HJB。记录实际module.__file__/Git Blob来源及真实载入依赖；不得用mock/stub/monkeypatch让误绑定名字或缺失算法看似可运行。可用GIT_NO_LAZY_FETCH=1检查现存对象；仅当operator的固定Blob缺失，授权**一次**普通SSH有界精确对象同步：仅上述operator Blob 9a511e151c9bf449412dc5605dfa1a2076711277，限<1MiB、60秒、不重试、不开新仓库、不materialize或覆盖历史受保护文件。若其他必要源码/依赖缺失则STOP并报告，不能扩大fetch。
6. 使用已有Python3.11+、NumPy、SciPy已安装环境；禁止pip、conda、系统环境修改、联网安装、Jupyter大批量进程、读取真实数据。限制BLAS线程至1、禁止自动并行/子进程科研复跑。脚本必须可由独立候选真实源码定位运行，并可对source缺失/identity drift给出fail-closed。

## 2. 两条真实运行命令和严格网格

固定仅一个2省**合成**输入上下文，不是真实31省数据：
- province_order=("A","B"), context_id="TEMP31_TINY_HA_SMOKE_SYNTHETIC_20261029", entering_iteration=1；
- 初始state参考标量w_initial=20.0、tau_legacy_reference=0.05，真实工资税tau_by_destination=(0.05,0.05)及sigma_destination_origin=((0,0),(0,0))保存在数据记录中，HA局部有效工资=19.0，绝不把真实tau_j全局设0；
- r_a/rah=0.09、r_b=0.02、rb_gap=0.07、Tt=0.1；上述数值只作为冻结历史来源的合成冒烟参数；
- params EconomicParams(rho=.05,gamma_c=2.0,phi=5.0,chi_0=.1,chi_1=2.0,a_bar=1e-6,mu_z=0,sigma_z=0)；
- grid.b=(-2.0,5.0) 2点，grid.a=(0.0,10.0) 2点，grid.z=(0.8,1.3) 2点，switch_matrix=((-1/3,1/3),(1/3,-1/3))，共8个state cells。不得擅自增大网格、扩展两省或改变参数去使测试变绿。
- HJB numerics delta=1000.0、convergence_tolerance=1e-7、max_iterations=1、drift_tolerance=1e-12。只允许单次HJB driver调用和至多1次内层迭代；KFE=0，GE=0。
- 每条test命令必须由监督外层调用以**30秒硬超时**终止（包括导入/求解），单进程、单线程BLAS；如可可靠施加RSS/内存上限1GiB则执行并记录，否则明确MEMORY_HARD_LIMIT_UNAVAILABLE并不得虚称已强制限制。任何超时、系统资源异常、失败即STOP；不得自动调整限额后重试。

**命令1：import-initial-policy。** 验证真实固定代码在隔离 namespace 内导入，构造真实Temp31EffectiveWageRecord及Temp31NetWageInputs；调用真实temp31_netwage_initial_arrays恰1次（这包含最多8个原始root单元求解，必须计数）；检查返回shape=(2,2,2)、有限数组、首轮19和税/迁移楔未在HA再扣。然后**最多直接调用1次真实select_temp31_netwage_local_policy**，仅使用上述网格的一个合法cell、实际源的真实参数和输入；记录有限的consumption/labor/return/drift摘要、有限性与异常。v_a/v_b可使用有限合成局部导数（例如正的v_b_forward/v_b_backward=1和v_a_forward/v_a_backward=1），但必须保持两方向状态/边界flag同原源约束一致。若源码按真实约束拒绝该输入，记录精确异常并STOP，**不调参、不选另一个cell尝试**。在调用前应只读静态核对目标签名与界约束。若命令1不通过，则命令2明确NOT_EXECUTED。
**命令2：tiny-hjb-one-iteration。** 仅在命令1完成并证据闭合后，新的独立进程加载同一固定源码及同一合成参数，重新调用真实初始化**至多1次**为HJB提供必需的initial_value/baseline_labor，然后调用**真实 corrected solve_temp31_netwage_hjb 恰1次**，内部max_iterations=1，网格8单元。允许真实SciPy有限差分operator组装和一次小规模spsolve，仅为检测当前修正源码的实际运行时闭包；禁止KFE、完整HA batch、真实外层稳态、生产数据IO。严格记录调用是否到达policy及operator、结果/异常类型与简化堆栈（公开日志需脱敏）、max_iterations、是否产生有限结果、converged/iterations/statistic，如果converged=False如实标记并不自行加迭代。任何异常均为观察到的结果，STOP且不得改代码重试。

真实消费者的调用次数须从实际计数和入口代码支持，不允许仅在输出JSON填0/1。可增加测试入口本身的局部调用计数但**不可monkeypatch HJB/policy/economics来改变算法或返回值**，不允许在HJB内部额外打印秘密/整张微观值函数，输出限少量scalar汇总。

## 3. 明确白名单、候选与测试预算

只有新增文件：
- validators/multi_province/temp31_real_ha_tinygrid_smoke_isolated.py（一个明确--phase选择入口；实现外部30秒进程hard timeout与预算计数的方式必须在报告中说明）
- tests/test_temp31_real_ha_tinygrid_smoke.py（如需；只针对上述2阶段、无全套suite）
- tasks/CH5_TEMP31_REAL_HA_RUNTIME_TINYGRID_SMOKE_R1_20261029/（本任务结果与可验收证据）

不得修改src/ch5_two_asset_hank下任何现有源码、包__init__、R4/R5/R1/R2补丁或已经发布的原始证据。若发现新的HJB/runtime bug，**不要修补以继续运行**；记录所在固定源码行和真实异常、最多STOP，等GPT独立审阅及Owner另批修复。旧生产init/正式年度runner和MATLAB-faithful旧求解器保持只读。不能增加对旧包的隐式实证数据依赖或改科学参数去修复失败。可以新增最小签名/固定路径源身份读取器于任务目录，禁止额外未批准模块。

TEST_INVOCATIONS_MAX=2
IMPORT_INITIAL_POLICY_COMMANDS_MAX=1
TINY_HJB_COMMANDS_MAX=1
INITIALIZATION_BATCH_CALLS_TOTAL_MAX=2
DIRECT_LOCAL_POLICY_CALLS_MAX=1
HJB_DRIVER_CALLS_MAX=1
HJB_ITERATIONS_MAX=1
HJB_GRID_STATES_MAX=8
KFE_GE_IRF_CALLS=0
OUTER_STEADY_STATE_TURNS=0
DATA_EXCEL_READS=0
PRODUCTION_CODE_WRITES=0
NEW_GIT_REPOSITORIES=0
AUTO_MERGE=FALSE
AUTO_NEXT=FALSE

## 4. 证据、两阶段交付、STOP

提交给GPT独立审阅的固定候选至少包括：
- result.md（COMPLETED/BLOCKED/NOT_COMPLETED/NEXT_ACTION，严禁把异常变成PASS）
- source_identity.json（治理发布commit、实际源码parent/tree/Blob/raw SHA256、import与必要依赖，固定真实源码不能被虚假mock替代）
- import_dependency_closure.md（真实import结果，显式列出哪些包initializer有意跳过，任何源对象缺失）
- phase1_initial_policy_runtime.md（真实参数/网格/调用次数/摘要/异常）
- phase2_tiny_hjb_runtime.md（是否真实执行、初值来源/8单元/迭代次数/算子/solver/异常、是否未收敛）
- test_command_budget.json、raw_stdout/stderr_public+raw原件本地保留及redaction_record（必要时）、gap_register.md、privacy_report.md
- manifest.json（每个发布文件的Git Blob/bytes/SHA256）、DELIVERY_FINAL_RECEIPT.json（提交parent/tree和精确远端readback），必要LOCAL_ONLY外置停止回执。

未完整通过某阶段允许只提交真实已完成的静态/执行证据，并将后续阶段列NOT_EXECUTED，不准补跑、不准扩大预算。普通授权SSH在**新独立候选分支**上有界小批次payload后seal，逐步核验远端commit、parent、root tree、路径、Blob、实际bytes与SHA256；遇网络失败需记录真实SSH结果、远端有界只读HEAD消歧、不可自动push retry/换账号协议。Seal如果超出白名单必须STOP，不反复重建后偷偷推送。

回执中按A来源→B数学、运行时、数值及其真实性→C分层终审给出可复核材料。交付后STOP，GPT从固定远端候选独立A/B/C，Owner决定下步。无自动Issue/PR/Merge/Cleanup/Next；P3持续BLOCKED，V010不改、V011不开始，Results=FALSE，FORMAL_SOURCE_FREEZE=FALSE，REAL_GE=FALSE，FULL_RUNNER_IO_CLOSURE=BLOCKED。无“正式HA科学PASS”暗示。
