# V0.0.9 冻结计划的唯一增补：Owner采纳 CES 跨省劳动厌恶权重方案B

2026-10-15（Asia/Shanghai）
**补充状态：`V009_CES_PHI_B_OWNER_ADOPTED__SUPPLEMENT_FROZEN__WAIT_SEPARATE_REMAINING_BUDGET_AUTHORIZATION__FULL_HANK_STATIONARY_NOT_RUN`。**
**不可逆历史原则**：原V009冻结计划 `versions/0.0.9/plan.md` 的blob `cb76a840fdd9d1756728189bf29518679831aba6` 和既有科学执行许可 `versions/0.0.9/authorization.md` blob `770a1fc304c3a602595e9d3d9d5ec21c2bdf1ee5` 不修改。本增补**仅填补原计划§2 CES φ[j,i]已有理论方程却在§3未赋数值的缺失参数**，没有打开原计划其它被冻结的经济机制、人工校准、网格或已关闭预算；后续执行须单独签发精确续跑许可。

## 1. Owner实际新科学决定及资料来源

Owner明确拒绝纯粹将所有φ设1的中性方案A，**批准方案B**：保留原博士论文“目的省相对富裕则来源家户跨省工作的劳动负效用权重较低”的偏好机制，确认偏离参数`max_phi=0.3`，并指明富裕目的省的人均GDP为来源省两倍时`φ=0.9`、反向`φ=1.1`；要求沿此科学方向继续。博士论文PDF物理p99（印刷p79）表5-1及下方`φ_{dest,source}=1+0.3*(pgdp_source-pgdp_dest)/(pgdp_source+pgdp_dest)`为解释权威，p100讲明富裕目的地权重小于1；用户上传原MATLAB `multi_prov_HANK_12sts.m`定义`max_phi=0.3`，`HANK_mp_1turn.m:10`用相反的`destination-source`差且用`Yt/Lt`代理，不是本新模型的理论正确性权威。这**不是**迁移费`sigma`、CES配置弹性`eta`、家户劳动厌恶曲率`nu`或综合劳动厌恶`kappa`。已冻结`eta=1, nu=5, sigma=0`及其它人工参数/经济制度原样。

## 2. 精确一次性补充冻结的人工φ输入

双边矩阵永远是`phi[j][i]`，**目的地j为行、来源地i为列**。固定`max_phi=0.3`及严格正的人工人均GDP参照`pgdp_ref`；经济权重：
`phi[j][i] = 1 + 0.3*(pgdp_ref[i]-pgdp_ref[j])/(pgdp_ref[i]+pgdp_ref[j])`。

- **1省**：`pgdp_ref=(1.0,)`，`phi=((1.0,),)`。
- **2省**：为延续Owner明确举例的人工相对发展差异，固定仅作**无量纲人均GDP参照比值**`pgdp_ref=(1.0,2.0)`；`phi=((1.0,1.1),(0.9,1.0))`。
- 必须逐元素检查：`phi[1][0]=0.9`（省1居民去经济水平是本地两倍的省2），`phi[0][1]=1.1`（省2居民去只有自己一半人均GDP的省1），`phi[0][0]=phi[1][1]=1`，全部有限正数；不得交换来源/目的轴、改符号、直接照抄旧MATLAB赋值、把跨省φ设置成反号、按`S`或工资/人口行列加权重新归一化。
- **工资—劳动对偶保持原冻结式**：`v[j][i]=(1-tau)*w_j`（费用sigma=0），`W_i=(sum_j phi[j][i]^(-1/eta)*v[j][i]^(1+1/eta))^(eta/(1+eta))`，`h_ji/ell_i=phi[j][i]^(-1/eta)*(v[j][i]/W_i)^(1/eta)`。重复征工资税、用CES指数等于目的劳动简单求和，均不得通过。
- 本人工参照`pgdp_ref`是**预注册外生值，不是2018现实GDP、不在macro root内使用内生Y/N重算，也不构成额外宏观未知量或新的反身性政策方程**；工资、CES家庭劳动配置及双边劳动供给仍由HJB/宏观价格**内生求解**。将来真正动态政策下的GDP反馈φ、真实历史省份GDP基期/年份及标定要另行科学采纳。

## 3. 原候选身份、资格及严格剩余预算

Codex已提交但未获完整HANK稳态接受的`V009 PRE-PHI`候选 `18256cd70b827e133e52d7609746c8afadb63ac1`、tree `6e06b66888a25640f40f265c3f4b5cb75e4cd575`，唯一parent `d41d229b681e09b913c21deff7a057085b9bc419`，GitHub实际diff仅原冻结13白名单新增路径。其`contracts.py`明示`phi=None`；在缺少φ预注册的正确拒绝门停止，**无完整HJB/KFE或宏观稳态**。Codex报告final tree `13 passed`、聚焦pytest累计`4/8`（含一次红灯）、完整科学driver 0/4、宏观solver 0/4、家庭HJB/KFE 0/176；toy数学审查已实际调用selector最多8、SCC最多6、GESVD最多3、toy Q转置校验最多3。以上Python运行/Windows receipt/原8 dirty/index保护为`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，网页GitHub静态源码/diff可独立核查。Codex时间约12.4分钟、逻辑新增存储约14.6MiB及RSS采样71.8MiB不得因候选更换清零。

**绝不重置额度**：本版累计pytest最多8，剩余最多4；完整science drivers最多4且此前0；macro roots最多4且此前0（1省2次、2省2次），家庭HJB/KFE总≤176且此前0；其余selector/scalar-root/KFE/工作集/磁盘/时间依原冻结与授权，并记录先前toy实际attempts（如分类重叠，宁可保守扣减，不双计为零）。若实际Codex不可验证剩余资源，先STOP而不是猜测可用额度。旧V008科学预算仍耗尽且不可借用。

**候选变更精确边界**：仅在原13白名单文件内修补`phi=None`的冻结输入、源方向预注册检查、相应测试/报告。已发表的PRE-PHI候选永久保留，不改其SHA、不force-push；在隔离候选目录形成新单父候选（**唯一parent仍必须是`d41d229b681e09b913c21deff7a057085b9bc419`**，可在新树承接已审的13个文件再封存，而不是基于PRE-PHI候选叠加第二个parent或合并main），一次普通non-force发布并readback；如安全隔离构造不可行就STOP并报告，不强改Git历史。

**不得先启动数值**：本增补文档不是续跑授权。Astra单独回读固定Git commit与blob、再签一条同V009严格**剩余额度续跑**文书之后，Codex才可按此前未消耗的完整科学限额继续。没有新数学问题时不重开Owner讨论；真HANK HJB/KFE不能收敛时按原硬门如实报告，禁止为通过再修改φ、参考pgdp、其它人工校准或B/D/KFE门槛。

原C8 source/real A–D只REQUEST_ONLY；A16 FAIL_CLOSED，window UNACCEPTED，C9 PAUSED，CALL_LEDGER_UNRESOLVED，model_activation=False，Results FALSE；24×24/31省/动态IRF与旧科学budget依旧0。V0.0.10 NOT_STARTED，V1.2及Owner连续顺序长版规则不变。
