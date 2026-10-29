# TEMP31 原MATLAB800状态：rah/rb/wt三维价格初筛与家户内部稳态 R1

TASK_ID=CH5_TEMP31_MATLAB800_THREE_PRICE_INTERIOR_HA_PILOT_R1_20261029
STATUS=ISSUED_AWAITING_OWNER_TRANSFER
OWNER_APPROVED=2026-10-29__RESTART_BOUNDED_HA_THREE_PRICE_PILOT
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=d3cc4ceb9d400f2aa00d26cbd577dcae8c5ef5d3
TASK_PUBLICATION_COMMIT=EXACT_40_HEX_FILLED_BY_GPT_AFTER_PUBLISH
EXPECTED_GOVERNANCE_REMOTE_HEAD=TASK_PUBLICATION_COMMIT_STRICT_EQUALITY
TASK_CONTRACT_PATH=tasks/CH5_TEMP31_MATLAB800_THREE_PRICE_INTERIOR_HA_PILOT_R1_20261029/CONTRACT.md
CANDIDATE_BRANCH=codex/ch5-temp31-matlab800-three-price-interior-ha-pilot-r1-20261029
FIXED_PARENT=56447829ce0e6c3c85552c53c351b26a2452a4bd
SOURCE_COMMIT=56447829ce0e6c3c85552c53c351b26a2452a4bd
SOURCE_PARENT=a51c2e7ff6548340a1ee86857b0ee55792fa69b4
SOURCE_ROOT_TREE=7b7cb29dd5b37be92561e7f1bc688c0d29789732
OWNER_PARAMETER_FREEZE_COMMIT=d3cc4ceb9d400f2aa00d26cbd577dcae8c5ef5d3
OWNER_PARAMETER_FREEZE_BLOB=175aa4c87fef037055e339e451ecf59663dd3650
BLACK_BOX_HJB_AND_KFE_IMMUTABLE=TRUE
SOURCE_WRITES=0
MAX_PRICE_POINTS=7
MAX_INITIALIZER_CALLS=7
MAX_HJB_CALLS=7
MAX_HJB_ITERATIONS=700
MAX_KFE_CALLS=7
REAL_31_PROVINCE_AND_FIRM_CALLS=0
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 1. 科研目标和不可越界的解释

本任务仅执行TEMP31第一阶段的七个800状态的合成数值价格点，寻找满足源HJB收敛、原MATLAB式KFE可信且a轴资产分布为内部态的离散价格候选。7点不能证明三维连续价格区间、实际31省经济结果、GE、论文Results。不得更改Moll/原MATLAB HJB及Python既定BB/AAH/Bswitch、边界和政策/初始化、迭代算法、KFE污染行机制。旧8状态不收敛结果已降为工程/数学证据，不能用于本轮科学可行域；原有20点以上历史结果保留但不移植为新TEMP31数值结果。Stage2劳动/资本分配、Stage3厂商/GE映射均只可写未来研究建议，运行预算严格为零。

## 2. 冻结MATLAB身份与非搜索参数

原ZIP SHA256 ceb94ccf34d2d218722b81e5111a8f4c530571a9f886bd4afe0610a00321f755；multi_prov_HANK_12sts.m 5531 bytes SHA256 3c44449cfd4047b5c9e17e540afea2f50b4251150f8f74ab8cceed26e15dec97；HANK_2ASSETS_HJB.m 12227 bytes SHA256 049136b769560040bc678f828f5d3ec5338ddcaa2090d6bed4e40732f56c3eae。Codex若安全隔离仓无原MATLAB字节，仅依本任务逐行摘录/冻结决策作限定来源映射，标MATLAB_RAW_LOCAL_VERIFICATION=NOT_AVAILABLE，不能访问P3/受保护树或私人目录，不得谎称读到原MATLAB。

唯一grid: b=linspace(-2,5,20),a=linspace(0,10,20),z=[0.8,1.3],Q=[[-1/3,1/3],[1/3,-1/3]]，shape=(20,20,2),800状态，db=7/19,da=10/19。不得采用2×2×2或历史扩域[-2,20]×[0,100]。
EconomicParams: rho=.05,gamma_c=2,phi=5,chi_0=.1,chi_1=2,a_bar=1e-6,mu_z=0,sigma_z=0；原MATLAB alphap=alphac=1,alphal=1,frisch_l=.2,fixcost=fixcost2=0；不新增这些隐含常量为可调参数。Tt=.1,rb_gap=.07,税率背景tau=.05,迁移楔全零,单类型labor_weights=1。HJB: delta=1000,max_iterations=100,convergence_tolerance=1e-7,drift_tolerance=1e-12。原MATLAB homecrit=0.01；Python TEMP31 HJB没有内部homecrit逐轮守卫，这属于待记录来源差异，不允许在黑箱内补写/修改；只读观察发现超阈值应标SOURCE_PARITY_BLOCKED不颁科学PASS。原版初始劳动根与V0公式按冻结科学源码使用，不许修改为自认为正确的新公式。

固定科学来源commit及关键Blob，实际读取检查：
src/ch5_two_asset_hank/contracts.py=c746b616bec38531a7d96da81a54e2899d8aba53
src/ch5_two_asset_hank/matlab_faithful_operator.py=9a511e151c9bf449412dc5605dfa1a2076711277
src/ch5_two_asset_hank/temp31_netwage_policy.py=d90eb4ba627d4c702062116c2a4ffadac0f43d86
src/ch5_two_asset_hank/temp31_netwage_hjb.py=56441c1c41ec94190997ce6f0ecbb2b5c2ca7b56
src/ch5_two_asset_hank/temp31_netwage_economics.py=30528d55b884c62f3c9785dfe59197a61f125a3c
src/ch5_two_asset_hank/matlab_faithful_kfe.py=4ccb7cec8c4754e91bd8830a95dc533811784391
src/ch5_two_asset_hank/multi_province/temp31_ha_taxfree_bootstrap.py=b82eadea383a4d7546a11d4f19686440f8d71870
src/ch5_two_asset_hank/multi_province/temp31_ha_wage_debug.py=7df9c03fdd55d72beded7383866d683ca9356bc9
src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py=90667ddc00c72b9290e91481af4835c808ecfccb
其他最小必要import源依赖须记Blob，不可更改或复制为替换版。禁止自动下载私人MATLAB或经济Excel。

## 3. 七个唯一价格点：逐点、一次、严格顺序

以下wt是HJB实际接收的已一次性扣税/迁移楔的净综合工资，是合成数值，不是实际地区工资：
P0 rah=.09 rb=.02 wt=19.0
P1 rah=.07 rb=.02 wt=19.0
P2 rah=.05 rb=.02 wt=19.0
P3 rah=.07 rb=.01 wt=19.0
P4 rah=.07 rb=.03 wt=19.0
P5 rah=.07 rb=.02 wt=15.5
P6 rah=.07 rb=.02 wt=22.0
这是覆盖rah[.05,.09]、rb[.01,.03]、wt[15.5,22]的七点轴向探索，不是盒内全部组合。不得追加点、变序、自动二分、贝叶斯搜索、重新调grid或更改经济参数。

### 净工资来源硬门

P0-P4使用完整源numerical_bootstrap19 -> netwage_inputs，语义NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL。
P5-P6不得把任意wt强塞首轮19或伪造真实31省工资。允许仅用已有source SyntheticNetWageCalculation -> calculated_round_record -> later_net_wage_record -> netwage_inputs构造**明示为反事实的合成数学见证**：仅两个虚拟A/B省份，tau_destination=(.05,.05),sigma全零,phi_destination_origin全1,phi_l=5,alphal=1；两个相同的合成firm wage = wt/[.95*2^(5/6)]。调用原有综合工资公式求得对应净wt，误差≤1e-12，且源上下文及顺序完全通过；generated_after_iteration=1/entering_iteration=2是合成数据合同的逻辑元数据，不意味着真实企业已更新或真实第一轮已运行。每份记录显式COUNTERFACTUAL_SYNTHETIC_WAGE_WITNESS_NO_REAL_FIRM_EMPIRICAL_PROVENANCE。若源校验拒绝或无法合规构造，WAGE_PROVENANCE_GATE_BLOCKED并在科研运行前STOP；不得monkeypatch/bypass/修改既有来源验证器、伪造实证。HJB内部不得再次扣tau=.05或迁移楔。

## 4. 科研执行与判断

严格先只读校验治理HEAD、源Blob、合成来源合同、7点预算及原版20×20×2；校验失败即STOP，不调用真实科研模型。
逐点从全新未修改的temp31_netwage_initial_arrays重建V0和l0；完整记录输入及各数组hash、有限性、初值极值；不能warm-start或跨点复用。每点最多一次source solve_temp31_netwage_hjb（至多100轮），不改内部算法。HJB converged=True且stat<1e-7才进入KFE；若未收敛，记HJB_NOT_CONVERGED并不运行该点KFE。观察原MATLAB homecrit和Python差异，但不偷改内核；如证据不能保证必要等价，标PARITY_UNCERTIFIED。
KFE仅用现有src/ch5_two_asset_hank/matlab_faithful_kfe.py的solve_matlab_faithful_stationary_kfe，将HJB原有post_convergence_operator.full传入，shape=(20,20,2),db=7/19,da=10/19；不能改污染行0.37*M、rhs=.007、原始signed密度或归一权重，不能clip/abs负密度或换求解器。KFE失败标KFE_NOT_CERTIFIED并完整登记，不自动重试。
后处理以源积分权重db*da得到At=sum(a*g*db*da),Bt=sum(b*g*db*da),Lt=sum(z*l*g*db*da),Ct=sum(c*g*db*da)。保留20-bin a/b边缘概率原数组、端点质量、内部质量、modal位置、At离上下界距离、负质量和KFE残差。真实KFE有效门须满足：密度/解有限，sum(g)*db*da偏离1≤1e-8，负质量sum(max(-g,0))*db*da≤1e-8，post G的驻定残差maxabs(G.T@g)≤1e-7，污染行系统残差≤1e-7；不得用原值负数的绝对值替代负质量。内点候选额外同时满足0<At<10、a轴内部质量≥0.10、两端各自质量≤0.50、a轴最大质量对应索引不全在端点、b轴内部质量≥0.05。这些是R1**预注册诊断量表**，不代表论文最终经济学临界值。At来自稳态概率分布，不是省级init.At=2。
结果标签只允许：PILOT_INTERIOR_HA_CANDIDATE / HJB_NOT_CONVERGED / KFE_NOT_CERTIFIED / BOUNDARY_DOMINATED_OR_NOT_INTERIOR / SOURCE_PARITY_BLOCKED / WAGE_PROVENANCE_GATE_BLOCKED / EXECUTION_BLOCKED。没有收敛点也合法完成有界测量，不因此自动变更参数或继续实验。R1结果只对给定7点有效，不称已确定连续三维可行域。

## 5. 严格预算、监督与禁止调用

MAX_PRICE_POINTS=7; MAX_INITIALIZER_CALLS=7; MAX_HJB_CALLS=7; MAX_KFE_CALLS=7; TOTAL_HJB_ITERATIONS_MAX=700。每点最多1次受监督Python科研命令，单次硬超时180秒、单活动科研子进程、Windows Job等安全隔离进程已提交内存限制1GiB、六种BLAS/OMP/MKL/NUMEXPR/VECLIB/BLIS环境线程限制1；若监督无法施加则科学调用0且STOP。不可自动retry；超时、OOM、越权读写、进程失控、权限拒绝立即STOP，全局上限无论执行结果均不得增大。
每条preclaim、supervisor、HJB和KFE真正调用计数、资源回执、退出状态、stdout/stderr原始字节大小及SHA256、公开脱敏副本与变换计数、fixture价格、hash都要可核查。LOCAL_ONLY原始日志不得提交。并以纯静态/合成、**不消耗额外HJB/KFE调用**的方式验证输入格点不足20、重复扣税、工资来源错配、warm start或未收敛提前调用KFE均能被拒绝。
仅授权Stage1：真实省级数据/Excel、劳动分配、资本流向、firm、GE、IRF、外层更新、31省联动、正式Results的调用预算全部为0。不能启动Stage2/3。

## 6. 允许提交路径与远端交付

仅新增validators/multi_province/temp31_matlab800_three_price_ha_pilot_isolated.py，以及tasks/CH5_TEMP31_MATLAB800_THREE_PRICE_INTERIOR_HA_PILOT_R1_20261029/下监督脚本、point_grid.json、result.md、parameter_freeze_readback.md、wage_provenance_and_tax_once.md、每点完整最小审阅证据、kfe_mass_and_interior_diagnostics.md、gap_register.md、source_identity.json、budget.json、privacy_report.md、manifest.json、DELIVERY_FINAL_RECEIPT.json及必要纯静态测试。CONTRACT仅存在治理分支，不复制到候选。
不得修改任何src、exports、既有validators、docs、tasks、旧证据、Git历史、P3、旧锁仓、WASM/reparse、证据库；不得新建repo/worktree、clean/reset/rebase/force push/自动merge。运行仅使用已授权安全隔离仓、已有正常权限普通SSH和现有依赖，不pip联网安装。
Codex启动前确认治理HEAD严格等于任务发布SHA，治理commit parent=d3cc4ceb9d400f2aa00d26cbd577dcae8c5ef5d3且diff只有tasks/CH5_TEMP31_MATLAB800_THREE_PRICE_INTERIOR_HA_PILOT_R1_20261029/CONTRACT.md；候选从固定SOURCE_COMMIT创建，parent不得采用治理branch；payload commit推送后回读git commit/parent/tree/file Blob/bytes/SHA256，seal commit只增加DELIVERY_FINAL_RECEIPT.json并再次回读同一证据。外置final回执LOCAL_ONLY不推送以避免seal自哈希循环。push失败不自动更换凭据/协议/账户/SSH路径；先只读消歧，安全拒绝则STOP。
结果包含每个点的HJB/KFE状态、At/Bt、a/b边缘质量、来源/经济语义、source-to-MATLAB差异、所有真实预算、未完成清单、manifest、privacy、远端字节证据。最终报告candidate branch/payload/final commit-parent-tree、每点分类及STOP__AWAITING_GPT_INDEPENDENT_ABC，禁止自动Issue/PR/merge/cleanup/next。GPT独立A/B/C另行执行；不能将执行者自报视为独立见证。

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
