# TEMP31 Owner 决策：原 MATLAB HA 外生参数与网格冻结、8状态证据降级、三阶段重启

DECISION_DATE=2026-10-29
STATUS=OWNER_FROZEN_DESIGN_BASELINE__NO_NEW_SCIENCE_TASK_ISSUED
ROUTE=TEMP31
DECISION_AUTHORITY=OWNER_DIRECT
SCOPE=HA_EXTERNAL_PARAMETERS_AND_INPUTS_ONLY
BLACK_BOX=HANK_2ASSETS_HJB_MATLAB_ALGORITHM_IMMUTABLE
GOVERNANCE_HEAD_BEFORE_RECORD=a54e9c24d36314e81d3a9074fe7ae9ba3e59adff
FROZEN_PYTHON_SCIENTIFIC_SOURCE=56447829ce0e6c3c85552c53c351b26a2452a4bd
FROZEN_PYTHON_SOURCE_ROOT_TREE=7b7cb29dd5b37be92561e7f1bc688c0d29789732
HISTORICAL_TEMP31_8STATE_AUDIT_FINAL=57af4365554396e2bd34b1e6a1256f0725111bf0
MATLAB_ZIP_SHA256=ceb94ccf34d2d218722b81e5111a8f4c530571a9f886bd4afe0610a00321f755
MATLAB_INIT_SOURCE=multi_prov_HANK_12sts.m
MATLAB_INIT_SHA256=3c44449cfd4047b5c9e17e540afea2f50b4251150f8f74ab8cceed26e15dec97
MATLAB_HJB_SOURCE=HANK_2ASSETS_HJB.m
MATLAB_HJB_SHA256=049136b769560040bc678f828f5d3ec5338ddcaa2090d6bed4e40732f56c3eae

## 0. 判决和边界

- Owner明确终止把TEMP31近期8状态(2x2x2)的HJB不收敛结果用于任何经济学收敛域判断，也不得由8状态推断KFE稳态资产分布。旧文件、历史STOP、实验日志、提交和独立审阅均原样保留；其有限的调用链/矩阵代数技术证据仍有效。
- 已有历史20x20及更高分辨率试验不受8状态降级牵连，但不直接充当新TEMP31净工资路径的科研PASS。
- 本轮**是外部参数与研究方法冻结，不是科研程序来源正式冻结**；FORMAL_SOURCE_FREEZE仍FALSE。未经Owner另行授权，不运行HA/HJB/KFE/GE/IRF、不开展自动调参、不增删改正式科研源文件。
- MATLAB HJB含BB、AAH、Bswitch、边界、离散化、隐式迭代与KFE既定方法均视为受保护黑箱。此前合成CTMC数学观察不授权任何clip负rate、修改diag、重分配边界流、重设delta或替代原版求解器的操作。Python/MATLAB尚未证实的完整等价性，不能仅凭名称自称全面通过。

## 1. HA固定外生网格（原MATLAB唯一默认权威）

原件multi_prov_HANK_12sts.m第33-47行与HANK_2ASSETS_HJB.m第10-20、46-49行：

| 参数 | 冻结数值/定义 | 解释 |
|---|---|---|
| grid.I, bmin, bmax | I=20; -2; 5 | 流动资产，19个内部间隔 |
| grid.J, amin, amax | J=20; 0; 10 | 非流动资产，19个内部间隔 |
| grid.Nz,zmin,zmax | Nz=2; 0.8;1.3 | 两状态劳动能力 |
| grid.z | linspace(0.8,1.3,2) | [0.8,1.3] |
| grid.la_mat | [ [-1/3,1/3],[1/3,-1/3] ] | 劳动能力切换强度 |
| arrays | MATLAB (I,J,Nz)=(20,20,2) | 每省800状态，Python的HJB内部维度为(b,a,z) |
| spacing | db=7/19; da=10/19 | 均匀资产间距 |

严禁把2026-10-29极小网格b=[-2,5],a=[0,10]误认为原MATLAB的20点区间；严禁把历史扩域bmax=20、amax=100自动代替原版bmax=5、amax=10。

## 2. 冻结HA结构/校准参数与数值参数（非本轮搜索轴）

原件multi_prov_HANK_12sts.m第13-30、59-65、85-105行，以及HANK_2ASSETS_HJB.m内部常量。

| 原版字段 | 数值 | Python对应/科研含义 |
|---|---|---|
| param.ga | 2 | gamma_c；消费风险厌恶 |
| param.phi_l | 5 | phi；劳动弹性倒数 |
| param.frisch_l | 0.2 | 1/phi，核对一致 |
| param.alphal | 1 | labor_weights=[1] 的单一合成家户权重 |
| param.alphap | 1 | MATLAB效用的消费权重；Python合同没有单独alphap字段，须保证隐式一倍含义 |
| param.rho | 0.05 | 时间贴现 |
| CHI.chi0 | 0.1 | 调整成本线性项 |
| CHI.chi1 | 2 | 调整成本二次项 |
| CHI.a_bar | 0.000001 | 调整成本分母下限 |
| CHI.fixcost,fixcost2 | 0,0 | MATLAB固定成本项默认 |
| init.rb_gap | 0.07 | 负b额外借款利差，外部输入阶段固定 |
| init.Tt | 0.1 | 转移支付，阶段1固定 |
| init.tau | 0.05 | 阶段1统一工资税率，采用单次应用语义 |
| HJB alphac,Cmin | 1,0 | 原版HJB内部字面常量，不修改 |
| num.maxit,num.crit | 100,1e-7 | 原版HJB最多100次与value迭代阈值 |
| num.homecrit | 1e-2 | 原版矩阵行和停止阈值；不可擅自强化为新算法 |
| num.Delta | 1000 | 原版隐式伪时间步 |
| num.maxiter | 100 | 原版num配置字段，与num.maxit不同；保持原样 |
| num.max2iter, max3iter | 200,500 | 原版其他级别迭代配置；非阶段1 HJB预算 |
| MATLAB常数 | Vb floor=1e-6; drift selector threshold=1e-12 | 黑箱内部保留 |

原版生产率为有限两状态切换，没有另行设置连续生产率扩散/漂移参数；Python EconomicParams.mu_z=0、sigma_z=0是与此相符的适配值，不冒称为原MATLAB同名赋值。

## 3. 原版其余外生/外层参数的锁定范围（仅备查，阶段1不调用）

- 厂商价格限幅：grid.ramin=0.02, grid.ramax=0.09, grid.wjtmin=0.8, grid.wjtmax=1.3。这是**厂商ra与目的地wjt**的边界，不能误写为HA直接消费的组合rah或净wt的实测收敛域。
- 固定结构系数：param.max_phi=0.3, param.max_sigmau=0.5; epsilon=10, theta=100, delta=0.025, rho_pi=1.25, istar=0.015, pistar=0.0075; corptau初值0.25。
- 外层历史初始记录：inter_prv_ratio=0.5, At=2, Bt=1, Ct=4, Lt=0.8, mt=0.9, GovInv=1000；这些是**初始值而不是求解后的资产分布**，不得误判为每格固定资产点。外层init.alpha=0.6、init.Zt=6等会由原版数据/企业逻辑派生或覆盖；不冻结成31省真实观测值。
- 原版数据管线初值：GDP_multiplier=1000, POP_multiplier=100, Ztratio=1, GovInv_ratio=1, smooth_method=0, reg_method=0; 涉及真实31省的年份、单位和实证证据仍遵守既有BLOCKED来源门，不因本冻结而获得认证。
- 固定上述外层字段**并不授权第2/3阶段执行**；如果一项后来被证明是内生更新量或仅初始猜测，必须按源码角色区分，不能作为永久外生常量。

## 4. 阶段1唯一待探索的三维价格输入

FREE_PRICE_DIMENSIONS=(rah,rb,wt)
OTHERS=FROZEN_AS_ABOVE
- rah：家户收到的非流动资本组合回报率，初始MATLAB参考值0.09；其是否等于厂商ra需经资本分配映射，暂不等同。
- rb：流动资产利率，初始MATLAB参考值0.02；借款端采用rb+0.07。
- wt：当前阶段定义为**进入TEMP31 HJB的已一次性扣除税费/迁移楔后的组合有效工资**，而不是省级统计工资或厂商的wjt。原版初值w=20、tau=0.05、没有额外楔时的等效HJB工资输入为19，只是参考起点、不是实证工资或已知可收敛点。
- 保留TEMP31此前Owner目的地tax_j以及迁移wedge仅在上游单次扣除的合同。原版MATLAB HJB内含(1-tau)*w；当前TEMP31消费者按净工资入参，不得在其内部再次扣tau。二者只能在逐项等效输入意义下对照，不能把不同参数化误称字面相同。
- MATLAB原版Lt_seperate.m把劳动分配税率索引写成来源地tau_i，但wage_caculate.m把工资税率索引写成目的地tau_j；该源码差异不可以静默统一。现行Owner较新的目的地tau_j单次应用决定优先，但实际第2阶段公式及实证接线必须显式审计差异。
- Stage1扫描区间、候选点数、试验顺序与计算预算尚**未**获批具体数值，不得把原版ra的限幅、wjt的限幅或历史a/b扩域当作已批准的rah/rb/wt搜索范围；必须另行冻结有限运行合同。

### Stage1科学判据（设计门，不是执行许可）
1. 使用原版800状态HA网格与原版固定校准/迭代参数；禁止2x2x2用于任何经济收敛域研究。
2. HJB必须达到原版停止规则，不把线性求解成功、有限数组或80轮未收敛称为稳态成功。
3. KFE稳态概率/密度归一、状态支持及数值可信性必须单独检验；不是HJB converged即分布完成。
4. 家户平均非流动资产At必须严格处于(amin,amax)=(0,10)，不可等于任何边界。同时单独查看a的内部格点概率质量与上/下边界集中现象（避免仅仅平均值非边界却是端点混合）。
5. b也须提供边界质量、内部分布及平均Bt；不采用缺乏中间资产点的格点做分布判定。
6. 每个有效价格点记录(rah,rb,wt)、经济单位、网格、参数来源、初始化hash、HJB停止状态、KFE状态、At/Bt、a/b边界与内部质量；先发现可行域而非寻找单个偶然收敛点。
7. 本文不预设任何额外At安全边际数值阈值或资产内点质量比例阈值；后续有限运行合同必须事先确定其统计判据，不能事后按结果改变。

## 5. Stage2假设性省级劳动/资本映射（仅未来方法，不调用）

阶段1得到经双重HJB/KFE认证的共同家户稳态后，才可以作为第2阶段**近似各省共同家户行为**的假设基线；这不是各省实证校准已完成。

- 原版劳动分配：phi_{ji}=1+max_phi*(Y_j/L_j-Y_i/L_i)/(Y_j/L_j+Y_i/L_i)，L_{ji}=N_i*C_i^(-ga/phi_l)*[wjt_j*(1-tau_i-sigmau_{ji})/phi_{ji}]^(1/phi_l)；目标地j为行、来源地i为列，L_j^supply=sum_i L_{ji}。这是**原MATLAB原式**；现行Owner目的地tau_j单次应用合同不同，需在新任务中明确所采用的政策参数化及等效性，不得隐含改算法。
- 原版资本流入：tempKt=sum_i(theta_i*At_i*N_i)，K_j^supply=[tempKt-theta_j*At_j*N_j]/(N-1)，其中theta_i初值0.5；这是旧源码明确的**外省资本流入项**，未自动包括本地未外流私人资本；原版厂商Kt=K_j^supply+GovInv_j。不能直接把它更名为全面私人资本供给或偷换成后来K1双边资本网络。
- Stage2必须提供真实或可审计的N_i、Y_i、目的地工资wjt_j、迁移楔和phi矩阵来源，以及口径、单位、截面/年份；假设共同HA稳态仅是近似分析，不生成正式31省结果。

## 6. Stage3有界价格反馈与调参（仅未来方法）

基于Stage2推导的L_j^supply和K_j^supply，检查厂商收益/工资映射与下一轮HA输入(rah,rb,wt)能否保持在Stage1经认证的可行域内；厂商价格clip、财政反馈与原版更新顺序不得被混同为家户HJB参数。即便映射保持在可行域，也不等于31省联合GE固定点已收敛。未授权执行、调参、改源码或正式Results。

## 7. 历史证据状态与科研保护

HISTORICAL_TEMP31_8STATE_CONVERGENCE_SCIENTIFIC_INFERENCE=SUPERSEDED_INVALID_FOR_800_STATE_ECONOMIC_DOMAIN
HISTORICAL_8STATE_UTILITY=TECHNICAL_SMOKE_AND_SYNTHETIC_LINEAR_ALGEBRA_ONLY
HISTORICAL_20PLUS_GRID_RESULTS=RETAIN_ORIGINAL_PROVENANCE_AND_LIMITATIONS
SOURCE_CODE_CHANGED=FALSE
MODEL_EXECUTION_THIS_DECISION=0
TASKS_CREATED_THIS_DECISION=0
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE
FORMAL_SOURCE_FREEZE=FALSE
P3=BLOCKED
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE
FULL_RUNNER_IO_CLOSURE=BLOCKED

NEXT_ACTION=OWNER_TO_AUTHORIZE_SEPARATE_FINITE_STAGE1_PRICE_DOMAIN_EXPERIMENT_TASK_WITH_FIXED_GRID_AND_BUDGET; NO_AUTOMATED_EXECUTION.
