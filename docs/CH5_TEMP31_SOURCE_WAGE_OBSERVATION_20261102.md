# TEMP31 单次源工资函数观测 · 2026-11-02

STATUS=COMPLETED_SINGLE_SOURCE_CALL_ON_FIXED_SYNTHETIC_INPUTS__NOT_PRODUCTION_OR_SCIENTIFIC_ACCEPTANCE
OWNER_EXACT_STATEMENT=可以我同意，请继续
AUTHORITY=APPROVE_PREVIOUS_FIXED_SYNTHETIC_SINGLE_WAGE_FUNCTION_OBSERVATION_PROPOSAL
GOVERNANCE_AUTHORIZATION_PARENT=6345dbcdbf475076f321cd7745cea38140ff3f45
SOURCE_WORKSPACE_HEAD_AT_EXECUTION=9bb924a3d717bfd8220c7e94a238117458d3d41f
CODE_CANDIDATE=dc87980d5377309f9b18c1928173488ba1050415__UNCHANGED_LOCAL_ONLY
SOURCE_FUNCTION=composite_household_wages
SOURCE_PATH=src/ch5_two_asset_hank/multi_province/wage.py
SOURCE_BLOB=48001b2e4ca64d81dda6174255f6ccf130e07004
SOURCE_BYTES=3004
SOURCE_SHA256=12393521821b5a7616eec8f19bcd4a10cbb2da37e0a87fcb5c5b4128a0c98dbe

Owner本次明确批准上一轮具体提案：最多3个新进程、每个≤30秒，累计实际源工资函数进入最多1次；仅进入前工程错误可在余量内修复，进入后无论结果均不重跑。初始化/root/HA/HJB/KFE/GE/IRF/policy/MATLAB及真实数据调用全部0。本次不是原8格初始化预算的续用，也不复活任何旧科学预算。

## 实际执行与计数

| 项目 | 现场结果 |
|---|---|
| 新worker | 1个，退出码0，父进程墙钟1.157秒，未超时 |
| 源工资函数 | Python frame进入1、允许主体执行1、实际返回1 |
| 重试 | 0；不存在第2或第3个worker |
| 其他原科学函数 | 拦截尝试0，主体进入0 |
| 初始化/root/HA/HJB/KFE/GE/IRF/policy/MATLAB | 全部0 |
| 导入范围 | 标准库工程接口+按精确文件加载的源wage.py及NumPy2.4.6；SciPy/完整原科学包/旧loader未导入 |
| 运行环境 | Python3.11.9；载入NumPy版本和解释器根身份核对通过，未安装升级依赖 |

父进程执行30秒超时门并回收worker；源函数进入前创建独占、flush/fsync的PRODUCER_ENTRY_CLAIM，随后才允许函数主体执行。该记录存在即禁止本授权的任何后续worker。虽然上限为3个进程，实际源函数额度1/1已消耗，余下两个启动槽不可用于再算一次。本轮没有发生保护/域/权限异常，没有修输入、公式、容差或source pin后重跑。

## 固定输入及观测输出

封存输入仍1230 bytes，SHA-256=98471bf5b9f3594b8051c5e25247aa95ab1e583a8fa769c58b127ee6dcded79f，原提案文件保留。A/B合成标签、目的地tau=[.05,.05]、phi全1、sigma全0、phi_l5、alphal1保持；两地企业工资表达式19/(.95*2^(5/6))只在本次获准worker内求值。没有向该工资函数传入ra/rb或HA网格，也没有调用企业/外层来生成这些工资。

实际返回为(19.000000000000004,19.000000000000004)，相对数值19的有符号差均为3.552713678800501e-15。该差仅作浮点诊断，没有新增科学接受容差。两元素均有限且非负，符合该函数自身返回约束；不能据此认证真实工资水平、稳态、非对称税配置或31省端到端单税修正。生成1/进入2仍为反事实见证标签，不是真实企业或外层期次。

## 执行见证与字节交接

现场在实际函数frame记录绑定参数，核对其规范字节等于封存调用参数；在实际return事件记录返回值及类型，并核对程序收到的值一致。前置九角色源字节预检通过，进入前再次核对工资源文件/函数globals与物理路径；载入函数co_filename对应同一原文件，不是用模拟callback冒充原函数。

源函数返回转为规范字节后，SHA-256=2900a554e1c52b4ffc9cb27a820046750ae902e79458b52d7892fd1ae54f23b3。六类输入封存来自实际进入frame的参数及明确的隔离合成快照，输出封存来自实际return；逐项交接与pending接口的输出身份一致，payload匹配通过。原始参数、日志、执行器、完整见证及输出字节均LOCAL_ONLY，公开只报聚合诊断/计数/哈希。

外部执行见证已证明“该固定源函数在该合成输入上进入并返回过一次”；现有PendingWageEnvelope的producer_invocation_verified和consumer_ready仍为FALSE，科学消费者仍以PRODUCER_INVOCATION_NOT_VERIFIED拒绝。两者不矛盾：外部观测尚未转换/采纳为消费者可接的类型化资格，不能自动升级为实际生产来源、实证工资或科学接受。本轮未修改该接口标志、旧科学校验器或SOURCE_COMMIT，也未放行消费者。

## 停止点、保护与下一工程工作

单次观测目标已完成，停止追加科学进程。停后九个源文件的字节/Blob/SHA-256及固定输入保持，科学源码、参数、价格和HA grid更改0；原初始化账本仍3/10已用、余7，与本次授权分开。

下一步只使用已保存进入/返回见证做类型化接口对接和拒绝路径检查，保留合成观测作用域，不再调用工资函数、不修改科学消费者、不放行HA。真实生产工资凭据、真实31省输入、HA组合、严格驻定/GE/IRF/福利和Results仍须对应门；本次观测不解除任何既有科学或保护STOP。

ENGINEERING_VERDICT=PASS_BOUNDED_OBSERVED_SOURCE_INVOCATION_AND_INPUT_OUTPUT_IDENTITY_CHAIN
OBSERVATION_WORKER_BUDGET=1_OF_3_USED__SOURCE_ENTRY_1_OF_1_CONSUMED__CLOSED_AFTER_ENTRY
SCIENTIFIC_CONSUMER_RELEASE=FALSE
INDEPENDENT_SCIENTIFIC_REVIEW=NOT_ESTABLISHED
OWNER_SCIENTIFIC_ACCEPTANCE_OF_PRODUCTION=NOT_GRANTED
FORMAL_SOURCE_FREEZE=FALSE
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE

旧dirty工作树/HEAD/index、历史原件/缓存/证据、V010、WASM/R12 STOP、R13未授权、保护重绑定未授权、16项义务和所有旧耗额保持。没有分支删除、main合并、原件移动或全局配置修改。

后续2026-11-02已完成[保存见证的类型化工程对接](CH5_TEMP31_SAVED_WAGE_WITNESS_IMPLEMENTATION_20261102.md)：只读取本次固定封存记录，未调用生产者，原观测及预算保持。所得回执仅声明保存记录一致，不声明新的现场执行或生产资格，科学消费者仍关闭。
