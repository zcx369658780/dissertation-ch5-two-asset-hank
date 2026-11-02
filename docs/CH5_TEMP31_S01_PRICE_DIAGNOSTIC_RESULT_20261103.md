# TEMP31 S01价格诊断：HJB25轮收敛，KFE原驻定未获认证 · 2026-11-03

STATUS=RAW_HA_CHAIN_RETURNED__HJB_CONVERGED25__STRICT_STATIONARITY_NOT_CERTIFIED__CLOSED_COMPLETED_NO_RETRY
OWNER_EXACT_STATEMENT=可以请继续
OWNER_DECISION=CH5_TEMP31_S2_OWNER_DECISION_20261103_04.json
OWNER_DECISION_SHA256=45597c53e677a3dc7e80d151edcf452fc59ef0cf17316eac6da24f1590d49de8
EXTERNAL_PRICE_INPUT=CH5_TEMP31_S01_PRICE_INPUT_20261102.json
EXTERNAL_PRICE_INPUT_SHA256=a5178cbf9d74df7f9eebd0e2cd51f7e1dfcd0baf6e52db1c0a92c3676f584776
S01_FIXTURE_SHA256=3722cd0883d495bc774d9bd780efd806d1c4d9648fb585a3bf37dda1a17f9862
FINAL_PROPOSAL=CH5_TEMP31_S01_EXECUTION_PROPOSAL_20261103.json
CODE_CANDIDATE=ee15d70469bca831ed1c613c52a737c88c73b411
CODE_TREE=a4754741c9e6a7dd9a7d971552840915cae5324c
MODEL_CODE_PUBLICATION=LOCAL_ONLY_NOT_PUSHED

## 本次具体结果

Owner对前述具体S01设计明确继续后，先实现限定外部输入绑定并检查，再登记新的不可变决定_04和累计账本，才启动唯一进程。实际26.234秒、峰值提交内存1,378,537,472字节，exit0、RETURN_VERIFIED，原计算链完成至diagnostics，父子Job限额/身份与退出清理确认。120秒/2GiB均未触限，重试0，无S02/S03或其他后继。

| 项目 | 本次实测 |
|---|---:|
| 家户输入rah/rb/净工资 | .05 / .02 / 19 |
| HJB原converged/iterations | true / 25 |
| 原max(abs(V新−V旧)) | 3.85018072979193e-10 |
| 原停止容差/最大轮数 | 1e-7 / 100，均未改变 |
| 初始化/劳动根/Python Brent/native Brent | 1 / 800 / 800 / 800 |
| HJB线性求解/policy格次 | 25 / 20000 |
| KFE/其线性求解/家户汇总 | 1 / 1 / 1 |

源HJB提前满足原条件即返回，没有强迫跑满50或100轮；保留25个完整值函数变化量和实际返回。该变化量不是HJB方程残差，不能由此声称非线性Bellman全局最优或严格HA通过。

## KFE：线性系统返回与原方程驻定分开

| 原始诊断 | 实测值 |
|---|---:|
| 替换归一化行后的raw线性系统残差 | 4.901949072350087e-17 |
| 完整原后置算子驻定残差（无穷范数） | **3.618851426605556** |
| 归一化质量sum(g)*db*da | 0.9999999999999999 |
| 密度有限 | true |
| 最小密度 | -2.014675496598056e-17 |
| 负质量 | 4.044727854761559e-17 |
| 原归一化因子 | 0.03779573587712039 |

KFE使用同次HJB实际返回的post_convergence_operator.full，原算子和源内CSR表示的哈希谱系检查通过，未裁剪密度、重建算子或再次归一化救通过。原污染/替换行系统小残差与质量接近1，不等于原KFE方程驻定。完整原算子残差3.61885保留，当前严格科学合同引用/阈值仍null；本次不自动沿用历史1e-7接受门，严格资格保持CRITERIA_UNBOUND/NOT_CERTIFIED，formal_ha_accepted=FALSE。

本次家户a_ss=7.635973632723667、b_ss=4.865261514661568、l_ss=0.6538909260277331、c_ss=11.443861023499785，total_assets=12.501235147385234，均仅为未获原驻定认证的条件数值输出。劳动保持源内z权重，未乘人口，不提交31省资本/劳动/企业或外层GE；这些数值不是正式稳态供给或论文Results。

## 与当前控制点及历史参考的关系

| 观察 | rah/rb/净工资 | 初始化算法 | HJB返回 |
|---|---|---|---|
| 当前保存控制（尝试3，未重跑） | .09/.02/19 | Owner采纳a*r_a | 100轮false，变化0.47047754769224237 |
| 本次S01 | .05/.02/19 | 同一a*r_a算法，按新价格重算初始数组 | **25轮true，变化3.85018072979193e-10** |
| 历史R1/P2，仅选点参考 | .05/.02/19 | 历史平方项初始化 | 22轮true；严格KFE未认证 |

相对当前控制，只替换外部rah=.09→.05，并保持相同科学源码、初始化算法、网格、非价格参数、净19及数值控制。本次实际INPUT记录同时确认state.rah与消费者r_a均为.05，rb=.02；原网格前后身份保持。工程包装版本不同，但两份运行的原11科学模块及数值公式字节相同。结果支持在当前固定黑箱/初始化算法下，这一个外部价格替换能够恢复原HJB收敛；不证明连续合理价格区间、市场出清或所有不收敛都由价格引起。

25轮不是对历史22轮的逐点复现，历史初始化/运行条件差异继续保留。当前a*r_a初始数组会随rah变化，这是相同算法对新价格的正常响应，不冒称固定了旧V0数组。本地对照图保留旧100点和新25点，S01曲线在收敛处结束，没有补齐或平滑；图/CSV/原始数组与CSR及完整日志均LOCAL_ONLY。

## 工程、预算与当前边界

仅修改监督器/worker两个工程源路径并新增一个测试。新增8项夹具先复现真实绑定遗漏与缺失功能，再实现通过；相关41项限定回归通过，错误/失败/skip0；工程阶段只新增1中性进程，科学导入/worker0。原594路径中592及原565基线保持，现595；原11科学源、公式、policy/边界、算子/KFE、网格、容差、max100和其余经济输入不改。

新固定价格清单与原固定计划分离，原计划/fixture/hash保留；父进程在建科研意图前核S01清单/决定/fixture，子进程在科学导入前独立核同一绑定。只允许S01 rah替换，S02/S03、其他工资/参数/网格或即使重报哈希的额外变化均拒绝。当前输入来源/代码/环境/保护基线在运行前匹配，历史dirty树HEAD/index/porcelain -z摘要及432状态运行前后保持；旧原件/证据未改。

本次新1/1已用、S2四份Owner决定累计4/4已用、重试0；CURRENT=CLOSED_COMPLETED_NO_RETRY，owner_approved=true只记历史，固定启动门拒绝。原3份决定/关闭账本保持，旧初始化3/10余7、工资/补录各1/1关闭不动；预备S02/S03额度0，不因S01成功自动启用。唯一进程按既定原KFE/汇总上限完成，未追加检查性求解或再跑控制点。

当前已有可审阅HJB成功候选及原始KFE/汇总见证，下一讨论需要保留KFE原方程残差与严格判据缺口；不把本次计算完成当科学接受，不自动开启31省或修改黑箱内部。FORMAL_SOURCE_FREEZE/consumer_ready/formal_ha_accepted/科学接受/Results/model_activation/REAL_GE均FALSE。R12 STOP、R13未授权、WASM六路径STOP、OWNER_BASELINE_REBIND未授权及16义务保持；无main合并、分支/原件清理、真实数据/MATLAB运行或全局配置变更。工程审查是主代理自审，不冒称独立科学评议。
