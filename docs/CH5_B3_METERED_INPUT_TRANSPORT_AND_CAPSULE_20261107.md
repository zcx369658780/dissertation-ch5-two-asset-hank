# CH5输入传输与worker capsule的可选同counter计数

保存与发布：本地两树已保存本轮工程。前次网络失败记录保留，本次恢复仅按四份脱敏文档生成治理分支API快照；最终以Blob、实际字节与SHA256回读回执为准。模型代码、测试和机器记录只在本地，main不合并。

日期：2026-11-07。代码候选`e93d69d2c047c389818d05ba7c0fc4a93db95bda`。本轮完成输入传输、capsule编解码的可选字节计数，接入休眠入口准备/反序列化和已有启动回查，并离线组合到同一原counter的root及原C/g输出。四份外部源码改变，HA/HJB/KFE/原汇总、算法/网格/controls及既定经济合同保持。子代理0，真实OS/HA/科学worker/实际网格/新额度0。

## 实现和保留合同

输入传输接口保留原startup拥有者的严格JSON解析器，包括重复键、非有限数、对象及2MiB限制；未换成宽松解析。路由JSON输出容量/解析输入、显式摘要、Base64/ASCII、工资/劳动权重的显式buffer复制及回读检查，每次往返重新计费。标量仍float.hex，原包只做不透明字节和摘要保留，不解释实际原包、不重算工资或税。原dtype/shape/只读及worker内request/context/record对象关系保持。

Base64在实际解码前核容量、预留array_bytes_copied；数组按声明f4/f8预期长度核对，错误长度先拒绝。通用组件仍受原大小上限限制。可选计数要求精确ArtifactByteMeter和相同context/origin/execution/binding/source-plan/grid元数据；外来身份在输入对象重建前拒绝。source-plan摘要核对需要先解码该声明字节，不声称所有外包都在任何Base64前拒绝。合法原编码字节不变；计数路径另要求可计算的Base64容量。

capsule保留原字段、重复键、外部/内部摘要、filename/argv和大小合同，canonical尾换行保持。编码前及解码source前核同execution/source/record身份，context检查要求原identity对象。BOOTSTRAP_SOURCE literal原字节保持，持久attempt预留、写入和inline loader未改，不用这些原语取得新运行资格。

入口prepare和私有rehydrate可转接同一meter。启动回查保持原六次载荷读取及executable摘要在前，随后对已核对的transport/capsule字节执行计数编解码检查，不创建counter、identity、attempt、预算或科学worker。公开main/execute仍拒绝，默认未接入路径保持；默认传输/capsule保存字节经旧实现严格对照。计数回查新增标记只在显式计数时返回。

JSON仍先预留保守ASCII表示容量，再渲染和记录实际长度；表示容量不是实际消耗或内存峰值。预算不足/坏载荷停止后保留已预留容量和已有工件，不退款、不重试。旧“两次回查只有两次digest”的断言已改为精确核两次python_executable摘要，再按全部操作账本严格核总字节与返回次数，新增codec成本没有隐藏或置零。

## 必要检查与工程验收

| 本轮检查组 | 通过入口数 |
| --- | ---: |
| 新capsule离线检查 | 7 |
| 新transport/entry/同counter root-Cg组合 | 10 |
| 原计数核心回归 | 11 |
| 原启动计数组合回归 | 6 |
| 原worker入口回归 | 16 |
| 原启动包回归 | 16 |
| 原capsule替身回归 | 16 |

17新+65相关回归共82个测试入口通过；组合复用既有fixture/检查，不宣称82份唯一独立证据，不跨历史相加。旧capsule回归仅执行toy bootstrap/fake kernel，不是科学worker或真实Win32/Job。NumPy仅合成容器，科学函数/SciPy sentinel/外部动作禁入检查保持。

固定本轮启动前的transport/capsule源码为格式参考，对照canonical字节、尾换行、metadata、摘要、原包、浮点位模式、大小端f4/f8、只读与worker内同对象关系。并检查重复计费、预算动作前拒绝、外来身份/重复键/非有限值拒绝和同原counter的preflight→root→原C/g输出。跨decode的新plan不与父侧旧plan硬拼对象身份；离线组合不证明真实跨进程输入/模块绑定。

绕过capsule解码计数的行为变异被预算拒绝测试捕获，源码逐字节恢复，核心7项再通过。首两次集成启动因缺测试目录环境变量、以及入口过早移除integration标记导致禁入模式错误而停止；仅修复离线测试调用/标记，日志保留，未调用科学函数或重开旧额度。

当前机器包`validators/multi_province/outer_metered_transport_capsule_20261107/`含source_manifest、startup_contract、codec_interfaces、binding_plan四份JSON，绑定52来源/102静态内部边（4延迟，保守装载图无环）。重新解析全部来源以更新行号；这不是实际调用次数或native闭包。合成fixture累计十份明确固定SHA差异，旧清单/reference/pin不反写。

65件启动基线中61件保持现场原字节，四份外部源码旧字节存Git和本地副本；其余48来源、前片四份机器记录、两份adoption及原7未跟踪项保持。主代理工程自审，不称独立科学审查。源码、测试和机器记录只本地保存；仅本报告及三个CURRENT同步治理线，main不合并。最终Blob、实际字节和SHA256回读见本地交付回执。

## 未覆盖、实际工件与许可缺口

本轮只扩展可选显式路由。startup合同本身的JSON/Base64、source-plan投影、工厂/工资证据协调与身份/网格计算、初次source/state守卫、未接入的复制（含JSON尾换行拼接）、独立save/load I/O、规划/验证/记账及native/求解器仍未完整计数。已有守卫端口可另行接入，不能追溯把准备成本算作已覆盖；complete_byte_accounting及live_counts_enforced仍FALSE。

实际原包未读取或解释，original_packet_semantic_mapping=null。实际合格传输、科学worker/capsule/声明采纳、冻结grid/参数/controls工件、当前依赖/模块及真实OS/source/root/Cg证明仍缺；实际工件槽位均null。可信有限Owner决定和全局消费账本仍缺，持久占位不是许可。actual grid hash/artifact、strict reference/thresholds和15实际预算仍null，NEW_RUN_BUDGET=0。

真实p/单位/劳动激励、RP、外层经济停止和严格科学接受标准仍待Owner，不补默认。Frisch/偏好、无额外z、原C/g/权重、A1、净工资/目的地税一次/财政同源H、Lt_prev及已采纳A第2轮输入不重问。原黑箱、a*r_a、同inputs和正式post→原KFE→原归一化保持。

全部运行/科学资格、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE及live_counts_enforced保持FALSE，公开门拒绝。旧关闭额度、STOP、16义务、历史dirty和保护基线保持；不改Desktop/CUA/全局配置，不移动缓存或重绑资产。后续独立工程可整理并接入剩余startup/身份准备成本；实际原包语义适配需已开放来源，真实科学/保护动作另需适用决定。
