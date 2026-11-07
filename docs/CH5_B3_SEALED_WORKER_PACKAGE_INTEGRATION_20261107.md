# 封存worker、同源装载与占位协议离线组合

日期：2026-11-07。Owner接续：“可以，请继续推进”。工程验收：离线组合完成；真实科学worker/可信Owner许可/OS运行资格未建立。子代理0。

工程代码候选：`c71f580c479753568012915c8c4a51b936c1702e`。本轮仅新增`outer_worker_package`和对应检查，原45份来源未改。

## 完整组合结果

此前封存字节、来源装载、导入计数及根回报各自准备，本轮将其绑定到同一个原request/record、原counter与原输出target，形成一次离线组合调用。封存capsule的原字节/摘要、execution/source/record、worker模块路径及类名、完整消费者来源声明均须相符，不能换入等值对象或另一个bundle。

组合顺序为：明确的离线占位请求→替身端reserve_once及原字节回读→按已校验来源装载模块→从该模块取得worker类并构造→核对构造器和所有阶段方法来自捕获源码→即时/延迟导入及原六阶段/输出/root同counter完成。阶段驱动、原HJB→正式post→原KFE→原汇总/归一化、同inputs和原Cg格式均复用，没有改HA或加入内部hook，也不接受调用者随意传入一个backend实例替代声明类。

占位端仅是测试注入协议：请求标为OFFLINE，实际Owner决定、可信账本、grid和15实际预算全部null，回执强制runtime_admitted、scientific_acceptance和可信账本资格为FALSE。该接口不签发许可、不读取真实账本，也不把文件占位升级为Owner批准。公开执行入口仍直接拒绝。

替身共享存储按claim_id保留已用记录，先占位、再装载；换包/目录不能重用该存储中的同一claim_id。占位写入后回报失败、模块体/延迟导入/输出失败均不回滚占位、不自动重试，部分模块和文件保留。这只证明协议顺序和共享替身行为，不证明跨存储、跨进程、重启持久性、并发原子性或真实全局可信消费。

## 必要检查与保存

| 检查组 | 本轮通过数 |
| --- | ---: |
| 新封存包/装载/占位/root组合 | 17 |
| 原根回报/Cg组合回归 | 17 |
| 原导入counter关联回归 | 23 |
| 原显式来源bundle回归 | 29 |
| 原worker capsule回归 | 16 |

本轮17项新检查+85项相关回归，共102项。与历史97等片段存在回归重叠，不累计为全项目唯一总数。准备/公开门无装载副作用、错身份/源码/类方法/实例替换、即时和延迟导入、消费先后、失败保留、原C/g及根封闭等路径通过。复核新增了回读必须先确认bytes类型的失败检查并修复；删除该类型判断的变异被捕获，随后恢复已通过检查的原源码字节。失败日志与通过日志均保存。

新package装载执行的全部是本轮新建替身源码。真实NumPy仅用于合成C/g与既有容器接口；科学函数禁入、真实HA实例化拦截、外部动作禁入检查有效。真实HA后端实例、科学求解器、实际Win32/Job后端、科学worker、网格构建和新增科学额度均0。未重跑旧V2或任何关闭的观察；旧V2不认证当前候选。

集成里程碑一次性绑定46份来源/79条静态内部边（4条函数体延迟边，保守装载图无环）。新增`validators/multi_province/outer_worker_package_20261107/`中的source_manifest、package_interfaces、package_plan三份JSON；接口清单仅覆盖本轮新模块，不宣称全native覆盖。原45来源、上片3份机器记录、两份Owner adoption及原7个未跟踪文件，共57件启动基线原字节保持。源码与代码候选Blob一致，主代理工程自审不冒充独立科学审查。

## 已覆盖的声明面与剩余缺口

即时/延迟import、原六阶段、输出创建/写/读及root返回/校验/封闭已在一条替身组合链上使用同counter。完整源读取、数组复制、序列化/摘要的重复字节量，所有求解器/有效回报/native子调用及实际OS观察仍未覆盖，`complete_byte_accounting`和`live_counts_enforced`均FALSE；不以静态位置或替身采样补实际上限。

实际固定科学worker程序及启动/输入/grid工件、当前环境和实际模块/native绑定、可信Owner账本后端、受保护Job/process/时钟/限额/cleanup，以及实际同record根回报/Cg均未形成。本轮封存包和方法来源检查只在替身上成立，actual_worker_program/capsule仍null，actual_worker_package_qualified仍FALSE。

后续普通工程可准备实际worker启动/输入工件的静态装配合同及完整计数覆盖计划，保持公开运行门拒绝；需要真实工件生成或科学/保护动作的部分依适用Owner有限决定推进。真实p/单位/劳动激励、RP、外层经济停止、严格reference/thresholds和未来有限范围/15预算仍待Owner，不补默认、不重问已定Frisch/A1/税/H/Lt_prev/A第2轮输入。

actual grid hash/artifact、strict reference/thresholds和15实际预算仍null，NEW_RUN_BUDGET=0；全部运行/科学资格、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE及可信全局账本资格均FALSE。全部旧额度、STOP、16义务和历史dirty保护保持，不重绑、不换目录续额度。

本轮双树只同步本报告和三个当前入口；GitHub仅这四份脱敏文档。模型代码/测试/机器记录、原始载荷和完整私有路径不公开，main不合并，Desktop/CUA/全局配置未改。最终提交及逐文件Blob/字节/SHA256回读见本地交付回执。
