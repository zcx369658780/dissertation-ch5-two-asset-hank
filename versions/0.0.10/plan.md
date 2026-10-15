# V0.0.10 正式冻结实施计划：原MATLAB方法的Python主线集中修复

**状态：FROZEN_IMPLEMENTATION_CONTRACT；冻结日期：2026-10-15（Asia/Shanghai）。**
**阶段身份：CH5_V010_MATLAB_FIRST_MAINLINE_IMPLEMENTATION_V1。**
**冻结文件自身的固定commit/tree由后续独立发布任务指定；不得把动态GitHub HEAD视为冻结身份。**
此前DRAFT blob `bcf1fb4aafd6304b46f1e4dd4109ccf7ff566bae` 保留在Git历史；原SOURCE_ONLY任务和先前科学验收保持不变。

## 0. 授权与成果边界

Owner已于2026-10-15恢复原MATLAB主线，并明确裁决GovInv原收益边界0.9/1.1、自适应Zt保留、C1旧验收仅历史有效；工资税按工作目的地且只扣一次、财政人均→省级总量桥接。Astra限域接受V010 SOURCE_ONLY方案，并在`versions/0.0.10/prefreeze_scientific_review_20261015.md`审议。Owner进一步同意继续正式冻结和实施。**本冻结计划本身不是运行指令；只有后续独立发布的`implementation_task.md`及`TASK_CURRENT.md`均准确匹配本计划固定Git身份，才能行使本文件所列的新预算。**

目标：在实际可信Python旧主线和已接受corrected数学模块上，一次集中恢复省级HA→多省单轮→GovInv/Zt有界稳态→原递推冲击；修真正实程序bug，输出可独立检验的synthetic实现和清楚的科学停止。不是新建人工HANK、Newton/fsolve/固定Bgov/内生T，也不要求本版得到现实31省GE、论文Results或完整前瞻动态IRF。

代码父（仅此推荐）：
- commit `a1db8c114dec0ab69d69a5576e153a7f868cba0e`
- tree `4a118642da526d6bf2dfb65a1130f4d59d371374`
- sole parent `cc2b94679c2c57ec01483b615305cf4ea1739c61`
它包含历史原顺序器和corrected已接受数学代码，但默认one_turn/旧HJB/KFE仍有缺陷，**不具有完整稳态或Results科学资格**。不得以最新V008/V009人工候选为父，不得回滚HJB/KFE、same-S/raw-ra0/lagged、人口人均和φ方向等已接受修复。

## 1. 实现合同：最小数学与接口

**1.1 HA** 每省两资产(b,a,z) `20×20×2`、F-order b-fast、`Delta=1000`。输入`rb,rah,w_eff,Tt,rb_gap`和省级参数/网格，输出`Ct,At,Bt,Lt_HA,AtTax`及终端政策、Q、概率质量和诊断。使用既有corrected selector（D1/D2/D3/F0364及边界原采纳规则）、同checkpoint Bellman B≤1e-8且value D≤1e-7、直接求解相对后向误差≤1e-12、deterministic 2^-k halving (k=0..52)、唯一闭类source-free KFE (`Q.T@p`、行和/边界/非负/单位质量)；任何省失败，该轮即失败，禁止仅靠旧`converged=True`。历史锁死seed/2018/C8的research runner **不可作为通用生产入口直接运行或修改**，只能重用已接受纯数学组件，在新窄适配器中清楚报告算法和不变量。分布质量和At>0/Lt>0是合格解目标而非任意价格必然成立的假设。

**1.2 省际劳动** `phi[j,i]=1+0.3*(pgdp_ref[i]-pgdp_ref[j])/(pgdp_ref[i]+pgdp_ref[j])`，`j`目的、`i`来源；给定参考年度的真实pgdp将是以后单独的数据许可，本版仅用冻结合成pgdp。双边税楔采用**目的地`tau[j]`**，`q[j,i]=wjt_gross[j]*(1-tau[j]-sigma[j,i])`；原加法楔不改为乘法。HJB进入已经扣过税的`w_eff[i]`，不得第二次扣`tau[i]`。允许内部`wages=w_eff,tau_HA=0,migration_cost_HA=0`这一标注清楚的数学等价接口，必须提供FOC/收入单次扣税解析oracle。构造`Lt_mat[j,i]`时仍按原来源平均Ct的公式乘`N[i]`；明确其与完整异质家庭政策积分或`N[i]*Lt_HA[i]`可能有偏差，独立记录，不偷偷替换为V008/V009双边归一化法。firm`L_j=sum_i Lt_mat[j,i]`不可再乘N。

**1.3 私人资本** `W_i=At_i*N_i`, `S[j,i]`含本地保留和外省配置，`sum_j S[j,i]=1`, `M[j,i]=S[j,i]*W_i`, `Kprivate_j=sum_i M[j,i]`；`rah_i=sum_j S[j,i]*ra0_raw_j`。沿用已接受K1固定foreign`theta_i`、foreign-only stable softmax；`beta_distance=2`, `beta_return=0.5`, 完整前轮的raw return进入下一轮score（zscore ddof=0），并与当轮数量/收益同一`S`。不得用旧foreign-only `capital_allocation.py`作为新主线分配器、C1覆盖GovInv、same-turn返回推同轮份额或夹改raw-ra0。

**1.4 企业/NKPC** 企业投入`Kt=Kprivate+GovInv`，分别保存`Lt_HA[origin]`、`Lt_mat[destination,origin]`、`Lt_firm_current[destination]`、`Lt_firm_previous[destination]`、`Lt_firm_ss[destination]`。原一轮的`Lt_prev=Lt_HA`错误必须修复。稳态手动迭代使用上一完整firm目的地劳动；冲击期原`mpHANK_shock_2000.m`实际传标志`1`，其`HANK_firm.m`采用**lagged-NKPC分支**，不能默改为另一个ss-reference分支。保留`ra0/raw`与用于边界的`ra_used`、`wt0/wjt_used`分账与clip补偿诊断；used触边不能伪装经济收敛。其余未经决定的利润、价格方程不得改写。

**1.5 GovInv/Zt与终止** 当outer本轮未达到收敛且`max_i abs(KN_i/tKN_i-1)<0.1`且`steady_state=True`时，依顺序逐省：若`abs(Y/Ytarget-1)>0.01`，`Zt_next=Ytarget*Kt^(-alpha)*Lt_firm^(alpha-1)`；若`ra_used<ramin+0.02`则`GovInv_next=0.9*GovInv`，否则若`ra_used>ramax-0.02`则`GovInv_next=1.1*GovInv`，其余不变。继续原`tKN_next=0.6*KN_current+0.4*tKN_previous`有界顺序外层；不自动添`GovInv floor`或C1。HJB全部PASS、全省K/L与Y对上期变化<冻结`reg_threshold`且used ra不触界，只够`OUTER_ITERATION_CONVERGED`；**冻结GovInv/Zt后关闭adapt并做独立同输入回读，且全部`abs(Y/Ytarget-1)≤0.01`，才能进一步声称`TARGET_CALIBRATION_VERIFIED`**。一切失败按证据停止，不为PASS改参数/容差/网格。

**1.6 目的地工资税与财政** `WageTax_j=tau_j*wjt_gross_j*Lt_firm_j`; `GovInc_j=Corptax_j+WageTax_j+N_j*AtTax_j+GovInv_j*ra_used_j-N_j*Tt_j`，`GovSurplus=sum_j GovInc_j-sum_i Bt_i*rb_i*N_i`仅诊断。财务总量与家庭人均量分别有单位桥接；不得把already-aggregate的Corptax/GovInv/WageTax再乘N，不得把GovSurplus变成零残差或增加`Bt=Bgov`/内生T。记录工资税额来源与`Lt_HA`和firm劳动桥残差，数量和收益的私人、国有产权单独分账。

**1.7 原递推** 起点必须为冻结并通过独立校准的稳态；逐期从baseline重设`Zt,GovInv,tau,corptau`等外生冲击字段，然后执行**一次**修正后的单轮HA/劳动/资本/firm/工资/货币财政，传递上期应递推的其余状态，不进入`_adapt`或`1eq`；测试冲击重置和零冲击回归。仅称原方法逐期条件稳态递推，不称前瞻动态完整HANK IRF。

## 2. 固定人工输入和V0边界（真实数据绝对禁止）

唯一新科学synthetic输入：`versions/0.0.10/synthetic_fixture_v1.json`，Git blob `40915658d93403cfc21b33a6b864b332b7857749`，schema `CH5_V010_MAINLINE_SYNTHETIC_TWO_PROVINCE_V1`。含两匿名省`SYN_A/SYN_B`所有名义参数、pgdp参照、税、人口、资本、价格、距离、迁移楔、人工GDP目标及3期TFP冲击。数值仅为**明确贴标的算法受界输入**，非历史V008/009 1:2比较、非现实北京河南/2018、非新计量估计，也非经济参数采纳。Code candidate中的`tests/fixtures/v010_mainline_synthetic_v1.json`必须是该Git blob的**原字节副本**，严格Git blob SHA一致；不能临场选择另一组数字救稳态。

**V0生成规则也在此冻结（无受保护旧seed依赖）**：每省每次独立条件HA输入进入时，在同一20×20×2网格上由当次`rb,rah,w_eff,Tt,rb_gap`推导。`r_b(b)=rb+rb_gap`当b<0否则rb；`r_a(a)=rah*(1-0.1*(a/a_max)^9)`；`R=r_b(b)*b+r_a(a)*a+Tt`；令`u=w_eff*z>0`；在`l>0,c=u*l+R>0`上求唯一正根`l-(u/alphal)^(1/phi_l)*(u*l+R)^(-gamma_c/phi_l)=0`。允许采用确定性bracketing+Brent标量根，根区间从`max(0,-R/u)+1e-12`至`1024`；绝对根误差≤1e-12、相对≤1e-12、最多100函数迭代，无法括根立即fail-closed，不floor c或删除状态。随后`c0=u*l0+R`，`V0=[alphac*c0^(1-gamma_c)/(1-gamma_c)-alphal*l0^(1+phi_l)/(1+phi_l)]/rho`，其中`phi_l=5`是Frisch倒数，消费负效用中劳动幂为`1+phi_l`（此式以本合同而非旧源码混乱符号为准）。**根与函数值须对照一阶条件独立oracle；V0只是初猜不构成新效用律**。禁止以旧MATLAB`Rah.*raah`初始化错误代替`a*r_a(a)`。生成`V0`前记录全部输入/代码/NumPy+SciPy版本；生成后以little-endian float64、F-order计算SHA-256并**在首次HJB尝试前**封存至本轮私有回执，作为执行输入身份。没有绑定/哈希或V0斜率非正不得启动HJB；不能临时改V0公式或clip为了通过。

注意：人工fixture中的财务/资产数只是单位一致性oracle，不能证明现实经济计量单位或校准；真实省级pgdp与数据桥仍未取证。

## 3. 准许修改的准确路径（只限独立候选工作区）

既有文件（仅相关函数最小更改）：
1. `src/ch5_two_asset_hank/multi_province/one_turn.py`
2. `src/ch5_two_asset_hank/multi_province/stationary_runtime.py`
3. `src/ch5_two_asset_hank/multi_province/steady_state.py`
4. `src/ch5_two_asset_hank/multi_province/firm.py`
5. `src/ch5_two_asset_hank/multi_province/wage.py`
6. `src/ch5_two_asset_hank/multi_province/migration_labor.py`
7. `src/ch5_two_asset_hank/multi_province/fiscal_diagnostics.py`

新增文件（仅）：
8. `src/ch5_two_asset_hank/multi_province/mainline_household_runtime.py`
9. `src/ch5_two_asset_hank/multi_province/mainline_response.py`
10. `tests/test_v010_mainline_household_binding.py`
11. `tests/test_v010_mainline_one_turn.py`
12. `tests/test_v010_mainline_controller.py`
13. `tests/test_v010_mainline_response.py`
14. `tests/fixtures/v010_mainline_synthetic_v1.json`（与冻结Git blob原字节匹配）
15. `validators/multi_province/v010_mainline_validation.py`

原`corrected_diagnostic/`数学代码、`capital_network.py`、原MATLAB、旧HJB/KFE、V008/009、保护的本地dirty源码、真实数据和全部科学既有报告**只读不修改**。历史数学修复只能在新适配器显式绑定；不能以复制一套不一致的改写solver取代。若实际不可避免需要第16条路径/另一方程/网格/容差，应STOP向Astra一次集中报告，不偷增白名单。

## 4. 独立环境和保护

禁止在历史`D:\ProjectTemp\c5k1bturn56`写入、checkout、reset、stash、clean、merge、index变更、worktree附挂或更新其外部Git common-dir。Codex可在独立受控`D:\ProjectTemp\ch5_v010_mainline_impl_<id>`使用**不共享原common-dir**的独立Git clone/sparse checkout，精确签出指定`a1db8c114dec0ab69d69a5576e153a7f868cba0e`；必要网络/认证失败则停止，不借原dirty树绕开。独立clone最多新增2GiB（自身Git对象+稀疏源文件，独立监测）；无权限/超过则停止。正式开发只在上述15个路径；不执行历史/真实数据扫描、`.mat`/2017/2018/C8/B3或旧V009失败数组读取、stat或hash，不读其它项目，不触QMD/Basic Memory。候选可建立新独立分支并最多一次**普通non-force push**仅白名单Python/test文件及脱敏证据；不合并main、不写治理分支/历史冻结或越权Git路径。外部推送失败不以强推救场，保留本地候选和摘要。

## 5. 新V010实施预算（非旧预算解封）

Owner本次批准同路线实施；本固定合同一旦被独立任务准确签发，**仅本V010受界synthetic**预算如下，累积跨修复/续会话计算；不继承、重置或混用过去C8/C9/人工V009上限。

- 总墙钟时间≤8小时，从本实施启动后的第一个写操作/测试操作开始累计；耗尽立即STOP。
- `pytest` focused子进程≤6次（每次≤600秒），其中至少保留1次用最终candidate Git tree的隔离签出测试；失败测试也消耗。
- synthetic science driver独立子进程≤4次（每次可多个明确受界步骤）；任何内部求解调用先扣全局账。
- **每省HA/HJB尝试含KFE资格检查的总调用≤26**：两个同输入HA binding（2），双省有界外层最多5轮×2（10），冻结配置独立HA回读（2），零冲击和1%TFP各3期×2（12）。若条件没达到，后继份额不允许换名挪作新轮次。失败、异常及最终树验证均计入相应总额，不得把一次失败重新命名成新实验。
- 每HA HJB直接value update≤100、同初值/终态policy/Q映射合计≤101；全轮最多`26×101×800=2,100,800`个policy selector cell evaluations。每HA scalar-root调用（**含V0每格正根及selector内部全部root**）≤400,000、全局≤10,400,000；每个selector例程还受其原采纳分支/切换资源门，不能以全局余量取消局部门。HJB direct sparse solve≤100/HA，terminal source-free KFE≤1/HA且仅在HJB严格双门后，不按checkpoint重复KFE。任何溢出fail-closed。
- 新运行生成的原始回执、fixture、日志、候选隔离视图等**增量artifact**≤256MiB，逐文件统计（原接受的源仓历史内容/独立clone对象另受上面2GiB界；不是无上限豁免）；禁止每格每期无限制大型JSON证据。只保留最小脱敏manifest、精确调用账、聚合资格、哈希和必要失败片段。
- 进程RSS采样目标≤512MiB；若资源不可量则标UNKNOWN，不推算伪数据；如明显内存失控或独立clone/artifact硬额超限停止。时间/次数/bytes/预算需保留已用与剩余，不能依赖进程退出0自动认定数值PASS。
- 所有科学执行都必须是此冻结fixture和固定V0派生的两省**synthetic**，旧研究科学预算/受保护数据仍0，`model_activation=False`、Results FALSE不变。

## 6. 必须按序完成的验证与STOP

A. 独立clone和fixture字节、保护、软件/入口及V0算法审计；无真实数据。
B. 先做stub/公式focused tests：高pgdp目的地低φ、两轴与目的地税一次、现金流量、三省非对称same-S守恒与lagged、家庭/firm Lt前后态、used/raw clip、GovInv低高边界及未授权C1不存在；这些**不得偷偷调用HA/HJB/KFE**。
C. 在余量中最多2个同输入HA独立绑定与严格HJB/KFE终端资格，具体每次输入/哈希先封存。局部非退化失败即诚实分类，保留无需新求解的工程验证。
D. 仅HA已合格，至多5轮×2 HA的synthetic有界外层；如果价格、HJB、资金、目标等失败，STOP并披露，不为PASS扩网格、补地板或自动Newton。
E. 仅outer真收敛，冻结Zt/GovInv运行2个HA回读（关闭adapt），验证冻结单位、GDP目标≤1%和共同固定点；失败就停止。
F. 仅冻结验证PASS后短3期×2省的零路径和1%衰减TFP响应；逐期指定外生量从基点重置并正确携带其他状态，不用`1eq`，核对原lagged-NKPC分支。不能将此短响应称正式IRF。
G. 最终提交准确候选tree，按V1.2有预算的最终树focused复测，脱敏回执独立于候选代码提交以免SHA自引用。若候选改变，早期测试不能充当最终证据；旧科学调用也不能重新获得。

任何硬门失败或8小时/次数/根上限达到，立即`STOP_AND_REPORT`；工程范围内普通可修缺陷可在预算余额内集中修复，不逐微步骤求批准。若无合格稳态，允许报告`ENGINEERING_IMPLEMENTED__SCIENCE_FAIL_CLOSED`，绝不能伪称稳态/Results成功。

## 7. 最终集中交付

只交一份`V010_MATLAB_FIRST_MAINLINE_IMPLEMENTATION_RESULT`，列：准确固定冻结计划/fixture blob与代码父SHA/tree、候选SHA/tree和仅白名单diff、计算入口/完整模块来源、真实调用数/失败数、每阶段终态、数学/会计/时序oracle、HJB B/D/Q/KFE原始摘要、GovInv/Zt/财政及年度口径界、时间/进程/存储账、未观测事项、受保护原tree未覆盖的证据等级、独立clone和普通push回读；只保留适量脱敏公开摘要，不外发私有原始证据。

验收必须分账：`SOURCE/ENGINEERING`、`SYNTHETIC_NUMERICAL`、`STEADY_STATE`、`DYNAMIC_RECURSION_DIAGNOSTIC`、`REAL_GE`（仍FALSE）、`RESULTS`（仍FALSE）。候选代码提交或pytest PASS不等于Astra科学ACCEPT，任务结束后`WAIT_ASTRA_V010_IMPLEMENTATION_REVIEW / STOP`，不得自动V011、解锁真实数据或改工作流。

原8 dirty/index/外common-dir/untracked/ignored、A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、real C8 A–D REQUEST_ONLY及旧耗尽科学预算均保持。
