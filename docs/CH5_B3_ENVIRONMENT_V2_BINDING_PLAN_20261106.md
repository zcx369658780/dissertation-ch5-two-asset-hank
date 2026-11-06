# B3独立环境V2：源码与合同绑定完成，执行决定未登记

DATE=2026-11-06
OWNER_CONTINUATION=请继续
STATUS=ENVIRONMENT_ONLY_V2_BINDING_COMPLETE__14_OFFLINE_CHECKS_PASS__NOT_RUN
MODEL_ENGINEERING_CANDIDATE=aa3fdc2574901d4aca33dc0c299f4db784741bf3
MODEL_ENGINEERING_TREE=8327f85612d32c3ebe0299952f22e997bc7c5f8d
MODEL_PARENT=0a746768c2f909db8b1a4b15e81c63405dba76b8
GOVERNANCE_PARENT=5dc067273e088bb5864f84fe77bdb6c589d8b948
EXECUTION_DECISION=NOT_ISSUED
ACTUAL_OUTPUT_DIRECTORY=NOT_CREATED
REAL_WORKERS=0
NUMPY_SCIPY_IMPORTS=0
PROJECT_SCIENTIFIC_CALLS=0
NEW_SCIENTIFIC_GRANTS=0
SUBAGENTS=0

## 本轮交付

上一片未应用补丁已落实到两个独立V2文件，并配套独立固定合同及测试，共四条新增路径。旧四份执行文件/合同/测试及三份修复草稿保持原字节，不在旧路径应用补丁。V2只支持environment_case；正常返回、超时、超额内存三个旧用例和任意science模式均不能进入合同读取。V2存在于本地模型分支，不是已运行或已接受状态。

合同绑定当前V2监督器、固定worker、原Windows Job支持、原只读安装元数据模块和24源码清单共5份基础文件，再回读原24份定义源码的长度/SHA；34条原相对import边及HA源码不改。安装元数据仍为Python3.11.9、NumPy2.4.6、SciPy1.17.1，读取了命名元数据/运行文件子集，未导入数值包，不认证动态或native依赖完整闭包。

V2保留上一片修复：向新子进程的Unicode环境块预置三个线程项为1及OPENBLAS_MAIN_FREE=1，并由子端回读证明；不修改父/全局环境或依赖包。停止结果不读取成功专属字段，原错误可传到父回执。worker的install_audit与DefinitionLoader和补丁候选AST一致，原网络/写入/进程/环境写拒绝与零项目函数体保护保持。未构造HA参数、网格或后端，未调用HJB/KFE/初始化/原汇总。

## 独立执行决定与单次消费

V2公开入口先读取固定合同并核全部pin，再核固定位置的独立execution_decision.json。该文件本轮**未创建**。缺失决定、错误状态、contract SHA/目标目录/限额不一致、额外字段或布尔冒充次数均拒绝；调用方不能用一个ready布尔值放行。当前默认拒绝已在实际入口的离线检查中确认：输出创建函数和支持装载函数均未进入，没有真实claim、Job或worker。

未来决定须绑定同一合同SHA、scope、固定environment_case、固定输出根与下表限额，并明确零科学调用。父端把决定原字节SHA写入独占claim；固定worker在依赖导入之前重新核决定，并要求同一SHA、同一合同及真实父PID/Job证明。它是无模型工程执行决定，不授予HA/科学运行或接受权。

新V2拟定输出定位符为LOCAL_ONLY_CH5_B3_ENVIRONMENT_V2_20261106/environment_case，完整私有根绑定在本地合同中。本轮没有创建该目录。使用独立定位符本身不授予重试：只有明确的前瞻决定成立后才可消费这一具体V2；不能沿旧闭合合同、修改旧claim、借旧额度或用目录改名续跑。

决定成立后，V2先独占创建case与claim，再进入环境核对、Job设置和启动。环境设置失败也保存最终回执、登记已消费1次，即使实际进程0也不能沿同一case再次尝试；claim/目录既存则直接拒绝。设置、执行、超时或清理失败均没有自动重试。原挂起创建→实际Job限制回读→恢复前挂接→子端证明→退出及清理链保留。

## 唯一下一步：拟议单次无模型环境验证

以下是已经具体化的未来方案，**不是本轮发放或消费的额度**：

| 项目 | 固定范围 |
| --- | --- |
| 目标 | 验证V2子环境、真实NumPy/SciPy导入、固定24源码定义装载及退出回报 |
| worker/尝试 | 仅1个Python worker，1次，无自动重试；失败保留后停止 |
| 墙钟 | 30秒，计入claim后的环境设置/启动；终止及清理单列记录 |
| 内存/进程 | 每进程提交内存上限2GiB，Job活跃进程上限2；不是整个Job总内存上限或单进程HA资格 |
| 可选辅助查询 | 如依赖需要，至多1次固定系统cmd.exe的只读ver查询；另一个进程名额仅用于它 |
| 输入 | 固定合同、安装元数据/命名运行文件pin、24源码原字节；无经济输入、网格或科学返回 |
| 科学范围 | 项目函数体进入0；HA/HJB/KFE/初始化/原外层组件/GE/MATLAB/求解器调用0 |
| 退出条件 | 元数据或源码漂移、决定/claim/Job证明不符、未列入清单的项目import、受禁止的审计事件、项目函数进入、超时、内存/进程拒绝、结果或清理不符，均停止且不补跑 |
| 结果资格 | 只接受该环境检查的工程证据；不赋予HA运行、科学接受、Results或激活资格 |

下一行动是在适用授权内明确前瞻登记上述独立决定，随后仅执行该一项。原三个资源通过用例不复跑。任何未来科学运行仍须适用Owner具体有限决定；本方案不选经济参数、实际网格、价格或科学接受阈值。

## 14项离线检查与限制

14项全部通过：实际合同/5基础pin/24源码回读；公开入口在决定缺失时、创建输出或支持装载前拒绝；旧模式/旧合同/扩大限额拒绝；固定决定精确schema、目标、SHA和次数类型；原审计/定义保护AST与环境单模式；mock成功、设置失败也消费claim、停止原错误、超时清理、子证明/成功字段反例、挂接失败终止及清理未确认拒绝。

mock的完整成功字段和Job回读由替身提供，只证明接线与拒绝逻辑。真实环境仍未导入，24份定义仍未实际装载。初次离线生成因元数据块缩进错误，在新源码写入之前编译停止；修正生成器后再完整编译并独占写入两个新文件，错误和派生记录LOCAL_ONLY保留。它不是一次真实worker失败或额度消费。代码图谱未覆盖新模块，按已列明精确路径读取；未重建或扩大索引。主代理工程自审，不称独立科学审查。

## 本地身份与保留

| 新路径 | Git Blob | 字节 | SHA256 |
| --- | --- | ---: | --- |
| src/ch5_two_asset_hank/multi_province/outer_environment_supervisor_v2.py | 2f41dd190788fa3da3880cd2bdd2926dd348d6b2 | 17620 | 3cbcb1f34805a4ea689aac1f9b45fb20f41f89d8f1fb318eed914d1e4bffca1c |
| validators/multi_province/outer_environment_worker_v2_20261106.py | ad2a1364e2992ddf685775ac124b64dfc9ad0f76 | 13077 | 8d82f13e30bb16327d7234af64327ee8be968964a3b13a56d7e0e1652af12b85 |
| validators/multi_province/outer_environment_v2_20261106/contract.json | 1bddb42d47d0fbc76e6465d15cab086e19b11519 | 4571 | 5f310241781c853fc45d40b4f2a616baed7c9e5bc820f24795754683d642f204 |
| tests/test_outer_environment_v2.py | af1e0a5cb3eca0a4397321d9ddacfde1cc27d919 | 10678 | 744ae6d7016e49e0e8de742f22ba8dab7b4435a984505130ca24d5dbce49cbbb |

旧执行/修复7份文件、四检查20份回执、上一片14份准备证据、原24份源码及六缓存长度/SHA保持，新缓存0。代码/测试/合同及完整安装/输出路径只在本地；GitHub仅脱敏治理文档，API写入0，不推模型代码或LOCAL_ONLY载荷，不合并main。

TEMP31 7/7、Moll 3/3、七入口1/1、工资/补录及旧四项检查均保持关闭、零重试；初始化余额仅原8格、不跨借。strict reference/thresholds为null，科学接受、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。HA整体黑箱及原算法/网格/controls冻结，A1/工资税/财政H/a*r_a决定不重开。R12 STOP、R13未授权、WASM六路径STOP、保护重绑定未授权及16项义务保持；历史dirty树、原件/缓存/证据不移动或清理，无reset/stash/clean、强推、删分支或全局配置修改。

前置：[未应用修复准备](CH5_B3_CHILD_ENVIRONMENT_STOP_REPAIR_PREPARATION_20261106.md)。当前：[路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)、[任务清单](../tasks/todo.md)。
