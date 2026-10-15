# V0.0.9 原HANK→corrected HANK完整稳态/动态路线：Astra独立科研审议（版前、未冻结）

日期：2026-10-15（Asia/Shanghai）
**状态：`V009_SOURCE_ONLY_SCIENTIFIC_PROPOSAL_REVIEWED__WAIT_OWNER_NEW_SYNTHETIC_HANK_ECONOMIC_AND_NUMERICAL_BASELINE__NO_SCIENCE_EXECUTION`。本版仍处DRAFT，非新的经济学方程采纳、非HJB/KFE计算许可、非真实2018/C8数据或IRF授权。**

## 1. 来源、Git身份、同步事实

- Owner持续立版授权已于治理HEAD `53d12f7a2117487f949a2bebb1819ae55e006960` 的 `docs/CH5_OWNER_CONTINUOUS_VERSION_DIRECTIVE_20261015.md` 固定；V009原DRAFT plan blob `a61dd9d93b8bc36351540dd348ef917870a621ba`，`versions/0.0.9/plan.md`不追改。现行V008 accepted candidate `d41d229b681e09b913c21deff7a057085b9bc419`，tree `88833acf90613380afa30ab8d6ee7e0297e98664`，相对上一代码基线仅13新增白名单，未合main。下版代码起点建议继承，`NEXT_BASELINE_ADOPTION`仍PROPOSED/UNDECIDED。
- Codex通过Owner本轮上传的 `V0.0.9_M2_FULL_CORRECTED_TWO_ASSET_HANK_STEADY_STATE_AND_DYNAMIC_CLOSURE_PROPOSAL` 回报：53份精确Git-tracked文档/源码（45份研究正文597,390B），23次只读Git调用无失败、0科学Python/MATLAB/HJB/KFE/pytest/模型/受保护原件、0源码修改及Git push。8个dirty类别/staged=0、原HEAD/分支保持只是`CODEX_REPORTED_READ_ONLY`；未重新hash原dirty/index，不能宣称完整字节恒定。
- Codex报告本地新建独立镜像五份治理文件及`SYNC_RECEIPT.json`，总104,808B，receipt SHA256 `22BC74F8EC66C2D77483769DEA4A3512E5BC6DAAAD0C00354FE02F1C8150B75A`；其中Owner指令、V1.2、知识入口、CURRENT、版本登记的Git blobs分别 `125663e485db2129e1866acd2051a366ef61b2e0`、`952c422108e55fda21045ebd777f730c3a9164ab`、`38e6ee104a3b2e6905181f51a492a129eb0a17aa`、`47983c342352ea7766922963a201abec50de352e`、`466be9349e3eba8c24a81188b5413268ad90d0cf`；**Astra独立GitHub读取确认上述五个远端blob存在且匹配，但未访问D盘LOCAL_ONLY镜像/回执，不可声称独立核实实际磁盘字节。**
- 两个行政错误：首次镜像调用超Windows命令长度而未执行；后续副本多一LF被blob复核拦下，经Codex本地修复。未涉及原工作树或科学尝试。无需再重复文档同步；**本次不改变现行工作流V1.2，也无需发起工作流变更审批**。

## 2. 来源可复用审议：接受哪些建议、拒绝哪些推断

- 独立GitHub静态核 `src/ch5_two_asset_hank/indexing.py`是`(a,b,z)` a-fast F-order；`corrected_diagnostic`为`(b,a,z)` b-fast。不能按相同形状直接替换索引；所有源KFE/策略数组应以轴顺序、byte-order和shape逐项oracle检查。
- 原top-level`kfe.py`通过替换归一化方程行解线性系统，且用阈值SCC；与已Owner采纳的**exact-positive unique closed class + restricted dense gesvd + same-Q final check** 不兼容。不能以旧“kfe.py”名称在新corrected-model直接复用。
- `corrected_diagnostic/nonlinear_continuation.py`、`q1_kfe_validation.py`、`v1_q1_topology.py`实有硬编码`N=800`、`(20,20,2)`、760条b边、rank799、`gamma(N+64)`和特定exact-positive edges。需要单独验证后才能推广到24×24×2，不能仅把800字面替换成1152；旧已接受800维科学证据不得追改。原HJB的`Delta=1000`、单次稀疏解、backward error/B/D门、正b斜率单调性；终端KFE单闭类、restricted-gesvd和精确零瞬态等是研究方法约束，但新经济输入兼容性必须另证。
- V008的6个reconciled模块可提供CES双边对偶、单税/全国财政人工账和数值残差报告，但其给定资产/分布的Newton稳态和逐期静态path不是完整HANK/HJB/KFE求解器，也没有跨期IRF；不能因此重开V008已耗完的31省root/路径预算。
- Codex正确提出`V(b,a,z)`、HJB控制/KKT、`Q^T mu=0`、内生`At/Bt/Ct/L`、资本份额`S[j,i]`/双边劳动、政府账/企业、资源约束和市场条件的完整系统，经济期t与求解迭代k应分账；动态Backward HJB/Forward KFE/资本与债务状态/前瞻定价/初末稳态为独立后续许可。**不过本次提交的经济账户还存在以下必须修正的跨省基金资金流问题。**

## 3. Astra新发现：固定S和不同地区资本回报下的省级投资再配置恒等式

本项为**纯代数推导**，不需读取原C8或运行科学solver，不能自行提升历史C8的经济资格。

定义来源省private基金权益`A_i=N_i E[a_i]`、从液态向非液态净投入`D_i=N_i E[d_i]`、目的省资本`K_j^p=Σ_i S_ji A_i`、来源基金平均净回报`r_{a,i}=Σ_j S_ji r_j`。在新synthetic `AtTax=0`、无收益taper/基金收费、`S`固定的候选下，家户资产漂移给出：
[
dot A_i=r_{a,i}A_i+D_i,qquad
dot K_j^p=sum_i S_{ji}(r_{a,i}A_i+D_i).
]
`D_j^{alloc}=Σ_i S_ji D_i`时，严格省级身份是
[
dot K_j^p=r_jK_j^p+D_j^{alloc}+R_j,qquad
R_j=sum_iS_{ji}A_i(r_{a,i}-r_j),qquad sum_jR_j=0.
]
如同质私公资本的该省净折旧率`delta_j`，新私人总投资`I_j^p=dot K_j^p+delta_j K_j^p=(r_j+delta_j)K_j^p+D_j^{alloc}+R_j`。若`S=S(t)`，还需`Σ_i \dot S_{ji} A_i`及其经济基金再配账户。
**Codex方案§4的`I^p=(r+δ)K^p+D`只可无歧义用作全国总量/同率/显式含R账户的特殊简式；不能当作一般省级投资资金流。**
反例：两来源各有100基金权益，S对角0.8、异地0.2，目的净资本回报0.10/0.20，来源基金回报0.12/0.18。在`D_i=0`条件下，两个目的资本存量均100，严格`dot K^p=(13.2,16.8)`而按本地`r_jK_j^p=(10,20)`给出错误，差额`R=(3.2,-3.2)`，全国净额仍为0。新模型是**省际外溢**研究，这一来源/目的地基金现金转换不能遗漏。
除非单独采纳动态变份额/结算，研究第一阶段选固定S和显式`R_j`更可审计。对`AtTax>0`或家庭回报`tilde r_a!=r_a`须另加费用/政府归属，不能直接应用上式。

## 4. 三项真正新的Owner经济与数值路线选择（优先完整一包批准）

### E1 两资产产权、b债券及转换会计

**Astra建议：只作为首个全合成HANK科研试验的明示pilot制度**，不代表真实中国制度：`a>=0`为私人实体资本基金权益，`b>=0`为**唯一全国政府债券**（无私人借贷spread/金融中介），来源`a`经固定列随机S分配目的地私人资本；资产收益先采用同一期净回报`ra_i=Σ_j S_ji r_j`，`dot a=ra_i a+d`、`dot b=rb b+zW_i ell+T-c-d-Psi`；调整成本`Psi`为真实资源消耗；`AtTax=0`、`sigma=0`、clip/taper不适用于此新synthetic试验，不追改历史C8合同。
资金分账必须带上述`R_j`、初始无`dot S`。`a,b`为2类资产但`b`不允许负值，所以不认证含私有借贷spread的完整最终HANK。

### E2 企业利润、全国财政及稳态工具

**Astra建议：首个人工全HANK稳态用竞争性无纯利润的企业，价格markup=1**，避免在未批准股票估值/利润发行权时把收益重复计入`a`。给定`K^g_j`和`B^g>0`，私人资本`K_j^p`由家户内生，生产`Y=ZK^αL^(1−α)`且资本与劳动FOCs真实求解，工资全国税只扣一次，国家政府税收/债息/维护公共资本/公共消费/人口转移按单个全国账户。统一`T`是明示可正可负的净人均财政工具；若负值即lump-sum税，不冒充纯补贴。公共资本gross rental需与用于净资本回报的折旧一致；建议人工`δ_g=δ_p`，政府收`(r+δ)K^g`、支维护`I_g=δK^g`，不能同时两次扣δ。
这一竞争性研究pilot**不是完整New Keynesian粘性价格/动态NKPC模型**。未来markup/利润所有权、银行与政府债务、零/非零稳态通胀需另经科学采纳。
宏观未知量可按Codex `(logw_j,r_j,rb,T)`的`2n+2`结构设计，但需要逐次内生HJB/KFE/资产供需、政府财政和独立商品资源残差；若任何非零残差未闭不能以Walras口号省略。

### E3 模型时间、资产网格与合成数值硬预算

**Astra建议**：初版明确`MODEL_TIME_SYNTHETIC`，绝不把历史0.025、论文0.0025或现有人工δ0.05混成真实已采纳参数。先请Codex在正式冻结前基于可核已接收源将`rho,gamma,nu,eta,chi_0,chi_1,delta,Lambda,alpha,tau,B_g,Kg,S,`资产端点/初值及债务财政工具**一次性预注册**（每项来源=OWNER_ADOPTED_ARTIFICIAL_BASELINE或明确人工建模选择；无法确认年度重校准原Owner范围则不能借用其科学身份），不允许事后因收敛失败调参求PASS。
首轮仅`20×20×2`主网格、1省真实HJB/KFE/资产市场联合求根；若已得到可靠门后才进入2省。任何`24×24×2`网格/全b边单调性/维度化KFE rank和算术误差界推广都须先经过独立数学oracle和明确的本次Owner采纳范围，不对旧800维证据追改。31省HJB/KFE和动态IRF科学调用预算先保持0，后续另立清晰门。Codex提出的≤8小时、≤8个focused pytest、单省/双省主网格+加密各≤2次、每次≤24/32外层evaluation、每家户≤100直接HJB更新/一个restricted-gesvd、总家庭≤176、512MiB与256MiB新增存储可作为**下一次冻结时的最高候选上限**，不是当前可消费额度；要从实际调用依赖闭包、SVD资源与失败计数重新审计。

上述E1–E3属于**实质新经济学与新HJB/KFE科学数值权限**，已授权的“连续版次DRAFT”不足以自行签发。若Owner一次性批准该研究pilot和本段数学修正，Astra才能正式冻结V009的精确实施范围、数值guards/asset域/具体人工参数/资源，并另签独立Codex Python合成科学实施许可；原C8/真实数据/旧科学与C9关闭不变。

## 5. 当前结论与停止理由

**`V009_SOURCE_ONLY_SCIENTIFIC_PROPOSAL_REVIEWED__WAIT_OWNER_NEW_SYNTHETIC_HANK_ECONOMIC_AND_NUMERICAL_BASELINE__NO_SCIENCE_EXECUTION`**，仅`SOURCE_ONLY_SCIENTIFIC_PROPOSAL_REVIEWED_WITH_CAPITAL_FUND_REBALANCING_CORRECTION`；尚不接受候选资金分录为最终科学方程。当前V009 DRAFT，不签发实现、科学HJB/KFE运行或任何真实C8访问许可；Codex文档镜像仅CODEX_REPORTED_WITH_LOCAL_RECEIPTS，无必要重新要求同步一次，也没有变更V1.2工作流。

仍保持原`(b,a,z)` corrected F-order、已采纳HJB Delta=1000/单解/B/D门、终端KFE exact-positive/唯一闭类/restricted gesvd等旧历史资格。旧Option1、raw-ra0 lagged同S、C1、人口/人均不N=P/3、2017/2018回溯及价格方法合同不追改；A16 UNRESOLVED/FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、C8原件A–D REQUEST_ONLY、旧科学和真实消费者预算CLOSED。V0.0.10 NOT_STARTED；Owner确定新pilot前不得擅自冻结或运行。
