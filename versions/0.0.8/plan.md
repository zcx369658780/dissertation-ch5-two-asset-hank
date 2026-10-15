# V0.0.8 正式冻结：corrected-model 劳动/财政联合实现、条件稳态及IRF资格门

**冻结日期：2026-10-15（Asia/Shanghai）**
**状态：V008_FROZEN__OWNER_ADOPTED_CORRECTED_MODEL__WAIT_SEPARATE_SYNTHETIC_IMPLEMENTATION_AUTHORIZATION__REAL_HANK_AND_IRF_CLOSED**
**版本目标：从跨来源科学提案进入新的隔离 Python 经济模型实现与数值可行性检验。**
**本文件为正式科研设计冻结，不因自身发布而授予执行许可；由Astra在实际回读固定commit/blob后单独签发受界工程/人工经济体数值授权。**

## 1. Owner科学采纳及资格边界

Owner在本次会话明确批准Astra此前提出的**完整科学方向包**，要求“落实到python程序中然后看看是否能得到稳态，以及IRF是否正常”：

1. **劳动**：新corrected-model的主线是单一家庭 CES 劳动指数与严格来源居民—工作目的地双边劳动/工资对偶；实际劳动量+外生配置份额为可证伪对照，不默认为第二条生产分支。
2. **税**：只存在**一套明确计价的全国工资税**，同一种税只扣一次；不得同时由destination composite wage和origin HJB预算重复扣除。迁移楔子的现金/真实资源/效用属性仍须明确，不能因名称默认为税。
3. **财政**：全国统一政府账户与各省份分析分账，不自行创设31份独立政府债。工资税、公司税、公共资本、私人收益、转移支付与流动资产/中介债务分账户，所有收入和成本须相同货币、人口和模型时间口径。
4. **AtTax**：仅保留原历史聚合的数值定义，不自动认定政府税收。政府征收/中介利润/真实资源成本是三种互斥的**待证解释**；新人工经济体默认使用\`AtTax=0\`的中性场景，非零则必须选择显式会计分类并完成双边分录，绝不把这种人工选择追认为真实C8的经济解释。
5. **研究顺序**：先完整静态/稳态经济账户、市场与资源约束、可证伪的数值资格；再评估有完整跨期方程时的IRF。原HANK/Python历史C8、已接受2009 parity、HJB/KFE/K1/C1和2017/2018诊断均不被本新支线覆盖或追认。

**明确未被Owner采纳**：AtTax固定为政府税、旧sigma固定为资源成本、对现存clip/资本收益作单方面修补、静态稳态通胀置零、固定\`delta\`改成论文表5-1数值、重启V007的受保护数据/模型权限。涉及这些科学制度选择时采用可切换且明确标成\`SYNTHETIC_SCENARIO\`的会计假设或FAIL_CLOSED。

## 2. 代码版本身份、原资产与高风险权限

- 实施候选的唯一固定代码基线采用已接受 V0.0.7 文档候选 \`d8bb49d86ea674ea4ff5e3fdf03929baa08a6514\`，完整 tree \`9b685397ad5bc76a4ac3bf4203776389742c5ec5\`，本基线已有V006合成模块。**NEXT_BASELINE_ADOPTION=ADOPTED_FOR_V008_ISOLATED_CORRECTED_MODEL**，并不代表原D盘checkout/main合并。
- 原模型工作树 \`D:\ProjectTemp\c5k1bturn56\`、历史HEAD \`a1db8c114dec0ab69d69a5576e153a7f868cba0e\`、外部Git common-dir \`D:\ResearchCode\dissertation-ch5-two-asset-hank\.git\`、8历史tracked dirty（包含\`government_assets.py\`与\`middle_stage.py\`）、既有untracked/ignored及C盘B3有限保全一律不覆盖、不stash/reset/clean/checkout、不开A16 hostile，不得为新版任务作清理/备份/G0重复循环。
- 本版所有代码只能写到精确新建、非reparse、与原worktree隔离的候选目录/branch。GitHub\`main\`仍不是接纳的新基线。用户上传博士论文PDF和MATLAB ZIP仅作只读辅助研究，不可上传原MATLAB源码全文、不能按历史C8原件使用。
- 真实2017/2018经济/原C8/31省受保护JSON/NPZ/CSV/receipts的stat/read/hash/parse/extract及所有D3-real/D4-real、原C8/C9/C10、旧真实consumer/HJB/KFE/outer runner调用预算：**0**，旧\`A16 UNRESOLVED/FAIL_CLOSED\`、\`window UNACCEPTED\`、\`C9 PAUSED\`、\`CALL_LEDGER_UNRESOLVED\`、\`model_activation=False\`、\`Results FALSE\`不变。
- 本次单独授权允许**新的、仅人工省份/人工资产/人工校准输入的corrected-model经济数值器**，不继承旧C8科技账，绝不通过改名包装、Mock原真实数据或new package import绕过旧零预算。

## 3. 经济学不可省略的实现公理

设来源省\`i\`、目的省\`j\`、效率态\`z\`、家户分布\`mu_i\`，新家庭劳动指数
\[
\ell_i=\left(\sum_j\phi_{ji} h_{ji}^{1+\eta}\right)^{1/(1+\eta)},\quad\eta>0,\;\phi_{ji}>0.
\]
在明确约束的正净工资效率价格\`v_ji\`下，同一效用问题的严格对偶
\[
W_i=\left(\sum_j\phi_{ji}^{-1/\eta}v_{ji}^{1+1/\eta}\right)^{\eta/(1+\eta)},\qquad
h_{ji}=\ell_i\phi_{ji}^{-1/\eta}(v_{ji}/W_i)^{1/\eta},
\]
并逐状态验证\(\sum_j v_{ji}h_{ji}=W_i\ell_i\)。\`kappa/alphal\`作为家庭劳动效用或单位系数的数学位置必须在一个且仅一个明确映射里定义；不同税或效用系数不能因旧名形似混用。
\[
L^s_j=\sum_iN_i\int z h_{ji}(a,b,z)d\mu_i.
\]
**不得强制\(\sum_j h_{ji}=\ell_i\)**；旧source-faithful按\`Ct_i^{-gamma/eta}\`构造劳动流不是异质性积分的精确等价；只有状态与消费分布具备证明时才能把新的 \`int z ell_i dmu_i\`绑定到真实HJB/KFE。来源人口N不等于家户数、不设N=P/3。

工资税一次计价：设税前工资 \`w_j\`，全国税率\`tau\`，同一工资税只能在\`v_ji\`构建时扣一次。令人工\`migration_cost\`的费用去向为显式枚举；若未指派而为非零则拒绝真实核算，人工测试可分互斥场景。按明确费用种类用同一双边税前工资base核算
\[
R^w=\tau\sum_{j,i}N_i\int w_j z h_{ji}d\mu_i.
\]
税前收入 = 净家户收入 + 税收入 + 已定义资源成本/中介收入/费用，任何分录遗漏、二次扣税必须FAIL。对家户异质性不能用 \`(E c)^{-a}\`替代\`E(c^{-a})\`。

财政必须有**完全列示的全国复式账户**：企业利润税与裁剪补贴分列；\`AtTax\`的政府征收、金融中介利润、真实成本互斥；\`Tt\`人均转移转地区总流需要N及同一期单位；流动资产\`Bt\`不能因同名即当政府债；公共资本\`K^g\`是存量，净/毛收益、\`delta\`与新增公共投资融资分别列；省际转移全国合计0。原\`GovInv=max(Ktarget-Kprivate,0)\`在旧科学历史原样冻结，新corrected模型只可将其做静态人工初值/给定资本约束，不能冒充已融资的政府投资流。
\`raw_ra0\`私人payoff与\`used ra\`政府收益/clip若同时出现，必须按**同一期、同资本池、明确所有权和clip调整现金接收者**写可核复式账，否则fail-closed，不允许重用历史clip税条目来虚构财政盈余。
- 人口/货币\`U=100 persons\`、\`M=100000 yuan\`、统计\`q=1000(Y/N)\`条件换算与模型期\`T\`分开。模型时间与外迭代计数不能混同；不能从历史数据直接认证任何动态参数。
- 静态财政平衡不能靠悄悄把\`GovSurplus\`设成0；人工稳态必须明确列一个**被选择的财政工具**（例如人工lump-sum transfer为内生、其余给定），出示同时满足的预算及资源恒等；真实政策制度未定时只称\`SYNTHETIC_FINANCING_CLOSURE\`。

## 4. Python实现目标与准许路径（不强求空占位）

本版受限的**真实交付应是工作代码+独立数学oracle+受限数值结果**，不是SOURCE_ONLY清单：
允许新增的模型模块（如确实需要，每个文件必须有实质算法）：
- \`src/ch5_two_asset_hank/multi_province/reconciled_labor.py\`
- \`src/ch5_two_asset_hank/multi_province/reconciled_household_prices.py\`
- \`src/ch5_two_asset_hank/multi_province/reconciled_fiscal.py\`
- \`src/ch5_two_asset_hank/multi_province/reconciled_stationary.py\`
- \`src/ch5_two_asset_hank/multi_province/reconciled_shock_diagnostic.py\`
- \`src/ch5_two_asset_hank/multi_province/reconciled_irf_gate.py\`
允许新增的focused测试：
- \`tests/test_v008_reconciled_labor_duality.py\`
- \`tests/test_v008_reconciled_fiscal_double_entry.py\`
- \`tests/test_v008_reconciled_stationary.py\`
- \`tests/test_v008_reconciled_shock_irf_gate.py\`
允许新增脱敏交付：
- \`versions/0.0.8/execution.md\`
- \`versions/0.0.8/scientific_reconciliation.md\`
- \`versions/0.0.8/acceptance_summary.json\`
最多13个准确路径；不强制全建。旧\`multi_province/one_turn.py\`、\`firm.py\`、\`wage.py\`、HJB/KFE、所有源码已有类与test、\`__init__.py\`、科学runner、旧dirty、\`versions/0.0.8/plan.md\`、治理文件均不可修改。不得把新实现隐式export到原生产路径。

## 5. 稳态检验、IRF检验与明确的不等价资格

**Gate A：经济学独立oracle（必须）**。1省、非对称2省、人工31省中检查双边劳动—工资对偶、税前/净收入/税/迁移成本恒等、财政逐项双边记账、资本私公所有权不重复、人口缩放、原/目的矩阵方向、FOC、分布异质性Jensen反例及资产负债表/金融中介分账。至少各设计一例错误税两次扣、\`AtTax\`跨账户重复、\`Lt_prev\`均值对总量的拒绝用例；\`N=1\`/零通胀掩盖缺陷的用例不得唯一支持通过。

**Gate B：人工条件稳态数值可行性（独立且受限）**。使用完全虚构的1、2和31省正参数经济体、显式人工 household distribution/asset holdings/资本分配条件和财政平衡工具，数值求解并审计：所有定量市场供需、firm FOCs、CES劳动/工资、政府预算、资源、账户、完整root向量/残差及停止次数。不得以\`Kt\`和\`Yt\`填函数输出或固定最优解来冒充求解；无法同时关闭全部被定义的剩余项则返回\`NO_CONDITIONAL_STEADY_STATE\`和最高残差、而非调整科学阈值/校准取PASS。**即便此门通过，结果仅为\`SYNTHETIC_CONDITIONAL_STATIONARY\`或\`SYNTHETIC_FACTOR_MARKET_STEADY_STATE\`；因为household HJB/KFE未联解且没有真实地区数据，不能称\`31_PROVINCE_HANK_GE_CONVERGED\`。**

**Gate C：冲击路径诊断（仅在Gate B稳态可接受后）**。允许在**明确人工外生AR(1)**、资本/家庭分布/财政策略固定或明确变化的条件下，用新模型计算已解稳态附近的条件冲击响应（TFP/工资税/公共资本至少各一个可行人工测试，可按预算选择小省份），每个期间重新检验本期静态均衡和现金账、路径起点为Gate B同一接受稳态。测试零冲击=零响应、不同冲击幅度局部可线性缩放、回归性、期末残差、改变路径长度不敏感及数值不爆炸；不要预设所有变量正向响应，反例说明其机制。可记录\`CONDITIONAL_SHOCK_PATH_DIAGNOSTIC\`，**不得将逐期重复静态解、旧\`mpHANK_shock_2000.m\`20期调用或画图标成\`DYNAMIC_HANK_IRF_ACCEPTED\`**。

**Gate D：正式IRF准入审查**。逐项检查是否已经有：被接受的带资产\`(a,b,z)\`跨期家户最优化/终端V、前向KFE/分布守恒、明确政策冲击过程/资本与政府债务状态方程、firm/NKPC期待通胀结构、货币政策及跨期市场出清、初末稳态、horizon/terminal residual与资产库存流量相容。如果缺任何核心闭合就返回\`IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE\`并列准确缺项，不能生成假正式IRF。**本版首个实施任务不授权原冻结HJB/KFE、真实31省HANK或动态模型实验。** 未来真正real/synthetic complete-HANK与IRF须明确新科学数值预算和独立审议（可保持为V008后续风险门，不预先立V009）。

用户要求的“看看是否能得到稳态和IRF”按证据实际报告：Gate B/C 可先取得数值可行性或明确失败，Gate D如果不具备跨期闭合必须诚实BLOCKED，不能用人工曲线满足Results。

## 6. 本轮数值/文件/资源预算与零预算

一次长任务总可操作时间≤10小时。允许最多8个新focused测试进程（包含修复/最终树验证），每进程≤600秒、峰值工作集目标≤512MiB（不可测记UNKNOWN）。Gate B新人工条件稳态求解总attempted≤12，其中人工31省求解≤2，单求解函数evaluation上限≤200；Gate C新人工冲击路径attempted≤4，每条最大40期，不隐式增加。失败与中途停止的调用全部计attempted，失败/修复也吃进程额度；不得按省/按日期重置。验证在进程预算内记录自动化pytest调用的所有实际solver attempts，而不是仅记用户级driver。
新增Git/candidate_view与操作性存储≤256MiB，人工fixture/LOCAL_ONLY日志≤64MiB，公开脱敏文档≤4MiB，新增总≤324MiB；涉及磁盘snapshot须先估算容量并原地留界。命令失败先stop其依赖、按V1.2保留stdout/stderr/exit/identity；普通工程修复自主完成，不为通过而更改原冻结经济方程。
- 原真实C8/31省经济输入，旧或生产HJB/KFE、C9/outer、任何真实消费者、MATLAB运行、protect A16/window试验、model_activation、Results、公开实值、真实GE/IRF科学预算：**0**。
- 无需沿用或跑V006 40项合成测试、V007 SOURCE_ONLY报告作为新测试；只读精确旧代码/文档/PDF/原MATLAB \`.m\` 文本以核实模型理论，原文件不得复写/发布。
- 当Gate B/C无收敛或资源封顶，Codex**仍交付**有数学oracle支持的新代码与失败/阻断证据；不可自行跑另一批旧科学测试、扩quota或悄悄改参数。

## 7. 候选交付与Astra验收上限

候选须基于 \`d8bb49d86ea674ea4ff5e3fdf03929baa08a6514\` 唯一parent建立隔离新branch，执行准确白名单diff，最后一个封存tree要有独立focused test receipt。允许一次非force候选push + SHA/tree/changed-path远端readback；旧main/原worktree不动。若候选因branch/仓库保护失败，LOCAL_ONLY完整报告停止，不强推，不偷合并main。

Codex集中报告必须分别列：
- 接受科学的L1一税与实际实现哪一层，AtTax/migration/clip/财政工具哪些仅为\`SYNTHETIC_SCENARIO\`；
- Gate A oracle、Gate B残差/solver attempt /人工省数、Gate C条件冲击图表可选但须明示\`NOT_REAL_IRF\`、Gate D真实动态缺项；
- 可信代码/数值/现实数据/动态/Results五类不同证据资格；
- 资源/错误、原dirty/index保全与未可独立网页回读的LOCAL_ONLY证据；
- 下一次完整HANK稳态/IRF若要开始所需的**一次集中**动态方程+安全数据/科学预算申请，不能把B/C的PASS当作数据/动态权限。

Astra本版首门最高可接受\`CORRECTED_MODEL_SYNTHETIC_ECONOMIC_ACCOUNTING_ACCEPTED\`、\`SYNTHETIC_CONDITIONAL_STATIONARY_ACCEPTED\`和\`CONDITIONAL_SHOCK_PATH_DIAGNOSTIC_ACCEPTED\`（逐项证据/残差独立确认），**不等于**\`TWO_ASSET_HANK_STATIONARY_GE_ACCEPTED\`或\`DYNAMIC_HANK_IRF_ACCEPTED\`、不等于真实31省政策反事实/投稿Results。

终态 \`WAIT_ASTRA_V008_CORRECTED_MODEL_NUMERICAL_GATE_ACCEPTANCE / STOP\`。V0.0.9 NOT_STARTED；如本版下一高风险门被提议仍必须另行独立批准，不自动继续。
