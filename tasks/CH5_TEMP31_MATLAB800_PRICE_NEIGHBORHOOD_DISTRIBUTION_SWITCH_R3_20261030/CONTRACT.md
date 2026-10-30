# TEMP31 R3 原MATLAB800状态：三价局部邻域与资产分布离散跃迁有界试验

TASK_ID=CH5_TEMP31_MATLAB800_PRICE_NEIGHBORHOOD_DISTRIBUTION_SWITCH_R3_20261030
STATUS=ISSUED_AWAITING_OWNER_TRANSFER
OWNER_APPROVAL=2026-10-30__CONTINUE_STAGE1_TEMP31_BOUNDED_PRICE_NEIGHBORHOOD_STUDY
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=a63b85af20182e0431d8f9a95ab839e90bae3159
TASK_PUBLICATION_COMMIT=GPT_SUPPLIES_EXACT_40_HEX_AFTER_PUBLISH
EXPECTED_GOVERNANCE_REMOTE_HEAD=TASK_PUBLICATION_COMMIT_STRICT_EQUALITY
TASK_CONTRACT_PATH=tasks/CH5_TEMP31_MATLAB800_PRICE_NEIGHBORHOOD_DISTRIBUTION_SWITCH_R3_20261030/CONTRACT.md
CANDIDATE_BRANCH=codex/ch5-temp31-matlab800-price-neighborhood-r3-20261030
FIXED_PARENT=56447829ce0e6c3c85552c53c351b26a2452a4bd
SOURCE_COMMIT=56447829ce0e6c3c85552c53c351b26a2452a4bd
SOURCE_PARENT=a51c2e7ff6548340a1ee86857b0ee55792fa69b4
SOURCE_ROOT_TREE=7b7cb29dd5b37be92561e7f1bc688c0d29789732
LATEST_INDEPENDENT_R2_REVIEW_COMMIT=a63b85af20182e0431d8f9a95ab839e90bae3159
LATEST_INDEPENDENT_R2_REVIEW_BLOB=5dbc7920dcfbf4a60b580dda64038335c54a993e
R2_FINAL_SEAL_COMMIT=ffb156712e56bd2fe24924ba40295858ad67e18f
R1_FINAL_SEAL_COMMIT=c46a6e5e7220009450cceaf5d59e6e4db7c34f11
OWNER_HA_PARAMETER_FREEZE_COMMIT=d3cc4ceb9d400f2aa00d26cbd577dcae8c5ef5d3
OWNER_KFE_METHOD_FREEZE_COMMIT=e6241bfa59317c93ef0eeb57d092e5ab3151ca10
CURRENT_GITHUB_WORKFLOW_PATH=docs/CH5_GITHUB_WORKFLOW_AUTHORITY_CURRENT_20261025.md
HJB_MATLAB_BLACKBOX=IMMUTABLE
KFE_MATLAB_BLACKBOX=IMMUTABLE
EXISTING_SCIENTIFIC_SOURCE_MODIFICATIONS_MAX=0
MAX_NEW_PRICE_POINTS=12
MAX_INITIALIZER_CALLS=12
MAX_HJB_CALLS=12
MAX_HJB_ITERATIONS_TOTAL=1200
MAX_POLICY_CELLS_TOTAL=960000
MAX_KFE_CALLS=12
MAX_SCIENCE_SUBPROCESS_COMMANDS=12
OTHER_MODEL_CALLS=0
AUTO_ADAPTIVE_NEXT_POINT=FALSE
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 0. 科研问题、证据等级与授权界限

Owner批准继R2 800状态局部区域实验后继续TEMP31第一阶段研究，重点检验：在rah=.05/rb=.02和净综合工资wt从19到20之间，**源HJB收敛和原MATLAB方法KFE输出的条件性资产分布**是否出现显著离散跳动；接着在wt=19.5邻域考察rb扰动，以及D09/D11低b上界集中候选附近的两/三价格联合变化。所有实验点事先冻结；没有正当证据可由某个单点宣称整个连续价格区间、真实经济分岔、真实31省稳态或GE固定点已证明。此任务不是动态改经济参数的许可，更不是搜寻“严格驻定零残差”而修改KFE。

原R2终审给出12点中11点HJB源停止收敛、11点原版风格KFE求得有限归一化g、10个探索性内部资产候选、0个严格驻定认证。D10虽At在区间内但a=0节点mass≈.725、模态在边界，失败；D00第72轮源迭代矩阵max|row sum|>.01，被原MATLAB homecrit约束警告。其他历史7点不得以8状态结论覆盖。所有既有执行、审阅、STOP、来源Git Blob不许更动或自动改标签。

## 1. 唯一固定HA网格、参数、算法和源身份

原MATLAB参考唯一网格：
b=np.linspace(-2,5,20)，a=np.linspace(0,10,20)，z=np.array([.8,1.3])，Q=[[-1/3,1/3],[1/3,-1/3]]。Python数组严格shape=(b,a,z)=(20,20,2)，800状态；db=7/19，da=10/19。严禁2×2×2、旧扩域a_max100/b_max20或其他资产分辨率。
固定经济参数EconomicParams(rho=.05,gamma_c=2,phi=5,chi_0=.1,chi_1=2,a_bar=1e-6,mu_z=0,sigma_z=0)，原MATLAB消费/劳动权重1，Frisch=.2，固定成本0；Tt=.1，rb_gap=.07，工资税率来源背景tau=.05，合成迁移楔0，labor_weights=[1]。
HJB数值：delta=1000,max_iterations=100,convergence_tolerance=1e-7,drift_tolerance=1e-12。原MATLAB num.homecrit=.01，只读监测迭代operator（含首次阈值超出的实际轮次）；现Python未在内部等价实现guard，不能为本任务修补黑箱或假装二者完全等价。原数学BB/AAH/Bswitch、policy selector、边界、默认初值/返回、source post operator均不可改。
KFE原版：只使用HJB返回的post-convergence A，transpose、替换floor(.37*800)-1=295零基行、rhs[295]=.007、原spsolve、sum(raw)*db*da归一、F-order reshape、按grid积分。不得通过更换pin行、修row sums、改diagonal、clip负率或密度等方式人为改善后验残差。原postA.T@g额外严格检验不属于原MATLAB求解算法内部硬门，保留独立风险记录。
冻结Python SOURCE_COMMIT下必须实际核验的核心blob：
- src/ch5_two_asset_hank/contracts.py c746b616bec38531a7d96da81a54e2899d8aba53
- src/ch5_two_asset_hank/multi_province/temp31_ha_taxfree_bootstrap.py b82eadea383a4d7546a11d4f19686440f8d71870
- src/ch5_two_asset_hank/multi_province/temp31_ha_wage_debug.py 7df9c03fdd55d72beded7383866d683ca9356bc9
- src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py 90667ddc00c72b9290e91481af4835c808ecfccb
- src/ch5_two_asset_hank/temp31_netwage_hjb.py 56441c1c41ec94190997ce6f0ecbb2b5c2ca7b56
- src/ch5_two_asset_hank/temp31_netwage_policy.py d90eb4ba627d4c702062116c2a4ffadac0f43d86
- src/ch5_two_asset_hank/temp31_netwage_economics.py 30528d55b884c62f3c9785dfe59197a61f125a3c
- src/ch5_two_asset_hank/matlab_faithful_operator.py 9a511e151c9bf449412dc5605dfa1a2076711277
- src/ch5_two_asset_hank/matlab_faithful_kfe.py 4ccb7cec8c4754e91bd8830a95dc533811784391
- exports/matlab_faithful_two_asset_ha.py e144c645d3f4dc842c2faa6b93b2ba0e24275dcf
原MATLAB ZIP sha256 ceb94ccf34d2d218722b81e5111a8f4c530571a9f886bd4afe0610a00321f755，HANK_2ASSETS_HJB.m sha256 049136b769560040bc678f828f5d3ec5338ddcaa2090d6bed4e40732f56c3eae。Codex若未在授权隔离目录拥有MATLAB原始字节，按之前Owner摘录做有界来源对照，MATLAB_RAW_LOCAL_VERIFICATION=NOT_AVAILABLE；不得进入P3、旧锁库、原私有目录或另外下载私人文件。

## 2. 预冻结12点：价格、顺序和单次源初始化

每点唯一变化变量rah、rb、wt，其中wt是HJB实际接收的已一次扣税的净综合工资数值，非原厂商wjt、非真实省级统计工资。按顺序且只各运行一次，不新增/替换/自适应找边界：
E00: rah=.050 rb=.020 wt=19.10
E01: rah=.050 rb=.020 wt=19.25
E02: rah=.050 rb=.020 wt=19.50
E03: rah=.050 rb=.020 wt=19.75
E04: rah=.050 rb=.020 wt=19.90
E05: rah=.050 rb=.0175 wt=19.50
E06: rah=.050 rb=.0225 wt=19.50
E07: rah=.055 rb=.025 wt=17.00
E08: rah=.055 rb=.025 wt=19.00
E09: rah=.060 rb=.025 wt=18.00
E10: rah=.065 rb=.025 wt=17.00
E11: rah=.070 rb=.025 wt=18.00

R2旧D06(.05,.02,18)、历史R1 P2(.05,.02,19)、R2 D07(.05,.02,20)、D08(.05,.02,21)是价格截面只读锚点；D09(.055,.025,18)、D11(.07,.025,17)和D03/D04(.05,.015/.025,19)是其他参考点。需在输出保留原commit/点ID/价格/来源标签，不把历史数值作为新的HJB或KFE调用。12点全部严格沿用原网格/初始构造/冷启动；不跨点warm-start，也不以临近已收敛值替代V0。

**所有E00-E11均非19的点**使用源合成净工资见证流程，唯E08的19须走原有numerical_bootstrap19链（参见下一节）；不得把E08错当非19，不能用合成工资回路标称首轮真实工资。

## 3. 净工资见证、初始化与预检

对于E08（wt=19），遵循源numerical_bootstrap19→netwage_inputs，标签NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL。
对于其余E00-E07、E09-E11，遵循冻结source SyntheticNetWageCalculation→calculated_round_record→later_net_wage_record→netwage_inputs；统一两个虚拟A/B地区，phi_ji=1，sigma=0，目的地tau_j=.05，phi_l=5，alphal=1，两个虚拟目的地等值合成firm_wage=wt/(.95*2^(5/6))。使用源公式重算并确认有效wt误差<=1e-12、来源context/顺序/税一次应用均合格。generated_after_iteration=1、entering_iteration=2仅为合成见证逻辑元数据，绝非真厂商回调；不得绕过现有provenance验证或为wt强造boot19。
12点全部工资链预检必须在任何真实HA初始化/HJB调用前完成，预检非法或源文件身份不符就STOP。每点从既有source temp31_netwage_initial_arrays独立初始化V0、l0，按源root/brentq原算法；记录本点grid、初值shape/有限性/最小最大/hashes、源首轮消费方程来源与经一次扣税工资。原初始化effective_return**2的原版来源仍照搬，解释有争议只登记，不擅自修正。每点不得修正经济参数以实现收敛。

## 4. 事前注册的科学层次、离散跃迁指标和风险

第一层HJB_SOURCE_CONVERGED：记录源标准converged=True且deltaV<1e-7、迭代轮数<=100、逐轮deltaV轨迹、冻结operator真实row sum/其他数学统计、初值身份、隐式线性一致性。若HJB不收敛则本点KFE=NOT_RUN；原MATLAB homecrit=.01 若在任一轮被超过，应标SOURCE_PARITY_WARNING_OR_BLOCKED，不能将阈值超后Python轨迹冒充MATLAB本来会继续的轨迹，不改源内部guard。无资源/安全全局hard-stop时允许按表继续下一点。
第二层MATLAB_KFE_METHOD_EXECUTED：仅HJB源停止收敛点允许调用固定核心matlab_faithful_kfe.py KFE一次。源KFE有限raw、非零有限归一系数、density finite、归一总质量有限时记方法已执行；算法本身数值报错必须记SOURCE_KFE_NUMERICAL_ERROR（不是严格残差未通过），不能自动重试、clip密度/修改数学源或用其它求解器。
第三层SOURCE_METHOD_INTERIOR_CANDIDATE：只对确已返回有限归一KFE密度的点按旧R1预注册指标检验：At严格(0,10)，a内部18格mass>=.10，a两端各mass<=.50，a模态至少1个内部，b内部18格mass>=.05。报告b上界mass>=.50为B_UPPER_BOUNDARY_WARNING。对4层结果各自True/False/NOT_EVALUATED，不用“均值At内点”替代内部质量判断。
第四层STRICT_ECONOMIC_STATIONARITY_CERTIFIED：另外检查post原始G.T@g最大绝对值<=1e-7、概率总质量偏差<=1e-8、负密度总质量<=1e-8、source污染行raw线性残差<=1e-7；详细列原始row295残差/剩余799行最大值、post原算子row sum、负密度格数、b/a边缘质量等。HJB和原KFE计算成功即便出现STATIONARITY_WARNING，也只可说SOURCE_KFE_COMPUTED_WITH_STATIONARITY_WARNING，不等于严格数学/实证稳态。
独立提供可重算的20-bin a_mass20与b_mass20、At/Bt/Lt/Ct、边界/内部mass、模态资产点、网格单位、源初始化/根/工资来源、后验余量。密度不能clip、abs或更改。旧实验的严驻定失败历史裁决不得追溯修改。

**跃迁仅作预注册离散诊断：**
按合成同一截面固定rah=.05、rb=.02，使用只读历史P2(wt19)、本轮E00(wt19.10)、E01(19.25)、E02(19.50)、E03(19.75)、E04(19.90)、历史R2 D07(wt20)的顺序，只有在相邻两点的HJB/KFE方法均成功且边缘质量真实可比的情况下，算|ΔAt|、|ΔBt|、|Δb_upper_mass|及分布差（例如总变差距离0.5*sum(abs(mass20_2-mass20_1)))。若|ΔAt|>=1或|Δb_upper_mass|>=.25，则标DISCRETE_TRANSITION_FLAG=TRUE，仅表示两个已观测点差异明显；不能宣称数学分岔临界点、连续价格域连通或稳态分支唯一。相邻缺点/没收敛需标UNTESTED_INTERVAL，不能插值补值。且所有比较都须显示STRICT_STATIONARITY_WARNING标记，不应基于不认证密度进行正式经济学比较静态估计。
第二组E05/E06与E02比较rb扰动；第三组E07-E11与只读D09、D11比较工作地有效工资/利率组合，分列单因素/多因素变化，不将多变量同时变化归因为其中一个因素。

## 5. 有界运行资源、隐私证据与STOP

硬预算：12点、12科学命令、12初始化、12 HJB、累积最多1200 HJB循环轮、960000 policy cells、12条件KFE，firm/GE/IRF/31省、Stage2/3、实证数据读取次数0。每点最多一个受监督Python子进程，不重试。每个科学命令180秒硬超时、1GiB **process committed-memory** 真实强制上限、一个活动科研子进程、六类BLAS/OMP/MKL/NUMEXPR/VECLIB/BLIS环境线程数设置1，在科学import前生效；本地不能可靠施加硬门则科学运行0并STOP。不把RSS等同于committed，不把环境线程限制称为独立测量native线程。
错误、资源限/权限失败、源文件身份/工资来源不一致或发生可能数据损坏，须STOP全任务；普通某点HJB不收敛或KFE源计算数值失败，真实报告后在无全局安全hard-stop时可执行下一个冻结点。每个点记录命令preclaim、SHA256、程序退出码、统计计数、逐轮trajectory、KFE是否执行/错误原文，预算用尽即STOP不得延长迭代/补点。
原始stdout/stderr与完整800维密度/postCSR及中间政策/初始原数组本地LOCAL_ONLY保留并用真实byte SHA绑定；公开脱敏20-bin和必要数值证据，不能以hash代替审阅所需的数值矩阵诊断。吸收以前R4_DOUBLE_BACKSLASH_BYTES误报，**仅对公众派生副本**规范化含隐私路径元数据与JSON转义，不得改原件科学字节、篡改原日志、忽略或放松既有隐私门。所有将提交文件包含manifest+seal须由原强制scanner实际PASS；扫描失败STOP、不推送。完整证据行文不得出现Windows私人绝对路径、密钥、令牌或受保护数据。若敏感性不确定须STOP并报告类别。
所有源、运行环境与隐私工作目录限制遵循已批准隔离安全仓，不能访问受保护P3/WASM/reparse/旧locked/shallow、重新下载私人Matlab/Excel、创建新repo/worktree或修改SSH凭证/协议。

## 6. 写入白名单、GitHub交付和独立验收

本任务固定工作流=GPT治理合同发布→Owner交本地Codex→安全隔离仓从FIXED_PARENT唯一建立candidate→按本合同执行→已授权普通SSH payload/seal两阶段远端核验→STOP→GPT独立A/B/C→Owner下一任务判断。
唯一允许新增文件：
validators/multi_province/temp31_matlab800_price_neighborhood_r3_isolated.py
tasks/CH5_TEMP31_MATLAB800_PRICE_NEIGHBORHOOD_DISTRIBUTION_SWITCH_R3_20261030/ 下的单独监督器、12点输入点表、preflight、工资见证、各点immutable evidence/、来源Hash、迭代轨迹、condition KFE与分布、wage_transition_ladder.md、joint_price_neighborhood.md、discrete_transition_flags.json、point_result_matrix.md/json、budget、gap_register、privacy_report、manifest、DELIVERY_FINAL_RECEIPT及最小必要独立审阅文档/纯静态脚本。
既有src、exports、老validator、旧tasks/docs/结果、MATLAB与Git工作流规则不得修改，旧R1/R2与其他项目证据不可重写/删除。禁止clean/reset/rebase/force push/自动checkout覆盖旧工作树/新repo/worktree；新candidate只有SOURCE_COMMIT单一parent。
发布前GitHub治理HEAD必须严格等于GPT随后给出的TASK_PUBLICATION_COMMIT，parent必须等于a63b85af20182e0431d8f9a95ab839e90bae3159且diff只新增本CONTRACT。合同Blob正确、本候选远端不存在、source commit/tree和必要源Blob一致才进入科研工作。GitHub发布之后不得在本科研candidate上引用治理commit为代码parent。
已发布工作仅2次正常已授权普通SSH：payload一次，remote exact commit/parent/root tree/每个允许文件Git Blob/bytes/SHA256 readback；seal commit仅允许新增本task目录的DELIVERY_FINAL_RECEIPT.json，再SSH一次、远端103/??依实际文件数完整readback。禁止预设文件数量或捏造hash；manifest/self/seal身份须在外置LOCAL_ONLY final receipt闭合，不能试图通过seal自哈希循环加第三commit。SSH不明/连接关闭时只能有界只读确认是否push成功，不允许在当前授权下第二次push/改认证；按证据STOP，等待Owner另行授权。
科研执行完交付后STOP__AWAITING_GPT_INDEPENDENT_ABC；出现身份/隐私/模型资源/SSH hard-stop则STOP并报告真实partial与阻塞；GPT再A身份交付、B数值与经济、C分层科学，不能让执行者自己声明独立GPT终审或自动发布下一任务。
要求最终汇报：TASK_ID、SOURCE_COMMIT/tree、治理HEAD、candidate、payload/final commit-parent-tree、文件逐个原字节身份核验数、所有12点价格和四层状态、At/Bt/20bin资产边缘与离散跳变标记、源方法/驻定风险、实际预算、隐私门、LOCAL_ONLY保护、尚未认证边界、终态。Stage2/Stage3/GE/IRF/31省全不执行。

## 7. 既有正式科研状态保留

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
