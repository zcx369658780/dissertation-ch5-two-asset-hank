# 同record根回报、原始C/g与准入接口集成准备

日期：2026-11-07。工程验收：离线集成准备完成；真实执行与科学接受未就绪。子代理0。

代码候选：`84778bf74b09dae29292cd38796259e0aeba14a0`；序列化提取提交：`cafb8a7`。模型代码、测试及机器记录仅本地保存。

## 完成的集成成果

新增外部`outer_worker_return_binding`，将原六阶段接线、同一个counter的原root ticket、原request/inputs/wage record和原输出target绑定。准备阶段不调用backend、不产生counter事件或输出文件；公开执行入口仍直接拒绝。

离线私有接线复用既有六阶段驱动，不复制HA算法。原initializer→HJB→正式post→原KFE→原汇总/归一化→AtTax→reply顺序和同inputs不变。六阶段返回后，复用原胶囊格式编码原始C、原g、原cell_weight；排他创建文件、写入并按固定摘要回读，检查同request和快照摘要后，才登记root正常返回、声明校验和封闭回放。各次输出创建/写/读在同counter中预登记；原始数组的shape、dtype、字节和权重经过往返核对，不重归一化、不回退Ct、不增加z或重复税。

仅从旧输出模块提取无文件副作用的`encode_bound_origin_output`。原编码段与原写入/读取段分别经AST等价核对，原胶囊格式及旧save接口保持。原44份来源中另外43份字节未变，冻结HA/网格/controls、逐格Frisch/A1、工资税与财政H口径未变。

提供绑定声明身份和完成状态的准入请求接口：导出已声明的execution/source/binding/worker/output/grid身份及离线回执摘要，集中列出缺件。实际工件、实际许可、严格标准和全部15类实际预算均不由合成声明填充。该接口不接收/签发Owner许可，不启动worker，也不是可信全局消费账本。

阶段异常、错record/target、无C/g、错快照、输出碰撞、短写、回读失败、资源/采样失败均停止当前集成，不重试；已有或部分文件保留。根的物理返回标记、counter正常返回、声明校验和科学有效回报分别记录。复核发现封闭回放后的counter配置漂移还需拦截，已先以失败检查复现，再修复seed/限额/容量核对。

## 必要离线检查与证据范围

| 检查组 | 本轮通过数 |
| --- | ---: |
| 新根回报/输出/准入集成 | 17 |
| 原同record输出胶囊回归 | 21 |
| 原C/g快照完整单文件检查 | 13 |
| 原六阶段接线回归 | 15 |
| 原counter回放回归 | 31 |

本轮五组共97项；80项为相关回归。此数不与历史片段相加为全项目唯一总数。初始缺模块失败、counter漂移失败和修复后的通过日志均留存；另一次短写条件变异被检查捕获，随后源码恢复到已通过检查的原字节。

真实NumPy仅用于合成数组和既有容器接口。原有科学函数禁入检查、真实HA backend实例化拦截及外部动作禁入检查有效；科学求解器调用、真实OS后端调用、科学worker、网格构建和新科学预算均0。不把这次数据接口检查说成无数值库导入，也不把旧V2环境证据迁移到当前候选。未运行包含科学/保护动作的全仓库测试集。

集成里程碑一次性绑定45份来源、76条静态内部导入边（4条函数体延迟边）。新目录`validators/multi_province/outer_worker_return_binding_20261107/`仅保存source_manifest、integration_interfaces和integration_plan三份JSON；不逐helper复制旧11份大清单。新接口清单只覆盖本轮两个外部文件，不宣称完整native闭包。第二次文件/Blob/摘要回读通过；主代理工程自审不冒充独立科学审查。

启动62件保护核对中，唯一允许变动为上述外部序列化提取；其余61件原字节保持，包括43份旧来源、11份上片机器记录和原7个未跟踪文件。两份Owner adoption记录也与启动提交Blob一致。历史dirty树、关闭额度、STOP与16义务未变、未重绑。

## 剩余真实工件与许可缺口

| 缺口 | 本轮边界 |
| --- | --- |
| 实际冻结网格artifact/hash | 仍null；未生成网格，合成身份不替代实际身份 |
| 固定worker包及source/module/import/capsule绑定 | 外部组合已有离线准备；当前实际worker程序、启动包和运行时同源证明仍缺 |
| 可信Owner准入与持久消费 | 请求接口已有；全局可信账本、有限决定、实际消费证明仍缺，占位不是许可 |
| 原生/有效回报与全部资源计数 | 本轮只登记声明阶段与输出创建/写/读；序列化/摘要、源读取、复制、求解器及native重复调用的完整覆盖未完成 |
| 实际OS保护与生命周期 | 当前Job/process身份、计时起点、限额执行和cleanup证明未取得；未调用真实Win32后端 |
| 实际同record根回报/C/g | 只有合成数据往返与声明root封闭，实际科学输出未取得；单A不等于完整A/B批次 |
| 科学输入与接受决定 | 真实p/单位/劳动激励、RP、外层经济停止、strict reference/thresholds及未来有限范围/15预算仍待Owner；不补默认 |

本轮目标已完整交付，无需为内部helper再请求继续。后续独立工程重点是固定worker包/同源装载、可信许可消费接口和完整计数的离线组合；依赖实际网格、真实保护运行或科学取值的部分继续关闭，不把工程目标或预算骨架当运行许可。

`runtime_admitted`、`actual_worker_root_verified`、`actual_OS_backend_qualified`、`actual_trusted_global_claim_ledger_qualified`、`live_counts_enforced`及全部scientific_acceptance、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE；actual grid、strict标准和15实际预算仍null，NEW_RUN_BUDGET=0。全部旧额度保持关闭，零科学重试。

双树仅同步本报告和三个当前入口，GitHub仅发布这四份脱敏文档。模型源码/测试/机器记录、原始数据、完整私有路径和LOCAL_ONLY载荷不公开；不强推、不合main、不修改Desktop/CUA/全局配置。最终提交和逐文件回读以本地交付回执为准。
