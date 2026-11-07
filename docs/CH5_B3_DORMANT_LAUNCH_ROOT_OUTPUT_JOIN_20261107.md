# CH5休眠启动包与同record根回报/Cg输出集成

日期：2026-11-07。Owner继续后，本轮完整工程包完成实现、必要离线检查/修复、主代理工程自审和保存；真实OS/科学运行/新额度0，子代理0。

代码候选：`009f0daa1b72a0a55fcab52423a8c3d40ceb1bc8`。新增outer_dormant_launch_return和对应检查，原50份来源原字节不变。原启动封装、反序列化、外部保护、六阶段和原格式输出实现均复用，不修改HA黑箱。

## 完整集成结果

将既有PreparedDormantLaunchPackage、worker内RehydratedWorkerEntry和WorkerReturnBinding接合。启动包的entry必须就是worker内守卫保留的声明，输出target.plan必须就是还原得到的plan，root phase的request和CounterIdentity必须就是原对象；等字节的另一份启动包/身份对象不能代替。原root合同继续核对execution、source、binding、grid及输出目标摘要。

输出必须在启动包指定根内，且与入口/startup/传输/capsule/声明及attempt路径分离；本轮专门构造满足各原接口的碰撞/越界目标，验证接合层拒绝。准备只绑定已有对象，不推进counter、不消费attempt、不生成工件。公开执行在守卫文件读取、阶段分派、文件创建和后端动作前无条件拒绝。

私有离线组合只用显式注入的不透明替身，复用原六阶段→原格式合成C/g写入/回读→原root封闭与准入请求。样本回调前后均核对启动包、来源/布局守卫及同record合同，回调中替换capsule也会阻止后续阶段。成功输出保持C、g的dtype/shape/原字节和原cell_weight，绑定同一request；root只有在原输出回读后才按原合同记录返回。未从Ct倒推或重新归一化。

同一counter只接合一次，组合只回放一次。阶段/保护/路径/预算替身/写入/回读失败后保留原日志和现有/部分输出，关闭该声明回放，不回滚、不重试、不重绑。停止回执使用准备时固定的声明和counter身份摘要，避免损坏的现场字段使失败回执本身丢失。

该组合不调用native准备/执行，不验证已物化启动文件，不创建或消费Owner账本，不装载真实科学worker；materialized_launch_verified为FALSE。逐阶段事件和本进程替身对象不构成实际进程返回、完整native计数或连续OS保护。局部一次性约束不能替代跨进程/全局可信账本，更不是Owner运行许可。

## 检查、修复和保存范围

| 本轮检查组 | 通过数 |
| --- | ---: |
| 新启动包/root/Cg接合 | 15 |
| 启动封装相关回归 | 16 |
| 原root/输出相关回归 | 17 |

本轮15新+33回归共48通过，不与历史片相加。覆盖原身份对象、等字节外包/声明替换、目标摘要错配、输出/attempt碰撞与越界、原C/g/权重往返、公开门先拒绝、源漂移、样本内变更、原六阶段失败、外来snapshot、部分写入/回读失败保留及失败不重放。合成预算0写入上限在写字节前停止，不作为实际预算。

首轮14新检查通过后，新增复现身份字段非法导致停止回执失败的问题，修复为使用准备时固定摘要；最终15项通过。变异检查删除同一CounterIdentity对象要求后，被等字节外包测试捕获，源码原字节恢复。定点复核不重复计入唯一测试数。主代理工程自审不冒充独立科学审查。

新机器包固定51源码/95静态内部边（4延迟、保守装载图无环），保留完整来源和两份adoption原字节，含source_manifest、startup_contract、join_interfaces及binding_plan四份JSON。接口清单仅覆盖新接合模块，不宣称完整求解器/native/重复字节覆盖。原50来源、前片4机器记录、2份adoption和原7未跟踪项共63件启动基线原字节保持。

NumPy只用于已封存合成请求和小型布局/Cg容器。既有科学函数、HA实例化与外部动作禁入检查有效；实际原包读取/解释、真实OS/HA/科学worker、实际网格构造和新额度均0。没有重开旧运行/环境资格、保护基线或已关闭额度。

## 实际缺口和边界

当前给定请求的启动→worker内原对象→输出/root→待准入请求离线链路已接合。实际原候选packet仍未读取或解释，original_packet_semantic_mapping仍null；实际输入传输、科学worker/capsule/声明资格、冻结grid/参数/controls、可信有限Owner决定与消费账本、完整求解器/native/重复字节计数、实际OS/source/module/root/Cg证明仍缺。

后续工程重点为已开放字段来源支持下的实际原包语义适配、完整计数覆盖及保护资格准备；实际工件获取/科学动作必须有适用授权。真实p/单位/劳动激励、RP、外层经济停止及严格科学标准待Owner，不补默认、不重问已定Frisch/输入/A1/税/H/Lt_prev。

actual grid hash/artifact、strict reference/thresholds及15实际预算仍null，NEW_RUN_BUDGET=0；实际工件槽位未填。scientific_acceptance、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE及live_counts_enforced均FALSE，公开执行拒绝。HA算法/网格/controls、a*r_a、净工资、同inputs、正式post→原KFE→原归一化及所有STOP/16义务保持。

模型代码/测试/机器记录仅本地；两树/GitHub仅同步本报告和三个CURRENT。main不合并，保护资产/缓存证据不移动，不改Desktop/CUA/全局配置。最终提交及逐文件Blob/实际字节/SHA256回读见本地交付回执。
