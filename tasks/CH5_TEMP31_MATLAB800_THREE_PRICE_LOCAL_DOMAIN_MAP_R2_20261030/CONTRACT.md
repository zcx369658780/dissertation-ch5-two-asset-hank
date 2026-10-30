# TEMP31 MATLAB800 三维价格局部区域探索 R2：原版HJB/KFE黑箱与两层驻定诊断

TASK_ID=CH5_TEMP31_MATLAB800_THREE_PRICE_LOCAL_DOMAIN_MAP_R2_20261030
STATUS=ISSUED_AWAITING_OWNER_TRANSFER
OWNER_APPROVAL=2026-10-30__RESUME_TEMP31_EXTERNAL_RAH_RB_WT_DOMAIN_EXPERIMENT_UNCHANGED_HJB_KFE_BLACKBOX
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=03b9b0d55b327ffe4412e043bb87f6b962a44569
TASK_PUBLICATION_COMMIT=EXACT_40_HEX_SUPPLIED_BY_GPT_AFTER_PUBLISH
EXPECTED_GOVERNANCE_REMOTE_HEAD=TASK_PUBLICATION_COMMIT_STRICT_EQUALITY
TASK_CONTRACT_PATH=tasks/CH5_TEMP31_MATLAB800_THREE_PRICE_LOCAL_DOMAIN_MAP_R2_20261030/CONTRACT.md
CANDIDATE_BRANCH=codex/ch5-temp31-matlab800-three-price-local-domain-r2-20261030
FIXED_PARENT=56447829ce0e6c3c85552c53c351b26a2452a4bd
SOURCE_COMMIT=56447829ce0e6c3c85552c53c351b26a2452a4bd
SOURCE_PARENT=a51c2e7ff6548340a1ee86857b0ee55792fa69b4
SOURCE_ROOT_TREE=7b7cb29dd5b37be92561e7f1bc688c0d29789732
LATEST_INDEPENDENT_REVIEW_COMMIT=03b9b0d55b327ffe4412e043bb87f6b962a44569
OWNER_MATLAB_PARAMETER_FREEZE_COMMIT=d3cc4ceb9d400f2aa00d26cbd577dcae8c5ef5d3
OWNER_MATLAB_KFE_METHOD_FREEZE_COMMIT=e6241bfa59317c93ef0eeb57d092e5ab3151ca10
PREVIOUS_SEVEN_POINT_FINAL=c46a6e5e7220009450cceaf5d59e6e4db7c34f11
PREVIOUS_KFE_REPLAY_FINAL=46fd085a98724f0bfefdea085502088e2f9ceb7f
HJB_BLACKBOX_IMMUTABLE=TRUE
KFE_METHOD_BLACKBOX_IMMUTABLE=TRUE
SOURCE_MODIFICATIONS=0
MAX_NEW_PRICE_POINTS=12
MAX_INITIALIZER_CALLS=12
MAX_HJB_DRIVER_CALLS=12
MAX_TOTAL_HJB_ITERATIONS=1200
MAX_KFE_SOLVES=12
MAX_SCIENCE_COMMANDS=12
FIRM_GE_IRF_REAL31_STAGE2_STAGE3_CALLS=0
NO_AUTO_ADAPTIVE_SEARCH=TRUE
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 0. 科研意义和不可改的原则

本任务仅在原MATLAB冻结HA格点及参数下，测量12个预先列明的三维价格点(rah,rb,wt)；重点是识别**局部离散HJB可收敛点、源MATLAB KFE计算可用点和有中间资产持有的探索性组合**，形成按实际试验点标注的有限价格邻域图，不冒充连续区域已经认证，也不启动阶段2省级资本/劳动供给或阶段3厂商/GE。

最新独立C结论：核心MATLAB风格KFE代码Blob及导出算法已在**有界KFE方法范围**冻结；四点KFE回放的被替换行之外原始驻定残差近机器精度，而被替换的行留下较大残差。Owner明确规定：HJB、KFE的MATLAB数学求解步骤均是黑箱，不为了后加严格驻定检查去改变KFE结果/算子；但不可隐匿余留驻定风险或把有风险分布冒称数学严格稳态。
旧八状态实验科学推断失效；旧20点及以上历史证据保留；原7点(含P2等)只能作为**只读参考锚点**，本次不能重跑它们来节约预算或追求数值一致性。核心/导出源码和全部既有证据/历史裁决不得修改；MATLAB原ZIP若本地安全库无原始bytes，只可使用Owner冻结及GPT独立原件核验记录作EXCERPT_PROVENANCE，不能访问P3/私有保护树/旧locked库或额外下载私人原件。

## 1. 唯一固定网格/HA偏好/KFE算法

b=linspace(-2,5,20), a=linspace(0,10,20), z=[.8,1.3], switch_matrix=[[-1/3,1/3],[1/3,-1/3]], Python shape(b,a,z)=(20,20,2), M=800, db=7/19, da=10/19。不得使用2×2×2或扩域 [-2,20]×[0,100]。
EconomicParams(rho=.05,gamma_c=2,phi=5,chi_0=.1,chi_1=2,a_bar=1e-6,mu_z=0,sigma_z=0)，原版消费权重1/劳动厌恶权重1、Frisch弹性.2；fixcost=fixcost2=0（原原版定义，不新增算法参数）。transfer_income=Tt=.1、borrowing_rate_gap=.07、目的地工资税率背景tau=.05、合成迁移楔=0、labor_weights=[1]。HJB唯一原数值设置delta=1000,max_iterations=100,convergence_tolerance=1e-7,drift_tolerance=1e-12；MATLAB homecrit=.01仅按现有合规外部只读观测，不能往黑箱补内部guard、更改delta、边界、spdiags或矩阵diagonal。
MATLAB KFE原版：后置post operator（由原HJB最后政策的资产漂移重构）A，AT=A'；MATLAB iFix=floor(.37*M)=296对应Python zero-based=295，替换AT第296行成单位行，rhs[iFix]=.007，spsolve，raw归一为g=raw/(sum(raw)*db*da)，Fortran reshape至(20,20,2)，依据原矩形积分权重计算At/Bt/Ct/Lt。不允许换行、改rhs、clip负密度、修改post A、隐含额外平滑/重新归一、把KFE算法改成严格零空间投影算法。
冻结核心源Git Blob：
src/ch5_two_asset_hank/temp31_netwage_hjb.py=56441c1c41ec94190997ce6f0ecbb2b5c2ca7b56
src/ch5_two_asset_hank/temp31_netwage_policy.py=d90eb4ba627d4c702062116c2a4ffadac0f43d86
src/ch5_two_asset_hank/temp31_netwage_economics.py=30528d55b884c62f3c9785dfe59197a61f125a3c
src/ch5_two_asset_hank/multi_province/temp31_ha_taxfree_bootstrap.py=b82eadea383a4d7546a11d4f19686440f8d71870
src/ch5_two_asset_hank/multi_province/temp31_ha_wage_debug.py=7df9c03fdd55d72beded7383866d683ca9356bc9
src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py=90667ddc00c72b9290e91481af4835c808ecfccb
src/ch5_two_asset_hank/matlab_faithful_operator.py=9a511e151c9bf449412dc5605dfa1a2076711277
src/ch5_two_asset_hank/matlab_faithful_kfe.py=4ccb7cec8c4754e91bd8830a95dc533811784391
src/ch5_two_asset_hank/contracts.py=c746b616bec38531a7d96da81a54e2899d8aba53
exports/matlab_faithful_two_asset_ha.py=e144c645d3f4dc842c2faa6b93b2ba0e24275dcf
所有实际使用的源须来自SOURCE_COMMIT相同字节并记录Blob/bytes/SHA256，不能改写、monkeypatch或替换数学函数。外部独立validator/只读wrapper不得改变输出/政策/算子；未完全认证源MATLAB-Python end-to-end等价，不得冒称通过。

## 2. 原7点只读基线与新12点顺序

历史合成800状态R1：
P0 (.09,.02,19) HJB 64轮收敛，KFE源法算出内部At≈7.274，b上边界质量≈.679；
P1 (.07,.02,19) 100轮未收敛；
P2 (.05,.02,19) 22轮收敛，KFE源法At≈5.072、Bt≈1.815、b上边界质量≈.249；
P3 (.07,.01,19) 100轮未收敛；
P4 (.07,.03,19) 12轮收敛；
P5 (.07,.02,15.5) 23轮收敛；
P6 (.07,.02,22) 100轮未收敛。
其中旧P0/P2/P4/P5的原KFE均返回了有限归一密度，但严格原postA'g残差>1e-7，旧外部严格认证未通过；这些历史证据不可改写/当作本轮新点。
P2是新实验**主要局部锚点**（其a分布与b集中度相对于其他历史成功点更有参考价值），但不是数学严格已认证稳态。

新12个点逐点固定，不得动态增加/改动/重排/自动补充，任何一个失败也不得自适应转点：
D00 rah=.045 rb=.020 wt=19
D01 rah=.055 rb=.020 wt=19
D02 rah=.060 rb=.020 wt=19
D03 rah=.050 rb=.015 wt=19
D04 rah=.050 rb=.025 wt=19
D05 rah=.050 rb=.020 wt=17
D06 rah=.050 rb=.020 wt=18
D07 rah=.050 rb=.020 wt=20
D08 rah=.050 rb=.020 wt=21
D09 rah=.055 rb=.025 wt=18
D10 rah=.045 rb=.015 wt=20
D11 rah=.070 rb=.025 wt=17
数值均为合成模型口径，不是统计实证工资/行业工资。全体候选在rah∈[.045,.07]、rb∈[.015,.025]、wt∈[17,21]中，但这**只是试验点的外包矩形，任何盒内未经测量的点均不可宣布可行**。P2与P4等历史点作为只读对照，不能把不同固定参数/数据源的历史扩域结果并入当前局部价格云。

## 3. 净工资来源和初始化硬门

对于wt=19的D00-D04，用原source numerical_bootstrap19→netwage_inputs，固定语义NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL。
对于非19的D05-D11，必须按上一轮R1已经批准/执行过的合成来源链：SyntheticNetWageCalculation→calculated_round_record→later_net_wage_record→netwage_inputs；只用两个虚拟A/B来源/目的地、phi_ji=1、sigma_ji=0、tau_j=.05、phi_l=5、alphal=1，各虚拟目的地同一firm_wage = wt/(.95*2^(5/6))。由源综合工资公式实际重算验证HJB净wt，误差≤1e-12。generated_after_iteration1、entering_iteration2只是合成来源见证标签，禁止宣称真实企业更新、真实跨省工资或经验数据。不得改source wage_record校验或设置fake真实工资身份；不能在HJB或政策中再次应用.05税/迁移楔。
每点必须调用同一真实source temp31_netwage_initial_arrays各一次产生本点独立V0和baseline_labor；不能warm start。记录init value/labor/consumption形状、极值、有限性、hash、root/brentq真实计数，遵循原冻结初始化方程，不可自作纠正。
运行前对全体12点工资来源、输入非负/有限、数组形状、旧新任务/HEAD/blob等进行无模型调用预检。若来源语义/固定文件身份无法验证，停止本任务科学执行，不能修补源/换条件/跳过硬门。

## 4. 四层独立数值评价，禁止隐匿KFE风险

每点先独立初值，再至多调用一次冻结HJB（最多100轮），记录实际迭代数、converged、deltaV轨迹/停止值、隐式方程代数一致性、post与iteration算子来源、row sums和上界相关量。原MATLAB HJB内部homecrit对照仅为外部观察；触发原MATLAB不应接受的严重问题，标SOURCE_PARITY_WARNING_OR_BLOCKED，不改黑箱/不宣称完整源等价。HJB没有源值函数收敛时，**不准执行该点KFE**，但允许在无权限/资源/计算hard-stop情况下按预定点表继续测量下一点。
HJB源收敛的点只调用原核心 matlab_faithful_kfe.solve_matlab_faithful_stationary_kfe(postG,...)，每点最多1次；原本身返回有限raw、density及合法normalization时记MATLAB_KFE_METHOD_EXECUTED=TRUE，不把额外严格原post驻定残差1e-7作为源KFE调用的成功硬门。源KFE如本身抛异常/非有限/归一为零或非法，记SOURCE_KFE_NUMERICAL_ERROR，并保留错误，不replay/不修算子。
外部结果必须至少分四层：
A HJB_SOURCE_CONVERGED=True/False（源停止逻辑）；
B MATLAB_KFE_METHOD_EXECUTED=True/False/NOT_RUN；
C SOURCE_METHOD_INTERIOR_CANDIDATE=True/False/NOT_EVALUATED（源KFE已给有限归一密度，且0<At<10；a内部格点质量>=.10、a两端各质量<=.50、a模态至少一个在内部、b内部格点质量>=.05。这些是R1继承的预注册探索性分布指标，不是MATLAB内核收敛条件）；
D STRICT_ECONOMIC_STATIONARITY_CERTIFIED=True/False/NOT_EVALUATED + 原始postG.T@g驻定残差、原post行和、最负密度/负质量、质量归一误差、被替换row295的残差及其余799行最大残差等。严格诊断继承原前序tol: post_original_stationarity_residual<=1e-7、质量偏差<=1e-8、负质量<=1e-8、污染行系统残差<=1e-7。KFE源方法计算成功但严格门失败时必须写SOURCE_KFE_COMPUTED_WITH_STATIONARITY_WARNING，**不得**隐瞒，也不得无说明地写KFE未执行/程序报错。
所有At/Bt/Ct/Lt都应基于真实未改的g及grid用db*da积分；公开可独立重算的20维a_mass、b_mass、上下边界和内部mass、模态、At距界限、负密度格数。不得clip/abs负密度。额外加入非约束的B_UPPER_BOUNDARY_WARNING=(b上边界质量>=.50)，仅用于排序优先探索候选，不改变原MATLAB数值算法或R1内点判据。若a/b质量不可信，给出条件性/未认证标签，禁止作为正式31省资产供给。
无已认证严格驻定点时，也允许呈现**源方法可计算性**与探索性资产内部条件的离散图；但不能声称严格驻定价格区域已存在。数值评价与理论解释均不得把连续插值、外包矩形或算法执行成功等价为联合GE稳态成功。

## 5. 模型调用/本地资源预算及隐私门

新价格点≤12，科学主命令≤12，initializer≤12，真实HJB driver≤12，实际HJB loop-entry总≤1200，HJB局部policy≤960000，真实KFE≤12，且仅HJB源收敛点可KFE。每点最多一条实际受监督Python子进程；单命令180秒硬超时、最多1活动科学子进程、Windows Job或等效真正1GiB进程committed-memory硬上限、六种BLAS/OMP/MKL/NUMEXPR/VECLIB/BLIS环境线程变量各1，在科研import前完成握手与硬限制；不能执行额外试点、重复HJB、重试失败点或重复运行P2。任何安全/资源/权限hard-stop立刻停止整任务，留下部分证据。科学预算不够时STOP，不准拆分任务规避。
每点必须保留实测计数和supervisor原始日志的bytes/SHA256，原始stdout/stderr、计算完整800状态向量、postG CSR数据若包含LOCAL_ONLY研究字节，保留在本地授权位置并以身份绑定，不要自动发布私有路径/二进制。公开足够数学诊断字段、20-bin密度边缘、每轮deltaV摘要与各run参数/root来源。Native线程数如未能实际测量只能标NOT_MEASURED；RSS不同于process committed-memory，不得混称。
本任务特别吸收上一轮隐私恢复经验：对所有publication JSON paths、source_identity与stdout记录的private Windows path、JSON双反斜杠转义、私人原始文件名称等**在事先允许的公开副本**作安全角色前缀及分隔符标准化，原原始文件和原科学数值数据保留原字节，逐字段脱敏原件bytes/SHA与公众bytes/SHA/Blob、转换记录须可审计；不得忽略、修改、放宽或关闭强制隐私扫描规则。Public file白名单逐件扫描通过才可提交；隐私硬门失败STOP并零push，不能循环尝试无界修复。

仅授权Stage1家户HA，真实31省Excel/统计工资/firm/GE/IRF/社会最优福利/政策模拟/Stage2/Stage3的模型调用严格为0，Results与model_activation保持FALSE。

## 6. 固定路径、payload→seal和独立STOP

允许只读固定科学source_commit列举的HA/HJB/KFE/wage依赖、原Owner冻结合同、最近GPT KFE独立终审和历史7价格点的**已发布摘要/边缘分布/来源身份**。不准读P3/旧锁仓、未经授权MATLAB私人路径/新经济Excel/其他connector私有资源。老任务完整LOCAL_ONLY档案若非本任务必要不必访问，禁止借用当作本轮新结果。
允许新增唯一独立validator：validators/multi_province/temp31_matlab800_three_price_local_domain_r2_isolated.py
以及 tasks/CH5_TEMP31_MATLAB800_THREE_PRICE_LOCAL_DOMAIN_MAP_R2_20261030/ 下 result.md、point_grid.json、baseline_anchor_readback.md、source_identity.json、preflight.json、wage_provenance.md、每点evidence、point_result_matrix.md、interior_domain_map.md、stationarity_warning_panel.md、budget.json、gap_register.md、privacy_report.md、manifest.json、DELIVERY_FINAL_RECEIPT.json、必要安全supervisor/纯静态测试证据。不得新增或编辑任何src、exports、原有validator、历史tasks/docs/原始科研Excel，或修改HJB/KFE数学代码。
治理branch发布本合同后，Codex必须先从GitHub查验远端HEAD=GPT提供的TASK_PUBLICATION_COMMIT，parent=03b9b0d55b327ffe4412e043bb87f6b962a44569、diff仅新CONTRACT、blob身份一致；再在已授权且经过预检的独立安全repo上从SOURCE_COMMIT新建唯一candidate codex/ch5-temp31-matlab800-three-price-local-domain-r2-20261030（不能从治理HEAD、上轮R1候选或KFE回放候选派生）。新repo/worktree/覆写老任务证据/clean/reset/rebase/history rewrite/force-push一律禁止。旧候选安全状态有歧义则STOP。
仅在全部科学执行和审阅证据/隐私硬门通过时，在candidate从SOURCE_COMMIT创建单一payload commit。普通授权SSH最多push一次并从远端readback commit/parent/root tree及每文件Blob、bytes、SHA256；确认后再创建仅增DELIVERY_FINAL_RECEIPT.json的seal commit、再普通SSH push最多一次并远端完整readback。seal commit的最终自身SHA/tree由外置LOCAL_ONLY回执绑定，避免循环自引用。任何权限拒绝/SSH网络不确定仅允许只读有界确认，禁止盲目重复或更换认证账号/协议。
必须提供完整可复核的每点价格、初始化来源、真实求解轮次/终态、KFE是否执行、源方法返回、20bin a/b、At/Bt、额外驻定残差、被替换行与未替换行、隐私/预算、短论文风格经济含义、严格科学解释边界，以及明显未完成的真实性与全系统源等价性。manifest逐文件记录源Git Blob/实际bytes/SHA256/目的/provenance，PUBLIC_DERIVATIVE需记录原始身份与脱敏字段语义。至少对一个HJB收敛+KFE可计算点和一个不收敛/警告点给出完整回读与足够数学证据。
交付成功后STOP__AWAITING_GPT_INDEPENDENT_ABC；若安全/隐私/执行hard stop则STOP并报真实部分结果且不允许越界提交。禁止自动Issue/PR/merge/cleanup/next task。报告payload/final sha/parent/tree、模型调用总预算、12点逐点分类、源冻结Git Blob、未证源问题与风险。GPT随后A远端身份→B数值与经济→C分层裁决；Owner再决定是否新任务。

## 7. 正式状态保持

P3=BLOCKED
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
