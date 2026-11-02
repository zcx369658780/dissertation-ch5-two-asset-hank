# TEMP31 锁闭科学worker与父子资源接合 · 2026-11-02

STATUS=ENGINEERING_COMPLETE__SCIENTIFIC_BRANCH_IMPLEMENTED_BUT_OWNER_AUTHORITY_PENDING__NO_HA_RUN
AUTHORIZATION_PARENT=eb85c03079c9378ddcae60a9ec0d6e8acb676ee5
OWNER_CONTINUATION=好的请继续
CODE_CANDIDATE=41eb30005c223eced9b25d744f5253c288256864
CODE_PARENT=aea0b62c1eccf2575f78ff3977c5374711c7f80e
CODE_TREE=de19a6390431afacbb6fa7fcc183c1b4f854753b
CODE_PUBLICATION=LOCAL_ONLY_NOT_PUSHED
AUTHORITY_RECORD=CH5_TEMP31_SINGLE_ORIGIN_HA_AUTHORITY_CURRENT.json__PENDING_OWNER_AUTHORIZATION

## 本轮实际完成

独立固定worker、父进程监督器与两份测试已实施，16项不同行为检查已验证通过。真实子进程只运行非科学模式，复用同一阶段编排；科学模式在固定位置Owner记录处拒绝。没有导入/执行NumPy、SciPy或原科学模块，没有生成生产网格、执行初始化/root/HJB/KFE/HA/GE/IRF或新科研计算。本轮只读了分发元数据、指定运行文件及必要库源码的静态接口信息。

父进程用挂起/隐藏窗口方式创建固定Python worker，配置并回读Windows Job的1个活跃进程、提交内存上限和关闭即终止行为，再绑定进程、写PRE_RESUME_JOB并恢复。子进程独立打开同一命名Job，实际查询成员关系与限额，写CHILD_JOB_LIMITS后关闭查询句柄，才进入主体；父进程在接受正常返回时再核该记录的pid、manifest与限额。没有无约束后备启动，不接受任意命令、模块或callback。

已实际验证120秒、2GiB配置下的非科学正常管线；这是上限配置核验，不是消耗120秒/2GiB或测试HA性能。96MiB测试下256MiB分配被拒，0.7秒测试被终止；崩溃无返回、重复意图不可重用，不收敛/网格错误在KFE及汇总之前停止。累计工程过程共21个中性worker进程，全部原意图/版本/结果保留；前轮E2的11意图/9进程和所有科学预算不变。科学worker=0。

## 真实科学路径：已写成，尚未执行

新worker只有固定的科学编排：原11文件大小/Blob/SHA核验并完整加载到独立包容器；导入期只允许模块/类定义代码，禁止源函数主体；随后实际对象/代码绑定观察器，顺序执行prepare→initializer→HJB→KFE→aggregate→diagnostics。新worker不通过旧年度bootstrap或公共包__init__装配，不改历史SOURCE_COMMIT或净工资消费者。

原20×20×2网格对象只创建一次并前后核身份，沿用原节点、边界、z与切换率。首轮用原bootstrap19及新a*r_a(a)初始化，HJB不收敛立即停止，不进入KFE；KFE只接同次HJB的post_convergence_operator.full，保留源内CSR转换与原始污染系统残差，核原算子数据表示未改。新增原方程驻定、质量/负质量及家户汇总仅拟作原始诊断，不新增接受阈值、不裁剪密度、不重建算子。

Python/闭包代码/global身份和实际Brent C对象/调用者、线性求解与policy限额已接入准备代码。静态核实本机brentq与spsolve无装饰器，Brent仍调用_zeros._brentq；真实SciPy调用观察、导入兼容与数值结果仍未运行验证。观察器按当前线程工作，worker拒绝额外Python线程；原生库内部线程不当作额外模型函数见证。科学允许分支的首次执行仍可能遇到依赖、域、驻定或超时失败，失败必须保留并停住，不能改参数/网格/容差救通过。

输入/原网格、初始化返回、HJB返回（包括不收敛返回）、KFE返回及诊断的LOCAL_ONLY保存点已写入，均独占创建并同步落盘，不能覆盖旧证据。中途突然死亡时最后检查点后的详细计数/返回为UNKNOWN，不推定0、不重试。科学数据分支本轮未产生任何数组或结果文件。

## 环境身份与科学授权边界

实际登记Python3.11.9、NumPy2.4.6、SciPy1.17.1。NumPy/SciPy各METADATA/WHEEL/RECORD以及10份指定运行文件（含初始化源码、Brent/线性求解包装与扩展及随附DLL）按RECORD核大小/SHA；不导入这些包，不遍历整个安装目录。记录线程环境，不更改配置。环境摘要：4dd77c75ee2b6743aff07e6875171fcdec3e8f7e32d1c326e81159d0b11256e8。完整动态依赖/实际加载与科学运行资格仍UNKNOWN。

科学启动只读取固定仓库位置的CH5_TEMP31_SINGLE_ORIGIN_HA_AUTHORITY_CURRENT.json。当前status=PENDING_OWNER_AUTHORIZATION、owner_approved=FALSE、decision_record=null。不能从调用方布尔值、环境变量、同批自报SHA或“继续”消息取得科学许可。未来必须有新的、不可变Owner决定记录及固定SHA，明确NEW_FINITE_HA_DIAGNOSTIC/指定动作，并匹配当前提案的代码、环境、来源/fixture摘要、严格整数限额和关闭的接受旗标；科学进程/意图根也是固定位置。此为可信仓库治理门，不是抵抗任意同工作区恶意篡改的密码学隔离。

前轮E3的永久关闭入口保持不变；本轮新增的是另一个受Owner固定记录控制的worker。任何实际科学导入/运行都未发生，旧初始化余7次不可用来支付本次800根/HA。

## 代码与检查

交付前自审再加强子进程的独立Owner预算绑定：不只信父清单，还核真实决定的mode/intent/case、代码/环境及严格整数限额。新增失败用例先复现，再修复并验证；新版worker正向子进程回归通过。最终候选41eb300...，初版工程提交aea0b62...保留，15项原套+1项新行为共16项无遗留失败。

API缺失先由失败检查复现。工程过程中输出阶段名重复被防覆盖门阻止，另存新阶段；一项测试误用另一个文件加载实例的异常类，修正为基础类型并核明确拒绝原因。全部原记录保留，无科学重试。16项不同检查通过（15项整套检查及新增子进程预算绑定检查通过；新版中性worker正向回归通过），主/子进程已载入科学模块均空；新增子进程限额回读后对正常返回的复核也实际通过。没有重复全项目科学测试。

| 路径 | 字节 | Git Blob | SHA-256 |
|---|---:|---|---|
| src/ch5_two_asset_hank/multi_province/temp31_worker_supervisor.py | 14790 | 9f7e270c92f475fe09ec6483fced76ac2c0d9b92 | e5e33f7c736ddbeaef40455df65c11f6d4d42ecfd128fc209999511cbc3ce455 |
| validators/multi_province/temp31_first_origin_worker.py | 24300 | 8aeb6580ddb72f2516f2132319014647fbc8f009 | 10889cb0e1f225378185f2c658e39392b89b0376aa16c0b2193ee8a3998fd784 |
| tests/test_temp31_worker_supervisor.py | 5014 | e2ed303725b993196db724ad65e6290981ef744e | a7e2e7ca3500aa74adc1647a91913fe9bcd95856f8e034c3b342bee6e8c13d57 |
| tests/test_temp31_locked_worker.py | 5197 | 4444ef8b9bd7094e72611435564f280712befc1e | b2884c3d839df1cea69221b4fb2042463d67714362891266f9dc1191d6d3005b |

仅新增监督器、独立worker和两份测试，原589条选定代码路径/最初565基线保持，现593路径；原科学核心、参数、输入、网格、公式、容差未改。以上为Local Codex工程自审，不是独立科学评议或数值验收。

## 可供Owner决定的S2单次申请：未授权

精确机器提案在上述AUTHORITY_CURRENT的proposal中，代码/环境/来源/fixture摘要已固定。建议一次A来源地（合成省序A/B、index0、进入期1、无实证年份）的诊断：原20×20×2网格，rah=.09、rb=.02、净工资19、rb_gap=.07、Tt=.1；原rho/gamma/phi/chi等参数与数值控制见提案，与已有静态计划一致，不外推价格可行盒。

| 限额/行为 | 本次请求 |
|---|---|
| 进程/资源 | 新1进程，含导入墙钟120秒，提交内存上限2GiB，单活跃进程 |
| 初始化 | 数组初始化最多1次；Python/native Brent各最多800次，原根域/xtol/rtol/maxiter100 |
| HJB | 进入最多1次、原max_iterations100，线性求解最多100、内部policy最多80000格次 |
| KFE/汇总 | 仅HJB收敛且网格不变后KFE最多1次/线性求解1次、汇总最多1次 |
| 禁止项 | 工资生产者/其他来源地/企业GE/IRF/校准/真实数据/MATLAB全部0，重试0、自动后继0 |
| 失败 | 来源/环境/保护/域/求根/不收敛/算子/密度/资源/观察或返回未知均停，保留原件；本次单一意图作废，不更名续跑 |
| 资格 | 原始合成诊断而已；科学判据仍null，formal_ha_accepted/科学接受/Results均FALSE |

授权后方可把Owner原话与本提案身份写成不可变决定、绑定固定记录并执行该唯一尝试；**本轮未填写批准记录，也未创建S2科学执行根。** 即使实际返回成功也不自动开放31省、生产工资兼容或正式驻定接受。

该新科学运行门来自CH5_TEMP31_DELEGATED_DEBUG_AUTHORITY_CURRENT.md“本委托不开放HA/HJB/KFE/GE/IRF/policy、校准、真实数据或MATLAB运行”；普通工程委托不代替它。原工资/补录各1/1关闭、初始化3/10余7、dirty树/HEAD/index、R12/R13/WASM、未授权保护重绑定及16义务保持；FORMAL_SOURCE_FREEZE/Results/model_activation/REAL_GE均FALSE，无分支删除/main合并/原件清理/全局配置修改。
