# V0.0.9 正式冻结：内生两资产 corrected HANK 的合成稳态首个数值长任务

冻结日：2026-10-15（Asia/Shanghai）
**状态：V009_FROZEN__OWNER_ADOPTED_SYNTHETIC_TWO_ASSET_HANK_PILOT__WAIT_SEPARATE_BOUNDED_SCIENTIFIC_IMPLEMENTATION_AUTHORIZATION__REAL_HANK_AND_IRF_CLOSED**
**本计划冻结本身不签发实施/数值许可；仅在Astra独立核验本固定Git commit、plan blob及代码基线后另行签发一次性独立限额实现授权。**

## 0. 来源、Owner采纳及优先目标

Owner已明确批准E1–E3人工两资产HANK科学研究基准，准确记录于 [V009 Owner科学决定](owner_scientific_adoption.md)；之前的版前DRAFT在commit `53d12f7a2117487f949a2bebb1819ae55e006960`、blob `a61dd9d93b8bc36351540dd348ef917870a621ba`；[Astra SOURCE_ONLY科研审议](scientific_proposal_review.md)固定在 `521a3a2971f0557712290deb84963ff9d65e87ba`、blob `ed18520862e63119511a2c91067437a81518bcfa`，含固定S跨省资本基金回流`R_j`修正。不可因数值求解失败改写这些历史冻结/审议的证据资格。

**只实施一个长任务，科学优先级：**
A. 在人工1省、`(b,a,z)=20×20×2`网格上计算内生HJB→同最终策略的stationary KFE→家庭资产/劳动/全国政府财政/商品等市场联合真实数值稳态；不给定最终家户分布与家庭资产均值。
B. 仅在A的全部冻结验收门合格并独立记录后，尝试人工**非对称2省**同一系统。
C. 若任一阶段失败，将失败作为科学结果封存并停止依赖后续，不降低阈值、不通过重调参数追PASS。
本版**不**运行31省HJB/KFE、24×24网格/1152维KFE、动态HJB/forward KFE/IRF、现实数据或生产HANK；V008的1/2/31省给定分布条件稳态及140期静态冲击只作已接受数值参考，不算本版完整HANK通过。

## 1. 基线、工作树及隔离

唯一候选源码父提交 **`d41d229b681e09b913c21deff7a057085b9bc419`**，tree **`88833acf90613380afa30ab8d6ee7e0297e98664`**。`NEXT_BASELINE_ADOPTION=ADOPTED_FOR_V009_ISOLATED_SYNTHETIC_HANK_ONLY`，不代表合并`main`或把原D盘模型树HEAD checkout到候选。Codex需先只读核准确commit、branch/source闭包、固定计划 blob、本地原树HEAD/index/8 tracked dirty/外置common-dir及上次未扫描untracked/ignored的保护等级；在**新、独立、非reparse**的candidate Git目录创建新分支，不写原index/objects/ref，安全read-only alternates必须核。
原模型worktree `D:\ProjectTemp\c5k1bturn56`、旧HEAD `a1db8c114dec0ab69d69a5576e153a7f868cba0e`、8 dirty中`government_assets.py`和`middle_stage.py`及6治理文件、历史untracked/ignored和C盘B3有限备份均不改/扫描/覆盖/备份或清理。私有用户原MATLAB ZIP/论文PDF仅按需作为辅助SOURCE_ONLY，不能用其历史bug当经济权威或发布全文。

仅能新建下列13条白名单，既有`src`、测试、model runner、`__init__.py`、旧历史文件和冻结计划不可修改：
- `src/ch5_two_asset_hank/reconciled_hank/__init__.py`
- `src/ch5_two_asset_hank/reconciled_hank/contracts.py`
- `src/ch5_two_asset_hank/reconciled_hank/household.py`
- `src/ch5_two_asset_hank/reconciled_hank/stationary_kfe.py`
- `src/ch5_two_asset_hank/reconciled_hank/accounts.py`
- `src/ch5_two_asset_hank/reconciled_hank/stationary.py`
- `tests/test_v009_household_hamiltonian.py`
- `tests/test_v009_stationary_kfe.py`
- `tests/test_v009_accounts_and_markets.py`
- `tests/test_v009_stationary_acceptance.py`
- `versions/0.0.9/execution.md`
- `versions/0.0.9/scientific_closure.md`
- `versions/0.0.9/acceptance_summary.json`

本候选不替换或导出到原`multi_province/one_turn.py`或`corrected_diagnostic/nonlinear_continuation.py`，不得偷偷把新数值输出标记为original-C8或原已接纳Python执行。只有完成真实算法的模块可新增，不能以六个空外壳占位。

## 2. 新人工HANK经济公理：两资产、CES和国家账户

来源省`i`、目的省`j`，人口`N_i`为`NU_100_PERSONS`数值、货币`MU_10WAN_YUAN`、时间`MODEL_TIME_SYNTHETIC`，两资产`a,b`的家庭单位为`MU/NU`；私人基金权益`a>=0`、流动`b>=0`是全国政府发行债券**家庭持有权**，`b`无私人借贷spread，调整成本真实资源消耗。稳态人口不等于户数，不用`N=P/3`。

家庭 CES 指数与双边工作地价格：
\[
\ell_i=\left(\sum_j\phi_{ji}h_{ji}^{1+\eta}\right)^{1/(1+\eta)},\quad
W_i=\left[\sum_j\phi_{ji}^{-1/\eta}((1-\tau)w_j)^{1+1/\eta}\right]^{\eta/(1+\eta)},
\]
\[
h_{ji}=\ell_i\phi_{ji}^{-1/\eta}((1-\tau)w_j/W_i)^{1/\eta},\qquad
\sum_j(1-\tau)w_jh_{ji}=W_i\ell_i.
\]
政策劳动`ell_i(b,a,z)`对效用指数定义，而目的总有效劳动`L_j=\sum_i N_iE_{\mu_i}[z h_{ji}]`；没有旧Ct均值迁移或工资二次扣税。`eta`为地区CES配置曲率、`nu`为家庭劳动厌恶曲率，彼此独立。

家户无限期真实最优化：
\[
\max E\int_0^\infty e^{-\rho t}\left[u(c)-\frac{\kappa_i\ell^{1+\nu}}{1+\nu}\right]dt,\qquad
u(c)=\frac{c^{1-\gamma}}{1-\gamma}\quad (\gamma\ne1).
\]
令 `d`表示b→a的连续转换速率，`Psi(d,a)=chi0*abs(d)+chi1*d^2/(2*max(a,abar))`，现金（家庭b）与财富（a）漂移：
\[
g_a=r_{a,i}a+d,\qquad
g_b=r_bb+zW_i\ell+T-c-d-\Psi(d,a),\quad
r_{a,i}=\sum_jS_{ji}r_j,\quad S_{ji}\ge0,\;\sum_jS_{ji}=1.
\]
首轮`AtTax=0, sigma=0, taper/clip=none`。`b`必须真实可偿债资产，不自行生成负负债、银行借贷或神秘供给。家庭KKT `q_b=u'(c)>0`，`kappa_i ell^nu=q_b z W_i`，`0∈q_a-q_b(1+∂_dPsi)` 与各边界互补；`a=0,b=0`处漂移禁止朝域外，不能通过控制裁剪、负梯度floor或扩散修复。

稳态家庭 HJB `rho V_i = max\{u(c)-kappa ell^(1+nu)/(1+nu)+V_b*g_b+V_a*g_a+Lambda V_i\}`，最终同一policy构造`Q_i`，`Q_i^T mu_i=0`，每省`mu_i>=0,sum(mu_i)=1`，只能在**唯一闭类、有限KFE误差**下取家庭分布矩；`Ct,At,Bt`皆为质量均值，劳动按两目的/状态积分并乘`N_i`。过去已采纳`(b,a,z)` F-order、HJB Delta=1000、同checkpoint B/D门、monotonicity-preserving first represented halving、scalar selector active-set和终端KFE exact-positive/唯一closed-class/restricted dense gesvd、完整`Q^Tp`验证属于**所选数值方法**，不能因初始人工模型收敛难就降低或替换；若原历史代码import依赖真实loader/路径，改为安全new pure wrapper/分离组件，不能修改原科学模块。

全国一套竞争性生产：`Y_j=Z_jK_j^alphaL_j^(1-alpha)`、`K_j=K_j^p+K_j^g`、`w_j=(1-alpha)Y_j/L_j`、`r_j+delta=alpha Y_j/K_j`，企业零纯利润，无markup/price-clipping/旧NKPC。不强加旧firm的迭代`Lt_prev`。省际私人基金数量与回报：
\[
A_i=N_iE_{\mu_i}[a],\quad B_i=N_iE_{\mu_i}[b],\quad
K_j^p=\sum_iS_{ji}A_i,\quad r_{a,i}=\sum_jS_{ji}r_j.
\]
`S`不进行来源真实性认证/最优组合求解，人工双省用精确固定`S`。动态/资金核算必须写清：
\[
D_i=N_iE_{\mu_i}[d],\quad \dot A_i=r_{a,i}A_i+D_i,
\]
\[
R_j=\sum_iS_{ji}A_i(r_{a,i}-r_j),\quad \sum_jR_j=0,\quad
\dot K_j^p=r_jK_j^p+\sum_iS_{ji}D_i+R_j.
\]
私人资本gross投资`I_j^p=\dot K_j^p+delta K_j^p`，不要只按当地`r_jK_j`重复加收入或漏`R_j`。单省`R=0`不能替代非对称双省数学oracle。首版S固定，S(t)动态、K1B旧lagged/raw-ra0/S吸引力模型不激活；原C8历史不改。

全国政府唯一发行人，B^g>0固定人工债务存量，必须`sum_i B_i=B^g`。公共资本`K_j^g`为给定存量，维护流`I_j^g=delta K_j^g`；政府收到`(r_j+delta)K_j^g`毛租金、支出`delta K_j^g`维护，净为`r_jK_j^g`，不能双计折旧。人工政府购买G为单独给定的正资源流，工资税只计`tau sum_j w_jL_j`一次；全国`T`为统一人均财政工具，可负（相当于lump-sum tax），必须由同一模型内求解、不是事后隐藏残差。稳态国家预算：
\[
0=\tau\sum_jw_jL_j+\sum_jr_jK_j^g-G-r_bB^g-T\sum_iN_i.
\]
家庭b正/资本a权益市场，国家债券与私人资本股权发行、公共资本、财政税/政府存量及商品资源`sum Y=sum_i N_i E[c_i]+G+delta sum_jK_j+sum_i N_i E[Psi]`都须独立验证。资产价格、利润发行与财政工具若新增未经采纳的会计项一律BLOCKED；按家庭资产存量与企业反向资本构造的一致性由真实供需残差验证，不能用定义强制0代替市场出清。资源约束即使由Walras冗余也必须逐项另算且失败不PASS。

## 3. 冻结的人工校准/网格/求解初值（Astra方法学选择，非中国实测参数）

**以下所有数字仅用于OWNER批准的纯合成pilot；Astra在首个实际HJB/KFE模型调用之前一次性预注册。不可根据运行后的收敛/资本/财政残差修改参数、网格、时间单位或初值追PASS。原历史delta=.025/论文=.0025/年度合同delta=.10/V008 delta=.05均不自动形成新现实校准；本段delta=.10是独立`SYNTHETIC_PILOT_CHOICE`，不援引历史年度合同的接受资格。**

| 人工参数 | 固定取值 |
|---|---|
| `rho` | 0.05 / MODEL_TIME_SYNTHETIC |
| `gamma` | 2 |
| `nu`，`eta` | 5，1（不同的劳动厌恶/配置曲率） |
| `kappa_i` | 1省 `(1.0)`，2省 `(1.0,1.02)` |
| `chi0`，`chi1`，`abar` | 0.10，2.0，0.10 |
| `alpha` | 0.30；竞争性价格markup=1，corporate_tax=0（零纯利润） |
| `tau` | 0.05（全国一税一次） |
| `delta_private=delta_public` | 0.10 / MODEL_TIME_SYNTHETIC |
| `z`和生成元`Lambda` | `z=(0.8,1.2)`，行生成元`[[-1/3,1/3],[1/3,-1/3]]` 每MODEL_TIME |
| `b`资产网格 | `linspace(0,2,20)`，0下界，2上界（精确20节点，负债禁止） |
| `a`资产网格 | `linspace(0,5,20)`，0下界，5上界（精确20节点） |
| `V0(b,a,z)` | `-1/(rho*(1+b+a+z))`，只作为固定初始猜值，严格正b边斜率；**非HJB结果或经济校准** |
| `N` | 1省`(1.0)`；2省`(1.0,1.1)`，人工NU |
| `Z` | 1省`(1.0)`；2省`(1.0,1.03)` |
| `Kg` | 1省`(0.20)`；2省`(0.20,0.22)` |
| `Bg` | `0.4*sum(N)` 人工MU；1省0.4，2省0.84 |
| `G` | `0.06*sum(N)` 人工MU/MODEL_TIME；1省0.06，2省0.126 |
| `S_{ji}` | 1省`[[1]]`；2省目的行来源列`[[0.8,0.2],[0.2,0.8]]` |
| 宏观未知量/初值 | `x=(log w_1,...,log w_n,r_1,...,r_n,r_b,T)`；`w_j=1.0`、`r_j=0.04`、`r_b=0.02`、`T=0.0` |
| 其他人工费用 | `AtTax=0, sigma=0, clip=none, spread=0, private borrowing=none` |

所有省使用相同`(b,a,z)`排列与F-order，网格状态总维`20*20*2=800`。不含24×24研究，假想2省是非对称人口/生产率/劳动效用和Kg，`R_j`的数学oracle必须在**人工预设不同`r_j`与A_i**的SOURCE_ONLY纯算术阶段独立验证；由于稳态可能只实现固定S的平衡`R`，它不能替代该非对称检验。人工高b/a上界的最终质量须输出；若`a`均值趋于0、资产角点/截断不合格则FAIL，不换网格和参数临时修复。

## 4. 源复用、数学oracle、HJB/KFE及稳态验收

源输入必须安全fail-closed：新代码只从既有**纯数学**corrected_diagnostic selector/cost/boundary/generator取经过静态依赖审计的函数，或在新模块中独立实现同等已采纳数学规则并以不同oracle核对。禁止直接导入旧`nonlinear_continuation.py`或`q1_kfe_validation.py`当runtime，因其历史报告路径/800 hardcode/runner耦合；旧顶层`hjb.py/kfe.py`使用`(a,b,z)`索引和row-pinning/threshold KFE，不可调用。新模块/测试任何Python import先核闭包无真实数据路径、副作用、生产consumer及历史写入，确保原core scientific calls为0。

**Gate A 科学正误oracle（先于任何昂贵HJB/KFE）：**
1. 20×20×2 F-order与局部状态索引/数组/累积质量、z Markov生成元Q1=0；
2. CES primal/dual与状态劳动/单位缩放/税前工资金额、一次税；家庭Hamiltonian/独立标量FOC、调整成本零kink、lower-a/liquid边state constraint/KKT、拒绝非法负影子与二次扣税；
3. toy Q三状态或更小的`Q^Tp=0`解析闭类/非负质量/SVD rank-nullity，对多个闭类、负质量、坏行和axis混淆的拒绝；`Qb=g_b, Qa=g_a, Q1=0`；
4. 省际资本S列守恒、`ra_i`加权回报、`R_j`不丢失、`sumR=0`、2省非对称`R=(3.2,-3.2)`的纸面oracle；人工全国融资/部门预算/商品资源从原始账户独立构造与人口复制/双计折旧拒绝；
5. 确认固定artificial parameter manifest唯一、Git源码/inputs闭包SHA清单、每次新根求解均从同一预注册模型参数加载，不能悄悄采用更有利的局部参数。

**Gate B 1省真正合成HANK稳态：**
- 内部HJB每次更新只能一次`Delta=1000`直接稀疏解、后向线性解相对误差≤`1e-12`；Bellman残差B≤`1e-8`、Value change D≤`1e-7`须是同一已合法checkpoint；所有代表的b边`(n_b-1)*n_a*n_z=760`斜率严格正，完整HJB更新遵循Owner采纳`alpha∈\{1,1/2,...,2^-52\}`的首个合法非bitwise相同候选；拒绝导数floor、人为截断、松门和第二替代solver。
- 每一次可核`Q`必须使用原policy真实drift，满足无域外跳转、offdiag≥0、`Q1≈0`与坐标drift恒等；终端KFE只用**最终同policy**的Q，一次exact-positive SCC、唯一闭类，restricted `Q_CC^T` dense `gesvd`（1次/家户）、正向归一、瞬态精确零嵌入、full`Q^Tp`校验。任何多闭类、rank/nullity不相符、负质量、回读身份不一致均FAIL，禁止替换一行、全空间退路、runtimes reparse/修复负p。
- 每次宏观残差eval重新求合格HJB/KFE并读取`Ct,At,Bt,Lt`内生分布；n省宏观独立未知`2n+2`：n工资、n资本净回报、一个rb、一个全国T；n wage FOC、n rental FOC、1债券市场`sum_iN_iBt_i=Bg`和1全国财政预算联立。private capital`Kp=S*(N*At)`，`Kg`如上给定；商品资源残差必须独立另算，不放进root凑数也不得无检查忽略。报告全部原始/归一化残差；`At>0`、`Bt>0`、真正Kp/劳动均正，国家债券债权等于国家负债，真实资产角点/上界质量可审计。
- 宏观独立每项缩放残差≤`1e-8`、现金财政/商品/来源目的资金会计残差≤`5e-11`；终端KFE误差、价值B/D及资产边界按冻结原验收合同不能松；人工上边界概率总质量≤`1e-6`（各省`b=bmax`或`a=amax`的并集）；`At,Bt`非退化。若goods residual无法满足、行业结构不闭合则`NO_SYNTHETIC_HANK_STEADY_STATE`并给出科学原因，不能把Walras冗余当作自动通过。

**Gate C 非对称2省条件执行**：仅Gate B 1省主网格严格达全部标准时允许同样固定20×20×2两省共同联立；按源/目的真实CES与S、全国唯一政府与资本`R`验各省/全国账及完全新的HOUSEHOLD HJB/KFE调用。相同门槛，不自动缩小/改变网格。若资源预检不能支撑则`TWO_PROVINCE_RESOURCE_BLOCKED`不启动；2省失败不追改已经独立验证的1省基础。

**Gate D 仅IRF缺项核验**：不创建或运行任何动态模型：识别backward HJB/forward KFE/资本基金/政府债务时序、前瞻价格、政策闭合和初末稳态/终端条件的缺口并返回`IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE`。无正式动态IRF或政策结果图，不能挪用V008静态response。

## 5. 一次长实施硬资源预算与失败停点

- **最长8小时**（实际子进程累计如有更严格执行门则取更严格者）。
- **新focused pytest最多8个进程**，每个≤600秒；全新科学driver≤4个进程、每个≤2小时，所有发起/失败均计。
- **人工宏观完整外层求解总≤4尝试**，1省≤2、2省≤2；每1省solve完整宏观残差eval≤24，每2省≤32。每个eval最多每省1次家庭HJB→终端KFE，**新家庭求解总≤176**（2×24×1+2×32×2），单家户≤100次HJB直接更新/≤101次policy/Q mapping/≤1次终端SVD，实际失败和未完成次数均计；整个版本HJB直接更新≤17,600，policy/Q映射≤17,776，terminal restricted gesvd≤176。
- `selector/scalar-root attempted`每家户≤400,000、版本累计≤70,400,000；switching/root分类另记实际attempted，不在不同进程/省份重置；全部预算必须从持久`LOCAL_ONLY`安全账本同步计数，模型命令失败先STOP依赖，无法可靠计数即STOP。
- 运行前从准确grid shape推导维数与rank标准（800、全闭类时rank799）；terminal restricted class size m时仅检查rank m−1/nullity1；一个800×800 dense double约5.12MiB，SVD临时矩阵需采样，不将估算当真实RSS。峰值工作集上限目标512MiB，若实测达到即停止下一个科学进入；不可测明写UNKNOWN及资格缺口。总新增文件存储≤256MiB（操作性Git≤64MiB、候选视图≤32MiB、人工数值/LOCAL_ONLY证据≤144MiB、公开脱敏≤16MiB，所有临时态计入），超过任何子上限立即STOP，不改名躲账；启动前必须评估输出规模。
- **同一n的第二次完整macro attempt**原则上只为冻结许可范围的**最终树独立验证**预留；如初始尝试遭一般软件bug失败，可在仍有预算时修复后重试，但若导致最终树科学门缺可核回执，则只提交`WITH_OBSERVATIONS/NOT_ACCEPTED`而不隐瞒。科学失败（无最优控制、HJB不收敛、多KFE闭类、rank/nullity、资产债务不出清、上界mass、宏观根/资源残差失败）即记录终态并停止后续依赖，禁止重校准、改变科学网格/guard和重新开额度救PASS。
- 31省全HANK求解、24×24/维度化rank推广、动态HJB/IRF、真实2017/2018/C8 protected文件存在性/stat/read/hash/parse/extract、旧HJB/KFE/C9/outer/source-faithful consumers、MATLAB程序运行、V008已耗旧路径/求解、A16/G0/B3保全与攻击、model_activation/Results **预算全部0**；本次合成新HJB/KFE数值额度专属新`reconciled_hank`，不会复活历史科学调用。

## 6. 候选封存与独立验收

Codex在全新受控隔离目录创建候选分支，唯一parent上述`d41d229b681e09b913c21deff7a057085b9bc419`。仅13白名单路径可改，严格PRE_SEAL报告与独立候选外最终交付回执分离（不能在Git文本里自嵌最后commit SHA）；至少一个在科学额度内完成的final-tree focused验证/真实科学回执，GitHub远端一次普通non-force push及远端SHA/tree/whitelist/readback。若不能安全做到，LOCAL_ONLY STOP，不强推、不删除/清理原资产。
交付三份候选文件应清晰记录Owner E1–E3人工条件、所有HJB/KFE会计接口、每次root与跨省基金`R`计算、每组宏观未知/残差/初值、转移政策、失败/消耗预算/内存及路径身份和证据资格。原始人工资产分布/长日志留LOCAL_ONLY，公开只提供可独立复算的必要人工数值与脱敏校验。提交给Astra后独立GitHub源审/数值交叉复算，不自授科学ACCEPT。

可能的有限ACCEPT：`SYNTHETIC_TWO_ASSET_HANK_ONE_PROVINCE_STATIONARY_ACCEPTED`及在相应证明后`SYNTHETIC_TWO_ASSET_HANK_TWO_PROVINCE_STATIONARY_ACCEPTED`。如果只有算法实现和oracle，最高仅`SYNTHETIC_HANK_ENGINEERING_ORACLES_ACCEPTED`，不得宣称完整稳态已求得。完整真实31省HANK GE、动态HANK IRF、论文Results仍FALSE，且C9旧资源账与A16/window的资格不变。

最终`WAIT_ASTRA_V009_SYNTHETIC_HANK_NUMERICAL_ACCEPTANCE / STOP`；V0.0.10 NOT_STARTED，本冻结不自动启动下一科学门。
