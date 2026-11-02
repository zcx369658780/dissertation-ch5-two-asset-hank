# TEMP31 真实工资兼容与首来源地HA：精确静态方案 · 2026-11-02

STATUS=STATIC_PROPOSAL_COMPLETE__NO_SCIENTIFIC_SOURCE_EDIT_OR_RUN
AUTHORIZATION_PARENT=b91146f8144ae565157c3170f1c66123b64ea241
MODEL_HEAD_AT_AUDIT=a62d9ae6b6d5102e5a6fbecf8648eb6f4c6117ff
MODEL_TREE_AT_AUDIT=0465ba986e91460a78c99b732c833968080f2cdc
ACTIVE_CODE_CANDIDATE=69745f9212c8997efc272ecd7d06cc8cd1318c92__UNCHANGED_LOCAL_ONLY
MACHINE_READABLE_PLAN=CH5_TEMP31_PRODUCTION_COMPATIBILITY_FIRST_HA_PLAN_20261102.json

本方案完成保存合成元数据闭环后的下一工程任务。16份指定代码/配置与固定HEAD的原字节、Git Blob、SHA-256一致，26项AST观察通过；没有导入项目/NumPy/SciPy，没有生成网格、读取原捕获/数组或调用科学函数。原198项工程检查属于前轮，本轮没有重新运行，更不能将26项静态观察称为HA运行测试。

采用light-system-design的现状/方案/资格区分；其通用intake脚本会递归遍历目录，超出Owner的精确路径范围，因此未运行该盘点器，改用限定allowlist审计。未建立或使用其他仓库的代码图谱，没有取得运行依赖/环境闭合认证。本机实际依赖版本、科学运行耗时/峰值内存仍UNKNOWN；pyproject只声明Python>=3.11、NumPy>=2.0、SciPy>=1.14，不能当作锁定环境。

## 已核实的兼容障碍

| 位置 | 本轮静态事实 | 对接含义 |
|---|---|---|
| temp31_ha_taxfree_bootstrap.py:44、134 | 后轮校验调用prepare_proposed_consumers；require_netwage_inputs先要求旧Temp31NetWageInputs，再校验其工资记录 | 新增一个凭据对象不能自动被现有消费者接受 |
| temp31_ha_wage_debug.py:161 | 必须是SyntheticNetWageCalculation，且重新执行合成工资公式 | 保存合成见证或真实现场记录均不能换标签进入该分支 |
| temp31_asset_return_initializer.py:67；temp31_netwage_hjb.py:65；temp31_netwage_policy.py:57；temp31_netwage_economics.py:81、121 | 共用同一require_netwage_inputs；数值消费只使用净工资，无再次tau扣减入口 | 推荐从共同校验门增加明确的新通道，不能改工资公式、复制数值黑箱或强制转换旧类型 |
| Temp31NetWageInputs:106 | 工资必须严格正、单劳动类别；初始化还要求labor_weights=[1] | 零/负/非有限工资拒绝，不加epsilon、裁剪或重新扣税 |
| 两个包的__init__.py | 普通包导入连带加载其他HJB、KFE与年度/外层模块 | 不能用普通年度入口试跑；首次诊断须先准备独立、限定模块的装配入口 |
| mp4c_python_annual_production.py:162–174 | 原800格构造、参数和控制值可静态定位；旧solve_batch仍走旧初始化/含税输入 | 可引用原网格构造与历史控制值，不能执行旧年度runner来替代新净工资路线 |

保存合成旁证已完整，但scope仍SAVED_SYNTHETIC_ONLY；source/input科学采纳、现场生产执行、正工资域和严格HA资格均不能从该元数据推导。旧记录中19.000000000000004也不能舍入后冒充首轮精确19初猜。

## 两个真实生产兼容选项

**推荐A：独立生产输入类型，共用门显式分派。** 新增独立、不可变的生产凭据/输入模块，拟议名称temp31_production_netwage_inputs.py；将来仅在require_netwage_inputs增加对该新类型的显式校验分支。旧Temp31EffectiveWageRecord、numerical_bootstrap19、later_net_wage_record、validate_effective_wage_record及SOURCE_COMMIT保持原义。新类型不继承旧类型以骗过isinstance，不复制字段改producer_record，不把旧scope置TRUE，不重新计算工资证明来源。新类型须公开同样的r_a/r_b/wages/labor_weights消费属性；源内调用可接受这种结构只是静态推断，真实运行兼容仍未验证。

新工厂须绑定独立获准的源码/输入pins、实际进入claim、完整frame/return见证、六角色输入、t生成进入t+1、省序/origin/context、精确净返回值及有限正值域。工资生产函数只在获准生产入口调用；消费者验证不能重算生产者或旧合成公式。当前惰性声明没有签发此类资格的能力，不能通过调用方自报布尔值/内容与hash获得资格。

**备选B：为旧记录增加明确版本化生产分支。** 可以统一消费者类，但须给生产分支独立来源身份，不能冒用旧SOURCE_COMMIT；旧构造、序列化和所有调用者的回归面更大。如果需要弱化旧校验、改旧序列化语义或覆盖历史pins，应拒绝这一选项。A/B均是建议，Owner尚未选择；本轮没有新增生产类型或修改共同门。

两种方案都不删除旧接口或历史分支，没有弃用日期/清理计划。未来若实施，旧工资/源清单继续作为原阶段证据，新源码变更须另登记前瞻pins，不能“更新”旧清单使旧见证看起来来自新代码。默认保持新生产路线不可达；如后续已启用而失败，通过经审查的前向提交关闭新路由，保留候选/回执，不reset、重写或删除证据。

建议兼容检查包括：原首轮/旧合成分支保持；保存合成拒绝冒充生产；错省序/origin/context/期次/源或输入身份/进入claim/返回字节拒绝；执行未知拒绝；零/负/非有限工资拒绝；调用方ready标志无效；重复消费不触发工资函数；旧元数据和预算不能被新版本修改。本轮仅列计划，未实施或运行这些新检查。

## 首个来源地HA诊断：独立于真实生产凭据

首次诊断可走现有numerical_bootstrap19路径，不必为运行这一个首轮诊断先开放真实后轮生产桥。建议使用下表固定合成方案；**这是待Owner批准的新HA提案，不是本轮运行许可，也不是正式省份或年份输入采纳。**

| 项目 | 建议固定内容与来源 |
|---|---|
| 上下文 | TEMP31_FIRST_ORIGIN_HA_DIAGNOSTIC_PROPOSAL_20261102；合成省序(A,B)，仅A/index0，进入期1、生成期None；calendar_year=None |
| 家户价格/转移 | rah=.09、rb=.02、rb_gap=.07、Tt=.1；沿已认证R1 P0价格角色及既有合成初始化参数，不外推连续可行盒 |
| 工资 | 用现有首轮20×(1-.05)=19数值初猜，税向量(.05,.05)、sigma零2×2、labor_weights=[1]；新工资生产调用0 |
| 偏好/成本参数 | rho=.05、gamma_c=2、phi=5、chi_0=.1、chi_1=2、a_bar=1e-6、mu_z=0、sigma_z=0；是已知源码/fixture提案，不是本轮新参数采纳 |
| 原HA网格 | b=linspace(-2,5,20)、a=linspace(0,10,20)、z=(.8,1.3)、switch=[[-1/3,1/3],[1/3,-1/3]]；(b,a,z)=(20,20,2) |
| 原网格对象 | 获准时只构造一次固定export的MatlabFaithfulHJBGrid，同对象交初始化/HJB/KFE汇总；不为另一个类名重建、不改节点/dtype/flags。原对象公开结构能否被新HJB消费仍待运行验证 |
| 新初始化 | temp31_asset_return_initial_arrays，显式V010_TOTAL_WEALTH_NUMERICAL_INITIAL_GUESS；800格最多800根，原brent上下域、xtol/rtol=1e-12、maxiter100不变 |
| HJB控制提案 | delta=1000、convergence_tolerance=1e-7、max_iterations=100、drift_tolerance=1e-12，来自年度源码164行；新HA用途仍待批准，不能当严格驻定接受阈值 |

800格的节点数量、b/a边界、z和切换率全部承接原HA网格，绝不为了收敛缩成8格。原8格成功不认证800格，剩余7个初始化worker不能用于800根或HA。新初始化只改变初猜资本收益为a*r_a(a)，不修改现有HJB两账户mu_b/mu_a、提款/积累/调整成本或边界语义；其政策可行性不由初猜通过证明。

拟议装配只包含11个固定模块、16条本地静态导入边，详见JSON。它在私有单次进程中建立限定包容器，逐件完整加载固定源码，不执行公共包__init__，不执行旧mp4b bootstrap，不提取重写科学函数，不替换科学类型/校验器以救通过。容器只是拟议加载方式，不冒充完整正式包导入认证；第三方与原生依赖仍未验证。

## 新预算提案与先决工程

建议另列一个新的、最多1进程×120秒（含导入）、进程内存上限2GiB的首次诊断许可；这些是Codex给Owner审阅的上限建议，不是测得耗时/内存，也不是委托下已签发HA许可。当前worker=0，许可尚未存在。父进程/Windows本地作业控制须在科学入口前可验证地施加限额；无可靠限额/源或输入pins/claim记录时不得进入科学函数。

最多1个来源地诊断尝试，初始化数组1次，Brent Python/native各最多800次，HJB进入1次/线性求解最多100次，内部local policy最多80000格次；仅HJB收敛且原网格保持后才允许KFE1次/其线性求解1次，随后汇总最多1次。这个未来许可必须明确包含HJB内部policy/operator/economics依赖，不能把“HA一次”理解为可调用任意科学函数。新工资生产、其他来源地、企业/GE/IRF、校准、真实数据与MATLAB均0，重试0、自动后继0。

进入初始化前持久独占claim锁定这一次来源地尝试；源码/输入/网格身份、时限/内存、计数和STOP先登记。初始化域/根/斜率失败，HJB异常/非有限/未收敛，算子谱系或网格身份变化，KFE失败/非有限/归一化零，保护故障、超时、失联或返回见证不全均停止；未知执行不当作未执行，不自动再试。原始数组、CSR、输入和完整日志仍LOCAL_ONLY。

先可继续的普通工程是E1：标准库预执行计划/pins/计数校验及元数据夹具；E2：用非科学toy夹具验证隔离启动、限额/计数/失败保留机制。E1/E2均不得导入真实科学模块、调用求解器或改生产消费者。它们的可运行结果和最终输入/代码pins就绪后，才向Owner提交S2的具体运行许可；本轮不要求Owner批准尚未实现的运行器。

## 诊断与接受保持分开

保留HJB的原converged/iterations/max|V_new−V_old|，该统计量不是方程残差。KFE只接同一次HJB返回的post_convergence_operator.full，记录传入与CSR表示转换、原算子/transpose/污染矩阵/raw向量/归一化因子/density的各自身份。保留原raw_residual_inf=||C@raw−rhs||∞；拟议另记完整原方程||A_post.T@g_F||∞，包括被污染行，不剪负值、不重建算子或再次归一化补救。

密度拟议记录有限性、最小值、sum(g)*db*da质量及sum(max(-g,0))*db*da负质量；离散z求和，不加dz。汇总只输出家户c_ss、已含z权重的l_ss、a_ss、b_ss等诊断，不乘人口、不提交资本/企业/外层。所有诊断本轮NOT_MEASURED；科学判据reference/thresholds仍null，不能因为HJB收敛或某残差小就标严格HA通过。首次诊断即使将来成功完成，formal_ha_accepted也保持FALSE，直到有独立对应的科学判据与Owner接受。

| 操作门 | 当前状态 |
|---|---|
| E1/E2普通工程准备 | 可在既有授权内推进；当前只是方案 |
| S1真实生产输入兼容 | A/B待选择，实际消费者改动未授权/未实施 |
| S2首来源地800格HA | 运行器/pins/限额夹具尚未就绪，新具体HA许可未授权 |
| S3严格科学判据 | 未绑定；本轮未添加数值阈值 |
| S4正式输入与新现场生产 | 源/输入采纳和相应调用预算另行决定；不复活旧工资观测 |

16份文件完整身份和26条观察见机读JSON；这里只通过了静态工程自审，不是独立科学评议或运行验收。所有生产/科学接受/FORMAL_SOURCE_FREEZE/Results/model_activation/REAL_GE门保持FALSE；初始化3/10余7、工资1/1关闭、补录1/1关闭、旧dirty树/HEAD/index、R12/R13/WASM保护门、OWNER_BASELINE_REBIND未授权及16义务保持。没有分支删除、main合并、原件清理或全局配置修改。
