# CH5指定启动工件载荷的字节计数与同counter接线

日期：2026-11-07。普通工程完整交付，代码候选`5fc18aff950051e3fc074dfa6bdf411c78eb6955`。新增outer_artifact_byte_meter及检查，为原outer_dormant_launch_package的显式只读回查增加可选计数入口。HA、算法/网格/controls未改；子代理0，真实科学运行/新额度0。

## 已实现范围

复用原CounterIdentity和已尝试的声明worker counter，读取前先预留source_file_bytes_read，显式载荷SHA256前先预留serialization_and_digest_bytes。计数器、身份对象和配置必须保持原绑定；调用方须显式给出样本及全部合成限额。重复读取和摘要逐次计费，不以缓存或上次校验替代。

每次文件读取按读取前核对的文件大小预留容量，单次read最多请求该容量；核对祖先/reparse、打开身份与读取前后状态。成功、短读、打开/读取异常和读取后漂移均不退还已预留容量。日志分开保存请求字节、获准预留字节、可知的实际载荷字节数、操作返回和校验完成状态；预算拒绝的预留量为0，异常无法确定实际字节时记null，不写成0。该容量约束不是native调用次数或内存峰值证明。

启动回查可接入这个计数对象，且必须与启动包共用原CounterIdentity。所选范围是五份声明启动工件、指定Python可执行文件的载荷读取，以及该可执行文件载荷的SHA256输入。两次回查会产生12次读取及2次摘要计费。校验发现坏工件、既存attempt、路径或其他失败会停止该声明计数，保留已消费额度、原异常和现有文件；不重试、不修复、不重绑attempt。

同counter组合检查将计费回查接到已有worker内守卫、原六阶段替身、原格式合成C/g回读、root封闭及待准入请求；所选读取/摘要计费在root封闭后仍保留。没有创建或消费Owner账本、启动科学worker、调用真实OS/HA或生成网格。

## 明确没有覆盖的成本

该入口为可选工程接口，未启用时保留原只读行为并明确标记未计费。不是强制运行门，不建立live_counts_enforced。元数据身份核对/摘要、JSON/base64、其他loader/source/守卫的重复读取、数组复制/物化、求解器和native闭包仍不在本次覆盖中。complete_byte_accounting与全部科学/运行资格继续FALSE，不将局部计费称为全部开销已受控。

回查的物化字节核对只对当前所给工件成立；原root组合不把它升级为科学启动/来源/进程资格，其materialized_launch_verified仍FALSE。声明counter中的合成整数限额不是Owner许可；actual_limits的15项仍null，NEW_RUN_BUDGET=0。

## 检查与修复

| 本轮检查组 | 通过数 |
| --- | ---: |
| 新字节计数核心 | 11 |
| 新启动/root组合 | 6 |
| 原启动封装回归 | 16 |
| 原counter回归 | 31 |

17新+47相关回归，共64通过，不与历史片相加。覆盖重复费用、读/摘要预算前置、短读与未知字节保留、身份/配置/回调漂移、reparse/大小拒绝、原异常保留、同counter root回放及权限不提升。真实kernel入口在组合检查中禁入；既有科学函数/HA实例化/外部动作禁入检查有效，NumPy只作合成容器。

审查复现非法日志标签在失败快照中再次导致序列化错误，修复为写入日志前验证标签。将载荷动作移到预算预留前的变异被禁止先打开文件的检查捕获；源码按原字节恢复，错误与通过日志保留。复核不重复计入唯一测试数。工程自审不冒充独立科学审查。

当前机器包固定52源码/98静态内部边（4延迟、保守装载图无环），含source_manifest、startup_contract、meter_interfaces、binding_plan。原64件启动基线中63件保持现场原字节；唯一既有源码变更是外部启动回查的可选计数接线，其旧字节保留在Git及本地副本。其余50来源、前片机器记录、两份adoption和原7未跟踪项未改；旧清单/pin不反向重写或重绑。

## 仍需的实际工件与科学决定

实际原包未读取/解释，original_packet_semantic_mapping仍null。合格输入传输、科学worker/capsule/声明、冻结grid/参数/controls、可信有限Owner决定及消费账本、完整求解器/native/重复字节覆盖、实际OS/source/module/root/Cg证明仍缺。后续普通工程可继续完善外部元数据/守卫/复制路径的明确计数覆盖；不得以局部接口消除未观察缺口。

真实p/单位/劳动激励、RP、外层停止及严格科学标准待Owner，不补默认；已定输入、Frisch/无额外z/A1/税/H/Lt_prev不重问。actual grid hash/artifact、strict reference/thresholds及15实际预算仍null；全部运行/科学资格、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE、live_counts_enforced均FALSE，公开执行拒绝。

全部旧关闭额度/STOP/16义务、历史dirty/保护基线和七件未跟踪证据保持，不重试旧科学观察，不移动证据或修改Desktop/CUA/全局配置。源码/测试/机器记录仅本地，GitHub只同步本报告和三个CURRENT，main不合并。最终保存与逐文件Blob/字节/SHA256回读以本地交付回执为准。
