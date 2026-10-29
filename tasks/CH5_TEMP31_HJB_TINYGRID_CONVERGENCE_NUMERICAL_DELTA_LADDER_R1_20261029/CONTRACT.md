# TEMP31：真实HJB 8状态收敛诊断与Owner授权的数值步长调参 R1

TASK_ID=CH5_TEMP31_HJB_TINYGRID_CONVERGENCE_NUMERICAL_DELTA_LADDER_R1_20261029
STATUS=ISSUED_AWAITING_OWNER_TRANSFER
OWNER_AUTHORIZATION=2026-10-29__CONTINUE_HJB_CONVERGENCE_CHECK__IF_NOT_CONVERGED_FIRST_TUNE_NUMERICAL_PARAMETERS
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=17eb34072d006bb92ea7517d6ec92e62baea1957
TASK_PUBLICATION_COMMIT=EXACT_40_HEX_TO_BE_SUPPLIED_BY_GPT_AFTER_PUBLICATION
EXPECTED_REMOTE_GOVERNANCE_HEAD=TASK_PUBLICATION_COMMIT__STRICT_EQUALITY
TASK_CONTRACT_PATH=tasks/CH5_TEMP31_HJB_TINYGRID_CONVERGENCE_NUMERICAL_DELTA_LADDER_R1_20261029/CONTRACT.md
FIXED_PARENT=ffdb7fcd41019bed7ce4652ee01c753bff6fcec8
SOURCE_COMMIT=ffdb7fcd41019bed7ce4652ee01c753bff6fcec8
SOURCE_ROOT_TREE=0e2c278ff8915c43dce0ccda8de82e02fe607fe7
SOURCE_PARENT=aa380ce3247feed25f67deddd09b387e313a7f96
CANDIDATE_BRANCH=codex/ch5-temp31-hjb-convergence-delta-ladder-20261029-r1
PREVIOUS_TASK=CH5_TEMP31_REAL_HA_RUNTIME_TINYGRID_SMOKE_R1_20261029
PREVIOUS_FINAL_REVIEW_COMMIT=17eb34072d006bb92ea7517d6ec92e62baea1957
PREVIOUS_CONCLUSION=PASS_BOUNDED_REAL_HA_8_STATE_ONE_ITERATION_RUNTIME_SMOKE__NOT_CONVERGED
AUTHORIZED_NUMERICAL_ARMS=BASELINE_DELTA1000__FALLBACK_DELTA100__FALLBACK_DELTA10
MAX_HJB_DRIVER_CALLS=3
MAX_HJB_ITERATIONS_PER_ARM=80
MAX_HJB_ITERATIONS_TOTAL=240
MAX_MODEL_TEST_COMMANDS=3
MAX_SUPERVISED_COMMAND_WALL_SECONDS=30
MAX_TOTAL_COMMAND_WALL_SECONDS=90
MAX_GRID_CELLS=8
MAX_TOTAL_HJB_POLICY_CELLS=1920
KFE_GE_IRF_CALLS=0
OUTER_STEADY_STATE_TURNS=0
REAL_31_PROVINCE_CALLS=0
SYNTHETIC_DATA_ONLY=TRUE
EXISTING_SCIENTIFIC_SOURCE_MODIFICATIONS=0
NEW_GIT_REPOSITORIES=0
NEW_WORKTREES=0
DEPENDENCY_INSTALLATIONS=0
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 0. 科学授权边界与前序结果

Owner已明确批准：继续进入HJB收敛阶段；**如果不收敛，首先调整数值参数**。本任务据此冻结最多三组数值设置，不能由Codex自行搜索新参数。前序2026-10-29真实8状态smoke只允许一次内层迭代：delta=1000、tolerance=1e-7、converged=False、收敛变化0.39023953207066997、所有检查结果有限。该单轮不收敛并不意味着在更大迭代预算下永不收敛。当前任务先以原delta延长最多80轮；如确实未收敛但没有错误，才顺序执行预批准delta调参。**除了delta与max_iterations这个数值预算，全部科学/经济参数必须固定**。

严禁调整rho、gamma_c、phi、chi、a_bar、mu_z、sigma_z、真实tau_j、sigma_ji、工资19数值起点、资产收益/转移、生产函数、HJB源方程、operator、网格、容差以及任何经验数据。禁止反复寻找“更容易收敛”的经济学标定；不执行二阶经济模型调参。本次调参只是伪时间步长对求解器稳定性的受界敏感性试验，不是经验证的经济机制修订。通过收敛门亦不能证明经济校准、模型量纲、KFE/GE闭合、财政或31省稳态成立。

## 1. 严格来源与保护门

1. 仅使用先前已经安全批准的同一个R3/R4/R5/R1/R2/HA-smoke独立Git仓库；先无follow只读确认源对象库、refs、隔离路径、未跟踪目录和本次分支创建安全，禁止触碰旧shallow.lock仓库、P3保护科研树、reparse/WASM、历史模型或本地真实Excel。严禁新建仓库、worktree、reset、rebase、clean、覆盖旧candidate/evidence及自动清理。安全异常即STOP。
2. GPT发布后由Owner提供精确40位TASK_PUBLICATION_COMMIT。现有普通SSH受界只读确认治理分支HEAD必须**严格等于发布SHA**，其唯一parent必须=17eb34072d006bb92ea7517d6ec92e62baea1957，diff只能新增本合同；不能把治理HEAD当作科学SOURCE_COMMIT；权限拒绝、漂移或SSH不明即STOP，不换账号/Key/协议绕过。
3. 科研来源为已获GPT独立A/B/C有界审阅的8-state runtime smoke最终候选：固定ffdb7fcd41019bed7ce4652ee01c753bff6fcec8；唯一parent=aa380ce3247feed25f67deddd09b387e313a7f96，root tree=0e2c278ff8915c43dce0ccda8de82e02fe607fe7。当前既有候选branch须在原始读取时严格等于SOURCE_COMMIT。新独立candidate仅从FIXED_PARENT生成，保留旧所有冻结历史。
4. 核验真实执行所需8个科研模块的fixed Git Blob/raw身份和来源，均必须同上轮源恒等（本轮禁止改动）：
   - src/ch5_two_asset_hank/multi_province/temp31_ha_taxfree_bootstrap.py Blob b82eadea383a4d7546a11d4f19686440f8d71870；
   - src/ch5_two_asset_hank/temp31_netwage_hjb.py Blob 56441c1c41ec94190997ce6f0ecbb2b5c2ca7b56；
   - src/ch5_two_asset_hank/temp31_netwage_policy.py Blob d90eb4ba627d4c702062116c2a4ffadac0f43d86；
   - src/ch5_two_asset_hank/temp31_netwage_economics.py Blob 30528d55b884c62f3c9785dfe59197a61f125a3c；
   - src/ch5_two_asset_hank/contracts.py Blob c746b616bec38531a7d96da81a54e2899d8aba53；
   - src/ch5_two_asset_hank/matlab_faithful_operator.py Blob 9a511e151c9bf449412dc5605dfa1a2076711277；
   - src/ch5_two_asset_hank/multi_province/temp31_ha_wage_debug.py Blob 7df9c03fdd55d72beded7383866d683ca9356bc9；
   - src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py Blob 90667ddc00c72b9290e91481af4835c808ecfccb。
5. 复用上轮已经验证的固定源码原字节（如本地只读认证的LOCAL_ONLY source cache），无权新下载科研原件、补充Git fetch或物化到历史保护树；如缺必需对象即STOP，不能伪造补丁。允许按上轮已独立审阅的**两套ModuleType隔离namespace shell**绕过ch5_two_asset_hank/__init__.py与multi_province/__init__.py；数学函数必须用真实SourceFileLoader加载，严禁mock/monkeypatch真实initializer、policy、HJB、operator、spsolve和返回值，且记录跳过包初始化导致生产导入不被验证。
6. 已安装Python、NumPy、SciPy；不得pip/conda联网装包，不读取真实31省原始资料，不修改src、__init__、生产runner或模型参数。在命令前检查上轮固定诊断driver/supervisor的实际源码身份，新增脚本须为纯数值控制、监控及证据模块，不得影响数学函数和返回值。

## 2. 冻结唯一网格、工资、模型参数及伪时间步长序列

复用上轮R1真实HA smoke的同一合成输入、相同数组/初值/劳动根方程，不以新实验内容复写旧结果。对所有arms固定：
- context_id=TEMP31_TINY_HA_SMOKE_SYNTHETIC_20261029；province_order=("A","B")；entering_iteration=1；origin_index=0。
- numerical_bootstrap19: w_initial=20.0，tau_legacy_reference=0.05，HA effective wage=19.0，真实tax_by_destination=(0.05,0.05)、sigma_destination_origin=((0,0),(0,0))保存在工资来源记录，不能设置真实税率0。
- r_a=.09；r_b=.02；rb_gap=.07；Tt=.1；labor_weights=(1,)。
- EconomicParams(rho=.05,gamma_c=2.0,phi=5.0,chi_0=.1,chi_1=2.0,a_bar=1e-6,mu_z=0,sigma_z=0)。
- grid.b=(-2.0,5.0)，grid.a=(0.0,10.0)，grid.z=(0.8,1.3)，switch_matrix=((-1/3,1/3),(1/3,-1/3))；shape=(2,2,2)，总state=8。
- convergence_tolerance=1e-7，drift_tolerance=1e-12，all arms max_iterations=80。
- Arm A: delta=1000.0，先执行一次真实HJB，至多80轮。
- **仅若Arm A在80轮内真实未收敛、但所有数值有限且无异常**，Arm B: delta=100.0，重新从同一不变初值启动一次真实HJB，至多80轮；不从A终值热启动。
- **仅若Arm B真实仍未收敛、但无异常**，Arm C: delta=10.0，重新从相同原初值启动一次真实HJB，至多80轮。
- 任一Arm达到下面的有界数值验收即停止，不执行更小delta、更大迭代、第四条命令、重新选初值或进一步调试。如发生异常、NaN/Inf、生产安全问题、超时、source drift、数值非法或budget越界，也必须STOP，不能把异常自动解释为一般“未收敛”从而换delta重试。
- 三个Arm仍未收敛时，如实标NUMERICAL_CONVERGENCE_NOT_ESTABLISHED_AFTER_FROZEN_LADDER；只允许报告诊断与科学风险，不能现场改算子或任何经济参数，也不自动创建修复任务。

## 3. 收敛监测与有限指标（不能仅以bool判定）

1. 为每Arm建立独立同一基线真实源加载及初始化；仅调用真实temp31_netwage_initial_arrays一次生成初值、真实corrected solve_temp31_netwage_hjb一次、最多80轮。每轮8个policy单格，最多每Arm640次；source operator每完成一次内层迭代后组装1次，并有最后post-iteration组装1次（最多每Arm81）；最多每Arm80次SciPy spsolve。全梯形最多3个HJB driver、240轮、1920内部policy单格。初始化最多3批、24个root/brentq；KFE/GE/IRF=0；不运行31省或完整suite。
2. 沿用/明确证明上一轮经过审阅的sys.setprofile源代码对象计数与sys.settrace进入HJB for-loop的真实行监测，记录循环实际次数、真实policy调用/算子组装/线性求解和单条进程退出状态。不能只在最终JSON手填计数；不能将trace工具改造成替换政策函数的模拟器。需通过原HJB真实局部变量读取（只读监测）得到每轮delta V supnorm的有界序列，建议仅写各轮标量、极值/增长比、非有限与异常，不保存敏感微观数组，不额外执行完整HA以获取残差。
3. 用返回的最后一次policy utility和最后一次来源operator G，在**相同source Fortran-order flatten**下，计算**冻结最后政策的离散残差诊断** R_stale = supnorm(rho*V_new - u_last - G_last@V_new)；同时独立核验数学一致性 R_stale≈supnorm(V_old - V_new)/delta，仅限上轮隐式步关系的代数审计（容许浮点舍入）。**该R_stale并非在V_new上重新优化政策后的完整非线性Bellman残差**，不得标“真HJB残差已完整验证”；不多调用policy或HJB以重算新政策。
4. 输出HJB实际result.converged、result.iterations、result.convergence_statistic、每轮变化序列、数值finite性，operator.shape、nnz、最大行和、最小offdiag、稀疏求解有限性、最终consumption/labor/drift及utility的finite性；如row-sum/offdiag出现异常，只作可追踪源算子诊断并标科学风险，不偷偷修改/重组operator。若非有限、不可解或明确数值非法，则STOP，不继续数值调参。
5. **有界收敛认证**仅限以下同时成立：真实HJB result.converged=True、迭代次数<=80、convergence_statistic<1e-7、所有相关返回数组/operator数据有限、R_stale<=1e-7且隐式步代数一致。此时状态PASS_BOUNDED_NUMERICAL_FIXED_POINT__STALE_POLICY_RESIDUAL_CHECKED，而不是完整HJB最优性、KFE/GE稳态或经验收敛。若HJB flag=True但残差异常/算子检查显示严重不一致，标INCONSISTENT_STOP，不能移步调参或虚报通过。若到80轮仍False且结果有限且无异常，自动进入下一项**本任务内已经Owner明确批准**的固定数值delta阶梯，不征求额外科学参数授权。
6. 环境：每条Arm由外部监督启动一个独立科学进程，严格30秒墙钟超时；Windows Job限一个活动科学进程、process committed memory最多1GiB（若硬限不可设须如实标UNAVAILABLE并STOP或严格遵守旧合同安全门），BLAS六个线程环境项全设1且记录native线程实测是否available；不声称未监测的native线程个数。每条cmd事前产生不可覆盖的claim，stdout/stderr原始本地保留、公开本只作精确路径脱敏并记录raw/public bytes/SHA256，失败不重跑。每个Arm一条真实科学命令，最多3条，总预算耗尽不能以“诊断命令”继续运行模型。
7. 若观察到数值平台相关不稳定或delta阶梯趋势不单调，忠实记录，不推断科学模型无法收敛或财政公式错误。只用真实固定值和严格指标表述结果，科学结论最高为数值收敛有界（8-state、single-origin、uniform-tax、zero-sigma）。

## 4. 仅新增实验与证据文件（不可改旧源）

允许新增：
- validators/multi_province/temp31_hjb_convergence_delta_ladder_isolated.py（专用命令入口，复用或源身份认证后导入上一轮已发布真实loader，不mock HJB）
- tasks/CH5_TEMP31_HJB_TINYGRID_CONVERGENCE_NUMERICAL_DELTA_LADDER_R1_20261029/run_convergence_supervised.py（如需要，只有外部监督、条件Arm gate、内存/超时/预算，不修改数学）
- tasks/CH5_TEMP31_HJB_TINYGRID_CONVERGENCE_NUMERICAL_DELTA_LADDER_R1_20261029/（source_identity.json、数值arm配置、逐轮标量证据、预算、运行记录、报告、manifest、seal）

禁止修改src、历史tests、validators原R1 smoke、已冻结证据及其他Task目录；不得新增任何其他路径。治理分支仅放任务合同，科研候选仅从SOURCE_COMMIT派生，不从治理HEAD派生。若旧监测代码需要调整，**仅在本任务新增入口**中通过非数学的监测实现，不改旧文件。用户批准的“调参”是修改测试调用时传入的numerics.delta，**不是修改HJB实现/既有参数源文件**。

## 5. 交付、证据、终态与审阅

每个Arm记录NOT_RUN/PASS_BOUNDED/NOT_CONVERGED_FINITE/STOP_EXCEPTION；条件跳过必须提供上一个Arm的真实终态与机器可复核依据。结果应列出按顺序实际触发的delta、max_iter、真实迭代数、末值变化、完整标量轨迹或节制量化轨迹、stale-policy离散残差、solver算子状态与是否finite、实测调用预算；若未收敛切换delta，要明确这只是数值求解器参数调整。严格保存所有执行claim、原始日志hash、脱敏记录、错误堆栈、预算、完整来源身份、隐私报告、gap_register与非重运行证据。

交付至少：result.md、source_identity.json、numerical_tuning_contract.json、arm_A_baseline.md、arm_B_delta100.md、arm_C_delta10.md、convergence_diagnostic_matrix.md、test_command_budget.json、privacy_report.md、gap_register.md、manifest.json（每文件bytes/SHA-256/Git Blob/来源）、DELIVERY_FINAL_RECEIPT.json（commit/parent/tree/远端回读），必要evidence/下逐命令raw/public日志与精确receipt。若Arm B/C没有执行必须交NOT_EXECUTED记录，不伪造输出。

普通已批准SSH对唯一新隔离候选分支做有界两阶段payload→seal交付，逐阶段精确远端HEAD/parent/root tree、Git Blob、bytes、SHA256回读。封存提交阶段只能新增一个指定DELIVERY_FINAL_RECEIPT.json；若候选seal出现超出白名单应STOP，不像过去那样事后默许。网络SSH不确定须只读查HEAD消歧，不自动重复push或更换认证。不得清理、Issue、PR、merge、生成下一任务或修改受保护目录。完成后STOP，等待GPT独立A/B/C：区分A来源/原字节、B真实数值与参数台阶、C收敛与科学上下限。

禁止自动推进任何经济学模型的新情景、HA/KFE/GE/IRF、真实省际非对称工资税或31省数据。即使8-state收敛，也不允许据此把Results设TRUE。

ACTIVE_TASK=ISSUED_AWAITING_OWNER_TRANSFER
PROTECTION_BASELINE=BLOCKED
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
