# B3外部编排与静态源码准备：运行准入仍关闭

DATE=2026-11-06
OWNER_CONTINUATION=可以请继续
STATUS=EXTERNAL_PHASE_SEQUENCE_AND_STATIC_SOURCE_PREPARATION_ENGINEERING_COMPLETE
LIVE_HA_ADMISSION=NOT_IMPLEMENTED_NOT_AUTHORIZED
MODEL_ENGINEERING_CANDIDATE=611435c76f5355cac87461490df6dc312763283b
MODEL_ENGINEERING_TREE=7477a0a1910d32fb7bacaa9c0e4480895e44889e
MODEL_PARENT=fffc2ef4d76cd5e1d53fcfb6e433e5cc33e73254
GOVERNANCE_PARENT=efe62675b4c2d56e9ea4648d407fb80ee1f9b2a2
FINAL_CHECKS=15_PASS__14_STDLIB_OPAQUE_PLUS1_NATIVE_PREPARATION
REAL_HA_BACKEND_INSTANTIATIONS_OR_CALLS=0
NEW_SCIENTIFIC_GRANTS=0
SUBAGENTS=0

## 本轮完成的范围

新增薄的HA外部编排层、工程检查和24文件静态源码清单，共3路径；原有任何源码、HA算法/网格/数值控制及既有消费门均未修改。公开execute_origin入口在真实后端构造、源模块加载或数值调用之前，经原待许可门拒绝；即便该门以后有变动，当前版本仍没有后端装载/有限准入安装入口。

这完成的是B3的**外部编排与静态源码准备片**，不是B3完整运行就绪。没有新科学输入/预算、Owner运行决定或claim，未启动HA、七入口探针、旧worker、旧年度runner、Windows Job测试或任何后继科学进程；科学接受和消费者资格保持FALSE。HA继续作为整体黑箱，不新增其内部诊断或误差门。

## 外部调用与数据交接

| 外部阶段 | 本轮编排约束 | 真实后端对应既有入口（休眠代码，未调用） |
| --- | --- | --- |
| 初始化 | 原O2 request.inputs引用保持；不重建工资或重标首轮19 | temp31_asset_return_initial_arrays，保持原V010总财富数值初猜与a*r_a来源 |
| HJB | 同一个inputs，原初始化返回、原Tt/rb_gap和既有numerics传入 | solve_temp31_netwage_hjb；只读取其原converged标记 |
| 正式KFE | 原converged必须为Python True；失败/非收敛在KFE前退出 | 直接传hjb.post_convergence_operator.full给原solve_matlab_faithful_stationary_kfe，绝不换成临时迭代operator |
| 原汇总 | 使用同次原HJB消费/劳动和KFE密度 | aggregate_stationary_household，不新增HA返回字段 |
| AtTax | 沿既有外部原式与同次原g/cell_weight、a_grid、源ra重构 | 原导出matlab_faithful_illiquid_return及旧外层求和表达式；不额外乘H/E或改符号 |
| 回复 | 原request及初始化/HJB相同inputs引用、实际网格身份和原五项家户量 | 原OriginHouseholdReply，仍为O2未乘人口单位，非科学接受 |

外部私有顺序器每阶段只尝试一次、成功才登记返回，异常保留原因/已尝试与已返回计数，立刻退出；没有补结果、自动重试或后继阶段。每阶段前后保护输入对象；休眠真实后端另检查输入数据/工资记录、网格对象/内容及正式post输入和原KFE返回的系数血缘。这些是外部引用/数据保护，不是新HJB/KFE残差或接受阈值。

本轮的6个阶段计数只是编排协议检查，**不是完整科学入口/native调用预算**。未来真实运行还必须单列初始化根、HJB/policy/线性求解、KFE及AtTax有效回报原函数等调用；不能把“每阶段1”当作已经实施800根/100轮等原控制或OS资源保护。本轮没有采用新的这些数值预算。

## 静态来源与请求准备

source_manifest.json从固定角色入口沿Python AST相对import只读展开：24份当前物理源码、34条相对import边，未解析相对import0；所有物理字节/长度/SHA在本次工程检查通过。包括本轮新外部编排、既有O2/B2接口及原HA依赖，另单列旧年度脚本作为网格/AtTax表达式参考，**不把该脚本导入或启动为生产runner**。清单不含绝对私有路径或原科学载荷。

该清单明确标STATIC_RELATIVE_IMPORT_CLOSURE_NOT_RUNTIME_ADMISSION、runtime_environment_verified=FALSE、runtime_admitted=FALSE；只证明本次静态选定范围，不认证动态import、native/DLL、公共包初始化或运行期环境完整性。不得与旧9角色来源、七入口14模块历史集合混同；旧清单/claim未重封，旧额度不复用。

prepare_origin_execution把现有PendingWageConsumerBinding、同一原O2 request和独立静态清单绑定。检查来源省/期次/快照、原rah/rb/Tt/rb_gap、工资/权重原值及只读声明、record/BindingContext引用、声明消费者文件范围和原角色路径；只是准备对象，不生成可执行凭证。直接构造、ready/admitted布尔值、对象/数据替换、源码角色或清单范围漂移都不能通过公开入口。

B1/B2的grid_metadata_identity是合成元数据，不能冒充实际网格SHA。休眠后端要求实际原网格数组内容与目标grid_sha256一致，当前未生成新网格，也未把合成标签改造成实际证明。未来必须绑定冻结原网格的真实字节、原参数/controls及新具体输入；本轮没有替Owner选择新价格、校准或网格。

## 检查结果及限制

最终15项通过：14项标准库/无数值替身检查，加1项原生O2请求准备检查。无数值替身只返回不透明对象/标签，验证顺序、同一输入、正式post选择、每阶段失败一次、非收敛在KFE前停、输入替换/身份变化退出，不构造经济数组、伪造g或声称模型已运行。真实_OriginalHABackend从未实例化或调用。

静态检查确认休眠后端只指向既有原入口；AtTax表达式与旧外层AST精确相同，仅将旧result.kfe对象路径归一为同次kfe变量以比较，未改数学运算/求和顺序。首次测试因全文件搜索同时选到顺序器的同名at_tax变量而失败；已将测试选取限定为真实后端at_tax方法，原表达式不改，失败日志保留。修正后14项通过；已通过的原生准备项未在无关测试修正后重复。

原生准备检查使用真实O2工厂/原Temp31NetWageInputs与B2附加观察，证明原request/inputs可进入准备对象，公开执行仍报SCOPED_CONSUMER_PERMISSION_NOT_GRANTED。它沿用B1/B2未用SciPy求解依赖的一触即停测试哨兵；实际SciPy/HA运行兼容仍未验证。最终原科学函数进入、外部命令/网络、SciPy哨兵调用均0；标准库模式无NumPy/SciPy导入。

补充只读安装元数据：Python3.11.9，NumPy2.4.6、SciPy1.17.1，记录Python可执行文件及两包METADATA/WHEEL身份。未导入数值包、未查询OS版本或启动命令，也未安装/修改环境。**安装元数据观察不是包二进制加载或HA运行资格**，完整私有路径及摘要回执LOCAL_ONLY。

主代理完成工程自审，不称独立科学审查。原有完成测试未整套重跑；闭合七入口probe文件名/字节/SHA保持，6份旧缓存保持/新增0，原全部科学源码和旧worker/监督器/pins不变。

## 准入差距与下一工程片

| 项目 | 当前状态 | 后续工程要求 |
| --- | --- | --- |
| 外部顺序/拒绝/AtTax原式与静态源码范围 | 本片15项工程检查通过 | 不扩大为实际HA见证 |
| 真实后端源码装载与实际类型/环境 | 尚未安装/验证 | 锁当前完整源码及运行依赖，核真实安装/导入，不用测试哨兵证明运行 |
| 具体科学输入与实际冻结网格字节 | 未选新输入、未绑定实际网格artifact | 形成可审阅的单来源或多来源有限输入方案；旧S03/旧初始化余额/七入口新工资不自动成为新HA授权 |
| Windows挂起创建/Job挂接/内存/超时/退出清理 | 本轮未测试或认证 | 复用底层既有保护，先做无模型工程检查；不得宣称当前仅数据层具备OS隔离 |
| 科学入口及native根/线性求解/内部计数 | 本片只核6个外部阶段 | 按完整被批准执行器与冻结控制登记，不借旧LIMITS或把phase计数冒充全调用预算 |
| 可执行消费许可与唯一worker准入 | 未实现、未授予 | 对具体新source/grid/input/资源与Owner决定/claim实现默认拒绝分支，再提出实际运行请求 |

既存temp31_worker_supervisor.py公开science路径固定旧AUTHORITY_PATH/SCIENCE_ROOT/FIXED_PLAN和S01—S03决定，不能给新执行器改名复用。其底层support位于src/ch5_two_asset_hank/multi_province而非validators目录；本轮只读确认此路由，未调用旧launch_worker、原保护测试或修改任何support pin。后续只在新具体范围内复用底层保护，不能绕过旧科学账本。

下一工程片聚焦上述真实后端装载/环境与无模型资源准入准备，不触发HA。待源码、输入、实际网格、所有调用与资源/退出保护具体且可审阅后，适用Owner新有限许可才执行；本轮不申请或发放运行额度，不自行设科学接受标准。

## 本地身份与保留边界

| 路径 | Git Blob | 物理字节 | 物理SHA256 |
| --- | --- | ---: | --- |
| src/ch5_two_asset_hank/multi_province/outer_ha_blackbox_executor.py | d504a9efe55310dba328647b15ad2fadac18b72d | 12669 | feeb9af2d199e3d4beabb9d03caab0216e30abeb820f98cde8a91a4eb9cd9efd |
| tests/test_outer_ha_blackbox_executor.py | b73d827f97064859f6529918d697ab4b92766451 | 14813 | 9e8972007a56cffa6150078142f2796e19a840eb46940a1fb70290617160b913 |
| validators/multi_province/outer_ha_blackbox_20261106/source_manifest.json | ebf6e21a54964587ec0547306a1a254cd3f42fb3 | 10521 | fad408406863feba037c9da0459bd2088e612be75fb358848c02caa20fbb82ef |

代码/测试/静态源码清单仅本地模型分支；GitHub只同步本报告与当前入口，API写入0，不推模型代码或LOCAL_ONLY载荷、不合并main。最终模型文档HEAD、治理提交与逐文件Blob/字节/SHA回读以私有交付回执为准。

TEMP31 7/7、Moll 3/3、七入口1/1及工资/补录全部按原关闭/零重试，旧初始化余量仅原8格，不跨借。strict reference/thresholds仍null；科学接受、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。A1/工资税/财政H聚合和原a*r_a决定不重开；实际p/来源单位、收入/劳动激励、Lt_prev、R/P及GE控制口径保持原未决。R12/R13/WASM、保护重绑定未授权、16项义务和历史dirty树/原件/缓存/LOCAL_ONLY保护保持；不reset/stash/clean、强推、删分支、移动证据或修改Desktop/CUA/全局配置。

前置：[B2保存观察与待许可绑定](CH5_B2_SAVED_WAGE_OBSERVATION_PENDING_BINDING_20261106.md)。当前：[路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)、[任务清单](../tasks/todo.md)。
